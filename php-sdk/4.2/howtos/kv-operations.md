---
title: Data Operations
description: Key Value (KV) or data service offers the simplest way to retrieve
  or mutate data where the key is known.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/howtos/pages/kv-operations.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.2@php-sdk:howtos:kv-operations.adoc[]
---

[View original HTML](/php-sdk/4.2/howtos/kv-operations.html)

# Data Operations

> Key Value (KV) or data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

The complete code samples used on this page can be found here:

* [kv-crud.php](https://github.com/couchbase/docs-sdk-php/blob/release/3.2/modules/howtos/examples/kv-crud.php)
* [kv-expiry.php](https://github.com/couchbase/docs-sdk-php/blob/release/3.2/modules/howtos/examples/kv-expiry.php)
* [kv-counter.php](https://github.com/couchbase/docs-sdk-php/blob/release/3.2/modules/howtos/examples/kv-counter.php)

## [](#documents)Documents

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform. Or read on, for a hands-on introduction to working with documents from the PHP SDK.

## [](#crud-operations)CRUD Operations

The core interface to Couchbase Server is simple KV operations on full documents. Make sure you’re familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK section](../hello-world/start-using-sdk.md). We’re going to expand on the short _Upsert_ example we used there, adding options as we move through the various CRUD operations. Here is the _Insert_ operation at its simplest:

```php
$document = ["foo" => "bar", "bar" => "foo"];
$res = $collection->insert("document-key-new", $document);
printf("document \"document-key-new\" has been created with CAS \"%s\"\n", $res->cas());
```

Options may be added to operations:

```php
$document = ["foo" => "bar", "bar" => "foo"];
$opts = new InsertOptions();
$opts->timeout(300000 /* milliseconds */);
$res = $collection->insert("document-key", $document, $opts);
printf("document \"document-key\" has been created with CAS \"%s\"\n", $res->cas());
```

Setting a Compare and Swap (CAS) value is a form of optimistic locking - dealt with in depth in the [CAS page](concurrent-document-mutations.md). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document’s metadata whenever a document is accessed. Without explicitly setting it, a newly-created document would have a CAS value of _0_.

_Timeout_ is an optional parameter which is a integer value representing time duration in milliseconds. Timeout sets the timeout value for the underlying network connection. We will add to these options for the _Replace_ example:

```php
// Replace document with incorrect CAS
$opts = new ReplaceOptions();
$opts->timeout(300000 /* milliseconds */);
$invalidCas = "776t3gAAAAA=";
$opts->cas($invalidCas);
try {
    $collection->replace("document-key", $document, $opts);
} catch (\Couchbase\Exception\CasMismatchException $ex) {
    printf("document \"document-key\" cannot be replaced with CAS \"%s\"\n", $invalidCas);
}

// Get and Replace document with CAS
$res = $collection->get("document-key");
$doc = $res->content();
$doc["bar"] = "moo";

$opts = new ReplaceOptions();
$oldCas = $res->cas();
$opts->cas($oldCas);
$res = $collection->replace("document-key", $doc, $opts);
printf("document \"document-key\" \"%s\" been replaced successfully. New CAS \"%s\"\n", $oldCas, $res->cas());
```

The example above also shows how to handle the case when optimistic falure will fail.

Expiration sets an explicit time to live (TTL) for a document. We’ll discuss modifying `expiry` in more details [below](#expiration-ttl). For a discussion of item (Document) _vs_ Bucket expiration, see the [Expiration Overview page](#7.1@server:learn:buckets-memory-and-storage/expiration.adoc#expiration-bucket-versus-item).

```php
$document = ["foo" => "bar", "bar" => "foo"];
$opts = new UpsertOptions();
$opts->expiry(60 * 1000 /* 60 seconds */);
$res = $collection->upsert("document-key", $document, $opts);
printf("document \"document-key\" has been created with CAS \"%s\"\n", $res->cas());
```

## [](#durability)Durability

In Couchbase Server releases before 6.5, Durability was set with these two options — see the [6.0 Durability documentation](#2.6@php-sdk::durability.adoc) — covering how many replicas the operation must be propagated to and how many persisted copies of the modified record must exist. If a version of Couchbase Server lower than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions).

If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

* `Majority` \- The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` \- Majority level, plus persisted to disk on the active node.
* `PersistToMajority` \- Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of safety. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

The following example demonstrates using the newer durability features available in Couchbase server 6.5 onwards.

```php
// Upsert with Durability
$opts = new UpsertOptions();
$opts->timeout(3000 /* milliseconds */);
$opts->durabilityLevel(DurabilityLevel::MAJORITY);
$res = $collection->upsert("document-key2", $opts);
printf("document \"document-key2\" has been created with CAS \"%s\"\n", $res->cas());
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

> [!TIP]
> Sub-Document Operations
> 
> All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Document Operations](subdocument-operations.md).

## [](#retrieving-full-documents)Retrieving full documents

Using the `Get()` method with the document key can be done in a similar fashion to the other operations:

```php
$res = $collection->get("document-key");
$doc = $res->content();
printf("document \"document-key\" has content: \"%s\" CAS \"%s\"\n", json_encode($doc), $res->cas());
```

Timeout can also be set - as in the earlier `Insert` example:

```php
$opts = new GetOptions();
$opts->timeout(3000 /* milliseconds */);
$res = $collection->get("document-key", $opts);
$doc = $res->content();
printf("document \"document-key\" has content: \"%s\" CAS \"%s\"\n", json_encode($doc), $res->cas());
```

## [](#removing)Removing

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

Remove (with options)

```php
$opts = new RemoveOptions();
$opts->timeout(5000); // 5 seconds
$result = $collection->remove("document-key", $opts);
printf("document \"document-key\" \"%s\" been removed successfully.\n", $res->cas());
```

## [](#expiration-ttl)Expiration / TTL

By default, Couchbase documents do not expire, but transient or temporary data may be needed for user sessions, caches, or other temporary documents. Using `Touch()`, you can set expiration values on documents to handle transient data:

> [!NOTE]
> Increment & Decrement are considered part of the ‘binary’ API and as such may still be subject to change.

```php
$collection->touch($key, 60 /* seconds */);
```

A network timeout can be set with the optional `TouchOptions()`, in the same fashion as earlier examples on this page:

```php
$opts = new TouchOptions();
$opts->timeout(500000 /* microseconds */);
$collection->touch($key, 60 /* seconds */);
```

Another way to change expiration time is to use `getAndTouch()` method of the collection.

```php
$res = $collection->getAndTouch($key, 1 /* seconds */);
printf("[getAndTouch] document content: %s\n", var_export($res->content(), true));

sleep(2); // wait until the document will expire

try {
    $collection->get($key);
} catch (Couchbase\Exception\DocumentNotFoundException $ex) {
    printf("The document does not exist\n");
}
```

## [](#atomic-counters)Atomic Counters

The value of a document can be increased or decreased atomically using `Binary.Increment()` and `.Binary.Decrement()`.

> [!NOTE]
> Increment & Decrement are considered part of the ‘binary’ API and as such may still be subject to change.

Increment

```php
// increment binary value by 1 (default)
$binaryCollection = $collection->binary();
$res = $binaryCollection->increment("foo");
```

```php
// Create a document and assign it to 10 -- counter works atomically
// by first creating a document if it doesn't exist. If it exists,
// the same method will increment/decrement per the "delta" parameter
$key = "phpDevguideExampleCounter";
$opts = new IncrementOptions();
$opts->initial(10)->delta(2);

$res = $binaryCollection->increment($key, $opts);
// Should print 10
printf("Initialized Counter: %d\n", $res->content());
```

Decrement

```php
// decremtnt binary value by 1 (default)
$res = $binaryCollection->decrement("foo");
```

Decrement (with options)

```php
$opts = new DecrementOptions();
$opts->initial(10)->delta(4);
// Decrement value by 4 to 8
$res = $binaryCollection->decrement($key, $opts);
// Should print 8
printf("Decremented Counter: %d\n", $res->content());
```

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

Unresolved include directive in modules/howtos/pages/kv-operations.adoc - include::7.5@sdk:shared:partial$atomic.adoc\[\]

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don’t know the document IDs. This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here’s an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```php
$results = $collection->scan(RangeScan::build());
foreach ($results as $result) {
    printf("\n ID: %s, content:\n ", $result->id());
    print_r($result->content());
}
```

| **1** | The RangeScan class has two optional parameters: from and to. If you omit them like in this example, you’ll get all documents in the collection. These parameters are for advanced use cases; you probably won’t need to specify them. Instead, it’s more common to use the "prefix" scan type shown in the next example. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix. Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user. For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with `alice::`

```php
$results = $collection->scan(PrefixScan::build("alice::"));
foreach ($results as $result) {
    printf("\n ID: %s, content:\n ", $result->id());
    print_r($result->content());
}
```

| **1** | Note the scan type is PrefixScan |
| ----- | -------------------------------- |

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```php
$results = $collection->scan(SamplingScan::build(100));
foreach ($results as $result) {
    printf("\n ID: %s, content:\n ", $result->id());
    print_r($result->content());
}
```

### [](#kv-range-scan-only-ids)Get IDs instead of full documents

If you only want the document IDs, set the `idsOnly()` in `ScanOptions` to `true`, like this:

KV Range Scan for all document IDs in a collection

```php
$results = $collection->scan(RangeScan::build(), ScanOptions::build()->idsOnly(true));
foreach ($results as $result) {
    printf("ID: %s \n", $result->id());
}
```

## [](#scoped-kv-operations)Scoped KV Operations

It is possible to perform scoped key value operations on named [Collections](#7.1@server:learn:data/scopes-and-collections.adoc) _with the beta version of the next Couchbase Server release, 7.0β_. See the [API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Collection.html) for more information.

> [!CAUTION]
> This feature is marked [_Uncommitted_](../project-docs/compatibility.md#interface-stability). Expect a promotion to _Committed_ API in a future minor release.

Here is an example showing an upsert in the `users` collection, which lives in the `travel-sample.tenant_agent_00` keyspace:

```php
$document = ["name" => "John Doe", "preferred_email" => "johndoe111@test123.test"];
$opts = new UpsertOptions();

$agentScope = $bucket->scope("tenant_agent_00");
$usersCollection = $agentScope->collection("users");

$res = $usersCollection->upsert("user-key", $document, $opts);
printf("document \"user-key\" has been created with CAS \"%s\"\n", $res->cas());
```

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages.

Another way of increasing network performance is to _pipeline_ operations with [Batching Operations](concurrent-async-apis.md#batching-with-process-forks).

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitary bytes, or binary format](#concept-docs:data-model:non-json.adoc).

Our [Query Engine](n1ql-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).