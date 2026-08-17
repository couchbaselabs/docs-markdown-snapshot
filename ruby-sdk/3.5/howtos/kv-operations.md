---
title: Data Operations
description: Data service offers the simplest way to retrieve or mutate data
  where the key is known.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/howtos/pages/kv-operations.adoc
  xref: xref:3.5@ruby-sdk:howtos:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.5/howtos/kv-operations.html)

# Data Operations

> Data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

## [](#documents)Documents

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform. Or read on, for a hands-on introduction to working with documents from the Ruby SDK.

## [](#crud-operations)CRUD Operations

The core interface to Couchbase Server is simple KV operations on full documents. Make sure you're familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK section](../hello-world/start-using-sdk.md). We're going to expand on the short _Upsert_ example we used there, adding options as we move through the various CRUD operations. Here is the _Insert_ operation, with simple error handling:

```ruby
begin
  collection.insert("document-key", {"title" => "My Blog Post"})
rescue Error::DocumentExists
  puts "The document already exists!"
end
```

Setting a Compare and Swap (CAS) value is a form of optimistic locking - dealt with in depth in the [CAS page](concurrent-document-mutations.md). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document's metadata whenever a document is accessed. Without explicitly setting it, a newly-created document would have a CAS value of _0_.

```ruby
collection.upsert("my-document", {"initial" => true})

result = collection.get("my-document")
content = result.content
content["modified"] = true
content["initial"] = false
collection.replace("my-document", content, Options::Replace(cas: result.cas))
```

Expiration sets an explicit time to live (TTL) for a document. For a discussion of item (Document) _vs_ Bucket expiration, see the [Expiration Overview page](#7.1@server:learn:buckets-memory-and-storage/expiration.adoc#expiration-bucket-versus-item).

```ruby
collection.upsert("my-document", {"doc" => true},
                  Options::Insert(expiry: 2 * 60 * 60))

# or with ActiveSupport::Duration
require 'active_support/core_ext/numeric/time'
collection.upsert("my-document", {"doc" => true},
                  Options::Insert(expiry: 2.hours))

# Time instances also acceptable as absolute time points
expiry = Time.now + 30 # 30 seconds from now
collection.upsert("my-document", {"doc" => true},
                  Options::Insert(expiry: expiry))
```

## [](#durability)Durability

Writes in Couchbase are written to a single node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas.

The optional `durability_level` parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding.

It can be used like this:

```ruby
collection.upsert("my-document", {"doc" => true},
                Options::Upsert(durability_level: :majority))
```

If no argument is provided the application will report success back as soon as the primary node has acknowledged the mutation in its memory. However, we recognize that there are times when the application needs that extra certainty that especially vital mutations have been successfully replicated, and the other durability options provide the means to achieve this.

The options differ depending on what Couchbase Server version is in use. If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

* `:majority` \- The server will ensure that the change is available in memory on the majority of configured replicas.
* `:majority_and_persist_to_active` \- Majority level, plus persisted to disk on the active node.
* `:persist_to_majority` \- Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of safety. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

If a version of Couchbase Server earlier than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions). Here the SDK will do a simple poll of the replicas and only return once the requested durability level is achieved. This can be achieved like this:

```ruby
collection.upsert("my-document", {"doc" => true},
                Options::Upsert(persist_to: :none, replicate_to: :two))
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

> [!TIP]
> Sub-Document Operations
> 
> All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Document Operations](subdocument-operations.md).

## [](#retrieving-full-documents)Retrieving full documents

Using the `.get()` method with the document key can be done in a similar fashion to the other operations:

```ruby
begin
  get_result = collection.get("document-key")
  title = get_result.content["title"]
  puts title
  #=> My Blog Post
rescue Error::DocumentExists
  puts "Document not found!"
end
```

You can then add in logic to filter on the fields returned:

```ruby
found = collection.get("document-key")
content = found.content
if content["author"] == "mike"
  # do something
else
  # do something else
end
```

## [](#removing)Removing

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

```ruby
begin
  collection.remove("my-document")
rescue Error::DocumentNotFound
  puts "Document did not exist when trying to remove"
end
```

## [](#expiration-ttl)Expiration / TTL

Couchbase Server includes an option to have particular documents automatically expire after a set time. This can be useful for some use-cases, such as user sessions, caches, or other temporary documents.

You can set an expiry value when creating a document:

```ruby
collection.upsert("my-document", {"doc" => true},
                  Options::Insert(expiry: 2 * 60 * 60))

# or with ActiveSupport::Duration
require 'active_support/core_ext/numeric/time'
collection.upsert("my-document", {"doc" => true},
                  Options::Insert(expiry: 2.hours))

