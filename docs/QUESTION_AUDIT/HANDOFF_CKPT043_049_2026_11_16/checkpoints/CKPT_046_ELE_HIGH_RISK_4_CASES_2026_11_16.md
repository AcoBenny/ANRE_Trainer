# CKPT-046 | ANRE Trainer | Două mini-loturi ELE problematice | 16.11.2026

**Stare:** document de audit **LOCAL**, nu commit GitHub. Continuă CKPT-042 pe PR #7 Draft și CKPT-043/044/045 locale. **Nu modifică baremele, QABC, HTML, APK sau main.**

## Status operațional

| Etapă | Distincte | ID-uri grad I/II |
|---|---:|---:|
| Toată banca | 568 | 822 |
| Probleme suspectate, de verificat întâi | 297 | 352 |
| Fișe contextuale deja înregistrate în GitHub la CKPT-042 | 15 | 25 |
| Noi cercetate în acest checkpoint local | **4** | **8** |
| Total contextual după sincronizare, dacă nu apar suprapuneri | **19** | **33** |
| Mai trebuie fișe contextuale după sincronizare | **549** | **789** |
| APROBATE pentru învățare | **0** | **0** |

Metodologie: 30/30 loturi de triere preliminară acoperă 568/568, dar cercetarea contextuală și QA independent nu sunt terminate. Nici o cercetare locală nu este numărată ca aprobare finală.
## Mini-lotul A | ELE-156 și ELE-219

### G1-ELE-156 | G1-ELE-156, G2-ELEC-294
**Baremuri originale neschimbate:** {"G1-ELE-156": "B", "G2-ELEC-294": "B"}. **Candidat cercetare:** `B_PLAUSIBLE_ONLY_FOR_DEFINED_PROTECTION_ZONE_NO_UNIQUE_PREFERENCE_PROVEN_NOT_APPROVED`.

> Pe liniile electrice de înaltă tensiune, unde se preferă montarea transformatoarelor de  curent ?:

- **A:** între barele colectoare şi separatorul de bare;
- **B:** între separatorul de bare şi întreruptor;
- **C:** între întreruptor şi separatorul de linie.

**Analiză prin suport direct + eliminare:**
- **A:** Nu corespunde celor două poziții tipice BE1/BE2 din schema Siemens și nu avem dovadă că ar fi preferată în configurația întrebată.
- **B:** Configurație fizic posibilă și susținută explicit de Siemens (BE1), coincide cu cheia veche; dar «se preferă» nu este dovedit fără schema de protecție.
- **C:** Configurație fizic posibilă și susținută explicit de Siemens (BE2); nu poate fi exclusă doar fiindcă B este cheia istorică.

**Explicație contextuală:** În manualul **Siemens SIPROTEC 7SS85 §5.4.3, figura 5-38**, sunt desenate **două amplasări interioare posibile** ale transformatorului de curent: **BE1** între separatorul de bare și întreruptor și **BE2** între întreruptor și separatorul de linie. Poziția afectează **limitele zonei de protecție** și modul în care funcțiile de protecție interpretează curenții. De aceea **B** este fezabilă, dar **C nu poate fi eliminată** doar din criteriul poziției fizice. **A** nu primește suport pozitiv din schema verificată, deși alte topologii ar necesita analiză separată. Pentru cuvântul **„se preferă”**, trebuie identificată **schema/norma exactă și scopul protecției**, nu presupusă o preferință universală.

