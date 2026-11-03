#!/usr/bin/env python3
"""Validate a source-to-book coverage matrix without requiring copied prose.

Usage: python3 -I check_coverage.py BOOK_DIR
Prefer inventario/copertura.json (version 1). Each item records sources,
labelled destinations and a documented manual review. Optional literals check
identifiers/data in the destination text, excluding diagrams and indices.
A zero exit status validates the records, not their scientific correctness.
Legacy inventario/NN.txt files are supported when no matrix exists.
"""
import json
import re
import sys
from pathlib import Path


def strip_comments(text):
    # Preserve literal environments: a percent sign in code is not a TeX comment.
    literals = []

    def save(match):
        literals.append(match[0])
        return f'ZZCOVERAGELITERAL{len(literals)-1}ZZ'

    text = re.sub(r'\\begin\{(lstlisting|verbatim|Verbatim|minted)\}.*?\\end\{\1\}', save, text, flags=re.S)
    text = re.sub(r'(?<!\\)%[^\n]*', '', text)
    return re.sub(r'ZZCOVERAGELITERAL(\d+)ZZ', lambda m: literals[int(m[1])], text)


def prose(text):
    text = strip_comments(text)
    text = re.sub(r'\\begin\{(lstlisting|verbatim|Verbatim|minted)\}(?:\[[^\]]*\])?(.*?)\\end\{\1\}', lambda m: m[2].replace('\\', 'ZZLITERALBACKSLASHZZ'), text, flags=re.S)
    text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', ' ', text, flags=re.S)
    text = re.sub(r'\\(?:aut|idx|label|ref|pageref|index(?:\[[^\]]*\])?)\{[^}]*\}', ' ', text)
    text = text.replace(r'\textbackslash{}', 'ZZLITERALBACKSLASHZZ')
    text = re.sub(r'\\([%&#_$\{\}])', lambda m: m[1], text)
    text = re.sub(r'\\(?:allowbreak|nobreak)\s*(?:\{\})?', '', text)
    text = re.sub(r'\\(?:,|;|:|!| )|~', ' ', text)
    text = re.sub(r'\\[A-Za-z]+\*?(?:\[[^\]]*\])?', '', text)
    text = text.replace('{', '').replace('}', '')
    return ' '.join(text.replace('ZZLITERALBACKSLASHZZ', '\\').split())


def labelled_body(text, label):
    """Read after the destination label, through the next same/higher heading."""
    text = strip_comments(text)
    scan = re.sub(r'\\begin\{(lstlisting|verbatim|Verbatim|minted)\}.*?\\end\{\1\}', lambda m: ' ' * len(m[0]), text, flags=re.S)
    mark = re.search(r'\\label\{' + re.escape(label) + r'\}', scan)
    if not mark:
        return None
    levels = {'chapter': 0, 'section': 1, 'subsection': 2, 'subsubsection': 3}
    headings = list(re.finditer(r'\\(chapter|section|subsection|subsubsection)\*?\{', scan))
    previous = [h for h in headings if h.start() < mark.start()]
    level = levels[previous[-1][1]] if previous else 0
    end = next((h.start() for h in headings if h.start() > mark.end() and levels[h[1]] <= level), len(text))
    return text[mark.end():end]


