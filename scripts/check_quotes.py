#!/usr/bin/env python3
"""check_quotes.py - verifica que `trecho_literal_fr` de cada regra aparece
literalmente no texto consolidado ATUAL (frances) da lei no Fedlex.

Uso:
    python scripts/check_quotes.py                      # rede (Fedlex)
    python scripts/check_quotes.py --offline DIR        # DIR/<rs>.html
    python scripts/check_quotes.py --rules-dir X --report Y.json

Exit code: 0 = tudo OK; 1 = alguma FALHA ou lei nao obtida.
Dependencias: Python 3.11, stdlib + PyYAML.

Resolucao RS -> HTML (funcao `resolve_law_urls`, isolada de proposito):
  1. scripts/fedlex_sources.yaml (opcional; mapa `rs: url`) tem prioridade.
  2. Descobrir o ELI: do `fonte.url` da regra (se contem /eli/cc/...) ou via
     SPARQL pelo numero RS (QUERY_ELI_BY_RS).
  3. Via SPARQL, listar as expressoes francesas desse ELI (QUERY_FR_EXPRESSIONS),
     escolher a de data mais recente <= hoje e usar o arquivo HTML associado;
     se a query nao trouxer arquivo, derivar a URL do filestore pelo padrao
     https://fedlex.admin.ch/filestore/fedlex.data.admin.ch/<eli>/<AAAAMMDD>/fr/html/
     fedlex-data-admin-ch-<eli com - no lugar de / e .>-<AAAAMMDD>-fr-html-1.html
NOTA: query e padrao de URL NAO foram testados contra a rede real (ver README
da tarefa); sao a parte mais provavel de precisar de ajuste.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SPARQL_ENDPOINT = "https://fedlex.data.admin.ch/sparqlendpoint"
ELI_PREFIX = "https://fedlex.data.admin.ch/eli/cc/"
USER_AGENT = "drive-theory-check-quotes/1.0 (+github actions; legal quote verification)"

PREFIXES = """\
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""

# RS -> ELI do ato. A notacao RS fica numa entrada de taxonomia
# (classificacao sistematica) ligada ao ato por jolux:classifiedByTaxonomyEntry.
QUERY_ELI_BY_RS = PREFIXES + """\
SELECT DISTINCT ?act WHERE {
  ?act a jolux:Act ;
       jolux:classifiedByTaxonomyEntry ?tax .
  ?tax skos:notation ?n .
  FILTER(STR(?n) = "%(rs)s")
}
LIMIT 5
"""

# ELI -> expressoes em frances (a versao consolidada tem URI com data
# AAAAMMDD; a versao original nao). Opcionalmente traz o arquivo HTML.
QUERY_FR_EXPRESSIONS = PREFIXES + """\
SELECT DISTINCT ?expr ?file WHERE {
  ?expr a jolux:Expression ;
        jolux:language <http://publications.europa.eu/resource/authority/language/FRA> .
  FILTER(STRSTARTS(STR(?expr), "%(eli)s/"))
  OPTIONAL {
    ?expr jolux:isEmbodiedBy ?man .
    ?man jolux:isExemplifiedBy ?file .
    FILTER(STRENDS(STR(?file), ".html"))
  }
}
LIMIT 500
"""


# --------------------------------------------------------------------------
# Normalizacao
# --------------------------------------------------------------------------
_APOS = dict.fromkeys(map(ord, "’‘ʼ′`´"), "'")
_QUOTES = dict.fromkeys(map(ord, "«»“”„"), '"')
_DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")
_INVISIBLE = dict.fromkeys(map(ord, "­​‌‍⁠﻿"), None)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.translate(_INVISIBLE).translate(_APOS).translate(_QUOTES).translate(_DASHES)
    text = re.sub(r"\s+", " ", text, flags=re.UNICODE)  # \s cobre nbsp/espacos finos
    text = re.sub(r'" (?=\S)|(?<=\S) "', '"', text)  # espacos de guillemets «  »
    return text.strip()


