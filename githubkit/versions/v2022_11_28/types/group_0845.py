"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0061 import RunnerLabelType


class OrgsOrgActionsRunnersRunnerIdLabelsGetResponse200Type(TypedDict):
    """OrgsOrgActionsRunnersRunnerIdLabelsGetResponse200"""

    total_count: int
    labels: List[RunnerLabelType]


__all__ = ("OrgsOrgActionsRunnersRunnerIdLabelsGetResponse200Type",)
