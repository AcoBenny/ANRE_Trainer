# CKPT-095 | P1 G2-LEG112–119, Cod tehnic distribuție și standard performanță | 2026-11-17

## Identitate, sursă, limite
- Branch audit/anre-v8-priority-17-20261109, PR #7 Draft/unmerged; HEAD înaintea scrierii 0a01c1d0b7af1b64d4ed8f201191108d8899c317. Baseline CKPT094 **268/568 unități, 323/822 ID-uri**; 8 P1 noi și 8 ID-uri => **276/568 unități, 331/822 ID-uri** contextual documentate. **0/822 learner-approved**.
- Sursă primară oficială ANRE bibliografie 05.2023, tabel **pagina 2**, pozițiile **7 și 8**, coloana grad **II=DA**, acces PDF și screenshot efectiv verificat. https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf. Nu declarăm o ediție 2026 diferită de cea publicată. Nu certificăm enunțurile G2-LEG ca fiind întrebări oficiale, chiar dacă conținutul listei este oficial.
- QABC/sha256/keys citite direct din MASTER_UNIT_CARDS_568.csv, fara mutație. Analiză vertical/orizontal/reversie, dar **fără reviewer independent**. Atenție la categoria «Legislație» a codurilor/standardelor în tabel, chiar dacă titlul documentului conține «tehnic».

## G2-LEG-112 | AU-17496b27825e8329
- id G2-LEG-112; hash 17496b27825e832949c79bece1aee56e0073b3536eb7fcc96927ebf14e7cd567; barem neschimbat {"G2-LEG-112":"A"}
- **Întrebare originală:** Care este documentul indicat de ANRE la punctul 7 pentru tematica Gradului II?
  - A. Ordinul ANRE nr. 128/2008
  - B. Ordinul ANRE nr. 20/2004
  - C. Ordinul ANRE nr. 103/2015
- **Sursă exactă:** ANRE 05.2023 p.2, rând 7 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** Punctul 7 din tabel identifică **Codul tehnic al rețelelor electrice de distribuție**, act aprobat prin **Ordin ANRE 128/2008**. Întrebarea spune «documentul indicat», dar A oferă **ordinul aprobator**, nu titlul actului tehnic; răspunsul A corespunde numai intenției referirii la coloana aprobatoare. Ordin ANRE 20/2004 aprobă codul tehnic al rețelei **de transport** (poziția 5), Grad II NU. Ordin ANRE 103/2015 aprobă Codul de **măsurare** (poziția 9), Grad II NU.
- **Vertical ABC:** A «Ordinul ANRE nr. 128/2008» este actul din rândul 7; B «Ordinul ANRE nr. 20/2004» și C «Ordinul ANRE nr. 103/2015» sunt alte acte pentru alte obiecte. Enunțul are TYPE_MISMATCH document-vs-ordin.
- **Orizontal ABC:** A↔B și A↔C: actul aprobator pentru obiectul rândului vs acte pentru alte documente; B↔C: cele două distrageri au alt obiect și alt rând.
- **Control invers/contraexemplu:** Schimbarea în analiză a enunțului în «care este ordinul aprobator» ar produce A exact, însă enunțul original «care este documentul» nu este reparat; rămâne avertismentul semantic.
- **Stare:** A_INTENDED_OFFICIAL_ROW_ACT__STEM_DOCUMENT_TYPE_MISMATCH; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## G2-LEG-113 | AU-730d5f7e6a9cadf6
- id G2-LEG-113; hash 730d5f7e6a9cadf6eff39a260b1e2ecea071956e17b765764569447fd33cb951; barem neschimbat {"G2-LEG-113":"A"}
- **Întrebare originală:** Prin ce act este aprobat documentul „Codul tehnic al rețelelor electrice de distribuție”, conform bibliografiei ANRE?
  - A. Ordinul ANRE nr. 128/2008
  - B. Ordinul ANRE nr. 20/2004
  - C. Ordinul ANRE nr. 103/2015
