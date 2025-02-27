"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ActionsCacheList(GitHubModel):
    """Repository actions caches

    Repository actions caches
    """

    total_count: int = Field(description="Total number of caches")
    actions_caches: List[ActionsCacheListPropActionsCachesItems] = Field(
        description="Array of caches"
    )


class ActionsCacheListPropActionsCachesItems(GitHubModel):
    """ActionsCacheListPropActionsCachesItems"""

    id: Missing[int] = Field(default=UNSET)
    ref: Missing[str] = Field(default=UNSET)
    key: Missing[str] = Field(default=UNSET)
    version: Missing[str] = Field(default=UNSET)
    last_accessed_at: Missing[datetime] = Field(default=UNSET)
    created_at: Missing[datetime] = Field(default=UNSET)
    size_in_bytes: Missing[int] = Field(default=UNSET)


model_rebuild(ActionsCacheList)
model_rebuild(ActionsCacheListPropActionsCachesItems)

__all__ = (
    "ActionsCacheList",
    "ActionsCacheListPropActionsCachesItems",
)
