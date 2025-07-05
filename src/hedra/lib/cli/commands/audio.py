"""
Audio management commands.
"""

from __future__ import annotations

from pathlib import Path

import click

from hedra.types.audio_create_response import AudioCreateResponse

from ..utils.output import ErrorHandler, ProgressTracker


@click.group()
@click.pass_context
def audio(ctx: click.Context) -> None:
    """🎵 Audio management commands."""
    pass


@audio.command("upload")
@click.argument("file_path", type=click.Path(exists=True, path_type=Path))
@click.pass_context
def upload_audio(ctx: click.Context, file_path: Path) -> None:
    """Upload an audio file for use in character generation.
    
    Supported formats: MP3, WAV, and other common audio formats.
    
    Args:
        file_path: Path to the audio file to upload
        
    Examples:
        hedra audio upload speech.mp3
        hedra audio upload /path/to/audio.wav
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    progress = ProgressTracker(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        # Validate file
        if not file_path.is_file():
            console.print(f"[red]❌ File not found: {file_path}[/red]")
            return
        
        # Check file size (reasonable limit)
        file_size = file_path.stat().st_size
        if file_size > 100 * 1024 * 1024:  # 100MB
            console.print(f"[yellow]⚠️  Large file detected: {file_size / 1024 / 1024:.1f}MB[/yellow]")
        
        progress.show_info(f"Uploading audio file: {file_path.name}")
        
        with console.status("[bold green]Uploading audio..."):
            response: AudioCreateResponse = hedra_ctx.client.audio.create(
                file=file_path
            )
        
        progress.show_success("Audio uploaded successfully!")
        console.print(f"Audio URL: [green]{response.url}[/green]")
        console.print(f"Use this URL in character generation commands")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)