"""
Hedra library extensions and utilities.
"""

# CLI is available as an optional import
try:
    from . import cli
    __all__ = ["cli"]
except ImportError:
    # CLI dependencies not installed
    __all__ = []