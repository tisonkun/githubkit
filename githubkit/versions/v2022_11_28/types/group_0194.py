"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict


class CodeScanningAnalysisDeletionType(TypedDict):
    """Analysis deletion

    Successful deletion of a code scanning analysis
    """

    next_analysis_url: Union[str, None]
    confirm_delete_url: Union[str, None]


__all__ = ("CodeScanningAnalysisDeletionType",)
