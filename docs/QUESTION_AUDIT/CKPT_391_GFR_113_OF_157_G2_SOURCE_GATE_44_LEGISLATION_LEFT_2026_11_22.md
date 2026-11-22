# CKPT-391 | GFR G2 recovery source audit: 113/157 triaged, remaining 44 legislation

Date: 2026-11-22. Follows CKPT-390. Audit branch `audit/anre-v8-priority-17-20261109`. PR #7 remains Draft.

## What was actually completed
1. ALL 104 source-original G2 Norme candidate rows now have a first-pass technical explanation or explicit blocker, reconciled by V309 across V299/V302/V303/V304/V305/V306/V307/V308. There are 3 exact-source hard blocks: G2-NOR rows 35,179,180. Numerically or semantically conditional questions remain held, including rows 55,106,183; no final score approvals.
2. Four additional G2 Legislație original row variants were checked against **the official ANRE-published Monitorul Oficial nr 417/16.05.2023** PDF `https://anre.ro/wp-content/uploads/2023/05/Ord-66-2023.pdf`, printed page 10 (zero-index page 8), Article 37 and relevant Articles 8 and 35, read as actual PDF screenshots with adjacent text. V310 covers G2-LEG original workbook rows 61, 62, 63, 69 with original A/B/C preserved and individual alternative rationale.
3. Important **row 62 linguistic omission**: the raw source original B says electrician cannot perform any works/maneuvers in operator network. Article 37(j) forbids those operations **without a contract with the operator**; an unconditional prohibition is technically inaccurate. B remains HISTORICAL INTENT but is **not uniquely certified as a literal rule**. Preserve as a source-scope hold rather than silently rewriting original question or assigning a scored key.
4. V311 QA read back V298/V309/V310 and confirmed original 4 stems+12 option fields unchanged, IDs unique, no previously reviewed overlap, exactly 4 new cases, and the prior source-staged 157 are all still learner-blocked.

## Numerical state
| Area | Candidate rows in quarantine | First-pass triaged or explicitly blocked | Not yet first-pass reviewed |
|---|---:|---:|---:|
| G2 Norme | 104 | 104 | 0 |
| G2 Legislație | 53 | 9 | 44 |
| **Total** | **157** | **113** | **44** |

Related audit outputs: `V309_157_STAGE_109_REVIEWED_48_LEGISLATION_QUEUE_QA_2026_11_22.json`, `V310_G2_LEG_4_ORIGINAL_ART37_ABC_ONE_CONTRACT_SCOPE_TRAP_2026_11_22.json`, `V311_G2_113_OF_157_SOURCE_REVIEW_44_LEGISLATION_PENDING_QA_2026_11_22.json`.

## Evidence and release gates
- Normative original G2 sources from 2023 and original user I7 PDF consolidated 2023-09-22 are **not** a blanket claim of effective 2026 law or authoritative examination scoring. Source-specific law edition must be reopened for each legal candidate and the ANRE 65/2024 amendment tracked.
- No independent qualified electrical/legal and linguistic reviewer has issued sign-off. Source-based preferred answer is not an official key. **0/157 added candidates approved for learning**; previous 822 mapped grade routes still **0/822 independent qualified approvals**.
- Unchanged: canonical 568 QABC, 822 grade routes, 153 didactic training QABC (all imported A), native XLSX, stored answer keys, HTML, APK. **No merge/release**.
- User's approval to expand original G2 exam-source coverage is a direction and staging authorization; it is not permission to auto-score or activate unverified questions.

## Next productive GFR stage
1. Source-edition-sensitive A/B/C review of **44 remaining G2 original legislation variants**: Legea 123/2012 rights/concessions; electric connection ATR deadlines, performance standard, supplier disputes, tariffs, ANRE operator atestare. Prioritize exact object/action and current effective 2026 wording.
2. Reconcile grade-original same-stem A/B/C variant conflicts, especially G2 LEG row18/34/82/93, and hold older source text where legal regulations changed. Never copy a G1 answer letter to differently-worded original G2 option set.
3. Seek qualified independent technical and linguistic review plus authenticated exam-key/clear didactic labeling, complete QA before live app migration, obtain explicit final release approval.
