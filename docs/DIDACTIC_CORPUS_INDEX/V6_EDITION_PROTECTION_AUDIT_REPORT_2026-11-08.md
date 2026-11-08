# ANRE Trainer | Audit didactic V6: ediții SR/EN și cerințe PV/eolian

**Data controlului:** 8 noiembrie 2026. **Scop:** în exclusivitate auditul surselor. **NU** se modifică HTML, APK, baza celor 822 de întrebări sau baremele. **CKPT-002** rămâne ultimul checkpoint. **QA tehnic independent: NOT_RUN; 0/44 aprobări**.

## Descoperiri demonstrate în surse

1. **ASRO afișează SR HD 60364-7-712:2016 drept „în vigoare”** în catalogul consultat. În schimb, **IEC 60364-7-712:2025** este noua ediție internațională, publicată la 21.10.2025, cu extinderi pentru stocare și funcționarea insularizată. Nu presupunem că ediția IEC a fost preluată în România sau a înlocuit deja SR HD: [catalog ASRO](https://magazin.asro.ro/ro/standard/247467) | [IEC](https://webstore.iec.ch/en/publication/65748).
2. **Familia SR EN 50549 necesită amendamentele românești A1:2023.** Buletinul oficial ASRO din decembrie 2023 listează `SR EN 50549-1+AC:2019/A1:2023` (JT) și `SR EN 50549-2:2019/A1:2023` (MT). Catalogul pentru partea 2 confirmă explicit „în vigoare” și legătura cu amendamentul A1:2023. În **PDF-ul ASRO s-a folosit textul extras**; screenshot-ul web a eșuat cu HTTP 403, astfel că nu pretindem confirmare vizuală a paginii. [ASRO bulletin](https://www.asro.ro/wp-content/uploads/2024/01/BS-12-2023.pdf) | [catalog ASRO, part 2](https://magazin.asro.ro/ro/standard/271205).
3. **Protecția, secționarea și comanda** au referința catalogată **SR HD 60364-5-53:2022**, cu erata **/AC:2025** menționată expres de ASRO. Catalogul nu dezvăluie articolele tehnice, deci nu deducem tipuri/dimensionări concrete de SPD, RCD ori selectivitate dintr-o simplă fișă bibliografică. [ASRO](https://magazin.asro.ro/ro/standard/278701).
4. **IEC 62116:2014** identifică procedura de testare anti-insularizare pentru invertoare PV, iar **IEC 61400-21-1:2019** tratează măsurarea caracteristicilor electrice ale turbinelor eoliene. Sunt domenii publicate de editor, **nu** rapoarte de test pe un model de echipament și nici reguli naționale de reglare. [IEC PV](https://webstore.iec.ch/en/publication/6479) | [IEC eolian](https://webstore.iec.ch/en/publication/29528).

## Dovezi tehnice și limitări verificate direct

**PDF-ul local I7**, snapshot **22.09.2023**, pp136–137: §7.11.4 (partea DC poate rămâne sub tensiune când AC este deconectată); §7.11.7–8 (condiții distincte pentru DDR tip B și excepția legată de invertor); §7.11.11–12 (excepția protecției la suprasarcină a cablurilor PV este condiționată, NU echivalează cu absența protecției de scurtcircuit); §7.11.14 (reducerea buclelor de cablu pentru tensiuni induse de trăsnet); §7.11.16–17 (dimensionare după caracteristicile DC ale echipamentelor); §7.11.21–24 (separare la întreținere și etichete de avertizare). Aceste pagini au text selectabil și figuri observate în V5, dar sunt **doar snapshot local, nu ediție juridic certificată pentru 2026**.

**Norma ANRE aprobată prin Ordinul 228/2018, consolidată după 132/2020** este accesibilă public la [Portal Legislativ](https://legislatie.just.ro/Public/DetaliiDocumentAfis/227152):
- **Art. 14(1)(b):** protecție de interfață pentru insularizare, tensiune, frecvență și supracurent în condițiile normei.
- **Art. 14(2)–(3):** diferențierea >30 kVA sau MT față de <=30 kVA racordare JT și utilizarea condiționată a funcțiilor încorporate ale invertorului; nu afirmați că toți prosumatorii au nevoie de relee externe.
- **Art. 14(4):** consum propriu în mod insularizat este condiționat de împiedicarea injecției în rețeaua ORR și de soluția tehnică agreată; nu afirmați că orice backup este interzis.
- **Art. 17(2):** un sistem de stocare cu invertor AC propriu are condiții explicite pentru întreruptor/protecții de interfață.
- **Art. 18(3), (8):** ORR coordonează selectivitatea și sunt necesare scheme/reglaje de proiect pentru etapa de probe; nu publicăm valori de protecție ca recomandări de execuție universală.

Dovada de **conținut normativ** (text legal disponibil) este distinctă de dovada de **ediție standard** (catalog), distinctă de **dovada verificării tehnice finale** (în continuare zero). Relevanța unui articol la data unei instalații trebuie verificată separat.

## Rezultat măsurabil

| Indicator | V6 |
|---|---:|
| Repere de ediții/catalog/surse locale | 10 |
| Constatări localizate la § / art. / domeniul public al standardului | 14 |
| Blocaje V5 revizuite | 7/7 |
| Blocaje final rezolvate | 0/7 |
| Categorii didactice aprobate independent | 0/44 |
| Implementare HTML/APK și bareme | Neschimbate |

### Ce continuăm

1. Obținerea **legală** a articolelor tehnice exacte din edițiile SR, necesare SPD/DC/RCD și selectivității; între timp folosim doar principiile deja confirmate în surse și rezumate originale.
2. Verificarea clasei A/B/C/D pentru turbine, cu documentația tipului de generator, tipului de conectare și cerințele ORR; standardul EN 50549-2 nu poate fi proiectat asupra tuturor claselor C/D.
3. Audit tehnic și normativ **real, independent**, cu nume/revizie/dovezi, apoi doar după validarea tuturor conceptelor se reia auditul celor 822 de întrebări. Drepturile pentru includerea PDF-urilor/figurilor protejate offline rămân neclarificate; utilizare numai privată până la permisiuni.

**Regulă de siguranță:** aceasta este mapare de surse pentru un material educațional, nicidecum proiect electric sau reglaj pentru instalație reală. Fără text comercial copiat în repo. Cost API nou: 0 lei. Nu s-a creat CKPT-003.
