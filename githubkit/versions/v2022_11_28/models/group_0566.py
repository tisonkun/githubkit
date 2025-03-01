"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0567 import (
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropPlan,
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropAccount,
)


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0(
    GitHubModel
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropAccount = (Field())
    billing_cycle: str = Field()
    free_trial_ends_on: None = Field()
    next_billing_date: Missing[Union[str, None]] = Field(default=UNSET)
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropPlan = (Field())
    unit_count: int = Field()


model_rebuild(
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0
)

__all__ = (
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0",
)
