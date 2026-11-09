# V13 data integrity QA | 822 canonicals vs V9 tracker, 2026-11-09

Canonical `const DATA` GitHub blob `bc5b5a61954ba138cf83987bfc932eca517f3b21` versus `V9_ALL_822_AUDIT_BACKLOG.csv` from PR #7; unique IDs 822; 6 answer key differences, **no** source name or source-row discrepancies among these 6. Key changes NOT AUTHORIZED. This is a repository metadata conflict, not independently proven error in either answer.

| ID | Canonical V10.29 | Tracker V9 | Source row |
|---|---|---|---|
| `G1-LEG-024` | A | C | 31 |
| `G1-LEG-028` | B | C | 35 |
| `G1-LEG-032` | B | A | 39 |
| `G1-LEG-034` | B | A | 41 |
| `G1-LEG-048` | A | B | 55 |
| `G2-ELEC-170` | C | A | 25 |

**Critical G2-ELEC-170:** canonical key **C** corresponds `Cs=C`, while V9 tracker key **A** corresponds `Cs=3 C`. Prior V9 prose derived `Cs=3C` under explicitly balanced delta-to-star equivalence, but this does NOT verify how `capacitate de serviciu Cs` is defined in ANRE source. Do not silently replace canonical C with A; demand authoritative handbook definition, edition and source, plus independent review and provenance reconciliation.

**Other five G1-LEG:** 024, 028, 032, 034 and 048 require legal review against governing ordinances in force and historical question-bank edition. For 048 canonical A says customers can impose any payment method including one not offered by supplier, which looks suspect; V9 tracker B describes choice among supplier-provided methods. This is a strong **model-flagged** consistency concern, not authorization to change the application. G1-LEG-032 contains 4-year authorization age and requires review of validity rules at the relevant date.

Audit screen counts inferred from prior V9 status labels plus new V10/V11/V12: {"NOT_SCREENED":605,"V8":17,"V9":50,"V10":50,"V11":50,"V12":50}. No independent QA approvals. Ledger intentionally retains both keys rather than overwriting historic V9; canonical remains unchanged. No HTML/APK/answer modifications, no merge. A QA specialist must reconcile tracker derived value against original workbook and legal/normative source.
