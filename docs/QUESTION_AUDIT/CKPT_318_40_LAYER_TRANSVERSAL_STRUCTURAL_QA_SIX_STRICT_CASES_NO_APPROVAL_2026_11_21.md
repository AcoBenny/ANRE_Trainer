# CKPT-318 | Cross-layer structural QA (40/40) and six strict hold triage | 2026-11-21

**Scope:** Read-only verification of CKPT-317 data plus external source-context comparison. This checkpoint is NOT expert certification, NOT confirmation of any official exam scoring key and NOT permission to use cards for learning. PR #7 remains Draft. Original questions, A/B/C, imported scoring keys, offline source assets, HTML and APK are unchanged.

## Locked baseline
- Repository: `AcoBenny/ANRE_Trainer`, audit branch `audit/anre-v8-priority-17-20261109`.
- Parent HEAD: `e2179fa47f17cd5153cad18285ce4ec237e1ed03` (CKPT-317).
- Manifest: `V241_568_QABC_ALL_FULL_ABC_822_GRADE_ROUTES_4_VERSION_HOLDS_2026_11_21.json`.
- Dual-version source comparison: `V240_FOUR_MATERIAL_SOURCE_VS_TRAINER_VARIANTS_3_NEW_FULL_DUAL_ABC_2026_11_21.json`.

## Executed structural controls
1. Fetched and parsed each of the 40 editorial layer files listed in V241, in bounded connector batches; every returned blob SHA matched the V241 layer reference.
2. Compared each layer's actual card count against `new_qabc`, each card's `unit_id` and `grade_ids` against its exact V241 matrix entry, and the manifest's `editorial_file` routing. All matched, with a schema-specific exception below.
3. Exception `V188_QABC0013_SOURCE_FREE_FIELD_EXACT_ANRE_TERM_COUNTEREXAMPLES_2026_11_20.json`: intentionally stores a **single** card as `original`, `ABC_editorial_draft`, and `rephrased_question` / `rephrased_answer`, not a `cards[]` array. Verified its QABC-0013 identity, G1-ELE-014 and G2-ELEC-166 grade IDs, and all three rationale fields A/B/C. The generic array-only count warning is a schema false positive, NOT a missing card.
4. For the `V240` dual-version appendix, exactly three `previous_draft_not_repeated=null` records are *new* cards; QABC-0236 points to the pre-existing `V194` card and is NOT double-counted.

**Observed reconciliation:** 40/40 layer file references, 568/568 unique QABC units, 822/822 unique grade-route IDs, 0 duplicate unit/route IDs, 0 missing card-file routes, 0 card-count mismatch after the V188 schema exception, 0 blob-SHA mismatch. Grade route distribution: G1=414, G2=408. Provenance classes remain 411 original-exact workbook cases, 4 materially edited original cases, 153 unofficial supplemental practice cases.

**Important scope limitation:** These are structural and identity tests, not a manual truth audit of every option rationale or full-source edition comparison. Independently qualified technical and linguistic review has not occurred. The original ANRE-hosted spreadsheets were NOT freshly re-downloaded and line-compared during CKPT-318; this phase relied on the provenance captured in prior V175/V240.

## Blocker set algebra, not additive totals
- V241 marks **136** unique explicit semantic/source/model holds.
- It marks **6** strict source/key/version conflicts, ALL already inside the 136: QABC-0017, QABC-0094, QABC-0143, QABC-0236, QABC-0362, QABC-0386.
- The **4** material source-vs-Trainer variants, ALL inside the same strict-six and semantic-136 set: QABC-0143, QABC-0236, QABC-0362, QABC-0386.
- Therefore the current **priority unresolved union is 136 QABC units, not 136+6+4=146**. There can be other review gates among the remaining 432 units; 136 is not the total number needing independent approval.
- **Learner approvals: 0 / 822.** No exam key authenticated.

