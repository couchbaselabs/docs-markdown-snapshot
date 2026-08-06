---
title: CREATE a Remote Collection
description: This topic describes how you use the `CREATE` statement to create a
  collection that shadows OLTP data from a remote data source.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_remote.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:sqlpp:5_ddl_remote.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/5_ddl_remote.html)

# CREATE a Remote Collection

> This topic describes how you use the \`CREATE\` statement to create a collection that shadows OLTP data from a remote data source. 

![ CreateRemoteCollection | CreateExternalCollection | CreateStandaloneCollection ](_images/CreateCollection.png) 

You use different statement syntax to create collections that shadow data located on a [Couchbase data service](#createcb) than you do for collections that shadow data from a [Kafka pipeline](#createkafka).

## [](#createcb)Create a Remote Couchbase Collection

> [!TIP]
> To create a link to a remote data source, you use the Enterprise Analytics UI. See [Stream Data from Remote Sources](../sources/manage-remote.md).

### [](#syntax)Syntax

**CreateRemoteCouchbaseCollection EBNF** 

```EBNF
CreateRemoteCouchbaseCollection ::= "CREATE" "ANALYTICS"? "COLLECTION" ("IF" "NOT" "EXISTS")?
                                 QualifiedName
                                 ( "WITH" ObjectConstructor )?
                                 "ON" KeyspaceName
                                 "AT" LinkName
                                 ( "WHERE" Expr | "APPLY" "FUNCTION" QualifiedName)?
```

**CreateRemoteCouchbaseCollection Diagram** 

!["CREATE" "COLLECTION" ("IF" "NOT" "EXISTS")? QualifiedName ( "WITH" ObjectConstructor )? "ON" KeyspaceName "AT" LinkName ( "WHERE" Expr )?](_images/CreateRemoteCollection.png) 

For all collections, the `QualifiedName` is the fully qualified name of the collection to create.

**Show QualifiedName Diagram** 

![(DatabaseAndScopeName ".")? Identifier](_images/QualifiedName.png) 

QualifiedName

**Show ObjectConstructor Diagram** 

!["{" ( Expr ( ":" Expr )? ( "," Expr ( ":" Expr )? )* )? "}"](_images/ObjectConstructor.png) 

ObjectConstructor

**Show KeyspaceName Diagram** 

![Identifier ( "." Identifier "." Identifier )?](_images/KeyspaceName.png) 

KeyspaceName

### [](#example)Example

This example adds a collection for French breweries and associates it with the remote link to Capella. As a prerequisite for running this example yourself, follow the [intro:connecting-to-data-sources.adoc#create-remote-collections-for-beer-sample](../intro/connecting-to-data-sources.md#create-remote-collections-for-beer-sample) procedures to add a remote link and collections to Enterprise Analytics.

```SQL++
  CREATE COLLECTION remoteCapella.remoteBeer.beerFrance
    ON `beer-sample`._default._default
    AT capellaLink
    WHERE country = "France";
```

This following example creates a new collection named `analytics.Commerce.customers` that shadows data from a remote source using the `capellaLink`. The `CustomerTransform` function must be created with a `CREATE TRANSFORM FUNCTION` statement before it can be used here. It then applies the `CustomerTransform` function to automatically transform incoming data before storing it in the collection.

Example

```SQL++
CREATE TRANSFORM FUNCTION analytics.Commerce.CustomerTransform (cust) {
    SELECT
        c.*,
        (c.address.street || ', ' || c.address.city || ', ' || c.address.zipcode) AS location
    FROM [cust] AS c
};
CREATE COLLECTION analytics.Commerce.customers
    ON `donc-book-sample`.Commerce.customers AT capellaLink
    APPLY FUNCTION analytics.Commerce.CustomerTransform;
