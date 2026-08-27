---
title: Indexes and Indexing
description: Couchbase mobile database indexing concepts
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/indexing.adoc
  xref: xref:2.8@couchbase-lite:objc:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/indexing.html)

# Indexes and Indexing

> Description — _Couchbase mobile database indexing concepts_  

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

```objc
CBLValueIndexItem *type = [CBLValueIndexItem property:@"type"];
CBLValueIndexItem *name = [CBLValueIndexItem property:@"name"];
CBLIndex* index = [CBLIndexBuilder valueIndexWithItems:@[type, name]];
[database createIndex:index withName:@"TypeNameIndex" error:&error];
```

If there are multiple expressions, the first one will be the primary key, the second the secondary key, etc.

> [!NOTE]
> Every index has to be updated whenever a document is updated, so too many indexes can hurt performance. Thus, good performance depends on designing and creating the _right_ indexes to go along with your queries.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/objc/gs-prereqs.md)
* [Install](../../current/objc/gs-install.md)
* [Build and Run](../../current/objc/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/objc/database.md)
* [Documents](../../current/objc/document.md)
* [Blobs](../../current/objc/blob.md)
* [Remote Sync using Sync Gateway](../../current/objc/replication.md)
* [Handling Data Conflicts](../../current/objc/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)