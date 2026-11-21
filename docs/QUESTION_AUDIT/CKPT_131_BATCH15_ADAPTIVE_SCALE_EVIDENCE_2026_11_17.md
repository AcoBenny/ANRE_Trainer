# CKPT-131 | ANRE adaptive BATCH15 experiment | 2026-11-17

## Recorded actions and actual GitHub evidence
- Start: Draft PR #7 at `809293ec80b20f707e239522d2fec4088129f329`, 491/568 contextual cards, 668/822 corresponding grade IDs, 77 QABC unit cards still absent.
- **BATCH15-1**: `CKPT_129_BATCH15_ELE230_235_237_238_239_241_251_252_254_255_256_258_259_260_262_2026_11_17.json`, committed `cf10c9eeaf900db586c0648971908b389f90de76`; ledger update `54e0ed2b5d4417f44202db9a30d83e8fb33a737e`, postwrite 506/568, 698/822 IDs, 62 QABC units remaining.
- **BATCH15-2**: `CKPT_130_BATCH15_ELE227_228_232_234_242_250_253_261_263_268_271_272_273_274_275_2026_11_17.json`, committed `3a96614973ec3a8f5eca8279b37f067d9d3ecc5a`; ledger update `110009ec25bb057aa76f17d4a1e555ffa2553ddd`.
- Final readback: **521/568 unique preliminary QABC cards**, **728/822 grade IDs covered**, **47 QABC units remaining**, **0/822 approved for learning**. All **30 cards have unique unit IDs** and match original QABC SHA, grade member IDs, and imported A/B/C key mapping. No canonical QABC, answer key, app HTML/APK, MASTER or release/merge changes.
- Source validation levels must not be conflated: NIST official SI table, OpenStax technical discussion, Schneider CT open-secondary hazard and certain manufacturer references were opened or researched publicly; many per-question norm/exam edition alignments and independent specialist review remain NOT_RUN/UNVERIFIED.

## Runtime/automation QA lesson
- **15-unit batches finished with final structural QA PASS and no persistent session stall.** However two local script-construction attempts failed before any write (syntax/unbound field errors), and one draft ledger reconciliation dry-run stopped at zero matched units; a corrected readback-based attempt successfully reconciled all 15 without duplicate credit.
- This is *not* a clean-error-free trial. Do **not** increase automatically to 20. Favor 12–15 on straightforward sourced questions, 5–8 on disputed terms and safety/normative cases. Precompile/cross-check array field names, prove the first unit match before processing all, and only then perform the atomic ledger update.
- Benchmark is limited to actual repository operations and readback; elapsed time, token cost, genuine independent AI evaluators and end-to-end exam correctness were NOT measured/tested.
- The 47 outstanding QABC units are disproportionately complex (e.g. busbar/coupling topology, ambiguous source qualifications, earthing, switching, 2026 F-gas SF6 regulatory changes). Never force an old technical key to pass on a mismatched generic source or mark it approved due to research-card completion.

## Next
1. Prioritize difficult remaining 47 by source/object match, using mandatory technical, source and linguistic checks; select batches based on risk instead of fixed count.
2. Confirm official 2026 exam-source edition/answer keys and obtain genuine independent QA before changing any approval flag. Keep the canonical exam text and keys unchanged until user authorizes edits.
3. Keep PR #7 Draft without merge/release.

**Avengers Asamble roles in this session:** one assistant following specialist checklists; no independent agent spawned or model re-trained.
