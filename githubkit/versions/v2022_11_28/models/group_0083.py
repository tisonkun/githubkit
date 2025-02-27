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
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class OrgMembership(GitHubModel):
    """Org Membership

    Org Membership
    """

    url: str = Field()
    state: Literal["active", "pending"] = Field(
        description="The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation."
    )
    role: Literal["admin", "member", "billing_manager"] = Field(
        description="The user's membership type in the organization."
    )
    organization_url: str = Field()
    organization: OrganizationSimple = Field(
        title="Organization Simple", description="A GitHub organization."
    )
    user: Union[None, SimpleUser] = Field()
    permissions: Missing[OrgMembershipPropPermissions] = Field(default=UNSET)


class OrganizationSimple(GitHubModel):
    """Organization Simple

    A GitHub organization.
    """

    login: str = Field()
    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    repos_url: str = Field()
    events_url: str = Field()
    hooks_url: str = Field()
    issues_url: str = Field()
    members_url: str = Field()
    public_members_url: str = Field()
    avatar_url: str = Field()
    description: Union[str, None] = Field()


class OrgMembershipPropPermissions(GitHubModel):
    """OrgMembershipPropPermissions"""

    can_create_repository: bool = Field()


model_rebuild(OrgMembership)
model_rebuild(OrganizationSimple)
model_rebuild(OrgMembershipPropPermissions)

__all__ = (
    "OrgMembership",
    "OrganizationSimple",
    "OrgMembershipPropPermissions",
)
