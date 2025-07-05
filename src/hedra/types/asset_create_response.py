# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .asset_type import AssetType

__all__ = ["AssetCreateResponse"]


class AssetCreateResponse(BaseModel):
    id: str
    """The id of the newly created asset. Should be used for upload."""

    name: str
    """Name of the asset. Default to user-provided file name."""

    type: AssetType
    """The type of the asset."""
