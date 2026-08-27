---
title: Capella Analytics Management API Reference
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/management-api-reference/pages/index.adoc
  xref: xref:analytics:management-api-reference:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/management-api-reference/index.html)

# Capella Analytics Management API Reference

* Allowed CIDRs (Analytics Cluster)
  * postCreate Allowed CIDR
  * getList Allowed CIDRs
  * getGet Allowed CIDR
  * delDelete Allowed CIDR
* Api Keys
  * postCreate API Key
  * getList API keys
  * getGet API Key
  * delDelete API Key
  * postRotate API Key
* Columnar Analytics Cloud Snapshot Backups & Restore
  * postCreate Cloud Snapshot Backup
  * getList Cloud Snapshot Backups
  * putUpdate Backup Retention
  * delDelete Backup
  * postRestore Backup
  * getList Cloud Snapshot Restores
* Columnar Analytics Cloud Snapshot Backups Schedule
  * putUpsert Backup Schedule
  * getGet Backup Schedule
  * delDelete Backup Schedule
* Columnar Analytics Clusters
  * postCreate new analytics cluster
  * getList project level analytics clusters
  * getList organization level analytics clusters
  * getGet analytics cluster details
  * putUpdate an analytics cluster
  * delDelete analytics cluster
  * postTurn On Analytics Cluster
  * delTurn Off Analytics Cluster
* Columnar Analytics On/Off Schedule
  * postCreate Analytics Cluster On/Off schedule
  * getGet Analytics Cluster On/Off Schedule
  * putUpdate Analytics Cluster On/Off Schedule
  * delDelete Analytics Cluster On/Off Schedule
* Columnar Analytics Private Endpoint Service
  * getGet Columnar Analytics Private Endpoint Service Status
  * postEnable Columnar Analytics Private Endpoint Service
  * delDisable Columnar Analytics Private Endpoint Service
  * postGet Columnar Private Endpoint CLI Command required to setup private endpoint for specific CSP
  * getList Columnar Analytics Private Endpoint Connections
  * postAccept or associate Columnar Analytics Private Endpoint Request
  * postReject or disassociate Columnar Analytics Private Endpoint connection
* Organizations
  * getGet Organization
  * putUpdate Organization Configuration
  * getList Organizations
* Projects
  * postCreate Project
  * getList Project
  * getGet Project
  * putUpdate Project
  * delDelete Project
* Users
  * postCreate User
  * getList Users
  * getGet User
  * patchUpdate User
  * delDelete User

