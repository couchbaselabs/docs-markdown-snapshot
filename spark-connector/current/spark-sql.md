---
title: DataFrames, Datasets, and SQL
description: Spark allows accessing query, analytics, Enterprise Analytics, and
  Capella Columnar in powerful and convenient ways.
editUrl: https://github.com/couchbase/docs-spark/edit/release/3.5/modules/ROOT/pages/spark-sql.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/spark-connector/current/spark-sql.html)

# DataFrames, Datasets, and SQL

> Spark allows accessing query, analytics, Enterprise Analytics, and Capella Columnar in powerful and convenient ways. 

While Apache’s low-level [RDDs](working-with-rdds.md) are powerful, Apache Spark now encourages users towards the higher-level DataFrames and Datasets. Let’s see how to use those with Couchbase.

Before you can create DataFrames or Datasets with Couchbase, you need to create a `SparkSession`. See [Getting Started (Scala)](getting-started.md) or [Getting Start(PySpark)](pyspark.md)

## [](#running-examples)Running examples

All query examples presented on this page at least require the `travel-sample` dataset to be installed on your Couchbase cluster, with a primary index. If you haven’t done so already, you can create a primary index by executing this SQL++ statement: `` CREATE PRIMARY INDEX ON `travel-sample` ``.

To use the operational analytics examples, corresponding datasets or collection mappings should be created.

Enterprise Analytics is also supported, and provides enhanced analytics capabilities for enterprise environments.

## [](#dataframes)DataFrames

A read `DataFrame` can be created through `spark.read.format(…​)`, and which format to choose depends on the type of service you want to use. For `spark.read`, `couchbase.query`, `couchbase.analytics`, `couchbase.enterprise-analytics`, and `couchbase.columnar` are available.

(For reading from the KV service - see [RDDs](working-with-rdds.md))

* Scala
* PySpark

```scala
val queryDf = spark.read.format("couchbase.query").load()

val analyticsDf = spark.read.format("couchbase.analytics").load()

val enterpriseAnalyticsDf = spark.read.format("couchbase.enterprise-analytics").load()

val columnarDf = spark.read.format("couchbase.columnar").load()
```

```python
queryDf = spark.read.format("couchbase.query").load()

analyticsDf = spark.read.format("couchbase.analytics").load()

enterpriseAnalyticsDf = spark.read.format("couchbase.enterprise-analytics").load()

columnarDf = spark.read.format("couchbase.columnar").load()
```

### [](#collections)Collections

You’ll generally want the DataFrame to work with a specific Couchbase collection, which can be done with the following:

* Scala
* PySpark
* Scala (Columnar)
* Scala (Enterprise Analytics)
* PySpark (Enterprise Analytics)

```scala
val airlines = spark.read.format("couchbase.query")
  .option(QueryOptions.Bucket, "travel-sample")
  .option(QueryOptions.Scope, "inventory")
  .option(QueryOptions.Collection, "airline")
  .load()
```

```python
airlines = (spark.read.format("couchbase.query")
            .option("bucket", "travel-sample")
            .option("scope", "inventory")
            .option("collection", "airline")
            .load())
```

```scala
val airlines = spark.read.format("couchbase.columnar")
  .option(ColumnarOptions.Database, "travel-sample")
  .option(ColumnarOptions.Scope, "inventory")
  .option(ColumnarOptions.Collection, "airline")
  .load()
```

```scala
val airlines = spark.read.format("couchbase.enterprise-analytics")
  .option(EnterpriseAnalyticsOptions.Database, "travel-sample")
  .option(EnterpriseAnalyticsOptions.Scope, "inventory")
  .option(EnterpriseAnalyticsOptions.Collection, "airline")
  .load()
```

```python
airlines = (spark.read.format("couchbase.enterprise-analytics")
            .option("database", "travel-sample")
            .option("scope", "inventory")
            .option("collection", "airline")
            .load())
```

