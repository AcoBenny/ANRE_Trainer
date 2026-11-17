# CKPT-106 | 20 P2 Grad II: RLC, circuit, puteri, unități și măsurări | 2026-11-17

## Convergență și limite
- Baza CKPT105 362/568 unități și 442/822 ID-uri; acest lot +20 unice, +20 ID-uri => **382/568 unități și 462/822 ID-uri** contextual documentate. **186 unități P2 rămase**, 0/822 approved for learning.
- S-a reutilizat raționamentul DEEP_ELE_17–18, cu verificarea familiei de formule față de OpenStax §9.5, §10.2, §15.3, §15.4 și Schneider Electric «Definition of reactive power», accesate textual în această sesiune. BIPM documentează SI; pentru aparate concrete se cere manual identic, nepretins aici.
- Nu confundăm această etapă cu QA independent. Cheile A importate și originea ca grile oficiale ANRE rămân neverificate; nu se modifică master/HTML/APK/main, fără merge.

## G2-ELEC-055 | AU-345c3f115e3a8af1
- sha256 345c3f115e3a8af1baec0d7338ff7985ea7fc4ab4749d315539cd0fe64cf8b78; member_ids G2-ELEC-055; imported key {"G2-ELEC-055":"A"} păstrată.
- **Original:** Într-un circuit ideal pur capacitiv, puterea activă medie este:
  - A. zero
  - B. egală cu puterea aparentă
  - C. egală cu energia stocată
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit; **Puterea medie în condensator ideal pur e 0: cos(90°)=0**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Puterea medie în condensator ideal pur e 0: cos(90°)=0**. A corespunde intenției importate, potrivit motivului: Într-un condensator ideal energia se stochează/returnează periodic, media puterii active este zero.. B nu se potrivește deoarece Puterea aparentă S=UI poate fi nenulă chiar când P=0.. C nu se potrivește deoarece Energia stocată se măsoară în J, nu are aceeași dimensiune cu puterea în W.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Într-un condensator ideal energia se stochează/returnează periodic, media puterii active este zero.; B Puterea aparentă S=UI poate fi nenulă chiar când P=0.; C Energia stocată se măsoară în J, nu are aceeași dimensiune cu puterea în W..
- **Orizontal ABC:** A «zero» se compară cu B «egală cu puterea aparentă» și C «egală cu energia stocată» folosind **Puterea medie în condensator ideal pur e 0: cos(90°)=0**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Puterea medie în condensator ideal pur e 0: cos(90°)=0** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-056 | AU-acd7fadf59ffd603
- sha256 acd7fadf59ffd6038dccbb168d647882a73209a6ced2ac111a4d2224ae84d25c; member_ids G2-ELEC-056; imported key {"G2-ELEC-056":"A"} păstrată.
- **Original:** Într-un sistem trifazat echilibrat, conductorul de nul poate avea curent:
  - A. nul, pentru sarcină perfect echilibrată și condițiile corespunzătoare
  - B. întotdeauna egal cu curentul de fază
  - C. întotdeauna dublu față de curentul de fază
