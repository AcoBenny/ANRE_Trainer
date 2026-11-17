# CKPT-182 | 10 existing blocked I7 cases: exact QABC/source/semantic recheck | 2026-11-17

## Scope and safety
Existing 568/568 source-scope inventory and 822 grade IDs remain unchanged (CKPT-180). This is a **source- and wording-review of ten pre-existing flagged units**, not 10 new questions, not 10 learner approvals and not a zero-blocker claim. CKPT-181 already preserves NOR066 and is not duplicated here. No canonical QABC/key/app edits; no merge/release. Same-assistant role check (technical + source + linguistic), **no independent reviewer runtime executed**.

Source reopened this session: [I7 text searchable, synchronized from official source on 2026-05-11](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011). Official current portal [document 286763](https://legislatie.just.ro/Public/DetaliiDocument/286763) was found/indexed but direct page fetch returned HTTP 502; no claim of independent confirmation of 2026 exam bibliography/answer key. Record which section was directly re-read for each case.

## 10 source/linguistic cases

### 1. G1-NOR-010 | SOURCE_ALTERNATE_CONFLICT
- Canonical unit: `AU-d07978446fc33e85`; QABC hash: `d07978446fc33e854f7d60d209def90beac4a709e75bbefe118fa86956f9151a`; **imported key B unchanged**, I7-intended **candidate C, NOT_APPLIED**.
- **Question original:** În instalaţiile de joasă tensiune aferente clădirilor, rezistenţa electrică a izolaţiei trebuie măsurată:
- **A:** numai între două conductoare active
- **B:** numai între conductoarele active luate 2 câte 2
- **C:** între conductoarele active şi conductorul de protecţie conectat la reţeaua de legare la pământ
- **ABC review:** A: «numai» două active exclude măsurarea obligatorie față de PE. B: «numai» perechi active contrazice obiectul verificării. C: coincide cu active−PE legat la pământ, iar activele pot fi unite la încercare.
- **Relevant source / qualifiers:** I7 §8.1.1.3.3: §8.1.1.3.2 continuitate, §8.1.1.3.3 încercarea izolării și tabel 8.1. Verificarea izolației cere active−PE; măsurarea între active nu înlocuiește această cerință.
- **Decision:** Provisional specific-scope disagreement with imported key, evidence review advanced. **Not closed for learning** pending independent source and answer-key signoff.

### 2. G1-NOR-029 | LINGUISTIC_MAXIMUM_AMBIGUITY
- Canonical unit: `AU-91a2ff4f7d7f1d9b`; QABC hash: `91a2ff4f7d7f1d9b9b595067efa1a9be1866f3c9d326b538a7c0031ecb3437d4`; **imported key B unchanged**, I7-intended **candidate C, NOT_APPLIED**.
- **Question original:** Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:
- **A:** 2 m
- **B:** 2,3 m
- **C:** 2,5 m
- **ABC review:** A: limita 2m este mai strictă și compatibilă fizic. B: 2,3m este limita GENERALĂ, nu excepția locuințelor. C: 2,5m este plafonul maxim admis explicit pentru locuințe.
- **Relevant source / qualifiers:** I7 §5.3.3.21: §5.3.3.21 regulă generală 2,3m, excepție locuințe 2,5m; §5.3.3.22 următoare tratează latura de jos. Intenția «maximul» favorizează C, dar «să nu depășească» nu exclude valori inferioare.
- **Decision:** Intended normative answer identified, but linguistic/model ambiguity remains; do not force a unique learner key.

### 3. G1-NOR-042 | SOURCE_ALTERNATE_CONFLICT
- Canonical unit: `AU-3ef030d9ababb8ef`; QABC hash: `3ef030d9ababb8ef969ff65ac81bd8b9daec10c3a96aca06aa4ec2cdf2577b2f`; **imported key B unchanged**, I7-intended **candidate A, NOT_APPLIED**.
- **Question original:** Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:
- **A:** în circuitele monofazate cu două conductoare, indiferent de secţiunea conductoarelor
- **B:** în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm2 Cu sau 35 mm2 Al
- **C:** în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază
- **ABC review:** A: corespunde literal circuit monofazat cu două conductoare. B: confuzie mono cu trei conductoare și praguri Cu25/Al35 inexistente; norma dă polifazat Cu16/Al25. C: afirmă pentru orice secțiune, deși restricțiile de armonici/echilibrare schimbă dimensionarea.
- **Relevant source / qualifiers:** I7 §5.2.4.6.1(a)-(d); 5.2.4.6.2-3: §5.2.4.6.1(a) same cross-section in monophase 2-wire regardless of size; b) polyphased Cu≤16/Al≤25; c,d context special. §5.2.4.6.2 >33% armonici -> N poate necesita secțiune mai mare; §5.2.4.6.3 condiții N redus.
- **Decision:** Provisional specific-scope disagreement with imported key, evidence review advanced. **Not closed for learning** pending independent source and answer-key signoff.

