Three Gemini submissions pasted by the author on 26 October 2026 (round 8). Their full texts are in
the session transcript. This file records their claims, quoted from the pastes.

R8-1 "The Eroder Contraction Lemma" (Peierls contour):
  - |∂E| ≥ c n^{(d-1)/d} for a connected failed cluster of size n;
  - "For an eroder E to persist or grow, every site on its boundary ∂E must either be hit by a fresh
    physical fault witness or be overwhelmed by corrupted erasures";
  - P(eroder of size n) ≤ Σ_shapes (z p̃)^{|∂E|} ≤ Σ_n A (z p̃)^{c n^{(d-1)/d}}, "forcing the sum to
    converge absolutely".

R8-2 "Formalization of Parts 1 and 2":
  - a failed patch u flags its handoff as an erasure e; "erasures are corrected up to the full code
    distance d−1, whereas unflagged errors are constrained by ⌊(d−1)/2⌋"; "failure at u does not
    amplify error weight at v";
  - windows beyond the dependence radius "have conditionally independent failure distributions given
    their boundaries"; P(∩ Y_k = 1) ≤ ∏_k (C(|W|,k) p^{k|U|});
  - "P(Σ Y_k ≥ N·n) ≤ K C(N,n) (C(w,k) p^k)^n".

R8-3 "Assembling the outer decoder W and the age-independent pathwise work bill":
  - an outer linear code W (expander or Reed–Solomon) across M macro-blocks tolerates a fraction
    δ_W/2 of failed patches; per time slice, P(failed fraction ≥ θ_crit) ≤ K C(M, θM) q^{θM};
  - E[W_total(t)] ≤ V t (U_healthy + O(ρ^k)(c_repair − U_healthy)); "the work per unit spacetime
    volume remains strictly bounded by a constant".
