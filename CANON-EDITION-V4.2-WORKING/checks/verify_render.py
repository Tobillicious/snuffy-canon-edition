#!/usr/bin/env python3
"""Verify the 4.2 renderings carry the citations unbroken and no door content.

Needles are matched after removing all whitespace, since renderers wrap lines
(and the PDF wraps the 64-character chain heads). Stdlib only; uses pdftotext
for the PDF and reads the EPUB as a zip archive.
"""
import html
import hashlib
import json
import re
import subprocess
import zipfile
import unicodedata
from pathlib import Path

R = Path(__file__).resolve().parents[1] / 'render'
B = 'Snuffy-Canon-Edition-4.2'
NEEDLES = {
    'chain_head_solvent': '6160d931d55767f39525671ff4ef8f3305b609cd22c6043cd9e0fb3eada69132',
    'chain_head_quarantine': 'd1a0d44bbad5a135928595e152a7a3e987e74a90017837e1491ad8b8430b0ef4',
    'chain_head_charged': '41143bb2756875b03975b1cbb7c5cd09e6e0ee495b06c29243624de52a6a2788',
    'doi_core': '10.5281/zenodo.23599528',
    'doi_canon_edition': '10.5281/zenodo.23608443',
    'canon_sentence': 'Uncompensated breach is deterministically impossible on the certified good event',
    'module_count': '192 modules and 1158 public theorem/lemma names',
    'joint_kernel_certificate': 'Exact joint kernel constraint and bounded residual',
    'gross_reset_cap': 'finite jump-budgeted primitive',
    'bounded_common_causes': 'specified physical jump causes',
}
DOOR_MARKERS = ['whakapapa', 'umuntu', 'ubuntu']


def norm(t, markup=False):
    if markup:
        t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', html.unescape(t)))


texts = {
    'pdf': subprocess.run(['pdftotext', str(R / f'{B}.pdf'), '-'], capture_output=True, text=True,
                          check=True).stdout,
    'html': (R / f'{B}.html').read_text(),
    'epub': ' '.join(zipfile.ZipFile(R / f'{B}.epub').read(n).decode('utf-8', 'ignore')
                     for n in zipfile.ZipFile(R / f'{B}.epub').namelist() if n.endswith('.xhtml')),
}
out = {}
for fmt, t in texts.items():
    n = norm(t, markup=fmt != 'pdf')
    out[fmt] = {k: norm(v) in n for k, v in NEEDLES.items()}
    out[fmt]['no_door_content'] = not any(m in t.lower() for m in DOOR_MARKERS)
    out[fmt]['bytes'] = (R / f'{B}.{fmt}').stat().st_size
pages = subprocess.run(['pdfinfo', str(R / f'{B}.pdf')], capture_output=True, text=True).stdout
out['pdf']['pages'] = int(re.search(r'Pages:\s+(\d+)', pages).group(1))
out['master_sha256'] = hashlib.sha256((R.parent / 'SNUFFY-CANON-EDITION-4.2-MASTER.md').read_bytes()).hexdigest()
out['render_sha256'] = {fmt: hashlib.sha256((R / f'{B}.{fmt}').read_bytes()).hexdigest() for fmt in ('pdf', 'html', 'epub', 'tex')}
out['method_note'] = 'Unicode and whitespace normalization; markup stripped only for HTML/EPUB, never from PDF inequality text'
out['all_pass'] = all(v for f in ('pdf', 'html', 'epub') for k, v in out[f].items() if isinstance(v, bool))
print(json.dumps(out, indent=2, sort_keys=True))
