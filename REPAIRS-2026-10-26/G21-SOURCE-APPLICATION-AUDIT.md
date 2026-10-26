# G.21 source application audit

26 October 2026. Local author-review evidence. This audits the ideal sampler's
prose application of published results. It does not certify the noisy physical
preparation, the physical holding of its residual-noise output, or completion
of the maximal UPT. The earlier full-history and arbitrary-reference targets
are retained.

## Source correspondence

The source is [Balasubramanian–Davydova–Lin, v1](https://arxiv.org/html/2605.10943v1),
Sections 3.4, 4.2–4.3 and 5.2. The facts used from it are the fixed bounded
gadgets and degrees, the local coarse maps, their chain identities, and the
alternating weight bounds. The new polymer graph, exact partition
identification, counting application and one-sided sampling bound below are
our derived application, not claims attributed to BDL.

Use `i` for the code's coarse-graining level and `a` for the archive's
doubling-age stage. They are different indices. A code prepared at stage `a`
can itself have many coarse-graining levels.

For an R_X step, `STEP2-FINE-CONDITIONAL.md`, Lemmas 2.1–2.2, gives the local
cut-out: membership in each local x coboundary space; membership in each
post-x-cleaning q coboundary space; and equality of the final cleaned
syndrome with the stored lifted next-level syndrome. We use only these
lemmas and the weight inequality, not that note's later Hypothesis E.
The deterministic local tables must select zero corrections on zero input.
All other tie-breaks are fixed. For an R_Z step, parity on each local z
complex gives the stored next-level bit; the difference from its lift is a
local coboundary. The constant seed's image membership is included as one
finite constraint.

Starting at the seed, the local chain identities give

    s_i = delta_i f_i + F_i(s_(i-1)).

If the stored lower syndrome is valid, so is the upper one. Induction proves
validity of every assignment accepted by these constraints. Conversely, a
valid finest syndrome passes the local maps and yields precisely one full
history. Corrections are computed table outputs, not extra unconstrained
variables. No multiplicity is introduced by summing over correction choices.

## Uniform incidence, not an observed finite degree

Let S bound the number of coordinates read by one constraint and I the
number of constraints reading any coordinate. These constants follow from
the fixed gadget sizes, bounded Tanner incidences and the bounded number of
cleaning layers. They do not depend on i. A stored intermediate coordinate
is read only in the constraints for the two adjacent coarse steps, along
with the seed constraint when applicable. Thus I does not acquire a factor
equal to the hierarchy depth.

Make each constraint scope a clique. Then

    degree(G) <= I (S - 1) = Delta.

This is the all-level bound used in G.21. The finite tests' observed maximum
degree, including 443 in one example, is not substituted for Delta. A scope
may connect distant physical locations across a scale; algorithmic incidence
and the physical routing bill are accounted for separately.

## Exact polymer partition function

Each accepted history has occupied coordinates H. Components below mean
components of the induced graph G[H], not components in a graph omitting
intermediate history coordinates. Every constraint scope intersects at most
one occupied component. Restricting to a component therefore leaves each
scope equal either to its original valid assignment or to the valid zero
assignment. The restriction is valid. Conversely, a union of nonadjacent
standalone valid components is valid by the same argument.

Every other coarse step halves the syndrome weight; intervening steps do
not increase it. Pairing the levels and summing their geometric series gives

    |H| <= 4 |s_finest|.

Apply this inequality also to each standalone component Gamma. Its energy
E(Gamma), the number of occupied finest coordinates, satisfies

    E(Gamma) >= |Gamma| / 4 > 0.

There is one occupied binary assignment per support. Histories are in
bijection with finest valid syndromes and with compatible polymer families.
Their energy is the sum of E(Gamma). Consequently the polymer partition
function is exactly the syndrome partition function, including all global
metachecks. No product structure of the conditional deletion fibres is used.

## Counting theorem hypotheses

The applied counting result is [Helmuth–Perkins–Regts, v4](https://arxiv.org/html/1806.11548),
Theorem 2.2 and, for the self-reduction, **Lemma 2.8** in Section 2.6. The
latter is essential: the available polymer set is restricted after each
choice. The following checks verify its hypotheses for this representation.

| Requirement | Application check |
| --- | --- |
| Bounded-degree graph | The symbolic incidence bound above is uniform in the code level. |
| Analytic weights with positive order proportional to support | w_Gamma(z)=z^E(Gamma); E(Gamma)>=|Gamma|/4, so the order constant is 1/4. |
| Computable truncated weights | The coefficient is 1 at the integer exponent E and zero elsewhere. Local membership testing and energy evaluation are finite computations. |
| Efficient listing for a connected support | There is at most one candidate: put 1 on that support and 0 elsewhere, and test the incident constraints. |
| Polynomial partition degree | Compatible supports are disjoint. Their total E is at most the number of finest coordinates, at most M=|G|. Deleting polymers preserves this bound. |
| Absolute cluster convergence | The explicit estimate below is valid for all polymer-deleted models. |

Put B=(Delta+1)^2 and r=B e |z|^(1/4). A depth-first support traversal gives
at most B^ell size-ell candidates through a specified vertex. The closed
neighbourhood of Gamma has at most (Delta+1)|Gamma| vertices. Hence

    sum_(eta incompatible Gamma) |w_eta(z)| e^|eta|
      <= (Delta+1)|Gamma| r/(1-r).

For delta=[1/(4eB(Delta+2))]^4 and |z|<delta the right side is strictly less
than |Gamma|. This verifies the Kotecky–Preiss criterion with a(Gamma)=|Gamma|.
Deleting polymers only reduces this nonnegative majorant. The empty family
contributes 1. Thus every partition function queried by self-reduction is
nonzero on the same disk, and positive at the chosen positive real z_0.
The fixed choice 0<z_0<delta is also made below the existing memory threshold.
An explicit rational z_0 can be chosen; the algorithm need not assume an
oracle for uncomputable real parameters.

Connected supports of logarithmic size can be enumerated in polynomial
time in M. Listing, table tests and monomial coefficients satisfy the
counting theorem's exponential-in-order enumeration requirement. The disk
slack and constants are fixed across levels. The published theorem supplies
the partition approximation algorithm; we have not implemented a separate
complete FPTAS in this repository.

## One-sided sampling and bounded random-bit use

Let q=B z_0^(1/4)<1. The union bound for a polymer larger than L is
M q^(L+1)/(1-q). Choose L=O(log M) making this at most 1/2. Conditioning on
the absence of such polymers costs a pointwise factor at most 2.

There are P<=poly(M) listed polymers of size at most L. In the finite
self-reduction, the exact inclusion probability p is at most 1/2 because
w<=1 and the compatible remaining partition function is at most the
unrestricted remaining one. Partition approximations within exp(+-eta),
eta=1/(16P), give each decision branch a factor at most exp(2eta).
Clamp an approximate p to at most 1/2 and round down by at most
d<=1/(16P). Inclusion does not increase. Exclusion increases by at most d;
its true probability is at least 1/2. The clamping case has exclusion at
most its true probability. Thus every branch has ratio at most

    exp(2eta)+2d <= exp(1/(4P)).

Multiplying over at most P decisions costs less than 2. Fixed dyadic coins
use O(log P) random bits each, without rejection or an expected-time bound.
If P=0 the sampler returns the empty family and uses no coins. Combining
with conditioning gives mu_sector<=4 pi_sector. Independent CSS-sector
sampling multiplies the factors: mu_joint<=16 pi_joint. The sector factor
is not combined by taking a maximum.

## Evidence and limit of this audit

The generic algebra is compiled in `HistoryPolymer`, `WarmStart` and
`ThermalEncoding`; checkpoint 11 freshly checks 191 modules / 1,150 names.
The local scope implementation was tested on one iteration pair in both
sectors and on the published seed: 8,871 component restrictions, 500
arbitrary assignments with invalid inputs rejected, and the four preserved
deletion witnesses. These finite checks support source correspondence;
they are not an all-level Lean implementation of the BDL construction.

This completes the stated **prose source-application audit of the ideal
sampler**. It leaves the actual physical transfer/holding application open.
For a residual channel N, complete positivity only transports the ideal
order bound to N(rho_beta), not back to stationary rho_beta. Neither the
counting theorem nor exact branch recovery supplies that additional bound.
