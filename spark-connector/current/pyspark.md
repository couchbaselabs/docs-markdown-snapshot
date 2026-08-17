---
title: Getting Started (PySpark)
description: You can use the Couchbase Spark Connector together with PySpark to
  quickly and easily explore your data.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-spark/edit/release/3.5/modules/ROOT/pages/pyspark.adoc
  xref: xref:spark-connector::pyspark.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/spark-connector/current/pyspark.html)

# Getting Started (PySpark)

> You can use the Couchbase Spark Connector together with PySpark to quickly and easily explore your data. 

This page is for PySpark users — Scala users should go to the [Scala getting started](getting-started.md) guide.

## [](#using-the-couchbase-spark-connector-with-pyspark)Using the Couchbase Spark Connector with PySpark

To use the Couchbase Spark Connector with PySpark:

Download and extract the [current version of the Couchbase Spark Connector](download-links.md) to get the `spark-connector-assembly-VERSION.jar` file. This file contains the connector.

There are many ways to run PySpark, and this documentation will cover the most common three:

1. Creating a Jupyter Notebook.
2. Creating a Python script and submitting it to a Spark cluster using `spark-submit`.
3. Creating a Python script and running it locally.

In addition the Couchbase Spark Connector can be used with Scala or PySpark in environments such as Databricks - see our [Databricks documentation](databricks.md).

Note the following examples assume you already have a Couchbase cluster running, with the `travel-sample` sample data loaded.

