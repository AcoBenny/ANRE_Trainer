# CKPT-096 | P1 G2-LEG120–127, autorizare electrician versus atestare operator | 2026-11-17

## Bază și surse
- Repo AcoBenny/ANRE_Trainer; branch audit/anre-v8-priority-17-20261109; PR #7 Open/Draft. Bază CKPT095 **276/568 unități, 331/822 ID-uri**. Lot de 8 noi P1 / 8 ID-uri => **284/568 unități, 339/822 ID-uri**, **0/822 approved for learning**.
- Document primar **ANRE 05.2023**, pagina 2 PDF, rândul 10 (autorizare prin Ordin66/2023) și 11 (atestare prin Ordin134/2021), ambele cu **Grad II DA**. Link https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf. Paginile 1/2 au fost verificate vizual prin instrumentul de screenshot web. Pentru atestarea 134/2021, bibliografia dă NU grad I și DA grad II.
- Sens juridic: electricianul persoană fizică are **autorizație**, operatorul economic are **atestat**; Ordin65/2024 modifică regulamentul autorizării, nu îl aprobă inițial. Enunțul «documentul la punctul...» are o problemă de tip dacă opțiunile reprezintă doar **ordine de aprobare**. Se consemnează, nu se editează.
- Master QABC și cheile originale au fost recitite, inclusiv hashul; indexul de dovezi CKPT043–049 nu conține aceste 8 ID-uri. Independent QA sursă, tehnic, lingvistic NOT_RUN, iar ediția **05.2023** nu certifică de la sine actualizări 2026 sau întrebări originale de examen.

