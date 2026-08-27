---
title: Data Operations
description: Data service offers the simplest way to retrieve or mutate data
  where the key is known. Here we cover CRUD operations, document expiration,
  and optimistic locking with CAS.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/kv-operations.adoc
  xref: xref:rust-sdk:howtos:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/kv-operations.html)

# Data Operations

> Data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

At its heart Couchbase Server is a high-performance key-value store, and the key-value interface outlined below is the fastest and best method to perform operations involving single documents.

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform.

Before proceeding, make sure you're familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK](../hello-world/start-using-sdk.md) section.

> [!TIP]
> The Query Service can also be used to perform many single-document operations, but we very strongly recommend using the key-value API for this instead. It can be much more efficient as the request can go directly to the correct node, there's no query parsing overhead, and it's over the highly optimized memcached binary protocol.

## [](#upsert)Upsert

Here is a simple upsert operation, which will insert the document if it does not exist, or replace it if it does.

```rust
let doc = json!({
        "foo": "bar",
        "baz": "qux",
});

match collection.upsert("document-key", doc, None).await {
    Ok(_result) => {
        println!("Document upsert successful");
    }
    Err(e) => {
        println!("Error: {e}");
    }
}
```

> [!NOTE]
> Handling Single Errors
> 
> We will use `println` to simply print any errors in these samples, but the application will of course want to perform better error handling.

## [](#insert)Insert

Insert works very similarly to upsert, but will fail if the document already exists:

```rust
let doc = json!({
        "foo": "bar",
        "baz": "qux",
});

match collection.insert("document-key", doc, None).await {
    Ok(_result) => {
        println!("Document insert successful");
    }
    Err(e) => {
        println!("Error: {e}");
    }
}
```

## [](#retrieving-documents)Retrieving Documents

We've tried upserting and inserting documents into Couchbase Server, let's get them back:

```rust
let result = collection.get("document-key", None).await?;
```

Of course if we're getting a document we probably want to do something with the content:

```rust
let doc = json!({
        "status": "bar",
});

collection.insert("document-key", doc, None).await?;

let result = collection.get("document-key", None).await?;
let value: serde_json::Value = result.content_as()?;
// Unwrap for simplicity.
let status = value.get("status").unwrap();
let status = status.as_str().unwrap();

println!("Couchbase is ${status}");
```

Let's break down what's going on here.

We're using the `?` operator to propagate errors for brevity.

First, we create some JSON using `serde_json` and insert it.

Then, we get the document.

If it's successful, we convert the document's content into a `serde_json::Value`.

We can use `contentAs` to return the document's content in all sorts of ways: as a String, as an int, as a custom type; it's very flexible. Here, we've asked for it to be returned as a `Value` — a flexible way to handle JSON.

Finally, if the conversion to a `Value` was successful, we try to get the "status" field (which returns an `Option`), and print it if we were successful.

## [](#replace)Replace

A very common operation is to `get` a document, modify its contents, and `replace` it.

```rust
let doc_id = "document-key";

let doc = json!({"status": "great"});

// Insert a document.  Don't care about the exact details of the result so just propagate
// the error.
collection.insert(&doc_id, &doc, None).await?;

// Get the document back
let get_result = collection.get(doc_id, None).await?;
let mut value: serde_json::Value = get_result.content_as()?;
value["status"] = json!("awesome");

// Replace the document with the updated content, and the document's CAS value
// (which we'll cover in a moment)
match collection
    .replace(doc_id, value, ReplaceOptions::new().cas(get_result.cas()))
    .await
{
    Ok(_result) => {
        println!("Document replace successful");
    }
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::CasMismatch => {
            println!("Could not write as another agent has concurrently modified the document");
        }
        _ => println!("Error: {e}"),
    },
}
```

There's a couple of things to cover with the `replace` line.

First, most of the methods in the Rust SDK take option blocks that have sensible defaults. One of them, `cas`, is provided here. We'll see more throughout this document.

### [](#optimistic-locking)What is CAS?

CAS, or Compare and Swap, is a form of optimistic locking. Every document in Couchbase has a CAS value, and it's changed on every mutation. When you `get` a document you also get the document's CAS, and then when it's time to write the document, you send the same CAS back. If another agent has modified that document, the Couchbase Server can detect you've provided a now-outdated CAS, and return an error instead of mutating the document. This provides cheap, safe concurrency. See [this detailed description of CAS](concurrent-document-mutations.md) for further details.

In general, you'll want to provide a CAS value whenever you `replace` a document, to prevent overwriting another agent's mutations.

### [](#retrying-on-cas-failures)Retrying on CAS Failures

But if we get a CAS mismatch, we usually just want to retry the operation. Let's see a more advanced `replace` example that shows one way to handle this:

```rust
    let doc_id = "document-key";

    let doc = json!({"status": "great"});

    collection.insert(&doc_id, &doc, None).await?;

    let op = async || {
        let get_result = collection.get(doc_id, None).await?;
        let mut value: serde_json::Value = get_result.content_as()?;
        value["status"] = json!("awesome");

        collection
            .replace(doc_id, value, ReplaceOptions::new().cas(get_result.cas()))
            .await
    };

    // Send our lambda to retryOnCASMismatch to take care of retrying it
    // For space reasons, error-handling of r is left out
    retry_on_cas_mismatch(op).await?;

    Ok(())
}

async fn retry_on_cas_mismatch<Fut>(
    operation: impl Fn() -> Fut,
) -> Result<MutationResult, ExamplesError>
where
    Fut: Future<Output = Result<MutationResult, couchbase::error::Error>>,
{
    loop {
        match operation().await {
            Ok(result) => return Ok(result),
            Err(e) => match e.kind() {
                couchbase::error::ErrorKind::CasMismatch => {
                    continue;
                }
                _ => {
                    return Err(ExamplesError::from(e));
                }
            },
        };
    }
}
```

## [](#removing)Removing

Removing a document is straightforward:

```rust
match collection.remove("document-key", None).await {
    Ok(_result) => {
        println!("Document remove successful");
    }
    Err(e) => {
        println!("Error: {e}");
    }
}
```

## [](#sub-document-operations)Sub-Document Operations

All of the operations seen so far involve fetching the complete document.

As an optimization the application may consider using the [Sub-Document API](subdocument-operations.md) to access or mutate specific parts of a document.

## [](#custom-structs)Custom structs

So far we've used JSON directly with `Value`, but it can be very useful to deal with Rust structs instead. The SDK operations will accept any type that implements `Serialize` for mutations, and any type that implements `DeserializeOwned` for retrievals.

## [](#durability)Durability

Writes in Couchbase are written initially to a single active node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas.

The optional `durability_level` parameter, which all mutating operations accept, allows the application to wait until this replication is successful before proceeding.

It can be used like this:

```rust
match collection
    .remove(
        "document-key",
        couchbase::options::kv_options::RemoveOptions::new()
            .durability_level(DurabilityLevel::MAJORITY),
    )
    .await
{
    Ok(_result) => {
        println!("Document remove successful");
    }
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::DocumentNotFound => {
            println!("Document not found");
        }
        _ => println!("Error: {e}"),
    },
}
```

The default is to run without durability, in which the SDK will return as soon as Couchbase Server has the mutation available in-memory on the active node. This is the default for a reason: it's the fastest mode, and the majority of the time is all the application needs.

However, we recognize that there are times when the application needs that extra certainty that especially vital mutations have been successfully replicated, and the other durability options provide the means to achieve this.

The options differ depend on what Couchbase Server version is in use. If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

`MAJORITY` — The server will ensure that the change is available in memory on the majority of configured replicas.

`MAJORITY_AND_PERSIST_TO_MAJORITY` — Majority level, plus persisted to disk on the active node.

`PERSIST_TO_MAJORITY` — Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of failure-resistance. Note that nothing comes for free — for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

## [](#expirationttl)Expiration/TTL

Couchbase Server includes an option to have particular documents automatically expire after a set time. This can be useful for some use-cases, such as user sessions, caches, or other temporary documents.

You can set an expiration value when creating a document:

```rust
let doc = json!({
        "foo": "bar",
        "baz": "qux",
});

collection
    .insert(
        "document-key",
        doc,
        InsertOptions::new().expiry(Duration::from_secs(10)),
    )
    .await?;
```

When getting a document, the expiry is not provided automatically by Couchbase Server but it can be requested:

```rust
let result = collection
    .get("document-key", GetOptions::new().expiry(true))
    .await?;

if let Some(expiry) = result.expiry_time() {
    println!("Document expires at {expiry}");
} else {
    println!("Document does not have an expiry");
}
```

Note that when updating the document, special care must be taken to avoid resetting the expiry to zero. Here's how:

```rust
let doc_id = "document-key";

let doc = json!({"status": "great"});

collection
    .replace(doc_id, doc, ReplaceOptions::new().preserve_expiry(true))
    .await?;
```

Some applications may find `getAndTouch` useful, which fetches a document while updating its expiry field. It can be used like this:

```rust
let result = collection
    .get_and_touch("document-key", Duration::from_secs(60 * 4), None)
    .await?;
```

## [](#atomic-counter-operations)Atomic Counter Operations

To support counter use-cases, a Couchbase document can be treated as an integer counter and adjusted or created atomically like this:

```rust
let counter_doc_id = "counter-doc";
// Increment by 1, creating doc if needed
collection.binary().increment(&counter_doc_id, None).await?;
// Decrement by 1
collection.binary().decrement(&counter_doc_id, None).await?;
// Increment by 5
collection
    .binary()
    .increment(&counter_doc_id, IncrementOptions::new().delta(5))
    .await?;
```

Note that a counter cannot be below 0.

> [!NOTE]
> Increment & Decrement are considered part of the 'binary' API and as such may still be subject to change

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements — see the [Sub-Document](subdocument-operations.md) pages.

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitrary bytes, or binary format](../concept-docs/nonjson.md).

Our [Query Engine](sqlpp-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).