import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_data as bd  # noqa: E402

RULES_YAML = """
rules:
- id: R-T-001
  categoria: D-Priorite
  subtema: teste
  regra_pt: "Regra validada (fixture)."
  termos_fr: ["priorité de droite"]
  fonte: { lei: OCR, rs: "741.11", artigo: "36", url: "https://example.org/x" }
  trecho_literal_fr: "nao deve ir para o app"
  excecoes: ["Excecao A"]
  versao_lei_em_vigor_desde: "2026-10-01"
  verificado_em: "2026-11-26"
  status: validado
- id: R-T-002
  categoria: D-Priorite
  subtema: teste
  regra_pt: "Regra pendente (fixture)."
  status: pendente
- id: R-T-003
  categoria: A-Sinais
  subtema: teste
  regra_pt: "Regra revisada pela IA, ainda sem OK do Luan."
  status: revisado_ia
"""


def question(qid, regra_ids, status="aprovado", categoria="D-Priorite"):
    return {
        "id": qid, "regra_ids": regra_ids, "categoria": categoria, "subtema": "teste",
        "competencia": "x", "nivel": 1,
        "enunciado": f"Pergunta FICTICIA {qid}",
        "alternativas": [
            {"texto": "Certa", "correta": True, "justificativa": "porque sim"},
            {"texto": "Errada", "correta": False, "justificativa": "porque nao"},
        ],
        "explicacao": {"regra_simples": "rs", "por_que": "pq", "como_identificar": "ci",
                       "erro_comum": "ec", "excecao": "ex", "palavras_fr": ["priorité"]},
        "etiqueta": "verificacao_pendente",
        "status": status,
    }


QUESTIONS = [
    question("Q-OK", ["R-T-001"]),                       # entra sempre
    question("Q-REGRA-PEND", ["R-T-001", "R-T-002"]),     # aprovada, mas 1 regra pendente
    question("Q-RASCUNHO", ["R-T-001"], status="rascunho"),
    question("Q-SEM-REGRA", []),                          # sem regras: nunca confiavel
    question("Q-REGRA-INEXISTENTE", ["R-NAO-EXISTE"]),
    question("Q-REV-IA", ["R-T-003"], categoria="A-Sinais", status="revisado_ia"),
]


def make_dirs(td: Path, questions=QUESTIONS, rules_yaml=RULES_YAML):
    rd, qd = td / "rules", td / "questions"
    rd.mkdir()
    qd.mkdir()
    (rd / "t.yaml").write_text(rules_yaml, encoding="utf-8")
    (qd / "t.json").write_text(json.dumps(questions), encoding="utf-8")
    return rd, qd


def run(td: Path, *flags, questions=QUESTIONS):
    rd, qd = make_dirs(td, questions)
    out = td / "out" / "content.json"
    code = bd.main(["--rules-dir", str(rd), "--questions-dir", str(qd), "--out", str(out), *flags])
    return code, json.loads(out.read_text(encoding="utf-8"))


