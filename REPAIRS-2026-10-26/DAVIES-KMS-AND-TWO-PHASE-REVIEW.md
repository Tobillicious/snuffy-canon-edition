# KMS stationarity and the proposed two-phase bridge

26 October 2026. The author's candidate is preserved verbatim under inputs/.
This review retains a valid stationarity proof and distinguishes it from
the physical preparation, holding and cost applications. It does not change
the maximal UPT, full historical/quantum domain, arbitrary-reference target,
original stage error allowances or gross/pathwise work ceiling.

## The valid stationarity statement

Take the lowering-frequency convention [H,L_omega] = -omega L_omega,
L_{-omega} = L_omega^dagger and nonnegative rates satisfying
gamma(-omega) = exp(-beta omega) gamma(omega). The jumps must be the actual
Bohr components of the specified coupling operators. For rho = exp(-beta H)/Z,

    L_omega rho = exp(-beta omega) rho L_omega.

Both L_omega^dagger L_omega and L_omega L_omega^dagger commute with H and rho.
Writing D[L](rho) = L rho L^dagger - {L^dagger L,rho}/2 gives

    D[L_omega](rho)
      = exp(-beta omega) rho L_omega L_omega^dagger
        - rho L_omega^dagger L_omega,

    D[L_omega^dagger](rho)
      = exp(beta omega) rho L_omega^dagger L_omega
        - rho L_omega L_omega^dagger.

The weighted positive/negative frequency pair therefore cancels exactly.
Zero-frequency jumps obey the same detailed-balance construction and give
zero contribution. The Hamiltonian commutator vanishes. Thus L(rho)=0 for
this specified generator. This is a valid finite-dimensional prose proof,
not a new Lean receipt. The standard Davies relations and separate role of
gap estimates are set out in [Temme, Lower bounds to the spectral gap of
Davies generators](https://arxiv.org/pdf/1305.5591), equations 8--9.

This proves stationarity, not preparation from a particular initial state,
uniqueness, a quantitative convergence rate or preservation of an unknown
logical input. Full convergence to one Gibbs state would not by itself
encode that input. The actual gauge preparation and logical transfer must
retain their existing source correspondence and arbitrary-reference guarantee.

The code Hamiltonian must also be identified with the G.21 Hamiltonian.
Adding generic noncommuting single-qubit fields changes its Gibbs state and
can invalidate the stabilizer/syndrome representation used by the sampler;
that representation cannot be carried over without a separate derivation.

## The global gap has not been proved

The proposed local gap or MLSI statements are assumptions in the reply.
A local spectral gap is not an MLSI proof, and overlapping updates do not
automatically tensorize with a polynomial global bound. The actual assembly
or comparison theorem and its verified hypotheses are required. The stated
gamma_local/poly(n) estimate would in any event be size-dependent, not the
claimed positive constant independent of n.

For the relevant class of commuting Pauli Hamiltonians, [Temme,
Thermalization time bounds for Pauli stabilizer Hamiltonians](https://arxiv.org/abs/1412.2858)
gives bounds involving system size and a generalized energy barrier, and
states additional conditions for constant bounds. It is not a theorem
giving a constant gap solely from bounded local patch size. No local source
for the proposed SLH/Fibonacci gap assertion has been identified.

A mixing construction remains optional. The existing G.21 sampler already
addresses ideal thermal preparation. Gibbs stationarity of the holding
generator does not make a residual preparation channel N fix rho_beta, or
bound Phi_t(N(rho_beta)) by the equilibrium envelope.

## The spacetime fault application is still separate

The correct existing probability tools are MatchingWitness, EdgeLaw or
WeightedEdgeLaw, Threshold and AgeReliability. HistoryPolymer controls static
coarse-graining histories, not physical spacetime fault statistics.
In minimum-weight recovery a failed residual has a path/cycle containing
faulty and correction edges, at least half faulty. It is not the asserted
if-and-only-if condition on a connected component of raw faults. The actual
recovery circuit must establish its witness correspondence and joint fault
law, including preparation and measurement/controller faults.

ThermalEncoding.recovers_reference proves ideal syndrome-branch recovery.
The trace-norm bound 2 Pr(fail) also requires reference-preserving correctness
on the actual good fault branches, or the corresponding diamond-norm fault
certificate. Those physical branches are not identified by invoking the
ideal equality alone.

## The distance calculation needs the duration twice

Use D for code distance, N for the spatial location count and
kappa = (alpha/2) ln(1/p) > 0. Even granting the proposed failure bound,

    error <= 2 C 2^a N exp(-kappa D),

the original error allowance epsilon/2^(a+2) requires

    kappa D >= (2a+3) ln 2 + ln(C N / epsilon).

The submitted distance condition is only

    kappa D >= (a+3) ln 2 + ln(C N / epsilon).

Substitution gives error <= epsilon/4, which does not decrease with a.
The missing term is a ln 2. The corrected logarithmic-distance calculation
is already retained in ACTIVE-HOLDING-BRIDGE-CANDIDATE-REVIEW.md; this
arithmetic is not itself the physical fault certificate.

## The recovery schedule must be one specified process

Phase 2 recovers after every one of 2^a clock cycles, whereas the work
summary charges only logarithmically many recovery epochs. The same physical
channel and its complete invoice must be used in both parts. If recovery is
sparse, the passive intervals need the actual noisy quantum holding bound;
if recovery is frequent, every cycle must be charged. The valid finite
geometric work summation is retained with complete epoch charges, but it
does not supply the protection during an unanalysed interval.

The KMS stationarity proof can be retained now. The two-phase text as a whole
does not yet provide the actual noisy holding/transfer certificate and is
not entered as the definitive G.21 proof. All 192 canonical sources remain
unchanged under checkpoint 12. No new build, merge, push or publication was
performed.
