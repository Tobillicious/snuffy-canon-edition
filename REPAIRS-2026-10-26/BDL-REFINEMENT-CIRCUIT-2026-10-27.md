# Actual BDL refinement as a local CNOT circuit

27 October 2026. Constructive development outside the canonical Lean tree.
The complete physical thermal transfer is still being joined. This note
constructs its ideal code-refinement primitive and checks actual finite
gate lists. It does not identify its bare multilevel noise with independent
single-qubit output noise.

## 1. One replacement can be reduced by local CSS elimination

Use the chain groups and attaching maps of the existing finite BDL
implementation, without changing its parity-check matrices. A physical CNOT
c->t adds the c column to the t column of X supports, and the t column to
the c column of Z supports. Stabilizer row operations change generators
without changing their joint eigenspace.

In an x cell, eliminate the internal X pivots. For a chosen row/pivot q,
CNOT(q,t) for each other occupied t makes that X generator X_q. Clear q
from other X generators by row operations. CSS commutation makes all Z
generators trivial on q. This qubit factors as |+> and is retired from the
active elimination.

The remaining internal Z generators are eliminated in the dual direction:
CNOT(c,q) makes a Z row Z_q, after which row operations clear its column.
That qubit factors as |0>. There is no remaining local H1 in an x cell,
so these two eliminations remove all its internal qubits.

Next, within each q cell, choose the root ('L',q,0). The connected local
repetition graph has Z rank |V|-1. Dual elimination therefore factors all
but its root into |0> ancillas. One physical qubit remains per old q.

The local homology and attachment identities used here are those of
[BDL, section 3.2.3, equations 77--80](https://arxiv.org/html/2605.10943v1):
the x-cell contribution has H0=F2 and H1=0, and the shifted q cell carries
one H1 generator. The induced attachment is the old incidence. The local
elimination above is our explicit circuit realization of that reduction.

The resulting CSS spans are the old code on the root qubits, plus the
isolated X_q and Z_q ancilla generators. Thus the inverse gate list encodes
any old-code state, including one entangled with an arbitrary reference,
into the new code with fixed ancillas. It is an isometry on the complete
old code; it does not prepare its logical state from scratch.

For an R_Z replacement, exchange X and Z and reverse control/target on
every CNOT. The isolated |+> and |0> roles exchange. This is an explicit
dual gate list, not an assumption that two noisy implementations coincide.

## 2. Structural depth and fault support

An x-cell program uses controls only in its own internal block. Other
cells' internal blocks are untouched; shared q-cell qubits are targets.
Different x-cell programs therefore commute. A bounded-degree conflict
graph colours their overlapping physical supports into a fixed number
of layers. The q-cell programs are disjoint. Fixed gadget sizes and Tanner
degrees bound the length of each cell program independently of level.
Hence one replacement has a fixed native CNOT depth D_0.

For any such depth-D_0 circuit, a postgate two-qubit Pauli can spread to
at most 2^(D_0+1) output qubits. Bounded check weight and incidence then
bound its syndrome footprint and the number of fault locations reaching
one check by constants. These constants can be large. They are structural
bounds; the finite observed maxima below are not asserted as all-level
upper bounds.

Composing every replacement as a bare circuit can multiply these support
bounds. The proposed complete transfer instead executes the encoder in
the short fault-tolerant processor and controls its final private output
interfaces separately. Native local reduction is not a proof that the
whole noisy encoder is already a product output channel.

The code reduction also does not by itself give a placement/routing
invoice. Source motion, target installation, swaps, idles, resets and
controller operations remain in the complete stage bill. Polynomial
nearest-neighbour routing can be included inside the short protected
processor; it must not be omitted because the algebraic gates are local
to a gadget.

## 3. Independent replay of the actual gate lists

The script refinement_circuit.py first constructs its gate list using local
CSS Gaussian elimination. A second calculation then replays only those
physical CNOTs on the original fine matrices, with no generator row
operations. It compares the entire final X and Z spans with the embedded
old code plus every isolated ancilla. This verifies the whole stabilizer
space, not merely the number of logical qubits or a compressed submatrix.

| Seed | Replacement | Old/new qubits | CNOTs | Native depth upper bound | Largest propagated Pauli/check footprint |
| --- | --- | ---: | ---: | ---: | ---: |
| 2x1 | R_X | 5 / 60 | 165 | 157 | 22 / 8 |
| 2x1 | R_Z | 5 / 60 | 164 | 167 | 22 / 10 |
| 3x2 | R_X | 13 / 206 | 604 | 309 | 41 / 12 |
| 3x2 | R_Z | 13 / 206 | 599 | 281 | 28 / 14 |
| 3x3 | R_X | 18 / 300 | 882 | 309 | 41 / 16 |
| 3x3 | R_Z | 18 / 302 | 861 | 281 | 28 / 14 |

All 15 nonidentity two-qubit post-CNOT faults are propagated through the
actual inverse circuit at every gate. The maximum check/fault-location
incidence in these cases is 132. The checks jointly retain both CSS sectors
and physical Y faults.

The next alternating step on the 3x2 seed was also replayed: 206 old qubits
to 5,116 new qubits, 16,292 CNOTs, depth upper bound 1,247, with the complete
stabilizer comparison passing. This larger run checks the circuit identity;
it does not enumerate every propagated fault of that circuit.

Reproduce both sets with:

    PYTHONHASHSEED=0 python3 REPAIRS-2026-10-26/checks/bdl-metacheck/refinement_circuit.py --second-step

REFINEMENT-CIRCUIT.json and REFINEMENT-SECOND-STEP.json record source
hashes and scope. Full gate lists, root positions, ancillas and parity
checks are under refinement-circuits/. The larger circuit artifact is
also hashed. These are finite computational receipts, not new Lean kernel
certificates or a global completion verdict.
