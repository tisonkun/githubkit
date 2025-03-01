"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0050 import MinimalRepositoryType


class ThreadType(TypedDict):
    """Thread

    Thread
    """

    id: str
    repository: MinimalRepositoryType
    subject: ThreadPropSubjectType
    reason: str
    unread: bool
    updated_at: str
    last_read_at: Union[str, None]
    url: str
    subscription_url: str


class ThreadPropSubjectType(TypedDict):
    """ThreadPropSubject"""

    title: str
    url: str
    latest_comment_url: str
    type: str


__all__ = (
    "ThreadType",
    "ThreadPropSubjectType",
)
