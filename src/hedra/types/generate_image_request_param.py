# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerateImageRequestParam"]


class GenerateImageRequestParam(TypedDict, total=False):
    ai_model_id: Required[str]
    """The model to use."""

    text_prompt: Required[str]
    """The text prompt for image generation or image editing."""

    aspect_ratio: Optional[str]
    """The aspect ratio to use."""

    resolution: Optional[str]
    """The resolution to use formatted like '540p', '1080p', '1440p (2K QHD)', etc."""

    start_keyframe_id: Optional[str]
    """The id of the Image asset to use as the start keyframe."""

    type: Literal["image"]
