---
title: Make an API Call with the Management API
description: How to make an API call with the Couchbase Capella Management API.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/management-api-guide/pages/management-api-use.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/management-api-guide/management-api-use.html)

# Make an API Call with the Management API

> How to make an API call with the Couchbase Capella Management API. 

This page is for Capella operational. For Capella Analytics, see [Make an API Call with the Capella Analytics Management API](../../analytics/management-api-guide/management-api-use.md).

## [](#prerequisites)Prerequisites

In order make an API call with the Management API, you must have an API key that was created for the Management API.

* The API key must have all the organization roles, project access, and project roles required to carry out the API call. In the Management API reference, each endpoint description lists the roles that are needed.
* The API key must not have expired.
* The API key must grant access to the Management API from your client’s IP address.
* You must have saved the API key secret when you created it.

To create an API key for the Management API, see [Get Started with the Management API](management-api-start.md).

## [](#make-an-api-call)Make an API Call

You can use a client such as [curl](https://curl.se) or a native SDK call to make an API call with the Management API.

To make an API call:

1. Use the following base URL.  
`<https://cloudapi.cloud.couchbase.com>`
2. Pass the API key secret as a Bearer token using the HTTP `Authorization` header.
3. If a request body is required, pass it in JSON format.

Alternatively, you can use a client such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com) to explore the details of the REST API, generate code samples, and so on. The Management API uses an [OpenAPI](https://swagger.io/resources/open-api) v3 specification. To download the Management API specification, go to the [Management API Reference](../management-api-reference/index.md) and click **Download**.

## [](#examples)Examples

### [](#ex-list-orgs)List Organizations

The following request lists all of the organizations available to the provided API key.

* `$apiKeySecret` is the API key secret, used as the Bearer token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations" \
   -H "Authorization: Bearer $apiKeySecret"
```

The response is a JSON object similar to the following. In this case, the provided API key is able to access a single organization.

HTTP Response

```json
{
  "data": [
    {
      "audit": {
        "createdAt": "2020-07-22T12:38:57.437248116Z",
        "createdBy": "",
        "modifiedAt": "2023-07-25T14:33:56.13967014Z",
        "modifiedBy": "<redacted>",
        "version": 0
      },
      "description": "",
      "id": "<redacted>",
      "name": "cbc-dev",
      "preferences": {
        "sessionDuration": 7200
      }
    }
  ]
}
```

The response includes the organization ID. You can use the organization ID for any further API calls in which `{organization}` is a path parameter.

### [](#ex-list-projects)List Projects in an Organization

The following request lists all of the projects available to the provided API key within the specified organization.

* `$organizationId` is the organization ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

The query parameters specify that each page of results should contain 3 projects, and that the request should return the first page of results.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects?perPage=3&page=1" \
   -H "Authorization: Bearer $apiKeySecret"
```

The response is a JSON object similar to the following.

HTTP Response

```json
{
  "cursor": {
    "hrefs": {
      "first": "https://cloudapi.cloud.couchbase.com/v4/organizations/<organizationId>/projects?page=1&perPage=3",
      "last": "https://cloudapi.cloud.couchbase.com/v4/organizations/<organizationId>/projects?page=182&perPage=3",
      "next": "https://cloudapi.cloud.couchbase.com/v4/organizations/<organizationId>/projects?page=2&perPage=3",
      "previous": ""
    },
    "pages": {
      "last": 182,
      "next": 2,
      "page": 1,
      "perPage": 3,
      "previous": 0,
      "totalItems": 544
    }
  },
  "data": [
    {
      "audit": {
        "createdAt": "2023-08-07T10:58:04.844838072Z",
        "createdBy": "<redacted>",
        "modifiedAt": "2023-08-07T10:58:04.844855439Z",
        "modifiedBy": "<redacted>",
        "version": 1
      },
      "description": "",
      "id": "<redacted>",
      "name": "Project 1"
    },
    {
      "audit": {
        "createdAt": "2023-08-30T10:52:25.834748195Z",
        "createdBy": "<redacted>",
        "modifiedAt": "2023-08-30T10:52:25.83476043Z",
        "modifiedBy": "<redacted>",
        "version": 1
      },
      "description": "terraform testing",
      "id": "<redacted>",
      "name": "Project 2"
    },
    {
      "audit": {
        "createdAt": "2023-07-18T09:28:13.334086299Z",
        "createdBy": "",
        "modifiedAt": "0001-01-01T00:00:00Z",
        "modifiedBy": "",
        "version": 0
      },
      "description": "",
      "id": "<redacted>",
      "name": "Project 3"
    }
  ]
}
```

This response contains `cursor` information, showing the pagination of the results. For each project, `audit` information is provided, showing metadata for the project.

### [](#ex-get-project)Get Details of a Project

The following request gets details about the specified project within the specified organization.

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId" \
   -H "Authorization: Bearer $apiKeySecret"
```

The response is a JSON object similar to the following.

HTTP Response

```json
{
  "audit": {
    "createdAt": "2023-03-14T15:12:25.671401417Z",
    "createdBy": "<redacted>",
    "modifiedAt": "0001-01-01T00:00:00Z",
    "modifiedBy": "",
    "version": 0
  },
  "description": "",
  "id": "<redacted>",
  "name": "Project 1"
}
```

### [](#ex-put-project)Update a Project

The following request updates the specified project within the specified organization with a new description.

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

HTTP Request

```sh
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId" \
   -H "Accept: application/json" \
   -H "Authorization: Bearer $apiKeySecret" \
   -d '{"name": "Project 1", "description": "New description"}'
```

In this example, only the `description` field is new. However, both the `name` and `description` fields are required, so the `name` field is supplied unchanged.

### [](#ex-get-etag)Get the ETag for a Project

The following request gets the ETag of the specified project within the specified organization.

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

HTTP Request

```sh
curl "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId" -i \
   -H "Authorization: Bearer $apiKeySecret" | grep etag
```

curl also has an `--etag-save` option, which provides a convenient way of saving the ETag value. This example requests the protocol response headers instead, for clarity.

The response is an ETag similar to the following.

HTTP Response

```text
etag: 1
```

You can use the ETag in a PUT request for concurrency control.

### [](#ex-put-etag)Update a Project with Concurrency Control

The following request checks whether the specified project within the specified organization has the expected ETag. If so, it updates the project with a new description.

This enables you to make sure that you’re applying your update to the correct revision of the project, in cases where the project may be updated by other processes concurrently.

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

HTTP Request

```sh
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId" \
   -H "Accept: application/json" \
   -H "Authorization: Bearer $apiKeySecret" \
   -H "If-Match: 1" \
   -d '{"name": "Project 1", "description": "Updated description"}'
```

curl also has an `--etag-compare` option, which provides a convenient way of checking the ETag value. This example specifies the `If-Match` request header instead, for clarity.

If the ETag of the project matches, the project is updated. If the ETag does not match, the request returns an error message similar to the following.

HTTP Response

```json
{
  "code": 9000,
  "hint": "Please include the correct ETag version with the request.",
  "httpStatusCode": 412,
  "message": "Unable to process update. The 'ETag' provided does not match the current version of the document being requested to update."
}
```

## [](#next-steps)Next Steps

* For a full reference guide, see [Management API Reference](../management-api-reference/index.md).
* For an error reference, see [Management API Errors](management-api-errors.md).