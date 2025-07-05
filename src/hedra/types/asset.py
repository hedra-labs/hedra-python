# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .asset_type import AssetType

__all__ = ["Asset"]


class Asset(BaseModel):
    id: str
    """The id of the asset."""

    asset: Asset
    """The asset itself."""

    created_at: datetime
    """Date the asset was created."""

    name: str
    """Name of the asset. Default to user-provided file name."""

    thumbnail_url: str
    """URL of the thumbnail image."""

    type: AssetType
    """The type of the asset."""

    description: Optional[str] = None
    """Optional description of the asset."""

    is_favorite: Optional[bool] = None
    """Whether the asset is favorited by the user."""


if PYDANTIC_V2:
    Asset.model_rebuild()
else:
    Asset.update_forward_refs()  # type: ignore
