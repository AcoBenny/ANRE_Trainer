# CKPT-088 | P1 AH: documente dosar ANRE grad II, G2-LEG-067–073 | 2026-11-17

## Source, preflight, uniqueness
- Repo AcoBenny/ANRE_Trainer, PR #7 Draft, branch audit/anre-v8-priority-17-20261109. Bază CKPT-087: 230/568 unități, 285/822 grade IDs documentate. Acest lot are **7 unități distincte P1 / 7 ID-uri**, care nu sunt prezente în ACTIVE_EVIDENCE_INDEX_87 și nu au fișă în master: **237/568 unități / 292/822 grade IDs** contextual documentate. 0/822 approved for learning.
- **Important:** pagina oficială ANRE este o descriere a documentelor de autorizare, NU o atestare că enunțurile G2-LEG-067–073 sunt întrebări publicate de ANRE. Proveniența XLSX, ediția de examen și baremele rămân NOT_VERIFIED. Aceasta e cercetare contextuală preliminară; evaluator independent juridic/lingvistic NOT_RUN.
- Ediție: pagina oficială ANRE 2026, corelată cu Regulamentul 66/2023 art.16–17. Cerințele de dosar nu sunt automat identice cu toate situațiile speciale de candidat. Nicio mutație la master CSV, enunț, variante, chei, HTML, APK, main, merge ori release.

## G2-LEG-067 | AU-e5b313c78cd5c101
- Canonical QABC hash e5b313c78cd5c101401decb00d80e181d27cd9202ed044a30c490a6cf3a30a10; members G2-LEG-067; original key preserved {"G2-LEG-067":"A"}
- **Original:** Care dintre următoarele este prevăzută de ANRE ca document pentru solicitarea autorizării?
  - A. Cererea de autorizare completată electronic pe portalul ANRE sau în PCUe
  - B. Doar o cerere scrisă depusă fizic la ANRE
  - C. Doar recomandarea angajatorului
- **Sursa și locatorul:** ANRE, pagină oficială pentru autorizarea electricienilor, secțiunea A1.I (documente) și A1.II (acceptare dosar), publicată/actualizată pe anre.ro în 2026: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; Regulament autorizare aprobat prin Ordinul 66/2023, art.16–17: https://legislatie.just.ro/Public/FormaPrintabila/00000G2RBDQDDPVSF7E37YMIVAW4OEAQ .
- **Context:** A1.I(a): cererea electronică pe portalul ANRE/PCUe; cererea scrisă exclusiv fizic (B) omite canalele în vigoare, iar recomandarea de la angajator (C) nu substituie cererea.
- **Vertical ABC:** A=A_DOCUMENT_PORTAL_PCUE; B=B_ONLY_PHYSICAL_FALSE; C=C_EMPLOYER_RECOMMENDATION_NOT_REQUEST.
- **Orizontal:** A versus B diferența de canal electronic; A versus C cerere oficială versus recomandare; B versus C două substituții nevalide.
- **Reversie/caz negativ:** Un candidat completează pe PCUe și depune electronic, dovedind falsitatea exclusivității fizice din B.
- **Status:** A_MATCHES_ANRE_A1_I_OR_II; ORIGIN_AS_OFFICIAL_ANRE_QUESTION_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-LEG-068 | AU-303b00d1f9ada86e
- Canonical QABC hash 303b00d1f9ada86e2ff2e017482423867471ee105dcd8a60fff37148c34e2b8b; members G2-LEG-068; original key preserved {"G2-LEG-068":"A"}
- **Original:** Care dintre documentele următoare este indicat de ANRE în dosarul de autorizare?
  - A. Copia actului de identitate
  - B. Doar permisul de conducere
  - C. Doar certificatul medical
- **Sursa și locatorul:** ANRE, pagină oficială pentru autorizarea electricienilor, secțiunea A1.I (documente) și A1.II (acceptare dosar), publicată/actualizată pe anre.ro în 2026: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; Regulament autorizare aprobat prin Ordinul 66/2023, art.16–17: https://legislatie.just.ro/Public/FormaPrintabila/00000G2RBDQDDPVSF7E37YMIVAW4OEAQ .
- **Context:** A1.I(b) prevede copia actului de identitate. Permisul de conducere nu este formularul general indicat la lit.b, iar certificatul medical este alt tip de document; niciuna dintre B/C nu înlocuiește cartea de identitate cerută.
- **Vertical ABC:** A=A_ID_COPY_EXPLICIT; B=B_DRIVING_LICENCE_ONLY_FALSE; C=C_MEDICAL_CERTIFICATE_ONLY_FALSE.
- **Orizontal:** A/B identitate cerută vs permis; A/C identitate vs medical; B/C documente neechivalente cu dosarul.
- **Reversie/caz negativ:** Un candidat cu permis valabil dar fără actul de identitate cerut la lit.b nu satisface automat lista.
- **Status:** A_MATCHES_ANRE_A1_I_OR_II; ORIGIN_AS_OFFICIAL_ANRE_QUESTION_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-LEG-069 | AU-9a4cf19dace24b65
- Canonical QABC hash 9a4cf19dace24b65b7113ac7d5373048e66c70cce54fb47d88e85d53a7bf6b32; members G2-LEG-069; original key preserved {"G2-LEG-069":"A"}
- **Original:** Ce document trebuie să ateste calificarea profesională, conform informațiilor ANRE privind autorizarea?
  - A. Certificatele sau diplomele care atestă calificarea profesională
  - B. Doar o declarație verbală
  - C. Doar o recomandare de la un electrician autorizat
