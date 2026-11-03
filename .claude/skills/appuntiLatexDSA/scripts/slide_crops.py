"""Ritaglia i blocchi di "inchiostro" da pagine già renderizzate (slide con figure vettoriali o a tasselli).

uso: python3 -I slide_crops.py <out_dir> <pagina.png> [<pagina.png> ...] [--threshold N] [--min-cells N]

Divide la pagina in celle da 8 px, unisce le celle con inchiostro contigue e salva ogni blocco
abbastanza grande come <out_dir>/<nome>-K.png. Stampa nome, dimensioni e riquadro (x0,y0,x1,y1).
Prende anche i blocchi di testo: scarta quelli inutili dopo averli guardati.
--threshold  sotto questo valore un pixel è inchiostro (default 235; abbassalo con sfondi colorati)
--min-cells  celle minime di un blocco (default 400; abbassalo per figure piccole)
"""
import os, sys
from collections import deque
from PIL import Image

args = sys.argv[1:]
threshold, min_cells = 235, 400
if '--threshold' in args:
    i = args.index('--threshold'); threshold = int(args[i + 1]); del args[i:i + 2]
if '--min-cells' in args:
    i = args.index('--min-cells'); min_cells = int(args[i + 1]); del args[i:i + 2]
if len(args) < 2:
    sys.exit(__doc__)
out, pages = args[0], args[1:]
os.makedirs(out, exist_ok=True)
CELL = 8
FILL = 90  # una cella conta se l'inchiostro ne copre almeno il 35% circa (90/255)

for path in pages:
    im = Image.open(path).convert('RGB')
    w, h = im.size
    W, H = w // CELL, h // CELL
    # il canale minimo riconosce come inchiostro anche i colori chiari ma saturi
    r, g, b = im.split()
    darkest = Image.frombytes('L', im.size, bytes(map(min, r.tobytes(), g.tobytes(), b.tobytes())))
    ink = darkest.point(lambda v: 255 if v < threshold else 0).resize((W, H), Image.BOX)
    px = ink.load()
    full = [[px[x, y] > FILL for x in range(W)] for y in range(H)]
    seen = [[False] * W for _ in range(H)]
    base = os.path.splitext(os.path.basename(path))[0]
    k = 0
    for y in range(H):
        for x in range(W):
            if not full[y][x] or seen[y][x]:
                continue
            queue = deque([(y, x)])
            seen[y][x] = True
            y0, y1, x0, x1, cells = y, y, x, x, 0
            while queue:
                cy, cx = queue.popleft()
                cells += 1
                y0, y1, x0, x1 = min(y0, cy), max(y1, cy), min(x0, cx), max(x1, cx)
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < H and 0 <= nx < W and full[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        queue.append((ny, nx))
            if cells < min_cells:
                continue
            box = (x0 * CELL, y0 * CELL, (x1 + 1) * CELL, (y1 + 1) * CELL)
            name = f'{base}-{k}.png'
            im.crop(box).save(os.path.join(out, name))
            print(f'{name}\t{box[2] - box[0]}x{box[3] - box[1]}\t{box}')
            k += 1
    if k == 0:
        print(f'{base}\tnessun blocco trovato')