def validate(root):
    problems = []
    sources = {}

    def report(kind, detail):
        problems.append(f'{kind:<18}{detail}')

    def read_included(path):
        path = path.resolve()
        if path in sources:
            return
        if not path.is_relative_to(root):
            report('OUTSIDE BOOK', str(path))
            return
        if not path.is_file():
            report('MISSING FILE', str(path))
            return
        text = path.read_text(encoding='utf-8')
        sources[path] = text
        # Ignore inputs written as example code.
        scan = re.sub(r'\\begin\{(lstlisting|verbatim|Verbatim|minted)\}.*?\\end\{\1\}', '', strip_comments(text), flags=re.S)
        for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', scan):
            read_included(root / (name if name.endswith('.tex') else name + '.tex'))

    read_included(root / 'main.tex')
    chapters = [p for p,t in sources.items() if p != root/'main.tex' and r'\chapter{' in strip_comments(t)
                and not p.name.startswith(('00-', '98-', '99-'))]
    matrix = root / 'inventario/copertura.json'
    total = 0
    if matrix.is_file():
        try:
            data = json.loads(matrix.read_text(encoding='utf-8'))
        except (ValueError, OSError) as exc:
            report('INVALID MATRIX', str(exc))
            return problems, total
        if not isinstance(data, dict) or type(data.get('version')) is not int or data.get('version') != 1:
            report('INVALID MATRIX', 'Serve un oggetto con version: 1')
            return problems, total
        items = data.get('items')
        if not isinstance(items, list) or not items:
            report('INVALID MATRIX', 'items deve essere una lista non vuota')
            return problems, total
        ids, covered = set(), set()
        for i, item in enumerate(items, 1):
            total += 1
            if not isinstance(item, dict):
                report('INVALID ITEM', f'voce {i}: serve un oggetto')
                continue
            ident = item.get('id')
            if not isinstance(ident, str) or not ident.strip():
                report('INVALID ID', f'voce {i}')
                ident = f'voce {i}'
            elif ident in ids:
                report('DUPLICATE ID', ident)
            ids.add(ident)
            if not isinstance(item.get('content'), str) or not item['content'].strip():
                report('NO CONTENT', ident)
            refs = item.get('sources')
            if not isinstance(refs, list) or not refs or any(not isinstance(x,str) or not x.strip() for x in refs):
                report('NO SOURCE', ident)
            review = item.get('review')
            if not isinstance(review, dict) or review.get('status') != 'verified' or not isinstance(review.get('note'), str) or not review['note'].strip():
                report('UNREVIEWED', f'{ident}: serve review.status=verified e una nota del confronto')
            destinations = item.get('destinations')
            if not isinstance(destinations, list) or not destinations:
                report('NO DESTINATION', ident)
                continue
            bodies = []
            for dest in destinations:
                if not isinstance(dest, dict) or not isinstance(dest.get('file'), str) or not isinstance(dest.get('label'), str) or not dest['label'].strip():
                    report('BAD DESTINATION', ident)
                    continue
                rel = Path(dest['file'])
                path = (root / rel).resolve()
                if rel.is_absolute() or not path.is_relative_to(root) or path.suffix != '.tex':
                    report('BAD DESTINATION', f'{ident}: {rel}')
                    continue
                if path not in sources:
                    report('NOT INCLUDED', f'{ident}: {rel}')
                    continue
                body = labelled_body(sources[path], dest['label'])
                if body is None:
                    report('BROKEN LABEL', f'{ident}: {rel}: {dest["label"]}')
                    continue
                covered.add(path)
                bodies.append(prose(body))
            literals = item.get('literals', [])
            if not isinstance(literals, list) or any(not isinstance(x,str) or not x.strip() for x in literals):
                report('BAD LITERALS', ident)
            else:
                for literal in literals:
                    if not any(' '.join(literal.split()) in b for b in bodies):
                        report('MISSING LITERAL', f'{ident}: {literal}')
        for path in chapters:
            if path not in covered:
                report('UNCOVERED CHAPTER', str(path.relative_to(root)))
    else:
        files = sorted((root/'inventario').glob('[0-9][0-9].txt'))
        if not files:
            report('NO INVENTORY', 'Serve inventario/copertura.json o un inventario legacy NN.txt')
        for path in files:
            chapters_for_number = list((root/'capitoli').glob(path.stem+'-*.tex'))
            if len(chapters_for_number) != 1:
                report('NO CHAPTER', f'{path.name}: {len(chapters_for_number)} corrispondenze')
                continue
            chapter = chapters_for_number[0].resolve()
            if chapter not in sources:
                report('NOT INCLUDED', str(chapter.relative_to(root)))
                continue
            text = prose(sources[chapter]).casefold()
            for line in path.read_text(encoding='utf-8').splitlines():
                term = line.strip()
                if not term or term.startswith('#'):
                    continue
                total += 1
                if ' '.join(term.split()).casefold() not in text:
                    report('MISSING', f'{chapter.name}: {term}')
        for path in chapters:
            number = path.name[:2]
            if not (root/'inventario'/f'{number}.txt').is_file():
                report('NO INVENTORY', path.name)
    return problems, total


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1]).resolve()
    if not (root/'main.tex').is_file():
        sys.exit('main.tex assente')
    problems, total = validate(root)
    for problem in problems:
        print(problem)
    print(f'(info) voci controllate: {total}; confronto semantico: revisione manuale registrata, non verificata dal programma')
    print('problems:', len(problems))
    return bool(problems)


if __name__ == '__main__':
    sys.exit(main())
