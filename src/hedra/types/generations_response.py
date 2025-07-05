# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "GenerationsResponse",
    "GenerateVideoResponse",
    "GenerateVideoResponseGeneratedVideoInputs",
    "GenerateTextToSpeechResponse",
    "GenerateImageResponse",
    "GenerateImageToImageResponse",
    "GenerateIsolatedAudioResponse",
    "GenerateSpeechToSpeechResponse",
    "GenerateVoiceCloneResponse",
]


class GenerateVideoResponseGeneratedVideoInputs(BaseModel):
    text_prompt: str
    """Prompt for video generation."""

    aspect_ratio: Optional[str] = None
    """Aspect ratio for the video."""

    bounding_box_target: Optional[List[object]] = None
    """Normalized coordinates for primary speaker position (Character3 only)"""

    duration_ms: Optional[int] = None
    """Duration of the video in milliseconds."""

    resolution: Optional[str] = None
    """Resolution for the video."""


class GenerateVideoResponse(BaseModel):
    id: str
    """The id of the generation created."""

    asset_id: str
    """The id of the video asset resulting from the generation."""

    generated_video_inputs: GenerateVideoResponseGeneratedVideoInputs
    """Inputs for generating the video."""

    ai_model_id: Optional[str] = None
    """ID of the model to use for the generation."""

    audio_id: Optional[str] = None
    """The id of the Audio asset to use."""

    start_keyframe_id: Optional[str] = None
    """The id of the Image asset to use as the start keyframe."""

    type: Optional[Literal["video"]] = None


class GenerateTextToSpeechResponse(BaseModel):
    id: str
    """The id of the generation created."""

    asset_id: str
    """The id of the audio asset resulting from the generation."""

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


class GenerateImageResponse(BaseModel):
    id: str
    """The id of the generation. Can be used to check status."""

    ai_model_id: str
    """The model to use."""

    asset_id: str
    """The id of the resulting image asset."""

    text_prompt: str
    """The text prompt for image generation or image editing."""

    aspect_ratio: Optional[str] = None
    """The aspect ratio to use."""

    resolution: Optional[str] = None
    """The resolution to use formatted like '540p', '1080p', '1440p (2K QHD)', etc."""

    start_keyframe_id: Optional[str] = None
    """The id of the Image asset to use as the start keyframe."""

    type: Optional[Literal["image"]] = None


class GenerateImageToImageResponse(BaseModel):
    id: str
    """The id of the generation. Can be used to check status."""

    ai_model_id: str
    """The model to use."""

    aspect_ratio: str
    """The aspect ratio to use"""

    asset_id: str
    """The id of the resulting image asset."""

    image_ids: List[str]
    """The id(s) of the image(s) to reference in the generation."""

    resolution: str
    """The resolution to use"""

    text_prompt: str
    """The text prompt for image generation or image editing."""

    start_keyframe_id: Optional[str] = None
    """The id of the Image asset to use as the start keyframe."""

    type: Optional[Literal["image_to_image"]] = None


class GenerateIsolatedAudioResponse(BaseModel):
    id: str
    """The id of the generation created."""

    ai_model_id: str
    """The id of the model to use for audio isolation."""

    asset_id: str
    """The id of the isolated audio asset resulting from the generation."""

    audio_id: str
    """The id of the audio asset requiring sound isolation."""

    type: Optional[Literal["audio_isolation"]] = None


class GenerateSpeechToSpeechResponse(BaseModel):
    id: str
    """The id of the generation created."""

    ai_model_id: str
    """The id of the model to use for audio isolation."""

    asset_id: str
    """The id of the isolated audio asset resulting from the generation."""

    audio_id: str
    """The id of the audio asset requiring sound isolation."""

    voice_id: str
    """The id of the Voice to use."""

    type: Optional[Literal["speech_to_speech"]] = None


class GenerateVoiceCloneResponse(BaseModel):
    id: str
    """The id of the generation. Can be used to check status."""

    asset_id: str
    """The id of the resulting Voice asset."""

    audio_id: str
    """The id of the Audio asset to use as the basis for the clone."""

    name: str
    """The name of the new voice. Required by ElevenLabs to create a new voice."""

    type: Optional[Literal["voice_clone"]] = None


GenerationsResponse: TypeAlias = Annotated[
    Union[
        GenerateVideoResponse,
        GenerateTextToSpeechResponse,
        GenerateImageResponse,
        GenerateImageToImageResponse,
        GenerateIsolatedAudioResponse,
        GenerateSpeechToSpeechResponse,
        GenerateVoiceCloneResponse,
    ],
    PropertyInfo(discriminator="type"),
]
