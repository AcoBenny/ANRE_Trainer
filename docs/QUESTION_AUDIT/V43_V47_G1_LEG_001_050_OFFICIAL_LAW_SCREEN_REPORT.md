# ANRE Trainer | V43–V47 | 50 de întrebări G1 Legislație
**Data:** 2026-11-11. **Input canonic:** V10.29 GitHub blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`, `LEGISLATIE-GR.-1-05.2023 (1).xlsx`, rândurile 8–57. `G1-LEG-024,028,032,034,048` fuseseră deja tratate în V34, acum sunt reluate pentru controlul întregii serii. **50 ID-uri auditate; 45 unice în plus față de V33–V40.**

## Surse autoritative, versiuni și articole
- **Legea 123/2012, art.1–3, 57, 92–93:** https://legislatie.just.ro/Public/DetaliiDocumentAfis/269124
- **Ordin ANRE 5/2023, Regulament furnizare:** https://legislatie.just.ro/Public/DetaliiDocument/264611 ; importante art.7–8, 26 și condițiile de reziliere.
- **Ordin ANRE 59/2013, Regulament racordare:** https://legislatie.just.ro/Public/DetaliiDocument/160289 ; art.26,33, anexa 3.
- **Ordin ANRE 74/2014, ATR și contestații:** https://legislatie.just.ro/Public/DetaliiDocument/230089 ; art.2 alin.(2–3) şi anexa.
- **Ordin ANRE 66/2023, Regulament autorizare:** https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046 ; art.9,12,14–16,30,35–37,41–47.
- **Pagina informativă oficială ANRE:** https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/
**Atenție:** actele au modificări în anii 2024–2026. Acest lot identifică suportul textual și conflictele, dar **nu demonstrează exhaustiv versiunea aplicabilă fiecărui item la data de 05.2023 și în prezent**, pentru fiecare articol. Cheile nu au fost schimbate.

## Conflicte de barem/întrebări invalide
| ID | Cheie originală | Candidat sau constatare | Probă |
|---|---|---|---|
| **015** | B | **B nu este contravenție, ci infracțiune. Nicio altă opțiune nu a fost confirmată.** | Legea 123, art.92(1), distinge clar modificarea fără drept a instalațiilor de contravențiile din art.93. |
| **017** | B | **A este cauza de reziliere explicită**, sustragere constatată prin hotărâre definitivă; B (racordare ilegală) nu demonstrează singură condiția juridică exactă. | Reg. 5/2023 clauzele de reziliere alin.(3)(a–c); și condiții de preaviz; verificarea contextuală rămâne deschisă. |
| **019** | C | **B, contravenție** | Legea 123, art.93(1) pct.3, „nerespectarea normelor tehnice emise de către ANRE” = contravenție. |
| **020** | A | **B**, contestațiile ATR inițiale se soluționează de comisia operatorului de rețea emitent | Ordin 74/2014 art.2 alin.(2–3), nu generic "organe ierarhice ale emitentului". |
| **026** | C | **B, infracțiune** | Legea 123 art.92(2), instalații clandestine pentru racordare directă/ocolirea măsurării. |
| **024** | A | **C candidat**, excepțiile temporare neepuizate | Ordin 59/2013; precizări V25/V34. |
| **028** | B | **C** pentru ansamblu de blocuri | Ordin 59/2013 anexa 3 pct.2.3; precizări V25/V34. |
| **032** | B | **A posibil**, temeiul concret de sancționare de completat | Ordin 66/2023 5 ani, Legea 123 art93. |
| **034** | B | **A**, proiect obligatoriu; recepție numai dacă e solicitată | Ordin 66 art37(e/h). |
| **048** | A | **B**, modalitate de plată din oferta furnizorului | Legea 123 art57(2). |

## Alte controale de expresii-limită
- **011:** anulare adeverință pierdută într-o publicație **de largă circulație**, nu orice „ziar local”; C conține și tariful duplicat corect dar include o condiție potențial greșită; nu aproba fără clarificare.
- **012:** diferența între tariful de vizare și tariful de acordare e dependentă de ediție/ordinul anual; confirmare la mai 2023 și 2026 încă necesară.
- **029:** rolul ANRE în soluționarea diferendelor e distinct de procedura inițială de contestare a ATR la operator; enunțul poate amesteca etapele.
- **039:** Ordin 59/2013 art26: 30 zile **calendaristice** după documentație completă pentru fișă soluție, indiferent de formularea MT a variantei B, deci B este adevărată dar nu formulată exhaustiv.
- **040:** grad I ≤10kW, sub 1kV, fără atestat, **doar în condițiile cumulative ale art35** (forme și colaborări autorizate). Nu deduce permisie nelimitată.
- **041,042:** data de regularizare 42 zile și excepția licențierii OD neconcesionar au rămas la `SOURCE_GAP` până la confirmarea punctului exact, nu vor fi certificate ca sigure.
- **043:** art26(4)(b) preaviz **5 zile lucrătoare** pentru clienți noncasnici, textul A are „minim 5 zile”, nu precizează lucrătoare, deci explică exact.
- **049:** art26(2)(b) permite furnizorului să ceară întreruperea în cazul neconstituirii garanției, numai cu pașii legali;
- **050:** art7(1)(d) eșalonare client vulnerabil *minimum* trei luni, B direct.

## Calitatea dovezilor
- 50/50 enunțuri și A/B/C/chei/identificatori/rânduri originale păstrate în cele cinci CSV: V43, V44, V45, V46, V47.
- Articole primare exacte legate pentru multe cazuri; întrebările cu excepții, versiunile schimbate și temeiuri nedemonstrate sunt `PENDING`, nu completate artificial.
- **0 corecturi de barem, 0 aprobări tehnice/lingvistice independente, 0 modificări HTML/APK/main, 0 builduri Actions, 0 merge**.

## Rezumat
Cea mai mare problemă este să nu antrenăm utilizatorul cu chei eronate doar pentru că au fost importate într-un fișier. Cel puțin 4 ID-uri noi (015/017/019/020/026: 017 condiționat) necesită blocare de la promovat ca "verificat" până la adjudecare. Duplicatele 024,028,032,034,048 își păstrează contextul de la V34.
