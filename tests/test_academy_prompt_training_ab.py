import json
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_prompt_training_ab as lab
from scripts import academy_full_qabc_review as qabc


def ledger_rows():
    result = []
    for unit in sorted(qabc.EXPECTED_UNITS):
        result.append({
            "unit_id": unit,
            "grade_ids": "G1-NOR-048" if unit == "QABC-0362" else "G1-NOR-072",
            "source_workbook": "original_2023.xlsx", "source_row": "55",
            "evidence_url": "https://legislatie.just.ro/Public/DetaliiDocument/286763",
            "source_stem_from_workbook": "Original source stem",
            "source_A_from_workbook": "Original exclusive A",
            "source_B_from_workbook": "Original B without tool",
            "source_C_from_workbook": "Original C",
            "current_stem_UNCHANGED": "Current altered stem",
            "current_A_UNCHANGED": "Current altered A",
            "current_B_UNCHANGED": "Current B only with tool",
            "current_C_UNCHANGED": "Current C",
        })
    return result


def sources():
    return {
        "QABC-0362": {
            "section": "5.4.13", "pdf_page": 70,
            "text": "Alimentarea transformatorului se face dintr-un circuit de iluminat normal, dintr-un circuit de prize sau direct din tabloul de distribuţie."
        },
        "QABC-0386": {
            "section": "5.5.2.3", "pdf_page": 72,
            "text": "Această conectare trebuie să fie sigură şi deconectabilă numai prin intermediul unei scule."
        },
    }


