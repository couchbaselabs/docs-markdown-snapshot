---
title: Enterprise Analytics Release Notes
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/release-notes/pages/release-notes.adoc
pubDate: 2026-04-21T05:28:09.835Z
link: xref:enterprise-analytics:release-notes:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/release-notes/release-notes.html)

# Enterprise Analytics Release Notes

## [](#release-2-1-1-april-2026)Release 2.1.1 (April 2026)

Enterprise Analytics 2.1.1 is a maintenance release that delivers new features, targeted improvements, and bug fixes including critical stability and security patches.

### [](#whats-new)What's New

* Support for Oracle Cloud Infrastructure (OCI) Object Storage  
Enterprise Analytics adds OCI Object Storage as a native storage layer, providing greater deployment flexibility for Oracle-native environments.  
For more information, see [S3-Compatible Storage](../manage/manage-nodes/s3-compatible-storage.md).
* Custom Certificate Authority (CA) Support  
You can now configure custom CA certificates for secure HTTPS connections to S3-compatible storage using private PKI or self-signed certificates.  
For more information, see [Configure Enterprise Analytics](../manage/manage-nodes/create-cluster.md#configure-couchbase-server).
* Simplified Storage Authentication  
To simplify cluster provisioning and credential rotation, Enterprise Analytics now supports direct configuration of storage credentials via the UI/REST API as an alternative to the default credential chain for S3 & S3-compatible storage.  
For more information, see [Configure Enterprise Analytics](../manage/manage-nodes/create-cluster.md#configure-couchbase-server).

### [](#fixed-issues-improvements)Fixed Issues & Improvements

| Category                                | Topic                                                                                                                                                                                           | Description                                                                                                                                                            | Issue                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Storage & Connectivity                  | Stale DNS entries on reconnect                                                                                                                                                                  | The cluster retry logic is updated to re-resolve DNS addresses on every attempt. This prevents extended retry loops on stale IPs, ensuring faster connection recovery. | [MB-70678](https://jira.issues.couchbase.com/browse/MB-70678) |
| Blob storage heartbeat timeout extended | Enhanced system stability in overloaded production environments by extending the blob storage heartbeat timeout, reducing the likelihood of unnecessary service halts.                          | [MB-71270](https://jira.issues.couchbase.com/browse/MB-71270)                                                                                                          |                                                               |
| Blob verification timeouts on Azure     | CloudGuardian blob verification timeouts during high load caused node halts, leaving the cluster in an unusable state. Timeout handling has been improved to prevent this under sustained load. | [MB-71392](https://jira.issues.couchbase.com/browse/MB-71392)                                                                                                          |                                                               |
| Query Engine & Indexes                  | Per-micro operator profiling for subplans                                                                                                                                                       | Query execution profiles now include per-micro operator timing for nested subplans, providing more granular performance diagnostics.                                   | [MB-67666](https://jira.issues.couchbase.com/browse/MB-67666) |
| Improved OR predicate index utilization | Queries using OR predicates can now leverage secondary indexes more effectively, improving performance in disjunctive workloads.                                                                | [MB-70726](https://jira.issues.couchbase.com/browse/MB-70726)                                                                                                          |                                                               |
| Metrics & Monitoring                    | Workbench metrics panel improvements                                                                                                                                                            | The Enterprise Analytics Workbench now shows compilation time and adds a Copy Metrics button to easily export query metrics.                                           | [MB-71071](https://jira.issues.couchbase.com/browse/MB-71071) |

### [](#known-issues)Known Issues

| Category               | Topic                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Issue                                                         |
| ---------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Storage & Connectivity | Static credential rotation after driver restart | When blob storage credentials, such as AWS\_ACCESS\_KEY\_ID or AWS\_SECRET\_ACCESS\_KEY, are updated, the Analytics service continues to use the previously cached credentials after a driver restart. This is caused by the environment being cached across Analytics driver starts, preventing updated credentials from being picked up. **Workaround:** Restart the cbas process to force the new credentials to take effect. For example: pkill -9 cbas. | [MB-71496](https://jira.issues.couchbase.com/browse/MB-71496) |

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

Couchbase is pleased to announce the launch of Enterprise Analytics, our robust data management solution that enables developers and data platform teams to create responsive analytic applications that adapt to rapidly changing data needs. Enterprise Analytics delivers the powerful capabilities seen in our cloud offering, Capella Analytics (formerly Capella Columnar), but in a new form that's optimized for on-premise and self-managed deployments.

Enterprise Analytics 2.0 includes the following features:

* A column-oriented, Log-Structured Merge (LSM) tree based storage engine built to deliver scalable analytic performance and capacity in customers' on-premise and/or self-managed environments. Enterprise Analytics has a shared-nothing compute and shared-object storage architecture that allows customers to scale compute resources independently of storage.
* An enhanced MPP-based query engine, enabling scalable, real-time analytical query computation.
* A [cost-based query optimizer](../sqlpp/5b%5Fcbo.md) for improved query planning without user intervention.
* A [SQL++](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fkv.md) based path for writing the results of a query back to the Couchbase Operational data service to support adaptive applications.
* [Zero ETL](../sources/remote-kafka.md) for incoming data, with real-time ingestion capabilities powered by Confluent Kafka, that provide the ability to connect, capture, and extract data from nearly any database or application.
* Data Lakehouse capabilities that enable direct [querying from Amazon S3 and S3-compatible storage](../sources/manage-external.md), with support for formats including JSON, Parquet, Avro, CSV, TSV, and Delta tables, providing the ability for queries to combine external data with other data in Enterprise Analytics.
* Native SQL-based support for [Tableau, PowerBI, and Apache Superset](../query/bi.md) for building business reports, visualizations, and dashboards.