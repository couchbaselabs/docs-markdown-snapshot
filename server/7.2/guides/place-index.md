---
title: Index Placement
description: How to place indexes on specified nodes, create index replicas, and
  partition indexes.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/place-index.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:guides:place-index.adoc[]
---

[View original HTML](/server/7.2/guides/place-index.html)

# Index Placement

> How to place indexes on specified nodes, create index replicas, and partition indexes.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

To improve query responsiveness, you can choose where to save primary and secondary indexes. You can also partition a large secondary index across multiple nodes. In Couchbase Server Enterprise Edition, you can create replicas of primary indexes, secondary indexes, and secondary index partitions, to enhance index availability.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

> [!NOTE]
> This how-to guide focuses on index placement, partitioning, and replication using SQL++ queries. The SDKs do not currently support all of these features fully.

## [](#placing-a-single-index)Placing a Single Index

When you create a primary or secondary index, you can specify the placement of the index.

To specify the placement of a single index:

1. Use the `WITH` clause to specify the index options.
2. In the index options, use the `nodes` attribute to specify an array containing a single node. The node name must include the cluster administration port, by default 8091.

The following query creates a secondary index that contains airports with an `alt` value greater than 1000 on the node `127.0.0.1`.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX idx_airport_over1000
  ON airport(geo.alt)
  WHERE geo.alt > 1000
  USING GSI
  WITH {"nodes": ["127.0.0.1:8091"]};
```

For more information and examples, see [CREATE PRIMARY INDEX](../n1ql/n1ql-language-reference/createprimaryindex.md) and [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md).

## [](#partitioning-an-index)Partitioning an Index

When you create a secondary index, you can split the index into multiple partitions. You can specify the placement of the partitions of an index, just as you can for a single index.

To partition a secondary index:

1. Use the `PARTITION BY HASH` clause to specify the field expression or expressions by which you want to partition the index.
2. If required, use the `WITH` clause to specify the index options, and use the `num_partition` attribute to specify the number of partitions. If you do not specify the number of partitions, the index has 8 partitions.

The following query creates an index partitioned by the document ID.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX idx ON airline
(country, name, id)
 PARTITION BY HASH(META().id);
```

For more information and examples, see [Index Partitioning](../n1ql/n1ql-language-reference/index-partitioning.md).

## [](#replicating-an-index)Replicating an Index

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

In Couchbase Server Enterprise Edition, when you create a secondary index, you can replicas of the index across multiple nodes.

You can specify replicas for a partitioned index, just as you can for a single index.

To replicate a secondary index by specifying the number of replicas:

1. Use the `WITH` clause to specify the index options.
2. In the index options, use the `num_replica` attribute to specify the number of replicas to create. The value of this attribute must be less than or equal to the number of index nodes.

If you specify `num_replica` but not `nodes`, the replicas are distributed amongst index nodes automatically.

The following query creates an index with two replicas, with no destination-nodes specified.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX country_idx ON airport(country, city)
WITH {"num_replica": 2};
```

To replicate a secondary index by specifying the replica nodes:

1. Use the `WITH` clause to specify the index options.
2. In the index options, use the `nodes` attribute to specify an array containing the nodes on which you want to create replicas. Each node name must include the cluster administration port, by default 8091.

If you specify `nodes` but not `num_replica`, the number of replicas (plus the original index) is equal to the number of nodes.

The following query creates an index on `node1`, with replicas on `node2` and `node3`.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX country_idx ON airport(country, city)
WITH {"nodes": ["node1:8091", "node2:8091", "node3:8091"]};
```

> [!NOTE]
> If you specify both `num_replica` and `nodes`, the number of nodes must be one greater than the number of replicas.

For more information and examples, see [Index Replication](../learn/services-and-indexes/indexes/index-replication.md#index-replication).

## [](#altering-index-placement)Altering Index Placement

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

In Couchbase Server Enterprise Edition, you can alter the placement of an existing index or replica, increase or decrease the number of replicas, or to drop a replica temporarily. You can also perform the same alterations to a partitioned index and any replica partitions.

To alter index placement:

1. Use the `ALTER INDEX` statement to specify the index to alter.
2. Use the `ON` clause to specify the keyspace on which the index was built.
3. Use the `WITH` clause to specify the action to take and the parameters of that action.

The following query moves the index `def_inventory_airport_faa` to node `192.168.10.11`.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
ALTER INDEX def_inventory_airport_faa ON airport
WITH {"action": "move", "nodes": ["192.168.10.11:8091"]};
```

For more information and examples, see [ALTER INDEX](../n1ql/n1ql-language-reference/alterindex.md).

## [](#related-links)Related Links

Reference and explanation:

* [Using Indexes](../learn/services-and-indexes/indexes/global-secondary-indexes.md)

Administrator guides:

* [Manage Indexes](../manage/manage-indexes/manage-indexes.md)
* [Monitor Indexes](../manage/monitor/monitoring-indexes.md)

Indexes with SDKs:

* [C](../../../c-sdk/current/concept-docs/n1ql-query.md#indexes)| [C++](../../../cxx-sdk/current/concept-docs/n1ql-query.md#indexes)| [.NET](../../../dotnet-sdk/current/concept-docs/n1ql-query.md#indexes)| [Go](../../../go-sdk/current/concept-docs/n1ql-query.md#indexes)| [Java](../../../java-sdk/current/concept-docs/n1ql-query.md#indexes)| Kotlin | [Node.js](../../../nodejs-sdk/current/concept-docs/n1ql-query.md#indexes)| [PHP](../../../php-sdk/current/concept-docs/n1ql-query.md#indexes)| [Python](../../../python-sdk/current/concept-docs/n1ql-query.md#indexes)| [Ruby](../../../ruby-sdk/current/concept-docs/n1ql-query.md#indexes)| [Scala](../../../scala-sdk/current/concept-docs/n1ql-query.md#indexes)