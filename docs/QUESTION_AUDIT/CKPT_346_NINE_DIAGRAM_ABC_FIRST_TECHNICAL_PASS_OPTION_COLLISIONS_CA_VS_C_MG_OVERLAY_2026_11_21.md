# CKPT-346 | Nine original ANRE vector diagrams: first technical A/B/C review and negative regressions | 2026-11-21

## What genuinely ran
- Branch head before additions: `78f6d523a7c560e8e4a39f5d7d842dbe163f352d`; PR #7 still Draft. **Original workbook source hash** `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c` matched the user's historical source evidence (V246/V257).
- Read-only Python OOXML regression suite **18/18 structural tests PASS**: 9 original source anchored rows, 36 anchors, 330 original nested shapes; all original image answer placements, repeated-shape fingerprints, literal CA marker, overlapping generator/motor symbols, literal S11. The script/tests and exact-geometry option plate are in a local user-downloadable QA package; neither script execution nor visual reconstruction constitutes official scoring validation.
- Two separate real Parallel AI research calls were made for busbar couplers and cell/motor/generator topics. **Second AI was NOT a qualified electrical reviewer and DID NOT see the local original images**, so its answers were treated as contestable hypotheses; one internal contradiction about S2 was explicitly rejected.

## Original source diagram pass (not new canonical grade-route validations)
| ANRE user-XLSX source row | A/B/C provisional assessment | Provenance / remaining hold |
| --- | --- | --- |
| EL15, equipment marked C | Candidate **B**, but original graphic literal marker **CA**, not C | original stem-label mismatch; exact circle symbol still needs expert review |
| EL30, two diagonal couplers | **A** may support two *alternative* cross connections | A diagram is fingerprint-identical to EL31.A and EL32.A; alternative-vs-simultaneous question |
| EL31, two longitudinal couplers | **A** may support two *alternative* same-level connections | A fingerprint-identical to EL30.A; B/C require actual graph/switch state tracing |
| EL32, two transverse couplers | Third-party suggests **C**, NOT authenticated | C diagram fingerprint-identical to EL31.C; true transversal path/number not independently proven |
| EL43, compartment no.2 | Candidate **B** switchgear | 2 is lower-right, 3 lower-left, 4 upper-right; source diagram common to EL15/EL44 |
| EL44, compartment no.3 | Candidate **A** cable/network connection | same original figure with no.3 lower-left |
| EL117, line circuit topology | Candidate **C** working bar plus bypass bar | second bus leads to line downstream of the ordinary breaker, not normal pre-breaker selection |
| EL176, motor, two isolators | **C** if non-backfeeding motor-load model; A may be justified by two-side maintenance isolation | exact motor/fault/lockout context is missing; alternatives not final |
| EL181, generator, two isolators | **B** under cited *generator reliably stopped during breaker maintenance* teaching model; **A** under other safe two-sided isolation models | **original source itself** has M/G overlapping at same XY, additional shifted G drawing and literal S11; no pristine one-image assumption |

## Important new source assertions verified by exact bytes
- **Options provenance:** EL30/31/32 graphical alternative A resides in Excel column B, B in C, C in D. Option A's normalized source-vector hash is IDENTICAL across all three rows: `1256c37b5a36ef1dbe59669e564fb2b35d76ab4bf3f529589e25c12b9bf25519`. Option C's normalized source-vector hash is IDENTICAL between EL31 and EL32: `88deae6f61a535a2482c26e5c6d5e7a73d60cf64ba76c4062c4dfa9ec3ef8849`. Similarity is not only a raster coincidence.
- **Graphical label trap:** original vector group used in EL15/43/44 includes text element **CA**. EL15 original question asks for **C**. This is not caused by generated SVG text concatenation: the literal original XML has a single text run with `CA`.
- **Double source overlay:** original EL181 drawing XML contains `M` and `G` at identical `(x=3810000,y=115995450)` and a second G at `y=116709825`, with **22 anchors** and literal **S11**. The original workbook may have stale overlapping objects or two intended images; an original native Excel screenshot is still needed to establish the exact visible layer.
- **Secondary AI result rejected:** one external model argued S2 is needed when the generator can backfeed yet called S2 'extra'. That does not follow. A mirrored university course text instead explicitly conditions the omission of generator-side separator on the generator being stopped during maintenance: https://www.studocu.com/ro/document/universitatea-politehnica-din-timisoara/instalatii-electrice-1/curs-iec-instalatii-electrice-de-conexiuni/6623276 . That textbook context is an interpretation, **not a safe live operational instruction** and not an official exam key.

## Completion/QA gates
- [Structured V258 evidence](V258_NINE_ORIGINAL_VECTOR_DIAGRAMS_A_B_C_SEMANTIC_NEGATIVE_QA_18_OF_18_TESTS_2026_11_21.json): all **9 original stem and A/B/C or graphical alternative links**, separate reasoning for each alternative, source row SHA and remaining conditions.
- **18/18 source-structure tests pass, 0/9 independently signed-off technical image answers, 0 newly imported QABC**, 0 changed imported keys; canonical target remains 568 QABC/822 grade routes. Known 136 semantic holds plus 6 historic strict subset remain open; **0/822 learner-approved**.
- Pixel-identical Excel rendering was NOT_RUN; original-source edition ANRE server bytes not rehashed here; no qualified reviewer, no official scoring key.
- Original XLSX, bank questions/answers, HTML, APK, `main`, merge/release untouched.

Next: explicit graph connectivity test for EL30–32 (not counts alone); native Excel screenshot / visibility of EL181 overlapping M/G; qualified specialist and exam-key check. No automatic learning release.
