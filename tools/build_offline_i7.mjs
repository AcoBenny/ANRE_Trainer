// ANRE Trainer | Generator de index I7 offline. Node.js 18+; zero dependinte.
// NU modifica APK, HTML-ul aplicatiei, intrebarile ori baremele.
// node tools/build_offline_i7.mjs --self-test
// node tools/build_offline_i7.mjs
// node tools/build_offline_i7.mjs --input "pagina-salvata.html"
// Output: offline_legal_build/i7_offline.html + i7_manifest.json
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { createHash } from "node:crypto";
import { resolve, join } from "node:path";

function decodeEntities(s){
 const named={amp:"&",lt:"<",gt:">",quot:'"',apos:"'",nbsp:" ",bdquo:"„",ldquo:"“",rdquo:"”",ndash:"–"};
 return s.replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi,(all,key)=>{
  if(key[0]==="#"){const n=key[1]?.toLowerCase()==="x"?parseInt(key.slice(2),16):parseInt(key.slice(1),10);return n>0&&n<=1114111?String.fromCodePoint(n):all;}
  return named[key.toLowerCase()]??all;
 });
}

function extractText(html){
 let s=html.replace(/<!--[\s\S]*?-->/g," ").replace(/<(script|style|nav|footer)\b[^>]*>[\s\S]*?<\/\1\s*>/gi," ");
 s=s.replace(/<br\s*\/?>/gi,"\n").replace(/<\/?(?:p|div|section|article|h[1-6]|tr|li|table|ul|ol)\b[^>]*>/gi,"\n").replace(/<\/?t[dh]\b[^>]*>/gi," | ");
 s=decodeEntities(s.replace(/<[^>]+>/g," ").replace(/\r/g,"").replace(/[ \t]+/g," ").replace(/ *\n */g,"\n").replace(/\n{3,}/g,"\n\n"));
 const p=s.toLowerCase().lastIndexOf("forma printabilă");if(p>=0)s=s.slice(p+"forma printabilă".length);
 const m=/(?:REGLEMENTARE TEHNICĂ|ORDIN nr\.|LEGEA nr\.)\s+(?:din|[\d.])/i.exec(s);if(m)s=s.slice(m.index);
 return s.trim();
}

function makeSections(text){
 const re=/(?:^|[\s\n])(\d{1,2}(?:\.\d{1,3}){1,6})\.\s+(?=[^\s])/g;
 let marks=[],m;while((m=re.exec(text))!==null)marks.push({id:m[1],start:m.index+m[0].indexOf(m[1])});
 let out=[],seen=new Set();for(let i=0;i<marks.length;i++){const x=marks[i],body=text.slice(x.start,i+1<marks.length?marks[i+1].start:text.length).trim().slice(0,12000);if(body.length>=24&&!seen.has(x.id)){out.push({id:x.id,text:body});seen.add(x.id);}}return out;
}

function validateI7(text,sections){
 const problems=[];if(text.length<90000)problems.push("text sub 90.000 caractere");if(!/Normativ pentru proiectarea, execuția și exploatarea instalațiilor electrice/i.test(text))problems.push("titlu I7 absent");
 for(const id of ["5.2.12.3.10","5.3.3.21","8.1.1.3.3"])if(!text.includes(id))problems.push("reper absent: "+id);if(sections.length<70)problems.push("sub 70 sectiuni indexate");return problems;
}

