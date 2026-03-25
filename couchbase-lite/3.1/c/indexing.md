---
title: Indexing your Data
description: Couchbase Lite database data model concepts - indexes
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/c/pages/indexing.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@couchbase-lite:c:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/c/indexing.html)

# Indexing your Data

> Description — _Couchbase Lite database data model concepts - indexes_  
> Related Content — [Databases](database.md) | [Documents](document.md) | [Indexing](indexing.md) |

## [](#introduction)Introduction

Querying documents using a pre-existing database index is much faster because an index narrows down the set of documents to examine — see: the [Query Troubleshooting](query-troubleshooting.md) topic.

When planning the indexes you need for your database, remember that while indexes make queries faster, they may also:

* Make writes slightly slower, because each index must be updated whenever a document is updated
* Make your Couchbase Lite database slightly larger.

Too many indexes may hurt performance. Optimal performance depends on designing and creating the _right_ indexes to go along with your queries.

> [!NOTE]
> Constraints
> 
> Couchbase Lite for c does not currently support partial value indexes; indexes with non-property expressions. You should only index with properties that you plan to use in the query.

## [](#creating-a-new-index)Creating a new index

You can use SQL++ or QueryBuilder syntaxes to create an index

[Example 2](#ex-create-index) creates a new index for the `type` and `name` properties, shown in this data model:

Example 1\. Data Model

```json
{
    "_id": "hotel123",
    "type": "hotel",
    "name": "The Michigander",
    "overview": "Ideally situated for exploration of the Motor City and the wider state of Michigan. Tripadvisor rated the hotel ...",
    "state": "Michigan"
}
```

### [](#sql)SQL++

The code to create the index will look something like this:

Example 2\. Create index

```c
// For value types, this is optional but provides performance enhancements
// NOTE: No error handling, for brevity (see getting started)

// Syntax for second argument is the same as taking from a N1QL SELECT
// i.e. SELECT (type, name) FROM _;
CBLValueIndexConfiguration config = {
    kCBLN1QLLanguage,
    FLSTR("type, name")
};

CBLError err;
CBLCollection_CreateValueIndex(collection, FLSTR("TypeNameIndex"), config, &err);
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)