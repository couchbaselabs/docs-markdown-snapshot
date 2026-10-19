---
title: Use a Couchbase SDK
description: Connect client code written in popular languages to Operational
  Insights using a Couchbase SDK.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/query/pages/use-sdk.adoc
  xref: xref:enterprise-analytics:query:use-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/query/use-sdk.html)

# Use a Couchbase SDK

> Connect client code written in popular languages to Operational Insights using a Couchbase SDK. You can connect existing applications to Operational Insights and develop new ones. 

## [](#about-sdk-use)About SDK Use

Existing applications that you originally designed for the Analytics Service in Couchbase Server or Capella continue to work with Operational Insights. For example, you continue to use the `cluster.Connect` object for any of the analytics functions, such as `analyticsQuery`.

To query Operational Insights from your application, connect with the SDK and submit SQL++ statements through its query API. The Operational Insights SDKs execute a query in buffered mode, returning all rows at once with `executeQuery`, or in streaming mode, processing each row as it arrives from the server with `executeStreamingQuery` — useful for large result sets. The 1.1 Analytics SDKs support both modes too.

The main differences are:

* How you obtain the connection string for your app.
* How Operational Insights links to, and organizes, collections of data from different sources.

## [](#operational-insights-sdks)Operational Insights SDKs

The Operational Insights SDKs are purpose-built for Operational Insights, with streaming APIs for large datasets and the connection management and error handling you expect from a modern database SDK. Use these SDKs for new applications.

Operational Insights provides SDKs for the following languages:

* [.NET](../../../dotnet-operational-insights-sdk/current/hello-world/overview.md)
* [Go](../../../go-operational-insights-sdk/current/hello-world/overview.md)
* [Java](../../../java-operational-insights-sdk/current/hello-world/overview.md)
* [Node.js](../../../nodejs-operational-insights-sdk/current/hello-world/overview.md)
* [Python](../../../python-operational-insights-sdk/current/hello-world/overview.md)

For an overview of all the Operational Insights SDKs, see [Develop with Operational Insights Enterprise](../../../home/operational-insights-sdk.md).

## [](#analytics-sdks)Analytics SDKs

If you're migrating an existing application from an earlier Analytics project, you can continue to use the Analytics SDKs, which are compatible with Operational Insights Enterprise 3.x. The [Operational Insights SDKs](../../../home/operational-insights-sdk.md) supersede these SDKs, and Couchbase is deprecating them.

For more information, see [Develop with Operational Insights](../../../home/analytics-sdk.md).

## [](#see-also)See Also

* [Develop with Operational Insights Enterprise](../../../home/operational-insights-sdk.md)
* [Develop with Operational Insights](../../../home/analytics-sdk.md)