[API docs by Redocly](https://redocly.com/redoc/)

# Couchbase Capella Analytics Management API (4.0)

Download OpenAPI specification:

The Couchbase Capella Analytics Management API provides a set of endpoints for creating and managing Capella Analytics clusters. Users are able to perform operations such as creating Capella Analytics clusters and managing their configurations. This API documentation specifies the endpoints, request and response formats, and authentication requirements for seamless integration with Couchbase Capella.

To access the Management API, you need an API key. To create an initial bootstrap API key you must use the Capella UI. Once you have created an initial bootstrap API key, you can use the Management API to create further API keys. To learn more, see [Get Started with the Capella Analytics Management API](https://docs.couchbase.com/analytics/management-api-guide/management-api-start.html).

For a history of updates to the Management API, see [Capella Analytics Management API Change Log](https://docs.couchbase.com/analytics/management-api-guide/management-api-log.html).

**API Base URL:**

`https://cloudapi.cloud.couchbase.com`

[Back to Capella Analytics Management API Documentation](https://docs.couchbase.com/analytics/management-api-guide/management-api-intro.html)

## [](#tag/Allowed-CIDRs-%28Analytics-Cluster%29)Allowed CIDRs (Analytics Cluster)

Columnar analytics clusters only allow connections from trusted IP addresses. Each analytics cluster has a configurable Allowed IP list that can include up to 75 entries. Each entry can be a single IP address or an IP address space. Any IP address you add to this list can have a user-specified expiration time for temporary access, or be permanent. Capella automatically denies any connection attempts to and from an IP not in the allowed IP list.

## [](#tag/Allowed-CIDRs-%28Analytics-Cluster%29/operation/postAnalyticsAllowedCidr)Create Allowed CIDR 

Adds a trusted CIDR to an clusters's list of allowed CIDRs.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

Note that updating this resource is not supported; you must delete and recreate allowed CIDRs instead. As a result, ETags are also not supported for this resource.

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### Request Body schema: application/json

| cidrrequired | string The trusted CIDR to allow the database connections from. The example represents a single IP address (i.e. a subnet mask of 32).                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| comment      | string A short description of the allowed CIDR.                                                                                                                                                  |
| expiresAt    | string <date-time\> An RFC3339 timestamp determining when the allowed CIDR should expire. If this field is empty/omitted then the allowed CIDR is permanent and will never automatically expire. |

### Responses

**201** 

Successfully added an allowed CIDR for the analytics cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "cidr": "6.60.28.100/32",
* "comment": "Allows access from my local developer machine",
* "expiresAt": "2023-05-14T21:49:58.465Z"
}`

### Response samples 

* 201
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Allowed-CIDRs-%28Analytics-Cluster%29/operation/listAnalyticsAllowedCidrs)List Allowed CIDRs 

Lists all of the allowed CIDRs for a given cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                  |
| sortBy        | Array of strings Example: sortBy=id Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **type**, **status**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                         |

### Responses

**200** 

Successfully listed all allowed CIDRs for the analytics cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "cidr": "1.23.45.67/32",
    * "comment": "Allows access from my local developer machine",
    * "expiresAt": "2023-05-14T21:49:58.465Z",
    * "status": "active",
    * "type": "temporary",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Allowed-CIDRs-%28Analytics-Cluster%29/operation/getColumnarAllowedCidrByID)Get Allowed CIDR 

Fetches the details for the specified allowed CIDR.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |
| allowedCidrIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the allowed CIDR.      |

### Responses

**200** 

Successfully fetched the allowed CIDR details.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs/{allowedCidrId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs/{allowedCidrId}

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "cidr": "1.23.45.67/32",
* "comment": "Allows access from my local developer machine",
* "expiresAt": "2023-05-14T21:49:58.465Z",
* "status": "active",
* "type": "temporary",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Allowed-CIDRs-%28Analytics-Cluster%29/operation/deleteColumnarAllowedCidrByID)Delete Allowed CIDR 

Deletes the existing allowed CIDR.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |
| allowedCidrIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the allowed CIDR.      |

### Responses

**204** 

Successfully deleted the allowed CIDR by its ID.

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs/{allowedCidrId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/allowedcidrs/{allowedCidrId}

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Api-Keys)Api Keys

Couchbase Capella Management API uses a Bearer token mechanism for authentication; each call to the Management API has to be authenticated by API key.

## [](#tag/Api-Keys/operation/postOrganizationAPIKeys)Create API Key 

Creates a new API key under an organization.

Organization Owners can create Organization and Project scoped API keys.

Project Owner and Project Creator can create project scoped keys.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| namerequired              | string (APIKeyName) Name of the API key.                                                                                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description               | string (APIKeyDescription) Default: "" Description for the API key.                                                                                                                                                                                                       |
| expiry                    | number <float\>  (APIKeyExpiry) Default: 180 Expiry of the API key in number of days. Must be at least 0.01 days. If set to -1, the token will not expire.                                                                                                                |
| allowedCIDRs              | Array of strings (APIKeyAllowedCIDRs) Default: \["0.0.0.0/0"\] List of inbound CIDRs for the API key. The system making a request must come from one of the allowed CIDRs.                                                                                                |
| organizationRolesrequired | Array of strings (APIKeyOrganizationRoles) Items Enum: "organizationOwner" "organizationMember" "projectCreator"                                                                                                                                                          |
| resources                 | Array of objects (APIKeyResources) Default: \[\] Resources are the resource level permissions associated with the API key. To learn more about Organization Roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html). |

### Responses

**201** 

Successfully created an API key under an organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/apikeys

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys

### Request samples 

* Payload

Content type

application/json

Example

createOrganizationOwnerAPIKeycreateProjectOwnerAPIKeycreateOrganizationOwnerAPIKey

Copy

 Expand all  Collapse all 

`{
* "name": "Organization Owner API Key",
* "description": "Creates an API key with a Organization Owner role.",
* "expiry": 720,
* "allowedCIDRs": [
  * "8.8.8.8/32"  
],
* "organizationRoles": [
  * "organizationOwner"  
],
* "resources": [ ]
}`

### Response samples 

* 201
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL",
* "token": "QktxVUtFU1dKV1FlMmxwbzJBYXdnTVlRemFZdlRDZTg6eFh4dzU4JUYjekJVYWZPY3lqdUwwYkJoTjZSTmlzRWFIRHF0b1h4a08yazBpQjJ1bms1OW4yTUhAenRib3IhVQ=="
}`

## [](#tag/Api-Keys/operation/listOrganizationAPIKeys)List API keys 

Lists all the API keys under an organization.

Organization Owners can list all the API keys inside the Organization.

Organization Members and Project Creators can list all the Project scoped API key for which they are Project Owner.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                           |
| sortBy        | Array of strings Example: sortBy=name Sets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **name**, **createdAt**, **expiry**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                  |

### Responses

**200** 

Successfully listed all the apikeys under an organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/apikeys

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL",
    * "name": "Production",
    * "description": "API key to manage production Capella Cluster.",
    * "expiry": 180,
    * "allowedCIDRs": [
      * "0.0.0.0/0"  
      ],
    * "organizationRoles": [
      * "organizationMember"  
      ],
    * "resources": [ ],
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Api-Keys/operation/getOrganizationAPIKeyByAccessKey)Get API Key 

Fetches the details of the given API key under an organization.

Organization Owners can get any API key inside the Organization.

Organization Members and Project Creator can get any Project scoped API key for which they are Project Owner.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| ApiKeyIdrequired       | string Example: ffffffffaaaa1414eeee000000000000The ID (Access key) of the API key.           |

### Responses

**200** 

Successfully fetched the API key by its Access key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "IS9DrRsw4KWFS72Zhbj4xmhllHvPcdCL",
* "name": "Organization Owner API Key",
* "description": "Creates an API key with an Organization Owner role.",
* "expiry": 720,
* "allowedCIDRs": [
  * "8.8.8.8/32"  
],
* "organizationRoles": [
  * "organizationOwner"  
],
* "resources": [ ],
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Api-Keys/operation/deleteOrganizationAPIKey)Delete API Key 

Deletes the given API key under an organization.

Organization Owners can delete any API key inside the Organization.

Organization Members and Project Creator can delete any Project scoped API key for which they are Project Owner.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| ApiKeyIdrequired       | string Example: ffffffffaaaa1414eeee000000000000The ID (Access key) of the API key.           |

### Responses

**204** 

Successfully deleted the API key by its Access key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys/{ApiKeyId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Api-Keys/operation/postOrganizationAPIKeyRotate)Rotate API Key 

Rotate the secret of a given API key under an organization.

Organization Owners can rotate any API key inside the Organization.

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| ApiKeyIdrequired       | string Example: ffffffffaaaa1414eeee000000000000The ID (Access key) of the API key.           |

##### Request Body schema: application/json

| secret | string A secret associated with API key. One has to follow the secret key policy, such as allowed characters and a length of 64 characters. If this field is left empty, a secret will be auto-generated. |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully rotated the API key.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/apikeys/{ApiKeyId}/rotate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/apikeys/{ApiKeyId}/rotate

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "secret": "<YOUR_SECRET_KEY_HERE>"
}`

### Response samples 

* 200
* 403
* 404
* 422
* 500

Content type

application/json

Copy

`{
* "secretKey": "<YOUR_SECRET_KEY_HERE>",
* "token": "<YOUR_TOKEN_HERE>"
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-and-Restore)Columnar Analytics Cloud Snapshot Backups & Restore

Couchbase provides a comprehensive backup solution, supporting both scheduled and on-demand backups to ensure robust disaster recovery for production data. In Couchbase Capella, you can perform scheduled and on-demand backups of columnar cloud snapshot data. On-demand backups are always full backups and start immediately upon request, ensuring you can capture the current state of your data whenever needed.

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-and-Restore/operation/createColumnarAnalyticsBackup)Create Cloud Snapshot Backup 

Creates a new backup for the specified Columnar Analytics Cluster.

This operation captures the current state of the cluster, which can later be used for restore purposes.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### Request Body schema: application/json

| retention | integer Represents interval in hours to retain the backup. |
| --------- | ---------------------------------------------------------- |

### Responses

**202** 

