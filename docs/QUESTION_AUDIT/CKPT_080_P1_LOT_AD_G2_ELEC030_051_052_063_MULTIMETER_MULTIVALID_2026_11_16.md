# CKPT-080 | P1 Lot AD: G2-ELEC-030/051/052/063 | model electric și CAT multimetrul | 2026-11-16

## Integritate și contorizare
- Repo AcoBenny/ANRE_Trainer, audit/anre-v8-priority-17-20261109, PR #7 Open/Draft, HEAD pre-write `afdc2d30b6308bd6c07d21a64a27182b312e2b00`.
- 4 unități P1/4 ID-uri G2 distincte, fără fișă contextuală în MASTER și fără apariție creditată în CKPT-046/047/049/050–079. De la CKPT-079 **187/568 unități, 242/822 ID-uri**, delta **+4/+4** ⇒ **191/568 unități, 246/822 ID-uri** documentate contextual. **0/822** aprobate.
- Surse utilizate efectiv: OpenStax online, ghidurile Fluke, definiția „tensiune nominală” din PDF I7/2011 forma 2023 oferită de utilizator. **QA independent NOT_RUN**, ultima versiune ANRE 2026 neconfirmată, `OFFICIAL_EXAM_QUESTION_PROVENANCE=UNVERIFIED` pentru întrebările G2-ELEC (este posibil să fie itemi generați din materia didactică și nu grile publicate explicit în XLSX ANRE).
- QABC, cheile, masterul, HTML/APK, main, merge și release rămân neatinse. **Nu se folosește aplicația pentru învățare**.

### G2-ELEC-030 | AU-4227cea322492431 | Transformatorul ideal și curentul continuu constant
**Grad/ID:** G2-ELEC-030, **cheie importată neschimbată:** {"G2-ELEC-030":"A"}.

**Întrebare:** Un transformator ideal nu poate funcționa în regim normal alimentat exclusiv cu:
- **A.** curent continuu constant
- **B.** curent alternativ
- **C.** tensiune alternativă

**Context:** Funcționarea unui **transformator ideal** se bazează pe un **flux magnetic variabil** care induce tensiunea în secundar conform legii lui Faraday, `us=−Ns·dΦ/dt`. Un **curent continuu constant** în primar, după tranzitoriul inițial, nu modifică în timp fluxul și **nu induce o tensiune secundară de regim normal**. Alimentarea în curent alternativ, B, este tocmai regimul clasic în care transformatorul poate transfera puterea prin inducție, iar C desemnează tensiune alternativă, compatibilă cu aceeași funcționare. **A** este răspunsul pozitiv din fizica transformatorului, dar distincția „alimentat cu curent” versus „alimentat cu tensiune” ține de modelul sursei: este cerută funcționarea de transformare în regim normal, nu un impuls temporar de comutare. Nu se deduce din aceasta un prag termic pentru transformatorul real conectat la o sursă DC, deoarece modelul ideal nu include saturație și rezistențe finite.

**A/B/C vertical:** A constant DC ⇒ dΦ/dt=0 în stare stabilă; B AC permis; C tensiune AC permisă.
**A↔B↔C orizontal:** A↔B timp constant vs variație de semn/flux, A↔C DC constant vs tensiune variabilă, B↔C curent și tensiune AC descriu aceeași clasă de regim, nu două răspunsuri prohibitive.
**Reversie/contraexemplu:** Un transformator ideal cu flux constant are us=0 chiar dacă Φ este nenul, iar un impuls DC poate produce un tranzitoriu us≠0 fără funcționare normală susținută.
**Sursă și limită:** OpenStax Transformers: https://openstax.org/books/college-physics-ap-courses-2e/pages/23-7-transformers .
**Verdict:** `A_DIRECT_FARADAY_MODEL; SOURCE_OFFICIAL_QUESTION_PROVENANCE_PENDING` + `INDEPENDENT_QA=NOT_RUN`, `LEARNING_APPROVAL=NO`.

### G2-ELEC-051 | AU-561b8e2f350ce192 | Valoare nominală versus tensiune efectivă măsurată
**Grad/ID:** G2-ELEC-051, **cheie importată neschimbată:** {"G2-ELEC-051":"A"}.

