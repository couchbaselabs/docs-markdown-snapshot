---
title: CREATE INDEX
description: The CREATE INDEX statement allows you to create a secondary index.
  Secondary indexes contain a filtered or a full set of keys in a given
  keyspace.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/createindex.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/createindex.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/createindex.html)

# CREATE INDEX

The `CREATE INDEX` statement allows you to create a secondary index. Secondary indexes contain a filtered or a full set of keys in a given keyspace. Secondary indexes are optional but increase query efficiency on a keyspace.

## [](#purpose)Purpose

`CREATE INDEX` allows you to make multiple concurrent index creation requests. The command starts a task to create the index definition in the background. If there is an index creation task already running, the Index Service queues the incoming index creation request. `CREATE INDEX` returns as soon as the index creation phase is complete.

By default, when the index creation phase is complete, the Index Service triggers the index build phase. If you lose connectivity, the index build operation continues in the background. You can defer the index build phase using the `defer_build` clause. In deferred build mode, `CREATE INDEX` creates the index definition, but does not trigger the index build phase. You can then build the index using the [BUILD INDEX](build-index.md) command.

You can create multiple identical secondary indexes on a keyspace and place them on separate nodes for better index availability. In Couchbase Server Enterprise Edition, the recommended way to do this is using the `num_replica` option. In Couchbase Server Community Edition, you need to create multiple identical indexes and place them using the `nodes` option. For more information, see [WITH Clause](#index-with) below.

## [](#prerequisites)Prerequisites

##### RBAC Privileges

User executing the CREATE INDEX statement must have the _Query Manage Index_ privilege granted on the keyspace. For more information about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
create-index ::= 'CREATE' 'INDEX' index-name ( 'IF' 'NOT' 'EXISTS' )? 'ON' keyspace-ref
                 '(' index-key lead-key-attribs? ( ( ',' index-key key-attribs? )+ )? ')'
                 index-partition? where-clause? index-using? index-with?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/create-index.png) 

