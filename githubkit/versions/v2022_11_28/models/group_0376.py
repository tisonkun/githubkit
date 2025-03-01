"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhookCheckRunCreatedFormEncoded(GitHubModel):
    """Check Run Created Event

    The check_run.created webhook encoded with URL encoding
    """

    payload: str = Field(
        description="A URL-encoded string of the check_run.created JSON payload. The decoded payload is a JSON object."
    )


model_rebuild(WebhookCheckRunCreatedFormEncoded)

__all__ = ("WebhookCheckRunCreatedFormEncoded",)
