# Latest author proposal — symmetry and gapped DOS

The author proposes defining the ideal block as a charge-q eigenspace,
using [H_coupling,Q]=0 and spectral functional calculus to obtain
[H_coupling,P_ideal]=0. They propose f_ideal(ω)=|g(ω)|² D(ω), with
D(ω)=Σ_k δ(ω−E(k)) and E(k)≥Δ, infer D and f vanish below Δ, then infer
f=0 μ-a.e. from μ([0,Δ])=0.

Disposition for Claude: the spectral-projector commutation implication is
valid under the required finite-dimensional/bounded or strong-commutation
hypotheses. One must still prove that all actual couplings preserve the
chosen system charge; conservation of a combined system+bath charge alone
allows charge exchange and does not supply this.

The almost-everywhere inference is false: vanishing on a μ-null gap gives
no vanishing on the region carrying μ. For example μ is Lebesgue measure
restricted to [Δ+1,Δ+2], and f=1 there and 0 on [0,Δ]. Both proposed gap
conditions hold, but f is not zero μ-a.e. The earlier valid separation lemma
needs the system spectrum supported INSIDE the bath-null region, rather than
both spectra vanishing there. Also treat density of states as a measure,
handle the threshold endpoint, and retain frequency/energy units.

No part of this proposal was added to canon code or declared physically
proved. The full UPT target is retained. The author requested banking and
handoff to Claude because the session usage window is almost exhausted.
