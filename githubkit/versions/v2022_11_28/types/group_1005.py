"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type(TypedDict):
    """ReposOwnerRepoDependencyGraphSnapshotsPostResponse201"""

    id: int
    created_at: str
    result: str
    message: str


__all__ = ("ReposOwnerRepoDependencyGraphSnapshotsPostResponse201Type",)