## G2-LEG-120 | AU-56a5d64747981da9
- unit_id AU-56a5d64747981da9; qabc_sha256 56a5d64747981da9adac4ddf1e41a32b8c3b65b40769988e11f99e8557a07efd; member G2-LEG-120; original key {"G2-LEG-120":"A"}
- **Original:** Care este documentul indicat de ANRE la punctul 10 pentru tematica Gradului II?
  - A. Ordinul ANRE nr. 66/2023
  - B. Ordinul ANRE nr. 65/2024
  - C. Ordinul ANRE nr. 134/2021
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 10; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** La poziția 10, documentul este **Regulamentul pentru autorizarea electricienilor în domeniul instalațiilor electrice**, iar actul aprobator e **Ordin ANRE 66/2023**. Întrebarea spune «care este documentul indicat», însă cele trei răspunsuri propun **ordine**, nu titlul regulamentului: A reprezintă doar intenția autorului de a selecta din coloana «Document aprobat prin». Ordin ANRE 65/2024 **modifică** Regulamentul aprobat prin 66/2023, nu este ordinul aprobator inițial. Ordin ANRE 134/2021 aprobă Regulamentul pentru **atestarea operatorilor economici**, rândul 11.
- **Vertical ABC:** A «Ordinul ANRE nr. 66/2023» corespunde coloanei aprobatoare pentru rândul 10; B «Ordinul ANRE nr. 65/2024» e alt act; C «Ordinul ANRE nr. 134/2021» e alt act, deci B/C nu au același obiect.
- **Orizontal ABC:** A↔B, A↔C aprobatorul din rând față de un alt act; B↔C două ordonanțe/ordine distincte fără corespondent la rând.
- **Reversie/contraexemplu:** Schimbarea mentală a întrebării în «care este ordinul aprobator al documentului la acest punct» ar identifica A, dar enunțul original spune «documentul», deci se marchează TYPE_MISMATCH.
- **Status:** A_INTENDED__DOCUMENT_VS_APPROVAL_ORDER_MISMATCH; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-LEG-121 | AU-e82c8e283e2b206d
- unit_id AU-e82c8e283e2b206d; qabc_sha256 e82c8e283e2b206dd3864c4d281312204aa20dfa5e08dee959bc4c770f9ea7da; member G2-LEG-121; original key {"G2-LEG-121":"A"}
- **Original:** Prin ce act este aprobat documentul „Regulamentul pentru autorizarea electricienilor”, conform bibliografiei ANRE?
  - A. Ordinul ANRE nr. 66/2023
  - B. Ordinul ANRE nr. 65/2024
  - C. Ordinul ANRE nr. 134/2021
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 10; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** Întrebarea cere explicit actul care aprobă **Regulamentul pentru autorizarea electricienilor în domeniul instalațiilor electrice**. Tabelul ANRE arată la rândul 10 **Ordin ANRE 66/2023**, iar forma ordonată a actului confirmă rolul aprobator. Ordin ANRE 65/2024 **modifică** Regulamentul aprobat prin 66/2023, nu este ordinul aprobator inițial. Ordin ANRE 134/2021 aprobă Regulamentul pentru **atestarea operatorilor economici**, rândul 11. Denumirea exactă a Regulamentului de autorizare include și verificatorii/experții tehnici; întrebarea o prescurtează, dar rândul 10 este identificabil fără echivoc.
- **Vertical ABC:** A «Ordinul ANRE nr. 66/2023» este aprobatorul din coloana ANRE; B «Ordinul ANRE nr. 65/2024» nu aprobă acest regulament; C «Ordinul ANRE nr. 134/2021» nu aprobă acest regulament.
- **Orizontal ABC:** A↔B și A↔C aceeași întrebare juridică pentru alte obiecte; B↔C două acte diferite, niciunul nu e actul aprobator căutat.
- **Reversie/contraexemplu:** Verificare inversă din numărul ordinului aprobat spre titlul regulamentului confirmă A; nu se consideră că o modificare ulterioară schimbă numărul ordinului inițial.
- **Status:** A_DIRECT_OFFICIAL_APPROVAL_ACT_2023; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-LEG-122 | AU-c92ba73e49e93016
- unit_id AU-c92ba73e49e93016; qabc_sha256 c92ba73e49e93016b2e9c936c8657604e13097dd94b1e9c1d414d75a0834590f; member G2-LEG-122; original key {"G2-LEG-122":"A"}
- **Original:** Este „Regulamentul pentru autorizarea electricienilor” inclus în bibliografia aplicabilă Gradului II?
  - A. Da
  - B. Nu
  - C. Doar pentru Gradele III și IV
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 10; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** Coloana **Grad II** pentru poziția 10 ANRE 05.2023 este **DA**; întrebarea cere acest fapt bibliografic, nu competența legală efectivă pentru o lucrare. B îl neagă, iar C îl limitează exclusiv la III/IV, deși tabelul indică și II. Denumirea exactă a Regulamentului de autorizare include și verificatorii/experții tehnici; întrebarea o prescurtează, dar rândul 10 este identificabil fără echivoc.
- **Vertical ABC:** A «Da» este celula II=DA; B «Nu» fals; C «Doar pentru Gradele III și IV» exclusivitatea pentru grade mai mari e falsă.
- **Orizontal ABC:** A↔B polaritate DA/NU; A↔C Grad II vs numai III/IV; B↔C forme diferite de negare a II.
- **Reversie/contraexemplu:** Dacă C ar fi adevărat, celula Grad II din PDF ar fi NU, dar ea este DA. Rândul 11 arată în schimb Grad I NU, deci trebuie respectat gradul exact.
- **Status:** A_GRADE_II_DA_OFFICIAL_2023; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-LEG-123 | AU-f5a5b36cf6429926
- unit_id AU-f5a5b36cf6429926; qabc_sha256 f5a5b36cf6429926b947dc6bd63cd6d02fba9d733cd009f14ca1e836fbc11f27; member G2-LEG-123; original key {"G2-LEG-123":"A"}
- **Original:** În ce domeniu tematic este încadrat „Regulamentul pentru autorizarea electricienilor” în bibliografia ANRE?
  - A. Legislație
  - B. Electrotehnică
  - C. Măsurări electrice
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 10; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** Poziția 10, **Regulamentul pentru autorizarea electricienilor în domeniul instalațiilor electrice**, este în domeniul **«Legislație»** din tabel, chiar dacă reglementează instalații electrice tehnice. B sau C sunt discipline tehnice, nu eticheta de domeniu a acestei linii. Denumirea exactă a Regulamentului de autorizare include și verificatorii/experții tehnici; întrebarea o prescurtează, dar rândul 10 este identificabil fără echivoc.
- **Vertical ABC:** A «Legislație» corespunde etichetei Legislație; B «Electrotehnică» este domeniu tehnic greșit; C «Măsurări electrice» este domeniu tehnic greșit.
- **Orizontal ABC:** A↔B lege/normativ vs Electrotehnică; A↔C legislație vs Măsurări; B↔C două discipline nealese ca etichetă.
- **Reversie/contraexemplu:** Clasificarea se ia din prima coloană, nu din faptul că regulamentul vorbește despre electricitate.
- **Status:** A_OFFICIAL_TABLE_LEGISLATIE_DOMAIN; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-LEG-124 | AU-d41271032629ba00
- unit_id AU-d41271032629ba00; qabc_sha256 d41271032629ba00fbd69c3f0ecdf5b10c65d5564ba34251fb323013b4665177; member G2-LEG-124; original key {"G2-LEG-124":"A"}
- **Original:** Care este documentul indicat de ANRE la punctul 11 pentru tematica Gradului II?
  - A. Ordinul ANRE nr. 134/2021
  - B. Ordinul ANRE nr. 66/2023
  - C. Ordinul ANRE nr. 102/2015
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 11; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** La poziția 11, documentul este **Regulamentul pentru atestarea operatorilor economici care proiectează, execută și verifică instalații electrice**, iar actul aprobator e **Ordin ANRE 134/2021**. Întrebarea spune «care este documentul indicat», însă cele trei răspunsuri propun **ordine**, nu titlul regulamentului: A reprezintă doar intenția autorului de a selecta din coloana «Document aprobat prin». Ordin ANRE 66/2023 aprobă Regulamentul de **autorizare a electricienilor persoane fizice**, rândul 10. Ordin ANRE 102/2015 aprobă Regulamentul privind **stabilirea soluțiilor de racordare**, rândul 12.
- **Vertical ABC:** A «Ordinul ANRE nr. 134/2021» corespunde coloanei aprobatoare pentru rândul 11; B «Ordinul ANRE nr. 66/2023» e alt act; C «Ordinul ANRE nr. 102/2015» e alt act, deci B/C nu au același obiect.
- **Orizontal ABC:** A↔B, A↔C aprobatorul din rând față de un alt act; B↔C două ordonanțe/ordine distincte fără corespondent la rând.
- **Reversie/contraexemplu:** Schimbarea mentală a întrebării în «care este ordinul aprobator al documentului la acest punct» ar identifica A, dar enunțul original spune «documentul», deci se marchează TYPE_MISMATCH.
- **Status:** A_INTENDED__DOCUMENT_VS_APPROVAL_ORDER_MISMATCH; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-LEG-125 | AU-c799827bea81bb79
- unit_id AU-c799827bea81bb79; qabc_sha256 c799827bea81bb792e61fb8774c057d552aad41ae16fb15f3505d04a23cff902; member G2-LEG-125; original key {"G2-LEG-125":"A"}
- **Original:** Prin ce act este aprobat documentul „Regulamentul pentru atestarea operatorilor economici care proiectează, execută și verifică instalații electrice”, conform bibliografiei ANRE?
  - A. Ordinul ANRE nr. 134/2021
  - B. Ordinul ANRE nr. 66/2023
  - C. Ordinul ANRE nr. 102/2015
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 11; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** Întrebarea cere explicit actul care aprobă **Regulamentul pentru atestarea operatorilor economici care proiectează, execută și verifică instalații electrice**. Tabelul ANRE arată la rândul 11 **Ordin ANRE 134/2021**, iar forma ordonată a actului confirmă rolul aprobator. Ordin ANRE 66/2023 aprobă Regulamentul de **autorizare a electricienilor persoane fizice**, rândul 10. Ordin ANRE 102/2015 aprobă Regulamentul privind **stabilirea soluțiilor de racordare**, rândul 12. Autorizarea unei persoane fizice electrician și atestarea operatorului economic sunt **obiecte juridice diferite**; nu se substituie doar pentru că ambele privesc instalații electrice.
- **Vertical ABC:** A «Ordinul ANRE nr. 134/2021» este aprobatorul din coloana ANRE; B «Ordinul ANRE nr. 66/2023» nu aprobă acest regulament; C «Ordinul ANRE nr. 102/2015» nu aprobă acest regulament.
- **Orizontal ABC:** A↔B și A↔C aceeași întrebare juridică pentru alte obiecte; B↔C două acte diferite, niciunul nu e actul aprobator căutat.
- **Reversie/contraexemplu:** Verificare inversă din numărul ordinului aprobat spre titlul regulamentului confirmă A; nu se consideră că o modificare ulterioară schimbă numărul ordinului inițial.
- **Status:** A_DIRECT_OFFICIAL_APPROVAL_ACT_2023; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-LEG-126 | AU-c1dd84694802f41f
- unit_id AU-c1dd84694802f41f; qabc_sha256 c1dd84694802f41f5327fca61bd0ac62c22015c8e99e2ea636ed4c651b9d5438; member G2-LEG-126; original key {"G2-LEG-126":"A"}
- **Original:** Este „Regulamentul pentru atestarea operatorilor economici care proiectează, execută și verifică instalații electrice” inclus în bibliografia aplicabilă Gradului II?
  - A. Da
  - B. Nu
  - C. Doar pentru Gradele III și IV
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 11; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** Coloana **Grad II** pentru poziția 11 ANRE 05.2023 este **DA**; întrebarea cere acest fapt bibliografic, nu competența legală efectivă pentru o lucrare. B îl neagă, iar C îl limitează exclusiv la III/IV, deși tabelul indică și II. Autorizarea unei persoane fizice electrician și atestarea operatorului economic sunt **obiecte juridice diferite**; nu se substituie doar pentru că ambele privesc instalații electrice.
- **Vertical ABC:** A «Da» este celula II=DA; B «Nu» fals; C «Doar pentru Gradele III și IV» exclusivitatea pentru grade mai mari e falsă.
- **Orizontal ABC:** A↔B polaritate DA/NU; A↔C Grad II vs numai III/IV; B↔C forme diferite de negare a II.
- **Reversie/contraexemplu:** Dacă C ar fi adevărat, celula Grad II din PDF ar fi NU, dar ea este DA. Rândul 11 arată în schimb Grad I NU, deci trebuie respectat gradul exact.
- **Status:** A_GRADE_II_DA_OFFICIAL_2023; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## G2-LEG-127 | AU-b6147b0f47236ba7
- unit_id AU-b6147b0f47236ba7; qabc_sha256 b6147b0f47236ba7f55907d2327ecb6659fa63b8e2c8bb030f553a669c266f26; member G2-LEG-127; original key {"G2-LEG-127":"A"}
- **Original:** În ce domeniu tematic este încadrat „Regulamentul pentru atestarea operatorilor economici care proiectează, execută și verifică instalații electrice” în bibliografia ANRE?
  - A. Legislație
  - B. Electrotehnică
  - C. Măsurări electrice
