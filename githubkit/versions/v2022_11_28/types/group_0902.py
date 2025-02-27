"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0109 import RepositoryRuleUpdateType
from .group_0128 import RepositoryRuleWorkflowsType
from .group_0114 import RepositoryRulePullRequestType
from .group_0105 import OrgRulesetConditionsOneof0Type
from .group_0106 import OrgRulesetConditionsOneof1Type
from .group_0107 import OrgRulesetConditionsOneof2Type
from .group_0096 import RepositoryRulesetBypassActorType
from .group_0126 import RepositoryRuleTagNamePatternType
from .group_0124 import RepositoryRuleBranchNamePatternType
from .group_0112 import RepositoryRuleRequiredDeploymentsType
from .group_0116 import RepositoryRuleRequiredStatusChecksType
from .group_0118 import RepositoryRuleCommitMessagePatternType
from .group_0111 import RepositoryRuleRequiredLinearHistoryType
from .group_0122 import RepositoryRuleCommitterEmailPatternType
from .group_0120 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0108 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class OrgsOrgRulesetsRulesetIdPutBodyType(TypedDict):
    """OrgsOrgRulesetsRulesetIdPutBody"""

    name: NotRequired[str]
    target: NotRequired[Literal["branch", "tag"]]
    enforcement: NotRequired[Literal["disabled", "active", "evaluate"]]
    bypass_actors: NotRequired[List[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[
        Union[
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            OrgRulesetConditionsOneof2Type,
        ]
    ]
    rules: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleWorkflowsType,
            ]
        ]
    ]


__all__ = ("OrgsOrgRulesetsRulesetIdPutBodyType",)
