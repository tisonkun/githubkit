"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict


class ReposOwnerRepoPagesPutBodyPropSourceAnyof1Type(TypedDict):
    """ReposOwnerRepoPagesPutBodyPropSourceAnyof1

    Update the source for the repository. Must include the branch name and path.
    """

    branch: str
    path: Literal["/", "/docs"]


__all__ = ("ReposOwnerRepoPagesPutBodyPropSourceAnyof1Type",)