### 4. G1-NOR-054 | LANGUAGE_RECOMMENDATION_VS_SHALL
- Canonical unit: `AU-20e9967c02fb958d`; QABC hash: `20e9967c02fb958d9fd44b281ab295812a37e00ddd776802b93f42ddeb6d2394`; **imported key A unchanged**, I7-intended **candidate B, NOT_APPLIED**.
- **Question original:** Întrerupătoarele, comutatoarele şi butoanele de lumină se montează, faţă de nivelul pardoselii finite, la înălţimea de:
- **A:** 1m de la axul aparatului
- **B:** (0,6-1,5) m de la axul aparatului
- **C:** 1,5 m de la axul aparatului
- **ABC review:** A: 1m se află în intervalul recomandat, dar nu îl exprimă integral. B: corespunde intervalului normativ 0,6–1,5m. C: 1,5m este punctul superior al intervalului și poate fi valid fizic.
- **Relevant source / qualifiers:** I7 §5.4.22: Norma spune «Se recomandă» și măsoară «de la aparat» la pardoseala finită; opțiunile spun «de la axul aparatului». Deosebirea recomandare/obligație și referința de măsură împiedică unicitatea strictă.
- **Decision:** Intended normative answer identified, but linguistic/model ambiguity remains; do not force a unique learner key.

### 5. G1-NOR-058 | SOURCE_ALTERNATE_CONFLICT
- Canonical unit: `AU-9d055f5d45c8c65a`; QABC hash: `9d055f5d45c8c65a55bcdaee3816f97ab0cf21f97e27c3c301faeca42faa9f18`; **imported key B unchanged**, I7-intended **candidate C, NOT_APPLIED**.
- **Question original:** Amplasarea instalaţiilor electrice sub conducte sau utilaje pe care poate să apară condens:
- **A:** se admite întotdeauna
- **B:** este total interzisă
- **C:** se admite condiţionat
- **ABC review:** A: «întotdeauna» contrazice interdicția generală. B: «total interzisă» ignoră excepția explicită. C: instalarea este admisă condiționat dacă execuția este închisă, IP minim 33 și materiale rezistente.
- **Relevant source / qualifiers:** I7 §3.0.3.4-6: §3.0.3.5 are interdicție și excepția exactă; §3.0.3.4 tratează traseele comune periculoase, §3.0.3.6 ventilația. Nu transforma excepția în permisiune generală.
- **Decision:** Provisional specific-scope disagreement with imported key, evidence review advanced. **Not closed for learning** pending independent source and answer-key signoff.