class SafeMode(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.addCleanup(self._td.cleanup)
        self.code, self.c = run(Path(self._td.name))

    def test_ok_and_mode(self):
        self.assertEqual(self.code, 0)
        self.assertEqual(self.c["modo"], "seguro")

    def test_pending_rules_out(self):
        self.assertEqual([r["id"] for r in self.c["regras"]], ["R-T-001"])

    def test_only_approved_with_all_rules_validated(self):
        self.assertEqual([q["id"] for q in self.c["perguntas"]], ["Q-OK"])

    def test_pending_counts_exported(self):
        p = self.c["pendentes"]
        self.assertEqual(p["regras"], 2)       # R-T-002 e R-T-003
        self.assertEqual(p["perguntas"], 5)
        self.assertEqual(p["por_categoria"]["D"], {"regras": 1, "perguntas": 4})
        self.assertEqual(p["por_categoria"]["A"], {"regras": 1, "perguntas": 1})
        cats = {c["id"]: c for c in self.c["categorias"]}
        self.assertEqual(cats["D"]["regras"], 1)
        self.assertEqual(cats["D"]["perguntas"], 1)
        self.assertEqual(cats["D"]["regras_pendentes"], 1)
        self.assertEqual(cats["A"]["regras"], 0)
        self.assertEqual(cats["A"]["regras_pendentes"], 1)

    def test_literal_quote_not_shipped(self):
        self.assertNotIn("trecho_literal_fr", self.c["regras"][0])


class DraftMode(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.addCleanup(self._td.cleanup)
        self.code, self.c = run(Path(self._td.name), "--include-pending")

    def test_includes_everything(self):
        self.assertEqual(self.c["modo"], "rascunho")
        self.assertEqual({r["id"] for r in self.c["regras"]}, {"R-T-001", "R-T-002", "R-T-003"})
        self.assertEqual(len(self.c["perguntas"]), len(QUESTIONS))

    def test_status_preserved_so_app_can_flag(self):
        st = {r["id"]: r["status"] for r in self.c["regras"]}
        self.assertEqual(st["R-T-002"], "pendente")

    def test_pending_counts_still_exported(self):
        self.assertEqual(self.c["pendentes"]["regras"], 2)


class Format(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.addCleanup(self._td.cleanup)
        _, self.c = run(Path(self._td.name), "--include-pending")

    def test_top_level_keys(self):
        self.assertEqual(set(self.c), {"schema", "gerado_em", "modo", "categorias",
                                       "regras", "perguntas", "pendentes"})
        self.assertEqual(self.c["schema"], 1)

    def test_categories_a_to_j_always_present(self):
        self.assertEqual([c["id"] for c in self.c["categorias"]][:10], list("ABCDEFGHIJ"))
        for c in self.c["categorias"]:
            self.assertEqual(set(c), {"id", "nome", "regras", "perguntas",
                                      "regras_pendentes", "perguntas_pendentes"})

    def test_rule_shape(self):
        r = next(r for r in self.c["regras"] if r["id"] == "R-T-001")
        self.assertEqual(r["cat"], "D")
        self.assertEqual(r["termos_fr"], ["priorité de droite"])
        self.assertEqual(r["excecoes"], ["Excecao A"])
        self.assertEqual(r["fonte"]["url"], "https://example.org/x")

    def test_question_shape(self):
        q = self.c["perguntas"][0]
        for k in ("id", "regra_ids", "cat", "enunciado", "alternativas", "explicacao", "status"):
            self.assertIn(k, q)
        self.assertEqual(set(q["explicacao"]), set(bd.EXPLICACAO_FIELDS))
        self.assertEqual(set(q["alternativas"][0]), {"texto", "correta", "justificativa"})
        self.assertIsInstance(q["alternativas"][0]["correta"], bool)


class EdgeCases(unittest.TestCase):
    def test_zero_content(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            rd, qd = td / "r", td / "q"
            rd.mkdir()
            qd.mkdir()
            out = td / "o" / "content.json"
            self.assertEqual(bd.main(["--rules-dir", str(rd), "--questions-dir", str(qd),
                                      "--out", str(out)]), 0)
            c = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual((c["regras"], c["perguntas"]), ([], []))
            self.assertEqual(c["pendentes"]["regras"], 0)
            self.assertEqual(len(c["categorias"]), 10)

    def test_invalid_question_dropped_even_in_draft(self):
        bad = {"id": "Q-BAD", "enunciado": "x", "alternativas": [{"texto": "a", "correta": True}]}
        with tempfile.TemporaryDirectory() as td:
            _, c = run(Path(td), "--include-pending", questions=[bad, question("Q-OK", ["R-T-001"])])
        self.assertEqual([q["id"] for q in c["perguntas"]], ["Q-OK"])

    def test_duplicate_rule_id_is_error(self):
        dup = RULES_YAML + "\n- id: R-T-001\n  categoria: D-Priorite\n  regra_pt: x\n  status: pendente\n"
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            rd, qd = make_dirs(td, [], dup)
            self.assertEqual(bd.main(["--rules-dir", str(rd), "--questions-dir", str(qd),
                                      "--out", str(td / "c.json")]), 2)

    def test_validated_rule_with_empty_text_not_trusted(self):
        y = "rules:\n- id: R-E\n  categoria: D-Priorite\n  regra_pt: ''\n  status: validado\n"
        c, _ = bd.build(bd.load_rules(_write(y)), [], False)
        self.assertEqual(c["regras"], [])

    def test_cat_letter(self):
        self.assertEqual(bd.cat_letter("D-Priorite"), "D")
        self.assertEqual(bd.cat_letter("a"), "A")
        self.assertEqual(bd.cat_letter(None), "X")
        self.assertEqual(bd.cat_letter("Priorite"), "X")


def _write(yaml_text: str) -> Path:
    d = Path(tempfile.mkdtemp())
    (d / "r.yaml").write_text(yaml_text, encoding="utf-8")
    return d


if __name__ == "__main__":
    unittest.main()