- **Sursă exactă:** ANRE 05.2023 p.2, rând 7 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** Documentul Codul tehnic al rețelelor electrice de distribuție este aprobat prin **Ordin ANRE 128/2008**, conform coloanei oficiale din rândul 7. Ordin ANRE 20/2004 aprobă codul tehnic al rețelei **de transport** (poziția 5), Grad II NU. Ordin ANRE 103/2015 aprobă Codul de **măsurare** (poziția 9), Grad II NU. În acest item, spre deosebire de cel anterior, enunțul întreabă explicit **«Prin ce act este aprobat»**, deci categoria răspunsului A este corectă.
- **Vertical ABC:** A «Ordinul ANRE nr. 128/2008»: act aprobator direct; B «Ordinul ANRE nr. 20/2004»: alt act; C «Ordinul ANRE nr. 103/2015»: alt act.
- **Orizontal ABC:** A↔B exact obiectul aprobat vs altă reglementare; A↔C obiectul din titlu vs alt obiect; B↔C numere diferite, dar niciunul nu aprobă documentul cerut.
- **Control invers/contraexemplu:** Din titlu spre coloana «Document aprobat prin» rezultă Ordin ANRE 128/2008; invers din numărul Ordin ANRE 128/2008 spre denumire revine același Codul tehnic al rețelelor electrice de distribuție.
- **Stare:** A_DIRECT_OFFICIAL_APPROVAL_2023; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## G2-LEG-114 | AU-333bfeb8d96dc48f
- id G2-LEG-114; hash 333bfeb8d96dc48f36ee2f5d0c3c95e0169f410114213e4f0ef2a7a134dcb18c; barem neschimbat {"G2-LEG-114":"A"}
- **Întrebare originală:** Este „Codul tehnic al rețelelor electrice de distribuție” inclus în bibliografia aplicabilă Gradului II?
  - A. Da
  - B. Nu
  - C. Doar pentru Gradele III și IV
- **Sursă exactă:** ANRE 05.2023 p.2, rând 7 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** În poziția 7, «Codul tehnic al rețelelor electrice de distribuție» are marcaj **DA** pentru gradul **II**. Rândul este din bibliografia 05.2023 și indică DA și pentru celelalte grade din tabel. C «Doar pentru Gradele III și IV» ar necesita NU la II, ceea ce este contrazis în document; B «Nu» contrazice direct celula.
- **Vertical ABC:** A «Da»: DA conform grad II; B «Nu»: fals, celula II este DA; C «Doar pentru Gradele III și IV»: fals din cauza exclusivității pentru III/IV.
- **Orizontal ABC:** A↔B DA/NU, antagonice; A↔C DA pentru II vs III/IV exclusiv; B↔C două moduri greșite de excludere a II.
- **Control invers/contraexemplu:** Pagină 2, coloana «II»: DA. Test negativ: C presupune celulă II=NU, dar screenshotul ANRE arată DA.
- **Stare:** A_OFFICIAL_2023_GRADE_II_DA; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## G2-LEG-115 | AU-36a9dca64afba294
- id G2-LEG-115; hash 36a9dca64afba29484ac5b2a68722a0b8b9fcd31c9fb8abd24403c2d900d03db; barem neschimbat {"G2-LEG-115":"A"}
- **Întrebare originală:** În ce domeniu tematic este încadrat „Codul tehnic al rețelelor electrice de distribuție” în bibliografia ANRE?
  - A. Legislație
  - B. Electrotehnică
  - C. Măsurări electrice
- **Sursă exactă:** ANRE 05.2023 p.2, rând 7 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** Documentul Codul tehnic al rețelelor electrice de distribuție apare la domeniul tematic **«Legislație»**, în rândul 7 al tabelului ANRE. Nu se clasifică la «Electrotehnică», deși descrie rețele electrice, deoarece criteriul întrebării este **clasificarea tabelară**. «Măsurări electrice» este o disciplină tehnică, nu eticheta acestei poziții.
- **Vertical ABC:** A «Legislație»: categorie din tabel; B «Electrotehnică»: alt domeniu tehnic; C «Măsurări electrice»: alt domeniu.
- **Orizontal ABC:** A↔B legal-reglementar vs discipline de electrotehnică; A↔C legal vs măsurări; B↔C două discipline tehnice nealese pentru rândul în cauză.
- **Control invers/contraexemplu:** Faptul că titlul include «Cod tehnic» nu face domeniul «Electrotehnică»; se citește celula categoriei din prima coloană, nu se deduce din titlu.
- **Stare:** A_OFFICIAL_2023_DOMAIN_LEGISLATIE; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## G2-LEG-116 | AU-d271456d74d12d42
- id G2-LEG-116; hash d271456d74d12d42cec0ac9847e758f7918af397355f7ca6a3a6bdca54c0810a; barem neschimbat {"G2-LEG-116":"A"}
- **Întrebare originală:** Care este documentul indicat de ANRE la punctul 8 pentru tematica Gradului II?
  - A. Ordinul ANRE nr. 46/2021
  - B. Ordinul ANRE nr. 12/2016
  - C. Ordinul ANRE nr. 103/2015
