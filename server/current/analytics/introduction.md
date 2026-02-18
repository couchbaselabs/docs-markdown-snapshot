---
title: Analyze Large Datasets
description: Overview of the Couchbase Analytics Service
editUrl: https://github.com/couchbase/docs-analytics/edit/release/8.0/modules/analytics/pages/introduction.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/analytics/introduction.html)

# Analyze Large Datasets

Couchbase Analytics is a parallel data management capability for Couchbase Server. Couchbase Analytics is designed to efficiently run complex queries over many records. By complex queries, we mean large ad hoc join, set, aggregation, and grouping operations, any of which may result in long running queries, high CPU usage, high memory consumption, and/or excessive network latency due to data fetching and cross node coordination.

Regardless of the technology used, analytic queries can be predetermined or ad hoc, and they can be cheap or expensive depending on how much data processing they involve. Performance challenges can arise when queries access large numbers of documents and when queries are not supported by a secondary index, as often happens with ad hoc analytics done using successive exploratory queries or an interactive visualization tool.

Couchbase Analytics is designed to support truly ad hoc queries in a reasonable amount of time, even when full scans or large joins or sorts are required. Because Analytics supports efficient parallel query processing and bulk data handling, and runs on separate nodes in a Couchbase cluster, Couchbase Analytics is often preferable for expensive queries, even if the queries are predetermined and could be supported by a frontend (operational) index.

## [](#overview)Overview

The Analytics service enables you to create shadow copies of the data that you want to analyze. When the shadowed Analytics data is linked to the operational data, changes in the operational data are reflected in your Analytics data in real time. You can then query the Analytics data without slowing down the operational Data or Query services. You can add more Analytics nodes to reduce Analytics query times.

![analytics-overview](_images/analytics-overview-fb1002a29408058abb4101c3805827c00be18cba.svg) 

The Couchbase Analytics approach has significant advantages compared to the commonly employed alternatives:

* **Common data model:** Couchbase Analytics natively supports the same rich, flexible-schema document data model used for your operational data — you don’t have to force your data into a flat, predefined, relational model to analyze it.
* **Workload isolation:** Operational query latency and throughput are protected from slow-downs due to your analytical query workload — but without the complexity of operating a separate analytical database.
* **Data freshness:** Couchbase Analytics uses [DCP](../learn/clusters-and-availability/intra-cluster-replication.md#database-change-protocol), a fast memory-to-memory protocol that Couchbase Server nodes use to synchronize data among themselves — so Analytics runs on data that’s extremely current, without ETL (extract, transform, load) or other hassles and delays.
* **High availability:** The shadowed Analytics data may be replicated up to 3 times. Each replica resides on a different Analytics node. The use of Analytics replicas ensures that, should an Analytics node fail over, the Analytics Service continues to work: one of the replicas is promoted to serve the shadow data that was stored on the failed over node.

You can also create remote links to analyze data on remote Couchbase clusters, and also external links, to analyze data from external sources such as Amazon S3, Microsoft Azure Blob, or Google Cloud Storage.

## [](#when-to-use-analytics)When to Use Analytics

Use the Query service for operational queries — for example, the front-end queries behind every page display or navigation.

Use the Analytics service when you don’t know every aspect of the query in advance — for example, if the data access patterns change frequently, or you want to avoid creating an index for each data access pattern, or you want to run ad hoc queries for data exploration or visualization.

Use the Full Text Search service when you want to take advantage of natural-language querying.

## [](#sql-for-analytics-query-language)SQL++ for Analytics Query Language

Couchbase Analytics is queried using the SQL++ for Analytics query language, a next-generation declarative query language for JSON data. SQL++ for Analytics has much in common with SQL, but it also includes a small number of extensions that address the different data models that the two languages were designed to query. Compared to SQL, SQL++ for Analytics is much newer and targets the nested, schema-optional or even schemaless world of modern NoSQL systems.

You may wonder why Couchbase Analytics uses a query language other than SQL++ for Query, the query language used by Couchbase Server’s Query service for operational data. In fact, SQL++ for Analytics and SQL++ for Query are very similar, with SQL++ for Analytics offering some additional advances beyond SQL++ for Query. The section [SQL++ for Analytics vs. SQL++ for Query](6%5Fn1ql.md) provides additional details.

For more details, refer to the [SQL++ for Analytics Reference](1%5Fintro.md) section.

## [](#Whats%5Fnext)What’s Next

Now you can continue to [Running Queries](run-query.md)to get familiar with the ways you can run a query or continue directly to the [Analytics Tutorial](primer-beer.md).