# I7 2011 | Offline figure recovery from archival 2023 PDF | 2026-11-09

## Request / source provenance
User could not locate the 151 local JPG files referenced in their Firefox HTML save `REGLEMENTARI (A) 01_11_2011.htm`, and requested that missing figures be retrieved individually and added to the offline I7 reader.

### Inputs
- User-uploaded government-page HTML from prior turn: SHA256 `99389c372d898dea067b80a93e1998f93a1b03302812e478de327ff2013d90b7`.
- User Library PDF `803493174-I7-2011-completat2023.pdf`, locally materialized via Files: 249 pages, PDF production date 2023-09-22, SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`.
- Official direct URL `https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132` returned 502 on web fetch / could not be downloaded in container. **No assertion of current official JPG direct download.**
- ARYA mirror `https://www.arya.ro/legislatie/pdf.php?download=1&slug=normativ-i7-2011` indexed online as a PDF, but does not replace the official graphic source without an independent artifact check.

## Work done (conversation artifacts generated, not added to app)
- Parsed all 151 missing-image filenames, original HTML captions and surroundings. Compared with PDF's 399 embedded image occurrences / 356 distinct xrefs across 249 pages.
- Direct caption matching with page, proximity, x-position and description, including distinguishing same-number 6.18 variants and 4.1/4.2 two-column figure placement; duplicate 6.24 amended/facsimile image was deliberately not given an incorrect match.
- **82/151 images recovered from 2023 PDF** with xref,page,description/adjacency mapping; remaining **69/151 unmatched** explicitly preserved as original missing-image warnings. 82 images embedded as base64 in new standalone HTML; 184 original HTML tables unchanged; original searchable indexes of 2247 sections and 48 annexes retained.
- Actual generated conversation deliverables: `I7_2011_OFFLINE_figuri_RECUPERATE_PARȚIAL.html` (8.4 MB, SHA256 `fab93749516a9c2ebdb11bc926cb5be8bd00a270fd3dac074c0f1dc1a84d7d84`), `I7_2011_OFFLINE_figuri_recuperate_PARTIAL_QA.zip` (3.1 MB, SHA256 `92532c25b3c0683512ba175de32cddc79f29db9538eeed8d6689597ae13af6a8`) including image manifest, detailed 151-row CSV and README. Artifacts remain user conversation files, NOT a source import in GitHub.
- **Actual QA**: 82/82 embedded image streams parsed and verified by PIL; 82 base64 image elements, 69 explicit missing warnings, 184 preserved HTML tables. Offline headless Chromium loaded HTML via set_content (file:// restricted by environment), searched `5.2.12.3.10` successfully, sampled image decoding on multiple positions (15 images loaded lazily, 5 manually forced and passed), no external requests and no JS page errors. Sample screenshot of Figure 3.1 inspected visually. Independent technical comparison of *each* figure with 2026 official JPGs NOT_RUN, offline Android hardware testing NOT_RUN.

## Constraints and follow-up
- **These are 2023 archival images**, not exact original 2026 portal image binaries, and legal validity/currentness must be re-verified before promoting them as current. Missing 69 are not silently replaced with guesses. Images may have amendments/renumbering; compare official 2026 figures one by one once source retrieval is possible.
- Prefer actual official JPG asset retrieval and side-by-side visual QA; do not use search-result decorative images or redraw figures from memory. Mark each match with official source URL, current legal edition, image hash, and independent reviewer status before replacing application documentation.
- User can open delivered offline HTML already; the application `app/src/main/assets/anre_trainer.html`, question keys, ABC, HTML/APK releases and `main` remain **unchanged**. PR #7 remains Draft and must not be merged without approval.
