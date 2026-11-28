// node linkedin-profil/render.js -> banner-bertan.png (1584x396) und banner-bertan@2x.png
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();for(const s of [1,2]){const p=await b.newPage({viewport:{width:1584,height:396},deviceScaleFactor:s});
await p.goto('file://'+__dirname+'/banner-bertan.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(700);
await p.screenshot({path:__dirname+'/banner-bertan'+(s===2?'@2x':'')+'.png'});await p.close()}await b.close();console.log('ok')})();
