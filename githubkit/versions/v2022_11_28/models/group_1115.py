"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class UserPatchBody(GitHubModel):
    """UserPatchBody"""

    name: Missing[str] = Field(default=UNSET, description="The new name of the user.")
    email: Missing[str] = Field(
        default=UNSET, description="The publicly visible email address of the user."
    )
    blog: Missing[str] = Field(
        default=UNSET, description="The new blog URL of the user."
    )
    twitter_username: Missing[Union[str, None]] = Field(
        default=UNSET, description="The new Twitter username of the user."
    )
    company: Missing[str] = Field(
        default=UNSET, description="The new company of the user."
    )
    location: Missing[str] = Field(
        default=UNSET, description="The new location of the user."
    )
    hireable: Missing[bool] = Field(
        default=UNSET, description="The new hiring availability of the user."
    )
    bio: Missing[str] = Field(
        default=UNSET, description="The new short biography of the user."
    )


model_rebuild(UserPatchBody)

__all__ = ("UserPatchBody",)
