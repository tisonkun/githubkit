"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0270 import TimelineCrossReferencedEventPropSourceType


class TimelineCrossReferencedEventType(TypedDict):
    """Timeline Cross Referenced Event

    Timeline Cross Referenced Event
    """

    event: Literal["cross-referenced"]
    actor: NotRequired[SimpleUserType]
    created_at: datetime
    updated_at: datetime
    source: TimelineCrossReferencedEventPropSourceType


__all__ = ("TimelineCrossReferencedEventType",)