- **Sursa și locatorul:** ANRE, pagină oficială pentru autorizarea electricienilor, secțiunea A1.I (documente) și A1.II (acceptare dosar), publicată/actualizată pe anre.ro în 2026: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; Regulament autorizare aprobat prin Ordinul 66/2023, art.16–17: https://legislatie.just.ro/Public/FormaPrintabila/00000G2RBDQDDPVSF7E37YMIVAW4OEAQ .
- **Context:** A1.I(c) cere copii ale certificatelor sau diplomelor de calificare profesională. Declarația verbală și recomandarea altui electrician nu probează formal o calificare potrivit actului, chiar dacă pot constitui informații auxiliare. Pentru studii străine, art.17/A1.I(d) poate cere și document de recunoaștere.
- **Vertical ABC:** A=A_QUALIFICATION_DOC_EXACT; B=B_VERBAL_ONLY_UNACCEPTABLE; C=C_RECOMMENDATION_ONLY_UNACCEPTABLE.
- **Orizontal:** A/B document calificare versus susținere verbală; A/C act academic vs recomandare; B/C probe informale diferite.
- **Reversie/caz negativ:** Un electrician recomandat, fără diplomă ori certificat admisibil, nu acoperă cerința de calificare.
- **Status:** A_MATCHES_ANRE_A1_I_OR_II; ORIGIN_AS_OFFICIAL_ANRE_QUESTION_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-LEG-070 | AU-e95951c55b615828
- Canonical QABC hash e95951c55b6158288f099a0beac297ea6d7858a9a3cd7093e9565185b8122046; members G2-LEG-070; original key preserved {"G2-LEG-070":"A"}
- **Original:** Cum poate fi dovedită experiența profesională, acolo unde este cazul, conform informațiilor ANRE?
  - A. Prin carnet de muncă sau adeverințe și, după caz, raport/extras din Registrul de evidență a salariaților
  - B. Numai prin declarație verbală
  - C. Numai prin factura de energie electrică
- **Sursa și locatorul:** ANRE, pagină oficială pentru autorizarea electricienilor, secțiunea A1.I (documente) și A1.II (acceptare dosar), publicată/actualizată pe anre.ro în 2026: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; Regulament autorizare aprobat prin Ordinul 66/2023, art.16–17: https://legislatie.just.ro/Public/FormaPrintabila/00000G2RBDQDDPVSF7E37YMIVAW4OEAQ .
- **Context:** A1.I(e) permite copia carnetului de muncă, adeverințe și, după caz, extras/raport din evidența salariaților asumat prin semnătură, pentru dovada experienței *acolo unde este cazul*. Declarația verbală și factura de energie nu atestă experiența relevantă. Nu transforma «acolo unde este cazul» într-o cerință universală identică pentru toate tipurile de calificări.
- **Vertical ABC:** A=A_DOCUMENTED_EXPERIENCE_CONDITIONAL; B=B_VERBAL_ONLY_FALSE; C=C_UTILITY_BILL_FALSE.
- **Orizontal:** A/B acte verificabile vs verbal; A/C vechime vs consum; B/C ambele incapabile să ateste profesional experiența.
- **Reversie/caz negativ:** Candidat fără condiție legală de experiență minimă nu primește o obligație inventată doar din acest item; dovada A e modalitatea când cerința se aplică.
- **Status:** A_MATCHES_ANRE_A1_I_OR_II; ORIGIN_AS_OFFICIAL_ANRE_QUESTION_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-LEG-071 | AU-07b288aa04a87371
- Canonical QABC hash 07b288aa04a87371b6cc2a04e804a5e1f5f5289e33877f608e9db8903f3cdfd3; members G2-LEG-071; original key preserved {"G2-LEG-071":"A"}
- **Original:** Declarația de consimțământ privind colectarea și prelucrarea datelor personale este enumerată de ANRE în documentele pentru autorizare?
  - A. Da
  - B. Nu
  - C. Doar pentru verificatori
