# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CharacterCreateParams", "AvatarImageInput"]


class CharacterCreateParams(TypedDict, total=False):
    aspect_ratio: Annotated[Literal["1:1", "16:9", "9:16"], PropertyInfo(alias="aspectRatio")]
    """URL of audio uploaded using the /v1/audio endpoint"""

    audio_source: Annotated[Literal["tts", "audio"], PropertyInfo(alias="audioSource")]
    """`tts` for text to speech or `audio`"""

    avatar_image: Annotated[Optional[str], PropertyInfo(alias="avatarImage")]
    """URL of image uploaded via /v1/portrait"""

    avatar_image_input: Annotated[Optional[AvatarImageInput], PropertyInfo(alias="avatarImageInput")]
    """Image metadata"""

    text: str
    """text to convert to audio. Ignored if audio_source is not tts"""

    voice_id: Annotated[Optional[str], PropertyInfo(alias="voiceId")]
    """Voice ID"""

    voice_url: Annotated[Optional[str], PropertyInfo(alias="voiceUrl")]
    """URL of audio uploaded using the /v1/audio endpoint"""


class AvatarImageInput(TypedDict, total=False):
    prompt: Required[str]

    seed: int
