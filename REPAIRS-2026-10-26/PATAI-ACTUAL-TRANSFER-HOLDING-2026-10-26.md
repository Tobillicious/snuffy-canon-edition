# Pātai: the actual transferred quantum state, at the original budgets

The maximal UPT target is fixed. This asks for one physical support, not a
change of protected content, quantifiers, fault model or complete work bill.

## Already available — do not rederive these

* Checkpoint 11 passed for the unchanged 191-module / 1,150-name canonical tree.
* G.21 gives the proposed full-decoding-history sampler, with ideal joint
  syndrome law mu <= 16 pi, and a deterministic polynomial work/bit budget.
* `ThermalEncoding.recovers_reference` proves exact recovery of the ideal
  syndrome mixture for every joint logical/reference operator.
* G.21 already derives the reference-uniform warm-start holding estimate
  `18 t Lambda(n) sqrt(C b)` from positive operator domination, Gibbs
  stationarity and the protected logical Pauli observables.
* The transfer schedule sums the original holding/transfer budgets; its
  polynomial per-stage cost has a constant-rate amortization candidate.

The physical output of a successful fault-tolerant transfer may still have
a sparse residual Pauli layer. Logical gadget correctness does not by itself
identify its syndrome/gauge law with the ideal prepared law.

## The support needed

Let E_mu be the actual G.21 ideal encoding channel and D its matching
decoder. Let Phi_t be the holding evolution already used by G.21, and let
N describe the actual residual preparation noise under the original local
stochastic fault standard, with the transfer's separately charged logical
failure event retained. The device parameters are fixed independently of
age and block size.

Please provide a construction and proof that, for every logical input and
every reference register R, the actual stage output can be held for duration
2^j within the original stage error budget epsilon/2^(j+2), using block size
and complete pathwise stage work polynomial in j and log(1/epsilon).

One sufficient form is a bound on the actual decoded channel, uniform in R:

    ||[(D Phi_t N E_mu) tensor id_R](rho_LR) - rho_LR||_1
       <= a poly(n) (t+1) exp(-c n^eta),

for the required stage times, with fixed positive constants. The estimate
must include the initial decoded error introduced by N, not just the
subsequent change from time zero.

Another sufficient form is an actual feed-forward transfer whose output
decomposes into a covered warm-start branch and a failure branch of the
original budget, with a physical implementation and full work certificate.
No Markov-chain preparation or stronger correlation ansatz is required by
this question. An equally strong different construction is suitable.

If using the bad-projector route, the existing G.21 calculation only needs
the time-integrated bad weight. A suitable bound for
`Tr(P-perp Phi_t(N(rho_beta)))`, together with the initial logical-error
certificate, would supply it. A one-time density bound or a local gap alone
does not establish that long-time estimate.

## Why the existing statements do not yet supply it

Complete positivity gives

    N(E_mu(rho_LR)) <= 4 C N(rho_beta tensor rho_R).

It does not replace N(rho_beta) by the stationary rho_beta. The G.21
stationarity argument therefore cannot simply be reused with no additional
estimate. Conversely, failure of that particular comparison is not a proof
that all permitted feed-forward constructions fail.

The full bill must retain preparation, handoff, random and syndrome records,
retirement, holding, guard, controller and export charges. The target remains
`W(t) <= C t^d` with C independent of age for every admitted d>=1. Replacing
the unknown quantum state/reference by classical records would not supply
the stated channel guarantee.

## Sources already followed

G.8, G.10, G.16 and G.18–G.21; `G1Held`, `G1Refinement`,
`KnillLaflamme`, `ExRecBound`, `EdgeLaw`, `ThermalEncoding`, `WarmStart`,
`StageSchedule`, `WorkBilling`, `G3CompleteBill`, and the TransferRate
candidate. The previous noisy-preparation and (R) notes have been read as
research records, with their corrections and unproved assertions retained
as such. BDL's coarse-graining/lifetime/initialization results and the
published counting theorem used by G.21 have already been followed.

The independent source audit and complete stage-cost bookkeeping continue
while this physical support is requested.
