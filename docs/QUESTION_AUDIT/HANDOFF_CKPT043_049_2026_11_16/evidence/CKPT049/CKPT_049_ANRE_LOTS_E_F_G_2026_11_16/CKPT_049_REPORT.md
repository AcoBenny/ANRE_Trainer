# CKPT-049 | Avengers Asamble ANRE | Loturile E/F/G, 36 de grile G1-NOR

**Status:** cercetare documentară preliminară, niciun barem modificat, QA independent `NOT_RUN`, aprobare de învățare `0`.

## Constrângeri și proveniență

- Baza: `ANRE_Trainer_MAPPING_FINAL_V1.csv` cu 822 ID-uri, SHA256 `effa386b6e9c4d8e529b313af822c068fea5e0ed0473e40eb2adcd4be8c0a43f`.
- Fiecare enunț, A/B/C și cheia au fost recitite din acest CSV original, care nu a fost modificat.
- 36 ID-uri noi față de CKPT-047/046, excluzând NOR-065 anterior cercetat. Nu se garantează încă reconcilierea cu toate fișele din GitHub.
- I7: [copie sincronizată la 11.05.2026](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011), de verificat independent ediția integrală efectiv aplicabilă examenului 2026. [Pagina ANRE de tematică și grile](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/).
- PE155: [scan istoric](https://www.baluna.ro/wp-content/uploads/2018/02/pe_155_92.pdf), redeschis textul §1.2.1–1.2.3 dar screenshot-ul sursei a eșuat. Din această cauză NOR-053 nu este autorizat la schimbare.
- În toate cazurile: analiză A/B/C generată din contextul documentat și control structural; **nu** revizie tehnică/lingvistică independentă.

## Constatări P0: barem local diferit de candidata susținută de sursă

| ID | Barem original | Candidat (neaplicat) | Indiciu din context |
|---|:---:|:---:|---|
| G1-NOR-053 | A | C | PE155/1992 §1.2.1–1.2.3 : Branșamentul ajunge la instalația interioară; bornele de ieșire din contor sunt delimitarea normativului PE155. A descrie doar racordul linie-firidă. |
| G1-NOR-054 | A | B | I7 §5.4.22; §5.4.21–.25 context : Interval recomandat pentru întrerupătoare/comutatoare/butoane: 0,6–1,5m. |
| G1-NOR-058 | B | C | I7 §3.0.3.5; §5.2.8.2.2 : Regula de neamplasare sub trasee cu condens are excepție pentru execuție închisă IP33 minim, material rezistent; alt articol cere protecție anti-condens. |
| G1-NOR-060 | B | C | I7 §5.5.3.1–.2 : I7 §5.5.3.2 interzice explicit folosirea conductelor pentru apă ca PE. |
| G1-NOR-061 | A | B | I7 §5.2.12.3.1–.4 : I7 §5.2.12.3.4 interzice îmbinarea tuburilor la trecerile prin elementele de construcție. |
| G1-NOR-062 | A | B | I7 §5.4.25, context §5.4.24 și .26 : Pentru camerele de copii din creșe/grădinițe/spitale: înălțime recomandată peste 1,5m. |
| G1-NOR-066 | B | A | I7 §5.2.12.1.3–.5; §5.2.3.2.5 : I7 §5.2.12.1.4 interzice explicit conductoare electrice în tuburi/țevi pozate în pământ. |

**Risc suplimentar NOR-081/082:** I7 §3.0.3.7 formulează cumulativ rezistența la foc **și** întârzierea propagării flăcării; grilele oferă separat proprietățile. Am blocat concluziile necondiționate fără să schimb baremele.

**Atenție:** anumite opțiuni numeric permise sunt toate literal posibile în intervalul §5.4.22 (`G1-NOR-054`), dar B este singura variantă care redă intervalul complet. Aceasta este problemă de unicitate, nu un răspuns validat definitiv.

## Fişe complete (enunț + opțiuni + explicație contextuală)

### Lotul E: 13 întrebări

#### G1-NOR-052 | original **A** | candidat **A** | `DIRECT_WITH_SCOPE`

**Întrebare:** Pentru circuite monofazate, conductorul neutru (N) va avea:

- A. aceeaşi secţiune ca şi conductorul de fază
- B. aceeaşi secţiune ca şi conductorul de fază, numai pentru conductoare de cupru
- C. aceeaşi secţiune ca şi conductorul de fază, numai pentru conductoare de aluminiu

**Sursa:** [I7 §5.2.4.6.1(a), §5.2.4.6.2–.3](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Monofazat uzual cu două fire: S_N = S_fază, indiferent de Cu/Al.
**Context înainte/după / eliminare:** În polifazat și la armonici există alte reguli; enunțul monofazat este generic.

**Evaluare fiecare variantă, preliminară:**
- **A:** Regula de bază a circuitului monofazat: N are aceeași secțiune cu faza, fără restricție la un metal.
- **B:** Adaugă restricția «numai cupru», pe care regula monofazată nu o cere.
- **C:** Adaugă restricția «numai aluminiu», pe care regula monofazată nu o cere.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-053 | original **A** | candidat **C** | `POTENTIAL_KEY_MISMATCH_SCOPE`

**Întrebare:** Branşamentul electric este partea din instalaţia de distribuţie a energiei electrice cuprinsă între linia electrică şi:

- A. firida de branşament
- B. coloana electrică
- C. punctul de delimitare între distribuitor şi consumator, reprezentat de bornele contorului

**Sursa:** [PE155/1992 §1.2.1–1.2.3](https://www.baluna.ro/wp-content/uploads/2018/02/pe_155_92.pdf)
**Răspuns preferat și motiv:** Branșamentul ajunge la instalația interioară; bornele de ieșire din contor sunt delimitarea normativului PE155. A descrie doar racordul linie-firidă.
**Context înainte/după / eliminare:** C reproduce nota privind delimitarea, nu definiția textuală completă; ediția și PE155 grad I încă trebuie confirmate.

**Evaluare fiecare variantă, preliminară:**
- **A:** Linie–firidă descrie racordul, doar o parte a branșamentului în terminologia PE155.
- **B:** Coloana este un element al traseului, nu punctul final de delimitare din definiția completă.
- **C:** Bornele dinspre consumator ale contorului corespund punctului de delimitare descris de nota PE155; verificare istorică și bibliografică necesară.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-054 | original **A** | candidat **B** | `POTENTIAL_KEY_MISMATCH_AMBIGUITY`

**Întrebare:** Întrerupătoarele, comutatoarele şi butoanele de lumină se montează, faţă de nivelul pardoselii finite, la înălţimea de:

- A. 1m de la axul aparatului
- B. (0,6-1,5) m de la axul aparatului
- C. 1,5 m de la axul aparatului

**Sursa:** [I7 §5.4.22; §5.4.21–.25 context](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Interval recomandat pentru întrerupătoare/comutatoare/butoane: 0,6–1,5m.
**Context înainte/după / eliminare:** A=1 m și C=1,5 m sunt și ele valori în interval; enunțul nu solicită explicit intervalul. B e formularea-sursă cea mai completă, unicitatea grilei e discutabilă.

**Evaluare fiecare variantă, preliminară:**
- **A:** 1 m este o înălțime permisă în interiorul intervalului, deci nu poate fi eliminată ca falsă.
- **B:** Reproduce integral intervalul recomandat de I7, 0,6–1,5 m.
- **C:** 1,5 m este tot o valoare inclusă în interval; întrebarea poate avea variante compatibile.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-055 | original **A** | candidat **A** | `DIRECT_WITH_SCOPE`

**Întrebare:** Prevederile normativului  I 7 – 2011 se aplică la proiectarea, execuţia şi exploatarea instalaţiilor electrice aferente:

- A. clădirilor cu funcţiuni agroindustriale şi agrozootehnice
- B. minelor şi carierelor
- C. depozitelor de materiale pirotehnice şi explozive

**Sursa:** [I7 §7.5.1, domeniu de aplicare](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Există prescripții I7 explicite pentru construcții agroindustriale și agrozootehnice.
**Context înainte/după / eliminare:** Mine/carieri și depozite pirotehnice sunt reglementate special și nu sunt în obiectul cerut.

**Evaluare fiecare variantă, preliminară:**
- **A:** I7 conține prescripții explicite pentru construcții agroindustriale/agrozootehnice.
- **B:** Exploatările miniere au regim special și nu sunt incluse în categoria normativă invocată.
- **C:** Depozitarea explozivilor/materialelor pirotehnice are regim special distinct.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-056 | original **A** | candidat **A** | `DIRECT_WITH_EXCEPTION`

**Întrebare:** Montarea, pe conductoarele de protecţie, a unor elemente care pot produce întreruperea circuitului este:

- A. interzisă
- B. permisă în anumite condiţii
- C. la latitudinea consumatorului

**Sursa:** [I7 §5.5.3.5–.6](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Niciun dispozitiv de comutație nu se inseriază pe conductorul PE.
**Context înainte/după / eliminare:** Îmbinări de test desfăcute cu sculă există; acestea nu echivalează cu comutație automată a PE în serviciu.

**Evaluare fiecare variantă, preliminară:**
- **A:** Regula interzice elementele de întrerupere/comutație în serie pe PE.
- **B:** O legătură de test demontabilă cu sculă nu justifică un dispozitiv care întrerupe PE în serviciu.
- **C:** O normă de securitate nu lasă protecția la alegerea consumatorului.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-057 | original **B** | candidat **B** | `CONTEXTUAL_INFERENCE`

**Întrebare:** Amplasarea aparatelor, echipamentelor şi receptoarelor electrice în locuri în care ar putea fi expuse direct la apă, ulei, substanţe corozive, căldură sau şocuri mecanice:

- A. se admite
- B. se admite condiţionat
- C. este interzisă

**Sursa:** [I7 §5.1.2.1–.2; §3.0.2.4–.5](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Echipamentul se alege pentru influențele externe; protecția suplimentară adecvată poate permite amplasarea.
**Context înainte/după / eliminare:** Permisiunea nu este necondiționată (A), iar interdicția absolută (C) ignoră măsurile de protecție. Enunțul exact nu este reprodus literal în norma găsită.

**Evaluare fiecare variantă, preliminară:**
- **A:** Permisiunea necondiționată omite influențele externe și gradul de protecție necesar.
- **B:** Este posibilă doar cu echipament și măsuri adaptate condițiilor locale.
- **C:** Interdicția generală absolută ignoră posibilitatea protecțiilor suplimentare; norma exactă de aplicare trebuie identificată.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-058 | original **B** | candidat **C** | `POTENTIAL_KEY_MISMATCH_DIRECT`

**Întrebare:** Amplasarea instalaţiilor electrice sub conducte sau utilaje pe care poate să apară condens:

- A. se admite întotdeauna
- B. este total interzisă
- C. se admite condiţionat

**Sursa:** [I7 §3.0.3.5; §5.2.8.2.2](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Regula de neamplasare sub trasee cu condens are excepție pentru execuție închisă IP33 minim, material rezistent; alt articol cere protecție anti-condens.
**Context înainte/după / eliminare:** A «întotdeauna» greșit, B «total interzisă» greșit din cauza excepției; C admis condiționat.

**Evaluare fiecare variantă, preliminară:**
- **A:** «Întotdeauna» ignoră pericolul de condens și condițiile restrictive.
- **B:** «Total interzisă» este prea absolut când norma prevede o derogare expresă cu IP adecvat.
- **C:** Sursei îi corespunde permisiunea condiționată de execuție închisă și protecție împotriva umezelii.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-059 | original **B** | candidat **B** | `DIRECT_WITH_CONTEXT`

**Întrebare:** Corpurile de iluminat echipate cu lămpi cu descărcări se prevăd în orice tip de încăpere cu:

- A. grătar protector
- B. dispozitiv pentru îmbunătăţirea factorului de putere
- C. difuzor

**Sursa:** [I7 §5.4.20; §5.4.19 context](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Lămpi cu descărcări: dispozitiv de îmbunătățire a factorului de putere.
**Context înainte/după / eliminare:** Grătar/difuzor apar în §5.4.19 numai pentru anumite depozite/riscuri, nu orice încăpere.

**Evaluare fiecare variantă, preliminară:**
- **A:** Grătarul protector este cerut în anumite amplasamente, nu universal pentru lămpi cu descărcări.
- **B:** Norma precizează compensarea factorului de putere pentru această categorie de lămpi.
- **C:** Difuzorul este o soluție constructivă specifică, nu cerință generală pentru lămpile cu descărcări.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-060 | original **B** | candidat **C** | `POTENTIAL_KEY_MISMATCH_DIRECT`

**Întrebare:** Utilizarea conductelor metalice pentru apă drept conductoare de protecţie:

- A. este recomandată
- B. este permisă condiţionat
- C. nu este permisă

**Sursa:** [I7 §5.5.3.1–.2](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** I7 §5.5.3.2 interzice explicit folosirea conductelor pentru apă ca PE.
**Context înainte/după / eliminare:** Carcasele metalice/tuburile dedicate pot fi PE condiționat în §5.5.3.1, dar aceasta nu autorizează conducte de apă. B confundă obiectele.

**Evaluare fiecare variantă, preliminară:**
- **A:** Folosirea conductelor de apă ca PE nu este recomandată, ci exclusă expres.
- **B:** Condițiile în care anumite învelişuri metalice pot avea funcție PE nu includ conductele pentru apă.
- **C:** Interdicția pentru conductele de apă apare expres în I7 §5.5.3.2.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-061 | original **A** | candidat **B** | `POTENTIAL_KEY_MISMATCH_DIRECT`

**Întrebare:** Îmbinarea tuburilor de protecţie a conductoarelor electrice la trecerile prin elemente de construcţie este:

- A. admisă
- B. interzisă
- C. admisă doar pentru tuburi cu diametru mai mic de 16 mm

**Sursa:** [I7 §5.2.12.3.1–.4](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** I7 §5.2.12.3.4 interzice îmbinarea tuburilor la trecerile prin elementele de construcție.
**Context înainte/după / eliminare:** A inversul interdicției, C inventează excepția diametrului 16mm.

**Evaluare fiecare variantă, preliminară:**
- **A:** Admiterea îmbinării în trecere contrazice formularea explicită de interdicție.
- **B:** §5.2.12.3.4 interzice îmbinările tuburilor la trecerea prin construcție.
- **C:** Pragul de diametru 16 mm nu este o derogare din paragraful citat.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-062 | original **A** | candidat **B** | `POTENTIAL_KEY_MISMATCH_MODALITY`

**Întrebare:** În camerele de copii din creşe, grădiniţe, spitale de copii, prizele trebuie montate pe pereţi la următoarele înălţimi măsurate de la axul aparatului la nivelul pardoselii finite:

- A. peste 1m
- B. peste 1,5 m
- C. peste 2m

**Sursa:** [I7 §5.4.25, context §5.4.24 și .26](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Pentru camerele de copii din creșe/grădinițe/spitale: înălțime recomandată peste 1,5m.
**Context înainte/după / eliminare:** A peste 1 m nu garantează minim 1,5; C peste 2m este nivelul recomandat pentru școli în clase, nu pentru categoria cerută. Verbul «trebuie» în grilă vs «se recomandă» în normă.

**Evaluare fiecare variantă, preliminară:**
- **A:** «Peste 1 m» permite și 1,2 m, sub recomandarea de peste 1,5 m din I7.
- **B:** Reproduce pragul «peste 1,5 m» din categoria creșe/grădinițe/spitale pentru copii.
- **C:** «Peste 2 m» privește alt context de încăperi pentru elevi, nu exact categoria din întrebare; totodată înălțimile peste 2 m ar îndeplini matematic și pragul 1,5 m.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-063 | original **C** | candidat **C** | `DIRECT_WITH_SCOPE`

**Întrebare:** Tablourile de distribuţie se vor executa

- A. numai în  construcţie deschisă
- B. numai în construcţie închisă (protejată)
- C. în construcţie deschisă sau închisă, în funcţie de condiţiile de influenţe externe şi grad de protecţie

**Sursa:** [I7 §5.3.3.5–.6](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Tablouri deschise sau închise în funcție de influențele externe și gradul de protecție.
**Context înainte/după / eliminare:** A/B «numai» exclud categoria permisă de normă.

**Evaluare fiecare variantă, preliminară:**
- **A:** «Numai deschisă» exclude tablourile închise permise după mediu.
- **B:** «Numai închisă» exclude tablourile deschise permise după mediu.
- **C:** Reflectă alegerea în funcție de condițiile de influențe externe și gradul de protecție.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-064 | original **B** | candidat **B** | `DIRECT_WITH_SCOPE`

**Întrebare:** În clădirile de locuit se prevăd în fiecare încăpere:

- A. cel mult două prize
- B. prize după necesităţi
- C. cel puţin trei prize

**Sursa:** [I7 §5.4.24–.25](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** În locuințe se prevăd prize în fiecare încăpere după necesități.
**Context înainte/după / eliminare:** A maximum 2 și C minimum 3 sunt cantități universale inexistente în articol.

**Evaluare fiecare variantă, preliminară:**
- **A:** Plafonul universal «cel mult două» nu rezultă din I7.
- **B:** Numărul prizelor se stabilește în funcție de necesitățile încăperii.
- **C:** Minimul universal «cel puțin trei» nu rezultă din I7.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

### Lotul F: 11 întrebări

#### G1-NOR-066 | original **B** | candidat **A** | `POTENTIAL_KEY_MISMATCH_OBJECT`

**Întrebare:** Instalarea conductoarelor electrice în tuburi sau ţevi pozate în pământ:

- A. este interzisă
- B. este admisă
- C. este admisă numai pentru conductoare de cupru

**Sursa:** [I7 §5.2.12.1.3–.5; §5.2.3.2.5](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** I7 §5.2.12.1.4 interzice explicit conductoare electrice în tuburi/țevi pozate în pământ.
**Context înainte/după / eliminare:** Cablurile pozate în tub îngropat apar în alte clauze ca obiect diferit; nu convertim «conductoare» în «cabluri».

**Evaluare fiecare variantă, preliminară:**
- **A:** Textul I7 §5.2.12.1.4 interzice conductoarele în tuburi/țevi pozate în pământ.
- **B:** Permisiunea pentru cabluri îngropate protejate în tub este un obiect distinct, nu excepție pentru conductoare izolate.
- **C:** Nicio derogare generală pentru conductoare din cupru în acest caz nu apare.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-067 | original **C** | candidat **C** | `CONDITIONAL_FUSE_TYPE`

**Întrebare:** Sigutanţele fuzibile sunt dispozitive care protejează:

- A. numai la curenţi de suprasarcină
- B. numai la curenţi de scurtcircuit
- C. atât la curenţi de suprasarcină cât şi la curenţi de scurtcircuit

**Sursa:** [I7 §5.3.4.3 / SR EN 60269; DEER ST89-1 JT 2026 §1.1](https://www.distributie-energie.ro/wp-content/uploads/2026/01/ST-89-1-JT-Sigurante-fuzibile-de-JT-tip-MPR-Ed.U1-Rev.1-2026.pdf)
**Răspuns preferat și motiv:** Fuzibile de uz general gG asigură protecție atât suprasarcină cât și scurtcircuit.
**Context înainte/după / eliminare:** Există tipuri aM care acoperă doar scurtcircuitul, deci «siguranțele fuzibile» fără tip poate supra-generaliza.

**Evaluare fiecare variantă, preliminară:**
- **A:** Există fuzibile gG care protejează și la scurtcircuit, deci «numai suprasarcină» nu este general.
- **B:** Există fuzibile gG care protejează și la suprasarcină, deci «numai scurtcircuit» nu este general.
- **C:** Descrie fuzibilele gG, nu orice clasă: cele aM pot fi doar pentru curenți de defect; întrebarea omite tipul.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-068 | original **B** | candidat **B** | `DIRECT_WITH_CONTEXT`

**Întrebare:** În încăperi în care se impun condiţii speciale de protecţie datorită utilizatorilor (copii, bolnavi mintal etc.), prizele trebuie să fie

- A. montate aparent
- B. prevăzute cu dispozitive de protecţie diferenţială ≤ 30 mA
- C. de tip îngropat

**Sursa:** [I7 §5.4.29](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Prize în încăperi cu utilizatori vulnerabili: DDR ≤30mA, obligatoriu împreună cu tip special.
**Context înainte/după / eliminare:** A și C descriu montaj aparent/îngropat, insuficient ca măsură de protecție a utilizatorilor.

**Evaluare fiecare variantă, preliminară:**
- **A:** Montajul aparent nu garantează protecția utilizatorilor vulnerabili.
- **B:** Protecția diferențială de cel mult 30mA este o cerință relevantă pentru acest tip de utilizatori.
- **C:** Montajul îngropat nu înlocuiește protecția diferențială.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-069 | original **A** | candidat **A** | `DIRECT_WITH_CONTEXT`

**Întrebare:** În încăperi în care se impun condiţii speciale de protecţie datorită utilizatorilor (copii, bolnavi mintal etc.), prizele trebuie să fie

- A. de tip special (de ex. cu obturatori)
- B. de tip îngropat
- C. montate aparent

**Sursa:** [I7 §5.4.29](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Aceleași încăperi: prize de tip special, ex. cu obturatori, și DDR ≤30mA.
**Context înainte/după / eliminare:** B/C reprezintă poziționări, nu tip special contra contactului accidental.

**Evaluare fiecare variantă, preliminară:**
- **A:** Prizele cu obturatori sunt o măsură specifică de prevenire a contactului accidental.
- **B:** Montajul sub tencuială nu definește tipul special de priză.
- **C:** Montajul aparent nu definește tipul special de priză.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-070 | original **A** | candidat **A** | `DIRECT_WITH_SCOPE`

**Întrebare:** Întrerupătoarele, comutatoarele, şi butoanele de lumină trebuie montate:

- A. numai pe conductoarele de fază
- B. numai pe conductorul de nul
- C. pe fază sau pe nul, nu are importanţă

**Sursa:** [I7 §5.4.22](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Comanda iluminatului pe fază, nu pe N.
**Context înainte/după / eliminare:** B/C lasă receptorul sub tensiune chiar dacă nu funcționează.

**Evaluare fiecare variantă, preliminară:**
- **A:** Întreruperea fazei este regula protectivă pentru dispozitivele de comandă a iluminatului.
- **B:** Dacă întrerupi doar N, elementele receptorului pot rămâne sub tensiune de fază.
- **C:** Alegerea fază/N nu este indiferentă din punct de vedere al securității.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-071 | original **C** | candidat **C** | `AMBIGUOUS_PEN_WORDING`

**Întrebare:** Culoarea verde-galben pentru izolaţia conductoarelor si cablurilor se foloseşte pentru marcarea conductorului de:

- A. faza
- B. neutru de lucru
- C. de protecţie şi de neutru

**Sursa:** [I7 §5.1.4.3.1(a)–(c)](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Verde/galben identifică PE și face parte din marcajul PEN, care are și marcaj bleu la capete.
**Context înainte/după / eliminare:** N singur e bleu, nu verde/galben. C este plauzibilă numai dacă «de protecție și de neutru» înseamnă conductor comun PEN, nu PE+N separat.

**Evaluare fiecare variantă, preliminară:**
- **A:** Faza nu este identificată prin combinația verde-galben.
- **B:** Neutrul N separat este identificat prin bleu, nu verde-galben.
- **C:** Are sens numai interpretând funcția mixtă drept PEN cu marcaj verde-galben și suplimentar bleu la capete; formularea este ambiguă.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-072 | original **B** | candidat **B** | `DIRECT_WITH_CONTEXT`

**Întrebare:** Fiecare conductor conectat la bara principală de legare la pământ la tabloul general:

- A. nu este obligatoriu să poată fi deconectat individual
- B. trebuie să poată fi deconectat individual, iar conectarea să fie sigură și deconectabilă numai prin intermediul unei scule
- C. trebuie să poată fi deconectat individual

**Sursa:** [I7 §5.5.2.3](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Conductorul conectat la bara principală se poate deconecta individual, sigur, numai cu sculă.
**Context înainte/după / eliminare:** C omite condiția deconectării cu sculă, A neagă cerința.

**Evaluare fiecare variantă, preliminară:**
- **A:** Contrazice condiția de deconectare individuală pentru verificare.
- **B:** Include atât posibilitatea deconectării individuale, cât și utilizarea unei scule.
- **C:** Omite condiția expresă privind deconectarea numai cu sculă.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-073 | original **B** | candidat **B** | `DIRECT_WITH_SIMPLIFICATION`

**Întrebare:** Legăturile conductoarelor din aluminiu pentru îmbinări sau derivaţii trebuie să se facă:

- A. prin răsucire şi matisare
- B. prin cleme speciale, prin presare cu scule speciale sau prin sudare
- C. prin lipire cu cositor

**Sursa:** [I7 §5.2.6.8–.9](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Îmbinări de Al cu cleme speciale, presare/scule adecvate, metalizare-lipire ori sudare.
**Context înainte/după / eliminare:** A răsucire simplă nu este normativ; C lipire simplă cu cositor nu este metoda din norma Al. B este cea mai apropiată dar simplifică lista permisă.

**Evaluare fiecare variantă, preliminară:**
- **A:** Răsucirea și matisarea simplă nu este metoda reglementată pentru conexiuni din aluminiu.
- **B:** Clemele speciale, presarea adecvată și sudarea corespund metodei de realizare a legăturilor Al.
- **C:** Lipirea simplă cu cositor nu reproduce metodele sau pregătirea specială din paragraf.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-074 | original **C** | candidat **C** | `DIRECT_WITH_SCOPE`

**Întrebare:** Marcarea conductorului neutru  care asigură simultan și funcţia de protecţie (PEN) se face

- A. cu  culoarea bleu                                 pe toată  lungimea
- B. prin culori verde/galben pe toată  lungimea
- C. prin culori verde/galben pe toată  lungimea şi suplimentar marcare cu
     culoarea bleu la fiecare extremitate;

**Sursa:** [I7 §5.1.4.3.1(b)](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** PEN: verde/galben pe lungime și albastru la fiecare extremitate.
**Context înainte/după / eliminare:** A sau B singure omit marcaje esențiale.

**Evaluare fiecare variantă, preliminară:**
- **A:** Bleu integral este identificarea N separat, nu PEN.
- **B:** Verde-galben fără marcajele bleu la capete este incomplet pentru PEN.
- **C:** Verde-galben pe lungime și bleu la capete este marcajul PEN complet.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-075 | original **A** | candidat **A** | `DIRECT_WITH_SCOPE`

**Întrebare:** Marcarea conductorului neutru (N) se face:

- A. cu culoarea bleu                                   pe toată lungimea.
- B. prin culori verde/galben pe toată  lungimea
- C. cu culoarea bleu                           la fiecare extremitate;

**Sursa:** [I7 §5.1.4.3.1(c)](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Conductorul N marcat bleu pe toată lungimea.
**Context înainte/după / eliminare:** B este marcaj PE, iar C doar la capete omite continuitatea la cablu cu N standard.

**Evaluare fiecare variantă, preliminară:**
- **A:** Bleu pe întreaga lungime este identificarea standard a conductorului N.
- **B:** Verde-galben este rezervat pentru funcția de protecție.
- **C:** Bleu doar la capete nu reproduce marcajul de-a lungul întregului N, cu excepțiile speciale neinvocate.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-076 | original **A** | candidat **A** | `DIRECT_WITH_SCOPE`

**Întrebare:** Conform normativului I-7-2011, o coloană electrică  este un circuit electric care:

- A. alimentează un tablou de distribuţie.
- B. alimentează un receptor de putere
- C. alimentează mai multe surse de iluminat

**Sursa:** [I7 Cap. 2 Terminologie: «coloană electrică»](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Coloană: circuit care alimentează unul sau mai multe tablouri de distribuție.
**Context înainte/după / eliminare:** B consumator receptor și C lumină sunt circuite terminale; A «un tablou» este caz valid al definiției mai generale.

**Evaluare fiecare variantă, preliminară:**
- **A:** Circuitul care alimentează un tablou este un caz inclus în definiția coloanei.
- **B:** Circuitul unui receptor de putere nu este, prin sine, circuit de alimentare a tabloului.
- **C:** Alimentarea surselor de iluminat este un circuit terminal, nu o coloană.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

### Lotul G: 12 întrebări

#### G1-NOR-077 | original **C** | candidat **C** | `DIRECT_WITH_SCOPE`

**Întrebare:** Conform normativului I-7-2011, o coloană electrică  este un circuit electric care:

- A. alimentează mai multe surse de iluminat
- B. alimentează un receptor de putere
- C. alimentează mai multe tablouri de distribuţie.

**Sursa:** [I7 Cap. 2 Terminologie: «coloană electrică»](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Aceeași definiție permite alimentarea mai multor tablouri de distribuție.
**Context înainte/după / eliminare:** A/B alte circuite; C nu e definiția completă dar un caz explicit permis.

**Evaluare fiecare variantă, preliminară:**
- **A:** Alimentarea surselor de iluminat este circuit terminal.
- **B:** Alimentarea unui receptor de putere este circuit terminal.
- **C:** Alimentarea mai multor tablouri este un caz explicit din definiția coloanei.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-078 | original **B** | candidat **B** | `DIRECT_DEFINITION`

**Întrebare:** În cazul instalațiilor electrice de joasă tensiune, izolaţia de bază reprezintă:

- A. Izolaţia care asigură protecţia de defect
- B. izolaţia părţilor active periculoase
- C. izolaţia maselor

**Sursa:** [I7 Cap. 2 Terminologie: «izolație de bază»](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Izolația părților active periculoase asigură protecția de bază.
**Context înainte/după / eliminare:** A se referă la defect, rol al izolației suplimentare; C izolația maselor, nu părților active.

**Evaluare fiecare variantă, preliminară:**
- **A:** Protecția la defect este distinctă de rolul izolației de bază la atingere directă.
- **B:** Izolația părților active periculoase asigură protecția de bază.
- **C:** Izolația maselor nu este definiția izolației de bază.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-079 | original **C** | candidat **C** | `DIRECT_WITH_SCOPE`

**Întrebare:** . Atunci când un echipament nu conţine, prin construcţie, caracteristici corespunzătoare influenţelor externe ale locului  (sau amplasamentului):

- A. el nu poate fi utilizat în instalația electrică
- B. el poate fi totuşi utilizat cu condiţia ca instalația să fie montată în tub
- C. el poate fi totuşi utilizat cu condiţia să fie prevăzut cu o protecţie suplimentară corespunzătoare la realizarea instalaţiei

**Sursa:** [I7 §5.1.2.1–.2](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Echipament fără caracteristici native de mediu poate fi folosit cu protecție suplimentară potrivită.
**Context înainte/după / eliminare:** A interdicție absolută greșită; B tubul nu este neapărat protecția adecvată tuturor influențelor.

**Evaluare fiecare variantă, preliminară:**
- **A:** Interdicția absolută ignoră posibilitatea montării unei protecții suplimentare.
- **B:** Un tub oarecare nu asigură automat toate caracteristicile necesare pentru influențele externe.
- **C:** Protecția suplimentară adecvată poate compensa lipsa caracteristicilor constructive.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-080 | original **C** | candidat **C** | `DIRECT_WITH_EXCEPTION`

**Întrebare:** Pentru instalaţiile electrice de iluminat şi putere (forţă):

- A. se prevede întotdeauna tablou electric de distribuţie comun
- B. se prevăd întotdeauna tablouri electrice  de distribuţie diferite
- C. se prevede tablou electric de distribuţie comun, cu unele excepţii:

**Sursa:** [I7 §3.1.5.5](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Tablou comun pentru iluminat și forță, cu excepții enumerate (tarife diferențiate etc.).
**Context înainte/după / eliminare:** A «întotdeauna» ignore excepții; B «întotdeauna separate» contrazice regula.

**Evaluare fiecare variantă, preliminară:**
- **A:** «Întotdeauna comun» ignoră cazurile expres exceptate.
- **B:** «Întotdeauna diferite» contrazice regula generală comună.
- **C:** Redă regula tabloului comun împreună cu excepțiile sale.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-081 | original **C** | candidat **C** | `NEEDS_SEMANTIC_SCOPE_QA_CABLE_AND`

**Întrebare:** Montarea în contact direct cu materiale combustibile se admite

- A. pentru cabluri cu izolație din PVC
- B. pentru toate tuburile şi plintele din materiale plastice
- C. pentru cabluri cu întârziere la propagarea flăcării

**Sursa:** [I7 §3.0.3.7, §5.2.12.2.13](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Montare directă cu materiale combustibile admisă pentru cabluri cu caracteristici de reacție la foc cerute, plus alte categorii condiționate.
**Context înainte/după / eliminare:** §3.0.3.7 folosește sintagma «cabluri rezistente la foc și cu întârziere la propagarea flăcării»; verificarea literală a conjuncției «și» este necesară. Varianta C redă doar una dintre caracteristici; nu se poate afirma o unicitate completă fără norma de produs și contextul tehnic.

**Evaluare fiecare variantă, preliminară:**
- **A:** Simpla izolație PVC nu dovedește clasificarea de reacție la foc cerută.
- **B:** Nu toate tuburile/plintele de plastic îndeplinesc condițiile de instalare la materiale combustibile.
- **C:** Caracteristica de întârziere a propagării flăcării este criteriul relevant, dar se verifică cerințele produsului și amplasamentul.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-082 | original **B** | candidat **B** | `NEEDS_SEMANTIC_SCOPE_QA_CABLE_AND`

**Întrebare:** Montarea în contact direct cu materiale combustibile se admite

- A. pentru toate tuburile şi plintele din materiale plastice
- B. pentru cabluri rezistente la foc
- C. pentru cabluri cu izolație din PVC

**Sursa:** [I7 §3.0.3.7](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Cablurile rezistente la foc fac parte din categoria admisă de articol, sub condiții de instalare.
**Context înainte/după / eliminare:** §3.0.3.7 folosește sintagma «cabluri rezistente la foc și cu întârziere la propagarea flăcării»; varianta B menționează numai rezistența la foc. A valida B necondiționat ignoră a doua proprietate formulată conjunctiv. Se menține candidatura, cu blocaj semantic până la verificare.

**Evaluare fiecare variantă, preliminară:**
- **A:** «Toate» tuburile și plintele de plastic este nejustificat.
- **B:** Cablurile rezistente la foc pot satisface categoria prevăzută pentru contact cu materiale combustibile, în condițiile articolului.
- **C:** PVC, fără clasa de reacție la foc verificată, nu este suficient.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-083 | original **B** | candidat **B** | `DIRECT_WITH_CONTEXT`

**Întrebare:** Prizele cu tensiunea de 230 V care se montează într-o instalație electrică trebuie să fie întotdeauna:

- A. în construcţie capsulată
- B. cu contact de protecţie
- C. în execuţie sub tencuială

**Sursa:** [I7 §5.4.8; §5.3.2.4 ca alt obiect](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Prizele fixe 230V cu contact de protecție.
**Context înainte/după / eliminare:** A capsulate/C îngropate nu sunt universal necesare; clasa II a aparatului nu elimină contactul PE al prizei fixe.

**Evaluare fiecare variantă, preliminară:**
- **A:** Capsularea nu este obligatorie universal pentru toate prizele fixe 230V.
- **B:** Contactul de protecție este cerință generală pentru aceste prize.
- **C:** Montajul sub tencuială nu este obligatoriu universal.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-084 | original **B** | candidat **B** | `DIRECT_DEFINITION`

**Întrebare:** Conform I7/2011, conductor de protecţie (PE)

- A. este un conductor prevăzut în linile aeriene de joasă tensiune pentru protecția împotriva loviturilor de trăsnet
- B. este un conductor prevăzut în scopuri de securitate, de exemplu protecţia împotriva şocurilor electrice.
- C. nu există conductor de protecție în instalațiile de joasă tensiune

**Sursa:** [I7 Cap. 2 Terminologie: «conductor de protecție (PE)»](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** PE conductor pentru securitate, inclusiv protecție la șoc electric.
**Context înainte/după / eliminare:** A parafulger LEA e alt rol, C neagă existența PE.

**Evaluare fiecare variantă, preliminară:**
- **A:** Conductorul paratrăsnet al unei LEA nu definește funcția generală PE.
- **B:** Definește PE drept conductor destinat securității și protecției la șoc.
- **C:** Conductorul PE există expres în I7 și schemele de instalații.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-085 | original **C** | candidat **C** | `DIRECT_DEFINITION`

**Întrebare:** Legarea la pământ  reprezintă realizarea unei legături electrice

- A. numai între un punct dat al unui echipament şi un pământ local.
- B. numai între un punct dat al unei reţele şi un pământ local.
- C. între un punct dat al unei reţele sau al unui echipament şi un pământ local.

**Sursa:** [I7 Cap. 2 Terminologie: «legare la pământ»](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Conexiune punct rețea/instalație/echipament la pământ local.
**Context înainte/după / eliminare:** A/B «numai» restrâng incorect sfera la echipament, respectiv rețea.

**Evaluare fiecare variantă, preliminară:**
- **A:** «Numai echipament» restrânge definiția, care include rețelele.
- **B:** «Numai rețea» restrânge definiția, care include echipamentele.
- **C:** Acoperă atât un punct al rețelei, cât și unul al echipamentului în legătură cu pământul local.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-086 | original **B** | candidat **B** | `DIRECT_WITH_EXCEPTION`

**Întrebare:** Conductoarele, barele, tuburile etc.

- A. nu se pot dispune pe trasee comune cu traseele altor instalaţii
- B. se pot dispune pe trasee comune cu traseele altor instalaţii cu îndeplinirea unor condiţii
- C. se pot dispune pe trasee comune cu traseele altor instalaţii, fără alte condiții, dacă sunt în montaj aparent.

**Sursa:** [I7 §3.0.3.1–.3](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Trasee comune cu alte instalații sunt permise condiționat de poziționare/distanțe/protecții.
**Context înainte/după / eliminare:** A total interzisă fals, C fără condiții fals.

**Evaluare fiecare variantă, preliminară:**
- **A:** Interdicția totală ignoră montările comune admise cu protecție/distante.
- **B:** Permite traseul comun condiționat de regulile de vecinătate și protecție.
- **C:** Montajul aparent nu elimină condițiile de distanță/protecție.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-087 | original **C** | candidat **C** | `DIRECT_WITH_SCOPE`

**Întrebare:** Utilizarea conductelor metalice pentru gaze şi/sau lichide inflamabile drept conductoare de protecţie:

- A. este recomandată
- B. este permisă condiţionat
- C. nu este permisă

**Sursa:** [I7 §5.5.3.2](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Conductele de gaz ori lichid inflamabil sunt explicit nepermise ca PE.
**Context înainte/după / eliminare:** A/B ar confunda cu obligativitatea echipotențializării, care nu le transformă în conductoare PE.

**Evaluare fiecare variantă, preliminară:**
- **A:** Folosirea conductelor de gaze/inflamabile ca PE este interzisă, nu recomandată.
- **B:** Nu există o permisiune generală condiționată pentru astfel de conducte.
- **C:** Interdicția expresă este relevantă pentru acest obiect.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

#### G1-NOR-088 | original **A** | candidat **A** | `DIRECT_WITH_EXCEPTION`

**Întrebare:** Dacă instalaţiile electrice sunt în distribuţie prefabricată în învelişuri metalice (cutii, carcase), aceste învelişuri

- A. pot fi utilizate drept conductoare de protecţie, în anumite condiții
- B. nu pot fi utilizate drept conductoare de protecţie
- C. pot fi utilizate întotdeauna drept conductoare de protecţie

**Sursa:** [I7 §5.5.3.1–.2](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011)
**Răspuns preferat și motiv:** Carcasa metalică a unui sistem de distribuție poate fi PE dacă asigură continuitate și conexiuni conform clauzei.
**Context înainte/după / eliminare:** B neagă permisiunea, C «întotdeauna» omite condițiile.

**Evaluare fiecare variantă, preliminară:**
- **A:** Învelişurile metalice de distribuție prefabricată pot funcționa ca PE dacă îndeplinesc condițiile specificate.
- **B:** Interdicția absolută ignoră excepția permisivă cu condiții.
- **C:** «Întotdeauna» omite condițiile de continuitate și adecvare.

**Limitări:** sursa/paragraful nu este atestată pentru ediția integrală 2026, QA independent nu a rulat, baremul original rămâne neschimbat.

## QA structural executat

- 36/36 ID-uri unice, în CSV original; 36/36 Q/A/B/C/cheie perfect identice cu snapshotul din Library.
- Fiecare intrare are paragraf de referință, domeniu, context, sursă, trei variante și **trei explicații distincte A/B/C**, candidat, limitări, și `approved_for_learning=false`.
- 7 candidați diferă de cheia locală; numărul de corecții efectuate este **zero**.
- Nu am efectuat un benchmark al modelelor, validarea independentă a legislației 2026, editări GitHub sau probe offline APK.

## Următorul pas

1. Preflight original Excel oficial ANRE (banca actualizată) și ediția exactă I7/PE155 pentru cazurile P0.
2. Revizie independentă pe A/B/C, mai ales pentru NOR053, 054, 058, 060, 061, 062, 066 și cele condiționate (NOR067, NOR071).
3. Continua loturile din grupa problemelor rămase; implică utilizatorul numai la interpretare lingvistică fără rezolvare după verificări.
