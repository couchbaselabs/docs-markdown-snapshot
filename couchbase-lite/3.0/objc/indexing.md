---
title: Indexes and Indexing
description: Couchbase mobile database indexing concepts
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/objc/pages/indexing.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:objc:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/objc/indexing.html)

# Indexes and Indexing

> Description — _Couchbase mobile database indexing concepts_  
> Related Content — [Databases](database.md) | [Documents](document.md) | [Indexing](indexing.md) |

## [](#introduction)Introduction

Before we begin querying documents, let’s briefly mention the importance of having an appropriate and balanced approach to indexes.

Creating indexes can speed up the performance of queries. A query will typically return results more quickly if it can take advantage of an existing database index to search, narrowing down the set of documents to be examined.

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

### [](#n1ql)N1QL

The code to create the index will look something like this:

Example 2\. Create index

```objc

CBLValueIndexConfiguration* config = [[CBLValueIndexConfiguration alloc]
                                      initWithExpression: @[@"type", @"name"]];

[self.database createIndexWithConfig: config name: @"TypeNameIndex" error: &error];
```

### [](#querybuilder)QueryBuilder

The code to create the index will look something like this:

Example 3\. Create index with QueryBuilder

```objc
CBLValueIndexItem *type = [CBLValueIndexItem property:@"type"];
CBLValueIndexItem *name = [CBLValueIndexItem property:@"name"];
CBLIndex *index = [CBLIndexBuilder valueIndexWithItems:@[type, name]];
[self.database createIndex:index withName:@"TypeNameIndex" error:&error];
```

## [](#summary)Summary

When planning the indexes you need for your database, remember that while indexes make queries faster, they may also:

* Make writes slightly slower, because each index must be updated whenever a document is updated
* Make your Couchbase Lite database slightly larger.

So too many indexes may hurt performance. Optimal performance depends on designing and creating the _right_ indexes to go along with your queries.

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