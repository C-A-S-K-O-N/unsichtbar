# Originalmusik und Sounddesign für «Beyond the Classroom» (45 s, 80 BPM, d-Moll -> F-Dur).
# Komposition als MIDI (mido), gespielt mit FluidSynth + FluidR3_GM (MIT-Lizenz); Geräusche synthetisch (numpy).
# Ausgabe: build/film-audio.wav (48 kHz, Stereo, -16 LUFS). Aufruf: python3 film/audio.py
import os, subprocess, json
import numpy as np, mido
from scipy.io import wavfile
from scipy.signal import butter, sosfilt, fftconvolve

HERE = os.path.dirname(os.path.abspath(__file__)); BUILD = os.path.join(HERE, "..", "build"); os.makedirs(BUILD, exist_ok=True)
SR, DUR, BPM = 48000, 45.0, 80
B = 60 / BPM                      # 0.75 s pro Schlag, 3 s pro Takt
SF2 = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
rng = np.random.default_rng(7)

# ---------------- Komposition ----------------
N = {n: i for i, n in enumerate(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])}
def m(s):  # "D4" -> MIDI
    return 12 * (int(s[-1]) + 1) + N[s[:-1].replace("Bb", "A#").replace("Eb", "D#")]
CH = {"Dm": ["D", "F", "A"], "Bb": ["Bb", "D", "F"], "F": ["F", "A", "C"], "C": ["C", "E", "G"]}
BARS = ["Dm", "Bb", "F", "C", "Dm", "Bb", "F", "C", "Dm", "Bb", "F", "C", "Bb", "C", "F"]
ROOT = {"Dm": "D", "Bb": "Bb", "F": "F", "C": "C"}
PAD = {"Dm": ["D3", "A3", "D4", "F4", "A4"], "Bb": ["Bb2", "F3", "D4", "F4", "Bb4"], "F": ["F2", "C4", "F4", "A4", "C5"], "C": ["C3", "G3", "C4", "E4", "G4"]}
ev = []  # (zeit_s, kanal, note, vel, dauer_s)
def note(t, ch, n, v, d): ev.append((t, ch, m(n) if isinstance(n, str) else n, int(v), d))
MEL = {8: [("F5", 2, 64), ("E5", 1, 58), ("D5", 1, 56)], 9: [("D5", 2, 60), ("C5", 1, 54), ("A4", 1, 52)],
       12: [("F5", 2, 62), ("D5", 1, 56), ("F5", 1, 58)], 13: [("G5", 2, 66), ("E5", 1, 58), ("G5", 1, 60)], 14: [("A5", 4, 70)]}
for b, c in enumerate(BARS):
    t0 = b * 4 * B; r = ROOT[c]; tones = CH[c]
    # Klavier links: Grundton-Oktave
    lv = 46 if b < 4 else 54 if b < 10 else 40 if b < 12 else 56
    note(t0, 0, r + "2", lv, 4 * B * .98); note(t0, 0, r + "3", lv - 6, 4 * B * .98)
    # Klavier rechts
    if b < 2 or b in (10, 11):        # spärlich: Viertel
        seq = [tones[0] + "4", tones[2] + "4", tones[1] + "5", tones[2] + "4"]
        for k, n in enumerate(seq): note(t0 + k * B, 0, n, 36 + 6 * (k == 0) + (4 if b >= 10 else 0), B * 1.6)
    elif b < 14:                       # Achtel-Arpeggio, wächst mit der Geschichte
        seq = [tones[0] + "4", tones[2] + "4", tones[1] + "5", tones[2] + "4", tones[0] + "5", tones[2] + "4", tones[1] + "5", tones[2] + "4"]
        base = 40 if b < 4 else 46 if b < 8 else 52 if b < 10 else 50
        for k, n in enumerate(seq): note(t0 + k * B / 2, 0, n, base + (8 if k % 4 == 0 else 0) - (k % 2) * 4, B * .9)
    if b in MEL:
        tt = t0
        for n, beats, v in MEL[b]: note(tt, 0, n, v, beats * B * .95); tt += beats * B
    # Streicher ab Takt 3, Cello ab Takt 5
    if b >= 2:
        sv = 46 if b < 4 else 58 if b < 8 else 72 if b < 10 else 44 if b < 12 else 74
        for n in PAD[c]: note(t0, 1, n, sv, 4 * B * (1.0 if b < 14 else .9))
    if 4 <= b < 10 or b >= 12:
        note(t0, 2, r + "2", 50 if b < 10 else 56, 2 * B * .95); note(t0 + 2 * B, 2, r + "2", 44, 2 * B * .95)
    # Schlagwerk: Takt 6 bis 10 und 13 bis 14, leise
    if 5 <= b < 10 or b in (12, 13):
        for k in (0, 2): note(t0 + k * B, 9, 36, 44 if b < 8 else 52, .2)
        for k in range(8): note(t0 + k * B / 2, 9, 70 if b < 12 else 82, 18 + (k % 2) * 8, .1)   # Maracas/Shaker
        if b == 9: [note(t0 + 3 * B + k * B / 4, 9, 45, 34 + k * 6, .15) for k in range(4)]