```

### [](#arguments)Arguments

WITH

The optional **`WITH`** clause enables you to specify parameters for the remote Couchbase collection. Its `ObjectConstructor` represents a JSON object containing key-value pairs.

The optional `storage-format` parameter determines the storage format used for this collection. This parameter takes a nested object value, `format`. Possible values for `format` are `column` or `row`. The default is `column`.

For example:

 WITH {
 "storage-format": {"format" : "column"}
};

ON

The **`ON`** clause specifies the data source for the collection. The \`Identifier\`s in this clause represent a database name, followed by an optional scope name and collection name, on the remote Couchbase Server or Capella cluster.

AT

The **`AT`** clause specifies the name of the link that contains credentials for the database. The specified link must have a type of Couchbase.

WHERE

The optional **`WHERE`** clause provides the option to filter the documents in the collection. The `Expr` in this clause must be deterministic, and it cannot contain a user-defined function. For example, you could filter content by specifying a predicate on the values for one or more of the fields in the objects.

> [!NOTE]
> The `WHERE` clause and the `APPLY FUNCTION` clause are mutually exclusive; you can use one or the other, but not both when creating a remote collection.

APPLY FUNCTION

The **`APPLY FUNCTION`** clause allows you to attach a `TRANSFORM FUNCTION` to a remote collection. When you use the `APPLY FUNCTION` keyword in the `CREATE COLLECTION` statement, Capella Analytics applies your specified SQL++ user-defined function (UDF) to each incoming document before storing it in the remote collection. This enables you to filter, modify, or reshape data automatically as it arrives from the remote source.

For more information about how to create a `TRANSFORM FUNCTION`, see [Create Transform Function](9%5Fudf.md#create-transform-function).

The following example uses the `APPLY FUNCTION` clause to apply a `TRANSFORM FUNCTION` when creating a remote collection:

Example

```sqlpp
CREATE COLLECTION analytics.Commerce.customers
    ON `donc-book-sample`.Commerce.customers
    AT capellaLink
    APPLY FUNCTION analytics.Commerce.CustomerTransform;
```

The `CustomerTransform` `TRANSFORM FUNCTION` processes each record before storing it in the `analytics.Commerce.customers` collection.

To create a link to a remote data source, you use the Enterprise Analytics UI. See [Stream Data from Couchbase Capella](../sources/remote-cb-capella.md).

## [](#createkafka)Create a Remote Kafka Collection

> [!TIP]
> To create a link to a remote data source, you use the Enterprise Analytics UI. See [Stream Data from Remote Sources](../sources/manage-remote.md).

### [](#syntax-2)Syntax

**CreateRemoteKafkaCollection EBNF** 

```EBNF
CreateRemoteKafkaCollection ::= "CREATE" "ANALYTICS"? "COLLECTION"
                                ("IF" "NOT" "EXISTS")?
                                 QualifiedName
                                 "PRIMARY" "KEY" "(" FieldList ")"
                                 "ON" TopicName ("," TopicName)*
                                 "AT" LinkName
                                 "WITH" KafkaObjectConstructor
                                 ("WHERE" Expr | "APPLY" "FUNCTION" QualifiedName)?
```

**CreateRemoteKafkaCollection Diagram** 

!["CREATE" "COLLECTION" ("IF" "NOT" "EXISTS")? QualifiedName "PRIMARY" "KEY" "(" FieldList ")" "ON" TopicName(,TopicName)* "AT" LinkName ( "WITH" KafkaObjectConstructor )? ( "WHERE" Expr )?](_images/CreateRemoteKafkaCollection.png) 

For all collections, the `QualifiedName` is the fully qualified name of the collection to create.

**Show QualifiedName Diagram** 

![(DatabaseAndScopeName ".")? Identifier](_images/QualifiedName.png) 

QualifiedName

**Show FieldList Diagram** 

![FieldDef ("," FieldDef)* ](_images/FieldList.png) 

FieldList

**Show FieldDef Diagram** 

![FieldName ":" FieldType](_images/FieldDef.png) 

FieldDef

**Show FieldName Diagram** 

![Identifier ("." Identifier)*](_images/FieldName.png) 

FieldName

**Show FieldType Diagram** 

![Identifier](_images/FieldType.png) 

FieldType

### [](#examples)Examples

This statement uses the JSON Commerce customers dataset as an example. It assumes that this data is in a Kafka topic named `remote-topic-1` for a MongoDB dataset that uses CDC. The primary key for the MongoDB dataset is `_id`, with string values. In addition, this example assumes that a link named `confluentLink` has the credentials for accessing the MongoDB dataset.

```SQL++
  CREATE COLLECTION sampleAnalytics.Commerce.customers
  PRIMARY KEY (_id:string)
  ON `remote-topic-1`
  AT confluentLink
  WITH {
      "keySerializationType":"JSON",
      "valueSerializationType":"JSON",
      "cdcEnabled": "true"
      "cdcDetails": {
        "cdcSource": "MONGODB"
        "cdcSourceConnector":"DEBEZIUM"
        },
      "deadLetterQueue":"dlq_topic-1"
  };
