"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class WebhookIssuesUnlockedPropIssueAllof0PropPullRequestType(TypedDict):
    """WebhookIssuesUnlockedPropIssueAllof0PropPullRequest"""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[Union[datetime, None]]
    patch_url: NotRequired[str]
    url: NotRequired[str]


__all__ = ("WebhookIssuesUnlockedPropIssueAllof0PropPullRequestType",)
