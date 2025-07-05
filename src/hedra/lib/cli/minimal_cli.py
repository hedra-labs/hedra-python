#!/usr/bin/env python3
"""
Minimal Hedra CLI for testing basic functionality.
"""

import click
from rich.console import Console

from hedra import Hedra

console = Console()

@click.command()
@click.option("--api-key", envvar="HEDRA_API_KEY", help="Hedra API key")
def voices_list(api_key):
    """List available voices."""
    if not api_key:
        console.print("[red]❌ No API key provided[/red]")
        return
    
    try:
        client = Hedra(api_key=api_key)
        response = client.voices.list()
        
        console.print("[bold blue]Available Voices:[/bold blue]")
        for voice in response.supported_voices:
            premium = "[red](Premium)[/red]" if voice.premium else ""
            console.print(f"• {voice.name} {premium}: [green]{voice.voice_id}[/green]")
            
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")

if __name__ == "__main__":
    voices_list()