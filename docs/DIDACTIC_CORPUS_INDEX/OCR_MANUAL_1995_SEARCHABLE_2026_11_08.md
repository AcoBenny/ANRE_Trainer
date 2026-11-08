# ANRE Trainer | OCR pentru manualul scanat din 1995 (2026-11-08)

**Operațiune:** conversia personală a PDF-ului scanat în PDF căutabil, fără schimbarea imaginilor originale și fără a modifica ANRE Trainer. OCR executat local cu motorul open-source Tesseract (`ron+eng`), strat de text invizibil Unicode.

## Proveniență
- Original încărcat de utilizator: `695172381-Manual-Pentru-Autorizarea-Electricienilor-Instalatori.pdf` (332 pagini), SHA-256 `b85057732a71d96d4d217a42f5e2c1e9996f24e0011c5de374e7c878341b110a`.
- Fișier local OCR: `ANRE_Manual_Electricieni_1995_332pag_OCR_RO_CAUTABIL.pdf`, 18,000,976 octeți, SHA-256 `1ceac1f2eec5469afdbb561f74060b985146987d9b062f3eb93d98788723702a`.
- Toate **332/332** paginile păstrate. **324/332** au text OCR semnificativ, **8 pagini** (2, 10, 16, 20, 30, 34, 162, 188) par albe / aproape albe la inspecția vizuală.
- Aproximativ **555.988 caractere** OCR extractibile; diacriticele românești sunt păstrate folosind un font Unicode (exemple: 709 „ș”, 1.576 „ț”, 9.571 „ă”).
- Verificare fidelitate vizuală: **8/8 pagini eșantionate (1, 7, 31, 81, 146, 201, 275, 332) cu pixeli identici** față de scanul original la rasterizare, deoarece s-a adăugat numai text invizibil.

## Limitări
- OCR poate interpreta greșit formule, indici, tabele, simboluri electrice, numerotări și diacritice; **nu este validare tehnică ori juridică**.
- Documentul este istoric (1995), nu reprezintă prin el însuși o versiune normativă actuală.
- Originalul și PDF-ul OCR rămân în fișierele conversației utilizatorului; **nu încărcăm manualul protejat de drepturi de autor în GitHub** și nu îl includem încă în APK.
- Scanul redundant de 149 de pagini și cursul scanat redundant de 258 pagini nu au fost OCR-izate separat, deoarece au echivalente deja disponibile; acestea rămân în inventarul inițial.

**Stare:** `OCR_SEARCHABLE_CONVERSION_PASS`, `FORMULAS_AND_DIAGRAMS_QA_PENDING`, `RIGHTS_UNVERIFIED`, `APP_IMPLEMENTATION_FROZEN`. Ultimul checkpoint rămâne CKPT-002. Cost API: 0 RON.
