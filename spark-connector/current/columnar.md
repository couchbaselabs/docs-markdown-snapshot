---
title: Capella Columnar Support
editUrl: https://github.com/couchbase/docs-spark/edit/release/3.5/modules/ROOT/pages/columnar.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:spark-connector::columnar.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/spark-connector/current/columnar.html)

# Capella Columnar Support

> Connecting to Capella Columnar is very similar to connecting to any Couchbase cluster. This section explains how. 

Capella Columnar clusters can be connected to using either Scala or PySpark. To get bootstrapped, users should view the [Scala getting started](getting-started.md) or [PySpark getting started](pyspark.md) guides.

## [](#spark-configuration)Spark Configuration

The first step as usual is to create a `SparkSession`, here connecting to your Capella Columnar cluster. This works just like connecting to any other type of Couchbase cluster.

Scala

Change the cluster configuration options to match your own.

```scala
val spark = SparkSession
  .builder()
  .appName("Couchbase Spark Connector Columnar Example") // your app name
  .master("local[*]") // your local or remote Spark master node
  .config("spark.couchbase.connectionString", "couchbases://your-columnar-endpoint.cloud.couchbase.com")
  .config("spark.couchbase.username", "username")
  .config("spark.couchbase.password", "password")
  .getOrCreate()
```

PySpark

Change the cluster configuration options to match your own, and provide the location of the Spark Connector library if needed (see the [PySpark getting started](pyspark.md) guide for more details).

```python
spark = (SparkSession.builder
    .appName("Couchbase Spark Connector Columnar Example")
    # Note whether you need the .master(...) and .config("spark.jars"...) lines depends on how you are using Spark.
    # See our PySpark documentation for more details.
    .master("local[*]")
    .config("spark.jars", "/path/to/spark-connector-assembly-<version>.jar")
    .config("spark.couchbase.connectionString", "couchbases://cb.your.columnar.connection.string.com")
    .config("spark.couchbase.username", "YourColumnarUsername")
    .config("spark.couchbase.password", "YourColumnarPassword")
    .getOrCreate())
```

The following examples will use the `travel-sample` example set of data, which can be loaded through the UI.

## [](#reading-a-dataframe)Reading a Dataframe

Let’s start by reading a Spark DataFrame from the `airline` collection, which is in the `inventory` scope of the `travel-sample` database:

* Scala
* PySpark

```scala
val airlines = spark.read
  .format("couchbase.columnar")
  .option(ColumnarOptions.Database, "travel-sample")
  .option(ColumnarOptions.Scope, "inventory")
  .option(ColumnarOptions.Collection, "airline")
  .load
```

```python
airlines = (spark.read
    .format("couchbase.columnar")
    .option("database", "travel-sample")
    .option("scope", "inventory")
    .option("collection", "airline")
    .load())
```

This is a normal Spark DataFrame that we can count, iterate and so on.

* Scala
* PySpark

```scala
println(airlines.count)

airlines.foreach(row => {
  val id = row.getAs[String]("id")
  val name = row.getAs[String]("name")
  println(s"Row: id=${id} name=${name}")
})
```

```python
airlines.show()
print(airlines.count())

collected = airlines.collect()

for airline in collected:
    print(airline)
    id = airline["id"]
    name = airline["name"]
    print(f"Airline: id={id} name={name}")
```

## [](#reading-a-dataset)Reading a Dataset

(Supported in Scala only, as Apache Spark does not support Datasets via PySpark.)

It can be preferable to read into a Spark `Dataset` rather than a DataFrame, as this lets us use Scala case classes directly.

To do this, we:

1. Create an `Airline` case class that matches our expected results.
2. Import the `SparkSession` implicits allowing Spark to convert directly to our `Airline` class.
3. Do `.as[Airline]` to turn our DataFrame into a `Dataset`.

```scala
case class Airline(id: String, name: String, country: String) // (1)

val sparkSession = spark
import sparkSession.implicits._ // (2)

val airlinesDataset = spark.read
  .format("couchbase.columnar")
  .option(ColumnarOptions.Database, "travel-sample")
  .option(ColumnarOptions.Scope, "inventory")
  .option(ColumnarOptions.Collection, "airline")
  .load
  .as[Airline] // (3)
```

## [](#spark-sql)Spark SQL

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
print(airlinesFromView.count())
```

Note this SQL is executed purely within Spark, and is not sent to the Capella Columnar cluster.