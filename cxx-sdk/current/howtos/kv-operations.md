---
title: Data Operations
description: Data service offers the simplest way to retrieve or mutate data
  where the key is known. Here we cover CRUD operations, document expiration,
  and optimistic locking with CAS.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/howtos/pages/kv-operations.adoc
  xref: xref:cxx-sdk:howtos:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/howtos/kv-operations.html)

# Data Operations

> Data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

At its heart Couchbase Server is a high-performance key-value store, and the key-value interface outlined below is the fastest and best method to perform operations involving single documents.

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform.

Before proceeding, make sure you're familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK](../hello-world/start-using-sdk.md) section.

The code samples below will use these imports:

```c++
#include <couchbase/cluster.hxx>
#include <couchbase/codec/tao_json_serializer.hxx>

#include <fmt/chrono.h>
#include <fmt/format.h>
#include <tao/json.hpp>

#include <couchbase/fmt/cas.hxx>
#include <couchbase/fmt/error.hxx>

#include <functional>
#include <iostream>
```

> [!TIP]
> The Query Service can also be used to perform many single-document operations, but we very strongly recommend using the key-value API for this instead. It can be much more efficient as the request can go directly to the correct node, there's no query parsing overhead, and it's over the highly optimized memcached binary protocol.

## [](#json)JSON

The Couchbase Server is a key-value store that's agnostic to what's stored, but it's very common to store JSON so most of the examples below will focus on that use-case.

