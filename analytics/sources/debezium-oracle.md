---
title: Stream CDC Data from Oracle
pubDate: 2026-08-25T04:30:40.250Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/debezium-oracle.adoc
  xref: xref:analytics:sources:debezium-oracle.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/debezium-oracle.html)

# Stream CDC Data from Oracle

> To continuously load change data capture (CDC) events from an Oracle database into Capella Analytics, you configure the Debezium Oracle connector to publish changes to a Kafka topic, then create a Kafka link and collection in Capella Analytics. 

The Debezium Oracle connector captures row-level changes in Oracle tables and publishes them as JSON events to a Kafka topic. Capella Analytics reads from that topic using a [Kafka link](remote-kafka.md).

## [](#prereqs)Prerequisites

* A running Kafka cluster with a Debezium connector configured for your Oracle database, producing messages in JSON, Avro, or Protobuf format.
* If using JSON format, schema embedding must be disabled for both key and value converters in your Debezium configuration:  
key.converter.schemas.enable=false  
value.converter.schemas.enable=false
* A Kafka link in Capella Analytics. See [Create a Kafka Pipeline Link](remote-kafka.md).

## [](#create-collection)Create a Capella Analytics Collection

The Kafka topic for an Oracle table follows the naming convention `<topic.prefix>.<schema>.<table>`. For example, if `topic.prefix` is `oracle`, the schema is `ADMIN`, and the table is `ORDERS`, the topic name is `oracle.ADMIN.ORDERS`.

The following example creates a collection on a Kafka link to ingest Debezium Oracle CDC records:

```sqlpp
CREATE COLLECTION `Default`.`Default`.oracleOrders
    PRIMARY KEY (ID: bigint)
    ON `oracle.ADMIN.ORDERS` AT kafkaLink
    WITH {
        "storage-format": {"format": "column"},
        "kafka-sink": "true",
        "keySerializationType": "JSON",
        "valueSerializationType": "JSON",
        "cdcEnabled": "true",
        "cdcDetails": {
            "cdcSource": "ORACLE",
            "cdcSourceConnector": "DEBEZIUM"
        }
    };
```

| Parameter          | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| PRIMARY KEY        | The primary key field and its data type. Must match a column in the Oracle table. |
| ON                 | The Kafka topic name. Must match the topic the Debezium connector publishes to.   |
| AT                 | The name of the Kafka link that connects to your Kafka cluster.                   |
| cdcEnabled         | Set to "true" to enable CDC processing for this collection.                       |
| cdcSource          | Set to "ORACLE" to indicate the upstream CDC source is Oracle.                    |
| cdcSourceConnector | Set to "DEBEZIUM" to indicate the Debezium connector is in use.                   |

To start ingesting data, connect the Kafka link:

```sqlpp
CONNECT LINK kafkaLink;
```

See [Connect or Disconnect a Remote Link](connect-link.md).

## [](#data-types)Data Type Handling and Limitations

During ingestion, Debezium may convert Oracle types in ways that differ from the native Oracle representation. Ingestion is performed based on the contents of the `after` field in each event. No schema metadata is used.

The following table shows how Oracle types map to Capella Analytics types with the default Debezium configuration.

| Oracle Type                                                                  | Capella Analytics Type |
| ---------------------------------------------------------------------------- | ---------------------- |
| CHAR\[(M)\], NCHAR\[(M)\], NVARCHAR2\[(M)\], VARCHAR\[(M)\], VARCHAR2\[(M)\] | STRING                 |
| BLOB, CLOB, NCLOB                                                            | STRING                 |
| BINARY\_FLOAT, BINARY\_DOUBLE                                                | DOUBLE                 |
| DECIMAL\[(P, S)\]                                                            | STRING or BIGINT       |
| DOUBLE PRECISION, FLOAT\[(P)\], NUMBER\[(P\[, \*\])\], REAL                  | OBJECT                 |
| INTEGER, INT                                                                 | STRING                 |
| NUMBER(P, S <= 0)                                                            | BIGINT                 |
| NUMBER(P, S > 0)                                                             | STRING                 |
| NUMERIC\[(P, S)\]                                                            | STRING or BIGINT       |
| SMALLINT                                                                     | STRING                 |
| DATE                                                                         | BIGINT                 |
| INTERVAL DAY\[(M)\] TO SECOND                                                | DOUBLE                 |
| INTERVAL YEAR\[(M)\] TO MONTH                                                | DOUBLE                 |
| TIMESTAMP(0-3), TIMESTAMP, TIMESTAMP(4-6), TIMESTAMP(7-9)                    | BIGINT                 |
| TIMESTAMP WITH TIME ZONE, TIMESTAMP WITH LOCAL TIME ZONE                     | STRING                 |

### [](#unsupported-oracle-types)Unsupported Oracle Types

The following Oracle types are not supported by Debezium:

* `BFILE` (binary file)
* `BOOLEAN`
* Direct joins in the `FROM` clause of `UPDATE` and `DELETE` statements
* Data Use Case Domains
* JavaScript-based stored procedures
* `LONG`
* `LONG RAW`
* `ROWID` (not supported on XStream)
* Table value constructors (TVCs)
* `UROWID` (Universal ROWID)
* `VECTOR`

### [](#debezium-configuration-options)Debezium Configuration Options

Debezium provides configuration options to reduce data type mismatches. For example, setting `decimal.handling.mode = double` causes Oracle decimal values to be ingested as `DOUBLE` values in Kafka. For a full list of options, see the [Debezium Oracle connector documentation](https://debezium.io/documentation/reference/stable/connectors/oracle.html).

> [!NOTE]
> Test your complete data model with all expected data types before deploying to production to verify data is ingested as expected under your chosen configuration.

## [](#see-also)See Also

* [Create a Kafka Pipeline Link](remote-kafka.md)
* [Create a Kafka Pipeline Collection](kafka-collection.md)
* [Stream CDC Data from SQL Server](debezium-sqlserver.md)
* [Connect or Disconnect a Remote Link](connect-link.md)
* [CREATE a Remote Kafka Collection](../sqlpp/5%5Fddl%5Fremote.md#createkafka)