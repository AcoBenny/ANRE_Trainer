# ANRE Trainer V10.29 — evidence candidate cross-ID audit (8 November 2026)

## Scope and provenance

Audit input: user-provided standalone `ANRE_Trainer_FINAL_STANDALONE_822_V10_28_CANDIDATE_CONTEXT_AUDIT.html`, SHA-256 `aaad6d47bca77191ed2f0a6f19ffd9d9ab4a6bbdf7aa362e1419698dc2d4ac92`. This file is **not identical to the older Android asset committed on main**. Do not assume a modified APK exists.

Read-only deterministic comparison of actual `DATA` question, option A/B/C, source row, and source filename (normalizing `(1).xlsx` suffix) against all 76 `G2_ELEC_CANDIDATES` records. No external source documents were revalidated.

## Findings

- Total `DATA`: **822** questions (Grad I 414, Grad II 408), stable IDs unchanged.
- **76/76** candidate sources match **exactly** (text + 3 options + source row + source file alias) to *two other* actual question records: one Grade I and one Grade II. **0/76** exactly match their assigned candidate target question.
- These 76 links point to **48 distinct XLSX rows** (some reused).
- The selected `G2-ELEC-001` ... `G2-ELEC-076` records are conceptual practice questions, status `VERIFICAT CONCEPTUAL`, citing ANRE thematic bibliography 2023; they should **not** be presented as verbatim questions from the ANRE XLSX bank.
- `G2-ELEC-050` asks about protective earthing, while candidate row 81 is Corona / bundled conductors; the real question is `G1-ELE-074` and `G2-ELEC-219`.
- `G2-ELEC-007`: series vs candidate parallel. `G2-ELEC-020`: apparent power VA vs reactive power var. `G2-ELEC-076`: resistance Ω vs reactive power var despite the historical `HIGH_CANDIDATE` label.
- Some links remain **conceptually related** (e.g. inductance↔henry); relation is not proof of **exact source** or of a didactic paragraph.
- These were ***wrong cross-ID associations***, not 76 proven wrong technical answer keys. **0 answer changes**.

## Full crosswalk: wrong target ID → true IDs of the referenced XLSX question