**Referințe precise:**
- [Siemens SIPROTEC 5 7SS85 V8.01, §5.4.3, figura 5-38, pagină imprimată 264 (2020)](https://cache.industry.siemens.com/dl/files/351/109742351/att_1010616/v1/SIP5_7SS85_V08.01_Manual_C019-9_en.pdf) | protecție diferențială de bare Siemens, nu toate instalațiile de înaltă tensiune. **Limitare:** text PDF citit prin căutare web; screenshot web a eșuat Cache miss.
- [ANRE, bibliografia și exemplele de întrebări, pagina oficială (la 16 nov. 2026 continuă să afișeze versiuni 2023/2024)](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) | navigare bibliografie, NU aprobare exactă a unei grile. **Limitare:** pagină ANRE citită (public).

**Rămâne de verificat:** norma/ediția efectivă care definește preferința B vs C pentru categoria de instalații; schema de protecție/zonă și condițiile de amplasare; QA tehnic și lingvistic independent.

### G1-ELE-219 | G1-ELE-219, G2-ELEC-355
**Baremuri originale neschimbate:** {"G1-ELE-219": "A", "G2-ELEC-355": "A"}. **Candidat cercetare:** `NO_UNIQUE_PROVEN_A_OR_B_ARC_MODEL_NOT_DEFINED`.

> Schema echivalentă de calcul în cazul producerii unui scurtcircuit trifazat şi la pământ, cu arc, se compune din:

- **A:** schema de secvenţă directă (pozitivă) înseriată cu triplul impedanţei arcului
- **B:** schema de secvenţă directă (pozitivă)
- **C:** schema de secvenţă directă (pozitivă) înseriată cu schema de secvenţă inversă (negativă).

**Analiză prin suport direct + eliminare:**
- **A:** 3×Zf este forma cunoscută în rețeaua de secvență zero la defectul monofazat la pământ; pentru TREI arcuri egale pe faze în regim simetric, modelul simplificat adaugă Zarc pe fază, nu 3×Zarc. Totuși definiția exactă a impedanței arcului din grilă lipsește, deci A nu este invalidată definitiv.
- **B:** Rețeaua numai de secvență pozitivă este corectă pentru defect TRIFAZAT SIMETRIC; însă dacă arcurile au impedanță nenulă, B nu precizează componenta impedanței de defect. B poate fi incompletă.
- **C:** Secvența negativă nu apare pentru defectul trifazat perfect simetric; C este incompatibilă cu modelul simetric, în absența unor arcuri distincte nesimetrice.

**Explicație contextuală:** Un **scurtcircuit trifazat simetric** are trei curenți egali ca modul și defazați cu 120°, astfel încât în analiza componentelor simetrice intervine **doar secvența pozitivă**, conform exemplelor **SEL, secțiunile II-b/III-d/IV-d**. Formula clasică **3Zf** apare în tratarea anumitor **defecte monofazate la pământ** în rețeaua homopolară, nu se aplică automat la trei arcuri identice. Într-un model simplificat cu **trei impedanțe de arc identice Zarc**, câte una pe fază, fiecare curent ar vedea **Z1 + Zarc**, nu **Z1 + 3Zarc**. **B** exprimă doar tipul rețelei de secvență și poate omite arcul, iar **C** introduce inutil secvența negativă pentru cazul simetric. Prin urmare cheia originală **A este neconfirmată**, iar o variantă unică nu se poate alege fără a ști **configurația și convenția impedanței arcului**.

**Referințe precise:**
- [SEL, Tutorial on Symmetrical Components Part 2, exemplul II-b / III-d / IV-d, figuri de secvență, 2020](https://cms-cdn.selinc.com/assets/Literature/Publications/White%20Papers/LWP0010-02_TutorialSymmetrical-Pt2_AH_20201019.pdf?v=20201020-155433) | 3-phase balanced fault; exemplele cu contact metalic (bolted) nu includ explicit modelul celor trei arcuri. **Limitare:** text PDF citit, screenshot web Cache miss.
- [ANRE, bibliografia și exemplele de întrebări, pagina oficială (la 16 nov. 2026 continuă să afișeze versiuni 2023/2024)](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) | navigare bibliografie, NU aprobare exactă a unei grile. **Limitare:** pagină ANRE citită (public).

**Rămâne de verificat:** manual exact de electrotehnică folosit în grila ANRE și definiția impedanței arcului; diagramă cu trei arcuri vs unul comun și posibilă asimetrie; QA independent de componente simetrice și calcul numeric.


## Mini-lotul B | ELE-221 și ELE-226

### G1-ELE-221 | G1-ELE-221, G2-ELEC-357
**Baremuri originale neschimbate:** {"G1-ELE-221": "A", "G2-ELEC-357": "A"}. **Candidat cercetare:** `B_SCOPE_SPECIFIC_NOT_APPROVED_STORED_A_NEEDS_ROMANIAN_NORM`.

> Scopul normării distanţelor de izolare în aer minime admisibile pentru instalaţiile electrice este asigurarea:

- **A:** protecţiei personalului de exploatare a instalaţiei;
- **B:** siguranţei în funcţionare a instalaţiei, prin reducerea numărului de defecte în instalaţie;
- **C:** realizării unei economii de teren.

**Analiză prin suport direct + eliminare:**
- **A:** Distanțele de siguranță pentru persoane sunt bazate parțial pe valorile dielectrice, dar scopul lor imediat este protecția împotriva atingerii/apropierii; nu confundăm două distanțe care pot avea valori și obiecte diferite. A este legată de scopul GENERAL al instalației, nu neapărat de obiectul exact minim dielectric.
- **B:** Distanța de izolare între faze ori față de pământ este stabilită pentru susținerea tensiunilor fără străpungere/conturnare; B descrie scopul dielectric mai direct. Este candidat tehnic, nu key confirmat în bibliografia ANRE.
- **C:** Economia de teren este un obiectiv secundar de compactare, nu justifică normarea unei DISTANȚE MINIME pentru izolație.

**Explicație contextuală:** **Distanța minimă de izolare în aer** dintre părțile sub tensiune este concepută în primul rând pentru **rezistența dielectrică** și evitarea conturnării sau străpungerii. **IEC 61936-1:2021 §5.4** tratează aceste distanțe, în timp ce **§7** le folosește ca bază pentru anumite **distanțe de siguranță** și măsuri de protecție a personalului. Astfel, varianta **B** descrie direct funcționarea fără defecte de izolație, dar **A** are o legătură indirectă reală cu protecția persoanelor. Varianta **C** nu exprimă obiectivul unei limite dielectrice minime. **Nu schimbăm A în B** fără clauza românească exactă folosită de examen și fără evaluarea scopului întrebării.

**Referințe precise:**
- [IEC 61936-1:2021 §5.4 (minime distanțe de izolare), §7 (distanțe de siguranță), pagina oficială a standardului](https://webstore.iec.ch/en/publication/64490) | instalații electrice cu tensiuni peste 1 kV, domeniul IEC specific; nu este certificată identitatea cu bibliografia ANRE. **Limitare:** pagina oficială de prezentare verificată; textul complet al clauzei §5.4 din copie secundară, NU verificat în originalul IEC cu acces licențiat.
- [ANRE, bibliografia și exemplele de întrebări, pagina oficială (la 16 nov. 2026 continuă să afișeze versiuni 2023/2024)](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) | navigare bibliografie, NU aprobare exactă a unei grile. **Limitare:** pagină ANRE citită (public).

**Rămâne de verificat:** PE101 ediție și paragraf românesc care distinge izolarea de protecția personalului; domeniul instalației în examen: JT/IT și gradul bibliografiei; QA separat și validare ediție.

### G1-ELE-226 | G1-ELE-226, G2-ELEC-362
**Baremuri originale neschimbate:** {"G1-ELE-226": "A", "G2-ELEC-362": "A"}. **Candidat cercetare:** `NO_DIRECTION_DEFINED_UNDER_BUDEANU_NO_UNIQUE_ABC_CERTIFIED`.

> Sensul puterii deformante într-un circuit format dintr-un generator care produce o undă sinusoidală şi o bobină cu miez de fier saturat este:

- **A:** de la generator spre bobină
- **B:** întotdeauna de la bobină spre generator
- **C:** poate avea oricare sens, în funcţie de încărcarea generatorului

**Analiză prin suport direct + eliminare:**
- **A:** În definiția clasică Budeanu, D_B=√(S²−P²−Q_B²) este scalar nenegativ și nu are sens fizic direcțional. Nu putem deriva A din această formulă. O altă definiție/flux de armonici ar necesita document și convenție.
- **B:** «Întotdeauna» atribuie sens obligatoriu bobină→generator; nicio dovadă primară disponibilă nu confirmă afirmația ca lege universală.
- **C:** Nu decurge din definiția scalară că semnul/„sensul” variază cu încărcarea generatorului; este posibil un model de armonici diferit, dar trebuie precizate condițiile.

**Explicație contextuală:** În teoria clasică **Budeanu**, puterea deformantă este o **mărime scalară** calculată din componentele aparente, active și reactive, nu un flux cu orientare fizică prestabilită. Articolul **Czarnecki (IEEE, 1987)** contestă interpretarea energetică a acestei mărimi, iar studiile moderne separă definițiile diferitelor componente ale puterii. Versiunea oficială **IEEE 1459-2025** este o rescriere semnificativă a celei din 2010, iar Anexa G discută noțiuni omise; sursele secundare ale **G.1** indică eliminarea vechii puteri deformante, însă textul licențiat nu a fost verificat direct. În această perspectivă, nici **A**, nici **B**, nici **C** nu rezultă demonstrabil fără a preciza **teoria și convenția de sens** a grilei istorice. **Baremul A rămâne nemodificat**, iar standardul IEEE modern nu se impune retroactiv fără verificarea bibliografiei ANRE.

**Referințe precise:**
- [Czarnecki, What is Wrong with the Budeanu Concept of Reactive and Distortion Power (IEEE TIM, 1987)](https://repository.lsu.edu/eecs_pubs/538/) | teorie a puterii în regim nesinusoidal; nu grilă ANRE. **Limitare:** fișa articolului și rezumatul citite, textul original complet nu a fost citit.
- [IEEE Std 1459-2025, standard activ, publicat 16 mai 2025, Anexa G privind omisiunile față de 2010](https://standards.ieee.org/ieee/1459/7578/) | standard de MĂSURARE IEEE; nu rezolvă automat baremul istoric ANRE. **Limitare:** pagina oficială IEEE verificată, conținutul Annex G.1 consultat DOAR prin indexări secundare, sursa integrală cu drepturi nu a fost deschisă.
- [Sołjan & Popławski, Energies 2024, 17(5), 1043, analiza teoriei Budeanu](https://www.mdpi.com/1996-1073/17/5/1043) | literatură generală puteri în regim nesinusoidal. **Limitare:** articol peer-reviewed cu text HTML citit.
- [ANRE, bibliografia și exemplele de întrebări, pagina oficială (la 16 nov. 2026 continuă să afișeze versiuni 2023/2024)](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) | navigare bibliografie, NU aprobare exactă a unei grile. **Limitare:** pagină ANRE citită (public).

**Rămâne de verificat:** manualul exact de curs/test care atribuie sens „puterii deformante” și convenția sa; comparare versiuni IEEE1459-2010/2025 NUMAI ca instrument didactic, nu normă de examen fără bibliografie; QA independent și verificare original ANRE.

## Regresii verificate local (structurale și matematice sintetice)

- G1-ELE-156: canonical identity, ABC, evidence & gate PASS
- G1-ELE-219: canonical identity, ABC, evidence & gate PASS
- G1-ELE-221: canonical identity, ABC, evidence & gate PASS
- G1-ELE-226: canonical identity, ABC, evidence & gate PASS
- ELE219 synthetic balanced 3-arc phasor counterexample PASS; NOT norm QA

**Limită:** comparația manualelor, citirea textului PDF și testul numeric nu sunt QA independent, nu certifică edițiile de examen și nu permit învățarea din aplicație. Un PDF oficial complet cu drepturi sau imaginea exactă nu au fost validate vizual; încercările de screenshot web pentru documentele Siemens/SEL au eșuat Cache miss.

## Lecții transferabile și ce urmează

1. Nu transfera formule între **defect trifazat** și **defect monofazat la pământ** fără schema exactă.
2. O poziție fizic posibilă nu stabilește unică **preferința** normativă; **distanță dielectrică** ≠ **distanță de protecție personal**.
3. Un concept istoric precum **puterea deformantă** nu garantează o noțiune fizică de **sens**; întâi se identifică teoria exactă a grilei și ediția.

**Următor:** sincronizează fișierele de la CKPT-043 la CKPT-046 în ramura de audit când GitHub revine, apoi QA independent pe această grupă și un nou lot de P0/P1 cu surse normative exacte. Nu cere utilizatorului să voteze variante fără a-i arăta mai întâi alineatul și raționamentul.

Fișa JSON anexată: `CKPT_046_ELE_HIGH_RISK_4_CASES_2026_11_16.json`.
