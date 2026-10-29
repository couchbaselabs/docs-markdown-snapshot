---
title: About Operational Insights Enterprise
description: Operational Insights Enterprise is a self-managed, JSON-native
  NoSQL analytical database that unifies data from diverse sources for complex
  analytical queries and timely insights.
pubDate: 2026-10-29T04:27:04.379Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/intro/pages/intro.adoc
  xref: xref:enterprise-analytics:intro:intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/intro/intro.html)

# About Operational Insights Enterprise

> Operational Insights Enterprise is a self-managed, JSON-native NoSQL analytical database that unifies data from diverse sources for complex analytical queries and timely insights. 

Operational Insights integrates seamlessly with both Couchbase Server and the Couchbase Capella cloud platform, enabling the creation of real-time, adaptive applications.

Traditionally, analyzing JSON data in NoSQL databases requires complex transformations, like flattening, to prepare it for analytics, causing delays and hindering real-time insights. Operational Insights eliminates these ETL complexities by using a unifying JSON data model with schema flexibility. This allows data to fluidly evolve at its source without requiring manual schema or transformation management. This facilitates a Zero ETL environment, leading to faster time to insight, reduced costs, and increased agility.

## [](#supported-platforms-and-infrastructure)Supported Platforms and Infrastructure

You deploy and manage Operational Insights on premises or in your own cloud environment.

### [](#operating-systems)Operating Systems

* Red Hat Enterprise Linux (RHEL) 10.x, 9.x, and 8.x
* Ubuntu 24.04 Long Term Support (LTS) and 22.x LTS (x86 and ARM64)
* Debian 12.x

### [](#object-storage)Object Storage

* Amazon S3
* Azure Blob Storage
* Google Cloud Storage (GCS)
* Any S3-compatible storage

For details, see [Supported Object Storage Solutions](../install/supported-object-storage.md).

### [](#system-resources)System Resources

Resource requirements depend on the size and resource demands of your deployment.

Processors

Supports x86 on all platforms, and ARM64 on Ubuntu.

Hardware and sizing

Compute and memory scale based on your data volume and workload demands. For minimum and recommended node specifications, see [System Resource Requirements](../install/sys-resource-req.md).

Storage and network

Requires adequate disk throughput for temporary query spilling and open ports for intra-cluster communication.

## [](#key-features)Key Features

Operational Insights offers the following features:

Column-oriented storage

A storage engine delivers scalable analytic performance and capacity for self-managed, on-premises or cloud deployments, by reading only the columns a query needs.

Independent scaling of compute and storage

A shared-nothing compute and shared-object storage architecture lets you scale compute resources independently of storage.

Massively parallel query processing

An MPP-based query engine runs analytical queries across all nodes in parallel, for scalable, real-time results.

Cost-based query optimization

A cost-based optimizer chooses efficient query plans using statistics gathered by `ANALYZE COLLECTION`.

Zero ETL and real-time ingestion

Stream data in real time from Couchbase Server, Couchbase Capella, and nearly any other database or application through Kafka. Analyze incoming data in its native JSON form, with no flattening or transformation pipelines, and optionally modify the target JSON structure while data is in transit.

Data Lakehouse queries

Query data directly in supported object storage, in JSON, Parquet, Avro, CSV, TSV, Delta table, and Apache Iceberg formats, with Iceberg tables accessed through [Iceberg catalogs](../sqlpp/5%5Fddl%5Ficeberg.md). A single query can combine external data with data already in Operational Insights.

Write-back to the operational database

Use SQL++ to write query results back to the Couchbase operational data service, to support adaptive applications.

BI tool support

Tabular views give Tableau, Power BI, and Apache Superset native SQL-based access, for building business reports, visualizations, and dashboards.

Vector search

Create a vector index for approximate nearest neighbor (ANN) search over embeddings, and use the `CLUSTER BY` clause to group embeddings by similarity.

Python UDFs

Extend SQL with Python functions running in an isolated sandbox, to bring a trained ML model into a query or implement logic that's hard to express in SQL.

Query plan caching

Operational Insights reuses a cached execution plan for a repeated query, skipping the optimization step to start executing faster.

## [](#data-sources-and-connections)Data Sources and Connections

Operational Insights brings in data from operational databases, streaming platforms, and object storage. You query and visualize that data with [SQL++](../sqlpp/1%5Fintro.md), SDKs, and BI tools.

### [](#data-sources)Data Sources

* Couchbase Server and Couchbase Capella operational databases.
* Kafka, to stream data from other databases or applications.
* Files in supported object storage, in JSON, Parquet, Avro, CSV, TSV, and Delta formats.
* Delta Lake tables and Apache Iceberg tables through Iceberg catalogs.

### [](#clients-and-tools)Clients and Tools

> [!TIP]
> Operational Insights SDKs
> 
> Operational Insights SDKs for the .NET, Go, Java, Node.js, and Python platforms are available [here](../../../home/operational-insights-sdk.md).

* [BI tools](../query/bi.md): Tableau, Power BI, and Apache Superset, through tabular views.

For setup steps, see [Manage Links](../sources/manage-links.md).

## [](#getting-started)Getting Started

* [Quick Start with Docker](do-a-quick-install.md)
* [Set up a Cluster](../manage/manage-nodes/create-cluster.md#set-up-a-new-cluster)
* [Configure Operational Insights](../manage/manage-nodes/create-cluster.md#configure-couchbase-server)
* [Quick Start Tutorial](connecting-to-data-sources.md)

## [](#see-also)See Also

* [Supported Platforms](../install/supported-platform.md)
* [Supported Object Storage Solutions](../install/supported-object-storage.md)
* [System Resource Requirements](../install/sys-resource-req.md)
* [Operational Insights Ports](../install/cb-operational-insights-ports.md)
* [Data Model & Hierarchy](../sources/database-objects.md)
* [Query Performance Optimization](../reference/query-performance.md)