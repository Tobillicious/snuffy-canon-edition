#!/usr/bin/env python3
"""Prepare reviewable prose changes. This does not edit any manuscript file."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[2]
edition = root / 'SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25'
master = (edition / 'SNUFFY-CANON-EDITION-4.2-MASTER.md').read_text()
changes = []


def add(title, before, after, file='SNUFFY-CANON-EDITION-4.2-MASTER.md'):
    text = (edition / file).read_text()
    if text.count(before) != 1:
        raise ValueError((title, text.count(before)))
    changes.append(dict(title=title, file=file, before=before, after=after))


def between(start, end):
    return master.split(start, 1)[1].split(end, 1)[0]


old = master.splitlines()[8]
assert old.startswith('The three joined supports')
add('Edition status: preserve the full target and distinguish the joins', old,
    'The three joined supports retain their full targets: the full-domain physical certificate '
    '(G1), realisability of the whole continuation-and-freedom tuple (G2), and recovery success '
    'with a complete pathwise work certificate (G3). This repair checkpoint corrects the '
    'normalised quantum-state domain and the clipped-reserve contraction, and develops the '
    'actual Bennett implementation. The physical source, whole-outcome, device-cost and '
    'external-theorem application correspondences remain explicit construction work; '
    'the component theorems do not by themselves declare the maximal argument complete.')

start = '#### The Master Storage / Lyapunov Functional\n'
end = '### 18.4 Theorem 8 (Complete Physical Accounting Statement)'
old = between(start, end)
new = r'''Define the actual storage functional
\[
\Phi(\rho,E)=\mathcal E_{\mathrm{code}}(\rho)+f(E),\qquad
f(E)=\frac{\max(0,W_{\mathrm{target}}-E)}{W_0},\quad W_0>0.
\]
The storage capacity \(K\) is chosen at least as large as the required reserve target.
For nonnegative income \(I\), replenishment gives
\[
E^+=\min(K,E+I),\qquad
f(E^+)-f(E)=-\min\{I/W_0,f(E)\}.
\]
Thus replenishment clears at most the existing deficit. Additional income does not
drive the clipped term below zero (`TheoremEightLyapunov.replenishment_exact`).

Let \(W_{\mathrm{cycle}}\) be the complete realised cycle charge, including
measurement, correction, reset, holding, guard, routing, verification and controller
work. Its physical escrow balance is
\[
E_{n+1}=\min(K,E_n-W_{\mathrm{cycle}}+I_n).
\]
The excess \(S_n=\max(0,E_n-W_{\mathrm{cycle}}+I_n-K)\) is explicitly exported:
\[
E_{n+1}+W_{\mathrm{cycle}}+S_n=E_n+I_n.
\]
`capacity_balance` and `solvent_cycle_energy_account` prove these identities.
Within-cycle reservations still fund every operation before it executes.

If \(W_{\mathrm{cycle}}\le I_n\), the reserve term does not increase
(`solvent_cycle_deficit`). The actual error drift and correction give
\[
\mathcal E_{\mathrm{drift}}\le\mathcal E_n+\lambda\tau,\qquad
\mathcal E_{n+1}\le\mathcal E_{\mathrm{drift}}-\eta C.
\]
Therefore the defined functional obeys
\[
\Phi_{n+1}-\Phi_n\le-(\eta C-\lambda\tau).
\]
`cycle_contracts` proves this from the realised error bounds and complete solvent
balance. For positive margin the contraction is strict on the stated error cycles.
The controller supplies its tracking rate; the reserve plateau does not imply an
additional exponential convergence theorem.

---

'''
add('18.3: exact saturated replenishment and complete cycle balance', old, new)

old = next(p for p in master.split('\n\n')
           if p.startswith('*Proof.* The stroke-by-stroke balance equations (18.2)'))
add('18.4: proof using the actual functional', old,
    '*Proof.* The actual error drift and repair bound, together with the complete solvent '
    'escrow balance of §18.3, give the cycle change at most '
    r'\(-(\eta C-\lambda\tau)\) (`TheoremEightLyapunov.cycle_contracts`). '
    'The reserve-deficit term is handled through saturation and is nonincreasing over the '
    'cycle; no linear replenishment descent past zero is assumed. Timeliness gives '
    r'\(\sigma_0=\eta C-\lambda\tau>0\) (`margin_pos`), and the cycle recurrence gives '
    r'\(\Phi_n\le\Phi_0-n\sigma_0\) over the stated error cycles (`lyapunov_iterate`). '
    'The physical holding and entropy-export certificates retain their separate roles. '
    r'$\blacksquare$')

old = between('**The Theorem 8 storage functional contracts**', '**The smearing integral is exact**')
new = r''' (`TheoremEightLyapunov`, §18.3–18.4). The functional is defined as code
error plus the clipped reserve deficit. Exact replenishment saturates at zero deficit
(`replenishment_exact`), and capacity overflow is retained in the energy account
(`solvent_cycle_energy_account`). A complete solvent cycle cannot increase the
reserve term (`solvent_cycle_deficit`). Combining this with the actual error drift
and repair gives the positive-margin contraction (`cycle_contracts`, `margin_pos`)
and its stated iteration (`lyapunov_iterate`).

'''
add('G.13: corrected Lyapunov join', old, new)

old = between('**Correspondence to an installation.**', '## G.11 The held source realises')
new = r''' The quantum held source uses the physical state type \(\|v\|=1\).
Initialisation, the held step and every reached frame preserve normalisation
(`initial_frame_normalised`, `held_step_normalised`, `held_run_normalised`).
The zero-Hamiltonian trajectory, concrete record \(1\in\mathbb C\), singleton
decoder and inhabited good event supply a nonvacuous instance.

For an installation transition \(T\), protection transfers through an actual
projection \(p\) satisfying
\[
p(T(s,c,e))=\operatorname{heldStep}(p(s),c,e),
\]
together with observation agreement, initial continuation, the physical perturbation
bound and the implemented repair precision. The journal theorem preserves its supplied
transition \(T\); it supplies the logging part of this correspondence after the
protective transition equation is proved. The guarded-source construction must join
the nominal/correction branches, response latency and complete charge to that same
physical execution. The full G1 target remains this combined certificate.

'''
add('G.10: normalisation and actual protective refinement', old, new)

old = between('## G.11 The held source realises the whole top outcome (G2 from G1)\n',
              '## G.12 The wavefront sweep succeeds')
new = r'''
The G2 target is the complete original tuple \((L_E,F_E,L_N,F_N)\), including
continuation in each particular's own direction and timely authorised opportunities.
The transaction record \((h_{\mathrm{pre}},h_{\mathrm{post}},w,a,c)\) records an
execution certificate; it does not replace this outcome tuple.

`G2Splice` proves union closure in its local-component policy model and proves block
agreement under its closed-block hypotheses. `G2Held` obtains the top of its graded
model from continuation and its one-step H5 opportunity predicate. The full physical
application must identify that model with the original realised policy/outcome family,
including interacting records, the shared constraints and successful R17 delivery on
the same trace. The author's bounded-crosstalk route supplies a construction direction:
derive its decoded joint-state error bound, prove correction on the named good event,
and transport the original continuation and freedom semantics through the resulting
execution correspondence. Sub-threshold noise alone is not an exact factorisation.

The full top witness `htopR` remains the target of that construction; `hsolv` remains
its separate complete funded-cost certificate. Neither target is reduced.

'''
add('G.11: preserve the original physical outcome target', old, new)

old = between('## G.14 Premise 5 with the Bennett counterpart constructed\n', '## G.15 Recovered')
new = r'''
For an administration \(f=h\circ g\), the specific reversible implementation
first computes, copies and uncomputes, then exchanges the output and live registers:
\[
(s,0,0)\longmapsto(f(s),0,s).
\]
`implementedProgram` and `implemented_program_computes` identify the implemented
administration, clean workspace and full retained input. `implemented_run_refines`
proves its trajectory correspondence and one retained input record per step.
`quantumProgram` is the induced unitary with an arbitrary reference register untouched;
its norm and round trip are preserved. An arbitrary bijection is not used as a
substitute for implementing \(f\).

The complete physical lifecycle also pays provisioning, compute/copy/uncompute,
archive writing and holding, routing, reset, guard, controller, verification and
endpoints. If \(B_{\rm rev},B_{\rm irr}\) are the complete non-heat charges and
\(Q_{\rm irr}\) the saved bath heat, the exact difference is
\[
W_{\rm rev}-W_{\rm irr}=B_{\rm rev}-B_{\rm irr}-Q_{\rm irr}
\]
(`complete_cost_difference`). Strictly more slack requires the implemented lifecycle
penalty to be less than the saved heat (`complete_cost_strict_iff`), while meeting the
same deadline. The adiabatic route must establish a switching-time window satisfying
both bounds (`adiabatic_slack_window`, `switched_program_meets_deadline`).

A fixed circuit multiplier and an actual full archive allowance preserve the original
polynomial exponent (`implemented_work_ceiling`). That upper bound does not by itself
establish the strict complete-cost comparison. The earlier heat-only option model and
Landauer results remain their stated mathematical components; completion of the
physical counterpart claim requires this lifecycle and deadline comparison for the
full intended class. The original premise-5 target remains fixed.

'''
add('G.14: actual implementation and exact remaining cost comparison', old, new)

old = next(p for p in (edition / 'README.md').read_text().split('\n\n')
           if p.startswith('This edition constructs the holding certificate in full.'))
new = ('This repair checkpoint keeps the full Universal Protection Theory target. '
       'The quantum holding state is normalised, with invariant and nonvacuity proofs; '
       'the reserve-deficit contraction handles saturation; and the Bennett program '
       'implements the administration with clean workspace and retained history. '
       'The physical-source, whole-outcome, complete lifecycle and external-theorem '
       'application certificates remain explicit work. Section 23 and the receipts '
       'record the compiled component theorems and their exact verification state.')
add('README summary: precise repair status', old, new, 'README.md')

description = json.loads((edition / 'zenodo.json').read_text())['description']


def html_block(start, end):
    first = description.index(start)
    last = description.index(end, first) + len(end)
    return description[first:last]


add('Zenodo bridge summary',
    html_block('<p><strong>The bridge to every mind.</strong>', '</p>'),
    '<p><strong>The bridge to every mind.</strong> The target remains reasons or faithful '
    'holding for every mind, including a bounded indifferent defector. The normalised held '
    'source has explicit invariant and nonvacuity proofs. Application to the complete '
    'physical domain joins the actual guarded-source transition, observations, timely '
    'correction, complete funding and named fault bounds. Journal fidelity preserves the '
    'transition it is given; the protective refinement is a separate construction. A hostile '
    'mind remains in the protected scope while its harmful channels are restrained.</p>',
    'zenodo.json')

add('Zenodo whole-outcome summary',
    html_block('<p><strong>Greatestness.</strong>', '</p>'),
    '<p><strong>Greatestness.</strong> The full outcome target includes all continuation and '
    'freedom stages and every admitted rival. The local-product and held-source models have '
    'compiled greatestness results. Their physical application must identify the original '
    'policy/outcome family and join successful R17 delivery on the same execution. The '
    'whole top witness and its complete funded cost retain their separate roles.</p>',
    'zenodo.json')

add('Zenodo storage-functional summary',
    html_block('<li><strong>The funded thermodynamic ledger.</strong>', '</li>'),
    '<li><strong>The funded thermodynamic ledger.</strong> Landauer and the entropy-export '
    'guard remain compiled components. The repaired storage functional uses a clipped '
    'reserve deficit, exact saturated replenishment and a complete cycle energy balance. '
    'A solvent cycle cannot increase its reserve term; the actual error drift and repair '
    'then give the stated positive-margin contraction.</li>', 'zenodo.json')

add('Zenodo complete recovery-work summary',
    html_block('<li><strong>Source identification and recovery work.</strong>', '</li>'),
    '<li><strong>Source identification and recovery work.</strong> The retained information, '
    'traffic, carrier and transport chain supplies the recovery-work lower bound. The '
    'one-pass shell calculation and conditional sweep/work theorems support the matching '
    'construction. The complete physical patch, fence, capacity, precision and pathwise '
    'bill are the remaining application certificates for the unchanged tight work target.</li>',
    'zenodo.json')

add('Zenodo Bennett summary',
    html_block('<li><strong>Reversible administration.</strong>', '</li>'),
    '<li><strong>Reversible administration.</strong> The specific compute-copy-uncompute '
    'program implements the administration, returns its workspace and retains its full '
    'input history. Its trajectory and quantum permutation are explicit. The complete '
    'lifecycle comparison must establish the saved heat exceeds the additional charges '
    'within the same deadline; a polynomial work ceiling alone does not prove this.</li>',
    'zenodo.json')

dest = Path(__file__).resolve().parent
(dest / 'PROSE-BATCH-01.json').write_text(json.dumps(changes, indent=2, ensure_ascii=False) + '\n')
lines = ['# Proposed manuscript changes — batch 01', '',
         'Author review required before application, as requested in the repair brief. '
         'This document changes no manuscript. The full target is preserved. '
         'Code candidates are individually compiled/kernel-checked; the G1 full audit is running. '
         'Generated theorem index/count updates follow successful receipts separately.', '']
for i, c in enumerate(changes, 1):
    lines += [f'## {i}. {c["title"]}', '', f'File: `{c["file"]}`', '',
              '**Before**', '', '```markdown', c['before'].strip(), '```', '',
              '**After**', '', '```markdown', c['after'].strip(), '```', '']
(dest / 'MANUSCRIPT-BEFORE-AFTER-BATCH-01.md').write_text('\n'.join(lines))
print(f'Prepared {len(changes)} replacements; no manuscript files edited.')