| Candidate target (conceptual) | Actual Grade I source question | Actual Grade II source question | Source XLSX row |
|---|---|---|---:|
| G2-ELEC-001 | G1-ELE-069 | G2-ELEC-214 | 76 |
| G2-ELEC-002 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-003 | G1-ELE-257 | G2-ELEC-392 | 264 |
| G2-ELEC-004 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-005 | G1-ELE-121 | G2-ELEC-263 | 128 |
| G2-ELEC-006 | G1-ELE-121 | G2-ELEC-263 | 128 |
| G2-ELEC-007 | G1-ELE-196 | G2-ELEC-332 | 203 |
| G2-ELEC-008 | G1-ELE-196 | G2-ELEC-332 | 203 |
| G2-ELEC-009 | G1-ELE-123 | G2-ELEC-265 | 130 |
| G2-ELEC-010 | G1-ELE-243 | G2-ELEC-379 | 250 |
| G2-ELEC-011 | G1-ELE-082 | G2-ELEC-227 | 89 |
| G2-ELEC-012 | G1-ELE-185 | G2-ELEC-321 | 192 |
| G2-ELEC-013 | G1-ELE-047 | G2-ELEC-193 | 54 |
| G2-ELEC-014 | G1-ELE-130 | G2-ELEC-270 | 137 |
| G2-ELEC-015 | G1-ELE-123 | G2-ELEC-265 | 130 |
| G2-ELEC-016 | G1-ELE-123 | G2-ELEC-265 | 130 |
| G2-ELEC-017 | G1-ELE-148 | G2-ELEC-286 | 155 |
| G2-ELEC-018 | G1-ELE-203 | G2-ELEC-339 | 210 |
| G2-ELEC-019 | G1-ELE-203 | G2-ELEC-339 | 210 |
| G2-ELEC-020 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-021 | G1-ELE-178 | G2-ELEC-314 | 185 |
| G2-ELEC-022 | G1-ELE-222 | G2-ELEC-358 | 229 |
| G2-ELEC-023 | G1-ELE-202 | G2-ELEC-338 | 209 |
| G2-ELEC-024 | G1-ELE-214 | G2-ELEC-350 | 221 |
| G2-ELEC-025 | G1-ELE-183 | G2-ELEC-319 | 190 |
| G2-ELEC-026 | G1-ELE-106 | G2-ELEC-249 | 113 |
| G2-ELEC-027 | G1-ELE-215 | G2-ELEC-351 | 222 |
| G2-ELEC-028 | G1-ELE-086 | G2-ELEC-231 | 93 |
| G2-ELEC-029 | G1-ELE-207 | G2-ELEC-343 | 214 |
| G2-ELEC-030 | G1-ELE-240 | G2-ELEC-376 | 247 |
| G2-ELEC-031 | G1-ELE-178 | G2-ELEC-314 | 185 |
| G2-ELEC-032 | G1-ELE-062 | G2-ELEC-207 | 69 |
| G2-ELEC-033 | G1-ELE-262 | G2-ELEC-397 | 269 |
| G2-ELEC-034 | G1-ELE-204 | G2-ELEC-340 | 211 |
| G2-ELEC-035 | G1-ELE-262 | G2-ELEC-397 | 269 |
| G2-ELEC-036 | G1-ELE-031 | G2-ELEC-180 | 38 |
| G2-ELEC-037 | G1-ELE-142 | G2-ELEC-280 | 149 |
| G2-ELEC-038 | G1-ELE-149 | G2-ELEC-287 | 156 |
| G2-ELEC-039 | G1-ELE-082 | G2-ELEC-227 | 89 |
| G2-ELEC-040 | G1-ELE-258 | G2-ELEC-393 | 265 |
| G2-ELEC-041 | G1-ELE-178 | G2-ELEC-314 | 185 |
| G2-ELEC-042 | G1-ELE-087 | G2-ELEC-232 | 94 |
| G2-ELEC-043 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-044 | G1-ELE-212 | G2-ELEC-348 | 219 |
| G2-ELEC-045 | G1-ELE-212 | G2-ELEC-348 | 219 |
| G2-ELEC-046 | G1-ELE-123 | G2-ELEC-265 | 130 |
| G2-ELEC-047 | G1-ELE-179 | G2-ELEC-315 | 186 |
| G2-ELEC-048 | G1-ELE-248 | G2-ELEC-384 | 255 |
| G2-ELEC-049 | G1-ELE-210 | G2-ELEC-346 | 217 |
| G2-ELEC-050 | G1-ELE-074 | G2-ELEC-219 | 81 |
| G2-ELEC-051 | G1-ELE-179 | G2-ELEC-315 | 186 |
| G2-ELEC-052 | G1-ELE-200 | G2-ELEC-336 | 207 |
| G2-ELEC-053 | G1-ELE-272 | G2-ELEC-405 | 279 |
| G2-ELEC-054 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-055 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-056 | G1-ELE-128 | G2-ELEC-268 | 135 |
| G2-ELEC-057 | G1-ELE-055 | G2-ELEC-201 | 62 |
| G2-ELEC-058 | G1-ELE-164 | G2-ELEC-302 | 171 |
| G2-ELEC-059 | G1-ELE-156 | G2-ELEC-294 | 163 |
| G2-ELEC-060 | G1-ELE-186 | G2-ELEC-322 | 193 |
| G2-ELEC-061 | G1-ELE-248 | G2-ELEC-384 | 255 |
| G2-ELEC-062 | G1-ELE-087 | G2-ELEC-232 | 94 |
| G2-ELEC-063 | G1-ELE-235 | G2-ELEC-371 | 242 |
| G2-ELEC-064 | G1-ELE-116 | G2-ELEC-258 | 123 |
| G2-ELEC-065 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-066 | G1-ELE-263 | G2-ELEC-398 | 270 |
| G2-ELEC-067 | G1-ELE-245 | G2-ELEC-381 | 252 |
| G2-ELEC-068 | G1-ELE-123 | G2-ELEC-265 | 130 |
| G2-ELEC-069 | G1-ELE-123 | G2-ELEC-265 | 130 |
| G2-ELEC-070 | G1-ELE-213 | G2-ELEC-349 | 220 |
| G2-ELEC-071 | G1-ELE-128 | G2-ELEC-268 | 135 |
| G2-ELEC-072 | G1-ELE-141 | G2-ELEC-279 | 148 |
| G2-ELEC-073 | G1-ELE-130 | G2-ELEC-270 | 137 |
| G2-ELEC-074 | G1-ELE-106 | G2-ELEC-249 | 113 |
| G2-ELEC-075 | G1-ELE-243 | G2-ELEC-379 | 250 |
| G2-ELEC-076 | G1-ELE-263 | G2-ELEC-398 | 270 |

## Corrective action and release gate

1. **QUARANTINE** the inaccurate candidate-source display for all 76 conceptual practice records; keep the source candidate data available for audit, do not delete questions or alter correct answers.
2. Show an explicit `Documentație în curs de verificare` notice instead of a misleading candidate question, answer set or external Corona teaching context.
3. Retain the exact source provenance of original question-bank records at their real Grade I/II IDs. Bank-of-questions provenance is **not** independent didactic theory.
4. For actual pedagogical content, await audited manuals, exact chapter/page/paragraph, permitted offline embedding, and per-question semantic mapping.
5. Promote source claims only after independent content audit and UI acceptance. Prevent candidate high score from overriding question identity.

## QA evidence and limits

- Deterministic cross-ID audit: **PASS (76/76 exact cross-ID identifications)** against the specified V10.28 HTML; external source provenance **NOT_VERIFIED**.
- Mitigated V10.29 HTML **preview** generated separately, not yet committed as Android asset. DATA and G2_ELEC_CANDIDATES unchanged by patch.
- Static JavaScript `node --check`: PASS.
- Chromium in-memory HTML, 390×844 and 1280×800 viewports: 76/76 candidate evidence popups show quarantine notice and no unrelated quote; **PASS for this scoped check**. This does not confirm `file://` behavior or Android APK runtime.
- Independent specialist QA: **NOT_RUN**. APK rebuild and on-device offline test: **NOT_RUN**.
- Academy's reusable deterministic checker: `AcoBenny/Avengers-Asamble/scripts/anre_candidate_crosswalk.py`.

Reference: [ANRE Trainer defect #1](https://github.com/AcoBenny/ANRE_Trainer/issues/1).
