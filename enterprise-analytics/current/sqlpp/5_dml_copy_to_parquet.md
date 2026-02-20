---
title: Parquet
description: This topic explains how to use the COPY TO statement to export data
  from a database to Amazon S3 or Azure Blob Storage in Parquet format.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_dml_copy_to_parquet.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sqlpp:5_dml_copy_to_parquet.adoc[]
---

[View original HTML](/enterprise-analytics/current/sqlpp/5_dml_copy_to_parquet.html)

# Parquet

> This topic explains how to use the COPY TO statement to export data from a database to Amazon S3 or Azure Blob Storage in Parquet format. 

Having results in Parquet format is highly efficient due to its columnar format, which enables better compression and faster query performance.

Parquet files takes less storage space, making it cost-effective for large-scale data storage and analytics.

The optimized format is for read-heavy workloads making it ideal for big data processing, data warehousing, and machine learning pipelines.

For more information, see [Query Data in External Data Sources](../sources/external-s3.md).

> [!NOTE]
> To be able to read or write data to or from external cloud storage, exclusive permissions are required. For more information see [Cloud Read/Write Permissions](../reference/cloud%5Fread%5Fwrite%5Fpermissions.md).

## [](#supported-methods)Supported Methods

You can copy data using one of the two methods:

1. **User-Defined Schema**: It’s a schema explicitly provided by the user in the `COPY TO` statement when the structure of the result or collection is known.
2. **Schema Inference**: The system infers the schema from the data.

## [](#syntax)Syntax

**CopyTo EBNF** 

```EBNF
CopyTo ::= "COPY" SourceDefinition
           "TO" ContainerIdentifier
           "AT" LinkQualifiedName
           OutputClause
           "WITH" ObjectConstructor
```

**CopyTo Diagram** 

!["COPY" SourceDefinition "TO" ContainerIdentifier "AT" LinkName OutputClause "WITH" ObjectConstructor](_images/CopyToExternal.png) 

**Show SourceDefinition Diagram** 

![( QualifiedName | "(" Query ")" ) ("AS"? AliasIdentifier )?](_images/SourceDefinition.png) 

SourceDefinition

**Show OutputClause Diagram** 

!["PATH" "(" OutputPathExpr ("," OutputPathExpr)* ")" OverClause? SchemaClause?](_images/OutputClauseWithSchema.png) 

OutputClause

**Show OutputPathExpr Diagram** 

![Expr](_images/OutputPathExpr.png) 

OutputPathExpr

**Show OverClause Diagram** 

!["OVER" "(" PartitionClause? OrderClause? ")"](_images/OverClause.png) 

OverClause

**Show SchemaClause Diagram** 

![TYPE](_images/Schema_Clause.png) 

SchemaClause

**Show TypeExpression Diagram** 

![ObjectTypeDef](_images/TypeExpr.png) 

TypeExpression

**Show ObjectTypeDefinition Diagram** 

