# BEYOND THE CLASSROOM · persönlicher Markenfilm

*Three worlds. One mindset.* Kyrill Elsensohn, 18, Maturand, Vertrieb, Model.
LinkedIn, 4:5, 1080 × 1350, 30 fps, 45 s, H.264 + AAC, -16 LUFS.

Dateien in diesem Ordner:

| Datei | Zweck |
|---|---|
| `beyond.html` | Der Film als Bildwerk: jede Einstellung, jede Schrift, jede Bewegung, Zeit `t` in Sekunden |
| `audio.py` | Originalmusik (MIDI, FluidSynth, FluidR3_GM, MIT-Lizenz) und Geräusche (synthetisch), Mischung, Lautheit |
| `render_film.js` | Bild für Bild rendern, Filmkorn, Ton anlegen, MP4 schreiben |
| `prep_media.py` | Datenschutz-Fassungen der Fotos, Laufsteg-Video als 60-fps-Einzelbilder (Zeitlupe) |

Fotos liegen nur lokal in `../privat/` und werden nicht eingecheckt. Ohne sie bleiben die Fotoflächen schwarz.

```
python3 film/prep_media.py <upload-ordner>          # -> privat/*.jpg, build/vid/*.jpg
python3 film/audio.py                                # -> build/film-audio.wav
node film/render_film.js video build/film-audio.wav  # -> out/film-beyond-the-classroom.mp4
node film/render_film.js still 20.9 /pfad/%t.png     # Einzelbild zu einer Zeit
```

---

## 1. Storyboard

Schnitt im Takt: 80 BPM, ein Schlag = 0,75 s, ein Takt = 3 s. Jeder Schnitt liegt auf einem Schlag.

| Zeit | Kapitel | Bild | Material | Bewegung | Ton |
|---|---|---|---|---|---|
| 0,00–2,25 | I Kontrast | Notizbuch im Tageslicht, liniertes Papier, Handschrift «Zuhören. Fragen stellen.» schreibt sich | illustrativ (gebaut) | Schub 1,00→1,06, Lichtstreifen wandern | Klavier solo, Füller auf Papier |
| 2,25–4,50 | I | Am Tisch: Laptop, handgeschriebenes Gesprächsskript, Glasfront (Text oben) | echtes Foto F4 | Schub 1,36→1,43 nach rechts (Kollege ausserhalb) | Luftzug beim Schnitt |
| 4,50–6,00 | I | Laufsteg-Totale: Kyrill kommt auf die Kamera zu, Spot öffnet sich aus dem Schwarz | echtes Video V1 (Echtzeit) | Lichtkegel 0→voll in 0,6 s | weicher Tiefton |
| 6,00–7,50 | I | Titelkarte Mitternachtsblau: «18 Jahre. Drei Welten.» | Grafik | Abblende 0,45 s | Tiefton, Streicher setzen ein |
| 7,50–11,25 | II Der Raum | Lichtschlitz wie eine Tür, öffnet auf das Sitzungszimmer, wir gehen hinein | echtes Foto | Schlitz, dann Öffnung, Schub 1,04→1,20 (POV) | Türluft, fünf Schritte |
| 11,25–14,25 | II | Meetingraum mit Kyrills Arbeitsplatz: Laptop, Tablet, Notizen, Lampe | echtes Foto F5 | Schwenk von rechts nach links | Raumton |
| 14,25–16,50 | III Paris | Kamerafahrt von den Schuhen über die Beine zum Oberkörper | echtes Video V1 (Echtzeit) | Auslöser-Blitz | Pauke, Auslöser, Publikum |
| 16,50–18,75 | III | Nahaufnahme Gesicht, «eingefroren» durch den Auslöser | echtes Foto F6 | langsamer Schub 1,00→1,07 | Auslöser, ferne Kameras |
| 18,75–22,50 | III | Editorial-Doppelseite: Text links, Foto als Abzug rechts, Lichtkegel | echtes Foto, ungeschnitten mit Wasserzeichen | Abzug zieht leicht zurück, Kegel atmet | Höhepunkt Musik setzt an |
| 22,50–24,75 | IV Verbindung | Diptychon: links Laufsteg-Totale in Zeitlupe, rechts Sitzungszimmer, goldene Haarlinie zeichnet sich | V1 (0,75×) und F2 | Hälften gleiten gegeneinander | Luftzug |
| 24,75–27,75 | IV | Objektiv: Iris öffnet auf sein Gesicht in Zeitlupe, im Kreis Überblendung ins Sitzungszimmer (Kamera → Blickkontakt) | V1 (0,55×) und F2 | Iris 0→100 %, Skalenring dreht | Fokusring-Klicks |
| 27,75–30,00 | IV | Rückansicht: Kyrill geht den Laufsteg hinunter, Lichtband wischt in den Meetingraum mit der leuchtenden Lampe (Spot → Geschäftsumfeld) | V1 (Echtzeit) und F5 | Lichtwischer 0,9 s | Schimmer |
| 30,00–36,00 | V Haltung | Architektur-Korridor in feinen Linien, wir gehen ruhig vorwärts, Abblende ins Dunkel | illustrativ (gebaut) | Linien kommen auf uns zu | nur Streicher und Klavier, Schritte mit Hall, Rückwärts-Anschwellen |
| 36,00–45,00 | VI Nächstes Kapitel | Zürich in der Dämmerung: Alpen, St. Peter, Fraumünster, Grossmünster, See mit Spiegelung | illustrativ (gebaut) | Kontur zeichnet sich in Gold, Schub 1,00→1,05 | Pauke, Auflösung nach F-Dur, Schlussakkord bei 42,0 |
| 44,10–45,00 | VI | Abblende ins Schwarz | | | Ausklang |

