"""Verifica una cartella di appunti LaTeX per DSA: sorgenti, accessibilità e log di compilazione.

uso: python3 -I check_latex.py <cartella-appunti> [--overfull PT] [--max-parole N]

Sorgenti:      immagini mancanti o non usate, \\ref senza \\label, \\label doppie, file di
               capitoli/ non inclusi, segnaposto @@...@@ rimasti.
Accessibilità: niente testo piccolo, corsivo, sottolineato o note a piè di pagina nei capitoli.
Editoriale:    paragrafi oltre N parole (default 110): avvisi, non errori.
Schemi:        ogni capitolo numerato ha mappainizio prima della prima sezione e mappafine dopo
               l'ultima, ciascuno seguito da testo (solo se main.tex definisce i due ambienti).
               Nessun altro minimo di diagrammi, flussi o riquadri; struttura flessibile.
Log:           errori, caratteri assenti dal font, riferimenti non risolti, file non trovati,
               righe oltre il margine di più di PT punti (default 10), log vecchio.
Termina con 'problems: N'; l'exit code è 1 se N > 0.
"""
import os, re, sys

args = sys.argv[1:]
limit, max_words = 10.0, 110
if '--overfull' in args:
    i = args.index('--overfull'); limit = float(args[i + 1]); del args[i:i + 2]
if '--max-parole' in args:
    i = args.index('--max-parole'); max_words = int(args[i + 1]); del args[i:i + 2]
if len(args) != 1:
    sys.exit(__doc__)
root = os.path.abspath(args[0])
main = os.path.join(root, 'main.tex')
if not os.path.isfile(main):
    sys.exit(f'main.tex non trovato in {root}')

problems = 0
editorial_warnings = 0


def report(kind, msg):
    global problems
    problems += 1
    print(f'{kind:<14}{msg}')


def advise(kind, msg):
    global editorial_warnings
    editorial_warnings += 1
    print(f'{kind:<14}{msg}')


def clean(tex):
    """Toglie ambienti letterali e commenti, dove i comandi non vanno interpretati."""
    tex = re.sub(r'\\begin\{(lstlisting|verbatim|Verbatim|minted)\}.*?\\end\{\1\}', '', tex, flags=re.S)
    return re.sub(r'(?<!\\)%.*', '', tex)


sources, raw, order = {}, {}, []


def load(path):
    rel = os.path.relpath(path, root)
    if rel in sources:
        return
    raw[rel] = open(path, encoding='utf-8').read()
    sources[rel] = clean(raw[rel])
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

# --- accessibilità -----------------------------------------------------------------------
BANNED = {
    r'\\(?:small|footnotesize|scriptsize|tiny)\b': 'testo piccolo',
    r'\\footnote\b': 'nota a piè di pagina',
    r'\\textit\b|\\itshape\b|(?<!\\)\\it\b|\\slshape\b': 'corsivo',
    r'\\underline\b|\\uline\b': 'sottolineatura',
    r'\\MakeUppercase\b': 'maiuscolo esteso',
}
UNCOUNTED = re.compile(r'\\begin\{(cit|tikzpicture|tabularx|tabular|longtable|simboli|cronologia|figure|align\*?|equation\*?)\}'
                       r'.*?\\end\{\1\}', re.S)
chapters = diagrams_total = 0
chapter_maps = r'\newtcolorbox{mappainizio}' in sources.get('main.tex', '') and r'\newtcolorbox{mappafine}' in sources.get('main.tex', '')


def check_chapter_maps(rel, tex):
    for env in ('mappainizio', 'mappafine'):
        found = len(re.findall(r'\\begin\{%s\}' % env, tex))
        if found != 1:
            report('CHAPTER MAP', f'{rel}: {env} presente {found} volte (ne serve una)')
            continue
        after = tex.split(r'\end{%s}' % env, 1)[1].lstrip()
        if after.startswith(('\\begin', '\\section', '\\end')) or not after:
            report('CHAPTER MAP', f'{rel}: {env} senza spiegazione a testo subito dopo')
    sections = [m.start() for m in re.finditer(r'\\section\*?\{', tex)]
    start, end = tex.find(r'\begin{mappainizio}'), tex.find(r'\begin{mappafine}')
    if sections and start > sections[0]:
        report('CHAPTER MAP', f'{rel}: mappainizio dopo la prima sezione')
    if sections and -1 < end < sections[-1]:
        report('CHAPTER MAP', f'{rel}: mappafine prima dell\'ultima sezione')


for rel in order:
    if not rel.startswith('capitoli' + os.sep):
        continue
    tex = sources[rel]
    for pattern, what in BANNED.items():
        count = len(re.findall(pattern, tex))
        if count:
            report('ACCESSIBILITY', f'{rel}: {what} ({count})')
    prose = UNCOUNTED.sub('\n\n', tex)
    prose = re.sub(r'^\\afronte.*$', '\n', prose, flags=re.M)
    for par in re.split(r'\n\s*\n', prose):
        words = len(re.sub(r'\\[a-zA-Z]+(?:\[[^\]]*\])?|[{}]', ' ', par).split())
        if words > max_words:
            advise('LONG PAR', f'{rel}: {words} parole: «{" ".join(par.split())[:50]}...»')

    count = len(re.findall(r'\\begin\{tikzpicture\}', tex))
    diagrams_total += count
    if r'\chapter{' in tex and not os.path.basename(rel).startswith(('00-', '98-', '99-')):
        chapters += 1
        if chapter_maps:
            check_chapter_maps(rel, tex)
    print(f'(info) {os.path.basename(rel)}: diagrammi {count}')

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

print(f'(info) file: {len(order)}, capitoli: {chapters}, diagrammi TikZ: {diagrams_total}, '
      f'immagini usate: {len(used)}/{len(on_disk)}, etichette: {len(labels)}')
print('editorial warnings:', editorial_warnings)
print('problems:', problems)
sys.exit(1 if problems else 0)
