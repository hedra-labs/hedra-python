# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GeneratedVideoInputs"]


class GeneratedVideoInputs(BaseModel):
    text_prompt: str
    """Prompt for video generation."""

    aspect_ratio: Optional[str] = None
    """Aspect ratio for the video."""

    bounding_box_target: Optional[List[object]] = None
    """Normalized coordinates for primary speaker position (Character3 only)"""

    duration_ms: Optional[int] = None
    """Duration of the video in milliseconds."""

    resolution: Optional[str] = None
    """Resolution for the video."""
