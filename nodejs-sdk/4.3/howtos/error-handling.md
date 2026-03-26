---
title: Handling Errors
description: Errors are inevitable. The developer’s job is to be prepared for
  whatever is likely to come up
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/howtos/pages/error-handling.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.3@nodejs-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/howtos/error-handling.html)

# Handling Errors

> Errors are inevitable. The developer's job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. 

Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

## [](#handling-errors)Handling Errors

The Node.js SDK works directly with the built in exception handling available in Javascript. This enables you to catch, interrogate, and handle or log them and continue. Depending on the type of the exception you catch, there are a number of properties which will be available to you.

```javascript
try {
  var result = await collection.get(docKey);
} catch (e) {
  // we can handle any exceptions thrown here.
}
```

## [](#key-value-errors)Key-Value Errors

The KV Service exposes several common errors that can be encountered — both during development, and to be handled by the production app. Here we will cover some of the most common errors.

If a particular key cannot be found it is return as a `DocumentNotFoundError`:

```javascript
try {
  var result = await collection.get("key-which-does-not-exist");
} catch (e) {
  if (e instanceof couchbase.DocumentNotFoundError) {
    console.log("the document is missing")
  }
}
```

On the other hand if the key already exists and should not (e.g. on an insert) then it is returned as a `DocumentExistsError`:

```javascript
try {
  var result = await collection.insert("key-which-exists", "hello");
} catch (e) {
  if (e instanceof couchbase.DocumentExistsError) {
    console.log("document unexpectedly exists")
  }
}
```

### [](#concurrency)Concurrency

Couchbase provides optimistic concurrency using [CAS](concurrent-document-mutations.md). Each document gets a CAS value on the server, which is changed on each mutation. When you get a document you automatically receive its CAS value, and when replacing the document, if you provide that CAS the server can check that the document has not been concurrently modified by another agent. If it has, it returns `CasMismatchError`, and the most appropriate response is to simply retry it:

```javascript
  for (var retryNum = 0; retryNum < 10; ++i) {
    try {
      var result = await collection.get(docKey);

      var airport = result.value;
      airport.views++;

      await collection.replace(docKey, airport, { cas: result.cas });

      // success!
      break;
    } catch (e) {
      if (e instanceof couchbase.CasMismatchError) {
        console.log("CAS mismatch")
        // We could now re-fetch the document and try again
        continue;
      }

      // if we ran into another kind of error, let's re-throw it...
      throw e;
    }
  }
```

### [](#ambiguity)Ambiguity

There are situations with any distributed system in which it is simply impossible to know for sure if the operation completed successfully or not. For example, your application requests that a new document be created on Couchbase Server. This completes, but, just before the server can notify the client that it was successful, a network switch dies and the application's connection to the server is lost. The client will timeout waiting for a response and will raise a `TimeoutError`, but it's ambiguous to the app whether the operation succeeded or not.

`TimeoutError` is one ambiguous error; another is `DurabilityAmbiguousError`, which can returned when performing a durable operation. This similarly indicates that the operation may or may not have succeeded: though when using durability you are guaranteed that the operation will either have been applied to all replicas, or none.

#### [](#given-the-inevitability-of-ambiguity-how-is-the-application-supposed-to-handle-this)Given the inevitability of ambiguity, how is the application supposed to handle this?

This needs to be considered case-by-case, but the general strategy is to become certain if the operation succeeded or not, and to retry it if required.

For instance, for inserts, they can simply be retried to see if they fail on `DocumentExistsError`, in which case the operation was successful:

```javascript
  for (var retryNum = 0; retryNum < 10; ++i) {
    try {
      var result = await collection.insert(docKey, "some value", {
        durabilityLevel: couchbase.DurabilityLevel.PersistToMajority,
      });

      // success!
      break;
    } catch (e) {
      if (e instanceof couchbase.DocumentExistsError) {
        if (retryNum > 0) {
          // If this is a retry and the document now exists, we can assume it was
          // written successfully by a previously ambiguous error.
          continue;
        }
      }
      if (e instanceof couchbase.DurabilityAmbiguousError) {
        // we can simply try the durable operation again...
        continue;
      }

      // if we ran into another kind of error, let's re-throw it...
      throw e;
    }
  }
```

That example is much closer to what an application will want to be doing. Let's flesh it out further.

### [](#non-idempotent-operations)Non-Idempotent Operations

Idempotent operations are those that can be applied multiple times yet still have the one, same effect. Repeatedly setting an email field is idempotent — increasing a counter by one is not.

Some operations we can view as idempotent as they will fail with no effect after the first success — such as inserts.

Idempotent operations are much easier to handle, as on ambiguous error results (`DurabilityAmbiguousError` and `TimeoutError`) the operation can simply be retried.

Most key-value operations are idempotent. For those that are not, such as a Sub-Document `arrayAppend` call, or a counter increment, the application should, on an ambiguous result, first read the document to see if that change was applied.

## [](#query-and-analytics-errors)Query and Analytics Errors

A SQL++ (formerly N1QL) query either returns results or will throw an error with a `QueryErrorContext`, like so:

```javascript
  try {
    var results = cluster.query("SELECT * FROM `travel-sample`");
  } catch (e) {
    if (e instanceof couchbase.IndexFailureError) {
      console.log("index doesn't exist, do we need to create it")
    }

    if (e.context instanceof couchbase.QueryErrorContext) {
      // We have a SQL++ (N1QL) error context, we can print out some useful information:
      console.log(e.context.statement);
      console.log(e.context.first_error_code);
      console.log(e.context.first_error_message);
      console.log(e.context.client_context_id);
      console.log(e.context.http_response_code);
      console.log(e.context.http_response_body);
    }
  }
```

Analytics works in an identical fashion, potentially raising an analytics specific error and having an `AnalyticsErrorContext`.

## [](#additional-resources)Additional Resources

Errors & Exception handling is an expansive topic. Here, we have covered examples of the kinds of exception scenarios that you are most likely to face. More fundamentally, you also need to weigh up [concepts of durability](../concept-docs/durability-replication-failure-considerations.md).

Logging methods are dependent upon the platform and SDK used. We offer [recommendations and practical examples](collecting-information-and-logging.md).