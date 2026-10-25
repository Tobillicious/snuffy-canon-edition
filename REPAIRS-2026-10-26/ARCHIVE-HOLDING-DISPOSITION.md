# Archive holding in the G3 bill — disposition of Gemini submissions A, B, C (26 October 2026)

Target, unchanged: the complete pathwise bill W(t) ≤ C·t^{d_G} with an age-independent C, for every
d_G ≥ 1, historical retention charged (master §21.7.5, line 2251), and decoding error at most ε on
the historical message W (master line 1045). Inputs preserved verbatim in `inputs/GEMINI-ARCHIVE-*.md`.

## Compiled this session (candidate module `Snuffy.G3ArchiveStock`, zero output, leanchecker 0, standard axioms)

* `live_stock_bill` — a holding charge of γ per held bit per step, with held stock at step s at most
  I₀ + c(s+1)^{d−1}, sums to at most γ(I₀ + c)·t^d for every d ≥ 1, **including d = 1**. With
  `G3GoodEvent.complete_bill_with_archive` this puts archive holding inside (C₁ + C₂)t^d.
* `retained_stock_quadratic` — when every transcript increment is retained (stock ≥ r·s), the
  holding charge is at least γ r t(t−1)/2.
* `rollover_quadratic` — an archive that copies the whole accumulated stock into fresh media at each
  of N epoch boundaries pays at least η r T N(N−1)/2.

The bill is charged on the **held stock**, not on the write rate. That one distinction decides all
three submissions.

## A — option (c) and the AFH refresh charge: not accepted

1. §1 integrates the write rate (b₀+b_N)(s) as if it were the held stock. If (b₀+b_N)(s) is the stock
   held at s (the live boundary transcript), the formula is right and is `live_stock_bill`, and it
   then covers d_G = 1 as well. The submission's own §2 contradicts it by giving t² for d_G = 1,
   which happens only when the whole transcript is retained (`retained_stock_quadratic`).
2. Option (c) moves the holding charge to "standing infrastructure funded by income". The G3 target
   is the complete bill with historical retention included; relabelling a term does not remove it.
   The proposed G1 guard suspension when income falls would pause protection on an income
   condition. That is a reduction of the target and is rejected.
3. The γ formula is a constant per-bit-step refresh rate. That is admissible, but constant γ alone
   does not change the stock question. "15 mK or 300 K" is not a device specification.

## B — logarithmic barrier and the hierarchical block tree: not accepted

1. §2 gives the bit written at s a barrier ∝ ln s. The barrier must cover that bit's remaining
   retention, not its write time. Over an unbounded age, no single fixed barrier suffices.
2. §3: a level-k block holds 2^k bits. Rewriting it every 2^k steps at a barrier ∝ k costs about k per
   step for that level. Summing over k ≤ log₂ t gives Θ(log² t) per step and O(t log² t) in total,
   not O(1) per step. The convergent series assumes Cost_k bounded, but Cost_k ∝ 2^k.

## C — constant-barrier epoch rollover: not accepted

Every bank written at the constant barrier ΔE₀ decays within T_epoch, so every bank that still
carries retained history must be copied at every rollover. At boundary k the transfer is the
accumulated stock r·k·T_epoch, not r·T_epoch. The total is quadratic (`rollover_quadratic`). The
scheme is constant-rate refresh with γ = η/T_epoch. Copying only the newest epoch would let the
older banks decay and lose history.

## The construction that closes the bit count for every d_G ≥ 1, d_G = 1 included

The archive holds the record's information I₀ and the **live** boundary transcript. Each transcript
increment is retired after the wave that consumes it. Then the held stock is at most
I₀ + c(s+1)^{d_G−1}, and `live_stock_bill` gives γ(I₀ + c)t^{d_G}.

The retirement must be lossless, or else charged. Each retired transcript bit is either
* recomputable from the fenced recovered region together with I₀, so dropping it loses no
  history — data processing, not coarse-graining; or
* correction entropy, whose reset is charged once at the vertex where it is produced. Such resets
  are already inside the sweep's per-vertex charge (F + α + β + R_*).

This is a property the supplied wavefront/TIWA construction must exhibit. It is not a weakening of
the target.

## Remaining point found while checking: reliability against age

The canon threshold bound `Threshold.fail_le_geometric` is P(fail) ≤ V r^d / (1 − r), linear in the
number of locations V. Holding a fixed failure ε as V grows with age therefore needs a code
distance that grows like log V, unless the final decoder of W uses redundancy across locations.

* **Decoded payload I₀ (constant size, held for about t).** This can be held passively. The archive
  is written when recovery starts, at which point t is known. Choose a barrier
  ΔE ≥ k_B T ln(c I₀ t / ε). The running power is zero within the holding, and finite-temperature
  decay at that barrier keeps the failure below ε (AFH: finite barrier, finite rate). The write
  cost is O(I₀ log t) even when the write energy grows with the barrier, which is inside O(t).
* **Live transcript and the sweep's patches (Θ(t^{d_G}) locations).** Their reliability is the
  sweep's own reliability. A per-location failure fixed by a constant distance gives a union bound
  that grows like t^{d_G}. Matching an age-independent C at fixed ε then needs the concatenation
  route: constant-distance inner patch codes, plus the final decoder of the constant-size message
  W using the redundancy of its carrier across Θ(t^{d_G}) sites, which tolerates a constant
  fraction of patch failures. This belongs to the objection-7 application certificate, which maps
  the fault model onto `Threshold` and `CorrelatedCeiling`. It is recorded there, not as a new
  objection to X3.

No canon prose has been changed by this disposition.