**Întrebare:** Tensiunea nominală a unei instalații reprezintă:
- **A.** valoarea de referință pentru care instalația și echipamentele sunt destinate să funcționeze
- **B.** curentul maxim permanent
- **C.** rezistența conductorului PE

**Context:** În glosarul I7/2011 forma 22.09.2023, p.10, **tensiunea nominală** este valoarea prin care **instalația sau o parte a sa este denumită și identificată**. Această valoare de referință este legată de echipamentele și de categoria de funcționare, așa cum indică A, fără a impune că **tensiunea instantanee reală** coincide tot timpul cu numărul nominal. Alternativa B descrie o mărime de **curent**, nu tensiune, în timp ce C descrie **rezistența unui conductor PE**, deci ambele sunt neconforme chiar la nivel dimensional. **A** este singura alternativă cu obiectul fizic corect, însă este o **parafrază practică** a definiției I7, nu identică cu formularea legală. Termenii „nominal” și „maxim admisibil” nu se pot substitui fără dovadă.

**A/B/C vertical:** A tensiune referențială/identificatoare, B A=amper, nu V, C ohmi, nu V.
**A↔B↔C orizontal:** A↔B și A↔C mărimi incompatibile dimensional; B↔C curent vs rezistență, niciunul nu definește U nominal.
**Reversie/contraexemplu:** O instalație de 230V nominal poate avea tensiune măsurată ce variază într-un interval admis, fără ca indicativul nominal să fie redefinit la fiecare măsurare.
**Sursă și limită:** Biblioteca utilizatorului PDF `803493174-I7-2011-completat2023.pdf`, glosar `tensiune nominală`, p.10, direct căutat și citit în sesiune; modificările post2023 `NOT_EXHAUSTIVELY_CHECKED`.
**Verdict:** `A_CONCEPT_SUPPORTED_WITH_DEFINITION_NUANCE; I7_2023_SOURCE_VERIFIED` + `INDEPENDENT_QA=NOT_RUN`, `LEARNING_APPROVAL=NO`.

### G2-ELEC-052 | AU-0d5ea942e5799e03 | Circuit închis și traseul de curent
**Grad/ID:** G2-ELEC-052, **cheie importată neschimbată:** {"G2-ELEC-052":"A"}.

**Întrebare:** Un circuit electric închis este necesar pentru:
- **A.** circulația continuă a curentului într-un circuit alimentat
- **B.** măsurarea exclusivă a rezistenței
- **C.** anularea tensiunii sursei

**Context:** În circuitul electric elementar alimentat de o sursă, curentul de **conducție** are nevoie de un **traseu închis** între bornele sursei și elementele receptoare. Dacă se deschide conductorul serie, componenta de curent de conducție susținută în acel traseu încetează, chiar dacă la borne poate persista tensiune. **A** corespunde condiției din rețeaua elementară, în timp ce B confundă necesitatea circuitului închis cu o anumită **metodă de măsurare a rezistenței** și C presupune fals că închiderea unui circuit **anulează** tensiunea electromotoare a sursei. Pentru regimuri AC, **cuplajul capacitiv sau electromagnetic** poate transfera energie fără o legătură metalică închisă între toate componentele; în modelul Maxwell există curent de deplasare, deci nu trebuie afirmat că este obligatoriu **circuit galvanic închis universal**. Sursa originală a formulării Grad II și modelul fizic vizat rămân neconfirmate.

**A/B/C vertical:** A traseu de conducție în circuit electric elementar; B operație de măsurare diferită; C fals deoarece U sursei poate persista la sarcină.
**A↔B↔C orizontal:** A↔B funcție de circuit vs metodă de instrumentare; A↔C curgere curent vs zero tensiune, B↔C măsurare rezistență vs anulare U.
**Reversie/contraexemplu:** Sursă ideală 12V + rezistor 12Ω, circuit închis ⇒ 1A, sursa păstrează 12V; comutator deschis ⇒ 0A de conducție în acea ramură.
**Sursă și limită:** OpenStax Kirchhoff circuit analysis https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules .
**Verdict:** `A_INTENDED_BASIC_CONDUCTIVE_NETWORK; NON_GALVANIC_AC_EXCEPTION` + `INDEPENDENT_QA=NOT_RUN`, `LEARNING_APPROVAL=NO`.

