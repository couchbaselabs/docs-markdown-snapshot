---
title: Enterprise Analytics Release Notes
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/release-notes/pages/release-notes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:release-notes:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/release-notes/release-notes.html)

# Enterprise Analytics Release Notes

## [](#release-2-1-november-2025)Release 2.1 (November 2025)

Enterprise Analytics 2.1, a self-managed version, was released in November 2025\. This release contains the following features:

* Microsoft Azure Support for Enterprise Analytics

  * Enterprise Analytics expands deployment flexibility by introducing native support for Microsoft Azure. Customers can now use Azure Blob Storage as the storage layer for their deployments.  
  For more information, see [Azure Blob Storage](../manage/manage-nodes/azure-blob-storage.md).
  * External collections now support Azure Blob Storage. This feature allows external query access, enabling direct querying of data files residing in external object storage, without requiring data movement.  
  For more information, see [Set Up an External Data Source](../sources/manage-external.md).
  * The COPY TO statement can now write processed data back to Azure Blob Storage.  
  For more information, see [COPY TO External Data Store Statements](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fexternal.md).
* Unlimited column support  
Enterprise Analytics removes previous constraints on schema width by introducing unlimited column support.  
For more information, see [View Metadata for a Collection](../sources/manage-collections.md#view-metadata-for-a-collection).
* Data transformation during ingestion  
Enterprise Analytics introduces the ability to perform lightweight data transformations directly during ingestion using SQL++ User-Defined Functions (UDFs).  
For more information, see [User-Defined Functions](../sqlpp/9%5Fudf.md).

## [](#release-2-0-august-2025)Release 2.0 (August 2025)

Couchbase is pleased to announce the launch of Enterprise Analytics, our robust data management solution that enables developers and data platform teams to create responsive analytic applications that adapt to rapidly changing data needs. Enterprise Analytics delivers the powerful capabilities seen in our cloud offering, Capella Analytics (formerly Capella Columnar), but in a new form that’s optimized for on-premise and self-managed deployments.

Enterprise Analytics 2.0 includes the following features:

* A column-oriented, Log-Structured Merge (LSM) tree based storage engine built to deliver scalable analytic performance and capacity in customers’ on-premise and/or self-managed environments. Enterprise Analytics has a shared-nothing compute and shared-object storage architecture that allows customers to scale compute resources independently of storage.
* An enhanced MPP-based query engine, enabling scalable, real-time analytical query computation.
* A [cost-based query optimizer](../sqlpp/5b%5Fcbo.md) for improved query planning without user intervention.
* A [SQL++](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fkv.md) based path for writing the results of a query back to the Couchbase Operational data service to support adaptive applications.
* [Zero ETL](../sources/remote-kafka.md) for incoming data, with real-time ingestion capabilities powered by Confluent Kafka, that provide the ability to connect, capture, and extract data from nearly any database or application.
* Data Lakehouse capabilities that enable direct [querying from Amazon S3 and S3-compatible storage](../sources/manage-external.md), with support for formats including JSON, Parquet, Avro, CSV, TSV, and Delta tables, providing the ability for queries to combine external data with other data in Enterprise Analytics.
* Native SQL-based support for [Tableau, PowerBI, and Apache Superset](../query/bi.md) for building business reports, visualizations, and dashboards.