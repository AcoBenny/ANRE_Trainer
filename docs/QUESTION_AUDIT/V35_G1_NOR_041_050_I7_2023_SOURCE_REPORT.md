# ANRE Trainer V35: G1-NOR-041–050, verificare exactă I7 + capcane lingvistice
**Data:** 2026-11-11. **Sursa întrebărilor:** HTML V10.29 blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`; fișier original `NORME-TEHNICE-Gr.-1-05.2023 (1).xlsx`, rânduri 48–57. **Sursa normativă:** PDF-ul utilizatorului `803493174-I7-2011-completat2023(1).pdf`, versiune sintetică 22.09.2023, 249 pagini. Originalul are SHA-256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`.

Nu sunt modificări de barem, opțiuni sau HTML/APK. **QA independent NOT_RUN.** Corespondența cu forma oficială consolidată https://legislatie.just.ro/Public/DetaliiDocument/286763 este verificată **parțial prin text indexat**; istoria legislativă integrală din 2026 nu este încă adjudecată, iar clauzele de tranziție trebuie respectate.

## Material verificat efectiv
- PDF **p.55** a fost **randat și inspectat vizual**, secțiunea **5.2.4.6.1(a–d)**. Prescrie secțiune N egală cu faza în circuite monofazate **cu două conductoare**, indiferent de secțiune; în circuite polifazate pentru fază **≤16 mm² Cu / ≤25 mm² Al**; și în condiții cu armonici 3 ori distribuție neechilibrată. Aceasta este exact clauza cheie pentru 041–042.
- PDF p.52–53 text `5.2.3.0.1–0.2` și `5.2.3.1`, anexele **5.5, 5.10–5.17**: curentul admisibil ține de secțiune, material, izolație, metodă de pozare și de disiparea termică. Un cablu mai lung afectează și căderea de tensiune, dar lungimea nu este parametrul primar pentru curentul permanent de încălzire în condiții uniforme.
- PDF **p.63 randat și inspectat**, **5.3.1.7.2.1**: protecția la suprasarcini a motoarelor monofazate cel puțin pe conductorul activ **nelegat la pământ**.
- PDF **p.70 randat și inspectat**, **5.4.13**: soneria sau transformatorul soneriei se poate alimenta din circuitul de iluminat, de prize ori direct din tablou.
- PDF **p.209 randat și inspectat vizual**, **Anexa 5.32, tabel rând 1.2**: minim **2,5 mm² Cu** pentru faza circuitelor de prize monofazate; câmpul corespunzător Al nu are valoare în acea linie.

## Rezultate precise (cheile rămân cele din aplicație)

| ID | Cheie | Candidat/propunere | Argument și limită | Status |
|---|---|---|---|---|
| G1-NOR-041 | B | B numai condiționat | B include pragul corect de 16Cu/25Al, dar folosește expresia **„monofazate cu trei conductoare”** în loc de **„cu două conductoare”**, cum spune I7. Posibilă convenție „+PE” în numărarea firelor; necesită redactor și expert să clarifice. A și C nu sunt exact valabile. | **AMBIGUU, de verificat formularea** |
| G1-NOR-042 | B | **A** | A reproduce exact clauza **monofazat, două conductoare, indiferent de secțiune**. B introduce trei conductoare și praguri eronate (25Cu/35Al). | **CONFLICT DE CHEIE CU SURSA** |
| G1-NOR-043 | C | C | Valoarea curentului admisibil depinde de secțiunea conductorului. | Sursă 2023 susține |
| G1-NOR-044 | B | B | Depinde și de material (Cu/Al). | Sursă 2023 susține |
| G1-NOR-045 | B | B | Depinde de izolație și temperatura de funcționare (PVC/XLPE). | Sursă 2023 susține |
| G1-NOR-046 | A | A | Depinde de modul de montare/pozare și evacuarea căldurii. | Sursă 2023 susține |
| G1-NOR-047 | A | A | Pe conductorul activ nelegat la pământ: pentru L/N uzual, conductorul de fază. | Sursă 2023 susține, cu această condiție |
| G1-NOR-048 | A | A | A include toate cele trei căi de alimentare acceptate de 5.4.13. | Potrivire directă |
| G1-NOR-049 | B | B | B este una dintre căile permise (iluminat); A și C formulează **„numai”**, fals față de 5.4.13. **Nu** confunda răspunsul B cu o listă exhaustivă. | Potrivire directă cu explicație lingvistică |
| G1-NOR-050 | A | A | Anexa 5.32, rând 1.2: 2,5 mm² Cu. | Potrivire directă, tabel vizual verificat |

## QA și concluzii
- **10/10** înregistrări originale vizate și confruntate cu capitole/pagini I7, **0 modificări cheie**.
- **1 conflict de cheie clar în ediția 2023**: G1-NOR-042 (B actual, A susținut).
- **1 potențial defect de redactare**: G1-NOR-041 (două vs trei conductoare).
- **8 întrebări** susținute de textul I7 2023, cu observații pentru 047 și 049. Aceste clasificări **nu sunt aprobări QA independente** și nu demonstrează automat actualitatea normativă din 2026.
- Împreună cu V33 (4 ID-uri) și V34 (9 ID-uri), **23 de ID-uri** au acum reverificări individuale noi în ultimele loturi; celelalte **799** nu au fost reverificate la aceeași profunzime.
- După aprobarea independentă se poate propune corecția cheilor și a textelor, **numai cu aprobarea utilizatorului**. Fără merge/release; documentație numai pe PR #7 Draft.

## Următorul lot
G1-NOR-051–060; în paralel rezolvarea edițiilor/derogărilor pentru 13 întrebări prioritare V33–V34 și pregătirea verificării sistematice a restului de 799 întrebări. Nu inventa surse ori concluzii de barem.
