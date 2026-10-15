"""Embed shared assets in the RDF lesson so the HTML also works by itself.

Run from any directory: python3 -I assets/build-rdf-lesson.py
Shared CSS and JS stay the editable sources; rerun after updating them.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
lesson = ROOT / 'lessons/0001-rdf-dalle-frasi-alle-triple.html'
html = lesson.read_text(encoding='utf-8')
css = (ROOT / 'assets/teaching.css').read_text(encoding='utf-8')
js = (ROOT / 'assets/rdf-practice.js').read_text(encoding='utf-8')
assert '</script' not in js.lower() and '</style' not in css.lower()

html = re.sub(r'<link rel="stylesheet" href="../assets/teaching.css">|<style id="lesson-styles">.*?</style>',
              lambda _: '<style id="lesson-styles">\n' + css + '\n</style>', html, flags=re.S)
# Inline scripts run at their position; put this after all forms, not in head.
html = re.sub(r'<script defer src="../assets/rdf-practice.js"></script>|<script id="lesson-practice">.*?</script>', '', html, flags=re.S)
html = html.replace('</body>', '<script id="lesson-practice">\n' + js + '\n</script>\n</body>')
# A missing/disabled handler must not turn a check into a page navigation.
html = re.sub(r'<form (?!onsubmit=)', '<form onsubmit="return false" ', html)
lesson.write_text(html, encoding='utf-8')
print('Built standalone lesson:', lesson.name)
