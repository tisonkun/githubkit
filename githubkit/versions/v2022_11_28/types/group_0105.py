"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0098 import RepositoryRulesetConditionsPropRefNameType
from .group_0100 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType,
)


class OrgRulesetConditionsOneof0Type(TypedDict):
    """repository_name_and_ref_name

    Conditions to target repositories by name and refs by name
    """

    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]
    repository_name: (
        RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType
    )


__all__ = ("OrgRulesetConditionsOneof0Type",)
