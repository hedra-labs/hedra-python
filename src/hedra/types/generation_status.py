# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["GenerationStatus"]

GenerationStatus: TypeAlias = Literal["complete", "error", "processing", "finalizing", "queued", "pending"]
