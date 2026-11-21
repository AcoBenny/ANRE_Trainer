# CKPT-343 | 9/9 figure-dependent source gaps: external candidate diagrams located, NOT authenticated | 2026-11-21

## Real research and negative evidence
- Original branch head before writing: `66c03cc329bdc4c2289c370643ce423e7a60e50b`, PR #7 Draft.
- Official ANRE source workbook https://anre.ro/wp-content/uploads/2024/11/ELECTROTEHNICA-09.2024-2.xlsx returns original textual rows but Firecrawl **image extraction returned no images**. Container HTTP download of official XLSX failed (DNS/network unavailable); therefore actual DrawingML contents were not inspected in this turn.
- Two earlier user-library ANRE Grade I consolidated XLSX versions were materialized into the container and programmatically inspected as ZIP/OOXML: **0 `xl/media/` files and 0 drawings** each. These workbooks cannot supply the nine missing official source diagrams.
- Third-party page accessible: [https://scientia.ro/tehnologie/96-internet/10558-test-oficial-anre-pentru-electricieni-275-de-intrebari-electrotehnica-masini-si-retele-electrice-cu-raspunsuri-si-explicatii.html](https://scientia.ro/tehnologie/96-internet/10558-test-oficial-anre-pentru-electricieni-275-de-intrebari-electrotehnica-masini-si-retele-electrice-cu-raspunsuri-si-explicatii.html); figure-candidate image links discovered for **all 9** source-only rows, each individual link separately returning **HTTP 200 `image/jpeg`** on external server.
- **No image byte/hash/visual side-by-side match against official ANRE Excel was performed**. These are CANDIDATES only, not the authentic missing official media or approved exam answers. We store external URLs without copying images into repo.

| Original ANRE Excel row | Third-party article question | Public image candidate | External-site answer assertion (NOT official) |
|---|---|---|---|
| EL15 | #8 | [Image i008](<https://scientia.ro/images/A0_2026/i008.jpg>) | B |
| EL30 | #23 | [Image i023](<https://scientia.ro/images/A0_2026/i023.jpg>) | A |
| EL31 | #24 | [Image i024](<https://scientia.ro/images/A0_2026/i024.jpg>) | A |
| EL32 | #25 | [Image i025](<https://scientia.ro/images/A0_2026/i025.jpg>) | C |
| EL43 | #36 | [Image i036](<https://scientia.ro/images/A0_2026/i036.jpg>) | B |
| EL44 | #37 | [Image i037](<https://scientia.ro/images/A0_2026/i037.jpg>) | A |
| EL117 | #110 | [Image i110](<https://scientia.ro/images/A0_2026/i110.jpg>) | C |
| EL176 | #169 | [Image i169](<https://scientia.ro/images/A0_2026/i169.jpg>) | C |
| EL181 | #174 | [Image i174](<https://scientia.ro/images/A0_2026/i174.jpg>) | A |

## Acceptance criteria to actually close image blockers
1. Obtain official ANRE XLSX original binary with its embedded media and drawing anchor map; inspect exact pixel content at source row, including all three graphical A/B/C choices, and hash bytes.
2. Compare each candidate side by side with the original. If not the same figure and answer ordering, mark `GRAPHIC_MISMATCH` even when text matches.
3. Obtain rights/permission for any in-app offline reuse of reproduced external drawings. Prefer the user-provided original/source-authenticated graphics when legally available.
4. Independently inspect each electrical diagram for component labels and connections; use the authentic image for A/B/C assessment, not the third-party answer assertions. Authenticate grade membership and 2026 source edition separately.

## Continuity and safety
- Structured candidate evidence: [V256_NINE_UNMAPPED_FIGURE_CANDIDATES_EXTERNAL_ARTICLE_LIVE_200_ZERO_OFFICIAL_IMAGE_APPROVAL_2026_11_21.json](./V256_NINE_UNMAPPED_FIGURE_CANDIDATES_EXTERNAL_ARTICLE_LIVE_200_ZERO_OFFICIAL_IMAGE_APPROVAL_2026_11_21.json).
- Result: 9/9 **candidate media pointers**, but **0/9 authenticated original images**, **0 new source-only questions integrated**, **0/822 independently approved**; 136 prior semantic holds and six strict historical conflicts unchanged.
- No original stem, answer key, HTML, APK, merge/release or main branch edited.
