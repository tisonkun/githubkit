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

from ..models import WebhookMergeGroupDestroyed, WebhookMergeGroupChecksRequested

Event: TypeAlias = Annotated[
    Union[
        WebhookMergeGroupChecksRequested,
        WebhookMergeGroupDestroyed,
    ],
    Field(discriminator="action"),
]

MergeGroupEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "checks_requested": WebhookMergeGroupChecksRequested,
    "destroyed": WebhookMergeGroupDestroyed,
}

merge_group_action_types = action_types

__all__ = ("Event", "MergeGroupEvent", "action_types", "merge_group_action_types")
