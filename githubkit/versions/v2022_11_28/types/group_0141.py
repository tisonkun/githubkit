"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class ReactionType(TypedDict):
    """Reaction

    Reactions to conversations provide a way to help people express their feelings
    more simply and effectively.
    """

    id: int
    node_id: str
    user: Union[None, SimpleUserType]
    content: Literal[
        "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
    ]
    created_at: datetime


__all__ = ("ReactionType",)
