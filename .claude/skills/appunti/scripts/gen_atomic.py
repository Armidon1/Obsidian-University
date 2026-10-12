"""Genera note atomiche (concetti) con formato uniforme.

uso: python3 -I gen_atomic.py <cartella-Concetti> <dati.py> [<dati2.py> ...]

Ogni file dati è un modulo Python che definisce:

    MOC = 'MOC - Sistemi Operativi'          # nome della nota MOC
    TAG = 'sistemi-operativi'                # tag del corso
    LESSONS = {1: '01 - SO - Introduzione', 2: '02 - SO - ...'}   # numero -> nome nota
    NOTES = [
        dict(name='Paging',                  # nome della nota (unico nel vault!)
             tags=['memoria'],               # tag aggiuntivi
             tldr='Una o due frasi.',         # contenuto del callout "In breve"
             body='''markdown libero''',     # corpo: bullet, tabelle, formule, codice
             related=['TLB', 'MMU'],         # concetti correlati
             refs=[(10, 'Paging'), (10, None)]),  # (lezione, titolo esatto della sezione o None)
    ]

MOC, TAG e LESSONS possono stare in uno solo dei file dati: vengono letti dal primo che li definisce.
I backslash nel body vanno raddoppiati (es. '\\\\alpha') oppure si usano stringhe raw.
"""
import sys, os, runpy

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
notes, cfg = [], {}
for f in sys.argv[2:]:
    mod = runpy.run_path(f)
    notes += mod.get('NOTES', [])
    for k in ('MOC', 'TAG', 'LESSONS'):
        if k in mod and k not in cfg:
            cfg[k] = mod[k]
missing = [k for k in ('MOC', 'TAG', 'LESSONS') if k not in cfg]
if missing:
    sys.exit(f'mancano nei file dati: {missing}')

for n in notes:
    tags = '\n'.join(f'  - {t}' for t in [cfg['TAG'], 'concetto'] + n.get('tags', []))
    refs = []
    for l, sec in n['refs']:
        lesson = cfg['LESSONS'][l]
        refs.append(f'> - [[{lesson}#{sec}|Lezione {l} — {sec}]]' if sec else f'> - [[{lesson}|Lezione {l}]]')
    related = ' · '.join(f'[[{r}]]' for r in n.get('related', []))
    text = f"""---
title: {n['name']}
tags:
{tags}
---

# {n['name']}

> [!summary] In breve
> {n['tldr']}

{n['body'].strip()}

## Collegamenti

- **Concetti correlati**: {related}
- **Mappa**: [[{cfg['MOC']}]]

> [!info] Approfondimento
{chr(10).join(refs)}
"""
    with open(os.path.join(out, n['name'] + '.md'), 'w', encoding='utf-8') as fh:
        fh.write(text)
print(len(notes), 'note scritte in', out)
