# Plan de finalizare ANRE Trainer | 822 ID-uri | 2026-11-19

## Baza verificată
- Ramură: `audit/anre-v8-priority-17-20261109`, PR #7 Draft, fără merge.
- Referință: CKPT-250 + V129 la commit `45ea75e1c6b25a4cf672284c758876892b5968f2`.
- `822/822` ID-uri au legătură către o dovadă focalizată, după reconcilierea ultimelor 37 de poziții P2. Acest procent măsoară **acoperirea documentară**, nu răspunsuri corecte certificate.
- Corpusul anterior: `568` grupuri QABC distincte / `822` ID-uri de grad. Recalculează grupurile la pornirea reconcilierii și raportează orice diferență; nu credita duplicatele ca investigații noi.
- `0/822` aprobări pentru învățare; recenzia tehnică și lingvistică realmente independentă și certificarea ediției relevante sunt încă bariere.
- Cel puțin `76` itemuri au proveniență `TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE` în V63/V64; nu le prezenta drept întrebări originale ANRE. Restul nu devine implicit oficial.

## Etapa 1. Eliminarea conflictelor și a ambiguităților cu impact mare
1. Generează o matrice de **unități QABC distincte**, nu doar rânduri, din registrul V129/V73 și dovezile CKPT. Fiecare rând: ID-uri echivalente, text + A/B/C nemodificate, cheile importate, proveniență, grad/bibliografie, sursă originală + versiune + paragraf, interpretare, toate contraexemplele, reviewer și stare.
2. Prima coadă: conflictele cu bareme diferite la aceeași întrebare (**G1-ELE-018/G2-ELEC-170** și **G1-ELE-102/G2-ELEC-245**); apoi cazurile sursă/semantică **G1-ELE-122, G1-ELE-219, G1-ELE-226, G1-NOR-027, G1-NOR-029, G1-NOR-032, G1-NOR-028** și conflictele legislative **LEG019/026/034/048**; ordonează restul după blocaj verificabil și reutilizează dovezile existente. Nu schimba chei pe baza eliminării opțiunilor.
3. Pentru fiecare conflict, înregistrează diferența dintre **barem importat**, **răspuns intenționat**, **concluzie tehnică** și **eventuală cheie oficial demonstrată**. Citește sursa cu antet/context/derogări, aplicabilitate la grad și ediție; verifică A/B/C separat. Dacă nu există dovadă suficientă, marchează `BLOCKED` cu motiv și exact ce probă lipsește, nu `PASS`.

**Ieșire:** matrice de contradicții fără conflicte ascunse; fiecare caz are verdict motivat sau blocaj explicit și urme de verificare.

## Etapa 2. Validarea finală a întregului set
1. Audit o singură dată pentru fiecare dintre cele `568` unități QABC (numărul trebuie recalculat). Reutilizează la toate ID-urile de grad numai dacă **Q+A+B+C** sunt identice și gradul nu modifică norma/interpretarea. Distingere obligatorie între `SOURCE_RESEARCHED`, `INDEPENDENT_OPTION_QA`, `EDITION_VERIFIED` și `LEARNER_APPROVED`.
2. Un verificator distinct de autor recitește sursa originală, verifică exact obiectul/condițiile/excepțiile și analizează independent A/B/C. Pentru legislație, validează forma aplicabilă și bibliografia examenului, nu doar un rezumat web. Pentru întrebările create intern, validează corectitudinea tehnică, marchează `TRAINER_AUTHORED` și separă-le clar de corpusul oficial.
3. Rulează validările automate: `822` ID-uri unice, `17` coloane în V129, parse CSV cu suport pentru câmpuri citate, maparea corectă a câmpurilor, chei QABC imutabile, duplicate și contradicții, linkuri ancore/ediții, teste negative pentru excepții (inclusiv NOR032 I7 generic vs PE155 specific). **Nu confunda QA structural cu certificare de barem.**

**Ieșire:** un registru consolidat cu o stare demonstrabilă per ID și un raport separat al blocajelor. Nu marca întregul set `approved` dacă există probleme sau lipsesc revizori real independenți.

## Etapa 3. Handoff în aplicație, numai după poarta de conținut
1. Exportă pentru aplicație întrebări, grade, opțiuni, răspunsuri autorizate, explicații concise, capcane, sursa + versiunea + ancora locală, proveniența și un indicator de verificare; nu publica explicații nesigure ca fapte.
2. Testează build-urile HTML offline și APK Android real: randomizare, evaluare A/B/C, repetarea greșelilor, progres, deduplicare cross-grad, popup cu fragmentul sursei și funcționare fără internet; teste negative și regresii.
3. Produce un release candidate după QA și raport de diferențe. **Nu modifica baremele canonice/HTML/APK în faza de audit**, nu face merge/release și nu prezenta aplicația drept sigură pentru învățare fără gate de aprobare explicit.

**Ieșire:** pachet de date validat + raport QA + candidat de aplicație testat doar după aprobarea fazei de conținut.

## Politica de execuție și raportare
- Continuă autonom în loturi de aproximativ 15–20 unități distincte, cu checkpoint incremental. Nu solicita utilizatorului intervenție pentru simplele rânduri de rutină.
- Escaladează utilizatorului numai întrebarea exactă, A/B/C și contradicția reală când datele sunt insuficiente sau trebuie aleasă o interpretare; observațiile utilizatorului sunt ipoteze pentru verificare, nu semnături de sursă.
- Raport scurt la fiecare checkpoint: `unități revizuite / unități rămase / conflicte deschise / aprobări reale / blocaje` și fișierele/commitul. Nu eticheta recenzia făcută de un singur asistent drept QA independent.
- Păstrează V129 și toate registrele istorice ca dovezi; corecțiile sunt **versionate și justifică supersedarea**, nu șterg concluziile anterioare.

## Neural Academy / Avengers Asamble training bridge (2026-11-19)
- The Academy is coupled to this existing one-pass audit; do **not** start parallel duplicate question rechecks. Role routing, exact-scope sources, Romanian linguistics, data audit, challenges, read-only evidence and staged QA are specified in [the training bridge](ANRE_NEURAL_ACADEMY_TRAINING_BRIDGE_2026_11_19.md).
- Pre-registered, safe [pilot exercises](ANRE_ACADEMY_PILOT_CASES_2026_11_19.json) cover two cross-grade key conflicts and three failure classes (exclusive wording, source-scope mismatch, missing physical assumption).
- Use actual installed Avengers Asamble and Precision Lab *skills* as workflow guides where relevant. Skills and role cards are not autonomous agents. Independent AI/multi-model execution, baseline-vs-skill trials and independent QA must be evidenced separately or remain `NOT_RUN`.
- Feedback is saved as versioned, redacted, source-linked transferable lessons and negative fixtures; only promote to Academy code/registry after real repeatable evaluation and approval. Content QA for ANRE remains the priority, and approval counts remain evidence-gated.
