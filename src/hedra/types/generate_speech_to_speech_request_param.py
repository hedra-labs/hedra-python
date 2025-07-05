# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerateSpeechToSpeechRequestParam"]


class GenerateSpeechToSpeechRequestParam(TypedDict, total=False):
    ai_model_id: Required[str]
    """The id of the model to use for audio isolation."""

    audio_id: Required[str]
    """The id of the audio asset requiring sound isolation."""

    voice_id: Required[str]
    """The id of the Voice to use."""

    type: Literal["speech_to_speech"]
