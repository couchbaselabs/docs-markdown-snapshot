---
title: Async &amp; Reactive APIs
description: The Rust SDK uses async/await via Tokio for all operations, giving
  you full control over concurrency and execution.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/concurrent-async-apis.adoc
  xref: xref:rust-sdk:howtos:concurrent-async-apis.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/concurrent-async-apis.html)

# Async &amp; Reactive APIs

> The Rust SDK uses async/await via Tokio for all operations, giving you full control over concurrency and execution. 

The Couchbase Rust SDK is fully asynchronous. All operations return `Future`s and must be `.await`ed within an async context. The SDK is built on top of [Tokio](https://tokio.rs), a popular async runtime for Rust.

To get started, you will need a Tokio runtime. The most common approach is to annotate your `main` function with `#[tokio::main]`:

```rust
#[tokio::main]
async fn main() {
    let cluster = Cluster::connect(
        "couchbase://localhost",
        ClusterOptions::new(Authenticator::PasswordAuthenticator(
            PasswordAuthenticator::new("username", "password"),
        )),
    )
        .await
        .unwrap();

    let bucket = cluster.bucket("travel-sample");
    let collection = bucket.default_collection();

    let result = collection.get("airline_10", None).await.unwrap();
    println!("Got document: {:?}", result.content_as::<serde_json::Value>());
}
```

## [](#futures-and-awaiting)Futures and Awaiting

Every SDK operation returns a `Future`. You must `.await` the future to drive it to completion. Unawaited futures do nothing — Rust's ownership model ensures you are aware of this at compile time.

```rust
let result = collection.get("airline_10", None).await?;
let content = result.content_as::<serde_json::Value>()?;
println!("Got document: {content}");
```

## [](#concurrent-operations)Concurrent Operations

A common pattern is to fire off multiple independent operations concurrently, rather than awaiting them one at a time. This can significantly reduce latency when operations are not dependent on each other.

### [](#using-join)Using `join!`

The `tokio::join!` macro awaits multiple futures concurrently and returns all of their results. Use this when you have a fixed, known set of operations:

```rust
let (get_result, upsert_result) = tokio::join!(
    collection.get("airline_10", None),
    collection.upsert("airline_10", json!({"type": "airline", "name": "40-Mile Air"}), None),
);

match get_result {
    Ok(doc) => println!("Got: {:?}", doc.content_as::<serde_json::Value>()),
    Err(e) => println!("Get failed: {e}"),
}
match upsert_result {
    Ok(_) => println!("Upsert succeeded"),
    Err(e) => println!("Upsert failed: {e}"),
}
```

### [](#using-join%5Fall)Using `join_all`

When you have a dynamic collection of futures (e.g. built from an iterator), use `futures::future::join_all`. Because the futures are stored in a collection, they must all have the same return type:

```rust
let keys = vec!["airline_10", "airline_10123", "airline_10226"];

let futures = keys
    .iter()
    .map(|key| collection.get(*key, None));

let results = join_all(futures).await;

for (key, result) in keys.iter().zip(results) {
    match result {
        Ok(doc) => println!("{key}: {:?}", doc.content_as::<serde_json::Value>()),
        Err(e) => println!("{key}: error — {e}"),
    }
}
```

Note that `join_all` waits for **all** futures to complete, even if some fail. Each result must be checked individually.

### [](#using-futuresunordered)Using `FuturesUnordered`

For more fine-grained control, such as processing results as they arrive, use `FuturesUnordered` from the `futures` crate:

```rust
let keys = vec!["airline_10", "airline_10123", "airline_10226"];

let mut unordered: FuturesUnordered<_> = keys
    .iter()
    .map(|key| {
        let col = collection.clone();
        async move { (*key, col.get(*key, None).await) }
    })
    .collect();

while let Some((key, result)) = unordered.next().await {
    match result {
        Ok(doc) => println!("{key}: {:?}", doc.content_as::<serde_json::Value>()),
        Err(e) => println!("{key}: error — {e}"),
    }
}
```

This is particularly useful when you want to act on the first available result without waiting for slower operations.

## [](#spawning-tasks)Spawning Tasks

To run operations truly in the background (detached from the current async task), use `tokio::spawn`. This is useful for fire-and-forget workloads or background processing:

```rust
// SDK handles are Clone, so you can clone the handle and move the clone into the task.
let col = collection.clone();
let handle = tokio::spawn(async move {
    col.upsert("background-key", json!({"processed": true}), None)
        .await
});

// Do other work concurrently while the task runs in the background...
collection.get("some-other-key", None).await?;

match handle.await {
    Ok(Ok(_)) => println!("Background upsert succeeded"),
    Ok(Err(e)) => println!("Background upsert failed: {e}"),
    Err(e) => println!("Task panicked: {e}"),
}
```

## [](#error-handling-in-concurrent-contexts)Error Handling in Concurrent Contexts

When running multiple operations concurrently, each operation returns its own `Result`. You should handle errors per-operation rather than assuming all will succeed:

```rust
let keys = vec!["airline_10", "airline_does_not_exist", "airline_10226"];

let futures = keys.iter().map(|key| collection.get(*key, None));
let results = join_all(futures).await;

for (key, result) in keys.iter().zip(results) {
    match result {
        Ok(doc) => println!("{key}: {:?}", doc.content_as::<serde_json::Value>()),
        Err(e) => println!("{key}: {e}"),
    }
}
```

If you want to short-circuit on the first error, consider `try_join!` from the `tokio` crate:

```rust
// try_join! returns early with the first error it encounters.
// Here the second key does not exist, so the whole expression returns
// a not-found error without waiting for any remaining futures.
match tokio::try_join!(
    collection.get("airline_10", None),
    collection.get("airline_does_not_exist", None),
) {
    Ok((first, second)) => {
        println!("First: {:?}", first.content_as::<serde_json::Value>());
        println!("Second: {:?}", second.content_as::<serde_json::Value>());
    }
    Err(e) => println!("One of the operations failed, aborting: {e}"),
}
```

## [](#timeouts)Timeouts

The Rust SDK does not have per-operation timeout options. Instead, wrap any future with `tokio::time::timeout` to apply a deadline. If the deadline is exceeded, the future is cancelled and a `tokio::time::error::Elapsed` error is returned:

```rust
let result = tokio::time::timeout(
    Duration::from_millis(200),
    collection.get("airline_10", None),
)
    .await;

match result {
    Ok(Ok(doc)) => println!("Got: {:?}", doc.content_as::<serde_json::Value>()),
    Ok(Err(e)) => println!("Operation error: {e}"),
    Err(_elapsed) => println!("Operation timed out after 200ms"),
}
```

> [!NOTE]
> When a `Future` wrapping an in-flight SDK operation is cancelled (e.g. by `tokio::time::timeout`), the SDK may still receive a response from the server for that operation. These are reported as _orphaned responses_ and can be useful for diagnosing timeout issues. See [Orphaned Requests Logging](observability-orphan-logger.md) for details.

## [](#batching-with-worker-pools)Batching with Worker Pools

The Rust SDK is designed to work efficiently across many concurrent async tasks, all sharing the same SDK handles. Because `Cluster`, `Bucket`, and `Collection` are all cheaply cloneable, you can pass them freely into `tokio::spawn`ed tasks without any synchronisation overhead.

In the following example we load data from one of the Couchbase sample datasets. This sample looks for the dataset in the default location for a Linux install; you can find the default locations for other operating systems in the [CLI reference](../../../server/current/cli/cli-intro.md).

First, connect to the cluster and obtain a collection handle:

```rust
let username = "<your-username>";
let password = "<your-password>";
let bucket_name = "travel-sample";

let cluster = tokio::time::timeout(
    Duration::from_secs(60),
    Cluster::connect(
        // For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
        "couchbase://localhost",
        ClusterOptions::new(Authenticator::PasswordAuthenticator(
            PasswordAuthenticator::new(username, password),
        )),
    ),
)
    .await.unwrap()?; // Unwrapping for brevity; handle errors as appropriate in production code.

let bucket = cluster.bucket(bucket_name);

tokio::time::timeout(Duration::from_secs(30), bucket.wait_until_ready(None)).await.unwrap()?;

let collection = bucket.default_collection();
```

Next, create a bounded channel and spawn a fixed pool of worker tasks. `crossfire::mpmc` receivers are cloneable, so each worker gets its own clone and pulls work independently. The bounded capacity means sending blocks when all workers are busy, naturally throttling the loader:

```rust
// We'll create 24 worker tasks and a channel with space for a maximum of 1 item per task.
// Writing to the channel will block if there are no tasks ready to pick up an item.
let num_workers = 24;
let (task_sender, task_receiver) =
    crossfire::mpmc::bounded_async::<(String, serde_json::Value)>(num_workers);

let workers: Vec<_> = (0..num_workers)
    .map(|_| {
        let collection = collection.clone();
        let receiver = task_receiver.clone();
        tokio::spawn(async move {
            while let Ok((doc_id, value)) = receiver.recv().await {
                if let Err(e) = collection.upsert(doc_id, value, None).await {
                    eprintln!("Upsert failed: {e}");
                }
            }
        })
    })
    .collect();
```

Iterate the sample zip and send each JSON document into the channel:

```rust
let sample_path = format!("/opt/couchbase/samples/{bucket_name}.zip");

// unwrap used for brevity; handle errors as appropriate in production code.
let mut archive =
    zip::ZipArchive::new(std::fs::File::open(sample_path).unwrap()).unwrap();

for i in 0..archive.len() {
    let mut file = archive.by_index(i).unwrap();

    let file_name = file.name().to_string();

    // We only want JSON files from the docs directory.
    if file.is_dir()
        || !(file_name.starts_with(&format!("{bucket_name}/docs/"))
        && file_name.ends_with(".json"))
    {
        continue;
    }

    let mut content = String::new();
    std::io::Read::read_to_string(&mut file, &mut content).unwrap();
    let doc_content: serde_json::Value = serde_json::from_str(&content).unwrap();

    task_sender.send((file_name, doc_content)).await.unwrap();
}
```

Finally, drop the sender so workers exit their receive loop once the queue drains, then wait for all tasks to complete:

```rust
drop(task_sender);

futures::future::join_all(workers)
    .await
    .into_iter()
    .collect::<Result<Vec<_>, _>>()
    .unwrap();
```

## [](#additional-resources)Additional Resources

* [Handling Errors](error-handling.md) — covers `Result`, retries, and ambiguity.
* [Tokio Tutorial](https://tokio.rs/tokio/tutorial) — in-depth guide to the async runtime used by the SDK.