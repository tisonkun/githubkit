"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookReleasePrereleasedPropReleaseAllof1(GitHubModel):
    """WebhookReleasePrereleasedPropReleaseAllof1"""

    assets: Missing[
        List[Union[WebhookReleasePrereleasedPropReleaseAllof1PropAssetsItems, None]]
    ] = Field(default=UNSET)
    assets_url: Missing[str] = Field(default=UNSET)
    author: Missing[WebhookReleasePrereleasedPropReleaseAllof1PropAuthor] = Field(
        default=UNSET
    )
    body: Missing[Union[str, None]] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    draft: Missing[bool] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    name: Missing[Union[str, None]] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    prerelease: Literal[True] = Field(
        description="Whether the release is identified as a prerelease or a full release."
    )
    published_at: Missing[Union[str, None]] = Field(default=UNSET)
    tag_name: Missing[str] = Field(default=UNSET)
    tarball_url: Missing[Union[str, None]] = Field(default=UNSET)
    target_commitish: Missing[str] = Field(default=UNSET)
    upload_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    zipball_url: Missing[Union[str, None]] = Field(default=UNSET)


class WebhookReleasePrereleasedPropReleaseAllof1PropAssetsItems(GitHubModel):
    """WebhookReleasePrereleasedPropReleaseAllof1PropAssetsItems"""


class WebhookReleasePrereleasedPropReleaseAllof1PropAuthor(GitHubModel):
    """WebhookReleasePrereleasedPropReleaseAllof1PropAuthor"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookReleasePrereleasedPropReleaseAllof1)
model_rebuild(WebhookReleasePrereleasedPropReleaseAllof1PropAssetsItems)
model_rebuild(WebhookReleasePrereleasedPropReleaseAllof1PropAuthor)

__all__ = (
    "WebhookReleasePrereleasedPropReleaseAllof1",
    "WebhookReleasePrereleasedPropReleaseAllof1PropAssetsItems",
    "WebhookReleasePrereleasedPropReleaseAllof1PropAuthor",
)
