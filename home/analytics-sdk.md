---
title: Develop with Operational Insights
description: Operational Insights is a JSON-native NoSQL analytical database. It
  serves to unify data from diverse sources, allowing for the execution of
  complex analytical queries and the extraction of timely insights.
pubDate: 2026-10-21T04:23:09.426Z
meta:
  component:
    title: Couchbase Documentation
    version: master
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/analytics-sdk.adoc
  xref: xref:home::analytics-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/analytics-sdk.html)

# Develop with Operational Insights

# Develop with Operational Insights

[Operational Insights](../operational-insights/current/intro/intro.md) is a JSON-native NoSQL analytical database. It serves to unify data from diverse sources, allowing for the execution of complex analytical queries and the extraction of timely insights.

  
* [Operational Insights Enterprise](../operational-insights/current/intro/intro.md) is a self-managed version of Couchbase's real-time analytical database (RT-OLAP), for running in your own datacenter or private cloud. These pages cover the older Analytic SDKs, which are compatible with Operational Insights Enterprise 3.x. Unless you are in the process of migrating from an earlier Analytics project using these SDKs, you should instead look at our [Operational Insights SDKs](operational-insights-sdk.md) — which will be developed to cover new functionality in future releases of Operational Insights.
* [Operational Insights Capella](../operational-insights-cloud/intro/intro.md) is a Couchbase-managed version of our real-time analytical database (RT-OLAP), accessed through the Capella control plane, and running in your choice of CSP (AWS, Azure, or GCP). Currently, [Columnar SDKs](columnar-sdk.md) must be used to connect to the Operational Insights Capella Service, as it presents a different connection interface, without Operational Insights Enterprise's load balancer.

  
## SDK APIs to work with Operational Insights

> [!TIP]
> This section covers Couchbase's older Analytics SDKs. These have been superseded by the new [Operational Insights SDKs](operational-insights-sdk.md), and these Analytics SDKs will be deprecated in due course.

Analytics SDKs are developed from the ground-up and while they maintain some syntactic similarities with the [operational SDKs](sdk.md), they are purpose built for Operational Insights' real-time analytical use cases. They support streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK — such as connection management and robust error handling.

* .NET
* Go
* Java
* Node.js
* Python

[.NET Analytics SDK Docs](../dotnet-analytics-sdk/current/hello-world/overview.md) | [Quickstart](../dotnet-analytics-sdk/current/hello-world/start-using-sdk.md) | [.NET Analytics API Reference](https://docs.couchbase.com/sdk-api/analytics-dotnet-client)

[Go Analytics SDK Docs](../go-analytics-sdk/current/hello-world/overview.md) | [Quickstart](../go-analytics-sdk/current/hello-world/start-using-sdk.md) | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocbanalytics)

[Java Analytics SDK Docs](../java-analytics-sdk/current/hello-world/overview.md) | [Quickstart](../java-analytics-sdk/current/hello-world/start-using-sdk.md) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-analytics-java-client/)

[Node.js Analytics SDK Docs](../nodejs-analytics-sdk/current/hello-world/overview.md) | [Quickstart](../nodejs-analytics-sdk/current/hello-world/start-using-sdk.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/analytics-nodejs-client)

[Python Analytics SDK Docs](../python-analytics-sdk/current/hello-world/overview.md) | [Quickstart](../python-analytics-sdk/current/hello-world/start-using-sdk.md) | [Python API Reference](https://docs.couchbase.com/sdk-api/analytics-python-client)

  
### Big Data Connectors

The available options for Operational Insights `DataFrame` and `Dataset` operations with the [Couchbase Spark Connector](../spark-connector/current/index.md)can be found on the Spark [DataFrames, Datasets, and SQL](../spark-connector/current/spark-sql.md#enterprise-analytics-options) page.

See the [Operational Insights](../operational-insights/current/sources/manage-remote.md) docs for information on streaming from Confluent for Kafka.

  
## Analytics Offerings in Couchbase

  
__SDKs by analytics offering__
| Analytics offering                                                                                     | Development option                                               |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [Operational Insights Enterprise](../operational-insights/current/intro/intro.md)                      | [Insights SDKs](operational-insights-sdk.md) [Analytics SDKs](#) |
| [Operational Insights Capella](../operational-insights-cloud/intro/intro.md)                           | [Columnar SDKs](columnar-sdk.md)                                 |
| [Analytics Service (CBAS)](../server/current/learn/services-and-indexes/services/analytics-service.md) | [Operational SDKs](sdk.md)                                       |

In addition to Operational Insights Enterprise Clusters, Operational Insights is also available as a managed service — Operational Insights Capella, formerly Columnar.

Traditional, row-based analytics is also available in Couchbase operational clusters — self-managed, or Capella Operational.

  
### SDK APIs to work with Operational Insights Capella:

[Operational Insights Capella](../operational-insights-cloud/intro/intro.md) is a standalone, managed cloud offering from Couchbase under the Capella family of products.

Operational Insights Capella SDKs, formerly known as Columnar SDKs, are similar to the Operational Insights SDKs. They must be used to connect to the current Operational Insights Capella Service, as it presents a different connection interface, without Operational Insights Enterprise's load balancer.

* Go
* Java
* Node.js
* Python

[Go Columnar SDK Docs](../go-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../go-columnar-sdk/current/hello-world/start-using-sdk.md) | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocbcolumnar)

[Java Columnar SDK Docs](../java-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../java-columnar-sdk/current/hello-world/start-using-sdk.md) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client)

[Node.js Columnar SDK Docs](../nodejs-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../nodejs-columnar-sdk/current/hello-world/start-using-sdk.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/columnar-nodejs-client)

[Python Columnar SDK Docs](../python-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../python-columnar-sdk/current/hello-world/start-using-sdk.md) | [Python API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client)

  
### Row-Based Couchbase Analytics

[CBAS (Couchbase Analytics Service)](../server/current/learn/services-and-indexes/services/analytics-service.md) is our classic OLAP available as part of self-managed Couchbase Server and Capella Operational. Use the [operational SDKs](sdk.md) to develop for this service.