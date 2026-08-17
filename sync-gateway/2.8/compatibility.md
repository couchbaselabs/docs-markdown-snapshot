---
title: Compatibility
description: Couchbase Sync Gateway
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/compatibility.adoc
  xref: xref:2.8@sync-gateway::compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/compatibility.html)

# Compatibility

> Couchbase Sync Gateway  
> Covers Couchbase Sync Gateway's compatibility with Couchbase Server and Couchbase Lite

## [](#sync-gateway-and-couchbase-server)Sync Gateway and Couchbase Server

> [!NOTE]
> Users of Couchbase Server 6.0 should ensure they have addressed the known issue ([MB-41255](https://issues.couchbase.com/browse/MB-41255)) by upgrading to one of the recommended Couchbase Server versions (6.0.5, 6.5.2, or 6.6.1).
> 
> The known issue can cause re-balance failures and/or failed replica writes of deleted or expired documents that use Xattrs.
> 
> This impacts Sync Gateway deployments running with shared bucket access enabled, which use Xattrs for metadata storage.

__Table 1\. Sync Gateway/Couchbase Server Compatibility Matrix__
| Sync Gateway ↓                                                                 | Couchbase Server →                               |                                                  |                                                  |     |     |         |   |
| ------------------------------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | --- | --- | ------- | - |
| 4.0\[[1](#%5Ffootnotedef%5F1 "View footnote.")\]                               | 4.1\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 4.5\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 4.6\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 5.0 | 5.1 | 5.5-7.1 |   |
| 1.3\[[2](#%5Ffootnotedef%5F2 "View footnote.")\] feed\_type: "DCP"             | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 1.4\[[2](#%5Ffootnotedef%5F2 "View footnote.")\] feed\_type: "DCP"             | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 1.5\[[3](#%5Ffootnotedef%5F3 "View footnote.")\] shared\_bucket\_access: false | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 1.5\[[3](#%5Ffootnotedef%5F3 "View footnote.")\] shared\_bucket\_access: true  | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.0 shared\_bucket\_access: false                                              | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 2.0 shared\_bucket\_access: true                                               | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.1 shared\_bucket\_access: false use\_views: true                             | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 2.1 shared\_bucket\_access: true                                               | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.1 use\_views: false                                                          | ✖                                                | ✖                                                | ✖                                                | ✖   | ✖   | ✖       | ✔ |
| 2.5-2.8 shared\_bucket\_access: false use\_views: true                         | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 2.5-2.8 shared\_bucket\_access: true                                           | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.5-2.8 use\_views: false                                                      | ✖                                                | ✖                                                | ✖                                                | ✖   | ✖   | ✖       | ✔ |

> [!NOTE]
> Couchbase Server Bucket Types
> 
> Use only **Couchbase** bucket types in _Couchbase for Mobile and Edge_. We do not support the use of Couchbase Server's **Ephemeral** or **Memcached** bucket types — for more on bucket types see: Couchbase Server [bucket types](../../server/current/learn/buckets-memory-and-storage/buckets.md).

## [](#sync-gateway-and-couchbase-lite)Sync Gateway and Couchbase Lite

The table below summarizes the compatible versions of Couchbase Lite with Sync Gateway.

> [!IMPORTANT]
> The beta version of Couchbase Lite 4.0 is only compatible with Sync Gateway 4.0

__Table 2\. Sync Gateway and Couchbase Lite Compatibility Matrix__
| Sync Gateway Versions ↓                                                                                         | Couchbase Lite →     |                      |                      |                      |                      |                      |                      |                      |
| --------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| 1.4 **\[[4](#%5Ffootnotedef%5F4 "View footnote.")\]**                                                           | 2.0                  | 2.1                  | 2.5 - 2.8            | 3.0.0                | 3.1.0                | 3.2.0                | 4.0.0                |                      |
| 1.4 **\[[2](#%5Ffootnotedef%5F2 "View footnote.")\]** and 1.5 **\[[3](#%5Ffootnotedef%5F3 "View footnote.")\]** | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   |
| 2.0 and 2.1                                                                                                     | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 2.5 to 2.8with delta sync disabled                                                                              | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 2.5 to 2.8with delta sync enabled                                                                               | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 3.0.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 3.1.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 3.2.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 4.0.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) |

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

[1](#%5Ffootnoteref%5F1). This Couchbase Server version is End of Support 

[2](#%5Ffootnoteref%5F2). This Sync Gateway version is End of Support 

[3](#%5Ffootnoteref%5F3). This Sync Gateway version is End of Life 

[4](#%5Ffootnoteref%5F4). This Couchbase Lite version is End of Support