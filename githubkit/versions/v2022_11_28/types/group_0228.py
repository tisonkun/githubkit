"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0227 import MetadataType


class DependencyType(TypedDict):
    """Dependency"""

    package_url: NotRequired[str]
    metadata: NotRequired[MetadataType]
    relationship: NotRequired[Literal["direct", "indirect"]]
    scope: NotRequired[Literal["runtime", "development"]]
    dependencies: NotRequired[List[str]]


__all__ = ("DependencyType",)
