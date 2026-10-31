---
title: Agent Memory API for Self-Managed Deployments
description: The Agent Memory API is a REST API that allows your AI agents to
  store and retrieve persistent memory on a self-managed Agent Memory server.
pubDate: 2026-10-31T04:25:29.610Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/api-guide/pages/self-managed/api-intro.adoc
  xref: xref:agent-mem:api-guide:self-managed/api-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/api-guide/self-managed/api-intro.html)

# Agent Memory API for Self-Managed Deployments

> The Agent Memory API is a REST API that allows your AI agents to store and retrieve persistent memory on a self-managed Agent Memory server. 

This page covers all changes for the Agent Memory API.

The Agent Memory API is a REST API for the Couchbase Agent Memory server. It allows your AI agents to store and retrieve persistent memory across user sessions.

This page covers self-managed Agent Memory, where you deploy and run the Agent Memory server on your own infrastructure. Your Agent Memory server can store its data in a Capella operational cluster or a Couchbase Server Enterprise Edition cluster. For more information, see [Agent Memory for Persistent Memory Storage](../../about-agent-mem.md).

You do not need any special tools, SDKs, or libraries to access the Agent Memory API. The Agent Memory API supports off-the-shelf HTTP clients, such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com).

To explore the Agent Memory API endpoints, you can use:

* The [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md), which you can browse without running a server.
* The API explorers on your running Agent Memory server:

  * Swagger UI at `/docs`, such as `http://localhost:8080/docs`, where you can try any endpoint directly in the browser.
  * ReDoc at `/redoc`, such as `http://localhost:8080/redoc`, a read-only reference view of the full API spec.

> [!NOTE]
> The API explorers show the version of the API that your Agent Memory server runs.

## [](#agent-memory-base-url)Base URL

The base URL for the Agent Memory API is the hostname and port of your Agent Memory server:

```text
http://localhost:8080
```

> [!NOTE]
> The Agent Memory server listens on port 8080 by default.

If you run your Agent Memory server on a different host or port, replace `localhost:8080` with your host and port.

For more information, see [Deploy Self-Managed Agent Memory for Production](../../self-managed/deploy-agent-mem-prod.md).

## [](#agent-memory-version)Versioning

The Agent Memory API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the API may be a non-versioned bug fix, a patch update, a minor update, or a major update. When a non-versioned bug fix releases, the version number is not updated. When a patch, minor, or major update releases, the version number also updates.

Endpoint paths do not include the version. To check the version of your Agent Memory server, call the `GET /health` endpoint.

For more information about changes between versions, see [The Agent Memory API Change Log](api-log.md).

## [](#agent-memory-auth)Authentication and Authorization

Self-managed Agent Memory uses access tokens from your identity provider (IdP) for authentication, not Capella API keys.

By default, your Agent Memory server does not require authentication. To require authentication, connect your Agent Memory server to an IdP that supports OpenID Connect (OIDC). For more information, including the requirements for access tokens, see [Configure Authentication for Self-Managed Agent Memory](../../security/config-agent-mem-auth.md).

When your Agent Memory server requires authentication, pass the access token as a Bearer token in the HTTP `Authorization` header of each request.

> [!NOTE]
> The `GET /health` and `GET /metrics` endpoints do not require an access token.

Depending on your Agent Memory version, you can also enable role-based authorization to control which endpoints an access token can call. For more information, see [Authorization](../../agent-memory-api-reference/rest-api.md#section/Authorization) in the Agent Memory API Reference.

## [](#agent-memory-logging)Request Logging

Every Agent Memory API response includes an `X-Request-ID` header. To identify your application in the server logs, pass an optional `X-Client-ID` header with each request.

To download server logs for troubleshooting, call the `GET /logs/collect` endpoint.

## [](#agent-memory-limits)Limits and Configuration

You configure your Agent Memory server's limits with environment variables. These limits include extraction rate limits, queue size, and timeouts. For more information about the default values, see [Self-Managed Agent Memory Environment Variable Reference](../../reference/config-agent-mem-env.md).

For more information about endpoint-specific limits, such as page sizes, see the [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).

## [](#see-also)See Also

* For more information about Agent Memory, see [Agent Memory for Persistent Memory Storage](../../about-agent-mem.md).
* For a full Agent Memory API reference guide, see [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).
* For a reference of the Agent Memory API errors, see [The Agent Memory API Errors](api-errors.md).
* For the change log, see [The Agent Memory API Change Log](api-log.md).