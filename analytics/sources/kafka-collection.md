---
title: Create a Kafka Pipeline Collection
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/kafka-collection.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:sources:kafka-collection.adoc[]
---

[View original HTML](/analytics/sources/kafka-collection.html)

# Create a Kafka Pipeline Collection

> To receive a data event stream from a remote data source that uses an Apache Kafka pipeline, you create a remote collection. 

You can create collections to associate with a Kafka pipeline link when you [create the link](remote-kafka.md) or at any time afterwards.

## [](#reqs)Requirements

Primary Key

When you set up a remote collection to receive data from a Kafka pipeline, you supply the primary key and its data type in `KEY_NAME:DATA_TYPE` format. For example, `id:string`.

* To use a key name that includes a space or any character other than an underscore (\_), escape the name with backtick (``` `` ```) characters.
* For source data that uses an object id, add `.` and then ```` `` `$oid ``` ```` after the `KEY_NAME`, in the following format:  
  KEY_NAME.`$oid`:DATA_TYPE  
For example:  
   _id.`$oid`:string
* For a composite key, enter a comma-separated list of the key names and their data types.

Topic

The Kafka topic or set of topics that contains the data you want to stream into the collection. You can stream data from one or more topics to multiple collections using the same link. However, the collections that stream the same topics must have the same data serialization and change data capture settings. Otherwise, you receive an `inconsistent details config` error.

Similarly, when streaming data from multiple topics into a collection, the data serialization and change data capture settings must apply to all of the topics that you provide.

Data Serialization

The type of data serialization used for keys and values:

* [JSON](https://www.json.org/json-en.html)
* [Apache Avro](https://avro.apache.org)
* [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol%5FBuffers) (Protobuf)

Dead Letter Queue

You can have Capella Analytics report any messages it fails to load to a Kafka topic called the dead letter queue. The credentials you supply for the link to connect to Kafka must have permission to produce messages on this topic.

Change Data Capture

Whether Change Data Capture (CDC) applies, and if so, the source.

## [](#create-a-collection-for-a-kafka-data-link)Create a Collection for a Kafka Data Link

If you have just saved a new [Kafka data link](remote-kafka.md) and are ready to add one or more collections to it, begin with step 5.

To create a remote collection that is associated with a Kafka data link:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to locate the link.
4. Move your cursor over the name of the link and then choose **⋮ (More)** **Create Linked Collection**. The Create Collection dialog opens.
5. Use the lists to select the **Database** and **Scope** for the collection.
6. In the **Collection Name** field, enter a name for the collection.  
The name must start with a letter (A-Z, a-z) and contain only upper- and lowercase letters, numbers (0-9), and underscore (\_) or dash (-) characters.
7. In the **Primary Key** field, enter the name of the primary key and its data type in the format `KEY_NAME:DATA_TYPE`. See the [requirements](#reqs) for examples.
8. Supply one or more **Kafka Topics** in a comma-separated list. If you supply multiple topics, the choices you make in the remaining fields must apply to all of them. Also enter the name of the [dead letter queue](#deadletter) topic (if any).
9. Select the data serialization type used for keys and values.
10. Select Change Data Capture (CDC) if applicable. Capella Analytics currently supports CDC via the Debezium and MOLO17 connectors for real-time database integrations.
11. Specify the CDC Source: MONGODB, MYSQLDB, POSTGRESQL, or DynamoDB.
12. Choose **Create Collection**. Your collection appears under the specified database and scope in the explorer.  
If the link is [connected](connect-link.md), the data stream from the specified topic or topics into this Capella Analytics collection begins immediately. If the link is not connected, see [Connect or Disconnect a Remote Link](connect-link.md).

You can also use an SQL++ statement to create a remote Kafka collection, see [CREATE a Remote Kafka Collection](../sqlpp/5%5Fddl%5Fremote.md#createkafka).

## [](#see-also)See Also

* [Connect or Disconnect a Remote Link](connect-link.md)
* [Delete a Collection or Link](delete-entity.md)
* [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md#createkafka)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)