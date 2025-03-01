"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsDeleteBodyOneof0(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsDeleteBodyOneo
    f0

    Examples:
        {'contexts': ['contexts']}
    """

    contexts: List[str] = Field(description="The name of the status checks")


model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsDeleteBodyOneof0
)

__all__ = (
    "ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsDeleteBodyOneof0",
)
