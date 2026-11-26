#!/usr/bin/env python3
"""Valida questions/*.json contra legal/rules/*.yaml e o formato de build_data.py."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_data as bd

ROOT = bd.ROOT
CAMPOS = ("id", "regra_ids", "categoria", "subtema", "competencia", "nivel", "enunciado",
          "imagem", "alternativas", "explicacao", "etiqueta", "status")
ETIQ = {"legislacao_verificada", "questao_original", "cenario_pratico", "verificacao_pendente"}


def main() -> int:
    rules = {r["id"] for r in bd.load_rules(ROOT / "legal" / "rules")}
    qs = bd.load_questions(ROOT / "questions")
    erros, ids = [], set()
    niveis, multi = {}, 0
    for q in qs:
        i = q.get("id", "?")
        for c in CAMPOS:
            if c not in q:
                erros.append(f"{i}: campo ausente {c}")
        if i in ids:
            erros.append(f"{i}: id duplicado")
        ids.add(i)
        p = bd.question_problem(q)
        if p:
            erros.append(f"{i}: {p}")
        for r in q.get("regra_ids", []):
            if r not in rules:
                erros.append(f"{i}: regra inexistente {r}")
        if not q.get("regra_ids"):
            erros.append(f"{i}: sem regra_ids")
        alts = q.get("alternativas", [])
        n_ok = sum(1 for a in alts if a.get("correta"))
        if not 3 <= len(alts) <= 4:
            erros.append(f"{i}: {len(alts)} alternativas (esperado 3-4)")
        if n_ok == 0 or n_ok == len(alts):
            erros.append(f"{i}: {n_ok} corretas de {len(alts)}")
        multi += n_ok > 1
        for a in alts:
            if not a.get("justificativa"):
                erros.append(f"{i}: alternativa sem justificativa")
        for k in bd.EXPLICACAO_FIELDS:
            if not q.get("explicacao", {}).get(k):
                erros.append(f"{i}: explicacao.{k} vazio")
        if q.get("status") == "aprovado":
            erros.append(f"{i}: status aprovado (so o aluno aprova)")
        if q.get("etiqueta") not in ETIQ:
            erros.append(f"{i}: etiqueta invalida")
        if q.get("imagem") is not None:
            erros.append(f"{i}: imagem deve ser null")
        niveis[q.get("nivel")] = niveis.get(q.get("nivel"), 0) + 1
    print(f"{len(qs)} perguntas; niveis {dict(sorted(niveis.items()))}; multiplas corretas: {multi}")
    for e in erros:
        print("ERRO", e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
