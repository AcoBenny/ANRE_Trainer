# CKPT-273 | P0 Academy execution recovery after provider timeout | 2026-11-20

## Measured execution, distinguish partial from complete
- [First P0 run 44757996875](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44757996875): QABC-0013, 0019, 0025 each received real Groq technical + Gemini skeptic outputs, QABC-0024 never sent (source image required). **10 total API attempts / 6 nonempty outputs / 1 source figure blocked / 1 linguistic role failed**. Mark no approvals. [CKPT-271](CKPT_271_ACADEMY_P0_FIRST_COHORT_2026_11_20.md).
- [First remaining-eight run 44759657761](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44759657761): job **cancelled on 10-minute timeout**. Recovered real [partial artifact](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44759657761) from `academy-p0-remaining-eight-source-gated`, with **13 API attempts / 3 successful reviewer outputs** and 2 partial QABC records. QABC-0036 technical Groq and linguistic OpenRouter had outputs, independent Gemini skeptic was unavailable after 5 fallbacks. QABC-0042 technical Groq had output, skeptic was unavailable after 5 fallbacks. No 0050/0065/0069/0080/0091/0096 record was produced in that run. Do **not** count unanswered cases or timeouts as completed QA.
- A later `[academy-p0]` run [44761592780](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44761592780), started while recovery work progressed, must be checked for actual per-QABC completeness before re-requesting any case; do not double count or lose any artifact.

## Implemented bounded recovery
- The P0 agent reviewer now accepts `--only-unit QABC-NNNN` and optional `--only-role technical_electrical|independent_skeptic|linguistic_scope` for an **exact** case, so a failed reviewer can be retried without repeating other successful independent outputs.
- For new P0 requests, free fallback chain is **maximum two provider candidates per role**: original role primary (Groq, Gemini or OpenRouter) then allowlisted, cost-checked Requesty Gemma (if configured). This avoids the observed serial five x 25-second timeout cascade. A successful single-role retry is labelled `ROLE_RETEST_PRESENT_NOT_RECONCILED` and **not** accepted as cross-model QA without original saved traces.
- Added negative regression tests for maximum two providers, no other question replay, role-only reconciliation, and source-figure blocking. Keep full A/B/C source text and hash unchanged.
- Source-evidence [CKPT-272](CKPT_272_ACADEMY_P0_TECHNICAL_SOURCE_SCOPE_2026_11_20.md) points to separately researched physics materials for key ambiguous P0 cases; **these sources were not automatically supplied to previous model requests**, so do not pretend those responses are source-grounded.
- Original ELE028 drawing remains **already recovered** in original workbook according to prior CKPT-255, but not yet attached to current model prompt. Stop on image dependency, never infer its topology anew.
- Any missing user/official 2026 source text, legal scope, edition, professional review and scored key remains `NOT_VERIFIED`. **0 learner approvals, zero changes to canonical keys/HTML/APK/main**.

## Next exact continuation
1. Inspect newest partial run artifacts for 44761592780 before scheduling more calls; separate completed and missing review roles per QABC.
2. Run per-unit jobs in isolated bounded API attempt windows for only unstarted cases or missing roles. Do not restart first four.
3. Reconcile exact source paragraphs, surrounding context, technical A/B/C and source-free vs induction or flux E/D definition, then obtain independent qualified QA before any learner approval or merge/release.

Project state: PR #13 Draft, audit PR #7 Draft. Source V149 and 822-ID mapping intact. This document is an evidence checkpoint, not closure of all remaining questions.
