# CKPT-293 | GFR complete 822-ID preflight; 11 unindexed source rows, 18 repeated-stem choice groups | 2026-11-20

## Result and non-overclaim
**All 822 existing grade IDs passed structural and provenance-join QA. The 822 answers did NOT receive independent technical/linguistic signoff, and remain UNAPPROVED FOR LEARNING.** The user requested maximal autonomous continuation without repeating old batches; this checkpoint records genuinely executed preflight and the exact remaining human/source gating conditions.

Baseline pinned `V149_568_QABC_FINAL_GATE_PROVENANCE_BIAS_AND_CHALLENGE_2026_11_20.csv` Git blob `ee2ac5536c78eb06a0461243be34c117e257188f`; `V151` blob `a233c6744a68af16ed434a0b1574ed33ba53061e`.
- **568 distinct QABC** / **822 distinct grade placement IDs**. No repeated grade IDs; each has original question, all A/B/C, associated source workbook+row, existing imported key, and a valid source-file pointer.
- **0** missing stored enunțs/option cells, **0** identical three choices, **0** invalid/missing A/B/C keys, **0** missing per-grade key references.
- **2** already known cross-grade conflicts `QABC-0017` and `QABC-0094`, previously researched and not silently changed.
- **All 568** master units explicitly retain technical QA, linguistic QA, source QA, human signoff `NOT_RUN`, `approved_for_learning=NO`. This is not evidence that no one ever researched them; rather, no separate recorded independent professional signoff has been completed.