_GLUED_NOTE = re.compile(r"(?<=[^\W\d_])\d{1,3}(?=[\s.,;:)\]]|$)")
_LEADING_NUM = re.compile(r"^\d{1,2}\s+(?=\D)")


def strip_notes(text: str) -> str:
    """Variante tolerante: remove numeros de nota colados ao fim de palavra e
    numero de alinea inicial. Usada so como segunda tentativa."""
    text = _GLUED_NOTE.sub("", text)
    text = _LEADING_NUM.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def norm_article(art) -> str:
    """'Art. 36', '36', '36a', '36 bis' -> '36', '36a', '36bis' (minusculo)."""
    s = normalize(str(art or "")).lower()
    s = re.sub(r"^(art(icle)?s?\.?\s*)", "", s)
    s = re.sub(r"[\s.]+", "", s)
    return s


# --------------------------------------------------------------------------
# Extracao de texto do HTML do Fedlex
# --------------------------------------------------------------------------
_BLOCK = {"p", "div", "li", "ul", "ol", "tr", "table", "article", "section",
          "br", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "dd", "dt", "dl",
          "blockquote", "body", "header", "footer", "nav"}
_VOID = {"br", "img", "hr", "meta", "link", "input", "col", "area", "base", "wbr"}
_SKIP = {"script", "style", "head", "noscript"}
_HEADING = {"h1", "h2", "h3", "h4", "h5", "h6"}
_LATIN = "bis|ter|quater|quinquies|sexies|septies|octies|novies|decies"
_ART_RE = re.compile(
    rf"^Art(?:icle)?\.?\s+(\d+(?:(?:\s?(?:{_LATIN}))|(?:[a-z](?![^\W\d_])))?)(?![^\W_])", re.I)
_NOTE_SUP = re.compile(r"^\d+[a-z]{0,6}$", re.I)


class _Extractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, bool]] = []  # (tag, skipping?)
        self.skip_depth = 0
        self.blocks: list[tuple[str, str]] = []  # (kind, texto) ; kind 'h' ou 'p'
        self.cur: list[str] = []
        self.in_heading = 0
        self.sup_buf: list[str] | None = None
        self.sup_depth = 0

    def _flush(self) -> None:
        txt = "".join(self.cur)
        self.cur = []
        if txt.strip():
            self.blocks.append(("h" if self.in_heading else "p", txt))

    def handle_starttag(self, tag, attrs):
        cls = " ".join(v or "" for k, v in attrs if k == "class").lower()
        skip = tag in _SKIP or "footnote" in cls
        if tag == "sup" and self.sup_buf is None:
            self.sup_buf = []
            self.sup_depth = 0
        if self.sup_buf is not None and tag == "sup":
            self.sup_depth += 1
        if tag in _BLOCK:
            self._flush()
        if tag in _VOID:
            return
        if skip:
            self.skip_depth += 1
        if tag in _HEADING:
            self.in_heading += 1
        self.stack.append((tag, skip))

    def handle_startendtag(self, tag, attrs):
        if tag in _BLOCK:
            self._flush()

    def handle_endtag(self, tag):
        if tag in _VOID:
            return
        # fecha ate o tag correspondente (tolerante a HTML mal formado)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                while len(self.stack) > i:
                    t, sk = self.stack.pop()
                    if sk:
                        self.skip_depth -= 1
                    if t == "sup":
                        self._end_sup()
                    if t in _HEADING:
                        self._flush()
                        self.in_heading -= 1
                break
        if tag in _BLOCK:
            self._flush()

    def _end_sup(self) -> None:
        if self.sup_buf is None:
            return
        self.sup_depth -= 1
        if self.sup_depth > 0:
            return
        content = "".join(self.sup_buf).strip()
        self.sup_buf = None
        if content and not _NOTE_SUP.match(content):
            self.cur.append(content)  # ex.: 1<sup>er</sup> -> mantem "er"
        # nota / numero de alinea (so digitos): descartada

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.sup_buf is not None:
            self.sup_buf.append(data)
        else:
            self.cur.append(data)

    def close(self):
        super().close()
        self._flush()


