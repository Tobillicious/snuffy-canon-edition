# Holding power — derivative and constitutive proposals

26 October 2026. The full UPT protection and complete pathwise work targets
remain fixed. Neither proposal is incorporated as a physical zero-drain
theorem. The existing ledger retains its holding, guard and controller costs.

## Derivative proposal

For `q(t) = Φ(h_aut(t))`, constancy on an interval does imply
`q'(t) = 0` in its interior. The mathematical quantity `‖q'(t)‖²` then
vanishes there. This does not identify it with physical holding power.
Different physical implementations of the same logical identity evolution
can have different clock, leakage, cooling and error-correction costs.
Defining the mathematical quantity to be “holding power” does not prove the
device energy equality that connects it to the complete bill. Its physical
units also need a device coefficient.

The displayed Lean statement additionally includes a degenerate-interval
counterexample: take `t1 = t2 = 0`, `h_aut(t) = t` and `Φ = id`. The
constancy hypothesis on `[0,0]` holds, while `‖q'(0)‖² = 1`. This exact
counterexample was checked with Lean `--stdin`, exit 0 and zero output; the
source text, log and result are in `checks/holding-derivative-counterexample.*`.
This is not a compilation of the supplied proof or a new canon theorem.
For an oriented integral, constancy on `Icc t1 t2` also needs the interval
ordering handled; when `t1 > t2`, that set is empty although the oriented
integral can be nonzero. A corrected interior/almost-everywhere statement
would still concern the mathematical observable rather than device power.

## Constitutive-nullification proposal

