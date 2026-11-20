# Bereitet Kyrills Material für den Film vor (nur lokal, nichts davon ins Repo):
#  - Fotos: Datenschutz-Fassungen in ../privat/ (Person unkenntlich, Notizen leicht unscharf)
#  - Laufsteg-Video: Querformat-Ausschnitt ohne Balken, 60 fps mit Zwischenbildern (für Zeitlupe) in ../build/vid/
# Aufruf: python3 film/prep_media.py <ordner-mit-uploads>  (Dateinamen siehe QUELLEN)
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
PRIV, VID = os.path.join(ROOT, "privat"), os.path.join(ROOT, "build", "vid")
SRC = sys.argv[1] if len(sys.argv) > 1 else "."
QUELLEN = {"vorbereitung": "39ef1f94-image.jpg", "meetingraum": "ff326526-image.jpg", "nah": "df0b2cdd-image.jpg",
           "video": "a37cbc61-ScreenRecording_10-08-2026_10-07-48_1.mov"}
os.makedirs(PRIV, exist_ok=True); os.makedirs(VID, exist_ok=True)


def soft(im, poly, radius, feather=18, darken=1.0):
    """Unschärfe innerhalb eines Polygons mit weicher Kante."""
    b = im.filter(ImageFilter.GaussianBlur(radius))
    if darken != 1.0: b = b.point(lambda v: int(v * darken))
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).polygon(poly, fill=255); m = m.filter(ImageFilter.GaussianBlur(feather))
    return Image.composite(b, im, m)


# Vorbereitung am Tisch: Kollege links unkenntlich, Gesprächsskript leicht unscharf
im = Image.open(os.path.join(SRC, QUELLEN["vorbereitung"])).convert("RGB")
im = soft(im, [(0, 880), (600, 880), (600, 1820), (0, 1820)], 46, 40, .55)
im = soft(im, [(990, 1840), (1515, 1840), (1760, 2275), (1000, 2275)], 3.2, 10)
im.save(os.path.join(PRIV, "kyrill-vorbereitung.jpg"), quality=93)
# Meetingraum mit Arbeitsplatz: Notizen und Tablet leicht unscharf
im = Image.open(os.path.join(SRC, QUELLEN["meetingraum"])).convert("RGB")
im = soft(im, [(1030, 1840), (1520, 1840), (1520, 2520), (1030, 2520)], 3.2, 10)
im = soft(im, [(1190, 1820), (1520, 1820), (1520, 2080), (1190, 2080)], 3.2, 10)
im = soft(im, [(950, 1760), (1150, 1760), (1150, 1990), (950, 1990)], 2.5, 8)
im.save(os.path.join(PRIV, "kyrill-meetingraum.jpg"), quality=93)
# Laufsteg nah (Screenshot), unverändert
Image.open(os.path.join(SRC, QUELLEN["nah"])).convert("RGB").save(os.path.join(PRIV, "kyrill-laufsteg-nah.jpg"), quality=95)
print("Fotos ok")

# Video: Bildschirmaufnahme im Querformat, Bild 2346 x 1320 bei x=260; 30 fps -> 60 fps mit Bewegungsinterpolation
v = os.path.join(SRC, QUELLEN["video"])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", v, "-an", "-vf",
                "crop=2346:1320:260:0,fps=30,minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1:scd=fdiff,scale=-2:1350",
                "-q:v", "3", "-start_number", "0", os.path.join(VID, "v%04d.jpg")], check=True)
print("Video ok", len(os.listdir(VID)), "Bilder")
