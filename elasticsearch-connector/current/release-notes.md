---
title: Release Notes
editUrl: https://github.com/couchbase/docs-elastic-search/edit/main/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:elasticsearch-connector::release-notes.adoc[]
---

[View original HTML](/elasticsearch-connector/current/release-notes.html)

# Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Elasticsearch Connector. 

## [](#installation)Installation

Scroll down to the version you want, then click the "Download" link to get the full connector distribution. Refer to [Getting Started](getting-started.md) for detailed installation instructions.

## [](#v4.4.14)Version 4.4.14 (2025-10-23)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.14/couchbase-elasticsearch-connector-4.4.14.zip)

This version adds additional tags to connector metrics, and updates dependencies.

> [!WARNING]
> Watch out for a change to the network detection heuristic. If the connector is unable to connect to Couchbase Server after the upgrade, you might need to specify `network = 'default'` in the `[couchbase]` section of your connector config.

### [](#behavioral-changes)Behavioral Changes

* [JVMCBC-1660](https://jira.issues.couchbase.com/browse/JVMCBC-1660): The `auto` network selection heuristic has been changed to fall back to the `external` network if there is no exact address match and the `external` network is present.  
Previously, if there was no exact match between an address in the connection string and an address in the cluster topology reported by the server, the connector would select the `default` network. Now, if there is no match and an `external` network is present, the connector selects the `external` network.  
> [!TIP]  
> If this change causes the connector to select the incorrect network for your deployment (you’ll know because the connector will be unable to connect to the Couchbase Server cluster), specify `network = 'default'` in the `[couchbase]` section of your connector config to force the connector to use the same network as before.

### [](#enhancements)Enhancements

* [CBES-337](https://jira.issues.couchbase.com/browse/CBES-337): Connector metrics are now tagged with "bucket" and "clusterUuid".
* [CBES-338](https://jira.issues.couchbase.com/browse/CBES-338): Upgraded Couchbase Java SDK from `3.8.0` to `3.9.2`.
* [CBES-339](https://jira.issues.couchbase.com/browse/CBES-339): Upgraded DCP client from `0.54.0` to `0.56.0`.

## [](#v4.4.13)Version 4.4.13 (2025-04-22)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.13/couchbase-elasticsearch-connector-4.4.13.zip)

This maintenance release fixes an issue with AWS IRSA authentication in Kubernetes, and upgrades dependency versions.

### [](#enhancements-2)Enhancements

* [CBES-332](https://jira.issues.couchbase.com/browse/CBES-332): Upgraded awssdk to version `2.31.2` for IRSA compatability. Thanks to [Christopher Lupo](https://github.com/clupo).
* [CBES-334](https://jira.issues.couchbase.com/browse/CBES-334): Upgraded Couchbase Java SDK from `3.7.9` to `3.8.0`.
* [CBES-335](https://jira.issues.couchbase.com/browse/CBES-335): Upgraded DCP client from `0.53.0` to `0.54.0`.

## [](#v4.4.12)Version 4.4.12 (2025-03-13)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.12/couchbase-elasticsearch-connector-4.4.12.zip)

This maintenance release adds support for AWS IRSA authentication in Kubernetes, improves the connector’s checkpoint behavior, and upgrades dependency versions.

### [](#enhancements-3)Enhancements

* [CBES-327](https://jira.issues.couchbase.com/browse/CBES-327): Added support for AWS IRSA authentication in Kubernetes. Thanks to [Christopher Lupo](https://github.com/clupo).
* [CBES-326](https://jira.issues.couchbase.com/browse/CBES-326): Added a `defaultCheckpoint` property to the `[couchbase]` section of the connector config file. This new property controls where in history the connector starts from if there is no replication checkpoint for a partition.  
Possible values:

  * `'ZERO'` — Replicate past and future changes. This is the default value.
  * `'NOW'` — Replicate only changes that happen after the connector starts.
* [CBES-331](https://jira.issues.couchbase.com/browse/CBES-331): All absent replication checkpoints are now immediately created when the connector starts up. This improves on the previous behavior, where the connector would not save a checkpoint for a partition until a document was received from that partition.
* [CBES-328](https://jira.issues.couchbase.com/browse/CBES-328): Upgraded Couchbase Java SDK from `3.7.6` to `3.7.9`.
* [CBES-329](https://jira.issues.couchbase.com/browse/CBES-329): Upgraded DCP client from `0.52.0` to `0.53.0`.
* [CBES-330](https://jira.issues.couchbase.com/browse/CBES-330): Upgraded Elasticsearch client from `8.14.3` to `8.17.3`. Upgraded OpenSearch client from `2.12.0` to `2.22.0`.

## [](#v4.4.11)Version 4.4.11 (2024-12-17)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.11/couchbase-elasticsearch-connector-4.4.11.zip)

This maintenance release updates the Couchbase Java SDK (and a few other dependencies) to the most recent versions.

Elasticsearch 8.16 and OpenSearch 2.18 join the list of supported versions.

### [](#enhancements-4)Enhancements

* [CBES-320](https://jira.issues.couchbase.com/browse/CBES-320): Support connecting to a Kubernetes API server that requires TLS 1.3\. (Upgrade `io.fabric8:kubernetes-client` from 5.11.2 to 7.0.0.)
* [CBES-321](https://jira.issues.couchbase.com/browse/CBES-321): Upgrade Couchbase Java Client from 3.7.5 to 3.7.6
* [CBES-324](https://jira.issues.couchbase.com/browse/CBES-324): Upgrade `ubi8/openjdk-17-runtime` from 1.20 to 1.21

## [](#v4.4.10)Version 4.4.10 (2024-11-12)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.10/couchbase-elasticsearch-connector-4.4.10.zip)

This maintenance release updates the Couchbase Java SDK to the most recent version.

### [](#enhancements-5)Enhancements

* [CBES-318](https://jira.issues.couchbase.com/browse/CBES-318): Upgrade Couchbase Java Client from 3.7.1 to 3.7.5
* [CBES-319](https://jira.issues.couchbase.com/browse/CBES-319): Upgrade Java DCP client from 0.51.0 to 0.52.0

### [](#bug-fixes)Bug Fixes

* [CBES-315](https://jira.issues.couchbase.com/browse/CBES-315): Resolved an issue that caused Kubernetes Native Integration to fail if log level is TRACE.

## [](#v4.4.9)Version 4.4.9 (2024-07-25)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.9/couchbase-elasticsearch-connector-4.4.9.zip)

This maintenance release updates the Couchbase Java SDK to the most recent version.

Added Elasticsearch 8.14, OpenSearch 2.15, and Consul 1.19.1 to the compatibility matrix as supported versions.

### [](#enhancements-6)Enhancements

* [CBES-311](https://issues.couchbase.com/browse/CBES-311): The connector now includes the `co.elastic.logging:log4j2-ecs-layout` library as a convenience for users who want to configure Log4j2 to use this layout.
* [CBES-314](https://issues.couchbase.com/browse/CBES-314): Upgrade Couchbase Java SDK from `3.6.1` to `3.7.1`.
* [CBES-310](https://issues.couchbase.com/browse/CBES-310): Upgrade Couchbase DCP client from `0.50.0` to `0.51.0`. Notably:

  * [JDCP-245](https://issues.couchbase.com/browse/JDCP-245): The DCP client now sets the `ACTIVE_VB_ONLY` flag when opening a stream. This prevents the connector from inadvertently streaming from a replica partition, which could cause problems with some versions of Couchbase Server.

## [](#v4.4.8)Version 4.4.8 (2024-04-16)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.8/couchbase-elasticsearch-connector-4.4.8.zip)

This maintenance release updates the Couchbase Java SDK to the most recent version.

### [](#enhancements-7)Enhancements

* [CBES-308](https://issues.couchbase.com/browse/CBES-308): Upgrade Couchbase Java SDK from `3.5.2` to `3.6.1`.  
Notably:

  * [JVMCBC-1499](https://issues.couchbase.com/browse/JVMCBC-1499)Disabled DNS SRV caching. The connector now responds quicker to DNS changes in dynamic environments like Kubernetes.

## [](#v4.4.7)Version 4.4.7 (2024-01-24)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.7/couchbase-elasticsearch-connector-4.4.7.zip)

This maintenance release improves the robustness of the connector in certain conditions.

Added Elasticsearch 8.12, OpenSearch 2.11, and Consul 1.17.1 to the compatibility matrix as supported versions.

### [](#enhancements-8)Enhancements

* [CBES-305](https://issues.couchbase.com/browse/CBES-305): Upgrade Couchbase Java SDK from `3.4.6` to `3.5.2`.
* [CBES-306](https://issues.couchbase.com/browse/CBES-306): Upgrade Couchbase DCP client from `0.46.0` to `0.48.0`.

### [](#bug-fixes-2)Bug Fixes

* [JDCP-239](https://issues.couchbase.com/browse/JDCP-239): Improved reliability of initial startup during a Couchbase Server cluster rebalance, or before a newly-created bucket is ready.
* [JDCP-240](https://issues.couchbase.com/browse/JDCP-240): When a partition is not active on any Couchbase Server node, the checkpoint management "catch up" command now waits for the partition to become active somewhere, instead of clearing the partition’s checkpoint.
* [JDCP-241](https://issues.couchbase.com/browse/JDCP-241): Improved handling of an edge case that could cause the connector to stop streaming for a partition. If a DCP socket connection is lost after receiving a snapshot marker for a partition and before receiving the first item in the snapshot, the connector now recovers instead of failing to resume streaming for that partition.

## [](#v4.4.6)Version 4.4.6 (2023-05-17)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.6/couchbase-elasticsearch-connector-4.4.6.zip)

If the connector is stopped for an extended period of time, it can now resume from where it left off, without having to roll back to zero. This behavior requires Couchbase Server 7.2 or later.

Added Elasticsearch 8.7 and OpenSearch 2.7 to the compatibility matrix as supported versions.

### [](#enhancements-9)Enhancements

* [CBES-297](https://issues.couchbase.com/browse/CBES-297): When resuming from an old checkpoint (where the connector’s sequence number is lower than Couchbase Server’s purge sequence number), the connector no longer rolls back to zero. This behavior requires Couchbase Server 7.2 or later.
* [CBES-300](https://issues.couchbase.com/browse/CBES-300): Upgrade Couchbase Java SDK from `3.4.4` to `3.4.6`.
* [CBES-301](https://issues.couchbase.com/browse/CBES-301): Upgrade Couchbase DCP client from `0.45.0` to `0.46.0`.

### [](#bug-fixes-3)Bug Fixes

* [CBES-293](https://issues.couchbase.com/browse/CBES-293): The connector now honors the `io.enableDnsSrv` client setting. Previously, it would always attempt DNS SRV resolution on an eligible Couchbase Server hostname, regardless of whether DNS SRV was disabled via the client setting. This typically has no functional impact, but the old behavior was generating noise in the logs.

## [](#v4.4.5)Version 4.4.5 (2023-03-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.5/couchbase-elasticsearch-connector-4.4.5.zip)

This version adds experimental support for Elastic Cloud, OpenSearch, and Amazon OpenSearch Service. If you’d like to share feedback on these features, please post in the [Elasticsearch category](https://forums.couchbase.com/c/elasticsearch-connector/36) on the Couchbase Forum.

### [](#enhancements-10)Enhancements

* [CBES-286](https://issues.couchbase.com/browse/CBES-286): Add [experimental support for Elastic Cloud](configuration.md#elastic-cloud).
* [CBES-285](https://issues.couchbase.com/browse/CBES-285): Add experimental support for OpenSearch. No special configuration is required; the connector automatically detects you’re using OpenSearch instead of Elasticsearch.
* [CBES-243](https://issues.couchbase.com/browse/CBES-243): Add [experimental support for Amazon OpenSearch Service](configuration.md#amazon-opensearch-service).
* [CBES-287](https://issues.couchbase.com/browse/CBES-287): When connecting to Elasticsearch/OpenSearch with TLS, the well-known Certificate Authority (CA) certificates from the JVM’s `cacerts` trust store are now trusted by default, unless you specify different CA certificates to trust.
* [CBES-288](https://issues.couchbase.com/browse/CBES-288): Add Consul 1.15.1 to the compatibility matrix as a supported version.
* [CBES-290](https://issues.couchbase.com/browse/CBES-290): Upgrade Couchbase Java SDK from `3.4.3` to `3.4.4`.
* [CBES-291](https://issues.couchbase.com/browse/CBES-291): Upgrade Couchbase DCP client from `0.44.0` to `0.45.0`.

## [](#v4.4.4)Version 4.4.4 (2023-02-17)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.4/couchbase-elasticsearch-connector-4.4.4.zip)

This maintenance release upgrades various dependencies, and adds Elasticsearch 8.6 to the compatibility matrix as a supported version.

### [](#enhancements-11)Enhancements

* [CBES-283](https://issues.couchbase.com/browse/CBES-283): Upgrade Couchbase Java SDK from `3.4.1` to `3.4.3`.
* [CBES-284](https://issues.couchbase.com/browse/CBES-284): Upgrade Couchbase DCP client from `0.43.0` to `0.44.0`.

## [](#v4.4.3)Version 4.4.3 (2022-12-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.3/couchbase-elasticsearch-connector-4.4.3.zip)

### [](#enhancements-12)Enhancements

* [CBES-278](https://issues.couchbase.com/browse/CBES-278): Elasticsearch 8.5 and Consul 1.14.3 are now supported.
* [CBES-276](https://issues.couchbase.com/browse/CBES-276): Upgrade Couchbase DCP client from `0.42.0` to `0.43.0`.
* [CBES-277](https://issues.couchbase.com/browse/CBES-277): Upgrade Couchbase Java SDK from `3.3.4` to `3.4.1`.

### [](#bug-fixes-4)Bug Fixes

* [CBES-281](https://issues.couchbase.com/browse/CBES-281): A regression in version `4.4.0` caused the connector to omit null-valued document fields when writing to Elasticsearch. Null-valued fields are now replicated correctly again.
* [JDCP-232](https://issues.couchbase.com/browse/JDCP-232): Fixed a race condition that sometimes caused the connector to fail on startup with the message: `java.lang.IllegalStateException: Tried to add duplicate channel`.

## [](#v4.4.2)Version 4.4.2 (2022-10-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.2/couchbase-elasticsearch-connector-4.4.2.zip)

You can now authenticate with Couchbase as an LDAP user, as long as secure connections are enabled.

### [](#enhancements-13)Enhancements

* [JDCP-224](https://issues.couchbase.com/browse/JDCP-224): Use SASL mechanism `PLAIN` when authenticating with Couchbase on a secure connection. `PLAIN` is the fastest mechanism, and the only one that works with LDAP users.
* [JDCP-217](https://issues.couchbase.com/browse/JDCP-217): Support Couchbase clusters that advertise only TLS ports.
* [CBES-267](https://issues.couchbase.com/browse/CBES-267): Include date and time zone in log message timestamps.
* [CBES-268](https://issues.couchbase.com/browse/CBES-268): Increase the DCP connection handshake timeout from 3 seconds to 12 seconds, allowing more time to connect to a remote/overloaded cluster.
* [CBES-275](https://issues.couchbase.com/browse/CBES-275): Upgrade Couchbase DCP client from `0.41.0` to `0.42.0`.
* Upgraded `commons-text` from `1.9` to `1.10.0`. Please see [our official response to CVE-2022-42889 (also known as Text4Shell)](https://www.couchbase.com/blog/security-vulnerability-text4shell/). In brief, no version of the Elasticsearch connector is vulnerable.

## [](#v4.4.1)Version 4.4.1 (2022-09-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.1/couchbase-elasticsearch-connector-4.4.1.zip)

Adds support for recent versions of HashiCorp Consul, and improves the lifecycle of the connector’s Consul service definitions.

Elasticsearch 8.4 joins the list of supported versions.

### [](#behavioral-changes-2)Behavioral Changes

* [CBES-240](https://issues.couchbase.com/browse/CBES-240): **Autonomous Operations Mode** When the connector shuts down gracefully in response to an interrupt signal, it now deregisters its Consul service definition before exiting. For ungraceful shutdowns, Consul automatically deregisters a service definition that remains in "critical" state for 7 days.  
> [!TIP]  
> You can customize these behaviors in the connector’s Consul-specific configuration, specified with the command-line option:  
```shell
--consul <path/to/consul.toml>  
```

### [](#enhancements-14)Enhancements

* [CBES-237](https://issues.couchbase.com/browse/CBES-237): **Autonomous Operations Mode** HashiCorp Consul 1.13, 1.12, and 1.11 are now supported.
* [CBES-144](https://issues.couchbase.com/browse/CBES-144): **Autonomous Operations Mode** The connector now recovers from transient Consul errors that sometimes occur during leader election. When Consul returns HTTP status code 500 or 503, the connector now retries the request instead of immediately terminating.
* [CBES-262](https://issues.couchbase.com/browse/CBES-262): Elasticsearch 8.4 is now supported.
* [CBES-256](https://issues.couchbase.com/browse/CBES-256): OpenJDK 17 is now supported, and is used by the Docker image. The Dockerfile now refers to the base image by a stable minor version tag (instead of a specific patch version), which should make it easier for us to update the connector image when the base image receives security updates.
* [CBES-263](https://issues.couchbase.com/browse/CBES-263): Upgraded Couchbase Java SDK from `3.3.2` to `3.3.4`.
* [CBES-266](https://issues.couchbase.com/browse/CBES-266): Upgraded Couchbase DCP client from `0.40.0` to `0.41.0`.

## [](#v4.4.0)Version 4.4.0 (2022-08-01)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.4.0/couchbase-elasticsearch-connector-4.4.0.zip)

The connector now supports Elasticsearch 8, and it’s easier to configure the trusted Certificate Authority (CA) certificates.

### [](#breaking-changes)Breaking Changes

* The minimum required version of Elasticsearch is now `7.14.0`.
* OpenSearch and Amazon OpenSearch Service are not supported. If you’re using a previous version of the connector with OpenSearch, please remain on that version for now. We’re investigating restoring support in a future version. **UPDATE**: [Version 4.4.5 (2023-03-21)](#v4.4.5) restores support for OpenSearch and Amazon OpenSearch Service as an experimental feature.

### [](#enhancements-15)Enhancements

* [CBES-254](https://issues.couchbase.com/browse/CBES-254): Added support for Elasticsearch 8.
* [CBES-258](https://issues.couchbase.com/browse/CBES-258): When using secure connections, the connector can now read the Couchbase and Elasticsearch CA certificates from separate PEM files instead of a single Java keystore. The `[couchbase]` and `[elasticsearch]` config sections each have a new `pathToCaCertificate` property that points to the respective PEM file.
* [CBES-257](https://issues.couchbase.com/browse/CBES-257): When connecting to Couchbase Capella, it’s no longer necessary to configure the CA certificate. Just make sure not to configure the deprecated `[truststore]` config section, and make sure to leave the `pathToCaCertificate` property in the `[couchbase]` config section blank.
* [CBES-259](https://issues.couchbase.com/browse/CBES-259): Upgraded Couchbase Java SDK from `3.3.1` to `3.3.2`.

### [](#deprecations)Deprecations

* The `[truststore]` config section is deprecated, and will be removed in a future version. Instead, please use the new `pathToCaCertificate` config properties added by [CBES-258](https://issues.couchbase.com/browse/CBES-258).
* The `typeName` property in the `[elasticsearch.typeDefaults]`, `[[elasticsearch.type]]`, and `[elasticsearch.rejectionLog]` config sections is deprecated, and will be removed in a future version. Specifying this property has no effect, since the concept of document types was removed in Elasticsearch 7.

## [](#v4.3.9)Version 4.3.9 (2022-12-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.9/couchbase-elasticsearch-connector-4.3.9.zip)

This release bumps various dependency versions. There are no new features or bug fixes.

### [](#enhancements-16)Enhancements

* [CBES-279](https://issues.couchbase.com/browse/CBES-279): Upgrade the Docker base image to the latest version of `ubi8/openjdk-11-runtime`. The Dockerfile now uses a floating tag for the base image. This makes it easier to refresh the connector image when the base image is updated.
* Upgraded `commons-text` from `1.9` to `1.10.0`. Please see [our official response to CVE-2022-42889 (also known as Text4Shell)](https://www.couchbase.com/blog/security-vulnerability-text4shell/). In brief, no version of the Elasticsearch connector is vulnerable.

## [](#v4.3.8)Version 4.3.8 (2022-06-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.8/couchbase-elasticsearch-connector-4.3.8.zip)

This release bumps various dependency versions. There are no new features or bug fixes.

### [](#enhancements-17)Enhancements

* [CBES-255](https://issues.couchbase.com/browse/CBES-255): Upgrade Couchbase Java SDK from 3.3.0 to 3.3.1.
* [CBES-253](https://issues.couchbase.com/browse/CBES-253): Upgrade the Docker base image to the latest version of `ubi8/openjdk-11-runtime`.

## [](#v4.3.7)Version 4.3.7 (2022-05-17)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.7/couchbase-elasticsearch-connector-4.3.7.zip)

This release bumps various dependency versions. There are no new features or bug fixes.

### [](#enhancements-18)Enhancements

* [CBES-249](https://issues.couchbase.com/browse/CBES-249): Upgrade Couchbase Java SDK from 3.2.6 to 3.3.0.
* [CBES-252](https://issues.couchbase.com/browse/CBES-252): Upgrade `ubi8/openjdk-11-runtime` base image from 1.11-2.1648459559 to 1.12-1.1651233103.

## [](#v4.3.6)Version 4.3.6 (2022-04-19)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.6/couchbase-elasticsearch-connector-4.3.6.zip)

This release adds a new `/info` HTTP endpoint that displays information about the connector.

### [](#enhancements-19)Enhancements

* [CBES-247](https://issues.couchbase.com/browse/CBES-247): The new `/info` HTTP endpoint reports the connector version and membership in a machine-readable format.
* [CBES-248](https://issues.couchbase.com/browse/CBES-248): Upgrade Couchbase Java SDK from 3.2.4 to 3.2.6.

## [](#v4.3.5)Version 4.3.5 (2022-01-18)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.5/couchbase-elasticsearch-connector-4.3.5.zip)

This is a maintenance released focused on upgrading dependencies to the latest versions.

### [](#enhancements-20)Enhancements

* [CBES-238](https://issues.couchbase.com/browse/CBES-238): Resolved an incompatibility with Consul 1.10.
* [CBES-241](https://issues.couchbase.com/browse/CBES-241): Upgraded Log4j from 2.17.0 to 2.17.1.

> [!NOTE]
> **Regarding CVE-2021-44832:** The connector’s out-of-the-box logging configuration does not use Log4j’s JDBC appender. You may still wish to upgrade to avoid false positives from vulnerability scanners.

* [CBES-245](https://issues.couchbase.com/browse/CBES-245): Upgraded Couchbase DCP client from 0.38.0 to 0.39.0:

  * [JDCP-210](https://issues.couchbase.com/browse/JDCP-210)Authentication no longer fails when credentials have non-ASCII characters and the system default encoding is not UTF-8.
* [CBES-242](https://issues.couchbase.com/browse/CBES-242): Upgraded other dependencies to the latest versions.

## [](#v4.2.15)Version 4.2.15 (2022-01-18)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.15/couchbase-elasticsearch-connector-4.2.15.zip)

This release upgrades Log4j again (sigh).

> [!NOTE]
> **Regarding CVE-2021-44832:** The connector’s out-of-the-box logging configuration does not use Log4j’s JDBC appender. You may still wish to upgrade to avoid false positives from vulnerability scanners.

### [](#enhancements-21)Enhancements

* [CBES-241](https://issues.couchbase.com/browse/CBES-241): Upgrade Log4j from 2.17.0 to 2.17.1.

## [](#v4.3.4)Version 4.3.4 (2021-12-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.4/couchbase-elasticsearch-connector-4.3.4.zip)

This release makes it easier to [deploy the connector in Kubernetes](kubernetes.md), and upgrades Log4j from 2.15.0 to 2.17.0.

### [](#enhancements-22)Enhancements

* [CBES-232](https://issues.couchbase.com/browse/CBES-232): Upgraded Log4j from 2.15.0 to 2.17.0\. This prevents vulnerability scanners from flagging Log4j 2.15.0 as a potential security risk.

> [!NOTE]
> All versions of the connector are immune to CVE-2021-45046 and CVE-2021-45105 because the connector does not use the Thread Context Map / Mapped Diagnostic Context (MDC) feature of Log4j.

* [CBES-200](https://issues.couchbase.com/browse/CBES-200): Added basic Kubernetes integration. See the new documentation page, [Deploying in Kubernetes](kubernetes.md).
* [CBES-226](https://issues.couchbase.com/browse/CBES-226): Added a LICENSE file to the distribution archive (Apache License Version 2.0, same as before).
* [CBES-234](https://issues.couchbase.com/browse/CBES-234): Upgraded DCP client from 0.37.0 to 0.38.0 for better error messages if the Couchbase user does not have the required permissions.
* [CBES-235](https://issues.couchbase.com/browse/CBES-235): Upgraded Couchbase Java client from 3.2.0 to 3.2.4 to pick up the latest dependency versions.

## [](#v4.2.14)Version 4.2.14 (2021-12-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.14/couchbase-elasticsearch-connector-4.2.14.zip)

This release upgrades Log4j from 2.15.0 to 2.17.0.

### [](#enhancements-23)Enhancements

* [CBES-232](https://issues.couchbase.com/browse/CBES-232): Upgraded Log4j from 2.15.0 to 2.17.0\. This prevents vulnerability scanners from flagging Log4j 2.15.0 as a potential security risk.

> [!NOTE]
> All versions of the connector are immune to CVE-2021-45046 and CVE-2021-45105 because the connector does not use the Thread Context Map / Mapped Diagnostic Context (MDC) feature of Log4j.

## [](#v4.3.3)Version 4.3.3 (2021-12-10)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.3/couchbase-elasticsearch-connector-4.3.3.zip)

This release fixes a high severity vulnerability related to Log4j 2\. All users should upgrade the connector to 4.3.3 (or 4.2.13) as soon as possible.

### [](#bug-fixes-5)Bug Fixes

* [CBES-230](https://issues.couchbase.com/browse/CBES-230): Upgrade Log4j 2 from 2.14.1 to 2.15.0 to address CVE-2021-44228.

## [](#v4.2.13)Version 4.2.13 (2021-12-10)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.13/couchbase-elasticsearch-connector-4.2.13.zip)

This release fixes a high severity vulnerability related to Log4j 2\. All users should upgrade the connector to 4.2.13 (or 4.3.3 and later) as soon as possible.

### [](#bug-fixes-6)Bug Fixes

* [CBES-230](https://issues.couchbase.com/browse/CBES-230): Upgrade Log4j 2 from 2.14.1 to 2.15.0 to address CVE-2021-44228.

## [](#v4.3.2)Version 4.3.2 (2021-10-19)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.2/couchbase-elasticsearch-connector-4.3.2.zip)

This version reduces the default flow control buffer size to a more reasonable value and improves DCP diagnostics.

### [](#enhancements-24)Enhancements

* [CBES-224](https://issues.couchbase.com/browse/CBES-224): The default flow control buffer size is now 16 MB instead of 128 MB. This makes it less likely the connector will run out of memory under heavy load with the default heap size. The documentation now describes how the DCP [flowControlBuffer](https://docs.couchbase.com/elasticsearch-connector/current/configuration.html#dcp) config property affects the connector’s memory requirements.
* [CBES-223](https://issues.couchbase.com/browse/CBES-223): Upgraded DCP client from 0.36.0 to 0.37.0\. This upgrade adds a workaround for [MB-48655](https://issues.couchbase.com/browse/MB-48655) so all versions of Couchbase now correctly log DCP diagnostic messages from the connector.
* [CBES-222](https://issues.couchbase.com/browse/CBES-222): The connector no longer logs the Couchbase Server version. Prior to this change the log message always had a placeholder version of `9999.0.0` which was misleading.

## [](#v4.3.1)Version 4.3.1 (2021-08-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.1/couchbase-elasticsearch-connector-4.3.1.zip)

This release restores compatibility with Couchbase Server 7.0.2.

If you are currently using a connector version between 4.2.2 and 4.3.0 inclusive, please upgrade to 4.3.1 or later before upgrading Couchbase Server beyond 7.0.1.

### [](#enhancements-25)Enhancements

* [CBES-221](https://issues.couchbase.com/browse/CBES-221): Upgraded the DCP client from 0.35.0 to 0.36.0 for compatibility with Couchbase Server 7.0.2.

## [](#v4.3.0)Version 4.3.0 (2021-07-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.3.0/couchbase-elasticsearch-connector-4.3.0.zip)

This release stabilizes the configuration options for working with Couchbase 7 Scopes and Collections. All previously "uncommitted" options are promoted to "committed" status.

### [](#enhancements-26)Enhancements

* The config options for working with Couchbase 7 Scopes and Collections are now part of the "committed" API.
* All other "uncommitted" config options are promoted to "committed" status as well.

### [](#breaking-changes-2)Breaking Changes

* [CBES-215](https://issues.couchbase.com/browse/CBES-215): **The connector now requires Java 11 (or later).**
* [CBES-212](https://issues.couchbase.com/browse/CBES-212): **Elasticsearch 5 is no longer supported.**It still works (at least for now), but we’re no longer testing it. Please upgrade to a more recent version of Elasticsearch.
* The deprecated `cbes.backfill*` metrics have been removed. As a replacement, please use the `cbes.backlog` metric which gives ongoing insight into the connector’s performance.

## [](#v4.2.12)Version 4.2.12 (2021-07-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.12/couchbase-elasticsearch-connector-4.2.12.zip)

This release upgrades various dependencies to the latest versions and improves how permanent indexing failures are logged.

### [](#enhancements-27)Enhancements

* [CBES-213](https://issues.couchbase.com/browse/CBES-213): When logging permanent indexing failures, the connector now sanitizes the contents of the failure message to ensure sensitive information is redacted.
* [CBES-209](https://issues.couchbase.com/browse/CBES-209): Upgraded the Couchbase Java SDK from 3.1.3 to 3.2.0.
* [CBES-217](https://issues.couchbase.com/browse/CBES-217): Upgraded the DCP client from 0.34.0 to 0.35.0.
* [CBES-211](https://issues.couchbase.com/browse/CBES-211): Upgraded various dependencies to the latest versions.

## [](#v4.2.11)Version 4.2.11 (2021-05-18)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.11/couchbase-elasticsearch-connector-4.2.11.zip)

This release makes it easier for custom tools to parse config files that have environment variable placeholders.

### [](#enhancements-28)Enhancements

* [CBES-206](https://issues.couchbase.com/browse/CBES-206): Integer and boolean config properties can now be specified as strings. For example: `7` and `'7'` are now both valid for an integer property, and `true` and `'true'` are now both valid for a boolean property. This lets you use environment variable placeholders for integer and boolean properties without invalidating the TOML syntax — just enclose them in quotes, like: `'${SOME_INTEGER}'`. The connector resolves placeholders before parsing the TOML, so it doesn’t care about the invalid syntax; this change just makes it easier for other tools to parse the connector config file.

## [](#v4.2.10)Version 4.2.10 (2021-04-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.10/couchbase-elasticsearch-connector-4.2.10.zip)

This release brings minor improvements to monitoring and configurability.

### [](#enhancements-29)Enhancements

* [CBES-202](https://issues.couchbase.com/browse/CBES-202): The connector now waits until it has connected to both Couchbase and Elasticsearch before starting the HTTP server for the `/metrics` endpoint. This makes it more useful as a "readiness" probe.
* [CBES-204](https://issues.couchbase.com/browse/CBES-204): Added a new `[couchbase.env]` [config section](configuration.md#couchbase-env) for tuning Couchbase Java SDK settings.
* [CBES-203](https://issues.couchbase.com/browse/CBES-203): Upgraded the Couchbase Java SDK from 3.1.2 to [3.1.3](https://docs.couchbase.com/java-sdk/3.1/project-docs/sdk-release-notes.html#version-3-1-3-2-march-2021).
* [CBES-205](https://issues.couchbase.com/browse/CBES-205): Upgraded the DCP client from 0.33.0 to 0.34.0.

## [](#v4.2.9)Version 4.2.9 (2021-03-16)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.9/couchbase-elasticsearch-connector-4.2.9.zip)

This release improves diagnostic logging and fixes an issue with scopes & collections.

### [](#enhancements-30)Enhancements

* [CBES-192](https://issues.couchbase.com/browse/CBES-192): When the new `logDocumentLifecycle` config property is set to true in the [logging](https://docs.couchbase.com/elasticsearch-connector/4.2/configuration.html#logging) section, the connector writes detailed log entries as each document flows through the connector.
* [CBES-198](https://issues.couchbase.com/browse/CBES-198): Log redaction is now configurable via the new `redactionLevel` config property in the [logging](https://docs.couchbase.com/elasticsearch-connector/4.2/configuration.html#logging) section.
* [CBES-199](https://issues.couchbase.com/browse/CBES-199): Upgraded the DCP client from 0.32.0 to 0.33.0.

### [](#bug-fixes-7)Bug Fixes

* [CBES-193](https://issues.couchbase.com/browse/CBES-193): If two documents in different collections had the same ID, and both were processed by the connector in the same batch, one would be incorrectly flagged as a duplicate and dropped, even if it had a different destination index. With this fix, documents are never considered duplicates if they have different destination indexes. _This issue only affected users experimenting with the Scopes & Collections feature._

## [](#v4.2.8)Version 4.2.8 (2021-02-16)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.8/couchbase-elasticsearch-connector-4.2.8.zip)

This release adds uncommitted support for client certificate authentication (mTLS), adds hostname verification for secure DCP connections, and improves the stability of the connector.

### [](#enhancements-31)Enhancements

* [CBES-183](https://issues.couchbase.com/browse/CBES-183): When secure connections are enabled, it is now possible to authenticate with Couchbase and/or Elasticsearch using an X.509 certificate instead of a username & password. See the [Client Certificates documentation](https://docs.couchbase.com/elasticsearch-connector/current/configuration.html#client-certificates) for details. (This feature is added as "uncommitted", meaning it may change without notice.)
* [CBES-187](https://issues.couchbase.com/browse/CBES-187): Errors during an early phase of connector startup were written to the console instead of being logged. Now these errors will appear in the log as well.
* [CBES-189](https://issues.couchbase.com/browse/CBES-189): Upgraded the Couchbase Java SDK from 3.1.0 to 3.1.2.
* [CBES-188](https://issues.couchbase.com/browse/CBES-188): Upgraded the DCP client from 0.31.0 to 0.32.0.
* [JDCP-188](https://issues.couchbase.com/browse/JDCP-188): Previously, TLS hostname verification was done only for the Couchbase Java client connection; now the DCP client connection is verified as well.

### [](#bug-fixes-8)Bug Fixes

* [JDCP-183](https://issues.couchbase.com/browse/JDCP-183): If an invalid stream offset is detected, the connector will now fail fast instead of potentially corrupting the saved checkpoint.
* [JDCP-184](https://issues.couchbase.com/browse/JDCP-184): Resolved an issue that could cause a flow control deadlock when streaming from a subset of a bucket’s collections or scopes.

## [](#v4.2.7)Version 4.2.7 (2021-01-19)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.7/couchbase-elasticsearch-connector-4.2.7.zip)

For those running the connector in Autonomous Operations mode, this release improves compatibility with recent Consul versions.

### [](#enhancements-32)Enhancements

* [CBES-185](https://issues.couchbase.com/browse/CBES-185): The connector no longer fails to start when using Consul version 1.8.4 and later. The list of tested and supported Consul versions now includes Consul 1.9.1.

## [](#v4.2.6)Version 4.2.6 (2020-12-15)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.6/couchbase-elasticsearch-connector-4.2.6.zip)

This release brings improvements to monitoring and adds an option for disabling TLS certificate hostname verification.

### [](#enhancements-33)Enhancements

* [CBES-184](https://issues.couchbase.com/browse/CBES-184): The connector now exposes Prometheus metrics at `/metrics/prometheus`. Prometheus metrics are "Uncommitted API" and subject to change between releases without notice. The original Dropwizard JSON metrics are still available at `/metrics`, and can now be accessed at the alternative path `/metrics/dropwizard`.
* [CBES-181](https://issues.couchbase.com/browse/CBES-181): Added a new config property, `hostnameVerification` (default: `true`). Couchbase TLS certificate hostname verification was silently enabled by default in version 4.2.3\. If this caused problems for your deployment, and you are unable to issue certificates matching the Couchbase server nodes, you can now disable hostname verification by setting this new config property to `false`.
* [CBES-182](https://issues.couchbase.com/browse/CBES-182): Upgraded the Couchbase Java SDK from 3.0.9 to 3.1.0.

## [](#v4.2.5)Version 4.2.5 (2020-11-17)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.5/couchbase-elasticsearch-connector-4.2.5.zip)

This release fixes an issue with configuring secure connections to Elasticsearch using custom ports. It also adds a new metric for monitoring the replication backlog.

### [](#enhancements-34)Enhancements

* [CBES-121](https://issues.couchbase.com/browse/CBES-121): Added new `cbes.backlog` metric which estimates the number of Couchbase document changes yet to be processed. This is a general indication of how well the connector is keeping up with changes in Couchbase. Note that the count only includes changes in the Couchbase partitions handled by the connector instance reporting the metric. Unlike `cbes.backfill`, this value is dynamic; it goes up when changes happen in Couchbase, and goes down as the changes are processed by the connector.
* [CBES-178](https://issues.couchbase.com/browse/CBES-178): Upgraded the DCP client from 0.30.0 to 0.31.0.

### [](#bug-fixes-9)Bug Fixes

* [CBES-179](https://issues.couchbase.com/browse/CBES-179): Fixed an issue that prevented the connector from establishing a secure connection to Elasticsearch if a custom port was specified.

## [](#v4.2.4)Version 4.2.4 (2020-10-20)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.4/couchbase-elasticsearch-connector-4.2.4.zip)

This release improves compatibility with Couchbase Cloud, and fixes a few minor issues.

### [](#enhancements-35)Enhancements

* [CBES-170](https://issues.couchbase.com/browse/CBES-170): Bootstrap performance is improved when specifying custom ports.
* [CBES-175](https://issues.couchbase.com/browse/CBES-175): Upgraded the Couchbase Java SDK from 3.0.6 to 3.0.9\. The connector no longer logs spurious warnings about being unable to fetch collections manifests.
* [CBES-177](https://issues.couchbase.com/browse/CBES-177): Upgraded the DCP client from 0.28.0 to 0.30.0.

### [](#bug-fixes-10)Bug Fixes

* [CBES-173](https://issues.couchbase.com/browse/CBES-173): Fixed a regression in version 4.2.3 that broke alternate address resolution. The connector now handles DNS SRV and alternate addresses correctly, and can connect to Couchbase Cloud or other network environments that use alternate addresses.
* [CBES-172](https://issues.couchbase.com/browse/CBES-172): Removed duplicate command line scripts from the ZIP archive. You can now `unzip` the archive without being prompted about overwriting the duplicate files.

## [](#v4.2.3)Version 4.2.3 (2020-07-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.3/couchbase-elasticsearch-connector-4.2.3.zip)

This release adds "uncommitted" support for Collections and Scopes, a new feature planned for Couchbase Server 7.0.

### [](#enhancements-36)Enhancements

* [CBES-163](https://issues.couchbase.com/browse/CBES-163): Type definitions now have a `matchOnQualifiedKey` property that lets a rule match against the qualified document name, which includes the scope and collection. This enables type definition rules that write to an Elasticsearch index whose name matches the Couchbase collection name.
* [CBES-164](https://issues.couchbase.com/browse/CBES-164): The `[couchbase]` config section now has optional `scope` and `collection` properties that limit the replication to a single scope or to a set of collections.
* [CBES-165](https://issues.couchbase.com/browse/CBES-165): The `[couchbase]` config section now has optional `metadataCollection` property that controls which collection is used to store metadata like replication checkpoints.

### [](#known-issues)Known Issues

* [CBES-170](https://issues.couchbase.com/browse/CBES-170): If you specify a custom port for a Couchbase host, it can take a long while to connect, and the connector will log lots of warnings about being unable to connect to the KV service.

The workaround is to bootstrap using a KV port (default 11210) instead of a manager port (default 8091), and to explicitly tag the port as belonging to the KV service, like this:

```toml
hosts = ['example.com:12345=kv']
```

## [](#v4.2.2)Version 4.2.2 (2020-05-19)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.2/couchbase-elasticsearch-connector-4.2.2.zip)

The connector now behaves better in environments where DNS entries are highly dynamic. Instead of caching resolved hostnames, it now resolves hostnames prior to every connection attempt.

This release also improves decompression performance, activates Netty native transports, and fixes a bug that prevented the 'couchbase.network' config setting from being honored.

The compatibility matrix is updated to add support for Elasticsearch 7.6 and 7.7\. Elasticsearch versions prior to 6.6 are dropped due to end of life, with the exception of 5.6.16.

### [](#bug-fixes-11)Bug Fixes

* [CBES-155](https://issues.couchbase.com/browse/CBES-155) Couchbase client ignores 'couchbase.network' config setting

### [](#enhancements-37)Enhancements

* [JDCP-163](https://issues.couchbase.com/browse/JDCP-156) Force DNS lookups on reconnect
* [JDCP-156](https://issues.couchbase.com/browse/JDCP-156) Enable Netty native transports by default
* [JDCP-82](https://issues.couchbase.com/browse/JDCP-82) Decompress with org.iq80.snappy instead of Netty
* [CBES-158](https://issues.couchbase.com/browse/CBES-158) Upgrade Couchbase SDK from 2.7.11 to 2.7.15
* [CBES-154](https://issues.couchbase.com/browse/CBES-154) Upgrade DCP client from 0.25.0 to 0.28.0
* [JDCP-146](https://issues.couchbase.com/browse/JDCP-146) Upgrade Netty from 4.0.56 to 4.1.48

## [](#v4.2.1)Version 4.2.1 (2020-01-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.1/couchbase-elasticsearch-connector-4.2.1.zip)

This maintenance release addresses an issue with shutdown hooks that could prevent the connector from terminating in some circumstances.

Also fixed in this release, bulk request timeouts longer than 30 seconds are now honored instead of being reduced to 30 seconds.

Metrics from the Couchbase DCP client are now included in the metrics report, along with gauges for CPU load.

### [](#bug-fixes-12)Bug Fixes

* [CBES-147](https://issues.couchbase.com/browse/CBES-147) Stuck shutdown hook can prevent/delay JVM termination
* [CBES-149](https://issues.couchbase.com/browse/CBES-149) Bulk request timeout is capped at 30 seconds

### [](#enhancements-38)Enhancements

* [CBES-143](https://issues.couchbase.com/browse/CBES-143) Report DCP metrics
* [CBES-148](https://issues.couchbase.com/browse/CBES-148) Report CPU usage metrics
* [CBES-150](https://issues.couchbase.com/browse/CBES-150) Upgrade Couchbase client to 2.7.11 and DCP client to 0.25.0

## [](#v4.2.0)Version 4.2.0 (2019-10-15)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.2.0/couchbase-elasticsearch-connector-4.2.0.zip)

Hot on the heels of 4.1, we’re releasing 4.2 with support for connecting directly to an Amazon Elasticsearch Service instance. There’s a new `[elasticsearch.aws]` config section for specifying the AWS region of the service. Amazon credentials are obtained from the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html).

Also new in 4.2, the `cbes-consul` command now takes an optional `--consul-config` argument which points to a separate config file where you can specify a Consul ACL token.

On the version compatibility front, we’ve added support for Elasticsearch 7.4 and removed support for Elasticsearch 5.4 (which reached EOL on 2018-11-04).

### [](#enhancements-39)Enhancements

* [CBES-129](https://issues.couchbase.com/browse/CBES-129) Support direct connections to Amazon Elasticsearch Service
* [CBES-140](https://issues.couchbase.com/browse/CBES-140) Support ACL Token Authentication when communicating with Consul
* [CBES-141](https://issues.couchbase.com/browse/CBES-141) Extend support coverage to Elasticsearch 7.4

## [](#v4.1.0)Version 4.1.0 (2019-09-05)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.1.0/couchbase-elasticsearch-connector-4.1.0.zip)

We are excited to unveil the new Autonomous Operations (AO) mode with major improvements to the availability and manageability of the connector. When the connector is deployed in AO mode, worker processes use your HashiCorp Consul cluster to communicate with each other and automatically distribute the replication workload. You can add or remove worker processes at any time without having to manually stop and reconfigure all of the workers. Any worker that fails a health check is automatically removed, and its workload is redistributed among remaining workers.

The new `cbes-consul` command line tool is used to start a worker in AO mode. It also provides streamlined checkpoint management and the ability to reconfigure or pause/resume all of the workers in an AO group at once.

Also new in this release is support for multi-network configuration. This feature allows the connector to talk to Couchbase Server nodes that have been configured to advertise alternate network addresses for connecting to the node from outside a container/cloud networking environment. The new `network` property in the `[couchbase]` section of the configuration gives you control over network selection (although the default value of `auto` is appropriate for most cases).

Finally, the range of supported Elasticsearch versions is extended to include 7.1, 7.2\. and 7.3.

### [](#enhancements-40)Enhancements

* [CBES-65](https://issues.couchbase.com/browse/CBES-65) Autonomous Operations Mode with Consul
* [CBES-135](https://issues.couchbase.com/browse/CBES-135) Expose multi-network config options
* [CBES-138](https://issues.couchbase.com/browse/CBES-138) Upgrade to Couchbase client 2.7.9 and DCP client 0.24.0

## [](#v4.0.2)Version 4.0.2 (2019-05-21)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.0.2/couchbase-elasticsearch-connector-4.0.2.zip)

This maintenance release fixes a bug that prevented some versions of Couchbase Server from rebalancing when the connector is running.

It also adds compatibility with the official Docker images for Elasticsearch 6.7.x and 7.0.x, and is the first version tested against OpenJDK 8 and OpenJDK 11.

### [](#enhancements-41)Enhancements

* [CBES-122](https://issues.couchbase.com/browse/CBES-122) Add support for OpenJDK
* [CBES-123](https://issues.couchbase.com/browse/CBES-123) Support Elasticsearch 6.7 & 7.0 docker images
* [CBES-125](https://issues.couchbase.com/browse/CBES-125) Suppress "types removal" warnings from Elasticsearch 7.0

### [](#bug-fixes-13)Bug Fixes

* [CBES-128](https://issues.couchbase.com/browse/CBES-128) Couchbase Server fails to rebalance if Elasticsearch connector is running

## [](#v4.0.1)Version 4.0.1 (2019-04-15)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.0.1/couchbase-elasticsearch-connector-4.0.1.zip)

This maintenance release improves the stability of the connector and adds new configuration options.

### [](#enhancements-42)Enhancements

* [CBES-90](https://issues.couchbase.com/browse/CBES-90) Ability to use environment variables inside config
* [CBES-107](https://issues.couchbase.com/browse/CBES-107) Misleading error message when can’t connect to Elasticsearch
* [CBES-110](https://issues.couchbase.com/browse/CBES-110) Need document routing to support join
* [CBES-114](https://issues.couchbase.com/browse/CBES-114) Allow saving checkpoints in a different bucket

### [](#bug-fixes-14)Bug Fixes

* [CBES-117](https://issues.couchbase.com/browse/CBES-117) Connector exits on values that fail to parse

## [](#v4.0.0)Version 4.0.0 (2018-10-12)

[Download](https://packages.couchbase.com/clients/connectors/elasticsearch/4.0.0/couchbase-elasticsearch-connector-4.0.0.zip)

### [](#new-in-this-version)New in this version

* The connector is now a standalone process instead of an Elasticsearch plug-in.
* Compatible with Elasticsearch versions 5 and 6.
* Support for secure connections to Couchbase and Elasticsearch.
* Tools for managing replication checkpoints.
* A "rejection log" for documents Elasticsearch permanently refuses to index.
* Configurable document structure (omit metadata if you don’t need it).
* The connector now listens for document changes using the high performance Couchbase Database Change Protocol (DCP).

#### [](#things-to-be-aware-of)Things to be aware of

> [!CAUTION]
> This is a major version upgrade. Because the plug-in and the standalone connector are so different, there is no online upgrade process. See the [Migration](migration.md) documentation for details.

* Parent-child relationships are no longer supported, as this feature was removed in ES 6.
* Routing documents to specific Elasticsearch shards is not implemented. Please let us know if this feature is still relevant for your deployment.

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).