```

**Show additional example** 

This statement uses the JSON Commerce orders dataset as an example. It assumes that the data is in a Kafka topic named `non_cdc_5m_json.mongo_database.mongo_collection` for a MongoDB dataset that does not use CDC. In addition, you have a link set up named `mskLink` with the credentials for accessing the dataset.

```SQL++
  CREATE COLLECTION sampleAnalytics.Commerce.orders
  PRIMARY KEY (orderno:int)
  ON `non_cdc_5m_json.mongo_database.mongo_collection`
  AT mskLink
  WITH {
      "keySerializationType":"JSON",
      "valueSerializationType":"JSON"
  };
```

The following example creates a new collection named `analytics.Commerce.orders` that uses `orderno` as the primary key and ingests data from a remote MongoDB source via the `mskLink`. The `WHERE` clause filters the documents in the collection to include only those where the `category` field has the value `Apparel`.

Example

```SQL++
CREATE TRANSFORM FUNCTION OrderTransform (ord)
{ SELECT orderno, custid, order_date, ship_date
  FROM [ord] AS o };
CREATE COLLECTION analytics.Commerce.orders
  PRIMARY KEY (orderno:int)
  ON `non_cdc_5m_json.mongo_database.mongo_collection` AT mskLink
  WITH {
      "keySerializationType":"JSON",
      "valueSerializationType":"JSON"
   }
   WHERE category = "Apparel";
```

**Show additional example** 

The following example creates a new collection named `analytics.Commerce.lineitems` with a composite primary key of `orderno` and `itemno`, ingesting data from a remote MongoDB source via the `mskLink`. It applies the `OrderTransform` function to automatically transform incoming data before storing it in the collection, using JSON serialization for both keys and values.

```SQL++
CREATE COLLECTION analytics.Commerce.lineitems
  PRIMARY KEY (orderno:int, itemno:int)
  ON `non_cdc_5m_json.mongo_database.mongo_collection` AT mskLink
  WITH {
      "keySerializationType":"JSON",
      "valueSerializationType":"JSON"
   }
   APPLY FUNCTION analytics.Commerce.OrderTransform;
