# CKPT-075 | P1 Lot Y: NOR-091/092/093/094/095, I7 ancore verificabile | 2026-11-16

## Integritate și progres
- Repo AcoBenny/ANRE_Trainer, audit/anre-v8-priority-17-20261109, PR #7 Open/Draft, HEAD pre-write 417fd1ab1b003137f9982c246ced6f82b0ccbcaf.
- Cinci unități **P1 NOI** necuprinse în CKPT-047/049/050–074: G1-NOR-091 AU-78d9198a7f47d9d5, NOR-092 AU-384b3aaa8eba709a, NOR-093 AU-a81734c570654139, NOR-094 AU-56400be12641a793, NOR-095 AU-721db7681719f9eb, câte un ID.
- Baza corectată după CKPT-074: **160/568 unități**, **204/822 ID-uri** contextual documentate. Delta +5/+5 ⇒ **165/568**, **209/822**. **0/822 aprobate**, source/linguistic/technical independent QA NOT_RUN.
- Surse citite din PDF-ul I7 2023 furnizat de utilizator (249 pagini, sinteză datată 22.09.2023): §§5.2.12.3.7–.8 p61, 5.5.2.1 p72, 5.4.1 p70, 5.5.7.10–.11 p76, glosarul p6. Nu se confundă sursa privată de lucru cu confirmarea oficială exhaustivă a ediției din sesiunea ANRE 2026.
- Bareme, întrebări, A/B/C, CSV canonic, HTML/APK, main, merge/release intacte.

## Y1 | G1-NOR-091 | cheie B
**Enunț:** „Dozele de derivaţie se instalează”
- A „numai pe suprafeţele verticale ale elementelor de construcţii”
- B „cu prioritate pe suprafeţele verticale ale elementelor de construcţii”
- C „pe sau în pardoseală, indiferent de tipul dozei”

**Context 5 propoziții:** I7 **§5.2.12.3.7**, p61, folosește explicit **„cu prioritate”** pentru suprafețele verticale. Articolul imediat următor, **§5.2.12.3.8**, admite și **doze montate pe sau în pardoseală**, dar **numai dacă sunt omologate** pentru aceasta. Prin urmare A transformă o recomandare de prioritate într-o exclusivitate falsă, iar C elimină condiția privind produsul omologat. B păstrează precis forța normativă a adverbului „prioritate”. **Orizontal:** A↔B doar vs prioritar; B↔C prioritate vs montaj permis condiționat; A↔C exclusivitate vs permisiune necondiționată, ambele contrazise. **Reversie:** B direct din articol, nu eliminare simplă. **Status `INTENDED_B_EXACT_5_2_12_3_7`.**

## Y2 | G1-NOR-092 | cheie B
**Enunț:** „În fiecare instalaţie la nivelul tabloului general trebuie prevăzută”
- A „o bornă / bară principală de legare la pământ, numai atunci când reţeaua de distribuţie este TN-C;”
- B „o bornă / bară principală de legare la pământ,”
- C „o bornă / bară principală de legare la pământ, numai în cazul în care alimentarea receptoarelor se face în sistem TN-S”

**Context 5 propoziții:** I7 **§5.5.2.1**, p72, prevede **o bornă/bară principală de legare la pământ la nivelul tabloului general în fiecare instalație**, fără a restrânge funcția la o singură schemă TN. Textul vecin enumeră **PEN în TN-C**, **PE în TN-S**, **N în TN-C-S**, legăturile de echipotențializare și conductorul de legare la pământ, fiecare în configurația aplicabilă. Astfel A și C includ câte o situație reală, dar termenul **„numai”** le face neconforme cu regula generală. B este varianta completă fără restricție falsă. **Vertical:** A/C `FALSE_ONLY`, B `EXACT_GENERAL`; **orizontal:** A↔C două sisteme cu roluri diferite, ambele inadmisibil de exclusive; B le include pe ambele. **Reversie:** B direct §5.5.2.1. **Status `INTENDED_B_EXACT_SOURCE`.**

## Y3 | G1-NOR-093 | cheie A
**Enunț:** „Circuitele iluminatului normal”
- A „trebuie să fie distincte de circuitele de prize.”
- B „poate fi un circuit comun pentru iluminat normal și prize dacă puterea totală instalată pe circuit nu depășește 2 kW”
- C „poate fi un circuit comun pentru iluminat normal și prize dacă puterea totală instalată pe circuit nu depășește3 kW pe un circuit monofazat şi 8 kW pe un circuit trifazat”

