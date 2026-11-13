# CKPT-038 | All-question problem-first screening | 2026-11-13

## User decision (authoritative)
**Identify all known and detectable problem signals first; adjudicate the problematic group before the apparently simple group.** Discover reusable logical, source-scope and linguistic rules in difficult questions; propagate these lessons to not-yet-examined questions. Do not mark unflagged questions correct. This order supersedes the prior easier-questions-first suggestion and continues CKPT-037.

## Evidence-based screening already completed
- Reused **30/30 original preliminary batch CSVs**; extracted per-unit source/candidate/scope warning and review fields into five traceable screening overlay JSONs under [PROBLEM_FIRST_SCREENING_2026_11_13](./INTEGRATED_ADJUDICATION_2026_11_13/PROBLEM_FIRST_SCREENING_2026_11_13/).
- Matched overlays **568/568** against canonical [MASTER_UNIT_CARDS_568.csv](./INTEGRATED_ADJUDICATION_2026_11_13/MASTER_UNIT_CARDS_568.csv) and pre-existing priority risk categories P0/P1/P2.
- Added deterministic *screening heuristics*, not proof: contradictory keys for the *same QABC*; earlier proposed alternative vs stored key; documented `NO_CORRECT`, `BLOCKED`, `MISSING_DIAGRAM`, `SOURCE_SCOPE_AMBIGUITY`, `MULTIPLE_TRUE`, `UNRESOLVED`, `DEPENDENCE_MISSING`; missing diagrams referred to in the stem; dangerous absolutes / uniqueness / preference qualifiers in the **stem or the stored correct option**.
- **Do not flag** all rows merely because 2026 edition/source and true independent QA are pending: this would collapse the two categories into one. Edition is a separate release gate applied equally to every ID.
- The P0/P1/P2 risk label is an *existing preliminary priority*, not confirmed incorrectness. Initial screening can make false negatives and false positives; not all problems can be identified before source-by-source validation.

## Screened results
| Category | Distinct QABC units | Interpretation |
|---|---:|---|
| Pre-existing P0 high priority | **66** | Technical/key/scope risk; investigate first |
| Pre-existing P1 elevated priority | **222** | Primarily applicable legal/normative source and edition risks; investigate before unflagged |
| Previously P2 newly promoted by warning | **5** | Newly detected semantic or alternative-key signal; investigate with problematic group |
| **Problematic or suspected review-first subtotal** | **293/568** | **NOT** 293 confirmed wrong answers |
| Previously P2 without current warning | **275/568** | No screening flag found; **NOT verified safe/correct** |
| **Total** | **568/568** | All QABC unique cases classified |

Per-grade [822-ID routing CSV](./INTEGRATED_ADJUDICATION_2026_11_13/PROBLEM_FIRST_SCREENING_2026_11_13/PROBLEM_FIRST_COMPLETE_822_ID_ROUTING_V1.csv):
- **344/822** ID placements mapped to the 293 review-first units: P0=101 IDs, P1=233 IDs, 5 newly promoted P2 units=10 IDs.
- **478/822** ID placements linked to 275 currently unflagged units, deferred until problem-first patterns are adjudicated.
- **0/822 approved for learning**, all old barems preserved.

## Newly promoted cases from P2: original QABC unchanged
- **G1-ELE-100**, original key **A**, preliminary `B_CONFLICT_LEAD_NOT_APPROVED`; and **G1-ELE-101**, original key **B**, preliminary `C_CONFLICT_LEAD_NOT_APPROVED`. Both are *suggested counter-key leads*, **not confirmed corrections**. They concern double-busbar operation, so can be adjudicated together with G1-ELE-102/G2-ELEC-245 to learn source/diagram preference rules.
- **G1-ELE-066** contains absolute language within a quotation of charge conservation; flag may be benign. Linguistic specialist must distinguish **quoted law** from universal assertion in the stem.
- **G1-ELE-167 / G1-ELE-168** use `de preferat` in contrasting line-transformer H bridge configurations; need precise operation/topology preference source. They are not automatically wrong.
- Each of these five unique units appears in two grade-specific placements, ten IDs total.

## Workflow: problematic-first with knowledge-transfer
1. **Problem clusters before any 'simple' completion:** cross-grade key contradictions and proposed alternate keys; missing diagrams / source-condition mismatches; no unique option / excessive qualifiers; legislation/regulatory edition + grade; remaining P0/P1. Order by *reuse potential*, not only severity.
2. For a difficult cluster, resolve original A/B/C + same exact physical/legal object, source document/edition + contextual mapped paragraph 4–6 sentences with **selective bold**, link/locator, offline rights and actual independent QA. **No barem changes without approval**.
3. Every resolved issue produces a **transferable rule** with scope limits and a search tag. Rerun **automated screening over all 568 units and 822 ID placements**, including the deferred group; promote newly exposed cases immediately instead of waiting for the end. Do **not** automatically apply a corrected key or invent a second reviewer.
4. Track separate counters `flagged`, `under_adjudication`, `research_mapped`, `independent_QA_passed`, `approved_for_learning`. Only the latter is safe for training; initial 6 contextual mapped units remain unapproved.
5. When all review-first units are handled, proceed to **all unflagged** with same full one-pass review and QA; finding zero flags is not a bypass of source and edition validation.

## Actual structural QA
- Fetched full 568-row classification and 822-row grade routing from GitHub after commit.
- Reconciled all unit memberships, original canonical keys, preliminary source paths and all 822 per-grade original keys, hashes, unit ID/routing with previous master/ledger: **0 mismatches**, no release approvals, no duplicate/replacement originals.
- **No new primary-source technical adjudication and no independent actual QA** is implied by this screening; this is an organization + evidence-routing milestone only.
- [PR #7 Draft](https://github.com/AcoBenny/ANRE_Trainer/pull/7) remains open unmerged. No changes to original QABC, keys, HTML, APK, or main. No background worker.

## Results
- [All unique questions screen](./INTEGRATED_ADJUDICATION_2026_11_13/PROBLEM_FIRST_SCREENING_2026_11_13/PROBLEM_FIRST_COMPLETE_568_CLASSIFICATION_V1.csv).
- [All grade-ID mappings](./INTEGRATED_ADJUDICATION_2026_11_13/PROBLEM_FIRST_SCREENING_2026_11_13/PROBLEM_FIRST_COMPLETE_822_ID_ROUTING_V1.csv).
- Initial research and contextual source mappings remain [CKPT-037](./CKPT_037_INTEGRATED_ONE_PASS_CONTEXT_6_P0_UNITS_2026_11_13.md).
