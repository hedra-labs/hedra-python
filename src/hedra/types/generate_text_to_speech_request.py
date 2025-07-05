# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GenerateTextToSpeechRequest"]


class GenerateTextToSpeechRequest(BaseModel):
    text: str
    """The text to convert to speech."""

    voice_id: str
    """The id of the Voice to use."""

    speed: Optional[float] = None
    """
    Speed should be between 0.7 and 1.2, where 0.7 is the slowest and 1.2 is the
    fastest. This varies the speed of the generated speech.
    """

    stability: Optional[float] = None
    """
    Stability should be between 0-1, where 0 is the most stable and 1 is the most
    unstable. This varies the consistency between your outputs.
    """

    type: Optional[Literal["text_to_speech"]] = None
