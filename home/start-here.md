---
title: Get Started with Couchbase
pubDate: 2026-10-19T14:21:08.937Z
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

Couchbase is a multipurpose NoSQL database for transactional, analytical, mobile, and AI applications. Our operational and analytical databases can be deployed self-managed or fully-managed as a service offering. Offline-first mobile takes Couchbase to the edge, and can be synced via App Services in the cloud, or a self-managed Sync Gateway deployment. AI Services (currently in private preview) simplify building agentic apps.

## A Multipurpose NoSQL Platform for Transactional, Analytical, Mobile / Edge, and AI Applications

###  Transactional Workloads — in the Cloud or Your Datacenter

Explore SQL++, or the fast CRUD interface of the Data Service.

[Sign Up to Capella](https://cloud.couchbase.com/sign-up), our managed cloud service, for the quickest start. Follow along with the built-in tutorial, or discover a [Couchbase Operational SDKs](sdk.md) in your favorite programming language:

[C](../c-sdk/current/hello-world/start-using-sdk.md)| [C++](../cxx-sdk/current/hello-world/start-using-sdk.md)| [.NET](../dotnet-sdk/current/hello-world/start-using-sdk.md)| [Go](../go-sdk/current/hello-world/start-using-sdk.md)| [Java](../java-sdk/current/hello-world/start-using-sdk.md)| [Kotlin](../kotlin-sdk/current/hello-world/start-using-sdk.md)| [Node.js](../nodejs-sdk/current/hello-world/start-using-sdk.md)| [PHP](../php-sdk/current/hello-world/start-using-sdk.md)| [Python](../python-sdk/current/hello-world/start-using-sdk.md)| [Ruby](../ruby-sdk/current/hello-world/start-using-sdk.md)| [Rust](../rust-sdk/current/hello-world/start-using-sdk.md)| [Scala](../scala-sdk/current/hello-world/start-using-sdk.md)

Install [Couchbase Server](server.md) in your own datacenter or private cloud — or use [Operator on Kubernetes or OpenShift](../operator/current/overview.md) for a truly cloud native solution.

###  Real Time Analytics with Operational Insights

* [Operational Insights Enterprise](../operational-insights/current/intro/intro.md) brings the power of NoSQL to the world of analytics — self-managed, in your private cloud or data centre.
* [Operational Insights Capella](../operational-insights-cloud/intro/intro.md) brings the power of NoSQL to the world of analytics — managed for you as a Capella service
* [Develop for Insights](operational-insights-sdk.md) with SDKs purpose built for Operational Insights' real-time analytical use cases — supportint streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK, such as connection management and robust error handling.

###  Develop for Mobile and the Edge

Build your app in Couchbase Lite (CBL) for offline-first connectivity, then sync to Couchbase Server with Capella App Services (or self-managed Sync Gateway) — or run peer-to-peer.

* Couchbase Lite for [Android in Java or Kotlin](../couchbase-lite/current/android/quickstart.md) | [iOS Swift](../couchbase-lite/current/swift/quickstart.md)and [iOS Objective-C](../couchbase-lite/current/objc/quickstart.md) | [Edge devices in C](../couchbase-lite/current/c/quickstart.md) | [C# .NET](../couchbase-lite/current/csharp/quickstart.md) | [Java](../couchbase-lite/current/java/quickstart.md) | [JavaScript — Ionic and React](#couchbase-lite:javascript:quickstart.adoc)
* Sync your data with:

  * [Capella App Services](../cloud/mobile-guides/intro.md)
  * [Self-managed SyncGateway](../sync-gateway/current/introduction.md)
  * [Edge Server](../couchbase-edge-server/current/introduction/intro.md)
  * [peer-to-peer](../couchbase-lite/current/android/p2psync-websocket.md)

###  Develop RAG and Agentic AI Applications

Explore AI Services and build Agentic Apps with the [AI Data Plane](../ai/get-started/intro.md).

[Couchbase MCP Server](../mcp-server/get-started/overview.md) is a self-hosted MCP Server that allows AI agents to connect to and interact with data in Couchbase clusters, whether hosted on Capella or self-managed.

Or see how Vector Query facilitates RAG applications speedily and at scale. Vector Search Service offers the ability to combine searches with our sophisticated Search API.

* [Vector Search in Capella Operational](../cloud/vector-search/vector-search.md)
* [Vector Search in self-managed Couchbase Server](../server/current/vector-search/vector-search.md)