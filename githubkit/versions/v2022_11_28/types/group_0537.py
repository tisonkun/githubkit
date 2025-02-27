"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookIssuesReopenedPropIssueAllof1Type(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1"""

    active_lock_reason: NotRequired[Union[str, None]]
    assignee: NotRequired[
        Union[WebhookIssuesReopenedPropIssueAllof1PropAssigneeType, None]
    ]
    assignees: NotRequired[
        List[Union[WebhookIssuesReopenedPropIssueAllof1PropAssigneesItemsType, None]]
    ]
    author_association: NotRequired[str]
    body: NotRequired[Union[str, None]]
    closed_at: NotRequired[Union[str, None]]
    comments: NotRequired[int]
    comments_url: NotRequired[str]
    created_at: NotRequired[str]
    events_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    labels: NotRequired[
        List[Union[WebhookIssuesReopenedPropIssueAllof1PropLabelsItemsType, None]]
    ]
    labels_url: NotRequired[str]
    locked: NotRequired[bool]
    milestone: NotRequired[
        Union[WebhookIssuesReopenedPropIssueAllof1PropMilestoneType, None]
    ]
    node_id: NotRequired[str]
    number: NotRequired[int]
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesReopenedPropIssueAllof1PropPerformedViaGithubAppType, None]
    ]
    reactions: NotRequired[WebhookIssuesReopenedPropIssueAllof1PropReactionsType]
    repository_url: NotRequired[str]
    state: Literal["open", "closed"]
    timeline_url: NotRequired[str]
    title: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    user: NotRequired[WebhookIssuesReopenedPropIssueAllof1PropUserType]


class WebhookIssuesReopenedPropIssueAllof1PropAssigneeType(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1PropAssignee"""


class WebhookIssuesReopenedPropIssueAllof1PropAssigneesItemsType(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesReopenedPropIssueAllof1PropLabelsItemsType(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesReopenedPropIssueAllof1PropMilestoneType(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1PropMilestone"""


class WebhookIssuesReopenedPropIssueAllof1PropPerformedViaGithubAppType(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssuesReopenedPropIssueAllof1PropReactionsType(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1PropReactions"""

    plus_one: NotRequired[int]
    minus_one: NotRequired[int]
    confused: NotRequired[int]
    eyes: NotRequired[int]
    heart: NotRequired[int]
    hooray: NotRequired[int]
    laugh: NotRequired[int]
    rocket: NotRequired[int]
    total_count: NotRequired[int]
    url: NotRequired[str]


class WebhookIssuesReopenedPropIssueAllof1PropUserType(TypedDict):
    """WebhookIssuesReopenedPropIssueAllof1PropUser"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


__all__ = (
    "WebhookIssuesReopenedPropIssueAllof1Type",
    "WebhookIssuesReopenedPropIssueAllof1PropAssigneeType",
    "WebhookIssuesReopenedPropIssueAllof1PropAssigneesItemsType",
    "WebhookIssuesReopenedPropIssueAllof1PropLabelsItemsType",
    "WebhookIssuesReopenedPropIssueAllof1PropMilestoneType",
    "WebhookIssuesReopenedPropIssueAllof1PropPerformedViaGithubAppType",
    "WebhookIssuesReopenedPropIssueAllof1PropReactionsType",
    "WebhookIssuesReopenedPropIssueAllof1PropUserType",
)
