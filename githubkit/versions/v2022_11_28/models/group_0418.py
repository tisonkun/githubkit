"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0355 import EnterpriseWebhooks
from .group_0356 import SimpleInstallation
from .group_0358 import RepositoryWebhooks
from .group_0359 import SimpleUserWebhooks
from .group_0357 import OrganizationSimpleWebhooks


class WebhookDiscussionCreated(GitHubModel):
    """discussion created event"""

    action: Literal["created"] = Field()
    discussion: WebhookDiscussionCreatedPropDiscussion = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookDiscussionCreatedPropDiscussion(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussion"""

    active_lock_reason: Union[None, None] = Field()
    answer_chosen_at: Union[None, None] = Field()
    answer_chosen_by: Union[None, None] = Field()
    answer_html_url: Union[Union[str, None], None] = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: Union[Union[str, None], None] = Field()
    category: WebhookDiscussionCreatedPropDiscussionMergedCategory = Field()
    comments: int = Field()
    created_at: datetime = Field()
    html_url: str = Field()
    id: int = Field()
    locked: Literal[False] = Field()
    node_id: str = Field()
    number: int = Field()
    reactions: Missing[WebhookDiscussionCreatedPropDiscussionMergedReactions] = Field(
        default=UNSET
    )
    repository_url: str = Field()
    state: Literal["open", "converting", "transferring"] = Field()
    timeline_url: Missing[str] = Field(default=UNSET)
    title: str = Field()
    updated_at: datetime = Field()
    user: WebhookDiscussionCreatedPropDiscussionMergedUser = Field()


class WebhookDiscussionCreatedPropDiscussionMergedCategory(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussionMergedCategory"""

    created_at: datetime = Field()
    description: str = Field()
    emoji: str = Field()
    id: int = Field()
    is_answerable: bool = Field()
    name: str = Field()
    node_id: Missing[str] = Field(default=UNSET)
    repository_id: int = Field()
    slug: str = Field()
    updated_at: str = Field()


class WebhookDiscussionCreatedPropDiscussionMergedReactions(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussionMergedReactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhookDiscussionCreatedPropDiscussionMergedUser(GitHubModel):
    """WebhookDiscussionCreatedPropDiscussionMergedUser"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookDiscussionCreated)
model_rebuild(WebhookDiscussionCreatedPropDiscussion)
model_rebuild(WebhookDiscussionCreatedPropDiscussionMergedCategory)
model_rebuild(WebhookDiscussionCreatedPropDiscussionMergedReactions)
model_rebuild(WebhookDiscussionCreatedPropDiscussionMergedUser)

__all__ = (
    "WebhookDiscussionCreated",
    "WebhookDiscussionCreatedPropDiscussion",
    "WebhookDiscussionCreatedPropDiscussionMergedCategory",
    "WebhookDiscussionCreatedPropDiscussionMergedReactions",
    "WebhookDiscussionCreatedPropDiscussionMergedUser",
)
