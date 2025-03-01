"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class PorterLargeFileType(TypedDict):
    """Porter Large File

    Porter Large File
    """

    ref_name: str
    path: str
    oid: str
    size: int


__all__ = ("PorterLargeFileType",)
