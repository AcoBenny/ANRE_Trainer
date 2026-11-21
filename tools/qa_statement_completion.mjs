// ANRE Avengers Academy v1: complete partial-statement A/B/C against structured source clauses.
// This is a narrow structural research helper. No normative-2026 or answer approval is implied.
function normalize(t){return String(t??"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").replaceAll("²","2").toLowerCase().replace(/\s+/g," ").trim();}

export function classifyContinuation({stem,options,rule}){
 const result=(status,extra={})=>({status,candidate_letter:null,graded_option_labels:[],approved_for_learning:false,verified_current_edition:false,independent_QA:"NOT_RUN",...extra});
 if(!rule?.source_locator||!Number.isInteger(rule.mono_conductors)||!Number.isInteger(rule.copper_mm2)||!Number.isInteger(rule.aluminium_mm2))return result("BLOCKED_SOURCE_EDITION_OR_RULE");
 const s=normalize(stem);
 if(!s.includes("conductorul neutru")||!s.includes("aceeasi sectiune")||!s.includes("conductorul de faza")||!s.endsWith(":"))return result("NOT_STATEMENT_COMPLETION_STEM");
 if(Object.keys(options??{}).sort().join(",")!=="A,B,C")return result("BLOCKED_ABC_MISSING");
 const monoMap={un:1,unu:1,una:1,doi:2,doua:2,trei:3,patru:4,cinci:5};
 const assessments=[];
 for(const [letter,text]of Object.entries(options)){
  const n=normalize(text),mono=n.match(/monofazate\s+cu\s+(\d+|un|unu|una|doi|doua|trei|patru|cinci)\s+conductoare/);
  const isPoly=/\bpolifazate\b/.test(n),cu=n.match(/(\d+)\s*mm2\s*(?:cupru|cu)\b/),al=n.match(/(\d+)\s*mm2\s*(?:aluminiu|al)\b/);
  const unbounded=/indiferent\s+de\s+sectiunea\s+conductoarelor\s+de\s+faza/.test(n);
  if(!mono||!isPoly){assessments.push({letter,judgment:"BLOCKED_STRUCTURE"});continue;}
  const monoNumber=/^\d+$/.test(mono[1])?Number(mono[1]):monoMap[mono[1]];
  if(monoNumber!==rule.mono_conductors){assessments.push({letter,judgment:"SOURCE_EDITION_SCOPE_MISMATCH"});continue;}
  if(unbounded){assessments.push({letter,judgment:"OVERBROAD_UNBOUNDED_POLYPHASE"});continue;}
  if(!cu||!al){assessments.push({letter,judgment:"BLOCKED_THRESHOLDS_OR_UNIT"});continue;}
  assessments.push({letter,judgment:Number(cu[1])===rule.copper_mm2&&Number(al[1])===rule.aluminium_mm2?"MATCH_RULE":"WRONG_MATERIAL_THRESHOLDS"});
 }
 const matches=assessments.filter(x=>x.judgment==="MATCH_RULE");
 if(matches.length>1)return result("MULTIPLE_MATCHING_COMPLETIONS",{graded_option_labels:assessments});
 if(matches.length===1)return result("ONE_COMPLETION_CANDIDATE",{candidate_letter:matches[0].letter,graded_option_labels:assessments,source_era:rule.edition});
 if(assessments.every(x=>x.judgment==="SOURCE_EDITION_SCOPE_MISMATCH"))return result("SOURCE_EDITION_SCOPE_MISMATCH",{graded_option_labels:assessments});
 return result("NO_SUPPORTED_COMPLETION",{graded_option_labels:assessments});
}
