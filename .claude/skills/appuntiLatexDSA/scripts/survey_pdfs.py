"""Primo sopralluogo su un gruppo di PDF: testo, miniature, fogli di contatto, pagine sospette.

uso: python3 -I survey_pdfs.py <out_dir> <file.pdf> [<file.pdf> ...] [--dpi N] [--per-sheet N]

Per ogni PDF, numerato D01, D02, ... nell'ordine degli argomenti, scrive:
  <out_dir>/txt/D01.txt           testo completo (pdftotext -layout)
  <out_dir>/thumbs/D01-NNN.png    una miniatura per pagina
  <out_dir>/sheet-D01-K.png       fogli di contatto con il numero di pagina
Stampa la corrispondenza tra sigle e file e, per ogni PDF, le pagine con immagini e meno di
20 parole: possono avere testo dentro un'immagine, che pdftotext non vede.
"""
import os, re, subprocess, sys

args = sys.argv[1:]
dpi, per_sheet = 40, 30
if '--dpi' in args:
    i = args.index('--dpi'); dpi = int(args[i + 1]); del args[i:i + 2]
if '--per-sheet' in args:
    i = args.index('--per-sheet'); per_sheet = int(args[i + 1]); del args[i:i + 2]
if len(args) < 2:
    sys.exit(__doc__)
out, pdfs = args[0], args[1:]
for sub in ('txt', 'thumbs'):
    os.makedirs(os.path.join(out, sub), exist_ok=True)


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True, errors='replace').stdout


for n, pdf in enumerate(pdfs, 1):
    tag = f'D{n:02d}'
    pages = int(re.search(r'Pages:\s+(\d+)', run('pdfinfo', pdf)).group(1))
    text = run('pdftotext', '-layout', pdf, '-')
    with open(os.path.join(out, 'txt', tag + '.txt'), 'w', encoding='utf-8') as f:
        f.write(text)

    # pdftotext separa le pagine con un form feed
    words = [len(p.split()) for p in text.split('\f')]
    images = {}
    for line in run('pdfimages', '-list', pdf).splitlines()[2:]:
        first = line.split()[0] if line.split() else ''
        if first.isdigit():
            images[int(first)] = images.get(int(first), 0) + 1

    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), pdf,
                    os.path.join(out, 'thumbs', tag)], check=True)
    # pdftoppm adatta gli zeri al numero di pagine: si raccolgono i file generati
    prefix = tag + '-'
    thumbs = sorted(f for f in os.listdir(os.path.join(out, 'thumbs'))
                    if f.startswith(prefix) and f.endswith('.png'))
    sheets = 0
    for k in range(0, len(thumbs), per_sheet):
        sheets += 1
        batch = [os.path.join(out, 'thumbs', f) for f in thumbs[k:k + per_sheet]]
        subprocess.run(['montage', '-label', '%t', *batch, '-tile', '6x',
                        '-geometry', '300x300+3+3', '-pointsize', '12',
                        os.path.join(out, f'sheet-{tag}-{sheets}.png')], check=True)

    suspects = [p for p in range(1, pages + 1)
                if images.get(p) and (words[p - 1] if p <= len(words) else 0) < 20]
    print(f'{tag}\t{pages} pp\t{sum(words)} parole\t{sum(images.values())} immagini\t{pdf}')
    if suspects:
        print(f'\tcon immagini e poco testo: {", ".join(map(str, suspects))}')
