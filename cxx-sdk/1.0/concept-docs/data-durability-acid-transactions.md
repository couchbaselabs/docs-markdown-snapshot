---
title: Data Modelling, Durability, and Consistency
description: Performance, availability, consistency -- balance your priorities,
  and model your data to achieve these goals.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/concept-docs/pages/data-durability-acid-transactions.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.0@cxx-sdk:concept-docs:data-durability-acid-transactions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.0/concept-docs/data-durability-acid-transactions.html)

# Data Modelling, Durability, and Consistency

> Performance, availability, consistency — balance your priorities, and model your data to achieve these goals. 

You want to query your data, but does that always mean a SQL++ query to the Query Service? The CRUD API of the SQL++ Query service is mirrored by the Data Service’s API, but without the need for indexes, and using a binary protocol gives faster access than streaming JSON from the Query Service.

```c++
std::string document_id{ "document_key" };
auto options = couchbase::remove_options().durability(couchbase::durability_level::majority);

auto [err, res] = collection.remove(document_id, options).get();

if (err.ec() == couchbase::errc::key_value::document_not_found) {
    fmt::println("The document does not exist");
} else if (err) {
    fmt::println("Got error: {}", err);
} else {
    fmt::println("id: {}, CAS: {}", document_id, res.cas().value());
}
```

At its heart, a database is in the business of storing data and letting you query and retrieve it. Putting a database on the network — in particular a remote network, or another company’s cloud service — and partitioning the data across multiple nodes, with several replicas, does not alter this. It does, however, mean that choices must be made to optimize for consistency or availability of data.

