# I7 web image search and authenticity pilot | 2026-11-10

## Request and safety decision
User proposed searching Google Images for missing I7 formulas/figures and comparing them before offline inclusion. A search is a **candidate discovery method**, not evidence that a random visually similar diagram is an authentic I7 figure. Exclude unverified, altered, differently numbered, historically obsolete, or restricted third-party artwork.

## Sources investigated
- Portalul Legislativ consolidated I7 official URL: https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132 (direct web open **HTTP 502** in this session).
- Ordin 959/2023, official: https://legislatie.just.ro/Public/DetaliiDocument/271142 . Article I, point 43 **amended I7 6.3.2.4** (PDA protection-radius equations). **Old online formula images MUST NOT be silently substituted**, particularly original missing visual references #61/#62.
- Reproduction of 2011 Monitorul Oficial 802 bis, including original figures 4.9 and 6.17: https://www.drimand.ro/download/44%20NORMATIV%20I%207%20-%202011.pdf . Indexed document and captions accessible by web; PDF web screenshot returned cache miss and binary container download failed, so this is **historical caption/text corroboration**, not a claim that 2011 pixel rendering was QA compared.
- IEC symbol cross-check from equipment manufacturer: https://product-help.schneider-electric.com/PowerLogic-ION9000/en-us/content/00-common/iec-61010-1-symbols.htm ; IEC 60417-5172 identifies Class II double insulation (#14 symbol candidate), but manufacturer's graphic cannot automatically become **the specific I7 JPG** or a licensed local copy.
- User-supplied I7-2011 synthetic consolidated PDF, **2023-09-22** (249 pages): byte SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`. Original user portal HTML screenshot: `REGLEMENTARI (A) 01_11_2011.htm`.

## Three authenticated-to-archive source visuals added (offline standalone ONLY)
Previously 108/151 available, 43 missing. After candidate and source-structure verification:

| Image index | Original HTML filename | Source | Verification evidence | Disposition |
| --- | --- | --- | --- | --- |
| #26 | `287132_A9540_dBB-.jpg` | 2023 PDF page **44**, image xref **333**, first 284 pixels | Fig. **4.9** combined star+mesh configurations, two diagrams and title; original HTML has 2 consecutive image slots before caption; 2011 MO reproduced Fig. 4.9 text and title | archival facsimile, **not** original portal JPG |
| #27 | `287132_A9541_dBB-.jpg` | same 2023 PDF page 44, image xref 333, final 87 pixels | Fig. **4.9** original legend split from PDF object; preserves diagram/legend ordering | archival facsimile, **not** original portal JPG |
| #46 | `287132_A13206_dBB-.jpg` | 2023 PDF page **95**, xrefs **696 + 698** and adjacent original printed captions | Fig. **6.17** two types of roofs, explicit width `w`, legend aligns exactly with old printed MO 2011 text | archival facsimile, **not** original portal JPG |

The exported standalone HTML `I7_2011_OFFLINE_111_FIGURI_ARHIVA_VERIFICARE_WEB.html` (SHA256 `8494f1c3a039e2143aa2cdb0bcd65975360896864f0cd38ec0a05d9b4976ee7f`) has **111/151** archival images, **40** explicit missing placeholders, **184** preserved original HTML tables. The two PDF sections selected are archive-original, not Google-result images. All 3 added visual records carry source edition labels.

## QA performed and gaps
- Automated exact HTML transformation: **only the 3 targeted spans changed**; replacing the new img tags with their old spans restores exact input HTML bytes. 111 `<img>` tags / 40 `missing-figure` warnings / 184 tables, all 151 original image references accounted for in CSV v5.
- Image integrity: 3/3 PNG bytes decoded and Pillow verified; in **offline Chromium headless** `page.set_content`, 3 new data-URI images decoded after lazy-loading override with natural dimensions **594×284, 594×87, 1334×457**; no JS errors, no network requests. Direct `file://` navigation and real Android WebView **NOT RUN**.
- New ZIP `I7_WEB_PILOT_111_FIGURI_QA.zip` includes HTML, 151-row v5 CSV, separate web-candidate evidence ledger, SHA/provenance manifest, this QA pilot report, and 3 PDF facsimiles. ZIP integrity PASS. It was delivered as **conversation artifact**, not committed or integrated into the APK.
- This is **source matching/structural QA**, **NOT** independent engineering or linguistic signoff, legal 2026 edition verification or official live JPG parity. Do not claim all 111 are original JPGs from current portal.
- Third-party pictures found via image search may aid explanation but are legally distinct educational illustrations; keep them in a separate optional didactic layer, never replace an I7 figure under the same ID unless the full normative comparison and usage rights pass.
- No changes to original ANRE Trainer HTML, APK, answer keys, release branch, or historical PDFs; PR #7 remains Draft, not merged.

## Next batch
Prioritize remaining **40** by exact source and 2023 amendments. Flag #61/#62 PDE radius protection equation and any 6.3.2.4 diagram as `HISTORICAL_FORMULA_REJECTED_UNTIL_2023_PARITY`; compare other images with original 2023 PDF layout (figure label, xref, page and legend) before exploring indexed web pictures. Map relevance to actual ANRE question IDs (G1/G2) before investing in less relevant figures. Keep currentness and rights as independent gates.
