# CKPT-076 | P1 Lot Z: NOR-096/097/098/099/100 și granița ≥ vs > | 2026-11-16

## Stare și proveniență
- Repo AcoBenny/ANRE_Trainer, branch audit/anre-v8-priority-17-20261109, PR #7 Open/Draft, HEAD pre-write 6b6c29732731546eeb8999dc3781113fb69410c8.
- Cinci unități P1 noi din MASTER, necreditate în CKPT-047/049/050–075: G1-NOR-096 AU-508227abb043a8f8, NOR-097 AU-db8ac3da5d827854, NOR-098 AU-f9d0079cffefc45c, NOR-099 AU-6050ffc3f4ef041c, NOR-100 AU-7f4876eff2e3a044, un ID/unitate.
- Cumul după CKPT-075: **165/568 unități, 209/822 ID-uri**; delta +5/+5 ⇒ **170/568 unități, 214/822 ID-uri** contextuale. **0/822 aprobate**.
- Sursă exactă direct citită din PDF Library utilizator `803493174-I7-2011-completat2023.pdf`, sinteză 22.09.2023, glosar pp6–9, §§5.5.7.2–.4 pp75–76, §4.1.5.5.6 p31. Nu se pretinde inspectarea ediției oficiale/anului 2026, nici QA independent. Nicio editare a baremului, textelor, variantei, aplicației, main, merge/release.

## Z1 | G1-NOR-096 | cheia A
**Original:** „Curentul admisibil  este”
- A „valoarea maximă a curentului electric care poate parcurge în permanenţă un conductor, un dispozitiv sau un aparat, fără ca temperatura sa în regim permanent, în condiţii date, să fie superioară valorii specificate.”
- B „valoarea maximă a curentului electric care poate parcurge un conductor, un dispozitiv sau un aparat, fără ca temperatura sa în regim de scurtcircuit să fie superioară valorii specificate.”
- C „valoarea maximă a curentului electric care poate parcurge în permanenţă un conductor, un dispozitiv sau un aparat, fără ca temperatura sa în condiţiile unei puneri la pământ, să fie superioară valorii specificate.”

**Context 5 propoziții:** Glosarul I7, p6, definește **curentul admisibil Iz** prin **regimul permanent** și **temperatura admisibilă** în condițiile date. Această mărime nu trebuie confundată cu **solicitarea termică la scurtcircuit**, care este limitată de timp și include parametri adiabatici specifici. De asemenea, un **defect de punere la pământ** nu este situația de funcționare normală permanentă din definiție. Alternativa A reproduce definirea cantității cu obiectul și durata corectă. B și C deplasează același obiect spre un regim de defect.
**Vertical:** A `DIRECT_I7_GLOSSARY`, B/C `WRONG_OPERATING_REGIME`. **Orizontal:** A vs B/C permanent normal vs defect, B vs C două defecte diferite. **Reversie:** A are definiție pozitivă. **Status `INTENDED_A_EXACT_GLOSSARY`.**

## Z2 | G1-NOR-097 | cheia C
**Original:** „Curent nominal este un”
- A „curent electric destinat a fi transportat de un circuit în funcţionarea în regim de defect simplu un timp limitat”
- B „curent electric destinat a fi transportat de un circuit în funcţionarea în regim de scurtcircuit un timp limitat”
- C „curent electric destinat a fi transportat de un circuit în funcţionarea normală pe timp nelimitat”

**Context 5 propoziții:** I7 glosar p7 definește **curent nominal** ca **curent destinat transportului în regim normal** pe timp nelimitat. Curentul de defect simplu sau de scurtcircuit poate solicita instalația pentru durate limitate, dar nu este valoarea nominală a circuitului. În vecinătate, glosarul distinge curentul de serviciu, curentul de scurtcircuit și curentul de suprasarcină. Variantele A/B sunt concepte diferite ca **regim și durată**, nu doar mărimi diferite numeric. C redă exact definiția normativului.
**Vertical:** A/B `FAULT_TEMPORARY`, C `NORMAL_UNLIMITED`. **Orizontal:** A↔B două tipuri de defecte, C↔A/C↔B regim normal vs defect. **Reversie:** C direct din glosar. **Status `INTENDED_C_EXACT`.**

## Z3 | G1-NOR-098 | cheia A
**Original:** „Pentru realizarea prizelor de pământ se recomandă electrozi din”
- A „bare rotunde, ţevi sau profil cruce”
- B „conductele metalice pentru lichide inflamabile sau gaze.”
- C „obiectele metalice cufundate în apă”

**Context 5 propoziții:** I7 **§5.5.7.2**, p75, enumeră exact **bare rotunde, țevi și profil cruce** drept tipuri recomandate de electrozi de pământ. Articolul imediat următor **§5.5.7.3** interzice folosirea ca electrozi a **conductelor pentru lichide inflamabile sau gaze**. **§5.5.7.4**, p76, interzice utilizarea **obiectelor metalice cufundate în apă** ca electrozi. Trimiterile vecine clarifică faptul că o **legătură de echipotențializare** la conducta metalică permisă în alte condiții **nu o transformă în electrod de pământ**. Alegerea A este susținută direct, iar B/C sunt interdicții specifice.
**Vertical:** A `POSITIVE_ELECTRODE_TYPE`, B/C `PROHIBITED_AS_ELECTRODE`. **Orizontal:** A↔B/A↔C electrod dedicat vs infrastructură interzisă; B↔C conducte periculoase vs obiecte în apă, ambele interzise ca electrozi. **Reversie:** A exact I7 cu condiții anticorozive din §5.5.7.5. **Status `INTENDED_A_POSITIVE_WITH_PROHIBITIONS`.**

