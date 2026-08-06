---
title: Iceberg Tables
description: Enterprise Analytics provides read-only query access to Apache
  Iceberg tables through external catalogs, enabling unified queries across data
  lake and operational data without moving data.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_ddl_iceberg.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sqlpp:5_ddl_iceberg.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_iceberg.html)

# Iceberg Tables

> Enterprise Analytics provides read-only query access to Apache Iceberg tables through external catalogs, enabling unified queries across data lake and operational data without moving data. 

Apache Iceberg is a high-performance open table format for large-scale analytic datasets. Enterprise Analytics connects to Iceberg catalogs to query Iceberg tables stored in external object storage — such as AWS S3, GCS, and Azure Blob Storage — using existing [links](../sources/manage-links.md) for authentication.

To get started, use [CREATE CATALOG](5%5Fddl%5Ficeberg%5Fcatalog.md) to register an Iceberg catalog, then use [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md) to expose individual Iceberg tables for querying.

## [](#iceberg-concepts)Iceberg Concepts

* [Catalog](#catalog)
* [Namespace](#namespace)
* [Data Files](#data-files)

### [](#catalog)Catalog

An Iceberg catalog is a metadata registry that maps table names to their metadata files. It manages table locations and handles create, drop, load, and list operations on tables.

In Enterprise Analytics, a catalog is a named entity registered with [CREATE CATALOG](5%5Fddl%5Ficeberg%5Fcatalog.md). Catalogs are globally unique and do not belong to an Analytics database.

### [](#namespace)Namespace

Namespaces logically group Iceberg tables within a catalog, similar to a database or schema in relational systems. A catalog can contain multiple namespaces, and namespaces can be nested.

catalog_name
├── namespace1
│   ├── table1
│   └── table2
└── namespace2
    └── table3

When creating an external collection on a catalog, you specify the namespace and table name in the `WITH` clause. For more information, see [CREATE EXTERNAL COLLECTION on a Catalog](5%5Fddl%5Ficeberg%5Ftable.md).

### [](#data-files)Data Files

The data files managed by Iceberg are stored in external object storage. Enterprise Analytics supports the following Iceberg data file formats:

| Format  | Support   |
| ------- | --------- |
| Parquet | Supported |

## [](#supported-catalog-types)Supported Catalog Types

| Source             | Description                                                                               | Required Link |
| ------------------ | ----------------------------------------------------------------------------------------- | ------------- |
| AWS\_GLUE          | AWS Glue Data Catalog — the centralized metadata repository in the AWS ecosystem.         | AWS link      |
| AWS\_GLUE\_REST    | AWS Glue accessed via the Iceberg REST endpoint, using Sigv4-signed credentials.          | AWS link      |
| S3\_TABLES         | Amazon S3 Tables — a managed Iceberg table bucket on Amazon S3.                           | AWS link      |
| BIGLAKE\_METASTORE | Google BigLake Metastore — GCP managed metadata service with an Iceberg REST catalog API. | GCS link      |
| NESSIE             | Nessie — an open source catalog with Git-like branching semantics.                        | HTTP link     |
| NESSIE\_REST       | Nessie accessed via its REST catalog implementation.                                      | HTTP link     |
| REST               | REST-compatible Iceberg catalogs.                                                         | HTTP link     |

## [](#supported-storage-locations)Supported Storage Locations

Iceberg data files can reside in the following object storage locations:

* AWS S3
* Google Cloud Storage (GCS)
* Azure Blob Storage

## [](#types-mapping)Types Mapping

The following table describes the type mapping between Iceberg types and Enterprise Analytics types:

| Iceberg Type    | Enterprise Analytics Type         | Comments                                                                                                                   |
| --------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| BOOLEAN         | BOOLEAN                           |                                                                                                                            |
| INTEGER         | BIGINT                            |                                                                                                                            |
| LONG            | BIGINT                            |                                                                                                                            |
| FLOAT           | FLOAT                             |                                                                                                                            |
| DOUBLE          | DOUBLE                            |                                                                                                                            |
| STRING          | STRING                            |                                                                                                                            |
| UUID            | UUID                              |                                                                                                                            |
| FIXED           | BINARY                            |                                                                                                                            |
| BINARY          | BINARY                            |                                                                                                                            |
| DECIMAL         | Not supported                     | Can be parsed as DOUBLE. See \[1\].                                                                                        |
| STRUCT          | OBJECT                            |                                                                                                                            |
| LIST            | ARRAY                             |                                                                                                                            |
| MAP             | ARRAY                             | ARRAY of key/value OBJECT pairs. Example: \[ { "key": "key1", "value": "value1" }, { "key": "key2", "value": "value2" } \] |
| DATE            | DATE                              | Can be converted to INTEGER (epoch days since 1970-01-01). See \[3\].                                                      |
| TIME            | TIME                              | Can be converted to INTEGER (milliseconds since midnight). See \[4\].                                                      |
| TIMESTAMP       | DATETIME (milliseconds precision) | Can be converted to BIGINT (microseconds since epoch). See \[2\].                                                          |
| TIMESTAMP\_NANO | DATETIME (milliseconds precision) | Can be converted to BIGINT (nanoseconds since epoch). See \[2\].                                                           |
| GEOMETRY        | Not supported                     |                                                                                                                            |
| GEOGRAPHY       | Not supported                     |                                                                                                                            |
| VARIANT         | Not supported                     |                                                                                                                            |
| UNKNOWN         | Not supported                     |                                                                                                                            |

\[1\] `DECIMAL` is not natively supported in Enterprise Analytics. To parse `DECIMAL` values as `DOUBLE`, set `decimal-to-double` to `"true"` in [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md). If `decimal-to-double` is not set, Enterprise Analytics returns an error: `Decimal is not supported. To parse it as DOUBLE, set decimal-to-double to true.`This property is not enabled by default because it's a temporary workaround. When Enterprise Analytics adds native `DECIMAL` support, this property is no longer required.

\[2\] Enterprise Analytics parses datetime types to milliseconds precision. To return the original long value (microseconds since epoch for `TIMESTAMP`, nanoseconds since epoch for `TIMESTAMP_NANO`), set `timestamp-as-long` to `"true"` in [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md).

\[3\] To return `DATE` as `INTEGER` (epoch days since 1970-01-01), set `date-as-int` to `"true"` in [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md).

\[4\] To return `TIME` as `INTEGER` (milliseconds since midnight), set `time-as-int` to `"true"` in [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md).

## [](#query-iceberg-tables)Query Iceberg Tables

1. **Create Authentication Links** — Create one or more [links](../sources/manage-links.md) to authenticate access to the Iceberg catalog and the underlying object storage. The catalog and data file locations can use the same link or different links, depending on your setup and permissions.  
> [!NOTE]  
> The link used to authenticate the catalog and the link used to read the data files can differ. For example, a Nessie catalog may use an HTTP link for catalog authentication while the underlying data files are stored in S3 and require an AWS link.
2. **Register the Iceberg Catalog** — Use [CREATE CATALOG](5%5Fddl%5Ficeberg%5Fcatalog.md) to connect Enterprise Analytics to a supported Iceberg catalog. Once registered, the catalog is available globally in Enterprise Analytics and automatically appears in the Analytics Workbench UI.
3. **Create an External Collection** — Use [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md) to expose an Iceberg table for querying. Once created, the Iceberg table can be queried using SQL++ in the same way as any external collection.

## [](#filtration)Filtration

When Enterprise Analytics reads an Iceberg table, the following filtrations are applied in order:

1. Only the files belonging to the specified table are scanned — no other table's files are accessed.
2. If a `WHERE` clause is provided, Enterprise Analytics applies predicates to perform partition pruning and manifest-level exclusion before reading data files.
3. Only columns referenced in the `SELECT` clause are projected — not all columns in the table are read.

Partition pruning, manifest-level exclusion, and column projection reduce the amount of data scanned for selective queries. See [Create an Iceberg Table](5%5Fddl%5Ficeberg%5Ftable.md) for details.

## [](#use-time-travel)Use Time Travel

Every write to an Iceberg table creates a new snapshot. Enterprise Analytics lets you query any past snapshot of an Iceberg external collection using `AT SNAPSHOT` or `AT TIMESTAMP` in a SQL++ statement, without modifying the collection definition. You can also pin a collection to a specific snapshot permanently by setting `snapshotId` or `snapshotTimestamp` in [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md).

### [](#at-timestamp)AT TIMESTAMP

Returns data from the most recent snapshot at or before the specified timestamp.

```SQL++
SELECT * FROM <collection-name> AT TIMESTAMP '<timestamp>'
```

The timestamp must be a string in one of the following formats:

* Milliseconds since Unix epoch: `'<ms-since-unix-epoch>'`
* Date: `'yyyy-MM-dd'`
* Datetime: `'yyyy-MM-ddTHH:mm:ss'`

Examples

```SQL++
SELECT * FROM usersTable AT TIMESTAMP '<ms-since-unix-epoch>'

SELECT * FROM usersTable AT TIMESTAMP '2022-07-01'

SELECT * FROM usersTable AT TIMESTAMP '2022-07-01T13:12:01'
```

### [](#at-snapshot)AT SNAPSHOT

Returns data from a specific snapshot by its ID.

```SQL++
SELECT * FROM <collection-name> AT SNAPSHOT '<snapshot-id>'
```

Example

```SQL++
SELECT * FROM usersTable AT SNAPSHOT '1339696213265401120'
```

### [](#listing-snapshots)Listing Snapshots

To find available snapshot IDs and timestamps, use the following data source functions or REST endpoints.

#### [](#data-source-functions)Data Source Functions

List all snapshots for an Iceberg external collection:

```SQL++
SELECT * FROM list_iceberg_snapshots("<database>", "<scope>", "<collection>") AS x;
```

List all catalogs, namespaces, and tables registered in Enterprise Analytics:

```SQL++
SELECT * FROM list_iceberg_catalogs() AS x;
SELECT * FROM list_iceberg_namespaces("<catalog-name>") AS x;
SELECT * FROM list_iceberg_tables("<catalog-name>", "<namespace>") AS x;
```

#### [](#rest-api)REST API

| Endpoint                                                                 | Description                                                          |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| GET /api/v1/iceberg/catalog/                                             | Returns all catalogs registered in Enterprise Analytics.             |
| GET /api/v1/iceberg/catalog/{catalogName}/namespace                      | Returns all namespaces in the specified catalog.                     |
| GET /api/v1/iceberg/catalog/{catalogName}/namespace/{namespace}/table    | Returns all tables in the specified namespace.                       |
| GET /api/v1/iceberg/snapshot/{databaseName}/{scopeName}/{collectionName} | Returns all snapshots for the specified Iceberg external collection. |

### [](#faq)FAQ

#### [](#can-you-use-both-snapshotid-and-snapshottimestamp-in-the-same-query)Can You Use Both `snapshotId` and `snapshotTimestamp` in the Same Query?

No — specify only one at a time. Providing both returns an error.

#### [](#what-snapshot-does-enterprise-analytics-read-if-no-snapshot-is-specified)What Snapshot Does Enterprise Analytics Read if No Snapshot Is Specified?

Enterprise Analytics reads from the latest snapshot of the table.

#### [](#whats-the-difference-between-a-query-level-snapshot-and-a-collection-level-snapshot)What's the Difference Between a Query-Level Snapshot and a Collection-Level Snapshot?

Setting `snapshotId` or `snapshotTimestamp` in [CREATE EXTERNAL COLLECTION](5%5Fddl%5Ficeberg%5Ftable.md) pins the collection to that snapshot permanently — all queries against that collection use it by default. Using `AT SNAPSHOT` or `AT TIMESTAMP` in a query overrides the collection-level setting for that query only.

#### [](#can-you-time-travel-on-a-collection-with-no-pinned-snapshot)Can You Time Travel on a Collection With No Pinned Snapshot?

Yes — `AT SNAPSHOT` and `AT TIMESTAMP` work on any Iceberg external collection regardless of whether a snapshot was set at creation time.

## [](#see-also)See Also

* [Create a Catalog](5%5Fddl%5Ficeberg%5Fcatalog.md)
* [Create an Iceberg Table](5%5Fddl%5Ficeberg%5Ftable.md)
* [Manage Links](../sources/manage-links.md)
* [Set Up an External Data Source](../sources/manage-external.md)