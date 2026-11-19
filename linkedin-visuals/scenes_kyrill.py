# Kyrill Mo 23.11.: Karriere-Beitrag im dunklen Premium-Stil (theme-gold) mit echtem Laufsteg-Foto.
# Das Foto liegt nur lokal in privat/ (nicht im Repo). Fehlt es, bleibt die Fläche dunkel.
from scenes import SCENES, ICON, rings

ICON.update({
    "cap": '<svg viewBox="0 0 24 24"><path d="M2 9.5L12 4.5l10 5-10 5z"/><path d="M6 11.5v4.8c3.2 2.6 8.8 2.6 12 0v-4.8"/><path d="M22 9.5v5.5"/></svg>',
    "talk": '<svg viewBox="0 0 24 24"><path d="M3 5h12v8H8l-5 3.5z"/><path d="M15 9h6v8.5L17.5 15H11v-2"/></svg>',
})


def world(icon, title, text, t):
    return (f'<div class="item" data-a="rise" data-t="{t}" data-buzz="{t + .45:.2f}" style="padding:22px 0">'
            f'<div class="tile">{ICON[icon]}</div><div><h3>{title}</h3><p style="font-size:19px;margin-top:4px">{text}</p></div></div>')


NODES = [("Heute", "Matura und Vertrieb"), ("Zuerst", "Sales und Business Development"), ("Langfristig", "Relationship Management im Private Banking")]
nodes = ''.join(
    f'<div class="node abs" data-k="{8.15 + i * .75:.2f}" style="left:{[0, 50, 100][i]}%;top:0;width:270px;transform:translateX({[0, -50, -100][i]}%);text-align:{["left", "center", "right"][i]}">'
    f'<div class="dot abs" style="top:0;{["left:0", "left:50%;margin-left:-11px", "right:0"][i]};width:22px;height:22px;border-radius:50%;border:2px solid rgba(226,192,122,.6);background:#141417"></div>'
    f'<div style="padding-top:38px"><div class="label mono" style="color:var(--gold);font-size:14px">{k}</div>'
    f'<div style="font:600 20px/1.25 Inter;margin-top:6px">{v}</div></div></div>' for i, (k, v) in enumerate(NODES))