# Time instances also acceptable as absolute time points
expiry = Time.now + 30 # 30 seconds from now
collection.upsert("my-document", {"doc" => true},
                  Options::Insert(expiry: expiry))
```

When getting a document, the expiry is not provided automatically by Couchbase Server but it can be requested:

```ruby
found = collection.get("my-document", Options::Get(with_expiry: true))
puts "Expiry of found doc: #{found.expiry_time})"
#=> Expiry of found doc: 2020-07-26 21:52:22 +0300
```

> [!NOTE]
> The type returned by `#expiry_time` is `Time`, and always represents absolute time when the document will expire. The `#expiry` method that returned integer number of seconds since epoch is _\*deprecated\*_, and will be removed in release `3.1`.

Note that when updating the document, special care must be taken to avoid resetting the expiry to zero. Here's how:

```ruby
found = collection.get("my-document", Options::Get(with_expiry: true))

collection.replace("my-document", {"content" => "something new"},
                   Options::Replace(expiry: found.expiry_time))
```

Some applications may find `getAndTouch` useful, which fetches a document while updating its expiry field. It can be used like this:

```ruby
collection.get_and_touch("my-document", 24 * 60 * 60)

# or with ActiveSupport::Duration
require 'active_support/core_ext/numeric/time'
collection.get_and_touch("my-document", 1.day)
```

## [](#atomic-counters)Atomic Counters

The value of a document can be increased or decreased atomically using `#increment()` and `#decrement()` on the `Couchbase::BinaryCollection`. See the [API Guide](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/BinaryCollection.html) for more information.

> [!NOTE]
> Increment & Decrement are considered part of the 'binary' API and as such may still be subject to change.

Increment

```ruby
# increment binary value by 1 (default)
binary_collection = collection.binary
res = binary_collection.increment("foo")
res.content
#=> 1
```

```ruby
# Create a document and assign it to 10 -- counter works atomically
# by first creating a document if it doesn't exist. If it exists,
# the same method will increment/decrement per the "delta" parameter
res = binary_collection.increment("counter",
           Options::Increment(initial: 10, delta: 2))
res.value
#=> 10
```

Decrement

```ruby
# decrement binary value by 1 (default)
res = binary_collection.decrement("foo")
res.content
#=> 0
```

Decrement (with options)

```ruby
# Decrement value by 4 to 8
res = binary_collection.decrement("counter",
           Options::Decrement(initial: 10, delta: 4))
res.value
#=> 8
```

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](#7.1@server:manage:manage-xdcr/xdcr-management-overview.adoc) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don't know the document IDs. This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here's an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```ruby
result = collection.scan(RangeScan.new) (1)
result.each do |item|
  puts "ID: #{item.id}, Content: #{item.content}"
end
```

| **1** | The RangeScan class has two optional attributes: from and to. If you omit them like in this example, you'll get all documents in the collection. These parameters are for advanced use cases; you probably won't need to specify them. Instead, it's more common to use the "prefix" scan type shown in the next example. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix. Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user. For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with `alice::`

```ruby
result = collection.scan(PrefixScan.new('alice::')) (1)
result.each do |item|
  puts "ID: #{item.id}, Content: #{item.content}"
end
```

| **1** | Note the scan type is PrefixScan |
| ----- | -------------------------------- |

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```ruby
result = collection.scan(SamplingScan.new(100))
result.each do |item|
  puts "ID: #{item.id}, Content: #{item.content}"
end
```

### [](#kv-range-scan-only-ids)Get IDs instead of full documents

If you only want the document IDs, set the `ids_only` attribute of `Options::Scan` to `true`, like this:

KV Range Scan for all document IDs in a collection

```ruby
result = collection.scan(RangeScan.new, Options::Scan.new(ids_only: true))
result.each do |item|
  puts "ID: #{item.id}"
end
```

## [](#scoped-kv-operations)Scoped KV Operations

It is possible to perform scoped key-value operations on named [Collections](../../../server/7.6/learn/data/scopes-and-collections.md) _with Couchbase Server release 7.x_. See the [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Collection.html) for more information.

Here is an example showing an upsert in the `users` collection, which lives in the `travel-sample.tenant_agent_00` keyspace:

```ruby
agent_scope = bucket.scope("tenant_agent_00")
users_collection = agent_scope.collection("users")
document = {"name" => "John Doe", "preferred_email" => "johndoe111@test123.test"}

result = users_collection.upsert("user-key", document)
```

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages.

Our [Query Engine](n1ql-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).

See the [Caching Example](caching-example.md) for ideas on integrating with Rails.