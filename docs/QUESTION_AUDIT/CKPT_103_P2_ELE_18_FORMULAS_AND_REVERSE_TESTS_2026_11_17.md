# CKPT-103 | P2 18 formule/relații electrotehnice, Grade I + II | 17.11.2026

## Reconciliere și grad de dovadă
- Bază CKPT-102: 304/568 unități și 366/822 ID-uri contextual documentate. În acest lot 18 P2 noi, toate perechi de grade (+36 ID-uri), astfel cumul **322/568 unități și 402/822 ID-uri**, **246 unități P2 rămân**. 0/822 aprobate.
- Original QABC + sha256/key din MASTER, preflight exact `unit_id`, `member_ids` și risc versus FINAL_APPROVAL_WORKLIST. Nu sunt dubluri ale CKPT050–102. S-a reutilizat cercetarea preliminară a fișierelor DEEP_ELE_05/06 pentru a nu reface același raționament. Relațiile verificabile în OpenStax sunt rederivate mai jos; dacă sursa este doar un principiu adiacent (ex. generator p perechi de poli, ½qV conductor izolat), acest lucru rămâne semnalat.
- Textele A/B/C de mai jos sunt din cercetare preliminară, nu un reviewer independent; pentru fiecare există context și test invers. **INDEPENDENT_TECH/SOURCE/LING_QA=NOT_RUN**, official exam item provenance/edition not certified, learner approval NO. Se protejează QABC, cheile, master, HTML/APK, main, merge/release.

