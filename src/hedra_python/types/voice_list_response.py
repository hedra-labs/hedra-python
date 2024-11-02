# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceListResponse", "SupportedVoice"]


class SupportedVoice(BaseModel):
    service: Literal["eleven", "cartesia"]

    voice_id: str

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    labels: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    premium: Optional[bool] = None

    preview_url: Optional[str] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None


class VoiceListResponse(BaseModel):
    supported_voices: List[SupportedVoice]
