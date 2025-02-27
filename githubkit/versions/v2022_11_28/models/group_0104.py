"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty(
    GitHubModel
):
    """RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty"""

    include: Missing[List[RepositoryRulesetConditionsRepositoryPropertySpec]] = Field(
        default=UNSET,
        description="The repository properties and values to include. All of these properties must match for the condition to pass.",
    )
    exclude: Missing[List[RepositoryRulesetConditionsRepositoryPropertySpec]] = Field(
        default=UNSET,
        description="The repository properties and values to exclude. The condition will not pass if any of these properties match.",
    )


class RepositoryRulesetConditionsRepositoryPropertySpec(GitHubModel):
    """Repository ruleset property targeting definition

    Parameters for a targeting a repository property
    """

    name: str = Field(description="The name of the repository property to target")
    property_values: List[str] = Field(
        description="The values to match for the repository property"
    )


model_rebuild(RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty)
model_rebuild(RepositoryRulesetConditionsRepositoryPropertySpec)

__all__ = (
    "RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty",
    "RepositoryRulesetConditionsRepositoryPropertySpec",
)
