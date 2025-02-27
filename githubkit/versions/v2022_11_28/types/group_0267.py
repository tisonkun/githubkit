"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict


class LabelType(TypedDict):
    """Label

    Color-coded labels help you categorize and filter your issues (just like labels
    in Gmail).
    """

    id: int
    node_id: str
    url: str
    name: str
    description: Union[str, None]
    color: str
    default: bool


__all__ = ("LabelType",)
