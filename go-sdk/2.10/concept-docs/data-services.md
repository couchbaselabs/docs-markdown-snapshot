[View original HTML](/go-sdk/2.10/concept-docs/data-services.html)

> Data in the Couchbase Data Platform can be accessed through Key Value (KV) Operations (including the Sub-Document API), the Analytics Service, the Query Service, Full Text Search, or even MapReduce Views: how do you pick the right service for your application? 

Couchbase Data Platform features several services to enable efficient information retrieval at a speed and scale to suit every use case. Although each service uses a different API, exposed on a different port, and often addressing different protocols, the Couchbase SDKs abstract away many of the differences — offering consistency across different language SDKs where it is reasonable to do so.

You can follow the links below for more information on the services with the Couchbase SDKs, or read on to see which use case matches which service.

Couchbase Data Services

* [KV Operations](../howtos/kv-operations.md)
* [Sub-Document API](../howtos/subdocument-operations.md)
* [Couchbase Analytics Service (CBAS)](analytics-for-sdk-users.md)
* [Query Service](n1ql-query.md)
* [Full Text Search](full-text-search-overview.md)
* [MapReduce Views](understanding-views.md)
* [Connectors](#7.1@server:connectors:intro.adoc)

## [](#use-cases)Use Cases

It’s an understandable temptation to reach for the familiar, and Couchbase’s SQL-like SQL++ (formerly N1QL) makes the Query service an easy starting point for many, but it’s important to take time to match your use case to the best tool for the job.

### [](#known-documents)Known documents

When you already know the _Key_ (ID) of the document, then _KV Operations_ is by far the simplest way to retrieve or mutate it. The binary protocol used is far quicker than streaming JSON.

If you know the path to the piece of information that you need within a JSON document, then _Sub-Document_ operations will not only retrieve the information more quickly, but will reduce the amount of data that needs to be sent over the network.

### [](#long-running-queries-big-data)Long Running Queries & Big Data

[Couchbase Analytics Service (CBAS)](#7.1@server:learn:services-and-indexes/services/analytics-service.adoc) performs well on huge datasets, with complex aggregations, and uses SQL++ for Analytics, which gives a similar query experience to SQL++ for Query. CBAS supports workloads involving only SELECT (not INSERT or UPDATE), and uses local secondary indexes. Scalable performance comes from multi-node partitioned-parallel join, sort, aggregate, and grouped aggregate operators, and multiple storage devices (vbuckets over several nodes).

Use the Analytics Service when you don’t know every aspect of the query in advance -- for example, if the data access patterns change frequently, or you want to avoid creating an index for each data access pattern, or you want to run ad hoc queries for data exploration or visualization.

### [](#mutations)Mutations

Use KV Operations - for better performance. Where your mutations are on just a path within the document, use the Sub-Document API.

For the “update from a WHERE clause” with our Query Service, in which case you don’t know which documents would be altered, read the section on CAS and Concurrent Document Mutation to be aware of all of the implications.

### [](#array-mutation)Array Mutation

Sub-Doc allows appending, prepending, and inserting into arrays. For more sophisticated array operations, use SQL++'s `USEKEY`.

### [](#aggregation-reduce)Aggregation / Reduce

MapReduce Views uses distributed Map-Reduce for very fast aggregation operations (fast, because the indexes are pre-computed results) — ideal for pre-grouped aggregations, such as grouping temporal data sets (by day, by month, etc.). Views’ spatial support allows for fast searching over extensive geo-spatial data in Couchbase Data Platform 5.x — however, Spatial Views are no longer supported in Couchbase Server 6.x, and so are not found in SDK 3.x. Continuing improvements to our Query Service makes the latter usually a better choice, particularly as Views does not scale as well as the other services, lacking a global Index node.

For queries over a larger number of documents, CBAS would be the best tool here, otherwise, for high throughput, simple queries, pick our Query Service.

### [](#fuzzy-searches)Fuzzy searches

Use the Full Text Search (FTS) service when you want to take advantage of natural-language querying. For phrase matching, over free-form text, or matching over word stems, FTS is a powerful solution.

There are more concepts to learn, as FTS offers a very flexible service. In particular, care should be taken over building indexes, to stop them becoming unnecessarily large — see our [FTS documentation](#7.1@server:fts:full-text-intro.adoc). Once again, the SDK abstracts away much of the complexity from deeply nested queries, and the interface is similar to our Query Service.

From Couchbase Server 6.5, [Search Functions](#7.1@server:n1ql:n1ql-language-reference/searchfun.adoc) allow the use of FTS _within_ SQL++ queries.

### [](#querying)Querying

For operational queries -- such as the front-end queries behind every page display or navigation — the Query Service is a natural fit.

The Query Service using SQL++ - SQL for JSON - is ideal for retrieving multiple documents that match specific queries. Data can be joined together, and Global Secondary Indexes can be used to speed up searches. It’s a powerful and flexible way of querying, retrieving, and updating data, using a familiar language, but if you know the document’s key, then regular KV (or Sub-Doc) operations will always be faster.

### [](#lowest-latency)Lowest Latency

Streaming in a distributed system is complex, and thus we do not make our internal streams and changes feed directly available. However, it is exposed through use of our [Spark](#2.4@spark-connector::index.adoc) or [Kafka](#3.4@kafka-connector::index.adoc) connectors, which give you a high level API to our low level primitives.