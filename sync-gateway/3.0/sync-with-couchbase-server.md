---
title: Sync with Couchbase Server
description: Use Sync Gateway to sync Couchbase Server changes securely from cloud to edge
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/sync-with-couchbase-server.adoc
  xref: xref:3.0@sync-gateway::sync-with-couchbase-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/sync-with-couchbase-server.html)

# Sync with Couchbase Server

> Use Sync Gateway to sync Couchbase Server changes securely from cloud to edge  
> This content explains how Sync Gateway synchronizes document changes made through Couchbase SDKs and N1QL queries.

Related _Sync_ topics: [Sync Using App](sync-using-app.md) | [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md) | [Delta Sync](delta-sync.md) | [Resync](resync.md)

> [!IMPORTANT]
> Users of Couchbase Server 6.0 should ensure they have addressed the known issue ([MB-41255](https://issues.couchbase.com/browse/MB-41255)) by upgrading to one of the recommended Couchbase Server versions (6.0.5, 6.5.2, or 6.6.1).
> 
> The known issue can cause re-balance failures and/or failed replica writes of deleted or expired documents that use Xattrs.
> 
> This impacts Sync Gateway deployments running with shared bucket access enabled, which use Xattrs for metadata storage.

## [](#introduction)Introduction

_Sync Gateway_ will automatically sync database changes if [database.import\_docs](configuration-schema-database.md#database-import%5Fdocs) and [database.enable\_shared\_bucket\_access](configuration-schema-database.md#database-enable%5Fxttrs) are set 'true'.

* Enable\_Shared\_Bucket\_Access  
This setting ensures that both sync gateway and _Couchbase Server_ can read and write to the same bucket simultaneously and that sync gateway can access Couchbase Server document XATTRS  
See: [Figure 1](#sgw-paths) and [database.enable\_shared\_bucket\_access](configuration-schema-database.md#database-enable%5Fxttrs).
* Import Docs  
Setting this property true ensures that the sync gateway node performs import processing, obtaining the mobile metadata it requires to replicate changes — see: [Import Processing](#import-process).

You can configure both these properties using the Admin Rest API [Database Configuration](configuration-schema-database.md) endpoint.

![shared bucket access](_images/shared-bucket-access.png) 

Figure 1\. Sync Gateway Data Access Paths

## [](#sba-feature)Shared Bucket Access

Mobile applications require additional metadata in order to manage security and replication.

sync gateway stores this information using Couchbase Server XATTRs (see Couchbase Server documentation on [Extended Attributes](../../server/current/learn/data/extended-attributes-fundamentals.md)).

### [](#extended-attributes-xattrs)Extended Attributes (XATTRs)

A document can be associated with zero or more extended attributes.

There are currently three types of XATTRS: User, System and Virtual.

Extended attributes:

* Are JSON objects that can be associated with Couchbase documents.
* Are stored and replicated along with the associated document in both intra-cluster and XDCR replication.
* Can be accessed via Couchbase Server SDKs using the sub-document API, via command-line tools, and via views.
* Are accessible from N1QL in Couchbase Server using the `` ().xattrs` `` property.  
For example, `SELECT meta().xattrs._sync from travel-sample where Meta().id = "user::demo"`;.

Both sync gateway and Couchbase Server use a System extended attribute, with the following characteristics to support mobile convergence (shared bucket access):

* Shares lifetime with the document metadata - when a document is deleted, system xattrs are preserved with the tombstone.
* Allocated 1MB of storage, independent of the 20MB available for the document

> [!WARNING]
> The sync metadata is maintained internally by sync gateway and its structure can change at any time. It should not be used to drive business logic of applications. The direct use of the N1QL query is unsupported and must not be used in production environments. The `_raw` endpoint (/db/\_raw/{docid}) on sync gateway's Admin REST API returns both the document and its associated mobile metadata.

### [](#documents)Documents

With bucket-sharing enabled, Couchbase Server documents can be inserted directly (using _N1QL_ or _SDKs_) or by using sync gateway's [Public REST API](rest-api.md).

sync gateway \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] creates the metadata it needs by abstracting it from the SDK or N1QL applications reading and writing data directly to Couchbase Server buckets. It uses Couchbase Server XATTRs \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] to store that metadata into an external document fragment — see [Extended Attributes (XATTR)](../../server/current/learn/data/extended-attributes-fundamentals.md).

### [](#blobs-and-attachments)Blobs and Attachments

Couchbase Server SDK/N1QL

Use sync gateway's REST API's [/{db}/{docid}/{attachment}](rest-api-admin.md#/attachment) endpoints to manage attachments and blob data; you cannot use Couchbase Server SDKs to do this directly.

Standard practice would be to create the document using the SDK and then associate its blobs/attachments using the [Add/Update Attachment (/{db}/{docid}/{attachment})](rest-api-admin.md#/attachment/put%5F%5Fdb%5F%5F%5Fdoc%5F%5F%5Fattachment%5F) endpoint. You can see a practical example in this blog post — <https://blog.couchbase.com/store-sync-binary-data-attachments-blobs-couchbase-mobile>

Couchbase Lite Apps

Couchbase Lite apps seamlessly handle blobs and attachments, see the appropriate platform examples here:

Related Couchbase Lite content

[Android](../../couchbase-lite/3.0/android/blob.md) | [C](../../couchbase-lite/3.0/c/blob.md) | [C#](../../couchbase-lite/3.0/csharp/blob.md) | [Java](../../couchbase-lite/3.0/java/blob.md) | [Objective-C](../../couchbase-lite/3.0/objc/blob.md) | [Swift](../../couchbase-lite/3.0/swift/blob.md)

Using a WebApp

Attachments can be accessed through sync gateway's REST API using the [/{db}/{doc}/{attachment}](rest-api.md#/attachment/GetAttachment%5F) endpoint.

### [](#tombstone-revisions)Tombstone Revisions

Note that, with bucket-sharing enabled, [tombstone revision![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#tombstone-revision)s are **not** retained indefinitely; they are purged based on the server's _metadata purge interval_.

To ensure tombstones are synced with clients, you should set the server's metadata purge interval based on your expected replication frequency — see the [$dbname.enable\_shared\_bucket\_access](configuration-schema-database.md#database-enable%5Fshared%5Fbucket%5Faccess) reference.

### [](#accessing-sync-metadata)Accessing Sync Metadata

As stated, mobile metadata is not kept in the document, but in a system extended attribute (XATTR) in Couchbase Server.

The N1QL query language \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] supports the ability to query these extended attributes (XATTRS) and hence the document's sync metadata — see: [Example 1](#simple-query).

Example 1\. Querying XATTRS-bsed sync metadata

```sql
SELECT meta().xattrs._sync FROM `travel-sample` WHERE meta().id = "mydocId"
```

> [!WARNING]
> The sync metadata is maintained internally by sync gateway and its structure can change at any time. It should not be used to drive business logic of applications. The direct use of the N1QL query is **unsupported** and must not be used in production environments.

### [](#enable-shared-bucket-access)Enable Shared Bucket Access

Shared bucket access is an opt-in feature. You can enable it without bringing down the entire sync gateway cluster — see [Example 2](#enable-sba).

Example 2\. Enable Bucket-Sharing

```json
{
    "databases": {
        "db": {
            "name": "dbname",
            "bucket": "my-bucket",
            "import_docs": true (1)
        }
    }
}
```

| **1** | The import\_docs property is used to specify that a sync gateway node participates (exclusively) in [Import Process](#import-process.adoc). The mechanism by which sync gateway incorporates changes to data buckets it shares with Couchbase Server — see: [Import Processing](#import-process). |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#import-process)Import Processing

The **import process** is a key part of mobile convergence. It is the means by which sync gateway becomes aware of non-sync gateway data changes and obtains the mobile metadata it requires to replicate changes.

![shared bucket access](_images/shared-bucket-access.png) 

Any non-sync gateway change is eligible for import. The document is first run through the Sync Function to compute read security and routing, with the following differences:

* The import is processed with an admin user context in the Sync Function, similar to writes made through the sync gateway Admin API. This means that `requireAccess`, `requireUser` and `requireRole` calls in the Sync Function are treated as no-ops.
* During import, `oldDoc` is `nil` when the Sync Function is executed.

You can specify a filter function using the [import\_filter](configuration-schema-database.md#database%5Fimport%5Ffilter) property, which will only import specific documents.

> [!TIP]
> Use the [logging.console.log\_keys](configuration-schema-bootstrap.md#logging-console-log%5Fkeys) log key to troubleshoot import processing issues in the logs.

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

In _Enterprise Edition_, import processing work is sharded across all sync gateway nodes with import enabled. This implies that if one of the nodes fail, the failed shard is automatically picked up by the remaining nodes in the cluster. This way, you get High Availability of import processing.

In _Community Edition_, there is no sharding of import across the nodes participating in the import processing. Each import node processes all server mutations.

### [](#workload-isolation)Workload Isolation

As described in the table above, if `import_docs` is set to `false`, the node will not be participating in the import process. This configuration is specifically recommended for workload isolation: to isolate import nodes from the client-facing nodes. Workload isolation may be preferable in deployments with high write throughput.

The following diagram shows an example architecture of two sync gateway nodes handling the incoming client connections (`import_docs: false`) and two nodes sharing the import processing (`import_docs: true`).

![workload isolation](_images/workload-isolation.png)

Next Steps

* Check out our getting started tutorial for more on how to setup, configure and run sync gateway replications - [Sync tutorial](#tutorials:userprofile-sync:userprofile%5Fsync.adoc)
* Further reading:

  * Couchbase Server documentation on [Extended Attributes](../../server/current/learn/data/extended-attributes-fundamentals.md)
  * Configuration file references:

    * [$dbname.enable\_shared\_bucket\_access](configuration-schema-database.md#database-enable%5Fshared%5Fbucket%5Faccess) to enable convergence for a given database.
    * [$dbname.import\_docs](configuration-schema-database.md#database-import%5Fdocs) to give a particular sync gateway node the role of importing the documents.
    * [$dbname.import\_filter](configuration-schema-database.md#database-import%5Ffilter) to select which document(s) to make aware to mobile clients.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). As of Sync Gateway 1.5 

[2](#%5Ffootnoteref%5F2). As of Couchbase Server 5.0