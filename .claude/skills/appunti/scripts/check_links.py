"""Verifica wikilink, sezioni e immagini di un corso.

uso: python3 -I check_links.py <cartella-corso> [<radice-vault>]

- I nomi delle note vengono risolti su tutto il vault (di default: la cartella che contiene
  la repo Obsidian-University), come fa Obsidian.
- Controlla i link [[Nota]], [[Nota#Sezione]], gli embed ![[img]] e le immagini in images/ non usate.
Termina con 'problems: N'.
"""
import os, re, sys

course = os.path.abspath(sys.argv[1])
if len(sys.argv) > 2:
    vault = os.path.abspath(sys.argv[2])
else:
    vault = course
    while os.path.basename(vault) != 'Obsidian-University' and vault != '/':
        vault = os.path.dirname(vault)
    vault = os.path.dirname(vault)

skip = {'.git', '.obsidian', '.trash', '.claude'}
notes, attachments = {}, {}
for d, dirs, fs in os.walk(vault):
    dirs[:] = [x for x in dirs if x not in skip]
    for f in fs:
        p = os.path.join(d, f)
        if f.endswith('.md'):
            notes.setdefault(f[:-3], []).append(p)
        else:
            attachments.setdefault(f, []).append(p)

heading_cache = {}
def headings(path):
    if path not in heading_cache:
        txt = open(path, encoding='utf-8').read()
        heading_cache[path] = {h.strip() for h in re.findall(r'^#{1,6} (.+)$', txt, re.M)}
    return heading_cache[path]

problems, used = 0, set()
for d, dirs, fs in os.walk(course):
    dirs[:] = [x for x in dirs if x not in skip]
    for f in fs:
        if not f.endswith('.md'):
            continue
        p = os.path.join(d, f)
        rel = os.path.relpath(p, course)
        txt = open(p, encoding='utf-8').read()
        txt = re.sub(r'```.*?```', '', txt, flags=re.S)  # ignora i blocchi di codice
        for m in re.findall(r'!\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]', txt):
            name = os.path.basename(m.strip())
            used.add(name)
            if name not in attachments and name not in notes and name[:-3] not in notes:
                print(f'MISSING IMG  {rel}: {m}'); problems += 1
        for m in re.findall(r'(?<!!)\[\[([^\]]+)\]\]', txt):
            target = m.split('|')[0]
            page, _, sec = target.partition('#')
            page = os.path.basename(page.strip())
            if not page:  # link interno [[#Sezione]]
                if sec and sec.strip() not in headings(p):
                    print(f'BAD SECTION  {rel}: {m}'); problems += 1
                continue
            if page not in notes:
                print(f'BROKEN LINK  {rel}: {m}'); problems += 1
                continue
            if len(notes[page]) > 1:
                print(f'AMBIGUOUS    {rel}: {page} -> {len(notes[page])} file con questo nome')
            if sec and not any(sec.strip() in headings(x) for x in notes[page]):
                print(f'BAD SECTION  {rel}: {m}'); problems += 1

img_dir = os.path.join(course, 'images')
if os.path.isdir(img_dir):
    unused = sorted(set(os.listdir(img_dir)) - used)
    # le immagini non usate sono un problema solo se le abbiamo estratte noi (SIGLA-LNN-XX)
    ours = [u for u in unused if not u.startswith('Pasted image')]
    for u in ours:
        print(f'UNUSED IMG   images/{u}'); problems += 1
    if len(unused) > len(ours):
        print(f'(info) {len(unused) - len(ours)} "Pasted image" non usate: solo da segnalare')

print('problems:', problems)