- **Sursa/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; **Suma curenților trifazați perfect echilibrați e zero; armonicile triplene cer excepții**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Suma curenților trifazați perfect echilibrați e zero; armonicile triplene cer excepții**. A corespunde intenției importate, potrivit motivului: În sistem trifazat perfect echilibrat și fără armonici de ordin 3, suma fazorială a curenților poate fi zero pe nul.. B nu se potrivește deoarece Curentul nulului nu este obligatoriu egal cu cel al unei faze.. C nu se potrivește deoarece Curentul nulului nu este obligatoriu dublul curentului de fază.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A În sistem trifazat perfect echilibrat și fără armonici de ordin 3, suma fazorială a curenților poate fi zero pe nul.; B Curentul nulului nu este obligatoriu egal cu cel al unei faze.; C Curentul nulului nu este obligatoriu dublul curentului de fază..
- **Orizontal ABC:** A «nul, pentru sarcină perfect echilibrată și condițiile corespunzătoare» se compară cu B «întotdeauna egal cu curentul de fază» și C «întotdeauna dublu față de curentul de fază» folosind **Suma curenților trifazați perfect echilibrați e zero; armonicile triplene cer excepții**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Suma curenților trifazați perfect echilibrați e zero; armonicile triplene cer excepții** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-057 | AU-3a89d119d8d12032
- sha256 3a89d119d8d1203216297ddbb9e7b6b040f949b490a5d98a9ab7909776cf5662; member_ids G2-ELEC-057; imported key {"G2-ELEC-057":"A"} păstrată.
- **Original:** Eficiența/randamentul unui echipament este raportul dintre:
  - A. puterea utilă și puterea absorbită
  - B. puterea absorbită și pierderi
  - C. tensiune și curent
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power; **Randament η=Putil/Pabsorbit**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Randament η=Putil/Pabsorbit**. A corespunde intenției importate, potrivit motivului: Randamentul η=P_util/P_absorbită, pentru P_absorbită pozitivă.. B nu se potrivește deoarece P_absorbită/pierderi nu este definiția η și poate fi >1.. C nu se potrivește deoarece U/I are dimensiunea rezistenței electrice, nu a eficienței.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Randamentul η=P_util/P_absorbită, pentru P_absorbită pozitivă.; B P_absorbită/pierderi nu este definiția η și poate fi >1.; C U/I are dimensiunea rezistenței electrice, nu a eficienței..
- **Orizontal ABC:** A «puterea utilă și puterea absorbită» se compară cu B «puterea absorbită și pierderi» și C «tensiune și curent» folosind **Randament η=Putil/Pabsorbit**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Randament η=Putil/Pabsorbit** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-058 | AU-545cd1006dc3e497
- sha256 545cd1006dc3e497a02641e384028572544e39335e175af36f7379f42e0bdbcc; member_ids G2-ELEC-058; imported key {"G2-ELEC-058":"A"} păstrată.
- **Original:** Pierderile Joule într-un conductor cresc cu:
  - A. I²·R
  - B. I/R
  - C. U/R²
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power; **Pierderea Joule este I²R**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Pierderea Joule este I²R**. A corespunde intenției importate, potrivit motivului: Pierderile Joule la rezistor P_J=I²R la R constant.. B nu se potrivește deoarece I/R are unitate A/Ω, nu putere.. C nu se potrivește deoarece U/R² nu are unitate watt.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Pierderile Joule la rezistor P_J=I²R la R constant.; B I/R are unitate A/Ω, nu putere.; C U/R² nu are unitate watt..
- **Orizontal ABC:** A «I²·R» se compară cu B «I/R» și C «U/R²» folosind **Pierderea Joule este I²R**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Pierderea Joule este I²R** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-059 | AU-406107db235e2329
- sha256 406107db235e2329c5de74a7832f6735eda52e72e0c3f95b6a29619f050c771d; member_ids G2-ELEC-059; imported key {"G2-ELEC-059":"A"} păstrată.
- **Original:** Într-o linie electrică, creșterea tensiunii pentru aceeași putere transmisă determină, ideal, un curent:
  - A. mai mic
  - B. mai mare de patru ori
  - C. neschimbat obligatoriu
- **Sursa/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; **La P și cosφ constante, I invers proporțional cu U**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **La P și cosφ constante, I invers proporțional cu U**. A corespunde intenției importate, potrivit motivului: La P și cosφ fixe, I=P/(√3U cosφ), deci U mai mare reduce I.. B nu se potrivește deoarece Nu există factor 4 obligatoriu pentru curent dacă U crește.. C nu se potrivește deoarece I nu rămâne obligatoriu același când P fix și U variază.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A La P și cosφ fixe, I=P/(√3U cosφ), deci U mai mare reduce I.; B Nu există factor 4 obligatoriu pentru curent dacă U crește.; C I nu rămâne obligatoriu același când P fix și U variază..
- **Orizontal ABC:** A «mai mic» se compară cu B «mai mare de patru ori» și C «neschimbat obligatoriu» folosind **La P și cosφ constante, I invers proporțional cu U**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **La P și cosφ constante, I invers proporțional cu U** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-060 | AU-a0150b5b3af992f1
- sha256 a0150b5b3af992f1aa51edd7c82ad437c6fd3b780e25724f4e2b90e4e451e99f; member_ids G2-ELEC-060; imported key {"G2-ELEC-060":"A"} păstrată.
- **Original:** Un wattmetru este destinat măsurării:
  - A. puterii electrice
  - B. rezistenței de izolație exclusiv
  - C. frecvenței exclusiv
