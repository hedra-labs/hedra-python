"""
Character generation commands with face detection integration.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import click

from hedra.types.character_create_response import CharacterCreateResponse

from ..utils.output import ErrorHandler, ProgressTracker
# Face detection imports - lazy loaded to avoid TensorFlow overhead
from ..face import get_face_detector, get_face_selector


@click.group()
@click.pass_context
def characters(ctx: click.Context) -> None:
    """🎭 Character generation commands."""
    pass


@characters.command("create")
@click.option(
    "--text",
    help="Text to convert to speech (for TTS mode)",
)
@click.option(
    "--voice-id",
    help="Voice ID to use for TTS",
)
@click.option(
    "--voice-url", 
    help="URL of uploaded audio file (for audio mode)",
)
@click.option(
    "--avatar-image",
    help="URL of uploaded avatar image",
)
@click.option(
    "--avatar-image-file",
    type=click.Path(exists=True, path_type=Path),
    help="Local avatar image file (will be uploaded)",
)
@click.option(
    "--aspect-ratio",
    type=click.Choice(["1:1", "16:9", "9:16"]),
    default="16:9",
    help="Video aspect ratio",
)
@click.option(
    "--audio-source",
    type=click.Choice(["tts", "audio"]),
    default="tts",
    help="Audio source type",
)
@click.option(
    "--avatar-prompt",
    help="Text prompt for AI-generated avatar",
)
@click.option(
    "--avatar-seed",
    type=int,
    help="Seed for AI avatar generation",
)
# Advanced parameters
@click.option(
    "--resolution",
    type=click.Choice(["512", "768", "1024"]),
    help="Video resolution (advanced parameter)",
)
@click.option(
    "--ai-model-id",
    help="AI model ID for generation (advanced parameter)",
)
@click.option(
    "--animation-prompt",
    help="Animation style prompt (advanced parameter)",
)
@click.pass_context
def create_character(
    ctx: click.Context,
    text: str | None,
    voice_id: str | None,
    voice_url: str | None,
    avatar_image: str | None,
    avatar_image_file: Path | None,
    aspect_ratio: str,
    audio_source: str,
    avatar_prompt: str | None,
    avatar_seed: int | None,
    resolution: str | None,
    ai_model_id: str | None,
    animation_prompt: str | None,
) -> None:
    """Create a character video with various input options.
    
    Examples:
        # Text-to-speech with uploaded image
        hedra characters create --text "Hello world" --voice-id Alice --avatar-image-file face.jpg
        
        # Using uploaded audio and avatar URL
        hedra characters create --voice-url <audio_url> --avatar-image <image_url> --audio-source audio
        
        # AI-generated avatar with TTS
        hedra characters create --text "Hello" --voice-id Alice --avatar-prompt "young woman smiling"
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    progress = ProgressTracker(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        # Validate inputs based on audio source
        if audio_source == "tts":
            if not text:
                console.print("[red]❌ --text is required for TTS mode[/red]")
                return
            if not voice_id:
                console.print("[red]❌ --voice-id is required for TTS mode[/red]")
                return
        else:  # audio
            if not voice_url:
                console.print("[red]❌ --voice-url is required for audio mode[/red]")
                return
        
        # Handle avatar image
        avatar_image_url = avatar_image
        
        if avatar_image_file and not avatar_image_url:
            progress.show_info(f"Uploading avatar image: {avatar_image_file.name}")
            
            # Optional: Use face detection for multi-face images
            if avatar_image_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                face_recognizer = get_face_detector()
                if face_recognizer:
                    try:
                        faces = face_recognizer.detect_faces(str(avatar_image_file))
                        if len(faces) > 1:
                            console.print(f"[yellow]⚠️  {len(faces)} faces detected in image[/yellow]")
                            
                            if click.confirm("Would you like to select a specific face?"):
                                face_selector = get_face_selector()
                                if face_selector:
                                    selected_face_path = face_selector.select_face_interactive(
                                        str(avatar_image_file), faces
                                    )
                                    if selected_face_path:
                                        avatar_image_file = Path(selected_face_path)
                                        progress.show_info(f"Using selected face: {avatar_image_file.name}")
                            
                    except Exception as e:
                        progress.show_warning(f"Face detection failed: {e}")
                        progress.show_info("Continuing with original image...")
                else:
                    progress.show_info("Face detection not available - using original image")
            
            with console.status("[bold green]Uploading avatar image..."):
                portrait_response = hedra_ctx.client.portraits.create(
                    file=avatar_image_file,
                    aspect_ratio=aspect_ratio,
                )
                avatar_image_url = portrait_response.url
            
            progress.show_success("Avatar image uploaded!")
        
        # Prepare character creation parameters
        create_params: Dict[str, Any] = {
            "aspect_ratio": aspect_ratio,
            "audio_source": audio_source,
        }
        
        # Add audio parameters
        if audio_source == "tts":
            create_params["text"] = text
            create_params["voice_id"] = voice_id
        else:
            create_params["voice_url"] = voice_url
        
        # Add avatar parameters
        if avatar_image_url:
            create_params["avatar_image"] = avatar_image_url
        elif avatar_prompt:
            create_params["avatar_image_input"] = {
                "prompt": avatar_prompt,
            }
            if avatar_seed is not None:
                create_params["avatar_image_input"]["seed"] = avatar_seed
        else:
            console.print("[red]❌ Either --avatar-image, --avatar-image-file, or --avatar-prompt is required[/red]")
            return
        
        # Add advanced parameters via extra_body if provided
        extra_body = {}
        if resolution:
            extra_body["resolution"] = int(resolution)
        if ai_model_id:
            extra_body["ai_model_id"] = ai_model_id
        if animation_prompt:
            extra_body["animation_prompt"] = animation_prompt
        
        if extra_body:
            create_params["extra_body"] = extra_body
            progress.show_info(f"Using advanced parameters: {list(extra_body.keys())}")
        
        # Create character
        progress.show_info("Creating character video...")
        
        with console.status("[bold green]Submitting character creation..."):
            response: CharacterCreateResponse = hedra_ctx.client.characters.create(
                **create_params
            )
        
        progress.show_success("Character creation job submitted!")
        console.print(f"Job ID: [cyan]{response.job_id}[/cyan]")
        console.print()
        console.print("Use the following commands to track progress:")
        console.print(f"  [dim]hedra projects get {response.job_id}[/dim]")
        console.print(f"  [dim]hedra projects wait {response.job_id}[/dim]")
        console.print(f"  [dim]hedra projects download {response.job_id}[/dim]")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


@characters.command("quick")
@click.argument("image_file", type=click.Path(exists=True, path_type=Path))
@click.argument("text")
@click.option(
    "--voice",
    default="Alice",
    help="Voice name or ID (default: Alice)",
)
@click.option(
    "--aspect-ratio",
    type=click.Choice(["1:1", "16:9", "9:16"]),
    default="16:9",
    help="Video aspect ratio",
)
@click.option(
    "--auto-face-select",
    is_flag=True,
    help="Automatically select best face if multiple detected",
)
@click.pass_context
def quick_create(
    ctx: click.Context,
    image_file: Path,
    text: str,
    voice: str,
    aspect_ratio: str,
    auto_face_select: bool,
) -> None:
    """Quick character creation with image file and text.
    
    This is a streamlined command for the most common use case:
    creating a character from a local image file with text-to-speech.
    
    Examples:
        hedra characters quick face.jpg "Hello, how are you today?"
        hedra characters quick avatar.png "Welcome to my channel" --voice Brian
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    progress = ProgressTracker(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        progress.show_info(f"Quick character creation: {image_file.name}")
        
        # Resolve voice ID
        voice_id = voice
        if not voice.startswith(('Xb7hH8MSUJpSbSDYk0k2', 'nPczCjzI2devNBz1zQrb')):
            # Try to resolve voice name to ID
            with console.status("[bold green]Resolving voice..."):
                voices_response = hedra_ctx.client.voices.list()
                
            for v in voices_response.supported_voices:
                if v.name.lower() == voice.lower():
                    voice_id = v.voice_id
                    progress.show_info(f"Using voice: {v.name} ({voice_id})")
                    break
            else:
                console.print(f"[yellow]⚠️  Voice '{voice}' not found, using as ID[/yellow]")
        
        # Handle face detection for uploaded image
        upload_file = image_file
        
        if image_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            face_recognizer = get_face_detector()
            if face_recognizer:
                try:
                    faces = face_recognizer.detect_faces(str(image_file))
                    if len(faces) > 1:
                        progress.show_info(f"Detected {len(faces)} faces in image")
                        
                        if auto_face_select:
                            # Select face with highest confidence
                            best_face = max(faces, key=lambda f: f.get('confidence', 0))
                            face_selector = get_face_selector()
                            if face_selector:
                                selected_face_path = face_selector.extract_face(
                                    str(image_file), best_face
                                )
                                if selected_face_path:
                                    upload_file = Path(selected_face_path)
                                    progress.show_info(f"Auto-selected best face (confidence: {best_face.get('confidence', 0):.2f})")
                        else:
                            progress.show_warning("Multiple faces detected. Use --auto-face-select or run 'hedra characters create' for manual selection")
                            
                except Exception as e:
                    progress.show_warning(f"Face detection failed: {e}")
            elif auto_face_select:
                progress.show_warning("Face detection not available - ignoring --auto-face-select")
        
        # Upload avatar image
        with console.status("[bold green]Uploading avatar image..."):
            portrait_response = hedra_ctx.client.portraits.create(
                file=upload_file,
                aspect_ratio=aspect_ratio,
            )
        
        # Create character
        with console.status("[bold green]Creating character..."):
            response: CharacterCreateResponse = hedra_ctx.client.characters.create(
                aspect_ratio=aspect_ratio,
                audio_source="tts",
                avatar_image=portrait_response.url,
                text=text,
                voice_id=voice_id,
            )
        
        progress.show_success("Character created successfully!")
        console.print(f"Job ID: [cyan]{response.job_id}[/cyan]")
        console.print(f"Track with: [dim]hedra projects wait {response.job_id}[/dim]")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)