---
title: Indexes
description: These guides explain how to create and use primary and secondary
  indexes for SQL++ queries.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/indexes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:guides:indexes.adoc[]
---

[View original HTML](/server/7.2/guides/indexes.html)

# Indexes

These guides explain how to create and use primary and secondary indexes for SQL++ queries.  
This page is for Couchbase Server.

## Creating Indexes

You must create an index on a keyspace to be able to query that keyspace. The Index service enables you to create two types of index: primary indexes and secondary indexes.

* [Creating Indexes](create-index.md)

## Index Placement

To improve query responsiveness, you can choose where to save primary and secondary indexes. You can also partition a large secondary index across multiple nodes. In Couchbase Server Enterprise Edition, you can create replicas of primary indexes, secondary indexes, and secondary index partitions, to enhance index availability.

* [Index Placement](place-index.md)

## Deferring Indexes

When you create a primary or secondary index, you can mark it as deferred. This means the index is not built at once; you can build the deferred index later. This enables you to build multiple indexes more efficiently.

* [Deferring Indexes](defer-index.md)

## Selecting Indexes

Couchbase Server attempts to select an appropriate secondary index for a query, based on the filters in the WHERE clause. You can use an index hint to specify that a query should use a particular index.

* [Selecting Indexes](select-index.md)

## Dropping Indexes

You can drop primary and secondary indexes when you do not need them any more.

* [Dropping Indexes](drop-index.md)

## Related Links

Refer to the following guide for information on the Index Advisor, and other optimization features.

* [Optimizing Performance](optimize.md)