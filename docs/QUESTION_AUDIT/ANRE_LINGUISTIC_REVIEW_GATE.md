# ANRE Trainer | Gate obligatoriu pentru auditul lingvistic

**Data adoptarii:** 2026-11-09. **Scop:** toate loturile prezente si viitoare, fara schimbarea baremelor prin acest protocol. Acesta este un document de proces, nu dovada rularii unor agenti independenti.

## Rol explicit in Avengers Asamble
- **Romanian Language Reviewer**, definit deja in catalogul `avengers-asamble/agent-router/references/ROLE_CATALOG.md`; skill `anre-question-bank-qa`. Responsabil: capcane in limba romana, cuantificatori, negatii, conditii, formularea variantei A/B/C, ambiguitati si diacritice.
- **Electrical Engineer / Normative Sources Auditor**: adjudeca daca interpretarea lingvistica este compatibila cu sursa exacta, versiunea si domeniul de aplicare.
- **Data QA**: comparatie ID, text, ABC, barem si provenienta din sursa canonica; teste deterministe si verificare a dovezilor.
- **Independent QA**: un reviewer/executant DISTINCT, daca instrumentele disponibile il permit. Daca nu este rulat separat, `INDEPENDENT_QA=NOT_RUN` si nu se afirma aprobare independenta.

## Gate pe fiecare intrebare
1. Fixeaza textul canonic si toate variantele, cheia si versiunea, fara reformulare sau corectii silentioase.
2. Verifica expresii decisive: `nu`, `exceptie`, `doar/numai`, `orice/toate/intotdeauna/niciodata`, `poate/trebuie`, `in cazul in care`, `chiar daca`, termeni tehnici, valori si unitati, domeniu/epoca/regim si conditiile explicite ori implicite.
3. Pentru fiecare optiune: exprima conditia in propozitie logica, cauta contraexemple, verifica sursa exacta (act normativ versiune/data/articol sau sursa didactica editie/pagina), respinge simpla coincidenta cu alte grile ca justificare.
4. Etichete DISTINCTE:
   - `VALID_TRAP`: exista o singura optiune sustinuta in conditiile explicite, cu text normativ/tehnic precis;
   - `AMBIGUOUS`: enunt insuficient, mai multe variante plauzibile ori neclaritate de referent;
   - `KEY_CONFLICT`: cheia canonica si dovada ori baza istorica difera; necesita reconciliere;
   - `SOURCE_GAP`: nu exista inca dovada exacta pentru a decide;
   - `NO_TRAP_DETECTED`: nu a fost gasita capcana, nu inseamna barem certificat.
5. Inregistreaza `trap_trigger`, `option_by_option_reasoning_summary`, `source_uri`, `edition`, `article_or_page`, `linguistic_status`, `technical_status`, `independent_QA`, `key_change_authorized=NO`. Un test automat poate detecta markeri, dar nu poate autoriza cheia.
6. Blocheaza aprobarea automata atunci cand textul contine termeni absoluti/conditii cu efect juridic, formule dependente de ipoteze, lipsa unei scheme sau contradictii intre surse. Se pastreaza toate dovezile in CSV/MD si se documenteaza QA in `PROJECT_JOURNEY.md`.

## Debt / revizie retrospectiva
- V8–V12: screeningul lingvistic este incomplet sau model-assisted; **nu** se eticheteaza retroactiv drept audit independent. Recontrol prioritizat al celor cu `AMBIGUITY`, `CONDITIONAL`, `KEY_CONFLICT` si formulare absolutizanta.
- V14 a folosit checklist-ul specialistului, dar nu a executat un reviewer separat. Nu sunt aprobari independente pe cele sase cazuri.
- G1-LEG-024/028/032/034/048 si G2-ELEC-170 raman in carantina; niciun barem nu se modifica fara aprobarea explicita a utilizatorului si QA pe surse.
- Restul loturilor urmeaza aceeasi regula. Daca lipseste instrumentul de executie separat pentru agent, rolul este inclus in workflow **fara** a pretinde executie multi-agent.

## Guardrails GitHub
Doar documentatie, teste si propuneri pe branch de dezvoltare + PR Draft; nu modifica bareme/HTML/APK si nu executa merge, release sau deploy fara aprobarea utilizatorului.
