[View original HTML](/java-sdk/current/howtos/kv-operations.html)

> Data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS — as well as KV Range scan, for querying without an index. 

The complete code sample used on this page can be downloaded from [here](https://github.com/couchbase/docs-sdk-java/blob/release/3.11/modules/devguide/examples/java/KvOperations.java).

At its heart Couchbase Server is a high-performance key-value store, and the key-value interface outlined below is the fastest and best method to perform operations involving single documents.

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform.

Before proceeding, make sure you’re familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK](../hello-world/start-using-sdk.md) section.

The code samples below will use these imports:

```java
import static com.couchbase.client.java.kv.GetOptions.getOptions;
import static com.couchbase.client.java.kv.InsertOptions.insertOptions;
import static com.couchbase.client.java.kv.ReplaceOptions.replaceOptions;
import static com.couchbase.client.java.kv.UpsertOptions.upsertOptions;

import java.time.Duration;
import java.time.Instant;
import java.time.Period;
import java.util.Optional;
import java.util.stream.Stream;

import com.couchbase.client.core.error.CasMismatchException;
import com.couchbase.client.core.error.CouchbaseException;
import com.couchbase.client.core.error.DocumentExistsException;
import com.couchbase.client.core.error.DocumentNotFoundException;
import com.couchbase.client.core.error.DurabilityImpossibleException;
import com.couchbase.client.core.error.ReplicaNotConfiguredException;
import com.couchbase.client.core.msg.kv.DurabilityLevel;
import com.couchbase.client.java.AsyncCollection;
import com.couchbase.client.java.Bucket;
import com.couchbase.client.java.Cluster;
import com.couchbase.client.java.Collection;
import com.couchbase.client.java.ReactiveCollection;
import com.couchbase.client.java.Scope;
import com.couchbase.client.java.json.JsonObject;
import com.couchbase.client.java.kv.GetResult;
import com.couchbase.client.java.kv.MutationResult;
import com.couchbase.client.java.kv.PersistTo;
import com.couchbase.client.java.kv.ReplicateTo;
```

|  | SQL++ vs. Key-Value [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) can also be used to perform many single-document operations but we very strongly recommend using the key-value API for this instead, as it can be much more efficient. The request can go directly to the correct node, there’s no query parsing overhead, and it’s over the highly optimized memcached binary protocol. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#json)JSON

The Couchbase Server is a key-value store that’s agnostic to what’s stored, but it’s very common to store JSON so most of the examples below will focus on that use-case.

The Java SDK provides you with several options for working with JSON.

