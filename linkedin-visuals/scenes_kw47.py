# KW 47: neun Video-Beiträge im Website-Stil (theme-web). Gleiches Gerüst: Hook-Überschrift,
# Motiv links, Abstimmung rechts (Diskussion), Pill «In die Kommentare», Linien mit blauen Punkten, Cursor.
from scenes import SCENES
import scenes_workspace_web as Wb

FT = {"seite": "digital-only.ch", "kyrill": "Kyrill Elsensohn · digital-only.ch", "bertan": "Bertan Findik · digital-only.ch", "cas": "Cas · digital-only.ch"}
OK = '<span style="color:#0d3b8b;font-weight:700">✓</span>'


def post(pid, konto, eye, h1, left, poll, o1, o2, pill, foot_l="Illustration", h1size=86, js="", left_top=470):
    body = f'''<canvas id="sph" class="abs" style="left:440px;top:360px;width:720px;height:720px"></canvas>
<div class="abs pill" data-a="pop" data-t=".2" style="right:80px;top:54px;font-size:18px;padding:13px 22px">{"digital-only.ch" if konto == "seite" else FT[konto].split(" · ")[0]}</div>
<div class="eyebrow" data-a="fade" data-t=".35" style="top:180px">{eye}</div>
<h1 data-words data-t=".5" style="top:228px;font-size:{h1size}px">{h1}</h1>
{Wb.lines([("M44 128 L44 190 C 60 380, 200 470, 330 " + str(left_top - 20), .9, 1.2), ("M840 470 C 960 520, 1000 600, 900 660", 5.4, .9), ("M80 1250 C 300 1300, 520 1260, 560 1190", 8.6, .9)])}
<div class="abs" style="left:80px;top:{left_top}px;width:480px">{left}</div>
<div class="abs wcard" data-a="up" data-t="5.6" data-d=".9" style="left:600px;top:680px;width:400px;padding:30px 30px">
 <div style="font:500 18px Inter;color:#0d3b8b">Ihre Meinung</div>
 <div style="font:700 30px/1.08 'Inter Tight';letter-spacing:-.03em;margin:8px 0 22px">{poll}</div>
 <div class="opt" id="o1" data-tap="7.0" style="margin-bottom:12px"><div id="b1" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(10,10,12,.08)"></div><span style="position:relative">{o1}</span></div>
 <div class="opt" id="o2" data-tap="7.8" style="border-color:#0d3b8b"><div id="b2" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(13,59,139,.16)"></div><span style="position:relative;color:#0d3b8b">{o2}</span></div>
 <div style="margin-top:14px;font:400 14px Inter;color:#9aa0aa">Illustration, keine echten Umfragewerte</div></div>
{Wb.dot(330, left_top - 20, 2.0)}{Wb.dot(900, 660, 6.2)}{Wb.dot(560, 1190, 9.4)}
<div class="abs" data-a="rise" data-t="8.8" style="left:80px;top:1130px;display:flex;align-items:center;gap:30px">
 <div class="pill" id="cta" data-tap="9.7" data-buzz="9.72">{pill} {Wb.ARROW}</div></div>
<div class="foot" data-a="fade" data-t="9.9"><span>{foot_l}</span><span>{FT[konto]}</span></div>{Wb.CUR}'''
    scene = Wb.SHARED_JS + '''
let K=null,C=[7.0,7.8,9.7];const b1=document.getElementById('b1'),b2=document.getElementById('b2');
''' + js + '''
window.SCENE=t=>{if(!K){const p1=pos(document.getElementById('o1')),p2=pos(document.getElementById('o2')),pc=pos(document.getElementById('cta'));
 K=[[6.4,1100,1340],[6.9,p1[0],p1[1]],[7.0,p1[0],p1[1]],[7.6,p2[0],p2[1]],[7.8,p2[0],p2[1]],[9.1,400,1260],[9.7,pc[0],pc[1]],[11,pc[0],pc[1]]]}
 base(t);const a=R(t,7.0,3.0),w=46+18*Math.sin(a*Math.PI*2.5)*Math.exp(-a*1.2);b1.style.width=(t<7?0:w)+'%';b2.style.width=(t<7.8?0:100-w-6)+'%';
 if(window.LOCAL)LOCAL(t)};'''
    SCENES[pid] = dict(theme="theme-web", grid=False, end=11, body=body, scene=scene)


def card(inner, t=1.5, pad="28px 30px", extra=""):
    return f'<div class="wcard" data-a="rise" data-t="{t}" style="padding:{pad};{extra}">{inner}</div>'


