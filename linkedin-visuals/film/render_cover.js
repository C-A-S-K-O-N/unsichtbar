// node film/render_cover.js  -> out/cover-three-worlds-4x5.png (1080x1350), -4x5@2x.png, -16x9.png (1920x1080)
const {chromium}=require('playwright'),path=require('path');
(async()=>{const out=path.join(__dirname,'..','out'),b=await chromium.launch();
for(const [h,w,hh,s,name] of [['P',1080,1350,1,'4x5'],['P',1080,1350,2,'4x5@2x'],['L',1920,1080,1,'16x9']]){
 const p=await b.newPage({viewport:{width:w,height:hh},deviceScaleFactor:s});
 await p.goto('file://'+__dirname+'/cover.html#'+h);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(900);
 await p.screenshot({path:out+'/cover-three-worlds-'+name+'.png'});await p.close();console.log('ok',name)}
await b.close()})();
