# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientListGenerationsParams", "PagingParams"]


class ClientListGenerationsParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    ids: Optional[str]

    paging_params: PagingParams

    type: Optional[
        Literal[
            "image",
            "audio",
            "video",
            "text_to_speech",
            "speech_to_speech",
            "voice_clone",
            "audio_isolation",
            "video_stitching",
            "agent_response",
        ]
    ]


class PagingParams(TypedDict, total=False):
    limit: int
    """Number of items returned in the page."""

    offset: int
    """Number of records skipped."""
