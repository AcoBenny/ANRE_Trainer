# V26 | Verificare exactă I7 actualizat 2023, G1-NOR-001–010

**Data:** 2026-11-09. **Sursa:** PDF încărcat în biblioteca utilizatorului, `803493174-I7-2011-completat2023.pdf`, 249 pagini, antet „Normativ din 2011 – forma sintetică pentru data 2023-09-22”. Conținutul nu este copiat în GitHub, deoarece drepturile de redistribuire nu au fost validate. Norma I7 a fost modificată prin Ordin 959/2023: https://legislatie.just.ro/Public/DetaliiDocument/271142 .

**Metoda:** am localizat fiecare cerință în sursa I7 exactă, am citit și inspectat inclusiv reprezentări de pagină ale PDF-ului (pag.36,70,162); pentru pag.38,61,63 am folosit textul PDF și paragraful exact. Am comparat enunț+ABC și litera din `const DATA` canonical V10.29 GitHub blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`. **Nu este un audit independent semnat** (`QA=NOT_RUN`), ci verificare documentară model-assisted, verificabilă.

## Rezultate

| ID | Canonical | Sursă susține | I7 pct. / pagina | Verdict |
|---|---|---|---|---|
| G1-NOR-001 | B | B | 4.2.3.2.14 / 36 | TEXT_MATCH |
| G1-NOR-002 | B | B | 8.1.1.3.3 + Tabelul 8.1 / 162 | TEXT_MATCH |
| G1-NOR-003 | A | A | 5.4.2 / 70 | TEXT_MATCH |
| G1-NOR-004 | B | B | 4.3.4.1.1 (cu exceptiile 4.3.4.1.2 si 4.3.4.2) / 38 | WORDING_CONDITION |
| G1-NOR-005 | B | B | 8.1.1.3.5 / 162 | TEXT_MATCH |
| G1-NOR-006 | C | C | 5.4.19 / 70 | TEXT_MATCH |
| G1-NOR-007 | C | C | 5.3.2.3 / 63 | TEXT_MATCH |
| G1-NOR-008 | C | C | 5.4.19 / 70 | TEXT_MATCH |
| G1-NOR-009 | C | C | 5.2.12.2.4 / 61 | TEXT_MATCH |
| G1-NOR-010 | B | C | 8.1.1.3.3 / 162 | CANONICAL_KEY_CONTRADICTS_NORM |

**Total:** 8 cazuri de potrivire directă cu sursa, 1 caz cu formulare condițională, 1 conflict canonic.

### G1-NOR-010: conflict nou, prioritate ridicată
- **Cheie canonică B**: `numai între conductoarele active luate 2 câte 2`.
- **Normativ I7, pct 8.1.1.3.3, pag.162, susține C**: verificarea rezistenței izolației între conductoarele active și conductorul PE racordat la pământ; pot fi legate împreună activele pentru încercare. Formularea exclusivă „numai” din B este incompatibilă cu cerința explicită a acestui punct.
- **Risc:** siguranță electrică și pregătire de examen; necesită QA tehnic/normativ separat înainte de orice schimbare de barem sau aplicație.

### G1-NOR-004: capcană validă cu condiție
I7 4.3.4.1.1 pag.38 prevede deconectarea conductorului în care se detectează supracurentul, dar nu impune întotdeauna deschiderea tuturor celorlalte conductoare. Însă există excepții 4.3.4.1.2 și 4.3.4.2 și pericole la funcționarea monofazată a motoarelor; varianta B (`de regulă numai`) trebuie explicată cu aceste condiții.

## Q&A și limitări
- **Source provenance:** este o formă sintetică actualizată la 22.09.2023, care poate să nu includă modificări ulterioare; pentru decizii de proiect actuale este obligatoriu control suplimentar asupra versiunii curente.
- **Atenție la surse:** aceste zece au referință paragraf/pagină, dar pentru întregul set 100 G1 norme această verificare nu a fost executată. Niciun text din XLSX nu a fost confundat cu sursă didactică.
- **QA:** `INDEPENDENT_QA=NOT_RUN`; nicio testare HTML/APK în acest lot.
- **Siguranță:** `key_changed=NO`; nu modifica baremele/HTML/APK, nu merge/release.
