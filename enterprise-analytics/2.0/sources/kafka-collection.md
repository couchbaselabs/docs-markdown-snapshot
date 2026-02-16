[View original HTML](/enterprise-analytics/2.0/sources/kafka-collection.html)

> To receive a data event stream from a remote data source that uses a Confluent Kafka pipeline, you create a remote collection. 

You can create collections to associate with a Kafka pipeline link. See [create the link](remote-kafka.md). You can also use a SQL++ statement to create a remote Kafka collection. See [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md#createkafka).

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

The Kafka topic or set of topics that contains the data you want to stream into the collection. You can stream data from 1 or more topics to multiple collections using the same link. However, the collections that stream the same topics must have the same data serialization and change data capture settings. Otherwise, you receive an `inconsistent details config` error.

Similarly, when streaming data from multiple topics into a collection, the data serialization and change data capture settings must apply to all of the topics that you provide.

Data Serialization

The type of data serialization used for keys and values:

* [JSON](https://www.json.org/json-en.html)
* [Apache Avro](https://avro.apache.org)
* [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol%5FBuffers) (Protobuf)

Dead Letter Queue

You can have Enterprise Analytics report any messages it fails to load to a Kafka topic called the dead letter queue. The credentials you supply for the link to connect to Kafka must have permission to produce messages on this topic.

Change Data Capture

Whether Change Data Capture (CDC) applies, and if so, the source.

## [](#create-a-collection-for-a-kafka-data-link)Create a Collection for a Kafka Data Link

1. In the UI, select the **Workbench** tab and locate the Kafka link for which you want to add a collection.
2. Select **\+ collection**.
3. In the **Collection Name** field, enter a name for the collection.
4. In the **Database** list, select the required database and in the **Scope** list, select the required scope or verify the supplied database and scope if you’re adding it to a specific scope.
5. In the **Topic** field, enter a name for the Kafka topic.
6. In the **Primary Key** field, enter the name of the primary key and its data type in the format `KEY_NAME:DATA_TYPE`. See the [requirements](#reqs) for examples.
7. In the **Key Serialization Type** field, select the data serialization type used for keys. See the [requirements](#reqs) for examples.
8. In the **Value Serialization Type** field, select the data serialization type used for keys. See the [requirements](#reqs) for examples.
9. Click **CDC Enabled** if the topics use Change Data Capture (CDC).
10. In the **Dead Letter Queue Topic** field, enter the dead letter topic. See the [requirements](#reqs) for more information.
11. In the **Source bucket.scope.collection** field, select the source bucket, scope and collection.
12. In the **Where (optional)** field, you can add an optional WHERE clause to filter documents in the dataset. Make sure you do not include the WHERE keyword.
13. Click **Save** to create the collection.  
If the link is [connected](connect-link.md), the data stream from the specified topic or topics into this Remote Kafka collection begins. If the link is not connected, see [Connect or Disconnect a Remote Link](connect-link.md).

## [](#see-also)See Also

* [Connect or Disconnect a Remote Link](connect-link.md)
* [Delete a Collection or Link](delete-entity.md)
* [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md#createkafka)
* [Access and Organize Data in Enterprise Analytics](database-objects.md)