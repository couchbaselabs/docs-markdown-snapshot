---
title: Drop Indexes
description: How to drop primary and secondary indexes.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/drop-index.adoc
  xref: xref:server:guides:drop-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/guides/drop-index.html)

# Drop Indexes

> How to drop primary and secondary indexes. 

## [](#introduction)Introduction

You can drop primary and secondary indexes when you do not need them any more. Dropping an index that has replicas will also drop all of the replica indexes too.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#dropping-a-primary-index)Dropping a Primary Index

You can drop a primary index using a SQL++ statement or an SDK call.

> [!NOTE]
> The SDK calls only enable you to drop indexes in the default collection and default scope within a bucket. A SQL++ statement enables you to drop indexes in _any_ collection and scope within a bucket.

* SQL++
* .NET
* Java
* Node.js
* Python

To drop an unnamed primary index, use the `DROP PRIMARY INDEX` statement.

To drop a named primary index, use the `DROP INDEX` statement. This statement has two possible syntaxes:

* Specify the index name, then use the `ON` keyword to specify the keyspace which contains the index.
* Specify the keyspace and index name using dotted notation.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query drops an unnamed primary index from the `airline` keyspace.

```sqlpp
DROP PRIMARY INDEX ON airline;
```

The following query drops a named primary index from the `airline` keyspace.

```sqlpp
DROP INDEX travel_primary ON airline;
```

The following query drops the index in exactly the same way, but uses alternative syntax.

```sqlpp
DROP INDEX airline.travel_primary;
```

For more information and examples, see [DROP PRIMARY INDEX](../n1ql/n1ql-language-reference/dropprimaryindex.md) and [DROP INDEX](../n1ql/n1ql-language-reference/dropindex.md).

To drop a primary index, use the task `DropPrimaryIndexAsync()` on the interface `IQueryIndexManager`.

1. Specify the keyspace which contains the index.
2. If the index has a name:

  1. Use `DropPrimaryQueryIndexOptions` to specify the index options.
  2. In the index options, invoke the `IndexName` method.

---

The following example drops an unnamed primary index from the specified keyspace.

```csharp
await cluster.QueryIndexes.DropPrimaryIndexAsync("`travel-sample`");
```

The following example drops a named primary index from the specified keyspace.

```csharp
await cluster.QueryIndexes.DropPrimaryIndexAsync(
	"`travel-sample`",
	options => options.IndexName("named_primary_index")
);
```

Click the  View button to see this code in context.

For more information, see [IQueryIndexManager()](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.IQueryIndexManager.html).

To drop a primary index, use the `dropPrimaryIndex` method and specify the keyspace which contains the index.

> [!NOTE]
> The Java SDK does not provide a call for dropping a named primary index. To drop a named primary index, use a SQL++ query.

---

The following example drops an unnamed primary index from the specified keyspace.

```java
cluster.queryIndexes().dropPrimaryIndex("travel-sample");
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/QueryIndexManager.html).

To drop a primary index, use the `dropPrimaryIndex` function on a `QueryIndexManager` object.

1. Specify the keyspace which contains the index.
2. If the index has a name:

  1. Use `DropPrimaryQueryIndexOptions` to specify the index options.
  2. In the index options, use the `name` property to specify the index name.

---

The following example drops an unnamed primary index from the specified keyspace.

```nodejs
Unresolved include directive in modules/guides/pages/drop-index.adoc - include::nodejs-sdk:hello-world:example$index-hello-world.js[]
```

The following example drops a named primary index from the specified keyspace.

```nodejs
Unresolved include directive in modules/guides/pages/drop-index.adoc - include::nodejs-sdk:hello-world:example$index-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/QueryIndexManager.html).

To drop a primary index, use the `drop_primary_index` function on a `QueryIndexManager` object.

1. Specify the keyspace which contains the index.
2. If the index has a name:

  1. Use `DropPrimaryQueryIndexOptions` to specify the index options.
  2. In the index options, use the `index_name` property to specify the index name.

---

The following example drops an unnamed primary index from the specified keyspace.

```python
cluster.query_indexes().drop_primary_index(
    "travel-sample"
)
```

The following example drops a named primary index from the specified keyspace.

