# CKPT-241 | GFR | 15 original P2 QABC plus 11 fresh exact cross-grade references | 2026-11-19

## Reconciliation and provenance
- Baseline register V119 Git blob `e6cd1eddbcffc1801b512c351f3434b3d5b38f00`; canonical source QABC/key V73 Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`.
- 15 original Grade-I cards receive source-scoped interpretive A/B/C analysis with explicit countermodels. 15 Grade-II identical QABC+key correspondences confirmed; only 11 Grade-II rows newly linked because G2-ELEC-268 was already V82 and G2-ELEC-293/325/329 were already V87. Existing evidence not overwritten, no double-counting.
- **26 Grade ID rows newly linked** (15 original +11 exact reuse), remaining without focused links **216 -> 190**. Reuse is NOT an independent technical review.
- Sources are physics textbooks, manufacturer guides, vendor or educational resources; multiple are SEARCH_ONLY and their full paragraphs were not accessible. No claim of 2026 ANRE bibliography authentication, official scored key, or source-rights redistribution.
- Original key / risk / learning approval unchanged. Independent technical review, independent linguistic/source review, 2026 bibliographic check, human sign-off remain NOT_RUN / NOT_VERIFIED. No release authority.

## G1-ELE-128 ↔ G2-ELEC-268
- **Original Q:** Într-un circuit electric monofazat cu caracter inductiv tensiunea este defazata fata de curent:
- **A:** înainte cu 90 de grade
- **B:** cu zero grade (sunt în faza)
- **C:** cu 90 de grade în urma
- **Imported key unchanged:** A
- **A/B/C and model / exceptions:** A presupune bobină pur inductivă L ideală și atunci U este înaintea I cu 90°. Pentru circuit cu R>0 și X_L>0 unghiul este φ=atan(X_L/R) în intervalul (0°;90°), astfel răspunsul A nu este universal pentru orice circuit cu «caracter inductiv». B este adevărat numai pentru φ=0 (rezistiv), C indică defazaj capacitiv. Necesită marcaj AMBIGUOUS_MODEL.
- **Source directly relevant to model:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- **Exact target locator:** Inductor: current lags voltage by pi/2 for pure ideal L
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-134 ↔ G2-ELEC-274
- **Original Q:** Intr-un tor (solenoid de formă circulară bobinat), energia magnetică produsă de un curent care străbate bobinajul torului este localizată:
- **A:** integral în câmpul magnetic din volumul torului
- **B:** integral în câmpul magnetic din afara torului
- **C:** 1/2 din energie este înmagazinată în volumul torului, iar 1/2 în afara torului
- **Imported key unchanged:** A
- **A/B/C and model / exceptions:** A corespunde toroidului ideal uniform bobinat: câmpul și energia sa sunt localizate în interior. B pretinde exclusiv exterior, fals în model. C împărțire 50/50 nejustificată. Sursa confirmă un câmp de scăpări mic la spire reale, deci «integral» nu este absolut pentru toroid fizic; condiție de model.
- **Source directly relevant to model:** https://openstax.org/books/university-physics-volume-2/pages/12-6-solenoids-and-toroids
- **Exact target locator:** Toroids paragraphs 113-145; outside ideal toroid B=0; finite winding leakage
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-146 ↔ G2-ELEC-284
- **Original Q:** La transformatoarele la care comutarea ploturilor se face cu transformatorul în sarcina, comutatorul de ploturi se montează:
- **A:** pe înfăşurarea de tensiune mai mica, deoarece tensiunea este mai mica
- **B:** pe înfăşurarea de tensiune mai mare, deoarece curentul este mai mic
- **C:** pe oricare dintre înfăşurări
- **Imported key unchanged:** B
- **A/B/C and model / exceptions:** B descrie amplasarea uzuală pe înfășurarea cu tensiune mai mare și curent mai mic pentru aceeași putere; A are argumentul tensiunii mici dar nu acoperă practica tipică. C «oricare» poate fi tehnic posibil în proiectări speciale, iar Reinhausen afirmă explicit că poziționarea este condiționată de design. Nu declara B universal.
- **Source directly relevant to model:** https://www.reinhausen.com/newsroom/mr-knowledge-base/tap-changer-basics
- **Exact target locator:** OLTC position high-voltage or low-voltage winding depends on transformer design and client requirements
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-151 ↔ G2-ELEC-289
- **Original Q:** O siguranţa mai mare în alimentarea consumatorilor de energie electrica se realizează prin:
- **A:** reţele radiale
- **B:** reţele buclate cu funcţionare radialã
- **C:** reţele buclate
- **Imported key unchanged:** C
- **A/B/C and model / exceptions:** C rețele buclate exploatate efectiv în buclă pot furniza redundanță și căi alternative; A radial simplu poate pierde alimentarea pentru un defect pe trunchi. B buclat cu exploatare radială permite restabilire prin manevre, poate oferi fiabilitate ridicată. Comparația B vs C nu este universală: protecția, exploatarea și continuitatea serviciului fac verdictul dependent de condiții. MARCAT AMBIGUU; sursa este numai rezumatul de căutare.
- **Source directly relevant to model:** https://ieeexplore.ieee.org/document/9162500/
- **Exact target locator:** IEEE urban mesh-constructed radial-operated outage transfer adjacent feeders; full paper not available
- **Actual retrieval status:** SEARCH_ONLY_SOURCE_ABSTRACT. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-155 ↔ G2-ELEC-293
- **Original Q:** Mărirea cuplului de pornire şi micşorarea curentului de pornire la motoarele asincrone cu rotorul în scurtcircuit se face:
- **A:** prin deconectarea şi reconectarea lor la reţeaua de alimentare
- **B:** numai prin utilizarea motoarelor cu rotorul în dublă colivie
- **C:** prin utilizarea motoarelor cu rotorul în colivie cu bare înalte
- **Imported key unchanged:** C
- **A/B/C and model / exceptions:** C barele înalte prin efect pelicular cresc rezistența efectivă la pornire, cresc cuplul relativ și pot reduce curentul de pornire. A reconectarea simplă nu produce tehnica solicitată. B «numai» cu dublă colivie este exclus de varianta cu bare înalte. Ambele construcții pot fi utile; C singura opțiune fără exclusivitate falsă.
- **Source directly relevant to model:** https://yourelectricalguide.com/2023/04/influence-of-rotor-parameters-on-torque-speed-curves.html
- **Exact target locator:** Deep Bar Rotors section: high-starting torque with lower current; double cage alternative
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-175 ↔ G2-ELEC-311
- **Original Q:** Care dintre urmatoarele enunturi nu este adevarat:
- **A:** energia electrica tranzitata            printr-un circuit este produsul dintre puterea medie si timpul de functionare;
- **B:** energia electrica tranzitata printr-un circuit este produsul dintre puterea maxima si timpul de functionare
- **C:** energia electrica tranzitata printr-un circuit este produsul dintre puterea maxima si timpul de utilizare al puterii maxime.
- **Imported key unchanged:** B
- **A/B/C and model / exceptions:** A E=Pmediu·T este definiția puterii medii pe interval; C E=Pmax·T_utilizare este definiția timpului echivalent de utilizare a puterii maxime. B E=Pmax·T_total nu este adevărat în general decât încărcare constantă la maxim, de aceea este enunțul fals cerut. Sursa EIA verifică termenii mediu/vârf dar definiția specifică T_utilizare trebuie confirmată în materialul ANRE.
- **Source directly relevant to model:** https://www.eia.gov/tools/glossary/index.php?id=load
- **Exact target locator:** Glossary load factor average and peak load; mathematical relation E=P_avg*T=P_max*T_equiv derived
- **Actual retrieval status:** OPENED_HTML_PARTIAL_SCOPE. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-176 ↔ G2-ELEC-312
- **Original Q:** Pentru calculul curenţilor de scurtcircuit într-o reţea prin metoda componentelor simetrice, reţeaua inversă (negativă) se compune din:
- **A:** impedanţe identice cu ale reţelei directe (pozitive) pentru elemente statice și impedanţe diferite de ale reţelei directe (pozitive) pentru maşini rotative
- **B:** impedanţe identice cu ale reţelei directe (pozitive) atât pentru elemente statice cât și pentru maşini rotative
- **C:** impedanţe diferite de ale reţelei directe (pozitive) pentru elemente statice
- **Imported key unchanged:** A
- **A/B/C and model / exceptions:** A corespunde analizei uzuale: elementele statice liniare și simetrice au Z2≈Z1, iar mașinile rotative au impedanțe de secvență diferite. B impune Z2=Z1 inclusiv pentru mașini rotative, fals în general. C susține că Z2 static diferă, în general fals. Necesită exacta ediție oficială și condițiile mașinii; oglindă a unui standard restricționat nu este sursă certificată.
- **Source directly relevant to model:** https://studylib.net/doc/28003419/30023-2018
- **Exact target locator:** IEEE 3002.3-2018 section 6.7.2: static sequence impedances same positive/negative; rotating differ
- **Actual retrieval status:** OPENED_HTML_SECONDARY_STANDARD_MIRROR. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-177 ↔ G2-ELEC-313
- **Original Q:** Pentru limitarea curenţilor de scurtcircuit se utilizează bobine:
- **A:** înseriate pe circuit, monofazate, fără miez de fier, răcite cu aer (uscate), de tip interior;
- **B:** racordate în derivaţie pe circuit, monofazate, fără miez de fier, răcite cu aer (uscate), de tip interior;
- **C:** înseriate pe circuit, monofazate, cu miez de fier, răcite cu ulei, de tip interior;
- **Imported key unchanged:** A
- **A/B/C and model / exceptions:** A descrie o configurație tipică pentru limitarea curentului de defect: reactor în serie fără miez feromagnetic pentru a evita saturarea. B în derivație nu crește reactanța serie a traseului de scurtcircuit; C cu fier și ulei poate exista în alte aplicații dar nu este tipul uzual menționat. Specificațiile «monofazat de interior și uscat» nu sunt demonstrate ca obligatorii pentru orice caz.
- **Source directly relevant to model:** https://trench-group.com/air-core-coils/air-core-series-reactors/
- **Exact target locator:** Current Limiting Reactors: series air-core line/bus-tie reactors
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-179 ↔ G2-ELEC-315
- **Original Q:** Puterea nominala a unui motor electric se defineşte astfel:
- **A:** puterea activã absorbitã de motor de la reţea când este alimentat la Un si absoarbe In
- **B:** puterea activã transmisã prin întrefierul motorului când este alimentat la Un si absoarbe In
- **C:** puterea mecanicã debitatã de motor la arbore când este alimentat la Un si absoarbe In
- **Imported key unchanged:** C
- **A/B/C and model / exceptions:** C definește puterea mecanică nominală la arbore. A este puterea electrică absorbită înainte de pierderi; B puterea electromagnetică de întrefier, înainte de pierderile rotor/mecanice. Barem C este compatibil cu definițiile uzuale, dar pagina ABB a fost returnată incomplet la deschidere; locatorul exact nu este certificat.
- **Source directly relevant to model:** https://www.abb.com/global/en/news/132261/how-to-read-a-nema-motor-nameplate
- **Exact target locator:** ABB search excerpt: horsepower is mechanical motor output rating
- **Actual retrieval status:** SEARCH_ONLY_FETCHEd_MINIMAL. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-189 ↔ G2-ELEC-325
- **Original Q:** Potenţialul electrostatic în punctul M este  :
- **A:** lucrul mecanic care trebuie produs spre a transporta unitatea de sarcină pozitivă de la infinit până în punctul M.
- **B:** forţa care este necesară pentru a transporta unitatea de sarcină pozitivă de la infinit până în punctul M
- **C:** forţa care este necesară pentru a transporta unitatea de sarcină pozitivă din punctul M până la infinit
- **Imported key unchanged:** A
- **A/B/C and model / exceptions:** A munca externă per sarcină pozitivă unitară din infinit la M definește potențialul electrostatic față de referința 0 la infinit. B și C vorbesc de forță și au unități N, nu J/C. Semnul depinde de distincția muncă externă versus muncă realizată de câmp; A «trebuie produs» presupune agent extern.
- **Source directly relevant to model:** https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference
- **Exact target locator:** Potential is work/charge or potential energy per unit test charge; infinity reference
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-193 ↔ G2-ELEC-329
- **Original Q:** Carcasa  unei celule electrice
- **A:** asigură numai protecţia persoanelor împotriva atingerii accidentale a pieselor aflate sub tensiune în funcţionare normală sau a pieselor în mişcare din interiorul învelişului;
- **B:** asigură protecţia echipamentului electric împotriva pătrunderii corpurilor străine şi a umezelii;
- **C:** asigură protecţia echipamentului electric împotriva supratensiunilor.
- **Imported key unchanged:** B
- **A/B/C and model / exceptions:** B protejarea echipamentului împotriva pătrunderii corpurilor străine și umezelii corespunde funcției învelișului și gradului IP. A conține «numai», însă carcasa protejează și echipamentul; C nu asigură în sine protecție la supratensiuni. Verifică tipul celulei/grad IP, nu toate carcasele oferă aceeași etanșeitate.
- **Source directly relevant to model:** https://electrical-engineering-portal.com/installation-guidelines-mv-metal-enclosed-switchgear-controlgear-iec-62271-200
- **Exact target locator:** IEC 62271-200 enclosure IP protection against contact and ingress
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-194 ↔ G2-ELEC-330
- **Original Q:** Principalul avantaj al motoarelor asincrone cu rotorul în scurtcircuit cu simplă colivie îl constituie:
- **A:** curentul mic de pornire
- **B:** pornirea fără dispozitiv de pornire
- **C:** cuplul de pornire foarte bun
- **Imported key unchanged:** B
- **A/B/C and model / exceptions:** B sugerează că motorul simplă colivie poate porni direct la rețea fără dispozitiv special de pornire, avantaj uzual față de rotor bobinat. A «curent mic» este fals la pornirea directă; C «cuplu foarte bun» nu se aplică universal simplei colivii. B este condiționată de mărime/rețea/sarcină și tot este necesar aparat de manevră.
- **Source directly relevant to model:** https://easa.com/resources/resource-library/squirrel-cage-induction-motor-starting-methods
- **Exact target locator:** Across-the-line starting applies full voltage; reduced voltage starters alternatives
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-195 ↔ G2-ELEC-331
- **Original Q:** Principalul avantaj al motoarelor de curent continuu îl constituie faptul că:
- **A:** permit reglarea în limite largi a turaţiei
- **B:** nu necesită întreţinere permanentă
- **C:** prezintă o construcţie simplă şi robustă
- **Imported key unchanged:** A
- **A/B/C and model / exceptions:** A turație reglabilă în limite largi prin tensiunea armăturii sau excitare descrie avantaj istoric al motoarelor DC. B lipsa întreținerii este fals pentru modelele cu colector; C construcția simplă robustă nu caracterizează tipic DC cu perii. Azi VFD pentru AC poate oferi beneficii comparabile; context istoric al baremului trebuie păstrat.
- **Source directly relevant to model:** https://technav.ieee.org/topic/dc-motors/
- **Exact target locator:** IEEE topic summary wide-range speed control; page fetch cache miss
- **Actual retrieval status:** SEARCH_ONLY_OPEN_FAILED. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-203 ↔ G2-ELEC-339
- **Original Q:** Reactanţa supratranzitorie a unui motor este:
- **A:** direct proporţionala cu curentul de pornire
- **B:** invers proporţionala cu curentul de pornire
- **C:** invers proporţionala cu pătratul tensiunii de alimentare
- **Imported key unchanged:** B
- **A/B/C and model / exceptions:** B: la aceeași tensiune și bază de putere, reactanța/impedanța supratranzitorie echivalentă estimată este invers proporțională cu curentul de rotor blocat pornire. A inversează dependența; C indică pătratul tensiunii, nejustificat pentru reactanța intrinsecă. Precizare esențială: sursa tratează Xʺ sau Xlr aproximativ prin impedanță, neglijând explicit R și variații de saturație. Nu universal pentru orice motor.
- **Source directly relevant to model:** https://help.easypower.com/ezp/25.0/Content/13_Database_Technical_Ref/Motor/Short_Circuit_Tab.htm
- **Exact target locator:** X double prime or locked-rotor reactance estimated as 100/LRM percent; starting current multiplier
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## G1-ELE-204 ↔ G2-ELEC-340
- **Original Q:** Un regim energetic  este deformant
- **A:** dacă undele de curent şi tensiune nu sunt periodice
- **B:** numai dacă undele de curent şi de tensiune sunt ambele periodice şi nesinusoidale
- **C:** undele de curent şi tensiune sunt periodice iar cel puțin una este nesinusoidală
- **Imported key unchanged:** C
- **A/B/C and model / exceptions:** C: regim periodic în care cel puțin unul dintre curent/tensiune este nesinusoidal constituie regim deformant. A nu cere periodicitate, nu descrie modelul armonic staționar; B «numai ambele» fals pentru sarcină neliniară alimentată de tensiune sinusoidală cu curent distorsionat. Condițiile periodicității și frecvenței fundamentale sunt relevante.
- **Source directly relevant to model:** https://www.electrical-installation.org/enwiki/Definition_of_harmonics
- **Exact target locator:** Harmonic currents and/or voltages deviate from sinusoidal waveforms under periodic operation
- **Actual retrieval status:** OPENED_HTML. NOT authenticated ANRE exam key; technical source QA by same assistant, not independent review.

## High-risk observations
- **G1-ELE-128:** A requires pure inductance; general inductive circuits need not be 90 degrees.
- **G1-ELE-134:** 'integral' only follows from ideal toroid; real toroidal windings leak magnetic field.
- **G1-ELE-146:** manufacturer states tap-changer placement depends on transformer design; do not claim high-voltage mounting mandatory.
- **G1-ELE-151:** network reliability comparison lacks protection, operation, switching and outage criteria. FLAG AMBIGUOUS.
- **G1-ELE-203:** Xʺ vs locked rotor current is an approximation under normalized assumptions, not universal circuit law.

## QA structural and scope
- Exact original question+A+B+C+key matches 15/15; Grade-II counterpart keys identical; 26 changed rows with allowed metadata only; unchanged grade rows preserved byte for byte; 822 IDs retained in original order.
- Existing 50 non-standard serialized comma rows remain intact, not silently repaired; separate full CSV parser/reconciliation gate remains.
- **No** key modification, app HTML/APK modification, merge/release, or learning approval. PR #7 stays Draft.