Successfully initiated the creation of a backup for the Columnar Analytics Cluster. The response contains the ID of the backup process.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "retention": 168
}`

### Response samples 

* 202
* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "backupId": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-and-Restore/operation/listColumnarAnalyticsBackups)List Cloud Snapshot Backups 

Retrieves a list of backups for the specified Columnar Analytics Cluster.

This list includes only the backups that are in progress, completed, or failed. It does not show backups that are queued but not yet initiated.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                                                     |
| sortBy        | Array of strings Example: sortBy=createdAtSets the order in which you would like to sort the results and the key you would like to sort by. Valid fields to sort the results are: **id**, **createdAt**, **expiration**, **retention**, **size**, **type**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                                            |

### Responses

**200** 

Successfully retrieved the list of backups for the Columnar Analytics Cluster. The response contains a paginated list of backup details in JSON format.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "createdAt": "2019-08-24T14:15:22Z",
    * "databaseSize": 0,
    * "type": "string",
    * "retention": 0,
    * "expiration": "2019-08-24T14:15:22Z",
    * "progress": {
      * "status": "string",
      * "time": "2019-08-24T14:15:22Z"  
      },
    * "region": "string",
    * "id": "string"  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-and-Restore/operation/updateColumnarAnalyticsBackupRetention)Update Backup Retention 

Updates the retention period for a specific backup in your analytics cluster.

The retention period determines how long a backup is stored before it is automatically deleted. Adjust this setting to extend or shorten the duration based on your retention policy.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |
| backupIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.            |

##### Request Body schema: application/json

| retentionrequired | integer Represents interval in hours to retain the backup. |
| ----------------- | ---------------------------------------------------------- |

### Responses

**204** 

The backup retention time was successfully updated. No content is returned in the response.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/{backupId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/{backupId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "retention": 720
}`

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-and-Restore/operation/deleteColumnarAnalyticsBackup)Delete Backup 

Permanently deletes a specific backup from the analytics cluster.

This action cannot be undone. Ensure that the backup is no longer needed before deletion, as it will remove all data associated with it.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |
| backupIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.            |

### Responses

**202** 

The backup deletion request was successfully received and is being processed.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/{backupId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/{backupId}

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-and-Restore/operation/restoreColumnarAnalyticsCluster)Restore Backup 

Initiates an immediate restore job from a specified backup for the Columnar Analytics Cluster.

This operation allows you to restore data from an existing backup to the current state of the cluster.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |
| backupIdrequired           | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the backup.            |

### Responses

**202** 

Successfully initiated a restore job for the Columnar Analytics Cluster. The response includes the ID of the restore operation.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/{backupId}/restore

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/{backupId}/restore

### Response samples 

* 202
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "restoreId": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-and-Restore/operation/listColumnarAnalyticsRestores)List Cloud Snapshot Restores 

Retrieves a list of restore operations that have been performed for the specified Columnar Analytics Cluster.

This allows you to track completed, ongoing, or failed restore jobs for your cluster.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                           |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                 |
| sortBy        | Array of strings Example: sortBy=createdAtSets the order in which you would like to sort the results and the key you would like to sort by. Valid fields to sort the results are: **id**, **createdAt** |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                        |

### Responses

**200** 

Successfully retrieved the list of restore operations for the Columnar Analytics Cluster. The response contains a paginated list of restore job details in JSON format.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/restores

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackups/restores

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "string",
    * "createdAt": "2019-08-24T14:15:22Z",
    * "status": "string",
    * "restoreEnd": "2019-08-24T14:15:22Z",
    * "restoreTo": "string",
    * "snapshot": "2019-08-24T14:15:22Z"  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-Schedule)Columnar Analytics Cloud Snapshot Backups Schedule

Couchbase provides automatic backup scheduling as part of its disaster recovery strategy at the cluster level. In Couchbase Capella, once a backup schedule is set, the system automatically backs up the entire cluster based on the defined schedule, ensuring that all data within the cluster is protected according to your retention policies.

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-Schedule/operation/upsertColumnarAnalyticsBackupSchedule)Upsert Backup Schedule 

Creates or updates the backup schedule for the specified Columnar Analytics Cluster.

This operation allows you to configure or modify the timing and frequency of backups. It ensures that the cluster's backup process follows the defined schedule.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information on access roles, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### Request Body schema: application/json

| intervalrequired  | integer Represents the time interval in hours.                    |
| ----------------- | ----------------------------------------------------------------- |
| retentionrequired | integer Represents the retention time of the backup in hours.     |
| startTimerequired | string <date-time\> Represents the start time in ISO 8601 format. |

### Responses

**204** 

The backup schedule was successfully created or updated. No content will be returned in the response.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackupSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackupSchedule

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "interval": 4,
* "retention": 24,
* "startTime": "2024-07-08T17:00:00+00:00"
}`

### Response samples 

* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-Schedule/operation/getColumnarAnalyticsBackupSchedule)Get Backup Schedule 

Retrieves the current backup schedule for the specified Columnar Analytics Cluster.

This operation provides the details of the backup schedule, including timing and frequency, so you can view and verify when backups are set to occur.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager

For more information on access roles, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**200** 

The backup schedule was successfully retrieved, and the response contains the details of the schedule in JSON format.

**204** 

The backup schedule was not found for the specified Columnar Analytics Cluster. No content will be returned in the response.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackupSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackupSchedule

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "interval": 4,
* "retention": 24,
* "startTime": "2024-07-08T17:00:00+00:00"
}`

## [](#tag/Columnar-Analytics-Cloud-Snapshot-Backups-Schedule/operation/deleteColumnarAnalyticsBackupSchedule)Delete Backup Schedule 

Deletes the existing backup schedule for the specified Columnar Analytics Cluster.

This action permanently removes the scheduled backups, so no future backups will be initiated unless a new schedule is created.

