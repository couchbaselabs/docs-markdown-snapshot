---
title: About Capella Analytics
description: Capella Analytics is a JSON-native NoSQL analytical database with
  GenAI capabilities. Use it to bring data from multiple sources together and
  run complex analytical queries to get timely insights from data.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/intro/pages/intro.adoc
  xref: xref:analytics:intro:intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/intro/intro.html)

# About Capella Analytics

> Capella Analytics is a JSON-native NoSQL analytical database with GenAI capabilities. Use it to bring data from multiple sources together and run complex analytical queries to get timely insights from data. 

Capella Analytics brings the power of NoSQL to the world of analytics. This cloud database-as-a-service (DBaaS) integrates seamlessly with the Couchbase Capella cloud platform, enabling the creation of real-time, adaptive applications.

Traditionally, analyzing JSON data in NoSQL databases requires complex transformations (like flattening) to prepare it for analytics, causing delays and hindering real-time insights. Capella Analytics eliminates these ETL complexities by unifying operational and analytical data stores into a single platform. This enables Zero ETL, reducing costs, complexity, and improving time to insight.

![capella analytics architecture](_images/capella-analytics-architecture.png) 

Figure 1\. Capella Analytics Architecture

Capella Analytics offers the following features:

* A column-oriented, Log-Structured Merge (LSM) plus B-tree structured storage engine built to expand the analytic performance and capacity of Capella. Its data is stored in cloud object stores, and separated from computation features.
* An enhanced MPP-based computation engine, allowing for real-time calculations regardless of data size.
* Zero ETL and real-time ingestion capabilities powered by Confluent Kafka and Amazon Manage Streaming for [Apache Kafka](../sources/remote-kafka.md) (MSK), which provide the ability to connect, capture, and extract data from nearly any database or application. This process also transforms the extracted data into developer-friendly JSON structures while in transit.
* File-based reads, imports and exports for data stored in cloud object stores including JSON, Parquet, Avro, TSV, and CSV.
* Reading Delta tables stored in S3 is supported.
* Conversational coding using [Capella iQ](../query/iq.md), to allow developers to use the power of a large language model (LLM) for SQL++ development.
* Native support for [Tableau and PowerBI](../query/bi.md) for analytic development and visualization.

> [!TIP]
> Capella Analytics SDKs
> 
> Capella Analytics SDKs for the Java, Node.js, and Python platforms are available [here](../../home/columnar-sdk.md).

## [](#next-steps)Next Steps

If you have not already created an account, [create an account for Couchbase Capella](../../cloud/get-started/create-account.md#sign-up-free-trial) and return to the Capella Analytics documentation for next steps. You do not have to deploy a Couchbase operational database or App Services trial to use Capella Analytics.

Get Started

* [Create a Cluster](../admin/prepare-project.md)
* [Access Data](examples.md)

Analyze

* [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md)
* [Query and Explore with the Workbench](../query/workbench.md)
* [Work with Query Results](../query/results.md)