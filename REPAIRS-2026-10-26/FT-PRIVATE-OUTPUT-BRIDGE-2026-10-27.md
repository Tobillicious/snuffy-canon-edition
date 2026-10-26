# Constructing a private output interface for the compensated preparation

27 October 2026, Pacific/Auckland. Constructive continuation. The remaining
application is the complete physical transfer, including its admitted noise
model and charged implementation. The results here supply a channel
construction and its error accounting. They are not a completed physical
installation, a canonical Lean increment, or a replacement of the maximal UPT.

The new route prepares an input law adjusted to the output noise, executes
the short transfer fault tolerantly, and then uses the existing passive
holding theorem. It does not perform active correction throughout an age
interval of length 2^a.

## 1. The source theorem and the correlation it leaves

[Christandl, Fawzi and Goswami, *Fault-tolerant quantum input/output*,
arXiv:2408.05260v3](https://arxiv.org/html/2408.05260), Definition 20 and
Lemmas 29--32, provide polynomial-size encoded computation and interfaces.
With logical coordinates L and an auxiliary code coordinate G, an encoded
unitary is close in diamond norm to its logical action tensor a channel on
G. An encoded measurement discards G. Encoded state preparation similarly
separates the prescribed logical state from its auxiliary state. Their
output interface W:L tensor G -> qubit is within 2cp of id tensor trace.
Theorem 33 explicitly retains a joint auxiliary channel: its general
output noise need not be independent. The model has independent noisy gate
channels and noiseless classical processing. Those hypotheses must be
realised or replaced; local-stochastic correlations alone do not establish
them. The construction below is our additional application, not a product
noise assertion attributed to that theorem.

## 2. Exact gauge-refresh identity

For each intended physical output, prepare a separate encoded logical Bell
pair A,B. In code coordinates its comparison state is

    |Phi><Phi|_(A_L B_L) tensor eta_(G_A G_B).

The two gauges may be entangled. Different resource pairs are independent.
The receiving B blocks never interact with one another or with the source.
They remain encoded during waiting and feed-forward; all their storage and
correction operations are private and included in the fixed schedule.

Let the source state be any omega_(S_L G_S R). In particular, G_S can be
correlated with both the logical state and the reference. Measure S_L,A_L
in the logical Bell basis through the encoded measurement gadget. In its
exact comparison channel, both measured gauges are traced out.

Tracing G_S,G_A commutes with this logical measurement. Before its logical
action, the remaining state is exactly

    omega_(S_L R) tensor |Phi><Phi|_(A_L B_L) tensor tau_(G_B),
    tau=Tr_(G_A) eta.

For Bell outcome m in {I,X,Z,Y}, the unnormalised B_L,G_B,R state is

    (1/4) (P_m tensor I_R) omega_(B_L R) (P_m tensor I_R)
              tensor tau_(G_B).

The outcomes are uniform and independent of the corrected logical/reference
state and receiving gauge. This equality extends to every reference by
linearity, not merely to unentangled inputs. For many outputs the statement
has the product factor 4^(-n), even when their logical inputs are entangled.
The receiving gauges are the product of their private marginals tau_j.

This is the specific reason fresh resources remove old output-gauge
correlations. Merely placing decoders in separate regions would not do so.

## 3. Private decoding and the resulting output channel

Let W_j be the physical decoding interface on B_L,j tensor G_B,j, including
its private storage, resets and circuit faults. Put

    D_j(rho)=W_j(rho tensor tau_j).

Decode before applying the teleportation Pauli correction. Summing the
uniform Bell outcomes then gives the effective one-qubit channel

    N_j(rho)=(1/4) sum_m P_m D_j(P_m rho P_m) P_m.

This is the Pauli twirl of D_j. Its Choi state is diagonal in the Bell
basis; thus N_j(rho)=sum_P q_(j,P) P rho P, with nonnegative q summing to
one. The interface norm bound gives

    ||D_j-id||_diamond <= 2cp,
    ||N_j-id||_diamond <= 2cp,
    sum_(P != I) q_(j,P) <= cp.

The last equality uses that a Pauli channel has diamond distance twice its
nonidentity probability. Private resources and independent private gate
noise make the joint channel the product of the N_j. Unequal X,Y,Z rates
are allowed. The new PauliInterface candidate proves the exact inverse
algebra for these unequal rates; depolarization is not assumed here.

The physical final Pauli corrections also have to be charged and modelled.
Independent Pauli-covariant correction noise composes with N_j and keeps
this form. Arbitrary outcome-dependent noisy corrections do not follow
from the displayed ideal twirl. The finite check states this limitation.
General correlated gate faults likewise do not become independent through
this algebra. This development establishes a construction in the stated
private-interface model; the full installation must supply that model or
a proved generalisation. It does not narrow the maximal target.

## 4. Approximation error does not acquire a holding-time multiplier

Use the encoded comparison channels from the source theorem for the
processor, each Bell preparation, private encoded waiting, and the Bell
measurements. Replace them one at a time. Their diamond errors sum because
the intervening maps are channels. The receiving blocks are references
when a Bell measurement gadget is replaced. Their entangled gauges are
therefore covered by its uniform norm estimate.

The exact comparison circuit has the output form

    (product_j N_j) Enc_mu Dec_old (product_i N_in,i).

The source auxiliary coordinates are discarded at the final encoded Bell
measurement. Consequently correlations carried by the input-interface
auxiliaries do not leave an unspecified output-gauge channel. The logical
input channels are N_in,i=Tr_(G_i) InputInterface_i. Under independent
stochastic Pauli faults in a stabilizer implementation they are Pauli
channels of rate O(p); general gate noise requires a separate input bound.

If the short transfer has M encoded locations and K private resources,
the source estimates give an overall comparison error bounded by

    delta_FT <= C (M+K) sqrt((cp)^r)

for the chosen accuracy parameter r, with polynomial circuit size in r.
Taking r=O(a+log(M+K)+log(1/epsilon)) meets an exponentially small stage
allocation while retaining polynomial work in a. The constants are fixed
by the selected fault-tolerant scheme.

If two prepared channels are within delta_FT in diamond norm, subsequent
holding and decoding keep that error at most delta_FT, for every reference.
It is not multiplied by 2^a. The nonvanishing O(p) output-interface noise
is handled by compensation, rather than put into this exceptional error.

## 5. The input endpoint uses the existing initial sparsity theorem

At the old block's input, the effective N_in layer is a bounded layer of
local Pauli noise. It is not an entire holding interval. The existing
thermal-plus-fault joint-occupation estimate therefore applies to every
partial layer, with the warm-start factor retained.

The BDL witness counting proof needs an upper bound on joint occupation of
its finest syndrome subsets. It does not require that the new law be Gibbs
if that upper bound is supplied directly. Apply the witness enumeration
with the effective occupation parameter in place of thermal fugacity.
At sufficiently small fixed parameters it bounds each partial layer's
unstable probability by polynomial(n) exp(-c n^eta).

For a fixed Pauli fault path, a single-qubit fault at a stable syndrome
preserves the decoded logical/reference state. A union bound over endpoint
locations, followed by the trace-norm bound two on a failing branch, gives

    e_in <= polynomial(n) exp(-c n^eta).

This charges initial logical error explicitly. No claim about long-time
transport of a sparse law is used. The additional joint-occupation lemma
in NOISE-COMPENSATED-PREPARATION-2026-10-27.md supplies the corresponding
bound for all partial compensated output layers.

## 6. Connect the actual output to passive holding

Sample mu<=4q, where q is the positive compensated law satisfying Nq=pi
for N=product_j N_j. The counting construction, its fixed finite coin
budget and the retained decoding history are in the compensation note.
Positivity of N gives

    Nmu <= 4pi.

For the logical/reference state this gives the existing domination by
16 rho_beta tensor rho_R. The retained sampling and teleportation records
need a more careful statement: they are kept physically, and need not be
independent of the syndrome. The tracked-record derivation below applies.
Its dynamical error is still at most

    36 Lambda(n) T sqrt(b_beta).

Include both endpoint logical errors and the short-transfer comparison:

    e_stage(T) <= e_old + e_in + e_out + delta_FT
                       + 36 Lambda(n) T sqrt(b_beta).

Here e_old is the incoming archive error, carried separately in the global
composition. The newly allocated stage errors are the other four terms,
plus any controller/calibration failure allowance. With n^eta a sufficiently
large fixed multiple of a+log(1/epsilon)+log n, and T=2^a, they fit the
original epsilon/2^(a+2) allocation. The factor 2a ln 2 is retained in
the size choice when comparing time growth with the shrinking allocation.

An explicit, deliberately nonoptimal size schedule avoids an implicit
equation involving log n. For fixed 0<epsilon<=1, take

    s=a+ln(1/epsilon)+1,
    n_target=ceil(K s^(2/eta)).

Choose the least available BDL level meeting that size, with the fixed
one-level growth factor included in the volume bound. The resulting volume
is polynomial in s. Each spatial exponent is at least a fixed multiple of
K^eta s^2; the time/allocation debt is O(s), and every polynomial prefactor
contributes only O(log K+log s) to its logarithm. Since log s<=s for s>=1,
a sufficiently large fixed K meets all stage inequalities simultaneously.
The same schedule accommodates the square-root endpoint bound below.
Constants are fixed for the chosen device and tolerance, independently of
archive age; a new noise rate is not selected at every age stage.

There is no protected-logical-state contraction, global Gibbs mixing or
time-suppressed failure probability in this construction.

### Keep the sampler and teleportation records

Let H contain the retained classical records and let E:L->Q tensor H be
the actual preparation channel. Put omega_QH=E(I/2). For every input with
reference R, the elementary reference inequality gives

    (E tensor id_R)(rho_LR) <= 4 omega_QH tensor rho_R.

No factorisation of omega_QH is asserted. Holding acts as Phi_t tensor id_H.
The bad projector acts on Q. Hence its weight in this comparison state
depends only on omega_Q=Tr_H omega_QH. The compensated, outcome-averaged
calculation proves omega_Q<=4rho_beta; the outcomes themselves remain in H.
Here id_H is the comparison for the retained-record holder. Its own physical
storage faults and lifecycle costs remain in the existing classical-record
accounts; this estimate does not grant a free perfect physical memory.

For a dressed Pauli derivative K with PKP=0 and ||K||<=Lambda, and any
observable B on R tensor H with norm at most one, projector-block
Cauchy--Schwarz gives

    |Tr[(K tensor B) rho_QHR]| <= 3 Lambda sqrt(Tr[Q_bad rho_QHR])
                               <= 6 Lambda sqrt(Tr[Q_bad omega_Q]).

The identity-Pauli coefficient of the decoded-state difference is zero:
holding Q cannot change the R,H marginal. Expanding the other three logical
Paulis and integrating gives the full retained-record estimate

    ||rho_decoded,LHR(T)-rho_decoded,LHR(0)||_1
        <= 18 Lambda integral_0^T sqrt(Tr[Q_bad Phi_s(omega_Q)]) ds
        <= 18 Lambda T sqrt(4 b_beta).

Thus retaining H does not require a false joint Gibbs/product domination.
The physical marginal suffices for this estimate, while the trace norm
still tests arbitrary joint observables on the old reference and records.

Initial correctness must also include H. In the stochastic Pauli circuit
model, a correctable fault path acts as logical identity and produces
records independent of the unknown logical state. The same good-path
argument therefore gives e_out<=8m B_n, with the records retained.

If a private decoder has coherent local errors before its outcome twirl,
use a conservative version. Insert the stable-syndrome projector before
each local channel only in a mathematical comparison process. Every Kraus
operator is a linear combination of the local Paulis, all of which act
as logical identity on that stable input sector. The comparison process
therefore factors into the unchanged logical/reference state and a
subnormalised record/gauge state. The gentle projection estimate and a
telescoping sum give distance at most 2 sum_j sqrt(b_j) from the actual
process. Normalising the comparison costs at most the same amount.

Each actual-input b_j is at most four times the max-mixed-input bad weight;
the latter is at most 4B_n by compensation and the partial-layer bound.
Consequently e_out,LHR<=16m sqrt(B_n) is sufficient. This merely halves
the spatial suppression exponent; it leaves the polynomial stage-size
and complete-work join intact. No physical postselection or extra
unmetered projection has been introduced.

## 7. Costs and implementation still to join

The sampler, ideal CSS encoder/decoder, FT overhead, private resources,
classical feed-forward and all retained records have to run on a fixed,
padded, bounded schedule. This keeps the private output channels independent
of sampled histories and gives a realised polynomial stage invoice. No
unbounded repeat-until-success step is used. The actual one-replacement
BDL CNOT encoder is constructed and replayed in the companion refinement
note; composing such replacements inside the short FT processor avoids
assuming that bare multilevel fault spread stays constant.

The existing TransferRate/G3 join absorbs polynomial stage work at the
doubling schedule for every admitted d_G>=1. It does not pay for active
correction throughout 2^a. Input/output transport, clocks, helper resets,
classical fault tolerance and entropy export remain explicit accounts.

The unresolved full-installation correspondences are: the precise admitted
correlated-fault model at the private endpoints; faulty final corrections;
the complete routed controller implementation; and rate calibration or a
specified known-rate device law. A robust O(1/n)-accuracy rate estimate is
sufficient by the bound in the compensation note. These tasks have not
been relabelled completed by the finite or Lean development checks.

## 8. Evidence from this continuation

- TELEPORTATION-GAUGE-REFRESH.json checks all 16 matrix units of S tensor G_S
  for three resource gauges, including two entangled gauges. It verifies
  the branch identity and the private-decoder twirl, with maximum error
  below 4e-16. This is floating-point complete-channel validation.
- A control with correlated, unrefreshed output gauges differs in trace
  norm by one from the product-noise assumption.
- PauliInterface.lean has six new development statements, with zero-output
  compilation and kernel checks and standard axioms only. The separate
  canonical receipt remains 192 modules / 1,158 names.
- PAULI-INTERFACE-EXACT.json records exact rational tests on the actual
  joint-CSS seed syndrome spaces, including unequal spatially varying
  Pauli rates and a whole-system rate-error bound.

No merge, publication, final canon insertion or global completion follows
from these development records.
