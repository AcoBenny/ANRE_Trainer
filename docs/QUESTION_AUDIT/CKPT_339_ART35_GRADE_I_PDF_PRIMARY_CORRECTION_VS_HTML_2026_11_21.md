# CKPT-339 | Rectificare demonstrată pe PDF-ul ANRE original: art.35 A(a) grad I | 2026-11-21

## Descoperirea și regula de corecție
- PR #7 Draft, HEAD anterior `c59b9d3b1a113bc8be8357e0a53a576abe5efc16`. În V252/CKPT-338 au fost folosite pasaje din reprezentarea HTML Portalul Legislativ (`https://legislatie.just.ro/Public/DetaliiDocumentAfis/270204`): aceea asociază condiția (i) din art.35 A(a) grad I cu autorizarea II/III/IV.
- O investigație **distinctă** prin Parallel AI a contestat această atribuție și a indicat originalul de la ANRE. **Verificarea vizuală manuală reală** a PDF-ului oficial [ANRE: Ordin 66/2023, Monitorul Oficial 417/16 mai 2023](https://anre.ro/wp-content/uploads/2023/05/Ord-66-2023.pdf), **pagina imprimată 9 (PDF index 7)** arată la art.35 A(a)(i) **„pentru gradul I, vizată la zi”**. Pe pagina imprimată 10 (PDF index 8) continuă art.35 A(b), unde sunt reglementate alte grade și se găsește **II/III/IV**.
- Aceasta este dovadă de **neconcordanță textuală între reprezentarea web HTML și PDF-ul oficial original**. Nu presupunem cauză (OCR, parser, bug ori eroare a paginii) fără investigare distinctă; nu copiem o condiție de la altă literă. Textul PDF 2023 are prioritate în verificarea fidelității **ediției istorice 2023**; încă nu există certificarea completă a ediției aplicabile întregii bibliografii din noiembrie 2026.
- Pentru exacta comparație vizuală: https://anre.ro/wp-content/uploads/2023/05/Ord-66-2023.pdf#page=8 și pagina următoare PDF #page=9. Varianta web HTML: https://legislatie.just.ro/Public/DetaliiDocumentAfis/270204.

## Rectificare versionată a V252 pentru două cazuri
| Original | Barem păstrat | Corecție sursă | Stare |
|---|---|---|---|
| **QABC-0271 / G1-LEG-007** | B | Art.35 A(a)(i) cere autorizare **grad I la zi**, NU grad II/III/IV; pct.(ii) impune asociere. 9 kW singur nu dovedește îndeplinirea condițiilor PFA; C nu se elimină ca fiind legală doar prin putere. | HOLD |
| **QABC-0304 / G1-LEG-040** | C | C exprimă excepția 10 kW/<1 kV/fără atestat de operator, însă trebuie citită cu autorizarea **grad I la zi**, asocierea cu alt electrician autorizat în condițiile pct.(i), și SSM. | HOLD |

## Negative test / limite
- [V253](./V253_ART35_ANRE66_ORIGINAL_PDF_VS_HTML_GRADE_I_CROSS_SOURCE_CORRECTION_2026_11_21.json) păstrează variantele originale, cheile importate nemodificate și sursele PDF vs HTML comparate, plus un caz negativ reproductibil pentru a bloca substituția II/III/IV în art.35 A(a). **QA vizual al celor două pagini: efectuat. QA automată a hashului PDF: NOT_RUN** (descărcarea binarului în runtime nu a reușit).
- Modelul extern a orientat căutarea, dar **nu este reviewer juridic calificat**, nici validare independentă a unei chei de examen. Concordanța sa a fost verificată efectiv contra paginii originale înainte de a o adopta.
- Istoricul V252 rămâne conservat; această corecție îl **suprascrie semantic doar pentru câmpurile din art.35(A)(a)(i)**, fără a rescrie fișierul precedent.
- Alte întrebări G1 PFA și grade II trebuie scanate pentru aceeași eroare de transpunere contextuală înainte de signoff.
- **136/136 hold-uri rămân deschise; 0/822 aprobări independente.** Nicio întrebare, barem, HTML, APK, main, merge sau release modificat.
