---
title: Indexes and Indexing
description: Couchbase mobile database indexing concepts
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/objc/pages/indexing.adoc
  xref: xref:3.1@couchbase-lite:objc:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/objc/indexing.html)

# Indexes and Indexing

> Description — _Couchbase mobile database indexing concepts_  
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
> Couchbase Lite for ios does not currently support partial value indexes; indexes with non-property expressions. You should only index with properties that you plan to use in the query.

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

```objc

CBLValueIndexConfiguration* config = [[CBLValueIndexConfiguration alloc]
                                      initWithExpression: @[@"type", @"name"]];

[collection createIndexWithName:@"TypeNameIndex" config:config error: &error];
```

### [](#querybuilder)QueryBuilder

> [!TIP]
> See the [QueryBuilder](querybuilder.md) topic to learn more about QueryBuilder.

The code to create the index will look something like this:

Example 3\. Create index with QueryBuilder

```objc
CBLValueIndexItem *type = [CBLValueIndexItem property:@"type"];
CBLValueIndexItem *name = [CBLValueIndexItem property:@"name"];
CBLIndex *index = [CBLIndexBuilder valueIndexWithItems:@[type, name]];
[collection createIndex:index name:@"TypeNameIndex" error:&error];
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