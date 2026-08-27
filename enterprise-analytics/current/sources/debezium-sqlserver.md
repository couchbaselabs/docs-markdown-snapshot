---
title: Stream CDC Data from SQL Server
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sources/pages/debezium-sqlserver.adoc
  xref: xref:enterprise-analytics:sources:debezium-sqlserver.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sources/debezium-sqlserver.html)

# Stream CDC Data from SQL Server

> To continuously load change data capture (CDC) events from a SQL Server database into Enterprise Analytics, you configure the Debezium SQL Server connector to publish changes to a Kafka topic, then create a Kafka link and collection in Enterprise Analytics. 

The Debezium SQL Server connector reads the CDC change tables that SQL Server maintains for tracked tables and publishes row-level changes as JSON events to a Kafka topic. Enterprise Analytics reads from that topic using a [Kafka link](remote-kafka.md).

## [](#prereqs)Prerequisites

* A running Kafka cluster with a Debezium connector configured for your SQL Server database, producing messages in JSON, Avro, or Protobuf format.
* If using JSON format, schema embedding must be disabled for both key and value converters in your Debezium configuration:  
key.converter.schemas.enable=false  
value.converter.schemas.enable=false
* A Kafka link in Enterprise Analytics. See [Create a Kafka Pipeline Link](remote-kafka.md).

## [](#create-collection)Create an Enterprise Analytics Collection

The Kafka topic for a SQL Server table follows the naming convention `<topic.prefix>.<database>.<schema>.<table>`. For example, if `topic.prefix` is `sqlserver`, the database is `sales`, the schema is `dbo`, and the table is `transactions`, the topic name is `sqlserver.sales.dbo.transactions`.

The following example creates a collection on a Kafka link to ingest Debezium SQL Server CDC records:

```sqlpp
CREATE COLLECTION `Default`.`Default`.sqlserverTransactions
    PRIMARY KEY (id: bigint)
    ON `sqlserver.sales.dbo.transactions` AT kafkaLink
    WITH {
        "storage-format": {"format": "column"},
        "kafka-sink": "true",
        "keySerializationType": "JSON",
        "valueSerializationType": "JSON",
        "cdcEnabled": "true",
        "cdcDetails": {
            "cdcSource": "SQLSERVER",
            "cdcSourceConnector": "DEBEZIUM"
        }
    };
```

| Parameter          | Description                                                                           |
| ------------------ | ------------------------------------------------------------------------------------- |
| PRIMARY KEY        | The primary key field and its data type. Must match a column in the SQL Server table. |
| ON                 | The Kafka topic name. Must match the topic the Debezium connector publishes to.       |
| AT                 | The name of the Kafka link that connects to your Kafka cluster.                       |
| cdcEnabled         | Set to "true" to enable CDC processing for this collection.                           |
| cdcSource          | Set to "SQLSERVER" to indicate the upstream CDC source is SQL Server.                 |
| cdcSourceConnector | Set to "DEBEZIUM" to indicate the Debezium connector is in use.                       |

To start ingesting data, connect the Kafka link:

```sqlpp
CONNECT LINK kafkaLink;
```

See [Connect or Disconnect a Remote Link](connect-link.md).

## [](#data-types)Data Type Handling and Limitations

During ingestion, Debezium may convert SQL Server types in ways that differ from the native SQL Server representation. Ingestion is performed based on the contents of the `after` field in each event — no schema metadata is used.

The following table shows how SQL Server types map to Enterprise Analytics types with the default Debezium configuration.

| SQL Server Type                                                         | Enterprise Analytics Type |
| ----------------------------------------------------------------------- | ------------------------- |
| BIT                                                                     | BOOLEAN                   |
| TINYINT, SMALLINT, INT                                                  | BIGINT                    |
| BIGINT                                                                  | BIGINT                    |
| REAL                                                                    | DOUBLE                    |
| FLOAT\[(N)\]                                                            | DOUBLE                    |
| CHAR\[(N)\], VARCHAR\[(N)\], TEXT, NCHAR\[(N)\], NVARCHAR\[(N)\], NTEXT | STRING                    |
| XML                                                                     | STRING                    |
| DATETIMEOFFSET\[(P)\]                                                   | STRING                    |
| DATE                                                                    | BIGINT                    |
| TIME(0), TIME(1), TIME(2), TIME(3)                                      | BIGINT                    |
| TIME(4), TIME(5), TIME(6)                                               | BIGINT                    |
| TIME(7)                                                                 | BIGINT                    |
| DATETIME                                                                | BIGINT                    |
| SMALLDATETIME                                                           | BIGINT                    |
| DATETIME2(0), DATETIME2(1), DATETIME2(2), DATETIME2(3)                  | BIGINT                    |
| DATETIME2(4), DATETIME2(5), DATETIME2(6)                                | BIGINT                    |
| DATETIME2(7)                                                            | BIGINT                    |
| NUMERIC\[(P\[,S\])\], DECIMAL\[(P\[,S\])\]                              | STRING                    |
| SMALLMONEY, MONEY                                                       | STRING                    |

### [](#debezium-configuration-options)Debezium Configuration Options

Debezium provides configuration options to reduce data type mismatches. For example, setting `decimal.handling.mode = double` causes SQL Server decimal values to be ingested as `DOUBLE` values in Kafka. For a full list of options, see the [Debezium SQL Server connector documentation](https://debezium.io/documentation/reference/stable/connectors/sqlserver.html).

> [!NOTE]
> Test your complete data model with all expected data types before deploying to production to verify data is ingested as expected under your chosen configuration.

## [](#see-also)See Also

* [Create a Kafka Pipeline Link](remote-kafka.md)
* [Create a Kafka Pipeline Collection](kafka-collection.md)
* [Stream CDC Data from Oracle](debezium-oracle.md)
* [Connect or Disconnect a Remote Link](connect-link.md)
* [CREATE a Remote Kafka Collection](../sqlpp/5%5Fddl%5Fremote.md#createkafka)