const READER="<!doctype html>\n<html lang=\"ro\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n<title>ANRE | Legislație offline</title>\n<style>body{font:16px system-ui,Segoe UI,sans-serif;margin:0;background:#f2f5fa;color:#17213b}\nheader{background:#182b54;color:white;padding:20px;position:sticky;top:0}\nheader h1{font-size:1.2rem;margin:0 0 10px}\ninput{box-sizing:border-box;width:100%;padding:13px;border-radius:7px;border:1px solid #c6d4e4;font-size:1rem}\nmain{max-width:900px;margin:auto;padding:18px}\nsmall{color:#596986}\n.card{background:white;border:1px solid #d5dfeb;border-radius:9px;padding:16px;margin:12px 0;white-space:pre-wrap;overflow-wrap:anywhere}\n.tag{font-weight:700;color:#182b54}button{padding:8px 12px;cursor:pointer;background:#fff;border:1px solid #c6d4e4;border-radius:7px}\n#full{display:none}\n</style></head>\n<body><header><h1>ANRE Trainer | Bibliotecă legislativă offline</h1><input id=\"q\" type=\"search\" placeholder=\"Caută articolul (5.2.12.3.10) sau expresie...\" autocomplete=\"off\"></header>\n<main><p id=\"meta\"></p><p><strong>Notă:</strong> aceasta este o copie datată și consultativă, nu o actualizare în timp real. Pentru uz juridic verifică Monitorul Oficial.</p><button id=\"fullToggle\">Arată textul integral</button><div id=\"full\" class=\"card\"></div><div id=\"result\"></div></main>\n<script id=\"source-data\" type=\"application/json\">__DATA__</script>\n<script>\n\"use strict\";\nconst DATA=JSON.parse(document.getElementById(\"source-data\").textContent);\nconst q=document.getElementById(\"q\"),result=document.getElementById(\"result\");\nfunction norm(v){return String(v).normalize(\"NFD\").replace(/[\\u0300-\\u036f]/g,\"\").toLowerCase();}\ndocument.getElementById(\"meta\").textContent=DATA.title+\" | Captură: \"+DATA.build_timestamp+\" | Secțiuni: \"+DATA.section_count+\" | SHA256: \"+DATA.sha256.slice(0,16)+\"…\";\nconst all=document.getElementById(\"full\");\nall.textContent=DATA.full_text;\ndocument.getElementById(\"fullToggle\").addEventListener(\"click\",function(){all.style.display=all.style.display===\"block\"?\"none\":\"block\";});\nfunction render(){\n const term=norm(q.value.trim()),hits=DATA.sections.filter(function(s){return !term||norm(s.id+\" \"+s.text).includes(term);}).slice(0,80);\n result.replaceChildren();const counter=document.createElement(\"p\");counter.textContent=hits.length+\" secțiuni afișate (maxim 80)\";result.append(counter);\n hits.forEach(function(s){const e=document.createElement(\"article\"),h=document.createElement(\"div\"),body=document.createElement(\"div\");e.className=\"card\";h.className=\"tag\";h.textContent=\"§ \"+s.id;body.textContent=s.text;e.append(h,body);result.append(e);});\n}\nq.addEventListener(\"input\",render);\nconst hash=decodeURIComponent(location.hash.slice(1));if(hash)q.value=hash;\nrender();\n</script></body></html>";

const OFFICIAL_URL="https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132";
const args=process.argv.slice(2);
if(args.includes("--self-test")){
 const fixture='<html><nav>MENIU</nav><p>Forma printabilă</p><p>REGLEMENTARE TEHNICĂ din 2011</p><p>5.2.12.3.10. Distanța maximă pe traseul drept este 25 m.</p><p>5.3.3.21. Excepție pentru clădiri.</p></html>';
 const t=extractText(fixture),s=makeSections(t);
 if(s.length!==2||s[0].id!=="5.2.12.3.10"||t.includes("MENIU"))throw Error("Self-test a esuat.");
 console.log("PASS: extragere și indexare HTML sintetice");process.exit(0);
}
const inIndex=args.indexOf("--input"),outIndex=args.indexOf("--output");
if(inIndex>=0&&!args[inIndex+1])throw Error("--input necesita cale");
if(outIndex>=0&&!args[outIndex+1])throw Error("--output necesita cale");
const input=inIndex>=0?args[inIndex+1]:null,outDir=resolve(outIndex>=0?args[outIndex+1]:"offline_legal_build");
async function download(){
 const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),30000);
 try{
  const r=await fetch(OFFICIAL_URL,{signal:controller.signal,headers:{"User-Agent":"ANRE-Trainer-offline-library/0.1"}});
  if(!r.ok)throw Error("HTTP "+r.status);
  if(new URL(r.url).hostname!=="legislatie.just.ro")throw Error("Redirect suspect: "+r.url);
  if(!(r.headers.get("content-type")||"").includes("text/html"))throw Error("Raspunsul nu este HTML");
  return await r.text();
 } finally {clearTimeout(timeout);}
}
let html;
try{html=input?await readFile(resolve(input),"utf8"):await download();}
catch(e){console.error("DESCARCARE EȘUATĂ:",e.message);process.exit(2);}
const full_text=extractText(html),sections=makeSections(full_text),errors=validateI7(full_text,sections);
if(errors.length){
 console.error("QA FAIL. Captură incompletă sau parser inadecvat: "+errors.join("; "));
 console.error("Niciun fișier nu a fost promovat la sursă activă.");process.exit(3);
}
const sha256=createHash("sha256").update(full_text).digest("hex");
const manifest={
 id:"I7-2011",title:"I7-2011 (copie offline din portalul legislativ)",source_url:OFFICIAL_URL,
 source_type:input?"USER_SUPPLIED_HTML_UNVERIFIED":"OFFICIAL_PORTAL_FETCH",
 build_timestamp:new Date().toISOString(),sha256,
 validation:"STRUCTURAL_ONLY",independent_qa:"NOT_RUN",approved_for_app:false,offline:true,
 section_count:sections.length
};
const payload={...manifest,sections,full_text};
const embedded=JSON.stringify(payload).replace(/</g,"\\u003c");
await mkdir(outDir,{recursive:true});
await writeFile(join(outDir,"i7_offline.html"),READER.replace("__DATA__",embedded),"utf8");
await writeFile(join(outDir,"i7_manifest.json"),JSON.stringify(manifest,null,2),"utf8");
console.log("INDEX OFFLINE CREAT:",outDir,"sectiuni=",sections.length,"hash=",sha256);
console.log("STATUS: VERIFICARE STRUCTURALĂ; NU este validare tehnică sau legală finală.");
