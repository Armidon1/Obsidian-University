"""Embed shared assets in a lesson so the HTML also works by itself.

Run from any directory:
    python3 -I assets/build-rdf-lesson.py                      # lesson 0001 + rdf-practice.js
    python3 -I assets/build-rdf-lesson.py lessons/X.html assets/quiz.js [assets/more.js ...]
Shared CSS and JS stay the editable sources; rerun after updating them.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
args = sys.argv[1:] or ['lessons/0001-rdf-dalle-frasi-alle-triple.html', 'assets/rdf-practice.js']
lesson = ROOT / args[0]
scripts = [ROOT / a for a in args[1:]]
html = lesson.read_text(encoding='utf-8')
css = (ROOT / 'assets/teaching.css').read_text(encoding='utf-8')
js = '\n'.join(sc.read_text(encoding='utf-8') for sc in scripts)
assert '</script' not in js.lower() and '</style' not in css.lower()

html = re.sub(r'<link rel="stylesheet" href="../assets/teaching.css">|<style id="lesson-styles">.*?</style>',
              lambda _: '<style id="lesson-styles">\n' + css + '\n</style>', html, flags=re.S)
# Inline scripts run at their position; put this after all forms, not in head.
for sc in scripts:
    html = re.sub(r'<script defer src="../assets/' + re.escape(sc.name) + r'"></script>', '', html)
html = re.sub(r'<script id="lesson-practice">.*?</script>', '', html, flags=re.S)
html = html.replace('</body>', '<script id="lesson-practice">\n' + js + '\n</script>\n</body>')
# A missing/disabled handler must not turn a check into a page navigation.
html = re.sub(r'<form (?!onsubmit=)', '<form onsubmit="return false" ', html)
lesson.write_text(html, encoding='utf-8')
print('Built standalone lesson:', lesson.name)
