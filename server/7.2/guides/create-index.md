---
title: Creating Indexes
description: How to create primary indexes and secondary indexes.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/create-index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:guides:create-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/guides/create-index.html)

# Creating Indexes

> How to create primary indexes and secondary indexes.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

You must create an index on a keyspace to be able to query that keyspace. The Index service enables you to create two types of index: primary indexes and secondary indexes.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#creating-a-primary-index)Creating a Primary Index

A primary index is an index of document keys. Primary indexes are optional, and are only required for running ad-hoc queries that are not supported by a secondary index.

You can create a primary index using a SQL++ statement or an SDK call.

* SQL++
* .NET
* Java
* Node.js
* Python

To create a primary index, use the `CREATE PRIMARY INDEX` command.

1. If required, specify a name for the primary index. If you do not specify a name, the index is called `#primary`.
2. Use the `ON` keyword to specify the keyspace on which to create the index.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query creates an unnamed primary index on the `airline` keyspace.

```sqlpp
CREATE PRIMARY INDEX ON airline;
```

The following query creates a primary index named `travel_primary` on the `airline` keyspace.

```sqlpp
CREATE PRIMARY INDEX travel_primary ON airline;
```

For more information and examples, see [CREATE PRIMARY INDEX](../n1ql/n1ql-language-reference/createprimaryindex.md).

To create a primary index, use the task `CreatePrimaryIndexAsync()` on the interface `IQueryIndexManager`.

1. Specify the keyspace on which to create the index.
2. If you want to specify a name for the index:

  1. Use `CreatePrimaryQueryIndexOptions` to specify the index options.
  2. In the index options, use the `IndexName` method to specify the index name.  
If you do not specify a name, the index is called `#primary`.

---

The following example creates an unnamed primary index.

```csharp
await cluster.QueryIndexes.CreatePrimaryIndexAsync(
	"`travel-sample`",
	options => options.IgnoreIfExists(true)
);
```

The following example creates a named primary index on the specified keyspace.

```csharp
await cluster.QueryIndexes.CreatePrimaryIndexAsync(
	"`travel-sample`",
	options => options.IndexName("named_primary_index")
);
```

Click the  View button to see this code in context.

For more information, see [IQueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.IQueryIndexManager.html).

To create a primary index, use the `createPrimaryIndex` method.

1. Specify the keyspace on which to create the index.
2. If you want to specify a name for the index:

  1. Use `CreatePrimaryQueryIndexOptions` to specify the index options.
  2. In the index options, use the `IndexName` method to specify the index name.  
If you do not specify a name, the index is called `#primary`.

---

The following example creates an unnamed primary index.

```java
CreatePrimaryQueryIndexOptions opts = CreatePrimaryQueryIndexOptions
    .createPrimaryQueryIndexOptions()
    .ignoreIfExists(true);

cluster.queryIndexes().createPrimaryIndex("travel-sample", opts);
```

The following example creates a named primary index on the specified keyspace.

```java
CreatePrimaryQueryIndexOptions opts = CreatePrimaryQueryIndexOptions
    .createPrimaryQueryIndexOptions()
    .indexName("named_primary_index");

cluster.queryIndexes().createPrimaryIndex("travel-sample", opts);
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/QueryIndexManager.html).

To create a primary index, use the `createPrimaryIndex` function on a `QueryIndexManager` object.

1. Specify the keyspace on which to create the index.
2. If you want to specify a name for the index:

  1. Use `CreatePrimaryQueryIndexOptions` to specify the index options.
  2. In the index options, use the `name` property to specify the index name.  
If you do not specify a name, the index is called `#primary`.

---

The following example creates an unnamed primary index.

```nodejs
await cluster.queryIndexes().createPrimaryIndex(
  'travel-sample',
  // Don't error if the primary index already exists.
  { ignoreIfExists: true }
)
```

The following example creates a named primary index on the specified keyspace.

```nodejs
await cluster
  .queryIndexes()
  .createPrimaryIndex('travel-sample', { name: 'named_primary_index' })
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/QueryIndexManager.html).

To create a primary index, use the `create_primary_index` function on a `QueryIndexManager` object.

1. Specify the keyspace on which to create the index.
2. If you want to specify a name for the index:

  1. Use `CreatePrimaryQueryIndexOptions` to specify the index options.
  2. In the index options, use the `index_name` property to specify the index name.  
If you do not specify a name, the index is called `#primary`.

---

The following example creates an unnamed primary index.

