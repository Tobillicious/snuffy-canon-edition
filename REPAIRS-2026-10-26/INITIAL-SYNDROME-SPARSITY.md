# Initial thermal-plus-residual syndrome sparsity

26 October 2026. A derived finite-state bound, independent of a dynamical
cluster assumption. This is a prose proof and exact finite cross-check,
not a newly compiled Lean theorem. It concerns the initial syndrome law;
it does not assert its preservation under the subsequent thermal evolution.

## Zero coset has maximal Boltzmann weight

For a binary linear space D<=F_2^m and 0<=z<=1, put

    Z_D(v)=sum_(x in D) z^|v+x|.

The character expansion of the indicator of D gives

    Z_D(v) = (|D|/2^m) sum_(u in D^perp)
               (-1)^(u dot v) (1+z)^(m-|u|) (1-z)^|u|.

To verify the identity, insert
1_D(x)=|D|/2^m sum_(u in D^perp)(-1)^(u dot x), translate x by v,
and factor the sum over the m binary coordinates. Every coefficient on
the right is nonnegative. Replacing each sign by +1 proves

    Z_D(v) <= Z_D(0).

The argument includes z=0 and z=1, using the usual empty-product and
zero-power conventions. It does not require bounded-degree metachecks.

## Local-stochastic bound despite the global constraints

Let C<=F_2^m be the valid syndrome space, with pi(s)=z^|s|/Z_C(0).
Fix a coordinate subset A. If no codeword is 1 on all of A, its occupation
probability is zero. Otherwise fix one such word c*. Let D be the puncturing
outside A of the shortened subspace {c in C : c|_A=0}, and let v be the
restriction of c* outside A. The numerator for the all-ones restriction is

    z^|A| Z_D(v) <= z^|A| Z_D(0).

The full partition function contains the zero-on-A fibre, whose weight is
Z_D(0). Therefore, for every A,

    Pr_pi[A subset supp(s)] <= z^|A|.

This applies to each CSS syndrome image, which is a binary linear space.
It is a joint occupation bound, not a claim of independent coordinates.
For example, the even-parity two-bit law is correlated but obeys this bound.
The same proof allows coordinate fugacities z_i in [0,1], giving the product
of z_i over A.

## Count the residual fault footprint

Suppose the actual residual fault set F has the local-stochastic bound
Pr[Q subset F]<=p^|Q|. Suppose each fault location affects at most w checks,
and each check is affected by at most ell possible residual fault locations.
These are bounds on the actual residual channel's footprints. They must be
derived from its circuit; one cannot set w=1 because the circuit is local.

For k specified occupied error checks, choose one incident faulty location
per check. There are at most ell^k such choices. Each choice uses at least
ceil(k/w) distinct locations. A union bound gives

    Pr[A subset error-check support] <= ell^k p^ceil(k/w)
                                    <= (ell p^(1/w))^k.

Set q=min(1,ell p^(1/w)); the minimum is justified by the trivial probability
bound. This accounts for a single fault creating several correlated checks.
Cancellation in the syndrome can only shrink its support.

If the residual Pauli fault law is independent of the ideal sampled
syndrome, the output support lies in the union of the thermal support and
the fault-check support. Splitting any required set A between those two
sources and summing gives

    Pr[A subset output-check support] <= (z+q)^|A|.

Thus the initial noisy syndrome remains local-stochastic at a controlled
parameter. If the two sources are correlated, the same union argument
using Cauchy–Schwarz instead gives (sqrt(z)+sqrt(q))^|A|. One must not silently
use the sharper independent-source bound in that case.

## What this does and does not close

The ideal thermal input supplies a proved initial occupation estimate;
global syndrome constraints do not invalidate it. A specified bounded-
footprint residual Pauli channel then gives the displayed noisy estimate.
The actual preparation must still supply that channel correspondence and
its initial decoded logical-error bound. Syndrome sparsity alone cannot
exclude an undetected logical Pauli error.

For a static bad event with a proved connected-history witness of size at
least m_0, at least a quarter of that support occupied at the finest level,
and at most M B^m candidate supports of size m, the initial occupation bound
would give

    Pr[bad initially] <= M sum_(m>=m_0) [B (z+q)^(1/4)]^m.

Applying this last implication requires identifying that witness for the
actual bad projector. No dynamical spacetime witness is inferred from it.
In particular, none of these calculations assigns a small p+exp(-beta)
factor to an energy-neutral hopping jump. The time-integrated bad weight
in `NOISY-G21-INTEGRATED-BAD-WEIGHT.md` remains the dynamical support needed.

`checks/initial-syndrome-sparsity.py` checks the coset maximum and occupation
bound exactly for all binary linear subspaces up to dimension-five ambient
space and several rational fugacities. It also checks a finite correlated
fault-footprint convolution. Those finite checks do not replace the general
character-expansion proof above.
