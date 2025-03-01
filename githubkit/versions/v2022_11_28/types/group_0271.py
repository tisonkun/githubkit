"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class TimelineCommittedEventType(TypedDict):
    """Timeline Committed Event

    Timeline Committed Event
    """

    event: NotRequired[Literal["committed"]]
    sha: str
    node_id: str
    url: str
    author: TimelineCommittedEventPropAuthorType
    committer: TimelineCommittedEventPropCommitterType
    message: str
    tree: TimelineCommittedEventPropTreeType
    parents: List[TimelineCommittedEventPropParentsItemsType]
    verification: TimelineCommittedEventPropVerificationType
    html_url: str


class TimelineCommittedEventPropAuthorType(TypedDict):
    """TimelineCommittedEventPropAuthor

    Identifying information for the git-user
    """

    date: datetime
    email: str
    name: str


class TimelineCommittedEventPropCommitterType(TypedDict):
    """TimelineCommittedEventPropCommitter

    Identifying information for the git-user
    """

    date: datetime
    email: str
    name: str


class TimelineCommittedEventPropTreeType(TypedDict):
    """TimelineCommittedEventPropTree"""

    sha: str
    url: str


class TimelineCommittedEventPropParentsItemsType(TypedDict):
    """TimelineCommittedEventPropParentsItems"""

    sha: str
    url: str
    html_url: str


class TimelineCommittedEventPropVerificationType(TypedDict):
    """TimelineCommittedEventPropVerification"""

    verified: bool
    reason: str
    signature: Union[str, None]
    payload: Union[str, None]


__all__ = (
    "TimelineCommittedEventType",
    "TimelineCommittedEventPropAuthorType",
    "TimelineCommittedEventPropCommitterType",
    "TimelineCommittedEventPropTreeType",
    "TimelineCommittedEventPropParentsItemsType",
    "TimelineCommittedEventPropVerificationType",
)
