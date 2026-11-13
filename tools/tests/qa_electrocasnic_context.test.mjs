import assert from "node:assert/strict";
import { contextFromDomesticAppliance } from "../qa_electrocasnic_context.mjs";
const cases = [
  {
    "id": "NOR051_original",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "CANDIDATE_INFERRED_DOMESTIC_SOCKET_CONTEXT",
    "candidate": "A"
  },
  {
    "id": "explicit_socket",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul de priză unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "CANDIDATE_EXPLICIT_SOCKET_CONTEXT",
    "candidate": "A"
  },
  {
    "id": "hardwired",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul cu alimentare fixă unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "NO_AUTOMATIC_SOCKET_MAPPING",
    "candidate": null
  },
  {
    "id": "industrial",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor industrial electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "BLOCKED_SCOPE_MISMATCH",
    "candidate": null
  },
  {
    "id": "lower_power",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 1 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "NOT_TARGET_SEMANTIC_CASE",
    "candidate": null
  },
  {
    "id": "wrong_material",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 aluminiu",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "OPTIONS_NEED_MANUAL_REVIEW",
    "candidate": null
  },
  {
    "id": "no_source",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.6",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "BLOCKED_EXACT_NORM_SOURCE",
    "candidate": null
  },
  {
    "id": "duplicate_correct",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "2.5 mm² cupru",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "OPTIONS_NEED_MANUAL_REVIEW",
    "candidate": null
  },
  {
    "id": "monofazat_missing",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic trifazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "NOT_TARGET_SEMANTIC_CASE",
    "candidate": null
  },
  {
    "id": "unit_ambiguity",
    "question": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm cupru",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "source": {
      "section": "5.4.7",
      "table": "5.32",
      "minimum_socket_cu_mm2": 2.5,
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "status": "OPTIONS_NEED_MANUAL_REVIEW",
    "candidate": null
  }
];
for (const x of cases) {
 const out=contextFromDomesticAppliance({question:x.question,options:x.options,source:x.source});
 assert.equal(out.status,x.status,x.id+": status");
 assert.equal(out.candidate_letter,x.candidate,x.id+": candidate");
 assert.equal(out.approved_for_learning,false,x.id+": learner gate");
}
console.log(cases.length+" electrocasnic context fixtures pass; NOT independent source QA");
