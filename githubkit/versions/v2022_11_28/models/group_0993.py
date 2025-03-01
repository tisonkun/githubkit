"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoCodespacesSecretsGetResponse200(GitHubModel):
    """ReposOwnerRepoCodespacesSecretsGetResponse200"""

    total_count: int = Field()
    secrets: List[RepoCodespacesSecret] = Field()


class RepoCodespacesSecret(GitHubModel):
    """Codespaces Secret

    Set repository secrets for GitHub Codespaces.
    """

    name: str = Field(description="The name of the secret.")
    created_at: datetime = Field()
    updated_at: datetime = Field()


model_rebuild(ReposOwnerRepoCodespacesSecretsGetResponse200)
model_rebuild(RepoCodespacesSecret)

__all__ = (
    "ReposOwnerRepoCodespacesSecretsGetResponse200",
    "RepoCodespacesSecret",
)
