# CKPT-239 | 15 QABC originale și 15 legături identice între grade | 2026-11-19

**Baseline:** V117 blob 03cfd4fb49cbc0b969457c3685b8dba190f26873; **sursa originală QABC:** V73 blob c027d417a8e4e605c830b2016fb55b099b8d130b.

- 15 întrebări originale G1; 15 potriviri G2 exacte între enunț + A/B/C + barem; dovezile se reutilizează, fără a pretinde analiză de sursă separată pentru gradul II.
- 12 surse deschise ca pagini HTML și 3 accesibile doar prin rezultatul indexat după eșec la deschiderea paginii integrale. Acest ultim nivel NU este certificare directă a textului sursă.
- **Concluzii preliminare**, separate de baremurile autentificate, verificarea ediției 2026 și de QA tehnic/lingvistic/sursă independent; toate aceste porți rămân NOT_RUN/NOT_VERIFIED.

## G1-ELE-184 / G2-ELEC-320
- **Enunț exact:** Permeabilitatea este o mărime:
- **A:** magnetică
- **B:** electrică
- **C:** mecanică
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** A este magnetică: μ leagă B de H; B electrică confundă cu ε; C mecanică nu este această proprietate.
- **Sursa candidat / locator:** https://openstax.org/books/university-physics-volume-2/pages/12-7-magnetism-in-matter (permeability)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-185 / G2-ELEC-321
- **Enunț exact:** Permitivitatea este o mărime:
- **A:** electrică
- **B:** magnetică
- **C:** chimică
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** A electrică: ε apare la E=σ/ε și C=εA/d. B magnetică confundă cu μ; C chimică greșit.
- **Sursa candidat / locator:** https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance (E=σ/ε0)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-186 / G2-ELEC-322
- **Enunț exact:** Regulatorul automat de tensiune (RAT) asigurã:
- **A:** deconectarea automatã a liniilor la suprasarcinã
- **B:** conectarea automatã a unui transformator de rezervã
- **C:** modificarea curentului (tensiunii) de excitaţie la generatoarele sincrone
- **Barem existent, nemodificat:** C
- **Raționament contextual A/B/C și contraexemple:** C: regulatorul automat de tensiune variază excitația. A: suprasarcina liniei ține de protecții; B: transferul de rezervă nu este RAT.
- **Sursa candidat / locator:** https://automationsolutionfinder.andritz.com/solutions/15006/power-systems/hydro-power-oil-gas-thermal-power/excitation-systems (generator AVR field current)
- **Acces:** INDEX_ONLY. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-187 / G2-ELEC-323
- **Enunț exact:** Pierderile de putere activã si reactivã pe o linie electricã, la aceeaşi putere aparentã vehiculatã, sunt invers proporţionale cu:
- **A:** pătratul curentului
- **B:** pătratul tensiunii
- **C:** pătratul puterii active
- **Barem existent, nemodificat:** B
- **Raționament contextual A/B/C și contraexemple:** Pentru S și impedanțele R/X fixate, I=S/(sqrt3 U), pierderile 3I²R și aproximativ 3I²X au dependență inversă de U²: B. A și C nu dau relația corectă. Atenție la modificările concomitente de topologie și parametri.
- **Sursa candidat / locator:** https://eepower.com/technical-articles/transmission-line-losses-and-efficiency-optimizationpart-1/ (line current and I2R loss)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-188 / G2-ELEC-324
- **Enunț exact:** Pierderile de putere într-o linie electrică prin care se transportă o putere activă P la un factor de putere = 0,9, faţă de cazul când se transportă aceeaşi putere la un factor de putere = 0,8 sunt:
- **A:** mai mici
- **B:** egale
- **C:** mai mari
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** La P,U,R fixe, I=P/(sqrt3 U cosφ). Raport pierderi (cosφ=0.9 față de 0.8)=(0.8/0.9)²≈0.7901; A mai mici. B și C neconcordante; condiția parametrilor constanți este necesară.
- **Sursa candidat / locator:** https://eepower.com/technical-articles/transmission-line-losses-and-efficiency-optimizationpart-1/ (power factor and resistive losses)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-190 / G2-ELEC-326
- **Enunț exact:** Prima teoremă a lui Kirchhoff, pentru o reţea electrică buclată cu N noduri, ne dă, pentru curenţii care circulă prin reţea:
- **A:** N-1 relaţii distincte
- **B:** N relaţii distincte
- **C:** N+1 relaţii distincte
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** Pentru o rețea conectată cu N noduri există N−1 ecuații KCL independente A. B include una redundantă și C excede. Dacă sunt k componente neconectate, rang N−k, deci formularea presupune conectivitate.
- **Sursa candidat / locator:** https://zrojec.fe.uni-lj.si/cao/circuit-topology-constitutive-relations-and-nodal-analysis/ (n-1 independent KCL)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-192 / G2-ELEC-328
- **Enunț exact:** Principalele elemente feromagnetice sunt:
- **A:** Fierul, nichelul şi cobaltul
- **B:** Fierul, cuprul, zincul
- **C:** Fierul, aluminiul, cuprul
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** A Fe/Ni/Co sunt trei feromagnetice clasice. B Cu/Zn și C Al/Cu includ metale neferomagnetice în condiții uzuale. Nu înseamnă că doar aceste trei elemente pot fi feromagnetice.
- **Sursa candidat / locator:** https://openstax.org/books/university-physics-volume-2/pages/12-7-magnetism-in-matter (iron nickel cobalt)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-196 / G2-ELEC-332
- **Enunț exact:** Rezistenţa echivalentă a două rezistenţe cu valori diferite montate în paralel este:
- **A:** mai mare decât rezistenţa mai mare
- **B:** mai mică decât rezistenţa mai mică
- **C:** egală cu suma rezistenţelor
- **Barem existent, nemodificat:** B
- **Raționament contextual A/B/C și contraexemple:** Pentru R1,R2 pozitive, 1/Req=1/R1+1/R2, deci Req<min(R1,R2): B. A fals; C este suma corespunzătoare seriei.
- **Sursa candidat / locator:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel (parallel equivalent resistance)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-200 / G2-ELEC-336
- **Enunț exact:** Releul termic se foloseşte pentru:
- **A:** protejarea motoarelor electrice la scurtcircuit
- **B:** protejarea generatoarelor si motoarelor electrice împotriva punerii la pământ
- **C:** protejarea motoarelor electrice împotriva suprasarcinilor
- **Barem existent, nemodificat:** C
- **Raționament contextual A/B/C și contraexemple:** C: releul termic protejează motorul la suprasarcină. A scurtcircuit necesită declanșare rapidă dedicată; B defect la pământ are altă protecție.
- **Sursa candidat / locator:** https://eshop.se.com/in/shop-by-category/low-voltage-products/overload-relay.html (overload relay motors)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-201 / G2-ELEC-337
- **Enunț exact:** Rezistenta echivalenta a trei rezistoare, având fiecare rezistenta de 2 ohm, montate în serie este:
- **A:** 5 ohm
- **B:** 0,66 ohm
- **C:** 6 ohm
- **Barem existent, nemodificat:** C
- **Raționament contextual A/B/C și contraexemple:** Trei rezistoare de 2 Ω în serie: 2+2+2=6 Ω, C. A 5 Ω greșit; B 0,66 Ω corespunde aproximativ conexiunii în paralel.
- **Sursa candidat / locator:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel (series sum)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-202 / G2-ELEC-338
- **Enunț exact:** Raportul nominal de transformare al unui transformator de putere este:
- **A:** raportul dintre tensiunea primara si secundara de mers în gol
- **B:** raportul dintre curentul primar si secundar la sarcina nominala
- **C:** raportul dintre tensiunea primara si secundara la sarcina nominala
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** A raportul tensiunilor la mers în gol corespunde modelului ideal al raportului de spire. B este raport de curenți, diferit; C sub sarcină include căderi de tensiune. Definiția exactă a lui «nominal» trebuie confirmată în bibliografia ANRE.
- **Sursa candidat / locator:** https://www.megger.com/en-us/et-online/september-2016/turns-ratio-testing-hand-crank-versus-automatic (ideal transformer no-load ratio)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-205 / G2-ELEC-341
- **Enunț exact:** Reglarea puterii active debitate de generatorul sincron se face variind:
- **A:** tensiunea de excitaţie
- **B:** admisia agentului primar la turbina
- **C:** curentul statoric
- **Barem existent, nemodificat:** B
- **Raționament contextual A/B/C și contraexemple:** B: admisia fluidului la turbină schimbă puterea mecanică și activă livrată în funcționare sincronizată. A excitația țintește predominant Q și tensiune; C curentul statoric rezultă din punctul de funcționare.
- **Sursa candidat / locator:** https://handbook.ashrae.org/Handbooks/S24/SI/S24_Ch07/S24_Ch07_si.aspx (steam admission valves / governor)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-206 / G2-ELEC-342
- **Enunț exact:** Reglarea puterii reactive debitate de generatorul sincron se face prin:
- **A:** modificarea curentului de excitaţie
- **B:** deschiderea aparatului director al turbinei
- **C:** deconectarea rezistentei de stingere
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** A: excitația generatorului sincron reglează predominant Q și U. B admisia turbinei acționează mai ales asupra puterii active; C deconectarea rezistenței de stingere nu este regulator Q.
- **Sursa candidat / locator:** https://automationsolutionfinder.andritz.com/solutions/15006/power-systems/hydro-power-oil-gas-thermal-power/excitation-systems (field current and reactive power)
- **Acces:** INDEX_ONLY. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-208 / G2-ELEC-344
- **Enunț exact:** Relaţia între curenţii de linie si de fazã în sisteme cu generatoare si receptoare conectate în triunghi este:
- **A:** curentul de linie este mai mare de 1,73 ori decât curentul de fazã
- **B:** curentul de linie este egal cu curentul de fazã
- **C:** curentul de fazã este mai mare de de 1,73 ori decât curentul de linie
- **Barem existent, nemodificat:** A
- **Raționament contextual A/B/C și contraexemple:** A pentru triunghi echilibrat: I_linie=√3·I_fază≈1,73 ori. B relația stea; C inversează raportul. Condiția de echilibru este esențială.
- **Sursa candidat / locator:** https://www.professorglasmachers.de/en/ema_drehstrom-in-stern-und-dreiecksschaltung/ (delta phase-line currents)
- **Acces:** INDEX_ONLY. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## G1-ELE-209 / G2-ELEC-345
- **Enunț exact:** Se considera ca un transformator funcţionează în gol atunci când:
- **A:** sarcina transformatorului este foarte mica
- **B:** curentul primar si curentul secundar sunt foarte mici
- **C:** o înfăşurare este conectata la reţea, iar cealaltă este deschisa
- **Barem existent, nemodificat:** C
- **Raționament contextual A/B/C și contraexemple:** C: o înfășurare alimentată iar cealaltă deschisă definește mersul în gol. A sarcină mică nu înseamnă gol; B ambii curenți mici nu definesc conexiunea. Primarul absoarbe curent de magnetizare.
- **Sursa candidat / locator:** https://eepower.com/technical-articles/open-circuit-and-short-circuit-tests-in-transformers/ (primary energized secondary open)
- **Acces:** HTML_OPENED. Candidat de răspuns, nu aprobare ANRE2026, fără verificator independent.

## Control de integritate și stare
- Exact 30 rânduri grade actualizate documentar, 792 rânduri păstrate identic byte-for-byte; 822 ID-uri păstrate. P2 fără verificare focalizată 276 -> 246.
- Cheile, riscurile originale și aprobarea pentru învățare rămân nemodificate. PR #7 Draft, fără merge și fără modificare HTML/APK.
- **Datorie tehnică CSV preexistentă:** V117 conține 50 linii cu un alt număr de câmpuri decât antetul la split simplu după virgulă (pot exista virgule neprotejate în valori). Le-am păstrat exact în loc să le normalizăm automat, pentru a evita alterarea dovezilor; QA structural al rândurilor atinse este PASS, dar parsarea completă trebuie revalidată cu un parser CSV strict și remediată separat prin reconciliere fără pierderi.
- Excepții și condiții: ELE-187/188 depind de S/P, tensiune și impedanțe fixate; ELE-190 de conectivitate; ELE-202 necesită ediția exactă a definiției «raport nominal»; ELE-208 presupune triunghi echilibrat.
