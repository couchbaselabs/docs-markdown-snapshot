---
title: Index Availability and Performance
description: The Index Service ensures availability and performance through
  replication and partitioning. You can control the scan consistency for
  individual queries.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/indexes/pages/index-replication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:indexes:index-replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/indexes/index-replication.html)

# Index Availability and Performance

> The Index Service ensures availability and performance through replication and partitioning. You can control the scan consistency for individual queries. 

Examples on this Page

The examples in this topic use the travel-sample dataset which is shipped with Couchbase Server. For instructions on how to install the sample bucket, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).

To use the examples on this page, you must set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#index-replication)Index Replication

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

You can replicate primary and secondary indexes across cluster nodes running the [Index Service](#services-and-indexes/services/index-service.adoc). This feature is available only in Couchbase Server Enterprise Edition. Index replication has the following benefits:

* **Availability**: If one Index Service node is lost, the others continues to provide access to replicated indexes.
* **High Performance**: If original and replica copies are available, incoming queries are load-balanced across them.

If the number of nodes running the Index Service decreases, and index replicas are lost, Couchbase Server progressively assigns replacement index replicas to all Index Service nodes subsequently added to the cluster, until the required number of index replicas again exists for each replicated index.

### [](#creating-index-replicas-for-a-single-index)Creating Index Replicas for a Single Index

You can create index replicas using the SQL++ [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md), [CREATE VECTOR INDEX](../n1ql/n1ql-language-reference/createvectorindex.md), and [CREATE PRIMARY INDEX](../n1ql/n1ql-language-reference/createprimaryindex.md) statements.

To create index replicas for a single index, do one of the following:

* In the `WITH` clause, use the `nodes` attribute to specify the destination nodes. When you use this attribute by itself, the index is placed on one of the destination nodes, and one replica is placed on each of the others.  
In the following example, an index with two replicas is created. The active index is on `node1`, and the replicas are on `node2` and `node3`:  
```sqlpp  
CREATE INDEX country_idx ON airport(country, city)  
WITH {"nodes": ["node1:8091", "node2:8091", "node3:8091"]};  
```
* In the `WITH` clause, use the `num_replica` attribute to specify the number of replicas required. When you use this attribute by itself, the index and the required number of replicas are automatically distributed across Index Service nodes. The distribution pattern is based on a projection of optimal index availability, given the number and disposition of Index Service nodes across defined server groups. The required number of replicas must be smaller than the number of cluster nodes currently running the Index Service. If it’s not, the index creation fails.  
In the following example, an index is created with two replicas, with no destination nodes specified:  
```sqlpp  
CREATE INDEX country_idx ON airport(country, city)  
WITH {"num_replica": 2};  
```
* In the `WITH` clause, use the `nodes` and `num_replica` attributes together. In this case, the Index planner chooses from the set of specified nodes to place the index and the required number of replicas. The required number of replicas must be smaller than the number of specified nodes. If it’s not, the index creation fails.

For more information on using SQL++, see [SQL++ for Query Reference](../n1ql/n1ql-language-reference/index.md).

### [](#creating-index-replicas-automatically)Creating Index Replicas Automatically

The Index Service can create a number of index replicas automatically whenever [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md), [CREATE VECTOR INDEX](../n1ql/n1ql-language-reference/createvectorindex.md), or [CREATE PRIMARY INDEX](../n1ql/n1ql-language-reference/createprimaryindex.md) is invoked. The default number of replicas is `0`. For example, if you change the number of automatic replicas to `2`, from that point on creation of a single index is accompanied by the creation of two replicas, which are automatically distributed across the nodes of the cluster running the Index Service. No explicit specification is required within the SQL++ statement.

The following example changes the index replication settings using the GSI Settings REST API:

```sh
curl -X POST -u 'Administrator:password' \
'http://localhost:8091/settings/indexes' \
-d 'numReplica=2'
```

Here, `numReplica` is an integer that establishes the default number of replicas that must be created whenever an index is created. This call only succeeds if the cluster contains enough Index Service nodes to host each new index and its replicas: for example, if you specify `2` as the default number of replicas, the Index Service must have been established on at least 3 nodes.

When you explicitly specify the number of replicas with the [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md), [CREATE VECTOR INDEX](../n1ql/n1ql-language-reference/createvectorindex.md), or [CREATE PRIMARY INDEX](../n1ql/n1ql-language-reference/createprimaryindex.md) statement, the explicit specification takes precedence over the index replication settings.

You can change the index replication settings using the [UI](../manage/manage-settings/general-settings.md#index-storage-mode), the [CLI](../cli/cbcli/couchbase-cli-setting-index.md), or the [REST API](../rest-api/post-settings-indexes.md).

## [](#index-partitioning)Index Partitioning

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Index partitioning increases query performance, by dividing and spreading a large index of documents across multiple nodes. This feature is available only in Couchbase Server Enterprise Edition.

The benefits include:

* The ability to scale out horizontally, as index size increases.
* Transparency to queries, requiring no change to existing queries.
* Reduction of query latency for large, aggregated queries; since partitions can be scanned in parallel.
* Provision of a low-latency range query, while allowing indexes to be scaled out as needed.

For more information, see [Index Partitioning](../n1ql/n1ql-language-reference/index-partitioning.md).

## [](#index-consistency)Index Consistency

Couchbase Server handles data mutations with full consistency — all mutations to a given key are applied to the same vBucket, and become immediately available. In contrast, Couchbase Server maintains indexes with degrees of eventual consistency. This means that indexes may at times not contain the most up-to-date information, especially when deployed in a write-heavy environment: changes may take some time to propagate over to the index nodes.

The asynchronous updating nature of Global Secondary Indexes means that they can be quick to query and do not require the additional overhead of index recalculations at the time documents are modified. SQL++ queries are forwarded to the relevant indexes and the queries are done based on indexed information, rather than the documents as they exist in the data service.

With default query options, the Query Service will rely on the current index state: the most up-to-date document versions are not retrieved, and only the indexed versions are queried. This provides the best performance. Only updates occurring with a small time frame may not yet have been indexed.

For every query, you can specify the following scan consistency options:

* `not_bounded`: Executes the query immediately, without requiring any consistency for the query. If index maintenance is running behind, out-of-date results may be returned.
* `at_plus`: Executes the query, requiring indexes first to be updated to the timestamp of the last update. If index maintenance is running behind, the query waits for it to catch up.
* `request_plus`: Executes the query, requiring the indexes first to be updated to the timestamp of the current query request. If index maintenance is running behind, the query waits for it to catch up.
* `statement_plus`: Executes the query with strong consistency per statement. Before processing each statement, the service obtains a current vector timestamp and uses it as a lower bound for that statement.

For SQL++, the default consistency is `not_bounded`. When using the `request_plus` consistency mode, the Query Service ensures that the indexes are synchronized with the Data Service before querying.

You can specify the scan consistency via the [run-time preferences](../tools/query-workbench.md#query-preferences) in the Query Workbench, or by setting the [scan\_consistency](../n1ql/n1ql-manage/query-settings.md#scan%5Fconsistency) request-level parameter.

## [](#index-snapshots)Index Snapshots

Couchbase Server maintains one or more index snapshots on disk, to permit rapid recovery if nodes fail. In cases where recovery requires an Index Service node to be restarted, the node’s indexes are rebuilt from the snapshots retained on disk.

By default, two index snapshots are stored on disk. You can change index snapshot settings via the [CLI](../cli/cbcli/couchbase-cli-setting-index.md) or the [REST API](../rest-api/post-settings-indexes.md).

## [](#index-rollback)Index Rollback

The index service also maintains a [DCP failover log](../learn/clusters-and-availability/intra-cluster-replication.md#database-change-protocol). If necessary, the data service can request the index service to return to a specified rollback point and update its history.

You can change index rollback settings via the [CLI](../cli/cbcli/couchbase-cli-setting-index.md) or the [REST API](../rest-api/post-settings-indexes.md).

### [](#index-rollback-after-failover)Index Rollback After Failover

When a data node [fails over](../learn/clusters-and-availability/failover.md), a replica data node is promoted to active. If the index service has more recent data than the new active data node, the data node issues a rollback request to the index service.

In Couchbase Server 6.5 and later, when the index service receives the rollback request, it first attempts to revert to a stored index snapshot. If successful, the index service does not need to rebuild its indexes from scratch when the data node fails over. The index service can continue servicing query clients without interruption.

If the index service cannot revert to a current index snapshot, it rebuilds all indexes from scratch.

> [!NOTE]
> If [scan consistency](#index-consistency) is set to `not_bounded`, the index service may return stale data for a short time after reverting to a snapshot, until the index service is fully up-to-date with the new active data node.
> 
> If [scan consistency](#index-consistency) is set to `request_plus`, the index service will not perform any scans until a consistent snapshot is created. In this case, stale results are not returned.