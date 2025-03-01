"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0127 import RepositoryRuleTagNamePatternPropParametersType


class RepositoryRuleDetailedOneof13Type(TypedDict):
    """RepositoryRuleDetailedOneof13"""

    type: Literal["tag_name_pattern"]
    parameters: NotRequired[RepositoryRuleTagNamePatternPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof13Type",)
