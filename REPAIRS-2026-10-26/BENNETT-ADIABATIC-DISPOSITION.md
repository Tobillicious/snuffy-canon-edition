# Bennett adiabatic proposal — exact remaining comparison

26 October 2026. The full premise-5 target and admitted rival class remain
unchanged. This records the assessment of the author's reply about finite-time
adiabatic hardware. It does not change the manuscript or declare the physical
counterpart complete.

The proposal supplies a useful candidate device model, but it does not yet
prove the complete-cost saving within the same deadline.

1. **Depth and dissipated energy are different quantities.** A compute/copy/
   uncompute depth multiplier `α_depth` is not also an energy multiplier. The
   displayed equation
   `(α_rev − 1) W_base = (π² R C α_rev / (4 τ)) W_base`
   does not follow from the circuit construction. With nonzero base work it
   imposes a relation between independent parameters. A device derivation
   must instead state its actual work function and account for the controller,
   clock, routing and finite-time losses.
2. **The switching time has an upper bound as well as a lower bound.** In the
   optimistic model with extra work `A/τ + H`, let `Q` be the actual heat saved,
   `D_rev` the actual sequential depth and `T_other` the other latency. The
   original deadline `T` requires

   `0 < τ ≤ τ_max = (T − T_other) / D_rev`.

   For `A ≥ 0` and `τ_max > 0`, strict saving is possible in this model exactly
   when

   `Q > H` and `A/(Q − H) < τ_max`.

   Choosing a slow switch proves neither inequality. For example, `A = 1`,
   `Q = 1`, `H = 0.1`, `τ_max = 0.5` leaves no feasible switching time, although
   the unconstrained expression tends below `Q` as `τ` tends to infinity.
   This is a counterexample to the inference from slow-switching asymptotics
   alone, not a claim about the measured parameters of a particular device.
3. **The actual history bill is still required.** `b0 + bN` is a bit count,
   not a logarithmic capacity theorem. `H` must include the full retained
   payload, clean-cell provisioning, archive writes, continued retention,
   readout, fault correction, guard and controller work, and endpoint costs.
   Time-dependent leakage or retention cannot be put into a constant `H`
   while varying `τ`. For example, if an extra loss is `L τ`, the function
   to compare is `A/τ + L τ + H`, subject to the same deadline.
4. **Heat must be measured consistently.** The canon's accepted result is
   `Q ≥ kT (H(p) − H(f_*p)) > 0` for a merging overwrite. It does not give
   `kT ln 2` for every logical overwrite. A biased bit can carry less than
   one bit of entropy. A conventional device's switching loss may provide
   a larger saving, but that requires a certificate for the compared device;
   it cannot be used as a universal lower bound for every admitted rival.
   Likewise, do not add a Landauer lower bound to a measured total switching
   dissipation if that total already includes the erasure contribution.

The construction can retain `(f(s), 0, s)` and prove its trajectory and clean
workspace identities. The compiled candidate also proves the complete-cost
difference and the feasible-window implication. These mathematical components
do not supply the missing device parameter inequalities.

## Precise pātai for the next construction

For each merging administration in the original admitted family, supply a
specific implementation of `f = h ∘ g` with the same required outcome,
reliability and deadline, and derive its *complete incremental work function*
`F(τ)` relative to that administration. Include the full history throughout
its required retention interval and every controller/clock/guard charge.
Prove there is a permitted switching time with

`0 < τ ≤ (T − T_other)/D_rev` and `F(τ) < Q_actual`.

If `F(τ) = A/τ + H` is the intended certified model, the missing result is
precisely `Q_actual > H` and
`A/(Q_actual − H) < (T − T_other)/D_rev`, derived from that implementation
for the original full class. An unspecified large-system limit or a new
restriction to conventional high-dissipation hardware does not discharge
that existing target. A more efficient construction is also a valid route.

## Primary sources checked

- [Frank et al., Reversible Computing with Fast, Fully Static, Fully Adiabatic
  CMOS](https://arxiv.org/abs/2009.00448): the proposed hardware still has
  leakage qualifications and a specified multi-phase clock and stage latency.
- [Reeb and Wolf, An improved Landauer Principle with finite-size
  corrections](https://arxiv.org/abs/1306.4352): the heat bound is tied to
  entropy decrease, with finite-reservoir corrections; logical overwrite
  counts alone do not establish the claimed complete-cost saving.

Existing project sources followed: `Bennett.lean`, `BennettCounterpart.lean`,
G.14, `BANKS/2026-10-24-glm-thermodynamic-route/PREMISE-REDUCTION.md`, and the
author's compute/copy/uncompute and adiabatic proposals in this conversation.

## Follow-up: explicit-window and holographic proposal

The author's next reply correctly rearranges the inequality to
`A < (Q_actual − H) (T − T_other)/D_rev`, but calls this a device engineering
constraint and assumes it can be met. It does not derive it from an actual
circuit/device. This remains the missing existence result, rather than a
new consequence of the rearrangement.

The proposed replacement of logarithmic capacity by boundary-area capacity
does not supply a history encoder. If an admissible source has `M` distinct
histories that must remain distinguishable, an exact binary encoder and
decoder require at least `ceil(log₂ M)` bits. In particular, `N` independently
variable recorded bits require `N` bits. An entropy bound on an applicable
spacetime region does not by itself prove that this cumulative historical
source has only `2^(c_h L^(d_G−1))` distinguishable histories, or construct a
decoder preserving their ordered queries and reference correlations. The
light-sheet/spacetime hypotheses also need an application to the chosen
register, retention interval and growing boundary. See
[Bousso's original covariant bound](https://arxiv.org/abs/hep-th/9905177)
and [review](https://arxiv.org/abs/hep-th/0203101).

The revised bill `H = e_write (b0+bN) + W_controller` omits previously named
fence, provisioning, retention, fault correction, reset, routing and endpoint
charges unless `W_controller` explicitly contains them. Its final displayed
bound also drops `W_controller`. Area-versus-volume scaling would establish
eventual dominance only after uniform coefficients and all charges were
proved, and still would not pay the finite initial interval or derive the
deadline inequality.

There is also a device-unit check: for a capacitor switched through voltage
`V` in time `τ`, current scales as `CV/τ`, so resistive work scales as
`R C² V²/τ`. Thus a coefficient for an `A/τ` model has units energy times
time. The newly displayed `A = π² R C V² N_ops/4` is missing one capacitance
factor if `R` is resistance and `C` is capacitance as stated. A waveform and
actual gate count are needed to determine the coefficient. `D_rev` must be
the total sequential depth, not just the approximately-threefold depth
multiplier. These checks precede a numerical device certificate.

**Disposition:** the algebraic feasibility test is now explicit. The actual
history-capacity/cost certificate and the circuit satisfying that test for
the original full class remain unproved. No maximal conclusion is reduced,
and this proposal is not recorded as a completed Bennett repair.
