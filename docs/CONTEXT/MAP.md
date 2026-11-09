# ANRE Trainer | Small, scoped map

| Need | Canonical source to inspect | Minimum retrieval | Gate |
|---|---|---|---|
| Stable question ID and original stored answer | app/src/main/assets/anre_trainer.html | Exact question ID projection; never whole 1.58MB HTML | Source hash/commit must match |
| Browser/JS behavior | app/src/main/assets/anre_trainer.html | Exact function + AST/line span; avoid massive DATA line | Browser runtime evidence separate |
| Supplemental script | app/src/main/assets/audit_patch.js | Exact symbol/range | Recheck file in current branch |
| Android WebView | app/src/main/java/ro/anre/trainer/MainActivity.java | Only relevant method | Device test still required |
| Prior manuals/chapter mapping | docs/CHECKPOINTS/LATEST.md and its linked source chapter docs | ID + local page + original didactic paragraph | Independent source QA required |
| Open audit | https://github.com/AcoBenny/ANRE_Trainer/pull/7 | Relevant audit row / question ID only | Draft is not main |
| Historical development | PROJECT_JOURNEY.md | Read only matched milestone | Do not duplicate chronology |

**No guessing:** stored source text may have obsolete version or be a question bank rather than didactic literature. Prefer authoritative current ANRE/government sources verified by paragraph. Never treat the stored multiple-choice key as independently proven by an index.
