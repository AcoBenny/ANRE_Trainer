# CKPT-331 | Read the three user-uploaded original question workbooks. 123/123 flagged original A/B/C match, 12 source rows unmapped | 2026-11-21

## Provenance
- Baseline: parent HEAD `e30c2e7ae2f25145f03cdcaca6598e4e617d5223` on `audit/anre-v8-priority-17-20261109`, PR #7 **Draft**, unmerged.
- Input files were actually uploaded by the user during this session and read directly from their original XLSX bytes using `artifact_tool`, not an indirect search engine parser or Trainer-derived copy.
- **These SHA256 hashes prove identity of the exact user-supplied bytes, NOT equality to files currently hosted by ANRE**:
  - Electrotehnică `ELECTROTEHNICA-09.2024-2(1).xlsx` SHA256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`; `Sheet1!A8:D282`, 275 source question rows.
  - Legislație `LEGISLATIE-GR.-1-05.2023(1).xlsx` SHA256 `b683200db51a20b625d00ed9680e4f9b6fd354535fa3cd6c277b632312d17f29`; `Sheet1!A7:D57`, 51 source question rows.
  - Norme tehnice `NORME-TEHNICE-Gr.-1-05.2023(1).xlsx` SHA256 `bed56a32f24d19774ec9dfff8c5b1438176078d0e9c4eb9e8fa1ff1fc98c3092`; `Sheet1!A8:D107`, 100 source question rows.
- File-level first import and direct visual samples successful; source XLSX were not edited or rewritten.

## Original versus historical editorial audit reconciliation
- Previous V243 contains 136 held unique QABC, of which **123 are `PUBLISHED_SAMPLE_CANDIDATE`** and **13 are explicit unofficial supplemental exercises**.
- Reopened the **25 editorial JSON files** referenced by the 123 published held cases, including the special schemas `V188.original` and `V240.four_versioned_records.original_hosted`. Compared each ORIGINAL question (stem, A, B, C) with the exact uploaded XLSX row `A:D` referenced by V243; never substituted the Trainer-mutated alternatives for an original source.
- Matching comparison used Unicode NFKC, consecutive whitespace collapse and edge trimming, with a pair of independent rolling checksums on all four values. **123 / 123 matched** these normalized original fields, **0 mismatches, 0 missing comparisons**:
  - Electrotehnică: **69 / 69** QABC groups;
  - Legislație: **17 / 17**;
  - Norme tehnice: **37 / 37**.
- This means **original wording/option-order provenance is strengthened for the 123 highlighted cases**, not that any imported ANSWER LETTER is correct. These workbooks do not contain an authenticated grade-specific scored-answer key among the A-D questions.
- Full per-case provenance and XLSX row fingerprints: `V244_UPLOADED_3_SOURCE_WORKBOOKS_123_PUBLISHED_HOLD_QABC_MATCH_PROVENANCE_2026_11_21.json`.
- The 13 supplemental held QABC must remain tagged **UNOFFICIAL DIDACTIC**; no attempt was made to present them as 2023/2024 workbook questions.
- Status: all 136 holds remain OPEN, no learner approval generated. The prior 0/822 independent QA status remains.

## Coverage inventory beyond current 123 held checks
- Direct XLSX row count **426** = EL275 + LE51 + NO100.
- V241 source-sample `PUBLISHED_SAMPLE_CANDIDATE` groups **415**, but **414 distinct source rows**, because EL row159 is shared by QABC-0143 and QABC-0568. These are two grade-route QABC records with a common source question; not an authorization to automatically delete either.
- **12 uploaded workbook source rows are not referenced by any V241 QABC**:
  - Electrotehnică: `15, 30, 31, 32, 39, 43, 44, 65, 117, 176, 181`;
  - Legislație: `7`;
  - Norme tehnice: `none`.
- Of these 12, **9 are figure/schematic-dependent** (EL15,30,31,32,43,44,117,176,181) and **3 primarily textual** (EL39,65; LE7). Some exclusions may be deliberate; investigate provenance/intended dataset scope before classifying as imports to add. **Do NOT automatically expand or regrade the 822 current grade IDs.**
- Gap inventory: `V245_UPLOADED_426_SOURCE_ROWS_VS_414_MAPPED_12_UNMAPPED_ORIGINAL_2026_11_21.json`.

## Diagrams: important recovered source material
- Electrotehnică workbook DrawingML contains **vector shapes/grouped drawings**, not just standard JPEG/PNG attachments. Direct XML inspection detected **128 drawing anchor records**, many parts of common diagram groups, not 128 independent diagrams.
- Rendered source workbook directly via artifact_tool, **EL rows 174–175**. The original **H inferior and H superior** substation bridge schematics are visible alongside original A/B/C at the exact question rows. This closes the narrow `ORIGINAL_H_BRIDGE_FIGURE_MISSING` data-access blocker for **QABC-0158 (EL174)** and **QABC-0159 (EL175)**. **It does not close their source-model/technical-answer QA holds**; future reviewer should inspect diagram and identify switching positions and topological conditions.
- QABC-0024 EL35 asks for the `schema de mai sus`. Vector shapes are anchored in the vicinity (EL34–35), but the automatic spreadsheet renderer omitted a complete readable diagram in an excerpt. **Authentic visual-to-question alignment still pending**. Do not claim the exact schematic has been visually verified or invent its components.
- Other vector-heavy/excluded cells include EL15, EL30–32, EL43–44, EL117, EL176, EL181. Image-free CSV extraction loses their essential input; perform vector-aware render/extraction and visual QA before any use.
- The actual source XLSX contains no standard image-media files; drawings are inside `xl/drawings/drawing1.xml`. Source content is user-provided, and in-repository JSON references alone cannot substitute a rendered diagram for a diagram-dependent question.

## Why this matters for approval and next step
- **What is now source-grounded:** all 3 uploaded XLSX parsed successfully; source A-D content for 123/123 held published candidates matches recorded editorial originals after text normalization; H bridge figures recovered; entire A-D source-to-V241 coverage gap inventoried.
- **What is NOT proved:** these are the current byte-identical ANRE-hosted files; imported grade-specific answer keys are ANRE-authenticated; normative I7/PE155/legal paragraph correct for 2026; a second qualified technical/legal and independent linguistic reviewer has approved any of 822 routes; before/focus/after *normative* quote windows are populated.
- Next **not another blind triage**: use original question A/B/C to evidence-gate historic strict six and priority candidate key conflicts. Independently source-validate applicable norm and immediate preceding/focus/following clauses, confirm official exam scoring or mark uncertainty. Audit 12 source-only rows for intended inclusion with diagram integrity; never change target 822 absent approved scope decision.
- User-approved future app behavior persists: **one original-source preceding sentence/paragraph, central exact passage in bold, one following sentence/paragraph, edition and offline anchor**, with A/B/C editorial explanation separate.
- **No imported key, original question/option text, HTML, APK, app build, stable branch or PR merge/release touched in this source retrieval.**
