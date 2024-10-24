# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
import datetime as dt
from ..core.serialization import FieldMetadata
from .avatar_project_item_aspect_ratio import AvatarProjectItemAspectRatio
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AvatarProjectItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAt")] = None
    username: typing.Optional[str] = None
    video_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="videoUrl")] = None
    avatar_image_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="avatarImageUrl")] = None
    aspect_ratio: typing_extensions.Annotated[AvatarProjectItemAspectRatio, FieldMetadata(alias="aspectRatio")]
    text: typing.Optional[str] = None
    voice_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="voiceId")] = None
    voice_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="voiceUrl")] = None
    user_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userId")] = None
    job_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="jobType")] = None
    status: typing.Optional[str] = None
    stage: typing.Optional[str] = None
    progress: typing.Optional[float] = None
    error_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="errorMessage")] = None
    audio_source: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="audioSource")] = None
    avatar_image_input: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="avatarImageInput")
    ] = None
    shared: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
