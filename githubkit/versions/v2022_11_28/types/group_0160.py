"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict


class SimpleCommitType(TypedDict):
    """Simple Commit

    A commit.
    """

    id: str
    tree_id: str
    message: str
    timestamp: datetime
    author: Union[SimpleCommitPropAuthorType, None]
    committer: Union[SimpleCommitPropCommitterType, None]


class SimpleCommitPropAuthorType(TypedDict):
    """SimpleCommitPropAuthor

    Information about the Git author
    """

    name: str
    email: str


class SimpleCommitPropCommitterType(TypedDict):
    """SimpleCommitPropCommitter

    Information about the Git committer
    """

    name: str
    email: str


__all__ = (
    "SimpleCommitType",
    "SimpleCommitPropAuthorType",
    "SimpleCommitPropCommitterType",
)
