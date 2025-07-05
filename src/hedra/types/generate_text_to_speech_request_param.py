# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerateTextToSpeechRequestParam"]


class GenerateTextToSpeechRequestParam(TypedDict, total=False):
    text: Required[str]
    """The text to convert to speech."""

    voice_id: Required[str]
    """The id of the Voice to use."""

    speed: float
    """
    Speed should be between 0.7 and 1.2, where 0.7 is the slowest and 1.2 is the
    fastest. This varies the speed of the generated speech.
    """

    stability: float
    """
    Stability should be between 0-1, where 0 is the most stable and 1 is the most
    unstable. This varies the consistency between your outputs.
    """

    type: Literal["text_to_speech"]
