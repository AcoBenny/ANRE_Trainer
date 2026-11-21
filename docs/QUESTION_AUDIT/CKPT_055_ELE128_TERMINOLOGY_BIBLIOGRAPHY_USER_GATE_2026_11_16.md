# CKPT-055 | ELE-128: extindere terminologică și bibliografică, fără modificarea grilei | 2026-11-16

## Identitate, proveniență și limite
- Punct de pornire: CKPT-054, HEAD verificat live `46dd60de2cf6369e289929b200c711814d9e059d`, PR #7 OPEN/DRAFT, ramura `audit/anre-v8-priority-17-20261109`.
- Unitate deja documentată în CKPT-050 și reanalizată în CKPT-051: `ELE-128`, hash `AU-14fb0886051fa595`, ID-uri `G1-ELE-128` și `G2-ELEC-268`. **Nu este unitate nouă**: rămân 114/568 unități și 139/822 ID-uri documentate contextual, 0/822 aprobate pentru învățare.
- Enunț canonic: „Într-un circuit electric monofazat cu caracter inductiv tensiunea este defazata fata de curent:”
  - **A** „înainte cu 90 de grade” | **B** „cu zero grade (sunt în faza)” | **C** „cu 90 de grade în urma”.
  - Barem importat: **A**, intact. Nu există o cheie oficială ANRE verificată direct pentru această literă, chiar dacă fișierul de întrebări ELECTROTEHNICA-09.2024 este publicat de ANRE.

## Delta de surse față de CKPT-050/051: nu repetăm analiza, adăugăm context decisiv
1. **Marian Pearsică, Electrotehnică, Academia Forțelor Aeriene, Brașov 2004**, capitolul 9, §9.8.1, relațiile (9.95)–(9.102), p. tipărită ~155: https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf .
   - În același pasaj, `tg φ=(X_L-X_C)/R=X/R`, urmată de clasificarea explicită `φ>0 (X_L>X_C) → circuit cu caracter inductiv`; `φ<0 → capacitiv`; `φ=0 → pur rezistiv`. Relația (9.100) păstrează unghiul `arctg(X/R)`, nu îl fixează la 90°.
   - **Context anterior și următor:** textul derivă faza pentru circuit RLC serie, apoi clasifică regimul și calculează curentul și impedanța. Termenul «caracter inductiv» nu desemnează exclusiv o bobină ideală.
   - Sursa a fost accesibilă prin text PDF indexat; screenshot vizual web al paginii relevante a eșuat `CACHE_MISS`. Nu se revendică verificare vizuală.
2. **Culegere istorică neoficială, Electrotehnica, set publicat ca „Subiecte rezolvate ... 2010”**, https://tomaradu.yolasite.com/resources/30749113-Subiecte-rezolvate-examen-autorizare-ANRE-electricieni-2010-Electrotehnica.pdf .
   - Întrebarea **nr. 140** reproduce același enunț și aceleași trei alternative în aceeași ordine. Aceasta este probă de **persistență a formulării în timp**, NU dovadă că litera A este cheie oficială ANRE.
   - În același set, întrebarea **nr. 43** afirmă explicit: într-un RLC serie, curentul rămâne în urma tensiunii dacă reactanța netă `X>0`. Acesta este un indiciu intern că banca recunoaște «inductiv» pentru circuite mixte, nu doar pentru unghiul ideal de 90°.
   - Textul culegerii a fost indexat; captura vizuală a eșuat `CACHE_MISS`. Nu interpreta culoarea/tipografia ca barem.
3. **ANRE, tematică/bibliografie 05.2023**, https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf . În CKPT-053 a fost verificat că pentru Electrotehnică sunt permise manualele/cărțile de specialitate la gradele I/II, fără a impune acest manual 2004 drept text unic sau a atesta cheia de răspuns. Referința provine din CKPT-053 (nu se creditează o inspecție nouă).
4. **ANRE, lista publică de exemple, „ELECTROTEHNICA-09.2024”**, https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; sursa canonică deja inventariată în CKPT-053: https://anre.ro/wp-content/uploads/2024/11/ELECTROTEHNICA-09.2024-2.xlsx .

## Separarea v0.4.5: sens tehnic, scop, barem istoric și verificare de alternativă
- **Obiect:** circuit monofazat sinusoidal cu reactanță netă pozitivă; `X>0`, posibil `R>0`.
- **Definiție demonstrată în manual:** `φ=atan(X/R)>0`, dar nu este impus `φ=90°` dacă `R>0`.
- **Contraexemplu reproductibil:** `R=10 Ω, X=+10 Ω` → `φ=atan(1)=45°`. Circuitul are «caracter inductiv», însă **niciun răspuns nu dă exact 45°**.
- **A** este adevărată pentru **pur inductiv ideal** (`R=0, X>0`), dar nu pentru toate circuitele «cu caracter inductiv».
- **B** descrie `φ=0°`, deci o impedanță echivalent rezistivă, nu `X>0`.
- **C** descrie direcția capacitivă, nu caracterul inductiv.
- **Eliminarea** justifică A ca *răspuns probabil intenționat dintre opțiuni*, dar nu repară lipsa condiției «pur» și nu validează propoziția ca regulă generală.
- **Autoritatea:** întrebare publicată ≠ cheie oficială verificată; apariție în culegere istorică ≠ semnătură ANRE.
- **Temporalitate:** faptul că întrebarea apare în sursa istorică 2010 și în banca 2024 *nu dovedește* că sensul termenului s-a schimbat între epoci. Din manualul 2004 reiese deja sensul general al «caracterului inductiv».
- **Statut:** `HISTORICAL_KEY_A_PRESERVED`, `EXAM_INTENT_A_PROBABLE`, `TECHNICAL_NO_UNIVERSAL_EXACT_OPTION`, `TERMINOLOGY_QUALIFIER_MISSING`, `USER_INTERPRETATION_PENDING`, `NOT_APPROVED_FOR_LEARNING`.

## QA, risc și pasul următor
- Citire nouă focalizată: manual universitar, pasaj cu definiția și contextul adiacent; culegere istorică, întrebările nr. 43 și 140. Am reutilizat controalele matematice 17/17 din CKPT-051, fără să pretindem o rerulare nouă.
- QA independent de alt agent/specialist: `NOT_RUN`. QA vizual PDF pentru cele două PDF-uri de mai sus: `NOT_COMPLETED_CACHE_MISS`. Nu a fost modificat niciun fișier de întrebări, bareme, HTML, APK sau master CSV.
- **Escaladare justificată:** utilizatorul poate interpreta expresia «cu caracter inductiv» din perspectiva intenției grilei. Prezentați-i întrebarea integrală și A/B/C, definiția din manual cu vecinătățile și exemplul de 45°. Înregistrați exact raționamentul ca ipoteză, separat de validarea științifică.
- **După ELE-128**, se continuă cu `ELE-222`, fără a repeta fișele CKPT-050/051.
