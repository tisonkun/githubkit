"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class PageBuildStatus(GitHubModel):
    """Page Build Status

    Page Build Status
    """

    url: str = Field()
    status: str = Field()


model_rebuild(PageBuildStatus)

__all__ = ("PageBuildStatus",)
