// Research-only classifier of permitted alternatives and false exclusivity.
// Requires externally verified exact clause, era and object. NOT answer QA signoff.
function norm(s){return String(s??"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replace(/\s+/g," ").trim();}

export function classifyDoorbellOptions({question,options,source}){
 const out=(status,detail={})=>({status,candidate_letter:null,source_edition_verified:false,independent_source_qa:"NOT_RUN",approved_for_learning:false,verdicts:[],...detail});
 if(!source?.locator||source?.object!=="doorbell_primary_supply"||!Array.isArray(source.allowed_routes)||source.allowed_routes.length===0)return out("BLOCKED_SOURCE_SCOPE");
 const q=norm(question);
 if(!q.includes("alimentarea")||!q.includes("sonerie")||!q.includes("220(230)"))return out("BLOCKED_OBJECT_OR_STEM");
 if(Object.keys(options??{}).sort().join(",")!=="A,B,C")return out("BLOCKED_ABC");
 const allowed=new Set(source.allowed_routes),verdicts=[];
 for(const [letter,raw] of Object.entries(options)){
  const t=norm(raw);
  const matches=[];
  if(/circuit de iluminat normal/.test(t))matches.push("normal_lighting");
  if(/circuit de prize/.test(t))matches.push("socket_circuit");
  if(/direct din tabloul de distributie/.test(t))matches.push("distribution_board");
  let verdict;
  if(!matches.length)verdict="BLOCKED_UNKNOWN_ROUTE";
  else if(/(?:\bnu\s+din|\bfara\b|\bnici\b)/.test(t))verdict="BLOCKED_NEGATED_ROUTE";
  else if(matches.length>1&&/ \bsi\b /.test(t))verdict="BLOCKED_SIMULTANEOUS_VS_ALTERNATIVE";
  else if(matches.some(x=>!allowed.has(x)))verdict="ROUTE_NOT_IN_SOURCE";
  else if(/(?:\bnumai\b|\bexclusiv\b|\bdoar\b)/.test(t)&&matches.length!==allowed.size)verdict="FALSE_EXCLUSIVITY";
  else verdict="SUPPORTED_PERMITTED_ROUTE";
  verdicts.push({letter,verdict,matches,exclusive:/(?:\bnumai\b|\bexclusiv\b|\bdoar\b)/.test(t)});
 }
 if(verdicts.some(x=>x.verdict.startsWith("BLOCKED_")))return out("MANUAL_REVIEW_UNKNOWN_OR_COMPLEX_OPTION",{verdicts});
 const valid=verdicts.filter(x=>x.verdict==="SUPPORTED_PERMITTED_ROUTE");
 if(valid.length===1)return out("ONE_VALID_EXAM_OPTION",{candidate_letter:valid[0].letter,verdicts});
 if(valid.length>1)return out("MULTIPLE_VALID_OPTIONS",{verdicts});
 return out("NO_VALID_OPTION",{verdicts});
}
