"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0130 import RepositoryRulesetType
from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType
from .group_0728 import WebhookRepositoryRulesetEditedPropChangesType


class WebhookRepositoryRulesetEditedType(TypedDict):
    """repository ruleset edited event"""

    action: Literal["edited"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    repository_ruleset: RepositoryRulesetType
    changes: NotRequired[WebhookRepositoryRulesetEditedPropChangesType]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookRepositoryRulesetEditedType",)
