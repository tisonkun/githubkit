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


class ReposOwnerRepoCheckSuitesPreferencesPatchBody(GitHubModel):
    """ReposOwnerRepoCheckSuitesPreferencesPatchBody"""

    auto_trigger_checks: Missing[
        List[ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItems]
    ] = Field(
        default=UNSET,
        description="Enables or disables automatic creation of CheckSuite events upon pushes to the repository. Enabled by default.",
    )


class ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItems(
    GitHubModel
):
    """ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItems"""

    app_id: int = Field(description="The `id` of the GitHub App.")
    setting: bool = Field(
        default=True,
        description="Set to `true` to enable automatic creation of CheckSuite events upon pushes to the repository, or `false` to disable them.",
    )


model_rebuild(ReposOwnerRepoCheckSuitesPreferencesPatchBody)
model_rebuild(ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItems)

__all__ = (
    "ReposOwnerRepoCheckSuitesPreferencesPatchBody",
    "ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItems",
)
