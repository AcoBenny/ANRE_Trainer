# CKPT-089 | P1 Lot AI G2-LEG-074–080, admitere, examen, viză periodică ANRE | 2026-11-17

## Contabilitate și QA
- Branch audit/anre-v8-priority-17-20261109, PR #7 Draft/Open; HEAD inițial verificat d6d2283f6782906c4526dac8e0989bfc891c70fd. Bază CKPT088: 237/568 unități, 292/822 ID-uri de grad. Șapte P1 distincte și necreditate, fără context în master și fără apariție în ACTIVE_EVIDENCE_INDEX_87: delta +7/+7 => **244/568 unități, 299/822 ID-uri**, **0/822 aprobate pentru învățare**.
- Sursă oficială ANRE https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ secțiunile A1.II, A1.III, A2; Regulament 66/2023 art.16,18,30,17 pentru confirmare. Informațiile se aplică practicii de autorizare, dar pagina NU certifică originea din XLSX oficial a acestor întrebări derivate G2-LEG; cheia de examen exactă și ediția bibliografică rămân nevalidate.
- Control QABC+hash recitit din MASTER. Analiză verticală, toate perechile, reversie și excepții pentru fiecare item. **Independent QA=NOT_RUN**; nu s-au modificat date, chei, aplicație, master, HTML/APK, main sau merge/release.

## G2-LEG-074 | AU-c79d169c7b05e8f7
- unit_id AU-c79d169c7b05e8f7; sha256 c79d169c7b05e8f71be5111a4200e85b799762af82066eadca875d3c3439a3a8; member_ids G2-LEG-074; barem canonical intact: {"G2-LEG-074":"A"}
- **Întrebare originală:** Acceptarea dosarului de autorizare presupune și demonstrarea experienței profesionale minime, în conformitate cu cerințele regulamentului?
  - A. Da
  - B. Nu
  - C. Numai pentru Gradul I
- **Locator:** ANRE A1.II/A1.III/A2 potrivit obiectului, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- **Context, condiții, excepții:** A1.II(c): pentru acceptarea dosarului, candidatul demonstrează experiența minimă **în concordanță cu art.16 din Regulamentul ANRE**. «Da» reflectă această condiție procedurală, dar nu stabilește aceeași experiență minimă pentru toate gradele și calificările. «Nu» ar nega condiția, iar «numai gradul I» inventează o restricție.
- **Vertical ABC:** A A_ART16_GRADE_CONDITIONAL; B B_NEGATES_EXPERIENCE_GATES; C C_ONLY_GRADE_I_FALSE.
- **Orizontal:** A vs B cerință gradată sau negare; A vs C condiție pe categorii vs doar I; B vs C două erori diferite.
- **Reversie/contraexemplu:** Dacă o categorie de grad II are experiență minimă conform art.16, acceptarea fără a o demonstra este incompatibilă; cerința exactă rămâne tabelară.
- **Stare:** IMPORTED_A_POSITIVE_CANDIDATE_ONLY; EXAM_OFFICIAL_ORIGIN_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-075 | AU-56ec07544ee0efa8
- unit_id AU-56ec07544ee0efa8; sha256 56ec07544ee0efa8e0291d57b81aa303dc37a37802ea2ecce7571e05a02d22ee; member_ids G2-LEG-075; barem canonical intact: {"G2-LEG-075":"A"}
- **Întrebare originală:** Examenele de autorizare a electricienilor se organizează, de regulă, de câte ori pe an?
  - A. De două ori pe an
  - B. O singură dată la cinci ani
  - C. În fiecare lună, obligatoriu
- **Locator:** ANRE A1.II/A1.III/A2 potrivit obiectului, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- **Context, condiții, excepții:** Secțiunea A1.III de pe site-ul ANRE precizează **de regulă de două ori pe an**. Acesta este număr orientativ, nu promisiunea că fiecare an are exact două sesiuni. B «o singură dată la cinci ani» confundă examenul inițial cu vizarea periodică, iar C impune organizare lunară obligatorie, neprevăzută.
- **Vertical ABC:** A A_TWICE_USUALLY_NOT_MANDATORY; B B_CONFUSES_VISA_5Y; C C_MONTHLY_NOT_REQUIRED.
- **Orizontal:** A↔B sesiune examen vs vizare; A↔C frecvență uzuală vs obligatorie lunară; B↔C cicluri de timp incompatible.
- **Reversie/contraexemplu:** Un an cu calendar ANRE excepțional diferit nu anulează formula «de regulă» și nici nu probează obligativitatea lunară.
- **Stare:** IMPORTED_A_POSITIVE_CANDIDATE_ONLY; EXAM_OFFICIAL_ORIGIN_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-076 | AU-5120aae8c0971046
- unit_id AU-5120aae8c0971046; sha256 5120aae8c09710464d6c0c59cc1d701328f2ff83cb00a34b4d67b59ab527e251; member_ids G2-LEG-076; barem canonical intact: {"G2-LEG-076":"A"}
- **Întrebare originală:** La ce interval este prevăzută vizarea periodică a autorizației de electrician?
  - A. O dată la cinci ani
  - B. Lunar
  - C. O dată la zece ani
