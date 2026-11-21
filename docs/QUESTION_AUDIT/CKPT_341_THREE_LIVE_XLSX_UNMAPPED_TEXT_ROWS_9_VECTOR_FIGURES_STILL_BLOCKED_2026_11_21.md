# CKPT-341 | 3/3 unrepresented source text questions reopened against LIVE ANRE XLSX | 2026-11-21

- Previous PR #7 Draft HEAD: `d258994011e4831c688397b7161d9dfff18f725e`; only audit-only additions permitted.
- Prior V175/V245 inventoried **426 original workbook question rows**, **414 unique used rows / 415 published QABC records**, leaving **12 source-only rows** (9 requiring figures, 3 textual). This checkpoint **does NOT repeat the completed 415 comparisons**.
- New live official ANRE XLSX reads on 21 November 2026: [Electrotehnică 09.2024](https://anre.ro/wp-content/uploads/2024/11/ELECTROTEHNICA-09.2024-2.xlsx) and [Legislație G1 05.2023](https://anre.ro/wp-content/uploads/2023/05/LEGISLATIE-GR.-1-05.2023.xlsx) both returned 200; the extracted original question and all A/B/C matched V175 in **all 3/3 textual source-only rows** after NFKC and whitespace normalization. This does not establish byte-for-byte XLSX identity, drawing fidelity, keys or current grade placement.

| Original row (source Excel mapping) | Scope | Candidate / core discovery |
| --- | --- | --- |
| **EL39** | Circulația câmpului magnetic pe un contur închis | A under **magnetostatics** (Ampère law), but the question does not state time-varying-field scope; Maxwell displacement current is an explicit qualifier |
| **EL65** | Two arbitrary 3-phase phasor systems with common tips and different origins | B under the common-translation model: V1 and V2 remain unchanged, V0 changes; option A says **«numai»** and is excluded because *both* direct and inverse stay equal |
| **LE7** | ANRE acronym and institutional name | C as source-supported agency expansion, without official 2026 scored-key certification |

## Negative/positive derivation for EL65
Let `a=e^(j 2π/3)` with `1+a+a²=0` and the same complex shift `d` applied to all three phases. Then `V1'=V1`, `V2'=V2`, but `V0'=V0-d`. A numerical independent recomputation with `(Va,Vb,Vc)=(2+3j, -1+0.5j, 0.2-2j)` and `d=1.4-0.3j` returned changes `|ΔV0|=1.4317821063`, `|ΔV1|=0`, `|ΔV2|=0`. The **word «numai»** is decisive for eliminating A; correct only if one common origin is assumed for all three vectors per system.

## Sources and three option rationales
- EL39: [Ellingson, Virginia Tech / LibreTexts magnetostatic Ampère law](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_I_(Ellingson)/07:_Magnetostatics/7.04:_Amperes_Circuital_Law_(Magnetostatics)_-_Integral_Form) specifies `∮ H·dl=I_enclosed` in magnetostatics, with time-varying E adding displacement current; zero and voltage-drop options are not general law.
- EL65: [Kirtley, symmetrical components teaching text](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Introduction_to_Electric_Power_Systems_(Kirtley)/04:_Introduction_to_symmetrical_components/4.01:_The_Symmetrical_Component_Transformation). The actual algebra is reproduced in V254; A is too exclusive, B survives, C does not under nonzero origin translation. Exact wording «origini diferite» must be checked against the intended graphic convention before signoff.
- LE7: [ANRE official institution](https://anre.ro/); option C spells out ANRE correctly, A/B do not.
- Full A/B/C from published source and qualifiers: [`V254_THREE_UNMAPPED_ANRE_OFFICIAL_XLSX_TEXT_ROWS_EL39_EL65_LE7_SOURCE_SCOPE_2026_11_21.json`](./V254_THREE_UNMAPPED_ANRE_OFFICIAL_XLSX_TEXT_ROWS_EL39_EL65_LE7_SOURCE_SCOPE_2026_11_21.json).

## Status and invariants
- **3/3** textual source-only gaps documented, not "imported", not "answer approved"; **9/9** diagram/vector source-only rows still need original DrawingML/figure-preserving inspection. The 822-bank target remains unchanged; 136 explicit known holds remain open; **0/822 independent learner approvals**.
- No changes to questions, keys, HTML, APK, base branch, merge or release. No truly independent qualified technical/legal/linguistic reviewer ran.
