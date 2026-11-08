# ANRE Trainer | Audit didactic V5: documentație PV/eolian și probe concrete

**Data:** 2026-11-08 | **Scop:** exclusiv bibliotecă de surse; **NO_IMPLEMENTATION**.  
**Checkpoint:** CKPT-002 (nemodificat). **Întrebări/bareme:** 822/822 nemodificate.  
**Aprobări independente finale:** 0/44 categorii.  
**Evidențe V5:** 20 rânduri cu proveniență explicită: 10 din I7 local 2023, 9 din articole/tabele oficiale românești, 1 material tehnic NREL extern pentru orientare. Niciun rând nu primește statut `FINAL_APPROVED`.

## 1. Descoperire în biblioteca existentă: I7 §7.11 (PDF pp. 136–138)

**Document local:** `803493174-I7-2011-completat2023.pdf` (I7-2011 sintetizat la data 2023-09-22). Paginile analizate textual: 136–138; figurile paginilor **137 și 138 inspectate vizual**.

Nu este nevoie să procurăm automat o nouă carte pentru o schemă PV introductivă: subcapitolul `7.11 Instalaţii electrice pentru sisteme fotoelectrice de alimentare cu energie` conține:
- `7.11.1–2` (PDF 136): domeniu, definiții celulă/modul/lanț PV, cutie de joncțiune, invertor, zona DC și AC;
- `7.11.4` (136): partea DC poate rămâne sub tensiune după deconectarea AC. **Atenție pentru siguranță**.
- `7.11.7–8` (136): tipul DDR și excepția condiționată de construcția invertorului. Nu deduceți lipsa universală a DDR.
- `7.11.11–13` (136): suprasarcină cabluri DC (cu o condiție legată de ISCSTC) și scurtcircuit pe cablul de alimentare AC. Nu confundați *suprasarcină* cu *scurtcircuit*.
- `7.11.20–25` (137): cabluri DC, separarea invertorului față de DC și AC, separatorul DC, avertizarea în cutiile de joncțiune;
- **Figura 7.11.1** (PDF 137): schema generală de grup PV, inclusiv conexiunile către invertor și partea AC;
- **Figura 7.11.2** (PDF 137–138): exemplu cu mai multe grupuri PV. Titlul figurii este la începutul paginii PDF 138.

**Statut:** `LOCAL_EXACT_ANCHOR_VISUAL_SPOTCHECK`, nu versiune normativă curentă aprobată. I7 sintetizat în 2023 face trimitere la ediții istorice ale standardelor; pentru 2026 verificarea ediției SR și compatibilitatea dispozițiilor tranzitorii rămân în lucru. Niciun desen nu este prezentat drept schemă de execuție.

## 2. Protecții PV: confirmări din acte oficiale

- Ordinul **132/2020**, art. I pct. 6 modifică art. 14 din Norma prosumatorilor aprobată prin Ordinul **228/2018**. În circumstanțele reglementate: comutații AC între sursa de producere și punctul de racordare, funcții de protecție insularizare/limită de tensiune/frecvență/supracurent, diferențe între JT și MT.
- Art. 14 alin. (2) tratează cazul instalației de producere cu puterea instalată **peste 30 kVA** sau locul de consum-producere racordat la MT: relee/funcții externe de interfață în condițiile normei. Nu generalizăm fără caz și configurație.
- Ordinul **959/2023** include explicit instalațiile fotovoltaice aferente clădirilor în domeniul I7, dar art. II stabilește excepții tranzitorii pentru anumite proiecte.

**Încă neacoperit:** un proiect actual de dimensionare și coordonare completă a aparatajului (SPD DC/AC, selectivitate, curent scurtcircuit, protecție diferențială, scheme de comutație și reglaje) validat pe documentul SR/IEC corespunzător cazului.

## 3. Eoliene: de la descriere generică la categorii normative verificabile

