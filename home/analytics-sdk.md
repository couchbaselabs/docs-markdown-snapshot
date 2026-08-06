---
title: Develop with Enterprise Analytics
description: Enterprise Analytics is a self-managed, JSON-native NoSQL
  analytical database. It serves to unify data from diverse sources, allowing
  for the execution of complex analytical queries and the extraction of timely
  insights.
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/analytics-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:home::analytics-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/analytics-sdk.html)

# Develop with Enterprise Analytics

# Develop with Enterprise Analytics

[Enterprise Analytics](../enterprise-analytics/current/intro/intro.md) is a self-managed, JSON-native NoSQL analytical database. It serves to unify data from diverse sources, allowing for the execution of complex analytical queries and the extraction of timely insights.

  
## SDK APIs to work with Enterprise Analytics

Analytics SDKs are developed from the ground-up and while they maintain some syntactic similarities with the [operational SDKs](sdk.md), they are purpose built for Enterprise Analytics' real-time analytical use cases. They support streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK — such as connection management and robust error handling.

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

The available options for Enterprise Analytics `DataFrame` and `Dataset` operations with the [Couchbase Spark Connector](../spark-connector/current/index.md)can be found on the Spark [DataFrames, Datasets, and SQL](../spark-connector/current/spark-sql.md#enterprise-analytics-options) page.

See the [Enterprise Analytics](../enterprise-analytics/current/sources/manage-remote.md) docs for information on streaming from Confluent for Kafka.

  
## Other Analytics Services

__Table 1\. SDK Compatibility with Analytics Service__
| Analytics solution                                                                                               | Development option                                   |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [Enterprise Analytics](../enterprise-analytics/current/intro/intro.md)                                           | [Analytics SDKs](#)                                  |
| [Capella Analytics](../analytics/intro/intro.md)                                                                 | [Columnar (Capella Analytics) SDKs](columnar-sdk.md) |
| [CBAS (Couchbase Analytics Service)](../server/current/learn/services-and-indexes/services/analytics-service.md) | [Operational SDKs](sdk.md)                           |

In addition to the Enterprise Analytics, older Couchbase Analytics services are available — Enterprise Analytics' forerunner, Columnar, remains available as Capella Analytics for the present time.

Traditional, row-based analytics is also available in Couchbase operational clusters — self-managed, or Capella Operational.

  
### SDK APIs to work with Capella Analytics:

[Capella Analytics](../analytics/intro/intro.md) is a standalone, managed cloud offering from Couchbase under the Capella family of products.

Capella Analytics SDKs, formerly known as Columnar SDKs, are similar to the Enterprise Analytics SDKs. They must be used to connect to the current Capella Analytics Service, as it presents a different connection interface, without Enterprise Analytics' load balancer.

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