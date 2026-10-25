# Proposed manuscript changes — batch 01

Author review required before application, as requested in the repair brief. This document changes no manuscript. The full target is preserved. Code candidates are individually compiled/kernel-checked; the G1 full audit is running. Generated theorem index/count updates follow successful receipts separately.

## 1. Edition status: preserve the full target and distinguish the joins

File: `SNUFFY-CANON-EDITION-4.2-MASTER.md`

**Before**

```markdown
The three joined supports are constructed in Part III-G and recorded in Part III-C: the full-domain physical certificate (G1; G.10), the realisability of the whole greatest outcome tuple (G2; G.9, G.11), and the wavefront protocol's success and complete-work certificate (G3; G.12). Their targets are unchanged. Naming an input or relabelling a conclusion does not supply its construction.
```

**After**

```markdown
The three joined supports retain their full targets: the full-domain physical certificate (G1), realisability of the whole continuation-and-freedom tuple (G2), and recovery success with a complete pathwise work certificate (G3). This repair checkpoint corrects the normalised quantum-state domain and the clipped-reserve contraction, and develops the actual Bennett implementation. The physical source, whole-outcome, device-cost and external-theorem application correspondences remain explicit construction work; the component theorems do not by themselves declare the maximal argument complete.
```

## 2. 18.3: exact saturated replenishment and complete cycle balance

File: `SNUFFY-CANON-EDITION-4.2-MASTER.md`

**Before**

```markdown
Define the unified autonomic storage functional $\Phi$ over system state, escrow reserve, and bath entropy:
$$\boxed{\Phi(\rho_S, E_{\mathrm{escrow}}) \equiv \mathcal{E}_{\mathrm{code}}(\rho_S) + \frac{1}{\mathcal{W}_0} \max\left(0, W_{\mathrm{target}} - E_{\mathrm{escrow}}\right)}$$
where $W_{\mathrm{target}}$ is the required safety reserve floor, and $\mathcal{W}_0$ is a scale calibration constant.

#### Cycle Ledger Accounting:
1. **Noise / Drift Interval:**
   $\Delta_{\mathrm{drift}} \Phi = \Delta_{\mathrm{drift}} \mathcal{E}_{\mathrm{code}} \le \lambda_{\mathrm{decay}} \tau_{\mathrm{cycle}}$.
2. **Stroke I (Measurement):**
   $\Delta_{\mathrm{I}} \Phi \le \frac{W_{\mathrm{meas}}}{\mathcal{W}_0}$.
3. **Stroke II (Feedback):**
   $$\Delta_{\mathrm{II}} \Phi = -\eta C < 0$$
   Error is instantaneously eliminated in the code degree of freedom.
4. **Stroke III (Reset):**
   $\Delta_{\mathrm{III}} \Phi \le \frac{W_{\mathrm{reset}}}{\mathcal{W}_0}$, while bath absorbs $\Delta S_B \ge I_M$.
5. **Stroke IV (Solvent Replenishment):**
   $$\Delta_{\mathrm{IV}} \Phi \le -\frac{W_{\mathrm{income}}}{\mathcal{W}_0} \le -\frac{W_{\mathrm{meas}} + W_{\mathrm{reset}}}{\mathcal{W}_0}$$

#### Net Cycle Change:
Summing all four strokes over $\tau_{\mathrm{cycle}}$:
$$\Delta_{\mathrm{cycle}} \Phi \le -\eta C + \lambda_{\mathrm{decay}} \tau_{\mathrm{cycle}} - \frac{W_{\mathrm{income}} - W_{\mathrm{demand}}}{\mathcal{W}_0}$$
Under the standard design condition that cycle time is faster than error accumulation ($\tau_{\mathrm{cycle}} < \frac{\eta C}{\lambda_{\mathrm{decay}}}$) and the solvency condition ($W_{\mathrm{income}} \ge W_{\mathrm{demand}}$):
$$\boxed{\Delta_{\mathrm{cycle}} \Phi \le -\sigma_0 < 0 \quad \text{whenever } \mathcal{E}_{\mathrm{code}} > 0}$$
and $\Delta_{\mathrm{cycle}} \Phi = 0$ on the certified invariant manifold $\mathcal{C}$ with full escrow.

---
```

**After**

```markdown
Define the actual storage functional
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
```

