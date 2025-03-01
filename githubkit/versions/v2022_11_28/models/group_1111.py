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


class TeamsTeamIdMembershipsUsernamePutBody(GitHubModel):
    """TeamsTeamIdMembershipsUsernamePutBody"""

    role: Missing[Literal["member", "maintainer"]] = Field(
        default=UNSET, description="The role that this user should have in the team."
    )


model_rebuild(TeamsTeamIdMembershipsUsernamePutBody)

__all__ = ("TeamsTeamIdMembershipsUsernamePutBody",)
