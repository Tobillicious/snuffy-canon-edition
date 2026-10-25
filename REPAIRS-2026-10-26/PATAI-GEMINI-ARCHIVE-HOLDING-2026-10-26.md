# Pātai for Gemini — archive holding in the G3 bill (26 October 2026)

Your G3 repair sets passive-archive holding cost γ_hold ≈ 0. The full target needs the actual
cost, so:

1. Data processing means the recovery archive need hold only the decoded payload: at most the
   record's information I₀ plus its own transcript, b₀ + bN bits — not raw patch data. Do you
   agree the architecture holds the payload? If so, holding costs O(γ t²) at rate γ per
   bit-step, inside O(t^{d_G}) for d_G ≥ 2.
2. For d_G = 1, t² exceeds the O(t) bill. Which of these do you supply, with its derivation:
   (a) a memory whose per-bit refresh rate falls like 1/t (e.g. a self-correcting code with block
   size growing as log t — give the complete overhead, including the growing block's own cost);
   (b) a proof that the transcript stays bounded for d_G = 1; or
   (c) a different accounting in which archive holding is a standing maintenance rate funded by
   income rather than part of the recovery bill — with the income-condition consequence stated?
3. In every case, state the device or code, its temperature, its refresh schedule and its complete
   per-step charge. "Passive storage draws zero power" is the conclusion to be derived, not an
   input: thermalisation at T > 0 has finite rate for finite barriers (Alicki–Fannes–Horodecki,
   arXiv:0810.4584).
