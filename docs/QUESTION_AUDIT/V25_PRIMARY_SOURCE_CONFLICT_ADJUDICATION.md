# V25 | Re-adjudecare pe surse a conflictelor ANRE (read-only)

**Data:** 2026-11-09. **Repo/PR:** `AcoBenny/ANRE_Trainer` PR #7 Draft. **Canon:** V10.29 blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`.

**ATENȚIE:** toate constatările sunt *model-assisted, evidențe externe punctuale*. Nu a fost executat un reviewer lingvistic sau juridic independent. Zero bareme sau fișiere ale aplicației modificate; fără merge.

## Concluzii pe caz

### **G1-LEG-024** (canonic A)
- **Capcană:** durata sub 6 luni / orice nou loc.
- **Sursă și reper:** ANRE Ordin 59/2013, Regulament art. 9 lit. b/c; art. 11 alin. (1), forma 2013.
- **Evaluare:** Art 11 alin 1 exige cerere de racordare independent de perioada si putere; art 9 prevede emiterea ATR. Nu exista scutire generala sub 6 luni in aceste prevederi. Varianta C conform acestui cadru, A contrazisa. Mai verifica orice derogare specifica si editia din mai 2023.
- **Stare:** `PRIMARY_REGULATION_SUPPORT`; QA gate `CONDITIONAL_2023_VERSION_QA`; `INDEPENDENT_QA=NOT_RUN`.
- **URLs:** https://legislatie.just.ro/Public/FormaPrintabila/00000G274VNG8B51XKX3UZLHX8NOAPLU

### **G1-LEG-028** (canonic B)
- **Capcană:** ansamblu de blocuri versus ansamblu de locuinte individuale.
- **Sursă și reper:** ANRE Ordin 59/2013, Anexa 3 pct. 2.2–2.3.
- **Evaluare:** Pct 2.3 cere amplasare centralizata la parter/palier in ansambluri de blocuri. Limita proprietatii din optiunea B se refera la alt context, locuinte individuale. C sustinut; B neadecvat pentru enuntul exact.
- **Stare:** `PRIMARY_REGULATION_SUPPORT`; QA gate `INDEPENDENT_LEGAL_QA`; `INDEPENDENT_QA=NOT_RUN`.
- **URLs:** https://legislatie.just.ro/Public/FormaPrintabila/00000G35R333SFHRDTH1XD6JRTZOZBPD

### **G1-LEG-032** (canonic B)
- **Capcană:** 4 ani versus termen de vizare 5 ani.
- **Sursă și reper:** ANRE informare vizare 5 ani; Ordin 66/2023 art. 37, art. 41.
- **Evaluare:** 4 ani de la eliberare nu reprezinta de la sine expirare ori contraventie, daca vizarea nu este depasita. Interdictiile regulamentului sunt sanctionabile in conditiile legii, dar forma exacta a contraventiei A cere verificarea legii primare. Tracker A plauzibil; canonical B slab fundamentat.
- **Stare:** `PRIMARY_REGULATION_PARTIAL`; QA gate `LEGAL_SANCTION_ELEMENT_NOT_YET_EXACT`; `INDEPENDENT_QA=NOT_RUN`.
- **URLs:** https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/electricieni/examene/ ; https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046

### **G1-LEG-034** (canonic B)
- **Capcană:** chiar daca nu i se solicita / in cazul in care i se solicita.
- **Sursă și reper:** ANRE Ordin 66/2023 art.37 lit.e si lit.h.
- **Evaluare:** Respectarea proiectului este obligatie la lit. e; participarea la receptie lit. h doar daca este solicitata. Varianta B inverseaza explicit conditia. A sustinut din textul articolului.
- **Stare:** `PRIMARY_REGULATION_SUPPORT`; QA gate `INDEPENDENT_LEGAL_QA`; `INDEPENDENT_QA=NOT_RUN`.
- **URLs:** https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046

### **G1-LEG-048** (canonic A)
- **Capcană:** orice modalitate chiar daca neofertata / una dintre cele ofertate.
- **Sursă și reper:** Legea 123/2012 art.57 alin.(2).
- **Evaluare:** Furnizorul ofera mai multe modalitati si permite alegerea dintre acestea; clientul nu poate impune o modalitate inexistenta in oferta. B sustinut, A contrazis.
- **Stare:** `PRIMARY_LAW_SUPPORT`; QA gate `INDEPENDENT_LEGAL_QA`; `INDEPENDENT_QA=NOT_RUN`.
- **URLs:** https://legislatie.just.ro/Public/DetaliiDocument/234802

