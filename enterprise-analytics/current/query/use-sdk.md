---
title: Use a Couchbase SDK with Enterprise Analytics [WIP]
description: The Analytics SDKs enable you to connect client code written in
  popular languages to Enterprise Analytics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/query/pages/use-sdk.adoc
  xref: xref:enterprise-analytics:query:use-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/query/use-sdk.html)

# Use a Couchbase SDK with Enterprise Analytics [WIP]

> The Analytics SDKs enable you to connect client code written in popular languages to Enterprise Analytics. You can connect existing applications to Enterprise Analytics and develop new ones. 

## [](#about-sdk-use)About SDK Use

Existing applications that you originally designed for the Analytics Service in Couchbase Server or Capella should continue to work seamlessly with Enterprise Analytics. For example, you continue to use the `cluster.Connect` object for any of the analytics functions, such as `analyticsQuery`.

The main differences are:

* How you obtain the connection string for your app.
* How Enterprise Analytics links to, and organizes, collections of data from different sources.

For more information about developing an application for analytics, see the Analytics topic in the SDK documentation for your preferred language. For example, for the Java SDK see [Analytics (Java SDK)](https://docs.couchbase.com/java-sdk/current/howtos/analytics-using-sdk.html).

## [](#getting-started)Getting Started

You can use the UI to manage links and collections for different data sources and for ad hoc querying and exploration.