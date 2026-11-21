# CKPT-338 | Five grade-I legal source checks, conditional answer traps | 2026-11-21

- Parent branch `df28449e7dc6d2e7b0f2d8aaa6a5e639b25e3181`, PR #7 Draft. Original questions/ABC imported exactly as prior V206/V211 audit records reconciled against user uploaded XLSX. **No fresh workbook byte-level check this run**.
- Source pages accessed on official Portalul Legislativ: [Regulamentul ANRE din 10.05.2023](https://legislatie.just.ro/Public/DetaliiDocument/288046), [Legea 123/2012 (consolidated portal rendering)](https://legislatie.just.ro/Public/DetaliiDocument/311821), [Regulamentul de furnizare din 03.02.2023](https://legislatie.just.ro/Public/DetaliiDocument/280249). HTML snippets were checked by substring comparison against the page returned. All **five** packets passed A/B/C presence, imported key preservation and textual source snippet presence. This is not a qualified independent expert review.
- Source data: [V252_FIVE_G1_LEG002_007_011_040_043_PRIMARY_SOURCE_CONDITIONAL_ABC_2026_11_21.json](./V252_FIVE_G1_LEG002_007_011_040_043_PRIMARY_SOURCE_CONDITIONAL_ABC_2026_11_21.json). Source contexts stored there are **limited exact surrounding snippets**, not certified complete paragraph-before/paragraph-after windows fit for final in-app presentation.

| QABC / G1 ID | Imported key | Evidence-supported assessment | Open issue |
| --- | --- | --- | --- |
| QABC-0266 / G1-LEG-002 | B | B explicitly art.58(4)a | C references invoice nonpayment, also art.58(4)b, so uniqueness cannot be assumed |
| QABC-0271 / G1-LEG-007 | B | B probably intended for unauthorized work | Art.35 imposes cumulative Grade I PFA conditions; C at 9 kW is not necessarily legal |
| QABC-0275 / G1-LEG-011 | C | C matches duplicate *fee* type | All three call for a *local newspaper* whereas art.47 requires a **wide-circulation publication** |
| QABC-0304 / G1-LEG-040 | C | C is nearest to 10 kW / <1 kV / no business attestation | Art.35 A(a) requires further cumulative qualification and association |
| QABC-0307 / G1-LEG-043 | A | 5 **working** days for non-domestic unpaid bills art.26(4)b | A says only 5 days; original stem covers all contractual obligations, not just nonpayment |

## Reusable QA lesson
1. The same nominal grade/power statement does **not** establish that a Grade I PFA meets the separate cumulative legal conditions. Apply to LEG007 and LEG040 without double counting a case as newly resolved.
2. **Termination** for nonpayment under Legea 123 art.58(4)b differs from disconnection notice under supply regulation art.26(4). Keep causality and legal effects distinct.
3. Never silently upgrade **"ziar local"** to **"publicație de largă circulație"**, **"5 zile"** to **"5 zile lucrătoare"**, or **"any contract breach"** to **"unpaid invoice"**.

## Release gates
- All five questions remain on HOLD pending 2026 exact law version, current official scoring answers, qualified independent legal/source and independent linguistic review. **0/822 approved, 136/136 prior explicit hold units still unresolved**, no further validation inferred.
- No question, A/B/C, imported key, HTML, APK, stable/main, merge or release modified. Only the new V252+CKPT338 audit documents were intended.

