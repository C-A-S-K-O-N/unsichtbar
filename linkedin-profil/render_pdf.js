// node linkedin-profil/render_pdf.js -> bertan-findik-profil.pdf
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(),p=await b.newPage();await p.goto('file://'+__dirname+'/bertan-findik-profil.html');
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
await p.pdf({path:__dirname+'/bertan-findik-profil.pdf',format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
 footerTemplate:'<div style="font:8px Inter,sans-serif;color:#8b919c;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>LinkedIn-Profil Bertan Findik · digitalONLY AG</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
 margin:{top:'16mm',bottom:'18mm',left:'16mm',right:'16mm'}});await b.close();console.log('ok')})();
