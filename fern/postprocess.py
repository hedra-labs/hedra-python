#!/usr/bin/env python3
"""Post-generation fixups for the Fern-generated SDK.

Run after every `fern generate` (CI + local). Patches two upstream Fern codegen
issues in the *generated* files so the fixes survive regeneration. Each patch
asserts it actually applied, so if a future generator version changes the
surrounding code this script fails loudly instead of silently dropping the fix.

Idempotent: running on already-patched code is a no-op.

Fixes:
  P1  client.py — read HEDRA_API_KEY at construction time, not import time.
      Fern emits `api_key=os.getenv("HEDRA_API_KEY")` as a default argument,
      which is evaluated once at import, breaking `load_dotenv(); Hedra()`.
  P2  core/http_client.py — `retry-after-ms` header is a str; Fern compares it
      to int 0 (`retry_after_ms > 0`), raising TypeError that is swallowed, so
      the header is ignored. Compare the parsed int instead.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def patch_api_key_env(text: str) -> str:
    default_old = 'api_key: typing.Optional[str] = os.getenv("HEDRA_API_KEY"),'
    default_new = "api_key: typing.Optional[str] = None,"
    raise_block = (
        "        if api_key is None:\n"
        '            raise ApiError(body="The client must be instantiated be either passing in api_key'
        ' or setting HEDRA_API_KEY")'
    )
    runtime_read = (
        "        if api_key is None:\n"
        '            api_key = os.getenv("HEDRA_API_KEY")\n' + raise_block
    )

    if default_old in text:
        n = text.count(default_old)
        assert n == 2, f"P1: expected 2 api_key defaults, found {n}"
        text = text.replace(default_old, default_new)
        assert text.count(raise_block) == 2, "P1: expected 2 api_key None-checks"
        text = text.replace(raise_block, runtime_read)
    else:
        # Already patched: verify the fixed shape is present.
        assert text.count(runtime_read) == 2, "P1: code shape changed; update postprocess.py"
    return text


def patch_retry_after_ms(text: str) -> str:
    old = "return int(retry_after_ms) / 1000 if retry_after_ms > 0 else 0"
    new = "return int(retry_after_ms) / 1000 if int(retry_after_ms) > 0 else 0"
    if old in text:
        text = text.replace(old, new, 1)
    else:
        assert new in text, "P2: retry-after-ms code shape changed; update postprocess.py"
    return text


def apply(rel_path: str, fn) -> bool:
    path = ROOT / rel_path
    original = path.read_text()
    patched = fn(original)
    if patched != original:
        path.write_text(patched)
        print(f"patched {rel_path}")
        return True
    print(f"{rel_path} already up to date")
    return False


def main() -> int:
    apply("src/hedra/client.py", patch_api_key_env)
    apply("src/hedra/core/http_client.py", patch_retry_after_ms)
    return 0


if __name__ == "__main__":
    sys.exit(main())