def lab(s):
    return f'<div style="font:500 18px Inter;color:#0d3b8b">{s}</div>'


def rowx(a, b, t, cls=""):
    return f'<div class="row {cls}" data-a="fade" data-t="{t}" data-buzz="{t + .1}" style="font:500 22px Inter;padding:15px 0;border-color:#eceef1"><span>{a}</span><span style="font-weight:700">{b}</span></div>'


# 1 Seite Fr 20.11. Plan B
items = ["Nummern auch offline", "Zweiter Kanal fürs Team", "Statusseite als Lesezeichen", "Abwesenheit vorbereitet"]
chk = ''.join(f'<div class="row" style="font:500 22px Inter;padding:15px 0;border-color:#eceef1"><span>{s}</span><span class="tick" data-k="{2.4 + i * .6:.1f}" data-a="fade" data-t="0" data-buzz="{2.42 + i * .6:.2f}" style="font:700 22px Inter;color:#c3c8cf">○</span></div>' for i, s in enumerate(items))
post("2026-11-20-fr", "seite", "Eine Woche nach dem Microsoft-Ausfall", "Hatten Sie einen<br>Plan B? Ehrlich.",
     card(lab("Plan B in einer Stunde") + '<div style="font:700 30px \'Inter Tight\';letter-spacing:-.03em;margin:4px 0 8px">Gilt bei jedem Anbieter</div>' + chk),
     "Hatten Sie letzte Woche einen Plan B?", "Ja, hatten wir", "Nein, ehrlich nicht", "Wechsel-Check · Kommentar",
     js="window.LOCAL=t=>{document.querySelectorAll('.tick').forEach(e=>{const on=t>=+e.dataset.k;e.textContent=on?'✓':'○';e.style.color=on?'#0d3b8b':'#c3c8cf'})};")

# 2 Kyrill Mi 18.11. Black Friday
post("2026-11-18-mi-kyrill", "kyrill", "Black Friday · 27. November", "Rabatt geben?<br>Lieber nicht.",
     card(lab("Ihr Black-Friday-Angebot") + '<div style="position:relative;display:inline-block;margin:14px 0 10px"><div id="pct" style="font:800 150px/1 \'Inter Tight\';letter-spacing:-.06em">−30 %</div>'
          '<div id="strike" style="position:absolute;left:-6%;top:52%;height:10px;width:0;background:#0d3b8b;border-radius:6px;transform:rotate(-8deg)"></div></div>'
          '<div data-a="fade" data-t="4.0" style="font:500 22px/1.4 Inter;color:#5b6270">Marge für Leute, die sowieso gekommen wären.</div>'),
     "Machen Sie bei Black Friday mit?", "Mitmachen", "Auslassen", "In die Kommentare",
     js="window.LOCAL=t=>{document.getElementById('strike').style.width=(112*eo(R(t,3.2,.5)))+'%';document.getElementById('pct').style.opacity=t>3.5?'.35':'1'};")

# 3 Kyrill Do 19.11. Eigener Name
post("2026-11-19-do-kyrill", "kyrill", "Google Ads", "Ihre Konkurrenz kauft<br>Ihren Namen?",
     card('<div style="display:flex;align-items:center;gap:12px;border:1.5px solid #d9dde3;border-radius:999px;padding:14px 20px;font:500 22px Inter"><span style="color:#8b919c">⌕</span><span id="q"></span><i id="qc" style="width:2px;height:24px;background:#0a0a0c;display:block"></i></div>'
          '<div data-a="rise" data-t="3.2" data-buzz="3.3" style="margin-top:18px;padding:16px 0;border-bottom:1px solid #eceef1"><div style="font:700 15px Inter;color:#0d3b8b">Anzeige · Mitbewerber</div><div style="font:600 23px Inter;margin-top:4px">Physio in Zug · Jetzt Termin</div></div>'
          '<div data-a="rise" data-t="3.8" style="padding:16px 0;opacity:.8"><div style="font:500 15px Inter;color:#5b6270">Ihr Eintrag</div><div style="font:600 23px Inter;margin-top:4px">Physio Muster · Zug</div></div>'),
     "Auf den eigenen Namen bieten?", "Pflicht", "Verschwendung", "In die Kommentare", foot_l="Fiktive Darstellung",
     js="const QQ='Physio Muster Zug';window.LOCAL=t=>{document.getElementById('q').textContent=QQ.slice(0,Math.round(QQ.length*R(t,1.9,1.0)));document.getElementById('qc').style.opacity=(Math.floor(t*3)%2)?'0':'1'};")

