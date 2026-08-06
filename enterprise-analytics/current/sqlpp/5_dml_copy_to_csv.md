---
title: CSV
description: This topic explains how to use the COPY TO statement to export data
  from a database to Amazon S3 or Azure Blob Storage in CSV format.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_dml_copy_to_csv.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sqlpp:5_dml_copy_to_csv.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_dml_copy_to_csv.html)

# CSV

> This topic explains how to use the COPY TO statement to export data from a database to Amazon S3 or Azure Blob Storage in CSV format. 

COPY TO CSV introduces the ability to write results of queries or entire collections to external stores (such as AWS S3 or Azure Blob Storage) in CSV format.

For more information, see [Query Data in Amazon S3](../sources/external-s3.md).

> [!NOTE]
> To be able to read or write data to or from external cloud storage exclusive permissions are required. For more information see [Cloud Read/Write Permissions](../reference/cloud%5Fread%5Fwrite%5Fpermissions.md).

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

![( QualifiedName | "(" Query ")" ) ("AS"? AliasIdentifier )?](_images/Source_Definition.png) 

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

**Show SchemaClause Diagram** 

!["AS" CSV_Type_Expr](_images/Schema_Clause.png) 

SchemaClause

**Show CSVTypeExpr Diagram** 

![(" Type_Expr ("," Type_Expr)* ")](_images/CSVTypeExpr.png) 

CSVTypeExpr

**Show TypeExpr Diagram** 

![Field_Name Flat_Type (](_images/Type_Expr.png) 

Type\_Expr

**Show FlatType Diagram** 

![(](_images/FlatType.png) 

FlatType

**Show WithClause Diagram** 

![WITH](_images/WithClauseProperties.png) 

WithClauseProperties

**Show NameValuePair Diagram** 

![NameStringLiteral ":" ValueLiteral](_images/NameValuePair.png) 

NameValuePair

## [](#example)Example

```SQL++
  COPY (
    SELECT o.custid, o.order_date, o.orderno, o.gender, o.zip
    FROM Orders o
  ) AS t
  TO myS3Bucket
  AT myS3Link
  PATH ("commerce/Orders/zip-" || zip || "/")
  OVER (PARTITION BY t.zip AS zip)
  AS (
      custid string NOT UNKNOWN,
      orderno int,
      order_date string,
      gender string,
      zip string
  )
  WITH {
	    "format": "csv",
	    "header": true
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
* If you do not specify a `PartitionClause`, Enterprise Analytics evaluates the `OutputPathExpr` once for the whole `COPY TO` output dataset. That is, all of the files end up in the same directory.

You use the `OrderClause` to define output object order, either within each partition or for the whole dataset.

AS (CSV Type Expression)

`UNKNOWN` refers to the field being null or missing.

```SQL++
  AS (
		custid STRING NOT UNKNOWN,
		orderno BIGINT,
		order_date DATE,
		gender STRING
	)
```

WITH

The **`WITH`** clause is used to specify the following additional parameters.

| Name                            | Description                                                                                                                                                                         | Schema                         |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| max-objects-per-file (Optional) | Maximum number of objects per file. **Default**: 10000. **Minimum allowed value**: 1000.                                                                                            | String                         |
| compression (Optional)          | Compression mechanism. **Default**: none.                                                                                                                                           | String enum (gz, gzip)         |
| header(Optional)                | Specifies if the header information must be written or not. **Default**: false                                                                                                      | Boolean                        |
| escape                          | Specifies the character used to escape the QUOTE and carriage return value. **Default**: same as the QUOTE value (the quote character is displayed twice if it appears in the data) | String                         |
| quote                           | A character used to enclose strings. **Default**: " **Value**: NONE, ', "                                                                                                           | String                         |
| null (Optional)                 | Emits text in CSV output for NULL or MISSING values. **Default**: unquoted empty string                                                                                             | String                         |
| record-delimiter                | Character that separates each row/line (record).                                                                                                                                    | String                         |
| delimiter                       | Specifies the character that separates columns within each row (line) of the file. **Default**: comma in CSV format                                                                 | String                         |
| empty-field-as-null             | Empty data values to be written by <null> string. **Default**: false                                                                                                                | Boolean                        |
| force-quote                     | A flag to enable or disable the quotes around the string non-null values. **Default**: Special characters within the string value are always enclosed within quotes.                | Boolean                        |
| format                          | Format of the data being written                                                                                                                                                    | The format of the page is CSV. |

### [](#supported-data-types)Supported Data Types

Following are the supported data types that can be used in CSV schema:

* Boolean
* String
* Bigint
* Double
* Null
* Temporal Data (Date / Time / DateTime)

### [](#unsupported-data-types)Unsupported Data Types

Following are the unsupported data types that cannot be used in CSV schema:

* Object
* Array
* Multiset

### [](#schema-mismatches-and-warnings)Schema Mismatches and Warnings

In case of a schema mismatch between the expected schema versus the actual record's schema, a warning is issued and returned as part of the final result. The system skips writing records with mismatches and continues to the next record.

Examples of schema mismatches:

* The provided schema has 4 fields, but the actual record has 5 fields.
* The type for the same field is different in the provided schema vs the field type in the record schema.
* The actual record has fields that are not present in the provided schema.