## G1-ELE-039 | AU-392983895ec560c1
- qabc_sha256 392983895ec560c1049637c87addc9a0860d2c5adc0c99770cb4c5620725a023; member_ids G1-ELE-039;G2-ELEC-185; imported key {"G1-ELE-039":"B","G2-ELEC-185":"B"} PĂSTRATĂ.
- **Original:** Conform Legii lui Coulomb, forţa de atracţie sau de repulsie care se exercită între sarcinile electrice este:
  - A. direct proporţională cu pătratul distanţei
  - B. invers proporţională cu pătratul distanţei
  - C. direct proporţională cu distanţa
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/5-3-coulombs-law ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: OpenStax 5.3 Coulomb F=k|q1q2|/r².
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **F = k|q1q2|/r²; sarcini constante**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: direct with r² contradicts denominator. Varianta B este verificată astfel: force inversely proportional to r². Varianta C este verificată astfel: direct with r contradicts 1/r². Condiția explicită și testul de falsificare: **dublarea distanței duce la o pătrime din forță; dacă sarcinile diferă, nu aplicăm simpla regulă față de r**.
- **Vertical:** A A: direct with r² contradicts denominator; B B: force inversely proportional to r²; C C: direct with r contradicts 1/r².
- **Orizontal (A↔B, A↔C, B↔C):** A «direct proporţională cu pătratul distanţei» versus B «invers proporţională cu pătratul distanţei»: valori/concepte diferite, comparați cu F = k|q1q2|/r²; sarcini constante. A versus C «direct proporţională cu distanţa» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa invers proporţională cu pătratul distanţei de direct proporţională cu distanţa prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** dublarea distanței duce la o pătrime din forță; dacă sarcinile diferă, nu aplicăm simpla regulă față de r.
- **Stare:** DIRECT_OPENSTAX_COULOMB_5_3; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-040 | AU-687aeeb1afce89dd
- qabc_sha256 687aeeb1afce89ddb241710167191d09c86fb528c9eb6e54a3ac2fceb03705d9; member_ids G1-ELE-040;G2-ELEC-186; imported key {"G1-ELE-040":"A","G2-ELEC-186":"A"} PĂSTRATĂ.
- **Original:** Constanta de timp a unui circuit format dintr-un rezistor de rezistenţă R înseriat cu un condensator de capacitate C, este:
  - A. RC
  - B. R/C
  - C. 1/(RC)
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: OpenStax 10.5 gives tau=RC.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **τ = RC pentru circuit RC de ordinul I**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: RC has units seconds and is exponential time constant. Varianta B este verificată astfel: R/C not units seconds. Varianta C este verificată astfel: 1/(RC) is rate s^-1, not the time constant. Condiția explicită și testul de falsificare: **R=1 kΩ și C=1 μF produc τ=1 ms; R/C are unități incompatibile cu timpul**.
- **Vertical:** A A: RC has units seconds and is exponential time constant; B B: R/C not units seconds; C C: 1/(RC) is rate s^-1, not the time constant.
- **Orizontal (A↔B, A↔C, B↔C):** A «RC» versus B «R/C»: valori/concepte diferite, comparați cu τ = RC pentru circuit RC de ordinul I. A versus C «1/(RC)» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa R/C de 1/(RC) prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** R=1 kΩ și C=1 μF produc τ=1 ms; R/C are unități incompatibile cu timpul.
- **Stare:** DIRECT_OPENSTAX_RC_10_5; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-042 | AU-14c80fd791619835
- qabc_sha256 14c80fd7916198355d370848225107f1432c1050d5c62ce6a29818124ad2ee89; member_ids G1-ELE-042;G2-ELEC-188; imported key {"G1-ELE-042":"B","G2-ELEC-188":"B"} PĂSTRATĂ.
- **Original:** Curentul care circula printr-un circuit de curent alternativ, având rezistenta r=3 Ω, reactanţa x= 4 Ω si la bornele căruia se aplica o tensiune de 220 V este:
  - A. 31,5 A
  - B. 44 A
  - C. 53,4 A
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: OpenStax AC phasor impedance; |Z|=sqrt(3²+4²)=5 ohm, I=220/5=44A.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **|Z|=sqrt(R²+X²)=sqrt(9+16)=5Ω; I=220/5=44A**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: 31.5A would imply Z≈6.98ohm not sqrt(3²+4²). Varianta B este verificată astfel: 220V/5ohm=44A. Varianta C este verificată astfel: 53.4A would imply Z≈4.12ohm not resultant magnitude. Condiția explicită și testul de falsificare: **valoarea 44 A folosește 220 V eficace și modelul serie R-X; altă topologie nu este acoperită**.
- **Vertical:** A A: 31.5A would imply Z≈6.98ohm not sqrt(3²+4²); B B: 220V/5ohm=44A; C C: 53.4A would imply Z≈4.12ohm not resultant magnitude.
- **Orizontal (A↔B, A↔C, B↔C):** A «31,5 A» versus B «44 A»: valori/concepte diferite, comparați cu |Z|=sqrt(R²+X²)=sqrt(9+16)=5Ω; I=220/5=44A. A versus C «53,4 A» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa 44 A de 53,4 A prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** valoarea 44 A folosește 220 V eficace și modelul serie R-X; altă topologie nu este acoperită.
- **Stare:** PHASOR_DIRECT_FORMULA_ASSUMPTIONS; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-050 | AU-807a4eaec50a6d09
- qabc_sha256 807a4eaec50a6d0944c468621141141e597b6fc9e2843018972ac452f39fefbb; member_ids G1-ELE-050;G2-ELEC-196; imported key {"G1-ELE-050":"C","G2-ELEC-196":"C"} PĂSTRATĂ.
- **Original:** Energia transmisă de undele electromagnetice cu intensitatea câmpului electric E şi intensitatea câmpului magnetic H se propagă după un vector:
  - A. S=E+H
  - B. S=HxE
  - C. S=ExH
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/16-3-energy-carried-by-electromagnetic-waves ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: Poynting S=E×H (B=mu H; OpenStax states E×B/mu0).
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Vector Poynting S=E×H, energie pe unitate arie și timp**. În modelul fizic corespunzător, răspunsul importat **C** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: adding vectors E+H has mismatched physical units and direction. Varianta B este verificată astfel: H×E is minus E×H, wrong propagation direction. Varianta C este verificată astfel: E×H correct ordered cross product. Condiția explicită și testul de falsificare: **inversarea ordinii H×E schimbă semnul vectorului, deci sensul propagării; E+H are și unități diferite**.
- **Vertical:** A A: adding vectors E+H has mismatched physical units and direction; B B: H×E is minus E×H, wrong propagation direction; C C: E×H correct ordered cross product.
- **Orizontal (A↔B, A↔C, B↔C):** A «S=E+H» versus B «S=HxE»: valori/concepte diferite, comparați cu Vector Poynting S=E×H, energie pe unitate arie și timp. A versus C «S=ExH» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa S=HxE de S=ExH prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** inversarea ordinii H×E schimbă semnul vectorului, deci sensul propagării; E+H are și unități diferite.
- **Stare:** POYNTING_CROSS_PRODUCT_16_3; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-052 | AU-ecaa28b689c1ea32
- qabc_sha256 ecaa28b689c1ea32fc82bbefe4ed3395ff22b5516a89b812188a2f946c7e3da1; member_ids G1-ELE-052;G2-ELEC-198; imported key {"G1-ELE-052":"A","G2-ELEC-198":"A"} PĂSTRATĂ.
- **Original:** Dacă printr-un condensator circulă un curent alternativ sinusoidal, la bornele sale se produce o cădere de tensiune:
  - A. defazată cu 90 de grade în urma curentului
  - B. defazată cu 90 de grade înaintea curentului
  - C. în fază cu curentul
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: OpenStax 15.2 states capacitor current leads voltage by 90deg.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **La condensator ideal i conduce u cu 90°, echivalent u rămâne în urma lui i cu 90°**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: capacitor voltage lags current by 90°. Varianta B este verificată astfel: voltage leading current corresponds to inductor. Varianta C este verificată astfel: in phase describes pure resistance. Condiția explicită și testul de falsificare: **pentru i=Imax cos(ωt), u proporțional sin(ωt), astfel vârful tensiunii vine un sfert de ciclu mai târziu**.
- **Vertical:** A A: capacitor voltage lags current by 90°; B B: voltage leading current corresponds to inductor; C C: in phase describes pure resistance.
- **Orizontal (A↔B, A↔C, B↔C):** A «defazată cu 90 de grade în urma curentului» versus B «defazată cu 90 de grade înaintea curentului»: valori/concepte diferite, comparați cu La condensator ideal i conduce u cu 90°, echivalent u rămâne în urma lui i cu 90°. A versus C «în fază cu curentul» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa defazată cu 90 de grade înaintea curentului de în fază cu curentul prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** pentru i=Imax cos(ωt), u proporțional sin(ωt), astfel vârful tensiunii vine un sfert de ciclu mai târziu.
- **Stare:** IDEAL_CAPACITOR_PHASE_15_2; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-056 | AU-613ea692a3390f13
- qabc_sha256 613ea692a3390f13c9e0b1ee591f1cd91bcb009799e52c7a6b614bdb21486979; member_ids G1-ELE-056;G2-ELEC-202; imported key {"G1-ELE-056":"A","G2-ELEC-202":"A"} PĂSTRATĂ.
- **Original:** Diferenţa de potenţial la bornele a n baterii de condensatoare montate în serie este egală cu:
  - A. suma diferenţelor de potenţial la bornele fiecărui condensator
  - B. diferenţa de potenţial la bornele fiecărui condensator în parte
  - C. diferenţa de potenţial a unui condensator împărţită la n
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: OpenStax §8.2 gives Vtot = V1 + ... + Vn for series capacitors.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Pentru condensatoare în serie Utotal=ΣUelement, păstrând semnul tensiunilor**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: sum of individual potential differences equals total. Varianta B este verificată astfel: individual voltages differ unless special conditions. Varianta C este verificată astfel: Vindividual/n not general for series. Condiția explicită și testul de falsificare: **la două condensatoare cu 4 V și 6 V distribuite concordant, tensiunea ansamblului este 10 V, nu 4 sau 6**.
- **Vertical:** A A: sum of individual potential differences equals total; B B: individual voltages differ unless special conditions; C C: Vindividual/n not general for series.
- **Orizontal (A↔B, A↔C, B↔C):** A «suma diferenţelor de potenţial la bornele fiecărui condensator» versus B «diferenţa de potenţial la bornele fiecărui condensator în parte»: valori/concepte diferite, comparați cu Pentru condensatoare în serie Utotal=ΣUelement, păstrând semnul tensiunilor. A versus C «diferenţa de potenţial a unui condensator împărţită la n» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa diferenţa de potenţial la bornele fiecărui condensator în parte de diferenţa de potenţial a unui condensator împărţită la n prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** la două condensatoare cu 4 V și 6 V distribuite concordant, tensiunea ansamblului este 10 V, nu 4 sau 6.
- **Stare:** SERIES_VOLTAGE_KVL_8_2; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-063 | AU-599db2eade72bfaa
- qabc_sha256 599db2eade72bfaaec3818a92d1cf66e3833b34e44967db7f4e82276722c5708; member_ids G1-ELE-063;G2-ELEC-208; imported key {"G1-ELE-063":"B","G2-ELEC-208":"B"} PĂSTRATĂ.
- **Original:** Energia magnetostatică produsă de curentul i care parcurge un circuit care conţine o inductanţă L este egală cu:
  - A. 1/2 L i
  - B. 1/2 Li2
  - C. Li
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Energia inductanței U=½LI²**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: 1/2 Li misses second factor I and fails joule dimensions. Varianta B este verificată astfel: 1/2 L I² is magnetic field energy. Varianta C este verificată astfel: Li not energy, units Wb (flux linkage). Condiția explicită și testul de falsificare: **pentru I dublu și L constant, energia este de 4 ori; în original «Li2» necesită verificarea exponentului grafic**.
- **Vertical:** A A 1/2 Li misses second factor I and fails joule dimensions; B B: 1/2 L I² is magnetic field energy; C C: Li not energy, units Wb (flux linkage).
- **Orizontal (A↔B, A↔C, B↔C):** A «1/2 L i» versus B «1/2 Li2»: valori/concepte diferite, comparați cu Energia inductanței U=½LI². A versus C «Li» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa 1/2 Li2 de Li prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** pentru I dublu și L constant, energia este de 4 ori; în original «Li2» necesită verificarea exponentului grafic.
- **Stare:** INDUCTOR_ENERGY_14_4_EXPONENT_FORMAT_GATE; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-064 | AU-62d5caa5fe654d18
- qabc_sha256 62d5caa5fe654d18fd2d00292484b772b7019f00670d316c7495cb9c2a3e4163; member_ids G1-ELE-064;G2-ELEC-209; imported key {"G1-ELE-064":"A","G2-ELEC-209":"A"} PĂSTRATĂ.
- **Original:** Energia electrostatică a unui conductor izolat în spaţiu, încărcat cu o sarcină q şi aflat la un potenţial V este egală cu:
  - A. 1/2 q V
  - B. q V
  - C. 2 q V
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Energia electrostatică U=½qV pentru capacitate liniară, referință potențial zero**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: U=1/2 qV for linear isolated conductor charged from 0. Varianta B este verificată astfel: qV is twice U when V increases with charge. Varianta C este verificată astfel: 2qV is four times actual for linear conductor. Condiția explicită și testul de falsificare: **pentru dublarea sarcinii pe un conductor izolat cu aceeași capacitate, U devine de patru ori mai mare; formula fără 1/2 supranumără aria triunghiului Q-V**.
- **Vertical:** A A: U=1/2 qV for linear isolated conductor charged from 0; B B qV is twice U when V increases with charge; C C 2qV is four times actual for linear conductor.
- **Orizontal (A↔B, A↔C, B↔C):** A «1/2 q V» versus B «q V»: valori/concepte diferite, comparați cu Energia electrostatică U=½qV pentru capacitate liniară, referință potențial zero. A versus C «2 q V» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa q V de 2 q V prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** pentru dublarea sarcinii pe un conductor izolat cu aceeași capacitate, U devine de patru ori mai mare; formula fără 1/2 supranumără aria triunghiului Q-V.
- **Stare:** ELECTROSTATIC_HALF_Q_V_UNDER_LINEAR_ASSUMPTIONS; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-067 | AU-e63952b743f529c0
- qabc_sha256 e63952b743f529c0cb34f40e33dd056b623dd9886135ae6b4026b327c50344a5; member_ids G1-ELE-067;G2-ELEC-212; imported key {"G1-ELE-067":"B","G2-ELEC-212":"B"} PĂSTRATĂ.
- **Original:** Enunţul "suma algebrică a tensiunilor electromotoare dintr-o buclă a unei reţele electrice este egală cu suma algebrică a căderilor de tensiune din buclă" reprezintă:
  - A. Prima lege a lui Kirchhoff
  - B. a doua lege a lui Kirchhoff
  - C. Legea Joule -Lenz
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Legea a doua Kirchhoff: ΣEMF=Σcăderi tensiune într-o buclă în model cvasi-staționar**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: KCL sums junction currents, not loop voltages. Varianta B este verificată astfel: loop EMF balances drops (KVL). Varianta C este verificată astfel: Joule-Lenz heating relation P=I²R unrelated. Condiția explicită și testul de falsificare: **într-o buclă 12 V cu căderi 7 și 5 V, bilanțul este zero; prima lege privește nodurile, nu buclele**.
- **Vertical:** A A KCL sums junction currents, not loop voltages; B B loop EMF balances drops (KVL); C C Joule-Lenz heating relation P=I²R unrelated.
- **Orizontal (A↔B, A↔C, B↔C):** A «Prima lege a lui Kirchhoff» versus B «a doua lege a lui Kirchhoff»: valori/concepte diferite, comparați cu Legea a doua Kirchhoff: ΣEMF=Σcăderi tensiune într-o buclă în model cvasi-staționar. A versus C «Legea Joule -Lenz» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa a doua lege a lui Kirchhoff de Legea Joule -Lenz prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** într-o buclă 12 V cu căderi 7 și 5 V, bilanțul este zero; prima lege privește nodurile, nu buclele.
- **Stare:** KIRCHHOFF_LOOP_RULE_10_3; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-068 | AU-058febcbfd238513
- qabc_sha256 058febcbfd2385135909a4993279a18bb9a425740b228542e43ae6d758eccb28; member_ids G1-ELE-068;G2-ELEC-213; imported key {"G1-ELE-068":"A","G2-ELEC-213":"A"} PĂSTRATĂ.
- **Original:** Expresia B x i x l , unde i este intensitatea curentului care străbate un conductor de lungime l, situat perpendicular pe câmpul de inducţie magnetică de mărime B, reprezintă:
  - A. o forţă
  - B. o tensiune
  - C. o rezistenţă
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/11-4-magnetic-force-on-a-current-carrying-conductor ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **F = BIl pentru conductor rectiliniu perpendicular pe B, în câmp uniform**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: |F|=B I l for perpendicular conductor. Varianta B este verificată astfel: BIl has force unit N not voltage. Varianta C este verificată astfel: BIl is not resistance Ω. Condiția explicită și testul de falsificare: **analiza dimensională (T)(A)(m)=N; dacă ar fi paralel cu B forța ar fi zero, condiția de perpendicularitate e decisivă**.
- **Vertical:** A A |F|=B I l for perpendicular conductor; B B BIl has force unit N not voltage; C C BIl is not resistance Ω.
- **Orizontal (A↔B, A↔C, B↔C):** A «o forţă» versus B «o tensiune»: valori/concepte diferite, comparați cu F = BIl pentru conductor rectiliniu perpendicular pe B, în câmp uniform. A versus C «o rezistenţă» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa o tensiune de o rezistenţă prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** analiza dimensională (T)(A)(m)=N; dacă ar fi paralel cu B forța ar fi zero, condiția de perpendicularitate e decisivă.
- **Stare:** MAGNETIC_FORCE_PERPENDICULAR_11_4; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-069 | AU-4b53a6fa89a1be41
- qabc_sha256 4b53a6fa89a1be411d6cb6966bea30c5c5cd83473f4e04dd4a8496c00d7e767d; member_ids G1-ELE-069;G2-ELEC-214; imported key {"G1-ELE-069":"A","G2-ELEC-214":"A"} PĂSTRATĂ.
- **Original:** Expresia matematica a legii lui Ohm pentru o porţiune de circuit este:
  - A. I = U / R
  - B. I = UxR
  - C. I = U - R
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/9-2-model-of-conduction-in-metals ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Legea lui Ohm pentru rezistor liniar: I=U/R**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: I=U/R exactly for ohmic circuit element. Varianta B este verificată astfel: U×R units VΩ wrong. Varianta C este verificată astfel: U−R subtraction incompatible units. Condiția explicită și testul de falsificare: **pentru U=12 V și R=6Ω, I=2A; produsul U×R are unități VΩ, iar scăderea U−R este dimensional imposibilă**.
- **Vertical:** A A I=U/R exactly for ohmic circuit element; B B U×R units VΩ wrong; C C U−R subtraction incompatible units.
- **Orizontal (A↔B, A↔C, B↔C):** A «I = U / R» versus B «I = UxR»: valori/concepte diferite, comparați cu Legea lui Ohm pentru rezistor liniar: I=U/R. A versus C «I = U - R» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa I = UxR de I = U - R prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** pentru U=12 V și R=6Ω, I=2A; produsul U×R are unități VΩ, iar scăderea U−R este dimensional imposibilă.
- **Stare:** OHM_LINEAR_RATIO; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-070 | AU-482817fbce16f0be
- qabc_sha256 482817fbce16f0be1603a18b4d1a251d23ef0e36771943e8910214bccc5de4dc; member_ids G1-ELE-070;G2-ELEC-215; imported key {"G1-ELE-070":"B","G2-ELEC-215":"B"} PĂSTRATĂ.
- **Original:** Extinderea domeniului de măsurare la ampermetre se realizează cu:
  - A. rezistente adiţionale
  - B. shunturi
  - C. bobine înseriate