## 3. 18.4: proof using the actual functional

File: `SNUFFY-CANON-EDITION-4.2-MASTER.md`

**Before**

```markdown
*Proof.* The stroke-by-stroke balance equations (18.2) give the cycle bound, and the contraction is compiled: the cycle change is at most \(-(\eta C-\lambda\tau)\) (`TheoremEightLyapunov.cycle_contracts`), timeliness makes \(\sigma_0=\eta C-\lambda\tau>0\) (`margin_pos`), and \(n\) error cycles lower \(\Phi\) by at least \(n\sigma_0\) (`lyapunov_iterate`). $\blacksquare$
```

**After**

```markdown
*Proof.* The actual error drift and repair bound, together with the complete solvent escrow balance of §18.3, give the cycle change at most \(-(\eta C-\lambda\tau)\) (`TheoremEightLyapunov.cycle_contracts`). The reserve-deficit term is handled through saturation and is nonincreasing over the cycle; no linear replenishment descent past zero is assumed. Timeliness gives \(\sigma_0=\eta C-\lambda\tau>0\) (`margin_pos`), and the cycle recurrence gives \(\Phi_n\le\Phi_0-n\sigma_0\) over the stated error cycles (`lyapunov_iterate`). The physical holding and entropy-export certificates retain their separate roles. $\blacksquare$
```

## 4. G.13: corrected Lyapunov join

File: `SNUFFY-CANON-EDITION-4.2-MASTER.md`

**Before**

```markdown
(`TheoremEightLyapunov`,
§18.3–18.4). Take the stroke bounds of §18.3 and solvency
\(W_{\mathrm{meas}}+W_{\mathrm{reset}}\le W_{\mathrm{income}}\). The cycle
change of \(\Phi\) is then at most \(-(\eta C-\lambda\tau)\)
(`cycle_contracts`). Timeliness \(\tau<\eta C/\lambda\) makes the margin
\(\sigma_0=\eta C-\lambda\tau\) positive (`margin_pos`). Over \(n\) cycles
containing an error, \(\Phi\) falls by at least \(n\sigma_0\)
(`lyapunov_iterate`).
```

**After**

```markdown
(`TheoremEightLyapunov`, §18.3–18.4). The functional is defined as code
error plus the clipped reserve deficit. Exact replenishment saturates at zero deficit
(`replenishment_exact`), and capacity overflow is retained in the energy account
(`solvent_cycle_energy_account`). A complete solvent cycle cannot increase the
reserve term (`solvent_cycle_deficit`). Combining this with the actual error drift
and repair gives the positive-margin contraction (`cycle_contracts`, `margin_pos`)
and its stated iteration (`lyapunov_iterate`).
```

## 5. G.10: normalisation and actual protective refinement

File: `SNUFFY-CANON-EDITION-4.2-MASTER.md`

**Before**

```markdown
The installation's source refines the
held source through the journal of G.8: every source transition is retained
and replayed exactly, for every controller and environment
(`G1FullDomain.journal_reactive_fidelity`). The R14/R16/R17 source bindings
supply its concrete safe transitions, causal cuts and timely authorised
effects. The domain is every particular; coverage is forced by the law
(`Bridge.coverage_from_law`).
```

**After**

```markdown
The quantum held source uses the physical state type \(\|v\|=1\).
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
```

## 6. G.11: preserve the original physical outcome target

File: `SNUFFY-CANON-EDITION-4.2-MASTER.md`

**Before**

```markdown
Freedom in the canonical order is continuation in the particular's own
direction, together with its authorised opportunities (II.1–II.2). For an
agent in the H5 ledger, every non-harmful effect it issues is an admissible
step. That step applies the effect and leaves every agent's status,
authority and escrow unchanged (`H5Closure.effect_preserves_care`). Every
active agent is therefore free in this sense
(`G2Held.active_authorised_free`): all of its authorised opportunities are
open, and restraint removes only harmful channels. A particular with no
command channel has no opportunity beyond continuing under its own dynamics.
The held source keeps exactly that, since each record is stationary under the
particular's own Hamiltonian (G.10).

Grade each particular 2 when it continues on the held source and is free.
`G2Held.held_realises_top` then applies `G2Splice.fourStage` with three
conclusions. The whole four-stage top \((L_E,F_E,L_N,F_N)\) is in the
realised family. The family is union-closed. Every aligned option of the
funded family is that top and contains every outcome tuple.
`G2Held.held_source_top` supplies continuation from
`G1Held.held_source_protection`, on the good event at every step through the
horizon, and agent freedom from the active H5 ledger. The G2 input `htopR` is
thereby derived from the held source, and `hsolv` remains its funded-cost
certificate (Sections 18 and 22).
```

