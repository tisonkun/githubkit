"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class CheckAnnotation(GitHubModel):
    """Check Annotation

    Check Annotation
    """

    path: str = Field()
    start_line: int = Field()
    end_line: int = Field()
    start_column: Union[int, None] = Field()
    end_column: Union[int, None] = Field()
    annotation_level: Union[str, None] = Field()
    title: Union[str, None] = Field()
    message: Union[str, None] = Field()
    raw_details: Union[str, None] = Field()
    blob_href: str = Field()


model_rebuild(CheckAnnotation)

__all__ = ("CheckAnnotation",)
