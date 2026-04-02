---
title: New In 3.3
description: Couchbase Sync Gateway -- What's new in the latest release
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/ROOT/pages/whatsnew.adoc
pubDate: 2026-04-02T05:14:13.149Z
link: xref:3.3@sync-gateway::whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/whatsnew.html)

# New In 3.3

> Couchbase Sync Gateway — What's new in the latest release  
> This content covers the new features introduced in Sync Gateway 3.3

> [!WARNING]
> Do not deploy Eventing/Sync Gateway until all SGW nodes are at version 3.2 or later. For earlier Sync Gateway versions that do not write import XATTRs, Eventing functions experience infinite recursions and duplicate mutations if deployed in a mixed mode SGW environment. This can only happen when you deploy a new Eventing/Sync Gateway function during an upgrade, with some SGW nodes at version 3.2 or later, and others at an earlier version.

## [](#release-3-3)Release 3.3

### [](#new-features)New Features

#### [](#partitioned-indexes)Partitioned Indexes

Sync Gateway 3.3 introduces support for partitioned indexes. Partitioned indexes offer horizontal scalability for large deployments by sharding indexes across multiple nodes. Only `allDocs` and `channels` indexes can be partitioned.

Partitioned indexes are not intended for general use in Sync Gateway. They may decrease performance, as each partition is queried separately and results are aggregated.

You should only migrate to partitioned indexes in cases where you are using memory-optimized indexes which exceed the memory capacity of a single index node, and you cannot reduce the index size using collections or database sharding.

For more information, see [Partitioned Indexes](deploy/index-partitions.md).

#### [](#disable-the-public-all-docs-endpoint)Disable the Public All Docs Endpoint

Sync Gateway 3.3 introduces an option to disable the [GET /{keyspace}/\_all\_docs](rest-api/rest%5Fapi%5Fpublic.md#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs) operation in the Public REST API. That operation is intended mainly for debugging in a small setup. With a large number of documents, it may lead to timeouts and out-of-memory conditions on the Query nodes.

In any sizeable setup, it is recommended that you should instead use the [GET /{keyspace}/\_changes](rest-api/rest%5Fapi%5Fpublic.md#tag/Database-Management/operation/get%5Fkeyspace-%5Fchanges) operation to get all documents for a user, or the [POST /{keyspace}/\_bulk\_docs](rest-api/rest%5Fapi%5Fpublic.md#tag/Document/operation/post%5Fkeyspace-%5Fbulk%5Fdocs) operation to return a specific subset of documents.

To disable the [GET /{keyspace}/\_all\_docs](rest-api/rest%5Fapi%5Fpublic.md#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs) operation in the Public REST API, set [disable\_public\_all\_docs](configuration/configuration-schema-database.md#disable%5Fpublic%5Fall%5Fdocs) to `true` in the database configuration. This option is set to `false` by default; it will be set to `true` by default in a future release.

#### [](#interactive-admin-credentials-for-sg-collect-info)Interactive Admin Credentials for SG Collect Info

In Sync Gateway 3.3 and later, the `--sync-gateway-password` command line argument has been removed from `sgcollect_info` for security reasons. When you specify the `--sync-gateway-username` option, `sgcollect_info` prompts you to enter the password interactively. Attempting to use the `--sync-gateway-password` option causes an error, with instructions for next steps.

Alternatively, you can set credentials using the `SG_USERNAME` and `SG_PASSWORD` environment variables to avoid the prompt.

For more information, see [SG Collect Info](manage/sgcollect-info.md).

#### [](#performance-improvements-for-larger-deployments)Performance Improvements for Larger Deployments

Sync Gateway 3.3 includes several performance enhancements for larger deployments. Change notification processing has been optimized to better support high volumes of connected clients per Sync Gateway node. Channel cache memory and CPU utilization has been optimized, particularly under high write load. Finally, memory and CPU usage associated with skipped sequence processing, which commonly occurs under high write load, has been reduced.

## [](#see-also)See Also

[What's new in previous version 3.2](../3.2/whatsnew.md).

### [](#sync-gateway-release-notes)Sync Gateway Release Notes

[Read the full 3.3 release notes here](product-notes/release-notes.md).

## [](#upgrading)Upgrading

[Upgrading Sync Gateway](upgrading.md).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](access-control/sync-function/sync-function.md)
* [Import filter](sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api/rest-api.md)
* [Admin REST API](rest-api/rest-api-admin.md)
* [Metrics REST API](rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)