# Pauke: Kapitelanfänge III, VI und Schlussakkord
for tt, n, v in ((14.25, "D2", 58), (36.0, "Bb1", 62), (42.0, "F2", 70)): note(tt, 3, n, v, 2.5)

mid = mido.MidiFile(ticks_per_beat=480); tr = mido.MidiTrack(); mid.tracks.append(tr)
tr.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(BPM)))
for ch, prog, vol, rev in ((0, 0, 100, 70), (1, 49, 92, 95), (2, 42, 78, 80), (3, 47, 96, 90), (9, 0, 70, 60)):
    if ch != 9: tr.append(mido.Message("program_change", channel=ch, program=prog))
    tr.append(mido.Message("control_change", channel=ch, control=7, value=vol))
    tr.append(mido.Message("control_change", channel=ch, control=91, value=rev))
    tr.append(mido.Message("control_change", channel=ch, control=93, value=12))
msgs = []
for t, ch, n, v, d in ev:
    msgs.append((t, 1, mido.Message("note_on", channel=ch, note=n, velocity=v)))
    msgs.append((t + d, 0, mido.Message("note_off", channel=ch, note=n, velocity=0)))
# Streicher-Ausdruck (CC11): Atmen der Sektionen
for i in range(int(DUR * 10)):
    t = i / 10; b = int(t // (4 * B)); x = (t % (4 * B)) / (4 * B)
    e = 70 + 40 * np.sin(np.pi * x) ** 2 * (0.6 if b < 8 else 1.0 if b < 10 else .4 if b < 12 else 1.0)
    if t > 43.0: e *= max(0, 1 - (t - 43.0) / 1.8)
    msgs.append((t, 2, mido.Message("control_change", channel=1, control=11, value=int(min(127, e)))))
msgs.sort(key=lambda x: (x[0], x[1])); last = 0
for t, _, msg in msgs:
    tick = int(round(t / B * 480)); msg.time = tick - last; last = tick; tr.append(msg)
midp, musp = os.path.join(BUILD, "film-music.mid"), os.path.join(BUILD, "film-music.wav")
mid.save(midp)
subprocess.run(["fluidsynth", "-ni", "-g", "0.55", "-r", str(SR), "-o", "synth.reverb.room-size=0.82", "-o", "synth.reverb.damp=0.35",
                "-o", "synth.reverb.width=0.9", "-o", "synth.reverb.level=0.75", "-F", musp, SF2, midp], check=True, capture_output=True)

# ---------------- Geräusche ----------------
n = int(SR * DUR); sfx = np.zeros((n, 2))
def bp(x, lo, hi): return sosfilt(butter(4, [lo, hi], btype="band", fs=SR, output="sos"), x)
def lp(x, f): return sosfilt(butter(4, f, btype="low", fs=SR, output="sos"), x)
def hp(x, f): return sosfilt(butter(4, f, btype="high", fs=SR, output="sos"), x)
def db(v): return 10 ** (v / 20)
def put(t, x, lvl, pan=0.0):
    i = int(t * SR); x = x[: max(0, n - i)] * db(lvl); g = np.array([np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)]) * 1.414
    sfx[i:i + len(x)] += x[:, None] * g[None, :]
def norm(x): return x / (np.max(np.abs(x)) + 1e-9)
IR = rng.standard_normal(int(SR * 1.1)) * np.exp(-np.linspace(0, 1.1, int(SR * 1.1)) * 5.5); IR = lp(IR, 5000); IR /= np.sum(np.abs(IR)) / 40
def verb(x, wet=.35): return (1 - wet) * x + wet * fftconvolve(x, IR)[: len(x)]
def env(L, a, r): e = np.ones(L); A = int(a * SR); Rr = int(r * SR); e[:A] = np.linspace(0, 1, A) if A else 1; e[-Rr:] *= np.linspace(1, 0, Rr) if Rr else 1; return e
def tt(L): return np.arange(L) / SR

# Raumton (ganz leise, durchgehend)
w = rng.standard_normal(n); brown = lp(hp(np.cumsum(w), 25), 380); put(0, norm(brown) * env(n, 1.5, 1.5), -50, 0)
# Füller auf Papier
L = int(1.8 * SR); scr = bp(rng.standard_normal(L), 1800, 7000); e = np.zeros(L); k = 0
while k < L:
    s = int(rng.uniform(.06, .19) * SR); g = int(rng.uniform(.02, .08) * SR); e[k:k + s] = np.hanning(min(s, L - k)) * rng.uniform(.5, 1); k += s + g
put(.28, norm(scr * e) * env(L, .1, .3), -36, .25)
def whoosh(t0, d, lvl, hi=False, pan=0):
    L = int(d * SR); x = rng.standard_normal(L); lo_ = lp(x, 600); hi_ = bp(x, 1200, 6000); p = np.linspace(0, 1, L)
    y = (lo_ * (1 - p) + hi_ * p * .5) if not hi else bp(x, 2500, 9000); put(t0, norm(y) * np.sin(np.pi * p) ** 2, lvl, pan)
