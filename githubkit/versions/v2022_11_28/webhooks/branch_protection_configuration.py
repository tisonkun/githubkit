"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.utils import TaggedUnion
from githubkit.compat import GitHubModel

from ..models import (
    WebhookBranchProtectionConfigurationEnabled,
    WebhookBranchProtectionConfigurationDisabled,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookBranchProtectionConfigurationDisabled,
        WebhookBranchProtectionConfigurationEnabled,
    ],
    Field(discriminator="action"),
]

BranchProtectionConfigurationEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "disabled": WebhookBranchProtectionConfigurationDisabled,
    "enabled": WebhookBranchProtectionConfigurationEnabled,
}

branch_protection_configuration_action_types = action_types

__all__ = (
    "Event",
    "BranchProtectionConfigurationEvent",
    "action_types",
    "branch_protection_configuration_action_types",
)
