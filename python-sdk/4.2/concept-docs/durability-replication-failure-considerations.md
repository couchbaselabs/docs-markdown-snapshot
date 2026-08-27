---
title: Failure Considerations
description: Data durability refers to the fault tolerance and persistence of
  data in the face of software or hardware failure.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.2/modules/concept-docs/pages/durability-replication-failure-considerations.adoc
  xref: xref:4.2@python-sdk:concept-docs:durability-replication-failure-considerations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.2/concept-docs/durability-replication-failure-considerations.html)

# Failure Considerations

> Data durability refers to the fault tolerance and persistence of data in the face of software or hardware failure. Even the most reliable software and hardware might fail at some point, and along with the failures, introduce a chance of data loss. Couchbase's durability features include Synchronous Replication, and the possibility to use distributed, multi-document ACID transactions. It is the responsibility of the development team and the software architect to evaluate the best choice for each use case. 

Couchbase's distributed and scalable nature exposes any set-up to the risk of potential network and hardware problems. The key to durability is planning for resilience, by evaluating the options on offer for persistence and replication, and carefully considering the performance trade-offs involved.

## [](#durability)Durability

Writes in Couchbase (from the SDK or elsewhere) are written to a single node. From there, Couchbase Server will take care of sending the mutation to any configured replicas, and to disk. By default all writes are asynchronous, but levels of durability can be set, to ensure replication and/or _persistence_ to disks, before the write is _committed_.

## [](#durable-writes)Durable Writes

Durability has been enhanced in Couchbase Data Platform 6.5, with [Durable Writes](#7.1@server:learn:data/durability.adoc), under which mutations will not be visible to other clients until they have met their durability requirements. These requirements are now enforced on the server side, rather than requiring client logic, which means that this committed durability can now be guaranteed.

The optional `durabilityLevel` parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding. If `durabilityLevel()` is used with no argument, the application will report success back as soon as the primary node has acknowledged the mutation in its memory. With Couchbase Server 6.5 and above, the three replication level options are:

* `Majority` — The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` — Majority level, plus persisted to disk on the active node.
* `PersistToMajority` — Majority level, plus persisted to disk on the majority of configured replicas.

The options are in order of increasing levels of safety. For a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. In particular, `PersistToMajority` will take longer than the other two, and `timeout` value needs to be selected with care — particularly for large numbers of documents — after testing on a representative network, with a realistic workload. Variation in network speeds and conditions, _inter alia_, make it difficult to give blanket recommendations.

> [!IMPORTANT]
> Durable Writes must not be made with three replicas. Attempting this will result in an error message: `DURABILITY_IMPOSSIBLE`.

While Durable Writes are being attempted, another client cannot write to the document concerned — see the diagram and explanation [in the Server Durability docs](#7.1@server:learn:data/durability.adoc#process-and-communication).

### [](#errors-exceptions)Errors & Exceptions

See [Durable Writes error codes](../ref/error-codes.md#107-durabilitylevelnotavailable).

#### [](#ambiguity)Ambiguity

Durable Writes do a great deal to mitigate against network problems, but working in a distributed environment always brings its own class of extra problems to any client-server communication.

Consider carefully the case where the client has sent the operation to the server, the server has sent the mutation on to the replica(s), and the replicas have acknowledged completion of their operation(s). Now, at the point where the server is sending the successful status to the client, the network drops. The client is in an ambiguous state, not knowing whether or not the operation was successful.

In cases where the operation is idempotent (such as an upsert operation), then simply retrying is a perfectly acceptable strategy, where the cost of doing so is justified by the importance of the operation. Where the operation is an array append, or somesuch, then [distributed, multi-document ACID transactions](#7.1@server:learn:data/transactions.adoc) should be considered.

## [](#older-server-versions)Older Server Versions

If a version of Couchbase Server lower than 6.5 is being used then the fallback is 'client verified' durability.

> [!WARNING]
> Client Verified durability is supported in [Python SDK 3.2](#3.2@durability-replication-failure-considerations.adoc#older-server-versions) but not in 4.0\. Legacy support will be available in a later 4.x release. See the [SDK 4.0 migration considerations](../project-docs/migrating-sdk-code-to-3.n.md#sdk4-specifics).

### [](#performance-considerations)Performance considerations

Note that Couchbase's design of asynchronous persistence and replication is there for a reason: The time it takes to store an item in memory is several orders of magnitude quicker than persisting it to disk or sending it over the network. Operation times and latencies will increase when waiting on the speed of the network and the speed of the disk.

Durability operations may also cause increased network traffic since it is implemented at the client level by sending special probes to each server once the actual modification has completed.