- **Sursa și locatorul:** ANRE, pagină oficială pentru autorizarea electricienilor, secțiunea A1.I (documente) și A1.II (acceptare dosar), publicată/actualizată pe anre.ro în 2026: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; Regulament autorizare aprobat prin Ordinul 66/2023, art.16–17: https://legislatie.just.ro/Public/FormaPrintabila/00000G2RBDQDDPVSF7E37YMIVAW4OEAQ .
- **Context:** A1.I(f) enumeră declarația de consimțământ pentru prelucrarea datelor completată electronic. A da este demonstrabil pentru dosarul electricianului; B neagă documentul, C limitează greșit obligația la verificatori. Documentul nu se substituie cu consimțământ implicit prin participare.
- **Vertical ABC:** A=A_LISTED_IN_ELECTRICIAN_A1; B=B_DENIAL_FALSE; C=C_ONLY_VERIFIERS_FALSE.
- **Orizontal:** A/B enumerat vs neenumerat; A/C toți candidații vizați vs numai verificatori; B/C două excluderi fără suport.
- **Reversie/caz negativ:** Dosarul de electrician are lit.f în secțiunea explicit A1, deci afirmația «doar verificatori» este contrazisă de poziția sursei.
- **Status:** A_MATCHES_ANRE_A1_I_OR_II; ORIGIN_AS_OFFICIAL_ANRE_QUESTION_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-LEG-072 | AU-9bd1329cb1a2c240
- Canonical QABC hash 9bd1329cb1a2c240a41825d0cb8bdf2f20ee60afdfe48506a74d00a91c8f575f; members G2-LEG-072; original key preserved {"G2-LEG-072":"A"}
- **Original:** Ce dovadă financiară este enumerată în dosarul de autorizare?
  - A. Copia chitanței de achitare a tarifului pentru autorizare
  - B. Extrasul de cont al angajatorului
  - C. Factura de energie electrică a locuinței
- **Sursa și locatorul:** ANRE, pagină oficială pentru autorizarea electricienilor, secțiunea A1.I (documente) și A1.II (acceptare dosar), publicată/actualizată pe anre.ro în 2026: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; Regulament autorizare aprobat prin Ordinul 66/2023, art.16–17: https://legislatie.just.ro/Public/FormaPrintabila/00000G2RBDQDDPVSF7E37YMIVAW4OEAQ .
- **Context:** A1.I(g) include copia chitanței plății tarifului pentru autorizare. Extrasul contului angajatorului și factura de energie a locuinței nu demonstrează plata taxei ANRE de autorizare. Calea de plată poate fi cont/casierie, ceea ce nu echivalează cu orice extras bancar fără identificarea plății.
- **Vertical ABC:** A=A_FEE_PROOF_EXACT; B=B_EMPLOYER_STATEMENT_NOT_RECEIPT; C=C_HOME_ELECTRIC_BILL_NOT_RECEIPT.
- **Orizontal:** A/B chitanță taxă ANRE vs extras generic; A/C chitanță vs factură utilități; B/C probe financiar diferite, dar nevalide.
- **Reversie/caz negativ:** O factură casnică achitată nu este aceeași obligație fiscală ca tariful pentru examen.
- **Status:** A_MATCHES_ANRE_A1_I_OR_II; ORIGIN_AS_OFFICIAL_ANRE_QUESTION_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## G2-LEG-073 | AU-11a4e32b38e7bdf4
- Canonical QABC hash 11a4e32b38e7bdf4c0678564db341423e2aa4e768dcb5ae3dcec7e144a4c57d1; members G2-LEG-073; original key preserved {"G2-LEG-073":"A"}
- **Original:** Pentru acceptarea dosarului de autorizare, cererea trebuie să fie însoțită de toate documentele cerute de regulament?
  - A. Da
  - B. Nu
  - C. Doar de actul de identitate
- **Sursa și locatorul:** ANRE, pagină oficială pentru autorizarea electricienilor, secțiunea A1.I (documente) și A1.II (acceptare dosar), publicată/actualizată pe anre.ro în 2026: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; Regulament autorizare aprobat prin Ordinul 66/2023, art.16–17: https://legislatie.just.ro/Public/FormaPrintabila/00000G2RBDQDDPVSF7E37YMIVAW4OEAQ .
- **Context:** A1.II(b) cere ca solicitarea să fie însoțită de **toate documentele cerute de regulament**. Aceasta este o cerință de completitudine, nu promisiune că orice dosar complet este automat admis; mai există condiții A1.II(a)/(c) privind formularul și experiența în cazurile prevăzute. B neagă condiția de completitudine; C limitează greșit documentația la actul de identitate.
- **Vertical ABC:** A=A_COMPLETENESS_NECESSARY_NOT_SUFFICIENT; B=B_DENIES_ALL_DOCS; C=C_ONLY_ID_FALSE.
- **Orizontal:** A/B complet vs incomplet; A/C toate actele vs unul singur; B/C negație generică versus listă subinclusivă.
- **Reversie/caz negativ:** Dosar cu CI dar fără diplomă nu este complet conform A1.I, contraexemplu la C.
- **Status:** A_MATCHES_ANRE_A1_I_OR_II; ORIGIN_AS_OFFICIAL_ANRE_QUESTION_UNVERIFIED; INDEPENDENT_QA_NOT_RUN; APPROVED_FOR_LEARNING_NO.

## Gates
- Test negativ anti-distorsiune: pentru experiență, «acolo unde este cazul» nu poate fi eliminat; pentru completitudine, toate documentele sunt condiție necesară, nu acceptare automată.
- Suspiciune structurală: toate cele șapte răspunsuri importate sunt A, necesită verificare separat față de fișierul-sursă (posibilă ordine artificială a opțiunilor). Nu se modifică răspunsurile.
- Următoarea etapă G2-LEG074–080 în aceeași sursă, apoi testare de unicitate/ediție și QA independent.
