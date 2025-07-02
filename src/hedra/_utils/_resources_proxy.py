from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `hedra.resources` module.

    This is used so that we can lazily import `hedra.resources` only when
    needed *and* so that users can just import `hedra` and reference `hedra.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("hedra.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
