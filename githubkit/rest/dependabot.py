"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api description.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .types import (
    OrgsOrgDependabotSecretsSecretNamePutBodyType,
    ReposOwnerRepoDependabotSecretsSecretNamePutBodyType,
    ReposOwnerRepoDependabotAlertsAlertNumberPatchBodyType,
    OrgsOrgDependabotSecretsSecretNameRepositoriesPutBodyType,
)
from .models import (
    BasicError,
    EmptyObject,
    DependabotAlert,
    DependabotSecret,
    DependabotPublicKey,
    ValidationErrorSimple,
    OrganizationDependabotSecret,
    DependabotAlertWithRepository,
    OrgsOrgDependabotSecretsGetResponse200,
    OrgsOrgDependabotSecretsSecretNamePutBody,
    ReposOwnerRepoDependabotSecretsGetResponse200,
    ReposOwnerRepoDependabotSecretsSecretNamePutBody,
    ReposOwnerRepoDependabotAlertsAlertNumberPatchBody,
    OrgsOrgDependabotSecretsSecretNameRepositoriesPutBody,
    OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class DependabotClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Union[Unset, str] = UNSET,
        severity: Union[Unset, str] = UNSET,
        ecosystem: Union[Unset, str] = UNSET,
        package: Union[Unset, str] = UNSET,
        scope: Union[Unset, Literal["development", "runtime"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        first: Union[Unset, int] = 30,
        last: Union[Unset, int] = UNSET,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[List[DependabotAlertWithRepository]]":
        url = f"/enterprises/{enterprise}/dependabot/alerts"

        params = {
            "state": state,
            "severity": severity,
            "ecosystem": ecosystem,
            "package": package,
            "scope": scope,
            "sort": sort,
            "direction": direction,
            "before": before,
            "after": after,
            "first": first,
            "last": last,
            "per_page": per_page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[DependabotAlertWithRepository],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    async def async_list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Union[Unset, str] = UNSET,
        severity: Union[Unset, str] = UNSET,
        ecosystem: Union[Unset, str] = UNSET,
        package: Union[Unset, str] = UNSET,
        scope: Union[Unset, Literal["development", "runtime"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        first: Union[Unset, int] = 30,
        last: Union[Unset, int] = UNSET,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[List[DependabotAlertWithRepository]]":
        url = f"/enterprises/{enterprise}/dependabot/alerts"

        params = {
            "state": state,
            "severity": severity,
            "ecosystem": ecosystem,
            "package": package,
            "scope": scope,
            "sort": sort,
            "direction": direction,
            "before": before,
            "after": after,
            "first": first,
            "last": last,
            "per_page": per_page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[DependabotAlertWithRepository],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    def list_alerts_for_org(
        self,
        org: str,
        state: Union[Unset, str] = UNSET,
        severity: Union[Unset, str] = UNSET,
        ecosystem: Union[Unset, str] = UNSET,
        package: Union[Unset, str] = UNSET,
        scope: Union[Unset, Literal["development", "runtime"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        first: Union[Unset, int] = 30,
        last: Union[Unset, int] = UNSET,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[List[DependabotAlertWithRepository]]":
        url = f"/orgs/{org}/dependabot/alerts"

        params = {
            "state": state,
            "severity": severity,
            "ecosystem": ecosystem,
            "package": package,
            "scope": scope,
            "sort": sort,
            "direction": direction,
            "before": before,
            "after": after,
            "first": first,
            "last": last,
            "per_page": per_page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[DependabotAlertWithRepository],
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    async def async_list_alerts_for_org(
        self,
        org: str,
        state: Union[Unset, str] = UNSET,
        severity: Union[Unset, str] = UNSET,
        ecosystem: Union[Unset, str] = UNSET,
        package: Union[Unset, str] = UNSET,
        scope: Union[Unset, Literal["development", "runtime"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        first: Union[Unset, int] = 30,
        last: Union[Unset, int] = UNSET,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[List[DependabotAlertWithRepository]]":
        url = f"/orgs/{org}/dependabot/alerts"

        params = {
            "state": state,
            "severity": severity,
            "ecosystem": ecosystem,
            "package": package,
            "scope": scope,
            "sort": sort,
            "direction": direction,
            "before": before,
            "after": after,
            "first": first,
            "last": last,
            "per_page": per_page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[DependabotAlertWithRepository],
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    def list_org_secrets(
        self,
        org: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[OrgsOrgDependabotSecretsGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsGetResponse200,
        )

    async def async_list_org_secrets(
        self,
        org: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[OrgsOrgDependabotSecretsGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsGetResponse200,
        )

    def get_org_public_key(
        self,
        org: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/orgs/{org}/dependabot/secrets/public-key"

        return self._github.request(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    async def async_get_org_public_key(
        self,
        org: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/orgs/{org}/dependabot/secrets/public-key"

        return await self._github.arequest(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    def get_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response[OrganizationDependabotSecret]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "GET",
            url,
            response_model=OrganizationDependabotSecret,
        )

    async def async_get_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response[OrganizationDependabotSecret]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=OrganizationDependabotSecret,
        )

    @overload
    def create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: OrgsOrgDependabotSecretsSecretNamePutBodyType,
    ) -> "Response[EmptyObject]":
        ...

    @overload
    def create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Unset = UNSET,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Union[Unset, List[str]] = UNSET,
    ) -> "Response[EmptyObject]":
        ...

    def create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Union[Unset, OrgsOrgDependabotSecretsSecretNamePutBodyType] = UNSET,
        **kwargs,
    ) -> "Response[EmptyObject]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgDependabotSecretsSecretNamePutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    @overload
    async def async_create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: OrgsOrgDependabotSecretsSecretNamePutBodyType,
    ) -> "Response[EmptyObject]":
        ...

    @overload
    async def async_create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Unset = UNSET,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Union[Unset, List[str]] = UNSET,
    ) -> "Response[EmptyObject]":
        ...

    async def async_create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Union[Unset, OrgsOrgDependabotSecretsSecretNamePutBodyType] = UNSET,
        **kwargs,
    ) -> "Response[EmptyObject]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgDependabotSecretsSecretNamePutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    def delete_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        params = {
            "page": page,
            "per_page": per_page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200,
        )

    async def async_list_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        params = {
            "page": page,
            "per_page": per_page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200,
        )

    @overload
    def set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: OrgsOrgDependabotSecretsSecretNameRepositoriesPutBodyType,
    ) -> "Response":
        ...

    @overload
    def set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Unset = UNSET,
        selected_repository_ids: List[int],
    ) -> "Response":
        ...

    def set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Union[
            Unset, OrgsOrgDependabotSecretsSecretNameRepositoriesPutBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgDependabotSecretsSecretNameRepositoriesPutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
        )

    @overload
    async def async_set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: OrgsOrgDependabotSecretsSecretNameRepositoriesPutBodyType,
    ) -> "Response":
        ...

    @overload
    async def async_set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Unset = UNSET,
        selected_repository_ids: List[int],
    ) -> "Response":
        ...

    async def async_set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        data: Union[
            Unset, OrgsOrgDependabotSecretsSecretNameRepositoriesPutBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OrgsOrgDependabotSecretsSecretNameRepositoriesPutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
        )

    def add_selected_repo_to_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return self._github.request(
            "PUT",
            url,
            error_models={},
        )

    async def async_add_selected_repo_to_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return await self._github.arequest(
            "PUT",
            url,
            error_models={},
        )

    def remove_selected_repo_from_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return self._github.request(
            "DELETE",
            url,
            error_models={},
        )

    async def async_remove_selected_repo_from_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return await self._github.arequest(
            "DELETE",
            url,
            error_models={},
        )

    def list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Union[Unset, str] = UNSET,
        severity: Union[Unset, str] = UNSET,
        ecosystem: Union[Unset, str] = UNSET,
        package: Union[Unset, str] = UNSET,
        manifest: Union[Unset, str] = UNSET,
        scope: Union[Unset, Literal["development", "runtime"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        first: Union[Unset, int] = 30,
        last: Union[Unset, int] = UNSET,
    ) -> "Response[List[DependabotAlert]]":
        url = f"/repos/{owner}/{repo}/dependabot/alerts"

        params = {
            "state": state,
            "severity": severity,
            "ecosystem": ecosystem,
            "package": package,
            "manifest": manifest,
            "scope": scope,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "first": first,
            "last": last,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[DependabotAlert],
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    async def async_list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Union[Unset, str] = UNSET,
        severity: Union[Unset, str] = UNSET,
        ecosystem: Union[Unset, str] = UNSET,
        package: Union[Unset, str] = UNSET,
        manifest: Union[Unset, str] = UNSET,
        scope: Union[Unset, Literal["development", "runtime"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        first: Union[Unset, int] = 30,
        last: Union[Unset, int] = UNSET,
    ) -> "Response[List[DependabotAlert]]":
        url = f"/repos/{owner}/{repo}/dependabot/alerts"

        params = {
            "state": state,
            "severity": severity,
            "ecosystem": ecosystem,
            "package": package,
            "manifest": manifest,
            "scope": scope,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "first": first,
            "last": last,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[DependabotAlert],
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    def get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[DependabotAlert]":
        url = f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}"

        return self._github.request(
            "GET",
            url,
            response_model=DependabotAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[DependabotAlert]":
        url = f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=DependabotAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: ReposOwnerRepoDependabotAlertsAlertNumberPatchBodyType,
    ) -> "Response[DependabotAlert]":
        ...

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Unset = UNSET,
        state: Literal["dismissed", "open"],
        dismissed_reason: Union[
            Unset,
            Literal[
                "fix_started",
                "inaccurate",
                "no_bandwidth",
                "not_used",
                "tolerable_risk",
            ],
        ] = UNSET,
        dismissed_comment: Union[Unset, str] = UNSET,
    ) -> "Response[DependabotAlert]":
        ...

    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Union[
            Unset, ReposOwnerRepoDependabotAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[DependabotAlert]":
        url = f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoDependabotAlertsAlertNumberPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=DependabotAlert,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: ReposOwnerRepoDependabotAlertsAlertNumberPatchBodyType,
    ) -> "Response[DependabotAlert]":
        ...

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Unset = UNSET,
        state: Literal["dismissed", "open"],
        dismissed_reason: Union[
            Unset,
            Literal[
                "fix_started",
                "inaccurate",
                "no_bandwidth",
                "not_used",
                "tolerable_risk",
            ],
        ] = UNSET,
        dismissed_comment: Union[Unset, str] = UNSET,
    ) -> "Response[DependabotAlert]":
        ...

    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Union[
            Unset, ReposOwnerRepoDependabotAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[DependabotAlert]":
        url = f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoDependabotAlertsAlertNumberPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=DependabotAlert,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
                "422": ValidationErrorSimple,
            },
        )

    def list_repo_secrets(
        self,
        owner: str,
        repo: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[ReposOwnerRepoDependabotSecretsGetResponse200]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ReposOwnerRepoDependabotSecretsGetResponse200,
        )

    async def async_list_repo_secrets(
        self,
        owner: str,
        repo: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[ReposOwnerRepoDependabotSecretsGetResponse200]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ReposOwnerRepoDependabotSecretsGetResponse200,
        )

    def get_repo_public_key(
        self,
        owner: str,
        repo: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/public-key"

        return self._github.request(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    async def async_get_repo_public_key(
        self,
        owner: str,
        repo: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/public-key"

        return await self._github.arequest(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    def get_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response[DependabotSecret]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "GET",
            url,
            response_model=DependabotSecret,
        )

    async def async_get_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response[DependabotSecret]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=DependabotSecret,
        )

    @overload
    def create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        data: ReposOwnerRepoDependabotSecretsSecretNamePutBodyType,
    ) -> "Response[EmptyObject]":
        ...

    @overload
    def create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        data: Unset = UNSET,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
    ) -> "Response[EmptyObject]":
        ...

    def create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        data: Union[
            Unset, ReposOwnerRepoDependabotSecretsSecretNamePutBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoDependabotSecretsSecretNamePutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    @overload
    async def async_create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        data: ReposOwnerRepoDependabotSecretsSecretNamePutBodyType,
    ) -> "Response[EmptyObject]":
        ...

    @overload
    async def async_create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        data: Unset = UNSET,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
    ) -> "Response[EmptyObject]":
        ...

    async def async_create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        data: Union[
            Unset, ReposOwnerRepoDependabotSecretsSecretNamePutBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoDependabotSecretsSecretNamePutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    def delete_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "DELETE",
            url,
        )
