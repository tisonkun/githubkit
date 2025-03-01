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


class ClassroomAssignmentGrade(GitHubModel):
    """Classroom Assignment Grade

    Grade for a student or groups GitHub Classroom assignment
    """

    assignment_name: str = Field(description="Name of the assignment")
    assignment_url: str = Field(description="URL of the assignment")
    starter_code_url: str = Field(
        description="URL of the starter code for the assignment"
    )
    github_username: str = Field(description="GitHub username of the student")
    roster_identifier: str = Field(description="Roster identifier of the student")
    student_repository_name: str = Field(
        description="Name of the student's assignment repository"
    )
    student_repository_url: str = Field(
        description="URL of the student's assignment repository"
    )
    submission_timestamp: str = Field(
        description="Timestamp of the student's assignment submission"
    )
    points_awarded: int = Field(description="Number of points awarded to the student")
    points_available: int = Field(
        description="Number of points available for the assignment"
    )
    group_name: Missing[str] = Field(
        default=UNSET,
        description="If a group assignment, name of the group the student is in",
    )


model_rebuild(ClassroomAssignmentGrade)

__all__ = ("ClassroomAssignmentGrade",)
