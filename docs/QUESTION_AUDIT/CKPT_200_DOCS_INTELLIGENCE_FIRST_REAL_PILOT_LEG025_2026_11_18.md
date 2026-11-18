# CKPT-200 | First real docs-intelligence workflow pilot: G1-LEG-025 | 2026-11-18

## Scope
This is a documented **in-session test of the Docs Intelligence skill-guided retrieval workflow**, NOT a separate independent agent invocation, model-quality benchmark, reviewer attestation, or learner approval.

- User objective: observe new Avengers Precision Lab v0.1 skills operating under Avengers Asamble v0.4.7.
- User format invariant: original question + ABC unchanged, then uninterrupted ORIGINAL statutory text with one paragraph before/after target, analysis only below the document; no summaries masquerading as source quotations.
- Source: Legea nr. 123/2012, Titlul I, Capitolul I, art. 1, alin. (1), (1^1), (2)(a), (2)(b), neighboring art. 2.
- Official source inspected in this session: https://legislatie.just.ro/Public/DetaliiDocument/300063 . The Portal Legislativ's consolidated-form index displayed 26.07.2026, 27.02.2026 and earlier dates, but direct retrieval of the 26.07.2026 historic form (document 311821) returned HTTP 502. **The latest dated version was NOT individually reopened and visually compared.** Do not claim current edition is certified.
- Direct source excerpt verified: art.1(2) excludes specified sources from *Titlul I*, and art.1(2)(b) names stationary DC energy sources not connected by inverters to SEN. Question says the *entire law*; source states *this title*; semantic caveat retained.
- Original question and imported key validated against existing CKPT-197; G1-LEG-025, unit AU-950954e2d16b0eb9, QABC sha256 950954e2d16b0eb9edac4c4c6ccb01ee7f6feb226546b082fd9037b0b6eb3a3a; imported B UNCHANGED.

## Actual gates, explicit
| Check | Status | Evidence |
| --- | --- | --- |
| Docs Intelligence skill read and applied | PASS_RETRIEVAL_WORKFLOW | Installed skill read and official source reopened through web |
| Original QABC/order preserved | PASS | CKPT-197 readback |
| Statutory object and title-scoping | PASS_SCOPE_RESEARCH | Art.1(2)(b), linked official source |
| Original exact paragraph + preceding + following freely reproduced in chat | NOT_MET | External source quotation cap; only a short verbatim excerpt may be copied. User-supplied full law document not available in current task. |
| 2026 consolidated version independently reopened | NOT_MET | Official 26.07.2026 form direct URL returned 502 |
| Independent source/language reviewer | NOT_RUN | No independent agent execution |
| Official ANRE answer-key match | NOT_VERIFIED | Imported B cannot be promoted by retrieval alone |
| Academy actual host skill routing test | GUIDED_SKILL_USED_ONLY | This shows the host followed the installed workflow, not hidden model execution |
| App files or imported answer changed | NO | Documentation-only checkpoint |

## Follow-on decision
The new Academy v0.4.7 routing is available, but **user's full verbatim statutory context requirement remains unmet in chat** for this web-only original source. Do not score the test as fully successful. If the official full text is user-supplied/loaded from a locally usable source in future, return the entire contiguous passage with no interleaved commentary. If external quote rights prevent full literal reproduction, show a permitted short original quote plus a direct official URL and explicitly disclose the gap.

TinyFish is NOT part of this trial. No barem, question, HTML, APK, main or PR merge changes.
