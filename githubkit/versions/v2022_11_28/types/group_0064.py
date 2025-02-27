"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0017 import RepositoryType


class AuthenticationTokenType(TypedDict):
    """Authentication Token

    Authentication Token
    """

    token: str
    expires_at: datetime
    permissions: NotRequired[AuthenticationTokenPropPermissionsType]
    repositories: NotRequired[List[RepositoryType]]
    single_file: NotRequired[Union[str, None]]
    repository_selection: NotRequired[Literal["all", "selected"]]


class AuthenticationTokenPropPermissionsType(TypedDict):
    """AuthenticationTokenPropPermissions

    Examples:
        {'issues': 'read', 'deployments': 'write'}
    """


__all__ = (
    "AuthenticationTokenType",
    "AuthenticationTokenPropPermissionsType",
)
