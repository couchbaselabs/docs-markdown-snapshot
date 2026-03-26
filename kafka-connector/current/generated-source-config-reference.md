---
editUrl: https://github.com/couchbase/docs-kafka/edit/release/4.3/modules/ROOT/pages/generated-source-config-reference.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:kafka-connector::generated-source-config-reference.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kafka-connector/current/generated-source-config-reference.html)

# undefined

## [](#connection)Connection

### [](#couchbase.seed.nodes)`couchbase.seed.nodes`

Addresses of Couchbase Server nodes, delimited by commas.

If a custom port is specified, it must be the KV port (which is normally 11210 for insecure connections, or 11207 for secure connections).

* Type: list
* Importance: high

### [](#couchbase.username)`couchbase.username`

Name of the Couchbase user to authenticate as.

* Type: string
* Importance: high

### [](#couchbase.password)`couchbase.password`

Password of the Couchbase user.

May be overridden with the KAFKA\_COUCHBASE\_PASSWORD environment variable.

* Type: password
* Importance: high

### [](#couchbase.bucket)`couchbase.bucket`

Name of the Couchbase bucket to use.

This property is required unless using the experimental AnalyticsSinkHandler.

* Type: string
* Default: `""`
* Importance: high

### [](#couchbase.network)`couchbase.network`

The network selection strategy for connecting to a Couchbase Server cluster that advertises alternate addresses.

A Couchbase node running inside a container environment (like Docker or Kubernetes) might be configured to advertise both its address within the container environment (known as its "default" address) as well as an "external" address for use by clients connecting from outside the environment.

Setting the 'couchbase.network' config property to 'default' or 'external' forces the selection of the respective addresses. Setting the value to 'auto' tells the connector to select whichever network contains the addresses specified in the 'couchbase.seed.nodes' config property.

* Type: string
* Default: `auto`
* Importance: medium

### [](#couchbase.bootstrap.timeout)`couchbase.bootstrap.timeout`

On startup, the connector will wait this long for a Couchbase connection to be established. If a connection is not established before the timeout expires, the connector will terminate.

* Type: string
* Default: `30s`
* Valid Values: An integer followed by a time unit (ms = milliseconds, s = seconds, m = minutes, h = hours, d = days). For example, to specify 30 minutes: 30m
* Importance: medium

## [](#security)Security

### [](#couchbase.enable.tls)`couchbase.enable.tls`

Use secure connection to Couchbase Server.

If true, you must also tell the connector which certificate to trust. Specify a certificate file with 'couchbase.trust.certificate.path', or a Java keystore file with 'couchbase.trust.store.path' and 'couchbase.trust.store.password'.

* Type: boolean
* Default: `false`
* Importance: medium
* Dependents: `[couchbase.trust.certificate.path](#couchbase.trust.certificate.path)`, `[couchbase.trust.store.path](#couchbase.trust.store.path)`, `[couchbase.trust.store.password](#couchbase.trust.store.password)`, `[couchbase.enable.hostname.verification](#couchbase.enable.hostname.verification)`, `[couchbase.client.certificate.path](#couchbase.client.certificate.path)`, `[couchbase.client.certificate.password](#couchbase.client.certificate.password)`

### [](#couchbase.enable.hostname.verification)`couchbase.enable.hostname.verification`

Set this to `false` to disable TLS hostname verification for Couchbase connections. Less secure, but might be required if for some reason you can't issue a certificate whose Subject Alternative Names match the hostname used to connect to the server. Only disable if you understand the impact and can accept the risks.

* Type: boolean
* Default: `true`
* Importance: medium

### [](#couchbase.trust.store.path)`couchbase.trust.store.path`

Absolute filesystem path to the Java keystore holding the CA certificate used by Couchbase Server.

If you want to use a PEM file instead of a Java keystore, specify `couchbase.trust.certificate.path` instead.

* Type: string
* Default: `""`
* Importance: medium

### [](#couchbase.trust.store.password)`couchbase.trust.store.password`

Password for accessing the trust store.

May be overridden with the KAFKA\_COUCHBASE\_TRUST\_STORE\_PASSWORD environment variable.

* Type: password
* Default: `[hidden]`
* Importance: medium

### [](#couchbase.trust.certificate.path)`couchbase.trust.certificate.path`

Absolute filesystem path to the PEM file containing the CA certificate used by Couchbase Server.

