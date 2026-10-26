# Disposition of the author's noisy-holding reply

26 October 2026. The reply is retained verbatim in
`inputs/AUTHOR-NOISY-HOLDING-REPLY-2026-10-26.txt`, with source and SHA-256 in
the adjacent JSON. It is a candidate support for the unchanged maximal
claim. Embedded suggestions to merge or package a final suite are not a
new instruction to merge or publish.

The geometric sums are usable. They do not derive the physical estimates
K or delta, which are still assumed. In particular, the reply's table calls
IPS dilution, disagreement-percolation and long-time spacetime estimates
rigorously proved, but does not provide proofs identifying the actual
generator, fault model or constrained code. Existing receipts do not cover
those assertions. A BDL syndrome-weight reduction is not by itself a
contraction theorem for the physical noisy channel.

## Exact arithmetic corrections

For e_1=epsilon/4 and equality in

    e_(j+1) = e_j/2 + epsilon/2^(j+2),

the exact solution is e_j=j epsilon/2^(j+1). The asserted induction fails
already at j=2: epsilon/4 is not at most epsilon/8. The infinite sum is
epsilon, so this recurrence can support a different cumulative estimate;
it does not give the original per-stage ceiling. We do not replace that
ceiling by the weaker statement.

For the claimed ceiling e_j<=epsilon/2^(j+1), one sufficient numerical
choice would instead be **both** K<=1/4 and
delta_j<=epsilon/2^(j+3). Neither numerical choice establishes that the
physical installation has those properties. No K<1 is required if a direct
decoded holding bound is supplied instead.

The reply also evaluates the first geometric budget incorrectly:

    sum_(j=1..D) epsilon/2^(j+2)
      = epsilon/4 (1-2^(-D)) < epsilon/4

for positive epsilon. Its looser final upper bound remains true.

For n_j=n/b^(j-1), summing W_j=C n_j log n_j gives O(n log n).
For the exact binary example n=2^D, with log base 2,

    sum_(k=0..D-1) (n/2^k)(D-k) = (D-1)2^(D+1)+2.

The ratio to n grows with D. Parallel execution bounds depth; it does not
prove constant gross work per node. Linear work follows if a separate
deterministic W_j<=C_1 n_j estimate is derived. The project only needs the
already sufficient polynomial stage work, so no linear decoder-work claim
is needed here.

`checks/noisy-join-arithmetic.py` records exact rational/integer checks in
`checks/NOISY-JOIN-ARITHMETIC.json`. These checks expose the stated arithmetic
errors; they do not verify or refute the full physical UPT.

## Physical support still needed

Keep archive-age index a distinct from code-decimation index i. For the
actual state prepared at age stage a, the needed conclusion concerns its
decoded channel on an arbitrary logical-reference input for holding time
2^a, including any initial logical error, at the original
epsilon/2^(a+2) allowance and polynomial pathwise preparation work.

One sufficient route is an initial decoding-error bound plus a bound on
the time-integrated bad-projector weight of Phi_t(N(rho_beta)). The existing
G.21 reference-norm proof can then be applied. This does not require the
protected logical channel itself to contract arbitrary state differences.
Indeed, an exactly recoverable channel preserves trace distance on its
encoded logical family, by applying data processing in both directions.
A uniform strict contraction on that whole family would conflict with
lossless recovery; any contraction claim must specify the correct gauge
or error variables.

Local-stochastic gate faults also need their actual footprint counted.
One fault flipping w nearby checks can make all w occupied with probability
O(p), rather than O(p^w). The arithmetic check includes a finite correlated
footprint example. A thermal-plus-fault cluster proof must account for that
correlation, rather than assume independent syndrome occupations.

The precise request remains `PATAI-ACTUAL-TRANSFER-HOLDING-2026-10-26.md`.
No new preparation-mixing investigation, classical replacement of the
unknown quantum input, or weakening of the stage ceiling is introduced.
