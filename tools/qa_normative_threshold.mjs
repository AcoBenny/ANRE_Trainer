// ANRE audit-only QA helper, v0.1. No canonical QABC/keys modified.
// Structural candidate classification only, NOT source-edition review or answer approval.
function normalizeRomanian(value) {
  return String(value ?? "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/\s+/g, " ").trim();
}

function numericMeters(raw) {
  const n = normalizeRomanian(raw).match(/^(\d+(?:[.,]\d+)?)\s*(m|cm|mm)$/);
  if (!n) return null;
  const val = Number(n[1].replace(",", "."));
  return n[2] === "mm" ? val / 1000 : n[2] === "cm" ? val / 100 : val;
}

export function evaluateNormativeBound({question, options, rule}) {
  const q = normalizeRomanian(question);
  const choices = Object.entries(options ?? {});
  const output = (status, extra = {}) => ({ status, candidate_letter: null, approved_for_learning: false, source_edition_verified: false, flags: [], ...extra });
  if (!rule || rule.ruleType !== "maximum" || !rule.source_locator || !Number.isFinite(rule.defaultMaxMeters)) {
    return output("BLOCKED_SOURCE_RULE_MISSING");
  }
  if (!q.includes(normalizeRomanian(rule.objectKeyword)) || !q.includes("inaltim") || !q.includes("pardose")) {
    return output("BLOCKED_OBJECT_OR_MEASURE_SCOPE");
  }
  if (choices.length !== 3 || choices.some(([k, v]) => !["A", "B", "C"].includes(k) || numericMeters(v) === null)) {
    return output("BLOCKED_OPTIONS_OR_UNITS");
  }
  const relevant = (rule.exceptions ?? []).find(e => q.includes(normalizeRomanian(e.scopeKeyword)));
  const limit = relevant ? relevant.maxMeters : rule.defaultMaxMeters;
  const scopedTo = relevant ? relevant.scopeKeyword : "general";
  const eligible = choices.filter(([_, v]) => numericMeters(v) <= limit + 1e-9).map(([k]) => k);
  const asksForExamples = /(?:care dintre|ce valori|care valori|care inaltimi)/.test(q) && /(?:admise|permise|se pot monta|se pot instala)/.test(q);
  if (asksForExamples) {
    return output(eligible.length > 1 ? "MULTIPLE_ADMISSIBLE_EXAMPLES" : "ADMISSIBLE_EXAMPLE_CHECK", { eligible_letters: eligible, scoped_to: scopedTo, normative_max_m: limit, flags: ["QUESTION_REQUESTS_ADMISSIBLE_EXAMPLES_NOT_THE_NORMATIVE_BOUND"] });
  }
  if (!/(?:sa nu depaseasca\s*:|sa nu depaseasca\s+ce|care este (?:inaltimea )?maxim|limita maxima|inaltimea maxima|de cel mult\s*:)/.test(q)) {
    return output("NOT_AN_EXPLICIT_BOUND_QUESTION");
  }
  const eq = choices.filter(([_, v]) => Math.abs(numericMeters(v) - limit) < 1e-9).map(([k]) => k);
  if (eq.length === 0) return output("SOURCE_OR_OPTIONS_MISMATCH", {scoped_to: scopedTo, normative_max_m: limit, flags: ["NO_CHOICE_EQUALS_NORMATIVE_MAXIMUM"]});
  if (eq.length > 1) return output("MULTIPLE_EQUIVALENT_BOUND_CHOICES", {scoped_to: scopedTo, normative_max_m: limit, flags: ["DUPLICATE_NUMERIC_ANSWERS"]});
  return output("SINGLE_NORMATIVE_BOUND_CANDIDATE", {
    candidate_letter: eq[0],
    scoped_to: scopedTo,
    normative_max_m: limit,
    flags: ["BOUND_EXACT_MATCH_NOT_ANY_PERMITTED_VALUE", ...(relevant ? ["SPECIFIC_EXCEPTION_OVERRIDES_GENERAL_RULE"] : [])],
  });
}
