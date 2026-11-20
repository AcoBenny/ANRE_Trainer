# CKPT-280 | P0 source-conditioned API review: three cases, exact failed roles and source-logic training | 2026-11-20

## Verified first real blind review
- [GitHub Actions 44771173694](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44771173694). Pinned external physics evidence pack `66a3fe0f35694fda732a177214b55f328da5849d` and pinned original workbook queue `db189edd918f5f780bb0ea75192b391deb165723` both checked in GitHub Actions.
- All **10/10 offline tests passed**, no evidence drift. Live API phase: **7 free-model API attempts, 3 substantive model responses**, with fail-closed workflow and expiring artifact `academy-p0-three-sourced-original-qabc`, ID `14647426681`.
- QABC-0036: original technical `groq` returned `INCOMPLETE_OR_BLOCKED_LENGTH` (its 1,400 output-token cap before correction); independent Gemini 3.5 Flash-Lite answered. Gemini's rejection of A/B/C is conditional on balanced sinusoidal 3-phase and holding powers fixed; do not universalize it to all generator loading regimes.
- QABC-0050: original technical `groq` `INCOMPLETE_OR_BLOCKED_LENGTH`; independent Gemini 3.5 Flash-Lite answered. It noted period ratio direction but erroneously treated existence of third harmonic (`1/3`) as a refutation of the second-harmonic sufficiency case (`1/2`); a specific true case need not cover *every* harmonic. The original A/B/C still need explicit semantic adjudication.
- QABC-0065: Groq GPT-OSS 120B answered; Gemini HTTP_503 then free Requesty Gemma network timeout. Groq correctly distinguished `∮E·dA=q/ε0` from `∮D·dA=q_free` but a later sentence described q as unsupported by either source. **Self-contradiction; not a valid scored-key finding**.
- Complete outputs remain in the archived artifact; this checkpoint is a factual summary, not a substitute for the raw traces.

## Prompt training and safety deltas
- Preserved earlier answers, no full-cases rerun. `scripts/academy_p0_source_conditioned_review.py` now supports `--unit` and `--only-role`; model artifact status `ONE_ROLE_RETEST_PRESENT_NOT_RECONCILED` never claims independent signoff.
- Explicit prompt v2 rules from **real** errors:
  1. Distinguish *necessary* vs *sufficient* conditions; `T_n/T_1=1/2` is one valid special harmonic, not a complete list.
  2. If source supports D flux = q_free, never conclude no source supports q; distinguish E, D and their SI units.
  3. State what is held constant when deriving generator current from powers and voltage; a conditional relation is not universal.
- Groq GPT-OSS 120B `reasoning_effort=low` and output token budget 1,800, documented at https://console.groq.com/docs/reasoning; this is an attempt to prevent overthinking truncation, not a guarantee.
- New source-identity, source-scope, preserved-key, two independent models, same-model fallback, focused retry and necessary/sufficient instruction tests in `tests/test_academy_p0_source_conditioned_review.py`.

## Exactly scoped next execution
- This explicit `[p0-source-retry]` commit triggers only missing roles: **QABC-0036 technical**, **QABC-0050 technical**, **QABC-0065 skeptic**. At most 6 free API attempts (primary then pinned Requesty Gemma), no repeated completed roles, separate artifacts for each.
- Previous successful outputs must be reconciled independently against new responses and exact cited public equations. Output format and model disagreement alone are NOT scored-key validation.
- The official ANRE site lists `ELECTROTEHNICA-09.2024-2.xlsx`, but official XLSX binary-cell comparison was not possible in this session; the 2023 official bibliography lists specialist electrotechnics texts, not scored solutions. No definitive 2026 answer key authenticated.

## Release gates
- 0 new student-learning approvals; no changes to original question text, keys, HTML, APK, source question-bank documents or main. PR #13 and audit PR #7 remain Draft. No merge or release without approval.
