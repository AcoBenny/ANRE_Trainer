# Source leads | cupla transversală şi bare duble | 2026-11-11

**Status: INVESTIGATION_LEADS_ONLY / NO ANSWER APPROVED / NO INDEPENDENT REVIEW.**

## Întrebări
- `G2-ELEC-266` (P0) / `G1-ELE-124` (P1): aceeaşi unitate QABC, barem A, conţine exclusivul „numai”.
- `G1-ELE-125` (P0): aceeaşi temă, dar alte opţiuni; barem B afirmă ocolirea unui întreruptor de linie.
- `G1-ELE-126` (P1): alt set de variante, posibilă pluralitate de afirmaţii adevărate.
Nu transferăm răspunsuri între seturi de variante.

## Piste tehnice specifice (NU drept de închidere)
1. **ABB, Distribution Automation Handbook, 1MRS757959**, §3.14.1.3 (bare cu transfer) vs §3.14.1.4 (două bare colectoare), Fig.3.7, pagină tipărită 9: în schema cu bară de transfer se poate menţine circuitul la întreţinerea întreruptorului prin calea dedicată, dar într-o schemă simplă de bare duble scoaterea întreruptorului din serviciu afectează întreaga celulă. Cupla transversală transferă circuitele între bare în cadrul interblocajelor. Locator din index/extragere text https://library.e.abb.com/public/7dca4ffad2206d36c1257be30048d4be/DAHandbook_Section_3_Power_distribution_systems_757959_ENa.pdf (link fără token semnat: NU declarat verificat). **Capturile PDF au eşuat cu cache miss**; textul şi schema nu au fost verificate vizual.
2. **APTRANSCO, Technical Reference Book (2004)**, capitolul despre double bus, pagină tipărită ~70: pentru întreţinerea întreruptorului se menţionează necesitatea scoaterii circuitului din funcţiune în configuraţia standard şi adăugarea unui separator de ocolire pentru a evita asta. URL indexat: https://www.apeasternpower.com/MqKfcSkRsjsSlg0NlDDHYCT7dKQ%3D?fileName=Technical_Reference_Book.pdf&filePath=%2Fupload%2FExternal_Files%2F%2Ffooter%2F . **Captura PDF p.69 a eşuat cu cache miss.** Material străin/mai vechi, nu automat bibliografie ANRE.
3. **Regulamentul de racordare 59/2013**, art.26(1), pentru cazul separat `G1-LEG-039`: indexul legislativ indică 30 zile calendaristice pentru fişa de soluţie fără distincţia JT/MT; https://legislatie.just.ro/Public/DetaliiDocumentAfis/297330 . Deschiderea directă a portalului: HTTP 502. Concluzie **numai indiciu de articol**, nu formă consolidată 2026 certificată.

## Ce verifică auditorul înaintea unui verdict
- Obiect exact: două bare + **un** întreruptor pe circuit, cupla transversală simplă sau configuraţie cu separator de ocolire / bară de transfer?
- Are schema din întrebare suficiente elemente pentru o afirmaţie despre ocolirea întreruptorului? Unde există cupla şi ce interblocaje?
- Identifică fiecare folosire a „numai”, „nu se poate” şi diferenţa dintre „permite cuplare”, „verificare izolaţie” şi „ocolire”.
- Consultă surse primare aplicabile obiectului, gradului şi ediţiei ANRE, redeschide figurile şi verifică A/B/C pentru fiecare ID; reviewer distinct înainte de propunerea schimbării baremului.

**Nicio schimbare Q/A/B/C/cheie/HTML/APK.** Sursa terţă chestionare-anre.ro a furnizat doar semnalul de investigare, nu baza concluziei.
