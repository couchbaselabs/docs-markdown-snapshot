---
title: Deferring Indexes
description: How to create deferred indexes and build them later.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/defer-index.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:guides:defer-index.adoc[]
---

[View original HTML](/server/7.2/guides/defer-index.html)

# Deferring Indexes

> How to create deferred indexes and build them later.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

When you create a primary or secondary index, you can mark it as deferred. This means the index is not built at once; you can build the deferred index later. This enables you to build multiple indexes more efficiently.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#deferring-an-index)Deferring an Index

You can defer an index to be built later using a SQL++ statement or an SDK call.

> [!NOTE]
> The SDK calls only enable you to create indexes in the default collection and default scope within a bucket. A N1QL statement enables you to create indexes in _any_ collection and scope within a bucket.

* SQL++
* .NET
* Java
* Node.js
* Python

To defer a primary or secondary index to be built later:

1. Use the `WITH` clause to specify the index options.
2. In the index options, set the `defer_build` attribute to `true`.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following queries create a set of primary and secondary indexes in the `landmark` keyspace, with build deferred until later.

```sqlpp
CREATE INDEX idx_landmark_country
  ON landmark(country)
  USING GSI
  WITH {"defer_build":true};
```

```sqlpp
CREATE INDEX idx_landmark_name 
  ON landmark(name)
  USING GSI
  WITH {"defer_build":true};
```

```sqlpp
CREATE PRIMARY INDEX idx_landmark_primary
  ON landmark
  USING GSI
  WITH {"defer_build":true};
```

For more information and examples, see [CREATE PRIMARY INDEX](../n1ql/n1ql-language-reference/createprimaryindex.md) and [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md).

To defer a primary or secondary index to be built later:

1. Use `CreatePrimaryQueryIndexOptions` or `CreateQueryIndexOptions` to specify the index options.
2. In the index options, invoke the `Deferred` method with the argument `true`.

---

The following examples create a set of primary and secondary indexes in the specified keyspace, with build deferred until later.

```csharp
await cluster.QueryIndexes.CreatePrimaryIndexAsync(
	"`travel-sample`",
	 options => options.Deferred(true)
);
```

```csharp
await cluster.QueryIndexes.CreateIndexAsync(
	"`travel-sample`",
	"idx_name_email",
	new[] { "name", "email" },
	options => options.Deferred(true)
);
```

Click the  View button to see this code in context.

For more information, see [CreatePrimaryQueryIndexOptions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.CreatePrimaryQueryIndexOptions.html) and [CreateQueryIndexOptions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.CreateQueryIndexOptions.html).

To defer a primary or secondary index to be built later:

1. Use `CreatePrimaryQueryIndexOptions` or `CreateQueryIndexOptions` to specify the index options.
2. In the index options, invoke the `deferred` method with the argument `true`.

---

The following examples create a set of primary and secondary indexes in the specified keyspace, with build deferred until later.

```java
CreatePrimaryQueryIndexOptions primaryOpts = CreatePrimaryQueryIndexOptions
    .createPrimaryQueryIndexOptions()
    .deferred(true);

cluster.queryIndexes().createPrimaryIndex("travel-sample", primaryOpts);
```

```java
CreateQueryIndexOptions secondaryOpts = CreateQueryIndexOptions
    .createQueryIndexOptions()
    .deferred(true);

cluster.queryIndexes().createIndex(
  "travel-sample", 
  "idx_name_email",	
  Arrays.asList("name", "email"), 
  secondaryOpts
);
```

Click the  View button to see this code in context.

For more information, see [CreatePrimaryQueryIndexOptions](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/CreatePrimaryQueryIndexOptions.html) and [CreateQueryIndexOptions](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/CreateQueryIndexOptions.html).

To defer a primary or secondary index to be built later:

1. Use `CreatePrimaryQueryIndexOptions` or `CreateQueryIndexOptions` to specify the index options.
2. In the index options, set the `deferred` property to `true`.

---

The following examples create a set of primary and secondary indexes in the specified keyspace, with build deferred until later.

```nodejs
await cluster
  .queryIndexes()
  .createPrimaryIndex('travel-sample', { name: '#primary', deferred: true })
```

```nodejs
await cluster
  .queryIndexes()
  .createIndex('travel-sample', 'idx_name_email', ['name', 'email'], {
    deferred: true,
  })
```

Click the  View button to see this code in context.

For more information, see [CreatePrimaryQueryIndexOptions](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/CreatePrimaryQueryIndexOptions.html) and [CreateQueryIndexOptions](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/CreateQueryIndexOptions.html).

To defer a primary or secondary index to be built later:

1. Use `CreatePrimaryQueryIndexOptions` or `CreateQueryIndexOptions` to specify the index options.
2. In the index options, set the `deferred` property to `True`.

---

The following examples create a set of primary and secondary indexes in the specified keyspace, with build deferred until later.

```python
cluster.query_indexes().create_primary_index(
    "travel-sample",
    CreatePrimaryQueryIndexOptions(deferred=True)
)
```

```python
cluster.query_indexes().create_index(
    "travel-sample",
    "idx_name_email",
    ["name", "email"],
    CreateQueryIndexOptions(deferred=True)
)
```