- **Exact locator:** ANRE 05.2023 PDF p.2, domeniu Legislație, rând 11; https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
- **Context și excepții:** Poziția 11, **Regulamentul pentru atestarea operatorilor economici care proiectează, execută și verifică instalații electrice**, este în domeniul **«Legislație»** din tabel, chiar dacă reglementează instalații electrice tehnice. B sau C sunt discipline tehnice, nu eticheta de domeniu a acestei linii. Autorizarea unei persoane fizice electrician și atestarea operatorului economic sunt **obiecte juridice diferite**; nu se substituie doar pentru că ambele privesc instalații electrice.
- **Vertical ABC:** A «Legislație» corespunde etichetei Legislație; B «Electrotehnică» este domeniu tehnic greșit; C «Măsurări electrice» este domeniu tehnic greșit.
- **Orizontal ABC:** A↔B lege/normativ vs Electrotehnică; A↔C legislație vs Măsurări; B↔C două discipline nealese ca etichetă.
- **Reversie/contraexemplu:** Clasificarea se ia din prima coloană, nu din faptul că regulamentul vorbește despre electricitate.
- **Status:** A_OFFICIAL_TABLE_LEGISLATIE_DOMAIN; OFFICIAL_QABC_QUESTION_PROVENANCE_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; LEARNING_APPROVAL_NO.

## Controale de regresie
- Tipul A/B pentru electrician persoană fizică nu este echivalent cu atestatul unui operator economic; rândul 10 Ordin66/2023 nu poate fi substituit cu rândul 11 Ordin134/2021.
- Rândul 11 aplicabil Grad II (DA) dar nu Grad I (NU). Răspunsurile A importate nu sunt certificarea provenienței dintr-un chestionar ANRE în format XLSX.
- Fără bareme, CSV, HTML, APK, main, merge sau release; QA independent și ediția exactă examen 2026 rămân porți.
