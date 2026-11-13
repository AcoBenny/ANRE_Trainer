# Pilot extern Perplexity | 20 întrebări P0 ANRE Trainer
Data: 2026-11-11, Europe/Bucharest. **ZERO aprobări automate pentru învățare.**

## Cerințe pentru executarea testului
1. Încarcă `INPUT_20_P0.csv` în Perplexity (sau copiază cele 20 întrebări fără modificări). Pentru acuratețe folosește **4 runde a câte 5 ID-uri**, păstrând același mod de căutare pentru toate (Standard/Pro/Research, specifică-l).
2. Pentru fiecare întrebare cercetează **surse PRIMARE verificabile**, cu **URL exact, versiune/ediție/data, paragraf/pagină**, obiect tehnic/juridic, condițiile de aplicabilitate, **gradul ANRE I sau II**; nu confunda I7 cu PE155, PE102 ori alte obiecte diferite. Nu considera simplul chestionar ANRE sau răspunsul unui forum drept dovadă normativă.
3. Justifică individual A/B/C, capcanele lingvistice, eventualele răspunsuri multiple, condițiile schemei și **motivul pentru care sursa susține sau nu fiecare opțiune**. Dacă figura nu există sau norma exactă nu e accesibilă, notează BLOCKED, nu alege o literă din ghicit.
4. Pune întâi dovezile și citările. Nu te baza pe cheie; această cheie este originală și **poate fi greșită**. Nu propune corectare fără identificarea normei exacte. Pentru legislație verifică explicit versiunea la 11 noiembrie 2026 și actele modificatoare, nu doar anul paginii.
5. Returnează tabel/JSON cu: `ID`, `key_original`, `candidate_key_NOT_APPROVED`, `A_proof`, `B_proof`, `C_proof`, `exact_source_url`, `source_locator`, `source_edition`, `grade_scope`, `source_opened`, `limitations`, `ambiguity`, `status`. Valori status: `POTENTIAL_SUPPORT`, `POTENTIAL_CONFLICT`, `BLOCKED_SOURCE`, `BLOCKED_FIGURE`, `BLOCKED_EDITION`, `BLOCKED_AMBIGUITY`. **NU folosi `VERIFIED`**, deoarece verificarea independentă este separată.
6. La final raportează `sources_new_to_project` doar pentru URL-uri realmente distincte de sursele existente, cu locator și motivul de utilitate; niciun rezumat fără URL.

## Setul fix de 4 runde
- **Runda 1:** G1-ELE-018, G1-ELE-028, G1-ELE-029, G1-ELE-088, G1-ELE-102
- **Runda 2:** G1-ELE-125, G1-ELE-137, G1-ELE-138, G2-ELEC-266, G2-ELEC-290
- **Runda 3:** G1-LEG-017, G1-LEG-019, G1-LEG-026, G1-LEG-032, G1-LEG-034
- **Runda 4:** G1-NOR-027, G1-NOR-029, G1-NOR-032, G1-NOR-089, G2-NOR-137

## Prompt gata de copiat
> Analizează DOAR următoarele ID-uri din fișierul anexat `INPUT_20_P0.csv`: [înlocuiește cu runda indicată mai sus]. Pentru fiecare, găsește surse primare aplicabile obiectului exact, gradului ANRE și ediției în vigoare la 11.11.2026, citează URL+articol/pagină, explică pe rând A, B și C, marchează divergențele și incertitudinile. Nu accepta cheia originală ca adevăr și nu modifica datele. Returnează rânduri structurate cu câmpurile și statusurile din cerințele de mai sus. Dacă sursele nu sunt accesibile, marchează BLOCKED și explică de ce.

## Criterii de comparație
Un link nou **nu este punct** dacă nu se poate redeschide, nu are locator sau nu reglementează exact obiectul/gradul/ediția. Rezultatele Perplexity se importă separat în `RESULTS_SCORECARD_TEMPLATE.csv` și primesc QA de sursă independent înainte să poată schimba vreo concluzie. Nu lansa în automatizare o cheie de API în GitHub. Niciun acces Perplexity direct nu s-a executat în acest chat.
