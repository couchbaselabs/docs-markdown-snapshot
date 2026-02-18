---
title: Java API
editUrl: https://github.com/couchbase/docs-spark/edit/release/3.5/modules/ROOT/pages/java-api.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/spark-connector/current/java-api.html)

# Java API

> In addition to the Scala API, some APIs can also be accessed from Java. 

## [](#creating-a-spark-session)Creating a Spark Session

When accessing Spark from java, a `SparkSession` needs to be created, similar to this:

```java
SparkSession spark = SparkSession
  .builder()
  .master("local[*]")
  .appName("Java API")
  .config("spark.couchbase.connectionString", "127.0.0.1")
  .config("spark.couchbase.username", "Administrator")
  .config("spark.couchbase.password", "password")
  .config("spark.couchbase.implicitBucket", "travel-sample")
  .getOrCreate();
```

Properties and configuration are set in the same way.

## [](#using-sparksql-dataframes)Using SparkSQL DataFrames

The `DataFrame` APIs can be accessed very similarly from Java compared to Scala.

```java
Dataset<Row> airlines = spark.read()
  .format("couchbase.query")
  .option(QueryOptions.Filter(), "type = 'airline'")
  .option(QueryOptions.Bucket(), "travel-sample")
  .load();

airlines.show(3);
```

Note that since later version of Spark 2, a `DataFrame` is just an alias for a `Dataset<Row>` and can be interacted with in the same way.

If executed against the `travel-sample` bucket, this will print:

```none
+-------------+--------+-------------+----+----+-----+-----------+-------+
|    __META_ID|callsign|      country|iata|icao|   id|       name|   type|
+-------------+--------+-------------+----+----+-----+-----------+-------+
|   airline_10|MILE-AIR|United States|  Q5| MLA|   10|40-Mile Air|airline|
|airline_10123|     TXW|United States|  TQ| TXW|10123|Texas Wings|airline|
|airline_10226|  atifly|United States|  A1| A1F|10226|     Atifly|airline|
+-------------+--------+-------------+----+----+-----+-----------+-------+
```

Please see the corresponding scala sections for `DataFrame` on how to configure the data source and which properties can be applied.

## [](#using-sparksql-datasets)Using SparkSQL Datasets

Since Datasets work with actual Java objects, first create one:

```java
public static class Airline implements Serializable {

  private String name;
  private String callsign;
  private String country;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getCallsign() {
    return callsign;
  }

  public void setCallsign(String callsign) {
    this.callsign = callsign;
  }

  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }

  @Override
  public String toString() {
    return "Airline{" +
      "name='" + name + '\'' +
      ", callsign='" + callsign + '\'' +
      ", country='" + country + '\'' +
      '}';
  }
}
```

Next, you can convert a `DataFrame` to a `Dataset` through the `.as()` API:

```java
Dataset<Airline> airlines = spark.read()
  .format("couchbase.query")
  .option(QueryOptions.Filter(), "type = 'airline'")
  .option(QueryOptions.Bucket(), "travel-sample")
  .load()
  .as(Encoders.bean(Airline.class));

airlines
  .limit(3)
  .foreach(airline -> {
    System.out.println("Airline:" + airline);
  });
```

This will print:

```none
Airline:Airline{name='40-Mile Air', callsign='MILE-AIR', country='United States'}
Airline:Airline{name='Texas Wings', callsign='TXW', country='United States'}
Airline:Airline{name='Atifly', callsign='atifly', country='United States'}
```

## [](#rdd-access)RDD Access

Raw RDD access from the Java API is currently not available, please use the higher level DataFrame and Dataset APIs.