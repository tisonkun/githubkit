"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoPullsPostBodyType(TypedDict):
    """ReposOwnerRepoPullsPostBody"""

    title: NotRequired[str]
    head: str
    head_repo: NotRequired[str]
    base: str
    body: NotRequired[str]
    maintainer_can_modify: NotRequired[bool]
    draft: NotRequired[bool]
    issue: NotRequired[int]


__all__ = ("ReposOwnerRepoPullsPostBodyType",)
