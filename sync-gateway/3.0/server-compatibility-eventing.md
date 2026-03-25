---
title: Eventing&#8201;&#8212;&#8201;Server Compatibility
description: How <em>Sync Gateway</em> works with <em>Couchbase Server's</em>
  <em>Eventing</em> feature
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/server-compatibility-eventing.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::server-compatibility-eventing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/server-compatibility-eventing.html)

# Eventing&#8201;&#8212;&#8201;Server Compatibility

> How _Sync Gateway_ works with _Couchbase Server’s_ _Eventing_ feature  

_Related topics_: [XDCR](server-compatibility-xdcr.md) | Eventing | [Transactions](server-compatibility-transactions.md) | [Collections](server-compatibility-collections.md)

_Other Topics_: [Compatibility Matrix](compatibility.md)

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

## [](#introduction)Introduction

Couchbase Server provides the backing data store for Sync Gateway.

> [!TIP]
> See: [Compatibility Matrix](compatibility.md) for version compatibility information.

Couchbase Server’s [Couchbase Eventing Service](../../server/current/eventing/eventing-overview.md) feature provides a framework to operate on changes to data in real time.

Here we provide details on how [Couchbase Eventing Service](../../server/current/eventing/eventing-overview.md) relates to data changes in the Couchbase Mobile ecosystem.

## [](#using-eventing)Using Eventing

You can use Eventing and Sync Gateway connected to the same bucket, when Eventing operates on server buckets in **read only** mode — see [Bucket Bindings](../../server/current/eventing/eventing-Terminologies.md#section%5Fmzd%5Fl1p%5Fm2b) for how to do this.

You should write your Eventing function to be **idempotent**; to behave correctly when the same mutation is seen more than once. This is necessary because:

* When a single document update is made directly by Sync Gateway, such as those replicated from Couchbase Lite, it generates a single server mutation that writes both the document body and the metadata.  
But when an update originates outside of Couchbase mobile then multiple mutations are generated. That is because Sync Gateway must update both the document’s body and its \_sync metadata (XATTRs).
* _Eventing_ detects these mutations and invokes its `OnUpdate` **for each**; whether it is for the modified body of the document, Sync Gateway metadata, or both. It is here that you need to code the function to apply the same update once only. One way to do this is to use the crc64 function call to identify when an update is to the Sync Gateway metadata only — see: [Eventing — crc64()](../../server/current/eventing/eventing-language-constructs.md#crc64%5Fcall) for more on how to do this.

_Eventing_ prevents inadvertent use of its functions on _Sync Gateway_ read-write buckets. You will see the following warning if you try to do this:  
`SyncGateway is enabled on: <bucket-name>, deployment of source bucket mutating handler will cause Intra Bucket Recursion`

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function-overview.md)
* [Import filter](import-filter.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](#rest-api-admin.html#/Access%5FControl/update%5Fsync%5Ffunction)
* [Sync Function Overview](sync-function-overview.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)