"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0153 import JobType


class ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200Type(
    TypedDict
):
    """ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200"""

    total_count: int
    jobs: List[JobType]


__all__ = ("ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200Type",)