For further details on managing backups, refer to [Backup and Restore Data](https://docs.couchbase.com/columnar/admin/backup-restore.html).

To access this endpoint, the provided API key must include one of the following roles.

* Organization Owner
* Project Owner
* Project Manager  
For more information on access roles, visit [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**204** 

The backup schedule was successfully deleted. No content will be returned in the response.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackupSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/cloudSnapshotBackupSchedule

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-Clusters)Columnar Analytics Clusters

The Columnar Analytics Clusters endpoint allows users to manage their Capella Columnar analytics clusters. Capella Columnar is an analytical database (RT-OLAP) for bringing data together for real time apps and operational intelligence. Using this endpoint, users can create new clusters, get details of a specific cluster or a listing of clusters, scale up or down existing clusters, and delete clusters.

## [](#tag/Columnar-Analytics-Clusters/operation/createAnalyticsCluster)Create new analytics cluster 

Creates a new analytics cluster

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager  
 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### Request Body schema: application/json

| namerequired          | string <= 256 characters Name of the analytics cluster                                                                                                                                                          |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description           | string <= 1024 characters The description of the analytics cluster.                                                                                                                                             |
| cloudProviderrequired | string Enum: "aws" "gcp" Cloud provider selection aws: Amazon Web Services gcp: Google Cloud Platform                                                                                                           |
| regionrequired        | string Which region should the analytics cluster be deployed in.                                                                                                                                                |
| nodesrequired         | integer \[ 1 .. 32 \] The number of nodes.                                                                                                                                                                      |
| supportrequired       | object (ColumnarSupport)                                                                                                                                                                                        |
| computerequired       | object (Compute) Following are the supported compute combinations for CPU and RAM for different cloud providers. To learn more, see [Amazon Web Services](https://docs.couchbase.com/cloud/reference/aws.html). |
| availabilityrequired  | object (Availability)                                                                                                                                                                                           |

### Responses

**202** 

Successfully created an analytics cluster

**401** 

The client does not have the valid credentials to access this resource.

**402** 

The request is unavailable unavailable for trial accounts.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "My-first-analytics-cluster",
* "description": "I won him in a game of hook a duck at a carnival",
* "cloudProvider": "aws",
* "region": "us-east-2",
* "nodes": 2,
* "support": {
  * "plan": "enterprise",
  * "timezone": "ET"  
},
* "compute": {
  * "cpu": 4,
  * "ram": 16  
},
* "availability": {
  * "type": "single"  
}
}`

### Response samples 

* 202
* 401
* 402
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Columnar-Analytics-Clusters/operation/listProjectLevelAnalyticsClusters)List project level analytics clusters 

Lists all the analytics clusters for a project

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                          |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **cloudProvider**, **name**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                 |

### Responses

**200** 

Successfully listed all the analytics clusters for the project

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters

### Response samples 

* 200
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "My-first-analytics-cluster",
    * "description": "I won him in a game of hook a duck at a carnival",
    * "cloudProvider": "aws",
    * "region": "us-east-2",
    * "nodes": 3,
    * "currentState": "deploying",
    * "support": {
      * "plan": "enterprise",
      * "timezone": "ET"  
      },
    * "compute": {
      * "cpu": 4,
      * "ram": 16  
      },
    * "availability": {
      * "type": "single"  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Columnar-Analytics-Clusters/operation/listOrganizationLevelAnalyticsClusters)List organization level analytics clusters 

Lists all the analytics clusters for an organization

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                          |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **cloudProvider**, **name**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                 |

### Responses

**200** 

Successfully listed all the analytics clusters for the organization

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/analyticsClusters

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/analyticsClusters

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "My-first-analytics-cluster",
    * "description": "I won him in a game of hook a duck at a carnival",
    * "cloudProvider": "aws",
    * "region": "us-east-2",
    * "nodes": 3,
    * "currentState": "deploying",
    * "support": {
      * "plan": "enterprise",
      * "timezone": "ET"  
      },
    * "compute": {
      * "cpu": 4,
      * "ram": 16  
      },
    * "availability": {
      * "type": "single"  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Columnar-Analytics-Clusters/operation/getAnalyticsCluster)Get analytics cluster details 

Gets the details of a single analytics cluster

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**200** 

Successfully retrieved details of the analytics cluster

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}

### Response samples 

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "My-first-analytics-cluster",
* "description": "I won him in a game of hook a duck at a carnival",
* "cloudProvider": "aws",
* "region": "us-east-2",
* "nodes": 3,
* "currentState": "deploying",
* "support": {
  * "plan": "enterprise",
  * "timezone": "ET"  
},
* "compute": {
  * "cpu": 4,
  * "ram": 16  
},
* "availability": {
  * "type": "single"  
}
}`

## [](#tag/Columnar-Analytics-Clusters/operation/putAnalyticsCluster)Update an analytics cluster 

Updates an analytics cluster. This could be the name, description, nodes(scaling up/down), or plan and timezone for support.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager  
 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| namerequired        | string <= 256 characters Name of the analytics cluster.                        |
| ------------------- | ------------------------------------------------------------------------------ |
| descriptionrequired | string <= 1024 characters The new cluster description (up to 1024 characters). |
| nodesrequired       | integer \[ 1 .. 32 \] The number of nodes you want for the cluster             |
| supportrequired     | object (ColumnarSupport)                                                       |

### Responses

**204** 

Successfully updated the analytics cluster

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "My first analytics cluster",
* "description": "The extended description of my new cluster.",
* "nodes": 2,
* "support": {
  * "plan": "enterprise",
  * "timezone": "ET"  
}
}`

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Columnar-Analytics-Clusters/operation/deleteAnalyticsCluster)Delete analytics cluster 

Deletes the analytics cluster

 In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**202** 

Successfully deleted the analytics cluster

**400** 

Returned when we are unable to decode the recevied payload.

**401** 

The client does not have the valid credentials to access this resource.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}

### Response samples 

* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Columnar-Analytics-Clusters/operation/analyticsClusterOn)Turn On Analytics Cluster 

Turn analytics cluster on.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**202** 

Successfully switched the cluster to on state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/activationState

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-Clusters/operation/analyticsClusterOff)Turn Off Analytics Cluster 

Turn analytics cluster off.

Turning off your analytics cluster turns off the compute for your analytics cluster but the storage remains. All of the data, indexes and analytics cluster configuration remain, including users and allow lists.

 In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**202** 

Successfully switched the analytics cluster to off state.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/activationState

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/activationState

### Response samples 

* 403
* 404
* 409
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-OnOff-Schedule)Columnar Analytics On/Off Schedule

The Columnar Analytics On/Off Schedule endpoint enables you to schedule when your Columnar analytics cluster should turn on or off to save costs. Turning off the cluster only turns off the compute; all of your data, indexes, and cluster configuration remain, including users and allow lists. When you turn your Columnar analytics cluster off, you will be charged the OFF amount for the cluster.

## [](#tag/Columnar-Analytics-OnOff-Schedule/operation/postAnalyticsOnOffSchedule)Create Analytics Cluster On/Off schedule 

This provides the means to add an on/off schedule for an analytics cluster

 In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### Request Body schema: application/json

| timezonerequired | string Enum: "Pacific/Midway" "US/Hawaii" "US/Alaska" "US/Pacific" "US/Mountain" "US/Central" "US/Eastern" "America/Puerto\_Rico" "Canada/Newfoundland" "America/Argentina/Buenos\_Aires" "Atlantic/Cape\_Verde" "Europe/London" "Europe/Amsterdam" "Europe/Athens" "Africa/Nairobi" "Asia/Tehran" "Indian/Mauritius" "Asia/Karachi" "Asia/Calcutta" "Asia/Dhaka" "Asia/Bangkok" "Asia/Hong\_Kong" "Asia/Tokyo" "Australia/North" "Australia/Sydney" "Pacific/Ponape" "Antarctica/South\_Pole" Timezone for the schedule |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| daysrequired     | Array of objects (Days)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Responses

**204** 

Successfully created an on/off schedule based on the analytics clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

### Request samples 

* Payload

Content type

application/json

Example

PostAnalyticsOnOffSchedulePostAnalyticsOnOffScheduleDefaultBoundaryWithoutToBodyPostAnalyticsOnOffScheduleDefaultsBoundaryWithoutHourMinutePostAnalyticsOnOffScheduleDefaultsBoundaryPostAnalyticsOnOffScheduleDefaultsBoundaryWithoutHourMinuteBodyPostAnalyticsOnOffSchedule

Copy

 Expand all  Collapse all 

`{
* "timezone": "US/Pacific",
* "days": [
  * {
    * "day": "monday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "tuesday",
    * "state": "custom",
    * "from": {
      * "hour": 21,
      * "minute": 30  
      },
    * "to": {
      * "hour": 23,
      * "minute": 30  
      }  
  },
  * {
    * "day": "wednesday",
    * "state": "on"  
  },
  * {
    * "day": "thursday",
    * "state": "on"  
  },
  * {
    * "day": "friday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 15,
      * "minute": 30  
      }  
  },
  * {
    * "day": "saturday",
    * "state": "off"  
  },
  * {
    * "day": "sunday",
    * "state": "off"  
  }  
]
}`

### Response samples 

* 403
* 404
* 409
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-OnOff-Schedule/operation/getAnalyticsOnOffSchedule)Get Analytics Cluster On/Off Schedule 

Fetches the details of the on/off schedule for the given analytics cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**200** 

Successfully fetched the on/off schedule based on the analytics clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "timezone": "US/Pacific",
* "days": [
  * {
    * "day": "monday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "tuesday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "wednesday",
    * "state": "on"  
  },
  * {
    * "day": "thursday",
    * "state": "on"  
  },
  * {
    * "day": "friday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "saturday",
    * "state": "off"  
  },
  * {
    * "day": "sunday",
    * "state": "off"  
  }  
]
}`

