"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgCodespacesAccessPutBodyType(TypedDict):
    """OrgsOrgCodespacesAccessPutBody"""

    visibility: Literal[
        "disabled",
        "selected_members",
        "all_members",
        "all_members_and_outside_collaborators",
    ]
    selected_usernames: NotRequired[List[str]]


__all__ = ("OrgsOrgCodespacesAccessPutBodyType",)
