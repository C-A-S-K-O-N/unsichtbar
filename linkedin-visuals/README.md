# LinkedIn-Visuals · Premium-Stil

Standbilder und Videos mit haptischen Bewegungen für LinkedIn-Beiträge,
4:5 (1080 × 1350). Anleitung und Regeln: `.claude/skills/linkedin-agent/modi/li-visual.md`.

- `engine.html` Stil und Bewegungs-Engine (`render(t)`)
- `scenes.py` ein Motiv pro Beitrag (Schlüssel = ID in der Zentrale)
- `build.py` erzeugt `build/<id>.html`
- `render.js <id> still|video` schreibt `out/<id>.png` bzw. `out/<id>.mp4`

Braucht Python 3, Node mit Playwright (Chromium) und ffmpeg.

Persönliche Fotos (z. B. `scenes_kyrill.py`) liegen nur lokal in `privat/` und
werden nicht eingecheckt. Für einen neuen Render das Foto dort ablegen
(`privat/kyrill-laufsteg.jpg`), sonst bleibt die Fotofläche leer.

`film/` enthält den persönlichen Markenfilm «Beyond the Classroom» (45 s, mit
Originalmusik). Storyboard, Shotlist und Schnittplan: `film/BEYOND-THE-CLASSROOM.md`.
Braucht zusätzlich `fluidsynth`, `fluid-soundfont-gm`, `scipy` und `mido`.