## [](#tag/Columnar-Analytics-OnOff-Schedule/operation/putAnalyticsOnOffSchedule)Update Analytics Cluster On/Off Schedule 

This provides the means to update an existing analytics cluster on/off schedule.

In order to access this endpoint, the provided API key must have at least one of the roles referenced below:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### Request Body schema: application/json

| timezonerequired | string Enum: "Pacific/Midway" "US/Hawaii" "US/Alaska" "US/Pacific" "US/Mountain" "US/Central" "US/Eastern" "America/Puerto\_Rico" "Canada/Newfoundland" "America/Argentina/Buenos\_Aires" "Atlantic/Cape\_Verde" "Europe/London" "Europe/Amsterdam" "Europe/Athens" "Africa/Nairobi" "Asia/Tehran" "Indian/Mauritius" "Asia/Karachi" "Asia/Calcutta" "Asia/Dhaka" "Asia/Bangkok" "Asia/Hong\_Kong" "Asia/Tokyo" "Australia/North" "Australia/Sydney" "Pacific/Ponape" "Antarctica/South\_Pole" Timezone for the schedule |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| daysrequired     | Array of objects (Days)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Responses

**204** 

Successfully updated the on/off schedule based on the analytics clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "timezone": "US/Pacific",
* "days": [
  * {
    * "day": "monday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "tuesday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "wednesday",
    * "state": "on"  
  },
  * {
    * "day": "thursday",
    * "state": "on"  
  },
  * {
    * "day": "friday",
    * "state": "custom",
    * "from": {
      * "hour": 12,
      * "minute": 30  
      },
    * "to": {
      * "hour": 14,
      * "minute": 30  
      }  
  },
  * {
    * "day": "saturday",
    * "state": "off"  
  },
  * {
    * "day": "sunday",
    * "state": "off"  
  }  
]
}`

### Response samples 

* 403
* 404
* 409
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-OnOff-Schedule/operation/deleteAnalyticsOnOffSchedule)Delete Analytics Cluster On/Off Schedule 

Deletes the on/off schedule for the given analytics cluster.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**204** 

Successfully deleted the on/off schedule by its analytics clusterId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/onOffSchedule

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Columnar-Analytics-Private-Endpoint-Service)Columnar Analytics Private Endpoint Service

Access your Analytics cluster from your cloud provider's private network. Supporting infrastructure is deployed and it may take a few minutes for private endpoints to be available. After it's enabled, you can create private endpoint in your network. You can do this using the cloud provider's CLI. For an example, use the POST privateEndpointService/endpointCommand endpoint to get the command.

## [](#tag/Columnar-Analytics-Private-Endpoint-Service/operation/getColumnarPrivateEndpointServiceStatus)Get Columnar Analytics Private Endpoint Service Status 

Private endpoint service allows you to access your Analytics cluster from your private network, using private endpoints. Currently limited to AWS.

This endpoint allows you to get the status of private endpoint to see whether the job to enable private endpoint was successful or not.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**200** 

Successfully retrieved private endpoint status of the Analytics cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "enabled": true,
* "status": "idle",
* "serviceName": "com.amazonaws.vpce.us-east-1.vpce-svc-0399b9a3337de6847",
* "privateDns": "ghfv2g8fyedebnae.pl.cloud.couchbase.com/"
}`

## [](#tag/Columnar-Analytics-Private-Endpoint-Service/operation/enableColumnarPrivateEndpointService)Enable Columnar Analytics Private Endpoint Service 

Enable private endpoint service on your Analytics cluster. Currently limited to AWS.

Supporting infrastructure is deployed and it may take a few minutes for private endpoints to be available. After it's enabled, you can create private endpoint in your network. You can do this using the cloud provider's CLI, UI and SDK.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**202** 

Successfully submitted request to enable private endpoint service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Columnar-Analytics-Private-Endpoint-Service/operation/disableColumnarPrivateEndpointService)Disable Columnar Analytics Private Endpoint Service 

Disable private endpoint service on your Analytics cluster. Currently limited to AWS.

Supporting infrastructure is removed and it may take a few minutes before private endpoints is disabled.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**202** 

Successfully submitted request to disable private endpoint service.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService

### Response samples 

