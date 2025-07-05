# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerateVoiceCloneRequestParam"]


class GenerateVoiceCloneRequestParam(TypedDict, total=False):
    audio_id: Required[str]
    """The id of the Audio asset to use as the basis for the clone."""

    name: Required[str]
    """The name of the new voice. Required by ElevenLabs to create a new voice."""

    type: Literal["voice_clone"]
