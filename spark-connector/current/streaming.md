[View original HTML](/spark-connector/current/streaming.html)

> Spark Structured Streaming for Couchbase is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine and the Couchbase Data Service. 

## [](#overview)Overview

The connector supports Spark Structured Streaming (as opposed to the older streaming support through `DStreams`) which is built on top of the Spark SQL capabilities.

|  | The basic concepts of how structured streaming works are not discussed in this document - please refer to the [official Spark documentation](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#basic-concepts) for further information. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Two modes of operation are available, both with different fault-tolerance guarantees that match the Spark semantics:

* **Continuous**: At-Least-Once
* **MicroBatch** (Intervals and Once): Exactly-Once

## [](#basic-usage)Basic Usage

To use the spark streaming integration a streaming source `DataFrame` needs to be created. Like the other APIs available, the basic configuration is picked up from the `SparkSession`:

```scala
val spark = SparkSession
  .builder()
  .master("local[*]")
  .appName("Structured Streaming Example")
  .config("spark.couchbase.connectionString", "127.0.0.1")
  .config("spark.couchbase.username", "Administrator")
  .config("spark.couchbase.password", "password")
  .config("spark.couchbase.implicitBucket", "travel-sample")
  .getOrCreate()
```

The simplest way to stream the whole bucket (picked up from the `spark.couchbase.implicitBucket`) is as follows:

```scala
val sourceDf = spark
  .readStream
  .format("couchbase.kv")
  .load
```

What to do with the created `DataFrame` is up to the application, but for demo purposes the following snippet will print the results to the console:

```scala
val query = sourceDf.writeStream
  .format("console")
  .trigger(Trigger.Once())
  .queryName("kv2console")
  .start

query.awaitTermination()
```

This will display something similar to this in the logs:

```none
+--------------+--------------------+--------+-------------------+--------+----------+
|            id|             content|deletion|                cas|   scope|collection|
+--------------+--------------------+--------+-------------------+--------+----------+
|  airport_7176|[7B 22 69 64 22 3...|   false|1640018764144705536|_default|  _default|
|  airport_9187|[7B 22 69 64 22 3...|   false|1640018764147261440|_default|  _default|
|   hotel_30258|[7B 22 74 69 74 6...|   false|1640018764151128064|_default|  _default|
|   route_63891|[7B 22 69 64 22 3...|   false|1640018764190580736|_default|  _default|
|   route_28969|[7B 22 69 64 22 3...|   false|1640018764195561472|_default|  _default|
|    route_1704|[7B 22 69 64 22 3...|   false|1640018764197265408|_default|  _default|
|   route_58807|[7B 22 69 64 22 3...|   false|1640018764202967040|_default|  _default|
|   route_30636|[7B 22 69 64 22 3...|   false|1640018764203491328|_default|  _default|
|    route_4785|[7B 22 69 64 22 3...|   false|1640018764203687936|_default|  _default|
|    route_7003|[7B 22 69 64 22 3...|   false|1640018764206374912|_default|  _default|
|    hotel_8340|[7B 22 74 69 74 6...|   false|1640018764211027968|_default|  _default|
|    route_5593|[7B 22 69 64 22 3...|   false|1640018764224397312|_default|  _default|
|    route_6215|[7B 22 69 64 22 3...|   false|1640018764228853760|_default|  _default|
|   route_47249|[7B 22 69 64 22 3...|   false|1640018764229509120|_default|  _default|
|landmark_40166|[7B 22 74 69 74 6...|   false|1640018764239798272|_default|  _default|
|  airport_8201|[7B 22 69 64 22 3...|   false|1640018764239994880|_default|  _default|
|   route_28945|[7B 22 69 64 22 3...|   false|1640018764241436672|_default|  _default|
|   route_40774|[7B 22 69 64 22 3...|   false|1640018764241829888|_default|  _default|
|landmark_25820|[7B 22 74 69 74 6...|   false|1640018764243402752|_default|  _default|
|landmark_10847|[7B 22 74 69 74 6...|   false|1640018764246745088|_default|  _default|
+--------------+--------------------+--------+-------------------+--------+----------+
only showing top 20 rows
```

## [](#source-schema)Source Schema

The schema returned by the `DataFrame` is fixed and by default contains the following columns:

__Table 1\. Default Schema Columns__
| Name       | Data Type   | Description                                      |
| ---------- | ----------- | ------------------------------------------------ |
| id         | StringType  | The document ID.                                 |
| content    | BinaryType  | The content of the document (if not a deletion). |
| deletion   | BooleanType | If the document got deleted.                     |
| cas        | LongType    | The CAS value of the document.                   |
| scope      | StringType  | The scope the document is stored in.             |
| collection | StringType  | The collection the document is stored in.        |

It is possible to modify the output schema through the `KeyValueOptions.StreamMetaData` option property: `.option(KeyValueOptions.StreamMetaData, KeyValueOptions.StreamMetaDataBasic)`.

The following options are available:

* `KeyValueOptions.StreamMetaDataNone`: if set, will only return `id`, `content` and `deletion`.
* `KeyValueOptions.StreamMetaDataBasic`: the default, returns the columns mentioned above.
* `KeyValueOptions.StreamMetaDataFull` Returns all columns from `StreamMetaDataBasic`, but also:

__Table 2\. Additional Full Schema Columns__
| Name      | Data Type                       | Description                                    |
| --------- | ------------------------------- | ---------------------------------------------- |
| timestamp | TimestampType                   | The modification timestamp of the document.    |
| vbucket   | IntegerType                     | The partition ID of the document.              |
| xattrs    | MapType(StringType, StringType) | Extended attributes stored aside the document. |

In addition, if you are only interested in the document IDs instead of their actual content, you can set the `KeyValueOptions.StreamContent` option to `false`, which will configure the underlying stream accordingly and not return the `content` column.

## [](#trigger-modes)Trigger Modes

At the moment, spark supports different trigger modes which will cause different behavior inside the connector.

* `Trigger.Once()`: gets the current state of the bucket and streams up to this point, then ends.
* `Trigger.ProcessingTime(…​)`: starts streaming to the current state, then waits until the processing time elapses, updates the new end state, and streams to that state (and again…​).
* `Trigger.Continuous(…​)`: does not stream micro-batches, but just keeps streaming as new mutations are performed in the bucket.

All three modes use the DCP protocol of the data service, but they slightly differ in how it is utilized. In both `Once` and `ProcessingTime`, spark will actively drive the "from state → to state" when streaming each batch where with `Continuous` it will just keep running until terminated as quickly as it can.

|  | please keep in mind that Continuous has different delivery guarantees inside spark streaming than MicroBatch. While MicroBatch can guarantee exactly-once semantics, the Continuous mode is only able to provide at-least-once semantics. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | for performance reasons it is recommended to use Continuous if small intervals are chosen (i.e. around a couple seconds and less) since it allows the client to reuse the underlying DCP client and TCP sockets. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#starting-offset)Starting Offset

When a stream is started for the first time, a fundamental choice needs to be made based on the use case:

* If all current data in the bucket/collection should be streamed as well, `KeyValueOptions.StreamFromBeginning` needs to be used.
* If the stream should be started at the current point in time and only subsequent changes should be processed, `KeyValueOptions.StreamFromNow` needs to be used.

The connector looks for a saved initial offset which is stored inside the `checkpointLocation`. If not provided explicitly be user, spark will create a temporary directory automatically.

|  | If it’s required to delete a current checkpoint location, please set spark.sql.streaming.forceDeleteTempCheckpointLocation to true. According to spark docs, deleting the temp checkpoint folder is best effort. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#persistence-polling-interval)Persistence Polling Interval

When a Couchbase Server node fails over, documents on the failing node that haven’t been fully replicated may be "rolled back" to a previous state. To ensure consistency between Couchbase and the Spark Stream, the connector can defer publishing a document to Spark until it has been saved to disk on all replicas.

To enable this feature, specify a non-zero persistence polling interval (it is enabled by default). The interval is how frequently the connector asks each Couchbase node which changes have been fully replicated and persisted. This ensures consistency between Couchbase and Spark, at the cost of additional latency and bandwidth usage.

To disable this feature, specify a zero duration (0). In this mode the connector publishes changes to Spark immediately, without waiting for replication. This is fast and uses less network bandwidth, but can result in publishing "phantom changes" that don’t reflect the actual state of a document in Couchbase after a failover.

The property to modify the default (`100ms`) is `KeyValueOptions.StreamPersistencePollingInterval`.

|  | Documents written to Couchbase with enhanced durability are never published to Spark until the durability requirements are met, regardless of whether persistence polling is enabled. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | When connecting to an ephemeral bucket, always disable persistence polling by setting this config option to 0, otherwise the connector will never publish any changes. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#configuration-options)Configuration Options

By default, the stream will be performed at the bucket level. It is possible to customize the bucket, as well as streaming a specific scope or individual collections.

__Table 3\. Coordinate Configuration Properties__
| Name                        | Value Type             | Description                                                    |
| --------------------------- | ---------------------- | -------------------------------------------------------------- |
| KeyValueOptions.Bucket      | String                 | The name of the bucket (overrides the implicit).               |
| KeyValueOptions.Scope       | String                 | The name of the scope (overrides the implicit).                |
| KeyValueOptions.Collection  | String                 | The names of an individual collection that should be streamed. |
| KeyValueOptions.Collections | Comma-Separated String | The names of the collections that should be streamed.          |

Other options are available to further tweak the behavior:

__Table 4\. Behavior Configuration Properties__
| Name                                             | Value Type | Description                                                                                                                                                                         |
| ------------------------------------------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KeyValueOptions.StreamFrom                       | String     | Defines from which logical point the stream should be started/restarted (KeyValueOptions.StreamFromBeginning, KeyValueOptions.StreamFromNow).                                       |
| KeyValueOptions.StreamMetaData                   | String     | Modifies the amount of columns that are present in the output schema (KeyValueOptions.StreamMetaDataNone, KeyValueOptions.StreamMetaDataBasic, KeyValueOptions.StreamMetaDataFull). |
| KeyValueOptions.StreamContent                    | Boolean    | If the document content should be streamed as well.                                                                                                                                 |
| KeyValueOptions.StreamFlowControlBufferSize      | Integer    | The flow control buffer size for acknowledgement, in bytes.                                                                                                                         |
| KeyValueOptions.StreamPersistencePollingInterval | String     | The connector defers publishing until a mutation has been persisted to replicas. Needs to be a parsable scala Duration value (like 100ms).                                          |

## [](#input-partition-mappings)Input Partition Mappings

While this is technically an implementation detail, it can be helpful to understand how the mechanics work under the hood.

Spark tries to split up the work into `InputPartitions` which are then distributed across all the executors. The number of `InputPartitions` defaults to the value of `SparkSession.active.sparkContext.defaultParallelism`.

Since Couchbase Server is a distributed system it splits up its documents into partitions as well (called `vbuckets`). On Linux and Windows there are 1024 vBuckets, on OSX there are 64.

In order to provide the best performance possible, the connector evenly distributes the vBuckets to stream across the number of configured `InputPartitions`. This means that if more than one executor is present, each one gets to stream a (roughly equal) subset.

As an example, if there are 12 `InputPartitions` and 1024 vBuckets, each `InputPartitions` will be responsible for roughly 85 vBuckets. If there are three executors in the spark cluster, each one will be responsible for 4 `InputPartitions`, so every executor will be responsible for streaming around 340 vBuckets.

Since the number of vBuckets is fixed and the number of executors is usually chosen independent of one specific workload, the only variable that can be influenced is the number of partitions (overridable through `KeyValueOptions.NumPartitions`).