```

### [](#arguments-2)Arguments

PRIMARY KEY

The **`PRIMARY KEY`** clause indicates the field or fields to use as the primary key for the collection. The **`FieldType`** can be any of the [primitive data types](10%5Fdata%5Ftype.md#PrimitiveTypes), where `INT` is an alias for `BIGINT`.

A common datatype for the MongoDB `_id` primary key is objectId. To specify a primary key with this datatype, you use the following syntax:

  PRIMARY KEY (`_id`.`$oid`:String)

If CDC is enabled for the collection, you should specify the primary key of the source collection as the primary key for your Enterprise Analytics collection.

ON

You specify one or more topics from the Kafka cluster in a comma-separated list.

WITH

The **`WITH`** clause enables you to specify parameters for the collection. Its `ObjectConstructor` represents an object containing key-value pairs, one for each parameter. The configuration that you supply applies to all of the topics listed by the ON clause. You can define the following parameters.

| Name                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        | Schema                             |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **keySerializationType** Required   | Specifies the format of the keys in the remote data. Accepts one of the following string values: JSON — [JSON](https://www.json.org/json-en.html) PROTOBUF — [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol%5FBuffers) AVRO — [Apache Avro](https://avro.apache.org) For information about the mapping that Enterprise Analytics performs for Avro data types, see [Data Type Mapping: Parquet and Avro](5%5Fddl%5Fexternal.md#avro).   | enum: json, protobuf, avro         |
| **valueSerializationType** Required | Specifies the format of the values in the remote data. Accepts one of the following string values: JSON — [JSON](https://www.json.org/json-en.html) PROTOBUF — [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol%5FBuffers) AVRO — [Apache Avro](https://avro.apache.org) For information about the mapping that Enterprise Analytics performs for Avro data types, see [Data Type Mapping: Parquet and Avro](5%5Fddl%5Fexternal.md#avro). | enum: json, protobuf, avro         |
| **cdcEnabled** Required             | Identifies whether the Kafka pipeline uses Change Data Capture (CDC) processing. When true, you also specify a cdcDetails object with the cdcSource and cdcSourceConnector parameters. When true, you should specify the primary key of the source collection as the primary key for your Enterprise Analytics collection. The Debezium source connector sends the primary key of the source collection as the key for records in the Kafka topic. | Boolean                            |
| **cdcSource** Optional              | Only used if **cdcEnabled** is true. Identifies the data source that uses CDC in the Kafka pipeline.                                                                                                                                                                                                                                                                                                                                               | enum: MONGODB, MYSQLDB, POSTGRESQL |
| **cdcSourceConnector** Optional     | Only used if **cdcEnabled** is true. Identifies the type of source data connector used in the pipeline.                                                                                                                                                                                                                                                                                                                                            | enum: DEBEZIUM                     |
| **deadLetterQueue** Optional        | Specifies a remote Kafka topic as the destination for failed messages. If you do not define a topic, failed messages are dropped.                                                                                                                                                                                                                                                                                                                  | string                             |

WHERE

The optional `WHERE` clause provides the option to filter the documents in the collection. The `Expr` in this clause must be deterministic, and it cannot contain a user-defined function. For example, you could filter content by specifying a predicate on the values for one or more of the fields in the objects.

> [!NOTE]
> The `WHERE` clause and the `APPLY FUNCTION` clause are mutually exclusive; you can use one or the other, but not both when creating a remote collection.

APPLY FUNCTION

The `APPLY FUNCTION` clause allows you to attach a `TRANSFORM FUNCTION` to incoming data during collection creation. When you use the `APPLY FUNCTION` keyword in the `CREATE COLLECTION` statement, Capella Analytics automatically processes each incoming record with your specified SQL++ user-defined function (UDF) before storing it in the collection. This enables you to filter, modify, or reshape data as it arrives from Kafka.

For more information about how to create a `TRANSFORM FUNCTION`, see [Create Transform Function](9%5Fudf.md#create-transform-function).

See the following example:

Example

```sqlpp
CREATE COLLECTION analytics.Commerce.orders
  PRIMARY KEY (orderno:int)
  ON `non_cdc_5m_json.mongo_database.mongo_collection` AT mskLink
  WITH {
      "keySerializationType":"JSON",
      "valueSerializationType":"JSON"
   }
   APPLY FUNCTION analytics.Commerce.OrderTransform;
```

The `OrderTransform` `TRANSFORM FUNCTION` processes each record before storing it in the `analytics.Commerce.orders` collection.

To create a link to a remote data source, you use the Enterprise Analytics UI. See [Create a Kafka Pipeline Link](../sources/remote-kafka.md).

## [](#see-also)See Also

* [Stream Data from Remote Sources](../sources/manage-remote.md)
* [Stream Data from Couchbase Capella](../sources/remote-cb-capella.md)
* [Create a Kafka Pipeline Link](../sources/remote-kafka.md)