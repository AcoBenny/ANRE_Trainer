# ANRE Trainer | V36–V37 | G1-NOR-051–070, audit efectiv cu sursă și capcane
**Data:** 11.11.2026. **Baza canonică:** V10.29 (GitHub blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`), 20 enunțuri, opțiuni A/B/C și bareme exact originale, rândurile XLSX 58–77. **Nicio cheie schimbată.**

## Proveniență și verificare
Am consultat fișierul PDF I7 încărcat de utilizator (249 pagini, ediția sintetică consolidată 22.09.2023; SHA-256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`) și, pentru reperele importante, textul indexat pe Portalul Legislativ: https://legislatie.just.ro/Public/DetaliiDocument/286763 . Am extras paragrafele prin parser PDF și inspectat vizual Anexa 5.32 p.209 și domeniul de aplicare p.5. Nu declarate verificări fizice Android sau auditor inginer/lingvist *independent*; istoria modificărilor până la data 2026 este încă verificată incomplet.

Inventarele de 10 rânduri, cu **enunțul original, toate variantele, sursa, pagina, cheia și explicația**:
- `V36_G1_NOR_051_060_SOURCE_KEY_RECHECK.csv`
- `V37_G1_NOR_061_070_SOURCE_KEY_RECHECK.csv`

## Conflicte și capcane importante
| ID | Cheie în aplicație | Evidență V36–V37 | Verdict preliminar |
|---|---|---|---|
| **G1-NOR-053** | A | În SR 234/PE106 termenii `branșament` și `racord` nu sunt sinonimi: racordul se oprește la firidă; branșamentul este ansamblul spre instalația interioară/punctul de delimitare. Text didactic reproducer SR234: https://electrician365.ro/wp-content/uploads/2019/04/Normativ-instalatii-electrice-Privind-proiectarea-si-executarea-bransamentelor-electrice-pentru-cladiri-civile.pdf , §1.2.1–1.2.2. | **A contestată; C este candidat, nu verdict juridic**, fiind necesară ediția normativă exact aplicabilă |
| **G1-NOR-054** | A (1 m) | I7 **5.4.22**, p.70, recomandă **0,6–1,5 m**. Varianta B dă intervalul, dar A=1 m și C=1,5 m sunt și ele exemple admise din interval. | **Enunț ambiguu cu mai multe opțiuni plauzibile**, nu schimbare automată doar B |
| **G1-NOR-058** | B (total interzisă) | I7 **3.0.3.5**, p.13, admite excepția cu închidere **IP ≥33** și materiale rezistente la condens. | **C (condiționat) susținut direct** |
| **G1-NOR-060** | B (permis condiționat) | I7 **5.5.3.2**, p.72, interzice expres **conductele pentru apă** ca PE. Nu confunda cu legarea conductelor la sistemul echipotențial. | **C (nu este permisă) susținut direct** |
| **G1-NOR-061** | A (admisă) | I7 **5.2.12.3.4**, p.61, interzice **îmbinarea tuburilor la trecerile prin elementele de construcție**. | **B susținut direct** |
| **G1-NOR-066** | B (admisă) | I7 **5.2.12.1.4**, p.59, interzice *conductoare electrice în tuburi/țevi pozate în pământ*. **Nu confunda cu cabluri** speciale care pot fi pozate în pământ conform 5.2.3.1.4. | **A susținut direct** |

Alte atenționări:
- **051**: receptor >2 kW necesită circuit separat, iar min. 2,5 mm² Cu este în Anexa 5.32 pentru circuite de **prize monofazate**; aceeași anexă indică 1,5 mm² Cu pentru unele **circuite de putere/forță**. Tipul de racord din enunț nu e explicit, deci păstrăm A ca ipoteză *condiționată*, nu aprobare universală.
- **056**: I7 5.5.3.5 interzice comutatoare pe PE, dar admite îmbinări deconectabile cu **sculă pentru încercări**. Termenul întrebării „elemente care pot produce întreruperea” necesită precizare.
- **062**: I7 5.4.25 indică **peste 1,5 m** în camere de copii de creșe/grădinițe/spitale, însă folosește **„se recomandă”**, iar întrebarea spune „trebuie”. B candidată, cu capcană de modalitate normativă.
- **067**: siguranțele fuzibile adecvate pot proteja la suprasarcină și scurtcircuit (C), dar trebuie validată categoria/curba de declanșare și standardul didactic/IEC 60269, nu prezentată fără condiții universale.

## Restul surselor individuale (toate preliminare)
- **052 → A**: Anexa 5.32, nota 1, p.210: neutralul în circuite monofazate cu secțiune ca faza.
- **055 → A**: I7 1.1–1.2, p.5: clădirile agro/zootehnice intră în sfera generală, minele și depozitele explozive sunt excluse.
- **057 → B**: I7 5.1.6.11, p.48: montarea la apă/ulei/coroziune/șoc se evită, dar poate fi permisă cu protecție dacă poziția nu se poate evita.
- **059 → B**: I7 5.4.20, p.70: dispozitiv îmbunătățire factor de putere la lămpi cu descărcări.
- **063 → C**: I7 5.3.3, p.63–65: tipul tabloului și gradul IP se adaptează mediului.
- **064 → B**: I7 5.4.24, p.71: prize după necesități.
- **065 → A**: I7 5.4.7, p.70: peste 2 kW, circuit separat la locuințe.
- **068 → B și 069 → A**: I7 5.4.29, p.71: prize speciale (obturatoare) **și** RCD ≤30mA în încăperi pentru utilizatori vulnerabili.
- **070 → A**: I7 5.4.22, p.70: întrerupătoare/butoane de iluminat numai pe fază.

## Măsura de calitate
- 20/20 ID-uri existente din canon; toate variantele și cheia păstrate într-un registru reproductibil.
- **4 contradicții directe cu I7 2023**: 058,060,061,066. **1 conflict de definiție externă**: 053, sursa de ediție incomplet verificată. **1 ambiguitate fără un singur răspuns exclusiv**: 054. **4 cazuri de verificare contextuală**: 051,056,062,067.
- Celelalte 10 ID-uri au suport preliminar în articolele indicate.
- TOTAL nou V33–V37 = 4 + 9 + 10 + 10 + 10 = **43/822 reverificate individual**; **779** fără reverificare la aceeași profunzime.
- **0/822** cu aprobarea unui expert independent final și **0** corecții aplicate aplicației.

## Blocaje / reguli
Confirmarea exactă a ediției legale 2026, revizuirea independentă de electrotehnică/lingvistică, sursele didactice licențiate, și verificarea aplicației reale sunt încă deschise. Nu se schimbă cheile, A/B/C, HTML/APK și nu se face merge/release înainte de aprobarea explicită a utilizatorului. Minimizăm GitHub Actions.

## Următorul lot
**G1-NOR-071–080**, ulterior restul G1/G2. Folosim aceeași schemă de evidență, interzicem transferul automat de la duplicate între grade când baremele sunt în conflict.
