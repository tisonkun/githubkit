"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoPullsCommentsCommentIdPatchBody(GitHubModel):
    """ReposOwnerRepoPullsCommentsCommentIdPatchBody"""

    body: str = Field(description="The text of the reply to the review comment.")


model_rebuild(ReposOwnerRepoPullsCommentsCommentIdPatchBody)

__all__ = ("ReposOwnerRepoPullsCommentsCommentIdPatchBody",)