Click the  View button to see this code in context.

For more information, see [SQL++ Index Management](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#n1ql-index-management).

## [](#building-a-deferred-index)Building a Deferred Index

You can build one or more deferred primary or secondary indexes using a SQL++ statement. You can also build all deferred indexes in a keyspace using an SDK call.

> [!NOTE]
> The SDK calls only enable you to build indexes in the default collection and default scope within a bucket. A N1QL statement enables you to build indexes in _any_ collection and scope within a bucket.

* SQL++
* .NET
* Java
* Node.js
* Python

To build one or more deferred indexes, use the `BUILD INDEX` statement:

1. Use the `ON` keyword to specify the keyspace which contains the index or indexes.
2. Specify the index or indexes that you want to build in parentheses `()`.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query builds a single deferred index.

```sqlpp
BUILD INDEX ON landmark(idx_landmark_country) USING GSI;
```

The following query builds multiple deferred indexes.

```sqlpp
BUILD INDEX ON hotel(idx_landmark_name, idx_landmark_primary);
```

For more information and examples, see [BUILD INDEX](../n1ql/n1ql-language-reference/build-index.md).

To build all deferred indexes in a keyspace, use the task `BuildDeferredIndexesAsync` on the interface `IQueryIndexManager`.

---

The following example builds all deferred indexes in the specified keyspace.

```csharp
// Start building any deferred indexes which were previously created.
await cluster.QueryIndexes.BuildDeferredIndexesAsync("`travel-sample`");

// Wait for the deferred indexes to be ready for use.
await cluster.QueryIndexes.WatchIndexesAsync(
	"`travel-sample`",
	new[] { "idx_name_email" },
	options => options.WatchPrimary(true)
);
```

Click the  View button to see this code in context.

For more information, see [IQueryIndexManager()](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.IQueryIndexManager.html).

To build all deferred indexes in a keyspace, use the `buildDeferredIndexes` method.

---

The following example builds all deferred indexes in the specified keyspace.

```java
// Start building any deferred indexes which were previously created.
cluster.queryIndexes().buildDeferredIndexes("travel-sample");

WatchQueryIndexesOptions opts = WatchQueryIndexesOptions
    .watchQueryIndexesOptions()
    .watchPrimary(true);

// Wait for the deferred indexes to be ready for use.
// Set the maximum time to wait to 3 minutes.
cluster.queryIndexes().watchIndexes(
  "travel-sample", 
  Arrays.asList("idx_name_email"), 
  Duration.ofMinutes(3), 
  opts
);
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/QueryIndexManager.html).

To build all deferred indexes in a keyspace, use the `buildDeferredIndexes` function on a `QueryIndexManager` object.

---

The following example builds all deferred indexes in the specified keyspace.

```nodejs
// Start building any deferred indexes which were previously created.
await cluster.queryIndexes().buildDeferredIndexes('travel-sample')

// Wait for the deferred indexes to be ready for use.
// Set the maximum time to wait to 3 minutes.
await cluster.queryIndexes().watchIndexes(
  'travel-sample',
  ['idx_name_email'],
  180000, // milliseconds
  { watchPrimary: true }
)
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/QueryIndexManager.html).

To build all deferred indexes in a keyspace, use the `build_deferred_indexes` function on a `QueryIndexManager` object.

---

The following example builds all deferred indexes in the specified keyspace.

```python
# Start building any deferred indexes which were previously created.
cluster.query_indexes().build_deferred_indexes("travel-sample")

# Wait for the deferred indexes to be ready for use.
# Set the maximum time to wait to 3 minutes.
cluster.query_indexes().watch_indexes(
    "travel-sample",
    ["idx_name_email"],
    WatchQueryIndexOptions(timeout=timedelta(minutes=3), watch_primary=True)
)
```

Click the  View button to see this code in context.

For more information, see [SQL++ Index Management](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#n1ql-index-management).

## [](#related-links)Related Links

Reference and explanation:

* [Using Indexes](../learn/services-and-indexes/indexes/global-secondary-indexes.md)

Administrator guides:

* [Manage Indexes](../manage/manage-indexes/manage-indexes.md)
* [Monitor Indexes](../manage/monitor/monitoring-indexes.md)

Indexes with SDKs:

* [C](../../../c-sdk/current/concept-docs/n1ql-query.md#indexes)| [C++](../../../cxx-sdk/current/concept-docs/n1ql-query.md#indexes)| [.NET](../../../dotnet-sdk/current/concept-docs/n1ql-query.md#indexes)| [Go](../../../go-sdk/current/concept-docs/n1ql-query.md#indexes)| [Java](../../../java-sdk/current/concept-docs/n1ql-query.md#indexes)| Kotlin | [Node.js](../../../nodejs-sdk/current/concept-docs/n1ql-query.md#indexes)| [PHP](../../../php-sdk/current/concept-docs/n1ql-query.md#indexes)| [Python](../../../python-sdk/current/concept-docs/n1ql-query.md#indexes)| [Ruby](../../../ruby-sdk/current/concept-docs/n1ql-query.md#indexes)| [Scala](../../../scala-sdk/current/concept-docs/n1ql-query.md#indexes)