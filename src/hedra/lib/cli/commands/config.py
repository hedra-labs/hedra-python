"""
Configuration management commands.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import click
from rich.table import Table

from ..utils.config import CliConfig
from ..utils.output import ErrorHandler


@click.group()
@click.pass_context
def config(ctx: click.Context) -> None:
    """⚙️  Configuration management commands."""
    pass


@config.command("show")
@click.pass_context
def show_config(ctx: click.Context) -> None:
    """Show current configuration."""
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    
    if not hedra_ctx.config:
        console.print("[red]No configuration loaded[/red]")
        return
    
    # Create table for config display
    table = Table(title="Hedra CLI Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    config_dict = hedra_ctx.config.to_dict()
    
    # Mask API key for security
    if config_dict.get("api_key"):
        config_dict["api_key"] = f"{config_dict['api_key'][:8]}..."
    
    for key, value in config_dict.items():
        table.add_row(key, str(value))
    
    console.print(table)


@config.command("set-api-key")
@click.argument("api_key")
@click.option(
    "--config-file",
    type=click.Path(path_type=Path),
    default=Path.home() / ".hedra" / "config.json",
    help="Config file path",
)
@click.pass_context
def set_api_key(ctx: click.Context, api_key: str, config_file: Path) -> None:
    """Set the API key and save to config file."""
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    try:
        # Load or create config
        if hedra_ctx.config:
            config = hedra_ctx.config
        else:
            config = CliConfig.load(config_file)
        
        # Update API key
        config.api_key = api_key
        config.save(config_file)
        
        console.print("[green]✅ API key saved successfully[/green]")
        console.print(f"Config saved to: {config_file}")
        
    except Exception as e:
        error_handler.handle_exception(e)


@config.command("set")
@click.argument("key")
@click.argument("value")
@click.option(
    "--config-file",
    type=click.Path(path_type=Path),
    default=Path.home() / ".hedra" / "config.json",
    help="Config file path",
)
@click.pass_context
def set_config(ctx: click.Context, key: str, value: str, config_file: Path) -> None:
    """Set a configuration value."""
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    try:
        # Load or create config
        if hedra_ctx.config:
            config = hedra_ctx.config
        else:
            config = CliConfig.load(config_file)
        
        # Update configuration
        config.update(**{key: value})
        config.save(config_file)
        
        console.print(f"[green]✅ {key} = {value}[/green]")
        console.print(f"Config saved to: {config_file}")
        
    except ValueError as e:
        console.print(f"[red]❌ {e}[/red]")
    except Exception as e:
        error_handler.handle_exception(e)


@config.command("init")
@click.option(
    "--config-file",
    type=click.Path(path_type=Path),
    default=Path.home() / ".hedra" / "config.json",
    help="Config file path",
)
@click.pass_context
def init_config(ctx: click.Context, config_file: Path) -> None:
    """Initialize configuration with interactive setup."""
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    try:
        console.print("[bold blue]🎭 Hedra CLI Configuration Setup[/bold blue]")
        console.print()
        
        # Get API key
        api_key = click.prompt("Enter your Hedra API key", hide_input=True)
        
        # Get optional settings
        console.print("\n[dim]Optional settings (press Enter for defaults):[/dim]")
        
        base_url = click.prompt(
            "Base URL", 
            default="https://mercury.dev.dream-ai.com/api"
        )
        
        default_voice = click.prompt("Default voice", default="", show_default=False)
        if not default_voice:
            default_voice = None
            
        aspect_ratio = click.prompt("Default aspect ratio", default="16:9")
        
        output_dir = click.prompt(
            "Output directory", 
            default=str(Path.cwd() / "hedra_output")
        )
        
        # Create config
        config = CliConfig(
            api_key=api_key,
            base_url=base_url,
            default_voice=default_voice,
            default_aspect_ratio=aspect_ratio,
            output_directory=Path(output_dir),
        )
        
        config.save(config_file)
        
        console.print()
        console.print("[green]✅ Configuration saved successfully![/green]")
        console.print(f"Config file: {config_file}")
        console.print("\nYou can now use the Hedra CLI. Try: [cyan]hedra voices list[/cyan]")
        
    except click.Abort:
        console.print("\n[yellow]Setup cancelled[/yellow]")
    except Exception as e:
        error_handler.handle_exception(e)