The substitution `G = 0 ⇒ Fᵀ G F = 0` is correct. The new **Latched
Insulation Hypothesis**, however, supplies `G = 0` as an input. The asserted
step from an energy gap or symmetry to exact zero dissipative conductance
has not been proved for an actual device, bath and admitted interactions.
A positive finite gap can suppress transitions without eliminating them at
nonzero temperature. In a concrete gapped model, thermal relaxation remains
finite: [Alicki, Fannes and Horodecki, On thermalization in Kitaev's 2D
model](https://arxiv.org/abs/0810.4584). This supplies a counterexample to
“positive gap alone implies perfect passive retention”; it is not a
no-go result for every possible UPT implementation.

The superconductor analogy reverses resistance and conductance. For a scalar
voltage-driven dissipative channel, `I = G V`, `P = V I = G V²` and `G = 1/R`.
Zero conductance describes insulation. Persistent current with zero resistance
is described using `P = I² R`; it does not establish the asserted `G = 0`.
More generally, only the symmetric dissipative part of an admittance enters
this quadratic power, so exact zero need not require the entire admittance
tensor to vanish.

The balance convention also needs consistency: the displayed equation
subtracts `P_ctrl` while describing it as work input. It can represent an
outgoing controller charge if labelled accordingly; an input has the other
sign. In either convention, proving zero for one internal dissipative term
does not remove controller, guard, clock, refrigeration, readout, reset or
history-retention charges elsewhere in the complete system boundary.

## Precise remaining construction

Give the actual device Hamiltonian or circuit, its system/bath couplings,
temperature, protected subspace and latched controls. Derive the dissipative
response for the admitted forces, rather than assume it vanishes. If exact
isolation is used, prove the required selection/decoupling identities for
every admitted interaction and for arbitrary retained reference states, and
show how the latch, guard and cooling are realised and charged.

A proved nonzero holding-cost bound that fits the original complete
`W(t) ≤ C t^d` ceiling is also a valid construction route. The original target
does not require replacing a physical holding term by a newly named zero
observable. Transition control costs should be integrated only after their
actual device power law, waveform and deadline are specified.

## Kubo and spectral-decomposition follow-up

The exponential-bound proof drops the `n = 0` part of its own spectral sum.
For `H = diag(0, Δ)` and `J = [[0,1],[1,0]]`, `J² = I`, so the equal-time
thermal correlation is exactly `Tr(ρβ J²) = 1` for every `β`. Its ground-to-
excited term has ground-state weight rather than `exp(−βΔ)`. A corrected
finite-dimensional estimate retains a ground contribution `M0` and bounds
only the excited contribution by `M1 exp(−βΔ)`. Eliminating `M0` requires an
actual current-operator identity. A damping factor `exp(−ηt)` and its
uniform relaxation bound also need a microscopic application; introducing
one is not a derivation from the system gap.

The charged-operator rule permits matrix elements with charge difference
`q`. It suppresses only the other matrix elements. For example,
`Q = diag(0,1)` and `J = |1><0|` satisfy `[Q,J] = J`, while
`<1|J|0> = 1`. Physical current correlations can contain `J†J`, whose net
charge is zero; symmetry does not force them to vanish.

## The two trilemma attachments

Both original attachments are preserved under `inputs/`, with their hashes
in `HOLDING-INPUTS.json`. The proposed three horns do not form a partition.

- **Missing case:** choose `dμ = 1_[1,2] dω` and `f = 1_[1,2]`. For the
  positive continuous thermal kernel, `P = ∫_[1,2] K(ω) dω > 0` and is
  finite. There is no origin overlap; no bath gap places the nonzero system
  spectrum below that gap; and `f` is not zero. None of the three stated
  horns holds. Dissipative spectral overlap away from zero is a missing case.
- **Overlap:** a gapped bath and `f = 0` satisfy both horns 2 and 3 as their
  mathematical conditions are stated. They are not mutually exclusive.
- **Symmetry does not imply a zero spectrum:** with
  `Q = diag(1,1,−1,−1)`, `H = diag(0,Δ,2Δ,3Δ)` and
  `X = |0><1| + |1><0|`, both `[H,Q] = 0` and `[Q,X] = 0`, yet
  `<1|X|0> = 1`. Transitions within a charge sector remain allowed. Likewise,
  `Π0 X Π0 = 0` alone does not prevent leakage out of that subspace: it
  holds for the two-level `J` above. Exact no-leakage needs the cross-block
  identity `(I−Π0)XΠ0 = 0`, and logical-history protection requires the
  appropriate action within the protected block as well.
- **Topological support alone is insufficient:** ordinary supports can
  intersect only at accumulation points while `f = 0` almost everywhere
  under `μ`. The final attachment strengthens its local hypothesis to
  `∫_[0,ε] f dμ > 0`; that weighted-overlap hypothesis does imply positivity,
  but is not supplied by arbitrary intersections of pointwise supports.

An Ohmic spectral density is also commonly proportional to frequency near
zero, rather than strictly positive at zero; no classification should turn
on the value at a single point of a continuous-density integral.

For the **specified mathematical model**, the exact usable statement is:
if `K > 0` almost everywhere under `μ`, `f ≥ 0`, and `K f` is integrable,
then

`∫ K f dμ = 0  ↔  f = 0 μ-almost everywhere`.

Spectral separation is one sufficient way to establish the right-hand side.
This criterion does not infer a physical power law, a protected spectrum,
or the other device charges. A candidate formalisation of precisely this
criterion is kept separately in `checks/snapshots/response/`; its verification
status belongs to its targeted receipt, not the canon's name count.

The next useful submission is one actual device's coupling operators,
bath measure, current spectrum and complete work/time ledger, with proofs
of their measured or derived properties. Declaring either proposed horn as
a new governing axiom would not supply that construction. No new axiom or
`sorry` is being added to the canon.

## Verified helpers and the latest composition

The separate `HoldingSpectralCriterion.lean` candidate now compiles with
zero output and passes `leanchecker` with zero output. It contains:

1. `zero_power_iff_spectrum_ae_zero`: real integral, with integrability.
2. `zero_power_of_spectral_separation`: a null bath-measure support suffices.
3. `zero_extended_power_iff_spectrum_ae_zero`: measurable ENNReal version,
   with no finite-integrability requirement.
4. `switching_energy_bound`: a measurable actual amplitude cap gives
   `0 ≤ E_switch ≤ peak (b−a)` on an ordered finite interval.
5. `conditional_model_certificate`: the spectral-separation and control
   bounds compose exactly as the author proposes for this specified model.

This is targeted verification of a separate helper candidate, not an
addition to the 169-module canon or a full physical certification. The
source hash and checks are in `checks/TARGETED-HoldingSpectralCriterion.json`.
The physical application still identifies the complete power with its model
at every relevant time, constructs the actual bath measure and spectrum,
and pays all remaining lifecycle channels, latency and reliability costs.

Writing `Hyp_gap` as a typeclass or module parameter is a convenient way to
state a conditional result. It does not prove the chosen material has that
bath measure. The proposed Arrhenius probability also requires the actual
escape-process/rate bound, temperature and finite-size barrier certificate;
the displayed inequality is not derived solely by naming a barrier. The
metered lifecycle machinery already exists in `G3CompleteBill` and
`WorkBilling`; the physical charges must populate it without deleting
holding, guard, archive, cooling or failed-attempt costs.

## Constraint-maintenance commutation proposal

`[H_total,Q] = 0` proves conservation of `Q`; it does not prohibit energy
exchange inside a degenerate `Q` sector. Charge conservation in a resistive
circuit is compatible with positive Joule dissipation. More abstractly, an
interaction can act nontrivially on one factor while a conserved charge acts
on another, leaving the charge exactly fixed throughout energy transfer.

The Fourier step is also false: a nonzero constant correlation transforms
to a delta contribution at zero frequency, not to an identically zero
spectrum. A power spectral density is the transform of a correlation; an
expression squaring a delta distribution is not automatically defined.
One must supply the actual spectral measure and its coupling to the power
kernel. A barrier diverging only in the thermodynamic limit also needs
finite-device reliability and work bounds before application to the bill.

**Disposition:** the model-composition theorem is verified. The proposed
symmetry argument does not construct a zero-cost constraint apparatus, and
wrapping that desired property as a new hypothesis does not discharge the
original physical construction. The maximal UPT target remains unchanged.

## Ideal/defect decomposition follow-up

Power is quadratic in current. For common spectral amplitudes a and b,
|a+b|² = |a|² + |b|² + 2 Re(a* b). Cauchy–Schwarz bounds the cross term;
it does not make it vanish. a=b=1 gives 4 > 1+1. Without an orthogonality
certificate, a general finite-power bound is
P_total ≤ (sqrt(P_ideal)+sqrt(P_defect))² ≤ 2(P_ideal+P_defect).

If the ideal amplitude is actually zero μ-almost everywhere in the same full
device model, then total and defect amplitudes agree there and their powers
are equal. This does not require a separate cross-term argument. A zero
spectrum computed for H_ideal alone is not automatically the ideal component
under H_total: the perturbation can change the state, dynamics and spectrum.

An upper bound by itself also does not prove the stated equality, nor compel
an arbitrary optimiser's design priority. The physical instance, complete
costs, outcomes, deadlines and the established canonical-order argument must
be joined. This decomposition is not recorded as closing those supports.

## Orthogonal blocks and final DOS proposal

Orthogonal blocks eliminate the time-dependent cross-correlations when the
full holding evolution and the relevant currents preserve those SAME blocks.
The block-preservation hypothesis must include the full evolution, not just
the current at time zero. Additivity does not itself prove zero ideal power.
The orthogonal-decomposition attachment is preserved verbatim under inputs/.

The final symmetry/DOS proposal and the precise null-set inference error are
recorded in LATEST-AUTHOR-SYMMETRY-DOS-PROPOSAL.md. No device-zero theorem is
claimed from these proposals.
