# CKPT-066 | P0 Lot R: cinci grile juridice Legea 123/2012 | 2026-11-16

## Integritate și versiuni
- Repo `AcoBenny/ANRE_Trainer`, branch `audit/anre-v8-priority-17-20261109`, PR #7 Draft, HEAD verificat înainte de commit `6fd0d6cb609612b3e7b67df2d9523c6b7ba87070`.
- Cinci **unități P0 distincte noi** cu câmp de context gol în `MASTER_UNIT_CARDS_568.csv`: `G1-LEG-015` (`AU-02ceaf178f459982`, cheie B), `G1-LEG-017` (`AU-4b365bd0966b300d`, cheie B), `G1-LEG-019` (`AU-438f264b2a9d1929`, cheie C), `G1-LEG-026` (`AU-6b631320f93aae79`, cheie C), `G1-LEG-048` (`AU-4225b9d615d2a302`, cheie A). Toate au **un singur ID** și nu s-au numărat anterior în CKPT-060–065.
- Bază CKPT-065: 137/568 unități și 180/822 ID-uri contextual documentate; delta +5/+5 => **142/568** unități, **185/822** ID-uri. **0/822 aprobate pentru învățare**.
- Sursă primară **Legea nr. 123/2012**, forma consolidată afişată pe Portalul Legislativ cu istoric până la **26.07.2026**, https://legislatie.just.ro/Public/DetaliiDocument/212091 , art. 57, 58, 92, 93, inclusiv art. 93 alin. (1) punctele 5 și 28. Surse de tip index/fragment Portal Legislativ pentru identificarea exactă a articolelor: https://legislatie.just.ro/Public/DetaliiDocument/209178 , https://legislatie.just.ro/Public/DetaliiDocument/249550 , https://legislatie.just.ro/Public/DetaliiDocument/300063 . **Limită factuală:** accesarea directă a unei versiuni a Portalului a dat timeout, dar căutarea a redat articolul exact din index. Forma 26.07.2026 a legii și schimbările după 2024 au fost reperate; încă nu s-a demonstrat cu o inspecție articol-cu-articol că toate cele cinci alineate au rămas neschimbate la data examenului ANRE. `CURRENT_EDITION_ARTICLE_BY_ARTICLE_QA_PENDING`.
- **Niciun barem modificat**, nicio aprobare de învățare, fără HTML/APK/master/main/merge/release, QA independent `NOT_RUN`. Testele raționamentului de mai jos nu substituie verdictul oficial.

## R1 | G1-LEG-015 | cheie B importată, contra-probă juridică
**Enunț exact:** „Constituie contravenţie:”
- A. „refuzul clienţilor finali de a permite accesul la grupurile de măsurare”
- B. „modificarea fără drept a componentelor instalaţiilor energetice”
- C. „sustragerea de energie electrica”

**Context și obiect în 5 fraze:** Art. **93 alin. (1) pct. 28** din Legea 123/2012 califică drept **contravenție** refuzul clientului de a permite accesul la grupurile de măsurare, în condițiile legii. Art. **92 alin. (1)** clasifică expres **modificarea fără drept a componentelor instalațiilor energetice drept infracțiune**, nu drept contravenție. Sustragerea de energie este o altă conduită cu regim sancționator separat, legată și de dreptul penal; nu devine contravenția cerută doar pentru că este o abatere față de lege. Într-o grilă care opune „contravenție” și „infracțiune”, **distincția juridică exactă** este eliminatorie și nu admite aproximări lingvistice. A este deci **candidatul puternic susținut pozitiv de sursa primară**, în contradicție cu baremul B importat.

**Vertical:** A `PRIMARY_LAW_ART93_28_CONTRAVENTION`; B `PRIMARY_LAW_ART92_1_CRIMINAL_NOT_CONTRAVENTION`; C `NOT_SUBSTANTIATED_AS_REQUESTED_CONTRAVENTION`. **Orizontal:** A↔B clase contravenție/infracțiune diferite; A↔C refuz acces vs sustragere, acte distincte; B↔C fapte diferite cu potențial penal, nu analogie pentru contravenție. **Reversie:** enunțul cere categoria juridică, nu gravitatea morală. **Status: `CRITICAL_IMPORTED_KEY_B_CONTRADICTED; CANDIDATE_A_EXACT_LEGAL_TEXT_NOT_APPLIED`**. Probă: Legea 123/2012, art. 92(1), art. 93(1) pct. 28, Portal Legislativ https://legislatie.just.ro/Public/DetaliiDocument/209178 .

