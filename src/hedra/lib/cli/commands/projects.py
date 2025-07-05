"""
Project management commands.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Dict

import click
import httpx

from hedra.types.project_list_response import ProjectListResponse  
from hedra.types.avatar_project_item import AvatarProjectItem

from ..utils.output import ErrorHandler, TableFormatter, ProgressTracker


@click.group()
@click.pass_context
def projects(ctx: click.Context) -> None:
    """📁 Project management commands."""
    pass


@projects.command("list")
@click.option(
    "--status",
    type=click.Choice(["Completed", "Failed", "Processing"]),
    help="Filter by project status",
)
@click.option(
    "--limit",
    type=int,
    default=20,
    help="Maximum number of projects to show",
)
@click.pass_context
def list_projects(
    ctx: click.Context, 
    status: str | None, 
    limit: int
) -> None:
    """List all projects with optional filtering.
    
    Examples:
        hedra projects list
        hedra projects list --status Completed
        hedra projects list --limit 10
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        with console.status("[bold green]Fetching projects..."):
            response: ProjectListResponse = hedra_ctx.client.projects.list()
        
        projects_data = []
        for project in response.projects:
            if status and project.status != status:
                continue
                
            project_dict = {
                "id": project.id,
                "status": project.status,
                "created_at": project.created_at,
                "video_url": getattr(project, 'video_url', None),
            }
            projects_data.append(project_dict)
            
            if len(projects_data) >= limit:
                break
        
        if not projects_data:
            console.print("[yellow]No projects found[/yellow]")
            return
        
        # Display table
        table = TableFormatter.create_projects_table(projects_data)
        console.print(table)
        
        # Show summary
        total_shown = len(projects_data)
        console.print(f"\n[dim]Showing {total_shown} projects[/dim]")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


@projects.command("get")
@click.argument("project_id")
@click.pass_context
def get_project(ctx: click.Context, project_id: str) -> None:
    """Get detailed information about a specific project.
    
    Examples:
        hedra projects get abc123def456
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        with console.status(f"[bold green]Fetching project {project_id}..."):
            project: AvatarProjectItem = hedra_ctx.client.projects.retrieve(project_id)
        
        # Display detailed project info
        console.print(f"[bold blue]Project Details[/bold blue]")
        console.print(f"ID: [cyan]{project.id}[/cyan]")
        console.print(f"Status: [green]{project.status}[/green]")
        console.print(f"Created: [yellow]{project.created_at}[/yellow]")
        
        if hasattr(project, 'video_url') and project.video_url:
            console.print(f"Video URL: [green]{project.video_url}[/green]")
        else:
            console.print("Video URL: [dim]Not available[/dim]")
        
        # Show additional attributes if available
        if hasattr(project, 'error_message') and project.error_message:
            console.print(f"Error: [red]{project.error_message}[/red]")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


@projects.command("download")
@click.argument("project_id")
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Output file path (default: project_id.mp4)",
)
@click.pass_context
def download_project(
    ctx: click.Context, 
    project_id: str, 
    output: Path | None
) -> None:
    """Download the video from a completed project.
    
    Examples:
        hedra projects download abc123def456
        hedra projects download abc123def456 -o my_video.mp4
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    progress = ProgressTracker(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        # Get project details
        with console.status(f"[bold green]Getting project info..."):
            project: AvatarProjectItem = hedra_ctx.client.projects.retrieve(project_id)
        
        if project.status != "Completed":
            console.print(f"[yellow]⚠️  Project status is '{project.status}', not 'Completed'[/yellow]")
            if project.status == "Processing":
                console.print("Use 'hedra projects wait' to wait for completion")
            return
        
        if not hasattr(project, 'video_url') or not project.video_url:
            console.print("[red]❌ No video URL available for this project[/red]")
            return
        
        # Determine output path
        if not output:
            output = Path(f"{project_id}.mp4")
        
        # Ensure output directory exists
        output.parent.mkdir(parents=True, exist_ok=True)
        
        progress.show_info(f"Downloading video from: {project.video_url}")
        
        # Download the video
        with console.status(f"[bold green]Downloading to {output}..."):
            response = httpx.get(project.video_url, follow_redirects=True)
            response.raise_for_status()
            
            with open(output, 'wb') as f:
                f.write(response.content)
        
        progress.show_success(f"Video downloaded to: {output}")
        console.print(f"File size: {output.stat().st_size / 1024 / 1024:.1f}MB")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


@projects.command("delete")
@click.argument("project_id")
@click.option(
    "--yes", "-y",
    is_flag=True,
    help="Skip confirmation prompt",
)
@click.pass_context
def delete_project(ctx: click.Context, project_id: str, yes: bool) -> None:
    """Delete a project.
    
    Examples:
        hedra projects delete abc123def456
        hedra projects delete abc123def456 --yes
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    progress = ProgressTracker(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        if not yes:
            if not click.confirm(f"Delete project {project_id}?"):
                console.print("[yellow]Delete cancelled[/yellow]")
                return
        
        with console.status(f"[bold green]Deleting project..."):
            hedra_ctx.client.projects.delete(project_id)
        
        progress.show_success(f"Project {project_id} deleted successfully")
        
    except Exception as e:
        error_handler.handle_hedra_error(e)


@projects.command("wait")
@click.argument("project_id")
@click.option(
    "--timeout",
    type=int,
    default=300,
    help="Maximum wait time in seconds (default: 300)",
)
@click.option(
    "--interval", 
    type=int,
    default=10,
    help="Check interval in seconds (default: 10)",
)
@click.pass_context
def wait_for_project(
    ctx: click.Context, 
    project_id: str, 
    timeout: int, 
    interval: int
) -> None:
    """Wait for a project to complete processing.
    
    Examples:
        hedra projects wait abc123def456
        hedra projects wait abc123def456 --timeout 600 --interval 5
    """
    hedra_ctx = ctx.obj
    console = hedra_ctx.console
    error_handler = ErrorHandler(console)
    progress = ProgressTracker(console)
    
    if not hedra_ctx.client:
        console.print("[red]❌ No API client available[/red]")
        return
    
    try:
        start_time = time.time()
        
        progress.show_info(f"Waiting for project {project_id} to complete...")
        
        while True:
            elapsed = time.time() - start_time
            
            if elapsed > timeout:
                console.print(f"[yellow]⚠️  Timeout reached ({timeout}s)[/yellow]")
                break
            
            with console.status(f"[bold green]Checking status... ({elapsed:.0f}s)"):
                project: AvatarProjectItem = hedra_ctx.client.projects.retrieve(project_id)
            
            if project.status == "Completed":
                progress.show_success(f"Project completed in {elapsed:.0f}s!")
                if hasattr(project, 'video_url') and project.video_url:
                    console.print(f"Video URL: [green]{project.video_url}[/green]")
                break
                
            elif project.status == "Failed":
                console.print(f"[red]❌ Project failed[/red]")
                if hasattr(project, 'error_message') and project.error_message:
                    console.print(f"Error: {project.error_message}")
                break
                
            elif project.status == "Processing":
                console.print(f"[blue]⏳ Still processing... ({elapsed:.0f}s)[/blue]")
                time.sleep(interval)
                
            else:
                console.print(f"[yellow]Unknown status: {project.status}[/yellow]")
                break
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Wait cancelled by user[/yellow]")
    except Exception as e:
        error_handler.handle_hedra_error(e)