- **Sursa/locator:** https://www.fluke.com/en/learn/blog/electrical/power-measurements; **Wattmetrul măsoară puterea electrică**; SOURCE_EXACT_DEVICE_OR_SYMBOL_PAGE_NOT_FULLY_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Wattmetrul măsoară puterea electrică**. A corespunde intenției importate, potrivit motivului: Wattmetrul măsoară puterea electrică activă în circuit în condițiile de conectare specificate.. B nu se potrivește deoarece Rezistența de izolație se măsoară cu megohmetru/echipament dedicat.. C nu se potrivește deoarece Frecvența se măsoară cu frecvențmetru, nu exclusiv wattmetru.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Wattmetrul măsoară puterea electrică activă în circuit în condițiile de conectare specificate.; B Rezistența de izolație se măsoară cu megohmetru/echipament dedicat.; C Frecvența se măsoară cu frecvențmetru, nu exclusiv wattmetru..
- **Orizontal ABC:** A «puterii electrice» se compară cu B «rezistenței de izolație exclusiv» și C «frecvenței exclusiv» folosind **Wattmetrul măsoară puterea electrică**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Wattmetrul măsoară puterea electrică** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-061 | AU-59b3bbc4578855a7
- sha256 59b3bbc4578855a79b58bb444e5ac1ab1ad4cc5a5642dde50efb335373d5b69c; member_ids G2-ELEC-061; imported key {"G2-ELEC-061":"A"} păstrată.
- **Original:** Un frecvențmetru este destinat măsurării:
  - A. frecvenței
  - B. rezistenței
  - C. inductanței
- **Sursa/locator:** https://www.bipm.org/en/publications/si-brochure; **Frecvențmetrul măsoară frecvența, Hz**; SOURCE_EXACT_DEVICE_OR_SYMBOL_PAGE_NOT_FULLY_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Frecvențmetrul măsoară frecvența, Hz**. A corespunde intenției importate, potrivit motivului: Frecvențmetrul măsoară numărul ciclurilor pe secundă în Hz.. B nu se potrivește deoarece Rezistența necesită ohmmetru.. C nu se potrivește deoarece Inductanța necesită LCR-metru sau metodă dedicată.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Frecvențmetrul măsoară numărul ciclurilor pe secundă în Hz.; B Rezistența necesită ohmmetru.; C Inductanța necesită LCR-metru sau metodă dedicată..
- **Orizontal ABC:** A «frecvenței» se compară cu B «rezistenței» și C «inductanței» folosind **Frecvențmetrul măsoară frecvența, Hz**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Frecvențmetrul măsoară frecvența, Hz** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-062 | AU-fd38731b580cdd50
- sha256 fd38731b580cdd503106da11593bc29255d99fafd43f72c10266cc7405fff075; member_ids G2-ELEC-062; imported key {"G2-ELEC-062":"A"} păstrată.
- **Original:** Un megohmetru este utilizat în principal pentru măsurarea:
  - A. rezistenței de izolație la tensiuni de încercare specifice
  - B. puterii active de rețea
  - C. curentului de scurtcircuit al rețelei
- **Sursa/locator:** https://www.fluke.com/en/learn/blog/insulation-testers/insulation-resistance-testing; **Megohmetrul măsoară rezistența de izolație la tensiune de încercare; circuit deconectat**; SOURCE_EXACT_DEVICE_OR_SYMBOL_PAGE_NOT_FULLY_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Megohmetrul măsoară rezistența de izolație la tensiune de încercare; circuit deconectat**. A corespunde intenției importate, potrivit motivului: Megohmetrul aplică tensiune DC de test și măsoară rezistența de izolație.. B nu se potrivește deoarece Nu este wattmetru pentru măsurarea puterii active.. C nu se potrivește deoarece Nu măsoară curentul de scurtcircuit al rețelei în exploatare.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Megohmetrul aplică tensiune DC de test și măsoară rezistența de izolație.; B Nu este wattmetru pentru măsurarea puterii active.; C Nu măsoară curentul de scurtcircuit al rețelei în exploatare..
- **Orizontal ABC:** A «rezistenței de izolație la tensiuni de încercare specifice» se compară cu B «puterii active de rețea» și C «curentului de scurtcircuit al rețelei» folosind **Megohmetrul măsoară rezistența de izolație la tensiune de încercare; circuit deconectat**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Megohmetrul măsoară rezistența de izolație la tensiune de încercare; circuit deconectat** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-064 | AU-abef5924a0220011
- sha256 abef5924a02200115277dee955567d805465afffed097f9917a27c8cbdbef0b4; member_ids G2-ELEC-064; imported key {"G2-ELEC-064":"A"} păstrată.
- **Original:** Simbolul electric pentru rezistență este în mod uzual:
  - A. R
  - B. C
  - C. L
