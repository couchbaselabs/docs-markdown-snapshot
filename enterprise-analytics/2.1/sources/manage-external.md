---
title: Set Up an External Data Source
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/manage-external.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:sources:manage-external.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sources/manage-external.html)

# Set Up an External Data Source

> To provide query access to data that resides in external object storage, you create an external link and associate it with an external collection. 

## [](#supported-external-sources)Supported External Sources

Enterprise Analytics supports external links to the following:

* Amazon S3
* S3-compatible object stores
* Azure Blob Storage

This data remains in the source location—​Enterprise Analytics does not copy it into a collection. You can query `Delta` tables residing in S3 buckets, S3 objects, or Azure Blob Storage containers, that are in one of the following formats:

* JSON
* CSV
* TSV
* Parquet
* Avro

## [](#creating-a-link-with-an-sdk)Creating a Link with an SDK

Enterprise Analytics uses different types of links to store credentials for accessing different types of data sources. You can use the UI to create links.

To create a link with an SDK, note the following:

* External: in an SDK, you use the `S3ExternalAnalyticsLink` class and then the `AnalyticsIndexManager` class to create the link.

For more information about data sources, see [Access and Organize Data in Enterprise Analytics](database-objects.md).

## [](#see-also)See Also

* [Query Data in External Data Sources](external-s3.md)
* [Design a Location Path](dynamic-prefixes.md)