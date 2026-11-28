# CKPT-104 | 20 P2 Grad II: AC, puteri, trifazat, transformatoare, mașini | 2026-11-17

## Unicitate, dovezi, limitări
- Cumul anterior CKPT103 **322/568 unități, 402/822 ID-uri**. Acest lot +20 P2 unice și 20 grade IDs: **342/568, 422/822**; **226 unități P2 restante**, **0/822 learner-approved**.
- Surse efectiv redeschise textual în această sesiune: OpenStax vol.2 §15.2, §15.6, §13.6; Schneider Electric Installation Guide «Definition of reactive power» și All About Circuits «Three-phase Y/Delta Configurations». Folosim modelul specific fiecărei grile și antecedente DEEP_ELE_15/16 ca ipoteze tehnice, nu ca QA independent.
- Proveniența întrebărilor ca grile oficiale ANRE rămâne **neconfirmată**, inclusiv tiparul celor 20 chei A. Datele canonice QABC și cheile nu s-au modificat, fără HTML/APK/main/merge. Independent technical/source/linguistic QA NOT_RUN.

## G2-ELEC-012 | AU-a5ee067dbb030ef7
- qabc_sha256 a5ee067dbb030ef7b82ce91ece68b108ea6b5fcb81fb717f443065222aefb45d; member_ids G2-ELEC-012; barem importat {"G2-ELEC-012":"A"} (neschimbat).
- **Enunț original:** Perioada T și frecvența f sunt legate prin:
  - A. T = 1/f
  - B. T = f
  - C. T = f²
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits; concept exact de verificat: **T=1/f, f>0; 50 Hz => 20 ms**.
- **Context 5–6 propoziții:** Întrebarea testează perioada t și frecvența f sunt legate prin. Modelul didactic corespondent este **T=1/f, f>0; 50 Hz => 20 ms**. Varianta A corespunde intenției pozitive întrucât T=1/f pentru orice fenomen periodic cu f nenul.. B nu descrie obiectul cerut, deoarece T=f inversează impropriu perioadă și frecvență; unități s versus Hz.. C diferă de valoarea sau regimul din model, deoarece T=f² dă unități Hz², nu secunde.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: T=1/f pentru orice fenomen periodic cu f nenul.; B: T=f inversează impropriu perioadă și frecvență; unități s versus Hz.; C: T=f² dă unități Hz², nu secunde..
- **Orizontal:** A («T = 1/f») versus B («T = f») și A versus C («T = f²») se verifică prin T=1/f, f>0; 50 Hz => 20 ms; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **T=1/f, f>0; 50 Hz => 20 ms** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-013 | AU-436f2b6e1f77709d
- qabc_sha256 436f2b6e1f77709de242c69e1800f4f288cdd8618435ca9043076d44a66a47b6; member_ids G2-ELEC-013; barem importat {"G2-ELEC-013":"A"} (neschimbat).
- **Enunț original:** Valoarea efectivă a unei tensiuni sinusoidale este folosită pentru:
  - A. evaluarea efectului echivalent în regim energetic/termic
  - B. determinarea directă a frecvenței
  - C. înlocuirea rezistenței
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits; concept exact de verificat: **RMS² este media pătratului tensiunii; 325V vârf => circa 230V eficace**.
- **Context 5–6 propoziții:** Întrebarea testează valoarea efectivă a unei tensiuni sinusoidale este folosită pentru. Modelul didactic corespondent este **RMS² este media pătratului tensiunii; 325V vârf => circa 230V eficace**. Varianta A corespunde intenției pozitive întrucât RMS indică tensiunea CC ce produce același efect Joule într-o rezistență.. B nu descrie obiectul cerut, deoarece Frecvența ține de perioada temporală, nu se deduce dintr-un singur RMS.. C diferă de valoarea sau regimul din model, deoarece Valoarea RMS nu înlocuiește rezistența ohmică a unui receptor.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: RMS indică tensiunea CC ce produce același efect Joule într-o rezistență.; B: Frecvența ține de perioada temporală, nu se deduce dintr-un singur RMS.; C: Valoarea RMS nu înlocuiește rezistența ohmică a unui receptor..
- **Orizontal:** A («evaluarea efectului echivalent în regim energetic/termic») versus B («determinarea directă a frecvenței») și A versus C («înlocuirea rezistenței») se verifică prin RMS² este media pătratului tensiunii; 325V vârf => circa 230V eficace; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **RMS² este media pătratului tensiunii; 325V vârf => circa 230V eficace** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-014 | AU-aa722f26d4d9202e
- qabc_sha256 aa722f26d4d9202ee2cb726058226449f81e80d43df60358a4534d9f34a91502; member_ids G2-ELEC-014; barem importat {"G2-ELEC-014":"A"} (neschimbat).
- **Enunț original:** Într-un circuit pur rezistiv de c.a., defazajul dintre tensiune și curent este:
  - A. 0°
  - B. 90°
  - C. 180°
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits; concept exact de verificat: **Rezistor pur i=u/R, φ=0**.
- **Context 5–6 propoziții:** Întrebarea testează într-un circuit pur rezistiv de c.a., defazajul dintre tensiune și curent este. Modelul didactic corespondent este **Rezistor pur i=u/R, φ=0**. Varianta A corespunde intenției pozitive întrucât La rezistor pur, U și I variază în fază, deci 0°.. B nu descrie obiectul cerut, deoarece 90° corespunde unui element reactiv ideal, nu rezistorului.. C diferă de valoarea sau regimul din model, deoarece 180° ar însemna opoziție de fază, absentă sub convenția pasivă.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: La rezistor pur, U și I variază în fază, deci 0°.; B: 90° corespunde unui element reactiv ideal, nu rezistorului.; C: 180° ar însemna opoziție de fază, absentă sub convenția pasivă..
- **Orizontal:** A («0°») versus B («90°») și A versus C («180°») se verifică prin Rezistor pur i=u/R, φ=0; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Rezistor pur i=u/R, φ=0** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-015 | AU-2710f090e7274001
- qabc_sha256 2710f090e7274001afc83a4ce6f51ea6cea2fa41fdb50bed78b0de9936336f0a; member_ids G2-ELEC-015; barem importat {"G2-ELEC-015":"A"} (neschimbat).
- **Enunț original:** Într-o bobină ideală, curentul este în urmă față de tensiune cu:
  - A. 90°
  - B. 0°
  - C. 180°
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits; concept exact de verificat: **Inductor ideal u=L·di/dt; curentul întârzie 90°**.
- **Context 5–6 propoziții:** Întrebarea testează într-o bobină ideală, curentul este în urmă față de tensiune cu. Modelul didactic corespondent este **Inductor ideal u=L·di/dt; curentul întârzie 90°**. Varianta A corespunde intenției pozitive întrucât Pentru bobină ideală U=L·dI/dt, curentul întârzie cu 90°.. B nu descrie obiectul cerut, deoarece 0° ar indica element rezistiv, nu inductiv ideal.. C diferă de valoarea sau regimul din model, deoarece 180° nu descrie integrarea sinusoidală din inductanța ideală.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Pentru bobină ideală U=L·dI/dt, curentul întârzie cu 90°.; B: 0° ar indica element rezistiv, nu inductiv ideal.; C: 180° nu descrie integrarea sinusoidală din inductanța ideală..
- **Orizontal:** A («90°») versus B («0°») și A versus C («180°») se verifică prin Inductor ideal u=L·di/dt; curentul întârzie 90°; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Inductor ideal u=L·di/dt; curentul întârzie 90°** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-016 | AU-331686af928349af
- qabc_sha256 331686af928349af1168934605c9de20d1dd4af35ce6982197c9efe761d79b9e; member_ids G2-ELEC-016; barem importat {"G2-ELEC-016":"A"} (neschimbat).
- **Enunț original:** Într-un condensator ideal, curentul este înaintea tensiunii cu:
  - A. 90°
  - B. 0°
  - C. 180°
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits; concept exact de verificat: **Condensator ideal i=C·du/dt; curentul precede 90°**.
- **Context 5–6 propoziții:** Întrebarea testează într-un condensator ideal, curentul este înaintea tensiunii cu. Modelul didactic corespondent este **Condensator ideal i=C·du/dt; curentul precede 90°**. Varianta A corespunde intenției pozitive întrucât Condensator ideal I=C·dU/dt, curentul precede tensiunea cu 90°.. B nu descrie obiectul cerut, deoarece 0° descrie relația rezistivă, nu capacitivă ideală.. C diferă de valoarea sau regimul din model, deoarece 180° nu este defazajul unui condensator pasiv ideal.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Condensator ideal I=C·dU/dt, curentul precede tensiunea cu 90°.; B: 0° descrie relația rezistivă, nu capacitivă ideală.; C: 180° nu este defazajul unui condensator pasiv ideal..
- **Orizontal:** A («90°») versus B («0°») și A versus C («180°») se verifică prin Condensator ideal i=C·du/dt; curentul precede 90°; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Condensator ideal i=C·du/dt; curentul precede 90°** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-017 | AU-c55dba0aaf6e588f
- qabc_sha256 c55dba0aaf6e588ff379a3652f5b612bfcd179d94a516afa2aad602fade80101; member_ids G2-ELEC-017; barem importat {"G2-ELEC-017":"A"} (neschimbat).
- **Enunț original:** Reactanța inductivă a unei bobine ideale este:
  - A. XL = 2πfL
  - B. XL = 1/(2πfL)
  - C. XL = R/I
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits; concept exact de verificat: **XL=2πfL; XL crește cu frecvența**.
- **Context 5–6 propoziții:** Întrebarea testează reactanța inductivă a unei bobine ideale este. Modelul didactic corespondent este **XL=2πfL; XL crește cu frecvența**. Varianta A corespunde intenției pozitive întrucât Din u=L di/dt rezultă |X_L|=ωL=2πfL.. B nu descrie obiectul cerut, deoarece 1/(2πfL) are dimensiune inversă și nu este reactanța inductivă.. C diferă de valoarea sau regimul din model, deoarece R/I nu exprimă Ω pentru datele din această formulă.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Din u=L di/dt rezultă |X_L|=ωL=2πfL.; B: 1/(2πfL) are dimensiune inversă și nu este reactanța inductivă.; C: R/I nu exprimă Ω pentru datele din această formulă..
- **Orizontal:** A («XL = 2πfL») versus B («XL = 1/(2πfL)») și A versus C («XL = R/I») se verifică prin XL=2πfL; XL crește cu frecvența; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **XL=2πfL; XL crește cu frecvența** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-018 | AU-d73a70d833fb0f04
- qabc_sha256 d73a70d833fb0f044a649c79938209e1c79b4f7c0b4a7b18007066c73881ded5; member_ids G2-ELEC-018; barem importat {"G2-ELEC-018":"A"} (neschimbat).
- **Enunț original:** Reactanța capacitivă este:
  - A. XC = 1/(2πfC)
  - B. XC = 2πfC
  - C. XC = R·C
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits; concept exact de verificat: **XC=1/(2πfC); XC descrește cu frecvența**.
- **Context 5–6 propoziții:** Întrebarea testează reactanța capacitivă este. Modelul didactic corespondent este **XC=1/(2πfC); XC descrește cu frecvența**. Varianta A corespunde intenției pozitive întrucât Din i=C du/dt, |X_C|=1/(ωC)=1/(2πfC).. B nu descrie obiectul cerut, deoarece 2πfC reprezintă susceptanța capacitivă în siemens, nu Ω.. C diferă de valoarea sau regimul din model, deoarece R·C este constantă de timp, nu reactanță.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Din i=C du/dt, |X_C|=1/(ωC)=1/(2πfC).; B: 2πfC reprezintă susceptanța capacitivă în siemens, nu Ω.; C: R·C este constantă de timp, nu reactanță..
- **Orizontal:** A («XC = 1/(2πfC)») versus B («XC = 2πfC») și A versus C («XC = R·C») se verifică prin XC=1/(2πfC); XC descrește cu frecvența; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **XC=1/(2πfC); XC descrește cu frecvența** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-019 | AU-c3d87c130955dad8
- qabc_sha256 c3d87c130955dad88268f55eede908896d5e93b89fb0231b64dfdb12d862a799; member_ids G2-ELEC-019; barem importat {"G2-ELEC-019":"A"} (neschimbat).
- **Enunț original:** Puterea aparentă într-un circuit monofazat este:
  - A. S = U·I
  - B. S = U/I
  - C. S = R·I
