---
title: Set Up an External Data Source
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sources/pages/manage-external.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sources:manage-external.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sources/manage-external.html)

# Set Up an External Data Source

> To provide query access to data that resides in external object storage, you create an external link and associate it with an external collection. 

## [](#supported-external-sources)Supported External Sources

Enterprise Analytics supports external links to the following object storage providers:

* Amazon S3
* S3-compatible object stores
* Azure Blob Storage
* Google Cloud Storage (GCS)

This data remains in the source location — Enterprise Analytics does not copy it into a collection. You can query Delta tables residing in S3 buckets, S3 objects, or Azure Blob Storage containers, in one of the following formats:

* JSON
* CSV
* TSV
* Parquet
* Avro

## [](#apache-iceberg)Apache Iceberg

Enterprise Analytics also supports read-only access to Apache Iceberg tables through external catalogs. Unlike S3 external collections, Iceberg tables are registered via a catalog entity rather than a direct link to object storage.

To query Iceberg data:

1. Register a catalog using [CREATE CATALOG](../sqlpp/5%5Fddl%5Ficeberg%5Fcatalog.md).
2. Register an Iceberg table on that catalog using [CREATE EXTERNAL COLLECTION](../sqlpp/5%5Fddl%5Ficeberg%5Ftable.md).

See [Iceberg Support](../sqlpp/5%5Fddl%5Ficeberg.md) for the full list of supported catalog types and prerequisites.

## [](#creating-a-link-with-an-sdk)Creating a Link with an SDK

Enterprise Analytics uses different types of links to store credentials for accessing different types of data sources. You can use the UI to create links.

To create a link with an SDK, note the following:

* External: in an SDK, you use the `S3ExternalAnalyticsLink` class and then the `AnalyticsIndexManager` class to create the link.

For more information about data sources, see [Access and Organize Data in Enterprise Analytics](database-objects.md).

## [](#see-also)See Also

* [Query Data in Amazon S3](external-s3.md)
* [Query Data in Azure Blob Storage](external-azureblob.md)
* [Query Data in Google Cloud Storage (GCS)](external-gcs.md)
* [Design a Location Path](dynamic-prefixes.md)
* [Iceberg Tables](../sqlpp/5%5Fddl%5Ficeberg.md)