![{](_images/ObjectTypeDef.png) 

ObjectTypeDefinition

**Show ArrayTypeDefinition Diagram** 

![(](_images/ArrayTypeDef.png) 

ArrayTypeDefinition

**Show ObjectField Diagram** 

![Identifier](_images/ObjectField.png) 

ObjectField

**Show PartitionClause Diagram** 

!["PARTITION" "BY" PartitionExpr ("," PartitionExpr)*](_images/PartitionClause.png) 

PartitionClause

**Show PartitionExpr Diagram** 

![Expression ("AS" AliasIdentifier)?](_images/PartitionExpr.png) 

PartitionExpr

**Show OrderClause Diagram** 

!["ORDER" "BY"  OrderExpr ("," OrderExpr)*](_images/OrderClause.png) 

OrderClause

**Show OrderExpr Diagram** 

![Expression ("ASC" | "DESC")? ( "NULLS" ( "FIRST" | "LAST" ) )?](_images/OrderExpr.png) 

OrderExpr

**Show WithClause Diagram** 

!["WITH" "{" NameValuePair ("," NameValuePair )* "}"](_images/WithClauseProperties.png) 

WithClauseProperties

**Show NameValuePair Diagram** 

![NameStringLiteral ":" ValueLiteral](_images/NameValuePair.png) 

NameValuePair

## [](#examples)Examples

You can copy the Customer Data from [Example Data](../../../server/current/analytics/appendix%5F4%5Fexamples.md) in parquet format with gzip compression.

### Example 1: Syntax for User-Defined Schema

```SQL++
  COPY (
    SELECT * from customers
  ) AS t
  TO myS3Bucket AT myS3Link
    PATH("commerce/Customers/zip=" || zip || "/")
    OVER(PARTITION BY t.address.zipcode AS zip)
  TYPE (
{
 orderno : int ,
 custid : string,
 order_date : date,
 ship_date : date,
 items : [ { itemno:int, qty : int, price : double } ]
}
  )
  WITH {
    "format": "parquet"  ,
    "compression": "gzip"
  }
```

### Example 2: Syntax for Schema Inference

```SQL++
  COPY (
    SELECT * from customers
  ) AS t
  TO myS3Bucket AT myS3Link
    PATH("commerce/Customers/zip=" || zip || "/")
    OVER(PARTITION BY t.address.zipcode AS zip)
  WITH {
    "format": "parquet",
    "compression": "gzip"
  }
```

## [](#arguments)Arguments

SourceDefinition

As the source, you specify either the fully qualified name of a collection or provide a query.

* If you specify a collection name, then the whole collection—or view or synonym—is the source of data to copy.
* If you specify a query, then the result of that query is the source of data.

TO

The **`TO`** clause identifies the bucket name on the external data source, an Amazon S3 bucket in this case.

AT

The **`AT`** clause specifies the name of the link that contains credentials for the S3 bucket name. The specified link must have a type of S3.

OutputClause

The **`OutputClause`** defines the destination path for the output objects. You supply one or more `OutputPathExpr` expressions to identify the path prefixes. You can include aliases. If you supply more than one expression, Enterprise Analytics concatenates the values of all `OutputPathExpr` and supplies `/` characters as the path separators. As a result, you do not need to include slash characters between `OutputPathExpr` expressions.

> [!NOTE]
> The target directory that you specify in the destination path must be empty. The operation fails if the target directory is not empty.

OverClause

You supply an optional **`OverClause`** to specify output partitioning with a `PartitionClause` and ordering with an `OrderClause`. This is similar to the `OVER` clause of a [WINDOW statement](3%5Fquery.md#Over%5Fclauses).

* If you specify a `PartitionClause`, Enterprise Analytics evaluates the `Output_Path_Expr` once per logical data partition and refers to aliases if defined by an `AS` sub-clause.
* If you do not specify a `PartitionClause`, Enterprise Analytics evaluates the `OutputPathExpr` once for the whole `COPY TO` output dataset. That’s, all of the files end up in the same directory.

You use the `OrderClause` to define output object order, either within each partition or for the whole dataset.

SchemaClause

The `SchemaClause` defines the schema for the output `Parquet` files. You specify the schema using a JSON-like format: { `field-name1`: `type1`, `field-name2`: `type2`, …​ }. The types can be flat types, array types, or object types. Supported flat types are listed in the Supported Types section.

WITH

The **`WITH`** clause is used to specify the following additional parameters.

| Name                     | Description                                                                                                                                                               | Schema                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| format (optional)        | Allowed values: "parquet" Default: JSON                                                                                                                                   | String Enum                        |
| max-objects-per-file     | Maximum number of objects per file. Default: 10000.                                                                                                                       | int                                |
| max-schemas(optional)    | Maximum number of heterogeneous schemas allowed. This value cannot be greater than 10. This value is valid only for schemaless mode (with TYPE not provided). Default : 5 | int                                |
| compression (Optional)   | Allowed values: "none", "snappy", "gzip","lzo","brotli","lz4","zstd" Default: none                                                                                        | String enum                        |
| row-group-size(Optional) | [Row Group Size](https://parquet.apache.org/docs/concepts/) in parquet file in byte values. Default: 10 MB                                                                | String                             |
| page-size(Optional)      | [Page Size](https://parquet.apache.org/docs/concepts/) in parquet file in byte values. Default: 8 KB                                                                      | String                             |
| version(Optional)        | Parquet Writer Version. Allowed values : 1,2 Default: 1                                                                                                                   | String Enum                        |
| format                   | Format of the data being written                                                                                                                                          | The format of the page is Parquet. |

### [](#supported-data-types)Supported Data Types

The supported types and the corresponding parquet types are in the following table:

| Analytics Type         | Parquet Type                  |
| ---------------------- | ----------------------------- |
| boolean                | BOOLEAN                       |
| string                 | BINARY(STRING)                |
| tinyint, smallint, int | INT32                         |
| bigint                 | INT64                         |
| float                  | FLOAT                         |
| double                 | DOUBLE                        |
| date                   | INT32(DATE)                   |
| time                   | INT32(TIME\_MILLIS)           |
| datetime               | INT64(TIMESTAMP\_MILLIS)      |
| UUID                   | FIXED\_LEN\_BYTE\_ARRAY(UUID) |