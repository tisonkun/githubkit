"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class DependencyGraphSpdxSbom(GitHubModel):
    """Dependency Graph SPDX SBOM

    A schema for the SPDX JSON format returned by the Dependency Graph.
    """

    sbom: DependencyGraphSpdxSbomPropSbom = Field()


class DependencyGraphSpdxSbomPropSbom(GitHubModel):
    """DependencyGraphSpdxSbomPropSbom"""

    spdxid: str = Field(
        alias="SPDXID", description="The SPDX identifier for the SPDX document."
    )
    spdx_version: str = Field(
        alias="spdxVersion",
        description="The version of the SPDX specification that this document conforms to.",
    )
    creation_info: DependencyGraphSpdxSbomPropSbomPropCreationInfo = Field(
        alias="creationInfo"
    )
    name: str = Field(description="The name of the SPDX document.")
    data_license: str = Field(
        alias="dataLicense",
        description="The license under which the SPDX document is licensed.",
    )
    document_describes: List[str] = Field(
        alias="documentDescribes",
        description="The name of the repository that the SPDX document describes.",
    )
    document_namespace: str = Field(
        alias="documentNamespace", description="The namespace for the SPDX document."
    )
    packages: List[DependencyGraphSpdxSbomPropSbomPropPackagesItems] = Field()


class DependencyGraphSpdxSbomPropSbomPropCreationInfo(GitHubModel):
    """DependencyGraphSpdxSbomPropSbomPropCreationInfo"""

    created: str = Field(description="The date and time the SPDX document was created.")
    creators: List[str] = Field(
        description="The tools that were used to generate the SPDX document."
    )


class DependencyGraphSpdxSbomPropSbomPropPackagesItems(GitHubModel):
    """DependencyGraphSpdxSbomPropSbomPropPackagesItems"""

    spdxid: Missing[str] = Field(
        default=UNSET,
        alias="SPDXID",
        description="A unique SPDX identifier for the package.",
    )
    name: Missing[str] = Field(default=UNSET, description="The name of the package.")
    version_info: Missing[str] = Field(
        default=UNSET,
        alias="versionInfo",
        description="The version of the package. If the package does not have an exact version specified,\na version range is given.",
    )
    download_location: Missing[str] = Field(
        default=UNSET,
        alias="downloadLocation",
        description="The location where the package can be downloaded,\nor NOASSERTION if this has not been determined.",
    )
    files_analyzed: Missing[bool] = Field(
        default=UNSET,
        alias="filesAnalyzed",
        description="Whether the package's file content has been subjected to\nanalysis during the creation of the SPDX document.",
    )
    license_concluded: Missing[str] = Field(
        default=UNSET,
        alias="licenseConcluded",
        description="The license of the package as determined while creating the SPDX document.",
    )
    license_declared: Missing[str] = Field(
        default=UNSET,
        alias="licenseDeclared",
        description="The license of the package as declared by its author, or NOASSERTION if this information\nwas not available when the SPDX document was created.",
    )
    supplier: Missing[str] = Field(
        default=UNSET,
        description="The distribution source of this package, or NOASSERTION if this was not determined.",
    )
    external_refs: Missing[
        List[DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItems]
    ] = Field(default=UNSET, alias="externalRefs")


class DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItems(
    GitHubModel
):
    """DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItems"""

    reference_category: str = Field(
        alias="referenceCategory",
        description="The category of reference to an external resource this reference refers to.",
    )
    reference_locator: str = Field(
        alias="referenceLocator",
        description="A locator for the particular external resource this reference refers to.",
    )
    reference_type: str = Field(
        alias="referenceType",
        description="The category of reference to an external resource this reference refers to.",
    )


model_rebuild(DependencyGraphSpdxSbom)
model_rebuild(DependencyGraphSpdxSbomPropSbom)
model_rebuild(DependencyGraphSpdxSbomPropSbomPropCreationInfo)
model_rebuild(DependencyGraphSpdxSbomPropSbomPropPackagesItems)
model_rebuild(DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItems)

__all__ = (
    "DependencyGraphSpdxSbom",
    "DependencyGraphSpdxSbomPropSbom",
    "DependencyGraphSpdxSbomPropSbomPropCreationInfo",
    "DependencyGraphSpdxSbomPropSbomPropPackagesItems",
    "DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItems",
)
