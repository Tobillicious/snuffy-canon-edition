#!/usr/bin/env python3
"""Assembly integration checks for SNUFFY-CANON-EDITION-MASTER.md.

Verifies, per the assembly briefing: the seven premises, the four integration
guards, the five rate components of the Master Solvency Condition, the sealed
ledger chain heads verbatim, the published DOI, and the ratified canon sentence.
Deterministic; stdlib only; prints one JSON verdict.
"""
import json
import re
from pathlib import Path

MASTER = Path(__file__).resolve().parents[1] / 'SNUFFY-CANON-EDITION-MASTER.md'

PREMISES = ['BCRD P1', 'Turing–Deutsch', 'cost model', 'shared action interface',
            'reversible administration', 'Master Solvency Condition', 'twenty-one charged']

GUARDS = ['Integration guard 1', 'Integration guard 2', 'Integration guards 3 and 4']

RATES = ['W_{\\mathrm{maint}}', 'W_{\\mathrm{damage}}', 'W_{\\mathrm{admin}}',
         'W_{\\mathrm{adv,sub}}', 'W_{\\mathrm{hold}}']

CHAIN_HEADS = {
    'solvent': '6160d931d55767f39525671ff4ef8f3305b609cd22c6043cd9e0fb3eada69132',
    'quarantine': 'd1a0d44bbad5a135928595e152a7a3e987e74a90017837e1491ad8b8430b0ef4',
    'charged': '41143bb2756875b03975b1cbb7c5cd09e6e0ee495b06c29243624de52a6a2788',
}

text = MASTER.read_text()


def count(needle):
    return text.count(needle)


out = {
    'master': MASTER.name,
    'premises_present': {p: count(p) > 0 for p in PREMISES},
    'guards_present': {g: count(g) > 0 for g in GUARDS},
    'five_rate_components_present': {r.replace('\\', ''): count(r) > 0 for r in RATES},
    'solvency_equation_rendered': count('Income}(t)') > 0,
    'chain_heads_verbatim': {k: v in text for k, v in CHAIN_HEADS.items()},
    'ledger_directory_cited': count('LEDGER-FOUR-STROKE-2026-10-24') >= 2,
    'published_doi_cited': '10.5281/zenodo.23599528' in text,
    'canon_sentence_rendered': 'Uncompensated breach is deterministically impossible on the certified good event' in text,
    'mirror_qualifier_present': 'exact stage-1–5 mirrors' in text,
    'bennett_form_present': count('Landauer') >= 4 and 'Bennett' in text,
    'word_count': len(text.split()),
}
out['all_pass'] = all(v for k, v in out.items() if isinstance(v, bool))
out['all_pass'] = out['all_pass'] and all(out['premises_present'].values()) \
    and all(out['guards_present'].values()) and all(out['five_rate_components_present'].values()) \
    and all(out['chain_heads_verbatim'].values())
print(json.dumps(out, indent=2, sort_keys=True))