### 6. G1-NOR-060 | SOURCE_ALTERNATE_CONFLICT
- Canonical unit: `AU-e69fb1c06d1d03a1`; QABC hash: `e69fb1c06d1d03a1db6053c8e3ba080f194f1d616c402404d86ed271ce297348`; **imported key B unchanged**, I7-intended **candidate C, NOT_APPLIED**.
- **Question original:** Utilizarea conductelor metalice pentru apă drept conductoare de protecţie:
- **A:** este recomandată
- **B:** este permisă condiţionat
- **C:** nu este permisă
- **ABC review:** A: conductele de apă nu sunt conductoare de protecție recomandate. B: permisivitatea condiționată ca PE este contrazisă de §5.5.3.2. C: interdicția ca PE coincide literal cu norma.
- **Relevant source / qualifiers:** I7 §5.5.3.1-3; 5.5.5: §5.5.3.2 exclude explicit conductele pentru apă din rol PE; §5.5.5 tratează separat legăturile de echipotențializare și nu autorizează o conductă ca PE.
- **Decision:** Provisional specific-scope disagreement with imported key, evidence review advanced. **Not closed for learning** pending independent source and answer-key signoff.

### 7. G1-NOR-061 | SOURCE_ALTERNATE_CONFLICT
- Canonical unit: `AU-a4bb099ae4081427`; QABC hash: `a4bb099ae40814275bc332794aad9f8500961ee1f4bbd3e1cf393bea64550feb`; **imported key A unchanged**, I7-intended **candidate B, NOT_APPLIED**.
- **Question original:** Îmbinarea tuburilor de protecţie a conductoarelor electrice la trecerile prin elemente de construcţie este:
- **A:** admisă
- **B:** interzisă
- **C:** admisă doar pentru tuburi cu diametru mai mic de 16 mm
- **ABC review:** A: admiterea este interzisă explicit la trecerea prin construcție. B: interdicția este formularea exactă a §5.2.12.3.4. C: diametrul <16mm nu creează o excepție în acest articol.
- **Relevant source / qualifiers:** I7 §5.2.12.3.1-5: §5.2.12.3.3 cere accesorii corespunzătoare influențelor externe, iar §5.2.12.3.4 interzice îmbinarea chiar în trecere, indiferent de diametru; §5.2.12.3.5 condiții distincte de curbură.
- **Decision:** Provisional specific-scope disagreement with imported key, evidence review advanced. **Not closed for learning** pending independent source and answer-key signoff.

### 8. G1-NOR-062 | LINGUISTIC_STRICTER_OPTION
- Canonical unit: `AU-afb2491f268f9ebe`; QABC hash: `afb2491f268f9ebefbe831ad98cf36fb44fbccf6274b0fa60f62ac3859eb77b1`; **imported key A unchanged**, I7-intended **candidate B, NOT_APPLIED**.
- **Question original:** În camerele de copii din creşe, grădiniţe, spitale de copii, prizele trebuie montate pe pereţi la următoarele înălţimi măsurate de la axul aparatului la nivelul pardoselii finite:
- **A:** peste 1m
- **B:** peste 1,5 m
- **C:** peste 2m
- **ABC review:** A: «peste 1m» nu reproduce pragul recomandat pentru camerele indicate; ar admite 1,2m. B: reproduce recomandarea «peste 1,5m». C: «peste 2m» este mai restrictivă, uneori compatibilă, dar cifra 2m din regula vecină vizează școlile, în clase.
- **Relevant source / qualifiers:** I7 §5.4.24-26: §5.4.25 textul spune «Se recomandă», nu «trebuie»; diferențiază școli peste 2m de camere copii peste 1,5m. Varianta C este un subconjunct, nu limita minimă exprimată.
- **Decision:** Intended normative answer identified, but linguistic/model ambiguity remains; do not force a unique learner key.

