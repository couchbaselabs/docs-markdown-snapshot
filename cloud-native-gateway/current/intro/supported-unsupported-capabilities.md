---
title: Supported and Unsupported Capabilities
description: An overview of which Couchbase services, SDK versions, and features
  are supported through Cloud Native Gateway, along with known limitations.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/intro/pages/supported-unsupported-capabilities.adoc
  xref: xref:cloud-native-gateway:intro:supported-unsupported-capabilities.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/intro/supported-unsupported-capabilities.html)

# Supported and Unsupported Capabilities

> An overview of which Couchbase services, SDK versions, and features are supported through Cloud Native Gateway, along with known limitations. 

## [](#supported-couchbase-services)Supported Couchbase Services

Cloud Native Gateway provides access to the following Couchbase Server services through the Protostellar gRPC interface:

| Service                       | Capabilities                                                                                                                                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KV (Data)**                 | All standard Couchbase Key-Value capabilities except: Multi-document Transactions and KV RangeScan.                                                                                                  |
| **Query (SQL++)**             | Full N1QL query execution with streaming results, prepared statements, parameterized queries, scan consistency, and query-level metrics. Multi-document transactions are not supported at this time. |
| **Search (Full-Text Search)** | All standard Couchbase FTS capabilities are supported (including KNN vector search, facets, sorting, highlighting, and index administration) with no exceptions.                                     |
| **Administration**            | Bucket management (create, update, delete, list), collection management (create, delete, list scopes and collections), query index administration, search index administration.                      |

The following services are available through the **Data API** (REST interface):

* Document CRUD (Get, Upsert, Insert, Replace, Remove).
* Sub-Document lookups and mutations.
* Binary operations (Append, Prepend, Increment, Decrement).
* Locking operations (GetAndLock, Unlock).
* Passthrough access to Query, Search, and Analytics REST APIs.

## [](#supported-couchbase-sdks)Supported Couchbase SDKs

The Protostellar protocol (using the `couchbase2://` connection scheme) is supported in at least the following Couchbase SDKs:

| SDK         | Minimum Version | Status              |
| ----------- | --------------- | ------------------- |
| Java SDK    | Since 3.5.0     | Generally Available |
| Kotlin SDK  | Since 1.2.0     | Generally Available |
| Scala SDK   | Since 1.5.0     | Generally Available |
| Go SDK      | Since 2.7.0     | Generally Available |
| .NET SDK    | Since 3.9.0     | Generally Available |
| Python SDK  | 4.2.0           | Volatile            |
| Ruby SDK    | 3.5.0           | Volatile            |
| Node.js SDK | 4.3.0           | Volatile            |

> [!NOTE]
> "Volatile" stability means the feature is available for experimental use but the interface may be incomplete or change in future releases. Check the SDK release notes for the latest status.

You can use the Data API from any HTTP client (curl, Postman, or HTTP client libraries) that supports HTTPS, without requiring an SDK.

## [](#supported-couchbase-server-versions)Supported Couchbase Server Versions

Cloud Native Gateway requires **Couchbase Server 7.2.2 or later**. Cloud Native Gateway validates the cluster server version at startup and logs a warning if the connected cluster is running an earlier version.

Couchbase Enterprise Analytics directly provides an HTTPS service endpoint and does not require a separate gateway to provide load balanced access to the Analytics SDKs.

## [](#known-limitations)Known Limitations

The following capabilities are **not available** through Cloud Native Gateway:

### [](#removed-by-design)Removed by Design

* **Legacy (client-side) durability** \- Couchbase does not support the older observe-based durability mechanism. Use synchronous replication instead (durability levels: Majority, MajorityAndPersistToActive, PersistToMajority).
* **Cluster capabilities negotiation** \- By design, the gateway gracefully handles differences in cluster capabilities across versions. If you attempt to use an unsupported feature, Cloud Native Gateway returns an `UNIMPLEMENTED` error.
* **Topology awareness at the client** \- Cloud Native Gateway handles all routing cluster-side. Clients do not receive cluster topology information.
* **Circuit breakers (client-side)** \- Client-side circuit breakers do not apply since Cloud Native Gateway abstracts the topology. Cloud Native Gateway monitors backend health and routes around failures.

### [](#not-yet-implemented)Not Yet Implemented

* **Eventing Service** \- Not exposed through Protostellar.
* **Views** \- The Views Service is not supported.
* **XDCR management** \- XDCR administration is not part of the public Protostellar specification.
* **Backup and Restore** \- The Couchbase Backup Service or `cbbackupmgr` handles these operations outside Cloud Native Gateway and depends on lower level network interfaces.

### [](#behavioral-differences)Behavioral Differences

* **Orphaned response reporting** \- In the classic protocol, the SDK tracks responses that arrive after the client has timed out. With Protostellar, request deadlines allow the server to discard expired work, so orphaned responses are no longer generated.
* **Retry observability** \- Cloud Native Gateway handles retries server-side, so the client may not have visibility into the number of retry attempts. Diagnostic information is available through Cloud Native Gateway's logging and metrics instead.