- **Sursă exactă:** ANRE 05.2023 p.2, rând 8 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** Punctul 8 din tabel identifică **Standardul de performanță pentru serviciul de distribuție a energiei electrice**, act aprobat prin **Ordin ANRE 46/2021**. Întrebarea spune «documentul indicat», dar A oferă **ordinul aprobator**, nu titlul actului tehnic; răspunsul A corespunde numai intenției referirii la coloana aprobatoare. Ordin ANRE 12/2016 este standardul pentru serviciul de **transport și sistem** (rândul 6), cu Grad II NU. Ordin ANRE 103/2015 privește **Codul de măsurare** (rândul 9), cu Grad II NU.
- **Vertical ABC:** A «Ordinul ANRE nr. 46/2021» este actul din rândul 8; B «Ordinul ANRE nr. 12/2016» și C «Ordinul ANRE nr. 103/2015» sunt alte acte pentru alte obiecte. Enunțul are TYPE_MISMATCH document-vs-ordin.
- **Orizontal ABC:** A↔B și A↔C: actul aprobator pentru obiectul rândului vs acte pentru alte documente; B↔C: cele două distrageri au alt obiect și alt rând.
- **Control invers/contraexemplu:** Schimbarea în analiză a enunțului în «care este ordinul aprobator» ar produce A exact, însă enunțul original «care este documentul» nu este reparat; rămâne avertismentul semantic.
- **Stare:** A_INTENDED_OFFICIAL_ROW_ACT__STEM_DOCUMENT_TYPE_MISMATCH; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## G2-LEG-117 | AU-fbfa68e55000c35c
- id G2-LEG-117; hash fbfa68e55000c35c6896bcaef39f308a58d4b735a3c8e4474897e64ecb6cea8a; barem neschimbat {"G2-LEG-117":"A"}
- **Întrebare originală:** Prin ce act este aprobat documentul „Standardul de performanță pentru serviciul de distribuție a energiei electrice”, conform bibliografiei ANRE?
  - A. Ordinul ANRE nr. 46/2021
  - B. Ordinul ANRE nr. 12/2016
  - C. Ordinul ANRE nr. 103/2015
- **Sursă exactă:** ANRE 05.2023 p.2, rând 8 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** Documentul Standardul de performanță pentru serviciul de distribuție a energiei electrice este aprobat prin **Ordin ANRE 46/2021**, conform coloanei oficiale din rândul 8. Ordin ANRE 12/2016 este standardul pentru serviciul de **transport și sistem** (rândul 6), cu Grad II NU. Ordin ANRE 103/2015 privește **Codul de măsurare** (rândul 9), cu Grad II NU. În acest item, spre deosebire de cel anterior, enunțul întreabă explicit **«Prin ce act este aprobat»**, deci categoria răspunsului A este corectă.
- **Vertical ABC:** A «Ordinul ANRE nr. 46/2021»: act aprobator direct; B «Ordinul ANRE nr. 12/2016»: alt act; C «Ordinul ANRE nr. 103/2015»: alt act.
- **Orizontal ABC:** A↔B exact obiectul aprobat vs altă reglementare; A↔C obiectul din titlu vs alt obiect; B↔C numere diferite, dar niciunul nu aprobă documentul cerut.
- **Control invers/contraexemplu:** Din titlu spre coloana «Document aprobat prin» rezultă Ordin ANRE 46/2021; invers din numărul Ordin ANRE 46/2021 spre denumire revine același Standardul de performanță pentru serviciul de distribuție a energiei electrice.
- **Stare:** A_DIRECT_OFFICIAL_APPROVAL_2023; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## G2-LEG-118 | AU-2d66be93f028f2f7
- id G2-LEG-118; hash 2d66be93f028f2f7c8bd28ac2f91c9cd503fcada342cbfbb160ba6e5e881102b; barem neschimbat {"G2-LEG-118":"A"}
- **Întrebare originală:** Este „Standardul de performanță pentru serviciul de distribuție a energiei electrice” inclus în bibliografia aplicabilă Gradului II?
  - A. Da
  - B. Nu
  - C. Doar pentru Gradele III și IV
