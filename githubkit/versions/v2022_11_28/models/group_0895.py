"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgPersonalAccessTokensPatIdPostBody(GitHubModel):
    """OrgsOrgPersonalAccessTokensPatIdPostBody"""

    action: Literal["revoke"] = Field(
        description="Action to apply to the fine-grained personal access token."
    )


model_rebuild(OrgsOrgPersonalAccessTokensPatIdPostBody)

__all__ = ("OrgsOrgPersonalAccessTokensPatIdPostBody",)
