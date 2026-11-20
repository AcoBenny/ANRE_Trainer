import json
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_p0_source_conditioned_review as review

EVIDENCE = pathlib.Path("docs/ACADEMY_P0_THREE_SOURCED_PHYSICS_CASES_2026_11_20.json")
QUEUE = pathlib.Path("docs/ACADEMY_P0_NEXT_12_EXACT_QABC_2026_11_20.json")

GOOD_TEXT = (
    "A: First option needs physical evidence and model assumptions.\n"
    "B: Second option can be appropriate only with a named convention.\n"
    "C: Third option is analyzed with an explicit counterexample.\n"
    "ASSUMPTIONS: All unit and condition constraints must be respected.\n"
    "COUNTEREXAMPLE: We must keep source conditions unchanged in any test.\n"
    "SOURCE_SCOPE: The source is engineering context only, not examiner scoring.\n"
    "VERDICT: NOT_APPROVED."
)


class P0SourcedEvidenceTests(unittest.TestCase):
    def test_three_evidence_cases_originals_are_identical_to_source_queue(self):
        cases = review.load_cases(EVIDENCE)
        original = {x["unit_id"]: x for x in json.loads(QUEUE.read_text())["cases"]}
        self.assertEqual(tuple(x["unit_id"] for x in cases), review.EXPECTED_IDS)
        for case in cases:
            actual = original[case["unit_id"]]
            self.assertEqual(case["question_original"], actual["question_original"])
            self.assertEqual(case["options_original"],
                             {k: actual[k + "_original"] for k in "ABC"})

    def test_physics_categories_never_equate_distinct_flux_fields(self):
        cases = {x["unit_id"]: x for x in review.load_cases(EVIDENCE)}
        e = cases["QABC-0065"]
        equations = " ".join(e["equations"]).lower()
        self.assertIn("epsilon_0", equations)
        self.assertIn("oint(d dot da)=q_free", equations)
        self.assertIn("units", e["key_uncertainty"])
        self.assertFalse(e.get("learner_approved", False))

    def test_period_direction_and_generator_condition_not_silently_filled(self):
        cases = {x["unit_id"]: x for x in review.load_cases(EVIDENCE)}
        self.assertIn("T_n=T_1/n", cases["QABC-0050"]["equations"])
        self.assertIn("which period is numerator", cases["QABC-0050"]["assumptions_to_check"])
        self.assertIn("which variables held constant", cases["QABC-0036"]["assumptions_to_check"])

    def test_fails_closed_if_sources_or_release_gates_change(self):
        with tempfile.TemporaryDirectory() as td:
            dst = pathlib.Path(td) / "bad.json"
            data = json.loads(EVIDENCE.read_text())
            data["official_ANRE_key_authenticated"] = True
            dst.write_text(json.dumps(data))
            with self.assertRaises(ValueError):
                review.load_cases(dst)
            data["official_ANRE_key_authenticated"] = False
            data["cases"][0]["sources"] = []
            dst.write_text(json.dumps(data))
            with self.assertRaises(ValueError):
                review.load_cases(dst)

    def test_prompt_does_not_leak_expected_letter_or_prior_review(self):
        x = review.load_cases(EVIDENCE)[0]
        x["imported_answer_key"] = "SECRET_A"
        x["previous_reviewer_letter"] = "SECRET_C"
        p = review.compiled_prompt(x)
        self.assertNotIn("SECRET_A", p)
        self.assertNotIn("SECRET_C", p)
        self.assertIn("paraphrased_evidence", p)
        self.assertIn("NO_AUTHENTICATED_ORIGINAL_SCORING_KEY", p)
        self.assertNotIn("key_uncertainty", p)

    def test_markdown_headers_accepted_but_verbatim_options_not_reasoning(self):
        x = review.load_cases(EVIDENCE)[0]
        output = "**A:** " + x["options_original"]["A"] + "\n" + GOOD_TEXT.replace(
            "A: First option needs physical evidence and model assumptions.\n", "")
        qa = review.structural_qa(output, x)
        self.assertTrue(qa["all_fields_present"])
        self.assertIn("A", qa["verbatim_only_options"])
        self.assertFalse(qa["format_ok"])

    def test_dry_run_never_calls_any_provider(self):
        with tempfile.TemporaryDirectory() as td:
            with mock.patch.object(review, "route_agent") as agent:
                res = review.run(["--evidence", str(EVIDENCE), "--out", td])
                agent.assert_not_called()
            self.assertEqual(res, 0)
            report = json.loads((pathlib.Path(td) / "results.json").read_text())
            self.assertEqual(len(report["records"]), 3)
            self.assertEqual(report["actual_api_attempts"], 0)
            self.assertFalse(report["approved_for_learning"])

    def test_two_blind_models_with_source_are_still_not_approved(self):
        models = iter(["openai/gpt-oss-120b", "gemini-3.5-flash-lite"] * 3)
        messages = []
        def fake_agent(system, message, candidates, state):
            messages.append(message)
            state["attempts"] += 1
            state["returned"] += 1
            return {"ok": True, "model": next(models), "provider": candidates[0],
                    "text": GOOD_TEXT, "usage": {"total_tokens": 250}}
        with tempfile.TemporaryDirectory() as td:
            with mock.patch.object(review, "route_agent", side_effect=fake_agent):
                code = review.run(["--evidence", str(EVIDENCE), "--out", td,
                                   "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(code, 0)
            self.assertEqual(len(messages), 6)
            self.assertEqual(messages[0], messages[1])
            report = json.loads((pathlib.Path(td) / "results.json").read_text())
            self.assertEqual(report["successful_role_outputs"], 6)
            self.assertTrue(all(x["model_independence"] for x in report["records"]))
            self.assertTrue(all(not x["approved_for_learning"] for x in report["records"]))

    def test_same_actual_model_and_missing_format_block(self):
        with tempfile.TemporaryDirectory() as td:
            def fake_agent(system, message, candidates, state):
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": "google/gemma-4-31b-it:free",
                        "provider": candidates[0], "text": GOOD_TEXT}
            with mock.patch.object(review, "route_agent", side_effect=fake_agent):
                status = review.run(["--evidence", str(EVIDENCE), "--out", td,
                                     "--mode", "live-free", "--unit", "QABC-0050",
                                     "--confirm", "FREE_ONLY"])
            self.assertEqual(status, 1)
            report = json.loads((pathlib.Path(td) / "results.json").read_text())
            self.assertFalse(report["records"][0]["model_independence"])
            self.assertFalse(report["approved_for_learning"])

    def test_live_requires_explicit_budget_confirmation(self):
        with self.assertRaises(SystemExit):
            review.run(["--evidence", str(EVIDENCE), "--mode", "live-free"])


if __name__ == "__main__":
    unittest.main()