Durchgehend: oben links «BEYOND THE CLASSROOM», oben rechts Kapitelziffer I bis VI, goldene Haarlinie. Feines Filmkorn, leichte Vignette, entsättigte, kühle Farbgebung mit warmem Weiss.

## 2. Shotlist

### Vorhanden und verwendet

| # | Material | Wo im Film | Hinweis |
|---|---|---|---|
| F1 | Laufsteg Paris, FDLA (Foto Yangzi LIU) | III (Editorial-Doppelseite) | Fotonachweis am Abzug |
| F2 | Sitzungszimmer (ohne Personen) | II, IV | |
| F3 | Arbeitsplatz Restaurant, Laptop | nicht mehr verwendet | nur die Fassung mit unkenntlichem Bildschirm (Kundendaten) |
| F4 | Am Tisch mit Laptop und Gesprächsskript | I | Kollege links unkenntlich und ausserhalb des Ausschnitts, Skript leicht unscharf (nicht lesbar) |
| F5 | Meetingraum mit Arbeitsplatz und Lampe | II, IV | Notizen und Tablet leicht unscharf |
| F6 | Laufsteg nah (Screenshot) | III | Fotograf noch offen, Nachweis ergänzen |
| V1 | Laufsteg-Video Paris (Bildschirmaufnahme, 7,5 s: Totale, Fahrt Füsse→Gesicht, Rückansicht) | I, III, IV | Querformat-Ausschnitt ohne Balken, 60 fps mit Bewegungsinterpolation für Zeitlupe, Originalton nicht verwendet. Quelle und Nutzungsrecht noch offen (`CREDIT_VIDEO` in `beyond.html`) |

### Fehlt, würde den Film auf Kinoniveau heben (Dreh mit Handy in 4K reicht)

| # | Einstellung | Kapitel | Hinweise zum Dreh |
|---|---|---|---|
| D1 | Nahaufnahme Notizbuch und Stift im Schulzimmer, Fensterlicht | I | 3 s, Stativ, 24 oder 30 fps, eigene Handschrift |
| D2 | Kyrill betritt einen Besprechungsraum, von hinten, Tür geht auf | II | Gimbal, langsam, Gegenlicht |
| D3 | Handschlag, Nahaufnahme | II | nur Hände, kein Logo, keine erkennbare Bank |
| D4 | Blickkontakt am Tisch, Halbnah, Gegenüber unscharf | II, IV | mit Einverständnis des Gegenübers |
| D5 | Backstage-Clips Paris (Laufsteg-Video ist jetzt drin) | III | nur wenn vorhanden, nichts nachstellen |
| D6 | Gang durch moderne Architektur (z. B. Europaallee) | V | ohne Firmenschilder im Bild |
| D7 | Kyrill schaut auf Zürich (Lindenhof, Polyterrasse oder Zürichhorn), blaue Stunde | VI | von hinten oder im Profil |
| D8 | Zürich Skyline, blaue Stunde, 5 s statisch | VI | ersetzt die gezeichnete Stadt |

Fehlende Einstellungen sind im aktuellen Film bewusst als klar erkennbare Illustration gelöst (Notizbuch, Korridor, gezeichnete Stadt). Es gibt kein erzeugtes Gesicht und keine nachgestellte Szene.

## 3. Typografie und Bewegung

**Farben:** Mitternachtsblau `#101B2B`, Anthrazit `#111315`, Elfenbein `#F2EFE8`, Champagner-Gold `#C3A77A` (nur Haarlinien, Kapitelziffer, je ein Akzentwort), Steingrau `#85888C`.

