# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["GeneratedVideoInputsParam"]


class GeneratedVideoInputsParam(TypedDict, total=False):
    text_prompt: Required[str]
    """Prompt for video generation."""

    aspect_ratio: Optional[str]
    """Aspect ratio for the video."""

    bounding_box_target: Optional[Iterable[object]]
    """Normalized coordinates for primary speaker position (Character3 only)"""

    duration_ms: Optional[int]
    """Duration of the video in milliseconds."""

    resolution: Optional[str]
    """Resolution for the video."""
