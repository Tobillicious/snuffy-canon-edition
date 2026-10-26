# The proposed active-correction holding bridge

26 October 2026. Review of the author's latest candidate, preserved verbatim
under inputs/. The candidate is recorded for review, not incorporated as a
completed proof in the canon. No canonical Lean source changed. All 192
sources still match checkpoint 12, covering 1,158 public theorem/lemma names;
no new compilation is claimed.

The same maximal quantum target, arbitrary references, original stage budget
and complete gross/pathwise work ceiling for all admitted d_G >= 1 are fixed.

## What can be retained

An active fault-tolerant recovery construction is a legitimate alternative to
the passive Davies holding application. It need not prove Gibbs domination
if it directly bounds the decoded channel error. The relevant existing
supports are KnillLaflamme, MatchingWitness, EdgeLaw/WeightedEdgeLaw,
Threshold and AgeReliability. These are genuine proved supports, not missing
derivations requested again here.

The candidate's good/bad trajectory decomposition gives error at most twice
the bad probability if, on every good fault branch, the actual decoded
channel preserves every logical/reference state, and the bad probability is
bounded uniformly in the logical input. For example, if the decoded channel
is (1-delta) id + delta F with F CPTP, its difference from identity has
diamond norm at most 2 delta. More generally the same conclusion follows
from the corresponding good/bad quantum instrument.

The ideal equality Dec Enc_mu = id is already proved, including arbitrary
references, by ThermalEncoding.recovers_reference. It does not by itself
prove correctness of the branches containing faults. The event being
bounded must include actual preparation, retained branch-record/controller,
measurement, recovery and holding faults, or the initial decoded error must
be allocated separately.

## The corrected conditional fault estimate

Write D for circuit distance, q for the induced spacetime edge fault rate,
N(D) for the relevant spatial location count, and a for archive-age stage.
Keep these distinct from the spatial exponent d_G.

For a specified actual finite circuit, suppose:

1. Its fault law is local stochastic over spacetime, with the physical
   footprint-to-edge conversion required by EdgeLaw or WeightedEdgeLaw.
2. Every decoded failure has a witness of length L >= D with at least half
   its edges faulty, as in MatchingWitness and Threshold.
3. The number of witnesses of length L is at most V_a Delta^L, with
   V_a <= K 2^a N(D), and r = 2 Delta sqrt(q) < 1.

The existing Threshold.fail_le_geometric then gives

    Pr(fail_a) <= K 2^a N(D) r^D / (1-r).

Consequently, if this event includes all the faults above and its good
branches have the full reference-preserving correctness property, a
sufficient distance condition for the original trace-norm stage target is

    D >= [(2a+3) ln 2 + ln(K N(D) / (epsilon (1-r)))] / (-ln r).

It gives Pr(fail_a) <= epsilon/2^(a+3), hence decoded error at most
epsilon/2^(a+2). This retains the geometric denominator and location count.
For polynomial N(D), logarithmic growth of distance in age is compatible
with this conditional reliability estimate. AgeReliability.log_distance_schedule
already supplies the corresponding logarithmic scheduling algebra.

The circuit application is still substantive. The present G.18/G.19 detector
data are for their specified surface-code circuits. They cannot simply be
assigned to the BDL circuit and decoder. In particular, a thermal syndrome
branch of Enc_mu can have many intentional defects. A proof must show which
new physical faults cause a logical failure relative to that branch and how
the branch record is used and protected; distance from the empty codespace
alone is not that correspondence.

HistoryPolymer counts a static deterministic coarse-graining history used
for ideal thermal preparation. Its support and truncation lemmas do not
enumerate fault trajectories in physical time or prove their probability
law. The proposed Step 2 asserts that new correspondence without defining
it. For the active route, the circuit witness theorem above is the suitable
existing tool; a new claim of polymer convergence is unnecessary. Bounded
single-location fault probability alone would not establish the required
joint local-stochastic law.

## The work join has not yet been derived

With T_a = 2^a full active recovery cycles, their realised cost is part of
the stage invoice:

    W_a = W_prep,a + sum_{u<T_a} c_a,u + W_handoff,a,

including every auxiliary, guard, record, controller, reset, export and
failure charge. A polynomial upper bound c_a,u <= P(a) yields a stage
maintenance upper bound 2^a P(a), not P(a). TransferRate's polynomial
per-stage invoices concern a finite preparation/handoff schedule; they
cannot absorb an omitted maintenance sum.

