# CKPT-109 | Protocol micro-lot pentru sesiuni stabile și reluare fără dublări | 17.11.2026

## Incident / observații verificabile
- Captura utilizatorului arată ultimul pas afișat: **„Reclasificarea celor 174 de itemi pentru verificarea surselor”**, cu opțiunea „Skip”, nu un cod explicit de eroare. Din captură NU se poate identifica un defect de server/client și nu afirmăm că browserul ori telefonul sunt cauza.
- GitHub a confirmat HEAD înainte de remediere `ed157997a7a23cd85db769ef987baeb608c914d1`, CKPT-107 și registrul cu **394/568 unități contextuale, 474/822 ID-uri, 174 unități G1-ELE restante**. PR #7 Open/Draft/Unmerged. Nicio pierdere de progres verificată.
- Factori de încărcare controlați de workflow: CKPT-103/104/105/106 au avut 18–20 de unități și zeci de mii de caractere în fișiere lungi; registrul de 568 rânduri este ~270k caractere și a fost rescris repetat; clasificarea simultană a celor 174 mărește consumul de context și riscul de întrerupere. **Cauză probabilă de supraîncărcare a fluxului, nu diagnostic confirmat al runtime-ului ChatGPT.**
- Pilotul CKPT-108 a redus lotul la **3 unități G1-ELE-082/130/135**; GitHub a returnat commituri reale de card și de registru. După sincronizare: **397/568 unități, 480/822 ID-uri contextuale; 171 unități G1-ELE restante**. 0/822 approved for learning.

## Regula operațională MICRO5, aplicabilă în continuare
1. **3–5 unități canonice per mini-lot**, fără a amesteca 174 de întrebări într-o singură clasificare semantică. Cel mult **două mini-loturi într-o execuție / răspuns**, apoi checkpoint și raport scurt; următoarea execuție reia din GitHub, fără promisiuni de lucru în fundal. Un singur caz foarte ambiguu este suficient pentru un mini-lot.
2. **Preflight unic și ieftin:** PR #7 HEAD + MASTER + registru, filtru `contextual_card_present=NO`, comparați `unit_id`, `qabc_sha256`, `member_ids`, A/B/C și cheile intacte. Nu recitiți toate checkpointurile pentru fiecare unitate, decât la conflict/duplicat detectat.
3. **Surse pe obiect și ediție:** redeschideți sursa exactă, paragraful relevant și vecinătatea. Pentru o sursă PDF folosiți inspecție vizuală când e necesar. Trierea preliminară nu certifică sursa; întrebări derivate didactic separate de cele oficiale ANRE. Comparați variantele vertical, orizontal și invers; un răspuns corect în model ideal nu este automat adevărat în orice regim real.
4. **Fișă compactă per mini-lot** (țintă până la ~8k caractere): enunț/variante originale, cheia intactă, 4–6 propoziții de context, dovadă pozitivă, alternativele A/B/C, contraexemplu, referință și blocaj. Nu repetați introducerile despre politică la fiecare card. Limită orientativă, nu tăiați dovezile esențiale ca să încăpeți.
5. **Checkpoint atomic înainte de credit:** publicați fișierul DOCUMENTAR pe branch, recitiți efectiv fișierul și numărați ID-uri unice/variante, apoi actualizați registrul central **o singură dată per mini-lot**, cu SHA-ul curent al fișierului pentru conflict control. Citire confirmativă a registrului și HEAD PR. Dacă scrierea registrului eșuează, fișa rămâne în GitHub, dar creditul se marchează `AWAITING_LEDGER_RECONCILIATION`, fără a relua cercetarea.
6. **Stop și reluare la risc:** dacă apar două erori consecutive ale aceleiași operațiuni, drift de HEAD sau dovadă insuficientă, păstrați cazul `BLOCKED`, închideți cu checkpoint și treceți la un caz simplu din următorul mini-lot. Nu declanșați bucle de reîncercare nelimitate și nu mențineți mesaje lungi de progres. În fața utilizatorului raportați doar totalul, delta reală și blocajul.
7. **Gates separate:** `CONTEXTUAL_DOCUMENTED` ≠ `EXAM_PROVENANCE_VERIFIED` ≠ `EXACT_SOURCE_EDITION_VERIFIED` ≠ `INDEPENDENT_TECH_SOURCE_LING_QA_DONE` ≠ `APPROVED_FOR_LEARNING`. Păstrați **0/822 aprobate** până la închiderea fiecărei porți cu dovezi.

## Politica immutabilă
- Nu modificați QABC, baremele, CSV master, HTML, APK, main/master, nu faceți merge/release.
- Păstrați toate checkpointurile vechi ca dovezi și folosiți unit_id unic ca să evitați dubla numărare.
- Continuarea pornește din registru la **171 unități restante**, nu din pasul UI care părea blocat la 174.
