# ANRE Trainer | V33: Primele patru conflicte I7, reverificare efectivă

**Statut:** analiză de sursă/limbaj asistată de model, verificare pe PDF I7 2023-09-22; NU aprobări independente. **Data:** 2026-11-11. **Ramură:** `audit/anre-v8-priority-17-20261109`, PR #7 Draft.

## Input și păstrarea baremelor
- Date canonice: V10.29 GitHub HTML blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`; toate 4 ID-uri/enunțuri/A/B/C/chei citite direct din acel blob.
- Referință: utilizatorul a încărcat `803493174-I7-2011-completat2023(1).pdf`, 249 pagini, forma sintetică 22.09.2023, SHA-256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`. Paragrafele au fost recitite local în paginile de mai jos, nu deduse doar din raportul V29.
- Portalul oficial I7 `https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132` este detectabil în indexul web, dar accesările directe ale paginii și operațiile de căutare în document au returnat HTTP 502 în sesiunea curentă. Istoricul complet al actelor aplicabile în 2026 rămâne `PENDING`.
- Toate cheile în aplicație rămân **neschimbate**; nu se modifică întrebările/opțiunile automat.

## Rezultatele pentru fiecare întrebare

### G1-NOR-010 | Cheia canonică B | candidata C
**Întrebare:** „În instalaţiile de joasă tensiune aferente clădirilor, rezistenţa electrică a izolaţiei trebuie măsurată:”
- A numai între două conductoare active
- B numai între conductoarele active luate 2 câte 2
- C între conductoarele active şi conductorul de protecţie conectat la reţeaua de legare la pământ

**I7 8.1.1.3.3 (PDF pagina 162):** cere măsurarea între conductoarele active și conductorul de protecție conectat la rețeaua de legare la pământ; activele pot fi conectate împreună pentru această încercare. Limitarea „numai” din A/B contrazice prezentarea condiției în I7.
**Propunere:** C susținută de PDF 2023, B în conflict. **Status:** `KEY_CONFLICT_CANDIDATE`, nu schimbare aprobată.

### G1-NOR-012 | Cheia canonică B | candidata C (condiționat)
**Întrebare:** „La circuitele electrice pentru alimentarea receptoarelor de importanţă deosebită (receptoare din blocul operator al spitalelor, iluminat de siguranţă, etc) materialul conductoarelor este:”
- A întotdeauna aluminiu
- B întotdeauna cupru
- C cupru sau aluminiu, condiţionat

**I7 5.1.7.2(a) (PDF pagina 49):** cerința de cupru pentru receptoare critice apare explicit **atunci când** secțiunea echivalentă a conductorului de aluminiu ar ieși sub 10 mm². Expresia „întotdeauna” din B elimină condiția citată.
**Propunere:** C este candidată în logica articolului, dar altă normă mai severă pentru circuite spital/siguranță ar putea conta. **Status:** `CONDITIONAL_OTHER_RULES_PENDING`.

### G1-NOR-029 | Cheia canonică B | candidata C
**Întrebare:** „Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:”
- A 2 m
- B 2,3 m
- C 2,5 m

**I7 5.3.3.21 (PDF pagina 65):** valoarea generală este 2,3 m; există o excepție formulată expres pentru **locuințe**, maximum 2,5 m.
**Propunere:** C corespunde enunțului „din locuințe”; B ignoră excepția. **Status:** `DWELLING_EXCEPTION_KEY_CONFLICT`.

### G1-NOR-032 | Cheia canonică B | nicio variantă 25 m
**Întrebare:** „Montarea dozelor de trecere este obligatorie în cazul în care lungimea coloanelor în linie dreapta, pe orizontală, depăşeşte:”
- A 10 m
- B 15 m
- C 20 m

**I7 5.2.12.3.10 (PDF pagina 62):** pe trasee drepte distanța uzuală între dozele de tragere este maximum 25 m, versus 15 m pe trasee cu până la trei curbe. **Fraza următoare permite distanțe mai mari prin utilizarea unui tub cu diametru cu o treaptă mărit**, deci chiar și formularea „obligatorie” din întrebare necesită control lingvistic.
**Propunere:** nu se schimbă doar cheia: se revizuiește **întreg enunțul și setul de opțiuni** pentru precizia tehnică. **Status:** `NO_VALID_OPTION_AND_ABSOLUTE_WORDING`.

## Protocol / gates
1. Confruntă cele patru paragrafe cu ultima formă legală și actele modificatoare și verifică în particular excepțiile de timp, ediție și regulile sectoriale.
2. Auditor electrotehnic și lingvist român independenți trebuie să verifice sensul exact al tuturor celor patru opțiuni, nu doar baremul curent.
3. QA independent revalidează sursa și legăturile offline, iar utilizatorul aprobă orice modificare în aplicație.

**Rezultat real în acest lot:** 4/4 întrebări confruntate cu articol exact în PDF-ul 2023, **3 propuneri condiționate de corectare a cheii** și **1 întrebare fără opțiune potrivită + problemă de formulare**. **0/4 aprobări independente**. Nu înseamnă că alte 818 sunt verificate la aceeași profunzime.

**Interdicții respectate:** fără schimbare chei, ABC, HTML, APK, main, fără merge/release; PR Draft.