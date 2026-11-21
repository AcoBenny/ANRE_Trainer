# I7 offline HTML import | 2026-11-09 | Read-only staging checkpoint

**Goal:** prepare an offline searchable legal reference from a government-page HTML snapshot supplied directly by the user. This records the extraction and QA only. It **does not** promote this snapshot to an officially certified 2026 version, replace app sources, change question keys, or change APK/HTML app source.

## Source
- User-supplied capture: `REGLEMENTARI (A) 01_11_2011.htm`, 5,504,033 bytes; SHA-256 `99389c372d898dea067b80a93e1998f93a1b03302812e478de327ff2013d90b7`.
- Header identifies `REGLEMENTARE TEHNICĂ din 1 noiembrie 2011`, I7-2011, published Monitorul Oficial 802 bis/14.11.2011; includes note regarding Ordin 959/18.05.2023, art. II transitional cases.
- Official reference https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132 . The upload is a local web-page save; **download/capture date and all potential later legal amendments not independently proven**.
- The original HTML has no network-dependent script or CSS. It references **151 JPG images** via sibling `REGLEMENTARI (A) 01_11_2011_files/` which were **NOT uploaded**. This prevents certification of complete visual/offline normative content; some figures, circuits and tables may require images.

## Actual conversion (executed in this session, generated local artifacts)
- Generated a standalone `I7_2011_cautare_offline.html` reader from the real uploaded HTML, retaining original textual HTML and **184 HTML tables**, without remote assets.
- Built JSON index: **2,247 point/article entries** and **48 annex entries**. Anchors match the actual HTML IDs (e.g. `#id_pctA2193`, `#id_pctA2352`, `#id_pctA5576`).
- Missing image links replaced with **151 visible warnings**, not recreated or misrepresented as source images.
- Created provenance/quality JSON manifest, original-SHA256, 151-image missing-assets CSV, priority question-to-paragraph evidence CSV, and reproducible Python builder; packaged everything in a ZIP for user delivery.
- **Static QA PASS:** each index anchor exists in reader; 184 tables retained; 151 warnings generated; no remote images/styles/scripts; title and article locators present; index JSON embedded.
- **Headless Chromium runtime QA PASS:** browser set to offline, loaded generated HTML content via `set_content` (local `file://` navigation blocked by testing environment policy); searched `5.2.12.3.10`, clicked match to `#id_pctA2193`, accent-insensitive search `inaltimea laturii`, validated 184 tables and 151 missing figure alerts; zero JavaScript page errors. No Android hardware/runtime APK test.
- All this is **structural and browser QA**. Independent electrical engineering, linguistic, normative and legal-currentness QA remain **NOT_RUN**.

## Evidence from supplied text for priority source review
- `G1-NOR-032` -> I7 `5.2.12.3.10`, `#id_pctA2193`: straight conduit runs max 25 m, up to 3 bends max 15 m, and following larger-conduit-diameter rule for longer routes. Existing MCQ needs careful context and key QA.
- `G1-NOR-029` -> I7 `5.3.3.21`, `#id_pctA2352`: general distribution-board top 2.3 m, but dwellings exception 2.5 m.
- `G1-NOR-010` -> I7 `8.1.1.3.3`, `#id_pctA5576`: insulation measured between active conductors and grounded PE, with table 8.1 present.
- `G1-NOR-012` -> I7 `5.1.7.2` (inspect sector-specific exceptions and wording). None of these is a final QA-approved key change.

## Next gate (not completed)
1. Obtain the missing `_files` folder (all 151 JPG assets, preferably ZIP) and confirm visual fidelity + offline navigation under real Android WebView and standalone HTML.
2. Verify the exact official edition and subsequent amendments current at implementation time against official legal sources, including scope and transitional provisions.
3. Compare approved snapshot vs historical PDF/manual revisions, perform technical and Romanian language QA, generate mapping `question ID -> official document hash -> paragraph anchor`.
4. After expert QA and explicit user approval: stage application integration in **a separate reviewable change**, never auto-merge PR #7 or alter answer keys.
