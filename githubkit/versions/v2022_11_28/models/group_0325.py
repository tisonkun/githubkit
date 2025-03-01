"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Tag(GitHubModel):
    """Tag

    Tag
    """

    name: str = Field()
    commit: TagPropCommit = Field()
    zipball_url: str = Field()
    tarball_url: str = Field()
    node_id: str = Field()


class TagPropCommit(GitHubModel):
    """TagPropCommit"""

    sha: str = Field()
    url: str = Field()


model_rebuild(Tag)
model_rebuild(TagPropCommit)

__all__ = (
    "Tag",
    "TagPropCommit",
)
