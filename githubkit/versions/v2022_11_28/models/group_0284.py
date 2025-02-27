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


class PageDeployment(GitHubModel):
    """GitHub Pages

    The GitHub Pages deployment status.
    """

    status_url: str = Field(
        description="The URI to monitor GitHub Pages deployment status."
    )
    page_url: str = Field(description="The URI to the deployed GitHub Pages.")
    preview_url: Missing[str] = Field(
        default=UNSET, description="The URI to the deployed GitHub Pages preview."
    )


model_rebuild(PageDeployment)

__all__ = ("PageDeployment",)
