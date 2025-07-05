# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GenerateImageRequest"]


class GenerateImageRequest(BaseModel):
    ai_model_id: str
    """The model to use."""

    text_prompt: str
    """The text prompt for image generation or image editing."""

    aspect_ratio: Optional[str] = None
    """The aspect ratio to use."""

    resolution: Optional[str] = None
    """The resolution to use formatted like '540p', '1080p', '1440p (2K QHD)', etc."""

    start_keyframe_id: Optional[str] = None
    """The id of the Image asset to use as the start keyframe."""

    type: Optional[Literal["image"]] = None