- **Sursa/locator:** https://www.bipm.org/en/publications/si-brochure/; **Simbolul rezistenței este R**; SOURCE_EXACT_DEVICE_OR_SYMBOL_PAGE_NOT_FULLY_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Simbolul rezistenței este R**. A corespunde intenției importate, potrivit motivului: R este simbol convențional al rezistenței.. B nu se potrivește deoarece C indică de regulă capacitate, nu rezistență.. C nu se potrivește deoarece L indică inductanță, nu rezistență.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A R este simbol convențional al rezistenței.; B C indică de regulă capacitate, nu rezistență.; C L indică inductanță, nu rezistență..
- **Orizontal ABC:** A «R» se compară cu B «C» și C «L» folosind **Simbolul rezistenței este R**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Simbolul rezistenței este R** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-065 | AU-181fe37e2a54f2a3
- sha256 181fe37e2a54f2a33f8cb80eabaeb06994f2a28f5fc5c24425032dd466a7dafc; member_ids G2-ELEC-065; imported key {"G2-ELEC-065":"A"} păstrată.
- **Original:** Simbolul uzual pentru inductanță este:
  - A. L
  - B. R
  - C. G
- **Sursa/locator:** https://www.bipm.org/en/publications/si-brochure/; **Simbolul inductanței e L, unitatea e H**; SOURCE_EXACT_DEVICE_OR_SYMBOL_PAGE_NOT_FULLY_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Simbolul inductanței e L, unitatea e H**. A corespunde intenției importate, potrivit motivului: L desemnează inductanța.. B nu se potrivește deoarece R desemnează rezistența.. C nu se potrivește deoarece G desemnează conductanța, nu inductanța.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A L desemnează inductanța.; B R desemnează rezistența.; C G desemnează conductanța, nu inductanța..
- **Orizontal ABC:** A «L» se compară cu B «R» și C «G» folosind **Simbolul inductanței e L, unitatea e H**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Simbolul inductanței e L, unitatea e H** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-066 | AU-56c0052ee30cdbc7
- sha256 56c0052ee30cdbc75bd11376b6de9321ad3f72d74b0c2601f9a7865f7e7a4e3f; member_ids G2-ELEC-066; imported key {"G2-ELEC-066":"A"} păstrată.
- **Original:** Simbolul uzual pentru capacitate este:
  - A. C
  - B. L
  - C. I
