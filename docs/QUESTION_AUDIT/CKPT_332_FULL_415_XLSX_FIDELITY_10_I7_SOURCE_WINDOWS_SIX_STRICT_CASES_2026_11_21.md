# CKPT-332 | Original workbook reconciliation complete for all 415 published QABC; 10 exact 2023-I7 windows; six historic strict cases reopened | 2026-11-21

## Scope and proofs
- Repo `AcoBenny/ANRE_Trainer`, PR #7 **DRAFT**, unmerged. Parent branch HEAD `5798753ae4b1f28494ec27a076523b95b73b37e5`.
- Input three original XLSX workbooks **as uploaded by user**. Source byte hashes and row ranges were authenticated at upload in CKPT-331, V244 and their full row-extraction evidence. These file hashes **do not prove byte equality to live ANRE-hosted files**.
- Canonical GitHub source master: **V149** at Git blob `ee2ac5536c78eb06a0461243be34c117e257188f`, containing 568 QABC source definitions. V241 contains 568 unique QABC / 822 grade-route IDs; of those 415 published-sample QABC cover **669 grade routes**, and 153 supplemental exercise QABC cover **153 grade routes**. Synthetic exercises are NOT original ANRE exam questions.
- **NEW V246 full direct-source text fidelity**: compared all **415** published-sample QABC stem + original A/B/C against the exact uploaded source XLSX row (A:D), Unicode NFKC + whitespace-collapse + FNV1a32/DJB2 32-bit paired source fingerprint. **411/415 unchanged**; **4/415 material Trainer-original mutations**; **0 missing source rows**. This is a text-fidelity check, NOT a certification of correct answers.
- Confirmed original-vs-Trainer material text divergences, **exactly**: `QABC-0143`, `QABC-0236`, `QABC-0362`, `QABC-0386`. V246 preserves both original original-XLSX and altered Master/Trainer fields for each; all grade keys remain unmodified. Two grade routes can legitimately reuse one source row (EL row159).
- The 3 uploaded workbooks have **426 source question rows**; V241 maps **414 distinct uploaded workbook rows** across 415 published QABC. **12 source rows currently unmapped**, including nine diagram-dependent; see V245. No extra question or route auto-inserted.

