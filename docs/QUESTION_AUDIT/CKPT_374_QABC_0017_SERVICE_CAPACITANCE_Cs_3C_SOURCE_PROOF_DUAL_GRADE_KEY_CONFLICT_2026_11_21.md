# CKPT-374 | QABC-0017: capacitatea de serviciu Cs = 3C, demonstrată în literatura tehnică | 2026-11-21

## Identitatea originală și cheia importată

- ID: **QABC-0017**, înregistrare originală **ELECTROTEHNICA-09.2024-2.xlsx**, rând **25**.
- Trasee: **G1-ELE-018** și **G2-ELEC-170**, aceeași întrebare, aceeași ordine a variantelor A/B/C.
- Enunț original: „Capacitatea de serviciu Cs a unei linii electrice aeriene simetrice, având capacităţile C12=C23=C31 =C şi neglijînd influenţa pământului, este:”
- **A:** `Cs=3 C`
- **B:** `Cs=C/3`
- **C:** `Cs=C`
- Chei **importate, neverificate ca bareme oficiale**: **G1-ELE-018=A; G2-ELEC-170=C**.
- Statut cercetare: `SOURCE_FORMULA_DIRECTLY_MATCHES_ORIGINAL_UNDER_BALANCED_POSITIVE_SEQUENCE_MODEL`, variantă sursă **A**, încă neaprobată pentru învățare.

## Sursă inginerească identificată cu ecuația exactă

1. *Rețele electrice, note de curs*, material tehnic în limba română distribuit la:
   https://consultform.ro/anre/wp-content/uploads/2021/09/Retele-electrice-note-de-curs.pdf
   - Secțiunea „Exprimarea capacităților de serviciu ale unui conductor în funcție de capacitățile parțiale fază-pământ și fază-fază”, pagini tipărite/slide-uri **36–37** (în fișierul PDF două slide-uri pot ocupa aceeași pagină).
   - Precedent: transfigurarea triunghi-stea pentru cele trei capacități identice de fază-fază dă `C_stea=3*C_ff`.
   - Focalizat: pentru regim simetric de secvență pozitivă `C_s^+ = 3*C_ff + C_p`, ecuația **(2.24)**; `C_ff` între faze, `C_p` față de pământ.
   - Următor: în regim de secvență zero rămâne doar `C_s^0=C_p`. **Nu confundați secvența pozitivă și secvența zero**.
   - **Scope:** enunțul este trifazat simetric, cu `C12=C23=C31=C`, „neglijând influența pământului”, deci `C_p=0` și `C_s^+=3C`.
   - **Limitare vizuală:** pasajul și formula au fost recitite în indexul text al PDF; tentativa de screenshot web PDF paginile 18–19 a eșuat cu `Cache miss`, deci **nu se pretinde verificare vizuală a paginii**.
2. *Note de curs Transportul și Distribuția Energiei Electrice*, copie text accesibilă:
   https://pdfcoffee.com/note-de-curs-transportul-i-distribuia-energiei-electrice-pdf-free.html
   - Paginile tipărite cca. **10–12**: formula matematică `q1 = C12(v1-v2)+C13(v1-v3)+C10*v1` și, în regim simetric `v1+v2+v3=0`, `C_s^+=3*C12+C10`.
   - Aceeași concluzie; această copie nu este o ediție oficială ANRE.
3. Universitatea Iowa State, curs EE455, *Modeling Shunt Admittance of Overhead and Underground Lines*, Zhaoyu Wang, pe baza Kersting 4th ed.:
   https://wzy.ece.iastate.edu/Courses/EE455/06%20EE455%20Modeling%20Shunt%20Admittance.pdf
   - Cadru independent pentru matricea capacitivă a liniei, nu substitut de barem ANRE.
4. ANRE publică fișierul de exemple `ELECTROTEHNICA-09.2024` la:
   https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/
   - Exemplul sursă a fost identificat prin Excel-ul original al utilizatorului; **simpla publicare a unei întrebări nu autentifică răspunsul punctat la examen**.
