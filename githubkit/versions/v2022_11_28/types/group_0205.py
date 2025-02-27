"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0033 import ReactionRollupType


class CommitCommentType(TypedDict):
    """Commit Comment

    Commit Comment
    """

    html_url: str
    url: str
    id: int
    node_id: str
    body: str
    path: Union[str, None]
    position: Union[int, None]
    line: Union[int, None]
    commit_id: str
    user: Union[None, SimpleUserType]
    created_at: datetime
    updated_at: datetime
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
    reactions: NotRequired[ReactionRollupType]


class TimelineCommitCommentedEventType(TypedDict):
    """Timeline Commit Commented Event

    Timeline Commit Commented Event
    """

    event: NotRequired[Literal["commit_commented"]]
    node_id: NotRequired[str]
    commit_id: NotRequired[str]
    comments: NotRequired[List[CommitCommentType]]


__all__ = (
    "CommitCommentType",
    "TimelineCommitCommentedEventType",
)
