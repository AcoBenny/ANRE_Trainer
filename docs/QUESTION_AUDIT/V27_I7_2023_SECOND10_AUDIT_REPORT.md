# V27 | G1-NOR-011–020, I7-2011 completat 2023, source-locator and trap audit

Date 2026-11-09. Source read from user's Library PDF `803493174-I7-2011-completat2023.pdf`, 249 pp, "forma sintetică pentru data 2023-09-22". I7 source checked with exact provision + PDF page; relevant page images 13,49,56 visually inspected, other pages read as extracted text. The PDF was NOT uploaded to GitHub. Canonical 822-question HTML remains unchanged, 10 IDs are existing `G1-NOR-011..020`. Independent SME QA `NOT_RUN`.

## Source QA by ID

| Question | Stored key | Text-supported | Provision/page | Finding |
|---|---|---|---|---|
| G1-NOR-011 | C | C | 5.1.7.2(a), p.49 | SOURCE_MATCH |
| G1-NOR-012 | B | C_CONDITIONALLY | 5.1.7.2(a), p.49 | CONDITIONAL_KEY_RISK |
| G1-NOR-013 | C | C | 5.2.6.10, p.56 | SOURCE_MATCH |
| G1-NOR-014 | C | C | 5.2.6.12, p.56 | SOURCE_MATCH |
| G1-NOR-015 | C | C | 5.2.6.7, p.56 | SOURCE_MATCH |
| G1-NOR-016 | C | C | 5.2.6.4–5, p.56 | CONDITIONAL_SCOPE |
| G1-NOR-017 | C | C | 3.0.3.8, p.13 | SOURCE_MATCH |
| G1-NOR-018 | C | C | 3.0.3.8, p.13 | SOURCE_MATCH |
| G1-NOR-019 | C | C | 5.2.12.2.5, p.61 | SOURCE_MATCH |
| G1-NOR-020 | A | A_IF_COMBUSTIBLE | 5.3.3.18; istoric PE 102 sec.5.2.57, p.65 | CONDITIONAL_SCOPE |

**Counts:** {"SOURCE_MATCH":7,"CONDITIONAL_KEY_RISK":1,"CONDITIONAL_SCOPE":2}. 7 direct source matches; 2 conditional scope cases; 1 potential key/wording conflict. No key or app changes.

## Critical linguistic/technical gates

**G1-NOR-012** asks whether conductors for critical hospital loads and safety lighting are **"întotdeauna cupru"** (canonical B). In I7 art.5.1.7.2(a), p.49, use of copper in certain especially important circuits is *conditional*, notably if an equivalent aluminium conductor section would be less than 10 mm². Variant C "cupru sau aluminiu, condiţionat" is more compatible with the source as written. Do **not** replace B without checking potentially applicable special hospital requirements or historical exam interpretation. Status `CONDITIONAL_KEY_RISK`, separate independent QA required.

**G1-NOR-016** canonical C "numai în doze sau cutii" is close to art.5.2.6.4, but norm permits specifically designed **connection accessories** including boxes, etc. The qualifier "numai" can narrow wording overly, though competing A/B (inside tubes/building voids) explicitly prohibited by art.5.2.6.5. Status `CONDITIONAL_SCOPE`.

**G1-NOR-020** I7 5.3.3.18 (p.65) prohibits apparatus with **combustible dielectrics**, such as oil, in distribution boards. Older PE 102 art.5.2.57 (in a separate user Library PDF, p.126) allows equipment with **incombustible dielectrics** with manufacturer guarantee. Canonical A is supported for combustible oil, but question "aparate cu ulei" omits combustibility. Status `CONDITIONAL_SCOPE`.

**G1-NOR-017–018** both directly sourced in I7 art.3.0.3.8 p.13: constraints apply to visible and embedded installation, with fire-safe barriers/spacers for devices below IP54.

## QA assurance
- Per question source locator and page verified textually and three page images inspected. No new passages embedded or copied, no claim of offline linkage beyond user's existing Library source.
- Norm is consolidated to Sept 2023, not necessarily latest in 2026; a temporal-currentness review remains mandatory.
- No independent agent/human electrical engineer/linguistic QA actually executed. `NOT_RUN`.
- No modification to canonical keys, ABC, HTML/APK or GitHub main, and no merge/release.
