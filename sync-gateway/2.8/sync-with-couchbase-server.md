---
title: Sync with Couchbase Server
description: Use Sync Gateway to sync Couchbase Server changes securely from cloud to edge
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/sync-with-couchbase-server.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::sync-with-couchbase-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/sync-with-couchbase-server.html)

# Sync with Couchbase Server

> Use Sync Gateway to sync Couchbase Server changes securely from cloud to edge  
> This content explains how Sync Gateway synchronizes document changes made through Couchbase SDKs and N1QL queries.

Related _Sync_ topics: [Sync with Couchbase Lite](../current/sync/sync-using-app.md) | [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md) | [Delta Sync](../current/sync/delta-sync.md) | [Resync](../current/manage/resync.md)

> [!NOTE]
> Users of Couchbase Server 6.0 should ensure they have addressed the known issue ([MB-41255](https://issues.couchbase.com/browse/MB-41255)) by upgrading to one of the recommended Couchbase Server versions (6.0.5, 6.5.2, or 6.6.1).
> 
> The known issue can cause re-balance failures and/or failed replica writes of deleted or expired documents that use Xattrs.
> 
> This impacts Sync Gateway deployments running with shared bucket access enabled, which use Xattrs for metadata storage.

## [](#introduction)Introduction

Sync Gateway uses the [Shared Bucket Access](#sba-feature) and [Import Processing](#import-process) features to synchronize document changes made through Couchbase Server with those made by Sync Gateway and Couchbase Lite clients, and vice versa \[[1](#%5Ffootnotedef%5F1 "View footnote.")\].

* Shared Bucket Access — this is mechanism that enables Couchbase Server's SDK applications, N1QL Queries, Sync Gateway and Couchbase Lite applications to read and write to the same bucket simultaneously — see: [Figure 1](#sgw-paths) and the configuration property [$dbname.enable\_shared\_bucket\_access](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-enable%5Fshared%5Fbucket%5Faccess)
* Import Processing — is the mechanism by which Sync Gateway becomes aware of non-Sync Gateway data changes and then obtains the mobile metadata it requires to replicate those changes — see: [Import Processing](#import-process).

## [](#sba-feature)Shared Bucket Access

![shared bucket access](_images/shared-bucket-access.png) 

Figure 1\. Sync Gateway Data Access Paths

### [](#documents)Documents

With bucket-sharing enabled, Couchbase Server documents can be inserted directly (using _N1QL_ or _SDKs_) or by using Sync Gateway's [Public REST API](../current/rest-api/rest-api.md).

Sync Gateway \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] creates the metadata it needs by abstracting it from the SDK or N1QL applications reading and writing data directly to Couchbase Server buckets. It uses Couchbase Server XATTRs \[[3](#%5Ffootnotedef%5F3 "View footnote.")\] to store that metadata into an external document fragment — see [Extended Attributes (XATTR)](../../server/current/learn/data/extended-attributes-fundamentals.md).

The REST API will also include the following behavioral changes:

* Purging — [/{db}/\_purge](../current/rest-api/rest-api-admin.md#/document/post%5F%5Fdb%5F%5F%5Fpurge) removes the document and its associated extended attributes
* Updating — [put /{db}/{docid}](../current/rest-api/rest-api-admin.md#/document/put%5F%5Fdb%5F%5F%5Fdoc%5F) will tombstone the active revision

### [](#blobs-and-attachments)Blobs and Attachments

Couchbase Server SDK/N1QL

Use Sync Gateway's REST API's [/{db}/{docid}/{attachment}](../current/rest-api/rest-api-admin.md#/attachment) endpoints to manage attachments and blob data; you cannot use Couchbase Server SDKs to do this directly.

Standard practice would be to create the document using the SDK and then associate its blobs/attachments using the [Add/Update Attachment (/{db}/{docid}/{attachment})](../current/rest-api/rest-api-admin.md#/attachment/put%5F%5Fdb%5F%5F%5Fdoc%5F%5F%5Fattachment%5F) endpoint. You can see a practical example in this blog post — <https://blog.couchbase.com/store-sync-binary-data-attachments-blobs-couchbase-mobile>

Couchbase Lite Apps

Couchbase Lite apps seamlessly handle blobs and attachments, see the appropriate platform examples here:

Related Couchbase Lite content

[Android](#2.8@couchbase-lite:android:learn/blob.adoc) | [C#](#2.8@couchbase-lite:csharp:learn/blob.adoc) | [Java](#2.8@couchbase-lite:java:learn/blob.adoc) | [Objective-C](#2.8@couchbase-lite:objc:learn/blob.adoc) | [Swift](#2.8@couchbase-lite:swift:learn/blob.adoc)

Using a WebApp

Attachments can be accessed through Sync Gateway's REST API using the [/{db}/{doc}/{attachment}](rest-api.md#/attachment/get%5F%5Fdb%5F%5F%5Fdoc%5F%5F%5Fattachment%5F) endpoint.

### [](#tombstone-revisions)Tombstone Revisions

Note that, with bucket-sharing enabled, [tombstone revision![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#tombstone-revision)s are **not** retained indefinitely; they are purged based on the server's _metadata purge interval_.

To ensure tombstones are synced with clients, you should set the server's metadata purge interval based on your expected replication frequency — see the [$dbname.enable\_shared\_bucket\_access](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-enable%5Fshared%5Fbucket%5Faccess) reference.

### [](#accessing-sync-metadata)Accessing Sync Metadata

Mobile metadata is not kept in the document, but in a system extended attribute (XATTR) in Couchbase Server.

The N1QL query language \[[3](#%5Ffootnotedef%5F3 "View footnote.")\] supports the ability to query these extended attributes (XATTRS) and hence the document's sync metadata — see: [Example 1](#simple-query).

Example 1\. Querying XATTRS-bsed sync metadata

```sql
SELECT meta().xattrs._sync FROM `travel-sample` WHERE meta().id = "mydocId"
```

> [!WARNING]
> The sync metadata is maintained internally by Sync Gateway and its structure can change at any time. It should not be used to drive business logic of applications. The direct use of the N1QL query is **unsupported** and must not be used in production environments.

### [](#enable-shared-bucket-access)Enable Shared Bucket Access

Shared bucket access is an opt-in feature. You can enable it without bringing down the entire Sync Gateway cluster — see [Example 2](#enable-sba).

Example 2\. Enable Bucket-Sharing

```json
{
    "databases": {
        "db": {
            "bucket": "my-bucket",
            "username": "my-user",
            "password": "my-password",
            "server": "http://localhost:8091",
            "enable_shared_bucket_access": true, (1)
            "import_docs": true (2)
        }
    }
}
```

| **1** | The enable\_shared\_bucket\_access property is used to enable bucket-sharing. It must be _true_ on all nodes participating in such a configuration.                                                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The import\_docs property is used to specify that a Sync Gateway node participates (exclusively) in [Import Processing](#sync-gateway::import-process.adoc). The mechanism by which Sync Gateway incorporates changes to data buckets it shares with Couchbase Server — see: [Import Processing](#import-process). |

### [](#reference)Reference

Configuration file references:

* [$dbname.enable\_shared\_bucket\_access](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-enable%5Fshared%5Fbucket%5Faccess) to enable convergence for a given database.
* [$dbname.import\_docs](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-import%5Fdocs) to give a particular Sync Gateway node the role of importing the documents.
* [$dbname.import\_filter](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter) to select which document(s) to make aware to mobile clients.

## [](#import-process)Import Processing

The **import process** is a key part of mobile convergence. It is the means by which Sync Gateway becomes aware of non-Sync Gateway data changes and obtains the mobile metadata it requires to replicate changes.

![shared bucket access](_images/shared-bucket-access.png) 

Any non-Sync Gateway change is eligible for import. The document is first run through the Sync Function to compute read security and routing, with the following differences:

* The import is processed with an admin user context in the Sync Function, similar to writes made through the Sync Gateway Admin API. This means that `requireAccess`, `requireUser` and `requireRole` calls in the Sync Function are treated as no-ops.
* During import, `oldDoc` is `nil` when the Sync Function is executed.

You can specify a filter function using the [import\_filter](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb%5Fimport%5Ffilter) property, which will only import specific documents.

> [!TIP]
> Use the [Import+](../current/configuration/configuration-properties-legacy.md#log) log key to troubleshoot import processing issues in the logs.

### [](#configuration)Configuration

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

### [](#high-availability)High Availability

In _Enterprise Edition_, import processing work is sharded across all Sync Gateway nodes with import enabled. This implies that if one of the nodes fail, the failed shard is automatically picked up by the remaining nodes in the cluster. This way, you get High Availability of import processing.

In _Community Edition_, there is no sharding of import across the nodes participating in the import processing. Each import node processes all server mutations.

### [](#workload-isolation)Workload Isolation

As described in the table above, if `import_docs` is set to `false`, the node will not be participating in the import process. This configuration is specifically recommended for workload isolation: to isolate import nodes from the client-facing nodes. Workload isolation may be preferable in deployments with high write throughput.

The following diagram shows an example architecture of two Sync Gateway nodes handling the incoming client connections (`import_docs: false`) and two nodes sharing the import processing (`import_docs: true`).

![workload isolation](_images/workload-isolation.png)

### [](#reference-2)Reference

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

---

[1](#%5Ffootnoteref%5F1). Prior to Release 2.5, Server 5.0 all writes had to go through Sync Gateway, or had to use bucket shadowing to ensure that the security and replication metadata needed by mobile applications was preserved. 

[2](#%5Ffootnoteref%5F2). As of Sync Gateway 1.5 

[3](#%5Ffootnoteref%5F3). As of Couchbase Server 5.0