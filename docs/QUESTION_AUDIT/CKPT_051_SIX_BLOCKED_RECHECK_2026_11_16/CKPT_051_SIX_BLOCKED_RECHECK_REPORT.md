# CKPT-051 | Reanaliza celor 6 BLOCKED din CKPT-050 | 2026-11-16

**Bază:** PR #7 Draft, ramura \`audit/anre-v8-priority-17-20261109\`, HEAD anterior \`b7c5f260407c91082d9a9b69a058a16db3c5942c\`. Acest checkpoint NU adaugă unități noi: cele șase QABC și cele 12 ID-uri sunt deja cuprinse în 114/568 unități și 139/822 ID-uri contextual documentate. Nu modificați aceste numărători pentru o reverificare.

**Restricții:** enunțuri, A/B/C, chei, CSV canonic, HTML, APK, main, release și merge intacte. Zero aprobări pentru învățare. Reanaliza tehnică este făcută de același asistent, NU de un specialist independent; ediția/referința oficială aplicabilă examenului ANRE în 2026 nu este atestată de sursele didactice. Sursele PDF au fost citite textual; încercările de screenshot prin browser au dat CACHE_MISS, deci nu se pretinde QA vizual al paginilor. Este cercetare documentară cu calcule reproductibile, nu semnătură finală.

## Rezumatul decizional

| Unitate/ID-uri G1+G2 | Barem original | Rezultat al reanalizei, FĂRĂ aprobare | Condiție-cheie |
|---|---|---|---|
| ELE-057 / G1-ELE-057, G2-ELEC-203 | A | BLOCKED_NON_UNIQUE | Ordinea raportului și definiția armonicilor permit exemple B/C |
| ELE-128 / G1-ELE-128, G2-ELEC-268 | A | BLOCKED_NO_EXACT_OPTION | „Cu caracter inductiv” nu implică 90°; pentru RL, φ poate fi 45° |
| ELE-222 / G1-ELE-222, G2-ELEC-358 | C | BLOCKED_WRONG_GENERALIZATION | B=Im(1/Z), nu neapărat 1/X într-un circuit mixt |
| ELE-231 / G1-ELE-231, G2-ELEC-367 | B | INTENDED_B_CONDITIONAL | Semnal fizic instantaneu versus fazor complex, dar RMS este real și măsurabil |
| ELE-245 / G1-ELE-245, G2-ELEC-381 | A | INTENDED_A_EQUIVALENT_BEHAVIOR | PF=1 caracter rezistiv la borne, NU obligatoriu doar rezistoare |
| ELE-257 / G1-ELE-257, G2-ELEC-392 | B | B_DIDACTIC_SUPPORT_STRONG | În electrotehnica românească ψ=∫D·dS [C]; E-flux are altă unitate |

