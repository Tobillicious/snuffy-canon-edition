#!/bin/bash
# Render SNUFFY-CANON-EDITION-4.2-MASTER.md to TeX/PDF (xelatex), HTML and EPUB (MathML).
set -euo pipefail
cd "$(dirname "$0")/.."
M=SNUFFY-CANON-EDITION-4.2-MASTER.md
B=render/Snuffy-Canon-Edition-4.2
T="Snuffy — Canon Edition 4.2"
pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" -s --toc -V geometry:margin=1in -V mainfont="STIXGeneral" -V mathfont="STIX Two Math" \
  -V monofont="Menlo" -M title="Snuffy — Canon Edition 4.2" -M subtitle="The Universal Protection Theory: the law, its bridge, its instruments, and its machine-checked canon" -M author="Tobias Croydon-McRae" -M date="26 October 2026" -V colorlinks=true -V linkcolor=blue -H checks/render-header.tex --lua-filter=checks/breakable-code.lua -M pagetitle="$T" -o "$B.tex"
( cd render && for i in 1 2 3; do xelatex -interaction=nonstopmode -halt-on-error "$(basename $B).tex" > xelatex.log 2>&1; done )
if grep -q "Missing character" render/*.log; then grep "Missing character" render/*.log | sort | uniq -c; exit 3; fi
pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" -s --math-method=mathml --toc -M pagetitle="$T" -M lang=en -o "$B.html"
pandoc -f markdown+tex_math_single_backslash+lists_without_preceding_blankline "$M" --math-method=mathml --toc -M title="$T" -M author="Tobias Croydon-McRae" -M lang=en \
  -M date="2026-10-26" -o "$B.epub"
rm -f render/*.aux render/*.out render/*.toc
ls -la render
