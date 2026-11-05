---
title: Set Up an External Data Source
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/manage-external.adoc
  xref: xref:analytics:sources:manage-external.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/sources/manage-external.html)

# Set Up an External Data Source

> To provide query access to data that resides in external object storage, you create an external link and associate it with an external collection. 

## [](#supported-external-sources)Supported External Sources

Operational Insights supports external links to data in [Amazon S3](external-s3.md), [GCS](external-gcs.md), and [Azure Blob Storage](external-azure.md). This data remains in the storage bucket or container—​Operational Insights does not copy it into a collection. You can query `Delta` tables residing in S3 buckets, GCS buckets, or Azure Blob Storage containers that are in one of the following formats:

* JSON
* CSV
* TSV
* Parquet
* Avro

## [](#apache-iceberg)Apache Iceberg

Operational Insights also supports read-only access to Apache Iceberg tables through external catalogs. Unlike S3 and GCS external collections, Iceberg tables are registered through a catalog entity rather than a direct link to object storage.

To query Iceberg data:

1. Register a catalog using [CREATE CATALOG](../sqlpp/5%5Fddl%5Ficeberg%5Fcatalog.md).
2. Register an Iceberg table on that catalog using [CREATE EXTERNAL COLLECTION](../sqlpp/5%5Fddl%5Ficeberg%5Ftable.md).

See [Iceberg Tables](../sqlpp/5%5Fddl%5Ficeberg.md) for the full list of supported catalog types and prerequisites.