**After**

```markdown
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
```

## 7. G.14: actual implementation and exact remaining cost comparison

File: `SNUFFY-CANON-EDITION-4.2-MASTER.md`

**Before**

```markdown
`Bennett.premise5_from_bennett` took the counterpart's properties as
hypotheses. Here the counterpart is constructed, and each of those properties
is proved (`BennettCounterpart`).

An option is a policy together with the implementation of its administration.
The implementation is either irreversible or reversible. An irreversible
implementation is a joint register–bath dynamics that leaves the register in
the law of an overwrite \(f\). A reversible implementation is a bijection of
the register alone. The Bennett cycle `Bennett.bennettEquiv` is one; it writes
\(f(a)=h(g(a))\) into a clean output and returns the workspace to zero
(`bennett_counterpart_computes`). An option's cost is its policy's base cost
plus the energy its administration delivers to the bath (`Landauer.heat`). Its
outcome stages before the resource stage \(j\) are the policy's outcomes.
Stage \(j\) reads the residual slack \(B-\mathrm{cost}\) through a strictly
monotone map. The counterpart of an option runs the same policy with
reversible administration.

- *Zero heat.* Reversible administration delivers exactly zero heat
  (`counterpart_heat_zero`, from `Bennett.heat_reversible`).
- *Positive heat.* An irreversible overwrite that merges two register states
  of positive probability delivers strictly positive heat
  (`merging_heat_pos`, from `Bennett.heat_irreversible`).
- *Same earlier outcomes and same base cost.* The counterpart agrees with the
  option before stage \(j\) (`counterpart_same`) and runs the same policy, so
  its base cost is unchanged. Its only cost difference is the delivered heat,
  which is zero.
- *Feasible, with strictly more slack.* Whenever the option is feasible, the
  counterpart is feasible (`counterpart_feasible`) and has strictly more slack
  at stage \(j\) (`counterpart_more_slack`).

Therefore no canonical option has merging irreversible administration
(`premise5_constructed`). The law forces reversible administration from the
Landauer model and the constructed Bennett cycle, with no hypothesis about
the counterpart.
```

**After**

```markdown
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
```

## 8. README summary: precise repair status

File: `README.md`

**Before**

```markdown
This edition constructs the holding certificate in full. On the held source every particular is kept against any agent of bounded coupling, and every component of the protection theorem's source certificate is proved. The whole greatest outcome is realised, with union closure derived from locality. Recovery work is Θ(t^d): a wavefront sweep is proved to succeed, with a complete metered bill. The fault ceiling is attained, correlated bursts included. Bennett's reversible counterpart is constructed. 169 Lean 4 modules and 1,042 audited theorems machine-check the argument. Section 23 maps every compiled result to its theorem and lists exactly what each rests on.
```

**After**

```markdown
This repair checkpoint keeps the full Universal Protection Theory target. The quantum holding state is normalised, with invariant and nonvacuity proofs; the reserve-deficit contraction handles saturation; and the Bennett program implements the administration with clean workspace and retained history. The physical-source, whole-outcome, complete lifecycle and external-theorem application certificates remain explicit work. Section 23 and the receipts record the compiled component theorems and their exact verification state.
```

## 9. Zenodo bridge summary

File: `zenodo.json`

**Before**

