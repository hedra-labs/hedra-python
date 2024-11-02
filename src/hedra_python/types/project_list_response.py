# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .avatar_project_item import AvatarProjectItem

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    projects: List[AvatarProjectItem]
