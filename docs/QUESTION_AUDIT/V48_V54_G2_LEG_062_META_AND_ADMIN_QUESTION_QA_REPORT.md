# ANRE Trainer | V48–V54 | Toate cele 62 de înregistrări G2-LEG verificate după sursele citate
Data: 2026-11-11. Baza canonică: V10.29, `app/src/main/assets/anre_trainer.html`, blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`.

## Defalcarea celor 62
- **45 de întrebări** sunt formulate din rândurile tabelului oficial **„Tematica şi bibliografie pentru examenul de autorizare electricieni” ANRE 05.2023**; 9 ID-uri `G2-LEG-001–009` și 36 `G2-LEG-100–135`. Sursa originală verificată vizual şi textual pe paginile 1–2 ale PDF-ului: https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf . Documente în tabel: Legea 123/2012 (rând 2), Ord 5/2023 (3), Ord 59/2013 (4), Ord 128/2008 (7), Ord 46/2021 (8), Ord 66/2023 (10), Ord 134/2021 (11), Ord 102/2015 (12), Ord 128/2020 (13). Coloana Grad II = `DA`. **Adevărul bibliografic** nu certifică faptul că întrebările sunt preluate din fișierul de *exemple de grile ANRE*.
- **17 întrebări administrative** `G2-LEG-067–083` sunt bazate pe pagina ANRE de informații despre autorizare, care enumeră documentele pentru dosar, 2 sesiuni de examen/an de regulă, viză la 5 ani, minimum 20 ore de pregătire, registru electronic, tarife: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ . Pentru `081`, `082`, valorile 250/500 lei au legătură cu Ordinul ANRE 118/2023 şi sunt marcate `TARIFF_DATE_RECHECK` până la verificarea completă a ordinelor ulterioare.
- **Toate cele 62 chei canonice sunt A**. Este un model de răspuns puternic dezechilibrat (100% A) și întrebare despre *documente bibliografice/administrative*, nu demonstrarea cunoștințelor tehnice. Se recomandă **carantină didactică** până la stabilirea provenienței reale și o decizie privind înlocuirea cu întrebări verificabile din sursa oficială Excel `LEGISLATIE-GR.-2-05.2023.xlsx`.
- Sursa XLSX oficială este linkată pe pagina ANRE, însă accesul web la binar a returnat `unsupported content-type` și descărcarea din container a eșuat. **Nu inventăm o comparație cu XLSX originală**.

## QA probator
- 62 ID-uri unice citite din V10.29, conținut integral enunț/A/B/C/cheie/sursă originală/rând, plus loc de verificare și statut, într-un CSV: `V48_V54_G2_LEG_062_BIBLIOGRAPHY_AND_ADMIN_SOURCE_QA.csv`.
- **Corespondența răspunsului A cu sursa de bază** este susținută la nivel de *fapt bibliografic/administrativ* (cu excepția gate-urilor temporale). Acest verdict NU este validare a autenticității întrebării ca grilă ANRE sau a valorii sale educaționale pentru examen.
- 0 aprobări ale unui evaluator tehnic/lingvistic independent, 0 integrare, 0 schimbări de barem, 0 HTML/APK/main, 0 merge.
- Împreună cu `G2-NOR-136–147` și `G2-NORM-001–003`, **toate cele 77 de înregistrări non-electrotehnice ale Gradului II au cheia A**. Dintre acestea, 3 (G2-NOR-137/141/145) sunt invalide prin lipsa unei opțiuni care să fie un *act de aprobare*. Acest tipar justifică un **P0 QA gate** înainte ca aplicația să fie folosită pentru examen.

## Următorul pas
Continuă electrotehnica G1-ELE/G2-ELEC prin surse tehnice/didactice reale și transformă proveniența celor 77 de elemente non-electrotehnice Grade II într-un verdict de autenticitate după obținerea unui fișier ANRE XLSX verificat. Nu modifica aplicația, nu atribui validarea independentă unui model.
