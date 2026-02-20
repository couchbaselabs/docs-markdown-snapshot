---
title: Handling Errors
description: Errors are inevitable. C&#43;&#43; offers several flexible
  approaches to handling them.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.1/modules/howtos/pages/error-handling.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.1@cxx-sdk:howtos:error-handling.adoc[]
---

[View original HTML](/cxx-sdk/1.1/howtos/error-handling.html)

# Handling Errors

> Errors are inevitable. C++ offers several flexible approaches to handling them. 

The developer’s job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

As covered [here](concurrent-async-apis.md), the C++ SDK ships with two different APIs, allowing you to structure your application the way you want. That guide also covers how errors are actually returned and handled, so this document will focus instead on specific errors, along with a broader look at error handling strategies.

Operations in the C++ SDK do not throw exceptions, instead, every operation returns a `couchbase::error`, that evaluates to `true` if an error occurred.

Each error contains a `std::error_code`, that can be fetched using `couchbase::error::ec()`, providing an easy way to handle anything that goes wrong.

## [](#key-value-errors)Key-Value Errors

The KV Service exposes several common error codes that can be encountered - both during development, and to be handled by the production app. Here we will cover some of the most common errors.

If a particular key cannot be found it returns a `couchbase::errc::key_value::document_not_found` error code:

```c++
auto content = tao::json::value{
        { "foo", "bar" },
        { "baz", "qux" },
};
auto [err, res] = collection.replace("does-not-exist", content).get();

if (err.ec() == couchbase::errc::key_value::document_not_found) {
    fmt::println("Key not found - full error: {}", err);
} else if (err) {
    fmt::println("Some other error happened: {}", err);
} else {
    fmt::println("Operation succeeded");
}
```

```c++
auto [err, res] = collection.get("does-not-exist").get();

if (err.ec() == couchbase::errc::key_value::document_not_found) {
    fmt::println("Key not found - full error: {}", err);
} else if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Operation succeeded");
}
```

On the other hand if the key already exists and should not (e.g. on an insert) then it returns a `couchbase::errc::key_value::document_exists` error code:

```c++
auto [err, res] = collection.get("does-not-exist").get();

if (err.ec() == couchbase::errc::key_value::document_not_found) {
    fmt::println("Key not found - full error: {}", err);
} else if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Operation succeeded");
}
```

### [](#concurrency)Concurrency

Couchbase provides optimistic concurrency using CAS ([Compare and Swap](concurrent-document-mutations.md)). Each document gets a CAS value on the server, which is changed on each mutation. When you get a document you automatically receive its CAS value. When replacing the document, if you provide that CAS the server can check that the document has not been concurrently modified by another agent in-between. If it has, it returns a `couchbase::errc::common::cas_mismatch` error code, and the most appropriate response is to simply retry it:

```c++
for (int i = 0; i < 3; i++) {
    auto [get_err, get_res] = collection.get(doc_id).get();
    if (get_err) {
        fmt::println("Got an error during get: {}", get_err);
    } else {
        auto [replace_err, replace_res] = collection.replace(doc_id, new_json, couchbase::replace_options().cas(get_res.cas())).get();
        if (replace_err.ec() == couchbase::errc::common::cas_mismatch) {
            continue; // Try again
        } else if (replace_err) {
            fmt::println("Error: {}", replace_err);
            break;
        } else {
            fmt::println("Success");
            break;
        }
    }
}
```

### [](#ambiguity)Ambiguity

There are situations with any distributed system in which it is simply impossible to know for sure if the operation completed successfully or not. Take this as an example: your application requests that a new document be created on Couchbase Server. This completes, but, just before the server can notify the client that it was successful, a network switch dies and the application’s connection to the server is lost. The client will timeout waiting for a response and will return a `couchbase::errc::common::ambiguous_timeout` error code, but it’s ambiguous to the app whether the operation succeeded or not.

Another ambiguous error code is `couchbase::errc::key_value::durability_ambiguous`, which can returned when performing a durable operation. This similarly indicates that the operation may or may not have succeeded — though when using durability you are guaranteed that the operation will either have been applied to all replicas, or none.

Given the inevitability of ambiguity, how is the application supposed to handle this?

It really needs to be considered case-by-case, but the general strategy is to become certain if the operation succeeded or not, and to retry it if required.

For instance, for inserts, they can simply be retried to see if they fail with `couchbase::errc::key_value::document_exists`, in which case the operation was successful:

```c++
std::string
do_insert(const couchbase::collection& collection, const std::string& doc_id, int max_retries = 10)
{
    auto json = tao::json::value{
            { "foo", "bar" },
            { "baz", "qux" },
    };
    for (int attempt = 0; attempt < max_retries; attempt++) {
        auto options = couchbase::insert_options().durability(couchbase::durability_level::majority);
        auto [err, res] = collection.insert(doc_id, json, options).get();

        if (err.ec() == couchbase::errc::key_value::document_exists) {
            // The logic here is that if we failed to insert on the first attempt then
            // it's a true error, otherwise we retried due to an ambiguous error, and
            // the operation was actually successful
            if (attempt == 0) {
                return "failure";
            }
            return "success";
        } else if (err.ec() == couchbase::errc::key_value::durability_ambiguous ||
                   err.ec() == couchbase::errc::common::ambiguous_timeout) {
            // For ambiguous errors on inserts, simply retry them
            continue;
        } else if (err) {
            // Some other non-ambiguous error occurred
            return "failure";
        } else {
            // No error
            return "success";
        }
    }
    // Maxed-out retry attempts
    return "failure";
}
```