**Schriften:**
- Aussagen: Cormorant Garamond 500, Akzentzeile kursiv 400, 70 bis 104 px, Laufweite -0,01 em, Zeilenabstand 1,02.
- Kennzeichnung: Inter 500, 15 px, Versalien, Laufweite 0,42 em, Steingrau.
- Fliesstext: Inter 300/400, 30 px.
- Handschrift im Notizbuch: Caveat 500.

**Raster und Ränder:** 72 px links und rechts. Aussagen unten zwischen 860 und 1130 px, in Kapitel V und VI oben bis mittig. Die unteren 150 px bleiben frei für die LinkedIn-Bedienelemente.

**Text-Bewegung:** Jede Zeile steigt aus einer Maske (105 % → 0 %, 1,0 s, ease-out kubisch). Unschärfe 6 px → 0, zweite Zeile 0,14 s versetzt, im Kapitel III 0,72 s. Abgang: 0,3 s Abblende. Kein Hüpfen und kein Überschwingen.

**Kamera:** Nur langsame Schübe (höchstens 8 % pro Einstellung), sanfte Sinus-Kurve, Parallaxe nur im Diptychon und in der Stadt.

**Übergänge:** Harte Schnitte auf dem Schlag. Dazu vier motivierte Übergänge: Lichtschlitz/Tür (II), Auslöser-Blitz (III, 0,2 s, 55 %), Iris (IV), Lichtwischer (IV). Abblenden nur vor Kapitel II, ins Dunkel am Ende von V und am Schluss.

**Nachbearbeitung:** Entsättigung 0,72, Kontrast 1,06, Helligkeit 0,82, Sepia 0,08. Verlauf Mitternachtsblau oben, Anthrazit unten. Vignette 50 %, Filmkorn zeitlich (ffmpeg `noise=alls=6:allf=t`).

## 4. Ton

**Musik (Original, 80 BPM, d-Moll → F-Dur):** Konzertflügel, Streicher-Ensemble, Cello, Pauke, ganz leises Schlagwerk (Bassdrum auf 1 und 3, Shaker).

| Takt | Zeit | Akkord | Was passiert |
|---|---|---|---|
| 1–2 | 0–6 | Dm, B | Klavier allein, Viertel, viel Raum |
| 3–4 | 6–12 | F, C | Streicher atmen ein, Klavier in Achteln |
| 5–8 | 12–24 | Dm, B, F, C | Cello, ab 15 s Puls, Pauke bei 14,25 (Paris) |
| 9–10 | 24–30 | Dm, B | Höhepunkt: Melodie im Klavier, volle Streicher, Tom-Wirbel |
| 11–12 | 30–36 | F, C | Rückzug: kein Schlagwerk, Klavier spärlich |
| 13–15 | 36–45 | B, C, F | Auflösung nach F-Dur, Melodie steigt, Pauke bei 36,0 und 42,0, Schlussakkord klingt aus |

**Geräusche (synthetisch, leise unter der Musik):** Raumton durchgehend (-50 dBFS), Füller auf Papier (0,3–2,1 s), Luftzüge an den Schnitten, Türluft und fünf Schritte (7,5–11), Auslöser auf jedem Paris-Schnitt mit fernen Kameras und Publikum (14,25–22,5), Fokusring-Klicks (24,8), Lichtschimmer (28,5), Schritte mit Hall im Korridor (30–35), Rückwärts-Anschwellen in Kapitel VI, tiefe Akzente bei 4,5, 6,0 und 36,0.

**Mischung:** Musik führt (Spitze -6 dB vor der Lautheitsanpassung), Geräusche liegen deutlich darunter. Ausblende 1,4 s. Lautheit -16 LUFS integriert, Spitze -1,5 dBTP, zwei Durchgänge, linear.

Der Film funktioniert vollständig stumm: Jede Aussage steht im Bild.

## 5. Bildschirmtexte und Timing

