"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ApplicationsClientIdTokenPatchBody(GitHubModel):
    """ApplicationsClientIdTokenPatchBody"""

    access_token: str = Field(
        description="The access_token of the OAuth or GitHub application."
    )


model_rebuild(ApplicationsClientIdTokenPatchBody)

__all__ = ("ApplicationsClientIdTokenPatchBody",)
