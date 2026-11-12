import assert from "node:assert/strict";
import { exactTableMinimum } from "../qa_normative_table_row.mjs";
const cases=[
  {
    "id": "NOR050_ORIGINAL",
    "q": "Secţiunea minimă admisă pentru conductoare de fază din circuite pentru prize monofazate în instalaţiile electrice din interiorul clădirilor este de:",
    "options": {
      "A": "2,5 mm2 cupru,",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "ONE_ROW_SPECIFIC_CANDIDATE",
    "letter": "A"
  },
  {
    "id": "NOR051_SOURCE_OBJECT_NOT_EXPLICIT",
    "q": "Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:",
    "options": {
      "A": "2,5 mm2 cupru,",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "SOURCE_OBJECT_MAPPING_REQUIRED",
    "letter": null
  },
  {
    "id": "FORCE_ROW_WITH_ORIGINAL_OPTIONS",
    "q": "Secţiunea minimă pentru circuite de putere este:",
    "options": {
      "A": "2,5 mm2 cupru,",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "ONE_ROW_SPECIFIC_CANDIDATE",
    "letter": "C"
  },
  {
    "id": "FORCE_COPPER",
    "q": "Secţiunea minimă pentru circuite de putere este:",
    "options": {
      "A": "1,5 mm2 cupru",
      "B": "2 mm2 cupru",
      "C": "3 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "ONE_ROW_SPECIFIC_CANDIDATE",
    "letter": "A"
  },
  {
    "id": "DUPLICATE_COPPER",
    "q": "Secţiunea minimă admisă pentru conductoare de fază din circuite pentru prize monofazate în instalaţiile electrice din interiorul clădirilor este de:",
    "options": {
      "A": "2,5 mm2 cupru",
      "B": "2.5 mm² cupru",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "MULTIPLE_ROW_SPECIFIC_CANDIDATES",
    "letter": null
  },
  {
    "id": "NEITHER_MATCH",
    "q": "Secţiunea minimă admisă pentru conductoare de fază din circuite pentru prize monofazate în instalaţiile electrice din interiorul clădirilor este de:",
    "options": {
      "A": "1,5 mm2 cupru",
      "B": "2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "NO_ROW_SPECIFIC_OPTION",
    "letter": null
  },
  {
    "id": "MISSING_SOURCE",
    "q": "Secţiunea minimă admisă pentru conductoare de fază din circuite pentru prize monofazate în instalaţiile electrice din interiorul clădirilor este de:",
    "options": {
      "A": "2,5 mm2 cupru,",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "BLOCKED_SOURCE_TABLE_MISSING",
    "letter": null
  },
  {
    "id": "MISSING_ABC",
    "q": "Secţiunea minimă admisă pentru conductoare de fază din circuite pentru prize monofazate în instalaţiile electrice din interiorul clădirilor este de:",
    "options": {
      "A": "2,5 mm2 cupru,",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "BLOCKED_OPTIONS",
    "letter": null
  },
  {
    "id": "UNMATCHED_CONTEXT",
    "q": "Secţiunea minimă pentru circuite iluminat este:",
    "options": {
      "A": "2,5 mm2 cupru,",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "SOURCE_OBJECT_MAPPING_REQUIRED",
    "letter": null
  },
  {
    "id": "DIACRITICLESS",
    "q": "Sectiunea minima admisa pentru conductoare de faza din circuite pentru prize monofazate in instalatiile electrice din interiorul cladirilor este de:",
    "options": {
      "A": "2,5 mm2 cupru,",
      "B": "1,5 mm2 cupru, 2,5 mm2 aluminiu",
      "C": "4 mm2 aluminiu"
    },
    "table": {
      "source_locator": "I7-2011 Anexa 5.32 nr.1.2 and 1.3; 5.4.6/5.4.7",
      "rows": [
        {
          "row_id": "1.2",
          "question_scope": "circuite pentru prize monofazate",
          "minimums": {
            "cupru": 2.5,
            "aluminiu": null
          }
        },
        {
          "row_id": "1.3",
          "question_scope": "circuite de putere",
          "minimums": {
            "cupru": 1.5,
            "aluminiu": 4
          }
        }
      ]
    },
    "expect": "ONE_ROW_SPECIFIC_CANDIDATE",
    "letter": "A"
  }
];
for(const x of cases){const o=exactTableMinimum({question:x.q,options:x.options,table:x.table});assert.equal(o.status,x.expect,x.id+" status");assert.equal(o.candidate_letter,x.letter,x.id+" letter");assert.equal(o.approved_for_learning,false,x.id+" learner safety");}
console.log(cases.length+" source-row synthetic cases PASS; no independent review");