### 9. G1-NOR-089 | SOURCE_ALTERNATE_CONFLICT
- Canonical unit: `AU-87be22d02147710f`; QABC hash: `87be22d02147710fdaefea5e4d81c54ed411e0ae636181e29c78ccf751f57f3d`; **imported key A unchanged**, I7-intended **candidate B, NOT_APPLIED**.
- **Question original:** Utilizarea unei singure culori pentru toate conductoarele de fază ale unui circuit
- **A:** este interzisă
- **B:** este permisă, cu marcarea corespunzătoare la cele două extremităţi
- **C:** este permisă dacă nu se folosește una dintre culorile verde sau galben
- **ABC review:** A: interdicția absolută contrazice expres permisiunea. B: este permisă aceeași culoare pentru faze ale unui circuit cu marcarea la ambele extremități. C: evitare verde/galben nu înlocuiește marcarea cerută la extremități.
- **Relevant source / qualifiers:** I7 §5.1.4.3.1-3; 5.1.4.5: §5.1.4.3.3 permisiune și marcare; §5.1.4.3.1-2 cod PE/N și recomandări faze; §5.1.4.5 consistența marcajului în tabloul de distribuție.
- **Decision:** Provisional specific-scope disagreement with imported key, evidence review advanced. **Not closed for learning** pending independent source and answer-key signoff.

### 10. G1-NOR-100 | LINGUISTIC_STRICT_VS_NONSTRICT
- Canonical unit: `AU-7f4876eff2e3a044`; QABC hash: `7f4876eff2e3a04476deeb0c397bdb62cbb5b97f0ecba93d37d0897f61531f17`; **imported key B unchanged**, I7-intended **candidate B, NOT_APPLIED**.
- **Question original:** Rezistenţa de izolaţie a pardoselii şi pereţilor în fiecare punct de măsurare în condiţiile specificate în SR EN 61140 şi verificate printr-o metoda recomandată în Anexa 8.1 din I7/2011, dacă tensiunea nominală a instalaţiei nu depăşeşte 500 V în tensiune continuă sau alternativă, trebuie să fie mai mare de
- **A:** 75 kΩ
- **B:** 50 kΩ
- **C:** 100 kΩ
- **ABC review:** A: pragul 75kΩ este mai mare decât limita normativă, dar nu e pragul prevăzut pentru Un≤500V. B: 50kΩ este pragul I7 pentru Un≤500V. C: 100kΩ este cifra din cealaltă categorie de tensiune (>500V).
- **Relevant source / qualifiers:** I7 §4.1.5.5.5-7: §4.1.5.5.6 spune «nu trebuie să fie mai mică de 50kΩ» (≥), pe când enunțul cere «mai mare de» (>), excluzând punctul egal 50kΩ; răspuns intenționat B dar unicitatea strictă este problematică.
- **Decision:** Intended normative answer identified, but linguistic/model ambiguity remains; do not force a unique learner key.

## QA and gates
- Before writing, exact Q/A/B/C/grade-key/string equality checked against **all 822 rows** of `V73_ALL_822_EVIDENCE_AND_RELEASE_GATES_MASTER.csv` for these 10 canonical IDs: **10/10 PASS (question/each option/key)**. Unit IDs and 64-hex SHA256 preserved from CKPT-171/175/178. This is deterministic cross-record **data QA**, not proof of normative correctness.
- 6 source-specific alternatives (010 C,042 A,058 C,060 C,061 B,089 B); 4 wording/interval ambiguities (029 C,054 B,062 B,100 B). **10 existing items triaged, 0 new unique units, 0 approved for learning, 0 original keys edited.**
- `independent_source_QA=NOT_RUN`, `independent_technical_QA=NOT_RUN`, `independent_linguistic_QA=NOT_RUN`, `official_exam_2026_edition=NOT_VERIFIED`, `official_ANRE_grading_key=NOT_VERIFIED`, `approved_for_learning=NO`.
- Source-matching gate performed conceptually: all 10 clauses address exactly the corresponding physical/electrical object; general conduit-pulling-box 25m paragraph MUST NOT be used for specific service-branch-column question NOR032 (PE155 §3.2.10, 15m). This gate is **manual**, not an executed automated selftest or independent QA.
- Previous sources and contradictory hypotheses retained as history: CKPT-171/175/178; CKPT-179/181 for NOR066. PR #7 remains Draft.

## Next smallest nonredundant action
Review the other blocked units directly from the remaining CKPT-138–178 cards, avoiding repeated source review; separate irreducible ambiguities for user interpretation only after source/evidence failure and reserve final app/barem changes for explicit approval.
