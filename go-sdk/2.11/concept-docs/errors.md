---
title: Errors and Diagnostics
description: When the unexpected happens, take a step-by-step approach.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/concept-docs/pages/errors.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.11@go-sdk:concept-docs:errors.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.11/concept-docs/errors.html)

# Errors and Diagnostics

> When the unexpected happens, take a step-by-step approach. 

## [](#general-approach-to-go-exceptions)General Approach to Go Exceptions

All Couchbase specific exceptions are derived from `CouchbaseException`. These unrecoverable errors are left to the application developer to handle — practical approaches to this are covered in our practical error handling doc. All the other Exception types used are part of the JDK, including `IllegalArgumentException`, `TimeoutException` and others.

See our [practical error handling docs](../howtos/error-handling.md) for some of the approaches to take.

## [](#durable-writes)Durable Writes

A durable write fails in the following situations:

1. _Server timeout exceeded_. The active node aborts the durable write, instructs all replica nodes also to abort the pending write, and informs the client that the durable write has had an ambiguous result. See [Handling Ambiguous Results](../../../server/current/learn/data/durability.md#handling-ambiguous-results), below.
2. _Replica node fails while SyncWrite is pending (that is, before the active node can identify whether the node hosted a replica)_. If enough alternative replica nodes can be identified, the durable write can proceed. Otherwise, the active node waits until a server-side timeout has expired; then aborts the durable write, and duly informs the client that the durable write has had an ambiguous result.
3. _Active node fails while SyncWrite is pending_. This disconnects the client, which must assume that the result of the durable write has proved ambiguous. If the active node is failed over, a replica is promoted from a replica node: depending on how advanced the durable write was at the time of active-node failure, the durable write may proceed.
4. _Write while SyncWrite is pending_. A client that attempts a durable or an asynchronous write on a key whose value is currently undergoing a durable write receives a `SYNC_WRITE_IN_PROGRESS` message, to indicate that the new write cannot currently proceed. The client may retry.

## [](#handling-ambiguous-results)Handling Ambiguous Results

Couchbase Server informs the client of an ambiguous result whenever Couchbase Server cannot confirm that an intended commit was successful. This situation may be caused by node-failure, network-failure, or timeout.

If a client receives notification of an ambiguous result, and the attempted durable write is _idempotent_, the durable write can be re-attempted. If the attempted durable write is _not_ idempotent, the options are:

* Verify the current state of the saved data; and re-attempt the durable write if appropriate.
* Return an error to the user.

Further discussion of handling ambiguous results can be found in our [Durability & Failure discussion](durability-replication-failure-considerations.md#ambiguity).

## [](#health-check)Health Check

Distributed systems are not easy to debug. One cause of errors to try to eliminate, or quickly diagnose to deal with, is those caused by the network. Our [Health Check API](health-check.md) offers status and diagnostics on your cluster's network, and can be used, for example, to diagnose network latencies that are behind timeout errors.

## [](#threshold-orphan-logging)Threshold & Orphan Logging

Observability is provided by the SDK in the following ways:

### [](#threshold-logging)Threshold Logging

Threshold logging is the recording of slow operations — useful for diagnosing when and where problems occur in a distributed environment. It is enabled by default.

You will see this information turning up in the logs something like this:

```json
Threshold Log: {"service":"kv","count":2,"top":[{"operation_name":"Insert","total_us":161679},{"operation_name":"Upsert","total_us":161451}]}
```

And as tracing values such as `total_us`, the duration of the total time taken for the operation, expressed as microseconds.

### [](#orphaned-response-reporting)Orphaned Response Reporting

Special reporting capabilities which explicitly collect information about responses which have been abandoned (i.e. timed out) at the time when the SDK tries to complete them. This is also enabled by default.