"""
Portrait/image management commands.
"""

from __future__ import annotations

from pathlib import Path

import click

from hedra.types.portrait_create_response import PortraitCreateResponse

from ..utils.output import ErrorHandler, ProgressTracker


@click.group()
@click.pass_context
def portraits(ctx: click.Context) -> None:
    """🖼️  Portrait/image management commands."""
    pass


@portraits.command("upload")
@click.argument("file_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--aspect-ratio",
    type=click.Choice(["1:1", "16:9", "9:16"]),
    help="Aspect ratio for the portrait",
)
@click.pass_context
def upload_portrait(
    ctx: click.Context, 
    file_path: Path, 
    aspect_ratio: str | None
) -> None:
    """Upload an image file for use as avatar/portrait.
    
    Supported formats: JPG, PNG, and other common image formats.
    
    Args:
        file_path: Path to the image file to upload
        
    Examples:
        hedra portraits upload avatar.jpg
        hedra portraits upload face.png --aspect-ratio 1:1
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
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > 10 * 1024 * 1024:  # 10MB
            console.print(f"[yellow]⚠️  Large image file: {file_size / 1024 / 1024:.1f}MB[/yellow]")
        
        progress.show_info(f"Uploading portrait: {file_path.name}")
        
        # Prepare upload parameters
        upload_params = {"file": file_path}
        if aspect_ratio:
            upload_params["aspect_ratio"] = aspect_ratio
        
        with console.status("[bold green]Uploading portrait..."):
            response: PortraitCreateResponse = hedra_ctx.client.portraits.create(
                **upload_params
            )
        
        progress.show_success("Portrait uploaded successfully!")
        console.print(f"Image URL: [green]{response.url}[/green]")
        console.print(f"Use this URL in character generation commands")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)