The SDK directly supports the [taoJSON](https://github.com/taocpp/json) library, which we'll be using for these examples. taoJSON also provides the ability to encode or decode user-defined types.

In addition you can supply and receive JSON as a `std::string` or `std::vector<std::byte>`, opening the door to any JSON library.

Support for other JSON libraries can also be added by defining your own custom JSON serializers, which is described in more detail in [this guide](#json.adoc).

## [](#upsert)Upsert

Here is a simple upsert operation, which will insert the document if it does not exist, or replace it if it does.

```c++
auto content = tao::json::value{
    { "foo", "bar" },
    { "baz", "qux" },
};
auto [err, result] = collection.upsert("document-key", content).get();
```

> [!NOTE]
> All of the examples here use the simplest of the two asynchronous APIs provided by the C++ SDK, which returns an `std::future`. There's also a callback-based asynchronous API. See [Choosing an API](#concurrent-async-apis) for more details.

The C++ SDK returns a `couchbase::error` instance that wraps an `std::error_code` rather than throwing exceptions. You can check whether an error occurred like this:

```c++
if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Document upsert successful");
}
```

> [!NOTE]
> We will use `fmt::println` to simply print any errors in these samples, but the application will of course want to perform better error handling.

## [](#insert)Insert

Insert works very similarly to upsert, but will fail if the document already exists:

```c++
auto content = tao::json::value{
    { "foo", "bar" },
    { "baz", "qux" },
};
auto [err, result] = collection.insert("document-key2", content).get();
if (err.ec() == couchbase::errc::key_value::document_exists) {
    fmt::println("The document already exists");
} else if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Document inserted successfully");
}
```

## [](#retrieving-documents)Retrieving Documents

We've tried upserting and inserting documents into Couchbase Server, let's get them back:

```c++
auto [err, result] = collection.get("document-key").get();
if (err) {
    fmt::println("Error getting document: {}", err);
}
```

Of course if we're getting a document we probably want to do something with the content:

```c++
// Create some initial JSON
auto content = tao::json::value{ { "status", "awesome!" } };

// Upsert it
auto [upsert_err, insert_result] = collection.upsert("document-key3", content).get();
if (upsert_err) {
    fmt::println("Error inserting document: {}", upsert_err);
} else {
    // Get it back
    auto [get_err, get_result] = collection.get("document-key3").get();

    // Get the content of the document as a tao::json::value
    auto res_content = get_result.content_as<tao::json::value>();

    // Pull out the JSON content's status field, if it exists
    if (const auto s = res_content.find("status"); s != nullptr) {
        fmt::println("Couchbase is {}", s->get_string());
    } else {
        fmt::println("Field 'status' does not exist");
    }
}
```

## [](#replace)Replace

A very common operation is to `get` a document, modify its contents, and `replace` it:

```c++
auto initial = tao::json::value{ { "status", "great" } };

// Upsert a document
auto [upsert_err, upsert_res] = collection.upsert("document-key4", initial).get();
if (upsert_err) {
    fmt::println("Error upserting document: {}", upsert_err);
} else {
    // Get the document back
    auto [get_err, get_res] = collection.get("document-key4").get();

    // Extract the document as tao::json::value
    auto content = get_res.content_as<tao::json::value>();

    // Modify the content
    content["status"] = "awesome!";

    // Replace the document with the updated content, and the document's CAS value
    // (which we'll cover in a moment)
    auto [replace_err, replace_res] =
      collection.replace("document-key4", content, couchbase::replace_options().cas(get_res.cas())).get();
    if (replace_err.ec() == couchbase::errc::common::cas_mismatch) {
        fmt::println("Could not write as another agent has concurrently modified the document");
    } else if (replace_err) {
        fmt::println("Error: {}", replace_err);
    } else {
        fmt::println("Document replaced successfully");
    }
}
```

There's a couple of things to cover with the `replace` line.

First, most of the methods in the C++ SDK take an 'options' parameter that contains optional parameters that have sensible defaults. One of them, `cas`, is provided here. We'll see more throughout this document.

### [](#optimistic-locking)What is CAS?

CAS, or Compare and Swap, is a form of optimistic locking. Every document in Couchbase has a CAS value, and it's changed on every mutation. When you `get` a document you also get the document's CAS, and then when it's time to write the document, you send the same CAS back. If another agent has modified that document, the Couchbase Server can detect you've provided a now-outdated CAS, and return an error instead of mutating the document. This provides cheap, safe concurrency. See [this detailed description of CAS](concurrent-document-mutations.md) for further details.

In general, you'll want to provide a CAS value whenever you `replace` a document, to prevent overwriting another agent's mutations.

### [](#retrying-on-cas-failures)Retrying on CAS Failures

But if we get a CAS mismatch, we usually just want to retry the operation. Let's see a more advanced `replace` example that shows one way to handle this:

```c++
auto
retry_on_cas_mismatch(std::function<couchbase::error()> op) -> couchbase::error
{
    while (true) {
        // Perform the operation
        auto err = op();
        if (err.ec() == couchbase::errc::common::cas_mismatch) {
            // Retry if the couchbase::error wraps a cas_mismatch error code
            continue;
        } else {
            // If success or any other failure, return it
            return err;
        }
    }
}

void
get_and_replace(const couchbase::collection& collection)
{
    auto initial = tao::json::value{ { "status", "great" } };

    // Insert some initial data
    {
        auto [err, res] = collection.insert("document-key5", initial).get();
        assert(!err); // Just for demo, a production app should check the result properly
    }

    // This is the get-and-replace we want to do, as a lambda
    auto op = [&]() -> couchbase::error {
        auto [get_err, get_res] = collection.get("document-key5").get();
        if (get_err) {
            return get_err;
        }
        auto content = get_res.content_as<tao::json::value>();
        content["status"] = "awesome!";
        auto options = couchbase::replace_options().cas(get_res.cas());
        auto [replace_err, replace_res] = collection.replace("document-key5", content, options).get();
        return replace_err;
    };

    // Send our lambda to retry_on_cas_mismatch to take care of retrying it.
    auto err = retry_on_cas_mismatch(op);
    if (err) {
        fmt::println("Error: {}", err);
    } else {
        fmt::println("Replace with CAS successful");
    }
}
```

## [](#removing)Removing

Removing a document is straightforward:

```c++
auto [err, result] = collection.remove("document-key").get();
if (err.ec() == couchbase::errc::key_value::document_not_found) {
    fmt::println("The document does not exist");
} else if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Document removed successfully");
}
```

## [](#sub-document-operations)Sub-Document Operations

All of the operations seen so far involve fetching the complete document.

As an optimization the application may consider using the [Sub-Document API](subdocument-operations.md) to access or mutate specific parts of a document.

## [](#durability)Durability

Writes in Couchbase are written initially to a single active node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas.

The `durability` option, which all mutating operations accept, allows the application to wait until this replication is successful before proceeding.

It can be used like this:

```c++
auto options = couchbase::remove_options().durability(couchbase::durability_level::majority);
auto [err, result] = collection.remove("document-key2", options).get();
if (err.ec() == couchbase::errc::key_value::document_not_found) {
    fmt::println("The document does not exist");
} else if (err) {
    fmt::println("Error: {}", err);
} else {
    // The mutation is available in-memory on at least a majority of replicas
    fmt::println("Document removed successfully");
}
```

The default is `durability_level::none`, in which the SDK will return as soon as Couchbase Server has the mutation available in-memory on the active node. This is the default for a reason: it's the fastest mode, and the majority of the time is all the application needs.

However, we recognize that there are times when the application needs that extra certainty that especially vital mutations have been successfully replicated, and the other durability options provide the means to achieve this.

The options differ depend on what Couchbase Server version is in use. If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

`majority` \- The server will ensure that the change is available in memory on the majority of configured replicas.

`majority_and_persist_to_active` \- Majority level, plus persisted to disk on the active node.

`persist_to_majority` \- Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of failure-resistance. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

If a version of Couchbase Server lower than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions). Here the SDK will do a simple poll of the replicas and only return once the requested durability level is achieved. This can be achieved like this:

```c++
auto options = couchbase::remove_options().durability(couchbase::persist_to::none, couchbase::replicate_to::two);
auto [err, result] = collection.remove("document-key2", options).get();
if (err.ec() == couchbase::errc::key_value::document_not_found) {
    fmt::println("The document does not exist");
} else if (err) {
    fmt::println("Error: {}", err);
} else {
    // The mutation is available in-memory on at least two replicas
    fmt::println("Document removed successfully");
}
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

## [](#expirationttl)Expiration/TTL

Couchbase Server includes an option to have particular documents automatically expire after a set time. This can be useful for some use-cases, such as user sessions, caches, or other temporary documents.

You can set an expiration value when creating a document:

```c++
auto content = tao::json::value{ { "foo", "bar" }, { "baz", "qux" } };

auto [err, result] = collection.insert("document-key", content, couchbase::insert_options().expiry(std::chrono::hours(2))).get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Document with expiry inserted successfully");
}
```

When getting a document, the expiry is not provided automatically by Couchbase Server but it can be requested:

```c++
auto [err, result] = collection.get("document-key", couchbase::get_options().with_expiry(true)).get();
if (err) {
    fmt::println("Error getting document: {}", err);
} else if (result.expiry_time().has_value()) {
    fmt::println("Got expiry: {}", result.expiry_time().value());
} else {
    fmt::println("Error: no expiration field");
}
```

Note that when updating the document, special care must be taken to avoid resetting the expiry to zero. Here's how:

```c++
auto new_content = tao::json::value{ { "foo", "bar" } };
auto options = couchbase::replace_options().preserve_expiry(true);
auto [err, result] = collection.replace("document-key", new_content, options).get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Document with expiry replaced successfully");
}
```

Some applications may find `getAndTouch` useful, which fetches a document while updating its expiry field. It can be used like this:

```c++
auto [err, result] = collection.get_and_touch("document-key", std::chrono::hours(4)).get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Document fetched and expiry updated");
}
```

## [](#atomic-counter-operations)Atomic Counter Operations

To support counter use-cases, a Couchbase document can be treated as an integer counter and adjusted or created atomically like this:

```c++
{
    auto options = couchbase::increment_options().delta(1).initial(1);
    auto [err, result] = collection.binary().increment("counter-key", options).get();
    if (err) {
        fmt::println("Error: {}", err);
    } else {
        fmt::println("Counter now: {}", result.content());
    }
}
{
    auto options = couchbase::decrement_options().delta(1).initial(10);
    auto [err, result] = collection.binary().decrement("counter-key", options).get();
    if (err) {
        fmt::println("Error: {}", err);
    } else {
        fmt::println("Counter now: {}", result.content());
    }
}
```

Note that a counter cannot be below 0.

> [!NOTE]
> Increment & Decrement are considered part of the 'binary' API and as such may still be subject to change

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don't know the document IDs. This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here's an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```c++
auto [err, res] = collection.scan(couchbase::range_scan()).get();

