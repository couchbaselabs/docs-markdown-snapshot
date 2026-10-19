---
title: Agent Memory APIs for Managed Deployments
description: The Couchbase Capella Management API and the Agent Memory API are
  secure REST APIs that enable you to deploy Agent Memory servers and store and
  retrieve memory for your AI agents.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/api-guide/pages/managed/api-intro.adoc
  xref: xref:agent-mem:api-guide:managed/api-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/api-guide/managed/api-intro.html)

# Agent Memory APIs for Managed Deployments

> The Couchbase Capella Management API and the Agent Memory API are secure REST APIs that enable you to deploy Agent Memory servers and store and retrieve memory for your AI agents. 

This page is for Agent Memory in Capella. It covers the Agent Memory features in the Management API, and the Agent Memory API. For more information about the Management API for Capella Operational features, see [Manage Deployments with the Capella Operational Management API](../../../../cloud/management-api-guide/management-api-intro.md).

For Agent Memory in Capella, you can use REST APIs to deploy Agent Memory servers and store and retrieve memory. This includes:

* [The Management API](#management-rest-api).
* [The Agent Memory API](#agent-memory-api).

You do not need any special tools, SDKs, or libraries to access the Management API or the Agent Memory API. Both of these APIs support off-the-shelf HTTP clients, such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com).

To get started with the APIs, [create an API key](api-start.md) and [make an API call](api-use.md).

> [!NOTE]
> The Management API is not available for free tier operational clusters. [Upgrade your account](../../../../cloud/billing/upgrade-account.md) to manage deployments with the Management API.

## [](#management-rest-api)The Management API

The Capella Management API is a secure, versioned REST API provided by Couchbase Capella that allows users to manage tasks for Couchbase operational clusters, App Services, and the AI Data Plane. For Agent Memory in Capella, this includes management tasks such as deploying Agent Memory servers and creating Agent Memory API keys.

For a full Management API reference guide, see [Couchbase Capella Management API Reference](../../../../cloud/management-api-reference/index.md).

### [](#management-api-version)Versioning

The Management API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the Management API may be a non-versioned bug fix, a patch update, a minor update, or a major update. All major, minor, and patch updates increment the version number. Only non-versioned bug fixes do not change the version number as they resolve defects without altering functionality or adding new features.

New versions of the Management API, with some [exceptions](#ver-exceptions), are backward compatible, minimizing the effect on existing deployments. In most cases, you do not need to update your existing infrastructure when Couchbase releases a new version of the Management API. Features added in a new version of the Management API do not break existing deployments.

Exceptions to backward compatibility are as follows:

* Critical security fixes. Couchbase marks a vulnerable version of the Management API as unsupported when it releases a version that fixes the vulnerability. In this case, you must plan to upgrade as soon as possible.
* Fundamental architectural changes, when unavoidable.

### [](#management-api-auth)Authentication and Authorization

The Management API uses API keys for authentication and authorization. They're required for accessing endpoints exposed by the Management API.

Couchbase Capella associates API keys with [roles and permissions](../../../../cloud/organizations/organization-projects-overview.md). To access an endpoint, an API key must have the appropriate Capella roles. The [Management API reference guide](../../../../cloud/management-api-reference/index.md) lists the roles required for each endpoint.

When you create an API key, you can configure an allowed IP address list. Every API key has an expiration date.

To authenticate a Management API call, pass the API key as a Bearer token in the HTTP `Authorization` header.

### [](#access-put-requests)Concurrent Access and PUT Requests

To support concurrent requests, PUT requests support optimistic concurrency control, using `If-Match` headers in combination with HTTP ETags (entity tags). Exceptions are noted in the endpoint descriptions of the [Management API reference](../../../../cloud/management-api-reference/index.md) page. A typical pattern is to do a GET request on a specified resource, which returns an ETag value. You can then include the ETag value in a PUT request to update the resource.

PUT requests ignore all fields in the body of the request that are not required. You can find the required fields for each PUT request in the [Management API reference guide](../../../../cloud/management-api-reference/index.md).

### [](#management-api-auditing)Auditing

All requests to the Management API are audited. All endpoints support Audit fields for audit purposes, except where noted in the Management API reference guide.

Lists are paginated.

### [](#service-limits)Service Limits

Service limits set boundaries for managing clusters, App Services, and the Couchbase AI Data Plane with the Management API.

Long-Running Requests

The following long-running requests are rejected with error 504, Gateway Timeout:

* Read requests taking longer than 90 seconds to process.
* Write requests taking longer than 120 seconds to process.

Rate Limiting

Requests are limited to 100 requests per minute per API key.

Payload Size

Requests and response payloads are restricted to 18 MB.

## [](#agent-memory-api)The Agent Memory API

The Agent Memory API is a REST API for the Couchbase Agent Memory server. It allows your AI agents to store and retrieve persistent memory across user sessions.

With Agent Memory in Capella, Capella deploys and runs your Agent Memory server and connects it to your Capella operational cluster. For more information, see [Deploy Managed Agent Memory](../../managed/deploy-agent-mem-managed.md).

For a full Agent Memory API reference guide, see [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).

### [](#agent-memory-version)Versioning

The Agent Memory API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the API may be a non-versioned bug fix, a patch update, a minor update, or a major update. When a non-versioned bug fix releases, the version number is not updated. When a patch update, a minor update, or a major update releases, the version number also updates.

Endpoint paths do not include the version. To check the version of your Agent Memory server, call the `GET /health` endpoint.

For more information about changes between versions, see [The Agent Memory API Change Log](api-log.md).

### [](#agent-memory-auth)Authentication and Authorization

To access your server, you must have:

* Your [Agent Memory API key](#agent-memory-api-keys) configured with an access level.
* Your [Agent Memory endpoint](#agent-memory-endpoint).
* Added to your Agent Memory server's [allowed IP address list](#agent-memory-ip-access).

#### [](#agent-memory-api-keys)Agent Memory API Keys

Agent Memory API keys are different from the API keys required by the Management API. A Management API key gives access to your Capella organization, while an Agent Memory API key gives access to an Agent Memory server.

Each API key for the Agent Memory API has the following characteristics:

* Every API key works with only 1 Agent Memory server. To access more than 1 Agent Memory server, [create a separate API key](api-start.md#generate-agent-memory-keys) for each server.
* Every API key has an [access level](#access-level).
* Every API key has an expiration date. By default, each API key expires 30 days after creation. You can [specify a different expiration, or specify that the API key does not expire](api-start.md#generate-agent-memory-keys). For security, you should let API keys expire and create new API keys regularly.

For more information about how to create Agent Memory API keys, see [Agent Memory API Keys](api-start.md#agent-memory-keys).

Access Levels

When you create an API key, you choose its access level:

| Access | Role       | Description                                                                                                                                                                      |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Read   | ams\_ro    | Read-only access to the Agent Memory server. This includes the ability to search, list, and get memory.                                                                          |
| Write  | ams\_rw    | Read and write access to the Agent Memory server. Everything in Read, plus the ability to add, update, and delete memory, sessions, and users. This is the default access level. |
| Admin  | ams\_admin | Full access to the Agent Memory server, including administrative operations. Everything in Write, plus the ability to list users, manage custom prompts, and collect logs.       |

For more information about access levels, see [Authentication](../../agent-memory-api-reference/rest-api.md#section/Authentication).

#### [](#agent-memory-endpoint)Agent Memory Server Endpoint

The Agent Memory API uses a different base URL than the Management API. The base URL for the Agent Memory API is your Agent Memory server's endpoint. Each Agent Memory server has a unique endpoint that uses HTTPS.

Capella labels the unique endpoint as:

* `network.endpoint` in the Management REST API.
* A server's **Endpoint** in the Capella UI.

For more information about how to copy your Agent Memory server endpoint, see [Agent Memory Server Endpoint](api-start.md#agent-memory-endpoint).

#### [](#agent-memory-ip-access)IP Access

Each Agent Memory server has an allowed IP address list. Your Agent Memory server only accepts requests from IP addresses in its allowed IP address list. A new Agent Memory server has no allowed IP addresses, so it blocks all requests until you add at least 1.

For more information about how to add allowed IP addresses, see [Allowed IP Addresses](api-start.md#agent-memory-allowed-ips).

### [](#agent-memory-logging)Request Logging

Every Agent Memory API response includes an `X-Request-ID` header. To identify your application in the server logs, pass an optional `X-Client-ID` header with each request.

### [](#agent-memory-limits)Limits and Configuration

You set your Agent Memory server's limits when you [deploy the server](../../managed/deploy-agent-mem-managed.md#server-settings). These limits include extraction rate limits, queue size, and timeouts. You cannot change the configuration of a deployed Agent Memory server. For more information, see [Changing Your Configuration](../../managed/deploy-agent-mem-managed.md#change-config).

For more information about endpoint-specific limits, such as page sizes, see the [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).

## [](#see-also)See Also

* To create an API key, see [Get Started with the Agent Memory APIs](api-start.md).
* To make an API call, see [Make an API Call with the Agent Memory APIs](api-use.md).
* For a full Management API reference guide, see [Couchbase Capella Management API Reference](../../../../cloud/management-api-reference/index.md).
* For a full Agent Memory API reference guide, see [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).
* For a reference of the Management API and Agent Memory API errors, see [The Agent Memory API Errors](api-errors.md).
* For the change log, see [The Agent Memory API Change Log](api-log.md).