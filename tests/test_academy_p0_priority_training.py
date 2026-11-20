import json
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_p0_priority_training as p0


def make_queue(folder):
    cases = []
    for uid in p0.EXPECTED_IDS:
        cases.append({
            "unit_id": uid,
            "grade_ids": "G1-ELE-014|G2-ELEC-166",
            "source_workbook": "original.xlsx",
            "source_row": "20",
            "question_original": "Condensatoare: numai atunci când este permis?",
            "A_original": "Opțiune A",
            "B_original": "Opțiune B",
            "C_original": "Opțiune C",
            "priority": "P0",
            "source_fidelity": "SOURCE_EXACT_TEXT_MATCH_LIBRARY_COPY",
            "requires_figure": uid == "QABC-0024",
            "source_paragraph_verified": False,
            "exam_key_proven": False,
            "learner_approved": False,
            "old_imported_key": "SECRET_C",
        })
    obj = {
        "schema": "academy_priority_v1",
        "source_git_blob": p0.EXPECTED_V149_BLOB,
        "status": "QUEUE_ONLY_NOT_REVIEWED",
        "official_exam_keys_authenticated": False,
        "release_approved": False,
        "question_or_key_modified": False,
        "cases": cases,
    }
    path = folder / "p0.json"
    path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    return path


FORMATTED = (
    "A: I assess first alternative independently and look for countermodels. "
    "\nB: I assess second alternative independently with physical evidence. "
    "\nC: I assess third alternative independently with physical evidence. "
    "\nPAIRS: A-B differs from A-C and B-C in the stated domain. "
    "\nCONDITIONS: I must respect all original stem limits. "
    "\nEVIDENCE_MISSING: Need current authoritative exact-source passage and version. "
    "\nVERDICT: NOT_APPROVED."
)


