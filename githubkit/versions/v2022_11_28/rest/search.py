"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from weakref import ref
from typing_extensions import Annotated
from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import Field, BaseModel

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from typing import Literal

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import (
        SearchCodeGetResponse200,
        SearchUsersGetResponse200,
        SearchIssuesGetResponse200,
        SearchLabelsGetResponse200,
        SearchTopicsGetResponse200,
        SearchCommitsGetResponse200,
        SearchRepositoriesGetResponse200,
    )


class SearchClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    def code(
        self,
        q: str,
        sort: Missing[Literal["indexed"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchCodeGetResponse200]:
        from ..models import (
            BasicError,
            ValidationError,
            SearchCodeGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/code"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCodeGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    async def async_code(
        self,
        q: str,
        sort: Missing[Literal["indexed"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchCodeGetResponse200]:
        from ..models import (
            BasicError,
            ValidationError,
            SearchCodeGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/code"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCodeGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    def commits(
        self,
        q: str,
        sort: Missing[Literal["author-date", "committer-date"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchCommitsGetResponse200]:
        from ..models import SearchCommitsGetResponse200

        url = "/search/commits"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCommitsGetResponse200,
        )

    async def async_commits(
        self,
        q: str,
        sort: Missing[Literal["author-date", "committer-date"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchCommitsGetResponse200]:
        from ..models import SearchCommitsGetResponse200

        url = "/search/commits"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchCommitsGetResponse200,
        )

    def issues_and_pull_requests(
        self,
        q: str,
        sort: Missing[
            Literal[
                "comments",
                "reactions",
                "reactions-+1",
                "reactions--1",
                "reactions-smile",
                "reactions-thinking_face",
                "reactions-heart",
                "reactions-tada",
                "interactions",
                "created",
                "updated",
            ]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchIssuesGetResponse200]:
        from ..models import (
            BasicError,
            ValidationError,
            SearchIssuesGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/issues"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchIssuesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    async def async_issues_and_pull_requests(
        self,
        q: str,
        sort: Missing[
            Literal[
                "comments",
                "reactions",
                "reactions-+1",
                "reactions--1",
                "reactions-smile",
                "reactions-thinking_face",
                "reactions-heart",
                "reactions-tada",
                "interactions",
                "created",
                "updated",
            ]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchIssuesGetResponse200]:
        from ..models import (
            BasicError,
            ValidationError,
            SearchIssuesGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/issues"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchIssuesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    def labels(
        self,
        repository_id: int,
        q: str,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchLabelsGetResponse200]:
        from ..models import BasicError, ValidationError, SearchLabelsGetResponse200

        url = "/search/labels"

        params = {
            "repository_id": repository_id,
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchLabelsGetResponse200,
            error_models={
                "404": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    async def async_labels(
        self,
        repository_id: int,
        q: str,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchLabelsGetResponse200]:
        from ..models import BasicError, ValidationError, SearchLabelsGetResponse200

        url = "/search/labels"

        params = {
            "repository_id": repository_id,
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchLabelsGetResponse200,
            error_models={
                "404": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    def repos(
        self,
        q: str,
        sort: Missing[
            Literal["stars", "forks", "help-wanted-issues", "updated"]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchRepositoriesGetResponse200]:
        from ..models import (
            ValidationError,
            SearchRepositoriesGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/repositories"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchRepositoriesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )

    async def async_repos(
        self,
        q: str,
        sort: Missing[
            Literal["stars", "forks", "help-wanted-issues", "updated"]
        ] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchRepositoriesGetResponse200]:
        from ..models import (
            ValidationError,
            SearchRepositoriesGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/repositories"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchRepositoriesGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )

    def topics(
        self,
        q: str,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchTopicsGetResponse200]:
        from ..models import SearchTopicsGetResponse200

        url = "/search/topics"

        params = {
            "q": q,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchTopicsGetResponse200,
        )

    async def async_topics(
        self,
        q: str,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchTopicsGetResponse200]:
        from ..models import SearchTopicsGetResponse200

        url = "/search/topics"

        params = {
            "q": q,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchTopicsGetResponse200,
        )

    def users(
        self,
        q: str,
        sort: Missing[Literal["followers", "repositories", "joined"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchUsersGetResponse200]:
        from ..models import (
            ValidationError,
            SearchUsersGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/users"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchUsersGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )

    async def async_users(
        self,
        q: str,
        sort: Missing[Literal["followers", "repositories", "joined"]] = UNSET,
        order: Missing[Literal["desc", "asc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[SearchUsersGetResponse200]:
        from ..models import (
            ValidationError,
            SearchUsersGetResponse200,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
        )

        url = "/search/users"

        params = {
            "q": q,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=SearchUsersGetResponse200,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
                "422": ValidationError,
            },
        )
