---
title: Data Model
description: Couchbase's use of JSON as a storage format allows powerful search
  and query over documents.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/concept-docs/pages/data-model.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:1.6@scala-sdk:concept-docs:data-model.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/concept-docs/data-model.html)

# Data Model

> Couchbase's use of JSON as a storage format allows powerful search and query over documents. Several data structures are supported by the SDK, including map, list, queue, and set. 

The power to search, query, and easily work with data in Couchbase, comes from the choice of JSON as a storage format. Non-JSON storage is supported — see the [Binary Storage Documentation](nonjson.md) — including UTF-8 strings, raw sequences of bytes, and language specific serializations, however, only JSON is supported by [Query](n1ql-query.md). In Couchbase, JSON's key-value structure allows the storage of collection data structures such as lists, maps, sets and queues — _see [below](#data-structures)_. JSON's tree-like structure allows operations against [specific paths in the Document](subdocument-operations.md), and efficient support for these data structures.

## [](#data-structures)Data Structures

Data structures in Couchbase are similar in concept to data structures in C# (.NET):

* **Map** is like .NET `Dictionary<TKey, TValue>`, and is a key-value structure, where a value is accessed by using a key string.
* **List** is like a .NET `List<TValue>` and is a sequential data structure. Values can be placed in the beginning or end of a list, and can be accessed using numeric indexes.
* **Queue** is like a `IQueue` implementation which offers First In First Out (FIFO) semantics, allowing it to be used as a lightweight job queue.
* **Set** is a wrapper over a `List<TValue>` which provides the ability to handle unique values.

These data structures are stored as JSON documents in Couchbase, and can therefore be accessed both using the Query Service and normal key-value operations. Data structures can also be manipulated using the traditional sub-document and full-document KV APIs.

Using the data structures API may help your application in two ways:

* **Simplicity**: Data structures provide high level operations by which you can deal with documents as if they were container data structures. Adding an item to a dictionary is expressed as `MapAdd`, rather than retrieving the entire document, modifying it locally, and then saving it back to the server.
* **Efficiency**: Data structure operations don't transfer the entire document across the network. Only the relevant data is exchanged between client and server, allowing for less network overhead and shorter latency.

> [!NOTE]
> Besides the `IBucket` level data structure methods, there is a new namespace called `Couchbase.Collections` which contains implementations of some of the core interfaces in `System.Collection.Generics` such as `ISet<TValue>`, `IList<TValue>`, `IDictionary<Tkey, TValue>` and a `CouchbaseQueue` class. See section [The Couchbase.Collections Namespace](#couchbase-collections) below for more details.

## [](#creating-a-data-structure)Creating a Data Structure