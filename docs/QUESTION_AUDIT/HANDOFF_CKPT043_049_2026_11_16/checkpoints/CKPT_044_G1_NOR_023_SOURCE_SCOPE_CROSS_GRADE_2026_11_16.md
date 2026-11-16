# CKPT-044 | G1-NOR-023: încălzire locală, PE102 vs I7, proveniență gr. I / II

**Data:** 16.11.2026. **Status:** checkpoint local, nu commit GitHub. Branch țintă `audit/anre-v8-priority-17-20261109`, PR #7 Draft. Continuă CKPT-043 local și CKPT-042 GitHub. Niciun barem, enunț, HTML, APK sau merge modificat.

## 1. Întrebarea canonică

**G1-NOR-023**, unitate `AU-dbc4b69b4a250d57`, barem **A** (nemodificat).

> În cazul în care temperatura minimă este sub valorile stabilite de norme, montarea aparatelor înglobate în echipamentul de joasă tensiune:
>
> A. se admite dacă se prevede o încălzire locală
>
> B. nu se admite
>
> C. se admite în cazul în care aparatele au ulei

## 2. Paragrafe exacte, domeniu și ediție

**PE102/1986 §2.12(a), tabelul 1 + Nota 1 și textul imediat ulterior**. Nota 1 precizează **minim +5°C în interiorul echipamentelor** pentru echipamente de măsurare, comandă, automatizare și similare înglobate în JT. Alineatul ulterior **admite instalarea aparatelor în stații cu temperaturi minime sub +5°C dacă încălzirea locală menține temperatura necesară, sau fabricantul o permite**. [Copie text PE102](https://electrician365.ro/wp-content/uploads/2019/04/Normativ-instalatii-electrice-ORDIN-PE-102-1986.pdf). Sursa a fost citită ca text; screenshot a eșuat Cache miss. Ediția republicată 1993 nu a fost verificată din original.

**I7/2011 §5.3.3.8** se referă **strict la tablouri de distribuție cu aparate de măsurare** în condiții de temperatură neadecvate. Încălzirea locală, ventilația sau climatizarea pot asigura condițiile de funcționare. **Nu** extinde automat regula la toate aparatele înglobate în orice echipament JT. [Copie de lucru I7 generată mai 2026](https://www.arya.ro/legislatie/pdf.php?slug=normativ-i7-2011); [Portal Legislativ oficial](https://legislatie.just.ro/Public/DetaliiDocument/286763). Text citit, dar pagina normativă exactă nu a putut fi verificată vizual; consolidarea oficială completă pentru 2026 rămâne neconfirmată.

**Bibliografie oficială ANRE 05.2023**, nr. 22: **PE102 este NU grad I / DA grad II**, verificat vizual în pagina 3 PDF. Nr. 14: **I7 este DA grad I / DA grad II**. [Bibliografia ANRE](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf). Pagina ANRE curentă încă afișează această tematică; nu este confirmare absolută că ediția aplicabilă în fiecare moment din 2026 nu are suplimente.

## 3. A/B/C și noua descoperire

- **A:** candidat istoric **puternic** din PE102 cu încălzire locală; I7 susține ideea **doar pentru obiectul său îngust**. Nu aprobăm A general fără verificarea sursei gradului I.
- **B:** interdicția absolută contrazice cazurile în care încălzirea locală permite funcționarea conform prevederilor și producătorului.
- **C:** existența uleiului nu este criteriul normativ de permisiune la temperaturi mici; nici nu trebuie mutată interdicția I7 pentru dielectrici combustibili la alte instalații din PE102.

**Proveniență istorică nou identificată:** enunțul apare în chestionare vechi de **grad II** (2016, 2017, 2020) cu sursă nominalizată **PE102 art.2.12**. Dar aceeași grilă apare și într-o colecție istorică etichetată **grad I, ianuarie 2021**. Sunt surse secundare, deci **nu concluzionăm că a fost transferată greșit în gradul I**. Formularea corectă a riscului: `CROSS_GRADE_LEGACY_SHARED_STEM; GRADE_SOURCE_SCOPE_MISMATCH`. [Grad II 2017](https://www.scribd.com/document/732483595/NORME-TEHNICE-2-2017) · [Grad I 2021](https://ro.scribd.com/document/727518663/NORME-TEHNICE-Gr-1-01-2021-NEREZOLVATE).

**Blocaj de proveniență:** linkurile ANRE la XLSX-urile **NORME TEHNICE Gr.1 / Gr.2 05.2023** există pe pagina oficială, dar browserul nu parsează acel tip de fișier, iar mediul de fișiere nu a putut descărca din exterior; **fișierele Excel oficiale NU au fost comparate**.

## QA local și pași

- 8/8 aserțiuni locale de structură, bibliografie consemnată și porți negative PASS. Nu reprezintă validare tehnică independentă ori acces nou la originalul întreg. Verdict de învățare **NO**.
- **Nu reclasifica** G1-NOR-023 automat, nu schimba baremul A și nu afirma proveniență oficială doar din arhive.
- Următorul control: XLSX ANRE original grad I/II 2023, comparație exactă enunț/ABC și originea referinței PE102; apoi QA independent.
- Păstrează instrucțiunea utilizatorului din CKPT-043: în fiecare dispută afișează întrebarea + paragraful exact + explicația A/B/C, iar feedbackul utilizatorului este **ipoteză de validat**, nu semnătură de expert.
