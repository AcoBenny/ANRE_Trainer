# CKPT-240 | 15 întrebări de electrotehnică + 15 corespondențe exacte G2 | 2026-11-19

Baseline V118 Git blob `1b13fb7384886e3a063de16327a9f41fa59cf1e0`, sursa canonică V73 Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`. 15 QABC originale analizate cu ipoteze și contraexemple, 15 potriviri grade II pe **enunț + A/B/C + barem**. Corespondențele grade II sunt doar reutilizare, nu QA tehnic independent.

**Acces surse:** 9 HTML deschise integral; 6 surse numai prin rezultate indexate. Fără confirmare de barem oficial 2026 sau review de specialiști independenți.

### G1-ELE-211 / G2-ELEC-347
- **Întrebare:** Rezistenta echivalenta a trei rezistoare, având fiecare rezistenta de 3 ohm, montate în paralel, este:
- A: 3 ohm
- B: 1 ohm
- C: 9 ohm
- **Barem importat (nemodificat): B.** 1/Req=1/3+1/3+1/3=1 S, deci Req=1Ω: B. A 3Ω este o singură rezistență, C 9Ω rezultatul seriei.
- **Sursă:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-212 / G2-ELEC-348
- **Întrebare:** Rezistivitatea unui conductor electric depinde de:
- A: natura materialului
- B: lungime, direct proporţional
- C: masa, direct proporţional
- **Barem importat (nemodificat): A.** A materialul determină rezistivitatea ρ, împreună cu temperatura și starea sa. Lungimea B și masa C nu determină direct ρ; lungimea afectează R=ρL/A, nu ρ în material uniform.
- **Sursă:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance; acces: SEARCH_INDEX_ONLY. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-213 / G2-ELEC-349
- **Întrebare:** Rezonanţa se obţine într-un circuit electric de curent alternativ dacă:
- A: reactanţele inductivă şi capacitivă în valoare absolută sunt egale
- B: reactanţa inductivă este mai mare decât reactanţa capacitivă
- C: reactanţa capacitivă este mai mare decât reactanţa inductivă
- **Barem importat (nemodificat): A.** La rezonanța RLC ideală în regim sinusoidal XL=XC, A. B circuit inductiv net, C capacitiv net. Condiția se raportează la modelul serie/rezonator corespunzător, nu la orice topologie arbitrară.
- **Sursă:** https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-215 / G2-ELEC-351
- **Întrebare:** Rolul dominant pentru reglarea nivelului de tensiune pe o linie electrica îl are:
- A: circulaţia de putere activa
- B: circulaţia de putere reactiva
- C: nici una din cele doua
- **Barem importat (nemodificat): B.** În sistemele cu reactanță dominantă, circulația și compensarea puterii reactive influențează decisiv tensiunea, B. A puterea activă influențează și ea căderile de tensiune în rețele rezistive; C ignoră relația Q-U. Nu este o regulă universală pentru rețele R/X mici.
- **Sursă:** https://technav.ieee.org/topic/voltage-control/; acces: SEARCH_INDEX_ONLY. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-218 / G2-ELEC-354
- **Întrebare:** Schema echivalentă de calcul în cazul producerii unui scurtcircuit trifazat, al unei reţele, izolat de pământ se compune din:
- A: schemele de secvenţă directă (pozitivă) , inversă (negativă) şi homopolară (zero) conectate în serie
- B: schema de secvenţă directă (pozitivă)
- C: schemele de secvenţă directă (pozitivă) şi inversă (negativă) conectate în paralel
- **Barem importat (nemodificat): B.** Defectul trifazat simetric în calculul componentelor simetrice folosește doar rețeaua directă pozitivă, B. A ar introduce incorect toate rețelele; C adaugă inutil secvența negativă. Model simetric și condiții de defect explicit cerute.
- **Sursă:** https://www.phasetophase.nl/book/book_2_10.html; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-223 / G2-ELEC-359
- **Întrebare:** Transformatoarele de măsurare de curent:
- A: pot fi racordate în circuitul primar cu înfăşurarea secundara deschisa
- B: pot fi lăsate în exploatare cu înfăşurarea secundara deschisa
- C: nu pot fi racordate in circuitul primar cu înfăşurarea secundara deschisa
- **Barem importat (nemodificat): C.** C: nu se exploatează CT cu primarul energizat și secundarul deschis, deoarece pot apărea supratensiuni foarte periculoase. A și B permit tocmai condiția interzisă. Regula privește CT convențional cu curent primar, nu senzorii speciali de mică putere.
- **Sursă:** https://www.se.com/us/en/faqs/FA125574/; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-227 / G2-ELEC-363
- **Întrebare:** Separatorul, ca echipament în cadrul unei staţii electrice, are rolul:
- A: de a proteja circuitul la supracurenţi
- B: de a separa vizibil un circuit
- C: de a măsură nivelul de izolaţie
- **Barem importat (nemodificat): B.** Separatorul are rol de izolare/separare vizibilă sau distanță de izolare verificabilă, B. A protecția la supracurenți aparține protecțiilor, C măsurarea izolației altor aparate. Nu confundați separatorul simplu cu separatorul de sarcină care poate întrerupe curent nominal.
- **Sursă:** https://www.abb.com/global/en/areas/electrification/medium-voltage/grid-components/switch-disconnectors; acces: SEARCH_INDEX_ONLY. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-230 / G2-ELEC-366
- **Întrebare:** Siguranţele fuzibile sunt aparate utilizate pentru protecţie la:
- A: supratensiuni
- B: supracurenţi
- C: defect de izolaţie
- **Barem importat (nemodificat): B.** Siguranțele fuzibile sunt dispozitive de protecție la supracurenți, B, incluzând de regulă scurtcircuite și, în limitele caracteristicii, suprasarcini. A supratensiuni nu este funcția lor; C defect de izolație nu constituie o categorie de declanșare în sine decât când provoacă supracurent.
- **Sursă:** https://www.eaton.com/us/en-us/products/electronic-components/topics/fuse-technology.html; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-235 / G2-ELEC-371
- **Întrebare:** Suma tensiunilor electromotoare ale unui sistem trifazat simetric este:
- A: egală cu 1
- B: nulă
- C: egală cu 1/2
- **Barem importat (nemodificat): B.** Pentru trei t.e.m. egale și fazate la 120°, suma vectorială (și instantanee pentru sinusoidale echilibrate) este zero, B. A=1 și C=1/2 sunt scalari arbitrar fără unități. Condiție: amplitudini egale și decalaj exact 120°.
- **Sursă:** https://www.phasetophase.nl/book/book_2_7.html; acces: SEARCH_INDEX_ONLY. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-237 / G2-ELEC-373
- **Întrebare:** Un conductor în care circulaţia curentului electric nu se supune legii lui Ohm se numeşte:
- A: liniar
- B: neomogen
- C: neliniar
- **Barem importat (nemodificat): C.** Un element cu caracteristică U-I neproporțională este neliniar C. A liniar contrazice enunțul, B neomogen se referă la variația structurii/proprietăților, nu indică automat încălcarea relației Ohm. Domeniul tensiunilor și temperatura contează.
- **Sursă:** https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law; acces: SEARCH_INDEX_ONLY. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-238 / G2-ELEC-374
- **Întrebare:** Teoremele (formulele) Biot Savart Laplace se referă la:
- A: intensitatea câmpului magnetic produs de un curent care circulă printr-un conductor
- B: forţa electromagnetică
- C: forţa exercitată între două conductoare paralele parcurse de curenţi
- **Barem importat (nemodificat): A.** Biot-Savart-Laplace descrie contribuția elementelor de curent la inducția/câmpul magnetic, A. B este forță electromagnetică, C forță între conductoare, nu obiectul direct al formulei Biot-Savart.
- **Sursă:** https://openstax.org/books/university-physics-volume-2/pages/12-1-the-biot-savart-law; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-239 / G2-ELEC-375
- **Întrebare:** Tesla este unitatea de măsură a:
- A: inducţiei magnetice
- B: fluxului magnetic
- C: intensităţii câmpului magnetic
- **Barem importat (nemodificat): A.** Tesla (T) măsoară inducția magnetică B, A. B fluxul magnetic se măsoară în weber, C intensitatea H în A/m. Relația 1 T=1 Wb/m².
- **Sursă:** https://goldbook.iupac.org/terms/view/T06283; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-242 / G2-ELEC-378
- **Întrebare:** Un motor electric trifazat legat în stea este în funcţiune si alimentat la 0,4 kV. Tensiunea între neutrul stelei si una dintre faze este:
- A: 0,4 kV
- B: 0 V
- C: 230 V
- **Barem importat (nemodificat): C.** La stea echilibrată, dacă 0,4kV este tensiunea între faze, Uf=400/√3≈230,9V, deci C 230V. A=400V este tensiune de linie, B=0V greșit. Se presupune un sistem trifazat nominal echilibrat și neutru de referință.
- **Sursă:** https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-243 / G2-ELEC-379
- **Întrebare:** Un separator pe un circuit de înalta tensiune poate fi manevrat:
- A: sub tensiune si cu curent
- B: cu curent fara tensiune
- C: fãrã curent, fãrã tensiune sau sub tensiune, fãrã curent
- **Barem importat (nemodificat): C.** Pentru separator simplu C: manevra se face fără curent de sarcină, posibil sub tensiune dacă lipsește curentul. A sub tensiune și cu curent de sarcină nu este capacitatea tipică, B cu curent și fără tensiune este inconsecvent pentru sarcina normală. Manevrele reale se fac numai conform procedurilor și clasificării aparatului.
- **Sursă:** https://www.abb.com/global/en/areas/electrification/medium-voltage/grid-components/switch-disconnectors; acces: SEARCH_INDEX_ONLY. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

### G1-ELE-244 / G2-ELEC-380
- **Întrebare:** Transformatoarele de măsurare de tensiune:
- A: nu pot fi lăsate în exploatare cu înfăşurarea secundara deschisa
- B: nu pot fi lăsate în exploatare cu înfăşurarea secundara în scurtcircuit
- C: pot fi puse sub tensiune cu înfăşurarea secundara in scurtcircuit
- **Barem importat (nemodificat): B.** Secundarul transformatorului de tensiune nu trebuie scurtcircuitat: B. A spune că nu poate rămâne deschis, dar mersul în gol poate fi admis; C permite scurtcircuit periculos. Nu confundați VT/PT cu CT, la care pericolul caracteristic apare la secundar deschis.
- **Sursă:** https://control.com/textbook/electric-power-measurement-and-control/electrical-sensors/; acces: HTML_OPENED. Verdict PRELIMINAR, fără QA independent sau confirmare bibliografie ANRE2026.

## Gates and integrity
- 30 rânduri cu metadate de evidență noi; alte 792 rânduri identice cu V118, fără schimbare de text/cheie/risc/release.
- 822 ID-uri canonice în același ordin, 246 -> 216 fără verificare focalizată P2.
- Surse exacte și ediție ANRE2026 pentru cazuri individuale NOT_AUTHENTICATED; QA independent NOT_RUN; semnătură umană NOT_RUN; approved_for_learning=NO pentru toate.
- 50 rânduri neuniforme de serializare CSV moștenite din V117/V118 rămân byte-identice și sunt datorie structurală separată. Nu se normalizează automat fără reconciliere completă.
- Cazuri cu modele condiționate: ELE-213 rezonanța RLC ideală; ELE-215 relație Q/U dependentă de R/X; ELE-218 defect trifazat simetric; ELE-242 stea echilibrată; ELE-243 separator simplu, nu separator de sarcină.
- PR #7 Draft, fără merge, fără modificare QABC/HTML/APK, fără aprobare pentru utilizare la învățare.
