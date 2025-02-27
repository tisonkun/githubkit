"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: (
        WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBasePropRepo
    ) = Field(title="Repo Ref")
    sha: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead(
    GitHubModel
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: (
        WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadPropRepo
    ) = Field(title="Repo Ref")
    sha: str = Field()


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase
)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBasePropRepo
)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead
)
model_rebuild(
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBasePropRepo",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadPropRepo",
)
