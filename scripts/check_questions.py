#!/usr/bin/env python3
"""Valida questions/*.json contra legal/rules/*.yaml e o formato de build_data.py."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_data as bd

ROOT = bd.ROOT
CAMPOS = ("id", "regra_ids", "categoria", "subtema", "competencia", "nivel", "enunciado",
          "imagem", "alternativas", "explicacao", "etiqueta", "status")
# Enunciado nao pode entregar quantas alternativas marcar nem usar a forma singular.
VAZAMENTO = re.compile(r"Qual (a )?(afirma|alternativa)|Marque (apenas |somente )?(uma|duas|tr[eê]s|1|2|3)\b|"
                       r"(uma|duas|tr[eê]s|1|2|3) (alternativas?|afirma)|Quantas", re.I)
MAX_PRIMEIRA_CORRETA = 0.5  # fracao maxima de perguntas com a 1a alternativa correta
ETIQ = {"legislacao_verificada", "questao_original", "cenario_pratico", "verificacao_pendente"}


def main() -> int:
    rules = {r["id"] for r in bd.load_rules(ROOT / "legal" / "rules")}
    qs = bd.load_questions(ROOT / "questions")
    erros, ids = [], set()
    niveis, multi, primeira = {}, 0, 0
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
        if VAZAMENTO.search(q.get("enunciado", "")):
            erros.append(f"{i}: enunciado entrega o numero de corretas ou usa o singular")
        if not str(q.get("enunciado", "")).rstrip().endswith("estão corretas?"):
            erros.append(f"{i}: enunciado deve terminar em 'Quais afirmações ... estão corretas?'")
        if alts and alts[0].get("correta"):
            primeira += 1
        if n_ok > 1 and [a.get("correta") for a in alts][:n_ok] == [True] * n_ok:
            erros.append(f"{i}: corretas todas no inicio da lista")
        for a in alts:
            if not a.get("justificativa"):
                erros.append(f"{i}: alternativa sem justificativa")
        for k in bd.EXPLICACAO_FIELDS:
            if not q.get("explicacao", {}).get(k):
                erros.append(f"{i}: explicacao.{k} vazio")
        if q.get("status") == "aprovado" and not (q.get("aprovado_por") and q.get("aprovado_em")):
            erros.append(f"{i}: status aprovado exige aprovado_por e aprovado_em (aprovacao do Luan, direta ou delegada)")
        if q.get("etiqueta") not in ETIQ:
            erros.append(f"{i}: etiqueta invalida")
        if q.get("imagem") is not None:
            erros.append(f"{i}: imagem deve ser null")
        niveis[q.get("nivel")] = niveis.get(q.get("nivel"), 0) + 1
    if qs and primeira / len(qs) > MAX_PRIMEIRA_CORRETA:
        erros.append(f"vies de posicao: {primeira}/{len(qs)} perguntas com a 1a alternativa correta")
    print(f"{len(qs)} perguntas; niveis {dict(sorted(niveis.items()))}; multiplas corretas: {multi}; 1a alternativa correta: {primeira}")
    for e in erros:
        print("ERRO", e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
