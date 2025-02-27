"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class CodeScanningDefaultSetupUpdateResponse(GitHubModel):
    """CodeScanningDefaultSetupUpdateResponse

    You can use `run_url` to track the status of the run. This includes a property
    status and conclusion.
    You should not rely on this always being an actions workflow run object.
    """

    run_id: Missing[int] = Field(
        default=UNSET, description="ID of the corresponding run."
    )
    run_url: Missing[str] = Field(
        default=UNSET, description="URL of the corresponding run."
    )


model_rebuild(CodeScanningDefaultSetupUpdateResponse)

__all__ = ("CodeScanningDefaultSetupUpdateResponse",)
