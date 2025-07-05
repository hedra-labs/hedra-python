# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerateIsolatedAudioRequestParam"]


class GenerateIsolatedAudioRequestParam(TypedDict, total=False):
    ai_model_id: Required[str]
    """The id of the model to use for audio isolation."""

    audio_id: Required[str]
    """The id of the audio asset requiring sound isolation."""

    type: Literal["audio_isolation"]
