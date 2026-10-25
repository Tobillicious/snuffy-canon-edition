#!/usr/bin/env python3
from pathlib import Path
import os, subprocess, sys
bank = Path(__file__).resolve().parent
root = bank.parent.parent
project = root / "BEAM-UPT-2026-10-22/mathlib-probe"
here = root / "SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25/lean"
bin_dir = Path("/Users/admin/.elan/toolchains/leanprover--lean4---v4.35.0/bin")
build = Path("/private/var/folders/1f/0218k3kx1zjgkp1n4km_3qhh0000gn/T/tmp.mgwDfFukaY")
env = os.environ.copy()
env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")
paths = subprocess.check_output([str(bin_dir / "lake"), "env", "printenv", "LEAN_PATH"],
    cwd=project, env=env, text=True).strip()
env["LEAN_PATH"] = paths + os.pathsep + str(build)
for module in sys.argv[1:]:
    p = subprocess.run([str(bin_dir / "lean"), "-R", str(here), "-o",
        str(build / "Snuffy" / f"{module}.olean"),
        str(here / "Snuffy" / f"{module}.lean")], cwd=here, env=env,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (bank / "checks" / f"{module}-development.txt").write_text(p.stdout)
    print(module, "exit", p.returncode, "output-bytes", len(p.stdout.encode()), flush=True)
    print(p.stdout, end="", flush=True)