```python
cluster.query_indexes().create_primary_index(
    "travel-sample",
    # Don't error if the primary index already exists.
    CreatePrimaryQueryIndexOptions(ignore_if_exists=True)
)
```

The following example creates a named primary index on the specified keyspace.

```python
cluster.query_indexes().create_primary_index(
    "travel-sample",
    CreatePrimaryQueryIndexOptions(index_name="named_primary_index")
)
```

Click the  View button to see this code in context.

For more information, see [SQL++ Index Management](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#n1ql-index-management).

## [](#creating-a-secondary-index)Creating a Secondary Index

A secondary index is actually the main type of index that queries use. For this reason, they are also known as Global Secondary Indexes or GSIs. You can create a secondary index on any fields or expressions necessary to support your queries.

You can create a secondary index using a SQL++ statement or an SDK call.

* SQL++
* .NET
* Java
* Node.js
* Python

To create a secondary index, use the `CREATE INDEX` statement.

1. Specify a name for the index.
2. Use the `ON` keyword to specify the keyspace on which to create the index.
3. Specify the index key (the expression or expressions to index) in parentheses `()`.

---

Context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query creates a secondary index on the `name` field in the `airline` keyspace.

```sqlpp
CREATE INDEX `idx-name` ON airline(name);
```

The following query creates a secondary index on an expression using the `name` field in the `airline` keyspace.

```sqlpp
CREATE INDEX travel_cxname ON airport(LOWER(name));
```

For more information and examples, see [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md).

To create a secondary index, use the task `CreateIndexAsync()` on the interface `IQueryIndexManager`.

1. Specify the keyspace on which to create the index.
2. Specify a name for the index.
3. Specify the field to index.

---

The following example creates a secondary index on the `name` field in the specified keyspace.

```csharp
await cluster.QueryIndexes.CreateIndexAsync(
	"`travel-sample`",
	"index_name",
	new[] { "name" }
);
```

Click the  View button to see this code in context.

For more information, see [IQueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.IQueryIndexManager.html).

To create a secondary index, use the `createIndex` method.

1. Specify the keyspace on which to create the index.
2. Specify a name for the index.
3. Specify the field to index.

---

The following example creates a secondary index on the `name` field in the specified keyspace.

```java
cluster.queryIndexes().createIndex(
  "travel-sample", 
  "index_name",
  Arrays.asList("name")
);
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/QueryIndexManager.html).

To create a secondary index, use the `createIndex` function on a `QueryIndexManager` object.

1. Specify the keyspace on which to create the index.
2. Specify a name for the index.
3. Specify the field to index.

---

The following example creates a secondary index on the `name` field in the specified keyspace.

```nodejs
await cluster
  .queryIndexes()
  .createIndex('travel-sample', 'index_name', ['name'])
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/QueryIndexManager.html).

To create a secondary index, use the `create_index` function on a `QueryIndexManager` object.

1. Specify the keyspace on which to create the index.
2. Specify a name for the index.
3. Specify the field to index.

---

The following example creates a secondary index on the `name` field in the specified keyspace.

```python
cluster.query_indexes().create_index("travel-sample", "index_name", ["name"])
```

Click the  View button to see this code in context.

For more information, see [SQL++ Index Management](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#n1ql-index-management).

### [](#creating-a-composite-index)Creating a Composite Index

A composite index is a secondary index which contains multiple index keys.

You can create a composite index using a SQL++ statement or an SDK call.

* SQL++
* .NET
* Java
* Node.js
* Python

To create a composite index, specify multiple index keys in the index definition, separated by commas.

---

The following example creates a secondary index on the `name`, `id`, `icao`, and `iata` fields in the `airline` keyspace.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX travel_info ON airline(name, id, icao, iata);
```

For more information and examples, see [CREATE INDEX](../n1ql/n1ql-language-reference/createindex.md).

To create a composite index, specify multiple fields in the index definition.

---

The following example creates a secondary index on the `name`, `id`, `icao`, and `iata` fields in the specified keyspace.

```csharp
await cluster.QueryIndexes.CreateIndexAsync(
	"`travel-sample`",
	"index_travel_info",
	new[] { "name", "id", "icao", "iata" }
);
```

Click the  View button to see this code in context.

For more information, see [IQueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.IQueryIndexManager.html).

To create a composite index, specify multiple fields in the index definition.

---

The following example creates a secondary index on the `name`, `id`, `icao`, and `iata` fields in the specified keyspace.

```java
cluster.queryIndexes().createIndex(
  "travel-sample", 
  "index_travel_info", 
  Arrays.asList("name", "id", "icao", "iata")
);
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/QueryIndexManager.html).