- **Sursă didactică/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; concept exact de verificat: **S=Urms·Irms în VA; 230V×10A=2300VA**.
- **Context 5–6 propoziții:** Întrebarea testează puterea aparentă într-un circuit monofazat este. Modelul didactic corespondent este **S=Urms·Irms în VA; 230V×10A=2300VA**. Varianta A corespunde intenției pozitive întrucât S=U_ef·I_ef exprimă puterea aparentă monofazată în VA.. B nu descrie obiectul cerut, deoarece U/I reprezintă impedanță, nu putere.. C diferă de valoarea sau regimul din model, deoarece R·I are dimensiune tensiune, nu putere.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: S=U_ef·I_ef exprimă puterea aparentă monofazată în VA.; B: U/I reprezintă impedanță, nu putere.; C: R·I are dimensiune tensiune, nu putere..
- **Orizontal:** A («S = U·I») versus B («S = U/I») și A versus C («S = R·I») se verifică prin S=Urms·Irms în VA; 230V×10A=2300VA; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **S=Urms·Irms în VA; 230V×10A=2300VA** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-020 | AU-9df87ebc9edda1c8
- qabc_sha256 9df87ebc9edda1c88d6eecfa4c8ea049da37784336a297602941c119c47aa7d7; member_ids G2-ELEC-020; barem importat {"G2-ELEC-020":"A"} (neschimbat).
- **Enunț original:** Unitatea puterii aparente este:
  - A. VA
  - B. W
  - C. var
