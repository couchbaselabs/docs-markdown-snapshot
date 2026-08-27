---
title: CREATE EXTERNAL COLLECTION on a Catalog
description: Use <code>CREATE EXTERNAL COLLECTION</code> to register an Iceberg
  table from an external catalog in Enterprise Analytics, enabling SQL++ queries
  against the data in object storage.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_ddl_iceberg_table.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_iceberg_table.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_iceberg_table.html)

# CREATE EXTERNAL COLLECTION on a Catalog

> Use `CREATE EXTERNAL COLLECTION` to register an Iceberg table from an external catalog in Enterprise Analytics, enabling SQL++ queries against the data in object storage. 

An external collection created on an Iceberg [catalog](5%5Fddl%5Ficeberg%5Fcatalog.md) maps to a specific table in that catalog. The collection name is used in queries and does not need to match the Iceberg table name, which is supplied in the `WITH` clause. The link in the `AT` clause is used to read data files in object storage, and may differ from the link used to authenticate the catalog.

For an overview of supported catalog types and authentication, see [Iceberg Support](5%5Fddl%5Ficeberg.md).

> [!NOTE]
> To read data from external cloud storage, exclusive permissions are required. For more information, see [Cloud Read/Write Permissions](../reference/cloud%5Fread%5Fwrite%5Fpermissions.md).

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
    [, "date-as-int": "true" ]
    [, "time-as-int": "true" ]
    [, "timestamp-as-long": "true" ]
    [, "snapshotId": "<snapshot-id>" ]
    [, "snapshotTimestamp": "<timestamp-ms>" ]
};
```

## [](#arguments)Arguments

collection-name

The name of the collection in Enterprise Analytics. Used in queries — does not need to match the Iceberg table name.

ON catalog-name

The name of the [catalog](5%5Fddl%5Ficeberg%5Fcatalog.md) this collection is created on.

AT link-name

The [link](../sources/manage-links.md) used to read data files in object storage. This may differ from the link used when creating the catalog.

WITH

A JSON object with the following properties.

| Property                      | Description                                                                                                                                                                                                                                                                                                         | Required |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| **table-format**Required      | The table format type. Must be "iceberg".                                                                                                                                                                                                                                                                           | Yes      |
| **tableName**Required         | The actual Iceberg table name in the catalog.                                                                                                                                                                                                                                                                       | Yes      |
| **namespace**Required         | The Iceberg namespace the table belongs to.                                                                                                                                                                                                                                                                         | Yes      |
| **decimal-to-double**Optional | When "true", converts Iceberg DECIMAL types to DOUBLE. Enterprise Analytics does not support the DECIMAL type. If the data contains decimal values, set this property to "true".                                                                                                                                    | No       |
| **date-as-int**Optional       | When "true", returns Iceberg DATE values as INTEGER (epoch days since 1970-01-01) rather than the native DATE type.                                                                                                                                                                                                 | No       |
| **time-as-int**Optional       | When "true", returns Iceberg TIME values as INTEGER (milliseconds since midnight) rather than the native TIME type.                                                                                                                                                                                                 | No       |
| **timestamp-as-long**Optional | When "true", returns Iceberg TIMESTAMP and TIMESTAMP\_NANO values as BIGINT rather than DATETIME. TIMESTAMP returns microseconds since epoch. TIMESTAMP\_NANO returns nanoseconds since epoch. DATETIME is parsed at millisecond precision — set this to "true" if microsecond or nanosecond precision is required. | No       |
| **snapshotId**Optional        | Snapshot ID to pin this collection to for time travel. Cannot be used together with snapshotTimestamp. See [Use Time Travel](5%5Fddl%5Ficeberg.md#use-time-travel).                                                                                                                                                 | No       |
| **snapshotTimestamp**Optional | Snapshot timestamp in milliseconds to pin this collection to. Enterprise Analytics reads from the most recent snapshot at or before this timestamp. Cannot be used together with snapshotId. See [Use Time Travel](5%5Fddl%5Ficeberg.md#use-time-travel).                                                           | No       |

## [](#example)Example

```SQL++
CREATE EXTERNAL COLLECTION usersTable
ON myGlueCatalog
AT myAwsLink
WITH {
    "table-format": "iceberg",
    "namespace": "pharmacy_namespace",
    "tableName": "users",
    "decimal-to-double": "true"
};
```

## [](#filtration)Filtration

When Enterprise Analytics queries an Iceberg external collection, the following filtrations are applied in order:

1. Only the files belonging to the specified Iceberg table are scanned — no other table's files are read.
2. If a `WHERE` clause is provided, Enterprise Analytics applies predicates to perform partition pruning and manifest-level exclusion before reading data files.
3. Only columns referenced in the `SELECT` clause are projected — not all columns in the table are read.

Partition pruning, manifest-level exclusion, and column projection reduce the amount of data scanned for selective queries. See [Cost-Based Optimizer](5b%5Fcbo.md) for further details on query optimization.

## [](#see-also)See Also

* [Iceberg Tables](5%5Fddl%5Ficeberg.md)
* [Create a Catalog](5%5Fddl%5Ficeberg%5Fcatalog.md)
* [Manage Links](../sources/manage-links.md)
* [Set Up an External Data Source](../sources/manage-external.md)
* [Cost-Based Optimizer](5b%5Fcbo.md)