## R2 | G1-LEG-017 | cheie B importată, contradicție cu obiectul rezilierii
**Enunț exact:** „Furnizorul de energie electrică este îndreptăţit sã rezilieze contractul de furnizare a energiei electrice  în caz de:”
- A. „sustragerea de energie electrică constatată prin hotărâre judecătorească definitivă”
- B. „racordare ilegală la reţeaua de distribuţie”
- C. „refuz al clientului final de a constitui garanţia solicitată de furnizor atunci când acesta constată acţiuni menite să denatureze în orice fel indicaţiile echipamentelor de măsurare”

**Context în 5 fraze:** Art. **58 alin. (4) lit. a)** din Legea 123/2012 menționează explicit **rezilierea contractului de către furnizor** când sustragerea energiei este constatată prin hotărâre judecătorească definitivă, exact alternativa A. La **art. 58 alin. (6)**, refuzul garanției financiare permite furnizorului să **solicite deconectarea** de către operatorul de distribuție, care este juridic distinctă de **rezilierea contractului**. **Racordarea ilegală** poate determina măsuri de sistare/deconectare și sancțiuni, însă nu a fost identificată în textul exact citat ca temei explicit unic pentru reziliere, în opoziție cu A. A confunda **deconectarea/sistarea fizică** cu **rezilierea contractuală** este o falsă echivalență. Baremul importat B este deci **cel puțin nesusținut față de A, care are suport legal afirmativ direct**.

**Vertical:** A `POSITIVE_ART58_4_A`; B `UNVERIFIED_SEPARATE_TERMINATION_GROUND`; C `ART58_6_DISCONNECTION_NOT_TERMINATION`. **Orizontal:** A↔B furt dovedit vs racordare ilegală (posibile coocurențe, dar condiții diferite); A↔C reziliere vs refuz garanție/deconectare; B↔C racordare ilegală vs măsuri după manipularea contorului. **Reversie:** A este **candidat solid**, dar nu se presupune exclusivitatea tuturor temeiurilor posibile din legislație fără art. 58(4)(c) și regulamentele de furnizare aplicabile. **Status `IMPORTED_B_NOT_ESTABLISHED; CANDIDATE_A_POSITIVE_ART58_4_NOT_APPLIED`**. Surse: Portal Legislativ art. 58(4)–(6) https://legislatie.just.ro/Public/DetaliiDocument/249550 ; Regulamentul de furnizare art. 41 https://legislatie.just.ro/Public/FormaPrintabila/00000G0QJUXGAKS9SDT0M9KUGP5VHX5C . Nu confundați anii actelor și aplicabilitatea exactă.

## R3 | G1-LEG-019 | cheie C importată, termen reglementări tehnice
**Enunț exact:** „Nerespectarea normelor tehnice emise de către ANRE constituie:”
- A. „Infracţiune”
- B. „Contravenţie”
- C. „Abatere”

**Context în 5 fraze:** Art. **93 alin. (1) pct. 5** din Legea 123/2012 plasează **nerespectarea reglementărilor tehnice/comerciale emise de ANRE** în enumerarea **contravențiilor**. Termenul generic „**abatere**” poate descrie o conduită neconformă în limbaj obișnuit, dar nu înlocuiește **calificarea contravențională** expresă atunci când se cere categoria sancționatorie din lege. Infracțiunea cere o normă penală distinctă și nu poate fi dedusă automat din încălcarea unui normativ tehnic. Varianta B corespunde calificării juridice demonstrate, pe când baremul importat C este mai puțin precis și potențial incompatibil cu întrebarea din categoria LEG. Totuși trebuie verificat **subiectul** (operator licențiat vs electrician persoană fizică, norme cu dispoziție sancționatorie specifică) înainte de extinderea universală.

**Vertical:** A `CRIMINAL_NOT_GENERAL`; B `POSITIVE_ART93_1_5_CONTRAVENTION`; C `GENERIC_WORD_ABATERE_NOT_SPECIFIC_LEGAL_CATEGORY`. **Orizontal:** A↔B tip sancțiune penal/contravențional; A↔C infracțiune vs termen generic; B↔C contravenție juridică vs etichetă necalificată. **Reversie:** B probabil în sensul explicit al legii, cu filtru pentru persoana/obligația reglementată. **Status `CRITICAL_IMPORTED_C_VS_ART93_CONTRAVENTION; CANDIDATE_B_NOT_APPLIED`**. Sursă Portal Legislativ Legea 123/2012 art. 93(1) pct. 5 https://legislatie.just.ro/Public/DetaliiDocument/249550 .

## R4 | G1-LEG-026 | cheie C importată, infracțiune expresă
**Enunț exact:** „Executarea sau folosirea de instalaţii clandestine în scopul racordării directe la reţea constituie:”
- A. „contravenţie”
- B. „infracţiune”
- C. „contravenţie sau infracţiune, după caz”

