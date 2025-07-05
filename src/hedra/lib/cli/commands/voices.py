"""
Voice management commands.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List

import click
from rich.table import Table

from hedra.types.voice_list_response import VoiceListResponse

from ..utils.output import ErrorHandler, TableFormatter


@click.group()
@click.pass_context  
def voices(ctx: click.Context) -> None:
    """🎤 Voice management commands."""
    pass


@voices.command("list")
@click.option(
    "--filter",
    "filters",
    multiple=True,
    help="Filter voices (e.g., gender=female, accent=british, premium=true)",
)
@click.option(
    "--format",
    "output_format", 
    type=click.Choice(["table", "json", "ids"]),
    default="table",
    help="Output format",
)
@click.option(
    "--premium/--no-premium",
    default=None,
    help="Filter by premium status",
)
@click.pass_context
def list_voices(
    ctx: click.Context,
    filters: tuple[str, ...],
    output_format: str,
    premium: bool | None,
) -> None:
    """List available voices with filtering options.
    
    Examples:
        hedra voices list --filter gender=female
        hedra voices list --filter accent=british --premium
        hedra voices list --format json
        hedra voices list --format ids
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        # Get voices from API
        with console.status("[bold green]Fetching voices..."):
            response: VoiceListResponse = hedra_ctx.client.voices.list()
        
        voices_data = []
        for voice in response.supported_voices:
            voice_dict = {
                "name": voice.name,
                "voice_id": voice.voice_id,
                "premium": voice.premium,
                "labels": voice.labels or {},
            }
            voices_data.append(voice_dict)
        
        # Apply filters
        filtered_voices = _filter_voices(voices_data, filters, premium)
        
        if not filtered_voices:
            console.print("[yellow]No voices found matching criteria[/yellow]")
            return
        
        # Output in requested format
        if output_format == "json":
            console.print(json.dumps(filtered_voices, indent=2))
            
        elif output_format == "ids":
            for voice in filtered_voices:
                console.print(voice["voice_id"])
                
        else:  # table format
            table = TableFormatter.create_voices_table(filtered_voices)
            console.print(table)
            
            # Show summary
            total_count = len(filtered_voices)
            premium_count = sum(1 for v in filtered_voices if v.get("premium"))
            console.print(f"\n[dim]Total: {total_count} voices ({premium_count} premium)[/dim]")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


@voices.command("preview")
@click.argument("voice_id")
@click.option(
    "--text",
    default="Hello, this is a voice preview.",
    help="Text to use for preview",
)
@click.pass_context
def preview_voice(ctx: click.Context, voice_id: str, text: str) -> None:
    """Preview a voice by generating a short audio sample.
    
    Note: This creates a character with the voice for preview purposes.
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        console.print(f"[blue]🎤 Generating voice preview for: {voice_id}[/blue]")
        
        with console.status("[bold green]Creating preview..."):
            response = hedra_ctx.client.characters.create(
                audio_source="tts",
                text=text,
                voice_id=voice_id,
                aspect_ratio="1:1",  # Small format for preview
            )
        
        console.print(f"[green]✅ Preview created![/green]")
        console.print(f"Job ID: {response.job_id}")
        console.print(f"Use 'hedra projects get {response.job_id}' to check status")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


@voices.command("info")
@click.argument("voice_id")
@click.pass_context
def voice_info(ctx: click.Context, voice_id: str) -> None:
    """Get detailed information about a specific voice."""
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        # Get voices and find the specific one
        with console.status("[bold green]Fetching voice info..."):
            response: VoiceListResponse = hedra_ctx.client.voices.list()
        
        voice = None
        for v in response.supported_voices:
            if v.voice_id == voice_id or v.name.lower() == voice_id.lower():
                voice = v
                break
        
        if not voice:
            console.print(f"[red]❌ Voice not found: {voice_id}[/red]")
            return
        
        # Display detailed info
        table = Table(title=f"Voice Details: {voice.name}")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Name", voice.name)
        table.add_row("Voice ID", voice.voice_id)
        table.add_row("Premium", "Yes" if voice.premium else "No")
        
        if voice.labels:
            for key, value in voice.labels.items():
                table.add_row(key.title(), str(value))
        
        console.print(table)
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


def _filter_voices(
    voices: List[Dict[str, Any]], 
    filters: tuple[str, ...], 
    premium: bool | None
) -> List[Dict[str, Any]]:
    """Filter voices based on criteria."""
    filtered = voices.copy()
    
    # Apply premium filter
    if premium is not None:
        filtered = [v for v in filtered if v.get("premium", False) == premium]
    
    # Apply custom filters
    for filter_str in filters:
        if "=" not in filter_str:
            continue
            
        key, value = filter_str.split("=", 1)
        key = key.strip().lower()
        value = value.strip().lower()
        
        if key == "premium":
            filter_premium = value in ("true", "1", "yes")
            filtered = [v for v in filtered if v.get("premium", False) == filter_premium]
            
        elif key in ["name", "voice_id"]:
            filtered = [v for v in filtered if value in v.get(key, "").lower()]
            
        else:
            # Check in labels
            filtered = [
                v for v in filtered 
                if v.get("labels", {}).get(key, "").lower() == value
            ]
    
    return filtered