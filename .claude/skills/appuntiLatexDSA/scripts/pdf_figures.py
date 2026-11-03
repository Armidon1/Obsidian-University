"""Ritaglia le figure (raster o vettoriali) da un PDF usando le didascalie come ancora.

uso: python3 -I pdf_figures.py <file.pdf> <out_dir> <prefisso> [prima_pagina] [ultima_pagina] [--caption REGEX] [--dpi N] [--bands]

Pensato per libri/dispense in cui ogni figura ha sotto una didascalia (default: righe che
iniziano con "Figura" o "Figure" o "Fig."). Per ogni didascalia:
  - la figura è la zona sopra la didascalia, risalendo finché c'è "inchiostro" (linee, forme,
    immagini, etichette brevi) e fermandosi alla prima riga di testo larga (un paragrafo),
    a un'altra didascalia o a un vuoto verticale ampio;
  - il ritaglio è a colori, con le etichette dentro la figura.
Scrive <out_dir>/<prefisso>-pNNN-K.png e stampa: nome, pagina, didascalia.
Con --bands, nelle pagine SENZA didascalie ritaglia ogni fascia di "inchiostro" compresa tra
paragrafi (utile per figure senza didascalia; prende anche riquadri di codice: scarta quelli che
non servono). Per slide usa invece pdftoppm sulla pagina intera (vedi SKILL.md).
"""
import sys, os, re, subprocess, tempfile, html
from PIL import Image, ImageDraw

args = sys.argv[1:]
caption_re = r'^(Figura|Figure|Fig\.)\s'
dpi = 130
bands_mode = '--bands' in args
if bands_mode:
    args.remove('--bands')
if '--caption' in args:
    i = args.index('--caption'); caption_re = args[i + 1]; del args[i:i + 2]
if '--dpi' in args:
    i = args.index('--dpi'); dpi = int(args[i + 1]); del args[i:i + 2]
pdf, out, prefix = args[:3]
first = int(args[3]) if len(args) > 3 else 1
last = int(args[4]) if len(args) > 4 else None
os.makedirs(out, exist_ok=True)
if last is None:
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    last = int(re.search(r'Pages:\s+(\d+)', info).group(1))

INK = 235            # pixel più scuri = inchiostro
STOP_GAP = 45        # vuoto verticale (px) che chiude la figura
WIDE = 0.55          # una riga più larga di questa frazione della pagina è testo di paragrafo
scale = dpi / 72.0

line_re = re.compile(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', re.S)
word_re = re.compile(r'<word[^>]*>(.*?)</word>')

with tempfile.TemporaryDirectory() as tmp:
    for page in range(first, last + 1):
        base = os.path.join(tmp, 'pg')
        subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page), '-l', str(page),
                        '-singlefile', pdf, base], check=True)
        rgb = Image.open(base + '.png').convert('RGB')
        W, H = rgb.size
        xml = subprocess.run(['pdftotext', '-bbox-layout', '-f', str(page), '-l', str(page), pdf, '-'],
                             capture_output=True, text=True).stdout
        lines = []
        for m in line_re.finditer(xml):
            x0, y0, x1, y1 = (float(v) * scale for v in m.groups()[:4])
            text = ' '.join(html.unescape(w) for w in word_re.findall(m.group(5))).strip()
            lines.append((x0, y0, x1, y1, text))
        captions = [l for l in lines if re.match(caption_re, l[4])]
        if not captions and not bands_mode:
            continue
        # maschera: paragrafi e didascalie bianchi; il resto (figure, etichette) resta
        gray = rgb.convert('L')
        mask = gray.copy()
        d = ImageDraw.Draw(mask)
        stop_rows = set()
        wide_x = [l[0] for l in lines if (l[2] - l[0]) > WIDE * W]
        margin = min(wide_x) if wide_x else None
        for x0, y0, x1, y1, text in lines:
            # paragrafo: riga larga, didascalia, o riga (anche corta) che parte dal margine del testo
            at_margin = margin is not None and abs(x0 - margin) < 0.015 * W
            if (x1 - x0) > WIDE * W or at_margin or re.match(caption_re, text):
                d.rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], fill=255)
                stop_rows.update(range(int(y0), int(y1) + 1))
        px = mask.load()
        def row_ink(y):
            return sum(1 for x in range(0, W, 3) if px[x, y] < INK) >= 3
        k = 0
        if not captions:  # modalità --bands
            band, gap, found = None, 0, []
            for y in range(int(H * 0.05), int(H * 0.93)):
                ink = y not in stop_rows and row_ink(y)
                if ink:
                    band = [y, y] if band is None else [band[0], y]; gap = 0
                elif band is not None:
                    gap += 1
                    if gap > STOP_GAP // 2 or y in stop_rows:
                        found.append(band); band = None
            if band: found.append(band)
            for y0, y1 in found:
                if y1 - y0 < 30:
                    continue
                xs = [x for yy in range(y0, y1 + 1, 2) for x in range(0, W, 2) if px[x, yy] < INK]
                k += 1
                name = f'{prefix}-p{page:03d}-{k}.png'
                rgb.crop((max(min(xs) - 10, 0), max(y0 - 10, 0), min(max(xs) + 10, W), min(y1 + 10, H))).save(os.path.join(out, name))
                print(f'{name}\t{page}\t(senza didascalia)')
            continue
        for cx0, cy0, cx1, cy1, ctext in sorted(captions, key=lambda c: c[1]):
            y = int(cy0) - 3
            top_ink = bottom_ink = None
            gap = 0
            while y > int(H * 0.04):
                if y in stop_rows:
                    break
                if row_ink(y):
                    if bottom_ink is None:
                        bottom_ink = y
                    top_ink = y
                    gap = 0
                elif top_ink is not None:
                    gap += 1
                    if gap > STOP_GAP:
                        break
                elif int(cy0) - y > 3 * STOP_GAP:
                    break  # niente sopra la didascalia: forse la figura è sulla pagina precedente
                y -= 1
            if top_ink is None or bottom_ink - top_ink < 20:
                print(f'NOFIG p{page}: {ctext[:70]}')
                continue
            xs = [x for yy in range(top_ink, bottom_ink + 1, 2) for x in range(0, W, 2) if px[x, yy] < INK]
            x0, x1 = max(min(xs) - 10, 0), min(max(xs) + 10, W)
            k += 1
            name = f'{prefix}-p{page:03d}-{k}.png'
            rgb.crop((x0, max(top_ink - 10, 0), x1, min(bottom_ink + 10, H))).save(os.path.join(out, name))
            print(f'{name}\t{page}\t{ctext[:90]}')