If you want to use a Java keystore instead of a PEM file, specify `couchbase.trust.store.path` instead.

* Type: string
* Default: `""`
* Importance: medium

### [](#couchbase.client.certificate.path)`couchbase.client.certificate.path`

Absolute filesystem path to a Java keystore or PKCS12 bundle holding the private key and certificate chain to use for client certificate authentication (mutual TLS).

If you supply a value for this config property, the `couchbase.username` and `couchbase.password` properties will be ignored.

* Type: string
* Default: `""`
* Importance: medium

### [](#couchbase.client.certificate.password)`couchbase.client.certificate.password`

Password for accessing the client certificate.

May be overridden with the KAFKA\_COUCHBASE\_CLIENT\_CERTIFICATE\_PASSWORD environment variable.

* Type: password
* Default: `[hidden]`
* Importance: medium

## [](#logging)Logging

### [](#couchbase.log.redaction)`couchbase.log.redaction`

Determines which kinds of sensitive log messages from the Couchbase connector will be tagged for later redaction by the Couchbase log redaction tool. NONE = no tagging; PARTIAL = user data is tagged; FULL = user, meta, and system data is tagged.

* Type: string
* Default: `NONE`
* Valid Values: One of \[NONE, PARTIAL, FULL\]
* Importance: medium

### [](#couchbase.log.document.lifecycle)`couchbase.log.document.lifecycle`

If true, document lifecycle milestones will be logged at INFO level instead of DEBUG. Enabling this feature lets you watch documents flow through the connector. Disabled by default because it generates many log messages.

* Type: boolean
* Default: `false`
* Importance: medium

### [](#couchbase.metrics.interval)`couchbase.metrics.interval`

The connector writes metrics to the log at this interval.

Disable metric logging by setting this to `0`.

UNCOMMITTED; this feature may change in a patch release without notice.

* Since: 4.2.3
* Type: string
* Default: `10m`
* Valid Values: An integer followed by a time unit (ms = milliseconds, s = seconds, m = minutes, h = hours, d = days). For example, to specify 30 minutes: 30m
* Importance: medium

## [](#source-behavior)Source Behavior

### [](#couchbase.topic)`couchbase.topic`

Name of the Kafka topic to publish data to.

This is a format string that recognizes the following placeholders:

${bucket} refers to the bucket containing the document.

${scope} refers to the scope containing the document.

${collection} refers to the collection containing the document.

**This property supports contextual overrides.** The context is the name of the collection containing the document, qualified by scope. Specify a context by enclosing it in square brackets and appending it to the property name. When there is no matching override, the value of the base property (without brackets) is used instead.

* Override example: `couchbase.topic[myScope.myCollection]=some-other-topic`
* Type: string
* Default: `${bucket}.${scope}.${collection}`
* Importance: medium

### [](#couchbase.collection.to.topic)`couchbase.collection.to.topic`

A map from Couchbase collection to Kafka topic.

Collection and Topic are joined by an equals sign. Map entries are delimited by commas.

For example, if you want to write messages from collection "scope-a.invoices" to topic "topic1", and messages from collection "scope-a.widgets" to topic "topic2", you would write: "scope-a.invoices=topic1,scope-a.widgets=topic2".

Defaults to an empty map. For collections not present in this map, the destination topic is determined by the `couchbase.topic` config property.

> [!WARNING]
> **DEPRECATED.** Instead, please use `couchbase.topic` with contextual overrides.

* Since: 4.1.8
* Type: list
* Default: `""`
* Valid Values: scope.collection=topic,…​
* Importance: medium

### [](#couchbase.source.handler)`couchbase.source.handler`

The fully-qualified class name of the source handler to use. The source handler determines how the Couchbase document is converted into a Kafka record.

The class must implement either `com.couchbase.connect.kafka.handler.source.SourceHandler` or `com.couchbase.connect.kafka.handler.source.MultiSourceHandler`.

To publish JSON messages identical to the Couchbase documents, use `com.couchbase.connect.kafka.handler.source.RawJsonSourceHandler` and set `value.converter` to `org.apache.kafka.connect.converters.ByteArrayConverter`.

When using a custom source handler that filters out certain messages, consider also configuring `couchbase.black.hole.topic`. See that property's documentation for details.

* Type: class
* Importance: medium

### [](#couchbase.headers)`couchbase.headers`

