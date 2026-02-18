---
title: Release Notes
editUrl: https://github.com/couchbase/docs-kafka/edit/release/4.3/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/kafka-connector/current/release-notes.html)

# Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Kafka Connector. 

This page covers version 4.x of the Couchbase Kafka Connector. For earlier versions, please see the [3.x Release Notes](#3.4@release-notes.adoc).

## [](#installation)Installation

Scroll down to the version you want, then click the "Download" link to get the full connector distribution. Refer to the [Quickstart Guide](quickstart.md) for detailed installation instructions.

Alternatively, Confluent Platform users can [install the connector via Confluent Hub](https://www.confluent.io/hub/couchbase/kafka-connect-couchbase).

### [](#java-api-maven-coordinates)Java API Maven Coordinates

You can optionally extend the connector’s functionality by writing custom components. When developing a custom component, include the connector’s Java API in your Maven project by adding this dependency to your POM:

```xml
<dependency>
    <groupId>com.couchbase.client</groupId>
    <artifactId>kafka-connect-couchbase</artifactId>
    <version><!-- connector version --></version>
</dependency>
```

## [](#v4.3.3)Version 4.3.3 (20 Jan 2026)

[Download](https://packages.couchbase.com/clients/kafka/4.3.3/couchbase-kafka-connect-couchbase-4.3.3.zip)

This release adds experimental support for Schema Registry enforcement, and upgrades dependency versions.

### [](#enhancements)Enhancements

* [KAFKAC-415](https://jira.issues.couchbase.com/browse/KAFKAC-415): **Source**Makes InvalidPathExceptions from JSONPath filtering fail the filter rather than be propagated.
* [KAFKAC-416](https://jira.issues.couchbase.com/browse/KAFKAC-416): **Source**Add more user control over the behaviour when there is a missing schema or schema mismatch.
* [KAFKAC-417](https://jira.issues.couchbase.com/browse/KAFKAC-417): Upgraded Couchbase Java SDK from `3.10.0` to `3.10.1`

### [](#bug-fixes)Bug Fixes

* [KAFKAC-412](https://jira.issues.couchbase.com/browse/KAFKAC-412): **Source**JSONPath filters now correctly ignore non-json documents.

## [](#v4.3.2)Version 4.3.2 (8 Dec 2025)

[Download](https://packages.couchbase.com/clients/kafka/4.3.2/couchbase-kafka-connect-couchbase-4.3.2.zip)

This release adds experimental support for Schema Registry enforcement, and upgrades dependency versions.

### [](#enhancements-2)Enhancements

* [KAFKAC-408](https://jira.issues.couchbase.com/browse/KAFKAC-408): **Source**Add experimental support for schema enforcement for the source connector using Avro and the Confluent Schema Registry.
* [KAFKAC-413](https://jira.issues.couchbase.com/browse/KAFKAC-413): Upgraded Couchbase Java SDK from `3.9.2` to `3.10.0`

### [](#bug-fixes-2)Bug Fixes

* [KAFKAC-412](https://jira.issues.couchbase.com/browse/KAFKAC-412): **Source**JSONPath filters now correctly ignore non-json documents.

## [](#v4.3.1)Version 4.3.1 (22 Oct 2025)

[Download](https://packages.couchbase.com/clients/kafka/4.3.1/couchbase-kafka-connect-couchbase-4.3.1.zip)

This release adds experimental support for config-driven schemas, and upgrades dependency versions.

### [](#enhancements-3)Enhancements

* [KAFKAC-399](https://jira.issues.couchbase.com/browse/KAFKAC-399): **Source**Added experimental support for config-driven schemas via [the new couchbase.value.schema connector config property](source-configuration-options.md#couchbase.value.schema).
* [KAFKAC-404](https://jira.issues.couchbase.com/browse/KAFKAC-404): Upgraded Couchbase Java SDK from `3.9.0` to `3.9.2`
* [KAFKAC-409](https://jira.issues.couchbase.com/browse/KAFKAC-409): Upgraded DCP client from `0.55.0` to `0.56.0`

## [](#v4.3.0)Version 4.3.0 (13 Aug 2025)

[Download](https://packages.couchbase.com/clients/kafka/4.3.0/couchbase-kafka-connect-couchbase-4.3.0.zip)

This release adds contextual overrides for connector config properties, support for filtering using JSONPath expressions, and various minor improvements.

> [!WARNING]
> Watch out for a change to the network detection heuristic. If the connector is unable to connect to Couchbase Server after the upgrade, you might need to specify `couchbase.network=default` in your connector config.

### [](#behavioral-changes)Behavioral Changes

* [JVMCBC-1660](https://jira.issues.couchbase.com/browse/JVMCBC-1660): The `auto` network selection heuristic has been changed to fall back to the `external` network if there is no exact address match and the `external` network is present.  
Previously, if there was no exact match between an address in the connection string and an address in the cluster topology reported by the server, the connector would select the `default` network. Now, if there is no match and an `external` network is present, the connector selects the `external` network.  
> [!TIP]  
> If this change causes the connector to select the incorrect network for your deployment (you’ll know because the connector will be unable to connect to the Couchbase Server cluster), specify `couchbase.network=default` in your connector config to force the connector to use the same network as before.
* [KAFKAC-400](https://jira.issues.couchbase.com/browse/KAFKAC-400): **Source**The default filter (`AllPassFilter`) now filters out documents whose IDs start with `_txn:`. These documents contain Couchbase transaction metadata, and might not be JSON. Filtering them out prevents warnings like:  
Skipping non-JSON document: bucket=<bucket> key=_default._default._txn:client-record
* [KAFKAC-401](https://jira.issues.couchbase.com/browse/KAFKAC-401): **Source**The default filter (`AllPassFilter`) now _actually_ filters out documents in the Couchbase system scope. This feature was originally announced in connector version 4.2.4, but it didn’t work until now.

If you wish to continue receiving transaction metadata and system documents, configure the source connector like this:

```properties
couchbase.event.filter=com.couchbase.connect.kafka.filter.AllPassIncludingSystemFilter
```

### [](#enhancements-4)Enhancements

* [KAFKAC-383](https://jira.issues.couchbase.com/browse/KAFKAC-383): **Source**The new `couchbase.jsonpath.filter` connector config property lets you filter out documents that do not match some [JSONPath expression](https://github.com/json-path/JsonPath).
* [KAFKAC-382](https://jira.issues.couchbase.com/browse/KAFKAC-382): Certain connector config properties now support contextual overrides. This lets you have a default value for a property, and override the default in different contexts.  
In the source connector, the context is usually the collection a document came from. In the sink connector, the context is usually the Kafka topic a record came from.  
See the source/sink configuration options documentation for examples and information about which properties support contextual overrides.
* [KAFKAC-398](https://jira.issues.couchbase.com/browse/KAFKAC-398): **Source**Metrics reported by the connector are now tagged with the UUID of the Couchbase cluster and the name of the bucket.
* [KAFKAC-390](https://jira.issues.couchbase.com/browse/KAFKAC-390): Lifecycle milestone messages are now logged to a category suffixed by the milestone type. For example, `SOURCE_OFFETS_READ` events are now logged to category `com.couchbase.connect.kafka.SourceDocumentLifecycle.SOURCE_OFFSETS_READ`. This lets you filter the events you’re interested in by configuring the log levels for the logging categories specific to each event type.
* [KAFKAC-397](https://jira.issues.couchbase.com/browse/KAFKAC-397): The connector no longer depends on Apache Commons Lang.
* [KAFKAC-402](https://jira.issues.couchbase.com/browse/KAFKAC-402): Upgraded Couchbase Java SDK from `3.8.0` to `3.9.0`
* [KAFKAC-403](https://jira.issues.couchbase.com/browse/KAFKAC-403): Upgraded DCP client from `0.54.0` to `0.55.0`

## [](#v4.2.8)Version 4.2.8 (22 Apr 2025)

[Download](https://packages.couchbase.com/clients/kafka/4.2.8/couchbase-kafka-connect-couchbase-4.2.8.zip)

This maintenance release includes a few minor improvements.

### [](#enhancements-5)Enhancements

* [KAFKAC-377](https://jira.issues.couchbase.com/browse/KAFKAC-377): **Source** Document lifecycle log messages now include a `taskUuid` field that uniquely identifies the source task instance handling the message.
* [KAFKAC-379](https://jira.issues.couchbase.com/browse/KAFKAC-379): **Source** `RawJsonWithMetadataSourceHandler` now has a protected method `customizeMetadata` that subclasses can override to add or remove metadata elements (like scope and collection, for example). Thank you to [Yeikel](https://github.com/yeikel).
* [KAFKAC-381](https://jira.issues.couchbase.com/browse/KAFKAC-381): Upgrade DCP client from `0.53.0` to `0.54.0`.
* [KAFKAC-380](https://jira.issues.couchbase.com/browse/KAFKAC-380): Upgrade Couchbase Java SDK from `3.7.9` to `3.8.0`.

## [](#v4.2.7)Version 4.2.7 (12 Mar 2025)

[Download](https://packages.couchbase.com/clients/kafka/4.2.7/couchbase-kafka-connect-couchbase-4.2.7.zip)

This maintenance release includes an important fix for a potential resource leak, and a handful of minor improvements.

### [](#enhancements-6)Enhancements

* [KAFKAC-366](https://jira.issues.couchbase.com/browse/KAFKAC-366): **Source** Added an optional `onRecordCommitted` method to the `SourceHandler` interface. This method is called whenever the Kafka Connect framework calls `SourceTask.commitRecord`. Subclasses may override this method to do something special with committed record metadata beyond the usual document lifecycle logging. The default implementation does nothing, which is always okay.  
Thank you to new contributor Eyal Nussbaum!
* [KAFKAC-369](https://jira.issues.couchbase.com/browse/KAFKAC-369): **Source** `OFFSET_COMMIT_HOOK` lifecycle messages are now logged at DEBUG level instead of INFO.
* [KAFKAC-374](https://jira.issues.couchbase.com/browse/KAFKAC-374): Upgrade DCP client from `0.52.0` to `0.53.0`.
* [KAFKAC-375](https://jira.issues.couchbase.com/browse/KAFKAC-375): Upgrade Couchbase Java SDK from `3.7.5` to `3.7.9`.

### [](#bug-fixes-3)Bug Fixes

* [KAFKAC-370](https://jira.issues.couchbase.com/browse/KAFKAC-370): **Source** Fixed a race condition that could cause a source task to fail to disconnect its DCP client if the task was stopped immediately after starting. This could lead to a resource leak for the Kafka Connect worker process, and performance issues for Couchbase Server.

## [](#v4.2.6)Version 4.2.6 (21 Nov 2024)

[Download](https://packages.couchbase.com/clients/kafka/4.2.6/couchbase-kafka-connect-couchbase-4.2.6.zip)

In addition to the usual dependency version bumps, this release adds the ability to include Couchbase document metadata in Kafka record headers, regardless of which `SourceHandler` is used.

### [](#enhancements-7)Enhancements

* [KAFKAC-362](https://jira.issues.couchbase.com/browse/KAFKAC-362): **Source** The connector can now set Couchbase document metadata headers on Kafka records.  
Specify the desired headers using [the new couchbase.headers connector config property](source-configuration-options.md#couchbase.headers).  
> [!NOTE]  
> This new config property is "uncommitted API", meaning it may change without notice. It may be promoted to "committed API" in a subsequent minor version.
* [KAFKAC-363](https://jira.issues.couchbase.com/browse/KAFKAC-363): Upgrade Couchbase Java SDK from `3.7.4` to `3.7.5`.

## [](#v4.2.4)Version 4.2.4 (31 Oct 2024)

[Download](https://packages.couchbase.com/clients/kafka/4.2.4/couchbase-kafka-connect-couchbase-4.2.4.zip)

In addition to the usual dependency version bumps, this release improves some behaviors and adds new connector configuration properties.

### [](#enhancements-8)Enhancements

* [KAFKAC-353](https://jira.issues.couchbase.com/browse/KAFKAC-353): **Source** When streaming from `SAVED_OFFSET_OR_NOW`, you can configure the connector to immediately save the "now" source offsets for all Couchbase partitions immediately on startup, instead of waiting for events to arrive for a partition before storing that partition’s source offset.  
To enable this new behavior, specify a topic name for [the new couchbase.initial.offset.topic connector config property](source-configuration-options.md#couchbase.initial.offset.topic).  
> [!NOTE]  
> This new config property is "uncommitted API", meaning it may change without notice. It may be promoted to "committed API" in a subsequent minor version.
* [KAFKAC-358](https://jira.issues.couchbase.com/browse/KAFKAC-358): **Sink** [The new couchbase.topic.to.document.id connector config property](sink-configuration-options.md#couchbase.topic.to.document.id) lets you override the `couchbase.document.id` property for specific topics. The value is a comma-delimited list of map entries, where each map entry looks like: `topicName=${/json/pointer/to/id/field}`  
Thank you to community member Hafiz Hussain Haroon Rasheed ([HafizHussain31](https://github.com/HafizHussain31)) for contributing this feature.  
> [!NOTE]  
> This new config property is "uncommitted API", meaning it may change without notice. It may be promoted to "committed API" in a subsequent minor version.
* [KAFKAC-359](https://jira.issues.couchbase.com/browse/KAFKAC-359): The connector now includes provider configuration files for [KIP-898: Modernize Connect plugin discovery](https://cwiki.apache.org/confluence/display/KAFKA/KIP-898%3A+Modernize+Connect+plugin+discovery).
* [KAFKAC-361](https://jira.issues.couchbase.com/browse/KAFKAC-361): Upgrade Couchbase Java SDK from `3.7.1` to `3.7.4`.
* [KAFKAC-360](https://jira.issues.couchbase.com/browse/KAFKAC-360): Upgrade DCP client from `0.51.0` to `0.52.0`.

### [](#bug-fixes-4)Bug Fixes

* [KAFKAC-352](https://jira.issues.couchbase.com/browse/KAFKAC-352): **Source** The default event filter, `com.couchbase.connect.kafka.filter.AllPassFilter`, now excludes events from Couchbase system scopes. (System scopes store internal metadata that is typically uninteresting to developers.)  
> [!TIP]  
> If you wish to keep the previous behavior of including system scopes, set the `couchbase.event.filter` property to `com.couchbase.connect.kafka.filter.AllPassIncludingSystemFilter`.

## [](#v4.2.3)Version 4.2.3 (25 Jul 2024)

[Download](https://packages.couchbase.com/clients/kafka/4.2.3/couchbase-kafka-connect-couchbase-4.2.3.zip)

This maintenance release updates the Couchbase Java SDK to the most recent version, and writes metrics to the connector log.

### [](#enhancements-9)Enhancements

* [KAFKAC-347](https://issues.couchbase.com/browse/KAFKAC-347): The connector now writes its metrics to the log (in addition to exposing them via JMX like before). Configure the logging interval by setting the new `couchbase.metrics.interval` connector property. The default interval is 10 minutes.
* [KAFKAC-348](https://issues.couchbase.com/browse/KAFKAC-348): **Source** The connector now captures additional metrics related to `Filter` and `SourceHandler` performance.

  * `handler` — A timer for `SourceHandler.handle()`
  * `filter` — A timer for `Filter.pass()`
  * `filtered.out` — A counter for events discarded by the `Filter` or `SourceHandler`.
* [KAFKAC-350](https://issues.couchbase.com/browse/KAFKAC-350): Upgrade Couchbase Java SDK from `3.6.1` to `3.7.1`
* [KAFKAC-343](https://issues.couchbase.com/browse/KAFKAC-343): Upgrade DCP client from `0.50.0` to `0.51.0`. Notably:

  * [JDCP-245](https://issues.couchbase.com/browse/JDCP-245): The DCP client now sets the `ACTIVE_VB_ONLY` flag when opening a stream. This prevents the connector from inadvertently streaming from a replica partition, which could cause problems with some versions of Couchbase Server.

## [](#v4.2.2)Version 4.2.2 (16 Apr 2024)

[Download](https://packages.couchbase.com/clients/kafka/4.2.2/couchbase-kafka-connect-couchbase-4.2.2.zip)

This maintenance release updates the Couchbase Java SDK to the most recent version.

### [](#enhancements-10)Enhancements

* [KAFKAC-340](https://issues.couchbase.com/browse/KAFKAC-340): Upgrade Couchbase Java SDK from `3.5.2` to `3.6.1`.  
Notably:

  * [JVMCBC-1499](https://issues.couchbase.com/browse/JVMCBC-1499)Disabled DNS SRV caching. The connector now responds quicker to DNS changes in dynamic environments like Kubernetes.

## [](#v4.2.1)Version 4.2.1 (26 Feb 2024)

[Download](https://packages.couchbase.com/clients/kafka/4.2.1/couchbase-kafka-connect-couchbase-4.2.1.zip)

This maintenance release fixes an issue that sometimes prevented the connector from starting successfully.

### [](#enhancements-11)Enhancements

* [KAFKAC-337](https://issues.couchbase.com/browse/KAFKAC-337): **Sink** The connector no longer logs `TooManyInstancesDetectedEvent` warnings on startup. These warnings were harmless, but annoying.
* [KAFKAC-334](https://issues.couchbase.com/browse/KAFKAC-334): Upgrade Couchbase DCP client from `0.48.0` to `0.49.0`.

### [](#bug-fixes-5)Bug Fixes

* [KAFKAC-333](https://issues.couchbase.com/browse/KAFKAC-333): Fixed a race condition that could cause the connector to fail at startup with a `ConcurrentModificationException`.

## [](#v4.2.0)Version 4.2.0 (26 Jan 2024)

[Download](https://packages.couchbase.com/clients/kafka/4.2.0/couchbase-kafka-connect-couchbase-4.2.0.zip)

With this minor version bump, the sink connector can now write documents to different buckets depending on the Kafka topic they were received from.

This release also improves the robustness of the source connector in certain conditions.

Apache Kafka 2.8 and Confluent Platform 6.2 are now the minimum supported versions.

### [](#enhancements-12)Enhancements

* [KAFKAC-327](https://issues.couchbase.com/browse/KAFKAC-327): **Sink** The `couchbase.default.collection` and `couchbase.topic.to.collection` config properties now support qualifying the collection with a bucket name, like `my-bucket.my-scope.my-collection`. This lets a single instance of the sink connector write to different buckets.
* [KAFKAC-332](https://issues.couchbase.com/browse/KAFKAC-332): The following connector config options, which were added in previous versions as "uncommitted" API, are now part of the "committed" (stable) API:

  * `couchbase.retry.timeout`
  * `couchbase.black.hole.topic`
  * `couchbase.enable.dcp.trace`
  * `couchbase.dcp.trace.document.id.regex`
* [KAFKAC-331](https://issues.couchbase.com/browse/KAFKAC-331): Upgrade Couchbase Java SDK from `3.4.7` to `3.5.2`.
* [KAFKAC-330](https://issues.couchbase.com/browse/KAFKAC-330): Upgrade Couchbase DCP client from `0.47.0` to `0.48.0`.

### [](#bug-fixes-6)Bug Fixes

* [JDCP-239](https://issues.couchbase.com/browse/JDCP-239): **Source** Improved reliability of initial startup during a Couchbase Server cluster rebalance, or before a newly-created bucket is ready.
* [JDCP-240](https://issues.couchbase.com/browse/JDCP-240): **Source** When `couchbase.stream.from` is set to `NOW` or `SAVED_OFFSET_OR_NOW` and there is an inactive partition when the connector starts up, the connector now waits for the partition to become active, instead of starting from the beginning for that partition.
* [JDCP-241](https://issues.couchbase.com/browse/JDCP-241): **Source** Improved handling of an edge case that could cause the connector to stop streaming for a partition. If a DCP socket connection is lost after receiving a snapshot marker for a partition and before receiving the first item in the snapshot, the connector now recovers instead of failing to resume streaming for that partition.

## [](#v4.1.14)Version 4.1.14 (3 Oct 2023)

[Download](https://packages.couchbase.com/clients/kafka/4.1.14/couchbase-kafka-connect-couchbase-4.1.14.zip)

This maintenance release improves how the source connector resolves DNS SRV addresses.

### [](#enhancements-13)Enhancements

* [KAFKAC-307](https://issues.couchbase.com/browse/KAFKAC-307): **Source** Instead of resolving a DNS SRV address just once when the connector starts up, the connector now passes the DNS SRV address along to the DCP client, so the DCP client can re-resolve it if necessary.

## [](#v4.1.13)Version 4.1.13 (21 Jun 2023)

[Download](https://packages.couchbase.com/clients/kafka/4.1.13/couchbase-kafka-connect-couchbase-4.1.13.zip)

This maintenance release fixes a memory leak that could occur if the source connector failed to establish the initial DCP connection to Couchbase Server.

### [](#enhancements-14)Enhancements

* [KAFKAC-323](https://issues.couchbase.com/browse/KAFKAC-323): **Source** If the initial DCP connection fails, the connector no longer throws `RejectedExecutionException` and no longer leaks memory.
* [KAFKAC-325](https://issues.couchbase.com/browse/KAFKAC-325): Upgraded Couchbase DCP client from 0.46.0 to 0.47.0.
* [KAFKAC-324](https://issues.couchbase.com/browse/KAFKAC-324): Upgraded Couchbase Java SDK from 3.4.6 to 3.4.7.

## [](#v4.1.12)Version 4.1.12 (17 May 2023)

[Download](https://packages.couchbase.com/clients/kafka/4.1.12/couchbase-kafka-connect-couchbase-4.1.12.zip)

If the connector is stopped for an extended period of time, it can now resume from where it left off, without having to roll back to zero. This behavior requires Couchbase Server 7.2 or later.

### [](#enhancements-15)Enhancements

* [KAFKAC-319](https://issues.couchbase.com/browse/KAFKAC-319): When resuming from an old checkpoint (where the connector’s sequence number is lower than Couchbase Server’s purge sequence number), the connector no longer rolls back to zero. This behavior requires Couchbase Server 7.2 or later.
* [KAFKAC-322](https://issues.couchbase.com/browse/KAFKAC-322): Upgraded Couchbase DCP client from 0.44.0 to 0.46.0.
* [KAFKAC-321](https://issues.couchbase.com/browse/KAFKAC-321): Upgraded Couchbase Java SDK from 3.4.3 to 3.4.6.

## [](#v4.1.11)Version 4.1.11 (17 February 2023)

[Download](https://packages.couchbase.com/clients/kafka/4.1.11/couchbase-kafka-connect-couchbase-4.1.11.zip)

The source connector now takes advantage of the new history preservation feature in Couchbase Server 7.2.

### [](#enhancements-16)Enhancements

* [KAFKAC-311](https://issues.couchbase.com/browse/KAFKAC-311): **Source** If the source bucket is configured to preserve history, the connector publishes every version of a document it sees within the history window, not just the latest version. See [Delivery Guarantees](delivery-guarantees.md) for details. Requires Couchbase Server 7.2 or later.
* [KAFKAC-316](https://issues.couchbase.com/browse/KAFKAC-316): Upgraded Couchbase DCP client from `0.43.0` to `0.44.0`.
* [KAFKAC-317](https://issues.couchbase.com/browse/KAFKAC-317): Upgraded Couchbase Java SDK from `3.4.1` to `3.4.3`.

## [](#v4.1.10)Version 4.1.10 (20 December 2022)

[Download](https://packages.couchbase.com/clients/kafka/4.1.10/couchbase-kafka-connect-couchbase-4.1.10.zip)

Dependency updates and source connector improvements.

### [](#enhancements-17)Enhancements

* [KAFKAC-303](https://issues.couchbase.com/browse/KAFKAC-303): **Source** The connector now includes DCP snapshot boundaries in its source offsets. This improves the reliability of resuming from saved offsets.
* [KAFKAC-302](https://issues.couchbase.com/browse/KAFKAC-302): **Source** The connector now logs more diagnostic information about lifecycle milestones.
* [KAFKAC-301](https://issues.couchbase.com/browse/KAFKAC-301): Upgraded Couchbase DCP client from `0.42.0` to `0.43.0`.
* [KAFKAC-305](https://issues.couchbase.com/browse/KAFKAC-305): Upgraded Couchbase Java SDK from `3.3.4` to `3.4.1`.

### [](#bug-fixes-7)Bug Fixes

* [JDCP-232](https://issues.couchbase.com/browse/JDCP-232): Fixed a race condition that sometimes caused the connector to fail on startup with the message: `java.lang.IllegalStateException: Tried to add duplicate channel`.

## [](#v4.1.9)Version 4.1.9 (21 October 2022)

[Download](https://packages.couchbase.com/clients/kafka/4.1.9/couchbase-kafka-connect-couchbase-4.1.9.zip)

You can now authenticate with Couchbase as an LDAP user, as long as secure connections are enabled.

### [](#breaking-changes)Breaking Changes

* The Couchbase `dcp-client` library no longer includes a repackaged version of Jackson. If you have written your own custom `Filter`, `SourceHandler`, or `SinkHandler` component that depends on the DCP client’s repackaged Jackson, search for:  
```java  
import com.couchbase.client.dcp.deps.  
```  
and replace with:  
```java  
import com.couchbase.client.core.deps.  
```  
to use the version in the Couchbase `core-io` library instead.

### [](#enhancements-18)Enhancements

* [JDCP-224](https://issues.couchbase.com/browse/JDCP-224): Use SASL mechanism `PLAIN` when authenticating with Couchbase on a secure connection. `PLAIN` is the fastest mechanism, and the only one that works with LDAP users.
* [JDCP-217](https://issues.couchbase.com/browse/JDCP-217): Support Couchbase clusters that advertise only TLS ports.
* [KAFKAC-299](https://issues.couchbase.com/browse/KAFKAC-299): Upgrade Couchbase DCP client from `0.41.0` to `0.42.0`.

## [](#v4.1.8)Version 4.1.8 (20 September 2022)

[Download](https://packages.couchbase.com/clients/kafka/4.1.8/couchbase-kafka-connect-couchbase-4.1.8.zip)

This version improves support for scopes & collections, adds an experimental `AnalyticsSinkHandler`, and adds a new feature that may reduce rollbacks by telling the Kafka Connect framework about the source offsets of ignored Couchbase events.

### [](#enhancements-19)Enhancements

* [KAFKAC-295](https://issues.couchbase.com/browse/KAFKAC-295) **Source** The new `couchbase.collection.to.topic` config property lets you specify an arbitrary mapping from Couchbase scope & collection to Kafka topic. This is useful when the `couchbase.topic` property is not sufficient because the desired topic name differs from the collection name. Thanks to Shahrzad Haji Amin Shirazi.
* [KAFKAC-293](https://issues.couchbase.com/browse/KAFKAC-293) **Sink** `N1qlSinkHandler` now honors the configured destination scope & collection. Thanks to Shahrzad Haji Amin Shirazi.
* [KAFKAC-294](https://issues.couchbase.com/browse/KAFKAC-294) **Sink** The new experimental `AnalyticsSinkHandler` sends documents directly to the Analytics service. Thanks to Shahrzad Haji Amin Shirazi.
* [KAFKAC-296](https://issues.couchbase.com/browse/KAFKAC-296) **Source** In extremely low-traffic environments that ignore a majority of Couchbase events, the new `couchbase.black.hole.topic` config property may reduce the occurrence of rollback to zero. If a topic is specified, the connector sends a tiny record to this topic for each ignored event, to inform Kafka Connect about the event’s source offset.
* [KAFKAC-297](https://issues.couchbase.com/browse/KAFKAC-297): Upgraded Couchbase Java SDK from 3.3.0 to 3.3.4.
* [KAFKAC-298](https://issues.couchbase.com/browse/KAFKAC-298): Upgraded DCP client from 0.40.0 to 0.41.0

## [](#v4.1.7)Version 4.1.7 (17 May 2022)

[Download](https://packages.couchbase.com/clients/kafka/4.1.7/couchbase-kafka-connect-couchbase-4.1.7.zip)

This version makes it easier to connect to Capella.

### [](#enhancements-20)Enhancements

* [KAFKAC-290](https://issues.couchbase.com/browse/KAFKAC-290)When connecting to Capella, it is no longer necessary to configure the Certificate Authority certificate. All you need to do is enable TLS.
* [KAFKAC-288](https://issues.couchbase.com/browse/KAFKAC-288): Upgraded Couchbase Java SDK from 3.2.5 to 3.3.0.

## [](#v4.1.6)Version 4.1.6 (15 Feb 2022)

[Download](https://packages.couchbase.com/clients/kafka/4.1.6/couchbase-kafka-connect-couchbase-4.1.6.zip)

Recommended for all users, this version fixes a memory leak when the connector stops.

### [](#bug-fixes-8)Bug Fixes

* [KAFKAC-283](https://issues.couchbase.com/browse/KAFKAC-283): The connector no longer leaks JMX MBeans on shutdown. The leak was a regression in version 4.0.2.

### [](#enhancements-21)Enhancements

* [KAFKAC-284](https://issues.couchbase.com/browse/KAFKAC-284) **Source** Added a new `couchbase.enable.dcp.trace` config option for enabling a DCP protocol trace to assist with diagnosing connector issues. Also added `couchbase.dcp.trace.document.id.regex` to narrow the scope of the trace.
* [KAFKAC-286](https://issues.couchbase.com/browse/KAFKAC-286): Upgraded Couchbase Java SDK from 3.2.4 to 3.2.5.
* [KAFKAC-287](https://issues.couchbase.com/browse/KAFKAC-287): Upgraded Couchbase DCP Client from 0.39.0 to 0.40.0.

## [](#v4.1.5)Version 4.1.5 (18 Jan 2022)

[Download](https://packages.couchbase.com/clients/kafka/4.1.5/couchbase-kafka-connect-couchbase-4.1.5.zip)

This version upgrades the Couchbase clients and other dependencies.

### [](#enhancements-22)Enhancements

* [KAFKAC-279](https://issues.couchbase.com/browse/KAFKAC-279): Upgraded Couchbase DCP Client from 0.37.0 to 0.39.0:

  * [JDCP-208](https://issues.couchbase.com/browse/JDCP-208)Improved the error message when the Couchbase user has insufficient permissions.
  * [JDCP-210](https://issues.couchbase.com/browse/JDCP-210)Authentication no longer fails when credentials have non-ASCII characters and the system default encoding is not UTF-8.
* [KAFKAC-281](https://issues.couchbase.com/browse/KAFKAC-281): Upgraded Couchbase Java SDK from 3.2.3 to [3.2.4](https://docs.couchbase.com/java-sdk/current/project-docs/sdk-release-notes.html#version-3-2-4-9-december-2021).
* [KAFKAC-282](https://issues.couchbase.com/browse/KAFKAC-282): Upgraded other dependencies to latest versions.

## [](#v4.1.4)Version 4.1.4 (16 Nov 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.1.4/couchbase-kafka-connect-couchbase-4.1.4.zip)

This version adds a new configuration options for making the connector resilient to more kinds of transient failures.

### [](#enhancements-23)Enhancements

* [KAFKAC-275](https://issues.couchbase.com/browse/KAFKAC-275): **Sink** Added the `couchbase.retry.timeout` config property. If non-zero, the connector retries write failures until the timeout expires. This is better than simply extending the KV timeout; see [the documentation](sink-configuration-options.md#couchbase.retry.timeout) for details.
* [KAFKAC-276](https://issues.couchbase.com/browse/KAFKAC-276): Upgraded Couchbase Java SDK from 3.2.0 to 3.2.3.

## [](#v4.1.3)Version 4.1.3 (19 Oct 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.1.3/couchbase-kafka-connect-couchbase-4.1.3.zip)

This version reduces the default flow control buffer size to a more reasonable value and improves DCP diagnostics.

### [](#enhancements-24)Enhancements

* [KAFKAC-271](https://issues.couchbase.com/browse/KAFKAC-271): **Source** The default flow control buffer size is now 16 MB instead of 128 MB. This makes it less likely the source connector will run out of memory under heavy load with the default heap size. The documentation now describes how the [couchbase.flow.control.buffer](https://docs.couchbase.com/kafka-connector/current/source-configuration-options.html#couchbase.flow.control.buffer) config property affects the Kafka Connect worker’s memory requirements.
* [KAFKAC-272](https://issues.couchbase.com/browse/KAFKAC-272): **Source** Upgraded DCP client from 0.36.0 to 0.37.0\. This upgrade adds a workaround for [MB-48655](https://issues.couchbase.com/browse/MB-48655) so all versions of Couchbase now correctly log DCP diagnostic messages from the source connector.

## [](#v4.1.2)Version 4.1.2 (24 Sep 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.1.2/couchbase-kafka-connect-couchbase-4.1.2.zip)

This release upgrades the jsoup library to address [CVE-2021-37714](https://github.com/jhy/jsoup/security/advisories/GHSA-m72m-mhq2-9p6c). That vulnerability does not affect the Kafka connector, since we don’t parse untrusted XML or HTML. You can skip this version unless your goal is to pacify a vulnerability scanner.

### [](#enhancements-25)Enhancements

* [KAFKAC-269](https://issues.couchbase.com/browse/KAFKAC-269): Upgraded the jsoup library from 1.13.1 to 1.14.2

## [](#v4.1.1)Version 4.1.1 (19 Aug 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.1.1/couchbase-kafka-connect-couchbase-4.1.1.zip)

This release makes the Source connector compatible with Couchbase Server 7.0.2.

If you are currently using an earlier 4.x version of the connector, please upgrade to 4.1.1 or later before upgrading Couchbase Server beyond 7.0.1.

### [](#enhancements-26)Enhancements

* [KAFKAC-266](https://issues.couchbase.com/browse/KAFKAC-266): **Source** Upgraded DCP client from 0.35.0 to 0.36.0 for compatibility with Couchbase Server 7.0.2.

## [](#v4.1.0)Version 4.1.0 (22 July 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.1.0/couchbase-kafka-connect-couchbase-4.1.0.zip)

This release stabilizes the configuration options for working with Couchbase 7 Scopes and Collections. All previously "uncommitted" options are promoted to "committed" status.

There’s also a new `SinkHandler` extension point, and bug fixes for the Subdocument and N1QL modes of operation.

### [](#breaking-changes-2)Breaking Changes

* Apache Kafka 2.4.0 is now the minimum required version. For Confluent Platform users, this corresponds to Confluent version 5.4.0.

### [](#enhancements-27)Enhancements

* The config options for working with Couchbase 7 Scopes and Collections are now part of the "committed" API.
* All other "uncommitted" config options are promoted to "committed" status as well.
* [KAFKAC-257](https://issues.couchbase.com/browse/KAFKAC-257): **Sink** The connector’s behavior is now completely customizable by implementing the `SinkHandler` interface. The new [couchbase.sink.handler](sink-configuration-options.md#couchbase.sink.handler) config option specifies the class to use. See the [custom extensions example code](https://github.com/couchbase/kafka-connect-couchbase/tree/master/examples/custom-extensions) to see how to implement your own handler.

> [!NOTE]
> The [couchbase.document.mode](sink-configuration-options.md#couchbase.document.mode) config option is now **DEPRECATED**. Instead, please use [couchbase.sink.handler](sink-configuration-options.md#couchbase.sink.handler) to specify one of the built-in handler classes.

* [KAFKAC-263](https://issues.couchbase.com/browse/KAFKAC-263): **Source** Upgraded DCP client from 0.34.0 to 0.35.0.
* [KAFKAC-258](https://issues.couchbase.com/browse/KAFKAC-258): **Sink** Upgraded Couchbase Java SDK from 3.1.3 to 3.2.0.

### [](#bug-fixes-9)Bug Fixes

* [KAFKAC-261](https://issues.couchbase.com/browse/KAFKAC-261): **Sink** A connector configured to use SUBDOCUMENT mode with an operation of `ARRAY_PREPEND` or `ARRAY_PREPEND` could mistakenly ignore updates if Kafka records targeting the same document arrive in rapid succession. This is now fixed.
* [KAFKAC-262](https://issues.couchbase.com/browse/KAFKAC-262): **Sink** A connector configured to use N1QL mode could mistakenly ignore updates if Kafka records targeting the same document(s) arrive in rapid succession. This is now fixed.

## [](#v4.0.6)Version 4.0.6 (20 April 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.0.6/couchbase-kafka-connect-couchbase-4.0.6.zip)

This release adds new Sink configuration options, and addresses a long-standing issue that caused the Source connector to fail when a rollback occurred in Couchbase.

### [](#enhancements-28)Enhancements

* [KAFKAC-250](https://issues.couchbase.com/browse/KAFKAC-250): **Sink** You can now [configure Couchbase Java SDK Settings](sink-configuration-options.md#couchbase.env) in the connector config file. This includes KV timeout durations, Response Time Observability settings, and lots more.
* [KAFKAC-251](https://issues.couchbase.com/browse/KAFKAC-251): **Source** Upgraded DCP client from 0.33.0 to 0.34.0.

### [](#bug-fixes-10)Bug Fixes

* [KAFKAC-211](https://issues.couchbase.com/browse/KAFKAC-211): **Source** A rollback in Couchbase no longer causes the connector to fail.

## [](#v4.0.5)Version 4.0.5 (16 March 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.0.5/couchbase-kafka-connect-couchbase-4.0.5.zip)

This release improves diagnostic logging and simplifies Couchbase Capella configuration.

### [](#enhancements-29)Enhancements

* [KAFKAC-234](https://issues.couchbase.com/browse/KAFKAC-234): The Couchbase root CA certificate can now be read directly from a PEM file; it’s no longer necessary to add it to a Java keystore first. The new `couchbase.trust.certificate.path` config property points to the PEM file.
* [KAFKAC-242](https://issues.couchbase.com/browse/KAFKAC-242): **Source** When the new `couchbase.log.document.lifecycle` config property is set to true, the connector writes detailed log entries as each document flows through the connector.
* [KAFKAC-245](https://issues.couchbase.com/browse/KAFKAC-245): **Sink** Upgraded Couchbase client from 3.1.2 to [3.1.3](https://docs.couchbase.com/java-sdk/3.1/project-docs/sdk-release-notes.html#version-3-1-3-2-march-2021).
* [KAFKAC-246](https://issues.couchbase.com/browse/KAFKAC-246): **Source** Upgraded DCP client from 0.32.0 to 0.33.0\. OBSERVE\_SEQNO events are now logged at TRACE level instead of DEBUG.

## [](#v4.0.4)Version 4.0.4 (17 February 2021)

[Download](https://packages.couchbase.com/clients/kafka/4.0.4/couchbase-kafka-connect-couchbase-4.0.4.zip)

This release adds uncommitted support for client certificate authentication (mTLS), adds hostname verification for secure DCP connections, and improves the stability of the connector.

### [](#enhancements-30)Enhancements

* [KAFKAC-241](https://issues.couchbase.com/browse/KAFKAC-241): When secure connections are enabled, it is now possible to authenticate with Couchbase using an X.509 certificate instead of a username & password. See [couchbase.client.certificate.path](https://docs.couchbase.com/kafka-connector/4.0/source-configuration-options.html#couchbase.client.certificate.path)and [couchbase.client.certificate.password](https://docs.couchbase.com/kafka-connector/4.0/source-configuration-options.html#couchbase.client.certificate.password)for details. (This feature is added as "uncommitted", meaning it may change without notice.)
* [KAFKAC-238](https://issues.couchbase.com/browse/KAFKAC-238): **Sink** Upgraded Couchbase client from 3.0.9 to 3.1.2.
* [KAFKAC-239](https://issues.couchbase.com/browse/KAFKAC-239): **Source** Upgraded DCP client from 0.31.0 to 0.32.0\. Previously, TLS hostname verification was done only for the Couchbase Java client connection; now the DCP client connection is verified as well. If for some reason you need to disable TLS hostname verification, this is now possible by setting the [couchbase.enable.hostname.verification](https://docs.couchbase.com/kafka-connector/4.0/source-configuration-options.html#couchbase.enable.hostname.verification) config property to `false`.

### [](#bug-fixes-11)Bug Fixes

* [JDCP-183](https://issues.couchbase.com/browse/JDCP-183): If an invalid stream offset is detected, the connector will now fail fast instead of potentially corrupting the saved checkpoint.
* [JDCP-184](https://issues.couchbase.com/browse/JDCP-184): Resolved an issue that could cause a flow control deadlock when streaming from a subset of a bucket’s collections or scopes.

## [](#v4.0.3)Version 4.0.3

Not released.

## [](#v4.0.2)Version 4.0.2 (17 November 2020)

[Download](https://packages.couchbase.com/clients/kafka/4.0.2/couchbase-kafka-connect-couchbase-4.0.2.zip)

In this release, the connector publishes metrics via JMX to facilitate monitoring.

### [](#enhancements-31)Enhancements

* [KAFKAC-152](https://issues.couchbase.com/browse/KAFKAC-152): **Documentation** \- Added a "Monitoring" page which refers users to the Kafka Connect framework documentation for monitoring connectors via JMX.
* [KAFKAC-232](https://issues.couchbase.com/browse/KAFKAC-232): **Source** \- Metrics specific to the Couchbase source connector are now exposed via JMX under the `kafka.connect.couchbase` domain.
* [KAFKAC-110](https://issues.couchbase.com/browse/KAFKAC-110): **Source** \- Added a gauge that reports the Couchbase connection status.
* [KAFKAC-231](https://issues.couchbase.com/browse/KAFKAC-231): **Source** \- Upgrade DCP client from 0.30.0 to 0.31.0

## [](#v4.0.1)Version 4.0.1 (20 October 2020)

[Download](https://packages.couchbase.com/clients/kafka/4.0.1/couchbase-kafka-connect-couchbase-4.0.1.zip)

This release improves compatibility with Couchbase Capella, and exposes extended attributes (XATTRS) to custom components.

### [](#enhancements-32)Enhancements

* [KAFKAC-227](https://issues.couchbase.com/browse/KAFKAC-227): **Source** \- Added config property `couchbase.xattrs` (boolean, defaults to false). If set to true, a custom `Filter` or `SourceHandler` may inspect a document’s extended attributes by calling `DocumentEvent.xattrs()`.
* [KAFKAC-226](https://issues.couchbase.com/browse/KAFKAC-226): Renamed the ZIP archive from `couchbaseinc-kafka-connect-couchbase` to `couchbase-kafka-connect-couchbase` (removed the "inc" from "couchbaseinc"). This made it easier to publish the connector on [Confluent Hub](https://www.confluent.io/hub/couchbase/kafka-connect-couchbase).
* [KAFKAC-228](https://issues.couchbase.com/browse/KAFKAC-228): Upgraded the Couchbase Java SDK from 3.0.6 to 3.0.9\. Bootstrap performance is improved when specifying custom ports, and the connector no longer logs spurious warnings about being unable to fetch collections manifests.
* [KAFKAC-229](https://issues.couchbase.com/browse/KAFKAC-229): Upgraded the DCP client from 0.29.0 to 0.30.0, adding support for XATTRs.

### [](#bug-fixes-12)Bug Fixes

* [KAFKAC-225](https://issues.couchbase.com/browse/KAFKAC-225): Fixed a regression in version 4.0.0 that broke alternate address resolution. The connector now handles DNS SRV and alternate addresses correctly, and can connect to Couchbase Capella or other network environments that use alternate addresses.

## [](#v4.0.0)Version 4.0.0 (18 August 2020)

[Download](https://packages.couchbase.com/clients/kafka/4.0.0/couchbaseinc-kafka-connect-couchbase-4.0.0.zip)

Version 4.0 is a major update that changes how you configure and extend the connector. If you are upgrading from a previous version of the connector, be sure to read the [Migration Guide](migration.md) which will help with the upgrade process.

The leap to 4.0 brings many new features, most notably:

* Enhanced durability options (requires Couchbase 6.5)
* Better workload distribution
* More flexible API for extensions
* Option to omit document contents
* Support for Couchbase collections and scopes (planned for Couchbase 7.0)

The notes below describe these features, and more.

> [!WARNING]
> The new configuration properties related to Couchbase scopes and collections are "uncommitted" and may change without notice in a patch release.

### [](#enhancements-33)Enhancements

> Complete list of changes since version 3.4.8 

* [KAFKAC-192](https://issues.couchbase.com/browse/KAFKAC-192): Renamed the connector config properties to follow the standard Kafka naming convention ("lowercase.with.dots.between.words"). See the [Migration Guide](migration.md) for a comprehensive list of changes, and a shell script that can help upgrade your 3.x config files to use the new property names.
* [KAFKAC-157](https://issues.couchbase.com/browse/KAFKAC-157): The connector is now packaged as a Confluent Hub component. Confluent Platform users can easily install the connector using the `confluent-hub install` command. The [Quickstart Guide](quickstart.md) has been updated to show how Apache Kafka users can install the connector.
* [KAFKAC-167](https://issues.couchbase.com/browse/KAFKAC-167): You can now specify custom ports in the list of Couchbase seed nodes. If you specify a port, it must be the port of the Key/Value service (which defaults to 11210 for unencrypted connections).
* [KAFKAC-207](https://issues.couchbase.com/browse/KAFKAC-207): **Sink** \- You can now specify an "enhanced durability" requirement with the new `couchbase.durability` config property. Enhanced durability requires Couchbase Server 6.5 or later.
* [KAFKAC-197](https://issues.couchbase.com/browse/KAFKAC-197): **Sink** \- Added config property `couchbase.topic.to.collection` which maps Kafka topics to Couchbase collections. Added config property `couchbase.default.collection` which is used when a message’s topic is not present in the map.
* [KAFKAC-209](https://issues.couchbase.com/browse/KAFKAC-209): **Source** \- The connector now evenly distributes the workload among all tasks, instead of trying to minimize the total number of Couchbase connections.
* [KAFKAC-177](https://issues.couchbase.com/browse/KAFKAC-177): **Source** \- The example config files now use `RawJsonSourceHandler` and publish Kafka messages whose contents are the same as the Couchbase documents.
* [KAFKAC-212](https://issues.couchbase.com/browse/KAFKAC-212): **Source** \- If you don’t care about the content of the Couchbase document, you can set the new `couchbase.no.value` config property to `true`, and the connector will omit the document content from Kafka messages.
* [KAFKAC-194](https://issues.couchbase.com/browse/KAFKAC-194): **Source** \- A custom `SourceHandler` can now set headers on the Kafka record.
* [KAFKAC-223](https://issues.couchbase.com/browse/KAFKAC-223): **Source** \- The connector is now more responsive to "pause" requests.
* [KAFKAC-220](https://issues.couchbase.com/browse/KAFKAC-220): **Source** \- Custom `Filter` and `SourceHandler` components can now access connector configuration properties. These interfaces now have an `init(Map<String, String>)` method. The connector config is passed to this method when the component is created.
* [KAFKAC-222](https://issues.couchbase.com/browse/KAFKAC-222): The `custom-extensions` example project now includes a `CustomFilter` class that demonstrates how to read properties from the connector config. This example filter accepts or rejects documents based on a field of the document. The target field and the list of acceptable values are both configurable.
* [KAFKAC-196](https://issues.couchbase.com/browse/KAFKAC-196): **Source** \- Added `couchbase.scope` and `couchbase.collection` config properties that let you stream from a specific scope or set of collections.
* [KAFKAC-195](https://issues.couchbase.com/browse/KAFKAC-195): **Source** \- Modified the `couchbase.topic` config property to be a format string that supports `${bucket}`, `${scope}`, and `${collection}` placeholders. This makes it easy to publish to different Kafka topics depending on the Couchbase document’s parent collection. The default value is `${bucket}.${scope}.${collection}`.
* [KAFKAC-171](https://issues.couchbase.com/browse/KAFKAC-171): The `couchbase.password` config property (previously called `connection.password`) no longer defaults to an empty string.
* [KAFKAC-175](https://issues.couchbase.com/browse/KAFKAC-175): APIs deprecated in version 3.x have been removed.
* Upgraded Kafka Connect API from 1.0.2 to 2.5.0.
* Upgraded Couchbase client from 2.7.13 to 3.0.6.
* Upgraded DCP client from 0.26.0 to 0.29.0.

### [](#bug-fixes-13)Bug Fixes

> Complete list of changes since version 3.4.8 

* [KAFKAC-169](https://issues.couchbase.com/browse/KAFKAC-169): **Sink** \- If two Kafka messages with the same key arrive in rapid succession, it’s no longer theoretically possible for them to be written to Couchbase in the wrong order.

### [](#changes-since-4-0-0-dp-3)Changes since 4.0.0-dp.3

* [KAFKAC-220](https://issues.couchbase.com/browse/KAFKAC-220): **Source** \- Custom `Filter` and `SourceHandler` components can now access connector configuration properties. These interfaces now have an `init(Map<String, String>)` method. The connector config is passed to this method when the component is created.
* [KAFKAC-222](https://issues.couchbase.com/browse/KAFKAC-222): The `custom-extensions` example project now includes a `CustomFilter` class that demonstrates how to read properties from the connector config. This example filter accepts or rejects documents based on a field of the document. The target field and the list of acceptable values are both configurable.

## [](#v4.0.0-dp.3)Version 4.0.0-dp.3 (21 July 2020)

[Download](https://packages.couchbase.com/clients/kafka/4.0.0-dp.3/couchbaseinc-kafka-connect-couchbase-4.0.0-dp.3.zip)

In this developer preview, both the Sink and Source connector now support Couchbase collections. This preview also brings a handful of fixes and new features, including support for enhanced durability, and optionally omitting document contents.

> [!NOTE]
> The new features in this pre-release version should be considered "volatile" and may change before the 4.0.0 GA release.

### [](#enhancements-34)Enhancements

* [KAFKAC-197](https://issues.couchbase.com/browse/KAFKAC-197): **Sink** \- Added config property `couchbase.topic.to.collection` which maps Kafka topics to Couchbase collections. Added config property `couchbase.default.collection` which is used when a message’s topic is not present in the map.
* [KAFKAC-207](https://issues.couchbase.com/browse/KAFKAC-207): **Sink** \- You can now specify an "enhanced durability" requirement with the new `couchbase.durability` config property. Enhanced durability requires Couchbase Server 6.5 or later.
* [KAFKAC-206](https://issues.couchbase.com/browse/KAFKAC-206): **Source** \- Config property `couchbase.connector.name.in.offsets` now defaults to false again. This property doesn’t do anything useful, and should only be set to `true` if you previously had `compat.connector_name_in_offsets` set to `true`.
* [KAFKAC-177](https://issues.couchbase.com/browse/KAFKAC-177): **Source** \- The example config files now use `RawJsonSourceHandler` and publish Kafka messages whose contents are the same as the Couchbase documents.
* [KAFKAC-209](https://issues.couchbase.com/browse/KAFKAC-209): **Source** \- The connector now evenly distributes the workload among all tasks, instead of trying to minimize the total number of Couchbase connections.
* [KAFKAC-212](https://issues.couchbase.com/browse/KAFKAC-212): **Source** \- If you don’t care about the content of the Couchbase document, you can set the new `couchbase.no.value` config property to `true`, and the connector will omit the document content from Kafka messages.
* [KAFKAC-205](https://issues.couchbase.com/browse/KAFKAC-205): Removed the unused `couchbase.force.ipv4` config property.

### [](#bug-fixes-14)Bug Fixes

* [KAFKAC-169](https://issues.couchbase.com/browse/KAFKAC-169): **Sink** \- If two Kafka messages with the same key arrive in rapid succession, it’s no longer theoretically possible for them to be written to Couchbase in the wrong order.
* [KAFKAC-214](https://issues.couchbase.com/browse/KAFKAC-214): **Sink** \- The Couchbase Java SDK has been updated from 3.0.5 to 3.0.6\. As a result, setting `couchbase.document.expiration` to longer than 30 days now works correctly instead of causing immediate expiration. (This was a regression in 4.0.0-dp.1.)
* [KAFKAC-203](https://issues.couchbase.com/browse/KAFKAC-203): **Source** \- The 3.x → 4.0 migration script now properly converts the old `couchbase.flow_control_buffer` property to the new name: `couchbase.flow.control.buffer.size`.
* [KAFKAC-204](https://issues.couchbase.com/browse/KAFKAC-204): **Source** \- Fixed the invalid value for `couchbase.bootstrap.timeout` in the `quickstart-couchbase-source.json` example config file.

## [](#v4.0.0-dp.1)Version 4.0.0-dp.1 (17 June 2020)

[Download](https://packages.couchbase.com/clients/kafka/4.0.0-dp.1/couchbaseinc-kafka-connect-couchbase-4.0.0-dp.1.zip)

This developer preview version offers a sneak peek at some features coming in version 4.0.0 of the Couchbase Kafka connector, including support for Couchbase Collections and Scopes.

Version 4.0 is a major update that changes how you configure and extend the connector. If you are upgrading from a previous version of the connector, be sure to read the [Migration Guide](migration.md) which will help you with the upgrade process.

> [!NOTE]
> The new features in this pre-release version should be considered "volatile" and may change before the 4.0.0 GA release.

### [](#enhancements-35)Enhancements

* [KAFKAC-182](https://issues.couchbase.com/browse/KAFKAC-182): Upgraded Kafka Connect API from 1.0.2 to 2.5.0.
* [KAFKAC-188](https://issues.couchbase.com/browse/KAFKAC-188): Upgraded Couchbase client from 2.7.13 to 3.0.5.
* [KAFKAC-189](https://issues.couchbase.com/browse/KAFKAC-189): Upgraded DCP client from 0.26.0 to 0.28.0.
* [KAFKAC-192](https://issues.couchbase.com/browse/KAFKAC-192): Renamed the connector config properties to follow the standard Kafka naming convention ("lowercase.with.dots.between.words"). See the [Migration Guide](migration.md) for a comprehensive list of changes, and a shell script that can help upgrade your 3.x config files to use the new property names.
* [KAFKAC-196](https://issues.couchbase.com/browse/KAFKAC-196): Source: Added `couchbase.scope` and `couchbase.collection` config properties that let you stream from a specific scope or set of collections.
* [KAFKAC-195](https://issues.couchbase.com/browse/KAFKAC-195): Source: Modified the `couchbase.topic` config property to be a format string that supports `${bucket}`, `${scope}`, and `${collection}` placeholders. This makes it easy to publish to different Kafka topics depending on the Couchbase document’s parent collection. The default value is `${bucket}.${scope}.${collection}`.
* [KAFKAC-194](https://issues.couchbase.com/browse/KAFKAC-194): Source: A custom `SourceHandler` can now set headers on the Kafka record.
* [KAFKAC-157](https://issues.couchbase.com/browse/KAFKAC-157): The connector is now packaged as a Confluent Hub component. Confluent Platform users can easily install the connector using the `confluent-hub install` command. The [Quickstart Guide](quickstart.md) has been updated to show how Apache Kafka users can install the connector.
* [KAFKAC-167](https://issues.couchbase.com/browse/KAFKAC-167): You can now specify custom ports in the list of Couchbase seed nodes. If you specify a port, it must be the port of the Key/Value service (which defaults to 11210 for unencrypted connections).
* [KAFKAC-171](https://issues.couchbase.com/browse/KAFKAC-171): The `couchbase.password` config property (previously called `connection.password`) no longer defaults to an empty string.
* [KAFKAC-173](https://issues.couchbase.com/browse/KAFKAC-173): The `couchbase.connector.name.in.offsets` config property (previously called `compat.connector_name_in_offsets`) now defaults to `true`.
* [KAFKAC-175](https://issues.couchbase.com/browse/KAFKAC-175): APIs deprecated in version 3.x have been removed.

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).

**Parent topic:** [Kafka Connector](index.md)

**Previous topic:** [Couchbase Sample with Kafka Streams](streams-sample.md)