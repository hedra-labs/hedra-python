# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GenerateVoiceCloneRequest"]


class GenerateVoiceCloneRequest(BaseModel):
    audio_id: str
    """The id of the Audio asset to use as the basis for the clone."""

    name: str
    """The name of the new voice. Required by ElevenLabs to create a new voice."""

    type: Optional[Literal["voice_clone"]] = None
