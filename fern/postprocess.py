#!/usr/bin/env python3
"""Post-generation fixups for the Fern-generated SDK.

Run after every `fern generate` (CI + local). Patches two upstream Fern codegen
issues in the *generated* files so the fixes survive regeneration. The patches are
located by content (not a hard-coded path) so they keep working regardless of the
output layout, and the script fails loudly if a target can't be found or if Fern's
surrounding code shifts — it never silently drops a fix.

Idempotent: running on already-patched code is a no-op.

Fixes:
  P1  the client — read HEDRA_API_KEY at construction time, not import time.
      Fern emits `api_key=os.getenv("HEDRA_API_KEY")` as a default argument,
      which is evaluated once at import, breaking `load_dotenv(); Hedra()`.
  P2  core http client — `retry-after-ms` header is a str; Fern compares it to
      int 0 (`retry_after_ms > 0`), raising a swallowed TypeError, so the header
      is ignored. Compare the parsed int instead.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "dist", "build", "tests", "__pycache__", "fern"}

# --- P1: API key read at construction time ---
P1_DEFAULT_OLD = 'api_key: typing.Optional[str] = os.getenv("HEDRA_API_KEY"),'
P1_DEFAULT_NEW = "api_key: typing.Optional[str] = None,"
P1_RAISE = (
    "        if api_key is None:\n"
    '            raise ApiError(body="The client must be instantiated be either passing in api_key'
    ' or setting HEDRA_API_KEY")'
)
P1_RUNTIME = "        if api_key is None:\n            api_key = os.getenv(\"HEDRA_API_KEY\")\n" + P1_RAISE

# --- P2: retry-after-ms parsing ---
P2_OLD = "return int(retry_after_ms) / 1000 if retry_after_ms > 0 else 0"
P2_NEW = "return int(retry_after_ms) / 1000 if int(retry_after_ms) > 0 else 0"


def py_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.py"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        out.append(p)
    return out


def main() -> int:
    files = py_files()
    p1_applied = p1_present = p2_applied = p2_present = 0

    for path in files:
        text = original = path.read_text()

        if P1_DEFAULT_OLD in text:
            p1_applied += text.count(P1_DEFAULT_OLD)
            text = text.replace(P1_DEFAULT_OLD, P1_DEFAULT_NEW).replace(P1_RAISE, P1_RUNTIME)
        p1_present += text.count(P1_RUNTIME)

        if P2_OLD in text:
            p2_applied += text.count(P2_OLD)
            text = text.replace(P2_OLD, P2_NEW)
        p2_present += text.count(P2_NEW)

        if text != original:
            path.write_text(text)
            print(f"patched {path.relative_to(ROOT)}")

    # Fail loudly if a fix has no home — means generation changed or produced an
    # unexpected layout, and we must not silently ship the unpatched bug.
    if p1_present < 2:
        print(f"ERROR: P1 (api_key construction-time read) not found — searched {len(files)} files; "
              f"applied={p1_applied}, present={p1_present}. Did the client move or change?", file=sys.stderr)
        return 1
    if p2_present < 1:
        print(f"ERROR: P2 (retry-after-ms) not found — searched {len(files)} files; "
              f"applied={p2_applied}, present={p2_present}. Did core/http_client.py change?", file=sys.stderr)
        return 1

    print(f"postprocess OK (P1 sites={p1_present}, P2 sites={p2_present})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