> [!TIP]
> Skipping Ahead
> 
> This page lays out some of the things you need to consider when designing an app. If you have already reached your decisions, and want to work with the Data API, then skip straight to our pages on [Data Operations](../howtos/kv-operations.md), [Sub-Document Operations](../howtos/subdocument-operations.md), or [Concurrent Document Mutations](../howtos/concurrent-document-mutations.md), and try some of the code snippets there. Or see some of the other links in the [Further Reading](#further-reading) section.

Whether you go through the Data Service, or Query, you’ll find that both follow the typical DML (Data Manipulation Language) patterns that you encounter in the relational database world. See the [SDK Query introduction](querying-your-data.md) for choices of SQL++ queries for OLTP (transactional queries) and OLAP (analytics) — including real-time analytics — as well as fuzzy searches and vector search.

Designing an application to offer guarantees of durability or consistency in a networked environment is hard. The newcomer to the area has to wrestle with concepts like [CAP Theorum](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/) and the [many possible interpretations](https://en.wikipedia.org/wiki/Isolation%5F%28database%5Fsystems%29) of ACID transactions. Here we hope to keep it _relatively_ simple, with a look at which Couchbase features give you which guarantees, when you may prefer to use them, and — perhaps equally important, though sometimes overlooked — what is the performance cost of these choices.

## [](#data-and-good-schema-design)Data and Good Schema Design

Each level of durability guarantee carries a price in time to persist to replicas or to disk. Transactional guarantees across multiple documents add another layer of performance cost — something readily borne when the data is important enough, and justifiably discarded for many categories of transient and unimportant data. However, many data fall into an intermediate category, and here the atomic consistency decision is made by what’s tolerable for read and write times. In this case, consider if a tweak to the schema, to bring items into the same document, can give you transactional guarantees without the performance penalty of multi-document transactions.

Consider, too, that many operations are performed at the _collection_ level, and keeping documents in the same collection can make for speedier indexing and queries — whether SQL++ or Search.

The Server enforces no schema, enabing evolutionary changes to your data model that reflect changes in the real world. The schema-on-read approach allows the client software that you write with the SDK to work with changes to an implicit schema, and allows heterogeneous data.

### [](#objects-relations-tables)Objects, Relations, Tables

In the Relational Database (RDBMS) world, a translation layer is often used between the objects of your data model in your application, and the tables that you store the data in. JSON storage allows you to store complex types, like nested records and arrays, without decomposing them to a second table (known in the SQL world as [database normalization](https://en.wikipedia.org/wiki/Database%5Fnormalization)).

When the relational model was proposed, more than 50 years ago, limitations in available computer resources meant that removing data duplication in one-to-many and many-to-many relationships this way made a great deal of sense. There is still a case to be made for it for reducing inconsistencies — the difference with a document database is that you get to choose when to do this.

### [](#collections-and-scopes)Collections and Scopes

Couchbase’s atomic units of data are documents, stored as key-value pairs. The value can be anything, but storing in JSON format enables indexing, searching, and many useful ways of working with the data from the SDK.

Collections are arbitary groupings of the data documents. Ones that suit your object model. For example, one collection of students enrolled at the college and one collection of courses available for them to take. Notionally you may view them as equivalent to an RDBMS table — but it’s up to you.

Within a bucket, you can organize your collections into scopes — some methods are available at the bucket level, but Search and Query Services favour Scope-level indexing and querying for greater efficiency.

## [](#durability)Durability

Writes in Couchbase (from the SDK or elsewhere) are written to a single node. From there, Couchbase Server will take care of sending the mutation to any configured replicas, and to disk. By default all writes are asynchronous, but levels of durability can be set, to ensure replication and/or _persistence_ to disks, before the write is _committed_.

### [](#durable-writes)Durable Writes

All supported versions of Couchbase Server (since 6.5) offer [Durable Writes](../../../server/7.6/learn/data/durability.md), under which mutations will not be visible to other clients until they have met their durability requirements.

The optional `durabilityLevel` parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding. If `durabilityLevel()` is used with no argument, the application will report success back as soon as the primary node has acknowledged the mutation in its memory. The three replication level options are:

* `Majority` — The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` — Majority level, plus persisted to disk on the active node.
* `PersistToMajority` — Majority level, plus persisted to disk on the majority of configured replicas.

The options are in order of increasing levels of safety. For a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. In particular, `PersistToMajority` will take longer than the other two, and the `timeout` value needs to be selected with care — particularly for large numbers of documents — after testing on a representative network, with a realistic workload. Variation in network speeds and conditions, _inter alia_, make it difficult to give blanket recommendations.

You can set Durablilty as part of regular [CRUD operations against the Data Service](../howtos/kv-operations.md#durability), or set it per Bucket from the Server or [Capella](../../../cloud/clusters/data-service/manage-buckets.md#configure-advanced-bucket-settings). If it is set in either the SDK, the Server, or both, then the highest level on either side (or the level on the only side that sets it) is enforced.

Further discussion can be found in the [Durability and Failure Considerations documentation](durability-replication-failure-considerations.md).

A practical look at this — using the `durability` parameter with mutating operations — can be found on the [Data Service page](../howtos/kv-operations.md#durability).

This durability is enforced by the database,

## [](#reading-from-replicas)Reading from Replicas

By default, read requests from the SDK are directed to the node with the active vbucket. This bucket will usually be updated before any replicas (see [Durability](#durability) above), and is best for consistency.

Some use cases benefit — for consistency or availability — from accessing both the active copy of the document, and/or one or all replicas. This can be direct from the [data service](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1collection.html#a50bd3c4c405242fdcf22564585af12ce), or a [SubDoc Read from Replica](../howtos/subdocument-operations.md#reading-sub-documents-from-replicas). The method can either be one to return the first result returned — active or replica — which is useful if a node is timing out; or to return _all_ of the results, for client code to handle any inconsistency, or to build a consensus answer.

### [](#preferred-server-group-replica-reads)Preferred Server Group Replica Reads

> [!IMPORTANT]
> Preferred Server Group Replica Reads are only accessible with the C++ SDK working with Couchbase Server 7.6.2 or newer (Capella or self-managed).

[Server Groups](../../../server/current/learn/clusters-and-availability/groups.md#understanding-server-group-awareness)can be used to define subsets of nodes within a Couchbase cluster, which contain a complete set of vbuckets (active or replica). As well as high availability use cases, Servre Groups can also be used to keep much traffic within the same cloud Availability Zone.

For Capella users with high data volumes, egress charges for reads from other Availability Zones (AZ) in AWS can be a significant cost. The C++ SDK, when making read replica requests, can make a request to a preferred Server Group — in this case the local AZ — and set to always read from a copy of the document in this local zone. This is done by putting cluster nodes in the same AZ into the same [Server Group](../../../server/current/learn/clusters-and-availability/groups.md#server-groups-and-vbuckets), too.

This may mean the application has to be tolerant of slight inconsistencies, until the local replica catches up. Alternatively, it may demand a stronger level of durability, to ensure that all copies of a document are consistent before they are accessible — provided that this is `persistToMajority` with [no more than one replica](../../../server/current/learn/data/durability.md#majority).

Couchbase does not recommend this feature where read consistency is critical, but with the appropriate durability settings consistency can be favored ahead of availability.

> [!CAUTION]
> Replicas, Nodes, and Server Groups
> 
> Implicit in the rules for durability, and the process of setting up Server Groups, is the following information — which we mention here explicitly to ensure it is all noted:
> 
> * Moving servers between Server Groups updates the `clustermap` immediately, but to move the data, an administrator **must** perform rebalance. Until the rebalance is complete, the SDK will see and be able to 'use' the new server groups, but the `vBucketMap` may still refer to data in the previous locations.
> * The cluster should have enough nodes and group to make sure that copies of the same document are not stored on the same node, and each group has nodes that cover all 1024 vbuckets (in other words, the number of the groups does not exceeds number of the copies: `active+num_replicas`). The Admin UI should emit small yellow warning if the configuration is considered unbalanced.
> * Setting **three** replicas for the bucket [disables durability for sync writes](../../../server/current/learn/data/durability.md#majority), also precluding the use of [multi-document ACID transactions](transactions.md).

## [](#concurrent-document-mutations)Concurrent Document Mutations

You can use the CAS value to control how concurrent document modifications are handled. It helps avoid and control potential race conditions in which some mutations may be inadvertently lost or overridden by mutations made by other clients.

### [](#performance-considerations)Performance considerations

CAS operations incur no additional overhead. CAS values are always returned from the server for each operation. Comparing CAS at the server involves a simple integer comparison which incurs no overhead.

### [](#cas-value-format)CAS value format

The CAS value should be treated as an opaque object at the application level. No assumptions should be made with respect to how the value is changed (for example, it is wrong to assume that it is a simple counter value). In the SDK, the CAS is represented as a 64 bit integer for efficient copying but should otherwise be treated as an opaque 8 byte buffer.

## [](#pessimistic-locking)Pessimistic locking

Pessimistic locking is the default approach for many RDBMS. With Couchbase, optimistic locking with CAS is the recommended way to perform locking and concurrency control.

Should you need the guarantees of explicit locking, documents can be locked using the _get-and-lock_ operation and unlocked either explicitly using the _unlock_ operation or implicitly by mutating the document with a valid CAS. While a document is locked, it may be retrieved but not modified without using the correct CAS value. When a locked document is retrieved, the server will return an invalid CAS value, preventing mutations of that document.

More information, including a table of behaviors while an item is locked, can be found in the [Pessimistic Locking section of the Concurrent Document Mutations page](../howtos/concurrent-document-mutations.md#pessimistic-locking).

## [](#multi-document-acid-transactions)Multi-Document ACID Transactions

Couchbase Distributed [ACID (atomic, consistent, isolated, and durable)](../../../server/current/learn/data/transactions.md#overview) Transactions allow applications to perform a series of database operations as a single unit — meaning operations are either committed together or all undone. Transactions are distributed and work across multiple documents, buckets, scopes, and collections, which can reside on multiple nodes. See the [C++ SDK transactions documentation](transactions.md).

## [](#additional-information)Additional Information

### [](#further-reading)Further Reading

This section of the docs covers the Data Service — Couchbase’s key-value document store, the heart of the database — from the client perspective. It addresses:

* Schemas for semi-structured data.
* The sub-document API for retrieving and modifying only a portion of a document (saving network bandwidth and transmission time).
* Durability options.
* Field-Level Encryption.
* Storing non-JSON documents.
* & Concurrent Document Mutations.

Below, we link some of the pages in this section that take a deeper dive into data structures, durability guarantees, and avoiding race conditions during concurrent document modifications — but if you are in a hurry to just learn more about querying your data, please skip ahead to [the next section](querying-your-data.md).

* A deeper dive into our [scopes and collections documentation](../../../server/current/learn/data/scopes-and-collections.md).
* [Working with other data structures from the SDK](data-model.md#data-structures).
* Backups
* Retry strategy

For more on Durability, see [Failure Considerations](durability-replication-failure-considerations.md).

### [](#lowest-latency-streams)Lowest Latency Streams

Streaming in a distributed system is complex, and thus we do not make our internal streams and changes feed directly available.

However, it is exposed through use of our [Spark](../../../spark-connector/current/index.md) or [Kafka](../../../kafka-connector/current/index.md) connectors, which give you a high level API to our low level primitives.

The source connector streams documents from Couchbase Server using the high-performance Database Change Protocol (DCP) and publishes the latest version of each document to a Kafka topic in near real-time.

The sink connector subscribes to Kafka topics and writes the messages to Couchbase Server.