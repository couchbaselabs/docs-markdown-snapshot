---
title: Develop with Couchbase
description: The Developer Data Platform for Critical Applications in Our AI
  World. Couchbase is a multipurpose NoSQL database for transactional,
  analytical, mobile, and AI applications. Develop at the edge with
  offline-first Couchbase Lite, for transactional workloads with SDKs in a dozen
  popular programming languages, for real-time analytics, and build agentic
  apps.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/developer.adoc
  xref: xref:home::developer.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/developer.html)

# Develop with Couchbase

# Develop with Couchbase

The Developer Data Platform for Critical Applications in Our AI World.

Couchbase is a multipurpose NoSQL database for transactional, analytical, mobile, and AI applications. Develop at the edge with offline-first Couchbase Lite, for transactional workloads with SDKs in a dozen popular programming languages, for real-time analytics, and build agentic apps.

## Development Choices for Your Use Cases

###  Transactional Workloads — in the Cloud or your Datacenter

Develop an app for [Capella Operational](https://docs.couchbase.com/cloud/develop/intro.html), or a [self-managed Couchbase Server](../server/7.6/develop/intro.md) — with [Operational SDKs](sdk.md). Explore SQL++, or the fast CRUD interface of the Data Service.

* [Get Started with the Java SDK](../java-sdk/current/hello-world/start-using-sdk.md)
* [NoSQL for RDBMS users](../cloud/tutorials/couchbase-tutorial-student-records.md)
* Try our [other SDKs](sdk.md):  
[C](../c-sdk/current/hello-world/overview.md)| [C++](../cxx-sdk/current/hello-world/overview.md)| [.NET](../dotnet-sdk/current/hello-world/overview.md)| [Go](../go-sdk/current/hello-world/overview.md)| [Kotlin](../kotlin-sdk/current/hello-world/overview.md)| [Node.js](../nodejs-sdk/current/hello-world/overview.md)| [PHP](../php-sdk/current/hello-world/overview.md)| [Python](../python-sdk/current/hello-world/overview.md)| [Ruby](../ruby-sdk/current/hello-world/overview.md)| [Rust](../rust-sdk/current/hello-world/overview.md)| [Scala](../scala-sdk/current/hello-world/overview.md)
* [Integrations, Connectors, and Tools](../cloud/third-party/integrations.md)

###  Real Time Analytics with Analytics SDKs

[Enterprise Analytics](../enterprise-analytics/current/intro/intro.md) brings the power of NoSQL to the world of analytics. Self-managed Enterprise Analytics brings real-time adaptive applications to your datacenter or private cloud — or try this service fully-hosted as [Capella Analytics](../analytics/intro/intro.md), which integrates seamlessly with the Couchbase Capella cloud platform. [Analytics SDKs](analytics-sdk.md) support streaming APIs to handle large datasets.

* [.NET Analytics SDK Docs](../dotnet-analytics-sdk/current/hello-world/overview.md)
* [Go Analytics SDK Docs](../go-analytics-sdk/current/hello-world/overview.md)
* [Java Analytics SDK Docs](../java-analytics-sdk/current/hello-world/overview.md)
* [Node.js Analytics SDK Docs](../nodejs-analytics-sdk/current/hello-world/overview.md)
* [Python Analytics SDK Docs](../python-analytics-sdk/current/hello-world/overview.md)

###  Develop for Mobile and the Edge

Build your app with [Couchbase Lite](../couchbase-lite/current/index.md) for offline-first connectivity, then sync to Couchbase Server with Capella App Services (or self-managed Sync Gateway) — or run peer-to-peer.

* [Develop for Android in Java or Kotlin](../couchbase-lite/current/android/quickstart.md)
* [Develop for iOS on Swift](../couchbase-lite/current/swift/quickstart.md)(and [Objective-C](../couchbase-lite/current/objc/quickstart.md))
* [Develop for Edge devices in C](../couchbase-lite/current/c/quickstart.md)
* Couchbase Lite [on C# .NET](../couchbase-lite/current/csharp/quickstart.md) | [Java](../couchbase-lite/current/java/quickstart.md) | [JavaScript — Ionic and React](#couchbase-lite:javascript:quickstart.adoc)
* Sync your data with [App Services](#cloud:app-services:index.adoc) / self-managed [SyncGateway](../sync-gateway/current/introduction.md) / [Edge Server](../couchbase-edge-server/current/introduction/intro.md) — or run [peer-to-peer](../couchbase-lite/current/swift/p2psync-websocket.md).

###  Develop RAG and Agentic AI Applications

Our Vector Search Service facilitates RAG applications — and offers the ability to combine searches with our sophisticated Search API. Agentic Apps can be built with Agent Catalog.

* [Vector Search](../cloud/vector-search/vector-search.md)
* [Agent Catalog](../ai/build/integrate-agent-with-catalog.md)