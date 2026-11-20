// node film/render_film.js still <t> <out.png> | video [audio.wav]  -> out/film-beyond-the-classroom.mp4
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),{execFileSync}=require('child_process');
(async()=>{const [,,mode,a1,a2]=process.argv;const dir=path.join(__dirname,'..');
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
await p.goto('file://'+__dirname+'/beyond.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1200);
if(mode==='still'){for(const t of a1.split(',')){await p.evaluate(t=>render(t),+t);await p.screenshot({path:a2.replace('%t',t),type:a2.endsWith('.jpg')?'jpeg':'png'})}}
else{const fd=dir+'/frames/film';fs.rmSync(fd,{recursive:true,force:true});fs.mkdirSync(fd,{recursive:true});const fps=30,n=Math.round(45*fps);
 for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:fd+'/f'+String(i).padStart(5,'0')+'.jpg',type:'jpeg',quality:94});if(i%150===0)console.log('frame',i,'/',n)}
 const base=dir+'/out/film-beyond-the-classroom',aud=a1&&fs.existsSync(a1)?['-i',a1]:['-f','lavfi','-i','anullsrc=r=48000:cl=stereo'];
 const inp=['-hide_banner','-loglevel','error','-y','-framerate','30','-i',fd+'/f%05d.jpg',...aud,'-t','45','-vf','noise=alls=4:allf=t,format=yuv420p','-c:v','libx264','-preset','slow','-profile:v','high','-tune','grain'];
 // Master zum Posten (hohe Qualität) und Web-Fassung unter 15 MB (Vorschau in der Zentrale)
 execFileSync('ffmpeg',[...inp,'-crf','19','-maxrate','14M','-bufsize','28M','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','-shortest',base+'.mp4']);
 const lg=dir+'/build/x264-pass';
 execFileSync('ffmpeg',[...inp,'-b:v','2200k','-pass','1','-passlogfile',lg,'-an','-f','mp4','/dev/null']);
 execFileSync('ffmpeg',[...inp,'-b:v','2200k','-pass','2','-passlogfile',lg,'-c:a','aac','-b:a','128k','-ar','48000','-movflags','+faststart','-shortest',base+'-web.mp4']);
 const out=base+'.mp4';
 fs.rmSync(fd,{recursive:true,force:true});console.log('ok',out)}
await b.close()})();
