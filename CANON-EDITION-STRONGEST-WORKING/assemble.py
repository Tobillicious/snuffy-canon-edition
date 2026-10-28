#!/usr/bin/env python3
"""Assemble the compiled master: the 4.2 spine byte for byte, then the recovered parts.

Checks that the spine copy matches the archived 4.2 master hash, writes
SNUFFY-UPT-STRONGEST-MASTER.md, and prints the hashes of every input and the output.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPINE = os.path.join(HERE, "SPINE-4.2-MASTER.md")
PARTS = ["PARTS-V-VIII.md", "PARTS-IX-XII.md"]
OUT = os.path.join(HERE, "SNUFFY-UPT-STRONGEST-MASTER.md")
SPINE_SHA = "83b62bd9ece8d35ba6ab221c6edd286b753f4a4093c8e322eb1f836cd8e6f933"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    spine = open(SPINE, "rb").read()
    if sha(spine) != SPINE_SHA:
        sys.exit(f"spine hash mismatch: {sha(spine)}")
    body = spine
    print(f"spine  {sha(spine)}  {len(spine)} bytes")
    for p in PARTS:
        data = open(os.path.join(HERE, p), "rb").read()
        print(f"{p:<14} {sha(data)}  {len(data)} bytes")
        body += data
    open(OUT, "wb").write(body)
    assert body.startswith(spine)
    print(f"master {sha(body)}  {len(body)} bytes; spine is a byte-identical prefix")


if __name__ == "__main__":
    main()
