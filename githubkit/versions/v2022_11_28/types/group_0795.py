"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0166 import DeploymentType
from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookWorkflowJobQueuedType(TypedDict):
    """workflow_job queued event"""

    action: Literal["queued"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType
    workflow_job: WebhookWorkflowJobQueuedPropWorkflowJobType
    deployment: NotRequired[DeploymentType]


class WebhookWorkflowJobQueuedPropWorkflowJobType(TypedDict):
    """WebhookWorkflowJobQueuedPropWorkflowJob"""

    check_run_url: str
    completed_at: Union[str, None]
    conclusion: Union[str, None]
    created_at: str
    head_sha: str
    html_url: str
    id: int
    labels: List[str]
    name: str
    node_id: str
    run_attempt: int
    run_id: int
    run_url: str
    runner_group_id: Union[int, None]
    runner_group_name: Union[str, None]
    runner_id: Union[int, None]
    runner_name: Union[str, None]
    started_at: datetime
    status: Literal["queued", "in_progress", "completed", "waiting"]
    head_branch: Union[str, None]
    workflow_name: Union[str, None]
    steps: List[WebhookWorkflowJobQueuedPropWorkflowJobPropStepsItemsType]
    url: str


class WebhookWorkflowJobQueuedPropWorkflowJobPropStepsItemsType(TypedDict):
    """Workflow Step"""

    completed_at: Union[str, None]
    conclusion: Union[None, Literal["failure", "skipped", "success", "cancelled"]]
    name: str
    number: int
    started_at: Union[str, None]
    status: Literal["completed", "in_progress", "queued", "pending"]


__all__ = (
    "WebhookWorkflowJobQueuedType",
    "WebhookWorkflowJobQueuedPropWorkflowJobType",
    "WebhookWorkflowJobQueuedPropWorkflowJobPropStepsItemsType",
)
