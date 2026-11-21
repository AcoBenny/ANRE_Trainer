# ANRE Trainer | V39–V40 | Audit întrebări G1-NOR-081–100
Data: **2026-11-11**. Prioritate utilizator: **822 de întrebări verificate ÎNAINTE de dezvoltarea sau livrarea aplicației** (GitHub issue #10 corectat). Nu se schimbă bareme, ABC, HTML, APK ori main.

## Sursele reale consultate
- Baza originală: GitHub `app/src/main/assets/anre_trainer.html` V10.29, blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`; 20/20 ID-uri reale, variante și chei, source XLSX `NORME-TEHNICE-Gr.-1-05.2023 (1).xlsx`, rânduri 88–107.
- PDF local încărcat de utilizator `803493174-I7-2011-completat2023(1).pdf`, 249p, sinteză 22.09.2023, SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`. Textul articolelor a fost extras local; nu a fost necesar OCR.
- Textul Portalului Legislativ https://legislatie.just.ro/Public/DetaliiDocument/286763, https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132, consultat pentru 3.0.3.7, 5.1.4.3.3, 5.2.12.2.12, 5.5.7.11. Istoria exhaustivă de modificare ulterioară 12.07.2023 și comparația cu MO pe toate cele 20 **NU** sunt certificate.

## V39 (081–090): rezultat pe surse
| ID | Cheie originală | Reper | Verdict preliminar |
|---|---|---|---|
| 081 | C | **3.0.3.7**, p13 | I7 cere cabluri *rezistente la foc ȘI cu întârziere la propagarea flăcării*. C are numai a doua condiție; nu certificăm un răspuns unic fără definiție de produs |
| 082 | B | **3.0.3.7**, p13 | B conține numai „rezistente la foc” fără a afirma și întârzierea flăcării; nu certificăm unicitatea |
| 083 | B | 5.4.8 p70 | B, contact PE la prize 230V, direct |
| 084 | B | Capitol 2 definiție PE p6 | B, rol de securitate/șoc |
| 085 | C | Capitol 2 legare la pământ p8 | C, rețea sau echipament, în timp ce norma include și instalația |
| 086 | B | 3.0.3.1–4 p11–13 | B, trasee comune condiționate |
| 087 | C | 5.5.3.2 p72 | C, conductele pentru gaze/lichide inflamabile nu se folosesc ca PE |
| 088 | A | 4.1.5.3.8 p30 | A, învelișuri metalice de distribuție prefabricată pot fi PE dacă 3 condiții cumulative sunt asigurate |
| **089** | **A** | **5.1.4.3.3 p47** | **CONFLICT DIRECT**: textul I7 *permite* o singură culoare pentru conductoarele de fază ale unui circuit, cu marcaj adecvat la ambele capete, deci varianta **B** |
| **090** | **B** | **5.2.12.2.12 p61** | **CONFLICT DE FORMULARE**: textul normativ spune că metalul „se poate monta direct” pe combustibil, corespunzător literal variantei **C**. B („condiționat”) poate fi adevărată în anumite amplasamente cu condiții suplimentare; revizie de unicitate |

## V40 (091–100): rezultat pe surse
| ID | Cheie originală | Reper | Verdict preliminar |
|---|---|---|---|
| 091 | B | 5.2.12.3.7–8 p61 | B, „cu prioritate” (nu exclusiv); pardoseală numai doze omologate |
| 092 | B | 5.5.2.1 p72 | B, bornă/bară principală pentru fiecare instalație |
| 093 | A | 5.4.1 p70 | A, iluminat normal distinct de prize |
| 094 | C | 5.5.7.11 p76 | C 4Ω, pentru protecție *numai* contra șocului; 1Ω dacă priză comună trăsnet |
| 095 | A | Definiția N, capitol 2 p6 | A; N nu este PEN |
| 096 | A | Definiția curent admisibil, capitol 2 p6 | A, continuu fără depășirea temperaturii maxime |
| 097 | C | Definiția curent nominal, capitol 2 p7 | C, regim normal pe durată nelimitată |
| 098 | A | 5.5.7.2–4 p75 | A, electrozi recomandați; B și C sunt categorii explicit neadmise |
| 099 | C | Definiția electrodului/prizei, capitol 2 p8–9 | C, pământ sau mediu conductor în contact cu pământul |
| **100** | **B** | **4.1.5.5.6 p31** | **CAPCANĂ LINGVISTICĂ**: I7 cere „nu mai mică de 50 kΩ” la ≤500V, care înseamnă **≥50**, în timp ce enunțul spune „mai mare de”, adică >50. Valoarea B este numeric corectă, dar semnul trebuie corectat |

## Garanții și ce NU s-a făcut
- Două fișiere CSV noi au 20 de rânduri unice, enunțurile originale, opțiunile A/B/C, baremul, PDF-ul, pagina, condițiile și statușii de QA.
- **1 conflict direct, 1 conflict de unicitate/formulare, 2 cazuri fără opțiune completă și 1 defect de inegalitate**. Restul 15 au sursă preliminară care justifică cheia, nu aprobări independente.
- **0/822 aprobări independente**; verificarea pe surse este asistată de model, nu semnată de inginer/lingvist independent; sursa didactică exactă pentru unele definiții rămâne de verificat.
- Nu s-a efectuat niciun build APK, test Android sau schimbare de aplicație. Nu se declară „DONE” până când toate cele 822 au sursă, sens tehnic și QA, iar conflictele sunt închise/controlate conform aprobării utilizatorului.
- Cumul actual din V33–V40: **73 ID-uri reverificate individual**, 749 rămase pentru un nou audit la aceeași profunzime; nu confunda cu screening-ul preliminar 822.

## Continuare
Următorul lot **G1-NOR-101–110**, tot din V10.29 canonic. Ține prioritatea totală pe întrebări, nu pe aplicație. La fiecare lot verifică stabilitatea ID/ABC, articol/versiune, capcane, duplicate și documentează individual. PR #7 Draft, fără merge.
