# ANRE Trainer | V8 | Lansarea auditului întrebărilor, lotul de risc 17

**Data:** 2026-11-09. **Mandat utilizator:** acord explicit pentru trecerea de la dosarul didactic V7 la *auditul* întrebărilor. **Nu s-a autorizat o corectare automată a baremelor ori un release.**

**Sursa de adevăr pentru textul întrebărilor:** `ANRE_Trainer_V10_29_SOURCE_AUDIT_QUARANTINE_STANDALONE.html`, SHA-256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`, **822 ID-uri distincte** (Grad I: 414, Grad II: 408). `DATA` și `G2_ELEC_CANDIDATES` au fost parsate din fișierul HTML real, nu reconstituite din rapoarte. Nu s-a generat o nouă versiune HTML/APK.

## Verdictul exact pe 17 întrebări cu risc prioritar

**17 din 17**: am confruntat enunțul și toate variantele A/B/C din V10.29, cheia originală și textul tehnic din PDF-urile locale sau surse externe identificate. Aceasta este **revizie asistată de același model**, nu QA tehnic independent.

- **4/17 `SUPPORTED_EXACT_PRELIMINARY`**: `G2-ELEC-011` (Hz), `012` (T=1/f), `033` (voltmetru paralel), `034` (ampermetru serie). Dovezi mai bune decât paginile candidate originale: `PREG` PDF pp132, 133, 135; paginile selectate au fost citite, p132 inspectată vizual.
- **12/17 `SUPPORTED_WITH_CONDITIONS`**: `006` (E=Pt doar pentru P constantă), `013` (valoare efectivă cu echivalență termică, PREG 86 vizual), `023` (pur R: cosφ=1), `029` (raport spire/tensiuni *de înfășurare*, nu generalizare pentru orice tensiune de linie trifazată, `MAS` PDF p30 vizual), `030` (imposibilă funcționarea normală stabilă la CC *constant*, nu interzicerea oricărui tranzitoriu), `035` (ohmmetru pe circuit fără alimentare; în plus, condensatoare descărcate și absența tensiunii verificată), `044`, `045` (formula `R=ρ l/S` pentru conductor omogen și ipoteze fixe, `PREG` p251 vizual), `046` (coeficient de temperatură pozitiv pentru metalele obișnuite, în domeniul uzual), `048` (declanșare termică/electromagnetică *după tipul aparatului*, `PREG` p181), `049` (suma curenților activi / curent rezidual; `I7` p25 numai enumeră DDR, explicația principiului provine de la fabricant), `050` (legarea la pământ în TN/TT/IT condiționată de măsuri de deconectare, ediția I7 locală 2023 nu certifică legalitatea 2026).
- **1/17 `NEEDS_EXACT_DEFINITION_SOURCE`**: `G2-ELEC-036` (impedanța mică poate produce curent de defect mare, dar vechea pagină `I7` p38 trata *amplasarea protecțiilor*, nu definiția exactă a scurtcircuitului; să nu fie aprobată ca dovadă didactică).
- **17/17** păstrează cheia originală `A`. **0 propuneri de schimbare a baremelor**, fără afirmația că acele bareme au validare independentă. Punctele sensibile se revizuiesc separat când un revizor competent este disponibil.

### Exemple de referințe exacte (fără copierea manualelor în repo)

| ID | Pagina fizică PDF și principiu | Limita dovezii |
|---|---|---|
| `G2-ELEC-012` | `PREG` p132: frecvența `f = 1/T` în secțiunea de mărimi alternative | Anterior `PREG` p86 nu prezenta relația explicit |
| `G2-ELEC-013` | `PREG` p86: curentul alternativ efectiv are efect termic echivalent în același rezistor | Nu confundăm RMS cu măsurarea frecvenței |
| `G2-ELEC-029` | `MAS` p30: relația de fază `k_f = U1f/U2f = N1/N2`; același text arată că raporturile de linie la Y-y/D-y/Y-z diferă | Enunțul nu spune explicit „tensiuni de fază”; se recomandă clarificarea pedagogică, nu schimbarea răspunsului |
| `G2-ELEC-033` | `PREG` p133: „voltmetrul se conectează în paralel” | Text tehnic direct, rămâne QA independent |
| `G2-ELEC-034` | `PREG` p135: „ampermetrul se conectează în serie” | Text tehnic direct, rămâne QA independent |
| `G2-ELEC-044/045` | `PREG` p251: formula (3.72) `R = ρ0 (1+αθ) l/s` | Formula verificată vizual; se cer ipoteze de material, temperatură, secțiune |
| `G2-ELEC-048` | `PREG` p181: declanșator termic pentru suprasarcină, electromagnetic pentru scurtcircuit | Tipul echipamentului controlează funcțiile efective |
| `G2-ELEC-050` | `I7` p23 §4.1.3.2 și p25 §4.1.4.1.11 | Distinge TN/TT/IT și DDR în TN-C/TN-C-S; I7 local are sinteză 2023 |

Surse auxiliare externe consultate pentru completarea locatoarelor, **nu** pentru distribuirea automată a textelor în aplicație:
- Energie/power: https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
- Transformator ideal: https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers
- Rezistivitate și variația cu temperatura: https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance
- Funcționare RCD: https://www.se.com/au/en/faqs/FAQ000210095/
- Ohmmetru: https://assets.fluke.com/manuals/2x_2____umeng0000.pdf, manual 27 II/28 II, pagină imprimată 4, text extras: alimentarea deconectată și condensatoarele descărcate înainte de măsurarea rezistenței. **Captura PDF web a eșuat din cache**, deci nu atribuim acestui document confirmare vizuală în instrumentul web.
- I7 local este `803493174-I7-2011-completat2023.pdf` (sinteză 22.09.2023). Originalele PDF sunt utilizate exclusiv în analiza privată, nu au fost incluse în acest PR.

## Recontrol determinist: 76 de asocieri de surse candidate

Din același HTML V10.29 am parsat 76 de obiecte `G2_ELEC_CANDIDATES` și le-am comparat **exact** cu toate cele 822 înregistrări `DATA` prin: nume normalizat fișier XLSX, rândul sursei, enunțul identic și cele trei opțiuni A/B/C păstrate în ordine.

- **76/76**: ținta conceptuală NU este întrebarea originală indicată de fișa sursă.
- **76/76**: fișa se potrivește cu **exact două alte ID-uri**: unul de Grad I și unul de Grad II.
- **48** rânduri distincte XLSX, repetate în 76 de fișe; **0/76** bareme dovedite greșite doar prin acest mismatch.
- Exemplu de test: fișa pentru `G2-ELEC-050` face trimitere la pierderile Corona ale `G1-ELE-074` / `G2-ELEC-219`, nu la întrebarea despre împământare.
- Toate 76 de întrebări conceptuale au răspunsul `A` și UI din sursa precedentă păstra poziția A/B/C. **Defect de bias în interfață**, nu verdict de barem; fixul nu intră în acest PR.
- Lista completă este în `G2_ELEC_76_CANDIDATE_CROSS_ID_RECHECK_V8.csv`, status `WRONG_TARGET_DO_NOT_USE_AS_DIDACTIC_PROOF`.

## Integritatea celor 822 de ID-uri și corectarea ordinii loturilor

Inventarul are **822 ID-uri unice**, fără modificarea datelor. Important: seria conceptuală `G2-ELEC-001..076` este urmată în HTML de `G2-ELEC-154..408`; **nu există ID-uri `G2-ELEC-077..153` în această versiune**, ceea ce NU dovedește lipsa a 77 de întrebări din total. Din acest motiv, recomandarea anterioară de lot `G2-ELEC-051..100` era neexecutabilă pentru 24 de numere. 

**Următoarele 50 de ID-uri reale în ordine numerică, după `050`:** `G2-ELEC-051..076` (26 ID-uri) și `G2-ELEC-154..177` (24 ID-uri). Sunt marcate `NEXT_50_PRESENT_IDS` în `ALL_822_AUDIT_BACKLOG_V8.csv`; nu sunt încă validate semantic.

## Control QA, limite și protocol de schimbare

- Intrare: SHA verificat al HTML V10.29; `len(DATA)=822`, ID-uri unice; 17 în auditul selectat; 76 de fișe; 76/76 cross-ID dublu; 48 rânduri XLSX distincte; testele de consistență din scripturile locale au trecut.
- Diferențiem **„susținere teoretică model-asistată”**, **„sursă externă cu domeniu public”**, **„întrebare originală XLSX”** și **„QA independent”**. Nu promovăm nicio întrebare drept `OFFICIAL_ANRE_KEY_CONFIRMED` sau `INDEPENDENT_QA_PASS`.
- Rămân **0 corecții de barem**, **0 schimbări în HTML/APK**, **0 PDF-uri publicate**, **0 revizii independente**. Nu s-a activat niciun agent autonom.
- Toate cele 822 rămân în backlog. `Status=VERIFICAT TEHNIC` din aplicație este etichetă istorică a proiectului, nu un certificat extern nou.
- **Următorul lot:** cele 50 de ID-uri efectiv existente, prioritizând capcanele cu formulări absolute, normativele cu ediții vechi, calculele și sursele ce indică alte ID-uri.
- Un **PR separat pe ramură de dezvoltare**, doar cu acest raport și CSV-uri de audit; nu merge în `main`, nu release și nu cod nou în aplicație fără aprobare explicită.

**Checkpoint:** `CKPT-002` rămâne checkpoint-ul de bază. Acest lot V8 este o evidență nouă de audit, nu un checkpoint de release.


## Următoarele 50: doar screening automat (nu verificare semantică)

- Inventar construit din ID-urile **prezente efectiv în V10.29**, nu dintr-un interval numeric continuu: `G2-ELEC-051..076` (26 întrebări conceptuale) și `154..177` (24 întrebări cu etichetă sursă XLSX).
- Distribuție inițială a cheilor: A=32, B=9, C=9. Aceasta este **distribuție**, nu un verdict despre corectitudine.
- Semnale euristice neexclusive: 26 fișe candidate asociate greșit, 9 formulă/calcul, 5 măsurare, 3 protecție, 2 negație, 2 comparație, 2 condiționalitate; 15 fără marker detectat.
- **50/50 statut `NOT_REVIEWED` semantic și `NOT_RUN` QA independent**. Markerii nu dovedesc capcane; propunerile de corectare a răspunsurilor rămân zero.
- Date: [V8 next50 automated preflight](V8_G2_ELEC_NEXT50_AUTOMATED_PREFLIGHT.csv). Acest fișier nu trebuie confundat cu validarea didactică pe articol/pagină.