## Reopened 2023 source for ten important Norme tehnice conflicts
- Original normative source is from **previously uploaded user PDF** `803493174-I7-2011-completat2023.pdf`, 249 pages, **edition explicitly as-of 2023-09-22**, SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`.
- V247 records **10** original-XLSX stem/A/B/C with imported keys, exact clause+page, **adjacent original before / decisive focus bold / after** and option-level scope comments: `QABC-0362, QABC-0386, QABC-0343, QABC-0356, QABC-0374, QABC-0375, QABC-0376, QABC-0403, QABC-0372, QABC-0380`.
- Focused source window recheck after publication **PASS 10/10**: each of the **30 distinct excerpts** was matched directly as a Unicode/whitespace-normalized substring of the original PDF's extracted page text. Each record preserves the exact PDF byte hash and leaves `approved_for_learning=false`.
- Especially:
  - `G1-NOR-048/QABC-0362`: original Excel A “numai direct” / B “numai iluminat” / C “din circuit de prize”; I7 2023 §5.4.13 **permits three supply routes**. **C is source-supported for the verbatim original**; imported A belongs only to altered Trainer A, not original A. Context page 70.
  - `G1-NOR-072/QABC-0386`: original B requires removing bar-connected conductor **without a tool**; I7 2023 §5.5.2.3 requires individual disconnection and secure disconnection **only by using a tool**. **C is source-supported for the original**; imported B belongs to edited Trainer option. Context page 72.
  - `G1-NOR-029/QABC-0343`: imported B 2.3m is general upper bound, while I7 §5.3.3.21 exception allows **up to 2.5m in dwellings** (**original C candidate**) at p65.
  - `G1-NOR-042/QABC-0356`: §5.2.4.6.1 says monophase **two conductors** N=phase regardless of cross-section (**original A**); imported B describes three conductors with different Cu/Al thresholds. p55.
  - `G1-NOR-060/QABC-0374`: §5.5.3.2 excludes metal water pipe **as the PE conductor** (original C), not the distinct question of bonding a metal pipe. p72.
  - `G1-NOR-061/QABC-0375`: §5.2.12.3.4 forbids joints **at building-element penetrations** (original B), unlike generic joints elsewhere. p61.
  - `G1-NOR-062/QABC-0376`: §5.4.25 **recommends** socket placement >1.5m in specified child rooms; exam uses stronger “trebuie”. B is source threshold candidate, NOT legally unconditional, and C >2m may also be sufficient. p71.
  - `G1-NOR-089/QABC-0403`: §5.1.4.3.3 explicitly allows same color on all phases with proper marking at both ends (original B). p47.
  - `G1-NOR-058/QABC-0372`: §3.0.3.5 **explicit exception for enclosed IP33-resistant equipment** means original B “total interzisă” ignores a permitted conditional case (C), p13.
  - `G1-NOR-066/QABC-0380`: §5.2.12.1.4 prohibits **individual conductors inside tubes/pipes buried in soil** (original A), not all suitably rated underground cables. p59.
- These ten candidate alternative letters are exact-version **technical-source research findings**, not officially authenticated grade-specific scoring keys and not signed independent expert QA.

## Remaining four of six historical strict cases
- V248 reviews `QABC-0017` (balanced delta-to-star `Cs=3C` conditional on exact service capacitance definition), `QABC-0094` (two-busbar preference depends on operation scheme, no universal rule established), `QABC-0143` (original “adimensională” vs physically `γ` inverse length), `QABC-0236` (original “inducţie electromagnetică” vs corrected electrostatic induction; neutral conductor may polarize without acquiring net charge).
- Original A/B/C options and imported keys are directly traceable to user-uploaded XLSX and V246; any provisional physics inference **does not authenticate an official answer key**.
- Thus all **6 historical strict QABC** have newly reopened uploaded-original source and focused technical/normative evidence across V247+V248, but **all 6 remain blocked/unapproved**.

## QA regression and explicit correction to the audit evidence
- Dedicated audit found a mistaken **`v246.mutations` key lookup** in initial V247/V248 generation: the records have field `.id`, **not `.unit_id`**. As a result initial new evidence reports had erroneously aliased Trainer-mutated wording into a field labeled “source original”.
- Both V247 and V248 were **explicitly amended in place with versioned correction**, committing authentic XLSX original wording to `source_original_stem_ABC` and keeping Trainer-mutated wording separately in `trainer_master_changed_stem_ABC`.
- **Subsequent regression PASS 4/4:** all four authentic original A/B/C sets exactly match V246's confirmed Excel-original sets; four Trainer-edited versions remain explicitly separate, not silently overwritten.
- Another minor source-window highlight QA correction removed the **following chapter heading** from NOR072's bold focus, leaving only §5.5.2.3 in bold. This is an editorial audit-doc fix, not a source change.
- Machine QA confirmed **10/10 exact source-before/focus/after windows**, **6/6 strict-case source-review coverage**, all source hashes consistent, **0 learner approvals**, and PR still Draft/unmerged.

## What is *not* complete
- No official **2026 effective I7 edition** was certified as identical to the user's 2023-09-22 PDF for all ten clauses. No claim that 2023 source applies unmodified to the upcoming exam without an edition/bibliography check.
- No officially authenticated ANRE **scored-answer key** has been received (the public example XLSX questions do not supply one), and no real independent qualified technical/legal+linguistic reviewer has approved each of 822 grade routes.
- V247 before/focus/after format has been populated **only for 10** source-evidenced cases so far, not 568 card drafts. Source-original fidelity alone does not establish the source of the correct **answer**.
- **136/136 known semantic holds remain held**, 432 QABC without known semantic holds remain subject to final source/answer review. **0/822 independently approved for learning**.
- The 12 source-only rows (9 diagram-dependent) are inventory findings, not authorization to change the 822 route target.

## Next execution gate, preserving GFR no-loop principle
1. Check **I7 exact current edition + 2026 exam bibliography** against the uploaded 2023 I7 for the ten cited clauses, and preserve version-delta findings; prioritize now source-backed candidate key conflicts rather than re-drafting cards.
2. Obtain and audit official scoring provenance/errata where available and create bounded independent technical+linguistic review packets from original question, all options, before/focus/after source, counterexamples, physical/legal scope and ambiguity status; never impersonate expert certification.
3. Continue on other top-risk legal/technical QABC and the 12 source-only rows while preserving grade keys and historical audit results.
4. Maintain UI requirement **before / exact decisive focus bold / after** with edition/paragraph/offline anchor, editorial A/B/C below source quote. Implementation deferred until content and release gates have actual approval.

**No question, original source workbook, imported key, HTML, APK, base branch, merge, release or app-learning approval changed.**
