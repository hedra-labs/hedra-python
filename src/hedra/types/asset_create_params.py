# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .asset_type import AssetType

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the asset. Default to user-provided file name."""

    type: Required[AssetType]
    """The type of the asset."""
