---
title: Data Model
description: Couchbase's use of JSON as a storage format allows powerful search
  and query over documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.3/modules/concept-docs/pages/data-model.adoc
  xref: xref:4.3@python-sdk:concept-docs:data-model.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.3/concept-docs/data-model.html)

# Data Model

> Couchbase's use of JSON as a storage format allows powerful search and query over documents. Several data structures are supported by the SDK, including map, list, queue, and set. 

The power to search, query, and easily work with data in Couchbase, comes from the choice of JSON as a storage format. Non-JSON storage is supported — see the [Binary Storage Documentation](nonjson.md) — including UTF-8 strings, raw sequences of bytes, and language specific serializations, however, only JSON is supported by [Query](n1ql-query.md). In Couchbase, JSON's key-value structure allows the storage of collection data structures such as lists, maps, sets and queues — _see [below](#data-structures)_. JSON's tree-like structure allows operations against [specific paths in the Document](subdocument-operations.md), and efficient support for these data structures.

## [](#data-structures)Data Structures

Data structures in Couchbase are similar in concept to data structures in Python:

* **Map** is like Python `dict`, and is a key-value structure, where a value is accessed by using a key string.
* **List** is like a Python `list` and is a sequential data structure. Values can be placed in the beginning or end of a list, and can be accessed using numeric indexes.
* **Queue** is a wrapper over a _list_ which offers FIFO (first-in-first-out) semantics, allowing it to be used as a lightweight job queue.
* **Set** is a wrapper over a _list_ which provides the ability to handle unique values.

These data structures are stored as JSON documents in Couchbase, and can therefore be accessed using Query, Full Text Search, and normal key-value operations. Data structures can also be manipulated using the traditional sub-document and full-document key-value APIs.

Using the data structures API can help your application in two ways:

* **Simplicity**: Data structures provide high level operations by which you can deal with documents as if they were container data structures. Adding an item to a dictionary is expressed as `map_add`, rather than retrieving the entire document, modifying it locally, and then saving it back to the server.
* **Efficiency**: Data structure operations do not transfer the entire document across the network. Only the relevant data is exchanged between client and server, allowing for less network overhead and lower latency.