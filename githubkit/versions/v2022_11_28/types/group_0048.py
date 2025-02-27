"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ApiOverviewType(TypedDict):
    """Api Overview

    Api Overview
    """

    verifiable_password_authentication: bool
    ssh_key_fingerprints: NotRequired[ApiOverviewPropSshKeyFingerprintsType]
    ssh_keys: NotRequired[List[str]]
    hooks: NotRequired[List[str]]
    github_enterprise_importer: NotRequired[List[str]]
    web: NotRequired[List[str]]
    api: NotRequired[List[str]]
    git: NotRequired[List[str]]
    packages: NotRequired[List[str]]
    pages: NotRequired[List[str]]
    importer: NotRequired[List[str]]
    actions: NotRequired[List[str]]
    dependabot: NotRequired[List[str]]
    domains: NotRequired[ApiOverviewPropDomainsType]


class ApiOverviewPropSshKeyFingerprintsType(TypedDict):
    """ApiOverviewPropSshKeyFingerprints"""

    sha256_rsa: NotRequired[str]
    sha256_dsa: NotRequired[str]
    sha256_ecdsa: NotRequired[str]
    sha256_ed25519: NotRequired[str]


class ApiOverviewPropDomainsType(TypedDict):
    """ApiOverviewPropDomains"""

    website: NotRequired[List[str]]
    codespaces: NotRequired[List[str]]
    copilot: NotRequired[List[str]]
    packages: NotRequired[List[str]]
    actions: NotRequired[List[str]]


__all__ = (
    "ApiOverviewType",
    "ApiOverviewPropSshKeyFingerprintsType",
    "ApiOverviewPropDomainsType",
)
