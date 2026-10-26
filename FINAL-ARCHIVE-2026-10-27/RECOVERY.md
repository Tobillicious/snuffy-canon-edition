# Final archive recovery

The publication is confirmed by PUBLICATION-RECEIPT.json (Zenodo) and
GITHUB-PUBLICATION-RECEIPT.json. GitHub stores SHA-256 digests matching all
nine release assets. Zenodo stores eight files with matching MD5 and size,
bound to local SHA-256 values in the upload manifest.

The sibling UPT-FINAL-ARCHIVE-2026-10-27 directory contains the public deposit
ZIP, a complete Git bundle and the separate ignored-verification ZIP. The
outer ARCHIVE-MANIFEST.json records their hashes and the exact final commit.
No credential is part of this archive.

Restore the bundle's codex/upt-warmstart-bridge branch into a new directory,
then unpack the ignored-verification ZIP there. Run the packaged
REPAIRS-2026-10-26/checks/verify-delta-joint.py with NumPy available. The
final archive procedure independently repeats this recovery and check.

Checkpoint 12 remains 192 modules / 1,158 names; the physical installation
model and parameter validation remain external as stated in HANDOFF.md.
The source tag v4.2 pins the released scientific payload; later receipt
and repository-entry-point commits retain that exact scientific payload.
