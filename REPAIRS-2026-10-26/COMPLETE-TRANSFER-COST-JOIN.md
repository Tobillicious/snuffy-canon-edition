# Complete transfer and retained-history bill

26 October 2026. Local author-review construction and accounting. The target
remains gross, pathwise W(t)<=C t^d, with C independent of archive age and
every d>=1. The ideal sampler's algorithmic source audit is recorded in
`G21-SOURCE-APPLICATION-AUDIT.md`. Its physical residual-noise holding
certificate is still required; the arithmetic here does not replace it.

## Which index controls the bill

Let a index doubling-age stages, whose holding durations are 2^a. The
passive code size needed by the established stretched-exponential holding
estimate is polynomial in a+log(1/epsilon). The sampler's history size M,
polymer list length P, fixed coin count, partition-approximation time and
workspace are consequently polynomial in that same quantity. For fixed
epsilon and fixed device parameters, each has a bound (A+B a)^k for finite
constants independent of a. Coarse-graining indices inside one code are
not additional archive-age stages.

This statement uses the finite approximation algorithm with fixed accuracy
eta=1/(16P) and dyadic coins. It does not use a rejection loop or an expected
mixing time. A deterministic cap must likewise be given for any physical
retry procedure. Aborting an attempt leaves its whole invoice payable.

## Full retained prefix

Let r_a count **all** new sampler bits at stage a: randomness, the complete
syndrome/coarse-graining history, branch choices, controller records and
the records of failed attempts. If r_a<=(A+B a)^k, the full retained prefix
through a obeys

    m_a=sum_(b=0..a) r_b <= [A+1+(B+1)a]^(k+1).

`TransferRate.retained_prefix_bound` proves this finite bound. No earlier
record is deleted. Copying or encoding the entire m_a-bit prefix at later
stages still has polynomial stage work. These are the sampler's additional
classical records; their retention does not replace the unknown protected
quantum payload by those records.

For a passive classical journal with attempt rate nu, reserve a subbudget
epsilon_R/2^(a+2) inside the existing stage allowance. This is not an extra
failure budget added after the original epsilon has been spent. A sufficient per-bit barrier is

    beta B_a >= (2a+2) ln 2 + ln(nu max(1,m_a)/epsilon_R).

Indeed the union bound on m_a bits over duration 2^a gives that journal
allowance. Since m_a is polynomial, this barrier is bounded by an affine
function of a, using ln(1+a)<=a. Writing, routing and retaining the whole
prefix at these barriers therefore remains polynomial per stage under the
same passive classical storage implementation already used for the record.
Physical write/retire/reset costs are included below. No continuous scan of
every journal bit is introduced: access is paid when the journal is used.
This classical journal calculation does not establish passive holding of
the unknown quantum payload; that is the separate noisy-state pātai.

## The actual invoice

The account boundary is `WorkBilling.HandoffCharge.total`, with nine fields:

| Field | Required contents of the stage/attempt invoice |
| --- | --- |
| encoding | Classical sampler and arithmetic, random-bit generation, branch encoding and the entire retained-prefix encoding. |
| transfer | Source decoding, destination encoding, conditional Paulis and every physical transfer gate. |
| verification | Syndrome/check extraction, comparisons, acceptance tests and failed tests. |
| routing | All transport/SWAP operations, including the sampler's cross-scale classical dependencies. |
| guard | Guard operation for the whole attempt, including waiting and failure handling. |
| reset | All workspace, ancilla and retired-device resets; reversible uncomputation where used; any outgoing entropy. |
| holding | Holding of the source, destination and retained records during execution. Long passive intervals are also kept in the archive account. |
| controller | The clock, classical computation/control, stored decisions and its exported work. |
| endpoints | Preparation, deployment, connection/disconnection and export/retirement at both ends. |

Algorithmic work counts **total operations**, not parallel depth. Even a
conservative serial routing implementation across a finite connected
stage device has polynomial path length and polynomial operation count.
No constant-time nonlocal classical operation is needed for the bill.
Finite arithmetic precision, random bits and the full workspace are counted.
The declared device cost bounds convert these finite local counts to
physical work. They do not follow merely from the word Clifford or from
logical reversibility.

