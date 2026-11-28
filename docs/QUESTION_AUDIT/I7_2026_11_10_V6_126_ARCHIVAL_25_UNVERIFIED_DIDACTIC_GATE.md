# I7 | Recovery V6 | 2026-11-10 | 126 archival facsimiles / 25 still missing original JPG

## Status and method
Follow-up user request: find the remaining missing I7 figures via internet image discovery, verify authenticity and alignment with didactic literature, and avoid routine interim updates.

**No all-found claim.** Current state:
- HTML originally referenced **151** missing external JPG files (original user save `REGLEMENTARI (A) 01_11_2011.htm`).
- Historical PDF I7 synthetic consolidation **2023-09-22**, source SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`, is NOT proof of current 2026 amendments.
- The standalone offline reader now embeds **126/151** matching *archival subject facsimiles*, up from 111.
- **15** further places are supplemented with expandable full archival PDF-page *context previews*, but retain their **missing figure warning** since the preview is not demonstrated to match original JPG boundaries/pixels.
- **10** original images lack defensible specific source matching and remain missing with no replacement.
- Thus **25/151 original JPG identities remain unverified**, including the 15 context-only cases. In particular, none of the 126 are claimed to be byte-identical to the official 2026 JPG.

## New 15 archival subject captures
Directly located in the uploaded 2023 PDF, with original section topic, page, crop coordinates and hash preserved in accompanying v6 manifest:
- #14/#15/#16: class-II and supplementary/reinforced insulation symbols (p.27).
- #19: class-I equipment symbol (p.32).
- #28: disconnecting/separation equipment mark (p.69).
- #30: conductor protective temperature coefficient `k` formula (p.73).
- #31: Figure 5.2 supplementary equipotential bonding (p.75).
- #55: Figure 6.24 down-conductor loop (p.103).
- #58: Figure 6.27 (a/b/c) earthing arrangement at foundation (p.106).
- #94: TT system residual-current protective relation (p.149).
- #105: Annex 5.5 reference installation methods (p.187).
- #114: Annex 5.7 conduit classification marking (p.194).
- #115: Annex 5.8 earthing terminal symbol (p.196).
- #144: Figure A6.8.2 coefficient kc in air termination network (p.230).
- #146: Table A6.9.4 exposure areas (p.232).

## 15 context-only previews, not recovered originals
The unmatched Annex 5.1/5.2 and Annex 5.6 image fragments **#97–103 and #106–113** have exact relevant **PDF pages 178–191**, but a full PDF page does not establish exact HTML JPG cropping/segment boundaries. Consequently the original missing warnings remain; supplemental previews are labeled `NOT_EXACT_JPG`.

## 10 unresolved: do NOT substitute similar web diagrams
Numbers **#61, #62, #63, #64, #65, #66, #67, #75, #85, #86**.
These include PDA radius and nomogram figures, where **official Ordin 959/2023 article I point 43 amended I7 6.3.2.4**. The new act's text and image placeholders are indexed on the official portal:
https://legislatie.just.ro/Public/DetaliiDocument/271142
The original official image URLs `/ImaginiDinActe/271142_A1547.jpg`, `/ImaginiDinActe/271142_A1553.jpg` were located, but **live binary retrieval FAILED** due environment/portal errors. Third-party manufacturer lightning formulas with different height/efficiency assumptions cannot be accepted as identical legal content.

## Independent didactic literature crosschecks (partial by subject, NOT 151/151)
1. Electrical Installation Guide (Schneider Electric), *General method for cable sizing* https://www.electrical-installation.org/enwiki/General_method_for_cable_sizing covers reference methods A1/A2/B1/B2/C/E/F/G (Annex 5.5, relevant #105). This supports methodology and naming, **not every numeric table cell**.
2. Same guide *TT system - Principle* https://www.electrical-installation.org/enwiki/TT_system_-_Principle states IΔn ≤ 50/RA; corroborates a restricted TT technical relationship (#94) but not historical I7 legal exceptions.
3. Same guide *Sizing of protective earthing conductor* https://www.electrical-installation.org/enwiki/Sizing_of_protective_earthing_conductor gives S_PE=sqrt(I²t)/k and factors; supports subject of #30, NOT an exact 2023 I7 k-formula image match.
4. Source law: https://legislatie.just.ro/Public/DetaliiDocument/271142 explicitly changes PDA formulas; until the authoritative 2023 figure can be inspected **do not import any unrelated Google picture** for #61-#67.

**These are *partial subject-level* academic/didactic confirmations, not independent engineering review of every figure.** The exact-current-legal JPG match, scholarly formula parity for all diagrams, and rights/license clearance are still open.

## Local QA actually executed
- Source builder: `build_i7_v6.py`; generated conversation artifacts, NOT committed into app.
- HTML standalone `I7_2011_OFFLINE_V6_126_FIGURI_2023_PLUS_15_CONTEXTE.html`, SHA256 `f584a4141ff0170487ce580a37662bad318ebcf9d12ec9f6a20e1a87d70a10d1`; 15,074,059 bytes.
- `I7_2011_151_FIGURI_QA_v6.csv`, SHA256 `909642447d3a9ff97d294f6700ead2f3f559a4ea5b5b92ec2a7f29eaed98556e`, 151-row audit.
- `I7_2011_V6_AUDIT_OFFLINE_PARTIAL.zip`, SHA256 `6711c89dbcb7ab8470c74392e96a13e903c71d26c6d92c59f265a4e1bd989c29`, reader+CSV+JSON.
- Structural QA PASS: unchanged 184 source HTML tables; 151 reference identities accounted for, 126 historical facsimile representations and 25 original missing warnings (15 supplemented by source page previews, 10 no previews); transformation reversal was byte-identical to prior 111-reader outside 30 target spans; ZIP integrity PASS.
- Chromium `set_content` with network forbidden: 141 data-image nodes (126 + 15 supplemental), 30/30 newly generated WebP samples decoded, article search `5.2.12.3.10` worked, 0 JavaScript errors, 0 network requests.
- **NOT RUN**: actual Android/WebView test, live official JPG pixel comparison, independent licensed electrician, per-figure didactic literature full technical signoff, latest 2026 legislation timeline assurance. The archive copy must not silently replace a more recent rule.

## Safeguards and checkpoint
PR #7 Draft only. No change to canonical question/answer keys, HTML APK, repository stable branch or releases. No app assets changed. No merge. The extracted user PDF and derived standalone HTML are not committed to public repository while legal redistribution/copyright parity unresolved.

## Resume condition
To *finish* this task genuinely: locate and independently verify every one of the 25 remaining official JPG images, including PDA nomograms as modified in 2023, against official act screenshots or exact official JPG bytes; cross-check each technical detail against source paragraphs and credible educational references; inspect equality of captions, diagram, equations, symbols and table numbers; write individual evidence + rights QA. Keep monitoring for accessible official files; notify user only on **all 151 fully validated**. Do not equate 126 archive facsimiles to exact official current figure identities.
