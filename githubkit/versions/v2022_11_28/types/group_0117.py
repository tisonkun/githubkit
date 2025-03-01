"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class RepositoryRuleRequiredStatusChecksPropParametersType(TypedDict):
    """RepositoryRuleRequiredStatusChecksPropParameters"""

    required_status_checks: List[RepositoryRuleParamsStatusCheckConfigurationType]
    strict_required_status_checks_policy: bool


class RepositoryRuleParamsStatusCheckConfigurationType(TypedDict):
    """StatusCheckConfiguration

    Required status check
    """

    context: str
    integration_id: NotRequired[int]


__all__ = (
    "RepositoryRuleRequiredStatusChecksPropParametersType",
    "RepositoryRuleParamsStatusCheckConfigurationType",
)
