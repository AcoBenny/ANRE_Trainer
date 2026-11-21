# ANRE Trainer | V9: 50 întrebări G2 existente, audit semantic pe surse, doar pregătire pentru QA

**Data:** 2026-11-09. **Mandat:** continuare fără intervenții între loturi, fără modificarea baremelor sau aplicației. **Versiune sursă:** V10.29 standalone sha256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`.

## Inventar verificat

- **50/50 ID-uri reale**: G2-ELEC-051..076 (26 întrebări conceptuale create pentru trainer; nu verbatim din XLSX) + G2-ELEC-154..177 (24 întrebări ale băncii XLSX 09.2024).
- Chei originale: **A=32, B=9, C=9**. Variantele A/B/C, textul întrebării, ID-urile și cheile au rămas nemodificate.
- **26/26 fișe candidate de XLSX pentru conceptele 051..076 rămân în carantină** pe motiv de nepotrivire de ID (din cele 76 confirmate anterior). Acest defect de proveniență nu demonstrează 26 bareme greșite.
- **Vizual inspectate** paginile PDF locale PREG pp52,89,101,151; MAS pp25,92; STATII p459 și documentul istoric de întrebări 2023 pp9–10. Au fost inspectate textual și alte pagini (PREG, MAS, UTCN, I7, Schneider, STATII).
- **Nu a fost executat QA independent** sau testarea reală a fișelor din HTML/APK. Valoarea `Status=VERIFICAT TEHNIC` din HTML este istorică, nu verdict independent nou.

## Rezultatul examinării asistate a celor 50 de enunțuri

| Clasă | Număr | Semnificație |
|---|---:|---|
| `DIRECT` | 24 | O afirmație relevantă este regăsită în text didactic local sau extern; control MODEL, fără validare independentă. |
| `CONDITIONAL` | 13 | Sursa sprijină principiul numai cu ipoteze sau delimitări suplimentare. |
| `DERIVATION` | 5 | Formula/calculul au fost rederivate; pagina exactă de teoria completă/revizor încă de confirmat. |
| `GAPPED` | 5 | Nu am găsit o pagină suficient de exactă pentru afirmație; sunt doar capitole candidate. |
| `AMBIGUOUS` | 2 | Formulare cu multiple interpretări sau un termen tehnic neclar. |
| `MISSING_FIGURE` | 1 | Desen necesar pentru rezolvare absent din datele learner-facing. |

**IMPORTANT:** `DIRECT` nu înseamnă `APPROVED_EXACT_SOURCE`, iar `DERIVATION` nu înseamnă barem verificat. Toate **50** rămân `INDEPENDENT_QA=NOT_RUN`, cu **0** corecții de barem.

## Dovezi tehnice speciale și observații cu valoare de corecție

### 1. Scheme și text lipsă

- **G2-ELEC-177:** obiectul DATA din V10.29 are doar `Intrebare` cu sintagma „schema de mai sus”, opțiuni A/B/C și cheia B; **nu conține un câmp de imagine/schemă**. În PDF-ul istoric al utilizatorului `979902894-Captura-de-ecran-din-2024-11-09-la-14-15-06.pdf`, pagina fizică 10, există figura deasupra aceluiași text, verificată vizual. Nu este demonstrat dreptul de redistribuire a figurii; nu modificăm aplicația în acest PR. Blocajul este de *completitudine a întrebării*, nu probă de barem greșit.
- **G2-ELEC-166:** versiunea istorică (aceeași sursă, PDF pagina 9) folosește „câmpul de inducție magnetică”, în timp ce HTML spune „câmpul de inducție electromagnetică”. Pentru câmpul magnetic liniile sunt închise și `div B=0`; nu presupunem că formulările sunt sinonime într-un barem fără revizor.

### 2. Formule, ipoteze și avertisment despre erori ale surselor

- **G2-ELEC-170:** dacă `C12=C23=C31=C`, neglijăm pământul și folosim excitație trifazată echilibrată, avem `IA=jωC[(VA−VB)+(VA−VC)]`. Din `VA+VB+VC=0` rezultă `IA=jω(3C)VA`, deci `Cs=3C` pentru capacitatea echivalentă fază-neutru. Acesta este un raționament derivat, **nu un paragraf integral găsit în manuale**; trebuie verificată semnificația exactă a `Cs` în programa ANRE.
- **G2-ELEC-176:** `P=I²R=4×10=40W`, pentru 10 ore `E=400Wh`. Cheia B este numeric coerentă. Atentie: PDF PREG p52, inspectat vizual, scrie formula corectă `Q=I²Rt` dar descrie eronat `R` (Ω) drept *rezistivitate*; în definiție trebuie *rezistență*, iar `ρ` are unități `Ω·m`.
- **G2-ELEC-157 și 171:** capacități în paralel `100+50+100=250 μF` (cheia B), respectiv două capacități `C` în serie dau `C/2` (B). Surse didactice suplimentare: OpenStax, *University Physics Vol.2* §8.2; fără importarea textului în aplicație.
- **G2-ELEC-158:** `L−N+1` ochiuri independente doar dacă graful rețelei este *conex*. Pentru `k` componente conexe formula generală este `L−N+k`. Enunțul nu menționează explicit conexitatea.
- **G2-ELEC-172:** răspunsul A conține „eliminarea totală”; formularea necesită limitare la scurtcircuitele interne între faze din aceleași compartimente, nu orice defect între faze din instalație. Sursa istorică pagina 9 confirmă *ce a fost încercuit*, nu validează afirmația universală.
- **G2-ELEC-175:** cupla multifuncțională poate reduce investiția, dar crește unele vulnerabilități/limite de manevră. Text tehnic găsit în Annals of University of Petroșani 2025, articol p283, dar captura web a PDF-ului a eșuat; verdictul este **TEXT_INDEX_ONLY** și cere control independent.
- **G2-ELEC-063:** răspunsul A (domeniu/categorie CAT adecvate) este corect ca principiu; varianta C (selectarea înaintea conectării sondelor) poate fi și ea o recomandare practică pentru anumite aparate, fără a fi suficientă singură. Cerem manual de multimetru și adjudecare a ambiguității.

### 3. Surse cu suport local direct

- **G2-ELEC-056:** PREG p101, sarcină trifazată echilibrată în stea, curent în conductorul de nul nul; imaginea originală a fost inspectată.
- **G2-ELEC-070/071:** PREG p89, formula RLC serie arată explicit rezonanța `XL=XC` și `Z=R`, verificată în imagine.
- **G2-ELEC-057:** MAS p25, ecuația (1.31) a randamentului transformatorului `η=P2/(P2+pierderi)`, verificată vizual.
- **G2-ELEC-159:** STATII p459, AAR reduce întreruperile alimentării prin conectarea rezervei, inclusiv cazurile când AAR trebuie blocat; verificat vizual.
- **G2-ELEC-155:** STATII p283 §3.6.5 și ABB/MdPI descriu compensarea curentului capacitiv de defect prin bobina de stingere.
- **G2-ELEC-165:** Schneider p50-51 compară lichid izolant inflamabil și rășini uscate; cerințele de instalare depind de proiect/mediu.

## Probleme care nu trebuie ascunse

- **5 rânduri `GAPPED`:** 051, 052, 063, 162, 167. Acestea pot părea evidente, dar pagina citată nu dovedește exact propoziția, ori siguranța/cuantificarea necesită o sursă separată.
- **2 rânduri `AMBIGUOUS`:** 166 și 172. Plus 63, 158 și 175 cu ipoteze/alternative potențial problematice.
- **1 `MISSING_FIGURE`:** 177, nu se poate aproba pentru prezentare până la asocierea schemei verificată pe dispozitiv.
- O altă observație preventivă: **160** trebuie încadrată în regimul de *motor* `0<s<1`; în regim de generator alunecarea poate fi negativă.
- **168** folosește o sursă cu greșeala `R` vs `ρ`, deci nu copiem explicația mecanic.

## Proveniență și surse

- Bază audit: HTML original încărcat de utilizator, SHA256 explicit. 26 întrebări conceptuale: **TRAINER_AUTHORED**, nu întrebări verbatim oficiale ANRE; 24 source XLSX sunt în această aplicație cu rândul original păstrat, dar documentele istorice de teste nu sunt bareme oficiale certificate.
- PDF-uri locale consultate doar privat: `466657067-Pregătirea-Tehnică-Pentru-Autorizarea-Electricienilor.pdf`; `161996742-Masini-Electrice.pdf`; `337393907-Cartea-Electricianului-Din-Statii-Si-PT-uri12.pdf`; `811053817-Manualul-Instalatiilor-Electrice-Schneider-Electric-Complet.pdf`; `979902894-Captura-de-ecran-din-2024-11-09-la-14-15-06.pdf`. Nu sunt comise în GitHub.
- Extern: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel ; https://www.mdpi.com/2673-4826/4/2/7 ; https://www.engineeringdevotion.com/electric-power-systems/lecture/chapter-7-capacitance-of-transmission-lines.html ; https://www.upet.ro/annals/electrical/doc/2025/Annals%20Electric%202025%20v1.pdf (text-only, web screenshot cache miss); https://cms.eirgrid.ie/sites/default/files/publications/1-GIS-Functional-Specification.pdf (scope text only).
- `SUPPORTED_CLAUSE_VERIFIED` independent și sursele normative actuale nu au fost stabilite pentru toate; **independent specialist NOT_RUN**. Nicio transformare automată a `Status=VERIFICAT TEHNIC` din HTML în certificare externă.

## Rezultat și livrabile

- `G2_ELEC_NEXT_50_SEMANTIC_SOURCE_AUDIT_V9.csv`: 50 rânduri cu textul și toate variantele sursei, cheia originală, statutul preliminar, paragraful/pagina, riscul și pasul de revizie.
- `G2_ELEC_V9_PRIORITY_7_REVIEW_GATES.csv`: 7 cazuri pentru control tehnic/lingvistic independent cu acțiune exactă.
- `ALL_822_AUDIT_BACKLOG_V9.csv`: 17 din V8 + 50 din V9 = **67/822 examinate preliminar**; **755** de examinat; 0 cu QA independent.
- Niciun fișier HTML/APK modificat, niciun răspuns corectat. GitHub: development branch și draft PR, fără merge sau release.

## Următorul lot

Continuați cu **următoarele 50 ID-uri efectiv existente din banca G2**, pornind de la `G2-ELEC-178` și fără generarea de ID-uri inexistente. Prioritizați calculul, imagini referite, termeni absoluți și surse care sunt doar alte bănci de întrebări.
