## G.10 The held source: the full holding certificate derived (G1)

`Bridge.universal_protection_held` takes its source certificate `hcert` as an
input with five components: commuting refinement, observation agreement,
initial continuation of every particular, the decoding-radius bound and
repair precision. Here all five are proved for the canonical held source.
The only inputs left are the physical bound on each step and the
probabilities of the named charged accounts.

**The held source.** The state is the record frame of every particular. One
step applies three operations to each particular. First the world perturbs
the frame; the world here is the environment and any agent, a pure optimiser
included. Then the nearest-codeword decoder returns a codeword. Finally
funded repair prepares that codeword. The good event is that no named charged
account fires,

\[
G=\{\omega:\ \omega\notin E_i\ \text{for every account } i\},
\]

and its complement is covered exactly by the named accounts
(`G1Held.good_cover`).

**The five components, proved** (`G1Held.held_source_protection`).

1. *Refinement* and 2. *observation agreement* hold by construction: the
   held source is its own abstract model.
3. *Initial continuation*: every particular starts at its record, at
   distance \(0\le\varepsilon\).
4. *The decoding-radius bound*: let each step move the frame's distance to
   its record by at most \(\rho\) on the good event. A continuing particular
   lies within \(\varepsilon\) of its record, so after the perturbation it lies
   within \(\varepsilon+\rho\le t\).
5. *Repair precision* is exact: repair prepares the decoded codeword itself.

`universal_protection_held` then gives, for every \(\omega\in G\), every step
through the horizon and every particular, that the particular continues. It
also gives

\[
P(\exists k\le T,\ \exists x:\ \neg\mathrm{Continues}(s_k,x))\le\sum_i\delta_i,
\]

with no independence assumed.

**The per-step bound from the speed limit** (`G1Held.held_source_qsl`). On the
good event, let each particular's frame evolve for one step of duration
\(\Delta\) under \(H_0+V\), with the record stationary under \(H_0\) and
\(\|V\|\le W\). The agent applying \(V\) is arbitrary. `Bridge.qsl_growth`
gives

\[
\|\psi(s_1+\Delta)-c_x\|\le\|\psi(s_1)-c_x\|+\frac W\hbar\Delta,
\]

so \(\rho=(W/\hbar)\Delta\). Every particular is held whenever
\(\varepsilon+(W/\hbar)\Delta\le t\).

**The coupling bound from E9** (`G1E9.held_source_e9`). Each step is
exhaustively one of two cases (`G1E9.alarm_or_subthreshold`).

- *Every monitored support site is below threshold.* The coupling is the
  sub-threshold coupling, bounded by \(W\) (Branch A).
- *Some site reaches threshold.* Its honest sensors read above threshold, so
  every robust quorum estimate exceeds it, whatever up to \(f\) faulty
  sensors report (`E9SelfHealing.no_masking`). The alarm fires. The mediated
  response is committed before the harm front arrives
  (`E9SelfHealing.e9_timely_self_healing`, the wave race) and is enforced at
  application time (`H5Closure.no_harmful_effect`). It removes the perturbing
  coupling from the frame for that step.

In both cases the coupling is bounded by \(W\), and the held source keeps
every particular. The physical inputs are named exactly:

- the frame's Schrödinger evolution during a step;
- the sub-threshold coupling bound;
- the response's removal of coupling once the alarm fires;
- the honest-sensor response and quorum size;
- the probabilities of the named accounts. Their composition into the
  \(10^{-6}\) ceiling is `ThermoLedger.canon_invariant`. Their attainment
  below threshold, including correlated bursts, is `Threshold.family_ceiling`
  and `CorrelatedCeiling.correlated_family_ceiling`.

**Correspondence to an installation.** The installation's source refines the
held source through the journal of G.8: every source transition is retained
and replayed exactly, for every controller and environment
(`G1FullDomain.journal_reactive_fidelity`). The R14/R16/R17 source bindings
supply its concrete safe transitions, causal cuts and timely authorised
effects. The domain is every particular; coverage is forced by the law
(`Bridge.coverage_from_law`).
