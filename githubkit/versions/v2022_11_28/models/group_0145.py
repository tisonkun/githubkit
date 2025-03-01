"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class ProjectCard(GitHubModel):
    """Project Card

    Project cards represent a scope of work.
    """

    url: str = Field()
    id: int = Field(description="The project card's ID")
    node_id: str = Field()
    note: Union[str, None] = Field()
    creator: Union[None, SimpleUser] = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    archived: Missing[bool] = Field(
        default=UNSET, description="Whether or not the card is archived"
    )
    column_name: Missing[str] = Field(default=UNSET)
    project_id: Missing[str] = Field(default=UNSET)
    column_url: str = Field()
    content_url: Missing[str] = Field(default=UNSET)
    project_url: str = Field()


model_rebuild(ProjectCard)

__all__ = ("ProjectCard",)
