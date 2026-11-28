# CKPT-345 | ALL 9 original ANRE XLSX vector diagrams RECOVERED, source-anchored | 2026-11-21

## Material breakthrough after CKPT-344
- Original user-uploaded source was found **directly in user's file Library**: `ELECTROTEHNICA-09.2024-2.xlsx` (67,250 bytes). The same exact SHA-256 appeared on **4** distinct historical user upload copies and matches **V246** recorded user original Excel hash: `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`.
- The missing diagrams are **NOT** embedded raster photos (`xl/media` count **0**). They are native Excel vector shapes in `xl/drawings/drawing1.xml` (SHA256 `c3339775430c6e7838405ef21c26bdd9b81426a88816fb5b15746ee20c958689`). Original XML has **128 drawing anchors, 477 shape elements**.
- Nine missing source rows confirmed by `xdr:twoCellAnchor/from/row` and shapes within each anchor. These nine rows jointly have **36 anchors and 330 original source shapes**. Rows EL30–32 contain **three separate image-choice schemes anchored at original Excel columns B, C and D** (the A/B/C choice locations), even when the textual extraction reports A/B/C blank.
- An actual read-only renderer parsed the original OOXML shapes (groups, rotations, flips, lines, circles, rectangles, labels) into **9 SVG and 9 PNG previews**, and one montage; ZIP package passed extraction CRC/self-test and all nine PNGs were checked as nonblank. Rendering is **approximate**, not a pixel-perfect native Excel/OOXML rendering.

| Original workbook row | Anchors | Source shapes | Graphic-column meaning |
|---:|---:|---:|---|
| EL15 | 1 | 34 | A = drawing alongside textual choices |
| EL30 | 3 | 61 | B,C,D = graphical answer choices |
| EL31 | 3 | 57 | B,C,D = graphical answer choices |
| EL32 | 3 | 57 | B,C,D = graphical answer choices |
| EL43 | 1 | 34 | A = drawing alongside textual choices |
| EL44 | 1 | 34 | A = drawing alongside textual choices |
| EL117 | 1 | 13 | A = drawing alongside textual choices |
| EL176 | 1 | 10 | A = drawing alongside textual choices |
| EL181 | 22 | 30 | A = drawing alongside textual choices |

## What this closes, and what it does NOT
- **CLOSED in source-evidence workflow:** `MISSING_ORIGINAL_XLSX_VECTOR_GRAPHIC` for all **9/9** previously missing source-only diagram rows. The original vector shapes are actually present and traceable to the same source XLSX as the question wording.
- **STILL OPEN:** publication-site exact binary identity as at 2026-11-21 (network could not download official hosted workbook directly; user original hash is known), native Microsoft Excel pixel-perfect rendering, independent electrical expert interpretation of all figures, official 2026 keyed answers, and source-only row placement into grade-specific canonical 822 routes.
- Earlier V256/CKPT343 third-party candidate images remain historical research pointers, **not** original/official image evidence; DO NOT infer those JPEGs match the original at a byte level or copy them to app.
- Diagnostic anomaly: EL181 contains 22 anchors and repeated vector elements; the approximate renderer displays duplicated generator drawings. Original drawing anchors need Excel native view or additional OOXML grouping analysis before a pixel-fidelity pass.
- The ZIP of reconstructed previews and local script exist as conversation artifacts, not uploaded to GitHub: manifest includes per-row exact original anchor SHA256 for reproducibility, and source itself remains unchanged.

## Source gates & safe continuation
- Evidence JSON: [V257_ORIGINAL_XLSX_9_VECTOR_GRAPHIC_ROW_ANCHORS_36_330_SHA256_VERIFIED_2026_11_21.json](./V257_ORIGINAL_XLSX_9_VECTOR_GRAPHIC_ROW_ANCHORS_36_330_SHA256_VERIFIED_2026_11_21.json). Formal overall answer signoff **still 0/822**, 136 known semantic holds, 6 historic strict conflicts. No claim that an original diagram provides an exam score key by itself.
- No question bank stem, variants, imported keys, HTML, APK, `main`, merge, or release changes. Only documentation in audit branch.
- Next: direct A/B/C technical review of the original row 15/30/31/32/43/44/117/176/181 graphics using the source shapes and exact question stem, verifying electrical semantics and hidden exceptional conditions; then independent reviewer gate. Reuse existing QABC records and avoid duplicate explanations.
