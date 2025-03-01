"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgDependabotSecretsGetResponse200Type(TypedDict):
    """OrgsOrgDependabotSecretsGetResponse200"""

    total_count: int
    secrets: List[OrganizationDependabotSecretType]


class OrganizationDependabotSecretType(TypedDict):
    """Dependabot Secret for an Organization

    Secrets for GitHub Dependabot for an organization.
    """

    name: str
    created_at: datetime
    updated_at: datetime
    visibility: Literal["all", "private", "selected"]
    selected_repositories_url: NotRequired[str]


__all__ = (
    "OrgsOrgDependabotSecretsGetResponse200Type",
    "OrganizationDependabotSecretType",
)