if (err) {
    fmt::println("Error during scan: {}", err);
} else {
    for (auto [iter_err, item] : res) {
        if (iter_err) {
            fmt::println("Error during iteration: {}", iter_err);
        } else {
            std::cout << "Id: " << item.id() << " Content: " << item.content_as<tao::json::value>() << "\n";
        }
    }
}
```

| **1** | The ScanType.rangeScan() method has two nullable parameters: from and to. If you pass null like in this example, you'll get all documents in the collection. These parameters are for advanced use cases; you probably won't need to specify them. Instead, it's more common to use the "prefix" scan type shown in the next example. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix.

Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user.

For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with "alice::"

```c++
auto [err, res] = collection.scan(couchbase::prefix_scan("alice")).get();

if (err) {
    fmt::println("Error during scan: {}", err);
} else {
    for (auto [iter_err, item] : res) {
        if (iter_err) {
            fmt::println("Error during iteration: {}", iter_err);
        } else {
            std::cout << "Id: " << item.id() << " Content: " << item.content_as<tao::json::value>() << "\n";
        }
    }
}
```

| **1** | Note the scan type is **prefix\_scan**. |
| ----- | --------------------------------------- |

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```c++
auto [err, res] = collection.scan(couchbase::sampling_scan(100)).get();

if (err) {
    fmt::println("Error during scan: {}", err);
} else {
    for (auto [iter_err, item] : res) {
        if (iter_err) {
            fmt::println("Error during iteration: {}", iter_err);
        } else {
            std::cout << "Id: " << item.id() << " Content: " << item.content_as<tao::json::value>() << "\n";
        }
    }
}
```

| **1** | In this example, no more than 100 documents are returned. |
| ----- | --------------------------------------------------------- |

### [](#kv-range-scan-only-ids)Get IDs instead of full document

If you only want the document IDs, set the `ids_only()` option to true, like this:

KV Range Scan for all document IDs in a collection

```c++
auto opts = couchbase::scan_options().ids_only(true);
auto [err, res] = collection.scan(couchbase::range_scan(), opts).get();

if (err) {
    fmt::println("Error during scan: {}", err);
} else {
    for (auto [iter_err, item] : res) {
        if (iter_err) {
            fmt::println("Error during iteration: {}", iter_err);
        } else {
            fmt::println("Id: {}", item.id());
        }
    }
}
```

| **1** | The returned scan\_result objects' content will be empty. |
| ----- | --------------------------------------------------------- |

Setting `ids_only()` to true also works with the other scan types described above.

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages.

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitrary bytes, or binary format](../concept-docs/nonjson.md).

Our [Query Engine](sqlpp-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).