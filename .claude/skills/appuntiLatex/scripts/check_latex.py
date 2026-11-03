"""Verifica una cartella di appunti LaTeX: sorgenti e log dell'ultima compilazione.

uso: python3 -I check_latex.py <cartella-appunti> [--overfull PT]

Sorgenti: immagini mancanti o non usate in images/, \\ref senza \\label, \\label doppie,
          file di capitoli/ non inclusi, segnaposto @@...@@ rimasti.
Log:      errori, caratteri assenti dal font, riferimenti non risolti, file non trovati,
          righe oltre il margine di più di PT punti (default 10), log più vecchio dei sorgenti.
Termina con 'problems: N'; l'exit code è 1 se N > 0.
"""
import os, re, sys

args = sys.argv[1:]
limit = 10.0
if '--overfull' in args:
    i = args.index('--overfull'); limit = float(args[i + 1]); del args[i:i + 2]
if len(args) != 1:
    sys.exit(__doc__)
root = os.path.abspath(args[0])
main = os.path.join(root, 'main.tex')
if not os.path.isfile(main):
    sys.exit(f'main.tex non trovato in {root}')

problems = 0


def report(kind, msg):
    global problems
    problems += 1
    print(f'{kind:<14}{msg}')


def clean(tex):
    """Toglie commenti e ambienti letterali, dove i comandi non vanno interpretati."""
    tex = re.sub(r'\\begin\{(lstlisting|verbatim|Verbatim|minted)\}.*?\\end\{\1\}', '', tex, flags=re.S)
    return re.sub(r'(?<!\\)%.*', '', tex)


sources, order = {}, []


def load(path):
    rel = os.path.relpath(path, root)
    if rel in sources:
        return
    raw = open(path, encoding='utf-8').read()
    sources[rel] = clean(raw)
    order.append(rel)
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', sources[rel]):
        target = os.path.join(root, name if name.endswith('.tex') else name + '.tex')
        if os.path.isfile(target):
            load(target)
        else:
            report('MISSING FILE', f'{rel}: {name}')


load(main)

# --- immagini --------------------------------------------------------------------------
img_dir = os.path.join(root, 'images')
on_disk = [f for f in os.listdir(img_dir) if not f.startswith('.')] if os.path.isdir(img_dir) else []
used = set()
for rel in order:
    tex = sources[rel]
    names = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', tex)
    names += re.findall(r'\\figw\{[^}]*\}\{([^}]+)\}', tex)
    for group in re.findall(r'\\figh\{[^}]*\}\{([^}]+)\}', tex):
        names += group.split(',')
    for name in names:
        name = name.strip()
        if '#' in name:  # argomento nella definizione di una macro
            continue
        name = os.path.basename(name)
        match = [f for f in on_disk if f == name or os.path.splitext(f)[0] == name]
        if match:
            used.update(match)
        else:
            report('MISSING IMG', f'{rel}: {name}')
for f in sorted(set(on_disk) - used):
    report('UNUSED IMG', f'images/{f}')

# --- rimandi ---------------------------------------------------------------------------
labels = {}
for rel in order:
    for name in re.findall(r'\\label\{([^}]+)\}', sources[rel]):
        if name in labels:
            report('DUP LABEL', f'{name}: {labels[name]} e {rel}')
        labels.setdefault(name, rel)
for rel in order:
    for name in re.findall(r'\\(?:page|auto|name|eq)?ref\{([^}]+)\}', sources[rel]):
        if name not in labels:
            report('BROKEN REF', f'{rel}: {name}')
    for name in re.findall(r'\\hyperref\[([^\]]+)\]', sources[rel]):
        if name not in labels:
            report('BROKEN REF', f'{rel}: hyperref[{name}]')

# --- capitoli non inclusi e segnaposto ---------------------------------------------------
chap_dir = os.path.join(root, 'capitoli')
if os.path.isdir(chap_dir):
    for f in sorted(os.listdir(chap_dir)):
        rel = os.path.join('capitoli', f)
        if f.endswith('.tex') and rel not in sources:
            report('NOT INCLUDED', rel)
for rel in order:
    for name in sorted(set(re.findall(r'@@[^@\n]+@@', sources[rel]))):
        report('PLACEHOLDER', f'{rel}: {name}')

# --- log -------------------------------------------------------------------------------
log_path = os.path.join(root, 'main.log')
if not os.path.isfile(log_path):
    report('NO LOG', 'main.log assente: compila prima di verificare')
else:
    stamp = os.path.getmtime(log_path)
    stale = [r for r in order if os.path.getmtime(os.path.join(root, r)) > stamp]
    if stale:
        report('STALE LOG', f'sorgenti più recenti del log: {", ".join(stale)}')
    log = open(log_path, encoding='utf-8', errors='replace').read()
    for line in re.findall(r'^! .*$', log, re.M):
        report('LATEX ERROR', line)
    for line in sorted(set(re.findall(r'^Missing character:.*$', log, re.M))):
        report('MISSING CHAR', line)
    for line in sorted(set(re.findall(r"LaTeX (?:Warning|Font Warning): (?:Reference|Citation|Label|Font shape|Some font|There were undefined).*", log))):
        report('LATEX WARNING', line)
    for name in sorted(set(re.findall(r"File `([^']+)' not found", log))):
        report('FILE NOT FOUND', name)
    over = [float(v) for v in re.findall(r'^Overfull \\[hv]box \(([\d.]+)pt too', log, re.M)]
    for value in sorted((v for v in over if v > limit), reverse=True):
        report('OVERFULL', f'{value:.1f}pt (le righe sono in main.log)')
    if over:
        print(f'(info) overfull totali: {len(over)}, massimo {max(over):.1f}pt')

print(f'(info) file: {len(order)}, immagini usate: {len(used)}/{len(on_disk)}, etichette: {len(labels)}')
print('problems:', problems)
sys.exit(1 if problems else 0)
