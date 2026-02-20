---
title: CREATE VECTOR INDEX
description: The CREATE VECTOR INDEX statement allows you to create Hyperscale
  Vector indexes.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/createvectorindex.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-language-reference/createvectorindex.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/createvectorindex.html)

# CREATE VECTOR INDEX

The `CREATE VECTOR INDEX` statement allows you to create Hyperscale Vector indexes.

To create secondary indexes or Composite Vector indexes, use the [CREATE INDEX](createindex.md) statement.

## [](#purpose)Purpose

`CREATE VECTOR INDEX` allows you to make multiple concurrent index creation requests. The command starts a task to create the index definition in the background. If there is an index creation task already running, the Index Service queues the incoming index creation request. `CREATE VECTOR INDEX` returns as soon as the index creation phase is complete.

By default, when the index creation phase is complete, the Index Service triggers the index build phase. If you lose connectivity, the index build operation continues in the background. You can defer the index build phase using the `defer_build` clause. In deferred build mode, `CREATE VECTOR INDEX` creates the index definition, but does not trigger the index build phase. You can then build the index using the [BUILD INDEX](build-index.md) command.

You can create multiple identical secondary indexes on a keyspace and place them on separate nodes for better index availability. The recommended way to do this is using the `num_replica` option. For more information, see [WITH Clause](#index-with).

Hyperscale Vector indexes and Composite Vector indexes require a codebook for the vector field. The codebook is the result of sampling the dataset and is saved as part of the index metadata.

The codebook is created as part of the [BUILD INDEX](build-index.md) process, and is not incrementally updated. If the data set changes dramatically, you must drop and rebuild the index to update the codebook.

## [](#prerequisites)Prerequisites

##### RBAC Privileges

To execute the CREATE VECTOR INDEX statement, your client must have the `Query Manage Index` privilege granted on the keyspace. For more information about cluster access privileges, see [Manage Cluster Access Credentials](../../clusters/manage-database-users.md).

## [](#syntax)Syntax

```ebnf
create-vector-index ::= 'CREATE' 'VECTOR' 'INDEX' ( index-name ( 'IF' 'NOT' 'EXISTS' )? |
                        'IF' 'NOT' 'EXISTS' index-name ) 'ON' keyspace-ref
                        '(' index-key-and-attrib ')'
                        index-include? index-partition? where-clause? index-using? index-with?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/create-vector-index.png) 

| index-name           | (Required) A unique name that identifies the index. Valid GSI index names can contain any of the following characters: A-Z a-z 0-9 # \_, and must start with a letter, \[A-Z a-z\]. The minimum length of an index name is 1 character and there is no maximum length set for an index name. When querying, if the index name contains a # or \_ character, you must enclose the index name within backticks. |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| keyspace-ref         | (Required) Specifies the keyspace where the index is created. See [Keyspace Reference](#keyspace-ref).                                                                                                                                                                                                                                                                                                        |
| index-key-and-attrib | (Required) Specifies the index key and index key attribute. See [Index Key and Attribute](#index-key-and-attrib).                                                                                                                                                                                                                                                                                             |
| index-include        | (Optional) Specifies non-key fields to include in the index. See [INCLUDE Clause](#index-include).                                                                                                                                                                                                                                                                                                            |
| index-partition      | (Optional) Specifies index partitions. See [PARTITION BY HASH Clause](#index-partition).                                                                                                                                                                                                                                                                                                                      |
| where-clause         | (Optional) Specifies filters for a partial index. See [WHERE Clause](#where-clause).                                                                                                                                                                                                                                                                                                                          |
| index-using          | (Optional) Specifies the index type. See [USING Clause](#index-using).                                                                                                                                                                                                                                                                                                                                        |
| index-with           | (Optional) Specifies options for the index. See [WITH Clause](#index-with).                                                                                                                                                                                                                                                                                                                                   |

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
> If there is a hyphen (-) inside any part of the keyspace reference, you must wrap that part of the keyspace reference in backticks (\` \`). See the examples on this page.

#### [](#keyspace-path)Keyspace Path

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

If the keyspace is a named collection, or the default collection in the default scope within a bucket, the keyspace reference may be a keyspace path. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

| namespace  | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                                                                                                           |
| scope      | (Optional) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the bucket’s default scope is used.                                                                                            |
| collection | (Optional) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the default collection in the bucket’s default scope is used.                                                             |

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

### [](#index-key-and-attrib)Index Key and Attribute

```ebnf
index-key-and-attrib ::= index-key index-vector
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-key-and-attrib.png) 

