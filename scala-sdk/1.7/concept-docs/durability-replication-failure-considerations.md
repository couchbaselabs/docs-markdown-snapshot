---
title: Failure Considerations
description: Data durability refers to the fault tolerance and persistence of
  data in the face of software or hardware failure.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/1.7/modules/concept-docs/pages/durability-replication-failure-considerations.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:1.7@scala-sdk:concept-docs:durability-replication-failure-considerations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.7/concept-docs/durability-replication-failure-considerations.html)

# Failure Considerations

> Data durability refers to the fault tolerance and persistence of data in the face of software or hardware failure. Prepare your app for the inevitable challenges of working in a distributed network environment. 

Even the most reliable software and hardware might fail at some point, and along with the failures, introduce a chance of data loss. Couchbase's durability features include Synchronous Replication, and the possibility to use distributed, multi-document ACID transactions. It is the responsibility of the development team and the software architect to evaluate the best choice for each use case.

This page covers the durability options offered by Couchbase Server, with the rest of this section covering logging, health check, and observability — all key to understanding the health of a complex, distributed environment.

Couchbase's distributed and scalable nature exposes any set-up to the risk of potential network and hardware problems. The key to durability is planning for resilience, by evaluating the options on offer for persistence and replication, and carefully considering the performance trade-offs involved.

## [](#durability)Durability

Writes in Couchbase (from the SDK or elsewhere) are written to a single node. From there, Couchbase Server will take care of sending the mutation to any configured replicas, and to disk. By default all writes are asynchronous, but levels of durability can be set, to ensure replication and/or _persistence_ to disks, before the write is _committed_.

### [](#durable-writes)Durable Writes

All supported versions of Couchbase Server (since 6.5) offer [Durable Writes](../../../server/7.6/learn/data/durability.md), under which mutations will not be visible to other clients until they have met their durability requirements.

The optional `durabilityLevel` parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding. If `durabilityLevel()` is used with no argument, the application will report success back as soon as the primary node has acknowledged the mutation in its memory. The three replication level options are:

* `Majority` — The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` — Majority level, plus persisted to disk on the active node.
* `PersistToMajority` — Majority level, plus persisted to disk on the majority of configured replicas.

The options are in order of increasing levels of safety. For a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. In particular, `PersistToMajority` will take longer than the other two, and the `timeout` value needs to be selected with care — particularly for large numbers of documents — after testing on a representative network, with a realistic workload. Variation in network speeds and conditions, _inter alia_, make it difficult to give blanket recommendations.

You can set Durablilty as part of regular [CRUD operations against the Data Service](../howtos/kv-operations.md#durability), or set it per Bucket from the Server or [Capella](../../../cloud/clusters/data-service/manage-buckets.md#configure-advanced-bucket-settings). If it is set in either the SDK, the Server, or both, then the highest level on either side (or the level on the only side that sets it) is enforced. Options for making changes to `numKvConnections` (kvEndpoints) and `kvDurableTimeout` for Durable Writes can be found on the [Client Settings page](../ref/client-settings.md#io-options). Increasing the number of reader and writer threads for Couchbase Server storage _may_ be advantageous: see the discussion on the [Server storage page](../../../server/7.6/learn/buckets-memory-and-storage/storage-settings.md#threading).

> [!IMPORTANT]
> Durable Writes must not be made with three replicas. Attempting this will result in an error message: `DURABILITY_IMPOSSIBLE`.

While Durable Writes are being attempted, another client cannot write to the document concerned — see the diagram and explanation [in the Server Durability docs](#7.1@server:learn:data/durability.adoc#process-and-communication).

### [](#errors-exceptions)Errors & Exceptions

See [Durable Writes error codes](../ref/error-codes.md#107-durabilitylevelnotavailable).

#### [](#ambiguity)Ambiguity

Durable Writes do a great deal to mitigate against network problems, but working in a distributed environment always brings its own class of extra problems to any client-server communication.

Consider carefully the case where the client has sent the operation to the server, the server has sent the mutation on to the replica(s), and the replicas have acknowledged completion of their operation(s). Now, at the point where the server is sending the successful status to the client, the network drops. The client is in an ambiguous state, not knowing whether or not the operation was successful.

In cases where the operation is idempotent (such as an upsert operation), then simply retrying is a perfectly acceptable strategy, where the cost of doing so is justified by the importance of the operation. Where the operation is an array append, or somesuch, then [distributed, multi-document ACID transactions](#7.1@server:learn:data/transactions.adoc) should be considered.

### [](#performance-considerations)Performance considerations

Note that Couchbase's design of asynchronous persistence and replication is there for a reason: The time it takes to store an item in memory is several orders of magnitude quicker than persisting it to disk or sending it over the network. Operation times and latencies will increase when waiting on the speed of the network and the speed of the disk.

Durability operations may also cause increased network traffic since it is implemented at the client level by sending special probes to each server once the actual modification has completed.

### [](#legacy-durability)Legacy Durability

Early versions of Couchbase Server used client-verified durablilty. This is still available in the SDK — see the [API documentation on durability](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/durability/index.html) for details of `PersistTo` and `ReplicateTo` — but in almost every case with current Couchbase Server versions it's best to use the guarantees offered by the the Server.

## [](#transactions)Transactions

Couchbase introduced [distributed, multi-document ACID Transactions](#7.1@server:learn:data/transactions.adoc), with Couchbase Data Platform 6.5\. Read more on the concepts and commitment level, and take a look at the implementation:

* [An introductory guide to how Couchbase ACID Transactions work](../../../server/current/learn/data/transactions.md).
* [A HOWTO guide](../howtos/distributed-acid-transactions-from-the-sdk.md).