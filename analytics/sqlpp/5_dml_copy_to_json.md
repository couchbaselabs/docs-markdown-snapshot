[View original HTML](/analytics/sqlpp/5_dml_copy_to_json.html)

> This topic describes how you use `COPY TO` statements to structure and write the results of a query—​or a copy of an entire collection—​out to an external data store such as Amazon S3 and GCS. 

Structuring the data on the external store is helpful in use cases where you plan to directly query the data there later, and to use [dynamic prefixes](../sources/dynamic-prefixes.md) to optimize those queries.

The output format of the data is JSON.

For more information, see [Query Data in Amazon S3](../sources/external-s3.md) and [Query Data in Google Cloud Storage (GCS)](../sources/external-gcs.md).

|  | To be able to read or write data to or from external cloud storage, exclusive permissions are required. For more information see [Cloud Read/Write Permissions](../reference/cloud%5Fread%5Fwrite%5Fpermissions.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#syntax)Syntax

**CopyTo EBNF** 

```EBNF
CopyTo ::= "COPY" SourceDefinition
           "TO" ContainerIdentifier
           "AT" LinkQualifiedName
           OutputClause WithClause
```

**CopyTo Diagram** 

!["COPY" SourceDefinition "TO" ContainerIdentifier "AT" LinkName OutputClause WithClause](_images/CopyTo.png) 

**Show SourceDefinition Diagram** 

![( QualifiedName | "(" Query ")" ) ("AS"? AliasIdentifier )?](_images/SourceDefinition.png) 

SourceDefinition

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

**Show WithClause Diagram** 

!["WITH" "{" NameValuePair ("," NameValuePair )* "}"](_images/WithClause.png) 

WithClause

**Show NameValuePair Diagram** 

![NameStringLiteral ":" ValueLiteral](_images/NameValuePair.png) 

NameValuePair

## [](#examples)Examples

### Example 1: COPY TO

This example copies all items in a `music.myPlaylist.countrySongs` collection into JSON files with gzip compression on an S3 bucket.

```SQL++
  COPY music.myPlaylist.countrySongs
  TO `my-music-bucket`
  AT musicLink
  PATH("music", "myPlaylist", "countrySongs")
  WITH {
    "compression": "gzip"
  };
```

The output object on S3 is a single compressed file containing one JSON object per line:

myPlaylist/countrySongs/0000-00000.json.gz:
{ "countrySongs": { "pk": "31d64e83-176c-4889-0081-fd8f3a2c249c", ... }}
{ "countrySongs": { "pk": "31d64e83-176c-4889-0081-fd8f3a2c2683", ... }}
...
{ "countrySongs": { "pk": "31d64e83-176c-4889-0081-fd8f3a2c26f3", ... }}

### Example 2: COPY TO with OVER

This example copies data for all customers living in Boston, MA or Hanover, MA into S3\. The output includes only data from the following fields: `custid`, `name`, `rating`, and `zipcode`. The `OVER` clause specifies partitioning by zip code for the output, with an AS expression that includes the zip value as an alias in one of the path prefixes. The zip code values must be non-unknowable, scalar values: that is, not NULL or MISSING, or an array or object. Within each partition, the statement orders objects by descending rating.

```SQL++
  COPY (
    SELECT c.custid, c.name, c.rating, c.zipcode
    FROM sampleAnalytics.Commerce.Customers c
    WHERE c.city IN ["Boston, MA", "Hanover, MA"]
  ) AS t
  TO myS3Bucket AT myS3Link
    PATH("commerce/Customers/zip", zip)
    OVER(
      PARTITION BY t.zipcode AS zip
      ORDER BY t.rating DESC
    );
```

The output objects are:

commerce/Customers/zip/02340/0000-00000.json (first file in first partition):
{"custid":"C25","name":"M. Sinclair","rating":690,"zipcode":02340}
commerce/Customers/zip/02115/0000-00000.json (first file in second partition):
{"custid":"C37","name":"T. Henry","rating":750,"zipcode":02115}
{"custid":"C35","name":"J. Roberts","rating":565,"zipcode":02115}

### Example 3: COPY TO with Output Exceeding File Maximum

This example copies all items from the Orders collection into JSON files on S3\. In this example, the Orders collection contains 25000 objects. The statement does not include a value for `max-objects-per-file`, so the default of 10000 applies. In addition, assume that two workers are doing the processing.

```SQL++
  COPY sampleAnalytics.Commerce.Orders TO myS3Bucket AT myS3Link
  PATH("commerce/Orders")
```

The output objects are:

commerce/Orders/0000-00000.json (1st worker, contains 10000 objects)
commerce/Orders/0001-00000.json (2nd worker, contains 10000 objects)
commerce/Orders/0000-00001.json (1st worker, contains 5000 objects)

### Example 4: COPY TO with Increased File Maximum

This example is similar to the previous example, but with the maximum number of objects per file set to 25000 and gzip compression. Only a single worker is writing the result.

```SQL++
  COPY sampleAnalytics.Commerce.Orders
  TO myS3Bucket AT myS3Link
  PATH("commerce/Orders")
  WITH {
    "max-objects-per-file": "25000",
    "compression": "gzip"
  }
```

The output objects are:

commerce/Orders/0000-00000.json.gz (contains 25000 objects)

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

The **`OutputClause`** defines the destination path for the output objects. You supply one or more `OutputPathExpr` expressions to identify the path prefixes. You can include aliases. If you supply more than one expression, Capella Analytics concatenates the values of all `OutputPathExpr` and supplies `/` characters as the path separators. As a result, you do not need to include slash characters between `OutputPathExpr` expressions.

|  | The target directory that you specify in the destination path must be empty. The operation fails if the target directory is not empty. |
|  | -------------------------------------------------------------------------------------------------------------------------------------- |

OverClause

You supply an optional **`OverClause`** to specify output partitioning with a `PartitionClause` and ordering with an `OrderClause`. This is similar to the `OVER` clause of a [WINDOW statement](3%5Fquery.md#Over%5Fclauses).

* If you specify a `PartitionClause`, Capella Analytics evaluates the `Output_Path_Expr` once per logical data partition and refers to aliases if defined by an `AS` sub-clause.
* If you do not specify a `PartitionClause`, Capella Analytics evaluates the `OutputPathExpr` once for the whole `COPY TO` output dataset. That’s, all of the files end up in the same directory.

You use the `OrderClause` to define output object order, either within each partition or for the whole dataset.

WITH

The **`WITH`** clause is optional. You use it to specify the following additional parameters.

| Name                            | Description                                                                       | Schema                 |
| ------------------------------- | --------------------------------------------------------------------------------- | ---------------------- |
| max-objects-per-file (Optional) | Maximum number of objects per file. Default: 10000\. Minimum allowed value: 1000. | String                 |
| compression (Optional)          | Compression mechanism. Default: none.                                             | String enum (gz, gzip) |

### [](#about-output-object-names)About Output Object Names

The number of processing threads (workers) that Capella Analytics uses to create new objects, and the maximum number of objects per file setting, affect the number of files that result from a given `COPY TO` statement.

Capella Analytics assigns file names to the output objects that result from a `COPY TO` statement. The filename consists of two monotonically incrementing counters followed by the file extension, in the format `0000-0000.json`.

* The number before the dash identifies the worker. If processing uses more than one worker, the name of the first output file is `0000-` and files created by the additional workers each increment this number by 1.
* The number after the dash identifies the file number. The first file written by each worker is file number `0000`. If the output exceeds the maximum number of objects per file, the process creates another file with a file number incremented by 1.