- **Sursă didactică/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; concept exact de verificat: **Unitatea puterii aparente VA este distinctă de W/var**.
- **Context 5–6 propoziții:** Întrebarea testează unitatea puterii aparente este. Modelul didactic corespondent este **Unitatea puterii aparente VA este distinctă de W/var**. Varianta A corespunde intenției pozitive întrucât VA este unitatea uzuală distinctivă pentru puterea aparentă S.. B nu descrie obiectul cerut, deoarece W reprezintă putere activă P.. C diferă de valoarea sau regimul din model, deoarece var este folosit pentru putere reactivă Q.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: VA este unitatea uzuală distinctivă pentru puterea aparentă S.; B: W reprezintă putere activă P.; C: var este folosit pentru putere reactivă Q..
- **Orizontal:** A («VA») versus B («W») și A versus C («var») se verifică prin Unitatea puterii aparente VA este distinctă de W/var; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Unitatea puterii aparente VA este distinctă de W/var** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-021 | AU-c82a5f7f574d777f
- qabc_sha256 c82a5f7f574d777f0c5594f05a44e028b196e02b685c8b236f225c1e6e9649d5; member_ids G2-ELEC-021; barem importat {"G2-ELEC-021":"A"} (neschimbat).
- **Enunț original:** Puterea reactivă se exprimă în:
  - A. var
  - B. W
  - C. VAh