- **Locator:** ANRE A1.II/A1.III/A2 potrivit obiectului, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- **Context, condiții, excepții:** Secțiunea A2 ANRE: condiția periodică a valabilității este **vizarea o dată la cinci ani**, confirmată și de Regulamentul 66/2023 art.18 și art.30. B lunară confundă vizarea cu activitățile administrative curente; C zece ani dublează fără temei. Calitatea autorizat este definitivă în condițiile legii, dar dreptul de practică depinde de viză.
- **Vertical ABC:** A A_FIVE_YEAR_VISA; B B_MONTHLY_NOT_IN_NORM; C C_TEN_YEAR_WRONG.
- **Orizontal:** A↔B vizare ani vs luni; A↔C 5 vs 10; B↔C 1/12 vs 10 ani, fără temei.
- **Reversie/contraexemplu:** Document emis la data T trebuie vizat până la termenul periodic T+5 ani, în condițiile calendaristice și procedurale.
- **Stare:** IMPORTED_A_POSITIVE_CANDIDATE_ONLY; EXAM_OFFICIAL_ORIGIN_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-077 | AU-7080838763fcc55c
- unit_id AU-7080838763fcc55c; sha256 7080838763fcc55c9bb8be5fff1d9d978ef5de1dc7a92910f7f2b66d3140ab9e; member_ids G2-LEG-077; barem canonical intact: {"G2-LEG-077":"A"}
- **Întrebare originală:** Pentru vizarea periodică a autorizației de electrician, ANRE enumeră dovada absolvirii în ultimele 12 luni a unui curs de pregătire teoretică de minimum: 
  - A. 20 de ore
  - B. 2 ore
  - C. 100 de ore
- **Locator:** ANRE A1.II/A1.III/A2 potrivit obiectului, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- **Context, condiții, excepții:** Secțiunea A2 lit.c cere dovada cursului teoretic de **minimum 20 ore absolvit în ultimele 12 luni** anterioare cererii de vizare. B două ore este sub minimum; C o sută de ore nu este minimul normat, chiar dacă cineva poate urma voluntar un curs mai lung. Cuvântul-cheie este **minimum**, nu interdicția cursurilor de altă durată.
- **Vertical ABC:** A A_20_HOURS_MINIMUM_WITHIN_12_MONTHS; B B_TWO_HOURS_TOO_SHORT; C C_100_HOURS_NOT_LEGAL_MINIMUM.
- **Orizontal:** A↔B două valori de minim, B fals; A↔C prag minim vs exces de curs; B↔C extreme fără susținere.
- **Reversie/contraexemplu:** Un curs de 24 de ore în intervalul cerut poate satisface limita; curs de 20 ore terminat înainte de ultimele 12 luni nu satisface condiția temporală.
- **Stare:** IMPORTED_A_POSITIVE_CANDIDATE_ONLY; EXAM_OFFICIAL_ORIGIN_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-078 | AU-911cf371783c9628
- unit_id AU-911cf371783c9628; sha256 911cf371783c9628c1bf89d2e68d9a4a4046bacf8efc27628d3e9d97c5ca9013; member_ids G2-LEG-078; barem canonical intact: {"G2-LEG-078":"A"}
- **Întrebare originală:** Ce se întâmplă dacă autorizația de electrician nu este vizată până la termenul de vizare?
  - A. Titularul nu are dreptul să desfășoare activități de proiectare, executare și verificare până la vizare
  - B. Autorizația se transformă automat în Gradul I
  - C. Nu există nicio consecință