**Context în 5 fraze:** Art. **92 alin. (2)** din Legea 123/2012 se referă exact la **executarea sau folosirea instalațiilor clandestine în scopul racordării directe la rețea ori ocolirii măsurării**. Acest act stabilește direct **infracțiunea**, fără sintagma „după caz” pentru aceeași faptă descrisă. Alte încălcări ale regulilor de racordare pot constitui **contravenții**, dar sunt alte obiecte și nu pot fi introduse prin analogie într-un enunț care reproduce art. 92(2). Prin urmare, B este **probat textual** și C, deși mai cuprinzător lingvistic, reprezintă o **generalizare juridică fără suport pentru obiectul exact**. Aceasta este o eroare de tip `SPECIFIC_CRIMINAL_OFFENSE_VS_GENERIC_POSSIBILITY`.

**Vertical:** A `NOT_ART92_2`; B `EXACT_ART92_2_OFFENSE`; C `WRONG_AFTER_CASE_WHEN_ART92_EXPLICIT`. **Orizontal:** A↔B categorii juridice separate; B↔C în C apare posibilitate de contravenție în loc de infracțiune necondiționată pentru cazul dat; A↔C includere vagă care nu anulează tipul special. **Reversie:** B candidat **foarte puternic** pe text primar, **C importat este contrazis**. **Status `CRITICAL_IMPORTED_C_VS_ART92_2; CANDIDATE_B_NOT_APPLIED`**. Sursă Portal Legislativ https://legislatie.just.ro/Public/DetaliiDocument/212091 , art. 92(2).

## R5 | G1-LEG-048 | cheie A importată, conflict direct cu dreptul la plată
**Enunț exact:** „Clienţii casnici de energie electrică:”
- A. „pot impune furnizorului orice modalitate de plată, chiar dacă nu este pusă la dispoziţie de către acesta”
- B. „pot să opteze pentru orice modalitate de plată pe care furnizorul o pune la dispoziţie”
- C. „sunt obligaţi să achite facturile pentru energia electrică la una din casieriile furnizorului”

**Context în 5 fraze:** Legea 123/2012 **art. 57 alin. (2)** obligă furnizorul să pună la dispoziția clienților casnici **mai multe modalități de plată** și să le permită să aleagă dintre acestea. Nu există în acest articol dreptul clientului de a **impune orice metodă**, inclusiv una pe care furnizorul nu o oferă. Plata la casierie nu este **singura metodă obligatorie** într-un sistem care prevede mai multe alternative. Varianta B reproduce corect raportul dintre oferta furnizorului și dreptul de opțiune al clientului, iar A depășește acest drept. Baremul A importat este **direct contradicționat de dispoziția legii**.

**Vertical:** A `FALSE_UNLIMITED_METHOD`; B `POSITIVE_ART57_2_EXACT`; C `FALSE_EXCLUSIVE_CASH_DESK`. **Orizontal:** A↔B alegere limitată la oferta disponibilă vs impunere nelimitată; A↔C libertate nelimitată vs obligare la casierie, ambele extreme; B↔C libertate de opțiune vs restricție rigidă. **Reversie:** B are dovadă afirmativă independentă de eliminare. **Status `CRITICAL_IMPORTED_A_VS_ART57_2; CANDIDATE_B_NOT_APPLIED`**. Sursă Portal Legislativ https://legislatie.just.ro/Public/DetaliiDocument/300063 , art. 57(2).

## Preflight, QA și prioritate
- **5/5 rute structurale** completate cu toate trei comparațiile verticale, 3 perechi orizontale și verificarea inversă; validarea efectivă a textului a fost parțial prin fragmente indexate ale Portalului, nu expertiză juridică independentă.
- **Rezultat de risc major:** pentru 015, 019, 026, 048, o **altă literă decât cheia importată** are suport explicit în Legea 123/2012; pentru 017, A are temei de reziliere explicit, cheia B fiind neconfirmată ca temei propriu. **Nicio corecție canonică făcută** și nici o întrebare aprobată pentru învățare.
- **Escaladare tehnică necesară:** confruntare cu textul complet forma 26.07.2026 al art. 57/58/92/93, ediția exact cerută de ANRE pentru grad și sursa răspunsului importat, apoi QA juridic/lingvistic independent. Nu solicitați utilizatorului o decizie între barem și textul legii înainte de această confruntare.
- Stare `NOT_APPROVED_FOR_LEARNING` pentru toate; PR Draft intact. Exemplu transversal: **categoria juridică exactă nu se deduce din gradul de gravitate sau termenul generic „abatere”; numele actului juridic/obiectul/efectul (reziliere vs deconectare) au prioritate.**