For example, if D_a is proportional to a and a full recovery round actually
uses proportional-to-D_a^2 work, then this schedule costs proportional to
2^a a^2 per stage. Its ratio to 2^a is unbounded. It does not establish the
d_G=1 work ceiling. Higher-dimensional applications may have room for some
such charge, but that room must be demonstrated in the actual total
ledger; an extra logarithmic factor on an already t^d_G bill cannot be put
inside an age-independent constant. AgeReliability.log_factor_not_absorbed
already proves that point.

G3CompleteBill.cumulative_charge_bound takes the complete per-wave charge
bound as an input, including routine maintenance. StageSchedule.total_with_transfers
sums supplied error budgets; it is not an upper bound on unmetered active
recovery work. No age-to-wave-count conversion alone proves the missing
per-wave charge estimate.

## Disposition

Retain the valid active-correction strategy and the corrected conditional
distance estimate. To close this application, specify and certify the
actual preparation/recovery circuit, including good-branch correctness and
its fault witnesses, and derive its complete maintenance invoice within the
unchanged G3 ceiling. These are application steps, not a request to re-prove
the ideal sampler, existing threshold algebra, reference extension or cost
summation. The candidate as written does not yet discharge them.

## Subsequent sparse-epoch and fidelity reply

The author's subsequent reply is preserved as
inputs/AUTHOR-SPARSE-EPOCH-FIDELITY-CANDIDATE-2026-10-26.txt.
Its finite geometric work estimate is correct: for d_G >= 1,

    sum_{j=0}^a 2^(j d_G) <= 2^(a d_G)/(1-2^(-d_G)).

The complete epoch invoice must actually satisfy the claimed bound,
including all holding between epochs, retained records and device charges.
Sparse recovery changes the physical schedule: its channel is a composition
of passive evolution intervals and the intervening recovery/transfer maps,
not (R E)^(2^a) with recovery at every microscopic step.

This saves active work only after the passive intervals are physically
covered. PassiveReference proves the classical-reference doubling-budget
and rewrite arithmetic. It is not the missing quantum holding theorem for
the actual noisy G.21 output.

The new universal commutation assertion is false. A correctable single-qubit
X error anticommutes with a stabilizer containing Z on that qubit. Distance
does not turn such detectable errors into commuting operators. The existing
KnillLaflamme.knill_laflamme_of_distance handles both cases: anticommuting
error products have zero code sandwich; commuting products below distance
act as scalars. Neither the three-layer ideal swap nor the nine-part charge
record establishes the actual circuit's spacetime local-stochastic law,
fault propagation or witness count. The per-weight exponential suppression
rate is derived from that law and multiplicity, while distance supplies
the witness threshold; it is not a proved factor of distance per fault.

The fidelity half of the reply returns to ideal Gibbs domination. Complete
positivity transports the actual input envelope to the actual channel's
image of that envelope. It does not prove that noisy preparation or active
recovery fixes the Gibbs state. In the residual-channel formulation the
needed physical weight remains

    b_N(s) = Tr(P_bad Phi_s(N(rho_beta))),

or the direct actual-preparation variant already derived in G.21. No bound
on this quantity is established by the reply. Also P_bad is a physical
syndrome-space projector and cannot be applied directly to an already
decoded logical/reference state without its specified observable transport.
The constants in the existing derived reference conversion are retained;
the proposed change from 18 to 12 is not justified by a new derivation.

The final code-size inequality is useful conditionally. With n^eta
proportional to a, exp(-c n^eta/2) is exponential in a, hence a power of
physical age 2^a; its coefficient must be chosen to beat the explicit
2^(2a) factor and polynomial norm prefactors. It is not automatically
super-exponential in age. The earlier polynomial-size scheduling argument
already handles the logarithm of those prefactors once the actual holding
estimate is established.

The geometric summation and conditional code-size calculation are retained.
The remaining physical certificate is still the one for the actual noisy
quantum state over the intervals between recovery epochs. No completed
physical proof or new kernel receipt is issued by this reply review.

The later two-phase reply is reviewed in DAVIES-KMS-AND-TWO-PHASE-REVIEW.md.
Its KMS stationarity calculation is valid for the specified paired Bohr jumps;
the global gap, actual circuit application and consistent maintenance invoice
are still separate. Its distance calculation also omits one duration factor,
giving epsilon/4 instead of the required epsilon/2^(a+2).