- **Sursă didactică/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; concept exact de verificat: **Unitatea puterii reactive este var; Q=UI sinφ**.
- **Context 5–6 propoziții:** Întrebarea testează puterea reactivă se exprimă în. Modelul didactic corespondent este **Unitatea puterii reactive este var; Q=UI sinφ**. Varianta A corespunde intenției pozitive întrucât var (volt-amper reactiv) identifică puterea reactivă Q.. B nu descrie obiectul cerut, deoarece W este unitatea puterii active.. C diferă de valoarea sau regimul din model, deoarece VAh măsoară integrarea în timp a puterii aparente, nu Q instantanee.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: var (volt-amper reactiv) identifică puterea reactivă Q.; B: W este unitatea puterii active.; C: VAh măsoară integrarea în timp a puterii aparente, nu Q instantanee..
- **Orizontal:** A («var») versus B («W») și A versus C («VAh») se verifică prin Unitatea puterii reactive este var; Q=UI sinφ; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Unitatea puterii reactive este var; Q=UI sinφ** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-022 | AU-d59694f35f3f3b0b
- qabc_sha256 d59694f35f3f3b0b478613991f12833ea79dd5afb0e1d523d0fd5a825625feaf; member_ids G2-ELEC-022; barem importat {"G2-ELEC-022":"A"} (neschimbat).
- **Enunț original:** Factorul de putere în regim sinusoidal este:
  - A. cos φ
  - B. sin φ
  - C. tan φ
