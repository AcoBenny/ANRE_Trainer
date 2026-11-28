# CKPT-421 | ANRE GFR 100 / 822 validated for educational content

Date 2026-11-23 | Parent CKPT-420 | PR #7 Draft; no merge.

**Target met exactly:** 50 → **100 / 822 G1+G2 grade routes**, +50 routes from **25 distinct original QABC groups**, each with one matching G1 and G2 key. Distinct validated QABC **28 → 53 / 568**.

| Status | Before | After |
|---|---:|---:|
| Validated educational-content grade routes | 50 | **100** |
| Validated QABC groups | 28 | **53** |
| Historical held grade routes | 200 | 200 |
| Not held, still requiring actual evidence decision | 572 | **522** |
| All grade routes registered | 822 | 822 |

## New verified teaching cards

| QABC | Grade IDs / untouched imported keys | Technical logic and model qualifier |
|---|---|---|
| QABC-0029 | G1-ELE-034=C / G2-ELEC-182=C | Neutral izolat, defect monofazat net și rețea ideală echilibrată: tensiunea fază-pământ sănătoasă crește cu √3. |
| QABC-0035 | G1-ELE-042=B / G2-ELEC-188=B | AC serie R=3Ω X=4Ω: |Z|=5Ω și 220V/5Ω=44A (tensiune eficace). |
| QABC-0037 | G1-ELE-044=C / G2-ELEC-190=C | Lampa incandescentă cu filament de wolfram: creșterea tensiunii nominale de funcționare micșorează durata de viață. |
| QABC-0049 | G1-ELE-056=A / G2-ELEC-202=A | Suma algebrică a tensiunilor pe condensatoare în serie dă tensiunea la bornele lanțului. |
| QABC-0051 | G1-ELE-059=C / G2-ELEC-204=C | În stea simetrică Ulinie=√3 Ufază, dar Ilinie=Ifază. |
| QABC-0052 | G1-ELE-060=A / G2-ELEC-205=A | Efectul pelicular și curenții turbionari sunt exploatați la încălzirea prin inducție, dependentă de frecvență. |
| QABC-0057 | G1-ELE-065=C / G2-ELEC-210=C | La debutul defectului și înaintea declanșării, scurtcircuitul micșorează impedanța și ridică curentul de defect. |
| QABC-0058 | G1-ELE-066=A / G2-ELEC-211=A | Conservarea sarcinii nete electrice, chiar dacă perechi opuse se pot produce fizic. |
| QABC-0060 | G1-ELE-068=A / G2-ELEC-213=A | B*i*l este modulul forței pe conductor perpendicular pe B, în câmp aproximativ uniform. |
| QABC-0066 | G1-ELE-074=A / G2-ELEC-219=A | Conductoare jumelate la LEA reduc gradientul câmpului la suprafață și pierderile corona. |
| QABC-0071 | G1-ELE-079=A / G2-ELEC-224=A | Legea Faraday: mărimea FEM induse e proporțională cu derivata temporală a fluxului; Lenz stabilește semnul. |
| QABC-0108 | G1-ELE-117=A / G2-ELEC-259=A | Pentru conductor drept lung H=i/(2πr), deci proporțional cu 1/r. |
| QABC-0110 | G1-ELE-119=C / G2-ELEC-261=C | La pornirea RL în c.c. curentul crește către U/R asimptotic, după câteva constante de timp. |
| QABC-0111 | G1-ELE-120=C / G2-ELEC-262=C | RL serie ideal sinusoidal: U=√(100²+70²)≈122V, nu suma aritmetică. |
| QABC-0118 | G1-ELE-127=A / G2-ELEC-267=A | Puterea aparentă √(4²+3²)=5kVA, factor de putere P/S=0,8. |
| QABC-0121 | G1-ELE-130=A / G2-ELEC-270=A | Circuit rezistiv ideal: I=100V/5Ω=20A. |
| QABC-0126 | G1-ELE-135=B / G2-ELEC-275=B | Rezistențe în paralel: 1/Req=Σ1/Rk. |
| QABC-0200 | G1-ELE-211=B / G2-ELEC-347=B | Trei rezistențe egale 3Ω în paralel: Req=1Ω. |
| QABC-0201 | G1-ELE-212=A / G2-ELEC-348=A | Rezistivitatea este proprietate de material și temperatură, nu lungime sau masă conductor. |
| QABC-0224 | G1-ELE-235=B / G2-ELEC-371=B | Tensiunile electromotoare ale unui sistem trifazat simetric au sumă fazorială nulă. |
| QABC-0228 | G1-ELE-239=A / G2-ELEC-375=A | Tesla (T) este unitatea inducției magnetice B; fluxul este în Wb, H în A/m. |
| QABC-0231 | G1-ELE-242=C / G2-ELEC-378=C | Stea echilibrată la 400V între linii: tensiunea pe fază este 400/√3≈230V. |
| QABC-0040 | G1-ELE-047=A / G2-ELEC-193=A | Pentru bobină ideală liniară, armonicile de rang mai înalt ale curentului sunt diminuate față de tensiune. |
| QABC-0041 | G1-ELE-048=A / G2-ELEC-194=A | Condensatorul ideal amplifică relativ armonicile curentului față de armonicile tensiunii nesinusoidale. |
| QABC-0202 | G1-ELE-213=A / G2-ELEC-349=A | Rezonanța de serie în model RLC simplu când |XL|=|XC|, reactanța netă nulă. |

## QA and anti-loop
- Every original A/B/C, source draft blob SHA and grade-specific matching answer imported from existing editorial card and master ledger. **No repeat source inventories** and no prior validated groups selected again.
- Two separate external AI technical reviews actually executed, IDs `resp_1762244d-f787-41bc-868b-0576b059b681` and `resp_0599a40f-eb9e-4097-a5b8-8da60a251669`, compared options and tested model counterexamples. From 30 candidates, **2 explicitly conditional** (0064 attenuation terminology and 0107 electric-field gradient) were excluded, plus 3 more nuanced candidates (0106,0053,0054) withheld. The 25 accepted all received source-backed teaching-model PASS with caveats.
- **Sources are historically researched URLs, not all fetched live in this session.** We do not certify scored ANRE answer provenance or full source edition. The source and model conditions are preserved. Product HTML/APK, offline text paragraph context, rights and release QA are later independent product tasks.
- 25 unique QABC, 50 unique grade IDs, no grade key drift, no merge/release, no canonical bank or application changes. Only docs and checkpoint updated.

## Next GFR, only after explicit instruction
Use `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_421_568_QABC_MASTER_2026_11_23.json` and `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_421_822_GRADE_MASTER_2026_11_23.json` as authoritative progress, never older CKPT-420 counts. Start with as-yet unapproved QABC only; use source A/B/C files and targeted independent challenger; mark model-conditional cases held without forced approvals. Goal later: steady real increase toward 822, with held 200 routes handled independently. No new research that merely recatalogs old reports.

## Documents
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_421_25_QABC_50_ROUTES_PROOF_PACK_2026_11_23.json` full 25-case proof packet
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_421_568_QABC_MASTER_2026_11_23.json` 568 QABC master
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_421_822_GRADE_MASTER_2026_11_23.json` 822 G1/G2 route master
- root `ACTIVE_HANDOFF.md` updated.
