---
title: Copy Results to External Storage
description: In Capella Analytics, you can write query results or entire
  collections to an external file system or data store.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/copy-to-external.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:query:copy-to-external.adoc[]
---

[View original HTML](/analytics/query/copy-to-external.html)

# Copy Results to External Storage

> In Capella Analytics, you can write query results or entire collections to an external file system or data store. This feature supports exporting data to an external cloud data store in JSON format. 

## [](#use-cases)Use Cases

In Capella Analytics, you can write the results of a query to an external data store, or copy an entire collection to a data store. To provide access to the data store, you use an external link to supply the credentials for accessing the data store. See [Set Up an External Data Source](../sources/manage-external.md).

Example uses of this feature include:

* Query to join several collections or views, or to invoke built-in or user-defined functions, and then write the results to storage outside of Capella Analytics services. Subsequently, you could define an external collection in Capella Analytics to query that stored data.
* Move a specified collection from Capella Analytics to cloud storage. For example, copy the contents of a standalone collection or a remote Couchbase collection to a data store.
* Use a query to transform data stored in an external collection, then write the results back to that same store.

When you write a collection or query results to an external data store, you specify the destination path. You can optionally specify partitioning, ordering, and whether to apply compression.

Structuring the data on the external store is helpful in use cases where you plan to directly query the data there later, and to use [dynamic prefixes](../sources/dynamic-prefixes.md) to optimize those queries.

> [!NOTE]
> The target directory that you specify in the destination path must be empty. The operation fails if the target directory is not empty.

## [](#copy-to-statements)COPY TO Statements

For information about writing `COPY TO` statements, see [COPY TO External Data Store Statements](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fexternal.md).

## [](#see-also)See Also

* [Set Up an External Data Source](../sources/manage-external.md)
* [Write and Run Queries](editor.md)