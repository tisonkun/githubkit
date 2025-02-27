"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0470 import WebhookIssueCommentDeletedPropIssueMergedMilestoneType
from .group_0471 import (
    WebhookIssueCommentDeletedPropIssueMergedPerformedViaGithubAppType,
)
from .group_0464 import (
    WebhookIssueCommentDeletedPropIssueAllof0PropAssigneeType,
    WebhookIssueCommentDeletedPropIssueAllof0PropLabelsItemsType,
    WebhookIssueCommentDeletedPropIssueAllof0PropPullRequestType,
)


class WebhookIssueCommentDeletedPropIssueType(TypedDict):
    """WebhookIssueCommentDeletedPropIssue

    The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) the comment
    belongs to.
    """

    active_lock_reason: Union[
        Literal["resolved", "off-topic", "too heated", "spam"], None
    ]
    assignee: Union[
        Union[WebhookIssueCommentDeletedPropIssueAllof0PropAssigneeType, None], None
    ]
    assignees: List[WebhookIssueCommentDeletedPropIssueMergedAssigneesType]
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
    labels: List[WebhookIssueCommentDeletedPropIssueAllof0PropLabelsItemsType]
    labels_url: str
    locked: bool
    milestone: Union[WebhookIssueCommentDeletedPropIssueMergedMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssueCommentDeletedPropIssueMergedPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[
        WebhookIssueCommentDeletedPropIssueAllof0PropPullRequestType
    ]
    reactions: WebhookIssueCommentDeletedPropIssueMergedReactionsType
    repository_url: str
    state: Literal["open", "closed"]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: WebhookIssueCommentDeletedPropIssueMergedUserType


class WebhookIssueCommentDeletedPropIssueMergedAssigneesType(TypedDict):
    """WebhookIssueCommentDeletedPropIssueMergedAssignees"""

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


class WebhookIssueCommentDeletedPropIssueMergedReactionsType(TypedDict):
    """WebhookIssueCommentDeletedPropIssueMergedReactions"""

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


class WebhookIssueCommentDeletedPropIssueMergedUserType(TypedDict):
    """WebhookIssueCommentDeletedPropIssueMergedUser"""

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
    "WebhookIssueCommentDeletedPropIssueType",
    "WebhookIssueCommentDeletedPropIssueMergedAssigneesType",
    "WebhookIssueCommentDeletedPropIssueMergedReactionsType",
    "WebhookIssueCommentDeletedPropIssueMergedUserType",
)
