"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class GitUser(GitHubModel):
    """Git User

    Metaproperties for Git author/committer information.
    """

    name: Missing[str] = Field(default=UNSET)
    email: Missing[str] = Field(default=UNSET)
    date: Missing[str] = Field(default=UNSET)


model_rebuild(GitUser)

__all__ = ("GitUser",)