Hyperscale Vector indexes only have one key, which must be a vector field. The index key takes one attribute, the VECTOR keyword.

| index-key    | (Required) Specifies an index key. See [Index Key](#index-key).                             |
| ------------ | ------------------------------------------------------------------------------------------- |
| index-vector | (Required) Specifies an attribute for the index key. See [VECTOR Keyword](#include-vector). |

#### [](#index-key)Index Key

```ebnf
index-key ::= expr | array-expr
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-key.png) 

The index key is a SQL++ [expression](index.md) referring to a vector field, or an ARRAY expression on the vector field.

| expr       | The name of a vector field in the document, or a [BASE64\_DECODE()](metafun.md#base64-decode) function on the vector field — this is necessary if the embedded vectors are stored as a base64-encoded string.                                                                                              |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| array-expr | An array expression on a vector field in the document. Only ALL ARRAY is supported. The [FLATTEN\_KEYS()](metafun.md#flatten%5Fkeys) function is supported, but more than one key in [FLATTEN\_KEYS()](metafun.md#flatten%5Fkeys) is not permitted. For details, see [Array Indexing](indexing-arrays.md). |

#### [](#include-vector)VECTOR Keyword

```ebnf
index-vector ::= 'VECTOR'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-vector.png) 

Indicates that the index key is a vector field.

### [](#index-include)INCLUDE Clause

```ebnf
index-include ::= 'INCLUDE' '(' expr ( ',' expr )* ')'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-include.png) 

Used to include scalar fields in the index, which you can use to filter the vector search. The INCLUDE clause cannot include a vector field. For details, see [Use Scalar Columns to Filter Hyperscale Vector Index Scans](../../vector-index/hyperscale-filter.md).

| expr | A SQL++ [expression](index.md) referring to any scalar field in the document. |
| ---- | ----------------------------------------------------------------------------- |

### [](#index-partition)PARTITION BY HASH Clause

Used to partition the index. Index partitioning helps increase the query performance by dividing and spreading a large index of documents across multiple nodes, horizontally scaling out an index as needed. For more information, see [Index Partitioning](index-partitioning.md).

With Hyperscale Vector indexes and Composite Vector indexes, training is done for each index node independently, and the codebook is provided to all partitions on that node. If there are multiple partitions for an index on a node, training is only done once for all partitions. See [The Importance of Index Training](../../vector-index/vectors-and-indexes-overview.md#index-training).

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

| Name                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Schema       |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **nodes** _optional_                 | An array of strings, each of which represents a node name. In clusters running Couchbase Server versions 7.6.0 and 7.6.1, you cannot use this option to choose which Index Service nodes contain the index. Clusters running Couchbase Server 7.6.2 and later do not have this restriction. See [Index Rebalance Methods](../../../server/current/learn/clusters-and-availability/rebalance.md#index-rebalance-methods). You can specify multiple nodes to distribute replicas of an index across nodes running the Indexing Service: for example, WITH {"nodes": \["node1:8091", "node2:8091", "node3:8091"\]}. For more information and examples, see [Index Replication](../../indexes/index-replication.md#index-replication). If nodes is not specified, then the system places the new index and any replicas on any of the nodes running the Indexing Service, in order to achieve the best resource utilization. This is done by taking into account the current resource usage statistics of index nodes. If you specify the nodes property by itself, the index is placed on one of the destination nodes, and a replica is placed on each of the others. If you specify both nodes and num\_replica, the Index planner chooses from the set of specified nodes to place the index and its replicas. In this case, the number of nodes in the array must be greater than the specified number of replicas. Otherwise, the index creation fails. A node name passed to the nodes property must include the cluster administration port, by default 8091. **Example:** \["192.0.2.0:8091"\] | String array |
| **defer\_build** _optional_          | Whether the index should be created in deferred build mode. When set to true, the CREATE VECTOR INDEX operation queues the task for building the GSI index but immediately pauses the building of the index. Index building requires an expensive scan operation. Deferring building of the index with multiple indexes can optimize the expensive scan operation. Admins can defer building multiple indexes and, using the BUILD INDEX statement, build multiple indexes efficiently with one efficient scan of bucket data. When set to false, the CREATE VECTOR INDEX operation queues the task for building the GSI index and immediately kicks off the building of the index. **Default:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean      |
| **num\_replica** _optional_          | The number of [replicas](../../indexes/index-replication.md#index-replication) of the index to create. The indexer will automatically distribute these replicas amongst index nodes in the cluster for load-balancing and high availability purposes. The indexer will attempt to distribute the replicas based on the server groups in use in the cluster where possible. The number of replicas must be lower than the number of index nodes in the cluster. If nodes is specified, the number of replicas must be lower than the number of nodes in the array. Otherwise, the index creation fails. **Default:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer      |
| **dimension** _required_             | The number of dimensions in the vector. The embedded model you use to embed the vectors determines the number of dimensions in the vector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer      |
| **similarity** _optional_            | Sets the distance metric to use when comparing vectors during index creation. Couchbase Capella uses the following strings to represent the distance metrics: COSINE [Cosine Similarity](../../vector-index/vectors-and-indexes-overview.md#cosine) DOT [Dot Product](../../vector-index/vectors-and-indexes-overview.md#dot) L2 EUCLIDEAN [Euclidean Distance](../../vector-index/vectors-and-indexes-overview.md#euclidean) L2\_SQUARED EUCLIDEAN\_SQUARED [Euclidean Squared Distance](../../vector-index/vectors-and-indexes-overview.md#euclidean-squared) For the greatest accuracy, use the distance metric you plan to use to query the data. **Default:** L2\_SQUARED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String       |
| **description** _optional_           | The settings for the quantization and index algorithms. The string is made up of the following settings: IVF The number of centroids allocated for the index. SQ For scalar quantization — the number of bits used to store the centroid for each bin. PQ For product quantization — the number of subquantizers, and the number of bits in the centroid’s index value. For more information, see [Quantization and Centroid Settings](../../vector-index/hyperscale-vector-index.md#algo%5Fsettings). **Pattern:** ^IVF\[0-9\]\*,(SQ\[468\]\|PQ\[0-9\]+x\[0-9\]+)$ **Default:** IVF,SQ8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **scan\_nprobes** _optional_         | The number of cells to search for each scan. **Default:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer      |
| **train\_list** _optional_           | The size of the sample set of vectors to be used for index training. If the index count is < 10000, the default is to sample everything. Otherwise, the default value is 10% of the index count, or 10 × the number of centroids, whichever is higher. **Maximum:** 1000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer      |
| **persist\_full\_vector** _optional_ | If true (the default), the index stores the full vector value in addition to the quantized value. This significantly increases the size of the index. Set to false if you do not plan to use reranking. For more information, see [Hyperscale Vector Index Reranking and Full Vector Persistence](../../vector-index/hyperscale-reranking.md). **Default:** true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean      |

Partitioned indexes support further options. See [Index Partitioning](index-partitioning.md).

## [](#usage)Usage

> [!IMPORTANT]
> Attention
> 
> Do not create (or drop) secondary indexes, Composite Vector indexes, or Hyperscale Vector indexes when any Index service node is down, as this may result in duplicate index names.

### [](#monitoring-indexes)Monitoring Indexes

Index metadata provides a state field. This state field and other index metadata can be queried using [system:indexes](../n1ql-intro/sysinfo.md#querying-indexes). The index state may be `scheduled for creation`, `deferred`, `building`, `pending`, `online`, `offline`, or `abridged`. You can also monitor the index state using the Capella UI.

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

### [](#index-replicas)Index Replicas

In the [Indexes page in the Couchbase Capella UI](../../clusters/index-service/manage-indexes.md), index replicas are marked with their replica ID.

To see the nodes where an index and its replicas are placed, click the name of an index or index replica to display the index definition.

You can also query the [system:indexes](../n1ql-intro/sysinfo.md#querying-indexes) catalog to find the ID of an index replica and see which node it’s placed on.

> [!NOTE]
> By default, index replicas are used to serve index scans. The system automatically load-balances an index scan across the index and all its replicas. Adding index replicas enables you to scale scan throughput, in addition to providing high availability.

With Hyperscale Vector indexes and Composite Vector indexes, training is done by each replica index independently, and the codebook is stored as part of index metadata. See [The Importance of Index Training](../../vector-index/vectors-and-indexes-overview.md#index-training).

## [](#examples)Examples

To try the examples in this section, you must install the `color-vector-sample` data as described in [Prerequisites](../../vector-index/hyperscale-vector-index.md#prerequisites).

Example 1\. Create a Hyperscale Vector index

For this example, the path to the required keyspace is specified by the query, so you do not need to set the query context.

Create a Hyperscale Vector index for the vector column named `embedding-vector-dot`.

```sqlpp
CREATE VECTOR INDEX `color_desc_hyperscale` 
       ON `color-vector-sample`.`color`.`rgb`(`embedding_vector_dot` VECTOR)
       WITH { "dimension":1536, "similarity":"L2", "description":"IVF8,SQ4" }
```

Example 2\. Create a Hyperscale Vector index with included scalar values

For this example, the path to the required keyspace is specified by the query, so you do not need to set the query context.

Create a Hyperscale Vector index for the vector column named `embedding-vector-dot`, including the scalar `brightness` field.

```sqlpp
CREATE VECTOR INDEX `color_desc_hyperscale_brightness` 
       ON `color-vector-sample`.`color`.`rgb`(`embedding_vector_dot` VECTOR)
       INCLUDE (`brightness`)
       WITH { "dimension":1536, "similarity":"L2", "description":"IVF8,SQ4" }
```

Example 3\. Create a Hyperscale Vector index with no reranking

For this example, the path to the required keyspace is specified by the query, so you do not need to set the query context.

Create a Hyperscale Vector index from the example RGB dataset that does not persist the full vector value.

```sqlpp
CREATE VECTOR INDEX `color_desc_hyperscale_no_persist` 
       ON `color-vector-sample`.`color`.`rgb`(`embedding_vector_dot` VECTOR)
       WITH { "dimension":1536, "similarity":"L2", "description":"IVF8,SQ4", 
              "persist_full_vector": false};
```

## [](#related-links)Related Links

* [Primary and Secondary Index Reference](../../indexes/indexing-overview.md)
* [Filtered Search Using Composite Vector Indexes](../../vector-index/composite-vector-index.md)
* [Vector Search Using Hyperscale Vector Indexes](../../vector-index/hyperscale-vector-index.md)
* [CREATE PRIMARY INDEX](createprimaryindex.md)| [CREATE INDEX](createindex.md)
* [BUILD INDEX](build-index.md)
* [ALTER INDEX](alterindex.md)| [ALTER VECTOR INDEX](altervectorindex.md)
* [DROP PRIMARY INDEX](dropprimaryindex.md)| [DROP INDEX](dropindex.md)| [DROP VECTOR INDEX](dropvectorindex.md)