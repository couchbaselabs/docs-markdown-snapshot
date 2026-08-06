---
title: Integrating the Data API with Cloud Native Gateway
description: How to integrate with the Data API served by Cloud Native Gateway,
  including authentication, document operations, and service passthrough.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/data-api/pages/integrating-data-api-cng.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:data-api:integrating-data-api-cng.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/data-api/integrating-data-api-cng.html)

# Integrating the Data API with Cloud Native Gateway

> How to integrate with the Data API served by Cloud Native Gateway, including authentication, document operations, and service passthrough. 

## [](#connecting-to-the-data-api)Connecting to the Data API

Cloud Native Gateway serves the Data API over HTTPS on the Data API port. The base URL depends on your deployment:

* **Kubernetes internal** — `<https://<cluster-name>-cloud-native-gateway-service.<namespace>.svc:<dapi-port>>;`
* **OpenShift Route** — `<https://<route-hostname>>;`
* **LoadBalancer** — `[:<external-port>](https://<external-ip-or-hostname>)` (the externally exposed port may differ from `<dapi-port>`, and is commonly `443`)
* **Self-managed** — `<https://<cng-host>:<dapi-port>>;`

All requests require TLS. If Cloud Native Gateway uses a self-signed certificate for development, you must configure your HTTP client to trust it or turn off certificate verification.

## [](#authentication)Authentication

Include an `Authorization` header with every request:

```console
$ curl -u Administrator:password \
    https://cng.example.com:18099/v1/callerIdentity
```

The `callerIdentity` endpoint verifies that authentication is working:

```json
{
  "user": "Administrator"
}
```

## [](#document-operations)Document Operations

This section describes the core actions you can perform with documents via the API, including retrieval, updates, and related workflows.

### [](#retrieving-a-document)Retrieving a Document

Retrieve returns the current document for the specified key if it exists.

```console
$ curl -u user:pass \
    https://cng.example.com:18099/v1/buckets/travel-sample/scopes/_default/collections/_default/documents/airline_10
```

Response:

```json
{
  "id": 10,
  "type": "airline",
  "name": "40-Mile Air",
  "iata": "Q5",
  "icao": "MLA",
  "callsign": "MILE-AIR",
  "country": "United States"
}
```

The response headers include:

* `ETag` — The CAS value for optimistic concurrency control.
* `X-CB-Flags` — The document's encoding flags.

### [](#retrieving-specific-fields)Retrieving Specific Fields

Retrieving specific fields returns only the requested fields for the specified document key. Use the `project` query parameter to retrieve only specific fields:

```console
$ curl -u user:pass \
    "https://cng.example.com:18099/v1/buckets/travel-sample/scopes/_default/collections/_default/documents/airline_10?project=name,country"
```

### [](#inserting-a-document)Inserting a Document

Insert creates a new document for the specified key only if it does not already exist.

```console
$ curl -X POST -u user:pass \
    -H "Content-Type: application/json" \
    -d '{"type": "hotel", "name": "Test Hotel", "city": "London"}' \
    https://cng.example.com:18099/v1/buckets/travel-sample/scopes/_default/collections/_default/documents/hotel_test_1
```

This fails with a `409 Conflict` if the document already exists.

### [](#upserting-a-document)Upserting a Document

Upsert creates the document if it does not exist or replaces it if it does.

```console
$ curl -X PUT -u user:pass \
    -H "Content-Type: application/json" \
    -d '{"type": "hotel", "name": "Updated Hotel", "city": "Paris"}' \
    https://cng.example.com:18099/v1/buckets/travel-sample/scopes/_default/collections/_default/documents/hotel_test_1
```

### [](#removing-a-document)Removing a Document

Remove deletes the document for the specified key if it exists.

```console
$ curl -X DELETE -u user:pass \
    https://cng.example.com:18099/v1/buckets/travel-sample/scopes/_default/collections/_default/documents/hotel_test_1
```

### [](#optimistic-concurrency-with-cas)Optimistic Concurrency with CAS

CAS applies the mutation only if the document's current CAS matches the `If-Match` value from the earlier read. Use the `ETag` header from a GET response as the `If-Match` header on a subsequent mutation to verify the document has not changed:

```console
$ curl -X PUT -u user:pass \
    -H "Content-Type: application/json" \
    -H "If-Match: \"1234567890\"" \
    -d '{"type": "hotel", "name": "Concurrent Update"}' \
    https://cng.example.com:18099/v1/buckets/travel-sample/scopes/_default/collections/_default/documents/hotel_test_1
```

If the document changed since the GET, the server returns `409 Conflict`.

## [](#service-passthrough)Service Passthrough

The `/_p/` prefix proxies requests to Couchbase service REST APIs.

### [](#executing-a-sql-query)Executing a SQL++ Query

```console
$ curl -X POST -u user:pass \
    -H "Content-Type: application/json" \
    -d '{"statement": "SELECT name, city FROM `travel-sample` WHERE type = \"hotel\" LIMIT 5"}' \
    https://cng.example.com:18099/_p/query/query/service
```

### [](#executing-a-search-service)Executing a Search Service

```console
$ curl -X POST -u user:pass \
    -H "Content-Type: application/json" \
    -d '{
      "query": {"match": "London", "field": "city"},
      "size": 5
    }' \
    https://cng.example.com:18099/_p/fts/api/index/travel-sample-index/query
```

The passthrough proxy forwards requests to the appropriate Couchbase service using Cloud Native Gateway's cluster credentials with On-Behalf-Of semantics. Cloud Native Gateway checks the request against the calling user's permissions.

## [](#error-handling)Error Handling

The Data API returns standard HTTP status codes with JSON error bodies:

| HTTP Status | Error Code                  | Description                                                               |
| ----------- | --------------------------- | ------------------------------------------------------------------------- |
| 400         | InvalidArgument             | The request contains invalid parameters or a malformed body.              |
| 401         | Unauthenticated             | Authentication credentials are missing or invalid.                        |
| 403         | Forbidden                   | The authenticated user does not have sufficient permissions.              |
| 404         | DocumentNotFound            | The requested document does not exist.                                    |
| 409         | AlreadyExists / CasMismatch | Document already exists on insert, or CAS mismatch on conditional update. |
| 429         | Rate limited                | Request rate limit exceeded.                                              |
| 500         | Internal                    | An internal error occurred.                                               |