class PriorityAcademyTests(unittest.TestCase):
    def test_exact_original_queue_contract(self):
        with tempfile.TemporaryDirectory() as td:
            path = make_queue(pathlib.Path(td))
            self.assertEqual(len(p0.load_priority_queue(path)), 12)
            obj = json.loads(path.read_text())
            obj["cases"][2]["requires_figure"] = False
            path.write_text(json.dumps(obj))
            with self.assertRaisesRegex(ValueError, "figure"):
                p0.load_priority_queue(path)

    def test_legacy_key_and_risk_not_leaked_into_prompt(self):
        with tempfile.TemporaryDirectory() as td:
            path = make_queue(pathlib.Path(td))
            case = p0.load_priority_queue(path)[0]
            payload = p0.prompt_data(case)
            self.assertIn("Opțiune A", payload)
            self.assertNotIn("SECRET_C", payload)
            self.assertNotIn("old_imported_key", payload)
            self.assertNotIn("source_paragraph_verified", payload)
            self.assertNotIn("priority", payload)

    def test_risk_selector_includes_linguistic_when_only(self):
        with tempfile.TemporaryDirectory() as td:
            case = p0.load_priority_queue(make_queue(pathlib.Path(td)))[0]
            roles = p0.role_plan(case)
            self.assertEqual(len(roles), 3)
            case["question_original"] = "Ce este curentul?"
            self.assertEqual(len(p0.role_plan(case)), 2)

    def test_option_only_absolute_word_routes_to_linguistic_reviewer(self):
        with tempfile.TemporaryDirectory() as td:
            case = p0.load_priority_queue(make_queue(pathlib.Path(td)))[0]
            case["question_original"] = "Câmp fără surse este"
            case["A_original"] = "numai o categorie specială"
            case["B_original"] = "un câmp electric"
            case["C_original"] = "un câmp magnetic"
            self.assertEqual(len(p0.role_plan(case)), 3)
            case["A_original"] = "o categorie specială"
            self.assertEqual(len(p0.role_plan(case)), 2)

    def test_training_prompt_covers_source_scope_and_error_patterns(self):
        t = p0.TRAINING_RULES
        for word in ("Counterexamples", "arithmetic", "abbreviations",
                     "A-B", "B-C", "EVIDENCE_MISSING", "NOT_APPROVED"):
            self.assertIn(word.casefold(), t.casefold())
        self.assertIn("not updating model weights", p0.__doc__)

    def test_past_i7_false_exclusivity_and_outside_standard_lessons_are_reused(self):
        rule = p0.TRAINING_RULES
        self.assertIn("missing ONLY/numai quantifier", rule)
        self.assertIn("nonexclusive in the PAIRS section", rule)
        self.assertIn("positive evidence for that condition", rule)
        self.assertIn("unrelated physical experiments", rule)
        self.assertIn("WITHOUT a tool", rule)
        self.assertIn("ONLY with a tool", rule)

    def test_structured_review_not_falsely_implied_by_abc_mentions(self):
        self.assertFalse(p0.check_reviewer_text("A, B, C all exist")["all_required_fields"])
        self.assertFalse(p0.check_reviewer_text("A: Yes\nB: No\nC: Maybe")["all_required_fields"])
        self.assertTrue(p0.check_reviewer_text(FORMATTED)["all_required_fields"])

    def test_markdown_bold_headings_do_not_hide_copied_original_options(self):
        with tempfile.TemporaryDirectory() as td:
            case = p0.load_priority_queue(make_queue(pathlib.Path(td)))[0]
            output = (
                "**A:** Opțiune A\n**B:** Opțiune B\n**C:** Opțiune C\n"
                "**PAIRS:** Reviewed logical pairs.\n"
                "**CONDITIONS:** Source context unknown.\n"
                "**EVIDENCE_MISSING:** Need scoped source.\n"
                "**VERDICT:** NOT_APPROVED."
            )
            result = p0.check_reviewer_text(output, case)
            self.assertTrue(all(result["labels"].values()))
            self.assertTrue(all(result["extra_fields"].values()))
            self.assertEqual(result["option_copied_without_assessment"], ["A", "B", "C"])
            self.assertFalse(result["all_required_fields"])

    def test_a_b_c_copied_only_is_not_a_review(self):
        with tempfile.TemporaryDirectory() as td:
            case = p0.load_priority_queue(make_queue(pathlib.Path(td)))[0]
            repeated = ("A: Opțiune A\nB: Opțiune B\nC: Opțiune C\n"
                        "PAIRS: Could be different.\nCONDITIONS: Unknown.\n"
                        "EVIDENCE_MISSING: Source.\nVERDICT: NOT_APPROVED.")
            result = p0.check_reviewer_text(repeated, case)
            self.assertEqual(result["option_copied_without_assessment"], ["A", "B", "C"])
            self.assertFalse(result["all_required_fields"])
            self.assertTrue(p0.check_reviewer_text(FORMATTED, case)["all_required_fields"])

    def test_dry_run_makes_no_api_calls_and_blocks_figure(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            q = make_queue(folder)
            with mock.patch.object(p0, "route_agent") as api:
                status = p0.main(["--queue", str(q), "--out", str(folder / "out")])
            self.assertEqual(status, 0)
            api.assert_not_called()
            obj = json.loads((folder / "out" / "results.json").read_text())
            self.assertFalse(obj["learner_approved"])
            self.assertEqual(obj["figure_blockers"], 1)
            self.assertEqual(obj["records"][2]["gate"], "BLOCKED_FIGURE_MISSING_NO_MODEL_CALLS")
            self.assertEqual(obj["attempts"], 0)

    def test_live_calls_only_three_source_visible_questions_in_first_cohort(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            queue = make_queue(folder)
            calls = []
            def fake_route(system, message, candidates, state):
                calls.append(json.loads(message)["unit_id"])
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": candidates[0], "provider": candidates[0],
                        "text": FORMATTED, "usage": {"total_tokens": 24},
                        "finish_reason": "stop"}
            with mock.patch.object(p0, "route_agent", side_effect=fake_route):
                result = p0.main(["--queue", str(queue), "--out", str(folder / "out"),
                                  "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 0)
            obj = json.loads((folder / "out" / "results.json").read_text())
            self.assertEqual(len(obj["records"]), 4)
            self.assertNotIn("QABC-0024", calls)
            self.assertEqual(len(set(calls)), 3)
            self.assertEqual(obj["figure_blockers"], 1)
            self.assertFalse(obj["learner_approved"])
            self.assertTrue(all(x["gate"] != "APPROVED" for x in obj["records"]))

    def test_missing_structured_fields_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            q = make_queue(folder)
            def poorly_formatted(system, message, candidates, state):
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": candidates[0],
                        "text": "A, B, and C might all matter. " * 10}
            with mock.patch.object(p0, "route_agent", side_effect=poorly_formatted):
                code = p0.main(["--queue", str(q), "--out", str(folder / "out"),
                                "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(code, 1)
            obj = json.loads((folder / "out" / "results.json").read_text())
            self.assertTrue(any("TRAINING_FORMAT" in x["gate"] for x in obj["records"]))
            self.assertFalse(obj["learner_approved"])

    def test_semantic_warning_must_fail_closed_even_when_format_is_correct(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            q = make_queue(folder)
            def suspicious_response(system, message, candidates, state):
                state["attempts"] += 1
                state["returned"] += 1
                return {
                    "ok": True,
                    "model": candidates[0],
                    "provider": candidates[0],
                    "text": FORMATTED + " AAR means Auto-Reclosing, not reserve transfer.",
                    "finish_reason": "stop",
                }
            from scripts import academy_agent_orchestrator as core
            with mock.patch.object(p0, "route_agent", side_effect=suspicious_response):
                with mock.patch.object(p0, "quality_gate", wraps=core.quality_gate) as qa:
                    # QABC-0013..0025 contain no QABC-0006; inject a real
                    # content warning only to exercise status-propagation logic.
                    original = core.quality_gate
                    def flagged(case, reviews, names):
                        result = original(case, reviews, names)
                        result["status"] = "CONTENT_WARNING_SOURCE_GATE_BLOCKED"
                        return result
                    qa.side_effect = flagged
                    result = p0.main(["--queue", str(q),
                                      "--out", str(folder / "out"),
                                      "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 1)
            report = json.loads((folder / "out" / "results.json").read_text())
            self.assertFalse(report["learner_approved"])

    def test_groq_linguistic_requests_low_reasoning_effort(self):
        from scripts import academy_free_router as router
        import os
        response = {
            "model": "openai/gpt-oss-20b",
            "choices": [{"finish_reason": "stop",
                         "message": {"content": "A: no; B: yes; C: no"}}],
            "usage": {"total_tokens": 45},
        }
        with mock.patch.dict(os.environ, {"GROQ_API_KEY": "synthetic-secret"}):
            with mock.patch.object(router, "post_json", return_value=response) as fn:
                result = router.call_provider("groq_linguistic", "review", "sample")
        self.assertIn("A:", result["text"])
        self.assertEqual(fn.call_args.args[2]["reasoning_effort"], "low")
        self.assertEqual(fn.call_args.args[2]["model"], "openai/gpt-oss-20b")

    def test_groq_20b_independent_linguistic_fallback_is_bounded(self):
        from scripts import academy_agent_orchestrator as orch
        from scripts import academy_free_router as router
        language = next(x for x in orch.SPECIALISTS if x[0] == "linguistic_scope")
        technical = next(x for x in orch.SPECIALISTS if x[0] == "technical_electrical")
        self.assertEqual(language[1][0], "groq_linguistic")
        self.assertEqual(p0.bounded_provider_candidates(language[1]),
                         ("groq_linguistic", "requesty_gemma"))
        self.assertEqual(router.KEYS["groq_linguistic"], "GROQ_API_KEY")
        self.assertEqual(router.MODELS["groq_linguistic"], "openai/gpt-oss-20b")
        self.assertNotEqual(router.MODELS["groq_linguistic"],
                            router.MODELS[technical[1][0]])

    def test_same_fallback_model_cannot_count_independent(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            q = make_queue(folder)
            def same_model(system, message, candidates, state):
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": "google/gemma-4-31b-it",
                        "text": FORMATTED}
            with mock.patch.object(p0, "route_agent", side_effect=same_model):
                code = p0.main(["--queue", str(q), "--out", str(folder / "out"),
                                "--mode", "live-free", "--confirm", "FREE_ONLY"])
            self.assertEqual(code, 1)

    def test_bounded_free_routing_avoids_five_sequential_provider_timeouts(self):
        self.assertEqual(p0.bounded_provider_candidates(
            ("gemini", "openrouter", "openrouter_fixed", "requesty_gemma", "requesty_lightning")
        ), ("gemini", "requesty_gemma"))
        self.assertEqual(p0.bounded_provider_candidates(
            ("openrouter", "openrouter_fixed", "requesty_gemma", "requesty_lightning")
        ), ("openrouter", "requesty_gemma"))
        self.assertEqual(p0.bounded_provider_candidates(("groq",)), ("groq",))
        self.assertTrue(all(len(p0.bounded_provider_candidates(x[1])) <= 2
                            for x in p0.SPECIALISTS))

    def test_exact_single_unit_is_not_a_full_batch(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            queue = make_queue(folder)
            with mock.patch.object(p0, "route_agent") as api:
                code = p0.main(["--queue", str(queue), "--out", str(folder / "out"),
                                "--only-unit", "QABC-0050", "--mode", "dry-run"])
                api.assert_not_called()
            self.assertEqual(code, 0)
            d = json.loads((folder / "out" / "results.json").read_text())
            self.assertEqual([x["unit_id"] for x in d["records"]], ["QABC-0050"])
            self.assertEqual(d["attempts"], 0)

    def test_failed_role_only_retest_cannot_certify_independence(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            queue = make_queue(folder)
            state_capture = []
            def one_role(system, message, candidates, state):
                state_capture.append(candidates)
                state["attempts"] += 1
                state["returned"] += 1
                return {"ok": True, "model": "gemini-3.5-flash-lite",
                        "provider": candidates[0], "text": FORMATTED,
                        "finish_reason": "stop", "usage": {}}
            with mock.patch.object(p0, "route_agent", side_effect=one_role):
                code = p0.main(["--queue", str(queue), "--out", str(folder / "out"),
                                "--mode", "live-free", "--only-unit", "QABC-0042",
                                "--only-role", "independent_skeptic", "--confirm", "FREE_ONLY"])
            d = json.loads((folder / "out" / "results.json").read_text())
            self.assertEqual(code, 0)
            self.assertEqual(d["attempts"], 1)
            self.assertEqual(d["records"][0]["roles_selected"], ["independent_skeptic"])
            self.assertEqual(d["records"][0]["gate"], "ROLE_RETEST_PRESENT_NOT_RECONCILED")
            self.assertFalse(d["records"][0]["qa"]["independent_model_families_proven"])
            self.assertTrue(d["records"][0]["qa"]["requires_prior_artifact_reconciliation"])
            self.assertFalse(d["learner_approved"])
            self.assertEqual(state_capture[0], ("gemini", "requesty_gemma"))

    def test_only_role_requires_exact_unit(self):
        with tempfile.TemporaryDirectory() as td:
            folder=pathlib.Path(td)
            q=make_queue(folder)
            with self.assertRaises(SystemExit):
                p0.main(["--queue",str(q),"--only-role","independent_skeptic"])
            with self.assertRaises(SystemExit):
                p0.main(["--queue",str(q),"--only-unit","QABC-0036",
                         "--only-role","unknown_reviewer"])

    def test_unconfirmed_live_run_does_not_call_providers(self):
        with tempfile.TemporaryDirectory() as td:
            folder = pathlib.Path(td)
            q = make_queue(folder)
            with mock.patch.object(p0, "route_agent") as api:
                with self.assertRaises(SystemExit):
                    p0.main(["--queue", str(q), "--mode", "live-free"])
                api.assert_not_called()


if __name__ == "__main__":
    unittest.main()
