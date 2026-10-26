#!/usr/bin/env python3
"""Show dependent status/count changes after batch 01; edit no canon prose."""
from pathlib import Path
import json

bank = Path(__file__).resolve().parent
root = bank.parents[1]
edition = root / 'SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25'
texts = {p: (edition / p).read_text() for p in
         ['SNUFFY-CANON-EDITION-4.2-MASTER.md', 'README.md', 'zenodo.json']}
for c in json.loads((bank / 'PROSE-BATCH-01.json').read_text()):
    assert c['before'] in texts[c['file']]
    texts[c['file']] = texts[c['file']].replace(c['before'], c['after'])
changes = []
master = 'SNUFFY-CANON-EDITION-4.2-MASTER.md'


def add(title, before, after, file=master):
    assert before in texts[file], title
    changes.append(dict(title=title, file=file, before=before, after=after,
                        occurrences=texts[file].count(before)))
    texts[file] = texts[file].replace(before, after)


def paragraph(start, file=master):
    matches = [p for p in texts[file].split('\n\n') if p.startswith(start)]
    assert len(matches) == 1, (start, len(matches))
    return matches[0]


add('Counts: bind 1,055 names only to the successful Lyapunov full receipt',
    '1042 audited public theorem/lemma names', '1055 audited public theorem/lemma names')
add('Counts: full axiom coverage', 'over all 1042 names', 'over all 1055 names')

add('Bennett implementation: distinguish the candidate from the canon model',
    'For an administration \\(f=h\\circ g\\), the specific reversible implementation',
    'The actual implementation below is a separately compiled and kernel-checked candidate '
    'in the repair bank (`drafts/Snuffy/BennettCounterpart.lean`); the canon still contains '
    'the earlier heat-only option model. It is not recorded as a completed physical '
    'counterpart repair. For an administration \\(f=h\\circ g\\), the candidate implementation')

add('README: candidate and current verified count',
    paragraph('This repair checkpoint keeps', 'README.md'),
    'This repair checkpoint keeps the full Universal Protection Theory target. The quantum '
    'holding state has normalisation, invariant and nonvacuity proofs. The defined '
    'reserve-deficit functional handles saturation and the complete solvent cycle. '
    'A separately checked Bennett candidate reproduces the administration with clean '
    'workspace and full retained history; its complete physical cost comparison remains '
    'open. The current canon has 169 modules and 1,055 audited names. Physical source, '
    'whole-outcome and external-theorem application certificates remain construction work. '
    'The repair reports and receipts distinguish these states.', 'README.md')

add('Zenodo: separately checked Bennett candidate',
    'The specific compute-copy-uncompute program implements the administration,',
    'A separately checked candidate compute-copy-uncompute program implements the administration,',
    'zenodo.json')
add('Zenodo: verified component count', '1,042 audited public theorems',
    '1,055 audited public theorems', 'zenodo.json')

old = texts['zenodo.json']
start = old.index('<li><strong>The fault ceiling.</strong>')
end = old.index('</li>', start) + len('</li>')
add('Zenodo: fault-ceiling application certificates', old[start:end],
    '<li><strong>The fault ceiling.</strong> The local-stochastic and bounded-footprint '
    'correlated-shock theorems give the target ceiling from their stated hypotheses. '
    'Their physical application still requires the selected code graph, noisy gadgets, '
    'preparation/readout and uniform coupling-to-noise certificates.</li>', 'zenodo.json')
add('Zenodo: cited theorem conditions require actual certificates',
    'cited as such and applied within their stated conditions:',
    'cited as such, with their actual application certificates still to be supplied:',
    'zenodo.json')

for old, new in [
 ('Premise 5 is **derived**: the Bennett counterpart is constructed, and the law forces reversible administration',
  'The full premise-5 target remains reversible administration. The canon proves the heat-only option-model result; its physical counterpart needs the actual lifecycle and deadline comparison'),
 ('**Derived:** the Bennett counterpart is constructed, and the law forces reversible administration (compiled, §23.6; G.14)',
  'Heat-only model compiled; actual implementation candidate checked; full lifecycle/deadline comparison remains the construction target (§23.6; G.14)'),
 ('The full-domain construction joining those inputs is G1, constructed in G.10, where all five `hcert` components are proved.',
  'G.10 proves the five `hcert` components on the held source. The full-domain G1 target additionally requires the actual installation/source correspondence and response device.'),
 ('G2 supplies its joined construction.',
  'G2 retains the target of identifying the physical policy/outcome family with the compiled local-component model.'),
 ('G2 supplies the full construction',
  'G2 retains the full physical policy/outcome correspondence as its construction target'),
 ('G1 is the combined full-domain source/event/observation/fault construction, proved in G.10.',
  'G1 is the combined full-domain source/event/observation/fault construction target; G.10 proves its held-source components and identifies the physical correspondence still needed.'),
 ('The installation\'s source refines the held source through the journal of G.8 (`G1FullDomain.journal_reactive_fidelity`).',
  'The journal of G.8 preserves its supplied transition (`G1FullDomain.journal_reactive_fidelity`); protective refinement of the actual installation is the separate transition equation identified in G.10.'),
]:
    add('Dependent manuscript status: ' + old[:65], old, new)