That example is much closer to what an application will want to be doing. Let’s flesh it out further.

### [](#real-world-error-handling)Real-World Error Handling

The application can write wrappers so that it can easily do operations without having to duplicate the error handling each time. Something like this:

```c++
std::string
do_insert(const couchbase::collection& collection,
               const std::string& doc_id,
               int max_retries = 10,
               std::chrono::milliseconds delay = std::chrono::milliseconds(5))
{
    auto json = tao::json::value{
            { "foo", "bar" },
            { "baz", "qux" },
    };
    for (int attempt = 0; attempt < max_retries; attempt++) {
        auto options = couchbase::insert_options().durability(couchbase::durability_level::majority);
        auto [err, res] = collection.insert(doc_id, json, options).get();

        if (err.ec() == couchbase::errc::key_value::document_exists) {
            // The logic here is that if we failed to insert on the first attempt then
            // it's a true error, otherwise we retried due to an ambiguous error, and
            // the operation was actually successful
            if (attempt == 0) {
                return "failure";
            }
            return "success";
        } else if (
                   // Ambiguous errors.  The operation may or may not have succeeded.  For inserts,
                   // the insert can be retried, and a DocumentExistsException indicates it was
                   // successful
                   err.ec() == couchbase::errc::key_value::durability_ambiguous ||
                   err.ec() == couchbase::errc::common::ambiguous_timeout ||
                   // Temporary/transient errors that are likely to be resolved
                   // on a retry.
                   err.ec() == couchbase::errc::common::temporary_failure ||
                   err.ec() == couchbase::errc::key_value::durable_write_in_progress ||
                   err.ec() == couchbase::errc::key_value::durable_write_re_commit_in_progress ||
                   // These transient errors won't be returned on an insert, but can be used
                   // when writing similar wrappers for other mutation operations.
                   err.ec() == couchbase::errc::common::cas_mismatch) {
            // Retry the operation after a sleep (which increases on each failure),
            // to avoid potentially further overloading an already failing server.
            std::this_thread::sleep_for(delay *= 2);
            continue;
        } else if (err) {
            // Some other non-ambiguous & non-transient error occurred
            return "failure";
        } else {
            // No error
            return "success";
        }
    }
    // Maxed-out retry attempts
    return "failure";
}
```

This will make a 'best effort' to do the insert (though its retry strategy is rather naïve, and applications may want to implement a more sophisticated approach involving exponential backoff and circuit breaking.)

If that best effort fails, and the `do_insert` call still returns a "failure", then it’s highly context-dependent how to handle that. Examples would include displaying a "please try again later" error to a user, if there is one, and logging it for manual human review. The application must make a suitable call for each case.

The application can write similar wrappers for the other operations — replace, upsert, _et al_. Note that the logic is a little different in each case: for inserts, we confirm if the operation has already been successful on an ambiguous result by checking for `couchbase::errc::key_value::document_exists`But this wouldn’t make sense for an upsert.

### [](#idempotent-and-non-idempotent-operations)Idempotent and Non-Idempotent Operations

> [!TIP]
> Idempotent operations are those that can be applied multiple times and only have one effect. Repeatedly setting an email field is idempotent — increasing a counter by one is not.

Some operations we can view as idempotent as they will fail with no effect after the first success — such as inserts.

Idempotent operations are much easier to handle, as on ambiguous error results (`couchbase::errc::key_value::durability_ambiguous` and `couchbase::errc::common::ambiguous_timeout`) the operation can simply be retried.

Most key-value operations are idempotent. For those that aren’t, such as a Sub-Document `array_append` call, or a counter increment, the application should, on an ambiguous result, first read the document to see if that change was applied.

## [](#query-and-analytics-errors)Query and Analytics Errors

A SQL++ (formerly N1QL) query returns a `couchbase::error` and `couchbase::query_result`, like so:

```c++
std::string statement = "SELECT * from `travel-sample` LIMIT 10;";
auto [err, res] = cluster.query(statement, {}).get();

if (err) {
    fmt::println("Error: {}", err);
} else {
    // Do something with the result
}
```

Analytics works in an identical fashion, returning a `couchbase::error` and `couchbase::analytics_result`.

## [](#additional-resources)Additional Resources

Error handling is an expansive topic. Here, we have covered examples of the kinds of exception scenarios that you are most likely to face. More fundamentally, you also need to weigh up [concepts of durability](../concept-docs/durability-replication-failure-considerations.md).

Diagnostic methods are available to check on the [health of the cluster](health-check.md), and the [health of the network](tracing-from-the-sdk.md).

Logging methods are dependent upon the platform and SDK used. We offer [recommendations and practical examples](collecting-information-and-logging.md).

We have a [listing of error messages](../ref/error-codes.md), with some pointers to what to do when you encounter them.