# 4 Kyrill Fr 20.11. Kundenwert
calc = ''.join(rowx(a, f'<span class="cnt" data-v="{v}" data-p="{p}" data-s="{s}" data-k="{k}">{p}0{s}</span>', k) for a, v, p, s, k in [
    ("Klick", 3, "CHF ", "", 2.0), ("Klicks pro Kunde", 25, "", "", 2.6), ("Kosten pro Kunde", 75, "CHF ", "", 3.2), ("Wert im 1. Jahr", 1200, "CHF ", "", 4.0)])
post("2026-11-20-fr-kyrill", "kyrill", "Google Ads", "Was ist ein Kunde<br>wert?",
     card(lab("Rechenbeispiel, keine echten Zahlen") + '<div style="font:700 30px \'Inter Tight\';letter-spacing:-.03em;margin:4px 0 8px">Klickpreis vs. Kundenwert</div>' + calc),
     "Kennen Sie Ihre zwei Zahlen?", "Ja", "Ehrlich gesagt nein", "In die Kommentare", foot_l="Rechenbeispiel",
     js="const CN=[...document.querySelectorAll('.cnt')];window.LOCAL=t=>{CN.forEach(e=>{const v=Math.round(+e.dataset.v*eo(R(t,+e.dataset.k,.8)));e.textContent=e.dataset.p+String(v).replace(/\\B(?=(\\d{3})+(?!\\d))/g,\"'\")+e.dataset.s})};")

# 5 Bertan Mi 18.11. «Das machen alle»
bub = ''.join(f'<div class="wcard" data-a="rise" data-t="{t}" data-buzz="{t + .1}" style="padding:20px 24px;margin-bottom:14px;border-radius:22px 22px 22px 6px"><div style="font:500 16px Inter;color:#0d3b8b">Gegenfrage {i + 1}</div><div style="font:700 26px/1.2 \'Inter Tight\';letter-spacing:-.02em;margin-top:4px">{s}</div></div>' for i, (s, t) in enumerate([("«Welche Betriebe genau? Darf ich einen anrufen?»", 2.4), ("«Und was hat es denen gebracht, in Zahlen?»", 3.4)]))
post("2026-11-18-mi-bertan", "bertan", "Aus dem Aussendienst", "«Das machen alle in<br>Ihrer Branche.»",
     bub + '<div data-a="pop" data-t="4.6" data-buzz="4.7" style="display:inline-block;border:1.5px solid #0a0a0c;border-radius:999px;padding:10px 20px;font:600 21px Inter;background:#fff">Belege: <b id="bel">?</b></div>',
     "Schon mal auf den Satz reingefallen?", "Ja", "Nie", "In die Kommentare", h1size=74,
     js="window.LOCAL=t=>{document.getElementById('bel').textContent=t>=4.9?'0':'?'};")

# 6 Bertan Do 19.11. Jahresvertrag
post("2026-11-19-do-bertan", "bertan", "Aus dem Aussendienst", "Jahresvertrag?<br>Erst die Zahlen.",
     card(lab("Werbevertrag") + '<div style="font:700 30px \'Inter Tight\';letter-spacing:-.03em;margin:4px 0 8px">Das Kleingedruckte</div>'
          + rowx("Laufzeit", "12 Monate", 2.0) + rowx("Kündigung", "3 Monate vorher", 2.5) + rowx("Sonst", "+ 1 Jahr", 3.0, "hl")
          + '<div class="row" style="font:600 22px Inter;padding:18px 0;border:0"><span>Monatlich kündbar</span><div id="sw" style="width:70px;height:40px;border-radius:20px;background:#d9dde3;position:relative"><i style="position:absolute;top:4px;left:4px;width:32px;height:32px;border-radius:50%;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.2);display:block"></i></div></div>'),
     "Was ist Ihnen lieber?", "Jahresvertrag", "Monatlich kündbar", "In die Kommentare", foot_l="Beispiel",
     js="window.LOCAL=t=>{const s=document.getElementById('sw'),p=spring(R(t,4.2,.4));s.style.background=t>=4.2?'#0d3b8b':'#d9dde3';s.firstChild.style.left=(4+30*p)+'px';document.querySelectorAll('.hl').forEach(e=>e.style.background=t>3.1&&t<4.2?'rgba(13,59,139,.08)':'transparent')};")

