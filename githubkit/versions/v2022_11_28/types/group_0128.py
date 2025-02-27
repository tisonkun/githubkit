"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0129 import RepositoryRuleWorkflowsPropParametersType


class RepositoryRuleWorkflowsType(TypedDict):
    """workflows

    Require all changes made to a targeted branch to pass the specified workflows
    before they can be merged.
    """

    type: Literal["workflows"]
    parameters: NotRequired[RepositoryRuleWorkflowsPropParametersType]


__all__ = ("RepositoryRuleWorkflowsType",)
