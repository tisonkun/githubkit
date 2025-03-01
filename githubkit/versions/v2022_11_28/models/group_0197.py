"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class CodeScanningDefaultSetupUpdate(GitHubModel):
    """CodeScanningDefaultSetupUpdate

    Configuration for code scanning default setup.
    """

    state: Missing[Literal["configured", "not-configured"]] = Field(
        default=UNSET, description="The desired state of code scanning default setup."
    )
    query_suite: Missing[Literal["default", "extended"]] = Field(
        default=UNSET, description="CodeQL query suite to be used."
    )
    languages: Missing[
        List[
            Literal[
                "c-cpp",
                "csharp",
                "go",
                "java-kotlin",
                "javascript-typescript",
                "python",
                "ruby",
                "swift",
            ]
        ]
    ] = Field(default=UNSET, description="CodeQL languages to be analyzed.")


model_rebuild(CodeScanningDefaultSetupUpdate)

__all__ = ("CodeScanningDefaultSetupUpdate",)
