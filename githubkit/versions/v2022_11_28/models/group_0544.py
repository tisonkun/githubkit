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

from .group_0550 import WebhookIssuesUnlockedPropIssueMergedMilestone
from .group_0548 import WebhookIssuesUnlockedPropIssueAllof0PropPullRequest


class WebhookIssuesUnlockedPropIssue(GitHubModel):
    """WebhookIssuesUnlockedPropIssue"""

    active_lock_reason: Union[None, None] = Field()
    assignee: Missing[Union[WebhookIssuesUnlockedPropIssueMergedAssignee, None]] = (
        Field(default=UNSET)
    )
    assignees: List[WebhookIssuesUnlockedPropIssueMergedAssignees] = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: Union[Union[str, None], None] = Field(description="Contents of the issue")
    closed_at: Union[datetime, None] = Field()
    comments: int = Field()
    comments_url: str = Field()
    created_at: datetime = Field()
    draft: Missing[bool] = Field(default=UNSET)
    events_url: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: Missing[List[WebhookIssuesUnlockedPropIssueMergedLabels]] = Field(
        default=UNSET
    )
    labels_url: str = Field()
    locked: Literal[False] = Field()
    milestone: Union[WebhookIssuesUnlockedPropIssueMergedMilestone, None] = Field()
    node_id: str = Field()
    number: int = Field()
    performed_via_github_app: Missing[Union[None, None]] = Field(default=UNSET)
    pull_request: Missing[WebhookIssuesUnlockedPropIssueAllof0PropPullRequest] = Field(
        default=UNSET
    )
    reactions: WebhookIssuesUnlockedPropIssueMergedReactions = Field()
    repository_url: str = Field()
    state: Missing[Literal["open", "closed"]] = Field(
        default=UNSET, description="State of the issue; either 'open' or 'closed'"
    )
    state_reason: Missing[Union[str, None]] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    title: str = Field(description="Title of the issue")
    updated_at: datetime = Field()
    url: str = Field(description="URL for the issue")
    user: WebhookIssuesUnlockedPropIssueMergedUser = Field()


class WebhookIssuesUnlockedPropIssueMergedAssignee(GitHubModel):
    """WebhookIssuesUnlockedPropIssueMergedAssignee"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesUnlockedPropIssueMergedAssignees(GitHubModel):
    """WebhookIssuesUnlockedPropIssueMergedAssignees"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesUnlockedPropIssueMergedLabels(GitHubModel):
    """WebhookIssuesUnlockedPropIssueMergedLabels"""

    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()
    description: Union[str, None] = Field()
    id: int = Field()
    name: str = Field(description="The name of the label.")
    node_id: str = Field()
    url: str = Field(description="URL for the label")


class WebhookIssuesUnlockedPropIssueMergedReactions(GitHubModel):
    """WebhookIssuesUnlockedPropIssueMergedReactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhookIssuesUnlockedPropIssueMergedUser(GitHubModel):
    """WebhookIssuesUnlockedPropIssueMergedUser"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssuesUnlockedPropIssue)
model_rebuild(WebhookIssuesUnlockedPropIssueMergedAssignee)
model_rebuild(WebhookIssuesUnlockedPropIssueMergedAssignees)
model_rebuild(WebhookIssuesUnlockedPropIssueMergedLabels)
model_rebuild(WebhookIssuesUnlockedPropIssueMergedReactions)
model_rebuild(WebhookIssuesUnlockedPropIssueMergedUser)

__all__ = (
    "WebhookIssuesUnlockedPropIssue",
    "WebhookIssuesUnlockedPropIssueMergedAssignee",
    "WebhookIssuesUnlockedPropIssueMergedAssignees",
    "WebhookIssuesUnlockedPropIssueMergedLabels",
    "WebhookIssuesUnlockedPropIssueMergedReactions",
    "WebhookIssuesUnlockedPropIssueMergedUser",
)
