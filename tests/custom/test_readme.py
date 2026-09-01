"""README.md may only reference things the shipped client actually has.

README.md is .fernignore'd, so a regeneration that renames a resource or a
method (queue/requests -> jobs, for one) leaves it behind silently -- and
pyproject.toml ships it as the PyPI long description, so the stale quickstart
is the first thing a new user sees. Every ``client.<resource>.<method>(`` call
and every ``from hedra... import ...`` line inside the README's python blocks
is checked against the installed package here.
"""

import importlib
import re
from pathlib import Path
from typing import List, Tuple

import pytest

from hedra import AsyncHedra, Hedra

README = Path(__file__).resolve().parents[2] / "README.md"

_PY_BLOCK = re.compile(r"```python\n(.*?)```", re.S)
_CALL = re.compile(r"\bclient\.([a-z_]+)\.(with_raw_response\.)?([a-z0-9_]+)\(")
_IMPORT = re.compile(r"^from (hedra(?:\.[\w.]+)?) import (.+)$", re.M)


def _python_blocks() -> str:
    return "\n".join(_PY_BLOCK.findall(README.read_text(encoding="utf-8")))


def _calls() -> List[Tuple[str, bool, str]]:
    return sorted({(resource, bool(raw), method) for resource, raw, method in _CALL.findall(_python_blocks())})


def _imports() -> List[Tuple[str, str]]:
    found = set()
    for module, names in _IMPORT.findall(_python_blocks()):
        for name in names.split(","):
            found.add((module, name.strip()))
    return sorted(found)


def test_readme_has_client_examples() -> None:
    # Guards the regexes themselves: an empty match set would pass vacuously.
    assert _calls(), "no client.<resource>.<method>( calls found in README python blocks"
    assert _imports(), "no `from hedra import ...` lines found in README python blocks"


@pytest.mark.parametrize(("resource", "raw", "method"), _calls())
def test_readme_call_exists_on_sync_and_async_client(resource: str, raw: bool, method: str) -> None:
    for client in (Hedra(api_key="k"), AsyncHedra(api_key="k")):
        target = getattr(client, resource)
        if raw:
            target = target.with_raw_response
        assert callable(getattr(target, method)), f"{type(client).__name__}.{resource}.{method} is missing"


@pytest.mark.parametrize(("module", "name"), _imports())
def test_readme_import_resolves(module: str, name: str) -> None:
    assert getattr(importlib.import_module(module), name) is not None
