# ANRE Mission Control | CKPT-448
2026-11-28 | Owner strategy supersedes CKPT-427 validation queue. [Mission issues](https://github.com/AcoBenny/ANRE_Trainer/issues?q=label%3Amission-control) | Draft PR #7.

## Current board (execution order, not issue creation order)

**Next critical path: MC-006 → MC-004 → MC-005.** Stable IDs remain unchanged. MC-004 candidate HTML and build kit are retained; final integration and APK compilation wait for MC-006 completion or explicit owner waiver. No intermediate build required.
| ID | Mission | Status | Evidence/dependency |
|---|---|---|---|
| ANRE-MC-000 | Strategy and board | DONE | Owner decision and this checkpoint; no bank change |
| ANRE-MC-001 | [Match Legislation + Technical Norms](https://github.com/AcoBenny/ANRE_Trainer/issues/14) | DONE | CKPT-430: 305 unique, G1 151 / G2 154; 140 legacy matches for cards only; [crosswalk](CONSULTFORM/CKPT_430_CROSSWALK_305.json) |
| ANRE-MC-002 | [Reuse cards and references](https://github.com/AcoBenny/ANRE_Trainer/issues/15) | DONE | CKPT-431: 305 cards; 167 original source anchors, 144 historical rationales (overlap); 67 reference-only/missing; [report](CONSULTFORM/CKPT_431_MC002_REPORT.md) |
| ANRE-MC-003 | [Electrotechnics](https://github.com/AcoBenny/ANRE_Trainer/issues/16) | DONE | CKPT-434: 275 Electro + 2 PDF imported; 185 historical explanations reused, 11 observations, 79 explicit gaps; [report](CONSULTFORM/CKPT_434_ELECTRO_CARD_REUSE_REPORT.md) |
| ANRE-MC-006 | [Complete educational explanations and source excerpts](https://github.com/AcoBenny/ANRE_Trainer/issues/19) | IN_PROGRESS | CKPT-448: 218 complete fields, 396 source excerpts/formulas/table rows, 582 explanations; 178 context gaps, 186 source gaps, 0 explanation gaps. [Report](CONSULTFORM/CKPT_448_MC006_I7_PROGRESS.md)|
| ANRE-MC-004 | [HTML/APK integration](https://github.com/AcoBenny/ANRE_Trainer/issues/17) | BLOCKED (finalization) | Await MC-006; CKPT-434 HTML 582 updated, 3492 permutations PASS; updated Android kit staged, actual APK compilation pending; [report](CONSULTFORM/CKPT_434_ELECTRO_CARD_REUSE_REPORT.md) |
| ANRE-MC-005 | [Functional QA and owner acceptance](https://github.com/AcoBenny/ANRE_Trainer/issues/18) | TODO | After MC-004 final integration/APK; MC-006 completion or explicit owner waiver required |

## Binding owner decisions
- CONSULTFORM solved worksheets define the new Trainer question text, options, correct answer and reference. Accept provided keys without technical/legislative re-adjudication. Not a claim of official ANRE certification. Compare the correct option text rather than letter when options are reordered.
- Grade allocation (owner approved CKPT-433): compare exact normalized stem and unordered ABC with grade-specific cached ANRE source rows. G1-only -> G1, G2-only -> G2, both or unmatched -> both. Electro common to both grades; original CONSULTFORM grade markers retained for provenance only. V1–V5 are supplemental sources only: add materially different questions, never separate test modes or duplicate imports. No technical key revalidation. Direct official XLSX retrieval blocked; use existing pinned source extracts with limitations recorded.
- Reuse existing compatible source cards; use original before/selected bold/after passage where available and allowed, otherwise explicit paraphrase/locator or missing-source flag. Do not invent source text. No new cycles of technical answer validation. Maintain import/scoring and functional QA.
- Preserve all CKPT-427 audit artifacts (400 educational routes, 200 holds, 222 pending were historical figures, not current release gates). Stop previous 450/822 target; new total from actual imports. Old audit remains available, not erased or retroactively reclassified.
- Keep original files and main intact; new versioned Trainer dataset and candidate builds only; no merge/release without explicit owner approval. No raw copyrighted workbooks/PDFs uploaded to GitHub without rights/authorization.

- CKPT-435: full card target is explanation + real supporting excerpt, source locator/edition and preceding/following context where available/permitted. Historical paraphrases and mere references are not complete quotations. Track distinct missing fields by stable ID; no new answer adjudication, no invented citations, no forced support if source disagrees. MC-006 remains separate from completed bounded reuse tasks.

## Anti-loop operating procedure
1. Read this board, current mission issue, ACTIVE_HANDOFF, and existing evidence at start of each GFR/ARA session. Select first eligible mission in execution order (respect dependencies, not numerical IDs); check for duplicate work by stable mission ID, existing manifests and checkpoints.
2. Transition TODO -> IN_PROGRESS -> DONE only with actual evidence; BLOCKED means exact missing dependency, not failed verification. Use issue body status, keep DONE closed, BLOCKED open. No duplicate issues, no re-running DONE without documented new material input/regression. Distinguish proposed from executed work.
3. At end, update mission issue, this board and ACTIVE_HANDOFF with result, counts, evidence commit/path, unresolved dependency and next action. Preserve historical audit. If board and issues diverge, reconcile actual evidence before further work. No paid Actions for documentation/import-only work; no background worker.

## Historical baseline
[CKPT-427 handoff at pinned commit](https://github.com/AcoBenny/ANRE_Trainer/blob/4ada6c74024d47d5c297ae2a415a34cfdff26b78/ACTIVE_HANDOFF.md). Earlier issue #10 strategy superseded, historical audit still retained. Intake counts from previous conversation: 104 legislation + 201 norms, not fresh extraction in this board task. No import or build executed by CKPT-428.
