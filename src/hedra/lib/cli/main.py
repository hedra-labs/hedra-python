"""
Main CLI entry point with Click framework integration.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

import click
from rich.console import Console
from rich.traceback import install

from hedra import Hedra
from hedra._exceptions import HedraError, APIError, AuthenticationError
from hedra._utils._logs import setup_logging

from .commands import (
    audio,
    characters, 
    config,
    generate,
    portraits,
    projects,
    voices,
)
from .utils.config import CliConfig
from .utils.output import ErrorHandler

# Install rich traceback for better error display
install(show_locals=True)

console = Console()
error_handler = ErrorHandler(console)


class HedraContext:
    """Shared context for CLI commands."""
    
    def __init__(self):
        self.client: Hedra | None = None
        self.config: CliConfig | None = None
        self.console = console
        self.debug = False


@click.group(invoke_without_command=True)
@click.option(
    "--api-key",
    envvar="HEDRA_API_KEY",
    help="Hedra API key (or set HEDRA_API_KEY env var)",
)
@click.option(
    "--base-url",
    envvar="HEDRA_BASE_URL", 
    default="https://mercury.dev.dream-ai.com/api",
    help="API base URL (default: official API)",
)
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Enable debug logging",
)
@click.option(
    "--config-file",
    type=click.Path(exists=False, path_type=Path),
    default=Path.home() / ".hedra" / "config.json",
    help="Config file path",
)
@click.pass_context
def cli(
    ctx: click.Context,
    api_key: str | None,
    base_url: str,
    debug: bool,
    config_file: Path,
) -> None:
    """🎭 Hedra CLI - AI Video Generation Tool
    
    Official command-line interface for the Hedra API.
    Generate talking avatar videos from text or audio.
    
    Quick Start:
        hedra generate --text "Hello world" --voice-name Alice --img face.jpg
    
    Other Examples:
        hedra voices list --filter gender=female
        hedra projects list --status completed
    """
    # Initialize context
    hedra_ctx = HedraContext()
    hedra_ctx.debug = debug
    ctx.ensure_object(dict)
    ctx.obj = hedra_ctx
    
    # Setup logging
    if debug:
        os.environ["HEDRA_LOG"] = "debug"
        setup_logging()
    
    # Load configuration
    try:
        hedra_ctx.config = CliConfig.load(config_file)
        
        # Override with CLI args
        if api_key:
            hedra_ctx.config.api_key = api_key
        if base_url != "https://mercury.dev.dream-ai.com/api":
            hedra_ctx.config.base_url = base_url
            
    except Exception as e:
        if debug:
            error_handler.handle_exception(e)
        else:
            console.print(f"[red]Config error: {e}[/red]")
        sys.exit(1)
    
    # Initialize Hedra client
    try:
        if not hedra_ctx.config.api_key:
            if ctx.invoked_subcommand not in ["config"]:
                console.print("[red]Error: No API key provided[/red]")
                console.print("Set HEDRA_API_KEY environment variable or use --api-key option")
                console.print("Run 'hedra config set-api-key <key>' to save permanently")
                sys.exit(1)
        else:
            hedra_ctx.client = Hedra(
                api_key=hedra_ctx.config.api_key,
                base_url=hedra_ctx.config.base_url,
            )
            
    except Exception as e:
        error_handler.handle_hedra_error(e)
        sys.exit(1)
    
    # Show help if no command provided
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())


# Register command groups
cli.add_command(audio)
cli.add_command(characters)
cli.add_command(config)
cli.add_command(generate)
cli.add_command(portraits)
cli.add_command(projects)
cli.add_command(voices)


if __name__ == "__main__":
    cli()