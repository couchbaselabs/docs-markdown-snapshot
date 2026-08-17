---
title: Indexing
description: Couchbase mobile database indexes and indexing concepts
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/indexing.adoc
  xref: xref:2.8@couchbase-lite:swift:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/indexing.html)

# Indexing

> Couchbase mobile database indexes and indexing concepts 

## [](#overview)Overview

Creating indexes can speed up the performance of queries. While indexes make queries faster, they also make writes slightly slower, and the Couchbase Lite database file slightly larger. As such, it is best to only create indexes when you need to optimize a specific case for better query performance.

The following example creates a new index for the `type` and `name` properties.

```json
{
    "_id": "hotel123",
    "type": "hotel",
    "name": "Apple Droid"
}
```

```swift
let index = IndexBuilder.valueIndex(items:
    ValueIndexItem.expression(Expression.property("type")),
    ValueIndexItem.expression(Expression.property("name")))
try database.createIndex(index, withName: "TypeNameIndex")
```

If there are multiple expressions, the first one will be the primary key, the second the secondary key, etc.

> [!NOTE]
> Every index has to be updated whenever a document is updated, so too many indexes can hurt performance. Thus, good performance depends on designing and creating the _right_ indexes to go along with your queries.