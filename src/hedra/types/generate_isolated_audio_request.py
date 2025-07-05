# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GenerateIsolatedAudioRequest"]


class GenerateIsolatedAudioRequest(BaseModel):
    ai_model_id: str
    """The id of the model to use for audio isolation."""

    audio_id: str
    """The id of the audio asset requiring sound isolation."""

    type: Optional[Literal["audio_isolation"]] = None
