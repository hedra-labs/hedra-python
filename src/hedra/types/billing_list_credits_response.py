# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BillingListCreditsResponse"]


class BillingListCreditsResponse(BaseModel):
    expiring: int
    """Credits that will expire in the future."""

    remaining: int
    """Remaining credits not yet used."""

    used: int
    """Credits used in the current billing period."""
