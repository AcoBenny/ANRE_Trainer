# CKPT-243 | 15 original QABC + 13 exact grade-II reuse references | 2026-11-19

Baseline V121 blob `0be4895adb766b0fcfab2d038447769148c24147`; original canonical V73 blob `c027d417a8e4e605c830b2016fb55b099b8d130b`.

- **15 source-scoped new original Grade-I analyses**, each with exact original Q/A/B/C and unchanged canonical key.
- All 15 Grade-II counterparts matched exact question+A+B+C+key; Grade II G2-ELEC-365 (V82) and G2-ELEC-367 (V87) already have prior evidence, retained untouched.
- **28 new grade records** referenced, 162 -> 134 with no focused evidence. 822 unchanged IDs, original keys and approvals retained.
- Web source access: 8 full HTML pages reviewed, 7 search-index-only links. Some are generic/noncanonical; these are preliminary analytical leads not ANRE 2026 scored-key proof.

### G1-ELE-228 / G2-ELEC-364
- Original Q: Siguranţele electrice au rolul de a:
- A: proteja instalaţia din aval la defecte la scurtcircuit ca si la suprasarcini de lunga durata
- B: face trecerea din linie electrica aeriana în line electrica în cablu
- C: asigura protecţia personalului
- Imported key remains A; A/B/C source model and countercases: A indică protecție aval la scurtcircuit și suprasarcină, dar numai dacă tipul/curba fuzibilului și coordonarea sunt potrivite. B trecere LEA/cablu nu este funcția siguranței; C protecția persoanelor nu este garantată doar de fuzibil. Unele clase sunt specializate pe scurtcircuit și nu protejează toate suprasarcinile.
- Source candidate: https://www.iteh.eu/catalog/standards/iec/147f17fc-7f2f-4220-a1d7-f86427ceabd5/iec-tr-60269-5-2010
- Access: SEARCH_INDEX_ONLY; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-229 / G2-ELEC-365
- Original Q: Siguranţele electrice sunt aparate electrice care împiedica:
- A: creşterea tensiunii peste o valoare limita
- B: creşterea curentului peste o valoare limita
- C: scăderea curentului sub o valoare limita
- Imported key remains B; A/B/C source model and countercases: B este funcția intenționată: întrerupe circuitele în cazul depășirii pragului curentului potrivit caracteristicii timp-curent. A limitarea supratensiunii nu este funcția sa; C lipsa curentului nu declanșează fuzibilul. Formularea «împiedică creșterea peste o valoare limită» este literal inexactă: curentul poate depăși nominalul un interval înaintea topirii și nu este obligatoriu limitat la o valoare instantanee.
- Source candidate: https://www.iteh.eu/catalog/standards/sist/5591b278-481b-44fe-9f3b-d990a37656db/sist-tp-iec-60269-5-trtr-ed-1-0-2022
- Access: SEARCH_INDEX_ONLY; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-231 / G2-ELEC-367
- Original Q: Singurele mărimi fizice reale în curent alternativ sunt:
- A: mărimile efective de curent sau de tensiune
- B: mărimile instantanee de curent sau de tensiune
- C: valorile medii de curent sau de tensiune
- Imported key remains B; A/B/C source model and countercases: B este răspunsul importat și poate reflecta faptul că i(t) și u(t) sunt funcțiile fizice instantanee. Totuși A valorile RMS sunt măsurabile și fizic semnificative pentru încălzire/putere, iar C mediile sunt de asemenea cantități fizice definite; «singurele mărimi fizice reale» nu este o afirmație tehnică riguros exclusivă. Marcați AMBIGUITATE_CONCEPTUALĂ și nu certificați B ca adevăr universal.
- Source candidate: https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-262 / G2-ELEC-397
- Original Q: Unitatea de măsură pentru măsurarea puterii active este:
- A: kWh
- B: kW
- C: kW/h
- Imported key remains B; A/B/C source model and countercases: B kilowatt kW măsoară putere activă; A kilowatt-oră kWh energie, C kW/h variația puterii per timp. Barem B compatibil cu SI și terminologia tehnică.
- Source candidate: https://www.eia.gov/energyexplained/electricity/measuring-electricity.php
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-263 / G2-ELEC-398
- Original Q: Unitatea de măsură pentru puterea reactiva este:
- A: kVAr
- B: kVA
- C: kW
- Imported key remains A; A/B/C source model and countercases: A kVAr este unitatea specială var pentru putere reactivă, cu prefix kilo; B kVA putere aparentă și C kW putere activă. Răspuns tehnic compatibil cu nomenclatura IEC.
- Source candidate: https://www.epo.org/en/legal/guidelines-epc/2025/f_iia2_1_2_2.html
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-264 / G2-ELEC-399
- Original Q: Utilizarea întreruptoarelor debroşabile:
- A: nu asigură eliminarea unor greşeli de manevră datorate separatoarelor;
- B: asigură scurtarea duratei reviziilor la celule;
- C: asigură numai izolarea personalului care lucrează la întreruptor, de restul instalaţiei aflată sub tensiune.
- Imported key remains B; A/B/C source model and countercases: B: întreruptorul debroșabil poate permite intervenție/înlocuire mai rapidă și reduce întreruperea serviciului. A presupune că nu previne erorile separatoarelor, dar elimină unele manevre de separare; C «numai» exclude alte beneficii. Timpul real al reviziilor depinde de părțile fixe rămase, interblocări, proceduri și condiții de siguranță.
- Source candidate: https://electrical-engineering-portal.com/fixed-withdrawable-medium-voltage-switchgear
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-265 / G2-ELEC-400
- Original Q: Autotransformatoarele sunt folosite
- A: între reţelele de                     110 kV şi 220 kV
- B: numai între reţelele de              220 kV şi 400 kV
- C: între reţelele de                   20 kV şi 110 kV
- Imported key remains A; A/B/C source model and countercases: A: utilizare posibilă între 110 și 220 kV este compatibilă cu stații interconectate românești; B «numai între 220 și 400kV» este fals prin exclusivitate, C 20/110kV necesită analiză exactă a raportului/izolării. Sursa Transelectrica confirmă existența nivelurilor și stațiilor, dar NU dovedește că toate transformările 110/220 sunt autotransformatoare sau că 20/110 nu poate folosi niciodată autotransformator. FLAG SOURCE_SCOPE_PARTIAL.
- Source candidate: https://www.transelectrica.ro/web/tel/codul-comercial-al-pietei-angro-de-energie-electrica%3Bjsessionid%3DB4866C5188A72F028074678AAF1B2543?_77_advancedSearch=false&_77_andOperator=false
- Access: SEARCH_INDEX_ONLY; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-268 / G2-ELEC-401
- Original Q: Utilizarea întreruptorului debroşabil:
- A: asigură doar compactarea celulei;
- B: asigură rapiditate în restabilirea alimentării în cazul unei defectări;
- C: creşte riscul de electrocutare a personalului care execută lucrări de revizie în celulă.
- Imported key remains B; A/B/C source model and countercases: B permite restabilirea relativ rapidă după defect de întreruptor prin înlocuirea modulului debroșabil dacă există rezervă compatibilă, personal autorizat și celula fixă este sigură. A «doar compactarea» fals, C creșterea riscului nu este avantaj intrinsec, dar operația de debroșare are riscuri specifice. NU afirmați restaurare automată.
- Source candidate: https://electrical-engineering-portal.com/fixed-withdrawable-medium-voltage-switchgear
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-269 / G2-ELEC-402
- Original Q: Utilizarea SF6 ca mediu de izolare
- A: conduce la realizarea unor celule cu pericol de incendiu
- B: conduce numai la realizarea unor celule cu întreţinere mult simplificată;
- C: conduce la realizarea unor celule compacte
- Imported key remains C; A/B/C source model and countercases: C: gazul SF6 permite izolarea cu distanțe mici, deci celule compacte. A pericol incendiu nu rezultă din caracterul său izolant, B «numai întreținere simplificată» este exclusivitate falsă. Important: impact climatic mare al SF6 și cerințe de etanșeitate/management gaze, fără a le confunda cu răspunsul de examen.
- Source candidate: https://www.csemag.com/saving-space/
- Access: SEARCH_INDEX_ONLY; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-270 / G2-ELEC-403
- Original Q: Utilizarea SF6 ca mediu de stingere a arcului electric permite
- A: doar realizarea unor întreruptoare fără pericol de incendiu;
- B: realizarea unor întreruptoare cu întreţinere mult simplificată;
- C: puţin silenţioase.
- Imported key remains B; A/B/C source model and countercases: B este efect plauzibil în întreruptoare moderne SF6 cu întreținere simplificată față de tehnologii istorice, dar nu lipsită complet de verificări de presiune/etanșeitate. A «doar fără incendiu» falsă exclusivitate; C «puțin silențioase» nu descrie beneficiul principal. Sursa Schneider compară tehnologii și arată întreținere redusă, nu certifică toate tipurile.
- Source candidate: https://www.se.com/eg/en/faqs/FA22640/
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-271 / G2-ELEC-404
- Original Q: Utilizarea vidului ca mediu de stingere a arcului electric:
- A: reduce pericolul de incendiu;
- B: nu reduce cheltuielile de întreţinere;
- C: creşte masa şi gabaritul întreruptoarelor
- Imported key remains A; A/B/C source model and countercases: A: întreruperea în vid elimină uleiul combustibil ca mediu de stingere și reduce un mecanism de incendiu. B nu reduce întreținere contrazice tehnologia cu vid, C dimensiuni/masă crescute nu sunt efect universal. Protecția nu înseamnă risc total de incendiu zero.
- Source candidate: https://www.abb.com/global/en/areas/electrification/medium-voltage/grid-components/primary-vacuum-circuit-breakers
- Access: SEARCH_INDEX_ONLY; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-272 / G2-ELEC-405
- Original Q: Valoarea frecventei în sistemul electroenergetic este determinata în principal de:
- A: bilanţul puterilor active
- B: circulaţia puterii reactive
- C: modul de tratare a neutrului reţelei
- Imported key remains A; A/B/C source model and countercases: A: frecvența sistemului sincron reflectă bilanțul dintre producția de putere activă și consum, prin accelerația rotorilor / ecuația de oscilație. B puterea reactivă influențează mai direct tensiunea; C tratarea neutrului vizează defecte la pământ. Excepție: sisteme cu convertoare și control sintetic păstrează corelația bilanț-frecvență dar dinamica diferă.
- Source candidate: https://link.springer.com/article/10.1186/s43067-022-00053-2
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-273 / G2-ELEC-406
- Original Q: Valoarea medie a capacităţii lineice pentru o linie electrică aeriană trifazată este ......... faţă de cea a unui cablu subteran.
- A: egală
- B: mai mică
- C: mai mare
- Imported key remains B; A/B/C source model and countercases: B: în medie capacitatea liniei aeriene pe kilometru este mult mai mică decât a cablului subteran, deoarece spațiile dintre conductoare și pământ sunt mai mari. A egalitate și C mai mare nu sunt tipice. Depinde de tensiune, geometrie, manta, material izolant și tipul instalației; comparați unități aceleași.
- Source candidate: https://opal-rt.atlassian.net/wiki/spaces/PDOCHS/pages/150307736
- Access: SEARCH_INDEX_ONLY; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-274 / G2-ELEC-407
- Original Q: Valoarea medie a inductanţei de serviciu pentru o linie electrică aeriană trifazată este ......... faţă de cea a unui cablu subteran.
- A: egală
- B: mai mare
- C: mai mică
- Imported key remains B; A/B/C source model and countercases: B: pentru sisteme trifazate comparabile, LEA are de regulă inductanță linică mai mare decât cablul compact, unde conductoarele sunt apropiate. A egalitate, C mai mică nu corespund cazului tipic; structură ecran și construcție pot altera cifrele. Susținut doar ca comparație medie de configurații.
- Source candidate: https://opal-rt.atlassian.net/wiki/spaces/PDOCHS/pages/150307736
- Access: SEARCH_INDEX_ONLY; NO confirmed exam2026 edition, NO independent external QA.