## Z4 | G1-NOR-099 | cheia C
**Original:** „Priza de pământ este o”
- A „parte conductoare încorporată obligatoiu în pământ”
- B „parte conductoare care poate fi încorporată într-un mediu conductor specific, de exemplu beton sau cărbune, izolat față de pământ.”
- C „parte conductoare care poate fi încorporată în pământ sau într-un mediu conductor specific, de exemplu beton sau cărbune, în contact cu pământul.”

**Context 5 propoziții:** Definiția exactă din glosarul I7 p9 descrie **priza de pământ** ca **parte conductoare încorporată în pământ sau mediu conductor specific aflat în contact cu pământul**. A introduce obligația ca electrodul să fie **direct** încorporat în sol, deși norma permite și varianta în **betonul fundației** în contact electric relevant cu pământul. B elimină **contactul cu pământul**, ceea ce ar împiedica funcția definită a prizei. C păstrează atât mediile alternative, cât și legătura necesară cu pământul. „Cărbune” este un exemplu istoric din definiție, nu recomandare de a modifica arbitrar umplutura unui electrod.
**Vertical:** A `FALSE_OBLIGATORIU_SOIL_ONLY`, B `FALSE_EARTH_INSULATED`, C `EXACT_GLOSSARY_EARTH_CONTACT`. **Orizontal:** A↔C sol exclusiv vs sol sau mediu conductor, B↔C izolat vs contact, A↔B condiții diferite. **Reversie:** C direct sursă. **Status `INTENDED_C_EXACT`.**

## Z5 | G1-NOR-100 | cheia B, capcană strictă de inegalitate
**Original:** „Rezistenţa de izolaţie a pardoselii şi pereţilor în fiecare punct de măsurare în condiţiile specificate în SR EN 61140 şi verificate printr-o metoda recomandată în Anexa 8.1 din I7/2011, dacă tensiunea nominală a instalaţiei nu depăşeşte 500 V în tensiune continuă sau alternativă, trebuie să fie mai mare de”
- A „75 kΩ”
- B „50 kΩ”
- C „100 kΩ”

**Context 5 propoziții:** I7 **§4.1.5.5.6**, p31, precizează că rezistența pardoselilor și pereților **„nu trebuie să fie mai mică de 50 kΩ”** pentru tensiuni nominale de cel mult 500 V. Aceasta înseamnă matematic **R≥50 kΩ**, inclusiv egalitatea exactă la 50 kΩ. Enunțul folosește însă **„mai mare de”**, adică strict **R>50 kΩ**, care exclude valoarea-limită exact permisă de sursă. **B** este răspunsul numeric și intenția evidentă a grilei, dar formularea strictă nu este o transcriere identică a normei. A și C sunt praguri mai mari decât minimum, care pot satisface anumite instalații bune, dar nu exprimă **limita normativă**; „peste 500V” are alt prag, 100 kΩ.

**Vertical:** A/C `WRONG_NORMATIVE_MINIMUM`; B `INTENDED_B_NUMERIC_BUT_STRICT_INEQUALITY_ERROR`. **Orizontal:** A/B/C sunt praguri alternative, nu afirmații despre rezistența măsurată a unui caz particular; însă „mai mare” și „nu mai mică” nu sunt identice la frontieră. **Reversie:** B justificată numeric prin §4.1.5.5.6, dar **nu este propoziția normativă exactă**; 50kΩ trece sursa, eșuează literala întrebării. **Status `INTENDED_B_STRONG` + `STRICT_VS_NONSTRICT_BOUNDARY_BUG`, QA independent necesar înainte de aprobare.**
**Test negativ:** la R=50 kΩ, `R>=50` este adevărat, `R>50` este fals. Diferența nu poate fi ignorată când itemul se referă exact la prag.

## Regresii și QA
- **Context vecin decisiv:** NOR098 paragrafele `§5.5.7.2–.4` stabilesc atât electrozii admiși, cât și excluderile; NOR099 glosarul condiționează mediul de **contactul cu pământul**.
- **`BOUNDARY_LANGUAGE_ERROR`** din NOR100 este lecție transversală pentru QA numeric/juridic: „peste”/„cel puțin”, „mai mare”/„mai mare sau egal”, „nu depășește”/„mai mic”, cu teste la egalitate.
- QA efectiv a fost citire sursă textuală în PDF Library și argumentare A/B/C același asistent; **nu** sunt teste independente de la alt agent și nu s-a verificat exhaustiv versiunea bibliografică ANRE 2026. Fără corecții barem/QABC; `0/822` approvals.
