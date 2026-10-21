---
title: Get Started with Couchbase
pubDate: 2026-10-21T04:23:09.426Z
meta:
  component:
    title: Couchbase Documentation
    version: master
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/start-here.adoc
  xref: xref:home::start-here.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/start-here.html)

# Get Started with Couchbase

# Get Started with Couchbase

The Developer Data Platform for Critical Applications in Our AI World.

Couchbase is a multipurpose NoSQL platform for operational, analytical, mobile, and AI applications. Use it fully managed in Capella, or self-manage it in your own environment.

## Explore the Platform

###  Run Operational Workloads with Couchbase Server

Use Couchbase Server as a fully managed service in Capella, or deploy it yourself:

* [Sign up for Capella](https://cloud.couchbase.com/sign-up), the fully managed cloud service and the quickest start
* [Install Couchbase Server](../server/current/install/install-intro.md) to self-manage it in your data center or private cloud
* [Deploy with Couchbase Autonomous Operator](../operator/current/overview.md) for a self-managed, cloud-native deployment on Kubernetes or OpenShift

Connect your application to Capella or Couchbase Server with the [Couchbase Operational SDKs](sdk.md).

###  Run Real-Time Analytics with Operational Insights

Use Operational Insights as a fully managed service in Capella, or deploy it yourself:

* [Operational Insights Capella](../operational-insights-cloud/intro/intro.md), the fully managed analytics database
* [Operational Insights Enterprise](../operational-insights/current/intro/intro.md), the self-managed analytics database

Connect your application with the Operational Insights SDKs for [Capella](columnar-sdk.md) or [Enterprise](operational-insights-sdk.md).

###  Develop for Mobile and the Edge

Sync data from your mobile and edge apps, fully managed in Capella, self-managed in your own data center or at the edge, or directly between devices:

* [Capella App Services](../app-services/index.md), the fully managed sync service
* [Sync Gateway](../sync-gateway/current/introduction.md), the self-managed sync service for Couchbase Server
* [Edge Server](../couchbase-edge-server/current/introduction/intro.md), a lightweight database that syncs Couchbase Lite apps in resource-constrained edge environments
* [Peer-to-peer sync](../couchbase-lite/current/android/p2psync-websocket.md) directly between devices

Build offline-first apps with Couchbase Lite for your platform:

[Android in Java or Kotlin](../couchbase-lite/current/android/quickstart.md)| [iOS Swift](../couchbase-lite/current/swift/quickstart.md)| [iOS Objective-C](../couchbase-lite/current/objc/quickstart.md)| [Edge devices in C](../couchbase-lite/current/c/quickstart.md)| [C# .NET](../couchbase-lite/current/csharp/quickstart.md)| [Java](../couchbase-lite/current/java/quickstart.md)| [JavaScript](#couchbase-lite-javascript::introduction.adoc)| [React Native](../cbl-reactnative/current/intro.md)

###  Develop Agentic AI Applications

Build agentic and RAG applications with hosted models, persistent agent memory, Model Context Protocol (MCP) tools, and more:

* [AI Data Plane](../ai/get-started/intro.md), with hosted models, data vectorization, AI Functions, and Agent Catalog
* [Agent Memory](../agent-mem/current/about-agent-mem.md), a persistent memory layer for agents
* [MCP Server](../mcp-server/get-started/overview.md), to connect AI agents to your Couchbase data

Retrieve relevant context for your AI applications with Hyperscale, Composite, and Search vector indexes in [Capella](../cloud/vector-index/vectors-and-indexes-overview.md) or [Couchbase Server](../server/current/vector-index/vectors-and-indexes-overview.md).