---
title: Handling Errors
description: Errors are inevitable. Rust offers several flexible approaches to
  handling them.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/error-handling.adoc
  xref: xref:rust-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/error-handling.html)

# Handling Errors

> Errors are inevitable. Rust offers several flexible approaches to handling them. 

The developer's job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

See the [async page](concurrent-async-apis.md#error-handling-in-concurrent-contexts) for information on error handling in concurrent contexts.

## [](#error-model)Error Model

The Rust SDK tries to make handling errors as easy as possible, whilst also attaching as much useful information as possible to the error to aid in debugging. Errors are a wrapper around a accessible `ErrorKind` enum, and an opaque `ErrorContext`. The `ErrorKind` is large enum containing a wide variety of error types, but most likely you will only want to handle a subset of them based on your requirements.

## [](#key-value-errors)Key-Value Errors

The KV Service exposes several common errors that can be encountered - both during development, and to be handled by the production app. Here we will cover some of the most common errors.

If a particular key cannot be found it is returned as a `DocumentNotFound`:

```rust
let doc = json!({
        "foo": "bar",
        "baz": "qux",
});

match collection.replace("does-not-exist", doc, None).await {
    Ok(_result) => {
        println!("Document upsert successful");
    }
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::DocumentNotFound => {
            println!("Document not found");
        }
        _ => println!("Error: {e}"),
    },
}
```

```rust
match collection.get("does-not-exist", None).await {
    Ok(_result) => {
        println!("Document get successful");
    }
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::DocumentNotFound => {
            println!("Document not found");
        }
        _ => println!("Error: {e}"),
    },
}
```

On the other hand if the key already exists and should not (e.g. on an insert) then it is raised as a `DocumentExists`:

```rust
let doc = json!({
        "foo": "bar",
        "baz": "qux",
});

match collection.insert("does-already-exist", doc, None).await {
    Ok(_result) => {
        println!("Document upsert successful");
    }
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::DocumentExists => {
            println!("Document exists");
        }
        _ => println!("Error: {e}"),
    },
}
```

### [](#concurrency)Concurrency

Couchbase provides optimistic concurrency using CAS ([Compare and Swap](concurrent-document-mutations.md)). Each document gets a CAS value on the server, which is changed on each mutation. When you get a document you automatically receive its CAS value. When replacing the document, if you provide that CAS the server can check that the document has not been concurrently modified by another agent in-between. If it has, it returns `CasMismatch`, and the most appropriate response is to simply retry it:

```rust
let mut guard = 3;
let new_json = json!({"foo": "bar"});

let doc = collection.get("doc", None).await?;
match collection
    .replace("doc", &new_json, ReplaceOptions::new().cas(doc.cas()))
    .await
{
    Ok(_result) => {
        println!("Document replace successful");
        return Ok(());
    }
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::CasMismatch => {
            guard -= 1;
            if guard > 0 {
                println!("CAS mismatch, retry up to {guard} times");
            } else {
                return Err(ExamplesError::from(e));
            }
        }
        _ => {
            println!("Error: {e}");
            return Err(ExamplesError::from(e));
        }
    },
};
```

### [](#ambiguity)Ambiguity

There are situations with any distributed system in which it is simply impossible to know for sure if the operation completed successfully or not. Take this as an example: your application requests that a new document be created on Couchbase Server. This completes, but, just before the server can notify the client that it was successful, a network switch dies and the application's connection to the server is lost. The application can drop the operation future, but it's ambiguous to the app whether the operation succeeded or not.

Another ambiguous error is `DurabilityAmbiguous`, which can returned when performing a durable operation. This similarly indicates that the operation may or may not have succeeded — though when using durability you are guaranteed that the operation will either have been applied to all replicas, or none.

Given the inevitability of ambiguity, how is the application supposed to handle this?

It really needs to be considered case-by-case, but the general strategy is to become certain if the operation succeeded or not, and to retry it if required.

For instance, for inserts, they can simply be retried to see if they fail on `DocumentExists`, in which case the operation was successful:

```rust
let mut guard = 3;
let doc = json!({"foo": "bar"});

loop {
    let result = collection
        .insert(
            "doc-id",
            &doc,
            InsertOptions::new().durability_level(DurabilityLevel::MAJORITY),
        )
        .await;

    match result {
        Ok(_result) => {
            println!("Document insert successful");
            return Ok(());
        }
        Err(e) => match e.kind() {
            couchbase::error::ErrorKind::DurabilityAmbiguous => {
                // For ambiguous errors on inserts, simply retry them.
                guard -= 1;
                if guard > 0 {
                    println!("Durability ambiguous, retry up to {guard} times");
                } else {
                    return Err(ExamplesError::from(e));
                }
            }
            couchbase::error::ErrorKind::DocumentExists => {
                // The logic here is that if we failed to insert on the first attempt then
                // it's a true error, otherwise we retried due to an ambiguous error, and
                // it's ok to continue as the operation was actually successful.
                println!("Document insert successful");
                return Ok(());
            }
            _ => {
                println!("Error: {e}");
                return Err(ExamplesError::from(e));
            }
        },
    }
}
```

That example is much closer to what an application will want to be doing. Let's flesh it out further.

### [](#real-world-error-handling)Real-World Error Handling

The application can write wrappers so that it can easily do operations without having to duplicate the error handling each time. Something like this:

```rust
let initial_guard = 3;
let base_delay = Duration::from_millis(10);
let mut current_backoff_factor = 1;
let mut guard = initial_guard;
let doc = json!({
        "foo": "bar",
        "baz": "qux",
});
let doc_id = "document-key";

loop {
    let result = timeout(
        Duration::from_millis(2500),
        collection.insert(
            &doc_id,
            &doc,
            InsertOptions::new().durability_level(DurabilityLevel::MAJORITY),
        ),
    )
    .await;

    match result {
        Ok(_result) => {
            println!("Document insert successful");
            return Ok(());
        }
        Err(e) => match e.kind() {
            couchbase::error::ErrorKind::DocumentExists => {
                // The logic here is that if we failed to insert on the first attempt then
                // it's a true error, otherwise we retried due to an ambiguous error, and
                // it's ok to continue as the operation was actually successful.
                if guard == initial_guard {
                    return Err(ExamplesError::from(e));
                }

                println!("Document insert successful");
                return Ok(());
            }
            couchbase::error::ErrorKind::DurabilityAmbiguous
            // Temporary/transient errors that are likely to be resolved
            // on a retry
            | couchbase::error::ErrorKind::TemporaryFailure
            | couchbase::error::ErrorKind::DurabilityWriteInProgress
            | couchbase::error::ErrorKind::DurableWriteRecommitInProgress
            // These transient errors won't be returned on an insert, but can be used
            // when writing similar wrappers for other mutation operations
            | couchbase::error::ErrorKind::CasMismatch => {
                if guard > 0 {
                    tokio::time::sleep(base_delay * current_backoff_factor).await;
                    current_backoff_factor *= 2;
                    guard -= 1;
                    println!("Transient error, retry up to {guard} times");
                } else {
                    return Err(ExamplesError::from(e));
                }
            }
            _ => {
                println!("Error: {e}");
                return Err(ExamplesError::from(e));
            }
        },
    }
}
```

This will make a 'best effort' to do the insert (though its retry strategy is rather naïve, and applications may want to implement a more sophisticated approach involving exponential backoff and circuit breaking.)

If that best effort fails, and the `do_insert` call still returns a `Error`, then it's highly context-dependent how to handle that. Examples would include displaying a "please try again later" error to a user, if there is one, and logging it for manual human review. The application must make a suitable call for each case.

The application can write similar wrappers for the other operations — replace, upsert, _et al_. Note that the logic is a little different in each case: for inserts, we confirm if the operation has already been successful on an ambiguous result by checking for `DocumentExists`But this wouldn't make sense for an upsert.

### [](#idempotent-and-non-idempotent-operations)Idempotent and Non-Idempotent Operations

> [!TIP]
> Idempotent operations are those that can be applied multiple times and only have one effect. Repeatedly setting an email field is idempotent — increasing a counter by one is not.

Some operations we can view as idempotent as they will fail with no effect after the first success — such as inserts.

Idempotent operations are much easier to handle, as on ambiguous error results (`DurabilityAmbiguous` or timeouts) the operation can simply be retried.

Most key-value operations are idempotent. For those that aren't, such as a Sub-Document `array_append` call, or a counter increment, the application should, on an ambiguous result, first read the document to see if that change was applied.

## [](#customizing-the-retrystrategy)Customizing the RetryStrategy

A custom `RetryStrategy` can be provided on `ClusterOptions` (so it will take effect globally):

```rust
let opts = ClusterOptions::new(Authenticator::PasswordAuthenticator(
    PasswordAuthenticator::new("username".to_string(), "password".to_string()),
))
.default_retry_strategy(Arc::new(BestEffortRetryStrategy::new(
    ExponentialBackoffCalculator::default(),
)));
```

Or it can be applied on a per-request basis:

```rust
let opts = UpsertOptions::new().retry_strategy(Arc::new(BestEffortRetryStrategy::new(
    ExponentialBackoffCalculator::default(),
)));
```

Both approaches are valid, although we recommend for most use cases to stick with the defaults and only to override it on a per requests basis.

If you find yourself overriding every request with the same different strategy, it can make sense to apply it locally in order to DRY it up a bit. There are no performance differences with both approaches, but make sure that even if you pass in a custom one on every request that you do not create a new one each time but rather share it across calls.

```rust
let retry_strategy = Arc::new(BestEffortRetryStrategy::new(
    ExponentialBackoffCalculator::default(),
));
let opts = UpsertOptions::new().retry_strategy(retry_strategy.clone());
let opts2 = InsertOptions::new().retry_strategy(retry_strategy.clone());
```

While it is possible to implement the `RetryStrategy` from scratch, we **strongly recommend** that instead the `BestEffortRetryStrategy` is embedded and to only implement handling of specific `RetryReasons`.

In practice, it should look something like this:

```rust
#[derive(Debug)]
struct CustomRetryStrategy {
    base_strategy: BestEffortRetryStrategy<ExponentialBackoffCalculator>,
}

impl RetryStrategy for CustomRetryStrategy {
    fn retry_after(&self, request: &RetryRequest, reason: &RetryReason) -> Option<RetryAction> {
        match reason {
            RetryReason::KvLocked => {
                // Override the default and don't retry.
                None
            }
            _ => self.base_strategy.retry_after(request, reason),
        }
    }
}

let base_strategy = BestEffortRetryStrategy::new(ExponentialBackoffCalculator::default());

let retry_strategy = Arc::new(CustomRetryStrategy { base_strategy });
let opts = UpsertOptions::new().retry_strategy(retry_strategy.clone());
```

One important rule is that you should never block inside `should_retry`, since it is called on the hot code path and can considerably impact performance.

If you need to call out to third party systems over the network or the file system to make retry decisions, we recommend that you do this from a different thread and communicate via atomics, for example, so that the hot code path only needs to do cheap lookups.

The `RetryAction` indicates what should be done with the request: if you return `None`, the orchestrator will cancel the request, resulting in the underlying error being returned. The other option is to provide an action with `RetryAction::new(duration: Duration)`, indicating the duration when the request should be retried next. This allows you to customize not only _if_ a request should be retried, but also _when_.

> [!IMPORTANT]
> Not retrying operations is considered safe from a data-loss perspective. If you are changing the retry strategy of individual requests keep the semantics discussed in [Idempotent vs. Non-Idempotent Requests](#idempotent-and-non-idempotent-operations) in mind. You can check if a request is idempotent through the `is_idempotent()` function on `RetryRequest`, and also check if the `RetryReason` allows for non-idempotent retry through `allows_non_idempotent_retry()`. If in doubt, check the implementation of the `BestEffortRetryStrategy` for guidance.

## [](#query-and-analytics-errors)Query and Analytics Errors

A SQL++ (formerly N1QL) query either returns results or an error as the same way as KV, like so:

```rust
let statement = "SELECT * from `airport` LIMIT 10;";
match scope.query(statement, None).await {
    Ok(res) => {
        println!("Success!");
    }
    Err(e) => {
        println!("Query failed: {e}");
    }
};
```

## [](#additional-resources)Additional Resources

Errors & Exception handling is an expansive topic. Here, we have covered examples of the kinds of exception scenarios that you are most likely to face. More fundamentally, you also need to weigh up [concepts of durability](../concept-docs/durability-replication-failure-considerations.md).

Diagnostic methods are available to check on the [health of the cluster](health-check.md), and the [health of the network](observability-tracing.md).

Logging methods are dependent upon the platform and SDK used. We offer [recommendations and practical examples](collecting-information-and-logging.md).

We have a [listing of error messages](../ref/error-codes.md), with some pointers to what to do when you encounter them.