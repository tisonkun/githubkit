"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType
from .group_0798 import WebhookWorkflowRunCompletedPropWorkflowRunType


class WebhookWorkflowRunCompletedType(TypedDict):
    """workflow_run completed event"""

    action: Literal["completed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType
    workflow: Union[WebhookWorkflowRunCompletedPropWorkflowType, None]
    workflow_run: WebhookWorkflowRunCompletedPropWorkflowRunType


class WebhookWorkflowRunCompletedPropWorkflowType(TypedDict):
    """Workflow"""

    badge_url: str
    created_at: datetime
    html_url: str
    id: int
    name: str
    node_id: str
    path: str
    state: str
    updated_at: datetime
    url: str


__all__ = (
    "WebhookWorkflowRunCompletedType",
    "WebhookWorkflowRunCompletedPropWorkflowType",
)
