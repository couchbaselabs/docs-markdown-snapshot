---
title: Compatibility
description: Couchbase Sync Gateway
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/product-notes/pages/compatibility.adoc
  xref: xref:3.3@sync-gateway:product-notes:compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/product-notes/compatibility.html)

# Compatibility

> Couchbase Sync Gateway  
> Covers Couchbase Sync Gateway's compatibility with Couchbase Server and Couchbase Lite

## [](#sync-gateway-and-couchbase-server)Sync Gateway and Couchbase Server

> [!IMPORTANT]
> Users of Couchbase Server 6.0 should ensure they have addressed the known issue ([MB-41255](https://issues.couchbase.com/browse/MB-41255)) by upgrading to one of the recommended Couchbase Server versions (6.0.5, 6.5.2, or 6.6.1).
> 
> The known issue can cause re-balance failures and/or failed replica writes of deleted or expired documents that use Xattrs.
> 
> This impacts Sync Gateway deployments running with shared bucket access enabled, which use Xattrs for metadata storage.

Sync Gateway/Couchbase Server

Compatibility Matrix

| Sync Gateway ↓                                        | Couchbase Server →                             |                                                       |                                                       |                            |                            |                            |                            |                            |                            |
| ----------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Version                                               | Scenario                                       | 5.0 **\[[1](#%5Ffootnotedef%5F1 "View footnote.")\]** | 5.1 **\[[1](#%5Ffootnotedef%5F1 "View footnote.")\]** | 5.5-6.0                    | 6.5-7.0                    | 7.1                        | 7.2                        | 7.6                        | 8.x                        |
| 1.4 **\[[2](#%5Ffootnotedef%5F2 "View footnote.")\]** | feed\_type: "DCP"                              | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 1.5 **\[[3](#%5Ffootnotedef%5F3 "View footnote.")\]** | shared\_bucket\_access: false                  | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 1.5 **\[[3](#%5Ffootnotedef%5F3 "View footnote.")\]** | shared\_bucket\_access: true                   | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.0                                                   | shared\_bucket\_access: false                  | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.0                                                   | shared\_bucket\_access: true                   | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.1                                                   | shared\_bucket\_access: false use\_views: true | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.1                                                   | shared\_bucket\_access: true                   | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.1                                                   | use\_views: false                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5-2.8                                               | shared\_bucket\_access: false use\_views: true | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5-2.8                                               | shared\_bucket\_access: true                   | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png)                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5-2.8                                               | use\_views: false                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.0.3                                                 |                                                | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.1.0                                                 |                                                | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.1.0                                                 | Using Scopes and Collections                   | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.2.0                                                 |                                                | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.2.0                                                 | Using Scopes and Collections                   | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.3.0                                                 |                                                | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.3.0                                                 | Using Scopes and Collections                   | ![no](../_images/no.png)                              | ![no](../_images/no.png)                              | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

> [!WARNING]
> Starting from Couchbase Server 7.0, the `use_views` feature is deprecated.
> 
> * Sync Gateway 3.1 only runs with `use_views` with a default scope/collection configuration
> * You cannot run `use_views` with a defined scope/collection

> [!IMPORTANT]
> Couchbase Server Bucket Types
> 
> Use only **Couchbase** bucket types in _Couchbase Mobile_. We do not support the use of Couchbase Server's **Ephemeral** or **Memcached** bucket types — for more on bucket types see: Couchbase Server [bucket types](../../../server/current/learn/buckets-memory-and-storage/buckets.md).

## [](#sync-gateway-and-couchbase-lite)Sync Gateway and Couchbase Lite

The table below summarizes the compatible versions of Couchbase Lite with Sync Gateway.

__Table 1\. Sync Gateway and Couchbase Lite Compatibility Matrix__
| Sync Gateway Versions ↓                                                                                         | Couchbase Lite →           |                            |                            |                            |                            |                            |                            |                            |
| --------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 1.4 **\[[4](#%5Ffootnotedef%5F4 "View footnote.")\]**                                                           | 2.0                        | 2.1                        | 2.5 - 2.8                  | 3.0.3                      | 3.1.0                      | 3.2.0                      | 3.3.0                      |                            |
| 1.4 **\[[2](#%5Ffootnotedef%5F2 "View footnote.")\]** and 1.5 **\[[3](#%5Ffootnotedef%5F3 "View footnote.")\]** | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 2.0 and 2.1                                                                                                     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5 to 2.8with delta sync disabled                                                                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5 to 2.8with delta sync enabled                                                                               | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.0.3                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.1.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.2.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.3.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). The 3.0 is compatible with these versions but its use is not recommended 

[2](#%5Ffootnoteref%5F2). This Sync Gateway version is End of Support 

[3](#%5Ffootnoteref%5F3). This Sync Gateway version is End of Life 

[4](#%5Ffootnoteref%5F4). This Couchbase Lite version is End of Support