def parse_law_html(raw: str) -> dict:
    """Retorna {'text': texto normalizado completo, 'articles': {id: texto}}.
    Artigos sao detectados por cabecalhos (h1-h6) que comecam com 'Art. N'.
    Se nenhum for detectado, 'articles' fica vazio (artigo nao conferivel)."""
    ex = _Extractor()
    ex.feed(raw)
    ex.close()
    articles: dict[str, list[str]] = {}
    full: list[str] = []
    current: str | None = None
    for kind, txt in ex.blocks:
        ntxt = normalize(txt)
        if not ntxt:
            continue
        if kind == "h":
            m = _ART_RE.match(ntxt)
            if m:
                current = norm_article(m.group(1))
                articles.setdefault(current, [])
            else:
                current = None if re.match(r"^(Section|Chapitre|Titre|Partie)\b", ntxt, re.I) else current
        full.append(ntxt)
        if current is not None:
            articles[current].append(ntxt)
    return {
        "text": " ".join(full),
        "articles": {k: " ".join(v) for k, v in articles.items()},
    }


# --------------------------------------------------------------------------
# Rede / resolucao RS -> HTML
# --------------------------------------------------------------------------
def http_get(url: str, accept: str = "text/html,*/*", timeout: int = 60, retries: int = 3) -> bytes:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET {url} falhou: {last}")


def sparql(query: str) -> list[dict]:
    url = SPARQL_ENDPOINT + "?" + urllib.parse.urlencode({"query": query})
    data = json.loads(http_get(url, accept="application/sparql-results+json"))
    return [{k: v.get("value") for k, v in b.items()} for b in data["results"]["bindings"]]


def eli_from_url(url: str | None) -> str | None:
    m = re.search(r"/eli/cc/([\w./-]+?)(?:/(?:\d{8}|fr|de|it|en)(?:/.*)?)?$", url or "")
    return ELI_PREFIX + m.group(1).strip("/") if m else None


def filestore_url(eli: str, date8: str) -> str:
    path = eli.replace("https://fedlex.data.admin.ch/", "")
    slug = "fedlex-data-admin-ch-" + re.sub(r"[/.]", "-", path).replace("_", "_")
    # observado no site: '_' preservado, '/' vira '-'
    return (f"https://fedlex.admin.ch/filestore/fedlex.data.admin.ch/{path}/{date8}/fr/html/"
            f"{slug}-{date8}-fr-html-1.html")


def pick_expression(rows: list[dict], today: str) -> tuple[str, str | None] | None:
    """Escolhe a expressao consolidada em vigor (data <= today, a maior)."""
    best = None
    for r in rows:
        m = re.search(r"/(\d{8})/fr/?$", r.get("expr", ""))
        if not m or m.group(1) > today:
            continue
        cand = (m.group(1), r.get("file"))
        if best is None or cand[0] > best[0] or (cand[0] == best[0] and cand[1] and not best[1]):
            best = cand
    return best


def resolve_law_urls(rs: str, eli_hint: str | None, today: str) -> list[str]:
    """RS -> lista de URLs candidatas do HTML consolidado em frances (rede).
    Isolada para ser trocada/ajustada sem mexer no resto."""
    eli = eli_hint
    if not eli:
        rows = sparql(QUERY_ELI_BY_RS % {"rs": rs})
        elis = [r["act"] for r in rows if r.get("act", "").startswith(ELI_PREFIX)]
        if not elis:
            raise RuntimeError(f"RS {rs}: nenhum ato encontrado no SPARQL")
        eli = elis[0]
    rows = sparql(QUERY_FR_EXPRESSIONS % {"eli": eli})
    best = pick_expression(rows, today)
    if not best:
        raise RuntimeError(f"RS {rs}: nenhuma expressao consolidada FR <= {today} para {eli}")
    date8, file_url = best
    urls = [file_url] if file_url else []
    urls.append(filestore_url(eli, date8))
    return urls


