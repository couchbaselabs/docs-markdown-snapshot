---
title: Managed MCP Server Tools Reference
description: The Couchbase AI Data Plane Managed MCP Server exposes specific
  tools that you can use with your agents to interact with an operational
  cluster.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase MCP Server
    version: managed
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/cloud/modules/learn/pages/tools.adoc
  xref: xref:managed@mcp-server:learn:tools.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/managed/learn/tools.html)

# Managed MCP Server Tools Reference

> The Couchbase AI Data Plane Managed MCP Server exposes specific tools that you can use with your agents to interact with an operational cluster. 

Managed MCP Servers can expose tools across the following categories to an LLM through the MCP protocol:

* [Cluster Setup and Health](#cluster-setup)
* [Data Model and Schema Discovery](#data-model)
* [Document KV Operations](#document-kv)
* [Query and Indexing](#query-index)
* [Query Performance Analysis](#query-performance)

## [](#cluster-setup)Cluster Setup and Health

Use cluster setup and health tools to check the status of your Managed MCP Server or its linked operational cluster.

| Tool                                | Required API Key Access | Description                                                                                 |
| ----------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------- |
| get\_server\_configuration\_status  | Read                    | Check the configuration status of your Managed MCP Server.                                  |
| test\_cluster\_connection           | Read                    | Check your connection to the operational cluster you linked to your Managed MCP Server.     |
| get\_cluster\_health\_and\_services | Read                    | Get information about the health and available Services on your linked operational cluster. |

## [](#data-model)Data Model and Schema Discovery

Use data model and schema discovery tools to explore and modify [buckets, scopes, and collections](../../../cloud/clusters/data-service/about-buckets-scopes-collections.md) in your linked operational cluster. You can also get the schema for documents in a collection.

If you want to get or modify specific documents, use [Document KV Operations](#document-kv) tools, instead. If you want to run a query, use [Query and Indexing](#query-index) tools.

| Tool                                      | Required API Key Access | Description                                                                                                                                      |
| ----------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| get\_buckets\_in\_cluster                 | Read                    | Get a list of all [buckets](../../../cloud/clusters/data-service/about-buckets-scopes-collections.md#buckets) on the linked operational cluster. |
| get\_scopes\_in\_bucket                   | Read                    | Get a list of all the [scopes](../../../cloud/clusters/data-service/about-buckets-scopes-collections.md#scopes) in a specified bucket.           |
| get\_collections\_in\_scope               | Read                    | Get a list of all the [collections](../../../cloud/clusters/data-service/about-buckets-scopes-collections.md#collections) in a specified scope.  |
| get\_scopes\_and\_collections\_in\_bucket | Read                    | Get a list of all the scopes and collections in a specified bucket.                                                                              |
| get\_schema\_for\_collection              | Read                    | Get an inferred document structure for all the documents in a collection.                                                                        |
| create\_scope                             | Read and Write          | Create a new scope in a specified bucket.                                                                                                        |
| create\_collection                        | Read and Write          | Create a new collection in a specified scope.                                                                                                    |
| delete\_scope                             | Read and Write          | Delete the specified scope.                                                                                                                      |
| delete\_collection                        | Read and Write          | Delete the specified collection.                                                                                                                 |

## [](#document-kv)Document KV Operations

Use document KV operations tools to get and modify specific documents and subdocuments inside your linked operational cluster.

If you want to run a query, use [Query and Indexing](#query-index) tools.

| Tool                      | Required API Key Access | Description                                                                                                                                                                 |
| ------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| get\_document\_by\_id     | Read                    | Get a document with a specified ID value from a scope and collection.                                                                                                       |
| upsert\_document\_by\_id  | Read and Write          | Insert a new document or update an existing document with the specified ID value in a scope and collection.                                                                 |
| insert\_document\_by\_id  | Read and Write          | Insert a new document into a scope and collection with a specified ID value. This operation fails if a document already exists with the specified ID value.                 |
| replace\_document\_by\_id | Read and Write          | Replace an existing document that has the specified ID value. This operation fails if there is no document with the specified ID value.                                     |
| delete\_document\_by\_id  | Read and Write          | Delete the document with the specified ID value.                                                                                                                            |
| lookup\_subdocument       | Read                    | Get parts of a document, such as specific fields, or run existence or array and object counts, without fetching the whole document.                                         |
| mutate\_subdocument       | Read and Write          | Edit parts of a document, such as specific fields, without rewriting the entire document. You can upsert, insert, replace, remove, run array operations or modify counters. |

## [](#query-index)Query and Indexing

Use query and indexing tools with your linked operational cluster and Managed MCP Server to:

* Run SQL++ queries using the [Query Service](../../../cloud/n1ql/query.md)
* Create and manage indexes using the [Index Service](../../../cloud/guides/indexes.md)

| Tool                                 | Required API Key Access | Description                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| run\_sql\_plus\_plus\_query          | Read and Write          | Run a SQL++ query using the [Query Service](../../../cloud/n1ql/query.md) on the linked operational cluster.                                                                                                                                                                                                                         |
| explain\_sql\_plus\_plus\_query      | Read and Write          | Get information about the execution plan for a SQL++ statement. The explain\_sql\_plus\_plus\_query tool includes operators such as scans, joins, and filters. It helps you tune query performance by showing index usage, cost estimates, and data access paths.                                                                    |
| list\_indexes                        | Read                    | Get a list of all indexes in the linked operational cluster, along with their definitions. You can filter indexes by bucket, scope, collection, or index name.                                                                                                                                                                       |
| get\_index\_advisor\_recommendations | Read and Write          | Get recommendations on the most optimal indexes from the Couchbase Index Advisor for a specific SQL++ query.                                                                                                                                                                                                                         |
| create\_index                        | Read and Write          | Create a [non-vector GSI index](../../../cloud/guides/create-index.md#creating-a-secondary-index) for a specified collection. By default, the created index is a [deferred index](../../../cloud/guides/defer-index.md). You cannot use this tool for [vector indexes](../../../cloud/vector-index/vectors-and-indexes-overview.md). |
| build\_index                         | Read and Write          | Start building all [deferred indexes](../../../cloud/guides/defer-index.md) on a collection.                                                                                                                                                                                                                                         |
| drop\_index                          | Read and Write          | Drop a specified [GSI index](../../../cloud/guides/create-index.md#creating-a-secondary-index) or [vector index](../../../cloud/vector-index/vectors-and-indexes-overview.md) from a collection.                                                                                                                                     |

## [](#query-performance)Query Performance Analysis

Use query performance analysis tools to identify slow queries, missing indexes, and other optimization opportunities on your linked operational cluster.

| Tool                                         | Required API Key Access | Description                                                                                                                                                                                                        |
| -------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| get\_longest\_running\_queries               | Read                    | Get the longest running queries on your linked operational cluster, based on average service time.                                                                                                                 |
| get\_most\_frequent\_queries                 | Read                    | Get the most frequently executed queries on your linked operational cluster.                                                                                                                                       |
| get\_queries\_not\_selective                 | Read                    | Get any queries from your linked operational cluster that are not selective. The index scans for these queries return many more documents than the final result set.                                               |
| get\_queries\_not\_using\_covering\_index    | Read                    | Get any queries from your linked operational cluster that do not use a [covering index](../../../cloud/indexes/covering-indexes.md).                                                                               |
| get\_queries\_using\_primary\_index          | Read                    | Get any queries from your linked operational cluster that use only a [primary index](../../../cloud/indexes/indexing-and-query-perf.md#primary-index). This can indicate a performance concern with these queries. |
| get\_queries\_with\_largest\_response\_sizes | Read                    | Get the queries from your linked operational cluster that have the largest response sizes.                                                                                                                         |
| get\_queries\_with\_large\_result\_count     | Read                    | Get the queries from your linked operational cluster that have the largest result counts.                                                                                                                          |

## [](#see-also)See Also

* [Connect Data to Agents with Managed MCP Server](../about-managed-mcp.md)
* [Deploy and Connect to Your Managed MCP Server](../deploy-connect-mcp.md)