---
title: Set Up an External Data Source
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/manage-external.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:sources:manage-external.adoc[]
---

[View original HTML](/analytics/sources/manage-external.html)

# Set Up an External Data Source

> To provide query access to data that resides in external object storage, you create an external link and associate it with an external collection. 

## [](#supported-external-sources)Supported External Sources

Capella Analytics supports external links to data in [Amazon S3](external-s3.md) and [GCS](external-gcs.md). This data remains in the storage bucket—​Capella Analytics does not copy it into a collection. You can query `Delta` tables residing in S3 buckets or GCS buckets that are in one of the following formats:

* JSON
* CSV
* TSV
* Parquet
* Avro