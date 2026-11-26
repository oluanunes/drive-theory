#!/usr/bin/env python3
"""Gera app/data/content.json a partir de legal/rules/*.yaml e questions/*.json.

Regra de ouro (SPEC §5): so entram no treino perguntas com status "aprovado"
cujas regras (todas) estao "validado". Regras entram no modo Aprender apenas se
"validado". O padrao e SEGURO. A flag --include-pending inclui tudo (modo
rascunho, so para desenvolvimento): o app mostra uma faixa vermelha.

O JSON tambem exporta, separado, a contagem de regras/perguntas pendentes por
categoria (campo "pendentes"), para o app mostrar "X regras aguardando validacao".

Uso:
    python3 scripts/build_data.py                      # modo seguro
    python3 scripts/build_data.py --include-pending    # rascunho (dev)
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

SCHEMA = 1

# Nomes de exibicao das categorias (letra -> nome em portugues). Editavel.
CATEGORIAS = {
    "A": "Sinais e marcações",
    "B": "Parar e estacionar",
    "C": "Condutor e comportamento",
    "D": "Prioridade (priorité)",
    "E": "Ultrapassagem",
    "F": "Acidentes e panes",
    "G": "Velocidade, distância e outros usuários",
    "H": "Assistência à condução",
    "I": "Ferramentas",
    "J": "Extras",
}

RULE_FIELDS = ("id", "categoria", "subtema", "regra_pt", "termos_fr", "fonte",
               "excecoes", "versao_lei_em_vigor_desde", "verificado_em", "status")
EXPLICACAO_FIELDS = ("regra_simples", "por_que", "como_identificar",
                     "erro_comum", "excecao", "palavras_fr")


def cat_letter(categoria) -> str:
    """'D-Priorite' -> 'D'. Se nao der para extrair, devolve 'X'."""
    m = re.match(r"^\s*([A-Za-z])\s*(?:-|$)", str(categoria or ""))
    return m.group(1).upper() if m else "X"


def _as_list(v) -> list:
    if v is None:
        return []
    return list(v) if isinstance(v, (list, tuple)) else [v]


# --------------------------------------------------------------------------
# Leitura
# --------------------------------------------------------------------------
def load_rules(rules_dir: Path) -> list[dict]:
    rules: list[dict] = []
    files = sorted(list(rules_dir.glob("*.yaml")) + list(rules_dir.glob("*.yml")))
    for f in files:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            for key in ("rules", "regras"):
                if isinstance(data.get(key), list):
                    data = data[key]
                    break
            else:
                data = [data] if "id" in data else []
        if not isinstance(data, list):
            continue
        rules.extend(r for r in data if isinstance(r, dict))
    return rules


def load_questions(questions_dir: Path) -> list[dict]:
    qs: list[dict] = []
    for f in sorted(questions_dir.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            for key in ("perguntas", "questions"):
                if isinstance(data.get(key), list):
                    data = data[key]
                    break
            else:
                data = [data] if "id" in data else []
        if isinstance(data, list):
            qs.extend(q for q in data if isinstance(q, dict))
    return qs


# --------------------------------------------------------------------------
# Transformacao
# --------------------------------------------------------------------------
def question_problem(q: dict) -> str | None:
    """Devolve o motivo se a pergunta tem formato invalido, senao None."""
    if not isinstance(q.get("id"), str) or not q["id"].strip():
        return "id ausente"
    if not isinstance(q.get("enunciado"), str) or not q["enunciado"].strip():
        return "enunciado ausente"
    alts = q.get("alternativas")
    if not isinstance(alts, list) or len(alts) < 2:
        return "menos de 2 alternativas"
    for a in alts:
        if not isinstance(a, dict) or not isinstance(a.get("texto"), str) \
                or not a["texto"].strip() or not isinstance(a.get("correta"), bool):
            return "alternativa invalida (texto/correta)"
    return None


def clean_rule(r: dict) -> dict:
    out = {k: r.get(k) for k in RULE_FIELDS}
    out["cat"] = cat_letter(r.get("categoria"))
    out["termos_fr"] = [str(x) for x in _as_list(r.get("termos_fr"))]
    out["excecoes"] = [str(x) for x in _as_list(r.get("excecoes"))]
    fonte = r.get("fonte")
    out["fonte"] = dict(fonte) if isinstance(fonte, dict) else {}
    for k in ("versao_lei_em_vigor_desde", "verificado_em"):
        if out[k] is not None:
            out[k] = str(out[k])
    return out


def clean_question(q: dict) -> dict:
    expl = q.get("explicacao") if isinstance(q.get("explicacao"), dict) else {}
    alts = [{"texto": a["texto"], "correta": a["correta"],
             "justificativa": a.get("justificativa") or ""} for a in q["alternativas"]]
    return {
        "id": q["id"],
        "regra_ids": [str(x) for x in _as_list(q.get("regra_ids"))],
        "categoria": q.get("categoria"),
        "cat": cat_letter(q.get("categoria")),
        "subtema": q.get("subtema"),
        "competencia": q.get("competencia"),
        "nivel": q.get("nivel"),
        "enunciado": q["enunciado"],
        "imagem": q.get("imagem") or None,
        "alternativas": alts,
        "explicacao": {k: expl.get(k) for k in EXPLICACAO_FIELDS},
        "etiqueta": q.get("etiqueta"),
        "status": q.get("status"),
    }


def build(rules: list[dict], questions: list[dict], include_pending: bool = False,
          now: str | None = None) -> tuple[dict, list[str]]:
    """Devolve (content, avisos)."""
    avisos: list[str] = []

    # IDs duplicados sao ambiguos (um validado, outro nao): erro.
    seen: set[str] = set()
    for r in rules:
        rid = str(r.get("id", ""))
        if not rid:
            avisos.append("regra sem id ignorada")
            continue
        if rid in seen:
            raise ValueError(f"id de regra duplicado: {rid}")
        seen.add(rid)
    seen_q: set[str] = set()
    for q in questions:
        qid = q.get("id")
        if isinstance(qid, str):
            if qid in seen_q:
                raise ValueError(f"id de pergunta duplicado: {qid}")
            seen_q.add(qid)

    rules = [r for r in rules if r.get("id")]
    status_by_rule = {str(r["id"]): r.get("status") for r in rules}

    pend: dict[str, dict] = {}

    def bucket(letter: str) -> dict:
        return pend.setdefault(letter, {"regras": 0, "perguntas": 0})

    out_rules: list[dict] = []
    for r in rules:
        letter = cat_letter(r.get("categoria"))
        validated = r.get("status") == "validado" and bool(str(r.get("regra_pt") or "").strip())
        if not validated:
            bucket(letter)["regras"] += 1
        if validated or include_pending:
            out_rules.append(clean_rule(r))

    out_questions: list[dict] = []
    invalidas = 0
    for q in questions:
        problem = question_problem(q)
        if problem:
            invalidas += 1
            avisos.append(f"pergunta {q.get('id', '?')} ignorada: {problem}")
            continue
        letter = cat_letter(q.get("categoria"))
        ids = [str(x) for x in _as_list(q.get("regra_ids"))]
        rules_ok = bool(ids) and all(status_by_rule.get(i) == "validado" for i in ids)
        eligible = q.get("status") == "aprovado" and rules_ok
        if not eligible:
            bucket(letter)["perguntas"] += 1
        if eligible or include_pending:
            out_questions.append(clean_question(q))

    letters = list(CATEGORIAS)
    for x in sorted({r["cat"] for r in out_rules} | {q["cat"] for q in out_questions} | set(pend)):
        if x not in letters:
            letters.append(x)

    categorias = []
    for L in letters:
        p = pend.get(L, {"regras": 0, "perguntas": 0})
        categorias.append({
            "id": L,
            "nome": CATEGORIAS.get(L, "Outras"),
            "regras": sum(1 for r in out_rules if r["cat"] == L),
            "perguntas": sum(1 for q in out_questions if q["cat"] == L),
            "regras_pendentes": p["regras"],
            "perguntas_pendentes": p["perguntas"],
        })

    content = {
        "schema": SCHEMA,
        "gerado_em": now or _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "modo": "rascunho" if include_pending else "seguro",
        "categorias": categorias,
        "regras": out_rules,
        "perguntas": out_questions,
        "pendentes": {
            "regras": sum(v["regras"] for v in pend.values()),
            "perguntas": sum(v["perguntas"] for v in pend.values()),
            "por_categoria": {L: pend[L] for L in sorted(pend)},
        },
    }
    return content, avisos


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rules-dir", type=Path, default=ROOT / "legal" / "rules")
    ap.add_argument("--questions-dir", type=Path, default=ROOT / "questions")
    ap.add_argument("--out", type=Path, default=ROOT / "app" / "data" / "content.json")
    ap.add_argument("--include-pending", action="store_true",
                    help="MODO RASCUNHO (dev): inclui regras/perguntas nao validadas")
    args = ap.parse_args(argv)

    rules = load_rules(args.rules_dir) if args.rules_dir.is_dir() else []
    questions = load_questions(args.questions_dir) if args.questions_dir.is_dir() else []
    try:
        content, avisos = build(rules, questions, args.include_pending)
    except ValueError as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2
    for a in avisos:
        print(f"AVISO: {a}", file=sys.stderr)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(content, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    p = content["pendentes"]
    print(f"{args.out}: modo={content['modo']} regras={len(content['regras'])} "
          f"perguntas={len(content['perguntas'])} | pendentes: regras={p['regras']} "
          f"perguntas={p['perguntas']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
