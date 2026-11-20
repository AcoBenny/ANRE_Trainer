# CKPT-274 | P0 Academy second and third cohorts: actual API evidence and training negatives | 2026-11-20

## Exact completed live execution
- GitHub Actions [44761592780](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44761592780) completed with expected **fail-closed QA** after real attempts. GitHub successfully archived both reports as `academy-p0-remaining-eight-source-gated`, artifact ID `14642201958` (short-lived).
- All 8 QABC attempted, 16 successfully returned nonempty model-role outputs from **37 API attempts** (21 attempts in first cohort, 16 in second); all eight retain original workbook stem/options/grade IDs and no learning approval.
- **All selected agent roles returned properly formatted preliminary model text** for QABC-0036, QABC-0042 and QABC-0069. This proves trace/format only, **not** technical correctness or exact source authentication.

## Exact unresolved slots (no automatic re-run)
| Unit | Unresolved reviewer(s) | Observed reason |
|---|---|---|
| QABC-0050 | independent_skeptic, linguistic_scope | Gemini 503, OpenRouter empty/429, Requesty timeout/429 |
| QABC-0065 | linguistic_scope | OpenRouter empty/429, Requesty timeout/429 |
| QABC-0080 | independent_skeptic | Gemini output returned A/B/C headings but **copied the three original options verbatim**, no option-specific reasoning; rejected correctly by format QA |
| QABC-0091 | linguistic_scope | OpenRouter empty/429, Requesty timeout/429 |
| QABC-0096 | linguistic_scope | OpenRouter empty/429, Requesty 429 |

For first 4 previously attempted P0: [44757996875](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44757996875) had six reviewer responses; QABC-0024 stayed figure-blocked; QABC-0025 had failed linguistic review. Do not replay complete cohorts solely because one role failed.

## Agent training and QA correction
- Existing P0 prompt training already includes explicit source scope, lexical quantifier polarity, no phantom acronyms, constraints on counterexamples, arithmetic checks, individual A/B/C and pairwise comparison, no automatic scored-key inference.
- New real **QABC-0080 copied-options false positive** caused a strengthened prompt requirement: each A:/B:/C: line needs distinct reasoning, not verbatim original option strings. Existing deterministic detector also rejects copied-only lines even if headings are present.
- Corrected workflow exit handling: a **semantic content warning** now fails the cohort rather than falsely reporting a green review; a single targeted role rerun may write a `ROLE_RETEST_PRESENT_NOT_RECONCILED` artifact but still cannot certify independent final QA.
- A role retry must use pinned `--only-unit` and `--only-role`, with at most two free provider candidates (primary, Requesty Gemma) per role to avoid serial quota cascades. The old 37-attempt run used the pre-bounded code; **do not retroactively call it a capped two-provider run**.

## Specific next gate
1. No more mass retries while OpenRouter and Requesty return 429/timeout. Resume **only the six missing/bad reviewer slots** when quota/capacity is verified. Preserve original successful outputs and compare actual model IDs to prevent same-model independence claims.
2. Complete exact primary-source and edition verification, including CKPT-272's physical object/scope caution. QABC-0024 must receive its previously recovered original 22-shape diagram as a validated image before any model prompt; do not fabricate one.
3. Independent qualified technical/source/language QA and official key provenance are still **NOT DONE**. The 12 P0 samples are preliminary; no student approval, no key changes, no application/HTML/APK edits, no merge/release.

PR #13 Draft; audit PR #7 Draft; canonical V149 568 distinct questions / 822 grade placements remains unchanged.
