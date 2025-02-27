"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class UserMigrationsPostBodyType(TypedDict):
    """UserMigrationsPostBody"""

    lock_repositories: NotRequired[bool]
    exclude_metadata: NotRequired[bool]
    exclude_git_data: NotRequired[bool]
    exclude_attachments: NotRequired[bool]
    exclude_releases: NotRequired[bool]
    exclude_owner_projects: NotRequired[bool]
    org_metadata_only: NotRequired[bool]
    exclude: NotRequired[List[Literal["repositories"]]]
    repositories: List[str]


__all__ = ("UserMigrationsPostBodyType",)
