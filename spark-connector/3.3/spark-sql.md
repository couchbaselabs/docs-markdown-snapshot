---
title: Spark SQL Integration
editUrl: https://github.com/couchbase/docs-spark/edit/release/3.3/modules/ROOT/pages/spark-sql.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/spark-connector/3.3/spark-sql.html)

# Spark SQL Integration

> Spark SQL allows accessing Query and Analytics in powerful and convenient ways. 

All query examples presented on this page at least require a primary index on the `travel-sample` data set - or on each collection respectively. If you haven’t done so already, you can create a primary index by executing this N1QL statement: `` CREATE PRIMARY INDEX ON `travel-sample` ``.

To use the analytics examples, corresponding datasets or collection mappings should be created.

## [](#dataframe-creation)DataFrame creation

Before you can create a DataFrame with Couchbase, you need to create a `SparkSession`.

```scala
val spark = SparkSession
  .builder()
  .master("local[*]")
  .appName("Spark SQL")
  .config("spark.couchbase.connectionString", "127.0.0.1")
  .config("spark.couchbase.username", "Administrator")
  .config("spark.couchbase.password", "password")
  .config("spark.couchbase.implicitBucket", "travel-sample")
  .getOrCreate()
```

A `DataFrame` can be created through `spark.read.format(…​)`, and which format to choose depends on the type of service you want to use. Both `couchbase.query` and `couchbase.analytics` are available.

```scala
val queryDf = spark.read.format("couchbase.query").load()

val analyticsDf = spark.read.format("couchbase.analytics").load()
```

While this is the easiest, it has an important property to keep in mind:

It will try to perform automatic schema inference based on the full data set, which is very likely to not hit the right schema (especially if you have a large or diverse data set) - unless you are using a specific collection for each document type.

There are two options to change this: you can either provide a manual schema or narrow down the automatic schema inference by providing explicit predicates. The benefit of the latter approach is also that the predicate provided will be used on every query to optimize performance.

If you want to get automatic schema inference on all airlines, you can specify it like this:

```scala
val airlines = spark.read
  .format("couchbase.query")
  .option(QueryOptions.Filter, "type = 'airline'")
  .load()
```

If you call `airlines.printSchema()`, it will print:

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

A manual schema can also be provided if the automatic inference does not work properly:

```scala
val airlines = spark.read
  .format("couchbase.query")
  .schema(StructType(
    StructField("name", StringType) ::
      StructField("type", StringType) :: Nil
  ))
  .load()
```

Now that you have a DataFrame, you can apply all the operations that Spark SQL provides. A simple example would be to load specific fields from the DataFrame and print some of those records:

```scala
airlines
  .select("name", "callsign")
  .sort(airlines("callsign").desc)
  .show(10)
```

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

It is also possible to provide a custom schema as well as a predicate for maximum flexibility when describing your data layout as well as optimizing the performance when retrieving unstructured data.

## [](#dataframe-partitioning)DataFrame partitioning

By default, one DataFrame read or write with query will result in one SQL++ statement being executed.

With very large DataFrames this can present issues, as all rows are streamed back to one Spark worker. In addition there is no parallelism.

So in some specific situations the user may wish to provide partitioning hints so that multiple SQL++ statements are executed.

In this example, say we are reading from an orders collection, where we know we have around 100,000 orders and want to partition into 100 SQL++ statements. Here we will partition on a numerical "id" column:

```none
spark.read
  .format("couchbase.query")
  .option(QueryOptions.PartitionColumn, "id")
  .option(QueryOptions.PartitionLowerBound, "1")
  .option(QueryOptions.PartitionUpperBound, "100000")
  .option(QueryOptions.PartitionCount, "100")
  .load()
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

## [](#dataframe-persistence)DataFrame persistence

It is also possible to persist DataFrames into Couchbase. The important part is that a `META_ID` (or different if configured) field exists which can be mapped to the unique Document ID. All the other fields in the DataFrame will be converted into JSON and stored as the document content.

You can store `DataFrames` using both `couchbase.query` and `couchbase.kv`. We recommend using the KeyValue data source since it provides better performance out of the box if the usage pattern allows for it.

The following example reads data from a bucket and writes the first 5 results into a different bucket. Also, to showcase properties, they are used on both the read and the write side:

```scala
val airlines = spark.read.format("couchbase.query")
  .option(QueryOptions.Filter, "type = 'airline'")
  .load()
  .limit(5)

airlines.write.format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "test")
  .option(KeyValueOptions.Durability, KeyValueOptions.MajorityDurability)
  .save()
```

### [](#savemode-mapping)SaveMode Mapping

SparkSQL DataFrames allow to configure how data is written to the data source by specifying a [SaveMode](https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/sql/SaveMode.html), of which there are four: `Append`, `Overwrite`, `ErrorIfExists` and `Ignore`.

Couchbase has similar names for different write semantics: `Insert`, `Upsert` and `Replace`. The following tables descripe the mappings for both `couchbase.query` and `couchbase.kv`:

Note that `SaveMode.Append` is not supported, since the operations are always writing the full document body (and not appending to one).

__Table 1\. couchbase.kv mappings__
| SparkSQL               | Couchbase KV                             |
| ---------------------- | ---------------------------------------- |
| SaveMode.Overwrite     | Upsert                                   |
| SaveMode.ErrorIfExists | Insert                                   |
| SaveMode.Ignore        | Insert (Ignores DocumentExistsException) |
| SaveMode.Append        | _not supported_                          |

__Table 2\. couchbase.query mappings__
| SparkSQL               | Couchbase N1QL  |
| ---------------------- | --------------- |
| SaveMode.Overwrite     | UPSERT INTO     |
| SaveMode.ErrorIfExists | INSERT INTO     |
| SaveMode.Ignore        | INSERT INTO     |
| SaveMode.Append        | _not supported_ |

## [](#working-with-datasets)Working with Datasets

You can call `.as[Target]` on your `DataFrame` to turn it into typesafe counterpart (most of the time a case class). Consider having the following case class:

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
  .option(QueryOptions.Filter, "type = 'airline'")
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

Fore more information on Datasets, please refer to the [Spark Dataset Docs](http://spark.apache.org/docs/latest/sql-programming-guide.html#datasets).

## [](#aggregate-push-down-spark-3-2-0)Aggregate Push Down (Spark 3.2.0+)

Apache Spark SQL 3.2.0 added support for [aggregate push downs](https://issues.apache.org/jira/browse/SPARK-34952), and since the Connector version 3.2.0 this feature is supported as well.

The following predicates are pushed down to both the query and analytics engines if possible:

* `MIN(field)`
* `MAX(field)`
* `COUNT(field)`
* `SUM(field)`
* `COUNT(*)`

They are supported both with and without grouping (`GROUP BY`).

For performance reasons, this feature is enabled by default. If for some reason it should be disabled, the `PushDownAggregate` option can be used. Note that your queries will still work fine (although likely slower) since Spark will handle the aggregations in this case.