"""Embed shared assets in a lesson so the HTML also works by itself.

    python3 -I assets/build-lesson.py lessons/X.html [assets/quorum.js ...]

All assets/*.css are embedded; the JS files named on the command line too.
Edit the assets, then rerun: never edit the embedded copies by hand.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
lesson = ROOT / sys.argv[1]
scripts = [ROOT / a for a in sys.argv[2:]]
html = lesson.read_text(encoding='utf-8')
css = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT / 'assets').glob('*.css')))
js = '\n'.join(p.read_text(encoding='utf-8') for p in scripts)
assert '</script' not in js.lower() and '</style' not in css.lower()

html = re.sub(r'<link rel="stylesheet" href="../assets/teaching.css">|<style id="lesson-styles">.*?</style>',
              lambda _: '<style id="lesson-styles">\n' + css + '\n</style>', html, flags=re.S)
html = re.sub(r'<script id="lesson-practice">.*?</script>\n?', '', html, flags=re.S)
if js:
    html = html.replace('</body>', '<script id="lesson-practice">\n' + js + '\n</script>\n</body>')
lesson.write_text(html, encoding='utf-8')
print('Built standalone lesson:', lesson.name)
