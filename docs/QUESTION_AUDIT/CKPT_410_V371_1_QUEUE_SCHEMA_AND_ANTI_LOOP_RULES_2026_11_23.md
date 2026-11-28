# CKPT-410 | ANRE V371.1 scaffold and anti-loop queue rules

Date: 2026-11-23. Parent CKPT-409, repo `AcoBenny/ANRE_Trainer`, branch `audit/anre-v8-priority-17-20261109`, PR #7 Draft.

## Actual scope (micro-increment 371.1 ONLY)
- Created `docs/QUESTION_AUDIT/ONEPASS_V2_PILOT/V371_SOURCE_READINESS_QUEUE_SCHEMA_2026_11_23.json`: queue contract, priority rules, field/verification gates, batch-size cap, anti-loop policy and empty `records` array. **No five-question batch processed yet.**
- Created/updated the stable resumption pointer `ACTIVE_HANDOFF.md` at repository root for future conversations.
- Parsed the existing V370A compact registry and V370 research-pointer index (no canonical changes); confirmed 568 distinct QABC, 822 route pointers, 136 historic semantic holds, 6 strict holds, 4 source/Trainer variants, 456 QABC with URL-like candidate and 112 with report-only pointers. Source-locator count in V370A is an incomplete index and cannot certify coverage.
- CKPT-409 remains the authoritative inventory and evidence boundary: 415 source-native + 153 unofficial trainer-didactic QABC, 157 quarantined G2 candidates and 11 Electro orphans OUTSIDE the current 822, **0 final learner approvals**. The new schema makes no official-source, key or reviewer claims.

## Definition of done for 371.1
1. Exactly these three documentation-only paths added in one commit on existing audit branch, with no application/barem edits.
2. Reopen GitHub versions and verify JSON parses, `records.length === 0`, checkpoint references V369/V370/CKPT-409, handoff points to 371.2 and PR remains Draft.
3. Report commit SHA, links and verified status; stop. Further batch processing belongs to 371.2.

## 371.2: bounded next increment (NOT STARTED)
Materialize and inspect **five distinct priority QABC** from V370A + V370 original prior-analysis paths. Deduplicate by QABC/grade and source clause; record exact previous->new gates. Prefer existing evidence before fresh searches. Unverified URLs are not proof. Write next checkpoint and update `ACTIVE_HANDOFF.md`. If no gate improves, credit ZERO advancement.

## Hard stops
No change to canonical question text, answer options, imported keys, HTML, APK, main or release. No merge. User engagement only for a named unresolved source-backed choice or bank-scope/key approval. QA script passes do not imply final content approval.
