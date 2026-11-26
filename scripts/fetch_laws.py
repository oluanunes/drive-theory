"""Baixa o texto consolidado em vigor (FR) das leis do projeto e salva em legal/sources/.

Roda no GitHub Actions (o ambiente do Claude nao acessa o Fedlex).
Saida por lei: legal/sources/<rs>.txt  (um bloco por linha; cabecalhos com '## ')
               legal/sources/INDEX.md (rs, nome, versao, url)
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_quotes as cq  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "legal" / "sources"

LAWS = {
    "741.01": "LCR — Loi fédérale sur la circulation routière",
    "741.11": "OCR — Ordonnance sur les règles de la circulation routière",
    "741.21": "OSR — Ordonnance sur la signalisation routière",
    "741.51": "OAC — Ordonnance réglant l'admission à la circulation routière",
    "741.41": "OETV — Ordonnance concernant les exigences techniques requises pour les véhicules routiers",
}

QUERY_CC_BY_RS = cq.PREFIXES + """\
SELECT DISTINCT ?act WHERE {
  ?act jolux:classifiedByTaxonomyEntry ?e .
  ?e skos:notation ?n .
  FILTER(STR(?n) = "%(rs)s" && STRSTARTS(STR(?act), "https://fedlex.data.admin.ch/eli/cc/"))
} LIMIT 5
"""


def eli_for(rs: str) -> str:
    if rs in cq.RS_ELI:
        return cq.RS_ELI[rs]
    rows = cq.sparql(QUERY_CC_BY_RS % {"rs": rs})
    elis = sorted({r["act"] for r in rows if r.get("act")})
    if not elis:
        raise RuntimeError(f"RS {rs}: ELI consolidado nao encontrado")
    return elis[0]


def to_text(raw: str) -> str:
    ex = cq._Extractor()
    ex.feed(raw)
    ex.close()
    lines = []
    for kind, txt in ex.blocks:
        t = cq.normalize(txt)
        if t:
            lines.append(("## " + t) if kind == "h" else t)
    return "\n".join(lines) + "\n"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().strftime("%Y%m%d")
    index = ["| RS | Lei | ELI | URL do HTML | Baixado em |", "|---|---|---|---|---|"]
    errors = 0
    for rs, name in LAWS.items():
        try:
            eli = eli_for(rs)
            url = cq.resolve_law_urls(rs, eli, today)[0]
            raw = cq.http_get(url).decode("utf-8", "replace")
            (OUT / f"{rs}.txt").write_text(to_text(raw), encoding="utf-8")
            index.append(f"| {rs} | {name} | {eli} | {url} | {today} |")
            print(f"OK {rs} {url}")
        except Exception as e:  # noqa: BLE001
            errors += 1
            index.append(f"| {rs} | {name} | ERRO | {e} | {today} |")
            print(f"ERRO {rs}: {e}")
    (OUT / "INDEX.md").write_text(
        "# Textos legais baixados do Fedlex (versão em vigor)\n\n"
        "Gerado por scripts/fetch_laws.py no GitHub Actions. Não editar à mão.\n\n"
        + "\n".join(index) + "\n", encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
