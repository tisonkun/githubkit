"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0016 import LicenseSimpleType


class PullRequestPropBasePropRepoType(TypedDict):
    """PullRequestPropBasePropRepo"""

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: Union[str, None]
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    node_id: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    notifications_url: str
    owner: PullRequestPropBasePropRepoPropOwnerType
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str
    clone_url: str
    default_branch: str
    forks: int
    forks_count: int
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_discussions: bool
    homepage: Union[str, None]
    language: Union[str, None]
    master_branch: NotRequired[str]
    archived: bool
    disabled: bool
    visibility: NotRequired[str]
    mirror_url: Union[str, None]
    open_issues: int
    open_issues_count: int
    permissions: NotRequired[PullRequestPropBasePropRepoPropPermissionsType]
    temp_clone_token: NotRequired[Union[str, None]]
    allow_merge_commit: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    license_: Union[None, LicenseSimpleType]
    pushed_at: datetime
    size: int
    ssh_url: str
    stargazers_count: int
    svn_url: str
    topics: NotRequired[List[str]]
    watchers: int
    watchers_count: int
    created_at: datetime
    updated_at: datetime
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]


class PullRequestPropBasePropRepoPropOwnerType(TypedDict):
    """PullRequestPropBasePropRepoPropOwner"""

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: Union[str, None]
    html_url: str
    id: int
    node_id: str
    login: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str


class PullRequestPropBasePropRepoPropPermissionsType(TypedDict):
    """PullRequestPropBasePropRepoPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    push: bool
    triage: NotRequired[bool]
    pull: bool


__all__ = (
    "PullRequestPropBasePropRepoType",
    "PullRequestPropBasePropRepoPropOwnerType",
    "PullRequestPropBasePropRepoPropPermissionsType",
)