- **Ordin 79/2016, anexă:** clasifică unitățile generatoare după **tensiunea punctului de racordare și putere**, nu doar după generatorul eolian: A de la 0,8 kW și sub 1 MW, B 1–sub 5 MW, C 5–sub 20 MW, pentru U<110kV; D pentru U≥110kV sau P≥20MW. Sunt pragurile din anexa oficială consultată, **nu reguli eterne fără revizie**.
- **Norma 208/2018, art. 16** (categorie A sub 1MW) și **art. 34** (categorie B) precizează necesitatea evitării funcționării insularizate neautorizate față de rețeaua publică. Nu concluzionăm că un sistem de backup deliberat, protejat și separat corect ar fi imposibil în orice situație.
- **Art. 35, 56**: cerințe diferențiate pentru categoriile C/D privind comportarea la frecvență și menținerea în funcțiune. Verificarea detaliată, cerințe U/f, Fault Ride Through și setări specifice rămân deschise.
- **Ordin 80/2025** modifică art. 136 din regulile procedurale: durata perioadei de probe în funcție de categorie A: cel mult 6 luni, B/C: 12 luni, D: 24 luni (în condițiile normei). Aceasta este o **cerință procedurală**, nu dovadă de conținut didactic certificat.
- **NREL/SR-5000-66486 (2016)** are, în indexul PDF, secțiuni despre controlul convertoarelor, P/Q și comportare la defect. Lucrarea investighează în principal interconectări la transport din SUA; **nu se importă valorile ca standarde românești**. Captura vizuală web a PDF-ului a eșuat, deci figurile nu sunt certificate vizual.

### Schemă conceptuală ORIGINALĂ, strict pedagogică

**PV conectat la rețea:** `module/lanțuri PV → colectare/combiner când există → comutație și măsuri de protecție DC → invertor DC/AC → comutație/protecție interfață AC → punct de delimitare → rețea`. Legare la pământ, protecțiile de defect și SPD se determină condiționat, conform proiectului și normelor aplicabile. Nu este o schemă executabilă.

**Eolian conectat la rețea:** `rotor → tren de antrenare (după tip) → generator → convertor (dacă topologia îl cere) → transformare/comutație/protecție după tensiune → punct de racordare → rețea`. Nu toate turbinele folosesc același tip de generator și convertor, iar categoria A/B/C/D se determină după U și P, nu după desenul bloc.

## 4. Cele șapte blocaje V4 după reevaluare

Toate **7 rămân deschise**, dar două au dovezi locale/legale mai puternice:
1. `GAP-PV-01`: îmbunătățit, figură și paragrafe PV I7 pp136–138; **nu** proiect complet, nu versiune SR certă.
2. `GAP-PV-02`: îmbunătățit prin art.14, art.16, art.34; valori/teste/ediții încă lipsă.
3. `GAP-PV-03`: edițiile SR EN 50549 și SR HD/IEC aplicabile 2026 încă de stabilit.
4. `GAP-WIND-01`: arhitectură didactică parțială; document extern american nu echivalează cu normă română.
5. `GAP-WIND-02`: pragurile A-D și articole relevante localizate; revizuire pe categorie necesară.
6. `GAP-BOTH-01`: audit de specialitate **independent NOT_RUN**.
7. `GAP-BOTH-02`: permisiuni offline pentru PDF-uri/figuri **NOT_CLEARED**.

## 5. Referințe precise și limitări

**Surse user-provided:** `803493174-I7-2011-completat2023.pdf`, PDF pp136–138 (fără redistribuirea PDF-ului în GitHub).

**Surse oficiale HTML:**
- [I7 consolidat, Portal Legislativ](https://legislatie.just.ro/Public/DetaliiDocument/287132)
- [Ordin 959/2023 modificare I7 și dispoziții tranzitorii](https://legislatie.just.ro/Public/DetaliiDocument/271142)
- [Ordin 132/2020, art.14 protecții prosumatori](https://legislatie.just.ro/Public/DetaliiDocument/227966)
- [Norma tehnică 208/2018, cerințe pe categorii](https://legislatie.just.ro/Public/DetaliiDocument/211640)
- [Ordin 79/2016, clasificare unități generatoare](https://legislatie.just.ro/Public/DetaliiDocument/183869)
- [Ordin 80/2025, art.136 procedură probe](https://legislatie.just.ro/Public/DetaliiDocument/305622)
- [NREL 2016, power converter control (PDF)](https://www.nrel.gov/docs/fy16osti/66486.pdf) (doar sursă de tehnologie; figurile neinspectate din cauza capturii indisponibile).

**QA limitări:** `SOURCE_TEXT_VERIFIED` ≠ `CURRENT_LAW_CERTIFIED`, iar `LOCAL_VISUAL_INSPECTED` ≠ aprobare de inginer proiectant. Verificările sunt realizate într-o sesiune asistată de model, **nu de agenți independenți executați**. Statut 44 categorii: 0 aprobate formal. Niciun răspuns/exercițiu ANRE nu a fost schimbat. Nu se importă documente terțe fără permisiuni.

**Următorul audit:** verificați exact SR EN 50549 și SR HD 60364-7-712 aplicabile, lista de condiții SPD/DC/RCD pentru configurații diferite și schema eoliană + testele de conectare pe categorii, apoi obțineți revizie independentă.