- **Sursă exactă:** ANRE 05.2023 p.2, rând 8 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** În poziția 8, «Standardul de performanță pentru serviciul de distribuție a energiei electrice» are marcaj **DA** pentru gradul **II**. Rândul este din bibliografia 05.2023 și indică DA și pentru celelalte grade din tabel. C «Doar pentru Gradele III și IV» ar necesita NU la II, ceea ce este contrazis în document; B «Nu» contrazice direct celula.
- **Vertical ABC:** A «Da»: DA conform grad II; B «Nu»: fals, celula II este DA; C «Doar pentru Gradele III și IV»: fals din cauza exclusivității pentru III/IV.
- **Orizontal ABC:** A↔B DA/NU, antagonice; A↔C DA pentru II vs III/IV exclusiv; B↔C două moduri greșite de excludere a II.
- **Control invers/contraexemplu:** Pagină 2, coloana «II»: DA. Test negativ: C presupune celulă II=NU, dar screenshotul ANRE arată DA.
- **Stare:** A_OFFICIAL_2023_GRADE_II_DA; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## G2-LEG-119 | AU-b4b00c4c0675527b
- id G2-LEG-119; hash b4b00c4c0675527b37b5f36ad99998b5ac7cad96462ee79ebed8926ccd760099; barem neschimbat {"G2-LEG-119":"A"}
- **Întrebare originală:** În ce domeniu tematic este încadrat „Standardul de performanță pentru serviciul de distribuție a energiei electrice” în bibliografia ANRE?
  - A. Legislație
  - B. Electrotehnică
  - C. Măsurări electrice
- **Sursă exactă:** ANRE 05.2023 p.2, rând 8 și coloanele «Document aprobat prin», «Domeniu», «Aplicabilitate II»; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context:** Documentul Standardul de performanță pentru serviciul de distribuție a energiei electrice apare la domeniul tematic **«Legislație»**, în rândul 8 al tabelului ANRE. Nu se clasifică la «Electrotehnică», deși descrie rețele electrice, deoarece criteriul întrebării este **clasificarea tabelară**. «Măsurări electrice» este o disciplină tehnică, nu eticheta acestei poziții.
- **Vertical ABC:** A «Legislație»: categorie din tabel; B «Electrotehnică»: alt domeniu tehnic; C «Măsurări electrice»: alt domeniu.
- **Orizontal ABC:** A↔B legal-reglementar vs discipline de electrotehnică; A↔C legal vs măsurări; B↔C două discipline tehnice nealese pentru rândul în cauză.
- **Control invers/contraexemplu:** Faptul că titlul include «Cod tehnic» nu face domeniul «Electrotehnică»; se citește celula categoriei din prima coloană, nu se deduce din titlu.
- **Stare:** A_OFFICIAL_2023_DOMAIN_LEGISLATIE; INDEPENDENT_QA_NOT_RUN; PROVENANCE_AS_OFFICIAL_EXAM_QUESTION_UNVERIFIED; NO_LEARNER_APPROVAL.

## QA și poartă
- Distincție expresă: rândul 5 cod transport (20/2004) și rândul 6 standard transport (12/2016) Grad II NU; rândurile 7 cod distribuție (128/2008) și 8 standard distribuție (46/2021) Grad II DA. Comparație cu poziția 9 Cod măsurare (103/2015) Grad II NU.
- Răspunsurile importate sunt toate A, dar aceasta poate proveni din poziționarea pedagogică a opțiunilor, nu certificare de bancă oficială. Control de proveniență XLSX + QA independent înainte de orice learner approval.
- Fără bareme/HTML/APK/CSV master/main/merge/release.