def thump(t0, lvl, f0=70, f1=42, d=.9):
    L = int(d * SR); tm = tt(L); ph = 2 * np.pi * np.cumsum(f0 + (f1 - f0) * tm / d) / SR
    x = np.sin(ph) * np.exp(-tm * 5.5) + .25 * lp(rng.standard_normal(L), 1500) * np.exp(-tm * 40); put(t0, verb(norm(x), .25), lvl)
def step(t0, lvl, pan=0, wet=.3):
    L = int(.5 * SR); tm = tt(L); heel = lp(rng.standard_normal(L), 600) * np.exp(-tm * 55) + .6 * np.sin(2 * np.pi * 85 * tm) * np.exp(-tm * 45)
    toe = np.zeros(L); o = int(.07 * SR); toe[o:] = bp(rng.standard_normal(L - o), 900, 3500) * np.exp(-tm[: L - o] * 90) * .45
    put(t0, verb(norm(heel + toe), wet), lvl + rng.uniform(-1.5, 1.5), pan)
def shutter(t0, lvl, pan=0, wet=.2):
    L = int(.3 * SR); tm = tt(L); x = np.zeros(L)
    for o, a, dec, lo_, hi_ in ((0, 1, 900, 3000, 12000), (.012, .7, 120, 1200, 6000), (.085, .8, 700, 2500, 11000), (.095, .5, 140, 900, 5000)):
        i = int(o * SR); x[i:] += a * bp(rng.standard_normal(L - i), lo_, hi_) * np.exp(-tm[: L - i] * dec)
    put(t0, verb(norm(x), wet), lvl, pan)

# I · Kontrast
whoosh(2.0, .5, -36); whoosh(4.25, .6, -33); thump(4.5, -30, 60, 38); thump(6.0, -33, 55, 36, 1.2)
# II · Raum: Tür, Schritte hinein
L = int(.9 * SR); put(7.45, norm(lp(rng.standard_normal(L), 500)) * np.sin(np.pi * np.linspace(0, 1, L)) ** 2, -32); thump(7.78, -36, 90, 60, .4)
for i, t0 in enumerate((8.35, 8.92, 9.49, 10.06, 10.63)): step(t0, -31 - i * 1.6, (-.15, .15)[i % 2])
whoosh(11.05, .45, -38)
# III · Paris: Publikum, Auslöser
L = int(8.25 * SR); cr = bp(rng.standard_normal(L), 250, 1700); tm = tt(L)
am = .65 + .2 * np.sin(2 * np.pi * .7 * tm + 1) + .15 * np.sin(2 * np.pi * 2.3 * tm)
put(14.25, norm(cr * am) * env(L, .4, .9), -42, 0)
for t0 in (14.25, 16.5, 18.75): shutter(t0, -22, 0)
for t0, p in ((14.62, -.6), (15.05, .5), (15.18, .5), (17.3, -.4), (19.6, .6), (20.4, -.5), (21.1, .3)): shutter(t0, -37, p, .45)
# IV · Verbindung
whoosh(22.25, .55, -33); L = int(.03 * SR)
for k in range(8): put(24.8 + k * .045, norm(hp(rng.standard_normal(L), 3500)) * np.exp(-tt(L) * 220), -38, .2)
whoosh(27.5, .55, -34); whoosh(28.5, 1.0, -38, hi=True, pan=-.2)
# V · Haltung: Schritte im Korridor
for i, t0 in enumerate(np.arange(30.15, 35.0, .75)): step(t0, -37, (-.12, .12)[i % 2], .55)
# Rückwärts-Anschwellen in Kapitel VI
L = int(1.45 * SR); tm = tt(L); x = lp(rng.standard_normal(L), 3000) * (np.exp(tm * 3.2) - 1) / (np.exp(1.45 * 3.2) - 1)
put(34.55, norm(x) * (tm / 1.45) ** 2, -30); thump(36.0, -31, 55, 34, 1.4)

# ---------------- Mischung ----------------
sr2, mus = wavfile.read(musp); mus = mus.astype(np.float64); mus /= 32768 if mus.dtype != np.float64 or np.max(np.abs(mus)) > 2 else 1
if mus.ndim == 1: mus = np.stack([mus, mus], 1)
mus = mus[:n] if len(mus) >= n else np.vstack([mus, np.zeros((n - len(mus), 2))])
mus /= np.max(np.abs(mus)) + 1e-9
mix = mus * db(-6) + sfx
fo = int(1.4 * SR); mix[-fo:] *= np.linspace(1, 0, fo)[:, None] ** 1.5
mix /= np.max(np.abs(mix)) / .9
raw = os.path.join(BUILD, "film-audio-raw.wav"); wavfile.write(raw, SR, (mix * 32767).astype(np.int16))
# Lautheit: zwei Durchgänge auf -16 LUFS, Spitzen -1.5 dBTP
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", raw, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
j = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
af = f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
out = os.path.join(BUILD, "film-audio.wav")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", raw, "-af", af, "-ar", str(SR), out], check=True)
print("ok", out, "gemessen", j["input_i"], "LUFS")