| Ein | Aus | Text | Stil |
|---|---|---|---|
| 0,45 | 2,25 | Im Klassenzimmer: / *Maturand.* | Serif 78, Tinte (auf Papier) |
| 2,55 | 4,50 | Im Kundengespräch: / *Vertrieb.* | Serif 78, oben im Bild |
| 4,85 | 6,00 | Auf dem Laufsteg: / *Paris.* | Serif 78 |
| 6,25 | 7,50 | 18 Jahre. / *Drei Welten.* | Serif 96, zentriert, zweite Zeile Gold |
| 8,70 | 11,00 | Oft der Jüngste / im Raum. | Serif 78 |
| 11,75 | 14,00 | Aber immer bereit, / *dazuzulernen.* | Serif 78 |
| 14,75 | 16,50 | Paris / *Fashion Week* | Serif 104 |
| 17,00 | 18,75 | FDLA | Inter 54, Laufweite 0,5 em |
| 19,00 | 22,30 | PARIS · OKTOBER | Kennzeichnung |
| 19,20 | 22,30 | Eine Chance. / Ein Vertrauen. / *Eine Erfahrung.* | Serif 62, je 0,72 s versetzt, letzte Zeile Gold |
| 23,00 | 24,75 | First impressions matter. | Serif 70, zentriert |
| 25,35 | 27,60 | Communication builds trust. | Serif 70, zentriert |
| 28,20 | 30,00 | Consistency creates progress. | Serif 70, zentriert |
| 30,60 | 32,75 | Not every opportunity / becomes a yes. | Serif 78, zentriert |
| 33,30 | 35,30 | But every experience / *moves me forward.* | Serif 78, zentriert |
| 36,45 | 41,00 | NEXT CHAPTER | Kennzeichnung, Gold |
| 36,85 | 41,00 | Sales. Business Development. / *Relationship Management.* | Serif 74, 0,8 s versetzt |
| 38,45 | 41,00 | Exploring opportunities in / Private Banking & Wealth Management. | Inter 30 |
| 41,35 | 45,00 | *Just getting started.* | Serif 100, kursiv, zentriert |
| 42,40 | 45,00 | KYRILL ELSENSOHN / BEYOND THE CLASSROOM · THREE WORLDS. ONE MINDSET. | Kennzeichnung |
| 18,75 | 22,50 | FOTO: YANGZI LIU (am Abzug) | Inter 14, Versalien |
| bei V1 | | Video-Nachweis, sobald die Quelle bestätigt ist | Inter 14, Versalien |

Die Sprachen sind wie im Briefing: Kapitel I bis III Deutsch, IV bis VI Englisch.

## 6. Schnittplan (für Premiere, Resolve oder CapCut)

```
Spur   0      7.5        14.25        22.5         30        36            45
V3     [Texte nach Tabelle 5, Kapitelziffer, Haarlinie, Fotonachweis F1 ..................]
V2     [Lichtschlitz]   [Blitz][Blitz][Blitz]  [Iris][Wischer]       [Abblende ins Schwarz]
V1     Notiz|F2|F1|Karte|F2 (POV)|F3|F1 Beine|F1 Gesicht|F1 Abzug|Diptych|Linse|Spot|Korridor|Zürich
A1     Musik ----------------------------------------------------------------------------->
A2     Füller  Luft     Schritte    Auslöser + Publikum   Klicks Schimmer  Schritte  Anschwellen
A3     Raumton -------------------------------------------------------------------------->
Marker Schnitte auf jedem Schlag (0,75 s), Pauke 14,25 · 36,0 · 42,0
```

Export: H.264 High, CRF 17, yuv420p, 1080 × 1350, 30 fps, AAC 192 kbit/s, 48 kHz, faststart.

## 7. Wenn gedreht wird: Anweisungen und Prompts

**Schnittregel:** Echte Aufnahmen ersetzen die illustrierten Einstellungen 1:1 (D1 → Notizbuch, D2/D3 → Kapitel II, D6 → Korridor, D7/D8 → Zürich). Timing, Texte und Musik bleiben gleich.

**Prompts für neutrales B-Roll aus einem Video-Generator** (nur Stimmung, keine Personen, im Film als «Illustration» behandeln):

- *Notizbuch:* «Extreme close-up of a lined paper notebook on a wooden school desk, fountain pen resting diagonally, soft morning window light with gentle shadows of window frames, shallow depth of field, slow push-in, desaturated warm ivory tones, 35mm film grain, no text, no people, 4:5 vertical»
- *Korridor:* «Slow forward dolly through a minimalist modern architectural corridor, concrete and glass, cool blue hour light, symmetrical composition, fine lines, muted navy and charcoal palette, subtle film grain, no people, no signage, 4:5 vertical»
- *Zürich:* «Zurich old town skyline at blue hour seen across the river Limmat, Grossmünster twin towers and Fraumünster spire, still water reflections, deep midnight navy sky with a faint warm glow on the horizon, slow push-in, restrained cinematic grade, no logos, 4:5 vertical»

Nicht erzeugen: Gesichter, Handschläge mit erkennbaren Personen, Laufsteg- oder Backstage-Szenen, Bankgebäude mit Logo.