Sursa tuturor celor șase enunțuri/chei: banca V73, \`docs/QUESTION_AUDIT/V73_ALL_822_EVIDENCE_AND_RELEASE_GATES_MASTER.csv\`, \`source_file=ELECTROTEHNICA-09.2024-2.xlsx\`. Control manual+automat de citire în această sesiune: 6/6 QABC exact și 12/12 ID-uri cu barem identic, fără drift.

## Fișe A/B/C și extinderea contextului

### ELE-057 | AU-84185dba0d7b87f1 | A intact | BLOCAT

**Original:** Două funcţii periodice sinusoidale sunt armonice între ele dacă:

- **A:** raportul perioadelor lor este un număr întreg oarecare
- **B:** au aceeaşi perioadă
- **C:** raportul perioadelor lor este egal cu 1/2

**Context:** „Armonice între ele” poate descrie o fundamentală și armonica ei, sau două componente cu multipli întregi ai *unei fundamentale comune*. Dacă T1=2 s, T2=1 s, T1/T2=2: A. Inversând numai denumirea celor două funcții, T1/T2=1/2: C; natura fizică a perechii este neschimbată. Dacă T1=T2: B și A pot fi simultan adevărate (n=1). Exemplu mai subtil: f1=100 Hz, f2=150 Hz, ambele multipli ai f0=50 Hz, dar raportul f2/f1=3/2 nu este întreg.

**A:** regula intenționată generală într-o ordine a perioadelor, dar nu necesară în toate ordonările; **B:** posibilă relație fundamentală/primă armonică dacă aceeași frecvență e permisă; **C:** caz armonic cu raport invers, specific, deci nu un fals general. Nu se poate declara A unică prin simpla eliminare a celorlalte variante.

**Surse și context verificat:** Carnegie Mellon University, „15.1 Psychoacoustics”, secțiunea „Harmonics (timbre)” definește raportul integral în ordinea frecvențelor joasă/înaltă: https://www.cs.cmu.edu/~15322/book/ch15/01.html ; OpenStax Physics §14.4 precizează că fundamentala este prima armonică: https://openstax.org/books/physics/pages/14-4-sound-interference-and-resonance . Ambele sunt ilustrații conceptuale, NU rezolvă convenția de formulare ANRE. Materialele comerciale care repetă grila nu sunt dovadă de unicitate.

**Poartă:** definiția originală românească/ordinea raportului; dacă nu se găsește, întreabă utilizatorul numai cu A/B/C și această explicație, înregistrează opinia separat.

### ELE-128 | AU-14fb0886051fa595 | A intact | BLOCAT

**Original:** Într-un circuit electric monofazat cu caracter inductiv tensiunea este defazata fata de curent:

- **A:** înainte cu 90 de grade
- **B:** cu zero grade (sunt în faza)
- **C:** cu 90 de grade în urma

**Context:** RLC serie cu X=X_L-X_C pozitiv este „cu caracter inductiv”, dar φ=arctg(X/R). Pentru R=X=10 Ω rezultă 45°, deci A nu este universal adevărată. Pentru R=0, X>0: 90° (L ideal). Pentru X=0: 0° (caracter rezistiv, nu inductiv). Pentru X<0: semnul defazajului este capacitiv.

**A:** adevărată doar într-un caz limită inductiv pur; **B:** falsă pentru X>0; **C:** direcție capacitivă, falsă pentru X>0. Un contraexemplu valid cu 45° lasă zero variante exacte; nu transforma cea mai apropiată variantă în „corectă” fără convenție a sursei.

**Surse cu context imediat:** Marian Pearsică, *Electrotehnică* (Academia Forțelor Aeriene, 2004), §9.8.1, formulele (9.96)-(9.101), descrie distinct „caracter inductiv” pentru X_L>X_C și „caracter pur rezistiv” pentru X_L=X_C: https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf ; OpenStax University Physics vol.2 §15.3, ecuația fazei: https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac .

**Poartă:** definiția convenției de „cu caracter inductiv” vs „pur inductiv” în manualul exact de examen; deocamdată BLOCKED_NO_EXACT_OPTION.

### ELE-222 | AU-ca89b1b43e098b0f | C intact | BLOCAT

**Original:** Susceptanţa unui circuit de curent alternativ sinusoidal este inversul:

- **A:** impedanţei
- **B:** rezistenţei
- **C:** reactanţei

**Context:** Inversul impedanței complexe este admitanța \`Y=1/Z\`, iar susceptanța este partea imaginară (cu semnul convenției) a admitanței. Pentru Z=3+j4 Ω, \`Y=(3-j4)/25\` S, astfel \`B=-0,16 S\`, nu \`1/X=+0,25 S\`. Pentru circuit pur reactiv R=0, \`|B|=1/|X|\`, cu semn dependent de L/C. Într-un circuit pur rezistiv B=0.

**A:** inversul total este admitanță, nu susceptanță; **B:** inversul unei rezistențe pure este conductanță; **C:** intenția didactică probabilă pentru componentă *pur reactivă*, nu identitate generală a oricărui circuit sinusoidal. Eliminarea A/B nu justifică automat C ca teoremă universală.

**Surse:** Pearsică §9.3, relațiile (9.27)-(9.35) cu context admittanță / conductanță / susceptanță: https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf ; All About Circuits „Susceptance and Admittance”, explicit separă cazul pur reactiv de amestec R+X: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/susceptance-and-admittance/ .

**Poartă de calitate a SURSEI:** PDF-ul românesc conține erori editoriale în aceeași secțiune (denumește G „rezistența”, B „reactanța”, iar unitatea susceptanței „Siemensul [Ω]”). Se citează ecuațiile confruntate matematic și cu a doua sursă, NU se copiază fără control unitățile/etichetele tipărite. În plus, se distinge modulul admitanței (scalar) de admitanța complexă.

### ELE-231 | AU-62bf06e215a53d51 | B intact | SUSȚINERE CONTEXTUALĂ, NU APROBAT

**Original:** Singurele mărimi fizice reale în curent alternativ sunt:

- **A:** mărimile efective de curent sau de tensiune
- **B:** mărimile instantanee de curent sau de tensiune
- **C:** valorile medii de curent sau de tensiune

**Context:** Dacă autorul contrastează semnalul fizic în domeniul timp \`i(t),u(t)\` cu fazorii complecși (reprezentare de calcul), B este interpretarea intenționată. Totuși, RMS este o valoare fizic măsurabilă, definită prin efect termic; media este o mărime reală derivată, chiar dacă 0 pentru un sinus ideal pe perioadă. Adjectivul exclusiv „singurele” devine prea tare dacă „reale” are sensul obișnuit și nu „valoare instantanee directă”.

**A:** efectivele sunt agregări, nu semnale instantanee, dar au semnificație fizică; **B:** descrie cel mai bine semnalul real temporal vs reprezentarea complexă; **C:** media este derivată și poate fi 0 pe o perioadă, dar nu e imaginară. Prin eliminare simplă nu se dovedește falsitatea absolută A/C.

**Surse:** S. Ellingson, *Electromagnetics I*, LibreTexts §1.5, „Phasors”: https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_I_%28Ellingson%29/01%3A_Preliminary_Concepts/1.05%3A_Phasors (pagina a dat cache miss la deschidere în această sesiune; pasajul indexat distinge signal real de fazor complex); Pearsică §9.4.1–9.4.2: https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf ; resursă curriculară română de CA sinusoidal pentru efect termic RMS: https://www.isjgorj.ro/resurse/wp-content/uploads/2024/06/CURENTUL-ALTERNATIV-SINUSOIDAL_Prof.-Andritoiu-Liliana.pdf .

**Poartă:** dovada convenției semantice a autorului/testului; B susținut interpretativ, dar exclusivitatea rămâne avertizată.

### ELE-245 | AU-bd60af52c290f7af | A intact | SUSȚINERE CONTEXTUALĂ

**Original:** Un circuit de curent alternativ, pentru care factorul de putere este egal cu 1, este un circuit:

- **A:** pur rezistiv
- **B:** pur inductiv
- **C:** pur capacitiv

**Context:** Factorul de putere \`cosφ=R/|Z|\`; la \`X_L=X_C\` în RLC serie, \`cosφ=1\` chiar dacă fizic există L și C. Manualul românesc, în capitolul despre rezonanță, descrie comportamentul de la borne al circuitului rezonant ca al unei rezistențe pure. A este deci răspunsul intenționat când „pur rezistiv” denumește *echivalentul electric văzut de sursă la frecvența dată*, nu o listă de componente.

**A:** corect în semantica de comportament echivalent rezistiv; **B:** inductiv pur defazaj +90°, factor de putere 0; **C:** capacitiv pur defazaj -90°, factor 0. Nu deduce greșit din factor de putere 1 că L și C nu există fizic.

**Surse:** Pearsică §9.8 și secțiunea de rezonanță: https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf ; OpenStax College Physics 2e §23.12: https://openstax.org/books/college-physics-2e/pages/23-12-rlc-series-ac-circuits .

**Poartă:** se păstrează distincția „echivalent la borne” / „componentă fizică”; adevăr tehnic condițional susținut, dar fără signoff ANRE 2026.

### ELE-257 | AU-23d536ba936f2f33 | B intact | SUPORT DIDACTIC ROMÂNESC PUTERNIC, NU APROBAT

**Original:** Unitatea de măsură a fluxului electric este:

- **A:** V/m
- **B:** Coulombul
- **C:** Faradul

**Context:** În electrotehnica macroscopică românească „flux electric” \`ψ=∫D·dS\`, cu \`D\` exprimat în C/m², deci fluxul în C. Prin contrast, în alte convenții „flux electric” al lui \`E\`, \`ΦE=∫E·dS\`, are dimensiunea V·m. În opțiuni, V/m este câmp E, nu flux E; F este capacitate. Așadar B are demonstrație directă sub convenția de electrotehnică românească.

**A:** unitate intensitate câmp E; **B:** corect pentru fluxul electric Ψ al inducției D; **C:** unitate capacitate electrică. Aici eliminarea este dublată de dovadă afirmativă directă a lui B.

**Două surse independente ca publicații, nu ca experți QA:** Pearsică, *Electrotehnică*, §2.3 (2.14)-(2.20), inclusiv propoziția despre unitatea fluxului: https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf ; *Electrician de întreținere și reparații în industria mică*, 2010, cap.I, (1.9)-(1.19) și unitate [C]: https://www.splt.ro/upload_content/files/manual-electrician-2010-1.pdf ; unități D și E în OG20/1992 / instituție metrologică: https://legislatie.just.ro/Public/FormaPrintabila/00000G0TQQI9H1SWV2J3QJJTIHG82DNA .

**Poartă:** bibliografie ANRE / ediție 2026 + QA distinct; fără schimbarea statutului final al grilei.

## Lecții transferabile descoperite și priorități de regresie

1. **Obiectul vs comportamentul echivalent:** verifică dacă „pur rezistiv”, „ideal”, „fără surse” descrie modelul la borne sau lista internă de componente; exemplu ELE245.
2. **Condiții la limită vs regim generic:** unghi 90° exact și \`B=1/X\` pot fi afirmații corecte numai în model pur/ideal; construiește obligatoriu o instanță mixtă R+X înainte de validare; ELE128,222.
3. **Ordinea și referința relației:** raportul T1/T2 poate deveni inversul său prin simpla schimbare a numelor; verifică n=1, raportul reciproc și armonicele cu fundamentală comună; ELE057.
4. **Mărime reală vs model matematic complex:** reprezentarea fazorială nu invalidează valoarea fizică RMS; cuvinte precum „singurele”/„numai” sunt probe lingvistice separate; ELE231.
5. **Termeni echivoci între discipline:** „flux electric” poate fi \`D\` sau \`E\`; prioritizează definiția din manualul *domeniului examenului* și control dimensional; ELE257.
6. **Eroare tipografică în sursa însăși:** rulați control de consistență matematică/dimensională pe un manual chiar reputabil, coroborați formula cu o sursă distinctă; ELE222.
7. **O grilă cu două alternative literalmente adevărate sau zero exacte este blocată**, chiar dacă baremul original și intenția pedagogică sunt clare; nu rescrie examenul, adnotează capcana.
8. **Straturi diferite de QA:** reproductibilitatea numerică și sursa didactică sunt dovadă pentru o ipoteză, NU evaluare independentă sau semnătură pentru învățare.

## Teste, regresie și control de risc

- \`ckpt051_math_checks.py\` rulează 17 instanțe sintetice/numerice și de unități pentru aceste șase cazuri. Rezultat executat local în sesiune înainte de publicare: **17/17 PASS**. Nu se confundă cu benchmark pe agenți sau reviewer extern.
- Control prealabil prin redeschiderea masterului V73 și CKPT050: **6/6 QABC exacte, cele 12 ID-uri de grad cu aceleași baremuri**, fără modificare în master.
- Nu s-au rerulat testele pe APK/HTML (ele rămân nemodificate).
- Nu a fost executat un reviewer tehnic/lingvistic/sursă diferit de acest asistent; marcajul rămâne \`NOT_RUN\`. PDF screenshot în browser a eșuat \`CACHE_MISS\` pe 3 copii; citire textuală accesibilă.
- Rezultat: trei blocaje de unicitate/generalizare neînchise (057,128,222), trei interpretări susținute contextual dar fără semnătură finală (231,245,257). **0/822 aprobat pentru învățare.**
- Nu promovați CKPT051 la unități noi de context; doar rafinează cele 6 fișe din CKPT050. În PR #7 Draft, păstrați ambele checkpoint-uri și motivul actualizării.

**Următorul pas:** căutați definiția exactă ANRE/ediția aplicabilă pentru 057/128/222, distingeți intenție de unicitate, apoi escaladați numai dacă raționamentul utilizatorului poate decide o convenție lingvistică. În acest caz, arătați enunțul integral + A/B/C + citarea sursei împreună cu contextul adiacent; înregistrați opinia ca ipoteză, nu drept QA independent.