BODY = f'''
<div class="eyebrow" data-a="fade" data-t=".15"><i></i>Maturand · Verkäufer · Model</div>
<h1 data-words data-t=".35">Ich will durch Chancen <span class="gold">Erfahrung sammeln.</span></h1>

<div class="abs" id="photo" data-a="up" data-t="1.3" data-d=".95" style="left:80px;top:440px;width:340px;height:600px;border-radius:26px;overflow:hidden;border:1.5px solid rgba(226,192,122,.55);box-shadow:0 40px 90px rgba(0,0,0,.65),0 0 60px rgba(226,192,122,.12);background:#121215">
 <div style="position:relative;height:531px;overflow:hidden">
  <img id="pimg" src="../privat/kyrill-laufsteg.jpg" style="width:100%;height:100%;object-fit:cover;transform-origin:50% 22%;display:block">
  <div id="flash" class="abs" style="inset:0;background:#fff;opacity:0"></div>
  <div id="sheen" class="abs" style="top:-20%;bottom:-20%;width:46%;left:-60%;background:linear-gradient(100deg,transparent,rgba(255,236,190,.38),transparent);transform:skewX(-14deg)"></div></div>
 <div style="padding:11px 20px 0;border-top:1px solid rgba(226,192,122,.35)">
  <div class="label mono" style="color:var(--gold);font-size:13px;letter-spacing:.18em">Oktober · Laufsteg</div>
  <div style="font:600 21px Inter;margin-top:4px">Jüngstes Model für FDLA</div></div>
</div>
{rings(342, 380, 160, 3.0, "rgba(226,192,122,.55)")}
<div class="abs" data-a="pop" data-t="2.6" data-buzz="2.78" style="left:372px;top:410px;width:100px;height:100px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#f7e3b0,#c9a466 70%);color:#16130d;display:grid;place-content:center;text-align:center;box-shadow:0 18px 40px rgba(0,0,0,.55),0 0 30px rgba(226,192,122,.45)">
 <div style="font:800 23px/1 'Inter Tight';letter-spacing:-.02em">Paris</div><div style="font:700 10px/1.2 'JetBrains Mono';letter-spacing:.08em;text-transform:uppercase;margin-top:4px">Fashion<br>Week</div></div>

<div class="abs" style="left:500px;right:80px;top:432px">
 {world("cap", "Klassenzimmer", "Maturand · Kantonsschule Uetikon am See", 3.4)}
 {world("talk", "Kundengespräch", "Verkäufer · Verling Solutions, digitalONLY", 3.9)}
 {world("star", "Laufsteg", "Model · Paris Fashion Week", 4.4)}
</div>

<div class="abs card" data-a="right" data-t="5.0" style="left:500px;right:80px;top:782px;height:258px;padding:30px 30px">
 <div class="row" style="padding:13px 0"><span style="color:var(--muted)">Nicht jedes Casting</span><span class="nein q" data-a="slam" data-t="5.5" data-d=".3" data-buzz="5.6" style="padding:0 14px;position:relative">Nein<i class="strike"></i></span></div>
 <div class="row" style="padding:13px 0"><span style="color:var(--muted)">Nicht jedes Kundengespräch</span><span class="nein q" data-a="slam" data-t="5.9" data-d=".3" data-buzz="6.0" style="padding:0 14px;position:relative">Nein<i class="strike"></i></span></div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:22px;gap:14px">
  <div data-a="fade" data-t="6.6" style="font:600 23px/1.2 Inter">Kein Grund<br>aufzuhören.</div>
  <div class="chip" data-a="pop" data-t="7.0" data-tap="7.25" data-buzz="7.27" style="background:linear-gradient(180deg,#f3d697,#c9a466);color:#16130d;font-weight:700;overflow:hidden;white-space:nowrap">Consistency is key.</div>
 </div>
</div>

<div class="abs card" data-a="rise" data-t="7.6" style="left:80px;right:80px;top:1066px;height:176px;padding:24px 34px">
 <div class="label mono" style="color:var(--muted);font-size:14px">Nach der Matura</div>
 <div class="abs" style="left:45px;right:45px;top:66px;height:2px;background:rgba(255,255,255,.12)"><div id="fill" style="height:100%;width:0;background:linear-gradient(90deg,#b8935a,#f3d697);box-shadow:0 0 14px rgba(226,192,122,.7)"></div></div>
 <div class="abs" id="lastring" style="right:34px;top:44px;width:44px;height:44px;margin-right:-11px"><div class="abs" data-rings="9.7" style="inset:0">{''.join('<div class="ring" style="inset:0;border-color:rgba(226,192,122,.6)"></div>' for _ in range(3))}</div></div>
 <div class="abs" style="left:34px;right:34px;top:56px">{nodes}</div>
</div>

<div class="foot" data-a="fade" data-t="9.8"><span>Laufsteg-Foto: Yangzi LIU</span><span>Kyrill Elsensohn · digital-only.ch</span></div>'''

SCENE = '''
const pimg=document.getElementById('pimg'),flash=document.getElementById('flash'),sheen=document.getElementById('sheen'),fill=document.getElementById('fill');
const strikes=[...document.querySelectorAll('.strike')],nodes=[...document.querySelectorAll('.node')];
strikes.forEach(s=>{s.style.cssText='position:absolute;left:8%;top:50%;height:3px;width:0;background:var(--ink);border-radius:2px;transform:rotate(-12deg)'});
window.SCENE=t=>{
 pimg.style.transform='scale('+(1.08-.08*eo(R(t,1.3,5)))+')';
 const f=t-1.95;flash.style.opacity=f<0||f>.5?0:(.75*Math.exp(-f*9)).toFixed(3);
 sheen.style.left=(-60+180*eo(R(t,2.0,1.1)))+'%';
 strikes.forEach((s,i)=>{s.style.width=(84*eo(R(t,6.25+i*.12,.3)))+'%'});
 document.querySelectorAll('.nein').forEach((n,i)=>{const k=R(t,6.25+i*.12,.3);n.style.color=k>0?'#c9c4b8':'';n.style.background=k>0?'rgba(255,255,255,.06)':'';n.style.borderColor=k>0?'rgba(255,255,255,.18)':''});
 const p=eo(R(t,8.0,1.7));fill.style.width=(p*100)+'%';
 nodes.forEach((n,i)=>{const d=n.querySelector('.dot'),on=t>=+n.dataset.k,b=buzzAt(t,+n.dataset.k);
  d.style.background=on?'#f3d697':'#141417';d.style.borderColor=on?'#f3d697':'rgba(226,192,122,.6)';d.style.boxShadow=on?'0 0 18px rgba(243,214,151,.85)':'none';
  n.style.translate=b?b+'px 0':'0 0';n.style.opacity=String(.45+.55*(on?1:0))});
};'''

SCENES["2026-11-23-mo-kyrill-karriere"] = dict(theme="theme-gold", grid=False, end=10.5, body=BODY, scene=SCENE)
