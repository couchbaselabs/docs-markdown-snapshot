---
title: Managing Enterprise Analytics Collections
description: This page describes how to manage collections with the Analytics Workbench.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/manage-collections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sources:manage-collections.adoc[]
---

[View original HTML](/enterprise-analytics/current/sources/manage-collections.html)

# Managing Enterprise Analytics Collections

This page guides you how to create, delete, and view metadata for collections in Enterprise Analytics, including best practices for managing column limits and data structure optimization.

## [](#whats-a-collection)What’s a Collection?

A collection is a data container within a scope that allows for the logical grouping of documents.

The Analytics Workbench enables you to create, edit, drop collections, and connect or disconnect local links and remote links.

## [](#creating-collections)Creating Collections

To stream data from a remote source like a Capella operational cluster, Couchbase Server, or a Kafka pipeline, create a remote link and an associated collection. To see your collections, go to **Analytics** **Workbench**. When you create a collection, you need to associate a specific database and scope.

* To create a remote link and associated collection, see [Stream Data from Remote Sources](manage-remote.md)
* To create an external link and associated collection, see [Set Up an External Data Source](manage-external.md).

## [](#deleting-a-collection)Deleting a Collection

To delete a collection:

1. Go to **Analytics** **Workbench** and find the collection you want to delete.
2. Go to **More Options (︙)** **Delete Collection**. The **Warning** dialog appears.
3. Confirm that you want to delete this collection and click **Delete**.

You can also delete a collection using the `DELETE` statement. For more information about deleting a collection, see [Delete Statements](../sqlpp/5%5Fdml%5Fdelete.md).

## [](#view-metadata-for-a-collection)View Metadata for a Collection

Each time you add a collection, Enterprise Analytics records its metadata in the `System.Metadata.Dataset` collection. To view metadata for a collection, you need to query this system collection. For more information, see [Querying Metadata](#5%5Fddl%5Fmetadata.adoc).

Enterprise Analytics supports both column and row storage formats.

> [!NOTE]
> The system uses the column format by default and it’s recommended not to exceed 4,000 unique columns across all documents in a collection.

When JSON documents are ingested, each unique leaf node is interpreted as a distinct column. See the following example:

```sqlpp
{
    "a": {
        "b": [1, 2],
        "c": "value",
        "d": [
            { "x": 1, "y": 2 },
            { "x": 3, "y": 4 }
        ]
    }
}
This document contributes 4 columns:
- a.b: [1, 2] → 1 column
- a.c: "value" → 1 column
- a.d: [{ "x": 1, "y": 2 }, { "x": 3, "y": 4 }] → 2 columns (a.d.x and a.d.y)
```

Additional documents or array elements with the same column structure do not count towards the 4,000-column limit.

Exceeding the recommended column limit may lead to degraded performance and high resource usage. To avoid this, design your schema and data model to minimize deeply nested or highly dynamic structures, and to prevent exceeding the column limit. Avoid naming fields in a way that causes each object to introduce new fields. For example, use a timestamp as the field name instead of storing it as a value.