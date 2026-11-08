#!/usr/bin/env python
"""
build.py -- one-command rebuild of the whole manroland knowledge base.

    python build.py                # everything except images
    python build.py --with-images  # also re-render all 1,351 sheets
    python build.py --only +EA     # one document

Stages (each resumable):
    1. extract.py   PDFs        -> data/raw/*.json
    2. tables.py    tables      -> data/derived/tables/*.json
    3. graph.py     graph       -> data/derived/graph.json
    4. mdgen.py     markdown    -> md/02_SHEETS, md/03_INDEX
    5. export.py    RAG exports -> data/exports/*.jsonl
    6. render.py    images      -> images/<doc>/*.png        (optional)
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable


def run(script, extra=()):
    cmd = [PY, os.path.join(HERE, script)] + list(extra)
    print("\n" + "=" * 70)
    print(">>> %s" % " ".join([script] + list(extra)))
    print("=" * 70, flush=True)
    t0 = time.time()
    r = subprocess.run(cmd, cwd=HERE)
    dt = time.time() - t0
    status = "ok" if r.returncode == 0 else "FAILED (exit %d)" % r.returncode
    print("<<< %s in %.1fs — %s" % (script, dt, status), flush=True)
    if r.returncode != 0:
        raise SystemExit("stage failed: %s" % script)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--with-images", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    only = ["--only", args.only] if args.only else []
    force = ["--force"] if args.force else []

    t0 = time.time()
    run("extract.py", only + force)
    run("tables.py", only)
    run("graph.py")
    run("mdgen.py", only)
    if not args.only:
        run("export.py")
        # Keep the measured numbers quoted in the hand-written system docs in
        # step with the data. Runs last so it reads the final graph.
        run("sync_docs.py")
    if args.with_images:
        run("render.py", only + force)

    print("\n" + "=" * 70)
    print("BUILD COMPLETE in %.1fs" % (time.time() - t0))
    print("Knowledge base: %s" % os.path.dirname(HERE))
    print("Start reading:  md/00_READ_ME_FIRST.md")
    print("=" * 70)


if __name__ == "__main__":
    main()
