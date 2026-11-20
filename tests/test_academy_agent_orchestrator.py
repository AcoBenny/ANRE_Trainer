import json
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_agent_orchestrator as academy


def make_queue(folder):
    data = {
        "status": "QUEUE_ONLY_NOT_REVIEWED",
        "official_exam_keys_authenticated": False,
        "release_approved": False,
        "question_or_key_modified": False,
        "source": "V149_568_QABC_FINAL_GATE_PROVENANCE_BIAS_AND_CHALLENGE_2026_11_20.csv",
        "cases": [
            {
                "unit_id": f"QABC-{i:04d}", "grade_ids": f"G1-ELE-{i:03d}|G2-ELEC-{i+100:03d}",
                "source_workbook": "technical.xlsx", "source_row": str(i),
                "question_original": f"Question {i}?",
                "A_original": "option one", "B_original": "option two", "C_original": "option three",
                "learner_approved": False, "historical_key": "SECRET_B",
                "expected_answer": "SECRET_C",
            } for i in range(1, 13)
        ],
    }
    p = folder / "queue.json"
    p.write_text(json.dumps(data), encoding="utf-8")
    return p


FULL_REVIEW = (
    "A: I evaluate option A and clarify the physical conditions. "
    "B: I evaluate option B and address counterexamples in the specified situation. "
    "C: I evaluate option C and consider when it might apply. "
    "The primary source and edition have not been authenticated, so the answer cannot be released."
)


class AcademyOrchestrationTests(unittest.TestCase):

    def test_queue_exact_count_fidelity_and_release_flags(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            self.assertEqual(len(academy.load_queue(p)), 12)
            o = json.loads(p.read_text())
            o["cases"][0]["learner_approved"] = True
            p.write_text(json.dumps(o))
            with self.assertRaises(ValueError):
                academy.load_queue(p)
            o["cases"][0]["learner_approved"] = False
            o["cases"].pop()
            p.write_text(json.dumps(o))
            with self.assertRaises(ValueError):
                academy.load_queue(p)

    def test_prompt_compiler_is_blind_to_legacy_key_and_previous_analysis(self):
        with tempfile.TemporaryDirectory() as d:
            c = academy.load_queue(make_queue(pathlib.Path(d)))[0]
            c["previous_reviewer_answer"] = "SECRET_REVIEWER"
            text = academy.compiled_prompt(c)
            self.assertIn("question", text)
            self.assertIn("option one", text)
            self.assertNotIn("SECRET_B", text)
            self.assertNotIn("SECRET_C", text)
            self.assertNotIn("SECRET_REVIEWER", text)
            self.assertNotIn("historical_key", text)

    def test_risk_selector_adds_linguistic_only_when_needed(self):
        with tempfile.TemporaryDirectory() as d:
            cases = academy.load_queue(make_queue(pathlib.Path(d)))
            self.assertEqual(len(academy.choose_roles(cases[0])), 3)
            self.assertEqual(len(academy.choose_roles(cases[1])), 2)
            self.assertEqual(len(academy.choose_roles(cases[4])), 3)
            self.assertEqual(len(academy.choose_roles(cases[6])), 3)
            self.assertEqual(len(academy.choose_roles(cases[10])), 3)

    def test_unverified_evidence_never_releases_answers(self):
        reviews = {
            "technical_electrical": {"ok": True, "model": "groq/oss", "text": FULL_REVIEW},
            "independent_skeptic": {"ok": True, "model": "gemini/flash", "text": FULL_REVIEW},
        }
        result = academy.quality_gate({}, reviews, list(reviews))
        self.assertFalse(result["learner_approved"])
        self.assertEqual(result["source_authentication"], "NOT_VERIFIED")
        self.assertEqual(result["status"], "MODEL_TRACES_PRESENT_SOURCE_GATE_BLOCKED")
        self.assertTrue(result["independent_model_families_proven"])

    def test_same_model_fallback_is_not_independent(self):
        reviews = {
            "technical_electrical": {"ok": True, "model": "free/one", "text": FULL_REVIEW},
            "independent_skeptic": {"ok": True, "model": "free/one", "text": FULL_REVIEW},
        }
        result = academy.quality_gate({}, reviews, list(reviews))
        self.assertFalse(result["independent_model_families_proven"])
        self.assertEqual(result["status"], "INCOMPLETE_MODEL_TRACES")

    def test_missing_abc_coverage_blocks(self):
        reviews = {
            "technical_electrical": {"ok": True, "model": "oss", "text": "A and B were assessed. " * 15},
            "independent_skeptic": {"ok": True, "model": "flash", "text": FULL_REVIEW},
        }
        result = academy.quality_gate({}, reviews, list(reviews))
        self.assertEqual(result["status"], "INCOMPLETE_MODEL_TRACES")

    def test_dry_run_never_calls_any_api(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            with mock.patch.object(academy, "route_agent") as api:
                self.assertEqual(academy.run(["--queue", str(p), "--out", str(pathlib.Path(d)/"out")]), 0)
                api.assert_not_called()
            o = json.loads((pathlib.Path(d)/"out"/"results.json").read_text())
            self.assertEqual(o["attempted"], 0)
            self.assertFalse(o["learner_approved"])
            self.assertEqual(o["records"][0]["qa_evidence_gate"]["status"], "NOT_RUN")

    def test_live_calls_separate_reviewers_and_writes_unapproved_artifact(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            models = iter(["groq/oss", "gemini/flash", "openrouter/free"] * 4)
            calls = []
            def mock_api(system, message, providers, state):
                calls.append((system, message))
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": next(models), "provider": providers[0],
                        "text": FULL_REVIEW, "usage": {"total_tokens": 100}, "finish_reason": "stop"}
            with mock.patch.object(academy, "route_agent", side_effect=mock_api):
                result = academy.run(["--queue", str(p), "--out", str(pathlib.Path(d)/"out"),
                                      "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 0)
            report = json.loads((pathlib.Path(d)/"out"/"results.json").read_text())
            self.assertEqual(len(report["records"]), 4)
            self.assertTrue(report["proposed_lessons"])
            self.assertTrue(all(l["status"] == "PENDING_VALIDATION_NOT_INSTALLED_AS_SKILL"
                                for l in report["proposed_lessons"]))
            self.assertTrue(all(call[1] == calls[0][1] for call in calls[:3]))
            self.assertTrue(all("SECRET_" not in call[1] for call in calls))
            self.assertEqual(report["paid_openai_calls"], 0)
            self.assertFalse(report["learner_approved"])

    def test_incomplete_role_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            def fail(*args):
                return {"ok": False, "error": "HTTP_429"}
            with mock.patch.object(academy, "route_agent", side_effect=fail):
                result = academy.run(["--queue", str(p), "--out", str(pathlib.Path(d)/"out"),
                                      "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 1)

    def test_invalid_run_without_confirmation(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            with self.assertRaises(SystemExit):
                academy.run(["--queue", str(p), "--mode", "live-free"])


if __name__ == "__main__":
    unittest.main()