def load_sources_map(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if isinstance(data, dict) and isinstance(data.get("sources"), dict):
        data = data["sources"]
    return {str(k): str(v) for k, v in data.items()} if isinstance(data, dict) else {}


def fetch_law(rs: str, eli_hint, today: str, sources: dict[str, str], offline: Path | None) -> tuple[str, str]:
    """Retorna (html, origem)."""
    if offline is not None:
        p = offline / f"{rs}.html"
        if not p.exists():
            raise RuntimeError(f"arquivo offline ausente: {p}")
        return p.read_text(encoding="utf-8"), str(p)
    if rs in sources:
        src = sources[rs]
        if re.match(r"^https?://", src):
            return http_get(src).decode("utf-8", "replace"), src
        p = (ROOT / src) if not Path(src).is_absolute() else Path(src)
        return p.read_text(encoding="utf-8"), str(p)
    urls = resolve_law_urls(rs, eli_hint, today)
    errs = []
    for u in urls:
        try:
            return http_get(u).decode("utf-8", "replace"), u
        except Exception as e:  # noqa: BLE001
            errs.append(str(e))
    raise RuntimeError(f"RS {rs}: nenhuma URL funcionou: {errs}")


# --------------------------------------------------------------------------
# Regras
# --------------------------------------------------------------------------
def load_rules(rules_dir: Path) -> list[dict]:
    rules: list[dict] = []
    for f in sorted(list(rules_dir.glob("*.yaml")) + list(rules_dir.glob("*.yml"))):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            for key in ("regras", "rules"):
                if isinstance(data.get(key), list):
                    data = data[key]
                    break
            else:
                data = [data] if "id" in data else []
        if not isinstance(data, list):
            continue
        for r in data:
            if isinstance(r, dict):
                r = dict(r)
                r["_arquivo"] = f.name
                rules.append(r)
    return rules


def rule_fields(r: dict) -> dict:
    fonte = r.get("fonte") if isinstance(r.get("fonte"), dict) else {}
    rs = fonte.get("rs")
    return {
        "id": str(r.get("id", "?")),
        "rs": str(rs).strip() if rs not in (None, "") else "",
        "artigo": str(fonte.get("artigo", "") or "").strip(),
        "url": str(fonte.get("url", "") or "").strip(),
        "trecho": str(r.get("trecho_literal_fr") or "").strip(),
        "arquivo": r.get("_arquivo", ""),
    }


def check_quote(trecho: str, law: dict, artigo: str) -> tuple[str, str, str]:
    """Retorna (status, motivo, artigo_check). status in OK/FALHA."""
    q = normalize(trecho)
    variants = [("literal", q, law["text"]), ("sem_notas", strip_notes(q), strip_notes(law["text"]))]
    mode = None
    for name, qq, tt in variants:
        if qq and qq in tt:
            mode = name
            break
    if mode is None:
        return "FALHA", "trecho nao encontrado no texto da lei", "-"
    note = "" if mode == "literal" else "encontrado so apos remover numeros de nota/alinea"
    art = norm_article(artigo)
    if not art:
        return "OK", note or "encontrado na lei; artigo nao informado", "nao_conferido"
    seg = law["articles"].get(art)
    if seg is None:
        return "OK", (note + "; " if note else "") + "encontrado na lei; artigo nao localizado no HTML", "nao_conferido"
    qq = q if mode == "literal" else strip_notes(q)
    ss = seg if mode == "literal" else strip_notes(seg)
    if qq in ss:
        return "OK", note, "confirmado"
    return "FALHA", f"trecho existe na lei mas nao dentro do art. {artigo}", "divergente"


def run(rules_dir: Path, report: Path, offline: Path | None, sources_path: Path, today: str) -> int:
    rules = load_rules(rules_dir)
    infos = [rule_fields(r) for r in rules]
    sources = load_sources_map(sources_path)

    need: dict[str, str | None] = {}
    for i in infos:
        if i["trecho"] and i["rs"]:
            need.setdefault(i["rs"], None)
            if not need[i["rs"]]:
                need[i["rs"]] = eli_from_url(i["url"])

    laws: dict[str, dict] = {}
    law_report: dict[str, dict] = {}
    fetch_errors = 0
    for rs, eli in sorted(need.items()):
        try:
            raw, origin = fetch_law(rs, eli, today, sources, offline)
            laws[rs] = parse_law_html(raw)
            law_report[rs] = {"ok": True, "origem": origin, "eli": eli,
                              "artigos_detectados": len(laws[rs]["articles"]),
                              "caracteres": len(laws[rs]["text"])}
            if not laws[rs]["text"]:
                raise RuntimeError("HTML sem texto extraivel")
        except Exception as e:  # noqa: BLE001
            fetch_errors += 1
            laws.pop(rs, None)
            law_report[rs] = {"ok": False, "erro": str(e)}

    results = []
    for i in infos:
        if not i["trecho"]:
            status, motivo, ac = "SEM_TRECHO", "trecho_literal_fr vazio", "-"
        elif not i["rs"]:
            status, motivo, ac = "FALHA", "fonte.rs ausente", "-"
        elif i["rs"] not in laws:
            status, motivo, ac = "FALHA", f"lei RS {i['rs']} nao obtida", "-"
        else:
            status, motivo, ac = check_quote(i["trecho"], laws[i["rs"]], i["artigo"])
        results.append({"id": i["id"], "rs": i["rs"], "artigo": i["artigo"], "status": status,
                        "artigo_check": ac, "motivo": motivo, "arquivo": i["arquivo"]})

    counts = {s: sum(1 for r in results if r["status"] == s) for s in ("OK", "FALHA", "SEM_TRECHO")}
    out = {"gerado_em": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "data_referencia": today, "modo": "offline" if offline else "rede",
           "resumo": {**counts, "total": len(results), "leis_nao_obtidas": fetch_errors},
           "leis": law_report, "regras": results}
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # tabela
    w = max([len(r["id"]) for r in results] + [2])
    print(f"{'ID'.ljust(w)}  {'RS':<9} {'ART':<6} {'STATUS':<10} {'ARTIGO':<13} MOTIVO")
    for r in results:
        print(f"{r['id'].ljust(w)}  {r['rs']:<9} {r['artigo']:<6} {r['status']:<10} {r['artigo_check']:<13} {r['motivo']}")
    for rs, lr in law_report.items():
        if not lr["ok"]:
            print(f"ERRO lei RS {rs}: {lr['erro']}", file=sys.stderr)
    print(f"\nResumo: {counts} | leis nao obtidas: {fetch_errors} | relatorio: {report}")
    return 1 if (counts["FALHA"] or fetch_errors) else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rules-dir", type=Path, default=ROOT / "legal" / "rules")
    ap.add_argument("--report", type=Path, default=ROOT / "reports" / "quotes.json")
    ap.add_argument("--offline", type=Path, metavar="DIR", help="usa DIR/<rs>.html em vez da rede")
    ap.add_argument("--sources", type=Path, default=Path(__file__).resolve().parent / "fedlex_sources.yaml")
    ap.add_argument("--today", default=dt.date.today().strftime("%Y%m%d"), help="AAAAMMDD (so afeta a escolha da versao)")
    a = ap.parse_args(argv)
    return run(a.rules_dir, a.report, a.offline, a.sources, a.today)


if __name__ == "__main__":
    sys.exit(main())