| index-name       | (Required) A unique name that identifies the index. Valid GSI index names can contain any of the following characters: A-Z a-z 0-9 # \_, \-, and must start with a letter, \[A-Z a-z\]. The minimum length of an index name is 1 character and there is no maximum length set for an index name. When querying, if the index name contains a # or \- character, you must enclose the index name within backticks. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| keyspace-ref     | (Required) Specifies the keyspace where the index is created. See [Keyspace Reference](#keyspace-ref) below.                                                                                                                                                                                                                                                                                                      |
| index-key        | (Required) Specifies an index key. See [Index Key](#index-key) below.                                                                                                                                                                                                                                                                                                                                             |
| lead-key-attribs | (Optional) Specifies attributes for the leading index key. See [Index Key Attributes](#index-key-attrib) below.                                                                                                                                                                                                                                                                                                   |
| key-attribs      | (Optional) Specifies attributes for a non-leading index key. See [Index Key Attributes](#index-key-attrib) below.                                                                                                                                                                                                                                                                                                 |
| index-partition  | (Optional) Specifies index partitions. See [PARTITION BY HASH Clause](#index-partition) below.                                                                                                                                                                                                                                                                                                                    |
| where-clause     | (Optional) Specifies filters for a partial index. See [WHERE Clause](#where-clause) below.                                                                                                                                                                                                                                                                                                                        |
| index-using      | (Optional) Specifies the index type. See [USING Clause](#index-using) below.                                                                                                                                                                                                                                                                                                                                      |
| index-with       | (Optional) Specifies options for the index. See [WITH Clause](#index-with) below.                                                                                                                                                                                                                                                                                                                                 |

### [](#if-not-exists)IF NOT EXISTS Clause

The optional `IF NOT EXISTS` clause enables the statement to complete successfully when the specified index already exists. If an index with the same name already exists within the specified keyspace, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

### [](#keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

Specifies the keyspace for which the index needs to be created. The keyspace reference may be a [keyspace path](#keyspace-path) or a [keyspace partial](#keyspace-partial).

> [!NOTE]
> If there is a hyphen (-) inside any part of the keyspace reference, you must wrap that part of the keyspace reference in backticks (\` \`). See the examples below.

#### [](#keyspace-path)Keyspace Path

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

If the keyspace is a named collection, or the default collection in the default scope within a bucket, the keyspace reference may be a keyspace path. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

| namespace  | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                                                                                                           |
| scope      | (Optional) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the bucket's default scope is used.                                                                                            |
| collection | (Optional) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the default collection in the bucket's default scope is used.                                                             |

For example, `` default:`travel-sample` `` indicates the default collection in the default scope in the `travel-sample` bucket in the `default` namespace.

Similarly, `` default:`travel-sample`.inventory.airline `` indicates the `airline` collection in the `inventory` scope in the `travel-sample` bucket in the `default` namespace.

#### [](#keyspace-partial)Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the keyspace reference may be just the collection name with no path. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |

For example, `airline` indicates the `airline` collection, assuming the query context is set.

### [](#index-key)Index Key

```ebnf
index-key ::= expr | array-expr
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-key.png) 

Refers to an attribute name or a scalar function or an ARRAY expression on the attribute. This constitutes an index-key for the index.

| expr       | A SQL++ [expression](index.md) over any fields in the document. This cannot use constant expressions, aggregate functions, or sub-queries.                                                                                 |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| array-expr | An array expression. Array indexing enables you to create global indexes on array elements and optimize the execution of queries involving array elements. For more information, see [Array Indexing](indexing-arrays.md). |

### [](#index-key-attrib)Index Key Attributes

```ebnf
lead-key-attribs ::= index-order include-missing? | include-missing index-order?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/lead-key-attribs.png) 

```ebnf
key-attribs ::= index-order
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/key-attribs.png) 

Specifies attributes for the index key.

| index-order     | (Optional) All index keys may include an index order clause. See [Index Order](#index-order) below.                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| include-missing | (Optional) The leading index key may also include INCLUDE MISSING clause. See [INCLUDE MISSING Clause](#include-missing) below. |

#### [](#index-order)Index Order

```ebnf
index-order ::= 'ASC' | 'DESC'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-order.png) 

Specifies the sort order of the index key.

| ASC  | The index key is sorted in ascending order.  |
| ---- | -------------------------------------------- |
| DESC | The index key is sorted in descending order. |

This clause is optional; if omitted, the default is `ASC`.

> [!TIP]
> If any queries that use this index include an ordering term on the same field as this index key, the sort order of the ordering term should match the sort order of the index key to ensure the best performance.
> 
> For example, if the index uses a descending sort order, then the query should also use a descending sort order. If the query uses the opposite sort order to the index, you may experience reduced performance.
> 
> If necessary, you could create two indexes that are identical except for opposite sort orders, and then use an index hint in the query to select the appropriate index.

#### [](#include-missing)INCLUDE MISSING Clause

```ebnf
include-missing ::= 'INCLUDE' 'MISSING'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/include-missing.png) 

The optional `INCLUDE MISSING` clause ensures that documents which do not include the index key field are indexed regardless. If this clause is not present, then documents without the index key field are not indexed.

The `INCLUDE MISSING` clause can only be applied to the leading index key. The `INCLUDE MISSING` clause may be included before or after the `ASC` or `DESC` keyword.

### [](#index-partition)PARTITION BY HASH Clause

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Used to partition the index. Index partitioning helps increase the query performance by dividing and spreading a large index of documents across multiple nodes, horizontally scaling out an index as needed. For more information, see [Index Partitioning](index-partitioning.md).

### [](#where-clause)WHERE Clause

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/where-clause.png) 

| cond | Specifies WHERE clause predicates to qualify the subset of documents to include in the index. |
| ---- | --------------------------------------------------------------------------------------------- |

### [](#index-using)USING Clause

```ebnf
index-using ::= 'USING' 'GSI'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-using.png) 

The index type for a secondary index must be Global Secondary Index (GSI). The `USING GSI` keywords are optional and may be omitted.

### [](#index-with)WITH Clause

```ebnf
index-with ::= 'WITH' expr
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-with.png) 

Use the WITH clause to specify additional options.

| expr | An object with the following properties. |
| ---- | ---------------------------------------- |

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Schema       |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **nodes** _optional_        | An array of strings, each of which represents a node name. In Couchbase Server versions 7.6.0 and 7.6.1, when you enabled file-based rebalance you could not use this option to choose which Index Service nodes would contain the index. Couchbase Server 7.6.2 and later have removed this restriction. See [Index Rebalance Methods](../../learn/clusters-and-availability/rebalance.md#index-rebalance-methods). [COMMUNITY EDITION](https://www.couchbase.com/products/editions) In Couchbase Server Community Edition, a single secondary index of type GSI can be placed on a single node that runs the Indexing Service. The nodes property enables you to specify the node that the index is placed on. If nodes is not specified, the Index planner may place the index on any of the nodes running the Indexing Service. [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) In Couchbase Server Enterprise Edition, you can specify multiple nodes to distribute replicas of an index across nodes running the Indexing Service: for example, WITH {"nodes": \["node1:8091", "node2:8091", "node3:8091"\]}. For more information and examples, see [Index Replication](../../learn/services-and-indexes/indexes/index-replication.md#index-replication). If nodes is not specified, then the system places the new index and any replicas on any of the nodes running the Indexing Service, in order to achieve the best resource utilization. This is done by taking into account the current resource usage statistics of index nodes. If you specify the nodes property by itself, the index is placed on one of the destination nodes, and a replica is placed on each of the others. If you specify both nodes and num\_replica, the Index planner chooses from the set of specified nodes to place the index and its replicas. In this case, the number of nodes in the array must be greater than the specified number of replicas. Otherwise, the index creation fails. A node name passed to the nodes property must include the cluster administration port, by default 8091. **Example:** \["192.0.2.0:8091"\] | String array |
| **defer\_build** _optional_ | Whether the index should be created in deferred build mode. When set to true, the CREATE INDEX operation queues the task for building the GSI index but immediately pauses the building of the index. Index building requires an expensive scan operation. Deferring building of the index with multiple indexes can optimize the expensive scan operation. Admins can defer building multiple indexes and, using the BUILD INDEX statement, build multiple indexes efficiently with one efficient scan of bucket data. When set to false, the CREATE INDEX operation queues the task for building the GSI index and immediately kicks off the building of the index. **Default:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean      |
| **num\_replica** _optional_ | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) This property is only available in Couchbase Server Enterprise Edition. The number of [replicas](../../learn/services-and-indexes/indexes/index-replication.md#index-replication) of the index to create. The indexer will automatically distribute these replicas amongst index nodes in the cluster for load-balancing and high availability purposes. The indexer will attempt to distribute the replicas based on the server groups in use in the cluster where possible. The number of replicas must be lower than the number of index nodes in the cluster. If nodes is specified, the number of replicas must be lower than the number of nodes in the array. Otherwise, the index creation fails. **Default:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer      |

Partitioned indexes support further options. See [Index Partitioning](index-partitioning.md).

## [](#usage)Usage

> [!NOTE]
> It's not recommended to create (or drop) secondary indexes when any node with a secondary index role is down, as this may result in duplicate index names.

### [](#monitoring-indexes)Monitoring Indexes

Index metadata provides a state field. This state field and other index metadata can be queried using [system:indexes](../n1ql-intro/sysinfo.md#querying-indexes). The index state may be `scheduled for creation`, `deferred`, `building`, `pending`, `online`, `offline`, or `abridged`. You can also monitor the index state using the Couchbase Web Console.

> [!IMPORTANT]
> If you kick off multiple index creation operations concurrently, you may sometimes see transient errors similar to the following. If this error occurs, the Index Service tries to run the failed operation again in the background until it succeeds, up to a maximum of 1000 retries.
> 
> ```json
> [
>   {
>     "code": 5000,
>     "msg": "GSI CreateIndex() - cause: Encountered transient error.  Index creation will be retried in background.  Error: Index ... will retry building in the background for reason: Build Already In Progress. Keyspace ...",
>     "query": "..."
>   }
> ]
> ```
> 
> If the Index Service still cannot create the index after the maximum number of retries, the index state is marked as `offline`. You must drop the failed index using the `DROP INDEX` command.

### [](#indexing-metadata)Using the `meta().id` Function

You can create indexes on metadata information. For more information, see [Indexing Meta Info](indexing-meta-info.md).

### [](#index-aggregates)Using Indexes for Aggregates

If you have an index on a simple expression, such as `geo.alt`, you can use that index to satisfy a query on an [aggregate](aggregatefun.md) of that expression, such as `MIN(geo.alt)` or `MAX(geo.alt)`. For more information and examples, see [Operator Pushdowns](../../learn/services-and-indexes/indexes/index%5Fpushdowns.md#operator-pushdowns).

### [](#index-replicas)Index Replicas

In the [Indexes screen in the Couchbase Web Console](../../manage/manage-ui/manage-ui.md#console-indexes), index replicas are marked with their replica ID.

![The Indexes screen showing an index and index replica with replica ID](../_images/create-index-replica-id.png) 

If you select `view by server node` from the drop-down menu, you can see the server node where each index and index replica is placed.

You can also query the [system:indexes](../n1ql-intro/sysinfo.md#querying-indexes) catalog to find the ID of an index replica and see which node it is placed on.

> [!NOTE]
> By default, index replicas are used to serve index scans. The system automatically load-balances an index scan across the index and all its replicas. Adding index replicas enables you to scale scan throughput, in addition to providing high availability.

### [](#defer-index-builds-by-default)Defer Index Builds by Default

Couchbase Server 7.6.2

Usually, the default setting for the `defer_build` option is `false`. In Couchbase Server 7.6.2 and later, you can change the default setting for the `defer_build` option.

If you change the default setting for `defer_build` to `true`, index creation operates in deferred build mode by default.

To change the default setting for deferred builds, use the REST API to set the `indexer.settings.defer_build` property. For example,

```sh
curl http://$BASEURL:9102/settings -u $USER:$PASSWORD \
-d '{"indexer.settings.defer_build": true}'
```

Use the following command to retrieve the indexer settings:

```sh
curl -X GET http://$BASEURL:9102/settings -u $USER:$PASSWORD
```

* `$BASEURL` is the base URL for the API call, for example: `localhost`.
* `$USER` is the username, for example: `Administrator`.
* `$PASSWORD` is the password.

## [](#examples)Examples

To try the examples in this section, you must set the query context as described in each example.

Example 1\. Create an index in the default scope and collection

For this example, unset the query context. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Create a secondary index that contains airports with an `alt` value greater than 1000 on the node `127.0.0.1`.

```sqlpp
CREATE INDEX idx_default_over1000
  ON `travel-sample`(geo.alt)
  WHERE geo.alt > 1000
  USING GSI
  WITH {"nodes": ["127.0.0.1:8091"]};
```

Example 2\. Create an index in a named scope and collection

For this example, the path to the required keyspace is specified by the query, so you do not need to set the query context.

Create a secondary index that contains airports with an `alt` value greater than 1000 on the node `127.0.0.1`.

```sqlpp
CREATE INDEX idx_airport_over1000
  ON `travel-sample`.inventory.airport(geo.alt)
  WHERE geo.alt > 1000
  USING GSI
  WITH {"nodes": ["127.0.0.1:8091"]};
```

Example 3\. Create a deferred index

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Create a secondary index with the `defer_build` option.

```sqlpp
CREATE INDEX idx_landmark_country
  ON landmark(country)
  USING GSI
  WITH {"defer_build":true};
```

Query `system:indexes` for the status of the index.

```sqlpp
SELECT * FROM system:indexes WHERE name="idx_landmark_country";
```

Results

```json
[
  {
    "indexes": {
      "bucket_id": "travel-sample",
      "datastore_id": "http://127.0.0.1:8091",
      "id": "d079aec40eb0c6cc",
      "index_key": [
        "`country`"
      ],
      "keyspace_id": "landmark",
      "name": "idx_landmark_country",
      "namespace_id": "default",
      "scope_id": "inventory",
      "state": "deferred", (1)
      "using": "gsi"
    }
  }
]
```

| **1** | The index is in the deferred state. |
| ----- | ----------------------------------- |

Example 4\. Build a deferred index

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Kick off a deferred build using the index name.

```sqlpp
BUILD INDEX ON landmark(idx_landmark_country) USING GSI;
```

Query `system:indexes` for the status of the index.

```sqlpp
SELECT * FROM system:indexes WHERE name="idx_landmark_country";
```

Results

```json
[
  {
    "indexes": {
      "bucket_id": "travel-sample",
      "datastore_id": "http://127.0.0.1:8091",
      "id": "d079aec40eb0c6cc",
      "index_key": [
        "`country`"
      ],
      "keyspace_id": "landmark",
      "name": "idx_landmark_country",
      "namespace_id": "default",
      "scope_id": "inventory",
      "state": "online", (1)
      "using": "gsi"
    }
  }
]
```

| **1** | The index has now been created. |
| ----- | ------------------------------- |

Example 5\. Create index with missing leading key

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

The following statement will not index airports where the `district` field is missing.

```n1ql
CREATE INDEX idx_airport_missing
ON airport(district, name);
```

The following statement will index all airports, even if the `district` field is not included in the document.

```n1ql
CREATE INDEX idx_airport_include
ON airport(district INCLUDE MISSING, name);
```

For more examples of indexes where the leading key may be missing, see [Index Selection](selectintro.md#index-selection).