## Six strict holds: source-context recheck (preliminary, no signoff)
| Unit / grade route(s) | Recheck and disposition | What is still required |
|---|---|---|
| QABC-0017 / G1-ELE-018, G2-ELEC-170 | Same original stem and ABC but imported A vs C. Under a balanced three-phase delta of equal mutual capacitances C, the equivalent star phase capacitance is 3C (A mathematically supported *for that model*); see `V201`. | Authenticate the official definition of `capacitatea de serviciu Cs` and applicable model/key before changing either grade's scoring. |
| QABC-0094 / G1-ELE-102, G2-ELEC-245 | Same original ABC but imported A vs C on double-busbar operating policy. NTE 009/10/00 reproductions define `rezerva caldă` and `rezerva rece` operational states but do NOT alone prove that either configuration is universally preferable. | Exact-scope operating policy and official answer adjudication. |
| QABC-0143 / G1-ELE-152 | ANRE-hosted original says propagation constant is `adimensională`; Trainer says `caracteristică`. Propagation constant γ=α+jβ has SI units m⁻¹; γ times length is dimensionless. Original A is conceptually intended but the original stem is dimensionally false. | Authenticate original exam intent; keep source-original and Trainer scoring separate. |
| QABC-0236 / G1-ELE-247, G2-ELEC-383 | Original B: `inducție electromagnetică`; Trainer B: `inducție electrostatică`. A conductor in an electrostatic field may polarize with net total charge still zero. | Do not mark original B as technically proven; require answer-key proof and scope review. |
| QABC-0362 / G1-NOR-048 | Original A says `numai direct din tabloul de distribuție`, C allows `dintr-un circuit de prize`; I7-2011 §5.4.13 permits illumination circuit OR socket circuit OR board feed. Original C source-supported; Trainer's edited A lists all three. | Do not apply Trainer A to original ABC; authenticate official 2026 normative text and official scoring. |
| QABC-0386 / G1-NOR-072 | Original B says disconnect `fără ... scule`, which contradicts I7-2011 §5.5.2.3 requiring individual disconnection with a tool. Original C states the individual disconnect requirement. Trainer B reverses the tool condition to `numai ... cu o sculă`; Trainer C remains partly true. | Source-original B scoring must remain blocked. Confirm edition, overlapping true alternatives, exact exam key and linguistic review. |

### External context inspected during this checkpoint (NOT an official scoring-key certificate)
- I7-2011 reproduced regulatory text and near-neighbor scope, §§5.4.12–5.4.14 and §§5.5.2.1–5.5.2.3:
  - https://legis.medleg.ro/legislatie/2011-reglementari-reglementare-tehnica-3
  - https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011
- The governmental Portal Legislativ page https://legislatie.just.ro/Public/DetaliiDocument/286763 returned HTTP 502 during this pass; therefore official-portal direct reopening NOT DONE. Do not infer effective 2026 edition from reproduced 2011 text alone.
- Propagation constant and units: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Fundamentals_of_Microwave_and_RF_Design_%28Steer%29/03%3A_Transmission_Lines/3.02%3A_Transmission_Line_Theory
- Electrostatic polarization and net charge distinctions: https://openstax.org/books/university-physics-volume-2/pages/6-4-conductors-in-electrostatic-equilibrium and https://openstax.org/books/university-physics-volume-2/pages/5-2-conductors-insulators-and-charging-by-induction
- NTE 009 definitions (secondary legal reproduction): https://legis.medleg.ro/legislatie/2010-regulament-general-manevre-2
- Symmetric delta/star conversion and phase capacitance: https://www.engineeringdevotion.com/electric-power-systems/lecture/chapter-7-capacitance-of-transmission-lines.html
- ANRE live page (bibliography labelled 2023, example ELECTROTEHNICA labelled 09.2024): https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ . The presence of these downloads does not establish an authenticated answer key for the 2026 exam.

## Gates after CKPT-318
1. Preserve the 136-member semantic union, starting with the six strict holds. Reopen official source/edition and verbatim A/B/C; prove affirmative answer and counterexamples, not elimination alone. Keep both original and Trainer versions.
2. Obtain distinct qualified technical/linguistic reviewing evidence plus official grade-specific scored-key confirmation where possible. An additional same-assistant reading, an automated structural PASS or a secondary website does NOT count as independent final signoff.
3. Then examine the other 432 QABC units with the same standard and check grade-route coverage for all 822. Any unresolved card remains blocked for learner use. No app, answer-key or release edits without separately authorized QA and review.

**Result:** CKPT-317 editorial completeness preserved. Cross-layer *structural* reconciliation finished. Final learning validation still NOT completed; 0/822 approved.