- **Sursa/locator:** https://www.bipm.org/en/publications/si-brochure/; **Simbolul capacității este C, unitate F**; SOURCE_EXACT_DEVICE_OR_SYMBOL_PAGE_NOT_FULLY_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Simbolul capacității este C, unitate F**. A corespunde intenției importate, potrivit motivului: C desemnează capacitatea electrică.. B nu se potrivește deoarece L desemnează inductanța.. C nu se potrivește deoarece I desemnează intensitatea curentului.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A C desemnează capacitatea electrică.; B L desemnează inductanța.; C I desemnează intensitatea curentului..
- **Orizontal ABC:** A «C» se compară cu B «L» și C «I» folosind **Simbolul capacității este C, unitate F**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Simbolul capacității este C, unitate F** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-067 | AU-28a594aabec05bbc
- sha256 28a594aabec05bbcbe0b3ee50b07e1fd60ab58cfb1ba916780899e495d3d18a7; member_ids G2-ELEC-067; imported key {"G2-ELEC-067":"A"} păstrată.
- **Original:** Într-un circuit rezistiv pur alimentat în curent alternativ sinusoidal, factorul de putere este: 
  - A. 1
  - B. 0
  - C. -1 în orice situație
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit; **La rezistor ideal φ=0 și cosφ=1**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **La rezistor ideal φ=0 și cosφ=1**. A corespunde intenției importate, potrivit motivului: Element rezistiv pur are U/I în fază și cos0°=1.. B nu se potrivește deoarece cosφ=0 corespunde situației ideal reactive.. C nu se potrivește deoarece −1 poate descrie convenție de putere livrată, dar nu factorul de putere al rezistorului pasiv din stem.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Element rezistiv pur are U/I în fază și cos0°=1.; B cosφ=0 corespunde situației ideal reactive.; C −1 poate descrie convenție de putere livrată, dar nu factorul de putere al rezistorului pasiv din stem..
- **Orizontal ABC:** A «1» se compară cu B «0» și C «-1 în orice situație» folosind **La rezistor ideal φ=0 și cosφ=1**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **La rezistor ideal φ=0 și cosφ=1** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-068 | AU-8cf044ffdaedd743
- sha256 8cf044ffdaedd743971b947fea9f97edc0cac047e294bc88c53e985714e873d0; member_ids G2-ELEC-068; imported key {"G2-ELEC-068":"A"} păstrată.
- **Original:** Într-un circuit inductiv pur, curentul este defazat față de tensiune astfel încât: 
  - A. curentul rămâne în urmă față de tensiune cu 90°
  - B. curentul este în fază cu tensiunea
  - C. curentul este înainte cu 180°
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit; **La bobina ideală curentul întârzie 90°**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **La bobina ideală curentul întârzie 90°**. A corespunde intenției importate, potrivit motivului: Inductanța ideală face curentul să rămână 90° în urma tensiunii.. B nu se potrivește deoarece În fază este regimul rezistiv, nu inductiv pur.. C nu se potrivește deoarece Un avans de 180° nu rezultă pentru bobină ideală.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Inductanța ideală face curentul să rămână 90° în urma tensiunii.; B În fază este regimul rezistiv, nu inductiv pur.; C Un avans de 180° nu rezultă pentru bobină ideală..
- **Orizontal ABC:** A «curentul rămâne în urmă față de tensiune cu 90°» se compară cu B «curentul este în fază cu tensiunea» și C «curentul este înainte cu 180°» folosind **La bobina ideală curentul întârzie 90°**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **La bobina ideală curentul întârzie 90°** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-069 | AU-21d05c743b0a3481
- sha256 21d05c743b0a3481fa9054893c184d6d34ada68731050e72b26012f6d18cba09; member_ids G2-ELEC-069; imported key {"G2-ELEC-069":"A"} păstrată.
- **Original:** Într-un circuit capacitiv pur, curentul este: 
  - A. înaintea tensiunii cu 90°
  - B. în urmă cu 90°
  - C. în fază cu tensiunea
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit; **La condensator ideal curentul precede 90°**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **La condensator ideal curentul precede 90°**. A corespunde intenției importate, potrivit motivului: Capacitatea ideală face curentul să fie înaintea tensiunii cu 90°.. B nu se potrivește deoarece Întârzierea de 90° descrie bobina ideală.. C nu se potrivește deoarece Fază egală apare în rezistor, nu în condensator ideal.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Capacitatea ideală face curentul să fie înaintea tensiunii cu 90°.; B Întârzierea de 90° descrie bobina ideală.; C Fază egală apare în rezistor, nu în condensator ideal..
- **Orizontal ABC:** A «înaintea tensiunii cu 90°» se compară cu B «în urmă cu 90°» și C «în fază cu tensiunea» folosind **La condensator ideal curentul precede 90°**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **La condensator ideal curentul precede 90°** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-070 | AU-6a50976c52ab6e28
- sha256 6a50976c52ab6e28d78cd8957ecfebc4bf20930e82e2e26980e64b65c0f0f484; member_ids G2-ELEC-070; imported key {"G2-ELEC-070":"A"} păstrată.
- **Original:** Într-un circuit serie R-L-C, rezonanța apare când: 
  - A. reactanța inductivă și cea capacitivă se compensează
  - B. rezistența devine infinită
  - C. curentul devine obligatoriu zero
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac; **Rezonanța RLC serie apare la XL=XC**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Rezonanța RLC serie apare la XL=XC**. A corespunde intenției importate, potrivit motivului: Rezonanța serie ideală când XL=XC și partea reactivă netă este nulă.. B nu se potrivește deoarece Rezistența serie R nu devine obligatoriu infinită la rezonanță.. C nu se potrivește deoarece Curentul serie nu devine obligatoriu zero; poate fi maxim pentru U și R date.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Rezonanța serie ideală când XL=XC și partea reactivă netă este nulă.; B Rezistența serie R nu devine obligatoriu infinită la rezonanță.; C Curentul serie nu devine obligatoriu zero; poate fi maxim pentru U și R date..
- **Orizontal ABC:** A «reactanța inductivă și cea capacitivă se compensează» se compară cu B «rezistența devine infinită» și C «curentul devine obligatoriu zero» folosind **Rezonanța RLC serie apare la XL=XC**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Rezonanța RLC serie apare la XL=XC** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-071 | AU-542a095f086827b1
- sha256 542a095f086827b131ae58570b3e9e1a8bac705e4bb1f3f312f0a4dab550105f; member_ids G2-ELEC-071; imported key {"G2-ELEC-071":"A"} păstrată.
- **Original:** Într-un circuit serie R-L-C la rezonanță ideală, impedanța este determinată de: 
  - A. rezistența R
  - B. numai reactanța capacitivă
  - C. suma XL + XC
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac; **La rezonanță RLC serie impedanța este R**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **La rezonanță RLC serie impedanța este R**. A corespunde intenției importate, potrivit motivului: La rezonanță serie XL−XC=0, astfel modulul impedanței este R.. B nu se potrivește deoarece XC necompensată nu determină Z când XL=XC.. C nu se potrivește deoarece Suma scalară XL+XC nu este reactanța netă, care este diferența.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A La rezonanță serie XL−XC=0, astfel modulul impedanței este R.; B XC necompensată nu determină Z când XL=XC.; C Suma scalară XL+XC nu este reactanța netă, care este diferența..
- **Orizontal ABC:** A «rezistența R» se compară cu B «numai reactanța capacitivă» și C «suma XL + XC» folosind **La rezonanță RLC serie impedanța este R**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **La rezonanță RLC serie impedanța este R** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-072 | AU-25904764f6d9f3ad
- sha256 25904764f6d9f3ad16b632297e63e9b57802543bfdcfdcb5129363806f3d53c5; member_ids G2-ELEC-072; imported key {"G2-ELEC-072":"A"} păstrată.
- **Original:** Legea lui Ohm pentru o porțiune de circuit poate fi exprimată ca: 
  - A. U = R·I
  - B. U = R/I
  - C. U = I/R
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law; **Pentru element ohmic U=R·I**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Pentru element ohmic U=R·I**. A corespunde intenției importate, potrivit motivului: Legea lui Ohm a rezistorului U=RI.. B nu se potrivește deoarece R/I are unitate Ω/A, nu V.. C nu se potrivește deoarece I/R are unitate A/Ω, nu V.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Legea lui Ohm a rezistorului U=RI.; B R/I are unitate Ω/A, nu V.; C I/R are unitate A/Ω, nu V..
- **Orizontal ABC:** A «U = R·I» se compară cu B «U = R/I» și C «U = I/R» folosind **Pentru element ohmic U=R·I**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Pentru element ohmic U=R·I** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-073 | AU-fcfc9c7a54a49ad4
- sha256 fcfc9c7a54a49ad41fdaea0440a96e693fe735efcd1e023c6c8537a13f911abb; member_ids G2-ELEC-073; imported key {"G2-ELEC-073":"A"} păstrată.
- **Original:** Într-un circuit cu rezistențe în serie, curentul este: 
  - A. același prin toate rezistențele
  - B. zero prin prima rezistență
  - C. diferit în mod obligatoriu prin fiecare rezistență
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel; **Rezistențele în serie au același curent**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Rezistențele în serie au același curent**. A corespunde intenției importate, potrivit motivului: Curentul prin toate rezistențele serie este același, fără ramificații.. B nu se potrivește deoarece Curentul nu este automat zero la prima rezistență într-un circuit închis alimentat.. C nu se potrivește deoarece Curentul nu este obligatoriu diferit între rezistențe serie.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Curentul prin toate rezistențele serie este același, fără ramificații.; B Curentul nu este automat zero la prima rezistență într-un circuit închis alimentat.; C Curentul nu este obligatoriu diferit între rezistențe serie..
- **Orizontal ABC:** A «același prin toate rezistențele» se compară cu B «zero prin prima rezistență» și C «diferit în mod obligatoriu prin fiecare rezistență» folosind **Rezistențele în serie au același curent**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Rezistențele în serie au același curent** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-074 | AU-40fbe06c583b55a8
- sha256 40fbe06c583b55a8c9dab82896b99cf18d88626bea17905ad14b5bf7ec1a5f12; member_ids G2-ELEC-074; imported key {"G2-ELEC-074":"A"} păstrată.
- **Original:** Într-o conexiune paralelă ideală, tensiunea pe ramuri este: 
  - A. aceeași
  - B. întotdeauna zero
  - C. diferită în mod obligatoriu
