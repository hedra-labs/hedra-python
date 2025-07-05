"""
Configuration management for Hedra CLI.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel, Field


class CliConfig(BaseModel):
    """CLI configuration model."""
    
    api_key: str | None = Field(default=None)
    base_url: str = Field(default="https://mercury.dev.dream-ai.com/api")
    default_voice: str | None = Field(default=None)
    default_aspect_ratio: str = Field(default="16:9")
    output_directory: Path = Field(default_factory=lambda: Path.cwd() / "hedra_output")
    face_detection_backend: str = Field(default="deepface")
    
    class Config:
        json_encoders = {
            Path: str
        }
    
    @classmethod
    def load(cls, config_path: Path) -> CliConfig:
        """Load configuration from file, creating defaults if needed."""
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    data = json.load(f)
                return cls(**data)
            except (json.JSONDecodeError, TypeError) as e:
                raise ValueError(f"Invalid config file {config_path}: {e}")
        
        # Create default config
        config = cls()
        
        # Try to load API key from environment
        api_key = os.environ.get("HEDRA_API_KEY")
        if api_key:
            config.api_key = api_key
            
        return config
    
    def save(self, config_path: Path) -> None:
        """Save configuration to file."""
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert to dict and handle Path objects
        data = self.dict()
        data["output_directory"] = str(data["output_directory"])
        
        with open(config_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def update(self, **kwargs: Any) -> None:
        """Update configuration values."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown config key: {key}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for display."""
        data = self.dict()
        data["output_directory"] = str(data["output_directory"])
        return data