- **Sursă și locator:** https://openstax.org/books/college-physics-2e/pages/21-4-dc-voltmeters-and-ammeters ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Ampermetru analog: șunt de rezistență mică în paralel cu mecanismul de măsurare**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: series additional resistor is standard voltmeter extension, not current meter. Varianta B este verificată astfel: low-resistance shunt diverts current and increases range. Varianta C este verificată astfel: series coils no general current range extension. Condiția explicită și testul de falsificare: **ramura șuntului preia surplusul de curent, spre deosebire de rezistența adițională serie folosită la voltmetre**.
- **Vertical:** A A series additional resistor is standard voltmeter extension, not current meter; B B low-resistance shunt diverts current and increases range; C C series coils no general current range extension.
- **Orizontal (A↔B, A↔C, B↔C):** A «rezistente adiţionale» versus B «shunturi»: valori/concepte diferite, comparați cu Ampermetru analog: șunt de rezistență mică în paralel cu mecanismul de măsurare. A versus C «bobine înseriate» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa shunturi de bobine înseriate prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** ramura șuntului preia surplusul de curent, spre deosebire de rezistența adițională serie folosită la voltmetre.
- **Stare:** ANALOG_AMMETER_SHUNT_21_4; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-071 | AU-faed8ff35fdb8d79
- qabc_sha256 faed8ff35fdb8d7903dc04421bf0e077469d65169f2e4e73a1e41418b54335f2; member_ids G1-ELE-071;G2-ELEC-216; imported key {"G1-ELE-071":"B","G2-ELEC-216":"B"} PĂSTRATĂ.
- **Original:** Extinderea domeniului de măsurare la voltmetre se realizează cu:
  - A. shunturi
  - B. rezistente adiţionale
  - C. condensatoare montate în paralel