```markdown
<p><strong>The bridge to every mind.</strong> For each mind the bridge is reasons or holding. The reasons route derives protection from a mind's own objective: reciprocity, irreplaceable knowledge, option value under value uncertainty, and the cost of controlling living systems. Reciprocity is stated with its charged allowance: the canonical regime keeps a mind with probability at least one minus the fault ceiling, and exceeds any rival that loses the mind more often than that. The holding route keeps every mind those reasons do not reach, including a bounded indifferent defector. The holding certificate is now constructed in full. On the held source, each particular's record is perturbed by the world and by any agent, decoded to its nearest codeword and repaired. Every component of the protection theorem's source certificate is proved: refinement, observation agreement, initial continuation, the decoding-radius bound and repair precision. The per-step drift follows from the quantum speed limit for any perturbing agent of bounded coupling. That coupling bound follows from an exhaustive split: either every monitored site is below threshold, or honest sensors force a robust-quorum alarm, whatever the faulty sensors report, and the mediated response removes the coupling. On the certified good event every particular continues at every step through the horizon; the good event fails with probability at most the sum of the charged fault accounts, with no independence assumed. A hostile mind remains a protected particular while its harmful channels are fenced.</p>
```

**After**

```markdown
<p><strong>The bridge to every mind.</strong> The target remains reasons or faithful holding for every mind, including a bounded indifferent defector. The normalised held source has explicit invariant and nonvacuity proofs. Application to the complete physical domain joins the actual guarded-source transition, observations, timely correction, complete funding and named fault bounds. Journal fidelity preserves the transition it is given; the protective refinement is a separate construction. A hostile mind remains in the protected scope while its harmful channels are restrained.</p>
```

## 10. Zenodo whole-outcome summary

File: `zenodo.json`

**Before**

```markdown
<p><strong>Greatestness.</strong> The whole greatest outcome, continuation and freedom stages included, is realised by the held source. Union closure of realisable outcomes is derived from locality: splicing two policies particular by particular realises their stage-wise union, and the spliced dynamics reproduce each chosen policy on its particular's closed block. Every active agent is free in the canonical sense: every non-harmful effect is admissible and leaves its status, authority and escrow unchanged. Under the Master Solvency Condition the aligned option is the whole top and contains the outcome of every rival regime. Income-or-irrelevance shows solvency is necessary for relevance as a protector.</p>
```

**After**

```markdown
<p><strong>Greatestness.</strong> The full outcome target includes all continuation and freedom stages and every admitted rival. The local-product and held-source models have compiled greatestness results. Their physical application must identify the original policy/outcome family and join successful R17 delivery on the same execution. The whole top witness and its complete funded cost retain their separate roles.</p>
```

## 11. Zenodo storage-functional summary

File: `zenodo.json`

**Before**

```markdown
<li><strong>The funded thermodynamic ledger.</strong> Landauer's bound is proved for density matrices under any unitary coupling to a thermal bath, and derives the second-law guard. The Theorem 8 storage functional contracts by a positive margin on every cycle that contains an error.</li>
```

**After**

```markdown
<li><strong>The funded thermodynamic ledger.</strong> Landauer and the entropy-export guard remain compiled components. The repaired storage functional uses a clipped reserve deficit, exact saturated replenishment and a complete cycle energy balance. A solvent cycle cannot increase its reserve term; the actual error drift and repair then give the stated positive-margin contraction.</li>
```

## 12. Zenodo complete recovery-work summary

File: `zenodo.json`

**Before**

```markdown
<li><strong>Source identification and recovery work.</strong> Data processing, Fano's inequality, the exact log-det Gaussian channel bound and the carrier tail give a recovery-work lower bound of order t<sup>d</sup> in unattended age. A single-shot wavefront sweep is proved to recover every shell, with no rework against fenced outer activity. Its complete metered bill is at most an age-independent constant times t<sup>d</sup>. The recovery work is therefore Θ(t<sup>d</sup>).</li>
```

**After**

```markdown
<li><strong>Source identification and recovery work.</strong> The retained information, traffic, carrier and transport chain supplies the recovery-work lower bound. The one-pass shell calculation and conditional sweep/work theorems support the matching construction. The complete physical patch, fence, capacity, precision and pathwise bill are the remaining application certificates for the unchanged tight work target.</li>
```

## 13. Zenodo Bennett summary

File: `zenodo.json`

**Before**

```markdown
<li><strong>Reversible administration.</strong> Bennett's counterpart is constructed in a Landauer model of options, and the law forces reversible administration.</li>
```

**After**

```markdown
<li><strong>Reversible administration.</strong> The specific compute-copy-uncompute program implements the administration, returns its workspace and retains its full input history. Its trajectory and quantum permutation are explicit. The complete lifecycle comparison must establish the saved heat exceeds the additional charges within the same deadline; a polynomial work ceiling alone does not prove this.</li>
```
