---
title: Indexing your Data
description: Working with Couchbase Lite's data model  --  Using indexes
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/java/pages/indexing.adoc
  xref: xref:2.8@couchbase-lite:java:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/java/indexing.html)

# Indexing your Data

> Description — _Working with Couchbase Lite's data model — Using indexes_  
> Related Content — [Databases](../../current/java/database.md) | [Documents](../../current/java/document.md) | [Indexing](../../current/java/indexing.md) |

## [](#introduction)Introduction

Before we begin querying documents, let's briefly mention the importance of having an appropriate and balanced approach to indexes.

Creating indexes can speed up the performance of queries. A query will typically return results more quickly if it can take advantage of an existing database index to search, narrowing down the set of documents to be examined.

> [!NOTE]
> Constraints
> 
> Couchbase Lite for jvm does not currently support partial value indexes; indexes with non-property expressions. You should only index with properties that you plan to use in the query.

Example 1\. Creating a new index

This example creates a new index for the `type` and `name` properties, shown in this data model:

```json
{
    "_id": "hotel123",
    "type": "hotel", (1)
    "name": "Apple Droid"
}
```

The code to create the index will look something like this:

```Java
database.createIndex(
    "TypeNameIndex",
    IndexBuilder.valueIndex(
        ValueIndexItem.property("type"),
        ValueIndexItem.property("name")));
```

When planning the indexes you need for your database, remember that while indexes make queries faster, they may also:

* Make writes slightly slower, because each index must be updated whenever a document is updated
* Make your Couchbase Lite database slightly larger.

So too many indexes may hurt performance. Optimal performance depends on designing and creating the _right_ indexes to go along with your queries.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/java/gs-prereqs.md)
* [Install](../../current/java/gs-install.md)
* [Build and Run](../../current/java/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/java/database.md)
* [Documents](../../current/java/document.md)
* [Blobs](../../current/java/blob.md)
* [Remote Sync using Sync Gateway](../../current/java/replication.md)
* [Handling Data Conflicts](../../current/java/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)