- **Sursă și locator:** https://openstax.org/books/college-physics-2e/pages/21-4-dc-voltmeters-and-ammeters ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Voltmetru analog: rezistență adițională serie cu galvanometrul, ridicând rezistența de intrare**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: shunt suitable ammeter, would load voltage source. Varianta B este verificată astfel: high-value series resistor limits current and extends voltmeter range. Varianta C este verificată astfel: capacitors in parallel do not form DC voltmeter range extension. Condiția explicită și testul de falsificare: **șuntul mic în paralel ar crește curentul galvanometrului, nepotrivit pentru extensia domeniului de tensiune**.
- **Vertical:** A A shunt suitable ammeter, would load voltage source; B B high-value series resistor limits current and extends voltmeter range; C C capacitors in parallel do not form DC voltmeter range extension.
- **Orizontal (A↔B, A↔C, B↔C):** A «shunturi» versus B «rezistente adiţionale»: valori/concepte diferite, comparați cu Voltmetru analog: rezistență adițională serie cu galvanometrul, ridicând rezistența de intrare. A versus C «condensatoare montate în paralel» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa rezistente adiţionale de condensatoare montate în paralel prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** șuntul mic în paralel ar crește curentul galvanometrului, nepotrivit pentru extensia domeniului de tensiune.
- **Stare:** ANALOG_VOLTMETER_SERIES_21_4; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-072 | AU-d40bfa2c99a13401
- qabc_sha256 d40bfa2c99a134018488239f8a121e5e047e57b1a89e2e882ed37f024f22e8d7; member_ids G1-ELE-072;G2-ELEC-217; imported key {"G1-ELE-072":"A","G2-ELEC-217":"A"} PĂSTRATĂ.
- **Original:** Factorul de atenuare al unui circuit format dintr-un rezistor de rezistenţă R înseriat cu o bobină de inductanţă L, alimentate de o tensiune electromotoare constantă este egal cu:
  - A. R/L
  - B. L/R
  - C. 1
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Circuit RL: τ=L/R; coeficient de atenuare în exp(-αt) este α=R/L**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: R/L is exponential damping coefficient s^-1. Varianta B este verificată astfel: L/R is time constant in s, not coefficient. Varianta C este verificată astfel: 1 dimensionless cannot equal attenuation coefficient generally. Condiția explicită și testul de falsificare: **R=10Ω,L=2H dă α=5 s⁻¹, în timp ce τ=0,2 s; diferența unităților de măsură separă A de B**.
- **Vertical:** A A R/L is exponential damping coefficient s^-1; B B L/R is time constant in s, not coefficient; C C 1 dimensionless cannot equal attenuation coefficient generally.
- **Orizontal (A↔B, A↔C, B↔C):** A «R/L» versus B «L/R»: valori/concepte diferite, comparați cu Circuit RL: τ=L/R; coeficient de atenuare în exp(-αt) este α=R/L. A versus C «1» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa L/R de 1 prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** R=10Ω,L=2H dă α=5 s⁻¹, în timp ce τ=0,2 s; diferența unităților de măsură separă A de B.
- **Stare:** RL_DECAY_ALPHA_R_OVER_L_14_4; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-075 | AU-fa5e005721b46549
- qabc_sha256 fa5e005721b4654920ebb50cfc431d425d4a623fb55b82c5d6a50331ee501aac; member_ids G1-ELE-075;G2-ELEC-220; imported key {"G1-ELE-075":"A","G2-ELEC-220":"A"} PĂSTRATĂ.
- **Original:** Formula de calcul a frecventei produsa în sistemul electroenergetic de un generator cu n [rot/min] si p perechi de poli este:
  - A. f =n p / 60
  - B. f = 60 n / p
  - C. f = 60 p / n
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/13-6-electric-generators-and-back-emf ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Generator sincron cu p perechi de poli: f=np/60 pentru n în rot/min**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: f=n p/60 for p pole pairs and n rpm. Varianta B este verificată astfel: 60n/p has inverted dimensions for rpm input. Varianta C este verificată astfel: 60p/n inverts physical proportionality. Condiția explicită și testul de falsificare: **pentru n=1500 rpm,p=2 => f=50 Hz; a confunda p cu numărul total de poli produce eroare de factor doi**.
- **Vertical:** A A f=n p/60 for p pole pairs and n rpm; B B 60n/p has inverted dimensions for rpm input; C C 60p/n inverts physical proportionality.
- **Orizontal (A↔B, A↔C, B↔C):** A «f =n p / 60» versus B «f = 60 n / p»: valori/concepte diferite, comparați cu Generator sincron cu p perechi de poli: f=np/60 pentru n în rot/min. A versus C «f = 60 p / n» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa f = 60 n / p de f = 60 p / n prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** pentru n=1500 rpm,p=2 => f=50 Hz; a confunda p cu numărul total de poli produce eroare de factor doi.
- **Stare:** GENERATOR_F_NP_OVER_60_POLE_PAIR_SCOPE; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-076 | AU-ae2f68fc7c532592
- qabc_sha256 ae2f68fc7c532592e11f71af755c41e94ad1dcc3ee62b28e61b70dc477a21108; member_ids G1-ELE-076;G2-ELEC-221; imported key {"G1-ELE-076":"B","G2-ELEC-221":"B"} PĂSTRATĂ.
- **Original:** Formula e = B l v, unde e este tensiune electromotoare, B este inducţia magnetică, l este lungimea unui conductor, v este viteza de deplasare a acestuia, reprezintă o forma particulară a:
  - A. teoremelor Biot-Savart
  - B. legii inducţiei electromagnetice
  - C. legii circuitului magnetic
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Mișcarea conductorului într-un câmp magnetic induce e=Blv în configurație perpendiculară, ca situație particulară a inducției Faraday**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: Biot-Savart calculates magnetic field from current, not e=Blv. Varianta B este verificată astfel: Faraday induction, motional special case |e|=Blv. Varianta C este verificată astfel: magnetic circuit laws relate flux and reluctance not moving conductor EMF. Condiția explicită și testul de falsificare: **dacă v=0 în geometria din enunț nu apare e motională; creșterea v dublează e la B,l constante**.
- **Vertical:** A A Biot-Savart calculates magnetic field from current, not e=Blv; B B Faraday induction, motional special case |e|=Blv; C C magnetic circuit laws relate flux and reluctance not moving conductor EMF.
- **Orizontal (A↔B, A↔C, B↔C):** A «teoremelor Biot-Savart» versus B «legii inducţiei electromagnetice»: valori/concepte diferite, comparați cu Mișcarea conductorului într-un câmp magnetic induce e=Blv în configurație perpendiculară, ca situație particulară a inducției Faraday. A versus C «legii circuitului magnetic» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa legii inducţiei electromagnetice de legii circuitului magnetic prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** dacă v=0 în geometria din enunț nu apare e motională; creșterea v dublează e la B,l constante.
- **Stare:** MOTIONAL_EMF_FARADAY_SCOPE; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-078 | AU-997ca119cd90035f
- qabc_sha256 997ca119cd90035f9dad5cc2d6bea82fc3f246e04bfa8f5fb2d3ba77fa4b1e89; member_ids G1-ELE-078;G2-ELEC-223; imported key {"G1-ELE-078":"B","G2-ELEC-223":"B"} PĂSTRATĂ.
- **Original:** Forţa care se exercită între două conductoare străbătute de curenţi electrici se numeşte:
  - A. forţă electrocinetică
  - B. forţă electrodinamică
  - C. forţă magnetomotoare
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/12-3-magnetic-force-between-two-parallel-currents ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Forța între doi conductori străbătuți de curent este interacțiune electrodinamică**. În modelul fizic corespunzător, răspunsul importat **B** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: 'electrocinetică' not standard named interaction for two current-carrying wires. Varianta B este verificată astfel: force interaction is electrodynamic, due to their magnetic fields. Varianta C este verificată astfel: magnetomotive force is NI in A-turns, not mechanical force. Condiția explicită și testul de falsificare: **curenți paraleli de același sens se atrag, sensuri opuse se resping; o «forță magnetomotoare» este mărime de excitație magnetică, nu această forță mecanică**.
- **Vertical:** A A 'electrocinetică' not standard named interaction for two current-carrying wires; B B force interaction is electrodynamic, due to their magnetic fields; C C magnetomotive force is NI in A-turns, not mechanical force.
- **Orizontal (A↔B, A↔C, B↔C):** A «forţă electrocinetică» versus B «forţă electrodinamică»: valori/concepte diferite, comparați cu Forța între doi conductori străbătuți de curent este interacțiune electrodinamică. A versus C «forţă magnetomotoare» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa forţă electrodinamică de forţă magnetomotoare prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** curenți paraleli de același sens se atrag, sensuri opuse se resping; o «forță magnetomotoare» este mărime de excitație magnetică, nu această forță mecanică.
- **Stare:** AMPERE_FORCE_12_3; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G1-ELE-079 | AU-ce8d3f759b552260
- qabc_sha256 ce8d3f759b552260639c220555e70331bc16668b8e78f13ddf26d38d9d298081; member_ids G1-ELE-079;G2-ELEC-224; imported key {"G1-ELE-079":"A","G2-ELEC-224":"A"} PĂSTRATĂ.
- **Original:** Tensiunea electromotoare indusă într-un circuit închis, prin variaţia fluxului magnetic, este:
  - A. direct proporţională cu variaţia în timp a fluxului magnetic
  - B. invers proporţională cu variaţia în timp a fluxului magnetic
  - C. dependentă de modul în care este produs fluxul magnetic
