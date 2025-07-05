# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .generated_video_inputs import GeneratedVideoInputs

__all__ = ["GeneratedVideo"]


class GeneratedVideo(BaseModel):
    audio: Optional["Asset"] = None
    """URL of the Audio asset used as the basis for the video."""

    duration_ms: int
    """Duration of the video."""

    generated_video_inputs: GeneratedVideoInputs
    """Inputs for generating the video."""

    height: int
    """Height of the image."""

    keyframe_start: Optional["Asset"] = None
    """URL of the Image asset used as the start keyframe."""

    preview_url: str
    """URL of the preview for animated thumbnails."""

    url: str
    """URL of the image."""

    width: int
    """Width of the image."""

    type: Optional[Literal["generated_video"]] = None


from .asset import Asset

if PYDANTIC_V2:
    GeneratedVideo.model_rebuild()
else:
    GeneratedVideo.update_forward_refs()  # type: ignore
