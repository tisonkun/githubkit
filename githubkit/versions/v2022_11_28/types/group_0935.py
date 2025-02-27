"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0151 import ArtifactType


class ReposOwnerRepoActionsArtifactsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsArtifactsGetResponse200"""

    total_count: int
    artifacts: List[ArtifactType]


__all__ = ("ReposOwnerRepoActionsArtifactsGetResponse200Type",)
