# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AvatarProjectItem"]


class AvatarProjectItem(BaseModel):
    aspect_ratio: Literal["1:1", "16:9", "9:16"] = FieldInfo(alias="aspectRatio")

    id: Optional[str] = None

    audio_source: Optional[str] = FieldInfo(alias="audioSource", default=None)

    avatar_image_input: Optional[object] = FieldInfo(alias="avatarImageInput", default=None)

    avatar_image_url: Optional[str] = FieldInfo(alias="avatarImageUrl", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    job_type: Optional[str] = FieldInfo(alias="jobType", default=None)

    progress: Optional[float] = None

    shared: Optional[bool] = None

    stage: Optional[str] = None

    status: Optional[str] = None

    text: Optional[str] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    username: Optional[str] = None

    video_url: Optional[str] = FieldInfo(alias="videoUrl", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_url: Optional[str] = FieldInfo(alias="voiceUrl", default=None)
