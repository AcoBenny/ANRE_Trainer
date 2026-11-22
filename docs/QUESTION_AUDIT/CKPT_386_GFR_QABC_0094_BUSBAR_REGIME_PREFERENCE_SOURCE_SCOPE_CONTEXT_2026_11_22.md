# CKPT-386 | GFR QABC-0094: double-busbar single-breaker normal mode, context expands C but no universal winner

Date 2026-11-22. Follows CKPT-385. Distinct external technical sources reopened. This is additional *research*, not qualified professional grading, and not alteration of prior CKPT-378.

## Original QABC-0094, original imported key not superseded

Stem: `În cazul unei scheme cu două bare colectoare şi un întreruptor pe circuit este de preferat ca în regim normal de funcţionare:`
- **A** `una dintre barele colectoare să fie sub tensiune, cealaltă bară fiind menţinută în rezervă rece;`
- **B** `ambele bare colectoare să fie sub tensiune, cupla transversală fiind menţinută în funcţiune;`
- **C** `ambele bare colectoare să fie menţinute sub tensiune, cupla transversală fiind în rezervă caldă.`

User hypothesis from previous approved conversation: **A for „siguranța exploatării”**; keep explicitly as *user interpretation*, not exam-scored confirmation. Prior second blind AI preferred C; CKPT-378 left `UNIVERSAL_ANSWER_NOT_ESTABLISHED`.

## Reopened source with exact equipment and adjacent paragraphs

Technical Romanian **Centrale, stații și rețele electrice**, double-busbar section and two explicitly discussed ordinary modes:
https://fliphtml5.com/twmvq/sbma/Centrale-statii-si-retele-electrice/ (HTML lines near 1518–1533, PDF printed pp. 180–181).

- Context before: double busbar, **one circuit breaker per feeder**, two bus disconnectors and a transverse bus coupler are the **same physical topology** as original question.
- In one described normal mode, the feeder circuits use one bus; second bus is **energized and kept in hot standby** through the bus coupler. It does *not* describe a second bus in `rezervă rece`.
- In another, sources and feeders are split across both buses, with bus coupler **closed or open** according to fault-current and dispatch requirements.
- Context after: sectionalizing and bus transfer requirements/maintenance; splitting two live buses with coupler open can improve selectivity and limit short-circuit interaction, while running coupler closed can serve other system objectives.

Independent technical corroboration, exact same **double-busbar single-breaker** physical arrangement:
https://electrical-engineering-portal.com/design-issues-hv-busbar-protection-systems (§1.2). The text describes improved bus-fault selectivity with coupler **open** and isolated protection zones, but explains cases where all feeders are shifted to one bus and other bus de-energized. It warns that the best topology/regime depends on **power-flow constraints** and protection strategy.

Relevant operational glossary: NTE 009/10/00 labels `rezervă caldă` and `rezervă rece` under specific circuit-breaker/separator configurations, but these state definitions alone **do not prescribe a universal mode preference**. Earlier source: https://legislatie.just.ro/Public/DetaliiDocument/122751 .

## A/B/C proof, counterexample and language

- **A**: one bus energised with other *cold*. Possible safety, isolation or maintenance condition; easy-to-isolate de-energized bus reduces its exposure but delays switching/transfers. Not supported as a **universal preferred normal regime** by reopened same-topology references; the textbook's one-working-bus mode explicitly calls the spare **hot**, not cold.
- **B**: both energized and transverse coupler operating/closed, a plausible normal mode in some operational and power-flow regimes; however may reduce bus fault selectivity/independent zones or enlarge contingency impact.
- **C**: both energized, coupler kept in hot reserve/open, a **specific technically supported normal topology** when feeders/sources can be split and bus coupler is prepared for switching. It aligns most directly with the fault-zone selectivity source, but not necessarily optimal for every plant or all loading conditions.
- Pairs A/B: trade-off cold reserve vs live parallel interconnection; A/C: spare not energized vs both energized, faster bus service; B/C: closed vs prepared open coupler affects fault-zone coupling and fault power.
- **Research finding:** in a common double-busbar scheme C has **better source-specific support** than the earlier impression that A must be default because of safety. However sources explicitly support multiple ordinary modes. `preferat` lacks stated objective (continuity/safety/single-bus/short-circuit constraints), so **a universally unique correct answer is not established** by these sources. User's A stays hypothesis, blind model's C is not signed off, imported grade key unchanged.

## Didactic card, paraphrase

Context before: two busbars and one breaker per outgoing circuit can be operated with different combinations of energized buses and transverse coupler according to operational goals.
**Central focus: An open bus coupler with both busbars energized can preserve independent protection zones and allow bus transfers; a cold spare bus trades readiness for isolation. Neither condition is a universal rule without an operating objective.**
Context after: system dispatch, protection selectivity, short-circuit current and switching procedures determine preferred scheme for the actual installation. This explanation is not an official answer key and must not be substituted for the original A/B/C exam choices.

## Gate and no mutation

- State `P0_DISPUTED__C_SOURCE_SUPPORTED_NORMAL_MODE__NO_UNIVERSAL_PREFERENCE` with pending qualified review and official answer-key evidence.
- Do not mark QABC-0094 approved; do not rewrite original options, canon, grades, HTML or APK; no merge/release PR #7 Draft.
- The existing 27 P0 / 2 P1 / 793 P2 validation queue remains intact; 0/822 qualified approvals.
