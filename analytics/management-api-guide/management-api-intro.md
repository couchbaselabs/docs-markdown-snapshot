---
title: Manage Deployments with the Capella Analytics Management API
description: The Capella Analytics Management API is a secure REST API that
  enables you to configure and manage your Capella Analytics services clusters.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/management-api-guide/pages/management-api-intro.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/management-api-guide/management-api-intro.html)

# Manage Deployments with the Capella Analytics Management API

> The Capella Analytics Management API is a secure REST API that enables you to configure and manage your Capella Analytics services clusters. 

This page is for Capella Analytics. For Capella operational, see [Manage Deployments with the Management API](../../cloud/management-api-guide/management-api-intro.md).

Clients do not need any special tools, SDKs, or libraries to access the Management API. The Management API supports off-the-shelf HTTP clients, such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com).

To get started quickly, [create an API key and make an API call](#see-also).

## [](#versioning)Versioning

The Management API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the Management API may be a non-versioned bug fix, a patch update, a minor update, or a major update. When a non-versioned bug fix is released, the version number is not updated. When a patch update, a minor update, or a major update is released, the version number is updated also.

With few exceptions, new versions of Management API are backward compatible, minimizing the effect on existing deployments. In most cases, you do not have to update your existing infrastructure when a new version of the Management API is released. Features added in a new version of the Management API will not break existing deployments.

Exceptions to backward compatibility are as follows:

* Critical security fixes. A vulnerable version is marked as unsupported when a fixed version is released. In this case, you must plan to upgrade as soon as possible.
* Fundamental architectural changes, when unavoidable.

## [](#initial-version)Initial Version

The Management API v4.0 is the initial release of the Capella Analytics Management API. The version numbering of the Capella Analytics Management API is aligned with the version numbering of the Capella operational Management API.

## [](#authentication-and-authorization)Authentication and Authorization

The Management API uses API keys for authentication and authorization. You need an API key to access endpoints exposed by the Management API.

API keys are associated with Couchbase Capella [roles and permissions](../../cloud/organizations/organization-projects-overview.md). An API key must have the appropriate Capella roles to access an endpoint. The Management API reference guide lists the roles that are needed for each endpoint.

Every API key is associated with an allowed IP Address list, which can be configured during API key creation. Every API key has an expiration date.

To authenticate a Management API call, you must pass the API key secret as a Bearer token using the HTTP `Authorization` header.

## [](#concurrent-access-and-put-requests)Concurrent Access and PUT Requests

To support concurrent requests, PUT requests support optimistic concurrency control, using `If-Match` headers in combination with HTTP ETags (entity tags). Exceptions are noted in the endpoint descriptions. A typical pattern is to do a GET request on a specified resource, which returns an ETag value. You can then include the ETag value in a PUT request to update the resource.

PUT requests ignore all fields in the body of the request that are not required. Required fields for each PUT request are specified in the Management API reference guide.

## [](#auditing)Auditing

All requests to the Management API are audited. All endpoints support Audit fields for audit purposes, except where noted in the Management API reference guide.

Lists are paginated.

## [](#service-limits)Service Limits

Long-Running Requests

The following long-running requests are rejected with error 504, Gateway Timeout:

* Read requests taking longer than 90 seconds to process.
* Write requests taking longer than 120 seconds to process.

Rate Limiting

Requests are limited to 100 requests per minute per API key.

Payload Size

Requests and response payloads are restricted to 18 MB.

## [](#see-also)See Also

* To create an API key, see [Get Started with the Capella Analytics Management API](management-api-start.md).
* To make an API call, see [Make an API Call with the Capella Analytics Management API](management-api-use.md).
* For a full reference guide, see [Capella Columnar Management API Reference](../management-api-reference/index.md).
* For an error reference, see [Capella Analytics Management API Errors](management-api-errors.md).
* For the change log, see [Capella Analytics Management API Change Log](management-api-log.md).