If you pass any object (like the provided `JsonObject` and `JsonArray`), including `Map<String, Object>` or `List<Object>` into the APIs provided, the SDK will use its internal JSON codec (utilizing [Jackson](https://github.com/FasterXML/jackson)) to encode/decode those objects transparently. The SDK also supports custom transcoders and serializers which are covered separately.

## [](#crud)CRUD

|  | Sub-Document Operations All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Document Operations](subdocument-operations.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#upsert)Upsert

Here is a simple upsert operation, which will insert the document if it does not exist, or replace it if it does.

We’ll use the built-in JSON types for simplicity, but you can use different types if you want.

```java
JsonObject content = JsonObject.create()
    .put("author", "mike")
    .put("title", "My Blog Post 1");

MutationResult result = collection.upsert("document-key", content);
```

|  | All the examples here use the Java SDK’s simplest API, which blocks until the operation is performed. There’s also an asynchronous API that is based around Java’s CompletableFuture, and a reactive API built around [Project Reactor](https://projectreactor.io/). They can be accessed like this: AsyncCollection asynccollection = collection.async(); ReactiveCollection reactivecollection = collection.reactive(); |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#insert)Insert

Insert works very similarly to upsert, but will fail if the document already exists with a `DocumentExistsException`:

```java
try {
  JsonObject content = JsonObject.create()
      .put("title", "My Blog Post 2");
  MutationResult insertResult = collection.insert("document-key2", content);
} catch (DocumentExistsException ex) {
  System.err.println("The document already exists!");
} catch (CouchbaseException ex) {
  System.err.println("Something else happened: " + ex);
}
```

### [](#retrieving-documents)Retrieving documents

We’ve tried upserting and inserting documents into Couchbase Server, let’s get them back:

```java
try {
  GetResult getResult = collection.get("document-key");
  String title = getResult.contentAsObject().getString("title");
  System.out.println(title); // title == "My Blog Post"
} catch (DocumentNotFoundException ex) {
  System.out.println("Document not found!");
}
```

Of course if we’re getting a document we probably want to do something with the content:

```java
GetResult found = collection.get("document-key");
JsonObject content = found.contentAsObject();
if (content.getString("author").equals("mike")) {
  // do something
} else {
  // do something else
}
```

Once we have a `GetResult`, we can use `contentAsObject()` to turn the content back into a `JsonObject` like we inserted it in the examples before, or use the more generic `contentAs(T.class)` equivalent to turn it back into other entity structures. In fact, the `contentAsObject()` method is just a convenience method for `contentAs(JsonObject.class)`.

### [](#replace)Replace

A very common sequence of operations is to `get` a document, modify its contents, and `replace` it.

```java
collection.upsert("my-document", JsonObject.create().put("initial", true));

GetResult result = collection.get("my-document");
JsonObject content = result.contentAsObject();
content.put("modified", true).put("initial", false);
collection.replace("my-document", content, replaceOptions().cas(result.cas()));
```

We `upsert` an initial version of the document. We don’t care about the exact details of the result, just whether it succeeded or not, so do not assign a return value. Then we `get` it back into `doc` and pull out the document’s content as a `JsonObject` using `contentAs`. Afterwards, we update a field in the `JsonObject` with `put`. `JsonObject` is mutable, we don’t need to store the result of the `put`. Finally, we `replace` the document with the updated content, and a CAS value, storing the final result as `result`.

#### [](#what-is-cas)What is CAS?

CAS, or Compare And Swap, is a form of optimistic locking. Every document in Couchbase has a CAS value, and it’s changed on every mutation. When you `get` a document you also get the document’s CAS, and then when it’s time to write the document, you send the same CAS back. If another thread or program has modified that document in the meantime, the Couchbase Server can detect you’ve provided a now-outdated CAS, and return an error. This provides cheap, safe concurrency. See [this detailed description of CAS](concurrent-document-mutations.md) for further details.

In general, you’ll want to provide a CAS value whenever you `replace` a document, to prevent overwriting another agent’s mutations.

### [](#retrying-on-cas-failures)Retrying on CAS failures

But if we get a CAS mismatch, we usually just want to retry the operation. Let’s see a more advanced `replace` example that shows one way to handle this:

```java
String id = "my-document";
collection.upsert(id, JsonObject.create().put("initial", true));

while (true) {
  GetResult found = collection.get(id);
  JsonObject content = found.contentAsObject();
  content.put("modified", true).put("initial", false);

  try {
    collection.replace(id, content, replaceOptions().cas(found.cas()));
    break; // if successful, break out of the retry loop
  } catch (CasMismatchException ex) {
    // don't do anything, we'll retry the loop
  }
}
```

Note that this code is simplistic to show how CAS retry works in general. If the `replace()` above never works, you would always get a CAS mismatch, and never break out of the loop - so `for(int i = 0; i < maxAttempts; i++)` would be a reasonable alternative.

In later chapters we cover more sophisticated approaches to this, including asynchronous retry, retry with backoff and bailing out after a maximum amount of tries. All these should be in place for robust, production ready code.

### [](#removing)Removing

Removing a document is straightforward:

```java
try {
  collection.remove("my-document");
} catch (DocumentNotFoundException ex) {
  System.out.println("Document did not exist when trying to remove");
}
```

Like `replace`, `remove` also optionally takes the CAS value if you want to make sure you are only removing the document if it hasn’t changed since you last fetched it.

## [](#durability)Durability

Writes in Couchbase are written to a single node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas.

The optional `durability` parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding.

It can be used like this:

```java
collection.upsert("my-document", JsonObject.create().put("doc", true),
    upsertOptions().durability(DurabilityLevel.MAJORITY));
```

If no argument is provided the application will report success back as soon as the primary node has acknowledged the mutation in its memory. However, we recognize that there are times when the application needs that extra certainty that especially vital mutations have been successfully replicated, and the other durability options provide the means to achieve this.

The options differ depend on what Couchbase Server version is in use. If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

* `Majority` — The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` — Majority level, plus persisted to disk on the active node.
* `PersistToMajority` — Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of safety. Note that nothing comes for free — for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These tradeoffs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

If a version of Couchbase Server lower than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions). Here the SDK will do a simple poll of the replicas and only return once the requested durability level is achieved. This can be achieved like this:

```java
collection.upsert("my-document", JsonObject.create().put("doc", true),
    upsertOptions().durability(PersistTo.NONE, ReplicateTo.TWO));
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

## [](#document-expiration)Document Expiration

Couchbase Server includes an option to have particular documents automatically expire after a set time. This can be useful for some use-cases, such as user sessions, caches, or other temporary documents.

You can set an expiry value from a `Duration` when creating a document:

```java
MutationResult insertResult = collection.insert("my-document2", json,
    insertOptions().expiry(Duration.ofHours(2)));
```

The expiry may be specified as a `Duration` only if the provided value is less than 50 years.

For expiration more than 50 years in the future, or if you have already calculated when a document should expire, you can specify the expiry as an `Instant`:

```java
MutationResult insertResult = collection.insert("my-document3", json,
    insertOptions().expiry(Instant.now().plus(Period.ofDays(62))));
```

When getting a document from Couchbase Server, the expiry is not included by default, but it can be requested by setting the `withExpiry` option to true:

```java
GetResult result = collection.get("my-document3", getOptions().withExpiry(true));
Optional<Instant> expiry = result.expiryTime();
System.out.println("Expiry of found doc: " + expiry);
```

Note that when updating the document, special care must be taken to avoid resetting the expiry to zero. If you are using Couchbase Server 7.0 or later, set the `preserveExpiry` option when updating the document:

```java
collection.replace("my-document3", json,
    replaceOptions().preserveExpiry(true));
```

Prior to Couchbase 7.0, it’s necessary to fetch the previous expiry and set it again:

```java
GetResult found = collection.get("my-document3", getOptions().withExpiry(true));

MutationResult result = collection.replace("my-document3", json,
    replaceOptions().expiry(found.expiryTime().get()));
```

Some applications may find `getAndTouch` useful, which fetches a document while updating its expiry field. It can be used like this:

```java
GetResult result = collection.getAndTouch("my-document3", Duration.ofDays(1));
```

## [](#atomic-counters)Atomic Counters

The value of a document can be increased or decreased atomically using `collecion.binary().increment()` and `collection.binary().decrement()`.

|  | Increment & Decrement are considered part of the ‘binary’ API and as such may still be subject to change |
|  | -------------------------------------------------------------------------------------------------------- |

See the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/kv/Increment.html) for full details.

|  | Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the Touch() method. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#scoped-kv-operations)Scoped KV Operations

It is possible to perform scoped key-value operations on named [Collections](../../../server/current/learn/data/scopes-and-collections.md) _with Couchbase Server release 7.x_. See the [API docs](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html) for more information.

Here is an example showing an upsert in the `users` collection, which lives in the `travel-sample.tenant_agent_00` keyspace:

```java
Scope agentScope = bucket.scope("tenant_agent_00");
Collection usersCollection = agentScope.collection("users");

JsonObject content = JsonObject.create().put("name", "John Doe").put("preferred_email",
    "johndoe111@test123.test");
MutationResult result = usersCollection.upsert("user-key", content);
```

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don’t know the document IDs. This feature requires Couchbase Server 7.6 or newer.

|  | KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-range)Range scan

Here’s an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```java
Stream<ScanResult> results = collection.scan(
    ScanType.rangeScan(null, null) (1)
);
results.forEach(System.out::println);
```

| **1** | The ScanType.rangeScan() method has two nullable parameters: from and to. If you pass null like in this example, you’ll get all documents in the collection. These parameters are for advanced use cases; you probably won’t need to specify them. Instead, it’s more common to use the "prefix" scan type shown in the next example. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix.

Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user.

For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with "alice::"

```java
Stream<ScanResult> results = collection.scan(
    ScanType.prefixScan("alice::") (1)
);
results.forEach(System.out::println);
```

| **1** | Note the scan type is **prefixScan**. |
| ----- | ------------------------------------- |

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```java
Stream<ScanResult> results = collection.scan(
    ScanType.samplingScan(100) (1)
);
results.forEach(System.out::println);
```

| **1** | In this example, no more than 100 documents are returned. |
| ----- | --------------------------------------------------------- |

### [](#kv-range-scan-only-ids)Get IDs instead of full document

If you only want the document IDs, set the `idsOnly` option to true, like this:

KV Range Scan for all document IDs in a collection

```java
Stream<ScanResult> results = collection.scan(
    ScanType.rangeScan(null, null),
    ScanOptions.scanOptions()
        .idsOnly(true)
);
results.forEach(it -> System.out.println(it.id())); (1)
```

| **1** | The returned ScanResult objects throw NoSuchElementException if you try to access any property other than id. |
| ----- | ------------------------------------------------------------------------------------------------------------- |

Setting `idsOnly` to true also works with the other scan types described above.

## [](#additional-resources)Additional resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements — see the [Sub-Document](subdocument-operations.md) pages.

For a significant performance speed up with large volumes of data, reference our [asynchronous programming options](concurrent-async-apis.md).

Another way of increasing network performance is to _pipeline_ operations with [Batching Operations](concurrent-async-apis.md#batching).

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitrary bytes, or binary format](../concept-docs/nonjson.md).

Our [Query Engine](sqlpp-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++.