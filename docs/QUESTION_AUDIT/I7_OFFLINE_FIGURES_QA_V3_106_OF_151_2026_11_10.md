# I7 offline library | Figure recovery V3 | 2026-11-10

## Result and source boundary
User requested continuation of exact missing figures recovery for offline I7 library (original portal HTML saved by user, source identifier `287132`). **106 / 151** referenced visual elements are now available in a standalone offline HTML **conversation artifact**, including **82 images previously recovered from an I7 PDF archived at 2023-09-22** and **24 archival PDF section crops (17 appendix tables + 7 labeled figures/tables/map)**. **45 still missing**. **No current official portal JPG image was downloaded or certified.**

- User HTML original filename `REGLEMENTARI (A) 01_11_2011.htm`, SHA256 `99389c372d898dea067b80a93e1998f93a1b03302812e478de327ff2013d90b7`. Its official reference is `https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132`.
- Historical 2023 I7 PDF available via the user's own Files Library `803493174-I7-2011-completat2023.pdf` (249 pages, 2023-09-22 synthetic consolidation). **No publishing of this source PDF** to GitHub.
- The government portal returned HTTP 502 via live web read, and container outbound requests failed DNS; links to unverified web imagery, Scribd and third-party mirror results were **not substituted** for official JPG assets.
- `I7_2011_OFFLINE_figuri_106_ARHIVA_PARTIAL.html`: **12,199,310 bytes**, SHA256 `b2620e262a557a59d3044ae3616e6f80cd66c77ab94ebdb03b863f2484063a00`.
- `I7_2011_OFFLINE_106_figuri_QA.zip`: **5,895,251 bytes**, SHA256 `db4c8b3a8c9914eb912d3eaf9b9861d145a9295c429475902438b5976557fb6e`.
- CSV `I7_2011_RECUPERARE_figuri_QA_v3.csv` has **151 rows**, one for each originally missing image with provenance and source page/method. Conversation download artifacts were supplied; **neither the 12 MB HTML nor copied third-party document content was committed to GitHub** pending source-rights and currentness QA.

## New validated source crops, 24 added after prior checkpoint
17 annex-heading-anchored sections, extracted as high-resolution facsimiles from the user Library 2023 PDF, with exact beginning and next-section boundaries:

- Annexes **5.10–5.17, 5.19–5.22, 5.24–5.28**, including conductor permissible current ratings, insulation/installation configurations, grouping and correction factors. Multiple PDF-page sections assembled in section order; **not** claimed to be original 2026 JPG bytes.
- Seven additional manually visually inspected locator crops: original image `nr 1` (Table 3.6 electrical earthing symbols, PDF page 16); `nr 33` (Table 6.4 lightning damage, page 81); `nr 104` (IP code diagram, page 186); `nr 134` (Table A5.34-1, pages 212–213); `nr 135` (Table A5.34-3, page 214); `nr 136` (Table A5.34-4, pages 214–215); `nr 147` (Annex 6.11 keraunic map, page 246).
- The reader explicitly labels each new crop as **2023 archival**, and is dated/consultative, not an assertion of 2026 legal completeness.

## QA actually executed
- **106/106** embedded base64 image objects decoded and passed Pillow file integrity.
- **184/184** HTML tables from original retained; **106** figure nodes and **45** explicit `missing-figure` warnings (no silent substitutions).
- Actual headless Chromium network-blocked test used `page.set_content` because this environment blocks direct `file://` navigation; lookup `5.2.12.3.10` yielded 1 result, clicking navigated to `#id_pctA2193`; 6 archival image samples reported `complete=true`, dimensions valid; **0 page JS errors**, **0 remote network requests**.
- ZIP archive integrity check PASS; all downloadable file paths explicitly verified in current container.
- Test provenance: structural and browser rendering tests, **NOT** independent electrician QA, normative-currentness QA, exact source JPG equivalence, physical Android/WebView test, or current manual-by-manual migration.

## Remaining 45
- 23 technical figures/formula/symbol image references before the annexes (nos. 14..94), including protection symbol markers and mathematical graphics.
- 18 appendix layout/figure-page images (nos. 97..115), many multi-page source table fragments which require unambiguous page-to-image mapping.
- 4 other (nos. 133, 137, 144, 146), primarily diagrams/formulas and a reference table.

Do not misreport 106 images as 106 **exact official JPG** replacements: 24 are PDF section crops, and all 106 are from an archive not confirmed identical to 2026 portal content. Future stage: recover official JPGs if possible; otherwise map visual page crops with exact label and inspect mathematical content and editions individually. Keep every unresolved item labeled. No claim of current legal certification.

## Change gate
This is **documentation-only** on the GitHub PR #7 Draft. No edits to original question keys, ABC/options, canonical HTML, APK, app assets or `main`, no merge or release. Independent technical/source/linguistic QA and user approval remain required before final source replacement.