Comma-delimited list of Couchbase metadata headers to add to records. Recognized values:

* **`bucket`** \- Name of the bucket the document came from.
* **`scope`** \- Name of the scope the document came from.
* **`collection`** \- Name of the collection the document came from.
* **`key`** \- The Couchbase document ID.
* **`qualifiedKey`** \- The document's scope, collection, and document ID, delimited by dots. Example: `myScope.myCollection.myDocumentId`
* **`cas`** \- The document's "compare and swap" value.
* **`partition`** \- The index of the Couchbase partition the document came from.
* **`partitionUuid`** \- Identifies the history branch of the partition the document came from.
* **`seqno`** \- The DCP sequence number of the event.
* **`rev`** \- The revision number of the event.
* **`expiry`** \- The epoch second when the document expires, or null if the document has no expiry (or if the event is a deletion).

UNCOMMITTED; this feature may change in a patch release without notice.

* Since: 4.2.5
* Type: list
* Default: `""`
* Valid Values: Zero or more of \[bucket, scope, collection, key, qualifiedKey, cas, partition, partitionUuid, seqno, rev, expiry\]
* Importance: medium

### [](#couchbase.header.name.prefix)`couchbase.header.name.prefix`

The connector prepends this value to header names to prevent collision with headers set by other parts of the system.

For example, if `couchbase.headers` is set to `bucket,qualifiedKey` and `header.name.prefix` is set to `example.` then records will have headers named `example.bucket` and `example.qualifiedKey`.

UNCOMMITTED; this feature may change in a patch release without notice.

* Since: 4.2.5
* Type: string
* Default: `couchbase.`
* Importance: medium

### [](#couchbase.event.filter)`couchbase.event.filter`

The class name of the event filter to use. The event filter determines whether a database change event is ignored.

As of version 4.3.0, the default filter ignores events from the Couchbase `_system` scope, and also ignores transaction metadata documents (documents whose keys start with "\_txn:").

If you are interested in those events too, set this property to `com.couchbase.connect.kafka.filter.AllPassIncludingSystemFilter`.

See also `couchbase.black.hole.topic`.

* Type: class
* Default: `com.couchbase.connect.kafka.filter.AllPassFilter`
* Importance: medium

### [](#couchbase.black.hole.topic)`couchbase.black.hole.topic`

If this property is non-blank, the connector publishes a tiny synthetic record to this topic whenever the Filter or SourceHandler ignores a source event.

This lets the connector tell the Kafka Connect framework about the source offset of the ignored event. Otherwise, a long sequence of ignored events in a low-traffic deployment might cause the stored source offset to lag too far behind the current source offset, which can lead to rollbacks to zero when the connector is restarted.

After a record is published to this topic, the record is no longer important, and should be deleted as soon as possible. To reduce disk usage, configure this topic to use small segments and the lowest possible retention settings.

* Since: 4.1.8
* Type: string
* Default: `""`
* Importance: medium

### [](#couchbase.initial.offset.topic)`couchbase.initial.offset.topic`

If `couchbase.stream.from` is `SAVED_OFFSET_OR_NOW`, and this property is non-blank, on startup the connector publishes to the named topic one tiny synthetic record for each source partition that does not yet have a saved offset.

This lets the connector initialize the missing source offsets to "now" (the current state of Couchbase).

The synthetic records have a value of null, and the same key:

__COUCHBASE_INITIAL_OFFSET_TOMBSTONE__a54ee32b-4a7e-4d98-aa36-45d8417e942a

Consumers of this topic must ignore (or tolerate) these records.

If you specify a value for `couchbase.black.hole.topic`, specify the same value here.

UNCOMMITTED; this feature may change in a patch release without notice.

* Since: 4.2.4
* Type: string
* Default: `""`
* Importance: medium

### [](#couchbase.batch.size.max)`couchbase.batch.size.max`

When the Kafka Connect framework polls the connector for new records, the connector returns no more than this many records at a time.

* Type: int
* Default: `2000`
* Importance: medium

### [](#couchbase.no.value)`couchbase.no.value`

If true, Couchbase Server will omit the document content when telling the connector about a change. The document key and metadata will still be present.

If you don't care about the content of changed documents, enabling this option is a great way to reduce the connector's network bandwidth and memory usage.

* Type: boolean
* Default: `false`
* Importance: medium

### [](#couchbase.connector.name.in.offsets)`couchbase.connector.name.in.offsets`

