# I7 | New upload duplicate check and two further archival formula recoveries (2026-11-10)

## Source duplicate gate (confirmed by bytes)
- New user attachment `803493174-I7-2011-completat2023(1).pdf`.
- Previously materialized user's Library file `803493174-I7-2011-completat2023.pdf`.
- Both files have **5,745,135 bytes** and the **identical SHA-256** `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`. Byte-for-byte comparison **PASS**.
- Both contain 249 pages and the 22 September 2023 synthetic consolidated version. **This is not a new legal edition or an independent new image source**; it cannot itself prove compliance or update correctness in November 2026.

## Reinspection of previously missing visual elements
Reinspected the same PDF against the original HTML list of 151 image URLs, especially missing images that were embedded as mathematics in the PDF, not presented as stand-alone JPGs.

- **#133**, missing HTML `287132_A24113__dBB-.jpg`: directly located the inline formula for the volume of combustible material in cables, **PDF page 211**. The text immediately before the original HTML placeholder is identical in topic; cropped the source formula at 3× rendering. Status: `RECOVERED_ARCHIVE_2023_PDF_FORMULA_FACSIMILE`, **not** original 2026 portal JPG.
- **#137**, missing HTML `287132_A24692__dBB-.jpg`: directly located **N_g ≈ 0.1 × T_d**, I7 appendix equation (A6.1.1), **PDF page 216**, and cropped the original source pixels. Same archival-only status.

No other unseen new page/artifact was found: it is the same file as before. The 43 remaining unmatched image references still need exact mapping and visual/content verification, not guesses.

## Standalone deliverables (conversation artifacts, not application files)
- `I7_2011_OFFLINE_108_FIGURI_ARHIVA_2023.html`, SHA256 `24c4fbd8ec0752c6ada74b3fd067cc4dff533c8159f469a6b87b03cb1c485468`; 12,230,064 bytes.
- `I7_2011_108_FIGURI_ARHIVA_2023_QA.zip`; includes standalone reader, 151-row CSV audit, JSON manifest and the two formula crops.
- `I7_2011_151_FIGURI_QA_v4.csv` and `I7_2011_IMPORT_DUPLICAT_QA_v4.json`.

## Tests executed
- Strict bytes and SHA-256 equality PASS between old and new PDFs.
- Exactly 151 original visual references accounted for: **108** archival PNG/figure facsimiles embedded in HTML, **43** visibly missing warnings.
- 184 original HTML tables retained. Both new PNGs verified by PIL decode and visually inspected.
- Chromium in **offline mode**, standalone HTML loaded through `page.set_content` (no direct `file://` navigation claim). Page DOM: **108 images, 43 missing warnings, 184 tables, 2 new formula elements**. Both images have `complete=true`, nonzero natural dimensions; **zero JS errors, zero network requests**. ZIP integrity PASS.
- **Not completed**: parity of archive facsimiles with official 2026 JPGs; official effective-date/legal changes; independent electrical/linguistic reviewer signoff; actual Android WebView/device test.

## GitHub guardrails
Only this QA/checkpoint document and `PROJECT_JOURNEY.md` are updated on PR #7 Draft. The large archived copyrighted PDF and derived standalone HTML were not committed; neither were keys, questions, app HTML, APK or main changed. No merge/release.
