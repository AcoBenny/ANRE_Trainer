# CKPT-242 | 15 exact QABC primary analyses and 13 exact grade-II reuse references | 2026-11-19

- Canonical original V73 Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`. Baseline ledger V120 `c6e0264f1698de897678b3451106d8b7acdfeff6`. All 15 original question+A+B+C+key strings matched exactly to one grade-II counterpart before any metadata field change.
- 15 source-scoped original case analyses; 13 previously unlinked G2 evidence references. G2-ELEC-381 and G2-ELEC-392 had prior V82 references that are **preserved**, not double counted.
- 28 grade ID evidence rows newly linked: 190 unfocused -> **162** unfocused. Original 822 IDs remain; QABC, keys, priority, learning approval, signatures preserved.
- Source review by same assistant only. Source types: NIST, OpenStax, industry articles and vendor sources. Some sources only SEARCH_INDEX; none are the official 2026 ANRE scored key. Technical and linguistic independent QA, exact exam-edition authentication and human signoff remain NOT_RUN.

### G1-ELE-245 / G2-ELEC-381
- Q exact: Un circuit de curent alternativ, pentru care factorul de putere este egal cu 1, este un circuit:
- A: pur rezistiv
- B: pur inductiv
- C: pur capacitiv
- Imported key unchanged: A
- A/B/C interpretation and counterexample: A «pur rezistiv» este modelul intenționat pentru cosφ=1 în regim sinusoidal. B pur inductiv și C pur capacitiv au ideal φ=±90° și PF=0, nu 1. Contraexemplu: o rețea cu rezistențe plus L și C compensate la intrare poate avea PF=1 fără a fi construită exclusiv din rezistențe. Barem A necesită calificare model, nu este universal.
- Source: https://wiki.analog.com/university/courses/alm1k/circuits1/alm-cir-ac-power-factor
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-247 / G2-ELEC-383
- Q exact: Un corp conductor situat într-un câmp electric de intensitate E se încarcă cu electricitate:
- A: prin conducţie
- B: prin inducţie electrostatică
- C: prin magnetizare
- Imported key unchanged: B
- A/B/C interpretation and counterexample: B inducția electrostatică determină separarea sarcinilor în conductor introdus într-un câmp E. A conducție ar necesita contact, iar C magnetizare privește proprietăți magnetice. Nu înseamnă că un conductor neutru și izolat primește automat sarcină NETĂ: pentru încărcare netă prin inducție e necesar proces auxiliar de împământare sau separare; enunțul confundă potențial polarizarea cu încărcarea netă.
- Source: https://openstax.org/books/university-physics-volume-2/pages/5-2-conductors-insulators-and-charging-by-induction
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-248 / G2-ELEC-384
- Q exact: Un întreruptor debroşabil asigură:
- A: numai protecţia în caz de scurtcircuit;
- B: protecţia la supratensiuni;
- C: izolarea personalului care lucrează la întreruptor, de restul instalaţiei aflată sub tensiune.
- Imported key unchanged: C
- A/B/C interpretation and counterexample: C exprimă avantajul de a izola întreruptorul debroșabil față de barele sub tensiune în poziție retrasă și condiții de protecție adecvate; A «numai la scurtcircuit» este prea restrictivă; B supratensiunile necesită protecții specifice. Important: debroșarea singură NU certifică absența tensiunii și nu înlocuiește LOTO, punerea la pământ ori verificările și ecranele de protecție. Norma IEC 62271-200 trebuie verificată la ediția și articolul exact.
- Source: https://studylib.net/doc/28010055/iec-62271-200--2021-05-
- Source access: SEARCH_INDEX_ONLY. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-250 / G2-ELEC-385
- Q exact: Un motor electric sincron, care funcţionează subexcitat:
- A: absoarbe putere activă şi putere reactivă
- B: absoarbe putere activă şi produce putere reactivă
- C: produce putere activă şi putere reactivă
- Imported key unchanged: A
- A/B/C interpretation and counterexample: A pentru motor sincron subexcitat operând ca motor: absoarbe putere activă mecanică și reactivă de la rețea (factor de putere inductiv). B pretinde că produce reactivă, caracteristic motorului supraexcitat; C ar descrie funcționare de generator, nu motor. Necesită precizarea regimului, a semnelor și a excitației.
- Source: https://edurev.in/t/95075/polyphase-synchronous-machines-2
- Source access: SEARCH_INDEX_ONLY. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-251 / G2-ELEC-386
- Q exact: Valoarea conductivităţii electrice este în ordine crescătoare la următoarele materiale:
- A: aluminiu, argint, cupru
- B: argint, cupru, aluminiu
- C: aluminiu, cupru, argint
- Imported key unchanged: C
- A/B/C interpretation and counterexample: C aluminium < copper < silver în conductivitate la ~20°C și materiale de puritate comparabilă. A pune argint înaintea cuprului într-o ordine greșită; B este ordine descrescătoare. Temperatura, aliajul și puritatea trebuie ținute constante pentru comparație.
- Source: https://hyperphysics.phy-astr.gsu.edu/hbase/Tables/rstiv.html
- Source access: SEARCH_INDEX_ONLY. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-252 / G2-ELEC-387
- Q exact: Un număr de n surse  având fiecare tensiunea electromotoare continua e si rezistenta interioara r, legate în paralel pot fi înlocuite printr-o sursa echivalenta având:
- A: tensiunea electromotoare e si rezistenta r/n
- B: tensiunea electromotoare ne si rezistentă r/n
- C: tensiunea electromotoare e si rezistenta nr.
- Imported key unchanged: A
- A/B/C interpretation and counterexample: A: n surse identice idealizate cu t.e.m. e și rezistență internă r, conectate în paralel cu aceeași polaritate, dau e și r/n. B ne corespunde surselor în serie, C nr inversează rezultatul pentru rezistență. Modelul cere t.e.m. identice și rezistențe identice; altfel pot apărea curenți de circulație.
- Source: https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- Source access: SEARCH_INDEX_ONLY. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-253 / G2-ELEC-388
- Q exact: Un receptor electric de rezistenţă R conectat la bornele AB ale unui circuit de alimentare oarecare absoarbe puterea maximă dacă:
- A: rezistenţa R este egală cu rezistenţa totală a circuitului văzută prin bornele AB
- B: rezistenţa R este egală cu rezistenţa internă a sursei de tem
- C: rezistenţa R tinde spre zero
- Imported key unchanged: A
- A/B/C interpretation and counterexample: A: pentru circuit liniar cu rezistență Thevenin Rth pozitivă și sarcină rezistivă R, puterea pe sarcină se maximizează la R=Rth. B rezistența «internă a sursei» nu descrie neapărat întreaga rețea văzută la borne AB, C R→0 anulează puterea pe sarcină în modelul Thevenin cu Rth>0. Pentru impedanță complexă condiția de conjugare este diferită.
- Source: https://www.sciencedirect.com/topics/engineering/maximum-power-transfer-theorem
- Source access: SEARCH_INDEX_ONLY. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-254 / G2-ELEC-389
- Q exact: Valoarea intensităţii câmpului electric produs de o sarcină electrică la distanţa r este:
- A: direct proporţională cu r
- B: direct proporţională cu pătratul lui r
- C: invers proporţională cu pătratul lui r
- Imported key unchanged: C
- A/B/C interpretation and counterexample: C pentru o sarcină PUNCTUALĂ în mediu omogen: E=k|q|/r². A și B ar face E crescător cu distanța, contrar legii Coulomb. Enunțul spune numai «o sarcină electrică», nu precizează punctuală, geometria ori mediul, astfel C cere modelul sursei punctuale și nu este universal pentru orice distribuție extinsă.
- Source: https://openstax.org/books/university-physics-volume-2/pages/5-3-coulombs-law
- Source access: SEARCH_INDEX_ONLY. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-255 / G2-ELEC-390
- Q exact: Un transformator de măsurare de curent nu poate fi lăsat cu secundarul în gol, deoarece:
- A: împiedica circulaţia curentului primar
- B: apar supratensiuni periculoase in secundar
- C: nu indica aparatele de măsurare
- Imported key unchanged: B
- A/B/C interpretation and counterexample: B: secundarul deschis al transformatorului de curent convențional, când prin primar circulă curent, poate dezvolta tensiuni periculoase. A nu oprește automat curentul primar; C absența indicației e efect secundar, nu explicația de securitate. Nu se manevrează fără procedură și personal calificat.
- Source: https://www.se.com/us/en/faqs/FA125574/
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-256 / G2-ELEC-391
- Q exact: Unitatea de măsură a capacităţii unui condensator este:
- A: F
- B: Axh
- C: A/h
- Imported key unchanged: A
- A/B/C interpretation and counterexample: A: capacitate în farazi F = C/V. B A·h reprezintă sarcină electrică, nu capacitate; C A/h are unități diferite.
- Source: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-257 / G2-ELEC-392
- Q exact: Unitatea de măsură a fluxului electric este:
- A: V/m
- B: Coulombul
- C: Faradul
- Imported key unchanged: B
- A/B/C interpretation and counterexample: B coulomb este compatibil cu fluxul deplasării electrice ∫D·dA. Însă fluxul vectorului câmpului electric ΦE=∫E·dA are unitatea N·m²/C sau V·m, NU coulomb. A V/m este intensitatea E, C farad este capacitatea. Enunțul «flux electric» fără precizarea D ori E este semantic ambiguu între definiții. NU certifica B universal și NU schimba baremul.
- Source: https://sathee.iitk.ac.in/sathee-jee/article/physics/physics-electric-flux/
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-258 / G2-ELEC-393
- Q exact: Unitatea de măsură a fluxului magnetic este:
- A: Tesla
- B: Weber
- C: Farad
- Imported key unchanged: B
- A/B/C interpretation and counterexample: B: flux magnetic Φ se măsoară în weber Wb = V·s. A tesla măsoară inducție magnetică B = Wb/m², C farad capacitatea electrică.
- Source: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-259 / G2-ELEC-394
- Q exact: Unitatea de măsură a frecvenţei mărimilor periodice se numeşte:
- A: Weber
- B: Hertz
- C: Henry
- Imported key unchanged: B
- A/B/C interpretation and counterexample: B: frecvența periodică f=1/T se măsoară în hertz Hz=s^-1. A weber măsoară flux magnetic, C henry inductanță.
- Source: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-260 / G2-ELEC-395
- Q exact: Unitatea de măsură a sarcinii electrice este:
- A: V/m
- B: Coulomb
- C: Farad
- Imported key unchanged: B
- A/B/C interpretation and counterexample: B: sarcina electrică q este măsurată în coulomb C=A·s. A V/m intensitatea câmpului electric, C farad capacitate.
- Source: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Source access: OPENED_HTML. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

### G1-ELE-261 / G2-ELEC-396
- Q exact: Unitatea de măsură ohm x mmp / m este pentru:
- A: rezistivitate
- B: greutate specifica
- C: coeficient de dilataţie
- Imported key unchanged: A
- A/B/C interpretation and counterexample: A: din R=ρl/A rezultă ρ=RA/l, deci unitatea practică Ω·mm²/m. B greutatea specifică are unități N/m³, C coeficientul de dilatație K^-1. Notația canonică «mmp» probabil mm pătrat, necesită păstrarea literală și clarificare în fișa sursei.
- Source: https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance
- Source access: SEARCH_INDEX_ONLY. This is not a primary approved ANRE-2026 answer-key proof and no independent technical/linguistic reviewer has signed off.

## Outstanding gates
- **G1-ELE-245:** PF=1 is compatible with compensating L/C and not exclusively pure R. Do not certify universal key.
- **G1-ELE-247:** polarization of a neutral isolated conductor is not the same as net charging; charge by induction requires additional process.
- **G1-ELE-257:** electric flux through E uses N·m²/C while electric-displacement flux through D uses C; term without qualifier is ambiguous. Preserve B imported, flag source-definition disagreement.
- **G1-ELE-248:** breaker withdrawal is not a substitute for safe isolation/lockout/earthing procedures.
- 50 pre-existing inconsistent CSV rows remain byte-identical; treat as separate data integrity issue before bulk reader/release.
- No canonical question/answer change, no HTML/APK, merge, main, release or approval for learning. PR #7 remains Draft.