## New V153 | source-workbook row-scope gap
- [V153 original 275 vs master 264 physical source rows](V153_ELE_2024_275_SOURCE_ROWS_V149_11_GAPS_VS_822_SCOPE_2026_11_20.json), Git blob `b1ac319bcd4342a90d1210f8d8ec92fdf06de5da`.
- Original user-supplied `ELECTROTEHNICA-09.2024-2(2).xlsx`, SHA-256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c` **reopened with artifact_tool**. `Sheet1!A8:D282`: **275 original question-stem rows**, **272 with all A/B/C as cell text**, and **3 whose three choice cells are empty because answers are originally drawn diagrams**.
- **265 V149 QABC units point to 264 unique physical source rows** (source row **159** mapped twice, `QABC-0143` edited-G1 and `QABC-0568` original-G2; this is a known variant-level mismatch, not a workbook duplicate).
- **11 original worksheet rows have no direct V149 `source_workbook+source_row` match**: **15, 30, 31, 32, 39, 43, 44, 65, 117, 176, 181**. Exact normalised-stem search in V149 found no direct text matches either.
- **9/11 are figure-dependent** (native OOXML drawing anchors physically present), including **30/31/32 with graphically represented A/B/C**. **2** are ordinary text math/electrotechnics rows (39 and 65). **8** of the 11 have all A/B/C as cell text.
- Crucial: these 11 omissions are **source coverage to adjudicate**, not proof that 822 approved-qualification placements lack 11 grade questions. **DO NOT autonomously increase the target to 833, insert synthetic IDs, or invent figure answer keys.** Must establish whether they were intentionally omitted due to grade/scope and recover the original figures as-is if needed. No source distribution occurred.

## New V154 | per-grade final QA matrix
- [V154 all 822 grade ID final validation gates](V154_ALL_822_GRADE_ID_FINAL_CONTENT_REVIEW_GATES_2026_11_20.csv), Git blob `231e5193ea74035f5614726f1636316531bc615a`.
- Exactly **822 line items**, each with grade ID, QABC ID, original selected letter unchanged, source locator, priority, V151 lane, historical evidence pointer, automatic **preflight flags** and explicit *independent QA NOT_RUN / official grade NOT VERIFIED / learning NO*.
- Risk flags count **per grade ID** (not mutually exclusive, not errors/certified answer defects): **153 nonworkbook/didactic keys with all letter A**, **160 cases with exclusive quantifier language** (`numai/doar/etc.`), **47 grade IDs in repeated-stem groups**, **10 questions mentioning figures among existing grade placements**, **9 grade IDs in six strict source/key blockers**, **4 grade IDs in two cross-grade key conflicts**, and **2 grade IDs with numeric source-cell type variance**.
- All 153 nonworkbook cases are still practice/didactic-origin with 153 imported A choices; all require provenance + exact source/edition and answer-position-bias gate. These values are not a verdict that the answers are false.

## New V155 | option-sensitive repeat audit
- [V155 18 same-stem source-specific A/B/C groups](V155_REPEATED_STEM_18_GROUPS_EXACT_A_B_C_AND_KEY_POSITION_GATES_2026_11_20.json), Git blob `cd59198b3d7823c9af63f2af5c66764c7b4f7b65`.
- **18 groups** containing **40 distinct QABC and 47 grade ID placements**, each with exact original A/B/C and stored answer letters.
- 7 groups from Electrotehnica source, 4 from G1 Legislație, 7 from G1 Norme; earlier CKPT-287's **8 source** same-stem group count included two original diagram questions in rows 176 and 181 **not in V149**, so the 18 current V149 groups have only 7 ELE groups; no conflict in those counts.
- **Every group varies in at least one option**. None is a pure permutation of all three choice texts. One group has text-identical selected options across different question choices. Never de-duplicate or remap answers using only the stem.

## Evidence pointer QA, bounded by connector tool limit
- All **55 distinct source-analysis file names** referenced in V149 are actually present in GitHub `docs/QUESTION_AUDIT`/ `docs`. This only confirms file existence, not correctness.
- Deeper read of the **eight most frequently cited existing files** covered **128 QABC**; **121** had an immediately matchable explicit grade ID, QABC ID or stem within those eight files. The other **7** referenced both CKPT-249's range-level provenance note and CKPT-248; CKPT-248 was reopened separately and contained explicit IDs **G2-ELEC-057, 058, 059, 060, 061, 062 and 064**. Thus **128/128** in this *selected subset* have an explicit textual identifier in at least one of their referenced documents; **not proof that all 568 have been semantically source-mapped**. The 55-file full-text sweep was attempted but stopped when the GitHub connector returned tool-call limit. No new paid or model calls.
- Existing Academy two-model runs are a limited separate historical experiment, **not independent accredited SME signoff**. No new external AI role run in this checkpoint.

## Executed regression
- After publishing V153, V154 and V155, re-fetched **V149, V151, V153, V154 and V155** from GitHub and ran **14/14 deterministic true assertions, 0 failures**:
  - V149 and V151 each 568 entries; V154 exactly 822 unique grade IDs.
  - Each V154 `grade_id` belongs to its V149 QABC and preserves the exact source workbook, row and stored letter.
  - All original key/learning flags remain frozen; official key not authenticated and distinct technical/linguistic QA not run.
  - Original workbook count 275 / 11 source-row gaps; 11 gap records; source 159 version split; original 822 bank not expanded.
  - V155 precisely 18 repeat groups, 40 unique QABC appearances, 47 grade ID appearances, every V155 original option and key exactly matches V149.
- Scope: **dataset/integrity/coverage**, not mathematical or regulatory proof for every answer, nor automated current CI.

## Source and release boundaries
- Official ANRE https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ currently lists **2023 syllabus**, **2024 electrotechnics examples**, and **2023 G1 NOR/LEG examples**. The user-uploaded XLSX is a readable copy, **not cryptographically matched to official server**. ANRE example questions do not automatically authenticate scoring letters.
- ANRE explicitly states https://anre.ro/informare-de-presa-anre-avertizeaza-site-ul-chestionare-anre-ro-nu-are-nicio-legatura-cu-institutia-noastra/ that chestionare-anre.ro **is not an ANRE-operated or affiliated official source**. It can only be supplemental/unofficial research, never proof of a signed ANRE answer key.
- **No original QABC, imported ABC keys, code, HTML, APK, main, merge/release changes. PR #7 and #13 are to remain Draft until authorized.**

## Exact next steps with nonduplicating execution
1. **Source coverage and priority content:** decide legitimate grade scope and original figure fidelity of the 11 V153 unmatched source rows, leaving fixed 822 target unchanged until supported. Keep six V150 strict conflicts separately blocked; no guessing corrected exam keys.
2. **Independent, source-specific A/B/C and language QA across the 568 QABC** (not 822 redundant independent reviews): use the 55 preserved evidence files, fetch official and edition-matched controlling source paragraphs, compare options, counterexamples, and register a real distinct reviewer signoff. Avoid 18 same-stem loss and 153 all-A practice memorization. Record each grade's approved **exam-sample** versus **educational** version separately. V154 is the exact queue for every individual grade ID.
3. **Only after authorized content approval**, remap approved educational alternatives with shuffled positions, preserve original public sample versions unchanged, then test actual HTML/APK offline. No merge/release without user authorization.

**Final status: 822/822 grade IDs structurally gated; 0/822 qualified-independent content approvals.**