- **Sursa/locator:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel; **Ramurile în paralel au aceeași tensiune**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Ramurile în paralel au aceeași tensiune**. A corespunde intenției importate, potrivit motivului: Două ramuri între aceleași noduri au aceeași diferență de potențial.. B nu se potrivește deoarece Tensiunea comună nu este întotdeauna zero.. C nu se potrivește deoarece Tensiunile ramurilor nu pot fi obligatoriu diferite dacă nodurile sunt aceleași.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Două ramuri între aceleași noduri au aceeași diferență de potențial.; B Tensiunea comună nu este întotdeauna zero.; C Tensiunile ramurilor nu pot fi obligatoriu diferite dacă nodurile sunt aceleași..
- **Orizontal ABC:** A «aceeași» se compară cu B «întotdeauna zero» și C «diferită în mod obligatoriu» folosind **Ramurile în paralel au aceeași tensiune**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Ramurile în paralel au aceeași tensiune** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-ELEC-075 | AU-2186c1a0e2ee0429
- sha256 2186c1a0e2ee0429b5128ee08ed2c75758cd0ad5b441d7ff060781334cfb1c5e; member_ids G2-ELEC-075; imported key {"G2-ELEC-075":"A"} păstrată.
- **Original:** Puterea activă într-un circuit monofazat sinusoidal poate fi exprimată prin: 
  - A. P = U·I·cosφ
  - B. P = U/I
  - C. P = U·I·sinφ în orice circuit
