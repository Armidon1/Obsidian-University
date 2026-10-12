"""Estrae un .docx in testo ordinato con marcatori immagine.

uso: python3 -I extract_docx.py <file.docx> <out_dir> <prefisso>
Scrive <out_dir>/<prefisso>.md e copia le immagini in <out_dir>/img/<prefisso>-NN.ext.
Marcatori: [IMG nome] posizione immagine, [LI] elenco/stile, [B] tutto grassetto, [szNN] font max.
"""
import sys, zipfile, re, os
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
V = '{urn:schemas-microsoft-com:vml}'

src, out, prefix = sys.argv[1:4]
os.makedirs(os.path.join(out, 'img'), exist_ok=True)
z = zipfile.ZipFile(src)
rels = ET.fromstring(z.read('word/_rels/document.xml.rels'))
relmap = {r.get('Id'): r.get('Target') for r in rels}
body = ET.fromstring(z.read('word/document.xml')).find(W + 'body')

lines = []
imgn = [0]

def image(rid):
    tgt = relmap.get(rid)
    if not tgt or 'media' not in tgt:
        return
    imgn[0] += 1
    ext = tgt.rsplit('.', 1)[-1]
    name = f'{prefix}-{imgn[0]:02d}.{ext}'
    with open(os.path.join(out, 'img', name), 'wb') as f:
        f.write(z.read('word/' + tgt.lstrip('/').replace('word/', '')))
    lines.append(f'[IMG {name}]')

def para(p):
    ppr = p.find(W + 'pPr')
    style, numbered = '', False
    if ppr is not None:
        s = ppr.find(W + 'pStyle')
        style = s.get(W + 'val') if s is not None else ''
        numbered = ppr.find(W + 'numPr') is not None
    text, sizes, bold = [], set(), True
    for el in p.iter():
        if el.tag == W + 'r':
            t = ''.join((x.text or '') if x.tag == W + 't' else ('\t' if x.tag == W + 'tab' else ('\n' if x.tag in (W + 'br', W + 'cr') else ''))
                        for x in el)
            if t.strip():
                rpr = el.find(W + 'rPr')
                b = rpr is not None and rpr.find(W + 'b') is not None
                sz = rpr.find(W + 'sz') if rpr is not None else None
                if sz is not None:
                    sizes.add(int(sz.get(W + 'val')) // 2)
                bold = bold and b
            text.append(t)
        elif el.tag == A + 'blip':
            image(el.get(R + 'embed'))
        elif el.tag == V + 'imagedata':
            image(el.get(R + 'id'))
    t = ''.join(text).rstrip()
    if not t.strip():
        return
    tag = []
    if sizes: tag.append(f'sz{max(sizes)}')
    if bold: tag.append('B')
    if numbered or style: tag.append('LI')
    lines.append(f'[{",".join(tag)}] {t}' if tag else t)

def table(tb):
    lines.append('[TABLE]')
    for tr in tb.iter(W + 'tr'):
        cells = []
        for tc in tr.iter(W + 'tc'):
            cells.append(' '.join(''.join(x.text or '' for x in p.iter(W + 't')) for p in tc.iter(W + 'p')).strip())
        lines.append('| ' + ' | '.join(cells) + ' |')
    for b in tb.iter(A + 'blip'):
        image(b.get(R + 'embed'))
    lines.append('[/TABLE]')

for child in body:
    if child.tag == W + 'p':
        para(child)
    elif child.tag == W + 'tbl':
        table(child)

with open(os.path.join(out, prefix + '.md'), 'w') as f:
    f.write('\n'.join(lines) + '\n')
print(prefix, len(lines), 'lines', imgn[0], 'images')