5. Exemplu de discuție secundară fără valoare de barem: chestionarele publice reiau `Cs=3C`, `Cs=C/3`, `Cs=C`; unele opinii explicite indică A, dar se bazează în această cercetare pe **demonstrația de manual**, nu pe sondaje:
   https://chestionare-anre.ro/gradul-iii-ab-simulare-test/

## Demonstrație formală și test negativ

Pentru `V1+V2+V3=0` și `C12=C13=C`, fără capacitate față de pământ (`C10=0`):

```text
q1 = C(V1-V2) + C(V1-V3) + C10*V1
   = C(2*V1 - V2 - V3)
   = C(2*V1 + V1)
   = 3*C*V1

Cs = q1/V1 = 3*C
```

- **A**: `3C` **AFIRMATIV** din transformarea triunghi-stea / fază-neutru.
- **B**: `C/3` **CONTRADICTORIU** cu relația de transformare corectă pentru capacități egale (impedanțele în stea sunt `Z_delta/3`, deci capacitățile în stea se multiplică cu 3).
- **C**: `C` descrie o capacitate parțială între doi conductori, nu echivalentul fază-neutru din modelul simetric.
- **Negativ 1, influența pământului nu mai e neglijabilă:** `Cp>0` -> `Cs^+=3C+Cp`, deci niciun A/B/C nu mai corespunde general. Enunțul precizează expres că influența pământului se neglijează, deci cazul negativ NU justifică C în enunțul original.
- **Negativ 2, secvență zero:** `V1=V2=V3`; nu există tensiune între faze, `Cs^0=Cp`, deci `Cs=0` dacă pământul e neglijat. Dar acest regim NU este modelul de serviciu trifazat simetric de secvență pozitivă vizat de definiția tradițională; nu permite deducerea literei C.
- **Negativ 3, schimbarea obiectului:** dacă cineva numește prin C chiar „capacitatea de serviciu” în loc de `C12`, litera C devine tautologică; însă enunțul indică explicit `C12=C23=C31=C` ca *capacități inter-fază*, nu `Cs`.

## A-B, A-C, B-C: verificare bidirecțională

- A vs B: transformarea **capacitivă** triunghi-stea multiplică cu 3; împărțirea la 3 se referă la **impedanță**, nu capacitate.
- A vs C: `3C` este capacitatea de serviciu a fazei în regim echilibrat, `C` este un braț dintre faze; pentru `C>0` ele nu coincid.
- B vs C: ambele sunt diferite de `3C` pentru un condensator real cu `C>0`; B micșorează greșit.

## Decizie de audit și limite

- **Verdict științific provizoriu puternic: A**, în convenția de capacitate de serviciu a fazei în regim trifazat echilibrat; definiția a fost regăsită cu ecuația exactă și context înainte/după.
- **Ce se poate închide:** disputa *fizică* despre formula `Cs` pentru modelul din enunț. Nu mai este necesară opinia utilizatorului pentru algebra `3C`.
- **Ce NU este închis:** conflictul celor două chei importate, în special **G2-ELEC-170=C**, și autenticitatea baremelor din examenul 2026. Nu s-a identificat un barem oficial distinct pentru gradul II care să confirme C.
- **Nu declarăm learner approval** și nu modificăm răspunsuri/chei până la revizuire independentă calificată și aprobare.

## Restricții respectate

- `source_original_XLSX_edited=false`
- `canonical_question_or_option_text_edited=false`
- `imported_grade_keys_changed=false`
- `HTML_APK_edited=false`
- `PR7_draft_and_unmerged=true`
- `qualified_independent_technical_signoff=false`
- `official_ANRE_scored_answer_key_authenticated=false`
- `learner_approved=false`

Anterior: CKPT-371 / V285. Acest checkpoint este **append-only**.