To create a composite index, specify multiple fields in the index definition.

---

The following example creates a secondary index on the `name`, `id`, `icao`, and `iata` fields in the specified keyspace.

```nodejs
await cluster
  .queryIndexes()
  .createIndex('travel-sample', 'index_travel_info', [
    'name',
    'id',
    'icao',
    'iata',
  ])
```

Click the  View button to see this code in context.

For more information, see [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/QueryIndexManager.html).

To create a composite index, specify multiple fields in the index definition.

---

The following example creates a secondary index on the `name`, `id`, `icao`, and `iata` fields in the specified keyspace.

```python
cluster.query_indexes().create_index(
    "travel-sample",
    "index_travel_info",
    ["name", "id", "icao", "iata"]
)
```

Click the  View button to see this code in context.

For more information, see [SQL++ Index Management](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#n1ql-index-management).

### [](#creating-an-index-on-metadata)Creating an Index on Metadata

You can also create a secondary index using document metadata.

To index metadata information, use the [META()](../n1ql/n1ql-language-reference/metafun.md#meta) function in the index key.

The following example creates a secondary index on the document key.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX idx_hotel_id ON hotel (META().id);
```

For more information and examples, see [Indexing Metadata Information](../n1ql/n1ql-language-reference/indexing-meta-info.md).

### [](#creating-an-index-on-an-array)Creating an Index on an Array

You can use an array index to optimize queries on fields which are nested within array elements.

To create an array index, specify the index key as follows:

1. Use the `ALL` keyword to index all values in the specified fields, or `DISTINCT` to index only distinct values.
2. Use a field name to index the entire array, or use an [ARRAY](../n1ql/n1ql-language-reference/collectionops.md#array) operator to index nested fields within the array.

The following example creates an index on distinct values of the `day` field within the `schedule` field.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX travel_sched ON route
(DISTINCT ARRAY v.day FOR v IN schedule END);
```

For more information and examples, see [Array Indexing](../n1ql/n1ql-language-reference/indexing-arrays.md).

### [](#creating-a-partial-index)Creating a Partial Index

A partial index is an index on a subset of documents within a keyspace — for example, just the documents which have a specific schema.

To create an index on a subset of documents, use the WHERE clause to specify the distinguishing fields for that subset.

The following example creates an index on documents in which the value of the `activity` field is `eat`.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
CREATE INDEX travel_eat ON landmark(name, id, address)
WHERE activity='eat';
```

For more information and examples, see [Partial Index](#n1ql:n1ql-language-reference/indexing-and-query-perf.adoc#partial-index).

### [](#creating-a-covering-index)Creating a Covering Index

A covering index is an index which contains all the fields in the query projection, not just the fields that are required for joins or filtering. A covering index is therefore usually a composite index. If a query uses a covering index, the query can get all the data it needs from the index, and the Query Service does not have to make a fetch request to the Data service.

To create a covering index, make sure the index includes all the fields and expressions required by the query.

For more information and examples, see [Covering Indexes](../n1ql/n1ql-language-reference/covering-indexes.md).

## [](#related-links)Related Links

Reference and explanation:

* [Using Indexes](../learn/services-and-indexes/indexes/global-secondary-indexes.md)

Administrator guides:

* [Manage Indexes](../manage/manage-indexes/manage-indexes.md)
* [Monitor Indexes](../manage/monitor/monitoring-indexes.md)

Indexes with SDKs:

* [C](../../../c-sdk/current/concept-docs/n1ql-query.md#indexes)| [C++](../../../cxx-sdk/current/concept-docs/n1ql-query.md#indexes)| [.NET](../../../dotnet-sdk/current/concept-docs/n1ql-query.md#indexes)| [Go](../../../go-sdk/current/concept-docs/n1ql-query.md#indexes)| [Java](../../../java-sdk/current/concept-docs/n1ql-query.md#indexes)| Kotlin | [Node.js](../../../nodejs-sdk/current/concept-docs/n1ql-query.md#indexes)| [PHP](../../../php-sdk/current/concept-docs/n1ql-query.md#indexes)| [Python](../../../python-sdk/current/concept-docs/n1ql-query.md#indexes)| [Ruby](../../../ruby-sdk/current/concept-docs/n1ql-query.md#indexes)| [Scala](../../../scala-sdk/current/concept-docs/n1ql-query.md#indexes)