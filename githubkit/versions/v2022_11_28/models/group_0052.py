"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ThreadSubscription(GitHubModel):
    """Thread Subscription

    Thread Subscription
    """

    subscribed: bool = Field()
    ignored: bool = Field()
    reason: Union[str, None] = Field()
    created_at: Union[datetime, None] = Field()
    url: str = Field()
    thread_url: Missing[str] = Field(default=UNSET)
    repository_url: Missing[str] = Field(default=UNSET)


model_rebuild(ThreadSubscription)

__all__ = ("ThreadSubscription",)