When true, the connector's offsets are saved under a key that includes the connector name. This is redundant, since the Kafka Connect framework already isolates the offsets of connectors with different names.

Set this to true only if you've previously deployed the connector to production with this set to true, and you do not wish to restart streaming from the beginning. Otherwise you should ignore this property.

* Type: boolean
* Default: `false`
* Importance: medium

### [](#couchbase.stream.from)`couchbase.stream.from`

Controls when in the history the connector starts streaming from.

* Type: string
* Default: `SAVED_OFFSET_OR_BEGINNING`
* Valid Values: One of \[SAVED\_OFFSET\_OR\_BEGINNING, SAVED\_OFFSET\_OR\_NOW, BEGINNING, NOW\]
* Importance: medium

### [](#couchbase.scope)`couchbase.scope`

If you wish to stream from all collections within a scope, specify the scope name here.

If you specify neither "couchbase.scope" nor "couchbase.collections", the connector will stream from all collections of all scopes in the bucket.

Requires Couchbase Server 7.0 or later.

* Type: string
* Default: `""`
* Importance: medium

### [](#couchbase.collections)`couchbase.collections`

If you wish to stream from specific collections, specify the qualified collection names here, separated by commas. A qualified name is the name of the scope followed by a dot (.) and then the name of the collection. For example: "tenant-foo.invoices".

If you specify neither "couchbase.scope" nor "couchbase.collections", the connector will stream from all collections of all scopes in the bucket.

Requires Couchbase Server 7.0 or later.

* Type: list
* Default: `""`
* Importance: medium

### [](#couchbase.jsonpath.filter)`couchbase.jsonpath.filter`

If you wish to filter the documents being sent, in addition to or instead of using a custom Filter class, this is applied before the couchbase.event.filter or the couchbase.source.handler

A document passes the jsonpath filter if the expression matches something in the document. If the property is blank or not specified then all documents will pass

Examples and uses of jsonpath can be found here: <https://github.com/json-path/JsonPath>

**This property supports contextual overrides.** The context is the name of the collection containing the document, qualified by scope. Specify a context by enclosing it in square brackets and appending it to the property name. When there is no matching override, the value of the base property (without brackets) is used instead.

* Override example: `couchbase.jsonpath.filter[myScope.myCollection]=$.key`
* Type: string
* Default: `""`
* Valid Values: A JSONPath expression
* Importance: medium

## [](#schema)Schema

### [](#couchbase.value.schema)`couchbase.value.schema`

The schema to apply to the value of each record.

This property will be ignored unless the source handler specified by `couchbase.source.handler` supports it.

The built-in `com.couchbase.connect.kafka.handler.source.ConfigurableSchemaSourceHandler` supports this property. ConfigurableSchemaSourceHandler expects the schema to be an Avro Schema Record, stored in a JSON object. Reference: <https://avro.apache.org/docs/1.12.0/specification/>

ConfigurableSchemaSourceHandler will filter out documents that do not have a JSON Object at the root, and any that do not match the specified Schema..

**This property supports contextual overrides.** The context is the name of the collection to apply the schema to, qualified by scope. Specify a context by enclosing it in square brackets and appending it to the property name. When there is no matching override, the value of the base property (without brackets) is used instead.

* Override example: `couchbase.value.schema[myScope.myCollection]={"type": "typeName", …​attributes…​}`

UNCOMMITTED; this feature may change in a patch release without notice.

* Type: string
* Default: `""`
* Importance: medium

### [](#couchbase.schema.failure.action)`couchbase.schema.failure.action`

Determines the behaviour when a Schema Mismatch or Missing Schema is encountered for a document using the Schema Registry. This property will be ignored unless the source handler specified by `couchbase.source.handler` supports it. The built-in `com.couchbase.connect.kafka.handler.source.SchemaRegistrySourceHandler` supports this property.

TERMINATE will stop processing documents so that the user can intervene or investigate. DROP will mark the document as SKIPPED\_BECAUSE\_HANDLER\_SAYS\_IGNORE. DLQ will send the document to a default topic acting as a dead letter queue, which can optionally be specified by the user.

UNCOMMITTED; this feature may change in a patch release without notice.

* Type: string
* Default: `TERMINATE`
* Valid Values: One of \[TERMINATE, DROP, DLQ\]
* Importance: medium

