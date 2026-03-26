---
title: SDKs &amp; Connectors
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home::sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/sdk.html)

# SDKs &amp; Connectors

# SDKs & Connectors

## 

Couchbase provides several SDKs to allow applications to access a Couchbase cluster (Capella or self-managed), as well as [Couchbase Lite](mobile.md) — an embedded, NoSQL JSON Document Style database for your mobile apps. To exchange data with other platforms, we offer various Big Data Connectors.

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.reactive.upsert("document-key", json)
    .doOnError(err  => println(s"Error during upsert: ${err}"))
    .doOnNext(_     => println("Success"))
    .subscribe()
```

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database (RT-OLAP) for real time apps and operational intelligence — are [available](analytics-sdk.md) for the Go, Java, Node.js, and Python platforms.
> 
> SDKs for [Capella Analytics](../analytics/intro/intro.md) are similar to the Enterprise Analytics SDKs. They must be used to connect to the current Capella Analytics Service, as it presents a different connection interface, without Enterprise Analytics' load balancer. They are [available](columnar-sdk.md) for the Go, Java, Node.js, and Python platforms.

  
## Server SDKs

The Couchbase SDKs allow applications to access a Couchbase cluster. They offer traditional synchronous APIs as well as scalable asynchronous APIs to maximize performance.

| SDK         | Documentation                                         | Hello World Example                                                             | API Reference                                                                                                          |
| ----------- | ----------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| .NET SDK    | [Docs](../dotnet-sdk/current/hello-world/overview.md) | [.NET Getting Started](../dotnet-sdk/current/hello-world/start-using-sdk.md)    | [.NET API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client)                                          |
| C SDK       | [Docs](../c-sdk/current/hello-world/overview.md)      | [C Getting Started](../c-sdk/current/hello-world/start-using-sdk.md)            | [C API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client/index.html)                                    |
| C++ SDK     | [Docs](../cxx-sdk/current/hello-world/overview.md)    | [C++ Getting Started](../cxx-sdk/current/hello-world/start-using-sdk.md)        | [C++ API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/index.html)                                |
| Go SDK      | [Docs](../go-sdk/current/hello-world/overview.md)     | [Go Getting Started](../go-sdk/current/hello-world/start-using-sdk.md)          | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2)                                                    |
| Java SDK    | [Docs](../java-sdk/current/hello-world/overview.md)   | [Java Getting Started](../java-sdk/current/hello-world/start-using-sdk.md)      | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client)                                         |
| Kotlin SDK  | [Docs](../kotlin-sdk/current/hello-world/overview.md) | [Kotlin Getting Started](../kotlin-sdk/current/hello-world/start-using-sdk.md)  | [Kotlin API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client)                                     |
| Node.js SDK | [Docs](../nodejs-sdk/current/hello-world/overview.md) | [Node.js Getting Started](../nodejs-sdk/current/hello-world/start-using-sdk.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/modules.html)                         |
| PHP SDK     | [Docs](../php-sdk/current/hello-world/overview.md)    | [PHP Getting Started](../php-sdk/current/hello-world/start-using-sdk.md)        | [PHP API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html)                 |
| Python SDK  | [Docs](../python-sdk/current/hello-world/overview.md) | [Python Getting Started](../python-sdk/current/hello-world/start-using-sdk.md)  | [Python API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/)                                    |
| Ruby SDK    | [Docs](../ruby-sdk/current/hello-world/overview.md)   | [Ruby Getting Started](../ruby-sdk/current/hello-world/start-using-sdk.md)      | [Ruby API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase.html)                          |
| Rust SDK    | [Docs](../rust-sdk/current/hello-world/overview.md)   | [Rust Getting Started](../rust-sdk/current/hello-world/start-using-sdk.md)      | [Rust API Reference](https://docs.rs/couchbase/)                                                                       |
| Scala SDK   | [Docs](../scala-sdk/current/hello-world/overview.md)  | [Scala Getting Started](../scala-sdk/current/hello-world/start-using-sdk.md)    | [Scala API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html) |

###### 

###### 

### Alternatives to SDKs

The Data API gives access to data in Capella Operational clusters — for when to use the Data API, or Capella's other REST APIs, see [Data API vs. Couchbase SDKs](../cloud/data-api-guide/data-api-sdks.md).

###### 

###### 

## SDK Extension Libraries

The SDK Extension Libraries are shipped as separate libraries.

###### 

Field Level Encryption

Fields within a JSON document can be securely encrypted by the SDK to support FIPS 140-2 compliance. This is a client-side implementation, with encryption and decryption handled by the Couchbase client SDK.

[Field Level Encryption](../sdk-extensions/field-level-encryption.md)

###### 

Response Time Observability

Health indicators can tell you a lot about the performance of an application. Monitoring them is vital both during its development and production lifecycle. For a database, performance is best encapsulated via per-request performance.

[Response Time Observability](../sdk-extensions/response-time-observability.md)

###### 

Distributed ACID Transactions

Previously, distributed ACID transactions were available as separate libraries for some of the SDKs. Please note that this feature, available now in most of the SDKs, is incorporated directly into these SDKs.

[Distributed ACID Transactions](../sdk-extensions/distributed-acid-transactions.md)

  
## Enterprise Analytics SDKs

[Enterprise Analytics](../enterprise-analytics/current/intro/intro.md) is an analytical database (RT-OLAP) for real time apps and operational intelligence. [Analytics SDKs](analytics-sdk.md) are tailored to the APIs offered by this service.

| Analytics SDK         | Documentation                                                   | Hello World Example                                                                       | API Reference                                                                                      |
| --------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| .NET Analytics SDK    | [Docs](../dotnet-analytics-sdk/current/hello-world/overview.md) | [.NET Getting Started](../dotnet-analytics-sdk/current/hello-world/start-using-sdk.md)    | [.NET Analytics API Reference](https://docs.couchbase.com/sdk-api/analytics-dotnet-client)         |
| Go Analytics SDK      | [Docs](../go-analytics-sdk/current/hello-world/overview.md)     | [Go Getting Started](../go-analytics-sdk/current/hello-world/start-using-sdk.md)          | [Go Analytics API Reference](https://pkg.go.dev/github.com/couchbase/gocbanalytics)                |
| Java Analytics SDK    | [Docs](../java-analytics-sdk/current/hello-world/overview.md)   | [Java Getting Started](../java-analytics-sdk/current/hello-world/start-using-sdk.md)      | [Java Analytics API Reference](https://docs.couchbase.com/sdk-api/couchbase-analytics-java-client) |
| Node.js Analytics SDK | [Docs](../nodejs-analytics-sdk/current/hello-world/overview.md) | [Node.js Getting Started](../nodejs-analytics-sdk/current/hello-world/start-using-sdk.md) | [Node.js Analytics API Reference](https://docs.couchbase.com/sdk-api/analytics-nodejs-client/)     |
| Python Analytics SDK  | [Docs](../python-analytics-sdk/current/hello-world/overview.md) | [Python Getting Started](../python-analytics-sdk/current/hello-world/start-using-sdk.md)  | [Python Analytics API Reference](https://docs.couchbase.com/sdk-api/analytics-python-client/)      |

  
## Capella Analytics SDKs

[Capella Analytics](../analytics/intro/intro.md) is an analytical database (RT-OLAP) for real time apps and operational intelligence. [Columnar SDKs](columnar-sdk.md) for Capella Analytics are tailored to the APIs offered by this service.

| Columnar SDK         | Documentation                                                  | Hello World Example                                                                      | API Reference                                                                                    |
| -------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Go Columnar SDK      | [Docs](../go-columnar-sdk/current/hello-world/overview.md)     | [Go Getting Started](../go-columnar-sdk/current/hello-world/start-using-sdk.md)          | [Go Columnar API Reference](https://pkg.go.dev/github.com/couchbase/gocbcolumnar)                |
| Java Columnar SDK    | [Docs](../java-columnar-sdk/current/hello-world/overview.md)   | [Java Getting Started](../java-columnar-sdk/current/hello-world/start-using-sdk.md)      | [Java Columnar API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client) |
| Node.js Columnar SDK | [Docs](../nodejs-columnar-sdk/current/hello-world/overview.md) | [Node.js Getting Started](../nodejs-columnar-sdk/current/hello-world/start-using-sdk.md) | [Node.js Columnar API Reference](https://docs.couchbase.com/sdk-api/columnar-nodejs-client/)     |
| Python Columnar SDK  | [Docs](../python-columnar-sdk/current/hello-world/overview.md) | [Python Getting Started](../python-columnar-sdk/current/hello-world/start-using-sdk.md)  | [Python Columnar API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client/)      |

  
## SDK doctor

SDK doctor is a tool to diagnose application-server-side connectivity issues with your Couchbase Cluster. [SDK doctor](../server/current/sdk/sdk-doctor.md)

###### 

## Mobile Development with Couchbase Lite

| Mobile Platform             | Documentation                                           | API Reference                                                                           |
| --------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Couchbase Lite Java Android | [Docs](../couchbase-lite/current/android/quickstart.md) | [API Reference](http://docs.couchbase.com/mobile/3.2.0/couchbase-lite-android/)         |
| Couchbase Lite C#           | [Docs](../couchbase-lite/current/csharp/quickstart.md)  | [API Reference](http://docs.couchbase.com/mobile/3.2.0/couchbase-lite-net)              |
| Couchbase Lite Java         | [Docs](../couchbase-lite/current/java/quickstart.md)    | [API Reference](http://docs.couchbase.com/mobile/3.2.0/couchbase-lite-java/index.html?) |
| Couchbase Lite Objective-C  | [Docs](../couchbase-lite/current/objc/quickstart.md)    | [API Reference](http://docs.couchbase.com/mobile/3.2.0/couchbase-lite-objc)             |
| Couchbase Lite Swift        | [Docs](../couchbase-lite/current/swift/quickstart.md)   | [API Reference](http://docs.couchbase.com/mobile/3.2.0/couchbase-lite-swift)            |
| Couchbase Lite JavaScript   | [Docs](#couchbase-lite::javascript.adoc)                |                                                                                         |

###### 

## Big Data Connectors

Elasticsearch

* [Get Started](../elasticsearch-connector/current/getting-started.md)
* [Configuration](../elasticsearch-connector/current/configuration.md)
* [Migrating from Elasticsearch Plug-in](../elasticsearch-connector/current/migration.md)

Kafka

* [Get Started](../kafka-connector/current/quickstart.md)
* [Source Configuration](../kafka-connector/current/source-configuration-options.md)
* [Sink Configuration](../kafka-connector/current/sink-configuration-options.md)
* [Sample Application with Kafka Steams](../kafka-connector/current/streams-sample.md)

Spark

* [Get Started](../spark-connector/current/getting-started.md)
* [Development Workflow](../spark-connector/current/dev-workflow.md)
* [Java API](../spark-connector/current/java-api.md)
* [PySpark](../spark-connector/current/pyspark.md)

ODBC and JDBC Drivers

ODBC and JDBC drivers enable any application based on the ODBC/JDBC standards, for example Microsoft Excel, QlikView, SAP Lumira, or Tableau, to connect to a Couchbase Server or cluster. [ODBC and JDBC Drivers](../server/current/connectors/odbc-jdbc-drivers.md)

###### 

## Couchbase Community

###### 

Community Help

In addition to the Couchbase [Support Team](https://www.couchbase.com/support-policy), help can be found from the community in our [forums](https://forums.couchbase.com/), and on our official [Couchbase Discord server](https://discord.com/invite/K7NPMPGrPk?utm%5Fsource=forums&utm%5Fmedium=post&utm%5Fcampaign=discord).

###### 

Integrations

Information on some 3rd-party SDK integrations, such as [Spring Data](../java-sdk/current/project-docs/compatibility.md#spring-compat), can be found in the SDK docs.

###### 

Tutorials

The [developer bootstrap exercises and other tutorials](https://docs.couchbase.com/tutorials/quick-start/quickstart-java3-native-intellij-firstquery-cb65.html) highlight the use of Couchbase SDKs in the stacks you are most likely to use in development, such as Spring Data, Node Ottoman, and Python Flask.