---
title: Manage Deployments with the Capella Operational Management API
description: The Couchbase Capella Operational Management API is a secure REST
  API that enables you to provision, deploy, and configure Capella deployments
  across all supported cloud service providers.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/management-api-guide/pages/management-api-intro.adoc
pubDate: 2026-04-01T05:25:30.286Z
link: xref:cloud:management-api-guide:management-api-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/management-api-guide/management-api-intro.html)

# Manage Deployments with the Capella Operational Management API

> The Couchbase Capella Operational Management API is a secure REST API that enables you to provision, deploy, and configure Capella deployments across all supported cloud service providers. 

This page is for Capella operational. For Capella AI Services, see [Manage Deployments with Capella AI Services APIs](../../ai/api-guide/api-intro.md). For Capella Analytics, see [Manage Deployments with the Capella Analytics Management API](../../analytics/management-api-guide/management-api-intro.md).

Clients do not need any special tools, SDKs, or libraries to access the Management API. The Management API supports off-the-shelf HTTP clients, such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com).

To get started quickly, [create an API key and make an API call](#see-also).

> [!NOTE]
> The Couchbase Capella Management API is not available for free tier operational clusters. [Upgrade your account](../billing/upgrade-account.md) to manage deployments with the Management API.

## [](#management-api-version)Versioning

The Management API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the Management API may be a non-versioned bug fix, a patch update, a minor update, or a major update. All major, minor, and patch updates increment the version number. Only non-versioned bug fixes do not change the version number as they resolve defects without altering functionality or adding new features.

New versions of the Management API, with some [exceptions](#ver-exceptions), are backward compatible, minimizing the effect on existing deployments. In most cases, you do not need to update your existing infrastructure when Couchbase releases a new version of the Management API. Features added in a new version of the Management API do not break existing deployments.

Exceptions to backward compatibility are as follows:

* Critical security fixes. Couchbase marks a vulnerable version of the Management API as unsupported when it releases a version that fixes the vulnerability. In this case, you must plan to upgrade as soon as possible.
* Fundamental architectural changes, when unavoidable.

## [](#management-api-auth)Authentication and Authorization

The Management API uses API keys for authentication and authorization. They're required for accessing endpoints exposed by the Management API.

Couchbase Capella associates API keys with [roles and permissions](../organizations/organization-projects-overview.md). To access an endpoint, an API key must have the appropriate Capella roles. The [Management API reference guide](../management-api-reference/index.md) lists the roles required for each endpoint.

When you create an API key, you can configure an allowed IP address list. Every API key has an expiration date.

To authenticate a Management API call, pass the API key as a Bearer token in the HTTP `Authorization` header.

## [](#access-put-requests)Concurrent Access and PUT Requests

To support concurrent requests, PUT requests support optimistic concurrency control, using `If-Match` headers in combination with HTTP ETags (entity tags). Exceptions are noted in the endpoint descriptions of the [Management API reference](../management-api-reference/index.md) page. A typical pattern is to do a GET request on a specified resource, which returns an ETag value. You can then include the ETag value in a PUT request to update the resource.

PUT requests ignore all fields in the body of the request that are not required. You can find the required fields for each PUT request in the [Management API reference guide](../management-api-reference/index.md).

## [](#management-api-auditing)Auditing

All requests to the Management API are audited. All endpoints support Audit fields for audit purposes, except where noted in the Management API reference guide.

Lists are paginated.

## [](#service-limits)Service Limits

Service limits set boundaries for managing clusters, App Services, and AI Services with the Management API.

Long-Running Requests

The following long-running requests are rejected with error 504, Gateway Timeout:

* Read requests taking longer than 90 seconds to process.
* Write requests taking longer than 120 seconds to process.

Rate Limiting

Requests are limited to 100 requests per minute per API key.

Payload Size

Requests and response payloads are restricted to 18 MB.

## [](#see-also)See Also

* To create an API key, see [Get Started with the Capella Operational Management API](management-api-start.md).
* To make an API call, see [Make an API Call with the Capella Operational Management API](management-api-use.md).
* For a full reference guide, see [Capella Operational Management API Reference](../management-api-reference/index.md).
* For an error reference, see [Capella Operational Management API Errors](management-api-errors.md).
* For the change log, see [Capella Operational Management API Change Log](management-api-log.md).