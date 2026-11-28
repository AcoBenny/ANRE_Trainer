# CKPT-422 | ANRE GFR reaches 150 / 822 educational content validations

Date 2026-11-23, parent CKPT-421, Draft PR #7. **Increment exactly +50 G1/G2 grade records = 25 source-original QABC groups, no duplicates.**

| State | Before | After |
|---|---:|---:|
| Validated grade routes for teaching content | 100 | **150** |
| Validated distinct QABC groups | 53 | **78** |
| Historical-held routes | 200 | 200 |
| No historic hold but still awaiting adjudication | 522 | **472** |
| Registered total | 822 | 822 |

## Accepted QABC source and ABC rationale

| QABC | Preserved G1/G2 answer keys | Source-supported logic and scope |
|---|---|---|
| QABC-0173 | G1-ELE-184=A; G2-ELEC-320=A | Permeabilitate μ este mărime magnetică: B=μH în model liniar. |
| QABC-0174 | G1-ELE-185=A; G2-ELEC-321=A | Permitivitatea ε este mărime electrică, nu magnetică ori chimică. |
| QABC-0175 | G1-ELE-186=C; G2-ELEC-322=C | Regulatorul automat de tensiune modifică excitația generatorului sincron. |
| QABC-0181 | G1-ELE-192=A; G2-ELEC-328=A | Elemente feromagnetice uzuale: fier, nichel și cobalt. |
| QABC-0185 | G1-ELE-196=B; G2-ELEC-332=B | La paralel, rezistența echivalentă este sub cea mai mică rezistență de ramură. |
| QABC-0189 | G1-ELE-200=C; G2-ELEC-336=C | Releul termic protejează motorul contra suprasarcinilor; nu înlocuiește protecția de scurtcircuit. |
| QABC-0190 | G1-ELE-201=C; G2-ELEC-337=C | Trei rezistoare de 2Ω în serie: 6Ω. |
| QABC-0194 | G1-ELE-205=B; G2-ELEC-341=B | Puterea activă la generator sincron se controlează prin puterea mecanică a turbinei. |
| QABC-0195 | G1-ELE-206=A; G2-ELEC-342=A | Puterea reactivă a generatorului sincron este influențată de curentul de excitație. |
| QABC-0198 | G1-ELE-209=C; G2-ELEC-345=C | Transformator în gol: primarul alimentat, secundarul în circuit deschis. |
| QABC-0124 | G1-ELE-133=C; G2-ELEC-273=C | Regim sincron staționar: viteza câmpului statoric egală cu viteza rotorului. |
| QABC-0127 | G1-ELE-136=C; G2-ELEC-276=C | Turația mașinii sincrone legate la o sursă cu frecvență stabilă rămâne sincronă la variația sarcinii în limita stabilității. |
| QABC-0138 | G1-ELE-147=C; G2-ELEC-285=C | Feromagneticele au permeabilitate relativă mult peste 1 în domeniul tipic. |
| QABC-0139 | G1-ELE-148=B; G2-ELEC-286=B | Bobina ideală liniară: u=L di/dt; celelalte relații sunt pentru R și C. |
| QABC-0140 | G1-ELE-149=A; G2-ELEC-287=A | Legea lui Coulomb descrie forța între sarcini electrice punctiforme. |
| QABC-0144 | G1-ELE-153=B; G2-ELEC-291=B | Reluctanța, nu permeanta, corespunde rezistenței magnetice. |
| QABC-0149 | G1-ELE-158=A; G2-ELEC-296=A | Tolele rotorice reduc curenții turbionari și pierderile asociate. |
| QABC-0148 | G1-ELE-157=B; G2-ELEC-295=B | Transfigurarea simplifică rețeaua echivalentă de calcul, nu modifică fizic pierderile. |
| QABC-0153 | G1-ELE-162=A; G2-ELEC-300=A | Linie adaptată dacă impedanța receptorului este egală cu impedanța caracteristică. |
| QABC-0172 | G1-ELE-183=A; G2-ELEC-319=A | La S fix, P=S·cosφ atinge maximul la cosφ=1. |
| QABC-0219 | G1-ELE-230=B; G2-ELEC-366=B | Siguranța fuzibilă protejează la supracurenți prin topirea elementului. |
| QABC-0226 | G1-ELE-237=C; G2-ELEC-373=C | Conductorul cu caracteristică tensiune-curent neohmică este neliniar. |
| QABC-0216 | G1-ELE-227=B; G2-ELEC-363=B | Separatorul asigură separare/izolare vizibilă, nu întrerupere generică de curent de sarcină. |
| QABC-0103 | G1-ELE-112=B; G2-ELEC-254=B | Nisipul cuarțos răcește/stinge arcul în siguranța de înaltă tensiune, mărind capacitatea de rupere. |
| QABC-0123 | G1-ELE-132=A; G2-ELEC-272=A | În circuit RLC serie, X=XL−XC>0 implică defazaj inductiv, curent în urmă. |

## Evidence QA and anti-loop
- Existing ORIGINAL source 2024 workbook question/3 answers, grade-specific keys and source card SHA read and compared against CKPT-421 master. Every original option has an explanation. **No canonical barem/stem/ABC changes.**
- Separate technical challenger AI ran 32 candidate reviews in two groups: resp_c8314ae4-52d2-4a77-a03c-c01703551b04 and resp_cb9e56d8-46f7-4150-a089-b5860b733208. The accepted 25 have PASS in the intended educational model. A reviewer marked QABC-0176 CONDITIONAL, and 0179/0197 and 0145 were kept outside because their conditions could change conclusions; 0107 remains excluded from prior run. No false claims that other cases were certified.
- Source URLs come from existing research and were scrutinized via independent source-grounded challenge, **not all individually reopened live today**. Educational-content approval does not assert exact full source paragraph neighbors were already copied to the offline app, nor official exam key certification.
- Exact arithmetic/physical model notes retained in per-case JSON. Totals checked: 150 content-validated +200 historically held +472 not yet adjudicated =822. 78 accepted groups +136 held +354 unflagged pending =568.
- No canonical app XLSX/HTML/APK/main or PR merge/release edits; **documentation only**.

## Files
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_422_25_QABC_50_GRADES_EDUCATIONAL_PROOFS_2026_11_23.json`: 25 A/B/C proof cases with source URLs, legacy card SHAs and independent review sessions.
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_422_568_GROUPS_MASTER_2026_11_23.json`: full 568 QABC group master state.
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_422_822_GRADES_MASTER_2026_11_23.json`: full 822 individual grade route master state.
- `ACTIVE_HANDOFF.md`: current status and next GFR action.

**Next:** choose new only unapproved source-original/didactic QABC, preserve withheld conditional issues, validate source/ABC/card in bounded batches; 200 held routes remain a separate queue. HTML/APK offline card UI, before/bold/after source excerpts, legal permissions and release QA are later stages.
