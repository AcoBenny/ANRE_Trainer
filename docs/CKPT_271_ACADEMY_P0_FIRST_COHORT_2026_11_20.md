# CKPT-271 | P0 first cohort: real agents, bounded failures, provenance | 2026-11-20

## Inputs checked directly
- Original exact source-copy V149 registry Git blob `ee2ac5536c78eb06a0461243be34c117e257188f`; approved learning: **NO** for all cases.
- P0 queue `docs/ACADEMY_P0_NEXT_12_EXACT_QABC_2026_11_20.json` Git blob `db189edd918f5f780bb0ea75192b391deb165723`.
- Prior technical evidence [CKPT-184](https://github.com/AcoBenny/ANRE_Trainer/blob/audit/anre-v8-priority-17-20261109/docs/QUESTION_AUDIT/CKPT_184_BLOCKED_ELECTROTECHNICS_7_TERMS_MATH_CONTEXT_2026_11_17.md) re-opened, including QABC-0013/0025. Do not count this prior single-assistant audit as independently executed Academy calls.
- Original QABC-0024 ELE028 drawing already recovered as **22 OOXML shapes** in [CKPT-255](https://github.com/AcoBenny/ANRE_Trainer/blob/audit/anre-v8-priority-17-20261109/docs/QUESTION_AUDIT/CKPT_255_GFR_OFFICIAL_SAMPLE_COPY_PROVENANCE_664_5_153_ELE028_FIGURE_2026_11_19.md). The image is missing from the *new model input queue*, NOT necessarily from original Excel. Do not invent a diagram.

## Actual first-P0 API execution
- GitHub Actions [run 44757996875](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44757996875). **4 P0 QABC encountered; 3 text cases sent; 1 original figure-dependent case blocked before any model call.**
- **10 real free-provider attempts; 6 successful, nonempty model outputs**: Groq specialist and Gemini skeptic returned for each of QABC-0013, 0019, 0025. The extra linguistic reviewer on QABC-0025 failed due OpenRouter empty answer/429 and Requesty timeout/429. Runner correctly exited failure with preserved partial evidence. The successful responses are preliminary, **not** source/SME certified or learner approved.
- `QABC-0013`: technical source-free field ambiguity (magnetic divergence vs exact Romanian phrase `câmp de inducţie electromagnetică`). Previous CKPT-184 already blocked unique answer until course-specific original definition.
- `QABC-0019`: technical model put original A/B/C wording in its A:/B:/C: lines without separate analysis, but naive structure check originally accepted it; added regression to **reject copied-only option lines** and preserve a false-positive example. No exact specialized GIS source authenticated.
- `QABC-0025`: Groq treated Faraday induction as universal source of alternating current, neglecting electronic inverters; Gemini called out model scope. Original stem includes `numai`: counterexample needs careful distinction between generating current directly and DC-to-AC conversion. Prior CKPT-184 source links a US DOE inverter reference but does not certify 2026 official ANRE key.
- `QABC-0024`: `BLOCKED_FIGURE_MISSING_NO_MODEL_CALLS`, despite source drawing recovery noted above. Missing asset must be accurately bridged into the queue first.

## Agent lessons and release gates
- Select linguistic agent using qualifiers in original **options**, not just stem. Do not label a model qualified merely because it echoes ABC and headings.
- Explicit unique/original source vs intended exam key vs technical truth; qualified independent source verification remains necessary.
- No model weights changed and no stable skills promoted. Revised prompts/regressions are *candidate agent training* only.
- No original ANRE QABC/key/HTML/APK/main changes, no merge/release, PR #13 and audit PR #7 Draft.
- Next: execute QABC-0036/0042/0050/0065, then QABC-0069/0080/0091/0096 as two independent four-item cohorts. A failed role should not erase other valid model traces, and prior results should not be rerun without a specific reason.
