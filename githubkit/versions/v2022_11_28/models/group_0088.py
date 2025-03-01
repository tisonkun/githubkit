"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0001 import SimpleUser


class OrganizationProgrammaticAccessGrantRequest(GitHubModel):
    """Simple Organization Programmatic Access Grant Request

    Minimal representation of an organization programmatic access grant request for
    enumerations
    """

    id: int = Field(
        description="Unique identifier of the request for access via fine-grained personal access token. The `pat_request_id` used to review PAT requests."
    )
    reason: Union[str, None] = Field(description="Reason for requesting access.")
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    repository_selection: Literal["none", "all", "subset"] = Field(
        description="Type of repository selection requested."
    )
    repositories_url: str = Field(
        description="URL to the list of repositories requested to be accessed via fine-grained personal access token. Should only be followed when `repository_selection` is `subset`."
    )
    permissions: OrganizationProgrammaticAccessGrantRequestPropPermissions = Field(
        description="Permissions requested, categorized by type of permission."
    )
    created_at: str = Field(
        description="Date and time when the request for access was created."
    )
    token_expired: bool = Field(
        description="Whether the associated fine-grained personal access token has expired."
    )
    token_expires_at: Union[str, None] = Field(
        description="Date and time when the associated fine-grained personal access token expires."
    )
    token_last_used_at: Union[str, None] = Field(
        description="Date and time when the associated fine-grained personal access token was last used for authentication."
    )


class OrganizationProgrammaticAccessGrantRequestPropPermissions(GitHubModel):
    """OrganizationProgrammaticAccessGrantRequestPropPermissions

    Permissions requested, categorized by type of permission.
    """

    organization: Missing[
        OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOrganization
    ] = Field(default=UNSET)
    repository: Missing[
        OrganizationProgrammaticAccessGrantRequestPropPermissionsPropRepository
    ] = Field(default=UNSET)
    other: Missing[
        OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOther
    ] = Field(default=UNSET)


class OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOrganization(
    ExtraGitHubModel
):
    """OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOrganization"""


class OrganizationProgrammaticAccessGrantRequestPropPermissionsPropRepository(
    ExtraGitHubModel
):
    """OrganizationProgrammaticAccessGrantRequestPropPermissionsPropRepository"""


class OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOther(
    ExtraGitHubModel
):
    """OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOther"""


model_rebuild(OrganizationProgrammaticAccessGrantRequest)
model_rebuild(OrganizationProgrammaticAccessGrantRequestPropPermissions)
model_rebuild(OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOrganization)
model_rebuild(OrganizationProgrammaticAccessGrantRequestPropPermissionsPropRepository)
model_rebuild(OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOther)

__all__ = (
    "OrganizationProgrammaticAccessGrantRequest",
    "OrganizationProgrammaticAccessGrantRequestPropPermissions",
    "OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOrganization",
    "OrganizationProgrammaticAccessGrantRequestPropPermissionsPropRepository",
    "OrganizationProgrammaticAccessGrantRequestPropPermissionsPropOther",
)
