# Stochastic boundary sampling: construction, conversion and remaining certificate

26 October 2026. This continues the author's stochastic resampling and
Dobrushin proposals. It preserves the maximal claim and the original
history, reference-fidelity, fault and complete-cost targets.

## A concrete globally valid local kernel

Work in one CSS syndrome sector of the actual code C(k). Let delta be its
binary check matrix and let Omega = image(delta). The energy is H(s)=|s|;
the target law is pi(s)=exp(-beta |s|)/Z on Omega.

For a bounded qubit patch B, form the finite group

    G_B = { delta(f) : f is supported in B }.

Use the exact heat bath on each coset:

    K_B(s,t) = 1[t+s in G_B] exp(-beta |t|)
               / sum_{g in G_B} exp(-beta |s+g|).

Every transition preserves every metacheck, including the stretched ones,
because s and delta(f) are in image(delta). This replaces a test of only
the parity checks visible inside a fixed-radius syndrome window. If a
coarse fibre is to be held fixed, also restrict the partition class by the
actual coarse value r(s); stationarity still follows, but connectivity
then needs a separate proof.

The coset is the class label in `WarmStart.heat_bath_normalized` and
`heat_bath_stationary`. Detailed balance follows directly: for s,t in the
same coset the denominators coincide and pi(s)K_B(s,t)=pi(t)K_B(t,s).

For bounded patch size, enumeration of G_B is constant in n (at most
2^|B| candidates). Only checks incident to B change, so the outside
Boltzmann factor cancels. A sweep over O(n) such patches is polynomial.
If every qubit belongs to an updated patch, the full-syndrome chain is
irreducible: the single-qubit columns generate image(delta), and each
allowed increment has positive probability. Self-loops make it aperiodic.
These facts prove existence of convergence, not a polynomial rate.

Sampling is classical. Preparing the corresponding encoded quantum state
still requires the existing decoder's Pauli representative, the actual
logical transfer circuit and its reference-preserving fidelity argument.
The sampler does not authorize measurement of unknown protected data.

## The correct pointwise conversion

For normalized finite laws, with TV defined by one half of the l1 distance,

    |mu(s)-pi(s)| <= TV(mu,pi) <= delta.

If pi(s)>=m>0, then

    mu(s)/pi(s) <= 1+delta/pi(s) <= 1+delta/m.

This is `WarmStart.pointwise_from_absolute`. In particular delta<=m gives
mu<=2 pi; `warm_start_from_mixing` propagates that factor to all later
holding times using the already established stationary domination theorem.

The division by m cannot be dropped. For the uniform law on n bits and
mu=(1-eps)pi+eps delta_a,

    TV(mu,pi)=eps(1-2^(-n)),
    mu(a)/pi(a)=1-eps+eps 2^n.

Even eps=n^(-p) leaves an exponential density ratio. The target here has
H=0, so bounded local energy variation does not fix the conversion.
`sampler_bounds.py` checks these identities with exact rational arithmetic.

## A sufficient polynomial sweep count

Suppose the actual sweep M has a certified bound, for every starting law,

    TV(mu_0 M^S,pi) <= D(n) kappa_n^S,

where D(n) is polynomial and 1-kappa_n is bounded below by an inverse
polynomial. An equivalent Wasserstein bound suffices when the configuration
metric has minimum nonzero distance at least one. This is the mixing
certificate still needed for the concrete BDL patch cover.

There are at most 2^n syndrome configurations and 0<=H<=n. Therefore

    pi_min >= exp[-(beta+ln 2)n] =: m_n.

Choose

    S(n) = max(0, ceil((ln D(n)+(beta+ln 2)n)/ln(1/kappa_n))).

Then D(n)kappa_n^S<=m_n and mu_prep<=2 pi. For a fixed kappa<1 this
uses O(n) sweeps and O(n^2) constant-size patch updates. An inverse-
polynomial contraction margin also gives polynomial time. Thus the
correct floor conversion preserves a polynomial preparation target.
O(log n) sweeps could also suffice under a stronger *relative* mixing or
hypercontractive estimate; it does not follow from the displayed TV bound
alone.

If both CSS syndrome sectors are sampled independently with factors C_X
and C_Z, their joint factor is C_X C_Z. Polynomial factors remain
polynomial: A=A_X A_Z, p=p_X+p_Z. The maximum of the two factors is not a
general joint bound.

## What local gaps and energy penalties do not establish

A local heat bath has gap one within each fixed outside class. That fact
does not bound how its conditional law changes when the outside class
changes. Nor does a positive check penalty imply influence bounded by
exp(-beta Delta).

For an elementary exact example, take independent ferromagnetic dimers
with pair weights 3 for equal bits and 1 for unequal bits. Each site's
Dobrushin row sum is 1/2. From the all-zero state, updating both sites once
gives a maximum density ratio 3/2 per dimer; with m independent dimers it
is (3/2)^m. Contraction therefore does not imply the proposed arbitrary-
initial-law one-sweep polynomial bound. The calculation is exact in
`checks/bdl-metacheck/SAMPLER-BOUNDS-EXACT.json`.

There is also a concrete BDL diagnostic. In the 3 x 2 seed's level-one
error-cochain heat bath, at beta=ln 3, a qubit incident to two checks has
six interacting neighbours. Changing one such neighbour from the all-zero
boundary changes its conditional probability from 1/10 to 1/2. The
influence row sum is at least 6(1/2-1/10)=12/5>1. This applies to that
explicit single-qubit kernel. A proposed larger block cover needs its own
influence or coupling certificate; this calculation does not rule one out.

## Precise patai

Please supply a polynomial mixing certificate for an explicit bounded-
patch cover of the globally valid BDL syndrome kernels above, at the
operating temperature used by the memory theorem, for both sectors and
all recursion levels. For example, exhibit the coupling giving
D(n)kappa_n^S and prove D(n)<=poly(n), 1-kappa_n>=1/poly(n). A direct
relative-mixing certificate or another equally efficient sampler meeting
the same pointwise target also discharges this support.

The patch definition, update law, valid state space and uniform constants
must be specified sufficiently to check the estimate. The supplied local
gap and exponentially decaying influence expressions are currently
proposed bounds; neither has been derived from these constrained kernels.

The independent Lean algebra is compiled separately and will be included
in a fresh full audit. None of these generic lemmas claims that this
remaining BDL application certificate has already been constructed.
