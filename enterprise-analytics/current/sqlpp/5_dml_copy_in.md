---
title: COPY INTO Statements
description: This topic describes how you use the  <code>COPY INTO</code> DML
  statement to upsert&mdash;both insert and update&mdash;objects from an
  external collection to a standalone collection.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_dml_copy_in.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sqlpp:5_dml_copy_in.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_dml_copy_in.html)

# COPY INTO Statements

> This topic describes how you use the `COPY INTO` DML statement to upsert—both insert and update—objects from an external collection to a standalone collection. 

> [!TIP]
> You can also populate a standalone collection by importing a file in a supported format from your local network. See [Install the Commerce Dataset in Standalone Collections](../intro/connecting-to-data-sources.md#install-the-commerce-dataset-in-standalone-collections).

> [!NOTE]
> To be able to read or write data to or from external cloud storage, exclusive permissions are required. For more information see [Cloud Read/Write Permissions](../reference/cloud%5Fread%5Fwrite%5Fpermissions.md).

## [](#syntax)Syntax

**CopyInto EBNF** 

```EBNF
CopyInto ::= "COPY" "INTO"? QualifiedName
             ("AS" CollectionTypeDef)?
             "FROM" Identifier
             "AT" QualifiedName
             ("PATH" StringLiteral) ?
             ("WITH" ObjectConstructor) ?
```

**CopyInto Diagram** 

!["COPY" "INTO"? QualifiedName FROM Identifier "AT" QualifiedName PATH StringLiteral "WITH" ObjectConstructor ?](_images/CopyInto.png) 

## [](#example)Example

This example refreshes the data in the `my-ad-hoc-collection` with documents located in an external file store named TravelShop. The referenced link, myS3Link, stores further details about the location of the external file store.

```SQL++
  COPY INTO database_name.scope_name.`my-ad-hoc-collection`
  FROM TravelShop AT myS3Link
  PATH "json-data/customers"
  WITH {
    "format": "json",
    "include": ["*2018*.json", "*2019*.json"]
  };
```

After you use `COPY INTO`, you can run `ANALYZE COLLECTION` on the collection to update the data sample used by cost-based optimization (CBO). See [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md).

## [](#arguments)Arguments

FROM

The **`FROM`** clause identifies the bucket name on the external data source, such as an Amazon S3 bucket.

AT

The **`AT`** clause specifies the name of the link that contains credentials for the S3 bucket name. The specified link must have a type of S3.

PATH

The **`PATH`** clause is a string that specifies the location path to the location of the data, relative to the external data source.

WITH

In the **`WITH`** clause, you define the same `ObjectConstructor` parameters for format and file parsing, and what to include or exclude, as you would provide when you create an external collection. See [CREATE an External Collection](5%5Fddl%5Fexternal.md).

## [](#see-also)See Also

* [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md)
* [Entities in Enterprise Analytics](1a%5Fentities.md)
* [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md)