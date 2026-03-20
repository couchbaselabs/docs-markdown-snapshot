---
title: Data Model
description: Couchbase's use of JSON as a storage format allows powerful search
  and query over documents.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.11/modules/concept-docs/pages/data-model.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:java-sdk:concept-docs:data-model.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/current/concept-docs/data-model.html)

# Data Model

> Couchbase’s use of JSON as a storage format allows powerful search and query over documents. Several data structures are supported by the SDK, including map, list, queue, and set. 

Data structures in Couchbase are similar in concept to data structures in the Java Collections Framework:

* **Map** is like Java `Map<String, Object>` and is a key-value structure, where a value is accessed by using a key string.
* **List** is like a Java `List<Object>` and is a sequential data structure. Values can be placed in the beginning or end of a list, and can be accessed using numeric indexes.
* **Queue** is a wrapper over a _list_ which offers FIFO (first-in-first-out) semantics, allowing it to be used as a lightweight job queue.
* **Set** is a wrapper over a _list_ which ensures each value in the list is unique.

In fact, the Java SDK provides implementations of the `Map`, `List`, `Set`, and `Queue` interfaces which are described in the [Collections Framework Integration](#jcf) section.

These data structures are stored as JSON documents in Couchbase, and can therefore be accessed using [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), Full Text Search, and normal key-value operations. Data structures can also be manipulated using the traditional sub-document and full-document KV APIs.

Using the data structures API may help your application in two ways:

* **Simplicity**: Data structures provide high level operations by which you can deal with documents as if they were container data structures. Adding an item to a dictionary is expressed as `mapAdd`, rather than retrieving the entire document, modifying it locally, and then saving it back to the server.
* **Efficiency**: Data structure operations do not transfer the entire document across the network. Only the relevant data is exchanged between client and server, allowing for less network overhead and lower latency.

## [](#jcf)Collections Framework Integration

In addition to the `Bucket` level methods for working with data structures, the Java SDK provides implementations of the `Map`, `List`, `Set`, and `Queue` interfaces from the Java Collections Framework. Instead of maintaining in-memory storage, these implementations are backed by JSON documents stored in Couchbase Server. The implementations are thread-safe and suitable for concurrent use. The `Map`, `List`, and `Queue` implementations may contain values of the following types:

* String
* Integer
* Long
* Double
* Boolean
* BigInteger
* BigDecimal
* JsonObject
* JsonArray

The `Set` implementation may contain values of all of the above types except `JsonObject` and `JsonArray`.

## [](#using-the-couchbasemap-object)Using the CouchbaseMap Object

If you need to feed a Couchbase document to an existing API that only works with `java.util.Map`, then CouchbaseMap may be a quick way to get started with tackling the task without delving into the [Sub-Document API](subdocument-operations.md). You can create a CouchbaseMap like this:

```java
Map<String, String> myMap = collection.map("name", String.class);
```

### [](#limitations)Limitations

The Map interface requires the "put" and "remove" methods to return the previous value associated with the key. To implement this behavior, CouchbaseMap needs to make at least 2 subdocument requests: one request to get the current value, and a second request to update it. If the document changes between these two requests, the code retries up to the `casMismatchRetries` limit, after which it gives up and throws an exception. If the return values of `put` and `remove` are never actually used, you could end up making a lot of unnecessary requests. There’s also the potential for exceptions if concurrent map updates are extremely frequent.

> [!TIP]
> For many use cases, the [Sub-Document API](../howtos/subdocument-operations.md) will be a useful and possibly better altermative to `CouchbaseMap`.