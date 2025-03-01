"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Email(GitHubModel):
    """Email

    Email
    """

    email: str = Field()
    primary: bool = Field()
    verified: bool = Field()
    visibility: Union[str, None] = Field()


model_rebuild(Email)

__all__ = ("Email",)
