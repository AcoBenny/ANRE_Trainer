# CKPT-381 | GFR original Excel recovered: physical source verification for all seven known fidelity deltas

Date: **2026-11-22**. Previous checkpoint CKPT-380. Branch `audit/anre-v8-priority-17-20261109`, PR #7 Draft. Source-native forensic registry: [V292](./V292_NATIVE_XLSX_DIRECT_BINARY_7_SOURCE_FIDELITY_REOPEN_2026_11_22.json).

## Material source access improvement

The user's **ChatGPT Library**, not Google Drive, contains the missing *physical original source binaries*:
- `ELECTROTEHNICA-09.2024-2(1)(3).xlsx` and two additional independently present copies, all exactly SHA-256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`.
- `NORME-TEHNICE-Gr.-1-05.2023(1)(3).xlsx` and another matching copy, both exactly SHA-256 `bed56a32f24d19774ec9dfff8c5b1438176078d0e9c4eb9e8fa1ff1fc98c3092`.

Both hashes **match the SHA256 declared in V140/V282**. Read the actual workbook through artifact_tool and independently inspected original ZIP SpreadsheetML cell types, indexes, and shared strings. Neither original workbook was modified. This specifically **closes CKPT-379's original binary re-open blocker**; it does *not* authenticate an ANRE exam key, validate the running UI, or constitute independent expert signoff.

## All seven historically flagged grade-route fidelity differences, physically reopened

| Grade route(s) | QABC | Raw source cell | Verified original vs canonical meaning | Classification |
|---|---|---|---|---|
| G1-ELE-152 | QABC-0143 | Electrotehnică A159 | original **„Mărimea adimensională”** vs rewritten **„Mărimea caracteristică”** | 1 MATERIAL STEM |
| G1-ELE-154, G2-ELEC-292 | QABC-0145 | A161:D161 | actual cells **A161 string question; B161 numeric 1; C161 numeric 0; D161 text „1,5”**; canonical options are displayed as strings. Imported B unchanged | 2 NUMERIC-TYPE ONLY |
| G1-ELE-247, G2-ELEC-383 | QABC-0236 | Electrotehnică A254:D254 | original option B **„prin inducţie electromagnetică”**, rewritten option B **„prin inducţie electrostatică”** | 2 MATERIAL OPTION |
| G1-NOR-048 | QABC-0362 | Norme G1 A55:D55 | original A `numai direct din tabloul de distribuţie`; B `numai dintr-un circuit de iluminat normal`; C `dintr-un circuit de prize`; canonical has wholly rewritten A/B/C | 1 MATERIAL A/B/C |
| G1-NOR-072 | QABC-0386 | Norme G1 A79:D79 | original option B **„trebuie să poată fi deconectat uşor, fără utilizarea unei scule”** vs rewritten B **„trebuie să poată fi deconectat individual, iar conectarea să fie sigură și deconectabilă numai prin intermediul unei scule”** | 1 MATERIAL LOGICAL NEGATION |

**Count check:** 1+2+2+1+1=7 grade routes; **5 material** and **2 numeric-type**. All match historical V140 source-side findings. New evidence is the direct independent physical source re-open, **not a newly discovered set of seven**.

### More precise new traps established on source object

1. **QABC-0362 versus QABC-0363:** Norme G1 original rows **55 and 56** share the same stem but have **different words in A/B/C**. Row 55 has source C as sockets *without “numai”*; row 56 has source B as lighting *without “numai”*. They are separate answerable source-native variants, not safe to deduplicate by question stem. The exact choice order must survive mapping.
2. **QABC-0143 versus QABC-0568:** Electrotehnică original row 159 is reused as G1-ELE-152 and G2-ELEC-290, but G1's canonical stem was rewritten and G2 retains the original wording, so they currently have **different QABC IDs**. Do not infer that every QABC is a unique original physical source question, nor combine them without an explicit original-to-canonical mapping.
3. **QABC-0236 source-scope discrepancy and second qualification:** Original question: „Un corp conductor situat într-un câmp electric de intensitate E se încarcă cu electricitate:” A=`prin conducţie`; B=`prin inducţie electromagnetică`; C=`prin magnetizare`. The app changes B to `prin inducţie electrostatică`. The two processes differ: `electromagnetic induction` concerns varying magnetic flux ([OpenStax Physics §20.3](https://openstax.org/books/physics/pages/20-3-electromagnetic-induction)), while electrical charging/polarization by induction is caused by electrostatic forces ([OpenStax University Physics 2 §5.2](https://openstax.org/books/university-physics-volume-2/pages/5-2-conductors-insulators-and-charging-by-induction)). **Even the rewritten phrase needs qualification:** a conductor placed near an external static charge can be polarized and **remain overall neutral**; net charging needs a grounding/separation sequence or other charge transfer. Original answer letter B should **not** be certified from the rewritten card; no unique source-native answer authenticated. Preserve as a flagged teaching point, not a user-approved answer alteration.
4. **No original keyed answer provenance:** The inspected source workbooks are A:D question-plus-3-choices layouts. In the inspected rows, B/C/D alternative cells have the same raw style index within the row; no highlighted-answer provenance is apparent. Current imported keys remain *unofficial app metadata*, not confirmed scored keys.

### What this completed versus what it did not

- **COMPLETE (raw source provenance):** Original XLSX binaries recovered and verified by exact SHA, A/B/C contents and cell types physically reopened for the **7 known discrepancy grade routes**.
- **COMPLETE (P1 narrowly):** `QABC-0145` / both grade routes source-cell-type fidelity confirmed; binary verification blocker removed. Text rendering/UI smoke test and true independent review **STILL PENDING**. Numeric stringification is not shown to change the displayed option content.
- **NOT COMPLETE:** the five source-material alterations remain unresolved for final learner approval. No original ANRE scored key authenticated. 2026 bibliography and full legal/technical source match still require grade-specific clearance. No qualified independent technician/legal/linguistic reviewer was magically created by re-reading Excel.
- **UNCHANGED:** V283/V291 27 P0 + 2 P1 + 793 P2 = 822 grade routes; all still unapproved. The P1 **subgate** improved only. All original and canonical answer files, HTML, APK and app remain untouched; PR #7 stays Draft, no merge/release.

## Next finite path

1. Document source-native `QABC-0236` as not safely auto-scoreable; preserve the original plus an annotated educational explanation about magnetic induction vs electrostatic polarization/net charge.
2. Perform an **observational** read-only runtime/render test for the two `QABC-0145` number choices if a testable build is available; do not interpret a screenshot alone as independent answer validation.
3. Prioritize edition- and qualifier-dependent P0 cases and commission/obtain identifiable independent professional confirmation. Every technically clear P2 still needs its own option, original-text, relevant edition and qualified review gates before learning release.

## Evidence preservation

This checkpoint supersedes only the earlier claims that the original binary could not be re-opened *in the current session*. It does **not** rewrite V140/V282 historical findings. Direct full-cell evidence is in V292 and local GFR forensic output; workbook binaries remain owned by the user in ChatGPT Library and were not copied into the public GitHub repository.
