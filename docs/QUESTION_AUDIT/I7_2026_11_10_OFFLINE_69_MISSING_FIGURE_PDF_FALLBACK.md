# I7 offline | 69 missing figures, traceable local archive fallback | 2026-11-10

## Result
- Continued the previous I7 figure-recovery work. Government portal `https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132` still returns 502 from the available web fetch. Literal JPG image filenames were not found through public search. No unsupported claim that 69 exact source JPGs were downloaded.
- Confirmed the user's Library PDF `803493174-I7-2011-completat2023.pdf` (249 pages), SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`, remains available for personal offline reference. **This is a 2023 archival PDF, not a newly verified 2026 government source.**
- Built a portable ZIP, conversation deliverable `I7_2011_offline_cu_PDF_si_82_figuri.zip`, containing the prior offline searchable HTML reader with 82 embedded archival figures, the user's archival PDF, a manifest, QA README, and a 69-row unresolved figure index.
- Linked **all 69 still missing** images to locally bundled PDF for visual/context access. Where nearby recovered figures place it within an at-most-eight-page window, the link uses an *orientation-only* `#page=N` jump. Long ranges link to the whole PDF. These links are **NOT verified figure equivalences**; each missing source image stays visibly flagged. The 69 original JPGs have **not** been recovered.
- Original HTML's **184 tables** retained. All 69 PDF fallback links inserted, report CSV 69 entries, archive ZIP CRC validation passed. Standalone reader SHA256 `656aa135b35a30094566689d54ebe1041eb5be12711211b7f89a0892a98dd9f5`.
- Headless Chromium with Internet disabled + HTML set_content: 69 link elements, 69 missing warnings, 184 tables, zero JS page errors. Direct `file://` navigation blocked by administrator policy in test environment, so actual portable offline file-opening QA and PDF anchors are **NOT_RUN**. Real Android WebView and normative/image-by-image reviewer QA **NOT_RUN**.

## Source/currentness/copyright and safety
- Web research found contemporary third-party consolidated copies (e.g. ARYA and LexApp), but neither certifies byte-identical direct official JPEGs; no third-party picture substituted or redistributed as an official matching graphic.
- The user-supplied archive PDF is bundled only as a **conversation artifact for that user**, not committed to GitHub or public distribution. Publishing copyright-sensitive documents requires separate rights assessment.
- No app HTML, APK, question choices/keys, historical evidence, or main branch changes. PR #7 remains Draft, no merge.
- Next: recover exact 69 portal JPGs when the portal is reachable, or validate individual page crops and their figure identity against official source, one-by-one, before promoting as replacement figures. Confirm 2026 legal effective version and official change history separately.
