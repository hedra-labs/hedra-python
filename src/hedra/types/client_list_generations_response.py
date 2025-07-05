# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .asset_type import AssetType
from .generation_status import GenerationStatus
from .generate_image_request import GenerateImageRequest
from .generated_video_inputs import GeneratedVideoInputs
from .generate_voice_clone_request import GenerateVoiceCloneRequest
from .generate_isolated_audio_request import GenerateIsolatedAudioRequest
from .generate_text_to_speech_request import GenerateTextToSpeechRequest
from .generate_speech_to_speech_request import GenerateSpeechToSpeechRequest

__all__ = ["ClientListGenerationsResponse", "Data", "DataInput", "DataInputGenerateVideoRequestOutput", "PageInfo"]


class DataInputGenerateVideoRequestOutput(BaseModel):
    generated_video_inputs: GeneratedVideoInputs
    """Inputs for generating the video."""

    ai_model_id: Optional[str] = None
    """ID of the model to use for the generation."""

    audio_id: Optional[str] = None
    """The id of the Audio asset to use."""

    start_keyframe_id: Optional[str] = None
    """The id of the Image asset to use as the start keyframe."""

    type: Optional[Literal["video"]] = None


DataInput: TypeAlias = Annotated[
    Union[
        DataInputGenerateVideoRequestOutput,
        GenerateTextToSpeechRequest,
        GenerateImageRequest,
        GenerateIsolatedAudioRequest,
        GenerateSpeechToSpeechRequest,
        GenerateVoiceCloneRequest,
    ],
    PropertyInfo(discriminator="type"),
]


class Data(BaseModel):
    id: str
    """ID of the generation and associated asset."""

    created_at: datetime
    """Date the generation was submitted."""

    input: DataInput
    """Inputs for the generation"""

    progress: float
    """Current progress to completion. Between 0-1"""

    status: GenerationStatus
    """Status of the generation"""

    type: AssetType
    """Type of generation."""

    asset: Optional["Asset"] = None
    """The generated asset.

    Value is not present unless the status of the generation is 'complete'
    """

    error_message: Optional[str] = None
    """Error message.

    Value is not present unless the status of the generation is 'error'
    """


class PageInfo(BaseModel):
    limit: int
    """Number of items returned in the page."""

    offset: int
    """Number of records skipped."""


class ClientListGenerationsResponse(BaseModel):
    data: List[Data]
    """Page data."""

    page_info: PageInfo
    """Paging information."""


from .asset import Asset

if PYDANTIC_V2:
    ClientListGenerationsResponse.model_rebuild()
    Data.model_rebuild()
    DataInputGenerateVideoRequestOutput.model_rebuild()
    PageInfo.model_rebuild()
else:
    ClientListGenerationsResponse.update_forward_refs()  # type: ignore
    Data.update_forward_refs()  # type: ignore
    DataInputGenerateVideoRequestOutput.update_forward_refs()  # type: ignore
    PageInfo.update_forward_refs()  # type: ignore
