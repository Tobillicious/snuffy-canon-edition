## G.12 The wavefront sweep succeeds, and its complete bill is \(O(t^{d_G})\) (G3)

The wavefront recovery of §21.7 is now proved to succeed, and its full bill is
derived, with no cumulative bound taken as input.

**Sweep and fence.** Give each vertex its shell index. Wave \(k\) applies the
single-shot local correction to shell \(k\), reading the already-frozen
interior as a static, gauge-fixed boundary. Between waves, outer activity
(the world and any agent) may write anything outside the frozen interior and
nothing inside it. This is the TIWA write fence
(`TIWASource.outerUpdate_read_frozen`).

**Success and quiescence** (`G3Sweep.sweep_recovers`). Suppose the local
correction of a vertex returns its target whenever every inner vertex already
holds its target. Then after \(k\) waves every vertex of the first \(k\)
shells holds its target, whatever the outer activity. The proof is induction
on waves. A vertex of shell \(k\) is corrected against an interior that the
fence has left recovered. A vertex of an earlier shell is untouched by the
wave and by the fenced outer activity. Recovery therefore succeeds, and the
recovered state is retained. Each vertex is corrected in exactly one wave,
its own shell (`sweep_visits`), so nothing is reworked.

**Wave count from finite propagation** (`waves_from_spread`). If the region
needing recovery at age \(t\) lies within the first \(c\,t+r\) shells, the
sweep needs at most \(c\,t+r\) waves. This is the upper use of finite
propagation, from locality (P4) and the Lieb–Robinson velocity. It does not
replace the lower radius of §21.5, which comes from the carrier information
argument.

**The complete bill** (`sweep_bill`). Let the complete metered ledger charge
each wave \(k\) at most \(\alpha k^{d-1}+\beta\). This charge includes
holding, guard, routing, reset, verification, controller export and
deployment. Add a metered rollback of at most \(R_*\) per wave and fixed
endpoint charges \(F\). Then, for \(t\ge1\), recovery succeeds on the whole
region and

\[
W(t)\le (F+\alpha+\beta+R_*)\,(c+r)^{d}\;t^{d},
\]

with a coefficient independent of age (`G3CompleteBill.valid_work_bill_from_complete_ledger`,
`valid_bill_bound_in_age`). This is the matching upper construction. With the
lower bound of §21.6, it gives \(W_{\min}(t)=\Theta(t^{d_G})\) in the original
permitted class.
