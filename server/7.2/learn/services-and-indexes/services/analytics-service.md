---
title: Analytics Service
description: The Analytics Service provides a parallel data-management
  capability, allowing the running of complex analytical queries.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/services-and-indexes/services/analytics-service.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:learn:services-and-indexes/services/analytics-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/learn/services-and-indexes/services/analytics-service.html)

# Analytics Service

> The Analytics Service provides a parallel data-management capability, allowing the running of complex analytical queries. 

## [](#understanding-analytics)Understanding Analytics

The Analytics Service helps analyze JSON data in Couchbase in real time, without the need to extract, transform, and load (ETL) the underlying operational data into a separate system. The Analytics Service leverages massively parallel processing (MPP) architecture to deliver analytics and insights at the speed of transactions. Couchbase Analytics is best suited for running large, complex queries involving data aggregations, typically on large amounts of data.

![analyticsEcosystem](../../_images/analyticsEcosystem-3f034ce93e22f3f7c529b988ce9f442045a0f836.svg) 

The Analytics Service allows you to develop insight-driven applications easily and quickly. There are two focus areas: _operational analytics_ and _near real-time analytics_. Operational analytics uses data analysis and business intelligence to improve efficiency and streamline everyday operations in real time.

## [](#deploying-the-analytics-service)Deploying the Analytics Service

The Analytics Service enables you to create shadow copies of the data you would like to analyze. When shadow collections are created, they are connected to the [Data Service](data-service.md), and any changes in the operational data are reflected in the Analytics Service in near-real time, using the Database Change Protocol. This continuous data ingestion allows operational and analytic queries to run concurrently without impacting one another.

Due to the large scale and duration of operations it is likely to perform, the Analytics Service should be run _alone_, on its node or nodes in the cluster, _with no other Couchbase Service running on the Analytics nodes_.

For the practical steps required to initialize or join a cluster, and to deploy services, see [Create a Cluster](../../../manage/manage-nodes/create-cluster.md). For information on how to run analytic queries, see the [Introduction](../../../analytics/introduction.md) to Couchbase Analytics.

> [!WARNING]
> Non-Uniform Memory Access (NUMA)
> 
> Non-Uniform Memory Access (NUMA) can significantly impact the performance and stability of the Couchbase Analytics Service. NUMA architectures divide memory into different zones, each with a specific CPU, and accessing memory across zones can lead to latency.
> 
> Couchbase Analytics is not configured to align with the NUMA architecture. Deploying Couchbase Analytics on a server with the NUMA architecture may result in uneven memory distribution, increased latency, and degraded performance. Specifically, queries can become slower, and overall system efficiency can drop as memory access times vary significantly.