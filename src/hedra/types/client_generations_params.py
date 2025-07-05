# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .generated_video_inputs_param import GeneratedVideoInputsParam

__all__ = [
    "ClientGenerationsParams",
    "GenerateVideoRequestInput",
    "GenerateTextToSpeechRequest",
    "GenerateImageRequest",
    "GenerateIsolatedAudioRequest",
    "GenerateSpeechToSpeechRequest",
    "GenerateVoiceCloneRequest",
]


class GenerateVideoRequestInput(TypedDict, total=False):
    generated_video_inputs: Required[GeneratedVideoInputsParam]
    """Inputs for generating the video."""

    ai_model_id: str
    """ID of the model to use for the generation."""

    audio_id: Optional[str]
    """The id of the Audio asset to use."""

    start_keyframe_id: Optional[str]
    """The id of the Image asset to use as the start keyframe."""

    type: Literal["video"]


class GenerateTextToSpeechRequest(TypedDict, total=False):
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


class GenerateImageRequest(TypedDict, total=False):
    ai_model_id: Required[str]
    """The model to use."""

    text_prompt: Required[str]
    """The text prompt for image generation or image editing."""

    aspect_ratio: Optional[str]
    """The aspect ratio to use."""

    resolution: Optional[str]
    """The resolution to use formatted like '540p', '1080p', '1440p (2K QHD)', etc."""

    start_keyframe_id: Optional[str]
    """The id of the Image asset to use as the start keyframe."""

    type: Literal["image"]


class GenerateIsolatedAudioRequest(TypedDict, total=False):
    ai_model_id: Required[str]
    """The id of the model to use for audio isolation."""

    audio_id: Required[str]
    """The id of the audio asset requiring sound isolation."""

    type: Literal["audio_isolation"]


class GenerateSpeechToSpeechRequest(TypedDict, total=False):
    ai_model_id: Required[str]
    """The id of the model to use for audio isolation."""

    audio_id: Required[str]
    """The id of the audio asset requiring sound isolation."""

    voice_id: Required[str]
    """The id of the Voice to use."""

    type: Literal["speech_to_speech"]


class GenerateVoiceCloneRequest(TypedDict, total=False):
    audio_id: Required[str]
    """The id of the Audio asset to use as the basis for the clone."""

    name: Required[str]
    """The name of the new voice. Required by ElevenLabs to create a new voice."""

    type: Literal["voice_clone"]


ClientGenerationsParams: TypeAlias = Union[
    GenerateVideoRequestInput,
    GenerateTextToSpeechRequest,
    GenerateImageRequest,
    GenerateIsolatedAudioRequest,
    GenerateSpeechToSpeechRequest,
    GenerateVoiceCloneRequest,
]