### **G1-ELE-018** (canonic A) / **G2-ELEC-170** (canonic C)
- **Capcană:** Cs capacitate de serviciu / C12=C23=C31; neglijam C10.
- **Sursă și reper:** Marian Pearsica, Electrotehnica, ed. 2004, pag. tiparita 70, eq.4.26–4.27; material didactic condensatoare eq.2.61–2.64 (provenienta neconfirmata).
- **Evaluare:** Din q1=C10U10+C12(U1-U2)+C31(U1-U3), la echilibru U1+U2+U3=0 si C12=C31=C, q1=(C10+3C)U1. Pentru influenta pamantului neglijata C10=0 => Cs=3C. G1 A sustinut; G2 canonical C incompatibil cu aceste ipoteze. Confirmare sursa primara si reviewer independent necesare.
- **Stare:** `ACADEMIC_FORMULA_SUPPORT`; QA gate `ELECTRICAL_QA_AND_SOURCE_RIGHTS`; `INDEPENDENT_QA=NOT_RUN`.
- **URLs:** https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf ; https://ro.scribd.com/document/392658803/CONDENSATOARELE-ELECTRICE

### **G1-ELE-102** (canonic A) / **G2-ELEC-245** (canonic C)
- **Capcană:** este de preferat / regim normal / cupla in rezerva calda.
- **Sursă și reper:** NTE 009/10/00, definiție rezervă caldă/rece; sursă secundară c pentru un scenariu presupus.
- **Evaluare:** Ambele scheme pot fi functionale, preferinta depinde de fiabilitate, sectiuni, scurtcircuit si modul de operare. NTE defineste rezerva calda a cuplei, dar nu stabileste singura o optiune universal preferata; sursa secundara alege C pentru schema presupusa. Fara diagrama si criteriu de optimizare conflictul ramane AMBIGUU.
- **Stare:** `OPERATIONAL_PREFERENCE_UNRESOLVED`; QA gate `STATION_DESIGN_SME_AND_SINGLE_LINE_DIAGRAM`; `INDEPENDENT_QA=NOT_RUN`.
- **URLs:** https://legis.medleg.ro/legislatie/2010-regulament-general-manevre-2 ; https://www.scientia.ro/tehnologie/96-internet/10558-test-oficial-anre-pentru-electricieni-275-de-intrebari-electrotehnica-masini-si-retele-electrice-cu-raspunsuri-si-explicatii.html

## QA/limite
- Surse juridice ANRE/portalul legislativ: linkurile au fost consultate la nivel de articol/punct, dar nu toate modificările 2023–2026 au fost adjudecate în consolidare temporală pentru fiecare caz.
- Sursa academică Pearsică, 2004 prezintă explicit ecuațiile de capacitate parțială și definiția Cs. Formula 3C este dedusă, nu citată ca barem oficial. Pentru PDF vizualizarea screenshot în instrumentul web a returnat cache-miss, deci pagina nu este certificată vizual, deși textul PDF a fost inspectat.
- Pentru G1-LEG-024 articolul 11 spune cerere pentru orice durată, dar un caz excepțional reglementat în alt act poate necesita revizie temporală; nu se revendică o imposibilitate absolută a excepțiilor.
- Pentru G1-LEG-032 existența unei contravenții depinde de prevederea contravențională exactă, nu doar de interdicția din regulament.
- Pentru G1-ELE-102/G2-ELEC-245 nu există schemă de stație ori obiectiv de proiectare atașat, deci preferința nu este decisă.
- Când se aprobă o schimbare de cheie, numai pe baza aprobării explicite a utilizatorului și a QA separat; până atunci aceste valori rămân nemodificate.

## Pași pentru rezolvare
1. Reviewer legal ANRE independent: ed.2023 și norma curentă, inclusiv sancțiuni și excepții de racordare.
2. Expert electrotehnic independent: capacități parțiale Maxwell / definiția Cs; expert stații electrice: schemă normală cu două bare.
3. Verifică originea baremului în fișierul original, nu în coloane auxiliare sau alte întrebări; toate dezacordurile rămân în registrul de carantină.
