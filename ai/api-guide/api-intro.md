---
title: Manage Deployments with AI Services APIs
description: The Couchbase Capella Management API and the Model Serving API are
  secure REST APIs that enable you to provision, deploy, and configure Capella
  AI Services.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/api-guide/pages/api-intro.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:api-guide:api-intro.adoc[]
---

[View original HTML](/ai/api-guide/api-intro.html)

# Manage Deployments with AI Services APIs

> The Couchbase Capella Management API and the Model Serving API are secure REST APIs that enable you to provision, deploy, and configure Capella AI Services. 

This page is for Capella AI Services. It covers the AI Services features in the Management API, and the Model Service API. For more information about the Management API for Capella Operational features, see [Manage Deployments with the Management API](../../cloud/management-api-guide/management-api-intro.md).

For Capella AI Services, you can use REST APIs to interact with and manage services. This includes:

* [The Management API](#management-rest-api).
* [The Model Service API](#model-service-api).

You do not need any special tools, SDKs, or libraries to access the Management API or the Model Service API. Both of these APIs support off-the-shelf HTTP clients, such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com).

To get started with the APIs, [create an API key](api-start.md) and [make an API call](api-use.md).

> [!NOTE]
> The Management API is not available for free tier operational clusters. [Upgrade your account](../../cloud/billing/upgrade-account.md) to manage deployments with the Management API.

## [](#management-rest-api)The Management API

The Capella Management API is a secure, versioned REST API provided by Couchbase Capella that allows users to manage tasks for Couchbase operational clusters, App Services, and AI Services. This includes management tasks such as scaling clusters, configuring access controls, and deploying embedding models and Large Language Models (LLMs) for AI Services.

For a full Management API reference guide, see [Management API Reference](../../cloud/management-api-reference/index.md).

### [](#management-api-version)Versioning

The Management API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the Management API may be a non-versioned bug fix, a patch update, a minor update, or a major update. When a non-versioned bug fix releases, the version number is not updated. When a patch update, a minor update, or a major update releases, the version number updates as well.

New versions of the Management API, with some exceptions, are backward compatible, minimizing the effect to existing deployments. In most cases, you’re not required to update your existing infrastructure when a new version of the Management API releases. Features added in a new version of the Management API do not break existing deployments.

Exceptions to backward compatibility are as follows:

* Critical security fixes. A vulnerable version is marked as unsupported when a fixed version releases. In this case, you must plan to upgrade as soon as possible.
* Fundamental architectural changes, when unavoidable.

### [](#management-api-auth)Authentication and Authorization

The Management API uses API keys for authentication and authorization. They’re required for accessing endpoints exposed by the Management API.

Couchbase Capella associates API keys with [roles and permissions](../../cloud/organizations/organization-projects-overview.md). To access an endpoint, an API key must have the appropriate Capella roles. The [Management API reference guide](../../cloud/management-api-reference/index.md) lists the roles required for each endpoint.

You can configure an allowed IP address list for each API key during its creation. Every API key has an expiration date.

To authenticate a Management API call, pass the API key as a Bearer token in the HTTP `Authorization` header.

### [](#access-put-requests)Concurrent Access and PUT Requests

To support concurrent requests, PUT requests support optimistic concurrency control, using `If-Match` headers in combination with HTTP ETags (entity tags). Exceptions are noted in the endpoint descriptions of the [Management API reference](../../cloud/management-api-reference/index.md) page. A typical pattern is to do a GET request on a specified resource, which returns an ETag value. You can then include the ETag value in a PUT request to update the resource.

PUT requests ignore all fields in the body of the request that are not required. You can find the required fields for each PUT request in the [Management API reference guide](../../cloud/management-api-reference/index.md).

### [](#management-api-auditing)Auditing

All requests to the Management API are audited. All endpoints support Audit fields for audit purposes, except where noted in the Management API reference guide.

Lists are paginated.

### [](#service-limits)Service Limits

Service limits set boundaries for managing clusters, App Services, and AI Services with the Management API.

Long-Running Requests

The following long-running requests are rejected with error 504, Gateway Timeout:

* Read requests taking longer than 90 seconds to process.
* Write requests taking longer than 120 seconds to process.

Rate Limiting

Requests are limited to 100 requests per minute per API key.

Payload Size

Requests and response payloads are restricted to 18 MB.

## [](#model-service-api)The Model Service API

The Model Service API is a secure, versioned inference REST API for Capella’s Model Service. Provided by Couchbase Capella AI Services, this API allows you to use your Large Language Models (LLMs) and embedding models. This includes sending inference requests and receiving outputs such as chats, completions, and embeddings.

For a full Model Service API reference guide, see [Inference API Reference](../model-service-api-reference/rest-api.md).

### [](#model-service-version)Versioning

The Model Service API uses [semantic versioning](https://semver.org). The full version number consists of 3 parts: `major.minor.patch`.

An update to the API may be a non-versioned bug fix, a patch update, a minor update, or a major update. When a non-versioned bug fix releases, the version number is not updated. When a patch update, a minor update, or a major update releases, the version number also updates.

### [](#model-service-auth)Authentication and Authorization

The Model Service API uses Model Service API keys for authentication and authorization. To access an endpoint, you must provide:

* A Model Service API key.
* A model’s connection string.

#### [](#model-service-api-keys)Model Service API Keys

Model Service API keys are different from the API keys required by the Management API. For more information about the difference in API keys, see [Get Started with AI Services APIs](api-start.md).

Couchbase Capella associates Model Service API keys with an AWS region. Your Model Service API key must have the same AWS region as the model you want it to connect to.

You can configure an allowed IP address list for each API key during its creation. Every API key has an expiration date.

To authenticate a Model Service API call, pass the API key as a Bearer token in the HTTP `` Authorization` `` header.

#### [](#model-connection-string)Model Connection String

The Model Service API uses a different base URL than the Management API. The base URL for the Model Service API is a unique string generated for every AI model you deploy. This unique string is labeled as:

* The model connection string in the Management API.
* A model’s **Model Endpoint** in the Capella UI.

### [](#model-service-auditing)Auditing

Couchbase Capella stores API requests and responses separately in audit log files. To get this information, contact Couchbase Support by [creating a Support ticket](../../cloud/support/manage-support.md).

Auditing Limits

* The maximum audit log file size is 100 MB.
* A maximum of 512 backup audit log files are retained.
* Audit logs have a retention period of 30 days.

### [](#rate-limits)Rate Limiting

Rate limits control how often you can call the Model Service API.

Calls Rate Limit

* The default limit is set to 1,000 calls per minute.

Token-Based Rate Limiting

There’s no token-based limiting.

Request Max Tokens

* If unspecified in the payload, the default max tokens is 512.

### [](#request-limits)Request Timeouts

Timeout limits set time limits for model requests.

Timeouts can be applied to:

* Queue time for the Model Service.
* Wait time for the model engine.
* Processing time for the model engine.
* Value-adds such as guardrails and caching.

Requests failing to complete within the timeout limit are rejected. These long-running request limits set time constraints for each request:

Completion Requests

* A maximum default timeout of 300 seconds (5 minutes).
* A minimum timeout of 3 seconds.

These limits are configurable in `X-cb-request-duration` header.

Embedding Requests

* A maximum default timeout of 60 seconds (1 minute).
* A minimum timeout of 3 seconds.

These limits are configurable in `X-cb-request-duration` header.

### [](#payload-limits)Payload Size Limits

Payload size limits restrict the size of a request.

File Upload Limits

* Maximum file upload size is 100 MB.
* Maximum request count per file is 1,000 requests.
* The file types allowed are JSONL files for batch processing.

### [](#access-process-limits)Concurrent Access and Processing Limits

Concurrent access and processing limits control the number of requests the Model Service API can handle simultaneously.

Worker Pool Management

* The default executor can handle up to 128 concurrent requests at a time.
* The request queue can hold up to 1,000 requests waiting to be processed.

Request Processing Priority

1. Real-time requests are always processed before batched requests.
2. Batched requests are processed after all the pending real-time requests.
3. With queue management, real-time and batched requests are placed in separate queues.

### [](#api-key-limits)API Key Limits

API key limits control usage tied to each Model Service API key.

Active API Keys

* You can have a maximum of 100 active API Keys.
* The API key expiration is configurable per API key.

API Key Caching

* The in-memory cache size is 100 entries (matches MaxActiveAPIKeys).
* The cache time to live (TTL) is 3 minutes for in-memory and 30 minutes for remote.
* The lookup timeout is 3 seconds for the cache and 30 seconds for the secrets manager.

### [](#cache-limits)Cache Limits

Cache limits control how much data the Model Service API temporarily stores in cache.

Cache Expiry

* The default cache expiry is 1 hour (3,600 seconds).
* The maximum cache expiry is 7 days.
* The minimum cache expiry is 1 hour.
* The cache expiry is configurable via the `X-cb-cache-expiry` header.

### [](#batch-limits)Batch Processing Limits

Batch processing limits control the size and number of batches the Model Service API processes at once.

Batch Configuration

* The default batch processor queue size is 1,000 requests.
* The default batch requests limit is 1,000 requests.
* The default batch file size limit is 100 MB.
* The default batch queries per second (QPS) is 100 requests per second.

Batch Record Expiry

* The default batch record expiry is 7 days.
* The default file record expiry is 30 days.
* The minimum expiry for batch and file records is 1 hour.
* The maximum batch expiry is 7 days.
* The maximum file expiry is 30 days.

### [](#model-service-errors)Error Handling and Retries

Error handling and retries define how the Model Service API responds to failures and when it attempts to repeat requests.

Retry Configuration

* The maximum number of retries is 3 attempts.
* The initial retry interval is 250 milliseconds.
* The number of retries is configurable per request via the `X-cb-max-retries` header.

## [](#see-also)See Also

* To create an API key, see [Get Started with AI Services APIs](api-start.md).
* To make an API call, see [Make an API Call with AI Services APIs](api-use.md).
* For a full Management API reference guide, see [Management API Reference](../../cloud/management-api-reference/index.md).
* For a full Model Service API reference guide, see [Inference API Reference](../model-service-api-reference/rest-api.md).
* For a reference of the Management API errors, see [Management API Error Messages ](api-errors.md#management-api-errors).
* For a reference of the AI Services Model Service API errors, see [Model Service API Error Messages ](api-errors.md#model-api-errors).
* For the change log, see [AI Services API Change Log](api-log.md).