* 400
* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Columnar-Analytics-Private-Endpoint-Service/operation/getColumnarPrivateEndpointServiceCommand)Get Columnar Private Endpoint CLI Command required to setup private endpoint for specific CSP 

Retrieve the command or script to be executed in order to create the private endpoint which will provides a private connection between the specified VPC and the specified Capella private endpoint service.  
Currently only available for AWS. An example for AWS:

```
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-1234 \
  --region us-east-1 \
  --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 \
  --vpc-endpoint-type Interface \
  --subnet-ids subnet-1234

```

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

##### Request Body schema: application/json

| vpcIDrequired     | string \[ 12 .. 21 \] characters The ID of your virtual network |
| ----------------- | --------------------------------------------------------------- |
| subnetIDsrequired | Array of strings                                                |

### Responses

**200** 

Successfully provided command to create a private endpoint.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpointCommand

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpointCommand

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "vpcID": "vpc-1234",
* "subnetIDs": [
  * "subnet-1234"  
]
}`

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "command": "aws ec2 create-vpc-endpoint --vpc-id vpc-1234 --region us-east-1 --service-name com.amazonaws.vpce.us-east-1.vpce-svc-1234 --vpc-endpoint-type Interface --subnet-ids subnet-1234"
}`

## [](#tag/Columnar-Analytics-Private-Endpoint-Service/operation/listColumnarPrivateEndpointServiceConnection)List Columnar Analytics Private Endpoint Connections 

Returns a list of private endpoints, along with the endpoint state, associated with the endpoint service for the Analytics cluster. Currently limited to AWS.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Creator
* Project Viewer

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |

### Responses

**200** 

Successfully retrieved private endpoint status for the Analytics cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpoints

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpoints

### Response samples 

* 200
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "endpoints": [
  * {
    * "endpointId": "vpce-000000000000aaaaa",
    * "status": "linked"  
  }  
]
}`

## [](#tag/Columnar-Analytics-Private-Endpoint-Service/operation/acceptColumnarPrivateEndpointServiceConnection)Accept or associate Columnar Analytics Private Endpoint Request 

Accept a new private endpoint connection request so that it is associated with the endpoint service. This means the private endpoint is available for use. Currently limted to AWS.

 In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

 To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |
| endpointIdrequired         | string Example: vpce-1234The VPC endpoint ID.                                                      |

### Responses

**204** 

Successfully accepted private endpoint connection for the Analytics cluster.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpoints/{endpointId}/associate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpoints/{endpointId}/associate

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Columnar-Analytics-Private-Endpoint-Service/operation/rejectColumnarPrivateEndpointServiceConnection)Reject or disassociate Columnar Analytics Private Endpoint connection 

Removes the private endpoint associated with the endpoint service. This means the private endpoint is no longer able to connect to the private endpoint service. Currently limited to AWS.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired     | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.      |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| projectIdrequired          | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.           |
| analyticsClusterIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the analytics cluster. |
| endpointIdrequired         | string Example: vpce-1234The VPC endpoint ID.                                                      |

### Responses

**204** 

Successfully rejected private endpoint connection

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpoints/{endpointId}/unassociate

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}/analyticsClusters/{analyticsClusterId}/privateEndpointService/endpoints/{endpointId}/unassociate

### Response samples 

* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Organizations)Organizations

Couchbase Capella uses an ordered hierarchy to help you keep all of your data organized and securely accessible. The entity at the top of the hierarchy is called an organization. Everything you do in Capella, whether it's creating a cluster or managing billing, happens within the scope of an organization.

## [](#tag/Organizations/operation/getOrganizationByID)Get Organization 

Fetches the details of an organization by ID.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator
* Organization Member

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

### Responses

**200** 

Successfully returned the organization details.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "My-Organization",
* "subdomain": "abc",
* "description": "The description of the organization.",
* "preferences": {
  * "sessionDuration": 3600  
},
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Organizations/operation/putOrganizationConfiguration)Update Organization Configuration 

Updates an existing organization configuration. Use this endpoint to add, update, and delete network subdomains.

Subdomains are not automatically available. You must contact Couchbase support to enable this feature. To open a Support ticket, see [Create a Support Ticket](https://docs.couchbase.com/cloud/support/manage-support.html#create-support-ticket).

Subdomains:

* Can have a maximum of 30 alphanumeric characters.
* Must be a unique string and not already in use in another tenant or organization. Empty strings are allowed.
* Only affect new clusters. You cannot update existing clusters to include a new subdomain.

In order to access this endpoint, the provided API key must have the following role:

* Organization Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| subdomainrequired | string <= 30 characters The new name of the subdomain for the organization. |
| ----------------- | --------------------------------------------------------------------------- |

### Responses

**204** 

Successfully updated the organization configuration.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/configuration

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/configuration

### Request samples 

* Payload

Content type

application/json

Example

UpdateSubdomainDeleteSubdomainUpdateSubdomain

Copy

`{
* "subdomain": "abc"
}`

### Response samples 

* 403
* 404
* 412
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Organizations/operation/listOrganizations)List Organizations 

Returns a list of all organizations the user has access to.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator
* Organization Member

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

### Responses

**200** 

Successfully listed all the organizations.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations

https://cloudapi.cloud.couchbase.com/v4/organizations

### Response samples 

* 200
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "My-Organization",
    * "subdomain": "abc",
    * "description": "The description of the organization.",
    * "preferences": {
      * "sessionDuration": 3600  
      },
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
]
}`

## [](#tag/Projects)Projects

Projects contain and allow access to Couchbase databases. Projects are used to organize and manage groups of Couchbase databases within organizations. An organization can contain any number of projects, and a project can contain any number of databases.

## [](#tag/Projects/operation/postProject)Create Project 

Creates a new project under the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Creator

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| namerequired | string <= 128 characters The name of the project (up to 128 characters).            |
| ------------ | ----------------------------------------------------------------------------------- |
| description  | string <= 256 characters A short description of the project (up to 256 characters). |

### Responses

**201** 

