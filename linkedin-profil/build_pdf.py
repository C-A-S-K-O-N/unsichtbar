# Baut das Profil-Dokument für Bertan Findik als HTML (danach render_pdf.js -> PDF). Texte in texte/*.txt (durch den Humanizer gelaufen).
import html, os, re
H = os.path.dirname(os.path.abspath(__file__))
T = lambda n: open(os.path.join(H, "texte", n + ".txt")).read().strip()
def box(t, n=True):
    e = html.escape(t)
    e = re.sub(r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", lambda m: '<span class="ph">{' + m.group(1) + '}</span>', e)
    return f'<div class="copy">{e}</div>' + (f'<div class="meta">{len(t)} Zeichen</div>' if n else "")
ROWS = [("Headline", 12, 10, 11), ("Info, erste zwei Zeilen", 10, 9, 9), ("Info, Rest", 10, 7, 9), ("Im Fokus", 8, 3, 8),
        ("Titelbild", 6, 6, 6), ("Profilfoto", 6, 4, 5), ("Aktuelle Position", 10, 5, 9), ("Berufserfahrung", 8, 5, 7),
        ("Kenntnisse, Top 3", 6, 4, 5), ("Empfehlungen", 8, 0, 6), ("Aktivität letzte 7 Tage", 10, 0, 10), ("Kontakt und eigene URL", 6, 6, 6)]
rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in ROWS)
tot = [sum(r[i] for r in ROWS) for i in (1, 2, 3)]
doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>LinkedIn-Profil Bertan Findik</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Inter+Tight:wght@700;800&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:16mm 16mm 18mm}}
*{{box-sizing:border-box}} body{{font:400 10.5pt/1.5 Inter,sans-serif;color:#0a0a0c;margin:0;-webkit-font-smoothing:antialiased}}
.top{{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:1px solid #e3e3e3;padding-bottom:10px}}
.top img{{height:30px}} .eye{{color:#0d3b8b;font:500 10pt Inter}}
h1{{font:800 26pt/1.05 'Inter Tight',Inter,sans-serif;letter-spacing:-.03em;margin:6px 0 4px}}
.lead{{color:#5b6270;margin:0}}
h2{{font:700 14pt 'Inter Tight',Inter,sans-serif;letter-spacing:-.02em;margin:20px 0 6px;break-after:avoid}}
h2 b{{color:#0d3b8b;margin-right:8px}} h3{{font:600 10.5pt Inter;margin:12px 0 4px;break-after:avoid}}
.copy{{white-space:pre-wrap;background:#f6f7f9;border:1px solid #e3e6ea;border-left:3px solid #0d3b8b;border-radius:6px;padding:10px 12px;font-size:10pt;break-inside:avoid}}
.meta{{font-size:8.5pt;color:#8b919c;margin:3px 0 8px}} .ph{{background:#fff3c4;border-radius:3px;padding:0 2px}}
.banner{{width:100%;border:1px solid #e3e3e3;border-radius:6px;margin-top:14px}}
.cap{{font-size:8.5pt;color:#8b919c}} ul{{margin:4px 0;padding-left:18px}} li{{margin:2px 0}}
.note{{background:#eef3fb;border-radius:6px;padding:8px 12px;font-size:9.5pt;margin:8px 0}}
table{{width:100%;border-collapse:collapse;font-size:9.5pt;break-inside:avoid}} th,td{{text-align:left;padding:5px 6px;border-bottom:1px solid #eceef1}}
th{{font-weight:600;color:#5b6270}} td:nth-child(n+2),th:nth-child(n+2){{text-align:right;width:15%}} tr.t td{{font-weight:700;border-top:2px solid #0a0a0c}}
.pb{{break-before:page}} .keep{{break-inside:avoid}}
</style></head><body>
<div class="top"><div><div class="eye">LinkedIn-Profil · Stand 24. November 2026</div><h1>Bertan Findik</h1>
<p class="lead">Partner, digitalONLY AG, Zug. Kopierfertige Texte in der Reihenfolge, die am meisten bringt.</p></div><img src="logo.png"></div>
<div class="note"><span class="ph">{{…}}</span> ist ein Platzhalter: nur mit echten, freigegebenen Angaben füllen. Alle Texte sind durch den Humanizer gelaufen.
Nichts davon ist bei LinkedIn gespeichert, jeder Abschnitt wird von Hand eingefügt.</div>
<img class="banner" src="banner-bertan.png"><div class="cap">Titelbild 1584 × 396 (Datei banner-bertan.png). Unten links bleibt Platz für das Profilfoto.</div>

<h2><b>1</b>Headline, eine Variante wählen</h2>
<h3>A · mit Aussendienst-Erfahrung</h3>{box(T('h1'))}
<h3>B · mit Kontaktweg</h3>{box(T('h2'))}
<h3>C · sobald die Zahl feststeht</h3>{box(T('h3'))}

<h2 class="pb"><b>2</b>Info</h2>
<p class="meta" style="margin-top:0">Die ersten zwei Sätze sind alles, was man vor «mehr anzeigen» sieht. Humanizer 85/100, bestanden.</p>
{box(T('info2'))}

<h2><b>3</b>Im Fokus, drei Elemente</h2>
<ul><li><b>Bester Beitrag:</b> «3 Fragen an jeden Werbeverkäufer» (Entwurf in der Zentrale), nach dem Posten anheften.</li>
<li><b>Beleg:</b> Fallbeispiel mit echter Zahl als Link oder PDF, sobald ein Kunde die Nennung freigegeben hat.</li>
<li><b>Kontakt:</b> Link auf die Kontaktseite von digital-only.ch.</li></ul>

<h2><b>4</b>Berufserfahrung</h2>
<div class="keep"><h3>Partner · digitalONLY AG · Zug · seit <span class="ph">{{Monat Jahr}}</span></h3>
<p class="meta" style="margin-top:0">Mit der Unternehmensseite digitalONLY AG verknüpfen.</p>{box(T('pos1'))}</div>
<div class="keep"><h3>Digital Marketing Consultant, Aussendienst · <span class="ph">{{Arbeitgeber}}</span> · 2021 bis <span class="ph">{{Jahr}}</span></h3>
{box(T('pos2'))}<p class="meta">Den früheren Arbeitgeber neutral nennen, nie bewerten.</p></div>

<h2><b>5</b>Kenntnisse, die Top 3 anheften</h2>
<p>Google Business Profile (Google-Unternehmensprofil) · Local SEO · Google Ads. Kunden und Kollegen um Bestätigung dieser drei bitten.</p>
<h2><b>6</b>Dienstleistungen</h2>
<p>Suchmaschinenoptimierung (SEO), Suchmaschinenmarketing (SEM), Digitales Marketing, Webdesign. Region: Zug, Zürich, Schweiz.</p>
<h2><b>7</b>Kontakt und eigene URL</h2>
<p>Eigene URL, z. B. linkedin.com/in/bertan-findik (falls frei). In den Kontaktinfos: Website digital-only.ch und die geschäftliche E-Mail-Adresse.</p>
<h2><b>8</b>Profilfoto</h2>
<p>Gesicht füllt etwa 60 % des Bildes, Augen sichtbar, ruhiger Hintergrund, nicht älter als zwei Jahre.</p>

<h2><b>9</b>Empfehlungen: drei zufriedene Kunden anfragen</h2>{box(T('empf'))}

<h2><b>10</b>Punkte: was die Texte bringen und was noch fehlt</h2>
<table><tr><th>Bereich</th><th>Max.</th><th>Nach dem Einfügen</th><th>Mit Zahlen, Empfehlungen, Aktivität</th></tr>{rows}
<tr class="t"><td>Total</td><td>{tot[0]}</td><td>{tot[1]}</td><td>{tot[2]}</td></tr></table>
<p class="meta">Schätzung nach der 100-Punkte-Rubrik des LinkedIn-Agents, ohne das heutige Profil gesehen zu haben. Profilfoto je nach Bild.</p>
<h3>Noch offen</h3>
<ul><li>Schreibweise des Namens (in der Zentrale: Findik)</li><li>Genauer Titel und Startdatum bei digitalONLY</li>
<li>Früherer Arbeitgeber, Dauer und was davon erzählt werden darf</li><li>Echte Zahlen für Headline C, Info und Positionen, mit Kundenfreigabe</li>
<li>Drei Empfehlungen, ein angehefteter Beitrag, Beiträge in den letzten sieben Tagen (Entwürfe liegen in der Zentrale)</li></ul>
</body></html>"""
open(os.path.join(H, "bertan-findik-profil.html"), "w").write(doc)
print("ok", tot)