### G1-ELE-275 / G2-ELEC-408
- Original Q: Valoarea medie pătratică a unei mărimi periodice se mai numeşte şi:
- A: amplitudine
- B: modul
- C: valoare efectivă sau valoarea eficace
- Imported key remains C; A/B/C source model and countercases: C: rădăcina mediei pătratelor (RMS) este valoarea efectivă/eficace. A amplitudinea reprezintă vârful unui semnal, B modul nu desemnează definiția RMS. Pentru semnal sinusoidal U_rms=Umax/√2; pentru forme arbitrarii formula generală de mediere pătratică.
- Source candidate: https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Access: OPENED_HTML; NO confirmed exam2026 edition, NO independent external QA.

## Interpretation and formal QA gates
- ELE-229 fuse does not instantly clamp current to an absolute limit in every fault; tripping obeys protection curves.
- ELE-231 «only real quantities are instantaneous» is semantic/philosophical and requires bibliography-specific definition. RMS is a measurable physical quantity; no universal approval of B.
- ELE-265 voltage-level existence alone does not prove a 110/220 auto-transformer device; **source_scope_partial**, historical intended A pending exact model/source.
- ELE-264, ELE-268 switchgear withdrawability affects maintenance and restoration conditionally; cannot substitute safety procedures.
- All independent reviewer, original standard edition, legal/technical signoff gates remain pending; no 822 approval.
- Existing 50 malformed CSV serialization rows preserved unchanged and isolated from modified 28 rows; full CSV reconciliation future gate.
- PR #7 Draft, no app, barem, HTML/APK, main, merge or release change.
