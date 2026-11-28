# CKPT-203 | G1-LEG-025 user interpretation and dual-source policy | 2026-11-18

## User decision recorded from current ANRE session
- The user explicitly chose BOTH the publicly accessible Portal Legislativ and the project/local GitHub legal corpus as complementary evidence sources, instead of restricting research to GitHub only.
- The user endorses keeping the already imported answer **B (Nu)** for G1-LEG-025. They consider the distinction between the statute's 'prezentului titlu' and the examination stem's 'Legea nr.123/2012' immaterial for the *intended exam answer in this context*.
- This is a **user interpretation / exam-key decision**, not proof that title and entire law are legally identical; the exact scope note remains visible for independent juridical QA. Do not repeatedly ask the user to choose A/B/C again without new contrary evidence.

## Grounding and audit constraints
- Exact case: G1-LEG-025 (AU-950954e2d16b0eb9). The canonical question, original A/B/C and imported key B are NOT modified.
- Statute evidence: Legea nr. 123/2012, Title I, Chapter I, art. 1(2)(b): official public source https://legislatie.just.ro/Public/DetaliiDocument/311821 ; previous official page extraction in CKPT-202 succeeded. A direct public-page open may produce HTTP 502, which does not render the law inaccessible.
- Source priority: preserve the official article wording, applicable consolidated date, annotations, and exceptions; cross-check against a rights-permitted archived / local GitHub copy when available and do not assume it is already present. If sources differ, log edition/locator rather than silently replacing one with the other.
- Important scope: source exempts described stationary DC sources not inverter-connected to SEN from Title I. A precise lawyerly statement cannot substitute 'entire law' as equivalent. In the supplied examination framing, B remains the adopted intended answer, pending separate legal-content QA.
- Prior 6/6 JS equality/order smoke tests in CKPT-202 are not full source-fidelity certification, not Python packaged validator execution, and not independent legal validation. Full continuous three-original-paragraph presentation remains unverified.

## Next steps and safeguards
- Do not reopen G1-LEG-025 for the same semantic debate without new evidence; keep exception/scope note in explanation and log as user-endorsed intended key B (not final certified legal answer).
- For the next ANRE case, do Docs Intelligence official + local reference dual check, select adjacent norm context, preserve original ABC, keep interpretation separate, and run content QA. Do not say full-context PASS without actual displayed-text verification.
- PR #7 remains Draft; do not change canonical bank, barem, HTML, APK, merge or release without explicit authorization.

## Prior checkpoint
- CKPT-202: docs/QUESTION_AUDIT/CKPT_202_LEG025_OFFICIAL_SOURCE_AND_FIDELITY_SMOKE_2026_11_18.md
