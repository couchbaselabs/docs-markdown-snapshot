---
title: About Data API
description: The Data API is a RESTful HTTPS interface in Cloud Native Gateway
  for document operations and passthrough access to Query, Search, and
  Analytics.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/data-api/pages/data-API-overview.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:data-api:data-API-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/data-api/data-API-overview.html)

# About Data API

> The Data API is a RESTful HTTPS interface in Cloud Native Gateway for document operations and passthrough access to Query, Search, and Analytics. 

## [](#whats-the-data-api)What's the Data API?

The Data API is a RESTful HTTP interface that lets you read and write data stored in Couchbase Server. It's served by Cloud Native Gateway on a dedicated HTTPS port alongside the gRPC Protostellar interface.

The Protostellar gRPC interface targets Couchbase SDKs. Use the Data API for:

* **Environments without a native SDK** — Languages or platforms where a Couchbase SDK is not available or practical.
* **Lightweight integrations** — FaaS/Lambda functions, webhooks, and low-code tools where a full SDK is not needed.
* **Direct REST use** — Debugging, scripting, and administrative tasks where tools like `curl` or Postman are more convenient than an SDK.
* **Browser-based applications** — The Data API supports CORS, making it usable from browser-based JavaScript applications.

## [](#api-structure)API Structure

An OpenAPI 3.0 specification defines the Data API. It serves endpoints under the `/v1/` path prefix.

### [](#document-operations)Document Operations

Address all document operations using the full document path:

```none
/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}
```

Supported operations:

| HTTP Method | Operation       | Description                                                                                   |
| ----------- | --------------- | --------------------------------------------------------------------------------------------- |
| GET         | Get Document    | Retrieves a document by key. Supports field-level projection via the project query parameter. |
| POST        | Insert Document | Creates a new document. Fails if the document already exists.                                 |
| PUT         | Upsert Document | Creates or replaces a document unconditionally.                                               |
| DELETE      | Remove Document | Deletes a document by key.                                                                    |

### [](#utility-endpoints)Utility Endpoints

* `GET /v1/callerIdentity` \- Returns the authenticated identity of the current request. Useful for verifying that authentication works.

### [](#service-passthrough)Service Passthrough

The Data API also proxies requests to Couchbase service REST APIs under the `/_p/` path prefix:

* `/_p/query/` \- SQL++ Query Service
* `/_p/fts/` \- Search Service
* `/_p/cbas/` \- CBAS Analytics Service

This lets you run SQL++ queries, Search Service queries and analytics through a single endpoint.

## [](#how-it-works)How It Works

The Data API maps HTTP requests to either Couchbase KV operations or proxied service requests.

### [](#document-operations-request-flow)Document Operations Request Flow

1. A client sends an HTTPS request to a `/v1/…​` endpoint such as a document path or `callerIdentity`.
2. Cloud Native Gateway routes the request and parses the path, query, and header values.
3. The gateway authenticates the caller and resolves an on-behalf-of identity. For document operations, it then finds the target bucket and runs the KV operation.
4. HTTP concepts map to Couchbase data semantics. For example, `ETag` maps to CAS, `Expires` maps to TTL, and `X-CB-*` headers carry flags and mutation metadata.
5. Cloud Native Gateway converts the response back to HTTP. It returns content as JSON, text, or binary based on document flags. The response can include metadata such as `ETag`, `Expires`, `X-CB-Flags`, and `X-CB-MutationToken`.

### [](#passthrough-request-flow)Passthrough Request Flow

1. A client sends a request to one of the `/_p/…​` prefixes.
2. Cloud Native Gateway selects a Couchbase service endpoint based on the current cluster topology. Clients use a single Data API entry point instead of managing separate Query, Search, or Analytics endpoints.
3. The gateway forwards the HTTP method, path, query string, headers, and body to the backend service.
4. When clients use a certificate instead of an `Authorization` header, the gateway validates it and forwards the request using an On-Behalf-Of identity.
5. The backend service streams its response back to the client, preserving the HTTP status and headers.

### [](#error-handling)Error Handling

The Data API normalizes KV and service errors into a consistent JSON error format. Where available, responses include the affected resource and request context. Clients can use this to distinguish authorization failures, Compare and Swap mismatches, and similar conditions.

```json
{
  "code": "BucketNotFound",
  "message": "bucket not found",
  "resource": "/buckets/invalid-bucket"
}
```

## [](#authentication)Authentication

All Data API requests require authentication.

* **Basic authentication** \- `Authorization: Basic <base64(username:password)>`
* **TLS client certificate authentication** \- Use this when Cloud Native Gateway has a client Certificate Authority certificate.

## [](#next-steps)Next Steps

* [Integrating the Data API with Cloud Native Gateway](integrating-data-api-cng.md) \- How to integrate the Data API into your applications.
* [Exposing the Data API](exposing-data-api.md) \- How to expose the Data API to different network environments.
* [Limits, Pricing, and Performance Considerations](limits-pricing-performance-considerations.md) \- Rate limits, sizing, and performance guidance.