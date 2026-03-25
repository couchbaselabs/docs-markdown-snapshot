---
title: Import Process
description: Sync Gateway replication keeps distributed database changes in sync
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/import-process.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::import-process.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/import-process.html)

# Import Process

> Sync Gateway replication keeps distributed database changes in sync  
> This content explaina how Sync Gateway synchronizes document changes made through Couchbase SDKs and N1QL queries.

Related _Sync_ topics: [Configuration Properties](../current/configuration/configuration-properties-legacy.md) | [Admin REST API](../current/rest-api/rest-api-admin.md)

## [](#introduction)Introduction

The import process is a key part of mobile convergence. It is the means by which Sync Gateway becomes aware of non-Sync Gateway data changes and obtains the mobile metadata it requires to replicate changes.

![shared bucket access](_images/shared-bucket-access.png) 

Any non-Sync Gateway change is eligible for import. The document is first run through the Sync Function to compute read security and routing, with the following differences:

* The import is processed with an admin user context in the Sync Function, similar to writes made through the Sync Gateway Admin API. This means that `requireAccess`, `requireUser` and `requireRole` calls in the Sync Function are treated as no-ops.
* During import, `oldDoc` is `nil` when the Sync Function is executed.

You can specify a filter function using the [import\_filter](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb%5Fimport%5Ffilter) property, which will only import specific documents.

> [!TIP]
> Use the [Import+](../current/configuration/configuration-properties-legacy.md#log) log key to troubleshoot import processing issues in the logs.

## [](#configuration)Configuration

Note that `import_docs` only takes effect if the `enabled_shared_bucket_access` is set to `true`.

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

The `import_docs` parameter defaults to `true`, implying that, by default, all nodes in a cluster participate in import processing. To exclude a node, set `"import_docs": false`.

[COMMUNITY EDITION](https://www.couchbase.com/products/editions)

The `import_docs` parameter defaults to false and must be explicitly set to `true`.

The following table describes the key behavior differences between Community Edition and Enterprise Edition when `import_docs` is enabled, disabled or not set at all.

| enabled\_shared\_bucket\_access | import\_docs | Behavior (EE)                                                              | Behavior (CE)                                             |
| ------------------------------- | ------------ | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| true                            | not set      | Assumes import: true by default                                            | Assumes import: false by default                          |
| true                            | false        | Node omitted from import processing (supported for workload isolation)     | Node omitted from import processing                       |
| true                            | true         | Node participates in import processing, and is assigned import partitions. | Node performs import processing for all server mutations. |
| false                           | not set      | import docs is false by default                                            | import docs is false by default                           |
| false                           | true         | import docs property ignored, warning logged                               | import docs property ignored, warning logged              |
| false                           | false        | Import docs is false                                                       | Import docs is false                                      |

## [](#high-availability)High Availability

In _Enterprise Edition_, import processing work is sharded across all Sync Gateway nodes with import enabled. This implies that if one of the nodes fail, the failed shard is automatically picked up by the remaining nodes in the cluster. This way, you get High Availability of import processing.

In _Community Edition_, there is no sharding of import across the nodes participating in the import processing. Each import node processes all server mutations.

## [](#workload-isolation)Workload Isolation

As described in the table above, if `import_docs` is set to `false`, the node will not be participating in the import process. This configuration is specifically recommended for workload isolation: to isolate import nodes from the client-facing nodes. Workload isolation may be preferable in deployments with high write throughput.

The following diagram shows an example architecture of two Sync Gateway nodes handling the incoming client connections (`import_docs: false`) and two nodes sharing the import processing (`import_docs: true`).

![workload isolation](_images/workload-isolation.png)

## [](#reference)Reference

The reference to the configuration properties can be found below.

* [$dbname.enable\_shared\_bucket\_access](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-enable%5Fshared%5Fbucket%5Faccess) to enable convergence for a given database.
* [$dbname.import\_docs](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-import%5Fdocs) to give a particular Sync Gateway node the role of importing the documents.
* [$dbname.import\_filter](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter) to select which document(s) to make aware to mobile clients.

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)