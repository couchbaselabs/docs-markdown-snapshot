---
title: CREATE EXTERNAL COLLECTION on a Catalog
description: Use <code>CREATE EXTERNAL COLLECTION</code> to register an Iceberg
  table from an external catalog in Operational Insights, enabling SQL++ queries
  against the data in object storage.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/5_ddl_iceberg_table.adoc
  xref: xref:analytics:sqlpp:5_ddl_iceberg_table.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/sqlpp/5_ddl_iceberg_table.html)

# CREATE EXTERNAL COLLECTION on a Catalog

> Use `CREATE EXTERNAL COLLECTION` to register an Iceberg table from an external catalog in Operational Insights, enabling SQL++ queries against the data in object storage. 

An external collection created on an Iceberg [catalog](5%5Fddl%5Ficeberg%5Fcatalog.md) maps to a specific table in that catalog. The collection name is used in queries and does not need to match the Iceberg table name, which is supplied in the `WITH` clause. The link in the `AT` clause is used to read data files in object storage, and may differ from the link used to authenticate the catalog.

For an overview of supported catalog types and authentication, see [Iceberg Tables](5%5Fddl%5Ficeberg.md).

> [!NOTE]
> To read data from external cloud storage, exclusive permissions are required. For more information, see [AWS](../sources/required-permissions-aws.md) and [GCS](../sources/required-permissions-gcs.md).

## [](#syntax)Syntax

```SQL++
CREATE EXTERNAL COLLECTION <collection-name>
ON <catalog-name>
AT <link-name>
WITH {
    "table-format": "iceberg",
    "tableName": "<iceberg-table-name>",
    "namespace": "<iceberg-namespace>"
    [, "decimal-to-double": "true" ]
    [, "date-to-int": "true" ]
    [, "time-to-int": "true" ]
    [, "timestamp-to-long": "true" ]
    [, "snapshotId": "<snapshot-id>" ]
    [, "snapshotTimestamp": "<timestamp-ms>" ]
};
```

## [](#arguments)Arguments

collection-name

The name of the collection in Operational Insights. Used in queries — does not need to match the Iceberg table name.

ON catalog-name

The name of the [catalog](5%5Fddl%5Ficeberg%5Fcatalog.md) this collection is created on.

AT link-name

The link used to read data files in object storage. This may differ from the link used when creating the catalog.

WITH

A JSON object with the following properties.

| Property              | Description                                                                                                                                                                                                                                                                                                                                                              | Required |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **table-format**      | The table format type. Must be "iceberg".                                                                                                                                                                                                                                                                                                                                | Yes      |
| **tableName**         | The actual Iceberg table name in the catalog.                                                                                                                                                                                                                                                                                                                            | Yes      |
| **namespace**         | The Iceberg namespace the table belongs to.                                                                                                                                                                                                                                                                                                                              | Yes      |
| **decimal-to-double** | When "true", converts Iceberg DECIMAL types to DOUBLE. Operational Insights does not support the DECIMAL type. If the data contains decimal values, set this property to "true".                                                                                                                                                                                         | No       |
| **date-to-int**       | When "true", returns Iceberg DATE values as INTEGER (epoch days since 1970-01-01) rather than the native DATE type.                                                                                                                                                                                                                                                      | No       |
| **time-to-int**       | When "true", returns Iceberg TIME values as INTEGER (milliseconds since midnight) rather than the native TIME type.                                                                                                                                                                                                                                                      | No       |
| **timestamp-to-long** | When "true", returns Iceberg TIMESTAMP and TIMESTAMP\_NANO values as BIGINT rather than DATETIME. TIMESTAMP returns microseconds since epoch. TIMESTAMP\_NANO returns nanoseconds since epoch. DATETIME is parsed at millisecond precision — set this to "true" if microsecond or nanosecond precision is required.                                                      | No       |
| **snapshotId**        | Snapshot ID to pin this collection to for time travel. Cannot be used together with snapshotTimestamp. See [Use Time Travel](5%5Fddl%5Ficeberg.md#use-time-travel).                                                                                                                                                                                                      | No       |
| **snapshotTimestamp** | Snapshot timestamp to pin this collection to. Accepts milliseconds since Unix epoch, a date string in yyyy-MM-dd format, or a datetime string in yyyy-MM-ddTHH:mm:ss format. Operational Insights reads from the most recent snapshot at or before this timestamp. Cannot be used together with snapshotId. See [Use Time Travel](5%5Fddl%5Ficeberg.md#use-time-travel). | No       |

## [](#example)Example

```SQL++
CREATE EXTERNAL COLLECTION usersTable
ON myGlueCatalog
AT myS3Link
WITH {
    "table-format": "iceberg",
    "namespace": "pharmacy_namespace",
    "tableName": "users",
    "decimal-to-double": "true"
};
```

## [](#see-also)See Also

* [Filtration](5%5Fddl%5Ficeberg.md#filtration)
* [Iceberg Tables](5%5Fddl%5Ficeberg.md)
* [Create a Catalog](5%5Fddl%5Ficeberg%5Fcatalog.md)
* [Set Up an External Data Source](../sources/manage-external.md)
* [Cost-Based Optimizer](5b%5Fcbo.md)