"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoIssuesIssueNumberAssigneesDeleteBody(GitHubModel):
    """ReposOwnerRepoIssuesIssueNumberAssigneesDeleteBody"""

    assignees: Missing[List[str]] = Field(
        default=UNSET,
        description="Usernames of assignees to remove from an issue. _NOTE: Only users with push access can remove assignees from an issue. Assignees are silently ignored otherwise._",
    )


model_rebuild(ReposOwnerRepoIssuesIssueNumberAssigneesDeleteBody)

__all__ = ("ReposOwnerRepoIssuesIssueNumberAssigneesDeleteBody",)