**Context 5 propoziții:** I7 **§5.4.1**, p70, cere ca **circuitele iluminatului normal** să fie **distincte de circuitele de prize**. Limitele de **3 kW monofazat / 8 kW trifazat** din §5.4.5 se referă la **numărul/dimensionarea circuitelor de iluminat**, nu autorizează unirea prize + iluminat. Limita de **2 kW** din §5.4.7 se referă la **puterea instalată pe circuitul de prize** în clădirile respective, nu la o excepție de separare a circuitelor. Variantele B și C importă astfel cifre autentice din articole vecine în **obiectul greșit**. A este răspunsul pozitiv și exact. **Vertical:** A `DIRECT_5_4_1`, B/C `WRONG_SCOPE_CIRCUIT_POWER`; **orizontal:** B/C au praguri/obiecte diferite fără a învinge interdicția generală de partajare. **Reversie:** A sprijinită direct, **status `INTENDED_A_EXACT_ARTICLE`.**

## Y4 | G1-NOR-094 | cheie C
**Enunț:** „Rezistenţa prizei de pământ a unei clădiri, atunci când este folosită numai pentru protecţia împotriva şocurilor electrice, trebuie să fie cel mult”
- A „10 Ω”
- B „1 Ω”
- C „4 Ω”

**Context 5 propoziții:** I7 2023 **§5.5.7.11**, p76, oferă **4 Ω** pentru priza folosită **numai la protecția împotriva șocurilor electrice**. În alineatul următor/aceeași rubrică, **1 Ω** este limita pentru **priza comună** care deservește și protecția împotriva trăsnetelor. Articolul precedent **§5.5.7.10** spune că rezistența trebuie în final să permită **deconectarea în timpul impus**, deci pragul de 4 Ω nu substituie calculul eficacității sistemului TN/TT și al dispozitivului de protecție. Varianta A este prea mare față de pragul dat, iar B reprezintă o condiție mai strictă ce apare într-un **alt obiect**. Pentru grila despre **valoarea-limită normativă aplicabilă exact cazului indicat**, C este răspunsul sursă.
**Vertical:** A `NOT_LIMITED_ENOUGH`, B `OTHER_CASE_1_OHM`, C `EXACT_SOURCE_4_OHM`. **Orizontal:** 1Ω respectă matematic ≤4Ω, dar întrebarea cere **limita numerică specificată**, nu exemplu de rezistență admisibilă; A/ C praguri diferite. **Reversie:** C sursă exactă cu aplicație; **status `INTENDED_C_EXACT_4OHM_WITH_DISCONNECTION_GATE`.**

## Y5 | G1-NOR-095 | cheie A
**Enunț:** „Conductorul neutru (N):”
- A „este un conductor conectat electric la punctul neutru al sursei şi care poate contribui la distribuţia energiei electrice”
- B „este un conductor conectat electric la punctul neutru al sursei şi care contribuie  la protecția contra atingerilor indirecte”
- C „este un conductor conectat electric la punctul neutru al sursei şi care contribuie la distribuţia energiei electrice și la protecția contra atingerilor indirecte”

**Context 5 propoziții:** I7 **glosarul §2**, p6, definește conductorul **N** drept conductor conectat la punctul neutru și care **poate contribui la distribuția energiei**. Textul vecin definește explicit **PEN** ca acel conductor care îndeplinește **și funcție de PE, și funcție de N**. Astfel varianta B confundă un conductor de distribuție cu funcția de protecție, iar C adaugă obligația de protecție proprie **PEN**, nedefinită ca funcție generală a simplului N. Varianta A reproduce tipul și modalitatea permisivă „poate”. Nu trebuie confundate **conectarea neutrului la punctul neutru al sursei** și **conductorul de protecție** al consumatorului.
**Vertical:** A `EXACT_N`, B/C `PEN_ROLE_IMPORTED_INTO_N`; **orizontal:** C adaugă protecția la A, B o presupune fără rolul de distribuție; A exclude atribuirea greșită a funcției PE. **Reversie:** A direct glosar, **status `INTENDED_A_EXACT_GLOSSARY`.**

## Asigurare QA și transfer
- Cele 5 au **dovezi afirmative și paragrafe vecine**, nu numai eliminare; falsurile se datorează „doar”/„indiferent”, criterii de sistem, cifre mutate între obiecte și confuzia N/PEN.
- **Atenție prag 4Ω vs1Ω:** nu se schimbă regimul de folosire al prizei de pământ în raționament, iar condițiile de deconectare au prioritate.
- Niciun reviewer independent nu a fost lansat; bibliografia ANRE 2026, drepturile offline și corectitudinea ediției curente rămân deschise. **0/822 approvals**.
