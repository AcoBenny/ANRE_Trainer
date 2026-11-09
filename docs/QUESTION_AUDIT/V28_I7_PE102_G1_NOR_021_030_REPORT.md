# V28 | G1-NOR-021–030 I7/PE 102 source and trap review

Date: 2026-11-09. Source: user Library `803493174-I7-2011-completat2023.pdf` (I7 sintetic 22.09.2023, 249p) and `95312451-Normativ-Proiectare-Si-Executare-Instalatii-Electrice-Pana-La-1000V.pdf` (older PE102-like 271p). Exact article/page only if actually found in these documents; absent sections deliberately `SOURCE_GAP`. Canonical V10.29 unchanged; independent QA `NOT_RUN`.

## Per question
| ID | Stored key | Supported / under review | Evidence | Status |
|---|---|---|---|---|
| G1-NOR-021 | A | A_WITH_CHEMICAL_CONDITION | 5.1.7.2(b), PDF p.49 | CONDITIONAL_SCOPE |
| G1-NOR-022 | C | C | 5.4.7, PDF p.70 | SOURCE_MATCH |
| G1-NOR-023 | A | NOT_ADJUDICATED | NOT_LOCATED_I7_2023, PDF p.not found | SOURCE_GAP |
| G1-NOR-024 | B | B_PRINCIPLE_ONLY | PE_SWITCHING_PROHIBITION_EXACT_ARTICLE_NOT_LOCATED, PDF p.not found | SOURCE_GAP |
| G1-NOR-025 | B | B_IN_OLDER_PE102 | PE102 art.5.2.62; I7 5.3.3.20, PDF p.127 PE102 / 65 I7 | EDITION_SCOPE_RISK |
| G1-NOR-026 | A | A_PRINCIPLE_ONLY | PE_FUSE_PROHIBITION_EXACT_ARTICLE_NOT_LOCATED, PDF p.not found | SOURCE_GAP |
| G1-NOR-027 | B | B_NOT_VERIFIED | SCREW_FUSE_SUPPLY_SIDE_NOT_LOCATED, PDF p.not found | SOURCE_GAP |
| G1-NOR-028 | C | C_WITH_EXCEPTIONS | 5.2.6.6, PDF p.56 | CONDITIONAL_TRAP |
| G1-NOR-029 | B | C | 5.3.3.21, PDF p.65 | CANONICAL_KEY_CONTRADICTS_I7 |
| G1-NOR-030 | A | A_NOT_VERIFIED | COLUMN_SECTION_UNIFORMITY_NOT_LOCATED, PDF p.not found | SOURCE_GAP |

## Priority traps
- **G1-NOR-029:** I7 art.5.3.3.21, p.65 gives standard max height **2.3m** for distribution board top, but explicitly *excepts apartment/house installations* up to **2.5m**. Because question says **"din locuinţe"**, **C** is supported; canonical **B** ignores the exception. Mark as newly source-contradicted, no edit allowed.
- **G1-NOR-025:** PE102 art 5.2.62 p127 supports historic **15mm**, but I7 2023 art 5.3.3.20 p65 delegates to standard SR EN 60439 without this numeric threshold. Keep separate historical key from current-applicability claim; no silent answer change.
- **G1-NOR-028:** I7 5.2.6.6 forbids tensile loads on electrical joints but has explicit exceptions; absolute form needs explanation.
- **G1-NOR-021:** Cu in corrosive conditions is conditional on chemical instability of alternatives and inability to apply protective coverings; „întotdeauna” in stem is overly broad in isolation.
- **G1-NOR-023,024,026,027,030:** exact normative locator not found from available source and search; **not validated**.

## QA release gates
Class counts: {"CONDITIONAL_SCOPE":1,"SOURCE_MATCH":1,"SOURCE_GAP":5,"EDITION_SCOPE_RISK":1,"CONDITIONAL_TRAP":1,"CANONICAL_KEY_CONTRADICTS_I7":1}. Source PDF owned by user remains Library only, not republished. All 10 text/keys inspected; exact didactic sources for 5 remain unavailable, 3 conditional/historical, 1 direct and 1 contradictory. `INDEPENDENT_QA=NOT_RUN`, no actual HTML/APK tests. No question/barem or app edits; PR Draft, no merge.
