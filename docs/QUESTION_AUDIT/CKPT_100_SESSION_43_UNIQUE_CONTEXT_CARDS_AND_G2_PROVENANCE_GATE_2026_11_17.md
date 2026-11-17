# CKPT-100 | Reconciliere sesiune 17.11.2026 și poarta de proveniență ANRE Grad II

## Situația documentară, verificată prin GitHub
- Repozitoriu: AcoBenny/ANRE_Trainer; branch `audit/anre-v8-priority-17-20261109`; PR #7 OPEN/DRAFT, NOT_MERGED; HEAD înaintea acestei scrieri `9615db2633e1a3f73d95429a68d3675cd8b7db2d`.
- Cumulul real la CKPT-091 era **250/568 unități și 305/822 ID-uri** cu fișe contextuale, **0/822 approved for learning**.
- CKPT-092: G2-LEG-081–083; delta unic **+3 unități/+3 ID-uri**.
- CKPT-093: G2-LEG-100–106; delta unic **+7 unități/+7 ID-uri**.
- CKPT-094: G2-LEG-007–009,107–111; delta unic **+8 unități/+8 ID-uri**.
- CKPT-095: G2-LEG-112–119; delta unic **+8 unități/+8 ID-uri**.
- CKPT-096: G2-LEG-120–127; delta unic **+8 unități/+8 ID-uri**.
- CKPT-097: G2-LEG-128–135; delta unic **+8 unități/+8 ID-uri**.
- CKPT-098: G1-NOR-036; delta unic **+1 unități/+1 ID-uri**.
- CKPT-099: 62 G2-LEG provenance negative matching, 0 new cards; delta unic **+0 unități/+0 ID-uri**.
- Suma delta **+43 unități, +43 ID-uri** din loturile 092–098. Totalul contextual **293/568 unități, 348/822 ID-uri**. CKPT-099 și acest CKPT-100 **nu** adaugă ID-uri. **0/822 aprobate pentru învățare**.

## QA efectiv
- Am citit efectiv în GitHub cele **7 fișiere CKPT-092–098**, comparând fiecare heading de identitate QABC cu lista așteptată: 43/43 identități distincte și exact o fișă fiecare, fără numărări repetate. Pentru fiecare fișă: **3 variante A/B/C**, în total **129/129** transcrise. Fiecare fișă păstrează baremul original și oferă sursă/context, interpretări de variante, comparații și contraexemple. Acesta este QA structural, NU verdict de adevăr ori QA independent.
- GitHub Compare între CKPT-091 HEAD `a887e158dfafbd3a05f5fcdcb1d6041f51a1eddc` și HEAD `9615db2633e1a3f73d95429a68d3675cd8b7db2d`: **8 commituri**, **8 fișiere numai adăugate** sub `docs/QUESTION_AUDIT/`. Nu s-a editat niciun barem, enunț, master, HTML, APK, cod, main. PR #7 rămâne Draft/Unmerged.
- Negativ real: în QA inițial de readback, un script de verificare a numelor a omis zerourile din `G2-LEG-081–083` și a raportat eronat 3 headings lipsă. Reexecutat cu ID-uri canonice zero-padded, **43/43 valid**. Această eroare a existat doar în scriptul QA, nu în fișiere și nu a creat modificări.

## Constatare P0 de proveniență nouă (nu confundată cu P0 de conținut)
- **CKPT-099** dovedește pentru copia de lucru din Library a sursei `LEGISLATIE-GR.-2-05.2023.xlsx` că **0/62 de enunțuri G2-LEG** din registrul de audit coincid textual cu cele **104 enunțuri** din workbook. Copii în 3 fișiere cu hash identic: `725323d136481e7ad5643251e2b89a19bd57a471527cbeec847a5fe7f32f2662`.
- Patru controale pozitive pe întrebări G1-LEG găsite exact în același workbook confirmă funcționarea comparatorului. În audit CSV, `Excel_ANRE` era gol pentru toate cele 62, iar toate cele 62 bareme G2-LEG sunt A. Aceste observații fac plauzibilă originea **didactică/sintetică**. Însă hashul workbookului de pe serverul ANRE nu a putut fi recitit, iar absența din XLSX 05.2023 nu demonstrează absența din orice ediție.
- **Nu eliminați niciuna dintre cele 62** și nu rescrieți un barem până la dovedirea provenienței și aprobarea utilizatorului. Marcați numai în documentație `G2_LEG_OFFICIAL_XLSX_2023_STEM_MATCH=NO`, `EXAM_PROVENANCE_OPEN`, `DERIVED_PRACTICE_ITEM_POSSIBLE`, `NO_LEARNING_APPROVAL`.

## Prioritate de continuare
- Înaintea altor carduri repetitive construite din același tabel bibliografic, verificați **proveniența reală** a celorlalte categorii din 822 și identificați dacă întrebările de proveniență didactică pot rămâne într-o secțiune separată a trainerului, fără a fi prezentate ca originale ANRE.
- Mențineți cazurile originale P0/P1 cu barem conflictual în escaladare: G1-ELE053 vs user reported ANRE key C; NOR042/LEG028; LEG029/031; imagini originale lipsă; sursa/exam edition 2026; efectuarea QA independent tehnic/surse/lingvistic.
- Fără modificări QABC/barem/master/HTML/APK, merge/release. Nu solicitați confirmări între loturi; utilizatorul este implicat numai pentru ambiguitate de interpretare cu pasajele normative complete sau aprobarea unui pachet de corecții deja demonstrat.
