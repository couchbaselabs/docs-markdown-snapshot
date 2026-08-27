---
title: Index Availability and Performance
description: The Index Service ensures availability and performance through
  replication and partitioning. You can control the scan consistency for
  individual queries.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/indexes/pages/index-replication.adoc
  xref: xref:cloud:indexes:index-replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/indexes/index-replication.html)

# Index Availability and Performance

> The Index Service ensures availability and performance through replication and partitioning. You can control the scan consistency for individual queries. 

Examples on this Page

The examples in this topic use the travel-sample dataset which is supplied with Couchbase Capella. For instructions on how to install the sample data, see [Import Sample Data](../clusters/data-service/import-data-documents.md#import-sample-data).

To use the examples on this page, you must set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#index-replication)Index Replication

You can replicate primary and secondary indexes across cluster nodes running the [Index Service](indexing-overview.md). Index replication has the following benefits:

* **Availability**: If one Index Service node is lost, the others continues to provide access to replicated indexes.
* **High Performance**: If original and replica copies are available, incoming queries are load-balanced across them.

If the number of nodes running the Index Service decreases, and index replicas are lost, Couchbase Capella progressively assigns replacement index replicas to all Index Service nodes subsequently added to the cluster, until the required number of index replicas again exists for each replicated index.

### [](#creating-index-replicas-for-a-single-index)Creating Index Replicas for a Single Index

You can create index replicas using the SQL++ [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md), [CREATE VECTOR INDEX](../n1ql/n1ql-language-reference/createvectorindex.md), and [CREATE PRIMARY INDEX](../n1ql/n1ql-language-reference/createprimaryindex.md) statements.

To create index replicas for a single index, do one of the following:

* In the `WITH` clause, use the `nodes` attribute to specify the destination nodes. When you use this attribute by itself, the index is placed on one of the destination nodes, and one replica is placed on each of the others.  
In the following example, an index with two replicas is created. The active index is on `node1`, and the replicas are on `node2` and `node3`:  
```sqlpp  
CREATE INDEX country_idx ON airport(country, city)  
WITH {"nodes": ["node1:8091", "node2:8091", "node3:8091"]};  
```
* In the `WITH` clause, use the `num_replica` attribute to specify the number of replicas required. When you use this attribute by itself, the index and the required number of replicas are automatically distributed across Index Service nodes. The distribution pattern is based on a projection of optimal index availability, given the number and disposition of Index Service nodes across defined server groups. The required number of replicas must be smaller than the number of cluster nodes currently running the Index Service. If it's not, the index creation fails.  
In the following example, an index is created with two replicas, with no destination nodes specified:  
```sqlpp  
CREATE INDEX country_idx ON airport(country, city)  
WITH {"num_replica": 2};  
```
* In the `WITH` clause, use the `nodes` and `num_replica` attributes together. In this case, the Index planner chooses from the set of specified nodes to place the index and the required number of replicas. The required number of replicas must be smaller than the number of specified nodes. If it's not, the index creation fails.

For more information on using SQL++, see [SQL++ for Query Reference](../n1ql/n1ql-language-reference/index.md).

## [](#index-partitioning)Index Partitioning

Index partitioning increases query performance, by dividing and spreading a large index of documents across multiple nodes.

The benefits include:

* The ability to scale out horizontally, as index size increases.
* Transparency to queries, requiring no change to existing queries.
* Reduction of query latency for large, aggregated queries; since partitions can be scanned in parallel.
* Provision of a low-latency range query, while allowing indexes to be scaled out as needed.

For more information, see [Index Partitioning](../n1ql/n1ql-language-reference/index-partitioning.md).

## [](#index-consistency)Index Consistency

Couchbase Capella handles data mutations with full consistency — all mutations to a given key are applied to the same vBucket, and become immediately available. In contrast, Couchbase Capella maintains indexes with degrees of eventual consistency. This means that indexes may at times not contain the most up-to-date information, especially when deployed in a write-heavy environment: changes may take some time to propagate over to the index nodes.

The asynchronous updating nature of Global Secondary Indexes means that they can be quick to query and do not require the additional overhead of index recalculations at the time documents are modified. SQL++ queries are forwarded to the relevant indexes and the queries are done based on indexed information, rather than the documents as they exist in the data service.

With default query options, the Query Service will rely on the current index state: the most up-to-date document versions are not retrieved, and only the indexed versions are queried. This provides the best performance. Only updates occurring with a small time frame may not yet have been indexed.

For every query, you can specify the following scan consistency options:

* `not_bounded`: Executes the query immediately, without requiring any consistency for the query. If index maintenance is running behind, out-of-date results may be returned.
* `at_plus`: Executes the query, requiring indexes first to be updated to the timestamp of the last update. If index maintenance is running behind, the query waits for it to catch up.
* `request_plus`: Executes the query, requiring the indexes first to be updated to the timestamp of the current query request. If index maintenance is running behind, the query waits for it to catch up.
* `statement_plus`: Executes the query with strong consistency per statement. Before processing each statement, the service obtains a current vector timestamp and uses it as a lower bound for that statement.

For SQL++, the default consistency is `not_bounded`. When using the `request_plus` consistency mode, the Query Service ensures that the indexes are synchronized with the Data Service before querying.

You can specify the scan consistency via the [run-time preferences](../clusters/query-service/query-workbench.md#query-settings) in the Query tab, or by setting the [scan\_consistency](../n1ql/n1ql-manage/query-settings.md#scan%5Fconsistency) request-level parameter.

## [](#index-snapshots)Index Snapshots

Couchbase Capella maintains one or more index snapshots on disk, to permit rapid recovery if nodes fail. In cases where recovery requires an Index Service node to be restarted, the node's indexes are rebuilt from the snapshots retained on disk.

By default, two index snapshots are stored on disk.

## [](#index-rollback)Index Rollback

The index service also maintains a [DCP failover log](../../server/current/learn/clusters-and-availability/intra-cluster-replication.md#database-change-protocol). If necessary, the data service can request the index service to return to a specified rollback point and update its history.

### [](#index-rollback-after-failover)Index Rollback After Failover

When a data node [fails over](../../server/current/learn/clusters-and-availability/failover.md), a replica data node is promoted to active. If the index service has more recent data than the new active data node, the data node issues a rollback request to the index service.

When the index service receives the rollback request, it first attempts to revert to a stored index snapshot. If successful, the index service does not need to rebuild its indexes from scratch when the data node fails over. The index service can continue servicing query clients without interruption.

If the index service cannot revert to a current index snapshot, it rebuilds all indexes from scratch.

> [!NOTE]
> If [scan consistency](#index-consistency) is set to `not_bounded`, the index service may return stale data for a short time after reverting to a snapshot, until the index service is fully up-to-date with the new active data node.
> 
> If [scan consistency](#index-consistency) is set to `request_plus`, the index service will not perform any scans until a consistent snapshot is created. In this case, stale results are not returned.