- **Sursă didactică/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; concept exact de verificat: **Factorul de putere sinusoidal P/S=cosφ**.
- **Context 5–6 propoziții:** Întrebarea testează factorul de putere în regim sinusoidal este. Modelul didactic corespondent este **Factorul de putere sinusoidal P/S=cosφ**. Varianta A corespunde intenției pozitive întrucât În regim sinusoidal, factorul de putere activă/aparentă este cosφ.. B nu descrie obiectul cerut, deoarece sinφ intră în Q/S, nu în factorul de putere uzual.. C diferă de valoarea sau regimul din model, deoarece tanφ=Q/P, nu P/S.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: În regim sinusoidal, factorul de putere activă/aparentă este cosφ.; B: sinφ intră în Q/S, nu în factorul de putere uzual.; C: tanφ=Q/P, nu P/S..
- **Orizontal:** A («cos φ») versus B («sin φ») și A versus C («tan φ») se verifică prin Factorul de putere sinusoidal P/S=cosφ; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Factorul de putere sinusoidal P/S=cosφ** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-023 | AU-f410bd66742016b5
- qabc_sha256 f410bd66742016b530da889f6715d4199b542a9a491ed5e73bd6f96f6aaa26b1; member_ids G2-ELEC-023; barem importat {"G2-ELEC-023":"A"} (neschimbat).
- **Enunț original:** Pentru o sarcină pur rezistivă, factorul de putere este:
  - A. 1
  - B. 0
  - C. -1
- **Sursă didactică/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; concept exact de verificat: **Rezistor pur φ=0 => cosφ=1**.
- **Context 5–6 propoziții:** Întrebarea testează pentru o sarcină pur rezistivă, factorul de putere este. Modelul didactic corespondent este **Rezistor pur φ=0 => cosφ=1**. Varianta A corespunde intenției pozitive întrucât La sarcină pur rezistivă φ=0 și cosφ=1.. B nu descrie obiectul cerut, deoarece Factor de putere zero corespunde puterii active nule ideal reactive.. C diferă de valoarea sau regimul din model, deoarece −1 ar însemna flux activ în sens opus, nu consum rezistiv pasiv.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: La sarcină pur rezistivă φ=0 și cosφ=1.; B: Factor de putere zero corespunde puterii active nule ideal reactive.; C: −1 ar însemna flux activ în sens opus, nu consum rezistiv pasiv..
- **Orizontal:** A («1») versus B («0») și A versus C («-1») se verifică prin Rezistor pur φ=0 => cosφ=1; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Rezistor pur φ=0 => cosφ=1** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-024 | AU-bef8a9057dc7df39
- qabc_sha256 bef8a9057dc7df3934271cce076ef5529ce6e8f9bc0ac4e7704261c5b42e5aa9; member_ids G2-ELEC-024; barem importat {"G2-ELEC-024":"A"} (neschimbat).
- **Enunț original:** Într-un sistem trifazat echilibrat, suma vectorială a curenților de fază este:
  - A. zero
  - B. egală cu curentul de linie
  - C. întotdeauna 3 A
- **Sursă didactică/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; concept exact de verificat: **I∠0°+I∠120°+I∠240°=0 fazorial**.
- **Context 5–6 propoziții:** Întrebarea testează într-un sistem trifazat echilibrat, suma vectorială a curenților de fază este. Modelul didactic corespondent este **I∠0°+I∠120°+I∠240°=0 fazorial**. Varianta A corespunde intenției pozitive întrucât Pentru fazori egali defazați 120°, I1+I2+I3=0.. B nu descrie obiectul cerut, deoarece Suma vectorială a celor trei faze nu se reduce la un singur curent de linie nenul.. C diferă de valoarea sau regimul din model, deoarece 3A este o valoare arbitrară, independentă de amplitudini.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Pentru fazori egali defazați 120°, I1+I2+I3=0.; B: Suma vectorială a celor trei faze nu se reduce la un singur curent de linie nenul.; C: 3A este o valoare arbitrară, independentă de amplitudini..
- **Orizontal:** A («zero») versus B («egală cu curentul de linie») și A versus C («întotdeauna 3 A») se verifică prin I∠0°+I∠120°+I∠240°=0 fazorial; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **I∠0°+I∠120°+I∠240°=0 fazorial** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-025 | AU-2912241f8d2a9f2f
- qabc_sha256 2912241f8d2a9f2fd38e37d6c26991dfcc017e8e9dce214d99b134622de0b56d; member_ids G2-ELEC-025; barem importat {"G2-ELEC-025":"A"} (neschimbat).
- **Enunț original:** Pentru un sistem trifazat echilibrat, puterea activă se poate calcula cu:
  - A. P = √3·UL·IL·cosφ
  - B. P = UL/IL
  - C. P = 3·UL·IL
