# CKPT-045 | ANRE Trainer | NOR-023: confirmare contextuală de utilizator și verificare prin eliminare

**Data:** 2026-11-16. **Stare:** checkpoint LOCAL; pregătit pentru viitoare sincronizare în `AcoBenny/ANRE_Trainer`, ramura `audit/anre-v8-priority-17-20261109`, PR #7 Draft, **nu** este commit GitHub.

**Continuitate:** completează `CKPT_044_G1_NOR_023_SOURCE_SCOPE_CROSS_GRADE_2026_11_16.md`. Documentele anterioare și toate dovezile rămân nemodificate. Nu s-au modificat întrebările canonice, A/B/C, baremurile, HTML, APK, main/master sau release. Niciun lot nu este certificat pentru învățare.

## 1. Confirmarea utilizatorului pentru G1-NOR-023

**Enunț:** „În cazul în care temperatura minimă este sub valorile stabilite de norme, montarea aparatelor înglobate în echipamentul de joasă tensiune:”

- **A.** se admite dacă se prevede o încălzire locală
- **B.** nu se admite
- **C.** se admite în cazul în care aparatele au ulei

**Baremul original:** A, păstrat integral.

**Interpretare comunicată explicit de utilizator la 2026-11-16:** „A e cel corect”. Raționament: **B** nu poate fi regula aplicabilă deoarece normativul prevede cazul de **încălzire locală**, iar **C** invocă o nișă (uleiul) care nu apare drept condiție de admitere în pasajul relevant; **A** rămâne susținută de regula pozitivă. Acest aport este o **confirmare de interpretare contextuală și logică din partea utilizatorului**, nu semnătură de verificare tehnică independentă și nici aprobare automată pentru învățare.

**Paragrafe relevante, cu delimitare de obiect:**
- **PE102/1986 §2.12(a), tabelul 1, Nota 1 și textul imediat următor:** temperatură minimă și dispozitive de măsurare/comandă/automatizare în echipament JT; încălzire locală pentru anumite aparate din stații în condiții sub temperatura uzuală. [Copie PE102](https://electrician365.ro/wp-content/uploads/2019/04/Normativ-instalatii-electrice-ORDIN-PE-102-1986.pdf).
- **I7/2011 §5.3.3.8:** încălzire locală/ventilație/climatizare pentru tablouri cu aparate de măsurare; **domeniu mai îngust decât toate dispozitivele înglobate JT**. [Portal Legislativ](https://legislatie.just.ro/Public/DetaliiDocument/286763).
- **Bibliografie ANRE mai 2023:** I7 DA pentru grad I, PE102 NU pentru grad I, DA pentru grad II. [Bibliografie oficială](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf).

## 2. Regulă reutilizabilă: dublă verificare prin suport direct + eliminare (`DUAL_PROOF_ELIMINATION_V1`)

1. **Mai întâi identifică obiectul, regimul, gradul și alineatul exact** și găsește o dovadă pozitivă pentru varianta candidat. O variantă plauzibilă nu este automat corectă; confirmă sursa originală și ediția.
2. **Analizează separat fiecare distractor**: `CONTRAZIS_DE_SURSĂ` dacă norma afirmă opusul; `NESUSȚINUT_PENTRU_OBIECTUL_ÎNTREBĂRII` dacă invocă un criteriu inexistent în norma relevantă; `POSIBIL_ÎNTR-UN_ALT_DOMENIU` dacă devine adevărat în altă configurație. „Nu apare în paragraf” **nu dovedește singur** că o variantă este falsă în toate împrejurările.
3. **Combină raționamentul**: dacă A este susținută de prevederea aplicabilă, B este contrazisă, iar C nu satisface criteriul normativ, A primește `USER_INTERPRETATION_SUPPORTS_A` + `ELIMINATION_SUPPORTS_A`. Dacă **toate trei** sunt nesusținute sau **două sunt adevărate în același domeniu**, activează `NO_PROVEN_UNIQUE_ANSWER`, nu forța ultima variantă rămasă.

**Transfer:** folosește în toate cele 568 unități, inclusiv în cele 297 suspecte, după validarea fidelității sursei. Eliminarea este un **al doilea mecanism de QA**, complement la dovada directă, nu o scurtătură pentru a ocoli sursa, excepțiile, versiunea sau grila de grad.

## 3. Schimbare de protocol în interacțiunea cu utilizatorul

Când rămâne o ambiguitate, prezintă în aceeași cerere: **întrebarea originală + variantele A/B/C**, **paragraful exact din sursă și linkul**, o **explicație simplă în limbaj obișnuit**, **eliminarea alternativelor** și **disputa reală**, fără a cere utilizatorului să refacă verificări deja făcute. Păstrează contribuția utilizatorului ca **evidență de interpretare**, separată de `SOURCE_EDITION_VERIFIED`, `INDEPENDENT_TECHNICAL_QA`, `APPROVED_FOR_LEARNING`.

## 4. QA și porți rămase

- Baremul original **A** nu s-a schimbat.
- `USER_INTERPRETATION_CONFIRMED = A`, `USER_ELIMINATION_REASONING_RECORDED = YES`.
- `SOURCE_EDITION_2026_VERIFIED = NO`, `GRADE1_ORIGINAL_ANRE_XLSX_PROVENANCE_VERIFIED = NO`, `INDEPENDENT_QA_FINAL = NOT_RUN`, `APPROVED_FOR_LEARNING = NO`.
- Nu se schimbă numărătoarea din CKPT-042: **297/568 problematice, 271/568 amânate, 15/568 fișe contextuale înregistrate, 25/822 mapări ID, 0/822 aprobate**; documentul adaugă evidență de interpretare, nu validează o nouă întrebare.

**Next:** când GitHub este accesibil, adaugă un fișier de evidență pe ramura de audit, leagă-l la `G1-NOR-023` în registru fără să schimbi baremul, și păstrează PR #7 Draft. Continuă celelalte probleme P0/P1 fără a bloca auditul pe această întrebare.
