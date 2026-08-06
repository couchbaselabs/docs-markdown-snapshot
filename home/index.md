---
title: Couchbase Documentation
description: Couchbase is the modern database for enterprise applications.
  Couchbase is a distributed document database with a powerful search engine and
  in-built operational and analytical capabilities. It brings the power of NoSQL
  to the edge and provides fast, efficient bidirectional synchronization of data
  between the edge and the cloud.
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/index.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:home::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/index.html)

# Couchbase Documentation

# Couchbase Documentation

###### 

_Couchbase is the modern database for enterprise applications._

Couchbase is a distributed document database with a powerful search engine and in-built operational and analytical capabilities. It brings the power of NoSQL to the edge and provides fast, efficient bidirectional synchronization of data between the edge and the cloud.

Find the documentation, samples, and references to help you use Couchbase and build applications.

###### 

// List the schedule of flights from Boston
// to San Francisco on JETBLUE

SELECT DISTINCT airline.name, route.schedule
FROM `travel-sample`.inventory.route
  JOIN `travel-sample`.inventory.airline
  ON KEYS route.airlineid
WHERE route.sourceairport = "BOS"
AND route.destinationairport = "SFO"
AND airline.callsign = "JETBLUE";

###### 

## Get Started

###### 

Couchbase Capella (DBaaS)

Explore Couchbase Capella, our fully-managed database as a service offering. Take the complexity out of deploying, managing, scaling, and securing Couchbase in the public cloud. Store, query, and analyze any amount of data — and let us handle more of the administration — all in a few clicks.

[Couchbase Capella](cloud.md)

  
Capella Analytics (RT-OLAP)

Capella Analytics is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Capella Analytics is a standalone, cloud-only offering from Couchbase under the Capella family of products.

[Capella Analytics](../analytics/intro/intro.md)

###### 

Couchbase Server

Explore Couchbase Server, a modern, distributed document database with all the desired capabilities of a relational database and more. It exposes a scale-out, key-value store with managed cache for sub-millisecond data operations, purpose-built indexers for efficient queries, and a powerful query engine for executing SQL-like queries.

[Couchbase Server](server.md)

  
Enterprise Analytics (RT-OLAP)

Enterprise Analytics is a self-managed analytical database (RT-OLAP) for real time apps and operational intelligence.

[Enterprise Analytics](../enterprise-analytics/current/intro/intro.md)

###### 

Couchbase Mobile

_Couchbase Mobile_ brings the power of NoSQL to the edge. The combination of _Sync Gateway_ and _Couchbase Lite_ coupled with the power of _Couchbase Server_ provides fast, efficient bidirectional synchronization of data between the edge and the cloud. Enabling you to deploy your offline-first mobile and embedded applications with greater agility on premises or in any cloud.

[Couchbase Lite](../couchbase-lite/current/index.md) | [Sync Gateway](../sync-gateway/current/introduction.md) | [Couchbase Edge Server](../couchbase-edge-server/current/introduction/intro.md)

  
The Couchbase AI Data Plane

The Couchbase AI Data Plane is a fully managed set of tools that help you build, deploy, and scale your agentic and retrieval-augmented generation (RAG) AI applications. These tools integrate seamlessly with the Couchbase Capella cloud platform, enabling you to develop your AI applications on the same platform as your data.

[The Couchbase AI Data Plane](../ai/get-started/intro.md)

###### 

## Developer Tools

###### 

SDK and Connectors

Couchbase SDKs allow applications to access a Couchbase cluster and the big data Connectors enable data exchange with other platforms.

[Developer Docs](developer.md) | [Operational SDKs](sdk.md) | [Enterprise Analytics SDKs](analytics-sdk.md) | [Capella Analytics SDKs](columnar-sdk.md)

###### 

CLI and REST APIs

Use the command-line interface (CLI) tools and REST API to manage and monitor your Couchbase deployment.

[Couchbase CLI](../server/current/cli/cli-intro.md) | [REST API](../server/current/rest-api/rest-intro.md)

###### 

Couchbase Shell

A modern shell to interact with Couchbase Server and Capella, now available.