Also see the examples under [Couchbase Spark Connector PySpark examples](#https://github.com/couchbase/couchbase-spark-connector/tree/master/src/test/pyspark/examples), which include a guide to using the Couchbase Spark Connector together with Spark MLLib.

## [](#using-the-couchbase-spark-connector-with-jupyter-notebooks)Using the Couchbase Spark Connector with Jupyter Notebooks

The Couchbase Spark Connector can easily be used together with a Jupyter Notebook.

To get started quickly, you can run the following commands.

First, download and extract the [current version of the Couchbase Spark Connector](download-links.md) to get the `spark-connector-assembly-VERSION.jar` file. This file contains the connector.

Now install Jupyter and PySpark. Note it is a standard Python best practice to do this inside a Python virtual environment (venv, Conda, etc.), but those details are omitted here:

```console
pip install jupyter pyspark
```

Run Jupyter:

```console
jupyter notebook
```

And now the same example from the section above can be copy and pasted into the Jupyter UI, and run. There is no need to install Apache Spark first.

Also see the notebook examples under [Couchbase Spark Connector PySpark examples](https://github.com/couchbase/couchbase-spark-connector/blob/master/src/test/pyspark/examples/).

### [](#using-spark-submit)Using `spark-submit`

Use the `spark-submit` command, which is part of the standard Apache Spark installation, with your Spark Python script to submit it to a local or remote Spark cluster.

The important points are:

* The `spark-submit` `--jars` argument is provided, pointing at the downloaded Couchbase Spark Connector assembly jar.
* The `SparkSession` config `.master()` is not provided, as deciding the Spark master is handled by the arguments provided to `spark-submit`.

  * To use a local Spark master (it will automatically start it if required):  
  ```console  
  bin/spark-submit --jars spark-connector-assembly-VERSION.jar YourPythonScript.py  
  ```
  * To connect to a pre-existing Spark master:  
  ```console  
  bin/spark-submit --master spark://your-spark-host:7077 --jars spark-connector-assembly-VERSION.jar YourPythonScript.py  
  ```

#### [](#example)Example

A sample Python/PySpark script that uses the Couchbase Spark Connector and can be used with `spark-submit` is:

```sh
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Couchbase Spark Connector Example") \
    .config("spark.couchbase.connectionString", "couchbases://YourCouchbaseClusterHostname") \
    .config("spark.couchbase.username", "test") \
    .config("spark.couchbase.password", "Password!1") \
    .getOrCreate()
df = spark.read.format("couchbase.query") \
    .option("bucket", "travel-sample") \
    .option("scope", "inventory") \
    .option("collection", "airline") \
    .load()
df.printSchema()
df.show()
spark.stop()
```

### [](#using-the-couchbase-spark-connector-with-a-local-spark-test-cluster)Using the Couchbase Spark Connector with a local Spark test cluster

For testing purposes, the `.master("local[*]")` Spark option can be used, which automatically starts a local Spark cluster.

The important points are:

* The location of the Couchbase Spark Connector assembly jar must be provided with `.config("spark.jars", "/path/to/spark-connector-assembly-<version>.jar")`.
* `.master("local[*]")` is used (though this is the default and so can be omitted).

A sample Python/PySpark script that uses the Couchbase Spark Connector and this mode is:

```sh
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Couchbase Spark Connector Example") \
    .master("local[*]") \
    .config("spark.jars", "/path/to/spark-connector-assembly-<version>.jar")
    .config("spark.couchbase.connectionString", "couchbases://YourCouchbaseClusterHostname") \
    .config("spark.couchbase.username", "test") \
    .config("spark.couchbase.password", "Password!1") \
    .getOrCreate()
df = spark.read.format("couchbase.query") \
    .option("bucket", "travel-sample") \
    .option("scope", "inventory") \
    .option("collection", "airline") \
    .load()
df.printSchema()
df.show()
spark.stop()
```

You can run this script normally, e.g. `python YourPythonScript.py`. There is no need to install Apache Spark first, but do install the dependencies:

```console
pip install pyspark
```

## [](#supported-operations)Supported Operations

Apache recommends using DataFrames over RDDs, and the Couchbase Spark Connector allows access to all DataFrame operations.

__Table 1\. Operations supported in PySpark__
| Operation                                                   | Examples                                                                                                                                                                                                       | PySpark Support | Scala & Java Support |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------- |
| [DataFrame reads](spark-sql.md)                             | \* spark.read.format("couchbase.query").load()\* spark.read.format("couchbase.analytics").load()\* spark.read.format("couchbase.enterprise-analytics").load()\* spark.read.format("couchbase.columnar").load() | ✅               | ✅                    |
| [DataFrame writes](spark-sql.md#%5Fdataframe%5Fpersistence) | \* airlines.write.format("couchbase.kv").save()\* airlines.write.format("couchbase.query").save()                                                                                                              | ✅               | ✅                    |
| [Datasets](spark-sql.md#%5Fdatasets)                        | spark.read.format("couchbase.query").load().as\[Airline\]                                                                                                                                                      | ❌ (1)           | ✅                    |
| [RDD operations](working-with-rdds.md)                      | \* spark.sparkContext.couchbaseGet(Seq(Get("airline\_10"))).collect()\* spark.sparkContext.couchbaseQuery\[JsonObject\](…​).collect()\* spark.sparkContext…​couchbaseUpsert(…​).collect()                      | ❌ (2)           | ✅                    |

(1) Apache Spark does not support Datasets in PySpark, as they are specific to Scala case classes.

(2) RDD operations are not supported, as these require Scala specifics that are not supportable through the PySpark interface. These operations include reading from KV and executing arbitrary SQL++, both of which use RDDs.

## [](#troubleshooting-pyspark)Troubleshooting PySpark

If problems are seen, then ensure you are using compatible Scala versions. The latest `pyspark` package (at the time of writing) is internally running Scala 2.12, so the 2.12-compiled version of the Couchbase Spark Connector must also be used. If you see errors mentioning `NoSuchMethodError`, this is very likely the cause.

The versions can be checked with the following:

```python
from py4j.java_gateway import java_import
from pyspark.sql import SparkSession
import pyspark

print(f"Versions: pyspark.__version__={pyspark.__version__}")

spark = SparkSession.builder # copy from code above

# Access the Spark Context's JVM directly, to check the Scala version (which must be compatible with the Couchbase Spark Connector)
sc = spark.sparkContext
gw = sc._gateway
java_import(gw.jvm, "org.apache.spark.repl.Main")
scala_version = gw.jvm.scala.util.Properties.versionString()

print(f"Versions: spark.version={spark.version} Scala version={scala_version}")

spark.stop()
```