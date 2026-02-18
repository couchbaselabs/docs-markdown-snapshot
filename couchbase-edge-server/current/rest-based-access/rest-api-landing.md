---
title: Edge Server REST API
description: Couchbase Edge Server has a REST API that enables you to get
  database information, perform document operations, run SQL++ queries, and
  manage replication.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/rest-based-access/pages/rest-api-landing.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-edge-server/current/rest-based-access/rest-api-landing.html)

# Edge Server REST API

> Couchbase Edge Server has a REST API that enables you to get database information, perform document operations, run SQL++ queries, and manage replication. 

Clients do not need any special tools, SDKs, or libraries to access the Edge Server REST API. The REST API supports off-the-shelf HTTP clients, such as [Insomnia](https://insomnia.rest) or [Postman](https://www.postman.com).

## [](#versioning)Versioning

To allow for future changes, the REST API is versioned. The current version is 1.0.

Requests may include an `API-Version` header to specify the API version. If omitted, it defaults to `1.0`. Currently, versioning is optional, but future releases may introduce other versions of the Edge Server REST API.

## [](#concurrent-access-and-revision-numbers)Concurrent Access and Revision Numbers

To support concurrent requests, the REST API supports optimistic concurrency control, using query parameters or `If-Match` headers in combination with revision numbers. Details are noted in the endpoint descriptions. A typical pattern is to do a GET request on a specified resource, which returns a revision number. You can then include the revision number in a PUT or DELETE request to update the resource.

## [](#see-also)See Also

* [Get Started with the Edge Server REST API](rest-api-start.md)
* [Database Operations with Edge Server](database-operations.md)
* [Document Access with Edge Server](document-access.md)
* [Monitor Changes with Edge Server](changes-feed.md)
* [Run Queries with Edge Server](queries-api.md)
* [Manage Replication with Edge Server](replication.md)
* [Edge Server Public REST API](../public-api-reference/index.md)