Successfully created a project under the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/projects

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "My Project",
* "description": "My awesome project"
}`

### Response samples 

* 201
* 400
* 403
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Projects/operation/listProjects)List Project 

Lists all the projects under the organization.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                       |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **name**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                              |

### Responses

**200** 

Successfully listed all the projects under the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "description": "The description of my awesome project",
    * "name": "My-Awesome-Project",
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Projects/operation/getProjectByID)Get Project 

Fetches the details of the given project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner
* Project Manager
* Project Viewer
* Database Data Reader/Writer
* Database Data Reader

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

### Responses

**200** 

Successfully fetched the project based on the projectId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/projects/{projectId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "description": "The description of my awesome project",
* "name": "My-Awesome-Project",
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Projects/operation/putProject)Update Project 

Update project name and or project description.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

##### header Parameters

| If-Match | string Example: 12A precondition header that specifies the entity tag of a resource. |
| -------- | ------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

| namerequired | string <= 128 characters The new project name (up to 128 characters).        |
| ------------ | ---------------------------------------------------------------------------- |
| description  | string <= 256 characters The new project description (up to 256 characters). |

### Responses

**204** 

Successfully updated the project metadata.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**412** 

Returned when there is a mismatch with the Etag version.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

put/v4/organizations/{organizationId}/projects/{projectId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "My-New-Project",
* "description": "The extended description of my awesome project."
}`

### Response samples 

* 400
* 403
* 404
* 412
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 400,
* "code": 1000,
* "message": "The request was malformed or invalid.",
* "hint": "The request was malformed or invalid."
}`

## [](#tag/Projects/operation/deleteProjectByID)Delete Project 

Deletes an existing project.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

To learn more, see [Organization, Project, and Database Access Overview](https://docs.couchbase.com/cloud/organizations/organization-projects-overview.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| projectIdrequired      | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.      |

### Responses

**204** 

Successfully deleted the project by its projectId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**409** 

Returned when there is a conflict with the current state of a resource.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/projects/{projectId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/projects/{projectId}

### Response samples 

* 403
* 404
* 409
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`

## [](#tag/Users)Users

To access an organization, your Couchbase Capella user account must be added to it. Accounts are added to an organization using email invitations sent from Capella by a user with the Organization Owner organization role. All organization users are given one or more organization roles that define what they can view and manage in their organization.

## [](#tag/Users/operation/postUser)Create User 

Invites a new user under the organization.

After making a REST API request, an invitation email is triggered and sent to the user. Upon receiving the invitation email, the user is required to click on a provided URL, which will redirect them to a page with a user interface (UI) where they can set their username and password.

The modification of any personal information related to a user can only be performed by the user through the UI. Similarly, the user can solely conduct password updates through the UI.

The "caller" possessing Organization Owner access rights retains the exclusive user creation capability. They hold the authority to assign roles at the organization and project levels.

At present, our support is limited to the resourceType of "project" exclusively.

In order to access this endpoint, the provided API key must have the following role:

* Organization Owner

To learn more, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| name                      | string <= 128 characters The name of the user.                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| emailrequired             | string (Email) Email of the user.                                                                          |
| organizationRolesrequired | Array of strings (OrganizationRoles) Items Enum: "organizationOwner" "organizationMember" "projectCreator" |
| resources                 | Array of objects (Resource) Default: \[\]                                                                  |

### Responses

**201** 

Successfully sent invite to the user.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

post/v4/organizations/{organizationId}/users

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users

### Request samples 

* Payload

Content type

application/json

Example

CreateOrganizationMemberCreateOrganizationOwnerCreateOrganizationMember

At present, our support is limited to the resourceType of "project" exclusively. Furthermore, the role designation is solely related to roles at the project level.

Copy

 Expand all  Collapse all 

`{
* "name": "John",
* "email": "john.doe@example.com",
* "organizationRoles": [
  * "organizationMember"  
],
* "resources": [
  * {
    * "id": "550e8400-e29b-41d4-a716-446655440000",
    * "type": "project",
    * "roles": [
      * "projectViewer"  
      ]  
  },
  * {
    * "id": "550e8400-e29b-41d4-a716-446655440000",
    * "type": "project",
    * "roles": [
      * "projectDataReaderWriter"  
      ]  
  }  
]
}`

### Response samples 

* 201
* 400
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000"
}`

## [](#tag/Users/operation/listUsers)List Users 

Lists all the users in the organization and filter on the basis of projectId.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member
* Project Creator

The results are always limited by the role and scope of the caller's privileges.

When retrieving a list of users through a GET request, if a user holds the organization owner role, the response will exclude project-level permissions for those users. This is because organization owners have full access to all resources within the organization, making project-level permissions irrelevant for them.

To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html) and [Project Roles](https://docs.couchbase.com/cloud/projects/project-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization. |
| ---------------------- | --------------------------------------------------------------------------------------------- |

##### query Parameters

| page          | integer Sets the page you would like to view.                                                                                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| perPage       | integer Sets the number of results you would like to have on each page.                                                                                                                                                            |
| sortBy        | Array of strings Example: sortBy=nameSets the order of how you would like to sort the results and the key you would like to order by. Valid fields to sort the results are: **id**, **name**, **email**, **status**, **inactive**. |
| sortDirection | string Enum: "asc" "desc" Example: sortDirection=ascThe order in which the items will be sorted.                                                                                                                                   |
| projectId     | string <uuid\> Example: projectId=ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the project.                                                                                                                                 |

### Responses

**200** 

Successfully listed all the user in the organization.

**400** 

Returned when we are unable to decode the recevied payload.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/users

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users

### Response samples 

* 200
* 400
* 403
* 404
* 429
* 500

Content type

application/json

Example

ApiKeyIsOrgOwnerApiKeyIsProjectOwnerReturnedUserIsOrganizationOwnerApiKeyIsOrgOwner

In the event that the API key holds "organizationOwner" access, information related to all projects within the organization will be returned.

Copy

 Expand all  Collapse all 

`{
* "data": [
  * {
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "name": "John",
    * "email": "john.doe@example.com",
    * "status": "verified",
    * "inactive": false,
    * "organizationId": "ffffffff-aaaa-1414-eeee-000000000000",
    * "organizationRoles": [
      * "organizationMember"  
      ],
    * "lastLogin": "2023-07-17T07:05:39.116Z",
    * "region": "North America",
    * "timeZone": "(UTC +5:30) India Standard Time",
    * "enableNotifications": false,
    * "expiresAt": "2023-07-17T07:05:39.116Z",
    * "resources": [
      * {
        * "id": "f98e6c87-41e3-4faa-9df4-906e8d4f1aaf",
        * "type": "project",
        * "roles": [
          * "projectViewer"  
                    ]  
            },
      * {
        * "id": "b7c745ac-9fb8-4b63-a0e4-51230097a169",
        * "type": "project",
        * "roles": [
          * "projectDataReaderWriter"  
                    ]  
            },
      * {
        * "id": "28b67422-63d5-46b1-9234-8ad4a1d2f7be",
        * "type": "project",
        * "roles": [
          * "projectDataReaderWriter"  
                    ]  
            },
      * {
        * "id": "e3942eaa-0f52-43da-963d-87a5b6cb3805",
        * "type": "project",
        * "roles": [
          * "projectDataReaderWriter"  
                    ]  
            }  
      ],
    * "audit": {
      * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "createdAt": "2021-09-01T12:34:56.000Z",
      * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
      * "modifiedAt": "2021-09-01T12:34:56.000Z",
      * "version": 1  
      }  
  }  
],
* "cursor": {
  * "pages": {
    * "page": 2,
    * "next": 3,
    * "previous": 1,
    * "last": 10,
    * "perPage": 10,
    * "totalItems": 10  
  },
  * "hrefs": {
    * "first": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "last": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "previous": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>",
    * "next": "<https://cloud.couchbase.com/v4/users?page=1&perPage=10>"  
  }  
}
}`

## [](#tag/Users/operation/getUser)Get User 

Fetches the details of the given user.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Organization Member
* Project Creator

The results are always limited by the role and scope of the caller's privileges.

When performing a GET request for a user with an organization owner role, the response will exclude project-level permissions for that user. This is because organization owners have access to all resources at the organization level, rendering project-level permissions unnecessary for them.

To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html) and [Project Roles](https://docs.couchbase.com/cloud/projects/project-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.       |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the control plane user. |

### Responses

**200** 

Successfully fetched the user based on the userId.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

get/v4/organizations/{organizationId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users/{userId}

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "alex",
* "email": "john.doe@example.com",
* "status": "not-verified",
* "inactive": false,
* "organizationId": "ffffffff-aaaa-1414-eeee-000000000000",
* "organizationRoles": [
  * "projectCreator"  
],
* "lastLogin": "2023-07-17T07:05:39.116124897Z",
* "region": "North America",
* "timeZone": "(UTC -9:00) Alaska Standard Time",
* "enableNotifications": true,
* "expiresAt": "2023-07-17T07:05:39.116124897Z",
* "resources": [
  * {
    * "type": "project",
    * "id": "ffffffff-aaaa-1414-eeee-000000000000",
    * "roles": [
      * "projectManager"  
      ]  
  }  
],
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56Z",
  * "version": 1  
}
}`

