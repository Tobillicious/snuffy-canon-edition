Three Gemini submissions on item 5, pasted by the author on 26 October 2026 (round 7). Their full
texts are in the session transcript. This file records their claims, quoted from the pastes, so
the disposition below can be read on its own.

R7-1 "The Markovian Renewal Property of Local Patches":
  - "time does not compound error depth; time is chopped into constant-depth renewal windows";
  - "the probability of a cascade growing to diameter s decays exponentially (e^{-s/ξ}). It cannot
    scale with system age t";
  - "The number of distinct witness configurations of size s is bounded independently of t."

R7-2 "The Bounded Causal-Cone Renewal Lemma":
  - Lemma 1 (Temporal Memory Erasure): "a projective measurement constitutes a complete decoherence
    of phase and error history … the error process [is] a finite-memory Markov random field";
  - Lemma 2: N(s) ≤ C^s poly(s), "with zero dependence on t";
  - Theorem: "P(Macroscopic failure of diameter S anywhere in Λ_t) ≤ Σ_{s≥S} N(s) ρ^s ≤ c0 e^{-c1 S}
    … Because this bound has no t multiplier, the total accumulated error probability … remains
    bounded by a constant expectation per unit spacetime volume. The work bill … stays strictly O(t)".

R7-3 "The Spacetime Density Bound":
  - Theorem: sup_t E[(1/|Λ|) Σ_v X_{v,t}] ≤ C ρ^k ≤ θ_crit, with k = ⌈d/2⌉;
  - Step 1: {X_{v,t}} is an m-dependent random field;
  - Step 2: P(X_{v,t} = 1) ≤ Σ_{s≥k} N(s) ρ^s with N(s) ≤ B^s;
  - Step 3: "we invoke a dependent law of large numbers or Liggett-Schrittnut-Stapley concentration
    inequality … the outer decoder almost surely succeeds … constant expected cost per unit volume
    … O(t)".
