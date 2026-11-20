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

    def test_same_model_different_gateway_is_not_independent(self):
        same = {
            "technical_electrical": {
                "ok": True, "model": "google/gemma-4-31b-it:free",
                "text": FULL_REVIEW,
            },
            "independent_skeptic": {
                "ok": True, "model": "requesty/google/gemma-4-31b-it",
                "text": FULL_REVIEW,
            },
        }
        self.assertEqual(academy.normalized_model_family(
            "google/gemma-4-31b-it:free"),
            academy.normalized_model_family("requesty/google/gemma-4-31b-it"))
        gate = academy.quality_gate({"unit_id": "QABC-0001"}, same, list(same))
        self.assertFalse(gate["independent_model_families_proven"])
        self.assertEqual(gate["status"], "INCOMPLETE_MODEL_TRACES")

    def test_requesty_fallback_is_available_to_all_adaptive_roles(self):
        for role, providers, system in academy.SPECIALISTS:
            self.assertEqual(providers[-2:], ("requesty_gemma", "requesty_lightning"))
            self.assertNotIn("openai", providers)

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

    def test_focused_retest_replays_only_failed_unit_and_role(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            calls = []
            def mock_api(system, message, providers, state):
                calls.append((system, message))
                state["attempts"] += 1
                state["returned"] += 1
                output = ("Only B is discussed, other options remain unspecified. " * 4
                          if len(calls) == 1 else FULL_REVIEW)
                return {"ok": True, "model": "gemini/flash", "text": output,
                        "provider": providers[0], "finish_reason": "stop"}
            with mock.patch.object(academy, "route_agent", side_effect=mock_api):
                code = academy.run(["--queue", str(p), "--out", str(pathlib.Path(d)/"retry"),
                                    "--mode", "live-free", "--only-unit", "QABC-0004",
                                    "--only-role", "independent_skeptic", "--confirm", "FREE_ONLY"])
            self.assertEqual(code, 0)
            self.assertEqual(len(calls), 2)
            self.assertEqual(calls[0][1], calls[1][1])
            report = json.loads((pathlib.Path(d)/"retry"/"results.json").read_text())
            self.assertEqual(report["only_unit"], "QABC-0004")
            self.assertEqual(report["only_role"], "independent_skeptic")
            self.assertEqual(len(report["records"]), 1)
            self.assertEqual(report["records"][0]["agent_selection"], ["independent_skeptic"])
            self.assertEqual(report["records"][0]["role_retests"][0]["role"], "independent_skeptic")
            self.assertEqual(report["records"][0]["qa_evidence_gate"]["status"],
                             "ROLE_RETEST_PRESENT_NOT_RECONCILED")
            self.assertFalse(report["records"][0]["qa_evidence_gate"]["independent_model_families_proven"])
            self.assertFalse(report["learner_approved"])

    def test_known_model_hallucinations_become_review_flags_not_source_proof(self):
        psi = {
            "technical_electrical": {
                "ok": True, "model": "oss",
                "text": FULL_REVIEW + " PSI (Presiune, Securitate, Izolație).",
            },
            "independent_skeptic": {"ok": True, "model": "flash", "text": FULL_REVIEW},
        }
        flags = academy.known_semantic_risk_flags("QABC-0002", psi)
        self.assertEqual(flags[0]["risk"], "POSSIBLE_PSI_ACRONYM_HALLUCINATION")
        qa = academy.quality_gate({"unit_id": "QABC-0002"}, psi, list(psi))
        self.assertEqual(qa["status"], "CONTENT_WARNING_SOURCE_GATE_BLOCKED")
        self.assertFalse(qa["learner_approved"])
        numeric = {
            "independent_skeptic": {
                "ok": True, "model": "flash",
                "text": FULL_REVIEW + " Totuși, nicio variantă nu corespunde corect acestei sume.",
            }
        }
        numeric_flags = academy.known_semantic_risk_flags("QABC-0004", numeric)
        self.assertEqual(numeric_flags[0]["risk"], "POSSIBLE_NUMERIC_SELF_CONTRADICTION")
        self.assertFalse(academy.quality_gate({"unit_id": "QABC-0004"},
                                               numeric, list(numeric))["learner_approved"])
        self.assertEqual(academy.known_semantic_risk_flags(
            "QABC-0004", {"technical": {"ok": True, "text": FULL_REVIEW}}), [])

    def test_other_actual_model_failure_modes_are_preserved(self):
        bad = {
            "technical_electrical": {
                "ok": True, "model": "groq/oss", "text": FULL_REVIEW
            }
        }
        examples = [
            ("QABC-0005", " N = 3 nodes and L = 3 branches.", "POSSIBLE_INVALID_COUNTEREXAMPLE"),
            ("QABC-0006", " AAR means Auto-Reclosing.", "POSSIBLE_AAR_RAR_CONFUSION"),
            ("QABC-0007", " At s = 0 there is a scurt-circuit.", "POSSIBLE_ZERO_SLIP_MISINTERPRETATION"),
        ]
        for unit, phrase, expected in examples:
            bad["technical_electrical"]["text"] = FULL_REVIEW + phrase
            flags = academy.known_semantic_risk_flags(unit, bad)
            self.assertEqual(flags[0]["risk"], expected)
            self.assertFalse(academy.quality_gate(
                {"unit_id": unit}, bad, ["technical_electrical"])["learner_approved"])

    def test_focused_retest_with_semantic_warning_returns_failure(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            bad = FULL_REVIEW + " Totuși, nicio variantă nu corespunde corect sumei."
            def mock_api(system, message, providers, state):
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": "gemini/flash", "text": bad}
            with mock.patch.object(academy, "route_agent", side_effect=mock_api):
                code = academy.run(["--queue", str(p), "--out", str(pathlib.Path(d)/"bad"),
                                    "--mode", "live-free", "--only-unit", "QABC-0004",
                                    "--only-role", "independent_skeptic", "--confirm", "FREE_ONLY"])
            self.assertEqual(code, 1)
            report = json.loads((pathlib.Path(d)/"bad"/"results.json").read_text())
            self.assertEqual(report["records"][0]["qa_evidence_gate"]["status"],
                             "ROLE_RETEST_CONTENT_WARNING_NOT_RECONCILED")
            self.assertFalse(report["learner_approved"])

    def test_invalid_run_without_confirmation(self):
        with tempfile.TemporaryDirectory() as d:
            p = make_queue(pathlib.Path(d))
            with self.assertRaises(SystemExit):
                academy.run(["--queue", str(p), "--mode", "live-free"])


if __name__ == "__main__":
    unittest.main()
