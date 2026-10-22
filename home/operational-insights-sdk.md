---
title: Develop with Operational Insights Enterprise
pubDate: 2026-10-22T04:25:56.080Z
meta:
  component:
    title: Couchbase Documentation
    version: master
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/operational-insights-sdk.adoc
  xref: xref:home::operational-insights-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/operational-insights-sdk.html)

# Develop with Operational Insights Enterprise

# Develop with Operational Insights

[Operational Insights Enterprise](../operational-insights/current/intro/intro.md) is a self-managed, JSON-native NoSQL analytical database. It serves to unify data from diverse sources, allowing for the execution of complex analytical queries and the extraction of timely insights.

  
## SDK APIs to work with Operational Insights Enterprise

Operational Insights SDKs are developed from the ground-up and while they maintain some syntactic similarities with the [operational SDKs](sdk.md), they are purpose built for Operational Insights' real-time analytical use cases. They support streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK — such as connection management and robust error handling.

* .NET
* Go
* Java
* Node.js
* Python

[.NET Operational Insights SDK Docs](../dotnet-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../dotnet-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [.NET API Reference](https://docs.couchbase.com/sdk-api/insights-dotnet-client/introduction.html)

[Go Operational Insights SDK Docs](../go-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../go-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocbinsights)

[Java Operational Insights SDK Docs](../java-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../java-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-operational-insights-java-client/)

[Node.js Operational Insights SDK Docs](../nodejs-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../nodejs-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/operational-insights-nodejs-client)

[Python Operational Insights SDK Docs](../python-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../python-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Python API Reference](https://docs.couchbase.com/sdk-api/operational-insights-python-client)

  
### Big Data Connectors

The available options for `DataFrame` and `Dataset` operations with the [Couchbase Spark Connector](../spark-connector/current/index.md)can be found on the Spark [DataFrames, Datasets, and SQL](../spark-connector/current/spark-sql.md#options) page.

See the [Operational Insights Enterprise](../operational-insights/current/sources/manage-remote.md) docs for information on streaming from Confluent for Kafka.

  
## Analytics Offerings in Couchbase

__SDK by analytics offering__
| Analytics offering                                                                                     | Development option                                                |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| [Operational Insights Enterprise](#enterprise-analytic:intro:intro.adoc)                               | [Operational Insights SDKs](#) [Analytics SDKs](analytics-sdk.md) |
| [Operational Insights Capella](../operational-insights-cloud/intro/intro.md)                           | [Columnar SDKs](columnar-sdk.md)                                  |
| [Analytics Service (CBAS)](../server/current/learn/services-and-indexes/services/analytics-service.md) | [Operational SDKs](sdk.md)                                        |

Operational Insights is Couchbase's analytical database. It comes in two deployment options: Operational Insights Enterprise, which you manage yourself, and Operational Insights Capella, which is fully managed. Use the SDK that matches your deployment. The Analytics Service (CBAS) provides row-based analytics inside Couchbase operational clusters. It's available in self-managed Couchbase Server and in Capella Operational. To query it, use the Operational SDKs.

  
### SDK APIs to work with Operational Insights Capella

Operational Insights Capella (formerly Capella Analytics) uses the Columnar SDKs, not the Analytics SDKs. Operational Insights Capella uses a different connection interface from Operational Insights Enterprise, which connects through a load balancer, so it needs its own SDKs. The Columnar SDKs are similar to the Analytics SDKs.

* Go
* Java
* Node.js
* Python

[Go Columnar SDK Docs](../go-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../go-columnar-sdk/current/hello-world/start-using-sdk.md) | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocbcolumnar)

[Java Columnar SDK Docs](../java-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../java-columnar-sdk/current/hello-world/start-using-sdk.md) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client)

[Node.js Columnar SDK Docs](../nodejs-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../nodejs-columnar-sdk/current/hello-world/start-using-sdk.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/columnar-nodejs-client)

[Python Columnar SDK Docs](../python-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../python-columnar-sdk/current/hello-world/start-using-sdk.md) | [Python API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client)

  