- **Sursa/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; **Puterea activă monofazată P=UI cosφ în regim sinusoidal**; SOURCE_FAMILY_TEXT_REOPENED.
- **Context:** Formula/definiția relevantă pentru obiectul întrebării este **Puterea activă monofazată P=UI cosφ în regim sinusoidal**. A corespunde intenției importate, potrivit motivului: Pentru sinusoidal monofazat P=U_ef I_ef cosφ.. B nu se potrivește deoarece U/I este impedanță, nu putere.. C nu se potrivește deoarece UI sinφ definește Q în model sinusoidal, nu P în orice circuit.. Limitările enunțului includ regimul ideal, factorul de putere, condițiile de conectare și semnificația unităților. Pentru aparate și siguranță, informația este conceptuală, nu procedură de intervenție în instalație.
- **Vertical ABC:** A Pentru sinusoidal monofazat P=U_ef I_ef cosφ.; B U/I este impedanță, nu putere.; C UI sinφ definește Q în model sinusoidal, nu P în orice circuit..
- **Orizontal ABC:** A «P = U·I·cosφ» se compară cu B «P = U/I» și C «P = U·I·sinφ în orice circuit» folosind **Puterea activă monofazată P=UI cosφ în regim sinusoidal**. B↔C sunt două afirmații alternative, cu valori/mărimi ori regim diferit; eliminarea lor nu înlocuiește verificarea pozitivă a lui A.
- **Reversie:** Dacă se schimbă ipoteza din **Puterea activă monofazată P=UI cosφ în regim sinusoidal** (element ideal, rețea echilibrată, sursă sinusoidală, conexiuni), verdictul poate să nu se păstreze; demonstrația nu trebuie extrapolată.
- **Status:** A_SOURCE_CONTEXT_PRELIMINARY; OFFICIAL_EXAM_STEM_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## Negative și follow-up
- G2-ELEC056: armonici de ordin triplu pot traversa conductorul neutru chiar în condiții de simetrie a componentelor fundamentale; nu generalizați curentul nul.
- G2-ELEC070–071: rezonanța serie necesită XL=XC, Z=R, nu rezistență infinită.
- G2-ELEC063 este deja creditat în CKPT080, nu e recreditat.
- Până la aprobarea finală: verificați exact ediția, original XLSX sau originea didactică, QA independent și sursa pentru instrumente.
