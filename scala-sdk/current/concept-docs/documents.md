---
title: Documents
description: Couchbase supports CRUD operations, various data structures, and
  binary documents.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/concept-docs/pages/documents.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/scala-sdk/current/concept-docs/documents.html)

# Documents

> Couchbase supports CRUD operations, various data structures, and binary documents. 

Although query and path-based (Sub-Document) services are available, the simplicity of the document-based kv interface is the fastest way to perform operations involving single documents.

## [](#document)Document

A _document_ refers to an entry in the database (other databases may refer to the same concept as a [_row_](../../../server/current/learn/data/document-data-model.md#couchbase-server-and-json-the-benefits)). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data.

**Document IDs** (keys) are assigned by application. A valid document ID must:

* Conform to UTF-8 encoding
* Be no longer than 246 bytes  
> [!NOTE]  
> There is a difference between bytes and characters: most non-Latin characters occupy more than a single byte.

You are free to choose any ID (key) for your document, so long as it conforms to the above restrictions. Unlike some other databases, Couchbase does not automatically generate IDs for you, though you may use a separate [counter](#counters) to increment a serial number — you can also use UUIDs as keys, the best choice being determined by your use case.

The **document value** contains the actual application data; for example, a _product_ document may contain information about the price and description. Documents are usually ([but not always](nonjson.md)) stored as JSON on the server. Because JSON is a structured format, it can be subsequently searched and queried.

```json
{
    "type": "product",
    "sku": "CBSRV45DP",
    "msrp": [5.49, "USD"],
    "ctime": "092011",
    "mfg": "couchbase",
    "tags": ["server", "database", "couchbase", "nosql", "fast", "json", "awesome"]
}
```

## [](#primitive-key-value-operations)Primitive Key-Value Operations

```python
upsert(docid, document)
insert(docid, document)
replace(docid, document)
get(docid)
remove(docid)
```

In Couchbase documents are stored using one of the operations: `upsert`, `insert`, and `replace`. Each of these operations will write a JSON document with a given document ID (key) to the cluster. The update methods differ in behavior in respect to the existing state of the document:

* `insert` will only create the document if the given ID is not found within the cluster.
* `replace` will only replace the document if the given ID already exists within the cluster.
* `upsert` will always replace the document, ignoring whether the ID already exists or not.

Documents can be retrieved using the `get` operation, and finally removed using the `remove` operations.

Since Couchbase’s KV store may be thought of as a distributed hashmap or dictionary, the following code samples are explanatory of Couchbase’ update operations in pseudo-code:

```cpp
map<string,object> KV_STORE;

void insert(string doc_id, object value) {
    if (!KV_STORE.contains(doc_id)) {
        KV_STORE.put(doc_id, value);
    } else {
        throw DocumentAlreadyExists();
    }
}

void replace(string doc_id, object value) {
    if (KV_STORE.contains(doc_id)) {
        KV_STORE.put(doc_id, value);
    } else {
        throw DocumentNotFound();
    }
}

void upsert(string doc_id, object value) {
    KV_STORE.put(doc_id, value);
}

object get(string doc_id) {
    if (KV_STORE.contains(doc_id)) {
        return KV_STORE.get(doc_id);
    } else {
        throw DocumentNotFound();
    }
}
```

You can also use [SQL++ Queries](n1ql-query.md) (formerly N1QL) and [Full Text Search](full-text-search-overview.md) to access documents by means other than their IDs, however these query operations Couchbase eventually translate into primitive key-value operations, and exist as separate services outside the data store.

## [](#storing-and-updating-documents)Storing and Updating Documents

Documents can be stored and updated using either the SDK, Command line, or Web UI. When using a storage operation, the _full content_ of the document is replaced with a new value.

The following example shows a document being stored using the [cbc](#webui-cli-access.adoc#cli-access) utility. The ID of the document is `docid` and its value is JSON containing a single field (`json`) with the value of `value`.

```console
# When storing JSON data using cbc, ensure it is properly quoted for your shell:
$ cbc create -u Administrator -P password docid -V '{"json":"value"}' -M upsert -U couchbase://cluster-node/bucket-name
docid               Stored. CAS=0x8234c3c0f213
```

You can also specify additional options when storing a document in Couchbase

* [Expiry](#expiry) (or `TTL`) value which will instruct the server to delete the document after a given amount of time. This option is useful for transient data (such as sessions). By default documents do not expire. See [Expiry](#expiry) for more information on expiration.
* CAS value to protect against concurrent updates to the same document.
* [Durability Requirements](durability-replication-failure-considerations.md)

> [!NOTE]
> If you wish to only modify certain parts of a document, you can use [Sub-Document](subdocument-operations.md) operations which operate on specific subsets of documents:
> 
> ```scala
> val result: Try[MutateInResult] = collection.mutateIn("customer123", Array(
>   upsert("email", "dougr96@hotmail.com")
> ))
> 
> result match {
>   case Success(_)   => println("Success!")
>   case Failure(err) => println(s"Error: ${err}")
> }
> ```
> 
> or [N1QL UPDATE](../../../server/current/n1ql/n1ql-language-reference/update.md) to update documents based on specific query criteria:
> 
> ```n1ql
> update `default` SET sale_price = msrp * 0.75 WHERE msrp < 19.95;
> ```

## [](#retrieving-documents)Retrieving Documents

This section discusses retrieving documents using their IDs, or primary keys. Documents can also be accessed using secondary lookups via [SQL++ queries](n1ql-query.md) and [MapReduce Views](querying-your-data.md). Primary key lookups are performed using the key-value API, which simplifies use and increases performance (as applications may interact with the KV store directly, rather than a secondary index or query processor).

In Couchbase, documents are stored with their IDs. Retrieving a document via its ID is the simplest and quickest operation in Couchbase.

>>> result = cb.get('docid')
>>> print result.value
{'json': 'value'}

```console
$ cbc cat docid
docid                CAS=0x8234c3c0f213, Flags=0x0. Size=16
{"json":"value"}
```

Once a document is retrieved, it is accessible in the native format by which it was stored; meaning that if you stored the document as a list, it is now available as a list again. The SDK will automatically deserialize the document from its stored format (usually JSON) to a native language type. It is possible to store and retrieve non-JSON documents as well, using a [transcoder](nonjson.md).

You can also modify a document’s expiration time while retrieving it; this is known as _get-and-touch_ and allows you to keep temporary data alive while retrieving it in one atomic and efficient operation.

Documents can also be retrieved with SQL++. While SQL++ is generally used for secondary queries, it can also be used to retrieve documents by their primary keys (ID) (though it is recommended to use the key-value API if the ID is known). Lookups may be done either by comparing the `META(from-term).id` or by using the `USE KEYS` \[...\] keyword:

```n1ql
SELECT * FROM default USE KEYS ["docid"];
```

or

```n1ql
SELECT * FROM default WHERE META(default).id = "docid";
```

You can also retrieve _parts_ of documents using [Sub-Document operations](subdocument-operations.md), by specifying one or more sections of the document to be retrieved

```scala
val result: Try[(String, Boolean)] = for {
  result   <- collection.lookupIn("customer123", Array(
    get("addresses.delivery.country"),
    exists("addresses.delivery.does_not_exist")))
  country  <- result.contentAs[String](0)
  exists   <- result.contentAs[Boolean](1)
} yield (country, exists)

result match {
  case Success((country, exists)) =>
    println(s"Country = ${country}, Exists = ${exists}}")
  case Failure(err)               =>
    println(s"Error: ${err}")
}
```

## [](#counters)Counters

You can atomically increment or decrement the numerical value of special counter document — examples can be found in the [practical K-V Howto document](../howtos/kv-operations.md#atomic-counters).

> [!CAUTION]
> Do not increment or decrement counters if using XDCR. Within a single cluster the `incr()` is atomic, as is `decr()`; across XDCR however, if two clients connecting to two different (bidirectional) clusters issue `incr` concurrently, this may (and most likely will) result in the value only getting incremented once in total. The same is the case for `decr()`.

A document may be used as a counter if its value is a simple ASCII number, like `42`. Couchbase allows you to increment and decrement these values atomically using a special `counter` operation in the `Binary.Collection`. The example below shows a counter being initialised, then being incremented and decremented:

```java
//  java example:
String counterDocId = "counter-doc";
// Increment by 1, creating doc if needed
collection.binary().increment(counterDocId);
// Decrement by 1
collection.binary().decrement(counterDocId);
// Decrement by 5
collection.binary().decrement(counterDocId,
DecrementOptions.decrementOptions().delta(5));
```

In the above example, a counter is created by using the `counter` method with an `initial` value. The initial value is the value the counter uses if the counter ID does not yet exist.

Once created, the counter can be incremented or decremented atomically by a given _amount_ or _delta_. Specifying a positive delta increments the value and specifying a negative one decrements it. When a counter operation is complete, the application receives the current value of the counter, after the increment.

Couchbase counters are 64-bit unsigned integers in Couchbase and do not wrap around if decremented beyond 0\. However, counters will wrap around if incremented past their maximum value (which is the maximum value contained within a 64-bit integer). Many SDKs will limit the _delta_ argument to the value of a _signed_ 64-bit integer.

[Expiration](#expiry) times can also be specified when using counter operations.

[CAS](../howtos/concurrent-document-mutations.md) values are not used with counter operations since counter operations are atomic. The intent of the counter operation is to simply increment the current server-side value of the document. If you wish to only increment the document if it is at a certain value, then you may use a normal `replace` function with CAS:

```python
# Python example:
rv = cb.get('counter_id')
value, cas = rv.value, rv.cas
if should_increment_value(value):
  cb.upsert('counter_id', value + increment_amount, cas=cas)
```

You can also use [sub-document counter operations](subdocument-operations.md) to increment numeric values _within_ a document containing other content. An example can be found in the [practical sub-doc page](../howtos/subdocument-operations.md#counters-and-numeric-fields).

### [](#use-cases)Use Cases

The SDK provides a high-level abstraction over the simple `incr()`/`decr()` of Couchbase Server’s memcached binary protocol, using `collections.binary()`. This enables you to work with counters using `get()` and `upsert()` operations — allowing, _inter alia_, the use of durability options with the operations. You will find several ways of working with counters [in the API docs](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/AsyncBinaryCollection.html).

## [](#expiry)Expiration Overview

Most data in a cluster is there to be persisted and long-lived. However, the need for transient or temporary data does arise in applications, such as in the case of user sessions, caches, or temporary documents representing a given process ownership. You can use expiration values on documents to handle transient data.

In databases without a built-in expiration feature, dealing with transient data may be cumbersome. To provide "expiration" semantics, applications are forced to record a time stamp in a record, and then upon each access of the record check the time stamp and, if invalid, delete it.

Since some logically ‘expired’ documents might never be accessed by the application, to ensure that temporary records do not persist and occupy storage, a scheduled process is typically also employed to scan the database for expired entries routinely, and to purge those entries that are no longer valid.

Workarounds such as those described above are not required for Couchbase, as it allows applications to declare the lifetime of a given document, eliminating the need to embed "validity" information in documents and eliminating the need for a routine "purge" of logically expired data.

When an application attempts to access a document which has already expired, the server will indicate to the client that the item is not found. The server internally handles the process of determining the validity of the document and removing older, expired documents.

### [](#setting-document-expiration)Setting Document Expiration

By default, Couchbase documents do not expire. However, the expiration value may be set for the _upsert_, _replace_, and _insert_ operations when modifying data.

Couchbase offers two additional operations for setting the document’s expiration without modifying its contents:

* The _get-and-touch_ operation allows an application to retrieve a document while modifying its expiration time. This method is useful when reading session data from the cluster: since accessing the data is indicative of it still being "alive", _get-and-touch_ provides a natural way to extend its lifetime.
* The _touch_ operation allows an application to modify a document’s expiration time without otherwise accessing the document. This method is useful when an application is handling a user session but does not need to access the cluster (for example, if a particular document is already cached locally).

Code snippets for setting document expiration can be found on the [data operations page](../howtos/kv-operations.md#document-expiration). This page also covers the nuances of setting relative or absolute document expiry times — all SDKs support duration, but options for setting an absolute timestamp vary by SDK and release version.

> [!IMPORTANT]
> Remember
> 
> * If you wish to use the expiration feature, then you should supply the expiry value for every mutation operation.
> * When dealing with expiration, it is important to note that _most operations will implicitly remove any existing expiration_. Thus, when modifying a document with expiration, it is important to pass the desired expiration time.
> * A document is expired as soon as the current time on the Couchbase Server node responsible for the document exceeds the expiration value. Bear this in mind in situations where the time on your application servers differs from the time on your Couchbase Server nodes.

Note that expired documents are not deleted from the server as soon as they expire. While a request to the server for an expired document will receive a response indicating the document does not exist, expired documents are actually deleted (_i.e._ cease to occupy storage and RAM) when an _expiry pager_ is run. The _expiry pager_ is a routine internal process which scans the cluster for items which have expired and promptly removes them from storage.

When gathering resource usage statistics, note that expired-but-not-purged items (such as the expiry pager has not scanned this item yet) will still be considered with respect to the overall storage size and item count.

> [!NOTE]
> Although the API only sets expiry values _per document_, it is possible that elsewhere in the server, an expiry value is being set for [every document in a bucket^](../../../server/current/learn/data/expiration.md). Should this be the case, the document TTL may be reduced, and the document may become unavailable to the app sooner than expected.