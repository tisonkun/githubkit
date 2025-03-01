"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0297 import ReleaseAsset
from .group_0033 import ReactionRollup


class Release(GitHubModel):
    """Release

    A release.
    """

    url: str = Field()
    html_url: str = Field()
    assets_url: str = Field()
    upload_url: str = Field()
    tarball_url: Union[str, None] = Field()
    zipball_url: Union[str, None] = Field()
    id: int = Field()
    node_id: str = Field()
    tag_name: str = Field(description="The name of the tag.")
    target_commitish: str = Field(
        description="Specifies the commitish value that determines where the Git tag is created from."
    )
    name: Union[str, None] = Field()
    body: Missing[Union[str, None]] = Field(default=UNSET)
    draft: bool = Field(
        description="true to create a draft (unpublished) release, false to create a published one."
    )
    prerelease: bool = Field(
        description="Whether to identify the release as a prerelease or a full release."
    )
    created_at: datetime = Field()
    published_at: Union[datetime, None] = Field()
    author: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    assets: List[ReleaseAsset] = Field()
    body_html: Missing[Union[str, None]] = Field(default=UNSET)
    body_text: Missing[Union[str, None]] = Field(default=UNSET)
    mentions_count: Missing[int] = Field(default=UNSET)
    discussion_url: Missing[str] = Field(
        default=UNSET, description="The URL of the release discussion."
    )
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")


model_rebuild(Release)

__all__ = ("Release",)
