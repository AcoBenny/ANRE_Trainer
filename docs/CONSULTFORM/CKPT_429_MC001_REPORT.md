# CKPT-429 | ANRE-MC-001 completed

2026-11-27 | Draft PR #7 | [crosswalk](CKPT_429_CROSSWALK_305.json) at commit ad1d078395590a2c2ad758d0f0467a6b25896315.

- 305 distinct CONSULTFORM rows (104 LEG + 201 NOR). Read both solved worksheets locally; source workbook SHA256 matches staging, all 305 Q/A/B/C/reference fields and keys match source cells; yellow marking agrees with staging on all 305. No source answer re-adjudication.
- Full normalized stem + sorted A/B/C set compared with existing 568 legacy groups, joined to CKPT-427 IDs/card locators. Normalize case, diacritics, whitespace, terminal punctuation and quotation variants; second pass permits commas/semicolons/colons/parentheses/quotes only, no substantive fuzzy match. 140 matches, all G1; 165 unmatched -> both G1/G2 per owner. No duplicate input identity. 24 matched questions differ in legacy correct option text; preserve old key metadata and use CONSULTFORM answer. No option reorder detected among matched rows.
- Legislation: 50 G1-only + 54 common via default = G1 104 / G2 54. Norms: 90 G1-only + 111 common via default = G1 201 / G2 111. Combined 305 unique questions, 470 grade memberships (G1 305, G2 165). No claim that unmatched questions are officially assigned to both grades; this is the requested Trainer policy.
- 304 references available; CF-LEGISLATIE-056 missing reference, key B remains accepted. MC-002 to fill locator/cards as possible, check compatibility of reused explanations with supplied answer, no new key audits.
- Published row/grade/key/reference and old ID/card crosswalk, not raw copyrighted workbooks or full text. Full text remains in attached source XLSX/staging JSON. Next session needs these inputs or the corresponding extracted data. No HTML/APK modification, no CI, no merge/release.
- Readback crosswalk: {"total":305,"unique":305,"g1":305,"g2":165,"invalid":0}. Structural checks only, not certified answer correctness. CKPT-427 evidence retained.

NEXT: ANRE-MC-002 (#15), map the 305 source rows to reusable educational cards and referenced passages; prioritize 140 matched card locators, then 165 unmatched. Electrotechnics MC-003 still blocked.