For each implemented attempt, the required source-level certificate is a
bound on all nine fields. Their sum is a polynomial if each is polynomial.
In particular the intended good branch cannot erase a failed attempt's
invoice. `WorkBilling.charged_attempt_accounting` charges the total even
when no payload commit occurs and preserves the escrow-plus-spent identity.
It still requires the reserve before that attempt. This note does not
replace prefix funding, success or physical fidelity by a final total bound.

## Compiled summation and the full G3 join

Suppose at most (u+v a)^r attempts are admitted at stage a, and each actual
complete attempt charge is at most (A+B a)^k. Then

    sum_(attempt h at a) charge(a,h)
       <= [A+u+(B+v)a]^(k+r).

`attempt_stage_bound` proves this inequality. `complete_attempt_bill` and
`polynomial_stage_bill` then prove an age-independent C_T for the full
attempt prefix:

    sum_(a<J) sum_(h<attempts(a)) charge(a,h) <= C_T t

whenever 2^J<=2t. The bound also covers the current stage's full reserved
invoice. The polynomial-to-exponential comparison is `poly_le_two_pow`;
it does not take a limit of the realised cost or average over fault paths.

The existing sweep and live-archive constructions retain their bills
W_S(t)<=C_S t^d and W_A(t)<=C_A t^d. For t>=1 and d>=1, t<=t^d. Thus

    W_S(t)+W_A(t)+W_T(t) <= (C_S+C_A+C_T)t^d.

`join_complete_bill` proves this last step, including d=1. Constants may
depend on the fixed initial payload, epsilon and device parameters; they
do not depend on total operating age. A polynomial stage overhead does not
have to be linear in the code volume. Conversely, running an active routine
on an age-growing code every physical time step would be a different bill
and is not justified by this stage calculation.

## Scope of what is now discharged

The complete-attempt **summation** and the full-prefix record-size bound
are derived, with Lean certificates. The ideal sampler's computation and
finite record production give polynomial algorithmic counts. The existing
device cost model must cover every realised account, including passive
holding and physical failure branches. No claim is made that a physical
transfer producing the required covered quantum state has been built: that
is precisely the outstanding certificate. Once it is supplied with the
stated polynomial account bounds, no new asymptotic summation gap remains.

## The corrected reset/startup connection in the later three-stream drafts

The subsequent prose proposals use an expected reset cost. That does not
replace this pathwise invoice. For the proposed at-most-one reset per wave,
with realised reset cost at wave k at most R k^(d-1), simply charge the
worst case: sum_(k<=t) R k^(d-1)<=R t^d. A bounded number of local resets
can be absorbed into the actual wave coefficient in the same way. For
larger retry schedules use the proved deterministic attempt cap and full
invoice above. Every failed attempt remains paid.

Likewise the active sum is at most (alpha+beta)t^d for all d>=1; beta t
cannot be discarded at d=1. A complete fixed bootstrap invoice B_boot is
at most B_boot t^d for t>=1, as already represented by G3CompleteBill's
fixed charge. A propagation-speed upper bound is not itself an upper
bound on startup completion time.

Thus, with C_S containing the actual full local wave charges and any
startup/reset charges already counted there, a combined coefficient is

    C_full=C_S+gamma(I0+c)+C_T+B_extra.

B_extra contains only genuinely additional fixed charges, avoiding double
counting of endpoints/startup already in C_S or C_T. The coefficient is
independent of age. Its dependence on the fixed payload capacity, hardware,
dimension and error tolerance remains explicit. Uniformity over logical
input states at that capacity is retained.

The full hostile disposition of the new drafts, including the stock/flux,
Landauer, burst-noise and series-constant issues, is in
`G3-HOSTILE-REVIEW-2026-10-26.md`. It preserves the existing stronger
ledger rather than substituting the proposed expectation argument.
