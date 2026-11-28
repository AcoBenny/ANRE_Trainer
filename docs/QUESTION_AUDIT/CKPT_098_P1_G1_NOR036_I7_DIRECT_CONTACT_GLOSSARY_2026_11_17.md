# CKPT-098 | P1 G1-NOR-036, atingere directă, I7 cap.2, 2026-11-17

## Bază și identitate
- AcoBenny/ANRE_Trainer, branch audit/anre-v8-priority-17-20261109, PR #7 Draft/Unmerged. Baseline CKPT097 **292/568 unități, 347/822 ID-uri** contextual documentate; această unitate G1-NOR-036 era fără fișă în MASTER și fără credit în arhiva CKPT043–049. **+1/+1 ⇒ 293/568 unități și 348/822 ID-uri**, **0/822 approved for learning**.
- Original întrebare A/B/C și cheia B din MASTER; qabc_sha256 f97b290dc4f08c185f2cb6139a67152e51f40bacfb2540ea91251a62f5311b4a; unit AU-f97b290dc4f08c18. Anterior o propunere de lot G1-NOR036–040 a fost **blocată** deoarece NOR037–040 erau deja în CKPT047/048. Acum se creează strict fișa NOR036; nu se recreditează celelalte patru.
- Sursa de obiect: I7-2011, cap. 2 «Terminologie și abrevieri», definiția «atingere directă» și vecina «atingere indirectă», document original oficial https://legislatie.just.ro/Public/DetaliiDocument/287132 . Forma oficială este indexată în Portal Legislativ, dar încărcarea completă prin browser a returnat **502**; textul celor două definiții a fost verificat în copia textuală https://lexapp.ro/legislatie/reglementare-tehnica-normativ-proiectarea-executia-exploatarea-2011/ și într-o copie istorică a I7/2011 https://www.sibotherm.com/wp-content/uploads/Normativ-I7-2011-Monitor-Electrice.pdf . Compatibilitatea cu ediția ANRE folosită la examen 2026 rămâne de confirmat; nu se pretinde o captură PDF nouă pentru această sursă.

## G1-NOR-036 | AU-f97b290dc4f08c18
- **Original:** Se consideră atingere directă:
  - A. contactul persoanelor sau animalelor domestice sau de crescătorie cu mase puse accidental sub tensiune datorită unui defect electric
  - B. contactul direct al persoanelor sau al animalelor cu părţi active
  - C. contactul persoanelor sau animalelor domestice sau de crescătorie cu părţi ale unei instalaţii electrice
- **Barem importat (NEAPLICAT):** {"G1-NOR-036":"B"}.
- **Context și paragraful vecin:** I7 cap.2 definește **atingerea directă** ca contactul persoanelor ori al animalelor cu **părți active**. Definiția imediat vecină pentru **atingere indirectă** descrie contactul cu **părți conductoare accesibile devenite sub tensiune ca urmare a unui defect**. Enunțul A amintește mase puse accidental sub tensiune din cauza defectului, prin urmare descrie atingere **indirectă**, nu directă. B folosește expresia normativă exactă «contactul direct ... cu părți active», fiind opțiunea pozitiv susținută. C vorbește generic despre părțile instalației, fără calificativul «active» și fără distincția regim normal/defect.
- **Vertical:** A=CONTRADICTED_INDIRECT_DEFINITION; B=EXACT_DIRECT_CONTACT_GLOSSARY; C=GENERIC_PARTS_NOT_ENOUGH_TO_DEFINE_DIRECT_CONTACT.
- **Orizontal:** A↔B (masă sub tensiune din defect vs parte activă normal) sunt fenomene distincte; A↔C (mase de defect vs oricare componente) nu echivalează; B↔C presupune **active**, absent din C.
- **Reversie/test negativ:** Contactul cu un conductor de fază dezizolat = atingere directă B; contactul cu o carcasă metalică devenită sub tensiune în urma unui defect de izolație = atingere indirectă A. Dacă atingerea unei carcase neenergizate ar fi clasificată ca directă, definiția s-ar prăbuși; C este astfel insuficientă.
- **Stare:** IMPORTED_B_SUPPORTED_BY_I7_DEFINITION, EDITION_EXAM_2026_NOT_CERTIFIED, INDEPENDENT_QA_NOT_RUN, APPROVED_FOR_LEARNING_NO.

## Cross-check și gate
- Fișele NOR037–040 există anterior în CKPT047/048; sunt parteneri didactici pentru definiții, nu noi unități. Fără duplicarea lor, fără suprapunere de contori.
- Informația exactă din I7 cap.2 trebuie confruntată cu PDF-ul oficial aplicabil examinărilor 2026 și reviewer independent; interpretarea școlară nu certifică singură cheia oficială.
- Nu modificați QABC, barem, CSV, HTML/APK/main și nu faceți merge/release.
