# CKPT-122 | BATCH8 scale probe and reusable Avengers routing lesson | 2026-11-17

## Evidence (actual GitHub actions, not synthetic model benchmark)
- Baseline PR #7 HEAD: `57d17bd853880d429d087155da0d1b7420eee999`, Draft, unmerged. Worklist: 431/568 preliminary units, 548/822 grade IDs.
- BATCH8-1 documentation: `CKPT_120_BATCH8_ELE096_098_112_115_116_117_119_120_2026_11_17.json`; 8 distinct QABC units / 16 grade IDs, canonical QABC hashes and keys checked; ledger re-read and written in one update (commit `984e3da6634a47abbe00feeb07b125e4fc70c7e9`).
- BATCH8-2 documentation: `CKPT_121_BATCH8_ELE061_121_123_127_132_133_135_136_2026_11_17.json`; **actual final content** contains ELE143 instead of ELE135. Preflight caught ELE135 already documented in CKPT108 (YES_PRELIMINARY). The initial draft commit and corrective revision both remain in history; duplicate was blocked before ledger credit. Final card commit `8f0a6e1e4b44e5a3ad9f3fc380a5539460eb037e`; reconciled ledger commit `1fb6b4a350bab144da83f6add52c71450f03a007`.
- Final readback: **447/568** unique QABC units preliminary documented, **580/822** grade IDs covered, **121 QABC units remaining**. **16/16 new cards uniquely mapped**, QABC/hash/key/member IDs unchanged, 0 learner approvals, all independent QA gates NOT_RUN in new cards.
- Two 8-unit documentary batches completed in this conversation without a runtime stall or lost committed data. A duplicated research candidate was caught and replaced. **No verified elapsed-time or token-per-unit measurements**, no evidence that larger batch sizes are safe.

## Adaptive-size rule
- Last proven safe scale in this session: 8 QABC units per atomic microbatch, at most two microbatches per request, separate documentation/readback and one worklist write each.
- Next experiment: **10 units in first batch only**, with immediate checkpoint and ledger readback; proceed to another 10 only if the first passes all canonical/scope gates and no tool stalls are observed. If HEAD drift, source scope blockers, readback failure or two repeated operation errors arise, fall back to 5 (or 1 high-risk item). Do not fabricate benchmarking evidence.
- Select only `contextual_card_present=NO` before work, not merely an absent recent CKPT number. Existing YES_PRELIMINARY cards may need independent QA; do not re-credit them.
- Never equate contextual research with validation of the official question provenance, exam bibliography, answer key, independent specialist review or learning approval.

No changes to canonical questions, keys, MASTER, HTML or APK; no merge or release.
