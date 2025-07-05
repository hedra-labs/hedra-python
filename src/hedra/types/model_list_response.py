# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "ModelListResponse",
    "ModelListResponseItem",
    "ModelListResponseItemPriceDetails",
    "ModelListResponseItemDimensionsModelListResponseItemDimensionsItem",
]


class ModelListResponseItemPriceDetails(BaseModel):
    billing_unit: str
    """Billing unit of the model (e.g. 'generation', 'second', 'character')."""

    credit_cost: int
    """Credit cost of the model."""

    unit_scale: int
    """Unit scaling for the cost."""


class ModelListResponseItemDimensionsModelListResponseItemDimensionsItem(BaseModel):
    height: int
    """Height of the image."""

    width: int
    """Width of the image."""


class ModelListResponseItem(BaseModel):
    id: str
    """ID of the model"""

    description: Optional[str] = None
    """Description of the model."""

    name: str
    """Name of the model"""

    price_details: ModelListResponseItemPriceDetails
    """Pricing details of the model."""

    type: str
    """Type of generation the model applies to."""

    aspect_ratios: Optional[List[str]] = None
    """Aspect ratios the model supports."""

    custom_resolution: Optional[bool] = None
    """Whether the model supports custom resolution."""

    dimensions: Optional[Dict[str, Dict[str, ModelListResponseItemDimensionsModelListResponseItemDimensionsItem]]] = (
        None
    )
    """Width and height for each aspect_ratio and resolution tuple."""

    durations: Optional[List[str]] = None
    """Durations the model supports."""

    requires_audio_input: Optional[bool] = None
    """Whether the model is conditioned by audio input."""

    requires_start_frame: Optional[bool] = None
    """Whether the model is conditioned by a start frame."""

    resolutions: Optional[List[str]] = None
    """Resolutions the model supports."""


ModelListResponse: TypeAlias = List[ModelListResponseItem]