[Explore Couchbase Shell](https://couchbase.sh)

###### 

## More Developer Resources

###### 

Developer Portal

Explore a variety of resources - sample apps, videos, blogs, and more, to build applications using Couchbase.

[Developer Portal](https://developer.couchbase.com) [Developer Tutorials](https://developer.couchbase.com/tutorials)

###### 

Academy

Explore extensive hands-on learning experiences through free, online courses or under the guidance of an in-person instructor.

[Academy](https://learn.couchbase.com/store)

###### 

Community

With open source roots, Couchbase has a rich history of collaboration and community. Connect with our developer community and get involved.

[Community](https://forums.couchbase.com/)

###### 

## Explore Products and Services

| Cloud                                                                          | Server                                                                                                                                                                                                                                                                                                 | SDK and Connectors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Mobile                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Couchbase Capella](cloud.md) [Capella Analytics](../analytics/intro/intro.md) | [Couchbase Server](server.md) [Enterprise Analytics](../enterprise-analytics/current/intro/intro.md) [Couchbase Autonomous Operator](../operator/current/overview.md) [Couchbase Service Broker](#service-broker::index.adoc) [Couchbase Monitoring and Observability Stack](../cmos/current/index.md) | [Couchbase Java SDK](../java-sdk/current/hello-world/overview.md) [Couchbase Scala SDK](../scala-sdk/current/hello-world/overview.md) [Couchbase .NET SDK](../dotnet-sdk/current/hello-world/overview.md) [Couchbase C++ SDK](../cxx-sdk/current/hello-world/overview.md) [Couchbase C SDK](../c-sdk/current/hello-world/overview.md) [Couchbase Node.js SDK](../nodejs-sdk/current/hello-world/overview.md) [Couchbase PHP SDK](../php-sdk/current/hello-world/overview.md) [Couchbase Python SDK](../python-sdk/current/hello-world/overview.md) [Couchbase Ruby SDK](../ruby-sdk/current/hello-world/overview.md) [Couchbase Go SDK](../go-sdk/current/hello-world/overview.md) [Couchbase Kotlin SDK](../kotlin-sdk/current/hello-world/overview.md) [Couchbase Elasticsearch Connector](../elasticsearch-connector/current/getting-started.md) [Couchbase Kafka Connector](../kafka-connector/current/quickstart.md) [Couchbase Spark Connector](../spark-connector/current/getting-started.md) [Go Analytics SDK](../go-analytics-sdk/current/hello-world/overview.md) [Java Analytics SDK](../java-analytics-sdk/current/hello-world/overview.md) [Node.js Analytics SDK](../nodejs-analytics-sdk/current/hello-world/overview.md) [Python Analytics SDK](../python-analytics-sdk/current/hello-world/overview.md) [Go Columnar SDK](../go-columnar-sdk/current/hello-world/overview.md) [Java Columnar SDK](../java-columnar-sdk/current/hello-world/overview.md) [Node.js Columnar SDK](../nodejs-columnar-sdk/current/hello-world/overview.md) [Python Columnar SDK](../python-columnar-sdk/current/hello-world/overview.md) | [Couchbase Lite JavaScript](#couchbase-lite:javascript:quickstart.adoc) [Couchbase Lite C#](../couchbase-lite/current/csharp/quickstart.md) [Couchbase Lite Java](../couchbase-lite/current/java/quickstart.md) [Couchbase Lite Java Android](../couchbase-lite/current/android/quickstart.md) [Couchbase Lite Swift](../couchbase-lite/current/swift/quickstart.md) [Couchbase Lite Objective-C](../couchbase-lite/current/objc/quickstart.md) [Couchbase Sync Gateway](../sync-gateway/current/index.md) |

###### 

## Feedback and Contributions

###### 

Provide Feedback

Provide feedback, and get help with any problem you may encounter.

[Provide Feedback](../server/current/introduction/contact-couchbase.md)

###### 

Contact Support

Couchbase Support provides online support for customers of Enterprise Edition who have a support contract.

[Contact Couchbase](../server/current/introduction/contact-couchbase.md)

###### 

Contribute

You can submit simple changes, such as typo fixes and minor clarifications directly on GitHub. Contributions are greatly encouraged.

[Contribute to the Documentation](contribute/index.md)