```python
cluster.query_indexes().drop_primary_index(
    "travel-sample",
    DropPrimaryQueryIndexOptions(index_name="named_primary_index")
)
```

Click the  View button to see this code in context.

For more information, see [SQL++ Index Management](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#n1ql-index-management).

## [](#dropping-a-secondary-index)Dropping a Secondary Index

You can drop a secondary index using a SQL++ statement or an SDK call.

> [!NOTE]
> The SDK calls only enable you to drop indexes in the default collection and default scope within a bucket. A SQL++ statement enables you to drop indexes in _any_ collection and scope within a bucket.

* SQL++
* .NET
* Java
* Node.js
* Python

To drop a secondary index, use the `DROP INDEX` statement. This statement has two possible syntaxes:

* Specify the index name, then use the `ON` keyword to specify the keyspace which contains the index.
* Specify the keyspace and index name using dotted notation.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query drops a named index from the `airline` keyspace.

```sqlpp
DROP INDEX `idx-name` ON airline;
```

The following query drops the index in exactly the same way, but uses alternative syntax.

```sqlpp
DROP INDEX airline.`idx-name`;
```

For more information and examples, see [DROP INDEX](../n1ql/n1ql-language-reference/dropindex.md).

To drop a secondary index, use the task `DropIndexAsync()` on the interface `IQueryIndexManager`.

1. Specify the keyspace which contains the index.
2. Specify the name of the index.

---

The following example drops a named index from the specified keyspace.

```csharp
await cluster.QueryIndexes.DropIndexAsync("`travel-sample`", "index_name");
```

Click the  View button to see this code in context.

For more information, see [IQueryIndexManager()](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.IQueryIndexManager.html).

To drop a secondary index, use the `dropIndex` method.

1. Specify the keyspace which contains the index.
2. Specify the name of the index.

---

The following example drops a named index from the specified keyspace.

```java
cluster.queryIndexes().dropIndex("travel-sample", "index_name");
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/QueryIndexManager.html).

To drop a secondary index, use the `dropIndex` function on a `QueryIndexManager` object.

1. Specify the keyspace which contains the index.
2. Specify the name of the index.

---

The following example drops a named index from the specified keyspace.

```nodejs
Unresolved include directive in modules/guides/pages/drop-index.adoc - include::nodejs-sdk:hello-world:example$index-hello-world.js[]
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/QueryIndexManager.html).

To drop a secondary index, use the `drop_index` function on a `QueryIndexManager` object.

1. Specify the keyspace which contains the index.
2. Specify the name of the index.

---

The following example drops a named index from the specified keyspace.

```python
cluster.query_indexes().drop_index("travel-sample", "index_name")
```

Click the  View button to see this code in context.

For more information, see [SQL++ Index Management](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#n1ql-index-management).

## [](#related-links)Related Links

Reference and explanation:

* [Primary and Secondary Index Reference](../indexes/indexing-overview.md)

Administrator guides:

* [Manage Indexes](../manage/manage-indexes/manage-indexes.md)
* [Monitor Indexes](../manage/monitor/monitoring-indexes.md)

Indexes with SDKs:

* [C](../../../c-sdk/current/concept-docs/n1ql-query.md#indexes)| [C++](../../../cxx-sdk/current/concept-docs/n1ql-query.md#indexes)| [.NET](../../../dotnet-sdk/current/concept-docs/n1ql-query.md#indexes)| [Go](../../../go-sdk/current/concept-docs/n1ql-query.md#indexes)| [Java](../../../java-sdk/current/concept-docs/n1ql-query.md#indexes)| Kotlin | [Node.js](../../../nodejs-sdk/current/concept-docs/n1ql-query.md#indexes)| [PHP](../../../php-sdk/current/concept-docs/n1ql-query.md#indexes)| [Python](../../../python-sdk/current/concept-docs/n1ql-query.md#indexes)| [Ruby](../../../ruby-sdk/current/concept-docs/n1ql-query.md#indexes)| [Rust](../../../rust-sdk/current/concept-docs/n1ql-query.md#indexes)| [Scala](../../../scala-sdk/current/concept-docs/n1ql-query.md#indexes)