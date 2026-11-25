# CKPT-276 | ANRE P0 targeted six missing specialist roles | 2026-11-20

## Why this lot exists
- Source-immutable P0 original questions and grades from pinned [V149](https://github.com/AcoBenny/ANRE_Trainer/blob/audit/anre-v8-priority-17-20261109/docs/QUESTION_AUDIT/V149_568_QABC_FINAL_GATE_PROVENANCE_BIAS_AND_CHALLENGE_2026_11_20.csv); full preserved result matrix in [CKPT-274](CKPT_274_P0_EIGHT_REAL_API_REPORTS_AND_6_ROLE_RETEST_QUEUE_2026_11_20.md).
- [44761592780](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44761592780): 8 questions, 37 attempted free provider calls, 16 returning substantive reviewer output, 3 original QABC with all roles complete on a **structural** level (0036, 0042, 0069); other five have missing roles or the copied-only A/B/C warning. These results are *not* independently validated scored keys.
- A separately executed retest [44763821572](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44763821572): exactly QABC-0065 linguistic role, 1 call, real `openai/gpt-oss-20b` through Groq, all A/B/C and review sections filled, `ROLE_RETEST_PRESENT_NOT_RECONCILED`. **No automatic learner approval**.
- Original P0 first cohort has an additional previously incomplete QABC-0025 linguistic role. QABC-0024 source figure remains blocked until recovered workbook OOXML drawing is attached and authenticated.

## Exact next six role-only requests
1. QABC-0050: independent_skeptic (prior Gemini 503 and free gateway quota errors).
2. QABC-0050: linguistic_scope (prior free gateway quota errors).
3. QABC-0080: independent_skeptic (prior answer copied all A/B/C verbatim with no reasoning; need substantive retest).
4. QABC-0091: linguistic_scope (prior free gateway quota errors).
5. QABC-0096: linguistic_scope (prior free gateway quota errors).
6. QABC-0025: linguistic_scope (prior first-cohort free gateway quota errors).

## Execution contract
- Explicit `[p0-roles]` trigger, max two free candidate models per role, original successful responses not replayed.
- Linguistic primary: Groq GPT-OSS 20B (distinct base model from Groq technical 120B and Gemini skeptic); independent skeptic primary Gemini 3.5 Flash Lite. Requesty Gemma is last fallback only. Paid OpenAI API not injected.
- Output artifacts contain model traces and usage but **not qualified human signoff**. Model diversity checked across original and retest role outputs during subsequent reconciliation.
- Flag original ambiguous physics, missing official ANRE scored keys, source edition and contextual paragraph. No source-specific answer allowed for learning yet.
- No question/answer-key/HTML/APK/main writes, PR #13 and audit PR #7 stay Draft. Failure of an API or structured review must save that unit's partial results, not erase other roles.

This checkpoint launches just the six role-specific calls; expect up to 12 provider attempts, not a complete rerun of 12 ANRE questions.
