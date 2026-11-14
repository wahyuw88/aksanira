#!/usr/bin/env node
/**
 * AKSANIRA staging browser QA. Requires Node.js, Playwright and Chromium.
 * Checks every root HTML route on desktop/mobile, metadata, overflow, lazy images,
 * accessible names, keyboard focus progression, same-origin resources and runtime errors.
 * Does not submit forms, complete payments, verify email delivery, or replace WCAG review.
 */
import { readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const base=(process.env.BASE_URL||'').replace(/\/$/,'');
if(!base){console.error('Set BASE_URL=https://your-staging.vercel.app');process.exit(2)}
let chromium; try{({chromium}=await import('playwright'))}catch{console.error('Playwright missing. Run npm ci && npx playwright install chromium');process.exit(2)}
const root=path.dirname(fileURLToPath(import.meta.url));
const files=(await readdir(root)).filter(f=>f.toLowerCase().endsWith('.html')).sort();
const routes=files.map(file=>({file,route:file==='index.html'?'/':`/${file.replace(/\.html$/i,'')}`}));
const browser=await chromium.launch({headless:true}); const results=[];
async function inspect(page,width,height){
 await page.setViewportSize({width,height});
 await page.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=Math.max(300,innerHeight*.8)){scrollTo(0,y);await new Promise(r=>setTimeout(r,30))}scrollTo(0,0)});
 await page.waitForTimeout(150);
 return page.evaluate(()=>{
  const visible=e=>{const s=getComputedStyle(e);return s.display!=='none'&&s.visibility!=='hidden'&&e.getAttribute('tabindex')!=='-1'};
  const name=e=>(e.getAttribute('aria-label')||e.getAttribute('aria-labelledby')||e.innerText||e.value||e.getAttribute('title')||'').trim();
  const controls=[...document.querySelectorAll('a[href],button,input,select,textarea,[role="button"],[tabindex]')].filter(visible);
  return {viewport:document.documentElement.clientWidth,document:document.documentElement.scrollWidth,title:document.title.trim(),h1:document.querySelectorAll('h1').length,
   brokenImages:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.currentSrc||i.src),
   unloadedImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.currentSrc||i.src),
   unlabeledInputs:[...document.querySelectorAll('input,select,textarea')].filter(e=>!['hidden','submit','button','reset'].includes((e.type||'').toLowerCase())&&!(e.labels?.length||e.getAttribute('aria-label')||e.getAttribute('aria-labelledby'))).map(e=>({tag:e.tagName,type:e.type||'',id:e.id||'',name:e.name||''})),
   unnamedControls:controls.filter(e=>['BUTTON','A'].includes(e.tagName)||e.getAttribute('role')==='button').filter(e=>!name(e)&&!e.querySelector('img[alt],svg[aria-label]')).map(e=>({tag:e.tagName,href:e.getAttribute('href'),text:e.innerText})),
   emptyLinks:[...document.querySelectorAll('a[href]')].filter(a=>!name(a)&&!a.querySelector('img[alt],svg[aria-label]')).length,
   formCount:document.forms.length,forms:[...document.forms].map(f=>({action:f.getAttribute('action'),method:f.method}))};
 });
}
try{
 for(const item of routes){const page=await browser.newPage({viewport:{width:1365,height:900}});const errors=[],bad=[];
  page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
  page.on('response',r=>{try{if(new URL(r.url()).origin===new URL(base).origin&&r.status()>=400)bad.push({status:r.status(),url:r.url()})}catch{}});
  let http=null,navigationError=null,desktop=null,mobile=null,keyboard=null;
  try{const response=await page.goto(base+item.route,{waitUntil:'domcontentloaded',timeout:30000});http=response?.status()??null;await page.waitForLoadState('load',{timeout:10000}).catch(()=>{});
   desktop=await inspect(page,1365,900);mobile=await inspect(page,390,844);
   await page.setViewportSize({width:1365,height:900});await page.evaluate(()=>{document.querySelector('body')?.setAttribute('tabindex','-1');document.body.focus()});
   const focus=[];for(let i=0;i<8;i++){await page.keyboard.press('Tab').catch(()=>{});focus.push(await page.evaluate(()=>({tag:document.activeElement?.tagName,id:document.activeElement?.id||'',text:(document.activeElement?.innerText||'').trim().slice(0,80),href:document.activeElement?.getAttribute('href')})))}
   keyboard={steps:focus.length,distinctTargets:new Set(focus.map(x=>`${x.tag}|${x.id}|${x.href}|${x.text}`)).size,targets:focus};
  }catch(e){navigationError=e.message}
  results.push({file:item.file,route:item.route,http,navigationError,desktop,mobile,keyboard,badSameOriginResponses:bad,pageErrors:errors});await page.close();
 }
 for(const route of ['/robots.txt','/sitemap.xml']){let status=null,error=null;try{status=(await fetch(base+route)).status}catch(e){error=e.message}results.push({route,http:status,error})}
}finally{await browser.close()}
const failures=results.filter(r=>r.http!==200||r.navigationError||r.error||(r.desktop&&(!r.desktop.title||r.desktop.h1<1||r.desktop.document>r.desktop.viewport||r.desktop.brokenImages.length||r.desktop.unlabeledInputs.length||r.desktop.unnamedControls.length||r.desktop.emptyLinks))||(r.mobile&&(r.mobile.document>r.mobile.viewport||r.mobile.brokenImages.length||r.mobile.unlabeledInputs.length||r.mobile.unnamedControls.length||r.mobile.emptyLinks))||(r.badSameOriginResponses?.length||r.pageErrors?.length||(r.keyboard&&r.keyboard.distinctTargets<2)));
const report={base,testedAt:new Date().toISOString(),scope:'all root HTML clean routes; Chromium desktop/mobile; lazy images, metadata, controls, keyboard progression, same-origin resources and runtime errors',htmlFiles:routes.length,totalChecks:results.length,failures:failures.length,results};
const output=process.env.REPORT_PATH||'browser-smoke-report.json';await writeFile(output,JSON.stringify(report,null,2));console.log(JSON.stringify({base,testedAt:report.testedAt,htmlFiles:report.htmlFiles,totalChecks:report.totalChecks,failures:report.failures,report:output},null,2));if(failures.length)process.exit(1);