- **Locator:** ANRE A1.II/A1.III/A2 potrivit obiectului, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- **Context, condiții, excepții:** Secțiunea A2 ANRE spune că electricianul fără viza periodică la termen **nu are dreptul să desfășoare activități de proiectare, execuție și verificare** până la vizare. B afirmă promovarea automată la grad I, care nu este efectul nevizării; C neagă consecința interdicției. Nu deducem că simpla nevizare conduce automat la retragerea definitivă a autorizării, fiind un efect diferit.
- **Vertical ABC:** A A_PRACTICE_PROHIBITED_UNTIL_VISA; B B_NO_AUTOMATIC_DEMOTION; C C_DENIES_SUSPENDED_PRACTICE.
- **Orizontal:** A↔B interdicție practică vs schimbare grad; A↔C consecință vs nicio consecință; B↔C două descrieri false.
- **Reversie/contraexemplu:** Titularul care nu a vizat poate relua activitatea după vizare în limitele gradului; nu primește grad nou prin expirarea perioadei.
- **Stare:** IMPORTED_A_POSITIVE_CANDIDATE_ONLY; EXAM_OFFICIAL_ORIGIN_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-079 | AU-6f67293be795236f
- unit_id AU-6f67293be795236f; sha256 6f67293be795236f03cd6a6349f37d7a74bdc46d9912c982218c167504eea5d6; member_ids G2-LEG-079; barem canonical intact: {"G2-LEG-079":"A"}
- **Întrebare originală:** Autorizația de electrician este valabilă numai în concordanță cu ce evidență a autorității competente?
  - A. Registrul electronic de evidență
  - B. Registrul auto
  - C. Registrul comerțului al angajatorului, exclusiv
- **Locator:** ANRE A1.II/A1.III/A2 potrivit obiectului, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- **Context, condiții, excepții:** ANRE A2: autorizația este valabilă doar în concordanță cu **Registrul electronic de evidență al ANRE** și împreună cu act de identitate. A corespunde sistemului oficial de evidență; B registrul auto e fără obiect, iar C registrul comerțului al angajatorului nu înlocuiește evidența persoanei autorizate. Grila nu include actul de identitate, care rămâne o condiție adițională de valabilitate.
- **Vertical ABC:** A A_ELECTRONIC_REGISTER_EXPLICIT; B B_VEHICLE_REGISTER_WRONG; C C_EMPLOYER_TRADE_REGISTER_NOT_ANRE_AUTHORIZATION.
- **Orizontal:** A↔B registru competențe vs auto; A↔C persoana autorizată vs firma angajatorului; B↔C ambele alte registre fără obiect.
- **Reversie/contraexemplu:** Electrician cu adeverință tipărită, dar neconcordantă cu registrul oficial, nu devine valid prin înscrierea firmei sale la Registrul Comerțului.
- **Stare:** IMPORTED_A_POSITIVE_CANDIDATE_ONLY; EXAM_OFFICIAL_ORIGIN_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-080 | AU-eeca1a252d40f916
- unit_id AU-eeca1a252d40f916; sha256 eeca1a252d40f91695e897a93fa008e62f56fad7a0ea6cb27df8d78da7268020; member_ids G2-LEG-080; barem canonical intact: {"G2-LEG-080":"A"}
- **Întrebare originală:** Prin ce mijloace poate solicita solicitantul înregistrarea la ANRE a documentelor prevăzute în regulament?
  - A. Prin portalul autorității competente sau prin încărcare în platforma PCUe
  - B. Numai prin telefon
  - C. Numai prin mesaj SMS
- **Locator:** ANRE A1.II/A1.III/A2 potrivit obiectului, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- **Context, condiții, excepții:** A1.I(a) ANRE prevede **cererea electronică în portalul autorității sau PCUe**; A formulează cele două canale. B «numai prin telefon» și C «numai prin SMS» nu realizează încărcarea documentației cerută. Denumirea «înregistrarea documentelor» implică formalizarea dosarului pe un canal oficial, nu simpla comunicare neformalizată.
- **Vertical ABC:** A A_PORTAL_OR_PCUE; B B_ONLY_PHONE_NOT_VALID_SUBMISSION; C C_ONLY_SMS_NOT_VALID_SUBMISSION.
- **Orizontal:** A↔B dosar electronic vs telefon; A↔C dosar electronic vs SMS; B↔C două canale insuficiente ca depunere formală.
- **Reversie/contraexemplu:** Un apel telefonic informativ către ANRE nu este depunerea efectivă a dosarului și nu substituie uploadul cererii.
- **Stare:** IMPORTED_A_POSITIVE_CANDIDATE_ONLY; EXAM_OFFICIAL_ORIGIN_UNVERIFIED; INDEPENDENT_TECH_SOURCE_LING_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## QA transversal / învățări
- De regulă **două** sesiuni ≠ exact două în fiecare an; minimum 20 ore în **ultimele 12 luni** ≠ orice curs trecut; nevizarea restrânge exercitarea, nu schimbă gradul.
- Toate cheile celor șapte itemi sunt **A**, ceea ce este avertisment de proveniență sau poziționare a opțiunilor, nu dovadă de greșeală; verificați XLSX oficial și ordinea A/B/C.
- Următorul lot poate examina G2-LEG bibliografie 001–006, cu actele normative inițiale; fără promovare la learner-ready până la QA distinct.
