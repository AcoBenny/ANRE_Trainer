# CKPT-349 | EL181 original Excel native vector duplicates, source-layer forensic | 2026-11-21

Source workbook `ELECTROTEHNICA-09.2024-2.xlsx`, SHA256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`. Original row EL181 in `xl/drawings/drawing1.xml`, first anchor at zero-based sheet row 180.

## Direct OOXML evidence (not inferred from image recognition)
- **22 xdr:twoCellAnchor objects, 30 nested xdr:sp shape objects** for EL181.
- Original object order: **anchors 1–10** draw a switch line with **M** motor; **11–20** draw a parallel source figure with **G** generator; **21** one extra line; **22** a source-original grouped figure with nine shapes including **G**.
- Paired original **first ten vs second ten match exactly 10/10 in spreadsheet-cell anchor coordinates AND 10/10 in full shape-properties XML**. They differ in text literal M vs G, and are not independent electrical source connections.
- Original text shape for S11 comes as three runs `S`, `1`, `1`. We keep the literal evidence instead of auto-correcting to S1. A renderer drawing `S 1 1` cannot prove an author-intended label.
- SVG/PNG was reconstructed for each of the four source layers and the full composite, side-by-side montage; **29/29 executable exact-source geometry tests PASS**. The original workbook remains unmodified.

## Consequences
1. It is **source-native duplication** and not merely a mistake of the SVG renderer. The prior CKPT345/346 notation that EL181 picture has duplicate M and G is validated in XML.
2. The source contains multiple overlapping generator candidates. One can inspect isolated source layers; **native Microsoft Excel final visible z-order, field interpretation and author intent still not proven**.
3. Generator shutdown/backfeed conditions and isolation goals affect the meaning of 'aparat în plus'. A didactic answer based on generator being stopped is **not a safe instruction for real electrical isolation**. The official source row and existing A/B/C variants stay unchanged; the scoring key remains **HOLD**.
4. Do not overwrite/delete the earlier M source shapes, change the canonical answer options, import the source-only row into the 822 grade routes or release learner cards.

## Traceability
- Detailed [V261 evidence record](./V261_EL181_ORIGINAL_XLSX_M_G_DUPLICATED_10_OF_10_SHAPE_XML_LAYER_FORENSIC_29_TESTS_2026_11_21.json).
- User-downloadable standalone QA package `ANRE_CKPT348_349_full_option_models_and_EL181_layers.zip` with actual Python scripts, 39/39 conditional 3×3 coupler tests, 29/29 exact-source duplication checks, nine source-option images and row181 separated-layer montage.
- Before reviewer signoff: native Excel rendering inspection for original layer visibility; independently confirm schematic electrical meaning in applicable edition and any official scoring errata.

**Baseline hold remains:** six original strict conflicts remain open, 136 explicitly semantic-hold groups, **0/822 independently learner approved**. PR #7 Draft documentation-only; no questions, keys, HTML, APK, `main`, merge or release changed.

