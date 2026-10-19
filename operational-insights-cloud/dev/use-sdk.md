---
title: Use a Couchbase SDK with Operational Insights Services
description: The Couchbase SDKs enable you to connect client code written in
  popular languages to Operational Insights services.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/dev/pages/use-sdk.adoc
  xref: xref:analytics:dev:use-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/dev/use-sdk.html)

# Use a Couchbase SDK with Operational Insights Services

> The Couchbase SDKs enable you to connect client code written in popular languages to Operational Insights services. You can connect existing applications to Operational Insights services and develop new ones. 

[Columnar SDKs](../../home/columnar-sdk.md), are similar to the Operational Insights SDKs. They must be used to connect to the current Operational Insights Capella Service, as it presents a different connection interface, without Operational Insights Enterprise's load balancer.

## [](#about-sdk-use)About SDK Use

Existing applications that you originally designed for the Analytics Service in Couchbase Server or Capella should continue to work with Operational Insights services after a few changes, centered on connection string, imports, and the query method. For more information, see the individual Operational Insights SDK pages for the [Go](../../go-columnar-sdk/current/hello-world/overview.md), [Java](../../java-columnar-sdk/current/hello-world/overview.md), [Node.js](../../nodejs-columnar-sdk/current/hello-world/overview.md), and [Python](../../python-columnar-sdk/current/hello-world/overview.md) Columnar SDKs.

The main differences are:

* How you obtain the connection string for your app.
* How Operational Insights links to, and organizes, collections of data from different sources.

For more information about developing an app for analytics, see the Analytics topic in the SDK documentation for your preferred language. For example, for the Java SDK see [Analytics (Java SDK)](../../java-sdk/current/howtos/analytics-using-sdk.md).

## [](#getting-started)Getting Started

Before you can connect an app built with a Couchbase SDK to Operational Insights services, you use the Capella UI to create a project and cluster. See [Create a Cluster](../admin/prepare-project.md).

You can also use the UI to manage links and collections for different data sources and for ad hoc querying and exploration.

## [](#connectionstring)Getting the Connection String

Each Operational Insights cluster has its own connection string. To find and copy the string:

1. In the Capella UI, select the **Operational Insights** tab.
2. Select the cluster you want to connect to. The workbench opens.
3. At top left, from the **Operational Insights Cluster <cluster name>** list select **Connection Information**.  
![Using the cluster name as a menu](_images/get_connection_string.png)  
The Connection Information dialog opens.
4. To copy the connection string, click it or the copy icon.
5. When you paste in the connection string, replace the `https://` protocol with `couchbases://`:  
`couchbases://cb.<your-endpoint>.cloud.couchbase.com`

For more information, see the Connection Strings section of the [Go](../../go-columnar-sdk/current/howtos/managing-connections.md#connection-strings), [Java](../../java-columnar-sdk/current/howtos/managing-connections.md#connection-strings), [Node.js](../../nodejs-columnar-sdk/current/howtos/managing-connections.md#connection-strings), and [Python](../../python-columnar-sdk/current/howtos/managing-connections.md#connection-strings) Columnar SDKs Connections pages.