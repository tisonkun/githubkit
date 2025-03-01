"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class HookDeliveryItem(GitHubModel):
    """Simple webhook delivery

    Delivery made by a webhook, without request and response information.
    """

    id: int = Field(description="Unique identifier of the webhook delivery.")
    guid: str = Field(
        description="Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event)."
    )
    delivered_at: datetime = Field(
        description="Time when the webhook delivery occurred."
    )
    redelivery: bool = Field(
        description="Whether the webhook delivery is a redelivery."
    )
    duration: float = Field(description="Time spent delivering.")
    status: str = Field(
        description="Describes the response returned after attempting the delivery."
    )
    status_code: int = Field(description="Status code received when delivery was made.")
    event: str = Field(description="The event that triggered the delivery.")
    action: Union[str, None] = Field(
        description="The type of activity for the event that triggered the delivery."
    )
    installation_id: Union[int, None] = Field(
        description="The id of the GitHub App installation associated with this event."
    )
    repository_id: Union[int, None] = Field(
        description="The id of the repository associated with this event."
    )


model_rebuild(HookDeliveryItem)

__all__ = ("HookDeliveryItem",)
