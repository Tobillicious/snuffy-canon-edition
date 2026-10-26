# BCRD and the existing history-preservation construction

26 October 2026. Source retrieval and mathematical application review, not a
new compilation or a completed noisy holding certificate. The author's pointer
and candidate reconstruction are preserved verbatim in inputs/.

The maximal UPT, its full quantum and relational domain, arbitrary references,
original stage budgets and complete pathwise work ceiling remain fixed.

## The relevant construction already exists

The current master states BCRD P1--P4 at line 31: one relational structure,
relational identity, real organisation and historical continuity, and local
finite-speed interaction. Its boundary accounting includes the apparatus and
environment. These principles do not remove environmental degrees of freedom
from a reduced physical evolution.

The concrete result closest to the author's pointer is already in G.8 and
HamiltonianDecomposition.lean:

- `partial_trace_local_conjugation`, line 91, transports the complete reduced
  history state under a tensor-factor unitary, with no product-state assumption.
- `guarded_history_reduced_state`, line 124, makes that history state unchanged
  when the history-factor operation is the identity. The history factor can
  include an arbitrary reference.
- `syndrome_exchange_preserves_history`, line 136, applies this result to the
  explicit syndrome/reservoir swap; `syndrome_exchange_charge`, line 152,
  accounts for the charge transferred to the reservoir.

These are existing kernel-checked results. The algebra and the reference
extension are not missing and are not requested again.

`GuardFactorization.commutativity` supplies the commuting Kronecker factors.
`ClosedCohold.factorised_cohold` gives the corresponding run decomposition.
The latter's definition explicitly takes a factorised transition; its final
boundary-crossing example distinguishes that construction from a coupled one.
G.9 identifies the actual dependency graph and closed record blocks with the
G1 source certificate. G1Held and G1Refinement supply the previously audited
holding and physical refinement constructions, with their actual trajectory,
correction and fault-account arguments. None is discarded here.

The supplied Claude export also discusses a BCRD pointer around lines
14622--15070. That exchange concerns an earlier proposed relational-tree
sampler and the content protected by BCRD. It is not a derivation that the
current actual residual-noise channel preserves the history factor. The
subsequent full-history ideal sampler is retained; no earlier sampler debt is
reopened by this retrieval.

## The precise algebraic bridge

Let L carry the full decoded history, G the syndrome/gauge/environment
registers, and R an arbitrary reference. If the actual corrected physical
process acts as identity on L and a trace-preserving channel on G, then

    Tr_G[(id_L tensor N_G tensor id_R)(rho_LGR)] = Tr_G(rho_LGR)

for every joint input, including all history/reference coherences. An
environment-only unitary dilation is covered by the existing partial-trace
result. Neither a Gibbs envelope nor a mixing-time argument is needed for
this identity.

Equivalently, let E_a be the actual preparation, D_a its decoder and Phi_t the
actual corrected holding evolution. A direct application can establish

    E_a^dagger Phi_t^dagger D_a^dagger(A) = A

for every logical observable A and every relevant t. Equality on an operator
basis proves D_a Phi_t E_a is the identity channel, hence also preserves an
arbitrary reference. For an approximate implementation, the existing
reference-uniform conversion or a bounded exceptional branch can give the
original stage error allowance. The initial decoded error and any exceptional
branch must be included, with every realised preparation, maintenance and
handoff charge supplied to the complete bill.

For a boundary automorphism kernel to supply this bridge, two correspondences
are needed: the protected decoded history algebra must be represented in that
boundary algebra, and the actual corrected physical evolution must have the
required trivial action on it, exactly or with the stated error bound.
Defining a gauge transformation to act trivially on a boundary proves the
property for that transformation; it does not identify an arbitrary residual
fault or a whole Davies trajectory with such a transformation. This is a
route to proving the existing target, not a restriction of the noise model or
of what the UPT protects.

## What the pasted reconstruction does not establish

The workspace search found no source containing the proposed Sovereign
Lattice/SLH, Fibonacci-resonance or Dittrich--Kogios Schur-complement channel
construction. This is a retrieval result about the searched local sources,
not a claim that no such external source exists.

The proposed local-to-global probability step also needs correction even
before any substrate-specific application. For independent two-level cells
with probabilities 3/4 and 1/4, every cell has constant energy range and
eigenvalue ratio 3, and the partition function factorises. The n-cell Gibbs
state nevertheless has eigenvalue ratio 3^n. Thus the asserted factorisation
and bounded local energy do not themselves remove a global exponential
ratio. Likewise, log(1/pi_min)=O(n) already holds for the uniform n-bit law
in the earlier TV counterexample; it does not imply a polynomial pointwise
ratio without the required accuracy and a proved physical mixing estimate.

Local marginal stationarity is also insufficient for full relational
preservation. The uniform mixture of 00 and 11 has the same one-bit marginals
as the uniform two-bit law, but different correlations. The bridge above
therefore uses the complete decoded history algebra, rather than only local
thermal marginals. A Schur-complement reduction would need its own channel,
observable and error correspondence; a formula for an effective quadratic
operator alone does not supply these identifications.

## Exact remaining source question

Where is the morning derivation identifying the actual noisy G.21 preparation
and hold with the history-preserving boundary dynamics above, including its
allowed physical faults or bounded exceptional trajectories? The already
followed sources are G.8--G.10, HamiltonianDecomposition, GuardFactorization,
ClosedCohold, G1Held/G1Refinement, the full-history sampler and the previous
module-dependency audit. A source pointer or the actual physical
identification can settle this without re-proving the partial-trace algebra,
ideal sampler, reference conversion or complete-cost arithmetic.

All 192 canonical Lean sources still match checkpoint 12 (1,158 public
theorem/lemma names). That existing PASS is retained. This review adds no
canonical source, new axiom, compilation claim or global completion verdict.
No merge, push, rendering seal or publication was performed.