old = next(line for line in texts[master].splitlines()
           if line.startswith("* Bennett's reversible counterpart, now constructed:"))
add('23.8: actual Bennett cost comparison remains explicit', old,
    '* Bennett\'s compute/copy/uncompute identity and the heat-only option model are compiled. '
    'The specific implementation and full ordered history are separately checked candidates '
    '(G.14). The physical counterpart still needs a complete-cost saving within the same '
    'deadline; this is not supplied by a zero-heat identity or a polynomial upper bound;')

add('23.8: summary distinguishes cited and constructed components',
    'the Bennett counterpart is constructed (G.14);',
    'the Bennett physical comparison remains construction work (G.14);')

add('Theorem mapping: heat-model strictness versus complete physical cost',
    'Premise 5 derived: the Bennett counterpart is constructed (zero heat, same earlier outcomes and base cost, feasible with strictly more slack), and the law forces reversible administration',
    'Premise 5 in the heat-only model; the actual counterpart still needs a complete physical cost and deadline comparison')

old = paragraph('*Proof.* The actual error drift and repair bound,')
add('18.4: identify the checked component without claiming the remaining physical join', old,
    old + '\n\nThe compiled result establishes the defined storage inequality from the actual '
    'drift, repair and complete solvent balance. The full Theorem 8 statement retains '
    'all its conclusions. Applying it to the physical installation still joins the '
    'protective source dynamics, invariant/error bounds and complete work/entropy '
    'accounts; those application certificates are not inferred from the reserve plateau '
    'or from the iteration identity alone.')

old = paragraph('*Now constructed:* `G1Held`')
add('Construction register: actual G1 device and refinement remain explicit', old,
    '*Compiled held-source components:* `G1Held` and `G1E9` (G.10) prove their '
    'five-component certificate and event cover on the normalised held source. '
    '*Physical construction target:* the actual installation projection/transition, '
    'observations, timely correction and device enforcing removal of coupling after '
    'alarm, with its complete charge and named fault bounds.')

for key, after in [
 ('| `G2Splice` | Union-closed realisability',
  '| `G2Splice` | Product-model union closure and block agreement under closed-block inputs; the original physical policy/outcome correspondence remains the G2 target (G.9, G.11) |'),
 ('| `G1Held` | The held source with all five',
  '| `G1Held` | Held-source certificate, normalised quantum domain, frame invariants and concrete nonvacuity; actual installation refinement remains separate (G.10) |'),
 ('| `G2Held` | Authorised freedom',
  '| `G2Held` | Top of the assigned held-source grade model; full freedom/R17 delivery and physical outcome correspondence remain the G2 target (G.11) |'),
 ('| `BennettCounterpart` | The Bennett counterpart constructed:',
  '| `BennettCounterpart` | Heat-only option model; specific implementation/history candidate checked separately; complete physical cost and deadline comparison remains open (G.14) |'),
]:
    line = next(x for x in texts[master].splitlines() if x.startswith(key))
    add('23.9: ' + key.split('`')[1] + ' evidence scope', line, after)

old = paragraph('*Constructed (G.9, G.11).*')
add('G2 ledger: model top versus physical top', old,
    '*Compiled components (G.9, G.11).* `G2Splice` proves product-model union closure '
    'and closed-block agreement. `G2Held` proves the top of its assigned grade model from '
    'held continuation and its one-step H5 predicate. The full construction must map '
    'actual policies and outcomes to that model, preserving all original continuation '
    'and freedom stages, shared constraints and R17 delivery for every admitted rival '
    'and world. `hsolv` remains the separate complete funded-cost certificate.')

old = paragraph('*Now constructed:* `G2Splice`')
add('Construction register: G2 application remains explicit', old,
    '*Compiled components:* `G2Splice` and `G2Held` establish their stated local-product '
    'and grade-model results. *Physical construction target:* identify the actual full '
    'policy/outcome family and R17 delivery on the same execution. `hsolv` pays the '
    'complete cost and does not replace this realisability witness.')

dest = bank / 'PROSE-BATCH-02.json'
dest.write_text(json.dumps(changes, ensure_ascii=False, indent=2) + '\n')
lines = ['# Proposed manuscript changes — batch 02', '',
         'Read after batch 01. No manuscript is changed by this generator. '
         'Count/PASS updates are applied only after the 1,055-name full checkpoint passes. '
         'The full UPT target is retained; these status corrections do not replace it '
         'with a conditional or smaller target.', '']
for i, c in enumerate(changes, 1):
    lines += [f'## {i}. {c["title"]}', '', 'File: `' + c['file'] + '`', '',
              '**Before**', '', '```markdown', c['before'], '```', '',
              '**After**', '', '```markdown', c['after'], '```', '']
(bank / 'MANUSCRIPT-BEFORE-AFTER-BATCH-02.md').write_text('\n'.join(lines))
print(f'Prepared {len(changes)} dependent replacements; no manuscript files edited.')
