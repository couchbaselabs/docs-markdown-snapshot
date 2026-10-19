---
title: Set Up an External Data Source
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sources/pages/manage-external.adoc
  xref: xref:enterprise-analytics:sources:manage-external.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sources/manage-external.html)

# Set Up an External Data Source

> To provide query access to data that resides in external object storage, you create an external link and associate it with an external collection. 

## [](#supported-external-sources)Supported External Sources

Operational Insights supports external links to the following object storage providers:

* Amazon S3
* S3-compatible object stores
* Azure Blob Storage
* Google Cloud Storage (GCS)

This data remains in the source location — Operational Insights does not copy it into a collection. You can query Delta tables residing in S3 buckets, S3 objects, or Azure Blob Storage containers, in one of the following formats:

* JSON
* CSV
* TSV
* Parquet
* Avro

## [](#apache-iceberg)Apache Iceberg

Operational Insights also supports read-only access to Apache Iceberg tables through external catalogs. Unlike S3 external collections, Iceberg tables are registered via a catalog entity rather than a direct link to object storage.

To query Iceberg data:

1. Register a catalog using [CREATE CATALOG](../sqlpp/5%5Fddl%5Ficeberg%5Fcatalog.md).
2. Register an Iceberg table on that catalog using [CREATE EXTERNAL COLLECTION](../sqlpp/5%5Fddl%5Ficeberg%5Ftable.md).

See [Iceberg Support](../sqlpp/5%5Fddl%5Ficeberg.md) for the full list of supported catalog types and prerequisites.

You can also register catalogs and Iceberg collections with the workbench, as described in [Set Up Iceberg Data with the Workbench](#iceberg-ui).

### [](#iceberg-ui)Set Up Iceberg Data with the Workbench

Before you begin, create the link or links that authenticate access to the catalog and to the object storage that holds its data files. See [Query Iceberg Tables](../sqlpp/5%5Fddl%5Ficeberg.md#query-iceberg-tables).

To register a catalog:

1. In the Web Console, click **Workbench** in the navigation bar.
2. In the explorer, next to **Catalogs**, click **\+ new catalog**. The **Create Catalog** dialog opens.
3. In **Catalog Name**, enter a name for the catalog. The **Catalog Type** is always **Iceberg**.
4. In **Catalog Source**, select the kind of catalog: **REST**, **AWS Glue**, **AWS Glue REST**, **S3 Tables**, **BigLake Metastore**, **Nessie**, or **Nessie REST**.
5. In **Link**, select the link that authenticates access to the catalog.
6. Complete the fields for the selected source, such as **URI**, **Warehouse**, **SigV4 Signing Name**, **SigV4 Signing Region**, or **Quota Project ID**. These correspond to the `WITH` properties for that source, described in [CREATE CATALOG](../sqlpp/5%5Fddl%5Ficeberg%5Fcatalog.md).
7. Optionally, under **Additional Parameters (Optional)**, click **\+ Add Parameter** to add any other property as a name and value pair.
8. Click **Save**.

The catalog appears under **Catalogs** in the explorer. Expand it to see its type, source, and link, or to drop it.

To add an Iceberg collection on a catalog:

1. In the explorer, under **Catalogs**, click **\+ collection** next to the catalog. The **Add Iceberg Collection** dialog opens.
2. Enter a **Collection Name**, and select the **Database** and **Scope** for the collection.
3. Select the Iceberg **Namespace** and **Table Name**. The lists are read from the catalog.
4. Optionally, select the type conversions to apply: **Decimal to Double**, **Timestamp to Long**, **Time to Int**, or **Date to Int**, and enter a **Timezone**. See [CREATE EXTERNAL COLLECTION](../sqlpp/5%5Fddl%5Ficeberg%5Ftable.md).
5. In **Link**, select the link that authenticates access to the table's data files.
6. Optionally, under **Time Travel**, pin the collection to a **Snapshot ID** or a **Snapshot Timestamp**.
7. Click **Save**.

## [](#creating-a-link-with-an-sdk)Creating a Link with an SDK

Operational Insights uses different types of links to store credentials for accessing different types of data sources. You can use the UI to create links.

To create a link with an SDK, note the following:

* External: in an SDK, you use the `S3ExternalAnalyticsLink` class and then the `AnalyticsIndexManager` class to create the link.

For more information about data sources, see [Data Model & Hierarchy](database-objects.md).

## [](#see-also)See Also

* [Query Data in Amazon S3](external-s3.md)
* [Query Data in Azure Blob Storage](external-azureblob.md)
* [Query Data in Google Cloud Storage (GCS)](external-gcs.md)
* [External Storage Data Organization](dynamic-prefixes.md)
* [Apache Iceberg](../sqlpp/5%5Fddl%5Ficeberg.md)