### [](#couchbase.dlq.topic)`couchbase.dlq.topic`

This property will be ignored unless the source handler specified by `couchbase.source.handler` supports it. The built-in `com.couchbase.connect.kafka.handler.source.SchemaRegistrySourceHandler` supports this property.

If `couchbase.schema.failure.action` is set to DLQ then documents that encounter any Schema failures will be sent to this topic. Headers will be added for future investigation such as the intended destination and the reason it was sent to the DLQ

UNCOMMITTED; this feature may change in a patch release without notice.

* Type: string
* Default: `couchbase.dlq`
* Importance: medium

## [](#database-change-protocol)Database Change Protocol

### [](#couchbase.compression)`couchbase.compression`

To reduce bandwidth usage, Couchbase Server 5.5 and later can send documents to the connector in compressed form. (Messages are always published to the Kafka topic in uncompressed form, regardless of this setting.)

* Type: string
* Default: `ENABLED`
* Valid Values: One of \[DISABLED, FORCED, ENABLED\]
* Importance: medium

### [](#couchbase.persistence.polling.interval)`couchbase.persistence.polling.interval`

When a Couchbase Server node fails over, documents on the failing node that haven't been fully replicated may be "rolled back" to a previous state. To ensure consistency between Couchbase and the Kafka topic, the connector can defer publishing a document to Kafka until it has been saved to disk on all replicas.

To enable this feature, specify a non-zero persistence polling interval. The interval is how frequently the connector asks each Couchbase node which changes have been fully replicated and persisted. This ensures consistency between Couchbase and Kafka, at the cost of additional latency and bandwidth usage.

To disable this feature, specify a zero duration (`0`). In this mode the connector publishes changes to Kafka immediately, without waiting for replication. This is fast and uses less network bandwidth, but can result in publishing "phantom changes" that don't reflect the actual state of a document in Couchbase after a failover.

> [!TIP]
> Documents written to Couchbase with enhanced durability are never published to Kafka until the durability requirements are met, regardless of whether persistence polling is enabled.

> [!CAUTION]
> When connecting to an ephemeral bucket, always disable persistence polling by setting this config option to `0`, otherwise the connector will never publish any changes.

* Type: string
* Default: `100ms`
* Valid Values: An integer followed by a time unit (ms = milliseconds, s = seconds, m = minutes, h = hours, d = days). For example, to specify 30 minutes: 30m
* Importance: medium

### [](#couchbase.flow.control.buffer)`couchbase.flow.control.buffer`

The flow control buffer limits how much data Couchbase will send before waiting for the connector to acknowledge the data has been processed. The recommended size is between 10 MiB ("10m") and 50 MiB ("50m").

> [!CAUTION]
> Make sure to allocate enough memory to the Kafka Connect worker process to accommodate the flow control buffer, otherwise the connector might run out of memory under heavy load. Read on for details.

There's a separate buffer for each node in the Couchbase cluster. When calculating how much memory to allocate to the Kafka Connect worker, multiply the flow control buffer size by the number of Couchbase nodes, then multiply by 2\. This is how much memory a single connector task requires for the flow control buffer (not counting the connector's baseline memory usage).

* Type: string
* Default: `16m`
* Valid Values: An integer followed by a size unit (b = bytes, k = kilobytes, m = megabytes, g = gigabytes). For example, to specify 64 megabytes: 64m
* Importance: medium

### [](#couchbase.xattrs)`couchbase.xattrs`

Should filters and source handlers have access to a document's extended attributes?

* Type: boolean
* Default: `false`
* Importance: medium

### [](#couchbase.enable.dcp.trace)`couchbase.enable.dcp.trace`

If true, detailed protocol trace information is logged to the `com.couchbase.client.dcp.trace` category at INFO level. Otherwise, trace information is not logged.

Disabled by default because it generates many log messages.

* Since: 4.1.6
* Type: boolean
* Default: `false`
* Importance: medium
* Dependents: `[couchbase.dcp.trace.document.id.regex](#couchbase.dcp.trace.document.id.regex)`

### [](#couchbase.dcp.trace.document.id.regex)`couchbase.dcp.trace.document.id.regex`

When DCP trace is enabled, set this property to limit the trace to only documents whose IDs match this Java regular expression.

Ignored if `couchbase.enable.dcp.trace` is false.

* Since: 4.1.6
* Type: string
* Default: `.*`
* Importance: medium