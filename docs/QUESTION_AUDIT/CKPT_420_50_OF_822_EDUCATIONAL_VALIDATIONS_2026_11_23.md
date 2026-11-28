# CKPT-420 | ANRE Trainer GFR reaches 50/822 educational-content validations

Date: 2026-11-23 | Parent CKPT-419 | PR #7 Draft.

**Real transition: 5 → 50 grade-specific validated-for-learning-CONTENT routes.** New: 23 distinct QABC units, 45 grade routes (22 paired G1/G2 electrotechnics, 1 original G1 legislation). Distinct approved groups 5 → 28. No app release or official certification claimed.

| Metric | Before | After |
|---|---:|---:|
| Educational content approved grade routes | 5 | **50** |
| Distinct approved groups | 5 | **28** |
| Grade routes held on existing semantic/source issues | 200 | 200 |
| Grade routes without historical hold still unapproved | 617 | **572** |
| Entire bank coverage | 822 | 822 |

## 23 new source-backed units

| Unit | grade keys preserved | Technical source condition |
|---|---|---|
| QABC-0002 | G1-ELE-002=C; G2-ELEC-155=C | Bobină Petersen: compensarea curentului capacitiv de defect, nu factorul de putere. |
| QABC-0003 | G1-ELE-003=C; G2-ELEC-156=C | Poate fi produs de magneți permanenți și electromagneți; «numai» elimină A/B. |
| QABC-0004 | G1-ELE-004=B; G2-ELEC-157=B | Ceq=100+50+100=250 µF, trei condensatoare paralele. |
| QABC-0006 | G1-ELE-006=B; G2-ELEC-159=B | AAR comută pe rezerva disponibilă pentru continuitatea alimentării. |
| QABC-0010 | G1-ELE-011=B; G2-ELEC-163=B | Reactanța inductivă X_L=2πfL limitează curentul în bucla de scurtcircuit. |
| QABC-0011 | G1-ELE-012=A; G2-ELEC-164=A | Intensitatea câmpului E caracterizează câmpul electrostatic; «numai D» este restrictiv. |
| QABC-0014 | G1-ELE-015=C; G2-ELEC-167=C | Bobina de pe plecare radială limitează defectele în aval, prin impedanța ei serie. |
| QABC-0016 | G1-ELE-017=A; G2-ELEC-169=A | Sarcina egală în modul pe elementele unui lanț ideal de condensatoare în serie. |
| QABC-0018 | G1-ELE-019=B; G2-ELEC-171=B | Pentru două capacități egale în serie: Ceq=C/2. |
| QABC-0023 | G1-ELE-027=B; G2-ELEC-176=B | I²Rt=4×10×10 h=400 Wh; parametrii constanți. |
| QABC-0032 | G1-ELE-039=B; G2-ELEC-185=B | Legea Coulomb: F proporțional cu 1/r² pentru sarcini punctiforme și mediu constant. |
| QABC-0033 | G1-ELE-040=A; G2-ELEC-186=A | Constanta de timp RC: τ=RC, nu 1/RC. |
| QABC-0038 | G1-ELE-045=B; G2-ELEC-191=B | Transportul unui corp încărcat în spațiu = curent de convecție. |
| QABC-0043 | G1-ELE-050=C; G2-ELEC-196=C | Vector Poynting = E×H, cu ordinea vectorială esențială. |
| QABC-0047 | G1-ELE-054=A; G2-ELEC-200=A | Descărcător ZnO limitator de supratensiuni, nu protector generic la supracurent. |
| QABC-0055 | G1-ELE-063=B; G2-ELEC-208=B | Energia bobinei liniare: W=½Li². |
| QABC-0056 | G1-ELE-064=A; G2-ELEC-209=A | Energia electrostatică: W=½qV cu geometrie/capacitate constantă. |
| QABC-0059 | G1-ELE-067=B; G2-ELEC-212=B | A doua lege Kirchhoff: suma algebrică a tensiunilor în buclă. |
| QABC-0062 | G1-ELE-070=B; G2-ELEC-215=B | Ampermetru analog: șunt de rezistență mică în paralel. |
| QABC-0063 | G1-ELE-071=B; G2-ELEC-216=B | Voltmetru analog: rezistență adițională în serie. |
| QABC-0067 | G1-ELE-075=A; G2-ELEC-220=A | Alternator: f=np/60; n în rot/min, p număr de perechi de poli. |
| QABC-0068 | G1-ELE-076=B; G2-ELEC-221=B | e=Blv este FEM de mișcare/inducție, pentru orientarea perpendiculară. |
| QABC-0277 | G1-LEG-013=C | ANRE: vizarea adeverinței la 5 ani de la eliberare sau ultima vizare. |

## Evidence and QA
Original stems and all A/B/C loaded from exact existing editorial drafts, crosschecked per G1/G2 grade IDs and unchanged imported keys. Historic A/B/C rationale and reported source links reused rather than rewriting or double-counting research. External separate adversarial AI research reviewed the electrotechnical items (responses resp_77589e3a-ff06-4f6a-906a-3527ec6dcc1e, resp_4e9467ab-d3f3-447c-a15c-f6ce50c9b415, resp_d9ad6493-f9f1-4d5d-bf76-30844b845ca7). Reviewer flagged **0045 and 0061** as conditional and those two were excluded instead of forcing approval. For 0277 official [ANRE guidance](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/electricieni/examene/) explicitly states 5 years.

Sources for capacitor series/parallel, analog ammeter/voltmeter construction and ANRE term were also directly accessed during this session. Remaining source URLs were prior indexed and source-grounded in previous research and separate AI challenge, not individually live-reopened in this run. Teaching scope and physical assumptions are preserved in detailed JSON. This status is *educational content accepted*, **not certified ANRE scored answer**, and does not imply textbook full preceding/following paragraphs already integrated offline.

**No app/original changes.** 822 total ID readback, 50 approved content, 200 historical held, 572 unflagged pending. HTML/APK offline QA, source display, attribution and rights still required before product release. 

## Files
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_420_23_SOURCE_ABC_CASES_2026_11_23.json` exact 23 cases with A/B/C, source, provenance and caveats
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_420_568_QABC_MASTER_2026_11_23.json` complete 568 QABC state ledger
- `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_420_822_GRADE_MASTER_2026_11_23.json` complete 822 grade state ledger
- `ACTIVE_HANDOFF.md` updated. No merge or release.

**Next GFR**: pick only NEW unapproved cases; count actual state transitions after source + ABC + card check, park conditional items separately. Never re-review already accepted cases without material new contradicting evidence.
