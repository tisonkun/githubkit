"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoPullsPullNumberReviewsReviewIdDismissalsPutBody(GitHubModel):
    """ReposOwnerRepoPullsPullNumberReviewsReviewIdDismissalsPutBody"""

    message: str = Field(
        description="The message for the pull request review dismissal"
    )
    event: Missing[Literal["DISMISS"]] = Field(default=UNSET)


model_rebuild(ReposOwnerRepoPullsPullNumberReviewsReviewIdDismissalsPutBody)

__all__ = ("ReposOwnerRepoPullsPullNumberReviewsReviewIdDismissalsPutBody",)