- **Sursă didactică/locator:** https://www.electrical-installation.org/enwiki/Definition_of_reactive_power; concept exact de verificat: **Trifazat echilibrat P=√3 Ulinie Ilinie cosφ**.
- **Context 5–6 propoziții:** Întrebarea testează pentru un sistem trifazat echilibrat, puterea activă se poate calcula cu. Modelul didactic corespondent este **Trifazat echilibrat P=√3 Ulinie Ilinie cosφ**. Varianta A corespunde intenției pozitive întrucât P=√3·U_L·I_L·cosφ în sistem trifazat echilibrat.. B nu descrie obiectul cerut, deoarece U_L/I_L are dimensiune impedanță, nu watt.. C diferă de valoarea sau regimul din model, deoarece 3U_LI_L omite cosφ și dublează conversia fază/linie.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: P=√3·U_L·I_L·cosφ în sistem trifazat echilibrat.; B: U_L/I_L are dimensiune impedanță, nu watt.; C: 3U_LI_L omite cosφ și dublează conversia fază/linie..
- **Orizontal:** A («P = √3·UL·IL·cosφ») versus B («P = UL/IL») și A versus C («P = 3·UL·IL») se verifică prin Trifazat echilibrat P=√3 Ulinie Ilinie cosφ; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Trifazat echilibrat P=√3 Ulinie Ilinie cosφ** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-026 | AU-003f1f386b038662
- qabc_sha256 003f1f386b03866203525d67b7fec1936e27cba0e5716916e3eb4ffeb0d85a35; member_ids G2-ELEC-026; barem importat {"G2-ELEC-026":"A"} (neschimbat).
- **Enunț original:** În conexiunea stea, tensiunea de linie este:
  - A. √3 ori tensiunea de fază
  - B. egală cu zero
  - C. jumătate din tensiunea de fază
- **Sursă didactică/locator:** https://www.allaboutcircuits.com/textbook/alternating-current/chpt-10/three-phase-y-delta-configurations/; concept exact de verificat: **Stea simetrică Ulinie=√3 Ufază**.
- **Context 5–6 propoziții:** Întrebarea testează în conexiunea stea, tensiunea de linie este. Modelul didactic corespondent este **Stea simetrică Ulinie=√3 Ufază**. Varianta A corespunde intenției pozitive întrucât La stea echilibrată, vectorii de fază la 120° dau U_L=√3·U_f.. B nu descrie obiectul cerut, deoarece U_L nu este nulă pentru sistem trifazat alimentat.. C diferă de valoarea sau regimul din model, deoarece Tensiunea de linie nu este jumătate din cea de fază.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: La stea echilibrată, vectorii de fază la 120° dau U_L=√3·U_f.; B: U_L nu este nulă pentru sistem trifazat alimentat.; C: Tensiunea de linie nu este jumătate din cea de fază..
- **Orizontal:** A («√3 ori tensiunea de fază») versus B («egală cu zero») și A versus C («jumătate din tensiunea de fază») se verifică prin Stea simetrică Ulinie=√3 Ufază; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Stea simetrică Ulinie=√3 Ufază** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-027 | AU-728feb33442fc437
- qabc_sha256 728feb33442fc4370abefb662f4de5eca3714d3cac17dc40e4b40fdeaad2caa7; member_ids G2-ELEC-027; barem importat {"G2-ELEC-027":"A"} (neschimbat).
- **Enunț original:** În conexiunea triunghi, tensiunea de linie este:
  - A. egală cu tensiunea de fază
  - B. √3 ori tensiunea de fază
  - C. jumătate din tensiunea de fază
