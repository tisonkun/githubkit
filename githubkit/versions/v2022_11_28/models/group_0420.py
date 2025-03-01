"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookDiscussionCreatedPropDiscussionAllof1(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussionAllof1"""

    active_lock_reason: Missing[None] = Field(default=UNSET)
    answer_chosen_at: None = Field()
    answer_chosen_by: None = Field()
    answer_html_url: Union[str, None] = Field()
    author_association: Missing[str] = Field(default=UNSET)
    body: Missing[Union[str, None]] = Field(default=UNSET)
    category: Missing[WebhookDiscussionCreatedPropDiscussionAllof1PropCategory] = Field(
        default=UNSET
    )
    comments: Missing[int] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    locked: Literal[False] = Field()
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    reactions: Missing[WebhookDiscussionCreatedPropDiscussionAllof1PropReactions] = (
        Field(default=UNSET)
    )
    repository_url: Missing[str] = Field(default=UNSET)
    state: Literal["open", "converting", "transferring"] = Field()
    timeline_url: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    user: Missing[WebhookDiscussionCreatedPropDiscussionAllof1PropUser] = Field(
        default=UNSET
    )


class WebhookDiscussionCreatedPropDiscussionAllof1PropCategory(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussionAllof1PropCategory"""

    created_at: Missing[str] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    emoji: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    is_answerable: Missing[bool] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    repository_id: Missing[int] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)


class WebhookDiscussionCreatedPropDiscussionAllof1PropReactions(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussionAllof1PropReactions"""

    plus_one: Missing[int] = Field(default=UNSET, alias="+1")
    minus_one: Missing[int] = Field(default=UNSET, alias="-1")
    confused: Missing[int] = Field(default=UNSET)
    eyes: Missing[int] = Field(default=UNSET)
    heart: Missing[int] = Field(default=UNSET)
    hooray: Missing[int] = Field(default=UNSET)
    laugh: Missing[int] = Field(default=UNSET)
    rocket: Missing[int] = Field(default=UNSET)
    total_count: Missing[int] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookDiscussionCreatedPropDiscussionAllof1PropUser(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussionAllof1PropUser"""

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


model_rebuild(WebhookDiscussionCreatedPropDiscussionAllof1)
model_rebuild(WebhookDiscussionCreatedPropDiscussionAllof1PropCategory)
model_rebuild(WebhookDiscussionCreatedPropDiscussionAllof1PropReactions)
model_rebuild(WebhookDiscussionCreatedPropDiscussionAllof1PropUser)

__all__ = (
    "WebhookDiscussionCreatedPropDiscussionAllof1",
    "WebhookDiscussionCreatedPropDiscussionAllof1PropCategory",
    "WebhookDiscussionCreatedPropDiscussionAllof1PropReactions",
    "WebhookDiscussionCreatedPropDiscussionAllof1PropUser",
)