### G2-ELEC-063 | AU-c402083bff80c5e8 | Multimetru: categorie CAT și alegere domeniu
**Grad/ID:** G2-ELEC-063, **cheie importată neschimbată:** {"G2-ELEC-063":"A"}.

**Întrebare:** La măsurarea unei tensiuni cu multimetrul, selectarea domeniului trebuie să fie:
- **A.** adecvată valorii estimate și categoriei de măsurare
- **B.** întotdeauna cea mai mică posibilă
- **C.** aleasă fără conectarea sondelor

**Context:** La măsurarea unei tensiuni, domeniul și funcția instrumentului trebuie să corespundă **tensiunii estimate**, iar aparatul și sondele trebuie să aibă **categoria CAT și limita de tensiune** adecvate punctului de măsură. Astfel **A** este o cerință tehnică pozitivă explicită susținută de producătorul Fluke. B spune **„întotdeauna cea mai mică posibilă”**, ceea ce poate provoca depășire de domeniu și este în dezacord cu alegerea unui domeniu suficient de mare pentru valoarea estimată sau necunoscută. Dar și C, **„aleasă fără conectarea sondelor”**, poate exprima o **practică sigură de alegere a funcției înainte de contactul sondelor cu circuitul energizat**, după pașii descriși de Fluke. Cele două idei A și C **nu sunt logic incompatibile**: unul răspunde la **ce domeniu/categorie**, celălalt la **când se face selecția**; dacă C înseamnă însă **fără sonde conectate la aparat** și nu la circuit, semnificația se schimbă. **Baremul A este intenția probabilă**, dar grila necesită clarificarea referentului „sondelor”, a originii reale a întrebării și a definiției operatorului de alegere pentru **unicitate**.

**A/B/C vertical:** A cerință CAT/range pozitivă; B fals „întotdeauna minim”; C poate fi adevărat ca alegere înainte de conectare la circuit, dar nu specifică un domeniu sigur.
**A↔B↔C orizontal:** A↔C **compatibile** ca cerințe independente (ce alegi vs când alegi), A↔B calibrare adecvată vs minim arbitrar, B↔C interval vs procedură; **nu** se exclud A/C doar prin eliminarea B.
**Reversie/contraexemplu:** Operatorul stabilește gama 600VAC pe multimetru CAT III 600V **înainte** de a conecta sondele la tabloul corespunzător; realizează simultan A și C. Fără referentul C, două variante pot fi valide.
**Sursă și limită:** Fluke Digital Multimeter Safety https://www.fluke.com/en/learn/blog/safety/multimeter-guide ; procedura Fluke selectează funcția **înainte de sonde** https://www.fluke.com/en/learn/blog/maintenance-monitoring/how-to-use-a-multimeter-guide .
**Verdict:** `CRITICAL_POTENTIAL_A_AND_C_TRUE; PROBE_WORDING_AMBIGUITY; USER_CONFIRM_ONLY_AFTER_SOURCE_REVIEW` + `INDEPENDENT_QA=NOT_RUN`, `LEARNING_APPROVAL=NO`.

## Regula transversală QA și poarta de escaladare
- **`ORTHOGONAL_TRUE_OPTIONS`**: două răspunsuri pot fi simultan corecte dacă unul spune **ce proprietate** trebuie să aibă o selecție, iar altul **când** trebuie făcută. În `G2-ELEC-063`, A și C pot fi simultan adevărate în procedura sigură. B se elimină, dar **eliminarea NU dovedește unicitatea A**.
- **`SOURCE_PROVENANCE_GATE`**: pentru itemi G2-ELEC cu enunț de sinteză generală, confirmați proveniența XLSX/ANRE înainte de aprobarea baremului. O sursă despre fizică nu dovedește automat că grila este oficială.
- Preflight structural: 4/4 QABC + 4/4 chei exact din MASTER; toate fișele au vertical, orizontal, reversie, sursă; aceasta nu este examinare expert independentă.
