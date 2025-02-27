"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0538 import WebhookIssuesReopenedPropIssueMergedMilestoneType
from .group_0536 import WebhookIssuesReopenedPropIssueAllof0PropPullRequestType
from .group_0539 import WebhookIssuesReopenedPropIssueMergedPerformedViaGithubAppType


class WebhookIssuesReopenedPropIssueType(TypedDict):
    """WebhookIssuesReopenedPropIssue"""

    active_lock_reason: Union[
        Literal["resolved", "off-topic", "too heated", "spam"], None
    ]
    assignee: NotRequired[Union[WebhookIssuesReopenedPropIssueMergedAssigneeType, None]]
    assignees: List[WebhookIssuesReopenedPropIssueMergedAssigneesType]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: Union[Union[str, None], None]
    closed_at: Union[datetime, None]
    comments: int
    comments_url: str
    created_at: datetime
    draft: NotRequired[bool]
    events_url: str
    html_url: str
    id: int
    labels: NotRequired[List[WebhookIssuesReopenedPropIssueMergedLabelsType]]
    labels_url: str
    locked: NotRequired[bool]
    milestone: Union[WebhookIssuesReopenedPropIssueMergedMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesReopenedPropIssueMergedPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[WebhookIssuesReopenedPropIssueAllof0PropPullRequestType]
    reactions: WebhookIssuesReopenedPropIssueMergedReactionsType
    repository_url: str
    state: Literal["open", "closed"]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: WebhookIssuesReopenedPropIssueMergedUserType


class WebhookIssuesReopenedPropIssueMergedAssigneeType(TypedDict):
    """WebhookIssuesReopenedPropIssueMergedAssignee"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookIssuesReopenedPropIssueMergedAssigneesType(TypedDict):
    """WebhookIssuesReopenedPropIssueMergedAssignees"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookIssuesReopenedPropIssueMergedLabelsType(TypedDict):
    """WebhookIssuesReopenedPropIssueMergedLabels"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesReopenedPropIssueMergedReactionsType(TypedDict):
    """WebhookIssuesReopenedPropIssueMergedReactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookIssuesReopenedPropIssueMergedUserType(TypedDict):
    """WebhookIssuesReopenedPropIssueMergedUser"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


__all__ = (
    "WebhookIssuesReopenedPropIssueType",
    "WebhookIssuesReopenedPropIssueMergedAssigneeType",
    "WebhookIssuesReopenedPropIssueMergedAssigneesType",
    "WebhookIssuesReopenedPropIssueMergedLabelsType",
    "WebhookIssuesReopenedPropIssueMergedReactionsType",
    "WebhookIssuesReopenedPropIssueMergedUserType",
)
