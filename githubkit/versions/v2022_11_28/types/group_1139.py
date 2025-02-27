"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


class UserSocialAccountsDeleteBodyType(TypedDict):
    """UserSocialAccountsDeleteBody

    Examples:
        {'account_urls': ['https://www.linkedin.com/company/github/',
    'https://twitter.com/github']}
    """

    account_urls: List[str]


__all__ = ("UserSocialAccountsDeleteBodyType",)
