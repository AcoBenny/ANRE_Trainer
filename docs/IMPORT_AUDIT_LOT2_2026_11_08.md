# ANRE Trainer | Lotul 2: audit de primire și suprapunere (2026-11-08)

**Stare:** `INVENTORY_DONE`, `STEM_OVERLAP_SCREENED`, `ANSWER_KEY_QA_PENDING`, `NO_IMPORT`. Nu este un checkpoint nou; ultimul checkpoint acceptat rămâne [CKPT-002](CHECKPOINTS/CKPT-ANRE-20261108-02.md).

## Intrări și probe executate

- Au fost primite **18 PDF-uri / 1.345 de pagini**. Lista completă de nume, SHA256, pagini și scoruri brute per fișier este în [manifestul Lot2](QUESTION_BANKS/HISTORICAL_LOT2_MANIFEST_2026-11-08.json). Documentele originale ale utilizatorului nu sunt încărcate în GitHub.
- Nu există două fișiere PDF cu SHA-256 identic în acest lot.
- A fost extras text din toate cele 1.345 de pagini și comparat cu `DATA` (822 intrări) din standalone V10.29, SHA256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`.
- **390/822 ID-uri** au enunțul complet regăsit textual (după normalizare) în cel puțin unul dintre documente, dar acestea reprezintă doar **228 de enunțuri distincte**. Un enunț poate exista sub două grade/ID-uri.
- Distribuția celor 390: `G1-ELE` 158, `G2-ELEC` 158, `G1-LEG` 45, `G1-NOR` 29; zero potriviri textuale exacte în `G2-LEG` din 62 (necesită evaluarea lacunei și a OCR/reformulărilor).
- Celelalte **432 ID-uri** fără potrivire textuală NU sunt declarate întrebări noi, corecte sau lipsă: un algoritm de text poate omite formulări echivalente sau pagini cu codificare stricată.
- Din **109 rânduri** cu enunț și opțiuni comparabile, într-un eșantion limitat la primele maximum 4 pagini din fiecare PDF: **69** au A/B/C identice textual și în aceeași ordine, **8** foarte apropiate, **32** au diferențe de opțiuni, ordine, adnotări sau calitate a extragerii. Nu s-a verificat cheia corectă pentru aceste 109 rânduri; 32 NU reprezintă 32 bareme greșite.
- Comparația TF-IDF a paginilor a identificat suprapuneri semnificative, fără a le declara documente identice:
  - `652919774` Grad II (160p) versus `652919777` Grad I/II (316p): **160/160 pagini** din documentul scurt au echivalent text foarte apropiat (cosinus ≥0,90).
  - `652919777` versus `127743254`: **221/316** pagini similare (cosinus ≥0,75).
  - `48560683` versus `87339166`: **14/15** pagini similare (≥0,75).
  - `622024653` versus `653594434`: **5/5** pagini similare (≥0,75).
- PDF `156130591-Subiecte-Anre-Grad-2.pdf` are codificarea textului sever defectuoasă; zero potriviri automate nu înseamnă lipsă de întrebări. Necesită inspecție vizuală selectivă.

## Relevanță și ordine de utilizare

1. **Prioritate Grad I/II, legislație:** `733260591` (Mai 2023 Grad II) și `668467690` (Grad II). Verificăm mai întâi dacă enunțurile și variantele sunt deja în banca curentă, apoi regulile/anul legal. Nu preluăm direct cheile istorice.
2. **Prioritate electrotehnică/norme:** `22553242` (toate gradele), `70074719` (electrotehnică), `147610015` (norme) și `156349771` (norme Grade II/III/IV).
3. **Secundar și arhivă:** restul de colecții cumulative/repetate, Grade III–IV și examene indicate 2010/2012/2016; le păstrăm cu metadate de origine, fără includere automată în Grade I/II.
4. **AGENT-031 lingvistic:** detectează negații, exclusivități, comparații, cuantificatori și diferențele subtile dintre variante; `TRAP_CANDIDATE` nu echivalează cu intenție dovedită sau barem valid.
5. **Versiuni legislative:** este necesară verificarea față de [bibliografia și exemplele publicate de ANRE](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) și legislația oficială, nu doar după numele PDF-ului sau anul din titlu.

## Clasificarea dovezilor

- `PDF_INVENTORY`: PASS, 18/18.
- `FILE_SHA256`: PASS, 18/18, fără duplicate byte-level.
- `NORMALIZED_STEM_MATCH`: EXECUTAT, **390 ID-uri** cu potriviri textuale; nu verifică A/B/C sau cheile.
- `PAGE_SIMILARITY`: EXECUTAT, semnal de suprapunere, nu certificare de duplicat.
- `A_B_C_SPOTCHECK`: SAMPLE_ONLY 109 rânduri.
- `FULL_QUESTION_EXTRACTION`: NOT_DONE.
- `HISTORICAL_ANSWER_KEYS`: NOT_VERIFIED.
- `CURRENT_LEGAL_REFERENCES`: NOT_VERIFIED pentru fiecare întrebare.
- `INDEPENDENT_AGENT_QA`: NOT_RUN.
- `NEW_APP_BUILD`: NOT_RUN.
- `ADDITIONAL_API_SPEND`: 0 lei.

**Regulă obligatorie:** nu se modifică cele 822 de întrebări, răspunsurile ori etichetele `SOURCE_VERIFIED` pe baza unei asemănări textuale. Duplicatele se consolidează logic păstrând toate metadatele istorice; conflictele se rezolvă numai cu documentație și audit.

## Continuarea fără checkpoint excesiv

Creăm un set structurat pentru întrebările noi din Grad II legislație, cu per-sursă PDF + pagina + variante A/B/C + dovezi de barem (dacă sunt efectiv vizibile), apoi generăm un registru `EXACT_DUPLICATE / REPHRASED / KEY_OR_VARIANT_CONFLICT / NEW_CANDIDATE / OUT_OF_SCOPE / LEGAL_OUTDATED_PENDING`. Abia după 2–3 loturi validate sau un handoff se va emite CKPT-003. Până atunci, acest fișier și manifestul reprezintă jurnalul de lucru.
