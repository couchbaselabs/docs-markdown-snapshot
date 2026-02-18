---
title: Migrating from Version 3.x
editUrl: https://github.com/couchbase/docs-kafka/edit/release/4.3/modules/ROOT/pages/migration.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/kafka-connector/current/migration.html)

# Migrating from Version 3.x

> Tools and information for upgrading your connector configuration. 

In version 4.x the names of the config properties have changed to follow a consistent naming convention. Some default values have changed to provide a better out-of-box experience for new users.

The Java API for customizing the connector’s behavior has also changed in a way that is not backwards compatible. If you have written a custom `SourceHandler` or `Filter` component, some minor changes are required for it to work with the new version of the connector.

## [](#configuration-properties)Configuration Properties

A shell script called `migrate-config-3-to-4.sh` is available to assist with updating a version 3.x config file. You can find this script in the `etc` directory of the connector distribution archive, or you can [download it from GitHub](https://github.com/couchbase/kafka-connect-couchbase/blob/master/config/migrate-config-3-to-4.sh).

The following tables show how the config properties changed between 3.x and 4.x.

__Table 1\. Properties used by both Source and Sink__
| Name in 3.x                      | Name in 4.x                    | Notes                                                         |
| -------------------------------- | ------------------------------ | ------------------------------------------------------------- |
| connection.cluster\_address      | couchbase.seed.nodes           |                                                               |
| couchbase.network                | couchbase.network              |                                                               |
| connection.bucket                | couchbase.bucket               |                                                               |
| connection.username              | couchbase.username             |                                                               |
| connection.password              | couchbase.password             |                                                               |
| connection.timeout.ms            | couchbase.bootstrap.timeout    | Now specified as qualified duration; 10 seconds would be: 10s |
| connection.ssl.enabled           | couchbase.enable.tls           |                                                               |
| connection.ssl.keystore.password | couchbase.trust.store.password |                                                               |
| connection.ssl.keystore.location | couchbase.trust.store.path     |                                                               |
| couchbase.log\_redaction         | couchbase.log.redaction        |                                                               |
| couchbase.forceIPv4              | (removed)                      |                                                               |

__Table 2\. Source properties__
| Name in 3.x                              | Name in 4.x                            | Notes                                                                                                                                         |
| ---------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| topic.name                               | couchbase.topic                        | Now a format string that supports placeholders "${bucket}", "${scope}", and "${collection}". Now defaults to ${bucket}.${scope}.${collection} |
| use\_snapshots                           | (removed)                              |                                                                                                                                               |
| dcp.message.converter.class              | couchbase.source.handler               | No longer has a default value.                                                                                                                |
| event.filter.class                       | couchbase.event.filter                 |                                                                                                                                               |
| batch.size.max                           | couchbase.batch.size.max               |                                                                                                                                               |
| compat.connector\_name\_in\_offsets      | couchbase.connector.name.in.offsets    | **Deprecated**. Only set this to true if you have previously deployed the connector to production with this set to true.                      |
| couchbase.stream\_from                   | couchbase.stream.from                  |                                                                                                                                               |
| couchbase.log\_redaction                 | couchbase.log.redaction                |                                                                                                                                               |
| couchbase.compression                    | couchbase.compression                  |                                                                                                                                               |
| couchbase.persistence\_polling\_interval | couchbase.persistence.polling.interval |                                                                                                                                               |
| couchbase.flow\_control\_buffer          | couchbase.flow.control.buffer          |                                                                                                                                               |

__Table 3\. Sink properties__
| Name in 3.x                            | Name in 4.x                       | Notes                                                      |
| -------------------------------------- | --------------------------------- | ---------------------------------------------------------- |
| couchbase.document.id                  | couchbase.document.id             |                                                            |
| couchbase.remove.document.id           | couchbase.remove.document.id      |                                                            |
| couchbase.durability.persist\_to       | couchbase.persist.to              |                                                            |
| couchbase.durability.replicate\_to     | couchbase.replicate.to            |                                                            |
| couchbase.subdocument.path             | couchbase.subdocument.path        |                                                            |
| couchbase.document.mode                | couchbase.document.mode           |                                                            |
| couchbase.subdocument.operation        | couchbase.subdocument.operation   |                                                            |
| couchbase.n1ql.operation               | couchbase.n1ql.operation          | UPSERT is no longer a valid value. Now defaults to UPDATE. |
| couchbase.n1ql.where\_fields           | couchbase.n1ql.where.fields       |                                                            |
| couchbase.subdocument.create\_path     | couchbase.subdocument.create.path |                                                            |
| couchbase.subdocument.create\_document | couchbase.create.document         |                                                            |
| couchbase.document.expiration          | couchbase.document.expiration     |                                                            |

## [](#java-api)Java API

> A summary of how the connector’s Java extension points have changed. 

### [](#filter)Filter

The `Filter` interface now accepts a `DocumentEvent` instead of a `ByteBuf`.

### [](#sourcehandler)SourceHandler

`SourceHandler` is now an interface instead of an abstract class.

The `handle(SourceHandlerParams)` method now returns a `SourceRecordBuilder` instead of a `CouchbaseSourceRecord`.

### [](#documentevent)DocumentEvent

The `rawDcpEvent()` method has been removed.

To determine the type of the event, call `type()`.

To get details of mutation events, call `mutationMetadata()`.

To get the document content as a byte array, call `content()`.

The `vBucket()` method is renamed `partition()`.

The `vBucketUuid()` method is renamed `partitionUuid()`.