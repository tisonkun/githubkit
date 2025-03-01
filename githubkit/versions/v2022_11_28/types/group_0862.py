"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgCodespacesSecretsGetResponse200Type(TypedDict):
    """OrgsOrgCodespacesSecretsGetResponse200"""

    total_count: int
    secrets: List[CodespacesOrgSecretType]


class CodespacesOrgSecretType(TypedDict):
    """Codespaces Secret

    Secrets for a GitHub Codespace.
    """

    name: str
    created_at: datetime
    updated_at: datetime
    visibility: Literal["all", "private", "selected"]
    selected_repositories_url: NotRequired[str]


__all__ = (
    "OrgsOrgCodespacesSecretsGetResponse200Type",
    "CodespacesOrgSecretType",
)
