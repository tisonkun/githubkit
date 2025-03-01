"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBasePropRepoType",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType",
    "WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadPropRepoType",
)
