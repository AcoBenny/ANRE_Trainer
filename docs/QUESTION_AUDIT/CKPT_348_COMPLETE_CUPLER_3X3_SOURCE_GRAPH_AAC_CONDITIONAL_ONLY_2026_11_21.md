# CKPT-348 | All 9 original graphical A/B/C coupler choices compared | 2026-11-21

Parent HEAD `2f68b19da7d12103d00722827d507539421a9fd4`; PR #7 Draft. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` SHA256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`. This checkpoint extends CKPT-347 by actually modeling **EL30.B, EL30.C, EL31.B, EL32.B** instead of excluding them.

## Source graph transcriptions

| Source diagram | Through-assumed-breaker pairs | Two paths / potential type | Known visual caveat |
|---|---|---|---|
| A, same original fingerprint in EL30/31/32 | {L_UP,L_DOWN} × {R_UP,R_DOWN} via ONE X | 2 longitudinal, 2 diagonal, alternate | Not 2 simultaneous independent breaker circuits |
| EL30.B | {L_UP,R_DOWN} × {L_DOWN,R_UP} via ONE X | 2 longitudinal, 2 transversal | No diagonal **through** X |
| EL30.C | L_UP-R_UP; L_DOWN-R_DOWN | 2 longitudinal by geometric terminals | Circle and cross-in-circle symbol identity unresolved |
| EL31.B | L_UP-R_DOWN **and** L_DOWN-R_UP, two X branches | 2 diagonal | Unlike EL30.B; cannot equate by component count |
| EL32.B | L_UP-R_DOWN **and** L_DOWN-R_DOWN, two X branches | 1 diagonal, 1 longitudinal | Possible RU/RD unprotected tie; graph junction/source visibility not fully certified |
| C, same fingerprint EL31/32 | {L_UP,R_UP} × {L_DOWN,R_DOWN} via ONE X | 2 transversal, 2 diagonal, alternate | Not independent simultaneous circuits |

Definitions: longitudinal = same bus level across two sections; transversal = upper/lower bus systems on same section; diagonal = crossed level and section. Drawing figures are user-original OOXML shape assets; our parsed SVG renderer is **not pixel-identical to Excel**. All graph labels and connections were **manually transcribed**, so test outputs are conditional.

## Real test results and provisional choices

Real Python script `anre_ckpt348_all_busbar_graphs.py` executed **39/39 passing assertions**: nine source graphical option hashes, six distinct diagrams, duplicate-image negative checks, pair classifications, breaker-count restrictions and conditional per-question comparisons. All actual inputs, test names, output and local scripts are preserved in the QA ZIP attached to the conversation. Tests validate the *model rules*, not independent source-electrical correctness.

- **EL30 diagonal:** A gives 2 alternate diagonals; B and C give zero diagonal through relevant drawn X under source model. **A provisional**.
- **EL31 longitudinal:** A gives 2 alternate longitudinals; B is two diagonal branches, C is transversal/diagonal. **A provisional**.
- **EL32 transversal:** C gives 2 alternate transversals; A yields none; B's apparent direct RU/RD tie is not a proper breaker-switched transversal. **C provisional**.

The structural analysis resolves a *model-comparison gap* from CKPT-347. It **does not** authenticate the original question answers or approve these source-only rows for the canonical 822 bank. Official exam rules still require one correct answer. The older question wording 'două circuite' may describe two selectable functions rather than two concurrently independent breakers.

## External context and stop gates

Comănescu/Costinaș Romanian substation course text on [combined multi-function bus couplers and fig. 3.16](https://www.academia.edu/12426427/SCHEME_PRINCIPIALE_FOLOSITE_PENTRU) expressly describes multiple coupler functions realized *in turn* and the difference between longitudinal, transversal and diagonal. This is a scraped course preview, not an authoritative ANRE scored-answer key and not pixel proof of the workbook source circuit.

For detailed input/proof: [`V260_NINE_GRAPHICAL_OPTIONS_ALL_A_B_C_MANUAL_NETLIST_39_ASSERTIONS_PROVISIONAL_AAC_2026_11_21.json`](./V260_NINE_GRAPHICAL_OPTIONS_ALL_A_B_C_MANUAL_NETLIST_39_ASSERTIONS_PROVISIONAL_AAC_2026_11_21.json).

**STOP gates:** native Excel visually verified junctions and electrical symbols (particularly EL30.C and EL32.B), qualified technical/linguistic review, 2026 exam key authenticity and actual grade mapping. These remain **0/822 learner approvals**; **136 explicit semantic holds and 6 pre-existing strict conflicts unchanged**. No original answer keys, questions, HTML, APK, main or merge/release changed.

