# CKPT-228 | ERRATUM / V107 superseded: exact QABC cross-grade pairing in V108 | 2026-11-18

## Issue detected during GFR post-write QA
- The intermediate `V107_GFR_P2_15_LEGACY_UNIT_GRADE_PAIRS_CKPT227_2026_11_18.csv` **must not be used as an authoritative tracking layer**.
- It used an arithmetic relation G2-ELEC-number = G1-ELE-number + 153, which is **wrong after a source row is skipped**. Eight of the 15 G2 references were attached to neighboring original questions. This affected **only the new audit metadata overlay**, not the canonical 822 original questions, A/B/C, answer keys, HTML, APK, source file, main branch or release.
- The correct pairing algorithm **never infers counterpart from ID arithmetic**. It requires exact equality of (original question, A, B, C, imported canonical key) and asserts exactly one Grade I plus one Grade II match. If ambiguous/duplicate more than twice, it blocks instead of guessing.
- CKPT-227's case evidence is still valid for its 15 original **G1** IDs; only V107's claimed G2 source linkage was incorrect.

## Supersession and verifiable correction
- **V108** `V108_GFR_P2_EXACT_QABC_PAIRING_CORRECTED_822_2026_11_18.csv` was reconstructed from **clean V106**, not from V107. Original Git V73 blob `c027d417a8e4e605c830b2016fb55b099b8d130b`; clean V106 blob `06b6dd9ac8478a7c91f53074a4756033780a3307`. New V108 commit `ff95c9c9c5807628838ce7ce296889fbbd6cf579`.
- Correct pairs: 001→G2-ELEC-154; 002→155; 003→156; 004→157; 005→158; 006→159; 007→160; **009→161** (not 162); **010→162** (not 163); **011→163** (not 164); **012→164** (not 165); **013→165** (not 166); **015→167** (not 168); **016→168** (not 169); **017→169** (not 170).
- 15 new individual G1 P2 reviews, 12 G2 exact-QABC references reused, 3 G2 previously focused kept **unchanged** (G2-ELEC-158, -162 and -167).
- **Hard verified invariants:** 822 grade IDs unique, 0 unrelated rows changed relative to V106, 0 keys authorized, 0 approved-for-learning, 15 reviewed G1/12 newly referenced G2/3 prior G2, 491 grade-ID P2 records without focused verification.
- Audit-source evidence `CKPT-227` remains; **V107 is explicitly superseded by V108 and has no release authority**.

## Regression rule, permanent for grade-pair joins
- Match grade records ONLY by exact tuple of (question, A, B, C, canonical_key) AND grade difference. Verify tuple equality (not merely shared workbook source row or similar wording) before recording crossgrade reuse. If no exactly matching counterpart, leave unresolved and report. Never infer grade ID from a numeric offset.
- No independent reviewer/model or actual ANRE scoring-key signoff from this correction. PR#7 still Draft. App stays paused while question audit completes.