- **Sursă didactică/locator:** https://www.allaboutcircuits.com/textbook/alternating-current/chpt-10/three-phase-y-delta-configurations/; concept exact de verificat: **Triunghi Ulinie=Ufază**.
- **Context 5–6 propoziții:** Întrebarea testează în conexiunea triunghi, tensiunea de linie este. Modelul didactic corespondent este **Triunghi Ulinie=Ufază**. Varianta A corespunde intenției pozitive întrucât În triunghi fiecare înfășurare este direct între două linii: U_L=U_f.. B nu descrie obiectul cerut, deoarece Factorul √3 se aplică tensiunii stea echilibrate, nu laturii triunghiului.. C diferă de valoarea sau regimul din model, deoarece U_L nu este jumătate din U_f în triunghi.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: În triunghi fiecare înfășurare este direct între două linii: U_L=U_f.; B: Factorul √3 se aplică tensiunii stea echilibrate, nu laturii triunghiului.; C: U_L nu este jumătate din U_f în triunghi..
- **Orizontal:** A («egală cu tensiunea de fază») versus B («√3 ori tensiunea de fază») și A versus C («jumătate din tensiunea de fază») se verifică prin Triunghi Ulinie=Ufază; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Triunghi Ulinie=Ufază** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-028 | AU-895f53655499e71b
- qabc_sha256 895f53655499e71b006e5f849bd24a8701883e56aa890ccb7a38697912b008b0; member_ids G2-ELEC-028; barem importat {"G2-ELEC-028":"A"} (neschimbat).
- **Enunț original:** Transformatorul electric funcționează pe baza:
  - A. inducției electromagnetice
  - B. efectului fotoelectric
  - C. efectului Hall exclusiv
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers; concept exact de verificat: **Transformatorul AC induce tensiune prin flux variabil; nu DC constant**.
- **Context 5–6 propoziții:** Întrebarea testează transformatorul electric funcționează pe baza. Modelul didactic corespondent este **Transformatorul AC induce tensiune prin flux variabil; nu DC constant**. Varianta A corespunde intenției pozitive întrucât Transformatorul se bazează pe flux magnetic variabil și inducția electromagnetică în secundar.. B nu descrie obiectul cerut, deoarece Efectul fotoelectric nu este principiul de conversie al transformatorului.. C diferă de valoarea sau regimul din model, deoarece Efectul Hall, cu atât mai puțin exclusiv, nu produce transferul inductiv.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Transformatorul se bazează pe flux magnetic variabil și inducția electromagnetică în secundar.; B: Efectul fotoelectric nu este principiul de conversie al transformatorului.; C: Efectul Hall, cu atât mai puțin exclusiv, nu produce transferul inductiv..
- **Orizontal:** A («inducției electromagnetice») versus B («efectului fotoelectric») și A versus C («efectului Hall exclusiv») se verifică prin Transformatorul AC induce tensiune prin flux variabil; nu DC constant; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Transformatorul AC induce tensiune prin flux variabil; nu DC constant** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-029 | AU-4734ee635228dc4e
- qabc_sha256 4734ee635228dc4e7ee4a88459dd4336f25728e8b87bd533264040958bdf24d0; member_ids G2-ELEC-029; barem importat {"G2-ELEC-029":"A"} (neschimbat).
- **Enunț original:** Într-un transformator ideal, raportul tensiunilor este egal cu raportul:
  - A. numărului de spire
  - B. rezistențelor de sarcină
  - C. frecvențelor
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers; concept exact de verificat: **Transformator ideal U2/U1=N2/N1**.
- **Context 5–6 propoziții:** Întrebarea testează într-un transformator ideal, raportul tensiunilor este egal cu raportul. Modelul didactic corespondent este **Transformator ideal U2/U1=N2/N1**. Varianta A corespunde intenției pozitive întrucât Pentru transformator ideal U1/U2=N1/N2 în regim sinusoidal.. B nu descrie obiectul cerut, deoarece Rezistențele sarcinilor nu stabilesc direct raportul nominal al tensiunilor.. C diferă de valoarea sau regimul din model, deoarece Frecvența este comună în ambele înfășurări în transformatorul ideal; raport f1/f2=1.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Pentru transformator ideal U1/U2=N1/N2 în regim sinusoidal.; B: Rezistențele sarcinilor nu stabilesc direct raportul nominal al tensiunilor.; C: Frecvența este comună în ambele înfășurări în transformatorul ideal; raport f1/f2=1..
- **Orizontal:** A («numărului de spire») versus B («rezistențelor de sarcină») și A versus C («frecvențelor») se verifică prin Transformator ideal U2/U1=N2/N1; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Transformator ideal U2/U1=N2/N1** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-031 | AU-22ce32685d81a384
- qabc_sha256 22ce32685d81a3849b3988e7d0aca7a0e32c100e46c4373c5e8dbf18d7cfbe34; member_ids G2-ELEC-031; barem importat {"G2-ELEC-031":"A"} (neschimbat).
- **Enunț original:** Motorul electric transformă în principal:
  - A. energia electrică în energie mecanică
  - B. energia mecanică în energie electrică exclusiv
  - C. energia termică în energie electrică
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/13-6-electric-generators-and-back-emf; concept exact de verificat: **Motor electric în regim motor: energie electrică în mecanică**.
- **Context 5–6 propoziții:** Întrebarea testează motorul electric transformă în principal. Modelul didactic corespondent este **Motor electric în regim motor: energie electrică în mecanică**. Varianta A corespunde intenției pozitive întrucât Motorul convertește energia electrică în lucru mecanic la arbore.. B nu descrie obiectul cerut, deoarece Conversia mecanică în electrică este funcția generatorului, nu exclusiv a motorului.. C diferă de valoarea sau regimul din model, deoarece Conversia termică în electrică nu este funcția dominantă a motorului.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Motorul convertește energia electrică în lucru mecanic la arbore.; B: Conversia mecanică în electrică este funcția generatorului, nu exclusiv a motorului.; C: Conversia termică în electrică nu este funcția dominantă a motorului..
- **Orizontal:** A («energia electrică în energie mecanică») versus B («energia mecanică în energie electrică exclusiv») și A versus C («energia termică în energie electrică») se verifică prin Motor electric în regim motor: energie electrică în mecanică; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Motor electric în regim motor: energie electrică în mecanică** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-ELEC-032 | AU-862299f3cc6cb15c
- qabc_sha256 862299f3cc6cb15c1b1ffbed72063a74d5d0c3f4dc0ce6b218cc57894ac5dfb6; member_ids G2-ELEC-032; barem importat {"G2-ELEC-032":"A"} (neschimbat).
- **Enunț original:** Generatorul electric transformă în principal:
  - A. energia mecanică în energie electrică
  - B. energia electrică în căldură
  - C. energia chimică în lumină