## [](#tag/Users/operation/patchUser)Update User 

Updates organizationRole and resources of the user.

In order to access this endpoint, the provided API key must have at least one of the following roles:

* Organization Owner
* Project Owner

An Organization Owner API key can be utilized to update organizational-level roles and project-level roles for all projects within the organization.

The Project Owner API key allows for updating project-level roles, solely within the projects where the API key holds the Project Owner role.

The modification of any personal information related to a user, such as password updates, can only be performed by the respective user through the user interface (UI).

The results are always limited by the role and scope of the caller's privileges. To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html) and [Project Roles](https://docs.couchbase.com/cloud/projects/project-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.       |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the control plane user. |

##### Request Body schema: application/json

 Array 

| oprequired   | string Enum: "add" "remove" Type of operation.                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pathrequired | string Path of resource that needs to be updated. Organization Roles: /organizationRoles Resources: /resources/{resourceId} Resource Roles: /resources/{resourceId}/roles |
| value        | Array of OrganizationRoles (strings) or Array of ProjectRoles (strings) or Resource (object)                                                                              |

### Responses

**200** 

Successfully updated the user metadata.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**422** 

Request validation error.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

patch/v4/organizations/{organizationId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users/{userId}

### Request samples 

* Payload

Content type

application/json

Example

addOrganizationRoleremoveOrganizationRoleaddResourceremoveResourceRoleaddResourceRoleremoveResourceperformMultipleOperationsaddOrganizationRole

Copy

 Expand all  Collapse all 

`[
* {
  * "op": "add",
  * "path": "/organizationRoles",
  * "value": [
    * "projectCreator"  
  ]  
}
]`

### Response samples 

* 200
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Example

addOrganizationRoleremoveOrganizationRoleaddResourceremoveResourceRoleaddResourceRoleremoveResourceperformMultipleOperationaddOrganizationRole

Copy

 Expand all  Collapse all 

`{
* "id": "ffffffff-aaaa-1414-eeee-000000000000",
* "name": "Jane",
* "email": "jane.doe@example.com",
* "status": "verified",
* "inactive": false,
* "organizationId": "ffffffff-aaaa-1414-eeee-000000000000",
* "organizationRoles": [
  * "organizationMember",
  * "projectCreator"  
],
* "lastLogin": "2023-07-17T07:05:39.116Z",
* "region": "North America",
* "timeZone": "(UTC +5:30) India Standard Time",
* "enableNotifications": false,
* "expiresAt": "2023-07-17T07:05:39.116Z",
* "resources": [
  * {
    * "id": "b7c745ac-9fb8-4b63-a0e4-51230097a169",
    * "type": "project",
    * "roles": [
      * "projectViewer"  
      ]  
  },
  * {
    * "id": "28b67422-63d5-46b1-9234-8ad4a1d2f7be",
    * "type": "project",
    * "roles": [
      * "projectDataReaderWriter"  
      ]  
  }  
],
* "audit": {
  * "createdBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "createdAt": "2021-09-01T12:34:56.000Z",
  * "modifiedBy": "ffffffff-aaaa-1414-eeee-000000000000",
  * "modifiedAt": "2021-09-01T12:34:56.000Z",
  * "version": 2  
}
}`

## [](#tag/Users/operation/deleteUser)Delete User 

Removes user from the organization.

In order to access this endpoint, the provided API key must have the following role:

* Organization Owner

To learn more about the roles, see [Organization Roles](https://docs.couchbase.com/cloud/organizations/organization-user-roles.html).

##### Authorizations:

_token_

##### path Parameters

| organizationIdrequired | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the organization.       |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| userIdrequired         | string <uuid\> Example: ffffffff-aaaa-1414-eeee-000000000000The GUID4 ID of the control plane user. |

### Responses

**204** 

Successfully removed the user from the organization.

**403** 

The client does not have the necessary permissions to access this resource.

**404** 

The requested resource was not found.

**429** 

Returned when the client exceeds the rate limit for the given APIKey.

**500** 

An unexpected error occurred in the server while processing this request.

delete/v4/organizations/{organizationId}/users/{userId}

https://cloudapi.cloud.couchbase.com/v4/organizations/{organizationId}/users/{userId}

### Response samples 

* 403
* 404
* 429
* 500

Content type

application/json

Copy

`{
* "httpStatusCode": 403,
* "code": 1002,
* "message": "Access Denied.",
* "hint": "Your access to the requested resource is denied. Please make sure you have the necessary permissions to access the resource."
}`