Note all query options are documented here [Query Options](#%5Fquery%5Foptions), all Capella Columnar options here [Capella Columnar options](#%5Fcolumnar%5Foptions), and all Enterprise Analytics options here [Enterprise Analytics options](#%5Fenterprise%5Fanalytics%5Foptions).

If you will usually be using the same collection, it can be more convenient to provide it in the SparkSession config instead:

```scala
val spark = SparkSession
  .builder()
  .master("local[*]")
  .config("spark.couchbase.connectionString", "couchbase://127.0.0.1")
  .config("spark.couchbase.username", "username")
  .config("spark.couchbase.password", "password")
  .config("spark.couchbase.implicitBucket", "travel-sample")
  .config("spark.couchbase.implicitScope", "inventory")
  .config("spark.couchbase.implicitCollection", "airline")
  .getOrCreate()
```

### [](#%5Fschemas)Schemas

Spark requires a schema for all DataFrame and Dataset operations.

The Couchbase Spark Connector will perform automatic schema inference based on a random sampling of all documents in the chosen collection — or bucket if no collection was chosen. This automatic inference can work well in cases where the data are very similar.

If the data are not similar, there are two options: you can either provide a manual schema, or narrow down what documents the automatic schema inference acts on by providing explicit predicates.

For example, say the schema of the `airlines` collection evolves and we add a `"version": 2` field to identify documents that have the new schema. We can limit both the inference and the SQL++ executed from the DataFrame to only those documents, by providing a filter:

* Scala (Columnar)
* PySpark (Columnar)
* Scala (Enterprise Analytics)
* PySpark (Enterprise Analytics)

```scala
val airlines = spark.read
  .format("couchbase.query")
  .option(ColumnarOptions.Database, "travel-sample")
  .option(ColumnarOptions.Scope, "inventory")
  .option(ColumnarOptions.Collection, "airline")
  .option(QueryOptions.Filter, "version = 2")
  .load()
```

```python
airlines = (spark.read
            .format("couchbase.query")
            .option("database", "travel-sample")
            .option("scope", "inventory")
            .option("collection", "airline")
            .option("filter", "version = 2")
            .load())
```

```scala
val airlines = spark.read
  .format("couchbase.enterprise-analytics")
  .option(EnterpriseAnalyticsOptions.Database, "travel-sample")
  .option(EnterpriseAnalyticsOptions.Scope, "inventory")
  .option(EnterpriseAnalyticsOptions.Collection, "airline")
  .option(EnterpriseAnalyticsOptions.Filter, "country = 'United States'")
  .load()
```

```python
airlines = (spark.read
            .format("couchbase.enterprise-analytics")
            .option("database", "travel-sample")
            .option("scope", "inventory")
            .option("collection", "airline")
            .option("filter", "country = 'United States'")
            .load())
```

You can call `airlines.printSchema()` to view the schema (either inferred or provided manually):

root
 |-- __META_ID: string (nullable = true)
 |-- callsign: string (nullable = true)
 |-- country: string (nullable = true)
 |-- iata: string (nullable = true)
 |-- icao: string (nullable = true)
 |-- id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- type: string (nullable = true)

Not only did it automatically infer the schema, it also added a `META_ID` field which corresponds to the document ID if applicable.

A manual schema can also be provided, and this is the recommended practice for production applications, to protect against future data changes:

* Scala

```scala
val airlines = spark.read
  .format("couchbase.query")
  .schema(StructType(
    StructField("name", StringType) ::
      StructField("type", StringType) :: Nil
  ))
  .load()
```

### [](#dataframe-operations)DataFrame Operations

Now that you have a DataFrame, you can apply all the operations that Spark SQL provides. A simple example would be to load specific fields from the DataFrame and print some of those records:

* Scala
* PySpark

```scala
airlines
  .select("name", "callsign")
  .sort(airlines("callsign").desc)
  .show(10)
```

```python
(airlines
 .select("name", "callsign")
 .sort(airlines("callsign").desc)
 .show(10))
```

Results in:

+-------+--------------------+
|   name|            callsign|
+-------+--------------------+
|   EASY|             easyJet|
|   BABY|             bmibaby|
|MIDLAND|                 bmi|
|   null|          Yellowtail|
|   null|               XOJET|
|STARWAY|   XL Airways France|
|   XAIR|            XAIR USA|
|  WORLD|       World Airways|
|WESTERN|    Western Airlines|
|   RUBY|Vision Airlines (V2)|
+-------+--------------------+

### [](#spark-sql)Spark SQL

We can use Spark’s `createOrReplaceTempView` to create a temporary view from a DataFrame, which we can then run Spark SQL on (which creates another DataFrame):

* Scala
* PySpark

```scala
airlines.createOrReplaceTempView("airlinesView")
val airlinesFromView = spark.sql("SELECT * FROM airlinesView")
```

```python
airlines.createOrReplaceTempView("airlinesView")
airlinesFromView = spark.sql("SELECT * FROM airlinesView")
```

Note this SQL is executed purely within Spark, and is not sent to the Couchbase cluster.

## [](#%5Fdataframe%5Fpartitioning)DataFrame partitioning

By default, one DataFrame read or write with query will result in one SQL++ statement being executed.

With very large DataFrames this can present issues, as all rows are streamed back to one Spark worker. In addition there is no parallelism.

So in some specific situations the user may wish to provide partitioning hints so that multiple SQL++ statements are executed.

In this example, say we are reading from an orders collection, where we know we have around 100,000 orders and want to partition into 100 SQL++ statements. Here we will partition on a numerical "id" column:

* Scala
* PySpark

```scala
spark.read
  .format("couchbase.query")
  .option(QueryOptions.PartitionColumn, "id")
  .option(QueryOptions.PartitionLowerBound, "1")
  .option(QueryOptions.PartitionUpperBound, "100000")
  .option(QueryOptions.PartitionCount, "100")
  .load()
```

```python
(spark.read
 .format("couchbase.query")
 .option("partitionColumn", "id")
 .option("partitionLowerBound", "1")
 .option("partitionUpperBound", "100000")
 .option("partitionCount", "100")
 .load())
```

This will result in 100 partitions with SQL++ statements along the lines of

```none
SELECT [...] WHERE [...] AND id < 1000
SELECT [...] WHERE [...] AND (id >= 1000 AND id < 2000)
SELECT [...] WHERE [...] AND (id >= 2000 AND id < 3000)
...
SELECT [...] WHERE [...] AND id >= 99000
```

If any of the four partitioning options is provided, then all must be.

The chosen partitionColumn must support the SQL comparison operators "<" and ">=". Any results where partitionColumn is null or otherwise not matched by those operators, will not be included.

`PartitionLowerBound` and `PartitionUpperBound` do not bound or limit the results, they simply choose how many results are in each partition. Note that the first and last queries in the example above use `<` and `>=` to include all results.

### [](#partitioning-performance-tips)Partitioning performance tips

When using query partitioning, users are often interested in obtaining the highest throughput possible. Internal testing has found these tips will provide the best possible performance:

* Duplicating or replicating the GSI indexes used by the query, so that multiple query nodes are not bottlenecked by going to a single GSI node.
* Increasing the data service reader and writer threads.
* Ensuring the disks used can provide sufficient throughput/IOPS.
* Increasing the number of Couchbase nodes, and the resources (cores, memory, disk) allocated to each.
* Increasing the count of Spark worker nodes, and the number of cores on each (each core can execute one partition at a time).
* Ensuring sufficient network bandwidth is available.

## [](#%5Fdataframe%5Fpersistence)DataFrame persistence

It is also possible to write DataFrames into Couchbase.

Couchbase documents require unique document ids, so this needs to be available in the DataFrame. By default the connector will look for a `META_ID` column, but this can be overridden with an option (see below).

All the other fields in the DataFrame will be converted into JSON and stored as the document content.

You can store `DataFrames` using both `couchbase.query` and `couchbase.kv`. We recommend using the KeyValue data source since it provides better performance out of the box if the usage pattern allows for it.

The following example reads data from a collection and writes the first 5 results into a different collection. Also, to showcase properties, they are used on both the read and the write side:

* Scala
* PySpark

```scala
val airlines = spark.read.format("couchbase.query")
  .option(QueryOptions.Bucket, "travel-sample")
  .option(QueryOptions.Scope, "inventory")
  .option(QueryOptions.Collection, "airline")
  .load()
  .limit(5)

airlines.write.format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "test-bucket")
  .option(KeyValueOptions.Scope, "test-scope")
  .option(KeyValueOptions.Collection, "test-collection")
  .save()
```

```python
airlines = (spark.read.format("couchbase.query")
            .option("bucket", "travel-sample")
            .option("scope", "inventory")
            .option("scope", "airline")
            .load()
            .limit(5))

(airlines.write.format("couchbase.kv")
 .option("bucket", "test-bucket")
 .option("scope", "test-scope")
 .option("collection", "test-collection")
 .save())
```

And to specify your own document id column for a DataFrame `df`:

* Scala
* PySpark

```scala
df.write.format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "test-bucket")
  .option(KeyValueOptions.Scope, "test-scope")
  .option(KeyValueOptions.Collection, "test-collection")
  .option(KeyValueOptions.IdFieldName, "YourIdColumn")
  .save()
```

```python
(df.write.format("couchbase.kv")
 .option("bucket", "test-bucket")
 .option("scope", "test-scope")
 .option("collection", "test-collection")
 .option("idFieldName", "YourIdColumn")
 .save())
```

Note all key-value options are documented here [Key-Value options](#%5Fkv%5Foptions) and all query options are documented here [Query Options](#%5Fquery%5Foptions).

### [](#customising-persistence)Customising persistence

Spark has four built-in [SaveModes](https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/sql/SaveMode.html) that can be used to control how data is written into Couchbase.

As these Spark SaveModes do not cover all Couchbase functionality, the Couchbase Spark Connector additionally has a `KeyValueOptions.WriteMode` option.

This example shows the two in use:

```scala
val airlines = spark.read.format("couchbase.query")
  .option(QueryOptions.Bucket, "travel-sample")
  .option(QueryOptions.Scope, "inventory")
  .option(QueryOptions.Collection, "airline")
  .load()
  .limit(5)

// Writing using a built-in Spark SaveMode
airlines.write.format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "test-bucket")
  .option(KeyValueOptions.Scope, "test-scope")
  .option(KeyValueOptions.Collection, "test-collection")
  .mode(SaveMode.Append)
  .save()

// Writing using one of the Couchbase WriteModes
airlines.write.format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "test-bucket")
  .option(KeyValueOptions.Scope, "test-scope")
  .option(KeyValueOptions.Collection, "test-collection")
  .option(KeyValueOptions.WriteMode, KeyValueOptions.WriteModeReplace)
  .save()
```

The modes are mapped as follows:

__Table 1\. couchbase.kv mappings__
| SaveMode               | Underlying Couchbase KV Operation                   | Behaviour                                                                 |
| ---------------------- | --------------------------------------------------- | ------------------------------------------------------------------------- |
| SaveMode.Overwrite     | Upsert                                              | Document will be created if it does not exist                             |
| SaveMode.ErrorIfExists | Insert                                              | Operations will fail with DocumentExistsException if doc already exists   |
| SaveMode.Ignore        | Insert                                              | If the document already exists, that operation will be skipped            |
| SaveMode.Append        | _not supported_                                     |                                                                           |
| WriteModeReplace       | Replace                                             | Operations will fail with DocumentNotFoundException if doc does not exist |
| WriteModeSubdocUpsert  | mutateIn (sub-document) with StoreSemantics.Upsert  | Document will be created if it does not exist                             |
| WriteModeSubdocInsert  | mutateIn (sub-document) with StoreSemantics.Insert  | Operations will fail with DocumentExistsException if doc already exists   |
| WriteModeSubdocReplace | mutateIn (sub-document) with StoreSemantics.Replace | Operations will fail with DocumentNotFoundException if doc does not exist |

__Table 2\. couchbase.query mappings__
| SaveMode               | Couchbase SQL++                               |
| ---------------------- | --------------------------------------------- |
| SaveMode.Overwrite     | UPSERT INTO                                   |
| SaveMode.ErrorIfExists | INSERT INTO                                   |
| SaveMode.Ignore        | INSERT INTO (Ignores DocumentExistsException) |
| SaveMode.Append        | _not supported_                               |

### [](#failure-handling-during-persistence)Failure handling during persistence

The default is that the failure of any individual operation will fail the overall job.

For key-value DataFrame writes, this can be overridden with two error handling options.

`KeyValueOptions.ErrorBucket` will cause any operation failure to write a document back into a Couchbase collection, containing information identifying the failing document and the failure reason. This is the recommended approach.

```scala
dataFrame.write
  .format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "aBucket")
  .option(KeyValueOptions.Scope, "aScope")
  .option(KeyValueOptions.Collection, "aCollection")
  // Specify a Couchbase collection to write errors to
  .option(KeyValueOptions.ErrorBucket, "errorBucket")
  .option(KeyValueOptions.ErrorScope, "errorScope")
  .option(KeyValueOptions.ErrorCollection, "errorCollection")
  .save()
```

`KeyValueOptions.ErrorHandler` will call an error handling callback. An example implementation of the interface is provided with the connector, and users are free to write their own also.

Refer to the Spark `KeyValueOptions` API documentation for further information.

### [](#safe-dataframe-persistence)Safe DataFrame persistence

Couchbase supports optimistic concurrency via CAS for query DataFrame reads and key-value DataFrame writes, which can be used with the Couchbase Spark Connector as shown:

```scala
val airlines = spark.read.format("couchbase.query")
  .option(QueryOptions.Bucket, "travel-sample")
  .option(QueryOptions.Scope, "inventory")
  .option(QueryOptions.Collection, "airline")
  // Adds a field named "__META_CAS" to the DataFrame, with each document's CAS
  .option(QueryOptions.OutputCas, "true")
  .load()
  .limit(5)

airlines.write.format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "test-bucket")
  .option(KeyValueOptions.Scope, "test-scope")
  .option(KeyValueOptions.Collection, "test-collection")
  // Both enables CAS and specifies the field name to use (the constant here is "__META_CAS")
  .option(KeyValueOptions.CasFieldName, DefaultConstants.DefaultCasFieldName)
  // CAS is only supported with replace operations
  .option(KeyValueOptions.WriteMode, KeyValueOptions.WriteModeReplace)
  .save()
```

This protects against documents being modified between the read and write points. Such modifications will cause the operation to fail with a `CasMismatchException`. This will by default also cause the job to fail, which can be configured with the error handling options detailed elsewhere.

### [](#sub-document-dataframe-kv-persistence)Sub-document DataFrame KV persistence

Couchbase supports sub-document writes that update only specific parts of the document, and users writing large documents may find this provides a performance optimisation, or allows concurrent actors to modify different parts of the same documents. The Spark Connector exposes sub-document KV writes via both [RDDs](working-with-rdds.md) and [DataFrames](subdocument.md).

### [](#dataframe-persistence-performance-tips)DataFrame persistence performance tips

We strongly recommend using the KeyValue data source for persisting DataFrames. This will automatically provide the best possible write performance.

But if the query data source is required, then we recommend:

* Partition the data before writing it. (Each partition results in one INSERT or UPSERT SQL++ statement being executed by the connector.)
* Observe the Spark worker logs to see how long each query is taking and if timeouts are occurring. Increase the partition count and/or the timeout value as needed.
* The multiple large SQL++ statements that can be generated by the connector with large datasets may fill query service’s system:completed\_requests table, leading to high query memory usage and potentially out-of-memory issues. Consider disabling or increasing the threshold for this, following [these docs](#https://docs.couchbase.com/server/current/n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config).
* And standard recommendations for writing at scale: consider using separate nodes for query and KV; use disks that can support the throughput needed; use powerful enough nodes to support the throughput needed; ensure there is sufficient network bandwidth.

## [](#%5Fdatasets)Datasets

You can call `.as[Target]` on your `DataFrame` to turn it into typesafe counterpart (most of the time a case class).

(Note that Apache Spark only supports Datasets in Scala - there is no PySpark equivalent.)

Consider having the following case class:

```scala
case class Airline(name: String, iata: String, icao: String, country: String)
```

Make sure to import the implicits for the `SparkSession`:

```scala
import spark.implicits._
```

You can now create a DataFrame as usual which can be turned into a Dataset:

```scala
val airlines = spark.read.format("couchbase.query")
  .option(QueryOptions.Bucket, "travel-sample")
  .option(QueryOptions.Scope, "inventory")
  .option(QueryOptions.Collection, "airline")
  .load()
  .as[Airline]
```

If you want to print all Airlines that start with "A" you can access the properties on the case class:

```scala
airlines
  .map(_.name)
  .filter(_.toLowerCase.startsWith("a"))
  .foreach(println(_))
```

For more information on Datasets, please refer to the [Spark Dataset Docs](http://spark.apache.org/docs/latest/sql-programming-guide.html#datasets).

## [](#options)Options

### [](#%5Fquery%5Foptions)Query options

The available options for query DataFrame and Dataset operations:

__Table 3\. Query Options__
| PySpark                                                                        | Scala & Java                                                                                                               | Option                                                                                                                                                                    | Default                                                                                                                                                     |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "bucket"                                                                       | QueryOptions.Bucket                                                                                                        | Name of a Couchbase bucket                                                                                                                                                | Mandatory unless [implicitBucket is set](configuration.md#%5Foptional%5Fproperties)                                                                         |
| "scope"                                                                        | QueryOptions.Scope                                                                                                         | Name of a Couchbase scope                                                                                                                                                 | Defaults to the default scope on the specified bucket. Note [implicitScope can be set in Spark config](configuration.md#%5Foptional%5Fproperties).          |
| "collection"                                                                   | QueryOptions.Collection                                                                                                    | Name of a Couchbase collection                                                                                                                                            | Defaults to the default collection on the specified scope. Note [implicitCollection can be set in Spark config](configuration.md#%5Foptional%5Fproperties). |
| "timeout"                                                                      | QueryOptions.Timeout                                                                                                       | Overrides the default timeout. The string must be parsable from a Scala Duration.                                                                                         | 75 seconds                                                                                                                                                  |
| "idFieldName"                                                                  | QueryOptions.IdFieldName                                                                                                   | Uses a different column when [persisting a DataFrame](#%5Fdataframe%5Fpersistence).                                                                                       | "META\_ID" column                                                                                                                                           |
| "filter"                                                                       | QueryOptions.Filter                                                                                                        | A SQL expression that will be interjected directly into the generated SQL, e.g. type = 'airport'.                                                                         | None                                                                                                                                                        |
| "partitionColumn" "partitionLowerBound" "partitionUpperBound" "partitionCount" | QueryOptions.PartitionColumn QueryOptions.PartitionLowerBound QueryOptions.PartitionUpperBound QueryOptions.PartitionCount | Control how [manual DataFrame partitioning](#%5Fdataframe%5Fpartitioning) is performed.                                                                                   | None                                                                                                                                                        |
| "scanConsistency"                                                              | QueryOptions.ScanConsistency                                                                                               | Valid options are "requestPlus" / QueryOptions.RequestPlusScanConsistency and "notBounded" / QueryOptions.NotBoundedScanConsistency.                                      | "notBounded"                                                                                                                                                |
| "inferLimit"                                                                   | QueryOptions.InferLimit                                                                                                    | Controls how many documents are initially sampled to perform [schema inference](#%5Fschemas).                                                                             | 1000                                                                                                                                                        |
| "connectionIdentifier"                                                         | QueryOptions.ConnectionIdentifier                                                                                          | Allows a different configuration to be used than the default one. See [Connecting to multiple clusters](configuration.md#%5Fconnecting%5Fto%5Fmultiple%5Fclusters).       | Default connection                                                                                                                                          |
| "outputCas"                                                                    | QueryOptions.OutputCas                                                                                                     | Adds a field to the DataFrame, containing each document’s CAS value for use in optimistic concurrency control. The field name is controlled by QueryOptions.CasFieldName. | <does not output CAS>                                                                                                                                       |
| "casFieldName"                                                                 | QueryOptions.CasFieldName                                                                                                  | Controls the name of the field that is output by QueryOptions.OutputCas                                                                                                   | "\_\_META\_CAS"                                                                                                                                             |

### [](#%5Fenterprise%5Fanalytics%5Foptions)Enterprise Analytics options

The available options for Enterprise Analytics DataFrame and Dataset operations:

__Table 4\. Enterprise Analytics Options__
| PySpark           | Scala & Java                               | Option                                                                                                                                                           | Default      |
| ----------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| "database"        | EnterpriseAnalyticsOptions.Database        | Name of an Enterprise Analytics database                                                                                                                         | Mandatory    |
| "scope"           | EnterpriseAnalyticsOptions.Scope           | Name of an Enterprise Analytics scope                                                                                                                            | Mandatory    |
| "collection"      | EnterpriseAnalyticsOptions.Collection      | Name of an Enterprise Analytics collection                                                                                                                       | Mandatory    |
| "timeout"         | EnterpriseAnalyticsOptions.Timeout         | Overrides the default timeout. The string must be parsable from a Scala Duration.                                                                                | 10 minutes   |
| "filter"          | EnterpriseAnalyticsOptions.Filter          | A SQL expression that will be interjected directly into the generated SQL, e.g. type = 'airport'.                                                                | None         |
| "scanConsistency" | EnterpriseAnalyticsOptions.ScanConsistency | Valid options are "requestPlus" / EnterpriseAnalyticsOptions.RequestPlusScanConsistency and "notBounded" / EnterpriseAnalyticsOptions.NotBoundedScanConsistency. | "notBounded" |
| "inferLimit"      | EnterpriseAnalyticsOptions.InferLimit      | Controls how many documents are initially sampled to perform [schema inference](#%5Fschemas).                                                                    | 1000         |

### [](#%5Fkv%5Foptions)KeyValue options

The available options for query DataFrame and Dataset operations:

__Table 5\. KeyValue Options__
| PySpark                | Scala & Java                         | Option                                                                                                                                                                                                                                 | Default                                                                                                                                                     |
| ---------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "bucket"               | KeyValueOptions.Bucket               | Name of a Couchbase bucket                                                                                                                                                                                                             | Mandatory unless [implicitBucket is set](configuration.md#%5Foptional%5Fproperties)                                                                         |
| "scope"                | KeyValueOptions.Scope                | Name of a Couchbase scope                                                                                                                                                                                                              | Defaults to the default scope on the specified bucket. Note [implicitScope can be set in Spark config](configuration.md#%5Foptional%5Fproperties).          |
| "collection"           | KeyValueOptions.Collection           | Name of a Couchbase collection                                                                                                                                                                                                         | Defaults to the default collection on the specified scope. Note [implicitCollection can be set in Spark config](configuration.md#%5Foptional%5Fproperties). |
| "timeout"              | KeyValueOptions.Timeout              | Overrides the default timeout. The string must be parsable from a Scala Duration.                                                                                                                                                      | 2.5 seconds for non-durable operations, 10 seconds for durable operations                                                                                   |
| "idFieldName"          | KeyValueOptions.IdFieldName          | Uses a different column when [persisting a DataFrame](#%5Fdataframe%5Fpersistence).                                                                                                                                                    | "META\_ID" column                                                                                                                                           |
| "durability"           | KeyValueOptions.Durability           | Valid options are "none", "majority" / KeyValueOptions.MajorityDurability, "majorityAndPersistToActive" / KeyValueOptions.MajorityAndPersistToActiveDurability, and "PersistToMajority" / KeyValueOptions.PersistToMajorityDurability. | "none"                                                                                                                                                      |
| "connectionIdentifier" | KeyValueOptions.ConnectionIdentifier | Allows a different configuration to be used than the default one. See [Connecting to multiple clusters](configuration.md#%5Fconnecting%5Fto%5Fmultiple%5Fclusters).                                                                    | Default connection                                                                                                                                          |
| "writeMode"            | KeyValueOptions.WriteMode            | Controls the write behavior, overriding the Spark SaveMode. The only valid option currently is KeyValueOptions.WriteModeReplace ("replace" for PySpark users).                                                                         | None (uses SaveMode)                                                                                                                                        |
| "casFieldName"         | KeyValueOptions.CasFieldName         | Both enables optimistic locking detection (CAS) for operations that support it, and specifies the field name containing CAS values.                                                                                                    | <CAS detection is disabled>>                                                                                                                                |
| "errorBucket"          | KeyValueOptions.ErrorBucket          | Enable writing error documents to a given bucket if operations fail.                                                                                                                                                                   | None (operations fail the job)                                                                                                                              |
| "errorScope"           | KeyValueOptions.ErrorScope           | Further customises KeyValueOptions.ErrorBucket to output to a particular scope.                                                                                                                                                        | Default scope                                                                                                                                               |
| "errorCollection"      | KeyValueOptions.ErrorCollection      | Further customises KeyValueOptions.ErrorBucket to output to a particular collection.                                                                                                                                                   | Default collection                                                                                                                                          |
| "errorHandler"         | KeyValueOptions.ErrorHandler         | Custom error handler class for handling operation failures. Must implement the appropriate interface.                                                                                                                                  | None (operations fail the job)                                                                                                                              |

### [](#%5Fcolumnar%5Foptions)Capella Columnar options

The available options for Capella Columnar DataFrame and Dataset operations:

__Table 6\. Capella Columnar Options__
| PySpark                | Scala & Java                         | Option                                                                                                                                                              | Default            |
| ---------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| "database"             | ColumnarOptions.Database             | Name of a Couchbase Columnar database                                                                                                                               | Mandatory          |
| "scope"                | ColumnarOptions.Scope                | Name of a Couchbase Columnar scope                                                                                                                                  | Mandatory          |
| "collection"           | ColumnarOptions.Collection           | Name of a Couchbase Columnar collection                                                                                                                             | Mandatory          |
| "timeout"              | ColumnarOptions.Timeout              | Overrides the default timeout. The string must be parsable from a Scala Duration.                                                                                   | 10 minutes         |
| "filter"               | ColumnarOptions.Filter               | A SQL expression that will be interjected directly into the generated SQL, e.g. type = 'airport'.                                                                   | None               |
| "scanConsistency"      | ColumnarOptions.ScanConsistency      | Valid options are "requestPlus" / ColumnarOptions.RequestPlusScanConsistency and "notBounded" / ColumnarOptions.NotBoundedScanConsistency.                          | "notBounded"       |
| "inferLimit"           | ColumnarOptions.InferLimit           | Controls how many documents are initially sampled to perform [schema inference](#%5Fschemas).                                                                       | 1000               |
| "connectionIdentifier" | ColumnarOptions.ConnectionIdentifier | Allows a different configuration to be used than the default one. See [Connecting to multiple clusters](configuration.md#%5Fconnecting%5Fto%5Fmultiple%5Fclusters). | Default connection |

## [](#aggregate-push-down)Aggregate Push Down

The following predicates are pushed down to the query, operational analytics, Enterprise Analytics, and Capella Columnar engines if possible:

* `MIN(field)`
* `MAX(field)`
* `COUNT(field)`
* `SUM(field)`
* `COUNT(*)`

They are supported both with and without grouping (`GROUP BY`).

For performance reasons, this feature is enabled by default, unless using [manual partitioning](#%5Fdataframe%5Fpartitioning). If for some reason it should be disabled, the `PushDownAggregate` option can be used in which case Spark will handle the aggregations after receiving the results.