---
title: Use Primary and Secondary Indexes
description: These guides explain how to create and use primary and secondary
  indexes for SQL++ queries.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/indexes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:guides:indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/indexes.html)

# Use Primary and Secondary Indexes

These guides explain how to create and use primary and secondary indexes for SQL++ queries.

## Create Indexes

You do not need to create an index to query a keyspace. However, an index can help you to query a keyspace more efficiently. The Index service enables you to create two types of index: primary indexes and secondary indexes.

* [Creating Indexes](create-index.md)

## Place Indexes

To improve query responsiveness, you can choose where to save primary and secondary indexes. You can also partition a large secondary index across multiple nodes. You can create replicas of primary indexes, secondary indexes, and secondary index partitions, to enhance index availability.

* [Index Placement](place-index.md)

## Defer Indexes

When you create a primary or secondary index, you can mark it as deferred. This means the index is not built at once; you can build the deferred index later. This enables you to build multiple indexes more efficiently.

* [Deferring Indexes](defer-index.md)

## Select Indexes

Couchbase Capella attempts to select an appropriate secondary index for a query, based on the filters in the WHERE clause. You can use an index hint to specify that a query should use a particular index.

* [Selecting Indexes](select-index.md)

## Drop Indexes

You can drop primary and secondary indexes when you do not need them any more.

* [Dropping Indexes](drop-index.md)

## Get Index Advice

The Index Advisor can analyze your queries and provide recommended indexes to optimize response times.

* [Get Index Advice](index-advisor.md)