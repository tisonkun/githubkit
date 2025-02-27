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


class WebhookPullRequestReviewCommentEditedType(TypedDict):
    """pull_request_review_comment edited event"""

    action: Literal["edited"]
    changes: WebhookPullRequestReviewCommentEditedPropChangesType
    comment: WebhookPullRequestReviewCommentEditedPropCommentType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestReviewCommentEditedPropPullRequestType
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookPullRequestReviewCommentEditedPropChangesType(TypedDict):
    """WebhookPullRequestReviewCommentEditedPropChanges

    The changes to the comment.
    """

    body: NotRequired[WebhookPullRequestReviewCommentEditedPropChangesPropBodyType]


class WebhookPullRequestReviewCommentEditedPropChangesPropBodyType(TypedDict):
    """WebhookPullRequestReviewCommentEditedPropChangesPropBody"""

    from_: str


class WebhookPullRequestReviewCommentEditedPropCommentType(TypedDict):
    """Pull Request Review Comment

    The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-
    for-a-pull-request) itself.
    """

    links: WebhookPullRequestReviewCommentEditedPropCommentPropLinksType
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: str
    commit_id: str
    created_at: datetime
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: NotRequired[int]
    line: Union[int, None]
    node_id: str
    original_commit_id: str
    original_line: int
    original_position: int
    original_start_line: Union[int, None]
    path: str
    position: Union[int, None]
    pull_request_review_id: Union[int, None]
    pull_request_url: str
    reactions: WebhookPullRequestReviewCommentEditedPropCommentPropReactionsType
    side: Literal["LEFT", "RIGHT"]
    start_line: Union[int, None]
    start_side: Union[None, Literal["LEFT", "RIGHT"]]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: datetime
    url: str
    user: Union[WebhookPullRequestReviewCommentEditedPropCommentPropUserType, None]


class WebhookPullRequestReviewCommentEditedPropCommentPropReactionsType(TypedDict):
    """Reactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookPullRequestReviewCommentEditedPropCommentPropUserType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropCommentPropLinksType(TypedDict):
    """WebhookPullRequestReviewCommentEditedPropCommentPropLinks"""

    html: WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropHtmlType
    pull_request: (
        WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropPullRequestType
    )
    self_: WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropSelfType


class WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropHtmlType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropPullRequestType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropSelfType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestType(TypedDict):
    """WebhookPullRequestReviewCommentEditedPropPullRequest"""

    links: WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropAssigneeType, None
    ]
    assignees: List[
        Union[
            WebhookPullRequestReviewCommentEditedPropPullRequestPropAssigneesItemsType,
            None,
        ]
    ]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    auto_merge: NotRequired[
        Union[
            WebhookPullRequestReviewCommentEditedPropPullRequestPropAutoMergeType, None
        ]
    ]
    base: WebhookPullRequestReviewCommentEditedPropPullRequestPropBaseType
    body: Union[str, None]
    closed_at: Union[str, None]
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: NotRequired[bool]
    head: WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: List[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropLabelsItemsType
    ]
    locked: bool
    merge_commit_sha: Union[str, None]
    merged_at: Union[str, None]
    milestone: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropMilestoneType, None
    ]
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: List[
        Union[
            WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: List[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Union[WebhookPullRequestReviewCommentEditedPropPullRequestPropUserType, None]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropAssigneeType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropAssigneesItemsType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropAutoMergeType(TypedDict):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropAutoMergePropEnabledByType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLabelsItemsType(
    TypedDict
):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropMilestonePropCreatorType,
        None,
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropMilestonePropCreatorType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof0Type(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropUserType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksType(TypedDict):
    """WebhookPullRequestReviewCommentEditedPropPullRequestPropLinks"""

    comments: (
        WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropCommentsType
    )
    commits: (
        WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropCommitsType
    )
    html: WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropHtmlType
    issue: WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropIssueType
    review_comment: WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropReviewCommentType
    review_comments: WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropReviewCommentsType
    self_: WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropSelfType
    statuses: (
        WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropStatusesType
    )


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropCommitsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropIssueType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropStatusesType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropBaseType(TypedDict):
    """WebhookPullRequestReviewCommentEditedPropPullRequestPropBase"""

    label: str
    ref: str
    repo: WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoType
    sha: str
    user: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropUserType, None
    ]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropUserType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropOwnerType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropPermissi
    ons
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadType(TypedDict):
    """WebhookPullRequestReviewCommentEditedPropPullRequestPropHead"""

    label: str
    ref: str
    repo: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoType, None
    ]
    sha: str
    user: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropUserType, None
    ]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropOwnerType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropPermissi
    ons
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropUserType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof1Type(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsO
    neof1PropParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedTeamsItemsType(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedTeamsItemsPropP
    arent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


__all__ = (
    "WebhookPullRequestReviewCommentEditedType",
    "WebhookPullRequestReviewCommentEditedPropChangesType",
    "WebhookPullRequestReviewCommentEditedPropChangesPropBodyType",
    "WebhookPullRequestReviewCommentEditedPropCommentType",
    "WebhookPullRequestReviewCommentEditedPropCommentPropReactionsType",
    "WebhookPullRequestReviewCommentEditedPropCommentPropUserType",
    "WebhookPullRequestReviewCommentEditedPropCommentPropLinksType",
    "WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropHtmlType",
    "WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropPullRequestType",
    "WebhookPullRequestReviewCommentEditedPropCommentPropLinksPropSelfType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropAssigneeType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropAutoMergeType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLabelsItemsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropMilestoneType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropUserType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropBaseType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropUserType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropHeadPropUserType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestReviewCommentEditedPropPullRequestPropRequestedTeamsItemsPropParentType",
)
