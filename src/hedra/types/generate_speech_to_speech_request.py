# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GenerateSpeechToSpeechRequest"]


class GenerateSpeechToSpeechRequest(BaseModel):
    ai_model_id: str
    """The id of the model to use for audio isolation."""

    audio_id: str
    """The id of the audio asset requiring sound isolation."""

    voice_id: str
    """The id of the Voice to use."""

    type: Optional[Literal["speech_to_speech"]] = None
