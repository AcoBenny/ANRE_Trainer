# CKPT-207 | G1-LEG-017 / G1-LEG-024 live source and option-scope reconciliation | 2026-11-18

## Context / no duplicated coverage
Resume from CKPT-206 and CKPT-205 on `audit/anre-v8-priority-17-20261109` (PR #7 Draft). These are two **previously blocked, previously researched** QABC units (CKPT-190 / CKPT-191); 0 new units and 0 learner approvals. No canonical question, options, keys, HTML, APK or release modifications.

## G1-LEG-017 | Supplier's right to terminate the supply contract
- Canonical ID: `G1-LEG-017`, unit `AU-4b365bd0966b300d`. Imported key **B**, unchanged.
- Original question (per CKPT-190): **Furnizorul de energie electrică este îndreptăţit sã rezilieze contractul de furnizare a energiei electrice  în caz de:**
- A: **sustragerea de energie electrică constatată prin hotărâre judecătorească definitivă**
- B: **racordare ilegală la reţeaua de distribuţie**
- C: **refuz al clientului final de a constitui garanţia solicitată de furnizor atunci când acesta constată acţiuni menite să denatureze în orice fel indicaţiile echipamentelor de măsurare**

### Primary source reopened successfully, 18 November 2026
Official consolidated Portal Legislativ view of Legea 123/2012, Title I, Article 58(4)-(6): https://legislatie.just.ro/Public/DetaliiDocument/311821 (live page HTTP 200 through retrieved public page).
- Art 58(4)(a) **specifically provides contract termination for electricity theft established by final court judgment**.
- Art 58(4)(b),(c) also mentions unpaid invoices and other legally specified situations. This means the listed termination cases are not restricted solely to A and a blanket exclusion of every conceivable illegal-connection termination scenario would be unsafe.
- Art 58(5) concerns supplier-requested financial security for meter manipulation/bypassing.
- Art 58(6) prescribes the distinct **right to request grid disconnection** on refusal of financial security, not automatically contract termination.

### Alternative and negative comparison
- **A: STRONG_EXACT_AFFIRMATIVE_MATCH** to art 58(4)(a). Strongest direct statutory answer. Candidate A only; original B not altered.
- **B: NOT_EXACTLY_ENUMERATED_IN_ART58_4**. Illegal connection can entail different legal consequences; cannot infer universal contractual termination solely from physical illegal connection. Art 58(4)(c) and supply-contract/sector regulation may contain relevant additional case-specific grounds not exhaustively adjudicated here.
- **C: DISCONNECTION_NOT_TERMINATION** under art 58(6); wrong legal action.
- Version caution: retrieval verifies displayed legal text on this date, **not** an officially authenticated examination bibliography edition/scored answer key. Contested possibility B under other law is still an explicit open caveat.
- Status `PROVISIONAL_A_WITH_ART58_4C_CAVEAT`; no independent legal or linguistic reviewer executed.

## G1-LEG-024 | Need for technical connection approval for a new site
- Canonical ID `G1-LEG-024`; unit `AU-99a07af473ffa794`. Imported key **A**, unchanged.
- Original question (per CKPT-190): **Obţinerea avizului tehnic de racordare de către un utilizator:**
- A: **nu este obligatorie pentru o durata mai mică de 6 luni**
- B: **nu este obligatorie pentru o putere ceruta sub 100 kW**
- C: **este obligatorie pentru orice loc de consum/producere nou**

### Primary source reopened successfully, 18 November 2026
Official consolidated Regulamentul de racordare (Ordin ANRE 59/2013) https://legislatie.just.ro/Public/DetaliiDocument/310640 (HTTP 200 live).
- Art 5(1)(a)-(c) includes **new production, new consumption including temporary sites, and new combined sites** in the application process.
- Art 9(b)-(c) describes an application to obtain ATR and ATR issuance as connection-process phases, explicitly **'după caz'**.
- Art 11(1) says the *connection/application or update request* covers each consumption/production site **regardless of period and power**. This supports rejection of a generic period/size exemption, but is a `cerere` provision and must not be deceptively re-labeled a direct unconditional `ATR` rule.
- Art 24 and 25(1) establish the content and issuing network operator of ATR for connected installations.
- The page includes 2026 amendments (e.g. Article 36), but source-applicability at the exam edition is not formally signed off.

### Alternatives and negative comparison
- **A: REJECT_AS_BLANKET_EXEMPTION**. Temporary <6 months is not generally exempt by the source: art 5(1)(b), art 11(1).
- **B: REJECT_AS_BLANKET_EXEMPTION**. A requested power <100 kW is not itself a general exemption: art 11(1).
- **C: CONDITIONAL_GENERAL_CONNECTION_RULE**. Strongest normal new-location answer by art 5 + art 9 + art 24-25, but `orice` is absolute, while art 9 says `după caz`; another applicable regime or exception could limit scope. Do not certify it as an exception-free universal legal statement.
- Status `PROVISIONAL_C_CONDITIONAL_UNIVERSALITY`. No independent legal/linguistic reviewer executed.

## QA and gate
- Both exact original QABC texts and imported keys copied from previously verified CKPT-190/191; source-current page re-opened, article-object/action compared option by option. No full rehash against the entire V73 canonical ledger performed during this iteration.
- A substantive human or genuinely independent model reviewer was **not** run. Live original portal retrieval is **not** official 2026 ANRE exam-key authentication.
- `new_unique_units=0`, `existing_blocked_cases_revisited=2`, `approved_for_learning=0`, `canonical_edits=0`, `independent_legal_QA=NOT_RUN`, `independent_linguistic_QA=NOT_RUN`.
- Next prioritize irreducible *new* blocked cases/source exceptions from the 50 blocked + 45 legacy-only ledger, without re-reading solved material. Maintain PR#7 Draft; no merge/release.