- **Sursă didactică/locator:** https://openstax.org/books/university-physics-volume-2/pages/13-6-electric-generators-and-back-emf; concept exact de verificat: **Generator clasic: energie mecanică în electrică**.
- **Context 5–6 propoziții:** Întrebarea testează generatorul electric transformă în principal. Modelul didactic corespondent este **Generator clasic: energie mecanică în electrică**. Varianta A corespunde intenției pozitive întrucât Generatorul transformă energia mecanică furnizată prin arbore în electrică.. B nu descrie obiectul cerut, deoarece Electric în căldură este disipare rezistivă, nu funcția generatorului.. C diferă de valoarea sau regimul din model, deoarece Conversia chimic în lumină nu este funcția generatorului.. Condiția specifică (AC sinusoidal, valori eficace, topologie Y/Δ, dispozitiv ideal ori regim motor/generator) nu se poate elimina fără verificare.
- **Vertical ABC:** A: Generatorul transformă energia mecanică furnizată prin arbore în electrică.; B: Electric în căldură este disipare rezistivă, nu funcția generatorului.; C: Conversia chimic în lumină nu este funcția generatorului..
- **Orizontal:** A («energia mecanică în energie electrică») versus B («energia electrică în căldură») și A versus C («energia chimică în lumină») se verifică prin Generator clasic: energie mecanică în electrică; comparația B versus C arată două erori diferite, nu o dovadă pozitivă de sine stătătoare.
- **Test invers/contraexemplu:** Înlocuirea valorii/condiției din modelul **Generator clasic: energie mecanică în electrică** printr-o conexiune, frecvență sau regim diferit poate schimba rezultatul. Cazul de referință original trebuie păstrat; opțiunile B/C nu corespund lui.
- **Stare:** POSITIVE_SOURCE_MODEL_MATCH_PRELIMINARY; ORIGINAL_ANRE_QUESTION_PROVENANCE_NOT_VERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## Regresie și următor
- «VA» puterea aparentă vs «W» activă vs «var» reactivă; √3 pentru stea versus tensiunea liniei egală fazei în Δ; curenți fazoriali versus module; transformatorul nu modifică frecvența.
- Cei 20 sunt carduri contextuale, nu certificări de cheie, de proveniență ori de ediție ANRE 2026. Recomandarea este segregarea grilelor didactice Grad II față de cele originale până la confirmare.
