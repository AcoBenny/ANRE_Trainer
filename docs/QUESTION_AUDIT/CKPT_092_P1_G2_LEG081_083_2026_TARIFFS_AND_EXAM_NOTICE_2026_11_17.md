# CKPT-092 | G2-LEG081–083: tarife 2026 și publicarea sesiunilor, 17.11.2026

## Bază și sursă oficială
- AcoBenny/ANRE_Trainer, audit/anre-v8-priority-17-20261109, PR #7 Draft/Unmerged. Bază CKPT-091: **250/568 unități, 305/822 ID-uri** cu fișe contextuale; se adaugă **3 P1 distincte / 3 ID-uri** necreditate (MASTER, CKPT043–091), total provizoriu **253/568 și 308/822**; **0/822 aprobate pentru învățare**.
- **Sursa principală cu adevărat aplicabilă anului 2026:** Ordinul ANRE **82/16.12.2025**, publicat în Monitorul Oficial nr.1176/18.12.2025, art.2 și Anexa nr.3 Tabel 1 rândurile 2–5: https://legislatie.just.ro/Public/FormaPrintabila/00000G02MV7ZC18ASQV1AOVO1CXFUCI2 . 250 lei grad II A sau B, 500 lei A+B, 125 lei vizare A/B și 250 lei vizare A+B.
- **Notă anti-eroare de ediție:** pagina oficială ANRE https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ conține în porțiunea explicativă un antet mai vechi «Tarifele în vigoare aprobate prin Ordin 118/2023»; **nu** cităm acel antet drept sursă 2026. Actul 82/2025 fixează explicit tarifele pentru anul 2026 și are prioritate temporală. Nu am identificat o modificare ulterioară care să schimbe aceste rânduri în sursele deschise, dar verificarea integrală a actelor ulterioare rămâne poartă.
- Teste: identitate și chei QABC din master; exact 3 variante/card; vertical, orizontal, reversie și diferență între autorizație și vizare. QA independent surse/juridic/lingvistic **NOT_RUN**; proveniența ca întrebare oficială ANRE **UNVERIFIED**. Fără modificări la chei, întrebări, HTML/APK/main, fără merge.

## G2-LEG-081 | AU-bd2691e93b5d1acc
- qabc_sha256 bd2691e93b5d1acc07b2ac97d062cb62e14bf83fc942be40059316f0c0455c92; member_ids G2-LEG-081; barem intact {"G2-LEG-081":"A"}
- **Original:** Conform tarifelor publicate de ANRE, care este tariful pentru autorizarea Gradului II de tip A sau de tip B?
  - A. 250 lei
  - B. 125 lei
  - C. 500 lei
- **Locator normativ:** Ordin ANRE nr.82/16.12.2025, art.2 și Anexa nr.3, tabel 1, rând 2
- **Dovadă pozitivă:** 250 lei.
- **Vertical ABC:** A = 250 lei: valoarea pozitivă a tarifului de autorizare grad II, pentru tip A SAU tip B; B = 125 lei: tariful pentru vizare periodică A sau B (rând 3), nu autorizarea inițială; C = 500 lei: tariful pentru tip A+B (rând 4), nu unul singur.
- **Orizontal ABC:** A↔B autorizare inițială vs vizare periodică; A↔C un singur tip vs autorizare comună A+B; B↔C vizare un singur tip vs autorizare dublă.
- **Reversie și contraexemplu:** Caz de test: candidat doar IIA plătește 250 lei. Dacă solicită concomitent IIA+IIB, tariful aplicabil este 500 lei, nu 250. La vizarea IIA, taxa e 125 lei. Nu confundați «A sau B» cu «A+B».
- **Statut:** A_DIRECT_OFFICIAL_TARIFF_2026_EXACT; OFFICIAL_EXAM_QUESTION_PROVENANCE_PENDING; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-082 | AU-2beb2cf09ad73f7b
- qabc_sha256 2beb2cf09ad73f7b0e747446b39b1f344db3494676e3ec773409e1cdff31d957; member_ids G2-LEG-082; barem intact {"G2-LEG-082":"A"}
- **Original:** Conform tarifelor publicate de ANRE, care este tariful pentru autorizarea Gradului II de tip A+B?
  - A. 500 lei
  - B. 250 lei
  - C. 125 lei
- **Locator normativ:** Ordin ANRE nr.82/16.12.2025, art.2, Anexa nr.3 tabel 1, rândurile 2, 4, 5
- **Dovadă pozitivă:** 500 lei.
- **Vertical ABC:** A = 500 lei: autorizare pentru tip A+B la grade II/III/IV, rândul 4; B = 250 lei: se aplică autorizării A sau B separat, ori vizării A+B, nu autorizării comune; C = 125 lei: vizare periodică A sau B separat, nu autorizare A+B.
- **Orizontal ABC:** A↔B autorizare A+B vs autorizare singulară sau vizare A+B; A↔C autorizare dublă vs vizare singulară; B↔C 250 vs 125 aplicabile altor operațiuni.
- **Reversie și contraexemplu:** Dacă o persoană solicită pentru grad II atât proiectare A, cât și execuție B, rândul 4 dă 500 lei; dacă doar vizarea A+B, rândul 5 dă 250 lei. Cuvântul «autorizare» decide între opțiunile A/B.
- **Statut:** A_DIRECT_OFFICIAL_TARIFF_2026_EXACT; OFFICIAL_EXAM_QUESTION_PROVENANCE_PENDING; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-LEG-083 | AU-bdede3f2fefe080e
- qabc_sha256 bdede3f2fefe080eb2eb73adb86ee188b9834850866ae806f3701782166330bb; member_ids G2-LEG-083; barem intact {"G2-LEG-083":"A"}
- **Original:** Unde este publicat, de regulă, anunțul privind desfășurarea unei sesiuni de autorizare?
  - A. Pe pagina de internet a Autorității competente
  - B. Doar la sediul angajatorului
  - C. Doar în presa locală
- **Locator normativ:** ANRE pagina Energie electrica, secțiunea A1.III «Organizarea și tematica examenului de autorizare»
- **Dovadă pozitivă:** Pe pagina internet a autorității competente.
- **Vertical ABC:** A: susținută exact de pagina oficială ANRE, anunțul se publică pe pagina autorității competente; B: sediul angajatorului nu e sursa oficială obligatorie și «doar» exclude publicarea ANRE; C: presa locală poate prelua un anunț, dar «doar» exclude pagina oficială ANRE.
- **Orizontal ABC:** A↔B instituție publică de reglementare vs angajator privat; A↔C web oficial vs ziar; B↔C două locuri neoficiale cu cuantificator absolut «doar».
- **Reversie și contraexemplu:** Un candidat fără angajator poate vedea anunțul pe ANRE. Publicarea pe web-ul oficial invalidează «doar la sediu» și «doar în presa locală», fără a interzice retransmiterea în alte canale.
- **Statut:** A_DIRECT_ANRE_WEBSITE_A1_III; OFFICIAL_EXAM_QUESTION_PROVENANCE_PENDING; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## Gates
- Cele trei chei sunt A, dar **nu există** dovadă că toate aceste întrebări în forma originală provin din XLSX oficial ANRE. Aceeași observație pentru G2-LEG001–006 și 067–080.
- Control de regresie de neconfundat: autorizare II A/B = 250; autorizare II A+B = 500; vizare A/B = 125; vizare A+B = 250; Ordin 82/2025 pentru 2026, nu Ordin 118/2023.
- QA independent, versiunile legislative și proveniența XLSX înainte de aprobarea pentru trainer; 0/822 aprobate.
