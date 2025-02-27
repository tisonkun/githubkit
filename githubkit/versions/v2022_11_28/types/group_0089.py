"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class OrganizationProgrammaticAccessGrantType(TypedDict):
    """Organization Programmatic Access Grant

    Minimal representation of an organization programmatic access grant for
    enumerations
    """

    id: int
    owner: SimpleUserType
    repository_selection: Literal["none", "all", "subset"]
    repositories_url: str
    permissions: OrganizationProgrammaticAccessGrantPropPermissionsType
    access_granted_at: str
    token_expired: bool
    token_expires_at: Union[str, None]
    token_last_used_at: Union[str, None]


class OrganizationProgrammaticAccessGrantPropPermissionsType(TypedDict):
    """OrganizationProgrammaticAccessGrantPropPermissions

    Permissions requested, categorized by type of permission.
    """

    organization: NotRequired[
        OrganizationProgrammaticAccessGrantPropPermissionsPropOrganizationType
    ]
    repository: NotRequired[
        OrganizationProgrammaticAccessGrantPropPermissionsPropRepositoryType
    ]
    other: NotRequired[OrganizationProgrammaticAccessGrantPropPermissionsPropOtherType]


class OrganizationProgrammaticAccessGrantPropPermissionsPropOrganizationType(TypedDict):
    """OrganizationProgrammaticAccessGrantPropPermissionsPropOrganization"""


class OrganizationProgrammaticAccessGrantPropPermissionsPropRepositoryType(TypedDict):
    """OrganizationProgrammaticAccessGrantPropPermissionsPropRepository"""


class OrganizationProgrammaticAccessGrantPropPermissionsPropOtherType(TypedDict):
    """OrganizationProgrammaticAccessGrantPropPermissionsPropOther"""


__all__ = (
    "OrganizationProgrammaticAccessGrantType",
    "OrganizationProgrammaticAccessGrantPropPermissionsType",
    "OrganizationProgrammaticAccessGrantPropPermissionsPropOrganizationType",
    "OrganizationProgrammaticAccessGrantPropPermissionsPropRepositoryType",
    "OrganizationProgrammaticAccessGrantPropPermissionsPropOtherType",
)
