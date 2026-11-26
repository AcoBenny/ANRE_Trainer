# ANRE Mission Control | CKPT-430
2026-11-26 | Owner strategy supersedes CKPT-427 validation queue. [Mission issues](https://github.com/AcoBenny/ANRE_Trainer/issues?q=label%3Amission-control) | Draft PR #7.

## Current board
| ID | Mission | Status | Evidence/dependency |
|---|---|---|---|
| ANRE-MC-000 | Strategy and board | DONE | Owner decision and this checkpoint; no bank change |
| ANRE-MC-001 | [Match Legislation + Technical Norms](https://github.com/AcoBenny/ANRE_Trainer/issues/14) | DONE | CKPT-430: 305 unique, G1 151 / G2 154; 140 legacy matches for cards only; [crosswalk](CONSULTFORM/CKPT_430_CROSSWALK_305.json) |
| ANRE-MC-002 | [Reuse cards and references](https://github.com/AcoBenny/ANRE_Trainer/issues/15) | TODO | NEXT; MC-001 complete, 305 cards |
| ANRE-MC-003 | [Electrotechnics](https://github.com/AcoBenny/ANRE_Trainer/issues/16) | BLOCKED | Await owner workbook |
| ANRE-MC-004 | [HTML/APK integration](https://github.com/AcoBenny/ANRE_Trainer/issues/17) | TODO | MC-001/002; full bank after MC-003 |
| ANRE-MC-005 | [Functional QA and owner acceptance](https://github.com/AcoBenny/ANRE_Trainer/issues/18) | TODO | MC-004 |

## Binding owner decisions
- CONSULTFORM solved worksheets define the new Trainer question text, options, correct answer and reference. Accept provided keys without technical/legislative re-adjudication. Not a claim of official ANRE certification. Compare the correct option text rather than letter when options are reordered.
- Grade allocation (owner correction CKPT-430): for the two CONSULTFORM workbooks, GR I = exclusively G1; blank = exclusively G2. For Electrotechnics inspect the marker convention when supplied; do not assume it if different. Legacy QABC matches are for card reuse/provenance only, not grade allocation. Supersedes CKPT-429 fallback-to-both rule. Keep all historical keys and supplemental exercises separate.
- Reuse existing compatible source cards; use original before/selected bold/after passage where available and allowed, otherwise explicit paraphrase/locator or missing-source flag. Do not invent source text. No new cycles of technical answer validation. Maintain import/scoring and functional QA.
- Preserve all CKPT-427 audit artifacts (400 educational routes, 200 holds, 222 pending were historical figures, not current release gates). Stop previous 450/822 target; new total from actual imports. Old audit remains available, not erased or retroactively reclassified.
- Keep original files and main intact; new versioned Trainer dataset and candidate builds only; no merge/release without explicit owner approval. No raw copyrighted workbooks/PDFs uploaded to GitHub without rights/authorization.

## Anti-loop operating procedure
1. Read this board, current mission issue, ACTIVE_HANDOFF, and existing evidence at start of each GFR/ARA session. Select first eligible TODO; check for duplicate work by stable mission ID, existing manifests and checkpoints.
2. Transition TODO -> IN_PROGRESS -> DONE only with actual evidence; BLOCKED means exact missing dependency, not failed verification. Use issue body status, keep DONE closed, BLOCKED open. No duplicate issues, no re-running DONE without documented new material input/regression. Distinguish proposed from executed work.
3. At end, update mission issue, this board and ACTIVE_HANDOFF with result, counts, evidence commit/path, unresolved dependency and next action. Preserve historical audit. If board and issues diverge, reconcile actual evidence before further work. No paid Actions for documentation/import-only work; no background worker.

## Historical baseline
[CKPT-427 handoff at pinned commit](https://github.com/AcoBenny/ANRE_Trainer/blob/4ada6c74024d47d5c297ae2a415a34cfdff26b78/ACTIVE_HANDOFF.md). Earlier issue #10 strategy superseded, historical audit still retained. Intake counts from previous conversation: 104 legislation + 201 norms, not fresh extraction in this board task. No import or build executed by CKPT-428.
