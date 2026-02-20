---
title: Enterprise Analytics Release Notes
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/release-notes/pages/release-notes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:release-notes:release-notes.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/release-notes/release-notes.html)

# Enterprise Analytics Release Notes

## [](#august-2025-changelog)August 2025 Changelog

Couchbase is pleased to announce the launch of Enterprise Analytics, our robust data management solution that enables developers and data platform teams to create responsive analytic applications that adapt to rapidly changing data needs. Enterprise Analytics delivers the powerful capabilities seen in our cloud offering, Capella Analytics (formerly Capella Columnar), but in a new form that’s optimized for on-premise and self-managed deployments.

Enterprise Analytics includes the following features:

* A column-oriented, Log-Structured Merge (LSM) tree based storage engine built to deliver scalable analytic performance and capacity in customers’ on-premise and/or self-managed environments. Enterprise Analytics has a shared-nothing compute and shared-object storage architecture that allows customers to scale compute resources independently of storage.
* An enhanced MPP-based query engine, enabling scalable, real-time analytical query computation.
* A [cost-based query optimizer](../sqlpp/5b%5Fcbo.md) for improved query planning without user intervention.
* A [SQL++](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fkv.md) based path for writing the results of a query back to the Couchbase Operational data service to support adaptive applications.
* [Zero ETL](../sources/remote-kafka.md) for incoming data, with real-time ingestion capabilities powered by Confluent Kafka, that provide the ability to connect, capture, and extract data from nearly any database or application.
* Data Lakehouse capabilities that enable direct [querying from Amazon S3 and S3-compatible storage](../sources/manage-external.md), with support for formats including JSON, Parquet, Avro, CSV, TSV, and Delta tables, providing the ability for queries to combine external data with other data in Enterprise Analytics.
* Native SQL-based support for [Tableau, PowerBI, and Apache Superset](../query/bi.md) for building business reports, visualizations, and dashboards.