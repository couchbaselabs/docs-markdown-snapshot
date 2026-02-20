---
title: Using Indexes
description: Primary Indexes and Global Secondary Indexes (GSI) support queries
  made by the Query Service.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/learn/pages/services-and-indexes/indexes/global-secondary-indexes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:learn:services-and-indexes/indexes/global-secondary-indexes.adoc[]
---

[View original HTML](/server/7.2/learn/services-and-indexes/indexes/global-secondary-indexes.html)

# Using Indexes

> Primary Indexes and Global Secondary Indexes (GSI) support queries made by the Query Service. 

Global Secondary Indexes provide the following:

* _Advanced Scaling_: GSIs can be assigned independently to selected nodes, without existing workloads being affected.
* _Predictable Performance_: Key-based operations maintain predictable low-latency, even in the presence of a large number of indexes. Index-maintenance is non-competitive with key-based operations, even when data-mutation workloads are heavy.
* _Low Latency Querying_: GSIs independently partition into the Index Service nodes: they do not have to follow hash partitioning of data into vBuckets. Queries using GSIs can achieve low latency response times even when the cluster scales out; since GSIs do not require a wide fan-out to all Data Service nodes.
* _Independent Partitioning_: The Index Service provides partition independence: data and its indexes can have different partition keys. Each index can have its own partition key, so each can be partitioned independently to match the specific query. As new requirements arise, the application will also be able to create a new index with a new partition key, without affecting performance of existing queries.

## Tuning and Query Performance

* [Index Lifecycle](index-lifecycle.md)
* [Indexing and Query Performance](indexing-and-query-perf.md)
* [Covering Indexes](../../../n1ql/n1ql-language-reference/covering-indexes.md)
* [Understanding Index Scans](index-scans.md)
* [Index Pushdown Optimizations](index%5Fpushdowns.md)
* [Grouping and Aggregate Pushdown](../../../n1ql/n1ql-language-reference/groupby-aggregate-performance.md)
* [Early Filters, Order and Pagination](early-filters-and-pagination.md)

## Index Commands

* [CREATE INDEX](../../../n1ql/n1ql-language-reference/createindex.md)
* [CREATE PRIMARY INDEX](../../../n1ql/n1ql-language-reference/createprimaryindex.md)
* [BUILD INDEX](../../../n1ql/n1ql-language-reference/build-index.md)
* [ALTER INDEX](../../../n1ql/n1ql-language-reference/alterindex.md)
* [DROP INDEX](../../../n1ql/n1ql-language-reference/dropindex.md)
* [DROP PRIMARY INDEX](../../../n1ql/n1ql-language-reference/dropprimaryindex.md)

## Storage and Availability

* [Index Availability](index-replication.md)
* [Storage Settings](storage-modes.md)

## Related Links

* [All Couchbase Server Indexes](indexes.md)
* [Index Service Architecture](../services/index-service.md)
* [Manage Indexes](../../../manage/manage-indexes/manage-indexes.md)
* [Monitor Indexes](../../../manage/monitor/monitoring-indexes.md)