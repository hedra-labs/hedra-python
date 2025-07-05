"""
Unified generate command for end-to-end character creation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Tuple

import click
from rich.table import Table

from hedra.types.character_create_response import CharacterCreateResponse

from ..utils.output import ErrorHandler, ProgressTracker
# Face detection imports - lazy loaded to avoid TensorFlow overhead
from ..face import get_face_detector, get_face_selector


@click.command()
@click.option(
    "--text",
    required=True,
    help="Text to convert to speech",
)
@click.option(
    "--voice-id",
    help="Voice ID to use for TTS (e.g., Xb7hH8MSUJpSbSDYk0k2 for Alice)",
)
@click.option(
    "--voice-name",
    help="Voice name to use for TTS (e.g., Alice, Brian)",
)
@click.option(
    "--img",
    "image_file", 
    type=click.Path(exists=True, path_type=Path),
    help="Source image file to animate (e.g., news-interview.png)",
)
@click.option(
    "--avatar-file",
    type=click.Path(exists=True, path_type=Path),
    help="Avatar/portrait reference image (will be cropped and saved to assets/)",
)
@click.option(
    "--avatar-image-url",
    help="URL of already uploaded avatar image",
)
@click.option(
    "--avatar-prompt",
    help="Text prompt for AI-generated avatar (alternative to --img)",
)
@click.option(
    "--avatar-seed",
    type=int,
    help="Seed for AI avatar generation (use with --avatar-prompt)",
)
@click.option(
    "--bounding-box",
    help="Face bounding box in source image as 'x,y,width,height' (normalized 0-1)",
)
@click.option(
    "--aspect-ratio",
    type=click.Choice(["1:1", "16:9", "9:16"]),
    default="16:9",
    help="Video aspect ratio",
)
@click.option(
    "--resolution",
    type=click.Choice(["512", "768", "1024", "720p", "1080p"]),
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
@click.option(
    "--auto-face-select",
    is_flag=True,
    help="Automatically select best face if multiple detected",
)
@click.option(
    "--wait/--no-wait",
    default=True,
    help="Wait for generation to complete",
)
@click.option(
    "--download/--no-download", 
    default=True,
    help="Download the video when complete",
)
@click.option(
    "--debug-payload",
    is_flag=True,
    help="Show detailed API payload information for debugging",
)
@click.option(
    "--visualize-bbox",
    is_flag=True,
    help="Create a visual overlay showing the bounding box on the image",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Output video file path (default: auto-generated)",
)
@click.pass_context
def generate(
    ctx: click.Context,
    text: str,
    voice_id: str | None,
    voice_name: str | None,
    image_file: Path | None,
    avatar_file: Path | None,
    avatar_image_url: str | None,
    avatar_prompt: str | None,
    avatar_seed: int | None,
    bounding_box: str | None,
    aspect_ratio: str,
    resolution: str | None,
    ai_model_id: str | None,
    animation_prompt: str | None,
    auto_face_select: bool,
    wait: bool,
    download: bool,
    output: Path | None,
    debug_payload: bool,
    visualize_bbox: bool,
) -> None:
    """🎬 Generate a character video with unified workflow.
    
    This command handles the complete workflow:
    1. Process avatar (crop, save to assets/, store embedding)
    2. Upload source image for animation with bounding box
    3. Resolve voice ID (if voice name provided)
    4. Create character with all parameters
    5. Wait for completion (optional)
    6. Download result (optional)
    
    Examples:
    
        # Correct workflow: separate avatar and source image
        hedra generate \\
          --text "Welcome to AI news" \\
          --voice-name "Alice" \\
          --img "news-interview.png" \\
          --avatar-file "anchor-headshot.jpg" \\
          --bounding-box "0.243,0.277" \\
          --aspect-ratio "16:9" \\
          --ai-model-id "d1dd37a3-e39a-4854-a298-6510289f9cf2" \\
          --animation-prompt "News anchor speaking confidently"
        
        # Legacy mode: use source image as avatar (backward compatibility)
        hedra generate \\
          --text "Hello world" \\
          --voice-name "Alice" \\
          --img "face.jpg"
          
        # AI-generated avatar with source image
        hedra generate \\
          --text "Hello from the future" \\
          --voice-name "Brian" \\
          --img "news-interview.png" \\
          --avatar-prompt "professional news anchor, confident expression" \\
          --bounding-box "0.243,0.277"
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    progress = ProgressTracker(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        console.print("Set HEDRA_API_KEY environment variable or use --api-key option")
        return
    
    try:
        progress.show_info("🎬 Starting unified character generation workflow")
        
        # Debug: Show bounding box visualization if requested
        if visualize_bbox and image_file and bounding_box:
            _visualize_bounding_box(image_file, bounding_box, console, progress)
        
        # Step 1: Validate inputs
        if not voice_id and not voice_name:
            console.print("[red]❌ Either --voice-id or --voice-name is required[/red]")
            return
            
        if not image_file and not avatar_file and not avatar_image_url and not avatar_prompt:
            console.print("[red]❌ One of --img, --avatar-file, --avatar-image-url, or --avatar-prompt is required[/red]")
            return
        
        # Step 2: Resolve voice ID if voice name provided
        resolved_voice_id = voice_id
        if voice_name and not voice_id:
            progress.show_info(f"🔍 Resolving voice name: {voice_name}")
            
            with console.status("[bold green]Fetching voices..."):
                voices_response = hedra_ctx.client.voices.list()
            
            for voice in voices_response.supported_voices:
                if voice.name.lower() == voice_name.lower():
                    resolved_voice_id = voice.voice_id
                    progress.show_info(f"✅ Found voice: {voice.name} ({resolved_voice_id})")
                    break
            else:
                console.print(f"[red]❌ Voice '{voice_name}' not found[/red]")
                console.print("Available voices:")
                for voice in voices_response.supported_voices[:10]:  # Show first 10
                    console.print(f"  - {voice.name}")
                return
        
        # Step 3: Handle avatar/portrait creation
        avatar_image_final_url = avatar_image_url
        
        if avatar_file and not avatar_image_final_url:
            progress.show_info(f"👤 Processing avatar file: {avatar_file.name}")
            
            # Process avatar: crop, save to assets/, store embedding
            avatar_image_final_url = _process_avatar_file(
                avatar_file, console, progress, hedra_ctx.client, aspect_ratio
            )
            
        elif image_file and not avatar_file and not avatar_image_final_url and not avatar_prompt:
            # Legacy mode: use source image as avatar (for backward compatibility)
            progress.show_info(f"📸 Using source image as avatar: {image_file.name}")
            
            upload_file = image_file
            
            # Handle face detection for multi-face images  
            if image_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                upload_file = _handle_face_detection(
                    image_file, auto_face_select, console, progress
                )
            
            # Upload the image
            progress.show_info(f"☁️  Uploading avatar image: {upload_file.name}")
            with console.status("[bold green]Uploading avatar image..."):
                portrait_response = hedra_ctx.client.portraits.create(
                    file=upload_file,
                    aspect_ratio=aspect_ratio,
                )
                avatar_image_final_url = portrait_response.url
            
            progress.show_success("Avatar image uploaded!")
            
            # Clean up temporary file if created
            if upload_file != image_file and upload_file.exists():
                upload_file.unlink()
        
        # Step 4: Prepare character creation parameters
        create_params: Dict[str, Any] = {
            "aspect_ratio": aspect_ratio,
            "audio_source": "tts", 
            "text": text,
            "voice_id": resolved_voice_id,
        }
        
        # Add avatar parameters
        if avatar_image_final_url:
            create_params["avatar_image"] = avatar_image_final_url
        elif avatar_prompt:
            create_params["avatar_image_input"] = {
                "prompt": avatar_prompt,
            }
            if avatar_seed is not None:
                create_params["avatar_image_input"]["seed"] = avatar_seed
        
        # Step 5: Handle source image and bounding box for animation
        if image_file and bounding_box:
            progress.show_info(f"🎯 Applying bounding box to source image: {image_file.name}")
            
            # Upload source image with bounding box for animation
            source_image_url = _upload_source_image_with_bbox(
                image_file, bounding_box, console, progress, hedra_ctx.client, aspect_ratio
            )
            
            # Use source image as the target for animation
            create_params["avatar_image"] = source_image_url
        
        # Add advanced parameters via extra_body using web app structure
        extra_body = {}
        generated_video_inputs = {}
        
        # Map resolution 
        final_resolution = None
        if resolution:
            if resolution in ["720p", "1080p"]:
                resolution_map = {"720p": "768", "1080p": "1024"}
                final_resolution = int(resolution_map[resolution])
            else:
                final_resolution = int(resolution)
        
        # Add bounding box in correct web app format
        if bounding_box:
            bbox_parts = bounding_box.split(',')
            if len(bbox_parts) >= 2:
                generated_video_inputs["bounding_box_target"] = [
                    float(bbox_parts[0]), float(bbox_parts[1])
                ]
                progress.show_info(f"🎯 Using bounding box target: {generated_video_inputs['bounding_box_target']}")
        
        # Add other video generation parameters
        if final_resolution:
            generated_video_inputs["resolution"] = final_resolution
        if animation_prompt:
            generated_video_inputs["text_prompt"] = animation_prompt
        if aspect_ratio:
            generated_video_inputs["aspect_ratio"] = aspect_ratio
        
        # Structure like web app: use nested generated_video_inputs
        if generated_video_inputs:
            extra_body["generated_video_inputs"] = generated_video_inputs
            
        if ai_model_id:
            extra_body["ai_model_id"] = ai_model_id
            # Web app also sets type
            extra_body["type"] = "video"
        
        if extra_body:
            create_params["extra_body"] = extra_body
            progress.show_info(f"🔧 Using advanced parameters: {list(extra_body.keys())}")
        
        # Debug: Show full payload if requested
        if debug_payload:
            _show_debug_payload(create_params, extra_body, bounding_box, console)
        
        # Step 5: Create character
        progress.show_info("🎭 Creating character video...")
        
        with console.status("[bold green]Submitting character creation..."):
            response: CharacterCreateResponse = hedra_ctx.client.characters.create(
                **create_params
            )
        
        job_id = response.job_id
        progress.show_success(f"Character creation job submitted!")
        console.print(f"Job ID: [cyan]{job_id}[/cyan]")
        
        # Step 6: Wait for completion (optional)
        if wait:
            progress.show_info("⏳ Waiting for generation to complete...")
            
            video_url = _wait_for_completion(
                hedra_ctx.client, job_id, console, progress
            )
            
            if not video_url:
                return  # Failed or timed out
            
            # Step 7: Download video (optional)
            if download:
                output_path = output or Path(f"{job_id}.mp4")
                _download_video(video_url, output_path, console, progress)
                
        else:
            console.print("\n[dim]Use these commands to track progress:[/dim]")
            console.print(f"  hedra projects get {job_id}")
            console.print(f"  hedra projects wait {job_id}")
            console.print(f"  hedra projects download {job_id}")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


def _apply_bounding_box_crop(
    image_file: Path, 
    bounding_box: str, 
    console, 
    progress
) -> Path:
    """Apply bounding box cropping to image."""
    try:
        import cv2
        import numpy as np
        
        # Parse bounding box "x,y,width,height" (normalized)
        bbox_parts = bounding_box.split(',')
        if len(bbox_parts) == 2:
            # Assume it's "x,y" center point, create square crop
            x_center, y_center = map(float, bbox_parts)
            crop_size = 0.3  # Default crop size
            x = max(0, x_center - crop_size/2)
            y = max(0, y_center - crop_size/2)
            w = min(crop_size, 1 - x)
            h = min(crop_size, 1 - y)
        elif len(bbox_parts) == 4:
            x, y, w, h = map(float, bbox_parts)
        else:
            raise ValueError("Bounding box must be 'x,y' or 'x,y,width,height'")
        
        progress.show_info(f"✂️  Applying bounding box crop: {x:.3f},{y:.3f},{w:.3f},{h:.3f}")
        
        # Load and crop image
        img = cv2.imread(str(image_file))
        if img is None:
            raise ValueError(f"Could not load image: {image_file}")
        
        height, width = img.shape[:2]
        
        # Convert normalized coordinates to pixels
        x_px = int(x * width)
        y_px = int(y * height)
        w_px = int(w * width)
        h_px = int(h * height)
        
        # Ensure bounds are valid
        x_px = max(0, x_px)
        y_px = max(0, y_px)
        w_px = min(w_px, width - x_px)
        h_px = min(h_px, height - y_px)
        
        # Crop image
        cropped = img[y_px:y_px+h_px, x_px:x_px+w_px]
        
        # Save cropped image
        output_path = image_file.parent / f"{image_file.stem}_cropped{image_file.suffix}"
        cv2.imwrite(str(output_path), cropped)
        
        progress.show_success(f"Image cropped and saved: {output_path.name}")
        return output_path
        
    except Exception as e:
        progress.show_warning(f"Bounding box crop failed: {e}")
        progress.show_info("Continuing with original image...")
        return image_file


def _handle_face_detection(
    image_file: Path,
    auto_face_select: bool,
    console,
    progress
) -> Path:
    """Handle face detection and selection."""
    face_recognizer = get_face_detector()
    if not face_recognizer:
        return image_file
    
    try:
        faces = face_recognizer.detect_faces(str(image_file))
        if len(faces) <= 1:
            return image_file
            
        progress.show_info(f"👥 Detected {len(faces)} faces in image")
        
        if auto_face_select:
            # Select face with highest confidence
            best_face = max(faces, key=lambda f: f.get('confidence', 0))
            face_selector = get_face_selector()
            if face_selector:
                selected_face_path = face_selector.extract_face(
                    str(image_file), best_face
                )
                if selected_face_path:
                    progress.show_info(f"🤖 Auto-selected best face (confidence: {best_face.get('confidence', 0):.2f})")
                    return Path(selected_face_path)
        else:
            progress.show_warning("Multiple faces detected. Use --auto-face-select for automatic selection")
            progress.show_info("Using original image with all faces")
            
    except Exception as e:
        progress.show_warning(f"Face detection failed: {e}")
    
    return image_file


def _wait_for_completion(client, job_id: str, console, progress, timeout: int = 300) -> str | None:
    """Wait for job completion and return video URL."""
    import time
    
    start_time = time.time()
    interval = 10
    
    while True:
        elapsed = time.time() - start_time
        
        if elapsed > timeout:
            console.print(f"[yellow]⚠️  Timeout reached ({timeout}s)[/yellow]")
            console.print(f"Use 'hedra projects wait {job_id}' to continue waiting")
            return None
        
        with console.status(f"[bold green]Checking status... ({elapsed:.0f}s)"):
            project = client.projects.retrieve(job_id)
        
        if project.status == "Completed":
            progress.show_success(f"Generation completed in {elapsed:.0f}s!")
            video_url = getattr(project, 'video_url', None)
            if video_url:
                console.print(f"Video URL: [green]{video_url}[/green]")
                return video_url
            else:
                console.print("[yellow]⚠️  No video URL available[/yellow]")
                return None
                
        elif project.status == "Failed":
            console.print(f"[red]❌ Generation failed[/red]")
            if hasattr(project, 'error_message') and project.error_message:
                console.print(f"Error: {project.error_message}")
            return None
            
        elif project.status in ["Processing", "Queued"]:
            status_emoji = "⏳" if project.status == "Processing" else "📋"
            console.print(f"[blue]{status_emoji} {project.status}... ({elapsed:.0f}s)[/blue]")
            time.sleep(interval)
            
        else:
            console.print(f"[yellow]Unknown status: {project.status}[/yellow]")
            console.print(f"Continuing to wait... Use Ctrl+C to stop")
            time.sleep(interval)


def _process_avatar_file(
    avatar_file: Path,
    console,
    progress, 
    client,
    aspect_ratio: str
) -> str:
    """Process avatar file: detect faces, crop, save to assets/, store embedding, upload."""
    try:
        # Ensure assets directory exists
        assets_dir = Path("assets")
        assets_dir.mkdir(exist_ok=True)
        
        progress.show_info(f"🔍 Analyzing avatar file for face detection")
        
        # Use face detection to find best face
        face_recognizer = get_face_detector()
        upload_file = avatar_file
        
        if face_recognizer and avatar_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            try:
                faces = face_recognizer.detect_faces(str(avatar_file))
                if faces:
                    # Get best face
                    best_face = max(faces, key=lambda f: f.get('confidence', 0))
                    
                    # Extract and save face to assets/
                    face_selector = get_face_selector()
                    if face_selector:
                        cropped_path = face_selector.extract_face(str(avatar_file), best_face)
                        if cropped_path:
                            # Move to assets directory
                            asset_filename = f"avatar_{avatar_file.stem}_cropped{avatar_file.suffix}"
                            asset_path = assets_dir / asset_filename
                            
                            import shutil
                            shutil.move(cropped_path, asset_path)
                            upload_file = asset_path
                            
                            progress.show_success(f"💾 Avatar saved to: {asset_path}")
                            
                            # TODO: Store embedding in face memory
                            # face_memory = get_face_memory() 
                            # if face_memory:
                            #     embedding = face_recognizer.create_embedding(str(asset_path))
                            #     face_memory.store_face(embedding, str(asset_path), {"type": "avatar"})
                            
            except Exception as e:
                progress.show_warning(f"Face processing failed: {e}")
                progress.show_info("Using original avatar file")
        
        # Upload the avatar file
        progress.show_info(f"☁️  Uploading avatar: {upload_file.name}")
        with console.status("[bold green]Uploading avatar..."):
            portrait_response = client.portraits.create(
                file=upload_file,
                aspect_ratio=aspect_ratio,
            )
        
        progress.show_success("Avatar uploaded and processed!")
        return portrait_response.url
        
    except Exception as e:
        progress.show_warning(f"Avatar processing failed: {e}")
        # Fallback: upload original file
        with console.status("[bold green]Uploading original avatar..."):
            portrait_response = client.portraits.create(
                file=avatar_file,
                aspect_ratio=aspect_ratio,
            )
        return portrait_response.url


def _upload_source_image_with_bbox(
    source_image: Path,
    bounding_box: str,
    console,
    progress,
    client,
    aspect_ratio: str
) -> str:
    """Upload source image for animation, with bounding box info preserved."""
    try:
        # For now, we'll upload the source image as-is
        # The bounding box will be handled by the API during animation
        progress.show_info(f"📤 Uploading source image for animation: {source_image.name}")
        progress.show_info(f"📍 Bounding box coordinates: {bounding_box}")
        
        with console.status("[bold green]Uploading source image..."):
            portrait_response = client.portraits.create(
                file=source_image,
                aspect_ratio=aspect_ratio,
            )
        
        progress.show_success("Source image uploaded for animation!")
        
        # NOTE: The bounding box coordinates should be passed to the character creation
        # as metadata or extra parameters - this depends on how Hedra API handles it
        
        return portrait_response.url
        
    except Exception as e:
        progress.show_warning(f"Source image upload failed: {e}")
        raise


def _visualize_bounding_box(
    image_file: Path,
    bounding_box: str,
    console,
    progress
) -> None:
    """Create a visual overlay showing the bounding box on the image."""
    try:
        import cv2
        import numpy as np
        
        progress.show_info(f"🎯 Creating bounding box visualization")
        
        # Parse bounding box
        bbox_parts = bounding_box.split(',')
        if len(bbox_parts) == 2:
            # Center point format: convert to bounding box
            x_center, y_center = map(float, bbox_parts)
            # Create a reasonable crop size around the center
            crop_size = 0.2
            x = max(0, x_center - crop_size/2)
            y = max(0, y_center - crop_size/2)
            w = min(crop_size, 1 - x)
            h = min(crop_size, 1 - y)
        elif len(bbox_parts) == 4:
            x, y, w, h = map(float, bbox_parts)
        else:
            progress.show_warning("Invalid bounding box format")
            return
        
        # Load image
        img = cv2.imread(str(image_file))
        if img is None:
            progress.show_warning(f"Could not load image: {image_file}")
            return
        
        height, width = img.shape[:2]
        
        # Convert normalized coordinates to pixels
        x_px = int(x * width)
        y_px = int(y * height)
        w_px = int(w * width)
        h_px = int(h * height)
        
        # Draw bounding box
        cv2.rectangle(img, (x_px, y_px), (x_px + w_px, y_px + h_px), (0, 255, 0), 3)
        
        # Add center point
        center_x = x_px + w_px // 2
        center_y = y_px + h_px // 2
        cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)
        
        # Add text overlay
        cv2.putText(img, f"BBox: {x:.3f},{y:.3f},{w:.3f},{h:.3f}", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(img, f"Center: {x_center:.3f},{y_center:.3f}" if len(bbox_parts) == 2 else f"Size: {w_px}x{h_px}px", 
                   (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Save visualization
        output_path = image_file.parent / f"{image_file.stem}_bbox_debug{image_file.suffix}"
        cv2.imwrite(str(output_path), img)
        
        progress.show_success(f"Bounding box visualization saved: {output_path}")
        
        # Show detailed info
        console.print("\n📊 [bold blue]Bounding Box Analysis:[/bold blue]")
        console.print(f"  📐 Normalized coordinates: x={x:.3f}, y={y:.3f}, w={w:.3f}, h={h:.3f}")
        console.print(f"  📏 Pixel coordinates: x={x_px}, y={y_px}, w={w_px}, h={h_px}")
        console.print(f"  🖼️  Image dimensions: {width}x{height}")
        console.print(f"  🎯 Center point: ({center_x}, {center_y})")
        console.print(f"  💾 Visualization: {output_path}")
        
    except Exception as e:
        progress.show_warning(f"Bounding box visualization failed: {e}")


def _show_debug_payload(
    create_params: Dict[str, Any],
    extra_body: Dict[str, Any],
    bounding_box: str | None,
    console
) -> None:
    """Show detailed debug information about the API payload."""
    console.print("\n🐛 [bold blue]DEBUG: API Payload Information[/bold blue]")
    console.print("=" * 60)
    
    # Show main parameters
    console.print("\n📋 [bold]Main Parameters:[/bold]")
    for key, value in create_params.items():
        if key != "extra_body":
            if isinstance(value, str) and len(value) > 50:
                display_value = f"{value[:47]}..."
            else:
                display_value = value
            console.print(f"  {key}: [green]{display_value}[/green]")
    
    # Show extra_body (advanced parameters)
    if extra_body:
        console.print("\n🔧 [bold]Advanced Parameters (extra_body):[/bold]")
        for key, value in extra_body.items():
            console.print(f"  {key}: [yellow]{value}[/yellow]")
        
        # Show actual extra_body structure being sent
        console.print("\n📄 [bold]Actual extra_body Structure:[/bold]")
        console.print(json.dumps(extra_body, indent=2))
    
    # Show bounding box info
    if bounding_box:
        console.print(f"\n🎯 [bold]Bounding Box:[/bold]")
        bbox_parts = bounding_box.split(',')
        if len(bbox_parts) == 2:
            console.print(f"  Format: Center point")
            console.print(f"  X Center: [cyan]{bbox_parts[0]}[/cyan]")
            console.print(f"  Y Center: [cyan]{bbox_parts[1]}[/cyan]")
        elif len(bbox_parts) == 4:
            console.print(f"  Format: Full bounding box")
            console.print(f"  X: [cyan]{bbox_parts[0]}[/cyan], Y: [cyan]{bbox_parts[1]}[/cyan]")
            console.print(f"  Width: [cyan]{bbox_parts[2]}[/cyan], Height: [cyan]{bbox_parts[3]}[/cyan]")
    
    console.print("\n" + "=" * 60)


def _download_video(video_url: str, output_path: Path, console, progress) -> None:
    """Download video from URL."""
    try:
        import httpx
        
        progress.show_info(f"⬇️  Downloading video to: {output_path}")
        
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with console.status(f"[bold green]Downloading..."):
            response = httpx.get(video_url, follow_redirects=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
        
        file_size = output_path.stat().st_size / 1024 / 1024
        progress.show_success(f"Video downloaded: {output_path} ({file_size:.1f}MB)")
        
    except Exception as e:
        progress.show_warning(f"Download failed: {e}")
        console.print(f"Manual download: [blue]{video_url}[/blue]")