#!/usr/bin/env python3
"""
Hedra CLI - Official command-line interface for the Hedra API.

Usage:
    python -m hedra.lib.cli [COMMAND] [OPTIONS]
    hedra [COMMAND] [OPTIONS]  # When installed as package
"""

from __future__ import annotations

import sys
from typing import Any

from .main import cli


def main() -> Any:
    """Entry point for the CLI when run as a module."""
    return cli()


if __name__ == "__main__":
    sys.exit(main())