"""Controlla che ogni voce dell'inventario compaia nella prosa del capitolo corrispondente.

uso: python3 -I check_coverage.py <cartella-appunti>

Legge <cartella>/inventario/NN.txt (una voce per riga, # per i commenti) e cerca ogni voce in
capitoli/NN-*.tex, senza distinguere maiuscole e minuscole. Non contano commenti, diagrammi TikZ,
voci d'indice, etichette e rimandi: un concetto presente solo in uno schema non è nel testo.
Trova le parole, non giudica la spiegazione. Termina con 'problems: N'; exit code 1 se N > 0.
"""
import glob, os, re, sys

if len(sys.argv) != 2:
    sys.exit(__doc__)
root = os.path.abspath(sys.argv[1])
inv_dir = os.path.join(root, 'inventario')
problems = 0


def prose(tex):
    tex = re.sub(r'(?<!\\)%.*', '', tex)
    tex = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', ' ', tex, flags=re.S)
    tex = re.sub(r'\\(?:aut|idx|label|ref|pageref|index(?:\[[^\]]*\])?)\{[^}]*\}', ' ', tex)
    tex = re.sub(r'\\(?:,|;|:|!| )|~', ' ', tex)
    tex = tex.replace('{', '').replace('}', '')
    return ' '.join(tex.split()).lower()


files = sorted(glob.glob(os.path.join(inv_dir, '*.txt')))
if not files:
    print('NO INVENTORY  nessun file in inventario/')
    problems += 1
total = 0
for path in files:
    number = os.path.splitext(os.path.basename(path))[0]
    chapters = glob.glob(os.path.join(root, 'capitoli', number + '-*.tex'))
    if len(chapters) != 1:
        print(f'NO CHAPTER    inventario/{number}.txt: {len(chapters)} capitoli corrispondenti')
        problems += 1
        continue
    text = prose(open(chapters[0], encoding='utf-8').read())
    for line in open(path, encoding='utf-8'):
        term = line.strip()
        if not term or term.startswith('#'):
            continue
        total += 1
        if ' '.join(term.split()).lower() not in text:
            print(f'MISSING       {os.path.basename(chapters[0])}: {term}')
            problems += 1

# Ogni capitolo di contenuto deve avere il suo inventario.
for path in sorted(glob.glob(os.path.join(root, 'capitoli', '[0-9][0-9]-*.tex'))):
    number = os.path.basename(path)[:2]
    if number not in ('00', '98', '99') and not os.path.exists(os.path.join(inv_dir, number + '.txt')):
        print(f'NO INVENTORY  {os.path.basename(path)}')
        problems += 1

print(f'(info) voci controllate: {total}')
print('problems:', problems)
sys.exit(1 if problems else 0)
