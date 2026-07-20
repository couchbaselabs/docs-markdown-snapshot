---
title: Set Up an External Data Source
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/manage-external.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:analytics:sources:manage-external.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/manage-external.html)

# Set Up an External Data Source

> To provide query access to data that resides in external object storage, you create an external link and associate it with an external collection. 

## [](#supported-external-sources)Supported External Sources

Capella Analytics supports external links to data in [Amazon S3](external-s3.md), [GCS](external-gcs.md), and [Azure Blob Storage](external-azure.md). This data remains in the storage bucket or container—​Capella Analytics does not copy it into a collection. You can query `Delta` tables residing in S3 buckets, GCS buckets, or Azure Blob Storage containers that are in one of the following formats:

* JSON
* CSV
* TSV
* Parquet
* Avro