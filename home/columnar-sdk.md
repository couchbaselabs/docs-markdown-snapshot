---
title: Develop with Operational Insights Capella
description: Operational Insights Capella is a real-time analytical database
  (RT-OLAP) for real time apps and operational intelligence. Operational
  Insights Capella is a standalone, managed offering from Couchbase under the
  Capella family of products — a self-managed Operational Insights Enterprise
  product is also available.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Documentation
    version: master
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/columnar-sdk.adoc
  xref: xref:home::columnar-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/columnar-sdk.html)

# Develop with Operational Insights Capella

# Develop with Operational Insights Capella

[Operational Insights Capella](../operational-insights-cloud/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Operational Insights Capella is a standalone, managed offering from Couchbase under the Capella family of products — a self-managed [Operational Insights Enterprise](../operational-insights/current/intro/intro.md) product is also available.

> [!TIP]
> Which Analytics Service?
> 
> Operational Insights Capella and Operational Insights Enterprise are column-based real-time analytical databases.
> 
> Operational Insights Capella SDKs, also known as Columnar SDKs, are similar to the Operational Insights SDKs. They must be used to connect to the current Operational Insights Capella Service, as it presents a different connection interface, without Operational Insights Enterprise's load balancer.
> 
> To connect to self-managed Operational Insights Enterprise, use our [Operational Insights SDKs](operational-insights-sdk.md).
> 
> [Analytics Service (CBAS)](../server/current/learn/services-and-indexes/services/analytics-service.md) is our classic OLAP available as part of self-managed Couchbase Server and Capella Operational. Use the [operational SDKs](sdk.md) to develop for this service.

## SDK APIs to work with Operational Insights Capella:

Columnar SDKs are developed from the ground-up and while they maintain some syntactic similarities with the [operational SDKs](sdk.md), they are purpose built for Operational Insights Capella's real-time analytical use cases. They support streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK — such as connection management and robust error handling.

* Go
* Java
* Node.js
* Python

[Go Columnar SDK Docs](../go-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../go-columnar-sdk/current/hello-world/start-using-sdk.md) | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocbcolumnar)

[Java Columnar SDK Docs](../java-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../java-columnar-sdk/current/hello-world/start-using-sdk.md) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client)

[Node.js Columnar SDK Docs](../nodejs-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../nodejs-columnar-sdk/current/hello-world/start-using-sdk.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/columnar-nodejs-client)

[Python Columnar SDK Docs](../python-columnar-sdk/current/hello-world/overview.md) | [Quickstart](../python-columnar-sdk/current/hello-world/start-using-sdk.md) | [Python API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client)