class AcademyTrainingABTests(unittest.TestCase):
    def test_prompt_is_identical_for_baseline_and_trained_inputs(self):
        row = ledger_rows()[-2]
        row["unit_id"] = "QABC-0362"
        row["candidate_original_NOT_OFFICIAL_KEY"] = "SECRET_A"
        row["canonical_keys_UNCHANGED"] = "SECRET_B"
        row["technical_evidence_or_countermodel"] = "SECRET_RATIONALE"
        prompt = lab.build_blind_case(row, sources()["QABC-0362"])
        self.assertIn("original_workbook", prompt)
        self.assertIn("trainer_current", prompt)
        self.assertIn("2026", prompt)
        self.assertNotIn("SECRET_A", prompt)
        self.assertNotIn("SECRET_B", prompt)
        self.assertNotIn("SECRET_RATIONALE", prompt)

    def test_trained_instruction_constrains_exact_I7_and_incomplete_exam_evidence(self):
        prompt = lab.trained_instruction("skeptic", "electrical scope")
        for essential in ("CONDITIONS", "arithmetic", "scored key", "2026", "A-B", "B-C",
                          "original workbook"):
            self.assertIn(essential.casefold(), prompt.casefold())

    def test_actual_repo_2023_context_has_two_pinned_clauses(self):
        from scripts.academy_source_excerpt_i7_pilot import load_context
        path = pathlib.Path("docs/ACADEMY_NORMATIVE_CONTEXT_I7_2023_TWO_CLAUSES.json")
        source = load_context(path)
        self.assertEqual(set(source), set(lab.SELECTED_IDS))
        self.assertTrue(all(c["pdf_page"] in (70, 72) for c in source.values()))

    def test_transfer_lesson_not_exhaustive_does_not_mean_false(self):
        from scripts.academy_source_excerpt_i7_pilot import load_context
        sources = load_context(pathlib.Path(
            "docs/ACADEMY_NORMATIVE_CONTEXT_I7_2023_TWO_CLAUSES.json"))
        clause = sources["QABC-0362"]["text"]
        self.assertIn("dintr-un circuit de prize", clause)
        self.assertIn("sau", clause)
        original_c = "dintr-un circuit de prize"
        exclusive_c = "numai dintr-un circuit de prize"
        self.assertIn(original_c, clause)
        self.assertFalse(original_c.startswith("numai"))
        self.assertNotEqual(original_c, exclusive_c)
        prompt = lab.trained_instruction("technical", "I7 source")
        self.assertIn("X OR Y OR Z", prompt)
        self.assertIn("nonexclusive", prompt)
        self.assertIn("ONLY Y", prompt)
        self.assertIn("true partial condition", prompt)

    def test_without_tool_is_not_equivalent_to_missing_tool_detail(self):
        from scripts.academy_source_excerpt_i7_pilot import load_context
        sources = load_context(pathlib.Path(
            "docs/ACADEMY_NORMATIVE_CONTEXT_I7_2023_TWO_CLAUSES.json"))
        clause = sources["QABC-0386"]["text"]
        self.assertIn("numai prin intermediul unei scule", clause)
        self.assertIn("deconectat individual", clause)
        prompt = lab.trained_instruction("skeptic", "I7 source")
        self.assertIn("WITHOUT a tool", prompt)
        self.assertIn("ONLY with a tool", prompt)
        self.assertIn("another necessary detail is omitted", prompt)

    def test_dry_run_persists_eight_slots_without_api(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = pathlib.Path(td) / "ledger.csv"
            ledger.write_text("fake", encoding="utf-8")
            context = pathlib.Path(td) / "context.json"
            context.write_text("{}")
            with (mock.patch.object(lab, "load_ledger", return_value=ledger_rows()),
                  mock.patch.object(lab, "load_context", return_value=sources()),
                  mock.patch.object(lab, "route_agent") as api):
                rc = lab.main(["--ledger", str(ledger), "--context", str(context),
                               "--out", str(pathlib.Path(td)/"results")])
                api.assert_not_called()
            self.assertEqual(rc, 0)
            report = json.loads((pathlib.Path(td)/"results"/"results.json").read_text())
            self.assertEqual(len(report["results"]), 8)
            self.assertEqual(report["attempts"], 0)
            self.assertFalse(report["learner_approved"])

    def test_live_baseline_and_trained_have_same_model_family_and_original_input(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = pathlib.Path(td) / "ledger.csv"
            ledger.write_text("fake", encoding="utf-8")
            context = pathlib.Path(td) / "context.json"
            context.write_text("{}")
            calls = []
            def fake_provider(system, message, candidates, state):
                calls.append((system, message, candidates))
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": candidates[0], "provider": candidates[0],
                        "finish_reason": "stop", "usage": {"cost": 0},
                        "text": "A: source original differs, B: tool condition, C: possible."}
            with (mock.patch.object(lab, "load_ledger", return_value=ledger_rows()),
                  mock.patch.object(lab, "load_context", return_value=sources()),
                  mock.patch.object(lab, "route_agent", side_effect=fake_provider)):
                rc = lab.main(["--ledger", str(ledger), "--context", str(context),
                               "--out", str(pathlib.Path(td)/"results"),
                               "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(rc, 0)
            self.assertEqual(len(calls), 8)
            self.assertEqual([x[2] for x in calls[:4]],
                             [("groq",), ("groq",), ("gemini",), ("gemini",)])
            for index in (0, 2, 4, 6):
                self.assertEqual(calls[index][1], calls[index+1][1])
                self.assertEqual(calls[index][2], calls[index+1][2])
            report = json.loads((pathlib.Path(td)/"results"/"results.json").read_text())
            self.assertFalse(report["model_weights_changed"])
            self.assertFalse(report["official_2026_source_validated"])
            self.assertFalse(report["learner_approved"])

    def test_mismatched_or_missing_case_is_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = pathlib.Path(td) / "ledger.csv"
            ledger.write_text("fake")
            ctx = pathlib.Path(td) / "ctx.json"
            ctx.write_text("{}")
            with (mock.patch.object(lab, "load_ledger", return_value=ledger_rows()),
                  mock.patch.object(lab, "load_context", return_value={"QABC-0362": sources()["QABC-0362"]}),
                  mock.patch.object(lab, "route_agent") as fn):
                with self.assertRaises(ValueError):
                    lab.main(["--ledger", str(ledger), "--context", str(ctx)])
                fn.assert_not_called()

    def test_live_requires_explicit_confirmation(self):
        with tempfile.TemporaryDirectory() as td:
            ledger = pathlib.Path(td) / "ledger.csv"
            ledger.write_text("fake")
            ctx = pathlib.Path(td) / "ctx.json"
            ctx.write_text("{}")
            with mock.patch.object(lab, "route_agent") as fn:
                with self.assertRaises(SystemExit):
                    lab.main(["--ledger", str(ledger), "--context", str(ctx), "--mode", "live-free"])
                fn.assert_not_called()


if __name__ == "__main__":
    unittest.main()
