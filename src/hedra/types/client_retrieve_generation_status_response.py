# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .asset_type import AssetType
from .generation_status import GenerationStatus

__all__ = ["ClientRetrieveGenerationStatusResponse"]


class ClientRetrieveGenerationStatusResponse(BaseModel):
    id: str
    """ID of the generation."""

    asset_id: str
    """ID of the generated asset."""

    created_at: datetime
    """Date the generation was submitted."""

    progress: float
    """Current progress to completion. Between 0-1"""

    status: GenerationStatus
    """Status of the generation."""

    type: AssetType
    """Type of generation."""

    error_message: Optional[str] = None
    """Error message.

    Value is not present unless the status of the generation is 'error'
    """

    url: Optional[str] = None
    """URL of the generated asset."""