- **Sursă și locator:** https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law ; locul/proporția exactă a teoremei se vede în secțiunea sursei indicată. Evidență preliminară: EDUCATIONAL_REFERENCE_AND_EXPLICIT_PHYSICAL_DERIVATION.
- **Context (teoremă, obiect, excepție):** Formula/definiția aplicabilă este **Legea Faraday e=-dΦ/dt, deci mărimea f.e.m. este proporțională cu viteza schimbării fluxului**. În modelul fizic corespunzător, răspunsul importat **A** este candidatul pozitiv, cu limitele și obiectul concret din enunț. Varianta A trebuie verificată distinct: e=−dΦ/dt means EMF proportional to flux RATE of variation. Varianta B este verificată astfel: inverse proportionality to derivative is wrong. Varianta C este verificată astfel: induced EMF arises from flux change irrespective of physical mechanism (under usual conditions). Condiția explicită și testul de falsificare: **dublarea vitezei de variație la aceeași geometrie dublează |e|; semnul minus al lui Lenz indică opoziția, nu o proporționalitate inversă**.
- **Vertical:** A A e=−dΦ/dt means EMF proportional to flux RATE of variation; B B inverse proportionality to derivative is wrong; C C induced EMF arises from flux change irrespective of physical mechanism (under usual conditions).
- **Orizontal (A↔B, A↔C, B↔C):** A «direct proporţională cu variaţia în timp a fluxului magnetic» versus B «invers proporţională cu variaţia în timp a fluxului magnetic»: valori/concepte diferite, comparați cu Legea Faraday e=-dΦ/dt, deci mărimea f.e.m. este proporțională cu viteza schimbării fluxului. A versus C «dependentă de modul în care este produs fluxul magnetic» testează aceeași sursă pozitivă și condițiile. B versus C separă alternativa invers proporţională cu variaţia în timp a fluxului magnetic de dependentă de modul în care este produs fluxul magnetic prin modelul exact, nu doar prin eliminare.
- **Test negativ/reversie:** dublarea vitezei de variație la aceeași geometrie dublează |e|; semnul minus al lui Lenz indică opoziția, nu o proporționalitate inversă.
- **Stare:** FARADAY_RATE_OF_CHANGE_13_1; PRIOR_RESEARCH_REUSED_WITH_DIRECT_FORMULA_TEST; SOURCE_EXACT_EXAM_TEXT_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## Regresii critice
- G1-ELE-063: originalul «Li2» nu are exponent clar textual. La verificarea oficialului XLSX, verificați că i2 este I la pătrat, nu 2 × i. Nu rescrieți enunțul aici.
- G1-ELE-072: distingeți *factorul de atenuare α* R/L de *constanta de timp τ* L/R, ambele pot apărea în surse, dar întrebarea cere α.
- Pentru toate grilele de electrotehnică, regula din manualul general nu înlocuiește condițiile speciale (curent sinusoidal, vector Poynting, topologie, sursă izolată).
- Continuare pe următoarele grupe originale din DEEP_ELE fără duplicate, nu pe chei schimbate.
