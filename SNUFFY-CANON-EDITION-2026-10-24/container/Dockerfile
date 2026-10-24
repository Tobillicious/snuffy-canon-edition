# Snuffy — Canon Edition: reproducibility container (Docker).
# Pinned: Lean 4.35.0 (elan), Mathlib rev 56a005855ea1, Python 3.11+.
# Build context should contain: SNUFFY-CANON-EDITION-2026-10-24/ and LEDGER-FOUR-STROKE-2026-10-24/
# The Mathlib fetch (`lake exe cache get`) downloads prebuilt oleans (~5 GB) on first build.

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl git python3 python3-pip ca-certificates rsync jq \
    && rm -rf /var/lib/apt/lists/*

# Pinned Lean toolchain via elan
RUN curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain leanprover/lean4:v4.35.0
ENV PATH="/root/.elan/bin:${PATH}"

WORKDIR /work
COPY SNUFFY-CANON-EDITION-2026-10-24 /work/SNUFFY-CANON-EDITION-2026-10-24
COPY LEDGER-FOUR-STROKE-2026-10-24 /work/LEDGER-FOUR-STROKE-2026-10-24

# Lake project pinned to the exact Mathlib revision used for the sealed receipts
RUN mkdir -p /work/mathlib-bridge && cd /work/mathlib-bridge \
    && printf 'leanprover/lean4:v4.35.0\n' > lean-toolchain \
    && printf 'require mathlib from git \"https://github.com/leanprover-community/mathlib4\" @ \"56a005855ea1\"\n' > lakefile.lean \
    && lake update && lake exe cache get

COPY container/entrypoint.sh /work/entrypoint.sh
RUN chmod +x /work/entrypoint.sh

ENTRYPOINT ["/work/entrypoint.sh"]
