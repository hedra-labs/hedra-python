"""
Output formatting and error handling utilities.
"""

from __future__ import annotations

import sys
import traceback
from typing import Any, Dict, List

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax

from hedra._exceptions import (
    HedraError,
    APIError, 
    AuthenticationError,
    PermissionDeniedError,
    NotFoundError,
    RateLimitError,
)


class ErrorHandler:
    """Centralized error handling for CLI."""
    
    def __init__(self, console: Console):
        self.console = console
    
    def handle_hedra_error(self, error: Exception) -> None:
        """Handle Hedra-specific errors with appropriate messaging."""
        if isinstance(error, AuthenticationError):
            self.console.print("[red]❌ Authentication Error[/red]")
            self.console.print("Invalid API key. Check your HEDRA_API_KEY environment variable.")
            self.console.print("Run 'hedra config set-api-key <key>' to update your API key.")
            
        elif isinstance(error, PermissionDeniedError):
            self.console.print("[red]❌ Permission Denied[/red]")
            self.console.print("Your API key doesn't have permission for this operation.")
            
        elif isinstance(error, NotFoundError):
            self.console.print("[red]❌ Not Found[/red]")
            self.console.print("The requested resource was not found.")
            
        elif isinstance(error, RateLimitError):
            self.console.print("[red]❌ Rate Limit Exceeded[/red]")
            self.console.print("Too many requests. Please wait and try again.")
            
        elif isinstance(error, APIError):
            self.console.print(f"[red]❌ API Error ({error.status_code})[/red]")
            self.console.print(f"Message: {error.message}")
            if hasattr(error, 'response') and error.response:
                self.console.print(f"Response: {error.response.text}")
                
        elif isinstance(error, HedraError):
            self.console.print("[red]❌ Hedra Error[/red]")
            self.console.print(str(error))
            
        else:
            self.handle_exception(error)
    
    def handle_exception(self, error: Exception) -> None:
        """Handle general exceptions with full traceback."""
        self.console.print("[red]❌ Unexpected Error[/red]")
        self.console.print(f"[red]{type(error).__name__}: {error}[/red]")
        
        # Show traceback in debug mode
        if hasattr(sys, '_getframe'):
            self.console.print("\n[dim]Traceback:[/dim]")
            tb = traceback.format_exc()
            syntax = Syntax(tb, "python", theme="monokai", line_numbers=True)
            self.console.print(syntax)


class TableFormatter:
    """Utilities for formatting data as tables."""
    
    @staticmethod
    def create_voices_table(voices: List[Dict[str, Any]], show_premium: bool = True) -> Table:
        """Create a formatted table for voices."""
        table = Table(title="Available Voices")
        
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Voice ID", style="green")
        table.add_column("Gender", style="blue")
        table.add_column("Accent", style="yellow")
        table.add_column("Age", style="magenta")
        
        if show_premium:
            table.add_column("Premium", style="red")
        
        for voice in voices:
            labels = voice.get("labels", {})
            row = [
                voice.get("name", "Unknown"),
                voice.get("voice_id", "Unknown"),
                labels.get("gender", "Unknown"),
                labels.get("accent", "Unknown"),
                labels.get("age", "Unknown"),
            ]
            
            if show_premium:
                premium_status = "✓" if voice.get("premium", False) else ""
                row.append(premium_status)
                
            table.add_row(*row)
        
        return table
    
    @staticmethod  
    def create_projects_table(projects: List[Dict[str, Any]]) -> Table:
        """Create a formatted table for projects."""
        table = Table(title="Projects")
        
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Status", style="green")
        table.add_column("Created", style="blue")
        table.add_column("Video URL", style="yellow", max_width=50)
        
        for project in projects:
            table.add_row(
                project.get("id", "Unknown"),
                project.get("status", "Unknown"),
                project.get("created_at", "Unknown"),
                project.get("video_url", "N/A") or "N/A",
            )
            
        return table


class ProgressTracker:
    """Progress tracking utilities."""
    
    def __init__(self, console: Console):
        self.console = console
    
    def create_spinner(self, text: str) -> Progress:
        """Create a spinner for long-running operations."""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
        )
    
    def show_success(self, message: str) -> None:
        """Show success message."""
        self.console.print(f"[green]✅ {message}[/green]")
    
    def show_warning(self, message: str) -> None:
        """Show warning message."""
        self.console.print(f"[yellow]⚠️  {message}[/yellow]")
    
    def show_info(self, message: str) -> None:
        """Show info message."""
        self.console.print(f"[blue]ℹ️  {message}[/blue]")
    
    def show_panel(self, content: str, title: str, style: str = "blue") -> None:
        """Show content in a panel."""
        panel = Panel(content, title=title, border_style=style)
        self.console.print(panel)