---
title: Eventing&#8201;&#8212;&#8201;Server Compatibility
description: How Sync Gateway works with Couchbase Server's Eventing feature
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/server-compatibility/pages/server-compatibility-eventing.adoc
  xref: xref:sync-gateway:server-compatibility:server-compatibility-eventing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/server-compatibility/server-compatibility-eventing.html)

# Eventing&#8201;&#8212;&#8201;Server Compatibility

> How Sync Gateway works with Couchbase Server's Eventing feature  

_Related topics_: [Buckets](server-compatibility-buckets.md) | [Collections](server-compatibility-collections.md) | [Eventing](server-compatibility-eventing.md) | [Transactions](server-compatibility-transactions.md) | [XDCR](server-compatibility-xdcr.md) | [Backup and restore](server-compatibility-backups.md)

_Other Topics_: [Compatibility Matrix](../product-notes/compatibility.md)

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

## [](#introduction)Introduction

Couchbase Server provides the backing data store for Sync Gateway.

> [!TIP]
> See: [Compatibility Matrix](../product-notes/compatibility.md) for version compatibility information.

Couchbase Server's [Couchbase Eventing Service](../../../server/current/eventing/eventing-overview.md) feature provides a framework to operate on changes to data in real time.

This page provides details on how [Couchbase Eventing Service](../../../server/current/eventing/eventing-overview.md) relates to data changes in the Couchbase Mobile ecosystem.

## [](#using-eventing-server-7-6-3)Using Eventing - Server 7.6.3+

> [!WARNING]
> Do not deploy Eventing/Sync Gateway until all SGW nodes are at version 3.2 or later. For earlier Sync Gateway versions that do not write import XATTRs, Eventing functions experience infinite recursions and duplicate mutations if deployed in a mixed mode SGW environment. This can only happen when you deploy a new Eventing/Sync Gateway function during an upgrade, with some SGW nodes at version 3.2 or later, and others at an earlier version.

> [!IMPORTANT]
> Sync Gateway must be running with [Configuration Overview](../configuration/configuration-overview.md) enabled to support compatibility with Eventing.
> 
> Databases created via file-based configuration (when running with `-disable_persistent_config`) are not recorded in the Couchbase Server registry. Without registry records, Eventing cannot:
> 
> * Detect Sync Gateway databases to prevent deployment conflicts
> * Prevent duplicate mutations when processing document changes
> 
> Persistent configuration is:
> 
> * The **only** option available on Capella
> * The default and **recommended** configuration mode for on-premises deployments since Sync Gateway 3.0

Sync Gateway 3.2.0 and later supports interoperability with Eventing from Couchbase Server version 7.6.3+. You can use Eventing to handle data changes that happen when applications interact and to integrate with other Couchbase services such as Data, Query and Full Text Search.

You can now create Eventing functions with read-write bindings with the source bucket associated with a Sync Gateway database.

You can also use Eventing to generate vector embeddings from document fields, see [Vector Search](#couchbase-lite:ROOT/cbl-whatsnew.adoc#vector-search) for more details about Vector Search with Couchbase Lite.

An Eventing function, based on deployment options, can now skip all documents with IDs prefixed with `_sync`.

For Sync Gateway versions that write import XATTRs:

* Eventing now prevents infinite recursion.
* Eventing now prevents duplicate mutations with the opt-in `import_mutation_aware` boolean flag.

> [!NOTE]
> If the `import_mutation_aware` flag is set to `true`, the performance of the Eventing function drops. This happens because every mutation processed by Eventing requires a Sub-Document operation to maintain a cursor or state for any function that shares a Sync Gateway endpoint.

The procedure to enable Sync Gateway support for an Eventing function is as follows:

1. On Couchbase Server, [pause the function](../../../server/current/eventing-rest-api/index.md#basic%5Fpause).
2. Using the Eventing REST API, set the `allow_sync_documents` setting for the function to false.  
> [!NOTE]  
> You must also include the `deployment_status` and `processing_status` settings in the request body.  
For example, for a global function with a scope of `**.**`:  
```shell  
curl -XPOST -d '{  
  "deployment_status": true,  
  "processing_status": false,  
  "allow_sync_documents": false  
}' "http://$ADMIN:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings"  
```  
For a scoped function:  
```shell  
curl -XPOST -d '{  
  "deployment_status": true,  
  "processing_status": false,  
  "allow_sync_documents": false  
}' "http://$USER:$PASSWORD@$HOST:8096/api/v1/functions/my_function/settings?bucket=bulk&scope=data"  
```  
Where:

  * `$HOST` is the hostname or IP address of a node running the Eventing service.
  * `$ADMIN` is the user name of an administrator.
  * `$USER` is the user name of any authorized user .
  * `$PASSWORD` is the password to connect to Couchbase Server.
3. On Couchbase Server, [resume the function](../../../server/current/eventing-rest-api/index.md#basic%5Fresume).

For more information, see [Eventing REST API](../../../server/current/eventing-rest-api/index.md).

## [](#using-eventing-pre-server-7-6-3)Using Eventing (Pre-Server 7.6.3)

You can use Eventing and Sync Gateway connected to the same bucket when Eventing operates on server buckets in **read only** mode — see [Bucket Bindings](../../../server/current/eventing/eventing-Terminologies.md#section%5Fmzd%5Fl1p%5Fm2b) for how to do this.

You should write your Eventing function to be idempotent so that it produces the same result when it processes the same mutation more than once. This is necessary because:

* When Sync Gateway makes a single document update directly, such as those replicated from Couchbase Lite, it generates a single server mutation that writes both the document body and the metadata.  
When an update originates outside of Couchbase mobile, Sync Gateway generates multiple mutations because it must update both the document's body and its `_sync` metadata (XATTRs).
* Eventing detects these mutations and invokes its `OnUpdate` handler for each one; whether it's for the modified body of the document, Sync Gateway metadata, or both. It's here that you need to code the function to apply the same update once only. One way to do this is to use the crc64 function call to identify when an update is to the Sync Gateway metadata only — see: [Eventing — crc64()](../../../server/current/eventing/eventing-language-constructs.md#crc64%5Fcall) for more on how to do this.

_Eventing_ prevents inadvertent use of its functions on _Sync Gateway_ read-write buckets. You'll see the following warning if you try to do this:  
`SyncGateway is enabled on: <bucket-name>, deployment of source bucket mutating handler will cause Intra Bucket Recursion`

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](../access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)