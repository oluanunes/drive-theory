import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_quotes as cq  # noqa: E402

FIX = HERE / "fixtures"


def run_cli(rules_files, extra_rules_text=None):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        rd = td / "rules"
        rd.mkdir()
        for f in rules_files:
            (rd / f).write_text((FIX / f).read_text(encoding="utf-8"), encoding="utf-8")
        if extra_rules_text:
            (rd / "extra.yaml").write_text(extra_rules_text, encoding="utf-8")
        # fixtures de lei: arquivo <rs>.html
        off = td / "off"
        off.mkdir()
        (off / "999.01.html").write_text((FIX / "999.01.html").read_text(encoding="utf-8"), encoding="utf-8")
        rep = td / "out" / "quotes.json"
        code = cq.main(["--rules-dir", str(rd), "--report", str(rep), "--offline",
                        str(off), "--sources", str(td / "nao_existe.yaml")])
        return code, json.loads(rep.read_text(encoding="utf-8"))


def by_id(report):
    return {r["id"]: r for r in report["regras"]}


class Normalize(unittest.TestCase):
    def test_apostrophe_nbsp_nfc(self):
        self.assertEqual(cq.normalize("l’a  b c"), "l'a b c")
        self.assertEqual(cq.normalize("é"), "é")

    def test_article_norm(self):
        self.assertEqual(cq.norm_article("Art. 36"), "36")
        self.assertEqual(cq.norm_article("2 A"), "2a")
        self.assertEqual(cq.norm_article(36), "36")


class Parse(unittest.TestCase):
    def setUp(self):
        self.law = cq.parse_law_html((FIX / "999.01.html").read_text(encoding="utf-8"))

    def test_articles_detected(self):
        self.assertEqual(set(self.law["articles"]), {"1", "2a"})

    def test_footnotes_and_alinea_numbers_dropped(self):
        t = self.law["text"]
        self.assertNotIn("Note de bas de page", t)
        self.assertIn("fictif avant chaque", t)
        self.assertIn("Le 1er véhicule", t)
        self.assertNotIn("FIXTURE DE TESTE", t)  # comentario HTML ignorado

    def test_entities(self):
        self.assertIn("piste d'essai", self.law["text"])

    def test_pick_expression(self):
        rows = [{"expr": "x/20200101/fr"}, {"expr": "x/20260101/fr", "file": "f.html"},
                {"expr": "x/29990101/fr"}, {"expr": "x/fr"}]
        self.assertEqual(cq.pick_expression(rows, "20261126"), ("20260101", "f.html"))
        self.assertIsNone(cq.pick_expression([{"expr": "x/fr"}], "20261126"))

    def test_eli_from_url(self):
        self.assertEqual(cq.eli_from_url("https://www.fedlex.admin.ch/eli/cc/1962/1364_1409_1428/fr"),
                         "https://fedlex.data.admin.ch/eli/cc/1962/1364_1409_1428")
        self.assertIsNone(cq.eli_from_url("https://example.invalid/x"))


class EndToEnd(unittest.TestCase):
    def test_ok_cases(self):
        code, rep = run_cli(["rules_ok.yaml"])
        self.assertEqual(code, 0)
        res = by_id(rep)
        for rid in ("T-OK-001", "T-OK-002", "T-OK-003", "T-OK-004"):
            self.assertEqual(res[rid]["status"], "OK", res[rid])
        self.assertEqual(res["T-OK-001"]["artigo_check"], "confirmado")
        self.assertEqual(res["T-OK-002"]["artigo_check"], "confirmado")

    def test_mixed_cases(self):
        code, rep = run_cli(["rules_mixed.yaml"])
        self.assertEqual(code, 1)
        res = by_id(rep)
        self.assertEqual(res["T-FAIL-001"]["status"], "FALHA")
        self.assertEqual(res["T-FAIL-002"]["status"], "FALHA")
        self.assertEqual(res["T-FAIL-002"]["artigo_check"], "divergente")
        self.assertEqual(res["T-EMPTY-001"]["status"], "SEM_TRECHO")
        self.assertEqual(res["T-EMPTY-002"]["status"], "SEM_TRECHO")
        self.assertEqual(res["T-NOART-001"]["status"], "OK")
        self.assertEqual(res["T-NOART-001"]["artigo_check"], "nao_conferido")
        self.assertEqual(res["T-FOOT-001"]["status"], "FALHA")
        self.assertEqual(res["T-SUP-001"]["status"], "OK")
        self.assertEqual(rep["resumo"]["SEM_TRECHO"], 2)

    def test_empty_only_does_not_fail(self):
        code, rep = run_cli([], extra_rules_text="- id: E-1\n  fonte: {rs: '999.01', artigo: '1'}\n  trecho_literal_fr: ''\n")
        self.assertEqual(code, 0)
        self.assertEqual(rep["resumo"]["SEM_TRECHO"], 1)

    def test_missing_law_fails(self):
        txt = "- id: M-1\n  fonte: {rs: '888.88', artigo: '1'}\n  trecho_literal_fr: 'abc'\n"
        code, rep = run_cli([], extra_rules_text=txt)
        self.assertEqual(code, 1)
        self.assertEqual(rep["resumo"]["leis_nao_obtidas"], 1)
        self.assertFalse(rep["leis"]["888.88"]["ok"])

    def test_rules_container_shapes(self):
        txt = "rules:\n  - id: S-1\n    fonte: {rs: '999.01', artigo: '1'}\n    trecho_literal_fr: 'panneau d’essai'\n"
        code, rep = run_cli([], extra_rules_text=txt)
        self.assertEqual(code, 0)
        self.assertEqual(by_id(rep)["S-1"]["status"], "OK")


if __name__ == "__main__":
    unittest.main()