# 7 Bertan Fr 20.11. Nur bis Freitag
post("2026-11-20-fr-bertan", "bertan", "Black Friday · 27. November", "«Nur bis Freitag.»<br>Und am Montag?",
     card(lab("Angebot endet in") + '<div id="cd" style="font:800 96px/1 \'Inter Tight\';letter-spacing:-.04em;margin:10px 0 16px;font-variant-numeric:tabular-nums">02:13:59</div>'
          '<div data-a="pop" data-t="4.0" data-buzz="4.1" style="display:inline-block;border:1.5px solid #0d3b8b;color:#0d3b8b;border-radius:999px;padding:10px 20px;font:600 21px Inter">Mo 30.11. · neues Angebot?</div>'),
     "Wie reagieren Sie auf eine Frist?", "Sofort zuschlagen", "Ruhig warten", "In die Kommentare", foot_l="Illustration",
     js="window.LOCAL=t=>{let s=2*3600+13*60+59-Math.floor(t*7);s=Math.max(0,s);const h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;document.getElementById('cd').textContent=[h,m,x].map(v=>String(v).padStart(2,'0')).join(':')};")

# 8 Cas Mi 18.11. Antwort auf schlechte Bewertung
REPLY = "Danke für Ihre ehrliche Rückmeldung. Das tut uns leid. Rufen Sie mich gern direkt an, dann klären wir es."
post("2026-11-18-mi-cas", "cas", "Google-Bewertungen", "Die beste Werbung:<br>Ihre Antwort.",
     card('<div style="display:flex;justify-content:space-between"><span style="font:600 20px Inter">Kundin · vor 2 Tagen</span><span style="color:#0d3b8b;font-size:22px;letter-spacing:2px">★<span style="color:#d9dde3">★★★★</span></span></div>'
          '<div style="font:500 21px/1.4 Inter;margin:10px 0 16px">«Lange gewartet, niemand hat sich gemeldet.»</div>'
          '<div data-a="rise" data-t="2.6" style="border-left:3px solid #0d3b8b;padding:4px 0 4px 16px"><div style="font:600 16px Inter;color:#0d3b8b">Antwort des Inhabers</div><div id="rp" style="font:500 20px/1.4 Inter;margin-top:4px;min-height:84px"></div></div>'),
     "Auf schlechte Bewertungen…", "Antworten", "Ignorieren", "In die Kommentare", foot_l="Fiktive Bewertung",
     js=f"const RP={REPLY!r};window.LOCAL=t=>{{document.getElementById('rp').textContent=RP.slice(0,Math.round(RP.length*R(t,3.0,2.4)))}};")

# 9 Cas Do 19.11. Öffnungszeiten als Bild
post("2026-11-19-do-cas", "cas", "KI-Sichtbarkeit", "Öffnungszeiten als Bild?<br>Maschinen raten.",
     card(lab("Ihre Website") + '<div style="font:700 30px \'Inter Tight\';letter-spacing:-.03em;margin:4px 0 14px">Öffnungszeiten</div>'
          '<div style="position:relative;height:120px;border-radius:14px;overflow:hidden;background:#eef1f5"><canvas id="pix" width="420" height="120" style="width:100%;height:100%;display:block"></canvas><div id="scan" style="position:absolute;top:0;bottom:0;width:4px;background:#0d3b8b;box-shadow:0 0 18px #0d3b8b;left:0;opacity:0"></div>'
          '<div id="txt" style="position:absolute;inset:0;display:grid;place-items:center;font:700 30px Inter;opacity:0;background:#fff">Mo–Fr 08:00–18:00</div></div>'
          '<div class="row" style="font:500 21px Inter;padding:16px 0 4px;border:0"><span>KI liest</span><b id="ki">…</b></div>'),
     "Ihre Öffnungszeiten sind …", "Text", "Ein Bild", "In die Kommentare", h1size=74, foot_l="Illustration",
     js="""(()=>{const c=document.getElementById('pix').getContext('2d');let s=5;const r=()=>(s=(s*16807)%2147483647)/2147483647;for(let y=0;y<120;y+=12)for(let x=0;x<420;x+=12){const v=200+Math.floor(r()*50);c.fillStyle='rgb('+(v-40)+','+(v-30)+','+v+')';c.fillRect(x,y,12,12)}})();
window.LOCAL=t=>{const p=R(t,2.2,1.4);const sc=document.getElementById('scan');sc.style.opacity=p>0&&p<1?'1':'0';sc.style.left=(p*100)+'%';const fx=t>=4.6;
 document.getElementById('ki').textContent=t<3.6?'…':(fx?'Mo–Fr 08:00–18:00 ✓':'??:?? – ??:??');document.getElementById('ki').style.color=fx?'#0d3b8b':'#8b919c';document.getElementById('txt').style.opacity=String(eo(R(t,4.6,.4)))};""")
