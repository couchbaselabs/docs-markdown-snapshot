---
title: SDK Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Java Client.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/temp/3.6/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-04-08T05:18:32.349Z
link: xref:3.6@java-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.6/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Java Client. 

These pages cover the 3._x_ versions of the Couchbase Java SDK. For release notes, download links, and installation methods for 2.7 and earlier releases of the Couchbase Java Client, which will not work with Distributed Transactions, please see the [2.x Java Release Notes & Download Archive](https://docs-archive.couchbase.com/java-sdk/2.7/sdk-release-notes.html).

### [](#installation)Installation

See the [Full Installation](sdk-full-installation.md) guide for details.

## [](#latest-release)Java SDK 3.11 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

Version 3.11 of the Java SDK implements the 3.9 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-3-11-1-16-february-2026)Version 3.11.1 (16 February 2026)

[Download](https://packages.couchbase.com/clients/java/3.11.1/Couchbase-Java-Client-3.11.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.11.1/index.html) | [Core API Reference](https://docs.couchbase.com/sdk-api/couchbase-core-io-3.11.1/)

This critical release fixes a regression in `3.11.0` that caused documents inserted in transactions to expire immediately.

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 1\. Optional Artifact Version Compatibility__
| Artifact              | Built Against        | API Stability |
| --------------------- | -------------------- | ------------- |
| tracing-opentelemetry | OpenTelemetry 1.57.0 | Committed     |
| tracing-opentracing   | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | OpenTelemetry 1.57.0 | Volatile      |
| metrics-micrometer    | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes)Bug Fixes

* [JVMCBC-1712](https://jira.issues.couchbase.com/browse/JVMCBC-1712): Document inserted in transactions no longer expire immediately. This fixes a regression in `3.11.0`.

### [](#version-3-11-0-04-february-2026)Version 3.11.0 (04 February 2026)

[Download](https://packages.couchbase.com/clients/java/3.11.0/Couchbase-Java-Client-3.11.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.11.0/index.html) | [Core API Reference](https://docs.couchbase.com/sdk-api/couchbase-core-io-3.11.0/)

> [!CAUTION]
> This version has [a serious bug that causes documents inserted in transactions to expire immediately](https://jira.issues.couchbase.com/browse/JVMCBC-1712). We recommend upgrading directly to `3.11.1`.

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 2\. Optional Artifact Version Compatibility__
| Artifact              | Built Against        | API Stability |
| --------------------- | -------------------- | ------------- |
| tracing-opentelemetry | OpenTelemetry 1.57.0 | Committed     |
| tracing-opentracing   | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | OpenTelemetry 1.57.0 | Volatile      |
| metrics-micrometer    | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes-2)Bug Fixes

* [JVMCBC-1705](https://jira.issues.couchbase.com/browse/JVMCBC-1705): Fixed an issue that could cause the transaction cleanup task to terminate unexpectedly, leaving the SDK unable to clean up incomplete transactions.

#### [](#improvements)Improvements

* [JCBC-1739](https://jira.issues.couchbase.com/browse/JCBC-1739): When inserting or replacing a document inside a transaction, it is now possible to specify an expiration time for the document.This feature was removed in `3.11.1` due to [a serious bug](https://jira.issues.couchbase.com/browse/JVMCBC-1712) in `3.11.0`.
* [JVMCBC-1708](https://jira.issues.couchbase.com/browse/JVMCBC-1708): Upgraded `OpenTelemetry` from `1.31.0` to `1.57.0`.
* [JVMCBC-1692](https://jira.issues.couchbase.com/browse/JVMCBC-1692): SQL++ statements are now excluded from tracing spans unless the query has parameters.
* [JCBC-2207](https://jira.issues.couchbase.com/browse/JCBC-2207): Developers who want to use the latest [OpenTelemetry semantic conventions for database client spans](https://opentelemetry.io/docs/specs/semconv/db/database-spans/)can now opt in by setting the `OTEL_SEMCONV_STABILITY_OPT_IN` environment variable to `database` (or `database/dup` to create duplicate spans using both old and new conventions). Java and Scala developers can also opt in via the `observabilitySemanticConventions` client setting, which has a higher precedence than the environment variable.
* [JVMCBC-1635](https://jira.issues.couchbase.com/browse/JVMCBC-1635): Upgraded Netty from `4.1.130` to `4.2.9`.  
> [!TIP]  
> Netty 4.2 introduces a new memory allocator called `AdaptiveByteBufAllocator`. By default, this version of the Couchbase SDK continues using the tried and true `PooledByteBufAllocator`. However, the default may change in a future minor version. If you want to use the new allocator now, set the Java system property `com.couchbase.client.core.deps.io.netty.allocator.type` to `adaptive`. On the other hand, if you want to insulate your project from possible future changes to the default allocator, set that property to `pooled`.
* [JCBC-2211](https://jira.issues.couchbase.com/browse/JCBC-2211): Added an optional `Jackson3JsonSerializer` which uses Jackson 3 for data binding.  
> [!CAUTION]  
> The new `Jackson3JsonSerializer` does not support the `@Encrypted` annotation for automatic Field-Level Encryption. If your application relies on this feature, please continue using Jackson 2 for now.

## [](#java-sdk-3-10-releases)Java SDK 3.10 Releases

### [](#version-3-10-1-14-january-2026)Version 3.10.1 (14 January 2026)

[Download](https://packages.couchbase.com/clients/java/3.10.1/Couchbase-Java-Client-3.10.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.10.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.10.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 3\. Optional Artifact Version Compatibility__
| Artifact              | Built Against        | API Stability |
| --------------------- | -------------------- | ------------- |
| tracing-opentelemetry | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes-3)Bug Fixes

* [JVMCBC-1709](https://jira.issues.couchbase.com/browse/JVMCBC-1709): Enabling TLS inside an OSGi container no longer causes `java.lang.ClassNotFoundException: javax.net.ssl.TrustManagerFactory not found by core-io`.

#### [](#improvements-2)Improvements

* [JVMCBC-1707](https://jira.issues.couchbase.com/browse/JVMCBC-1707): Upgraded `Netty` from `4.1.128` to `4.1.130`.
* [JCBC-2206](https://jira.issues.couchbase.com/browse/JCBC-2206): Deprecated the Views API.  
> [!NOTE]  
> Server-side support for Views has been deprecated since Couchbase Server 7.0, and will be removed in a future server release.

### [](#version-3-10-0-11-november-2025)Version 3.10.0 (11 November 2025)

This is the first release of the 3.10 series.

[Download](https://packages.couchbase.com/clients/java/3.10.0/Couchbase-Java-Client-3.10.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.10.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.10.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 4\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 3.10.0            | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 3.10.0            | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 3.10.0            | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 3.10.0            | Micrometer 1.12.9    | Volatile      |

##### [](#bug-fixes-4)Bug Fixes

* [JVMCBC-1696](https://couchbasecloud.atlassian.net/browse/JVMCBC-1696): The client no longer makes bucketful KV connections to nodes that aren't hosting the bucket, ensuring that unconnected endpoints don't cause SDC health check to fail.
* [JVMCBC-1697](https://couchbasecloud.atlassian.net/browse/JVMCBC-1697): Fixed a problem that caused the SDK to use more bandwidth than necessary when polling Couchbase Server 7.6 and later, for cluster topology updates when the topology is in a steady state.

##### [](#improvements-3)Improvements

* [JVMCBC-1693](https://couchbasecloud.atlassian.net/browse/JVMCBC-1693): The SDK now tracks server cluster topology changes more efficiently, and no longer sends redundant "get topology" requests during failover and rebalance.
* [JVMCBC-1699](https://couchbasecloud.atlassian.net/browse/JVMCBC-1699): If the bootstrap address resolution task does not complete before the cluster is disconnected, the task now terminates gracefully instead of logging a scary warning.
* [JVMCBC-1700](https://couchbasecloud.atlassian.net/browse/JVMCBC-1700): Upgraded to `Jackson` `2.20.1`.
* [JVMCBC-1704](https://couchbasecloud.atlassian.net/browse/JVMCBC-1704): Upgraded `Netty` from `4.1.127` to `4.1.128`.

##### [](#new-features)New Features

* [JVMCBC-1679](https://couchbasecloud.atlassian.net/browse/JVMCBC-1679): Support for short lived mTLS certs refresh without application restart. Added new `cluster.authenticator(Authenticator)` method for updating the authenticator used by a cluster. Useful for scenarios where you want to refresh credentials without restarting your app.
* [JVMCBC-1689](https://couchbasecloud.atlassian.net/browse/JVMCBC-1689): Added `JwtAuthenticator`.

## [](#java-sdk-3-9-releases)Java SDK 3.9 Releases

Version 3.9 of the Java SDK implements the 3.8 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-3-9-2-10-october-2025)Version 3.9.2 (10 October 2025)

This is the second maintenance release of the 3.9 series.

[Download](https://packages.couchbase.com/clients/java/3.9.2/Couchbase-Java-Client-3.9.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.9.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.9.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 5\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 3.9.2             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 3.9.2             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 3.9.2             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 3.9.2             | Micrometer 1.12.9    | Volatile      |

#### [](#improvements-4)Improvements

* [JVMCBC-1694](https://couchbasecloud.atlassian.net/browse/JVMCBC-1694): Updated `Netty` to `4.1.127`.
* [JCBC-2204](https://couchbasecloud.atlassian.net/browse/JCBC-2204): Added an `io.configNotifications` client setting. If advised by Couchbase Technical Support, set this to false to disable server-initiated cluster topology change notifications.

### [](#version-3-9-1-5-september-2025)Version 3.9.1 (5 September 2025)

This is the first maintenance release of the 3.9 series.

[Download](https://packages.couchbase.com/clients/java/3.9.1/Couchbase-Java-Client-3.9.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.9.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.9.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 6\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 3.9.1             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 3.9.1             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 3.9.1             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 3.9.1             | Micrometer 1.12.9    | Volatile      |

#### [](#improvements-5)Improvements

* [JVMCBC-1678](https://couchbasecloud.atlassian.net/browse/JVMCBC-1678): Upgraded `Netty` to `4.1.124`.
* [JVMCBC-1680](https://couchbasecloud.atlassian.net/browse/JVMCBC-1680): When parsing cluster topology into a `ClusterTopology` object, the original JSON is now retained, so it can be re-parsed with different parameters later.

### [](#version-3-9-0-5-august-2025)Version 3.9.0 (5 August 2025)

This is the first release of the 3.9 series.

[Download](https://packages.couchbase.com/clients/java/3.9.0/Couchbase-Java-Client-3.9.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.9.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.9.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 7\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 3.9.0             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 3.9.0             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 3.9.0             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 3.9.0             | Micrometer 1.12.9    | Volatile      |

#### [](#behavioral-changes)Behavioral Changes

* [JVMCBC-1660](https://couchbasecloud.atlassian.net/browse/JVMCBC-1660): The "auto" network selection heuristic has been changed to fall back to the "external" network if the "external" network is present. Previously, if there was no exact match between an address in the connection string and an address in the cluster topology reported by the server, the SDK would select the "default" network. Now, if there is no match and an "external" network is present, the SDK selects the "external" network.  
If this change causes the SDK to select the incorrect network for your deployment, use the [io.networkResolution](../ref/client-settings.md#io.networkResolution) client setting to configure the SDK to use the "default" network.

#### [](#bug-fixes-5)Bug Fixes

* [JVMCBC-1656](https://couchbasecloud.atlassian.net/browse/JVMCBC-1656): Fixed an issue that could prevent the SDK from periodically updating its list of KV node addresses. This could occur if the addresses in the connection string (or DNS SRV record) differ from the server's self-reported address as they appear in the admin UI. This issue can lead to `UnknownHostException` messages in the SDK logs. To resolve the issue, the SDK now feeds both "global" and "bucket" topology info into the same funnel, so the SDK can update its list of node addresses from either source.
* [JVMCBC-1662](https://couchbasecloud.atlassian.net/browse/JVMCBC-1662): Fixed an issue that prevented the SDK from honoring the "preferred server group" option inside transactions.
* [JVMCBC-1664](https://couchbasecloud.atlassian.net/browse/JVMCBC-1664): Exceptionally long-running analytics queries no longer throw `ArrayIndexOutOfBoundsException`.
* [JVMCBC-1671](https://couchbasecloud.atlassian.net/browse/JVMCBC-1671): All expected attributes are now included in transactions metrics exported by the SDK.

#### [](#improvement)Improvement

* [JVMCBC-1639](https://couchbasecloud.atlassian.net/browse/JVMCBC-1639): We've adopted a mono-versioning strategy for the Couchbase JVM client libraries. The Scala and Kotlin SDKs, along with the core library and optional modules, are now aligned with the Java SDK at version 3.9.0.  
Although this is a technically a major version bump for some components, in this exceptional case it does not indicate a breaking change. The goal of this alignment is twofold: to minimize confusion about which versions are compatible with each other, and to enable a more disciplined branch management strategy where patch releases contain only low-risk bug fixes.
* [JVMCBC-1607](https://couchbasecloud.atlassian.net/browse/JVMCBC-1607): Improved how the SDK logs information about trusted TLS certificates on startup. It now logs up to 5 certificates at `INFO` level, and the full list at `DEBUG` level. Previously, the SDK logged the full list at `INFO` level, which could prevent other interesting configuration info from being included in the log, depending on how logging was configured.
* [JVMCBC-1612](https://couchbasecloud.atlassian.net/browse/JVMCBC-1612): The SDK is now more aggressive about detecting dead or half-open KV connections. It closes a connection if there is no incoming traffic for the duration specified by `io.configIdleRedialTimeout` (default value: 5 minutes), and sends a `NOOP` request if there is no incoming traffic for hallf that duration.
* [JVMCBC-1648](https://couchbasecloud.atlassian.net/browse/JVMCBC-1648): Upgraded `Jackson` from `2.17.3` to `2.19.2`.
* [JVMCBC-1651](https://couchbasecloud.atlassian.net/browse/JVMCBC-1651): Improved internal support for sub-document replica reads against upcoming server versions.
* [JVMCBC-1652](https://couchbasecloud.atlassian.net/browse/JVMCBC-1652): Shading the Couchbase SDK no longer causes it report a version number of `0.0.0`.
* [JVMCBC-1657](https://couchbasecloud.atlassian.net/browse/JVMCBC-1657): Improved the backpressure implementation for reactive SQL++, Analytics, and Full-Text Search queries. The SDK now requires less memory to buffer results if the consumer cannot keep up with the producer.
* [JVMCBC-1658](https://couchbasecloud.atlassian.net/browse/JVMCBC-1658): When the SDK removes uninteresting Netty stack frames from stack traces, it now also applies the filtering to suppressed exceptions. This improves stack trace readability in some cases when Project Reactor debugging is enabled.

#### [](#new-features-2)New Features

* [JVMCBC-1637](https://couchbasecloud.atlassian.net/browse/JVMCBC-1637): A Bill of Materials (BOM) for Couchbase JVM clients is now available. It specifies compatible versions of the Java, Scala, and Kotlin clients, as well as the optional metrics and tracing components. <https://central.sonatype.com/artifact/com.couchbase.client/couchbase-client-bom>.
* [JCBC-2193](https://couchbasecloud.atlassian.net/browse/JCBC-2193): A Full-Text Search vector query now has an optional "prefilter" parameter. This is a non-vector query that the server executes first to get an intermediate result. Then it executes the vector query on the intermediate result to get the final result.

## [](#java-sdk-3-8-releases)Java SDK 3.8 Releases

### [](#version-3-8-3-11-july-2025)Version 3.8.3 (11 July 2025)

This is the third maintenance release of the 3.8 series.

[Download](https://packages.couchbase.com/clients/java/3.8.3/Couchbase-Java-Client-3.8.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.8.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 8\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.6.3             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.6.3             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.8.3             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.8.3             | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes-6)Bug Fixes

* [JVMCBC-1654](https://couchbasecloud.atlassian.net/browse/JVMCBC-1654): FIxed a bug that prevented `Collection.getAnyReplica()`, `getAllReplicas()`, `lookupInAnyReplica()`, `lookupInAllReplicas()`, `scan()`, `[Reactive]BatchHelper.exists()`, and `getIfExists()` from timing out if the bucket does not exist or is not accessible.

### [](#version-3-8-2-3-june-2025)Version 3.8.2 (3 June 2025)

This is the second maintenance release of the 3.8 series.

[Download](https://packages.couchbase.com/clients/java/3.8.2/Couchbase-Java-Client-3.8.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.8.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 9\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.6.2             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.6.2             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.8.2             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.8.2             | Micrometer 1.12.9    | Volatile      |

#### [](#improvements-6)Improvements

* [JVMCBC-1647](https://couchbasecloud.atlassian.net/browse/JVMCBC-1647): Upgraded `Jackson` from `2.17.2` to `2.17.3`.

### [](#version-3-8-1-9-may-2025)Version 3.8.1 (9 May 2025)

This is the first maintenance release of the 3.8 series.

[Download](https://packages.couchbase.com/clients/java/3.8.1/Couchbase-Java-Client-3.8.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.8.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 10\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.6.1             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.6.1             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.8.1             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.8.1             | Micrometer 1.12.9    | Volatile      |

#### [](#improvements-7)Improvements

* [JVMCBC-1631](https://couchbasecloud.atlassian.net/browse/JVMCBC-1631): Updated `Netty` to `4.1.119`.

### [](#version-3-8-0-9-april-2025)Version 3.8.0 (9 April 2025)

This is the first release of the 3.8 series.

[Download](https://packages.couchbase.com/clients/java/3.8.0/Couchbase-Java-Client-3.8.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.8.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 11\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.6.0             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.6.0             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.8.0             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.8.0             | Micrometer 1.12.9    | Volatile      |

#### [](#new-features-3)New Features

* [JVMCBC-1602](https://couchbasecloud.atlassian.net/browse/JVMCBC-1602:): Application Telemetry improvements.

#### [](#improvements-8)Improvements

* [JCBC-2183](https://couchbasecloud.atlassian.net/browse/JCBC-2183): Added `TransactionAttemptContext.getMulti()`, a new transaction method for fetching multiple documents with minimal read skew.
* [JCBC-2186](https://couchbasecloud.atlassian.net/browse/JCBC-2186): The bucket management API now supports specifying the number of VBuckets for a Magma bucket (requires Couchbase Server 8.0 or later).

## [](#java-sdk-3-7-releases)Java SDK 3.7 Releases

Version 3.7 of the Java SDK implements the 3.6 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-3-7-9-11-march-2025)Version 3.7.9 (11 March 2025)

This is the ninth maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.9/Couchbase-Java-Client-3.7.9.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.9/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.9/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 12\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.9             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.9             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.9             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.9             | Micrometer 1.12.9    | Volatile      |

#### [](#improvements-9)Improvements

* [JVMCBC-1614](https://couchbasecloud.atlassian.net/browse/JVMCBC-1614): Added `ServiceType.id()`
* [JVMCBC-1615](https://couchbasecloud.atlassian.net/browse/JVMCBC-1615): Moved `nodeUUID` from `NodeIdentifier` to `HostAndServicePorts`.
* [JVMCBC-1616](https://couchbasecloud.atlassian.net/browse/JVMCBC-1616)Upgraded Netty to `4.1.118`.

### [](#version-3-7-8-11-february-2025)Version 3.7.8 (11 February 2025)

This is the eighth maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.8/Couchbase-Java-Client-3.7.8.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.8/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.8/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 13\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.8             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.8             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.8             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.8             | Micrometer 1.12.9    | Volatile      |

#### [](#improvements-10)Improvements

* [JVMCBC-1609](https://jira.issues.couchbase.com/browse/JVMCBC-1609): Added experimental client settings for tuning socket send/receive buffer size and channel outbound buffer high/low-water marks.

  * `io.sendBuffer`
  * `io.receiveBuffer`
  * `io.lowWaterMark`
  * `io.highWaterMark`  
  > [!NOTE]  
  > We do not currently recommend configuring these settings unless you are working with Couchbase technical support to diagnose a network performance issue.
* [JCBC-2179](https://jira.issues.couchbase.com/browse/JCBC-2179): `CouchbaseHttpClient` can now send `PATCH` requests.

### [](#version-3-7-7-08-january-2025)Version 3.7.7 (08 January 2025)

This is the seventh maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.7/Couchbase-Java-Client-3.7.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.7/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.7/)

The supported and tested dependencies for this release are: \* io.projectreactor:**reactor-core:3.6.9**\* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 14\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.7             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.7             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.7             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.7             | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes-7)Bug Fixes

* [JVMCBC-1592](https://jira.issues.couchbase.com/browse/JVMCBC-1592): When fetching fresh cluster topology information for a bucket, the SDK now dispatches the request to a random eligible node instead of using a round-robin algorithm. Randomizing the node selection avoids a pathological condition where if the number of open buckets is equal to the number of nodes, and one of the nodes is degraded, the config refresh attempt for a particular bucket would fail repeatedly because it was always sent to the degraded node.
* [JCBC-2152](https://jira.issues.couchbase.com/browse/JCBC-2152): Return the inserted document in the form of a TransactionGetResult instead of the old content from the Get operation.

#### [](#improvements-11)Improvements

* [JVMCBC-1585](https://jira.issues.couchbase.com/browse/JVMCBC-1585): When a thread executing clusterOrScope.queryStreaming() is interrupted, the thrown CancellationException now has the original InterruptedException as its cause.
* [JCBC-2174](https://jira.issues.couchbase.com/browse/JCBC-2174): Added experimental queryStreaming methods to Cluster and Scope. These methods let you process SQL++ query result rows as they arrive from the server, without having to use the Reactive API. See the Javadoc for details. Example usage:

clusterOrScope.queryStreaming(
  "select 'hello' as greeting",
  row -> System.out.println(row.contentAsObject())
);

### [](#version-3-7-6-04-december-2024)Version 3.7.6 (04 December 2024)

This is the sixth maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.6/Couchbase-Java-Client-3.7.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.6/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.6/)

The supported and tested dependencies for this release are: \* io.projectreactor:**reactor-core:3.6.9**\* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 15\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.6             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.6             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.6             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.6             | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes-8)Bug Fixes

* [JVMCBC-1583](https://jira.issues.couchbase.com/browse/JVMCBC-1583): Fixed a race condition that could cause the SDK to continuously attempt to reconnect to a node, even after the node is rebalanced out of the cluster.

#### [](#improvements-12)Improvements

* [JVMCBC-1560](https://jira.issues.couchbase.com/browse/JVMCBC-1560): Added cluster UUID and name to metrics and spans.
* [JVMCBC-1582](https://jira.issues.couchbase.com/browse/JVMCBC-1582): Upgraded `Netty` from `4.1.112` to `4.1.115`.
* [JCBC-2173](https://jira.issues.couchbase.com/browse/JCBC-2173): Upgraded `jctools-core` to `4.0.5`.
* [JCBC-2175](https://jira.issues.couchbase.com/browse/JCBC-2175): Separated `MpscArrayQueue` creation in certain classes.

### [](#version-3-7-5-06-november-2024)Version 3.7.5 (06 November 2024)

This is the fifth maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.5/Couchbase-Java-Client-3.7.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.5/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.5/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 16\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.5             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.5             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.5             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.5             | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes-9)Bug Fixes

* [JVMCBC-1572](https://jira.issues.couchbase.com/browse/JVMCBC-1572): Due to a regression in 3.7.1, using a secure connection would cause `waitUntilReady()` to not wait, and would cause `ping()` to report failures even when nothing was wrong. The issue that caused these problems is now fixed.
* [JVMCBC-1577](https://jira.issues.couchbase.com/browse/JVMCBC-1577): Due to a regression in 3.7.1, sometimes a request made shortly after calling `Cluster.connect()` would fail with a message that said the service is not available in the cluster, even if the service was actually available. This no longer happens.
* [JVMCBC-1579](https://jira.issues.couchbase.com/browse/JVMCBC-1579): Deprecated `com.couchbase.client.core.node.NodeIdentifier` in favor of `com.couchbase.client.core.topology.NodeIdentifier`.

#### [](#improvements-13)Improvements

* [JVMCBC-1576](https://jira.issues.couchbase.com/browse/JVMCBC-1576): Bumped `protobuf` version from `3.23.2` to `3.25.5`.
* [JCBC-2167](https://jira.issues.couchbase.com/browse/JCBC-2167): When using the Reactive API, it's now possible to specify the default Scheduler results are published on. The new `ClusterEnvironment.Builder.publishOnScheduler(Supplier<Scheduler>)` method takes a supplier that the SDK invokes every time you subscribe to a Mono/Flux. The supplier is invoked by the same thread that does the subscription.  
> [!WARNING]  
> This new configuration option is `volatile` API, meaning it could change without notice as we refine it based on your feedback.
* [JCBC-2169](https://jira.issues.couchbase.com/browse/JCBC-2169): QueryMetrics now has a useful `.toString()` method.

### [](#version-3-7-4-08-october-2024)Version 3.7.4 (08 October 2024)

This is the fourth maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.4/Couchbase-Java-Client-3.7.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.4/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.4/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 17\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.4             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.4             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.4             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.4             | Micrometer 1.12.9    | Volatile      |

#### [](#bug-fixes-10)Bug Fixes

* [JVMCBC-1570](https://jira.issues.couchbase.com/browse/JVMCBC-1570): The SDK was producing an incorrect partition map in `CouchbaseBucketConfig`, for buckets with >= 2 replicas. This has now been fixed.

#### [](#improvements-14)Improvements

* [JCBC-2147](https://jira.issues.couchbase.com/browse/JCBC-2147): New APIs added to allow getting KV documents from a preferred server group. This feature allows the implementation of network optimization when traffic cost between server groups is higher than in the local group. In this case the application might select preferred server group in the connection options, and later opt-in for local operations during replica reads.
* [JVMCBC-1573](https://jira.issues.couchbase.com/browse/JVMCBC-1573): `ExtParallelUnstaging` was producing more threads than required, leading to OOM when many concurrent transactions were executed. This has been rewritten to produce only the necessary number of threads are produced for each transaction.

### [](#version-3-7-3-23-september-2024)Version 3.7.3 (23 September 2024)

This is the third maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.1/Couchbase-Java-Client-3.7.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 18\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.3             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.3             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.3             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.3             | Micrometer 1.12.9    | Volatile      |

#### [](#improvements-15)Improvements

* [JCBC-2095](https://jira.issues.couchbase.com/browse/JCBC-2095): Transactions, `ExtParallelUnstaging` — Commit and rollback documents in parallel, keeping concurrency to a max of 1000.
* [JVMCBC-1564](https://jira.issues.couchbase.com/browse/JVMCBC-1564): Query index manager operation `watchIndexes()` now uses any provided `parentSpan`, and sets required span attributes.
* [JVMCBC-1562](https://jira.issues.couchbase.com/browse/JVMCBC-1562): Updated version dependencies:

  * `netty`: `4.1.122.Final`,
  * `HdrHistogram`: `2.2.2`,
  * `reactor`: `3.6.9`,
  * `blockhound`: `1.0.9.RELEASE`,
  * `micrometer`: `1.12.9`,
  * `grpc`: `1.66.0`,
  * `micrometer-tracing`: `1.3.3`.
* [JVMCBC-1297](https://jira.issues.couchbase.com/browse/JVMCBC-1297): When the SDK starts up, it now logs its actual Git commit hash instead of a `${buildNumber}` placeholder.

### [](#version-3-7-2-13-august-2024)Version 3.7.2 (13 August 2024)

This is the second maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.2/Couchbase-Java-Client-3.7.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 19\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.2             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.2             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.2             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.2             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-16)Improvements

* [JVMCBC-1547](https://issues.couchbase.com/browse/JVMCBC-1547): Updated DnsJava to 3.6.0.
* [JCBC-2157](https://issues.couchbase.com/browse/JCBC-2157): Transaction settings are now configurable using the same callback pattern used by other environment settings. Here's an example of the new syntax:  
```java  
Cluster cluster = Cluster.connect(  
  connectionString,  
  ClusterOptions.clusterOptions(username, password)  
    .environment(env -> env  
      .transactionsConfig(txn -> txn  
        .durabilityLevel(DurabilityLevel.MAJORITY_AND_PERSIST_TO_ACTIVE)  
        .metadataCollection(someKeyspace)  
        .queryConfig(query -> query.scanConsistency(QueryScanConsistency.REQUEST_PLUS))  
        .cleanupConfig(cleanup -> cleanup  
          .cleanupWindow(Duration.ofSeconds(10))  
          .addCollection(someOtherKeyspace))  
      )  
    )  
);  
```

### [](#version-3-7-1-23-july-2024)Version 3.7.1 (23 July 2024)

This is the first maintenance release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.1/Couchbase-Java-Client-3.7.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.7.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 20\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.1             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.1             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.1             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.1             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-17)Improvements

* [JVMCBC-1523](https://issues.couchbase.com/browse/JVMCBC-1523): Upgraded `org.iq80.snappy` from 0.4 to 0.5.
* [JCBC-1528](https://issues.couchbase.com/browse/JCBC-1528): Provided default values for tags for Micrometer.
* [JVMCBC-1532](https://issues.couchbase.com/browse/JVMCBC-1532): Upgraded Jackson from 2.17.0 to 2.17.2.
* [JVMCBC-1540](https://issues.couchbase.com/browse/JVMCBC-1540): Improved compatibility with Spring Data Couchbase by reversing an internal API change present in Couchbase Java SDK 3.6.2 and 3.7.0\. This API change prevented upgrading to the latest Couchbase SDK, independently of the Spring Data Couchbase version.
* [JVMCBC-1544](https://issues.couchbase.com/browse/JVMCBC-1544): The `upsertIndex()` call now prevents vector indexes from being created on server versions before version 7.6.0, which do not support these index types.

#### [](#bugfixes)Bugfixes

* [JVMCBC-1530](https://issues.couchbase.com/browse/JVMCBC-1530): Deprecated the `com.couchbase.client.core.error.QueryException` class. This exception is from the SDK 3 API's beta development, and has never been thrown in a GA version of a Couchbase SDK.
* [JVMCBC-1534](https://issues.couchbase.com/browse/JVMCBC-1534): Fixed possible `DURABILITY_INVALID_LEVEL` if `Durability.NONE` is used with transactions.

### [](#version-3-7-0-15-june-2024)Version 3.7.0 (15 June 2024)

This is the first release of the 3.7 series.

[Download](https://packages.couchbase.com/clients/java/3.7.0/Couchbase-Java-Client-3.7.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.7.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.7.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 21\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.5.0             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.5.0             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.7.0             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.7.0             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-18)Improvements

* [JCBC-2149](https://issues.couchbase.com/browse/JCBC-2149): Adds support for base64-encoded vectors in `VectorQuery`.

## [](#java-sdk-3-6-releases)Java SDK 3.6 Releases

### [](#version-3-6-3-19-august-2024)Version 3.6.3 (19 August 2024)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.6.3/Couchbase-Java-Client-3.6.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.6.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 22\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.4.2             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.4.2             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.6.2             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.6.2             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-19)Improvements

* [JVMCBC-1540](https://issues.couchbase.com/browse/JVMCBC-1540): This release improves compatibility with Spring Data Couchbase by reversing an internal API change present in Couchbase Java SDK 3.6.2 and 3.7.0, that prevented upgrading to the latest Couchbase SDK independently of the Spring Data Couchbase version.
* [JVMCBC-1532](https://issues.couchbase.com/browse/JVMCBC-1532), [JCBC-2160](https://issues.couchbase.com/browse/JCBC-2160): Upgraded Jackson to 2.17.2.

### [](#version-3-6-2-29-april-2024)Version 3.6.2 (29 April 2024)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.6.2/Couchbase-Java-Client-3.6.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.6.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 23\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.4.2             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.4.2             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.6.2             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.6.2             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-20)Improvements

* [JVMCBC-1508](https://issues.couchbase.com/browse/JVMCBC-1508): Upgraded Netty dependency.
* [JVMCBC-1509](https://issues.couchbase.com/browse/JVMCBC-1509): Upgraded Jackson dependency.
* [JCBC-2135](https://issues.couchbase.com/browse/JCBC-2135): Added binary support for transactions.

#### [](#bugfixes-2)Bugfixes

* [JVMCBC-1506](https://issues.couchbase.com/browse/JVMCBC-1506): Reduced the rate at which messages appear in the server's `http_access.log` when a user provides valid credentials but does not have permission to access the bucket.
* [JVMCBC-1512](https://issues.couchbase.com/browse/JVMCBC-1512): Updated Service in Cluster Configuration if only the port is changed.

### [](#version-3-6-1-5-april-2024)Version 3.6.1 (5 April 2024)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.6.1/Couchbase-Java-Client-3.6.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.6.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 24\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.4.1             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.4.1             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.6.1             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.6.1             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-21)Improvements

* [JVMCBC-1477](https://issues.couchbase.com/browse/JVMCBC-1477): Reduced the rate at which messages appear in the server's `http_access.log` when invalid credentials are provided resulting in 401 errors. Issues resulting in 403 errors will be handled in a future release.
* [JVMCBC-1498](https://issues.couchbase.com/browse/JVMCBC-1498): The fields of a `SearchRow` from a Full-Text Search result are now included in the output of `SearchRow.toString()`.
* [JVMCBC-1499](https://issues.couchbase.com/browse/JVMCBC-1499): Disabled DNS SRV caching. The SDK now responds quicker to DNS changes in dynamic environments like Kubernetes.
* [JVMCBC-1500](https://issues.couchbase.com/browse/JVMCBC-1500): Added `EventingFunctionLanguageCompatibility.VERSION_7_2_0`.
* [JVMCBC-1504](https://issues.couchbase.com/browse/JVMCBC-1504): Deprecated static methods that return new config builders, like `TimeoutConfig.builder()` and `TimeoutConfig.kvTimeout(Duration)`. See the following example for the recommended way to configure client settings:  
```java  
Cluster cluster = Cluster.connect(  
  connectionString,  
  ClusterOptions.clusterOptions(username, password)  
    .environment(env -> env  
      .timeoutConfig(timeout -> timeout  
        .kvTimeout(Duration.ofSeconds(3))  
      )  
    )  
);  
```

### [](#version-3-6-0-11-march-2024)Version 3.6.0 (11 March 2024)

Version 3.6.0 is the first release of the 3.6 series.

[Download](https://packages.couchbase.com/clients/java/3.6.0/Couchbase-Java-Client-3.6.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.6.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 25\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.4.0             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.4.0             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.6.1             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.6.1             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-22)Improvements

* [JCBC-2116](https://issues.couchbase.com/browse/JCBC-2116): Added support for vector search, a new feature in Couchbase Server 7.6\. This API is currently at `@Stability.Uncommitted` level.
* [JCBC-2131](https://issues.couchbase.com/browse/JCBC-2131): `Scope.searchIndexes()` is now part of the committed public API.
* [JVMCBC-1487](https://issues.couchbase.com/browse/JVMCBC-1487): Upgraded reactor-core from 3.5.8 to 3.6.3.
* [JVMCBC-1488](https://issues.couchbase.com/browse/JVMCBC-1488): Upgraded Jackson from 2.16.0 to 2.16.1.
* [JVMCBC-1489](https://issues.couchbase.com/browse/JVMCBC-1489): Upgraded Netty from 4.1.101 to 4.1.107.
* [JVMCBC-1491](https://issues.couchbase.com/browse/JVMCBC-1491): `Collection.scan()` methods are now part of the SDK's committed public API. These methods do range-scans of documentIds. This feature requires Couchbase Server 7.6 or later.
* [JVMCBC-1493](https://issues.couchbase.com/browse/JVMCBC-1493): `Collection.lookupInAnyReplica()` and `Collection.lookupInAllReplicas()` are now part of the SDK's committed public API. These methods do sub-document lookups against replicas. This feature requires Couchbase Server 7.6 or later.

#### [](#bugfixes-3)Bugfixes

* [JCBC-2125](https://issues.couchbase.com/browse/JCBC-2125): Fixed an issue with `ScopeSearchIndexManager`, `disallowQuerying`, and `freezePlan` methods, which were not waiting for the server result before returning in the blocking API.
* [JVMCBC-1480](https://issues.couchbase.com/browse/JVMCBC-1480): `couchbase2:` should use exponential backoff when bypassing `BestEffortRetryStrategy`.
* [JVMCBC-1494](https://issues.couchbase.com/browse/JVMCBC-1494): If you specify `min=1` for a Full-Text Search disjunction query, the SDK now always sends the value to the server. Previously, the SDK assumed `1` was the default value, and omitted the parameter in that case.

## [](#java-sdk-3-5-releases)Java SDK 3.5 Releases

### [](#version-3-5-3-6-february-2024)Version 3.5.3 (6 February 2024)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.5.3/Couchbase-Java-Client-3.5.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.5.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 26\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.3.3             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.3.3             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.5.3             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.5.3             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-23)Improvements

* [JVMCBC-1460](https://issues.couchbase.com/browse/JVMCBC-1460): `couchbase2` now supports compressing data between the SDK and the server.
* [JVMCBC-1464](https://issues.couchbase.com/browse/JVMCBC-1464): The `metrics-opentelemetry` package is now aligned with the same `OpenTelemetry` version as `tracing-opentelemetry`.
* [JVMCBC-1468](https://issues.couchbase.com/browse/JVMCBC-1468): `Cluster.connect` now validates that connection strings using the `couchbase2` scheme have exactly one host. (Previously, hosts after the first were silently ignored.).
* [JVMCBC-1470](https://issues.couchbase.com/browse/JVMCBC-1470): Improved support for Full Text Search in `couchbase2` mode.
* [JVMCBC-1472](https://issues.couchbase.com/browse/JVMCBC-1472): `couchbase2` errors will now include diagnostic information when CNG is running with the `--debug` flag.
* [JCBC-2117](https://issues.couchbase.com/browse/JCBC-2117): Support added for `maxTTL` value of -1 for collection "no expiry".

#### [](#bugfixes-4)Bugfixes

* <https://issues.couchbase.com/browse/JVMCBC-1475>\[JVMCBC-1475: Accessing the terms of a `TermFacet` result no longer throws `NullPointerException` if the target field is absent from all documents.

### [](#version-3-5-2-5-january-2024)Version 3.5.2 (5 January 2024)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.5.2/Couchbase-Java-Client-3.5.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.5.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 27\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.3.2             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.3.2             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.5.2             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.5.2             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-24)Improvements

* [JCBC-2113](https://issues.couchbase.com/browse/JCBC-2113): Added a `QueryMetadata.signatureBytes()` method for accessing query signatures that are not JSON Objects.

#### [](#bugfixes-5)Bugfixes

* [JVMCBC-1455](https://issues.couchbase.com/browse/JVMCBC-1455): Fixed compatibility with `couchbase2://` endpoints by upgrading internal GRPC dependency. All `couchbase2://` users should upgrade to this release.
* [JVMCBC-1463](https://issues.couchbase.com/browse/JVMCBC-1463): Fixed compatibility between `couchbase2://` endpoints and the `tracing-opentelemetry` module.

### [](#version-3-5-1-8-december-2023)Version 3.5.1 (8 December 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.5.1/Couchbase-Java-Client-3.5.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.5.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 28\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.3.1             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.3.1             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.5.1             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.5.1             | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-25)Improvements

* [JVMCBC-1435](https://issues.couchbase.com/browse/JVMCBC-1435), [JVMCBC-1436](https://issues.couchbase.com/browse/JVMCBC-1436): Upgraded Netty and Jackson dependencies.
* [JVMCBC-1440](https://issues.couchbase.com/browse/JVMCBC-1440): Adding `DocumentNotLockedException` supporting future Couchbase Server versions that will return an error code when unlocking a document that is not locked.

#### [](#bugfixes-6)Bugfixes

* [JVMCBC-1433](https://issues.couchbase.com/browse/JVMCBC-1433): The SDK can now connect to Memcached buckets whose names contain the percent (`%`) character. (We'd like to take this opportunity to remind everyone that Memcached buckets are deprecated in favor of Ephemeral buckets.)
* [JVMCBC-1437](https://issues.couchbase.com/browse/JVMCBC-1437): With Couchbase Server versions that support updating a collection's max expiry, it's now possible to clear the expiry by passing `Duration.ZERO` for the new value.
* [JVMCBC-1441](https://issues.couchbase.com/browse/JVMCBC-1441): The SDK now handles an additional error case for `IndexNotFoundException`.
* [JVMCBC-1442](https://issues.couchbase.com/browse/JVMCBC-1442): Fixed a dependency issue with `tracing-opentelemetry` module.

### [](#version-3-5-0-21-november-2023)Version 3.5.0 (21 November 2023)

Version 3.5.0 is the first release of the 3.5 series.

The SDK now supports the new couchbase2 protocol, which is upcoming in future Couchbase Server versions. It can be enabled through using a connection string starting with `couchbase2://`. Please see [Cloud Native Gateway](../howtos/managing-connections.md#cloud-native-gateway) for more information.

The SDK now directly depends on SLF4J, which may impact some users — see below for details.

[Download](https://packages.couchbase.com/clients/java/3.5.0/Couchbase-Java-Client-3.5.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.5.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 29\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.3.0             | OpenTelemetry 1.31.0 | Committed     |
| tracing-opentracing   | 1.3.0             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.5.0             | OpenTelemetry 1.31.0 | Volatile      |
| metrics-micrometer    | 0.5.0             | Micrometer 1.10.9    | Volatile      |

#### [](#api-impacting)API Impacting

* [JVMCBC-1319](https://issues.couchbase.com/browse/JVMCBC-1319): BEHAVIORAL CHANGE  
As [previously announced](https://www.couchbase.com/forums/t/embracing-slf4j-in-couchbase-java-sdk-3-5/36474), the SLF4J API is now a required dependency, and the SDK does all logging through SLF4J. The following client settings for customizing logging behavior are deprecated, and no longer have any effect:

  * `logger.disableSlf4J`
  * `logger.fallbackToConsole`
  * `logger.consoleLoggerFormatter`  
  If your project does not already use SLF4J, please follow the announcement link for details and a mini-migration guide.

#### [](#improvements-26)Improvements

* [JVMCBC-1402](https://issues.couchbase.com/browse/JVMCBC-1402), [JVMCBC-1410](https://issues.couchbase.com/browse/JVMCBC-1410): Upgraded Netty from 4.1.96 to 4.1.100, and upgraded `OpenTelemetry` dependency.
* [JVMCBC-1430](https://issues.couchbase.com/browse/JVMCBC-1430): Optimization: removed creation of unnecessary metrics labels when default `LoggingMeter` is used.
* [JVMCBC-1391](https://issues.couchbase.com/browse/JVMCBC-1391): The Bucket Manager API is now forward-compatible with future versions of Couchbase Server that might support storage engine types other than "magma" and "couchstore".
* [JVMCBC-1327](https://issues.couchbase.com/browse/JVMCBC-1327): Improved support for failover handling in future server versions.

#### [](#bugfixes-7)Bugfixes

* [JVMCBC-1264](https://issues.couchbase.com/browse/JVMCBC-1264): DNS SRV lookups now honor the DNS search path. This enables DNS SRV resolution in Kubernetes environments where the `*-srv` hostname advertised by the Couchbase Operator is a partial name that must be resolved using a suffix from the DNS search path.
* [JVMCBC-1426](https://issues.couchbase.com/browse/JVMCBC-1426): When Couchbase Server is too busy to start a new KV range scan, the SDK now retries instead of throwing a `CouchbaseException`.

## [](#java-sdk-3-4-releases)Java SDK 3.4 Releases

### [](#version-3-4-11-4-october-2023)Version 3.4.11 (4 October 2023)

With thanks to our community for the contribution, support for Micrometer Observation has been added via the new `tracing-micrometer-observation` module.

[Download](https://packages.couchbase.com/clients/java/3.4.11/Couchbase-Java-Client-3.4.11.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.11/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.11/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 30\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.11            | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.11            | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.11            | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.11            | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-27)Improvements

* [JCBC-2046](https://issues.couchbase.com/browse/JCBC-2046): With thanks to our community for the contribution, support for Micrometer Observation has been added via the new `tracing-micrometer-observation` module.
* [JVMCBC-1327](https://issues.couchbase.com/browse/JVMCBC-1327): Internal improvements to support upcoming faster failover and config push features.

#### [](#bugfixes-8)Bugfixes

* [JVMCBC-1364](https://issues.couchbase.com/browse/JVMCBC-1364): Fixed decoding of certain niche sub-document errors, so they no longer raise a `DecodingFailureException`.

### [](#version-3-4-10-6-september-2023)Version 3.4.10 (6 September 2023)

This is a standard maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.10/Couchbase-Java-Client-3.4.10.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.10/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.10/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 31\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.10            | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.10            | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.10            | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.10            | Micrometer 1.10.9    | Volatile      |

#### [](#improvements-28)Improvements

* [JVMCBC-1367](https://issues.couchbase.com/browse/JVMCBC-1367): The `db.couchbase.operations` metric now has `db.name` (bucket), `db.couchbase.scope`, `db.couchbase.collection` and `outcome` labels (tags). This new feature is at Stability.Volatile, and may change before it is promoted to Stability.Committed in a future release.
* [JVMCBC-1311](https://issues.couchbase.com/browse/JVMCBC-1311), [JVMCBC-1352](https://issues.couchbase.com/browse/JVMCBC-1352): Upgraded dependencies.

#### [](#bugfixes-9)Bugfixes

* [JVMCBC-1350](https://issues.couchbase.com/browse/JVMCBC-1350): `lookupInAnyReplica` now throws `FeatureNotAvailableException` if the server does not support the feature.
* [JVMCBC-1351](https://issues.couchbase.com/browse/JVMCBC-1351): `lookupInAnyReplica` no longer hangs when too many operations are specified.
* [JVMCBC-1353](https://issues.couchbase.com/browse/JVMCBC-1353): Removed the unrelocated `io.opentracing` classes that accidentally slipped into version 2.4.9 of the Couchbase `core-io` library.
* [JVMCBC-1361](https://issues.couchbase.com/browse/JVMCBC-1361): When the SDK receives multiple cluster map versions at the same time, it is now more careful about applying only the most recent version. Before this change, there was a brief window where the SDK could apply an obsolete cluster map. If this happened, the SDK would temporarily dispatch requests to incorrect or non-existent nodes. This condition was typically short-lived, and healed the next time the SDK polled for an updated cluster map, or dispatched a KV request to the wrong node.
* [JVMCBC-1368](https://issues.couchbase.com/browse/JVMCBC-1368): Fixed a rare `java.lang.ArithmeticException: / by zero` exception in `RoundRobinSelectionStrategy.select` that could occur during rebalance.

### [](#version-3-4-9-2-august-2023)Version 3.4.9 (2 August 2023)

This release adds support for Sub-Document reads from replicas at @Stability.Volatile level: see `collection.lookupInAnyReplica()` and `collection.lookupInAllReplicas()`.

[Download](https://packages.couchbase.com/clients/java/3.4.9/Couchbase-Java-Client-3.4.9.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.9/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.9/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 32\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.9             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.9             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.9             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.9             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-29)Improvements

* [JVMCBC-1339](https://issues.couchbase.com/browse/JVMCBC-1339): When KV traffic capture is enabled, each `ReadTrafficCapturedEvent` now contains a single protocol frame, and the human-readable frame description is more accurate.
* [JVMCBC-1320](https://issues.couchbase.com/browse/JVMCBC-1320): The `waitUntilReady` method is now more aggressive about retrying failed pings. Also, waiting for a desired state of `DEGRADED` no longer fails when the client is fully connected to the cluster.
* [JVMCBC-1343](https://issues.couchbase.com/browse/JVMCBC-1343): Reduced the default value for the `io.idleHttpConnectionTimeout` client setting to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures.
* [JCBC-2078](https://issues.couchbase.com/browse/JCBC-2078): Support for Sub-Document read from replica.

### [](#version-3-4-8-19-july-2023)Version 3.4.8 (19 July 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.8/Couchbase-Java-Client-3.4.8.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.8/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.8/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 33\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.8             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.8             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.8             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.8             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-30)Improvements

* [JCBC-2077](https://issues.couchbase.com/browse/JCBC-2077): Upcoming Couchbase server release 7.6 will support having SQL++ queries read from replicas, in scenarios where the active is unavailable (such as failover). This improves availability, though users should be aware that they may be reading stale data. The option is activated with `scope.query("…​", queryOptions().useReplica(true))`, and is disabled by default. It will only work against 7.6 and above: against older server versions, it will raise a `FeatureNotAvailableException`.
* [JVMCBC-1322](https://issues.couchbase.com/browse/JVMCBC-1322): The `waitUntilReady()` method now logs additional diagnostic information to the `com.couchbase.core.WaitUntilReady` logging category at `DEBUG` level.
* [JCBC-2059](https://issues.couchbase.com/browse/JCBC-2059): If a `Cluster` becomes eligible for garbage collection, and you haven't called `cluster.disconnect()` yet, the SDK now logs a warning and disconnects the cluster for you. This prevent the abandoned cluster's network connections from living forever. Please do not rely on this "auto-disconnect" feature. It's always better to call `cluster.disconnect()` as soon as you're done talking to the cluster, so the network connections and other resources get released right away.
* [JCBC-2076](https://issues.couchbase.com/browse/JCBC-2076): `Collection.touch` now has an additional overload that allows specifying the expiry as an `Instant` instead of a `Duration`.

### [](#version-3-4-7-12-june-2023)Version 3.4.7 (12 June 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.7/Couchbase-Java-Client-3.4.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.7/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.7/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 34\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.7             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.7             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.7             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.7             | Micrometer 1.10.0    | Volatile      |

#### [](#api-impacting-2)API Impacting

* [JCBC-2075](https://issues.couchbase.com/browse/JCBC-2075): Deprecated `ArrayInsert.createPath()`. Calling this method always causes `mutateIn` to throw an exception, because the "array insert" sub-document command does not support creating missing parent objects. If you want to create missing parent objects, please use `MutateInSpec.arrayAppend()` or `arrayPrepend()` instead of `arrayInsert()`.

#### [](#improvements-31)Improvements

* [JCBC-2069](https://issues.couchbase.com/browse/JCBC-2069): `Collection.getAndTouch` now has an additional overload that allows specifying the expiry as an `Instant` instead of a `Duration`.
* [JVMCBC-1290](https://issues.couchbase.com/browse/JVMCBC-1290): Added a new environment config property, `SecurityConfig.enableCertificateVerification(boolean)`, which defaults to true. The purpose of this property is to allow disabling TLS certificate verification in development environments where configuring the CA certificate to trust is not practical. Setting this to false is equivalent to configuring the environment to use `InsecureTrustManager.INSTANCE`. For compatibility with other modern Couchbase SDKs, certificate verification can now be disabled using the connection string parameter: `tls_verify=none`. This config property is introduced at stability level `Volatile`, meaning it may change in a patch release without notice.
* [JVMCBC-1278](https://issues.couchbase.com/browse/JVMCBC-1278), [JVMCBC-1310](https://issues.couchbase.com/browse/JVMCBC-1310), [JVMCBC-1313](https://issues.couchbase.com/browse/JVMCBC-1313): Dependencies updated.

#### [](#bugs)Bugs

* [JVMCBC-1283](https://issues.couchbase.com/browse/JVMCBC-1283): A faceted Full-Text Search result's `SearchNumericRange.min()` and `max()` methods now correctly return null instead of zero when the respective range endpoint is unbounded.
* [JVMCBC-1288](https://issues.couchbase.com/browse/JVMCBC-1288): Fixed a regression in Couchbase Java SDK 3.4.5 and Scala SDK 1.4.5 that prevented Full-Text Search result rows from including an explanation when requested.
* [JVMCBC-1292](https://issues.couchbase.com/browse/JVMCBC-1292): Removed `META-INF/versions/9/module-info.class` from the `core-io` jar. This file was associated with an improperly repackaged dependency, and never should have been there.

### [](#version-3-4-6-4-may-2023)Version 3.4.6 (4 May 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.6/Couchbase-Java-Client-3.4.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.6/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.6/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 35\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.6             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.6             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.6             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.6             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-32)Improvements

* [JCBC-1570](https://issues.couchbase.com/browse/JCBC-1570), [JCBC-2058](https://issues.couchbase.com/browse/JCBC-2058): The `osgi-feature` artifact now uses Log4j 2 instead of Log4j 1.

#### [](#bugs-2)Bugs

* [JCBC-2062](https://issues.couchbase.com/browse/JCBC-2062): Fixed a regression in 3.4.5 that caused `ReactiveCollection.lookupIn` to always throw `StackOverflowException`.
* [JVMCBC-1275](https://issues.couchbase.com/browse/JVMCBC-1275): Fixed a regression in Couchbase Java SDK 3.4.5 and Scala SDK 1.4.5 that caused Full Text Search `term` queries to throw `NullPointerException` unless `prefixLength` and `fuzziness` were specified.
* [JVMCBC-1281](https://issues.couchbase.com/browse/JVMCBC-1281): Fixed a regression in Java SDK 3.4.5 that could cause Full-Text Search results to be sorted in the wrong order if the sort option was specified using a mix of strings and `SearchSort` objects.
* [JVMCBC-1285](https://issues.couchbase.com/browse/JVMCBC-1285): Fixed a regression in Couchbase Java SDK 3.4.5 and Scala SDK 1.4.5 that caused Full-Text Search queries to fail to report the locations of some terms. Specifically, any location that did not have `arrayPositions` was omitted from the results.

### [](#version-3-4-5-13-april-2023)Version 3.4.5 (13 April 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.5/Couchbase-Java-Client-3.4.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.5/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.5/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 36\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.5             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.5             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.5             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.5             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-33)Improvements

* [JVMCBC-1223](https://issues.couchbase.com/browse/JVMCBC-1223): Adds a `RetryReason.AUTHENTICATION_ERROR` at `Uncommitted` API stability level. A custom `RetryStrategy` can use this new, more granular information to distinguish if a connection problem is down to an authentication issue.

#### [](#bugs-3)Bugs

* [JCBC-2032](https://issues.couchbase.com/browse/JCBC-2032): The JSON returned by `SearchQuery.export()` no longer contains extra fields unrelated to the query.
* [JVMCBC-1252](https://issues.couchbase.com/browse/JVMCBC-1252): Orphaned "observe" operations will no longer occasionally contain a `total_duration_us` field equal to 0.
* [JVMCBC-1255](https://issues.couchbase.com/browse/JVMCBC-1255): If you were subscribing to the event bus and printing all the events, you may have noticed `Event.toString()` throwing a `NullPointerException` if the event context is null. `Event.toString()` now handles null contexts more gracefully, and no longer throws this exception.

### [](#version-3-4-4-8-march-2023)Version 3.4.4 (8 March 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.4/Couchbase-Java-Client-3.4.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.4/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.4/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 37\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.4             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.4             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.4             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.4             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-34)Improvements

* [JCBC-2050](https://issues.couchbase.com/browse/JCBC-2050): Coordinates in Full-Text Search geographic queries can now be specified using a staged builder, so it's harder to accidentally swap the latitude and longitude components. Example usage:

```none
Coordinate eiffelTower = Coordinate.lat(48.858093).lon(2.294694);
```

Or, if you prefer to specify longitude first:

```none
Coordinate eiffelTower = Coordinate.lon(2.294694).lat(48.858093);
```

* [JVMCBC-1237](https://issues.couchbase.com/browse/JVMCBC-1237): Added "network" as an alias for the "io.networkResolution" connection string parameter. For example, the connection string "couchbase://example.com?network=external" is now equivalent to "couchbase://example.com?io.networkResolution=external". This was done for compatibility with other Couchbase SDKs that use "network" as the name of this parameter.

#### [](#bugs-4)Bugs

* [JVMCBC-1232](https://issues.couchbase.com/browse/JVMCBC-1232): `Cluster.connect()` now rejects connection strings that have no addresses (like "couchbase://"). Before this change, it would accept the invalid connection string, and subsequent operations would fail with a misleading error message: "The cluster does not support cluster-level queries".
* [JVMCBC-1234](https://issues.couchbase.com/browse/JVMCBC-1234): Fixed a regression in Java SDK 3.4.3 and Scala SDK 1.4.3 that caused SQL++ query result metadata to always include metrics, regardless of the "metrics" query option.

### [](#version-3-4-3-9-february-2023)Version 3.4.3 (9 February 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.3/Couchbase-Java-Client-3.4.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 38\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.3             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.3             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.3             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.3             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-35)Improvements

* [JCBC-2034](https://issues.couchbase.com/browse/JCBC-2034): `CollectionQueryIndexManager` has been added at a `@Stability.Volatile` level, to better allow management of query indexes at the Collection level. Documentation and an upgrade to a higher stability level will follow in the next minor SDK bump. Until then, users are encourage to try out the new functionality and provide feedback — but should expect the possibility of API changes.
* [JVMCBC-1181](https://issues.couchbase.com/browse/JVMCBC-1181): It is now possible to authenticate over secure connections even if the JVM does not support the SASL PLAIN authentication mechanisms.
* [JVMCBC-1184](https://issues.couchbase.com/browse/JVMCBC-1184): Updated dependencies.
* [JVMCBC-1213](https://issues.couchbase.com/browse/JVMCBC-1213): If too many operations are specified in a single sub-document lookup, the exception message now indicates why the operation failed.

#### [](#bug-fixes-11)Bug Fixes

* [JVMCBC-1160](https://issues.couchbase.com/browse/JVMCBC-1160): When a sub-document path has a syntax error or is inappropriate for an operation, the SDK now throws `PathInvalidException`. Prior to this change, it would throw a generic `CouchbaseException` with the message "Unexpected SubDocument response code".
* [JCBC-2045](https://issues.couchbase.com/browse/JCBC-2045): `WatchQueryIndexOptions` now extends `CommonOptions`, allowing standard options such as timeout to be specified.

### [](#version-3-4-2-16-january-2023)Version 3.4.2 (16 January 2023)

This is a regular maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.4.2/Couchbase-Java-Client-3.4.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.4.2**
* com.couchbase.client:**core-io:2.4.2**
* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 39\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.2             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.2             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.2             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.2             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-36)Improvements

* [JVMCBC-1175](https://issues.couchbase.com/browse/JVMCBC-1175): The SDK now includes native libraries for IO and TLS that can enhance performance on `aarch_64` architectures like Graviton and Apple Silicon. Previously, native libraries were included only for `x86_64` architectures. Native libraries for IO and TLS are enabled by default. If you need to disable native IO, set the `ioEnvironment.enableNativeIo` client setting to false. To disable native TLS, set the `security.enableNativeTls` client setting to false.

#### [](#bugs-5)Bugs

* [JVMCBC-1161](https://issues.couchbase.com/browse/JVMCBC-1161): Fixed a minor issue where `cluster.disconnect()` could occasionally timeout due to a race condition.
* [JVMCBC-1176](https://issues.couchbase.com/browse/JVMCBC-1176): Setting `security.enableNativeTls` to false now prevents the SDK from even attempting to load the native TLS library. (Prior to this change, the SDK would load the library and just not use it.) In addition to saving a bit of memory, this prevents the JVM from segfaulting on Alpine Linux where glibc is not available.
* [JVMCBC-1180](https://issues.couchbase.com/browse/JVMCBC-1180): Supporting in transactions a future version of Couchbase Server that requires query\_context be sent in all queries.
* [JVMCBC-1174](https://issues.couchbase.com/browse/JVMCBC-1174): Fixed a regression that prevented native TLS from being used regardless of whether the `security.enableNativeTls` client setting was set to true.

### [](#version-3-4-1-7-december-2022)Version 3.4.1 (7 December 2022)

Version 3.4.1 is the second release of the 3.4 series. The headline change is support for the KV range scan feature (`collection.scan()`), added at @Stability.Volatile level. This feature will be available in a future version of Couchbase Server.

[Download](https://packages.couchbase.com/clients/java/3.4.1/Couchbase-Java-Client-3.4.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.1/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.4.1**
* com.couchbase.client:**core-io:2.4.1**
* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 40\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.1             | OpenTelemetry 1.19.0 | Committed     |
| tracing-opentracing   | 1.2.1             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.1             | OpenTelemetry 1.19.0 | Volatile      |
| metrics-micrometer    | 0.4.1             | Micrometer 1.10.0    | Volatile      |

#### [](#improvements-37)Improvements

* [JVMCBC-1163](https://issues.couchbase.com/browse/JVMCBC-1163): Dependencies have been updated.
* [JVMCBC-1156](https://issues.couchbase.com/browse/JVMCBC-1156): The traffic tracing functionality has been enchanced to perform Wireshark-style dissection of portions of the KV protocol.
* [JCBC-1984](https://issues.couchbase.com/browse/JCBC-1984): KV range scan functionality (`collection.scan()`) added at @Stability.Volatile level. Users are encouraged to experiment with the feature and provide feedback ahead of its formal release in 3.5.0.
* [JCBC-2018](https://issues.couchbase.com/browse/JCBC-2018): Make Core and CoreEnvironment Autocloseable.
* [JCBC-2009](https://issues.couchbase.com/browse/JCBC-2009): Fixed an issue where ArraySetOptions was extending CommonDatastructureOptions incorrectly.
* [JCBC-2021](https://issues.couchbase.com/browse/JCBC-2021): Diagnostics for an endpoint now include the state of the endpoint's circuit breaker.
* [JCBC-2027](https://issues.couchbase.com/browse/JCBC-2027): The `ClusterEnvironment.Builder` methods that take a `Builder` are deprecated in favor of the overloads that take a `Consumer<Builder>`. For example, `ioConfig(IoConfig.Builder)` is deprecated in favor of `ioConfig(Consumer<IoConfig.Builder>)`. The methods that take a `Consumer<Builder>` are preferable because they allow customizing the config without clobbering the previous values.
* [JCBC-2028](https://issues.couchbase.com/browse/JCBC-2028): `Cluster.connect` now throws an `IllegalArgumentException` if you pass a pre-built `ClusterEnvironment` and a connection string incompatible with the environment. Before this change, an incompatibility was logged as a warning, and the connection string scheme and parameters were ignored. `ConnectionStringIgnoredEvent` is now deprecated, since the SDK never publishes it anymore.

  * A pre-built environment without TLS enabled is incompatible with a connection string that specifies the secure `couchases` scheme.
  * A pre-built environment is incompatible with a connection string that has parameters.
* [JVMCBC-1159](https://issues.couchbase.com/browse/JVMCBC-1159): Transactions now support upcoming server query\_context changes.

#### [](#bugs-6)Bugs

* [JVMCBC-1157](https://issues.couchbase.com/browse/JVMCBC-1157): The SDK no longer rejects a `PersistTo` requirement in a bucket using the Magma storage engine. Before this change, the SDK would refuse the request because it misidentified Magma buckets as ephemeral (unable to persist documents).
* [JVMCBC-1167](https://issues.couchbase.com/browse/JVMCBC-1167): If you call `CancellationErrorContext.getWaitUntilReadyContext()` on an error context that didn't come from a "wait until ready" request, the method is now guaranteed to return null instead of sometimes throwing a `ClassCastException`.
* [JCBC-2024](https://issues.couchbase.com/browse/JCBC-2024): Fixed a memory leak in ManagerMessageHandler.
* [JVMCBC-1247](https://issues.couchbase.com/browse/JVMCBC-1247): The SDK now throws `InvalidArgumentException: Failed to parse connection string` if the connection string has a syntax error. For example, the following connection string is malformed, because the `couchbase://` part is repeated: `couchbase://foo.example.com,couchbase://bar.example.com`. The correct way to include multiple addresses in a connection string is to specify the scheme only once, and to join addresses with commas, like: `couchbase://foo.example.com,bar.example.com`

### [](#version-3-4-0-24-october-2022)Version 3.4.0 (24 October 2022)

Version 3.4.0 is the first release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/java/3.4.0/Couchbase-Java-Client-3.4.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.4.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.4.0**
* com.couchbase.client:**core-io:2.4.0**
* io.projectreactor:**reactor-core:3.4.24**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 41\. Optional Artifact Version Compatibility__
| Artifact              | Couchbase Version | Built Against        | API Stability |
| --------------------- | ----------------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.2.0             | OpenTelemetry 1.16.0 | Committed     |
| tracing-opentracing   | 1.2.0             | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.4.0             | OpenTelemetry 1.16.0 | Volatile      |
| metrics-micrometer    | 0.4.0             | Micrometer 1.9.2     | Volatile      |

#### [](#improvements-38)Improvements

* [JVMCBC-1102](https://issues.couchbase.com/browse/JVMCBC-1102): Added support for serverless execution environments including AWS Lambda.
* [JCBC-2004](https://issues.couchbase.com/browse/JCBC-2004): Changed `AuthenticationFailureException` error message to indicate that bucket hibernation is now a potential cause. Bucket hibernation is a feature coming in a future Couchbase release.
* [JCBC-1979](https://issues.couchbase.com/browse/JCBC-1979): A transactional `ctx.insert()` now consistently raises a `DocumentAlreadyExistsException` if the document already exists. If this is caught, the transaction is now allowed to continue.
* [JVMCBC-1144](https://issues.couchbase.com/browse/JVMCBC-1144): If your Couchbase Server cluster's root certificate is signed by a well-known certificate authority whose certificate is included in the JVM's trust store, it's no longer necessary to configure the certificate in the securityConfig settings.
* [JVMCBC-1154](https://issues.couchbase.com/browse/JVMCBC-1154): Maintenance dependency bump.

#### [](#bugs-7)Bugs

* [JCBC-2002](https://issues.couchbase.com/browse/JCBC-2002): `expiryTime` will now return an empty optional if no expiry set.
* [JCBC-1987](https://issues.couchbase.com/browse/JCBC-1987): Fixed a problem where `QueryIndexManager.buildDeferredIndexes` would throw `InternalServerFailureException` when building indexes on the default collection if there were also deferred indexes in a different collection.
* [JVMCBC-1141](https://issues.couchbase.com/browse/JVMCBC-1141): Provide required OpenTelemetry span attributes.
* [JVMCBC-1155](https://issues.couchbase.com/browse/JVMCBC-1155): Make sure targeted round robin request keeps retrying if no config is available.

## [](#java-sdk-3-3-releases)Java SDK 3.3 Releases

### [](#version-3-3-4-9-september-2022)Version 3.3.4 (9 September 2022)

Version 3.3.4 is the fifth release of the 3.3 series, and is a maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.3.4/Couchbase-Java-Client-3.3.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.3.4/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.4/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.3.4**
* com.couchbase.client:**core-io:2.3.4**
* io.projectreactor:**reactor-core:3.4.22**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 42\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against        | API Stability |
| --------------------- | ------- | -------------------- | ------------- |
| tracing-opentelemetry | 1.1.4   | OpenTelemetry 1.16.0 | Committed     |
| tracing-opentracing   | 1.1.4   | OpenTracing 0.33.0   | Committed     |
| metrics-opentelemetry | 0.3.4   | OpenTelemetry 1.16.0 | Volatile      |
| metrics-micrometer    | 0.3.4   | Micrometer 1.9.2     | Volatile      |

#### [](#improvements-39)Improvements

* [JVMCBC-1131](https://issues.couchbase.com/browse/JVMCBC-1131): Added ability to track the number of created instances. Users can now set to hard-fail if too many instances are created.
* [JVMCBC-1134](https://issues.couchbase.com/browse/JVMCBC-1134): Updated `MemcachedProtocol::decodeStatus` to be inlineable.
* [JVMCBC-1135](https://issues.couchbase.com/browse/JVMCBC-1135): Moved `Core#reconfiguration` off IO threads.
* [JVMCBC-1143](https://issues.couchbase.com/browse/JVMCBC-1143): Failed telemetry spans will now record their exception and error status.
* [JVMCBC-1145](https://issues.couchbase.com/browse/JVMCBC-1145): Updated maintenance dependencies.
* [JCBC-1985](https://issues.couchbase.com/browse/JCBC-1985): Added optional `Cluster` instance limit.
* [JCBC-1975](https://issues.couchbase.com/browse/JCBC-1975): Added support for a Couchbase Server 7.1 performance optimisation for transactions that reduces memory requirements in clients.
* [JCBC-1989](https://issues.couchbase.com/browse/JCBC-1989): Added `Closeable` capability to the `Cluster` class, which enables usage of the `try-with-resources` pattern.
* [JVMCBC-1139](https://issues.couchbase.com/browse/JVMCBC-1139): Added support for Configuration Profiles. Note that this API is currently marked as `@Stability.Volatile` and could be subject to change.
* [JVMCBC-1126](https://issues.couchbase.com/browse/JVMCBC-1126): Updated metrics and tracing dependencies.

#### [](#bug-fixes-12)Bug Fixes

* [JVMCBC-1125](https://issues.couchbase.com/browse/JVMCBC-1125): Fixed a rare `CompletionException` seen from transactions when a very aggressive cleanup window is configured.
* [JVMCBC-1136](https://issues.couchbase.com/browse/JVMCBC-1136): Removed verbose transactions cleanup debug "stop on" logging that was being logged at INFO level.
* [JCBC-1993](https://issues.couchbase.com/browse/JCBC-1993): Fixed issue where a `NullPointerException` was thrown for a non-existent FTS index.
* [JCBC-1955](https://issues.couchbase.com/browse/JCBC-1955): Fixed a bug where concurrent transactions could hang due to scheduler starvation.

### [](#version-3-3-3-2-august-2022)Version 3.3.3 (2 August 2022)

Version 3.3.3 is the fourth release of the 3.3 series, and is a maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.3.3/Couchbase-Java-Client-3.3.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.3.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.3/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.3.3**
* com.couchbase.client:**core-io:2.3.3**
* io.projectreactor:**reactor-core:3.4.21**
* org.reactivestreams:**reactive-streams:1.0.4**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 43\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against              | API Stability |
| --------------------- | ------- | -------------------------- | ------------- |
| tracing-opentelemetry | 1.1.2   | OpenTelemetry 1.13.0       | Committed     |
| tracing-opentracing   | 1.1.2   | OpenTracing 0.33.0         | Committed     |
| metrics-opentelemetry | 0.3.2   | OpenTelemetry 1.13.0-alpha | Volatile      |
| metrics-micrometer    | 0.3.2   | Micrometer 1.8.4           | Volatile      |

#### [](#improvements-40)Improvements

* [JVMCBC-1116](https://issues.couchbase.com/browse/JVMCBC-1116): Dependency versions have been increased.
* [JVMCBC-1121](https://issues.couchbase.com/browse/JVMCBC-1121): In some rare cases — such as an application crash — a transaction is left for the async cleanup algorithm to finish; by default it will find this within one minute. In cases where this does not happen, this will trigger a warning after two hours — not the two days that was previously the case.

#### [](#bug-fixes-13)Bug Fixes

* [JVMCBC-1110](https://issues.couchbase.com/browse/JVMCBC-1110): Transaction clients now reliably remove themselves from client records on shutdown.
* [JVMCBC-1119](https://issues.couchbase.com/browse/JVMCBC-1119): The num (kv) nodesExt to equal number of nodes check can lead to otherwise healthy clusters being flagged as not ready. The check has been removed, and now the \` Bucket `waitUntilReady` will not timeout on these edge cases.
* [JVMCBC-1120](https://issues.couchbase.com/browse/JVMCBC-1120): `ClusterConfig#allNodeAddresses` now takes global config into account — avoiding the triggering of some unnecessary reconfigurations.
* [JVMCBC-1112](https://issues.couchbase.com/browse/JVMCBC-1112): Deprecated Reactor Processors have been replaced.
* [JVMCBC-1115](https://issues.couchbase.com/browse/JVMCBC-1115): The SDK now allows for configurations with _only_ TLS ports.

### [](#version-3-3-2-6-july-2022)Version 3.3.2 (6 July 2022)

Version 3.3.2 is the third release of the 3.3 series, and is a maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.3.2/Couchbase-Java-Client-3.3.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.3.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.3.2**
* com.couchbase.client:**core-io:2.3.2**
* io.projectreactor:**reactor-core:3.4.17**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 44\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against              | API Stability |
| --------------------- | ------- | -------------------------- | ------------- |
| tracing-opentelemetry | 1.1.2   | OpenTelemetry 1.13.0       | Committed     |
| tracing-opentracing   | 1.1.2   | OpenTracing 0.33.0         | Committed     |
| metrics-opentelemetry | 0.3.2   | OpenTelemetry 1.13.0-alpha | Volatile      |
| metrics-micrometer    | 0.3.2   | Micrometer 1.8.4           | Volatile      |

#### [](#bug-fixes-14)Bug Fixes

* [JVMCBC-1103](https://issues.couchbase.com/browse/JVMCBC-1103): To reduce overhead, the `MAX_PARALLEL_FETCH` value in `KeyValueBucketRefresher` has been updated to only fetch one config per poll interval.
* [JVMCBC-1104](https://issues.couchbase.com/browse/JVMCBC-1104): Fixed issue where the global refresher did not honor the config poll interval.

### [](#version-3-3-1-8-june-2022)Version 3.3.1 (8 June 2022)

Version 3.3.1 is the second release of the 3.3 series, and is a maintenance release.

[Download](https://packages.couchbase.com/clients/java/3.3.1/Couchbase-Java-Client-3.3.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.3.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.1/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.3.1**
* com.couchbase.client:**core-io:2.3.1**
* io.projectreactor:**reactor-core:3.4.17**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 45\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against              | API Stability |
| --------------------- | ------- | -------------------------- | ------------- |
| tracing-opentelemetry | 1.1.1   | OpenTelemetry 1.13.0       | Committed     |
| tracing-opentracing   | 1.1.1   | OpenTracing 0.33.0         | Committed     |
| metrics-opentelemetry | 0.3.1   | OpenTelemetry 1.13.0-alpha | Volatile      |
| metrics-micrometer    | 0.3.1   | Micrometer 1.8.4           | Volatile      |

#### [](#improvements-41)Improvements

* [JVMCBC-1089](https://issues.couchbase.com/browse/JVMCBC-1089): SDK users can now customize the `ConsoleLogger` format.
* [JVMCBC-1093](https://issues.couchbase.com/browse/JVMCBC-1093): Previously, when a DNS SRV lookup failure occured, the SDK logged this as a `WARNING` along with a stack trace. The lookup failure is typically harmless, so the log message has now been downgraded to `INFO` level, without a stack trace.
* [JVMCBC-1088](https://issues.couchbase.com/browse/JVMCBC-1088): Updated Netty to version `4.1.77.Final`.

### [](#version-3-3-0-26-april-2022)Version 3.3.0 (26 April 2022)

Version 3.3.0 is the first release of the 3.3 series.

The three headline changes in this release:

* Supports the new functionality of Couchbase Server 7.1.
* Directly integrates transactions into the SDK rather than requiring a separate library. Existing users of the transactions library can refer to the [Distributed Transactions Migration Guide](distributed-acid-transactions-migration-guide.md) to see the simple steps needed to migrate, which we recommend.
* Bundles the public server security certificates for Couchbase Capella, to make it easier for users to get started with Capella.

[Download](https://packages.couchbase.com/clients/java/3.3.0/Couchbase-Java-Client-3.3.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.3.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.3.0**
* com.couchbase.client:**core-io:2.3.0**
* io.projectreactor:**reactor-core:3.4.17**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 46\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against              | API Stability |
| --------------------- | ------- | -------------------------- | ------------- |
| tracing-opentelemetry | 1.1.0   | OpenTelemetry 1.13.0       | Committed     |
| tracing-opentracing   | 1.1.0   | OpenTracing 0.33.0         | Committed     |
| metrics-opentelemetry | 0.3.0   | OpenTelemetry 1.13.0-alpha | Volatile      |
| metrics-micrometer    | 0.3.0   | Micrometer 1.8.4           | Volatile      |

#### [](#improvements-42)Improvements

* [JCBC-1929](https://issues.couchbase.com/browse/JCBC-1929): Integrated transactions library into SDK.
* [JVMCBC-1070](https://issues.couchbase.com/browse/JVMCBC-1070): Bundled public Capella CA certificate.
* [JVMCBC-1074](https://issues.couchbase.com/browse/JVMCBC-1074): If you try to connect to Capella without enabling TLS, now you'll get an exception that says TLS is required (instead of an `UnknownHostException`).
* [JVMCBC-1076](https://issues.couchbase.com/browse/JVMCBC-1076): Deprecated `Event.createdAt()` in favor of a version that returns an `Instant`.
* [JVMCBC-1078](https://issues.couchbase.com/browse/JVMCBC-1078): Made `schedulerThreadCount` customizable.
* [JVMCBC-1079](https://issues.couchbase.com/browse/JVMCBC-1079): Added ConnectionString SDK 3 compatibility attributes.
* [JVMCBC-1082](https://issues.couchbase.com/browse/JVMCBC-1082): Updated maintenance dependencies.
* [JVMCBC-1085](https://issues.couchbase.com/browse/JVMCBC-1085): Exposed last connect attempt failure through `Diagnostics`.
* [JCBC-1886](https://issues.couchbase.com/browse/JCBC-1886): Allow to list the number of currently available replicas for a document ID.
* [JCBC-1923](https://issues.couchbase.com/browse/JCBC-1923): Added warning when ignoring connection string parameters or scheme.

#### [](#bugs-8)Bugs

* [JCBC-1922](https://issues.couchbase.com/browse/JCBC-1922): `NOT_STORED` when inserting a document will now correctly raise a `DocumentAlreadyExistsException` (rather than a `DocumentNotFoundException` as before).
* [JVMCBC-1077](https://issues.couchbase.com/browse/JVMCBC-1077): Shutting down a ClusterEnvironment now correctly stops a `Meter` owned by the cluster. This plugs a resource leak where `LoggingMeter` worker threads would never be stopped.

## [](#java-sdk-3-2-releases)Java SDK 3.2 Releases

### [](#version-3-2-7-25-april-2022)Version 3.2.7 (25 April 2022)

Version 3.2.7 is the eighth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/java/3.2.7/Couchbase-Java-Client-3.2.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.7/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.7/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.7**
* com.couchbase.client:**core-io:2.2.7**
* io.projectreactor:**reactor-core:3.4.17**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 47\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.7   | OpenTelemetry 1.9.1       | Committed     |
| tracing-opentracing   | 1.0.7   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.7   | OpenTelemetry 1.7.1-alpha | Volatile      |
| metrics-micrometer    | 0.2.7   | Micrometer 1.7.5          | Volatile      |

#### [](#bugs-9)Bugs

* [JCBC-1922](https://issues.couchbase.com/browse/JCBC-1922): The KeyValue error code `NOT_STORED` is now properly mapped to `DocumentExistsException` on `insert` and `mutateIn`.
* [JVMCBC-1077](https://issues.couchbase.com/browse/JVMCBC-1077): The environment now properly shuts down the `Meter` if it is owned and not passed in externally.

#### [](#improvements-43)Improvements

* [JVMCBC-1082](https://issues.couchbase.com/browse/JVMCBC-1082): Updated internal and external dependencies.
* Netty from 4.1.73 to 4.1.76
* Jackson from 2.13.1 to 2.13.2 (and 2.13.2.2)
* Reactor from 3.4.14 to 3.4.17

### [](#version-3-2-6-2-march-2022)Version 3.2.6 (2 March 2022)

Version 3.2.6 is the seventh release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/java/3.2.6/Couchbase-Java-Client-3.2.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.6/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.6/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.6**
* com.couchbase.client:**core-io:2.2.6**
* io.projectreactor:**reactor-core:3.4.14**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 48\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.6   | OpenTelemetry 1.9.1       | Committed     |
| tracing-opentracing   | 1.0.6   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.6   | OpenTelemetry 1.7.1-alpha | Volatile      |
| metrics-micrometer    | 0.2.6   | Micrometer 1.7.5          | Volatile      |

#### [](#bugs-10)Bugs

* [JVMCBC-1060](https://issues.couchbase.com/browse/JVMCBC-1060): Fixed an issue where rate limited exceptions were not thrown for `SearchIndexManager` errors.
* [JVMCBC-1071](https://issues.couchbase.com/browse/JVMCBC-1071): The SDK now ensures that negative values are not sent to the `ValueRecorder`.
* [JCBC-1918](https://issues.couchbase.com/browse/JCBC-1918): Executing a Full-Text Search query with an open-ended date range facet no longer results in a `NullPointerException`.
* [JCBC-1919](https://issues.couchbase.com/browse/JCBC-1919): Index fields are now quoted in the analytics index manager.
* [JCBC-1921](https://issues.couchbase.com/browse/JCBC-1921): QueryIndexManager `buildDeferredIndexes` no longer throws a `ParsingFailureException` against Couchbase Server 6.0.

#### [](#new-features-4)New Features

* [JVMCBC-1057](https://issues.couchbase.com/browse/JVMCBC-1057): Added core infrastructure for the Backup service. Users can now make custom HTTP requests to the Backup service.
* [JVMCBC-1064](https://issues.couchbase.com/browse/JVMCBC-1064): When implementing a custom `RetryStrategy`, a new overload of `RetryAction.noRetry` lets you specify an exception translator for converting the default request cancellation exception into your preferred exception class.

#### [](#improvements-44)Improvements

* [JVMCBC-1065](https://issues.couchbase.com/browse/JVMCBC-1065): `RetryReason.allowsNonIdempotentRetry()` is now public, so you can call it from a custom `RetryStrategy`.
* [JVMCBC-1066](https://issues.couchbase.com/browse/JVMCBC-1066): When `SecurityConfig.Builder.trustCertificate(Path)` is given a file containing more than one certificate, it now trusts all the certificates instead of just the first one. Likewise, the result of `SecurityConfig.decodeCertificates(List<String>)` now includes all certificates in each string, not just the first certificate in each string.
* [JVMCBC-1068](https://issues.couchbase.com/browse/JVMCBC-1068): Added explicit handling of `FeatureNotAvailable` for Magma on CE.
* [JVMCBC-1069](https://issues.couchbase.com/browse/JVMCBC-1069): Added explicit handling of `FeatureNotAvailable` for Query CE.
* [JCBC-1916](https://issues.couchbase.com/browse/JCBC-1916): Updated the Analytics Management API Javadocs.
* [JCBC-1917](https://issues.couchbase.com/browse/JCBC-1917): You can now configure properties of the `ClusterEnvironment` without having to build and shut down the environment. The new `ClusterOptions.environment(Consumer<ClusterEnvironment.Builder>)` method lets you configure properties of a `ClusterEnvironment` owned by the Cluster, so you don't need to manage the environment yourself. Example usage:

Cluster cluster = Cluster.connect("localhost", clusterOptions(username, password)
    .environment(env -> env.ioConfig().captureTraffic(ServiceType.MANAGER)));

### [](#version-3-2-5-2-february-2022)Version 3.2.5 (2 February 2022)

Version 3.2.5 is the sixth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/java/3.2.5/Couchbase-Java-Client-3.2.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.5/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.5/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.5**
* com.couchbase.client:**core-io:2.2.5**
* io.projectreactor:**reactor-core:3.4.14**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 49\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.5   | OpenTelemetry 1.9.1       | Committed     |
| tracing-opentracing   | 1.0.5   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.5   | OpenTelemetry 1.7.1-alpha | Volatile      |
| metrics-micrometer    | 0.2.5   | Micrometer 1.7.5          | Volatile      |

#### [](#api-impacting-3)API Impacting

* [JCBC-1901](https://issues.couchbase.com/browse/JCBC-1901): Removed the Azure link type from the analytics management API, due to a change in the underlying server API. (Note that this interface is marked @Stability.Volatile indicating that it can change.)

#### [](#bugs-11)Bugs

* [JCBC-1895](https://issues.couchbase.com/browse/JCBC-1895): Fixed an issue where `lookupInResult.contentAs(0, Boolean.class)` was throwing a `DecodingFailureException` on a Sub-Document exists operation.
* [JCBC-1896](https://issues.couchbase.com/browse/JCBC-1896): Fixed an issue where `JsonValueSerializerWrapper` was unable to support decoding via TypeRef.
* [JCBC-1904](https://issues.couchbase.com/browse/JCBC-1904): Fixed issues with constant and URL bindings and also introduced convenience methods to load a function from raw JSON.
* [JVMCBC-1046](https://issues.couchbase.com/browse/JVMCBC-1046): Added fix to not load the global config if a node is not in the seed node list anymore.
* [JVMCBC-1058](https://issues.couchbase.com/browse/JVMCBC-1058): The SDK now throws a more descriptive `FeatureNotAvailableException` for scopes and collections on memcached buckets.

#### [](#improvements-45)Improvements

* [JCBC-1860](https://issues.couchbase.com/browse/JCBC-1860): `ConflictResolutionType.CUSTOM` has now been added to the bucket management API.
* [JCBC-1864](https://issues.couchbase.com/browse/JCBC-1864): FTS options now include `IncludeLocations` and `Operator`.
* [JCBC-1876](https://issues.couchbase.com/browse/JCBC-1876): Query API now supports preserving TTL.
* [JCBC-1882](https://issues.couchbase.com/browse/JCBC-1882): Index management API now supports managing indexes for a collection.
* [JCBC-1898](https://issues.couchbase.com/browse/JCBC-1898): Added convenience method for getting raw bytes from `GetResult`.
* [JCBC-1902](https://issues.couchbase.com/browse/JCBC-1902): The SDK now sends the configured user timeout to search.
* [JCBC-1905](https://issues.couchbase.com/browse/JCBC-1905): Added convenience methods for loading eventing function JSON.
* [JCBC-1909](https://issues.couchbase.com/browse/JCBC-1909): Added `scanWait` to `AnalyticsOptions`.
* [JCBC-1903](https://issues.couchbase.com/browse/JCBC-1903): Added javadocs for bucket management API.
* [JCBC-1908](https://issues.couchbase.com/browse/JCBC-1908): Added javadocs for query index management APIs.
* [JVMCBC-1055](https://issues.couchbase.com/browse/JVMCBC-1055), [JVMCBC-1047](https://issues.couchbase.com/browse/JVMCBC-1047), [JVMCBC-1051](https://issues.couchbase.com/browse/JVMCBC-1051): Updated dependencies. Netty goes from 4.1.72.Final to 4.1.73.Final. Jackson from 2.13.0 to 2.13.1\. Reactor from 3.4.12 to 3.4.14\. log4j (an optional dependency) from 2.15.0 to 2.17.1.
* [JVMCBC-1037](https://issues.couchbase.com/browse/JVMCBC-1037): Added a minor performance optimisation that avoids `whenComplete` closure for timeout cancellation.
* [JVMCBC-1045](https://issues.couchbase.com/browse/JVMCBC-1045): Added an internal watchdog that updates the cluster configuration if the number of nodes changes.
* [JVMCBC-1048](https://issues.couchbase.com/browse/JVMCBC-1048): Added change that ensures the SDK always sets `RequestContext` on `RequestSpan`.
* [JVMCBC-1056](https://issues.couchbase.com/browse/JVMCBC-1056): Added more log information on unexpected endpoint disconnect.
* [JVMCBC-1059](https://issues.couchbase.com/browse/JVMCBC-1059): The SDK now handles any `retry:true` field in a query error result by retrying it.

### [](#version-3-2-4-9-december-2021)Version 3.2.4 (9 December 2021)

Version 3.2.4 is the fifth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/java/3.2.4/Couchbase-Java-Client-3.2.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.4/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.4/)

> [!NOTE]
> This release introduces support for JDK 17\.

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.4**
* com.couchbase.client:**core-io:2.2.4**
* io.projectreactor:**reactor-core:3.4.12**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 50\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.4   | OpenTelemetry 1.7.1       | Committed     |
| tracing-opentracing   | 1.0.4   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.4   | OpenTelemetry 1.7.1-alpha | Volatile      |
| metrics-micrometer    | 0.2.4   | Micrometer 1.7.5          | Volatile      |

#### [](#bugs-12)Bugs

* [JCBC-1892](https://issues.couchbase.com/browse/JCBC-1892): `EventingFunctionSettings` can now be empty - this fixes an issue with loading eventing functions from the cluster.

#### [](#improvements-46)Improvements

* [JVMCBC-1033](https://issues.couchbase.com/browse/JVMCBC-1033), [JVMCBC-1034](https://issues.couchbase.com/browse/JVMCBC-1034): Updated internal and external dependencies to their latest bugfix versions. This also updates OpenTelemetry to 1.7.x.
* [JCBC-1881](https://issues.couchbase.com/browse/JCBC-1881): Added (volatile) support for the `magma` storage backend when creating a bucket through the bucket manager.
* [JVMCBC-1035](https://issues.couchbase.com/browse/JVMCBC-1035): The (internal) `subDocumentField` is now serializable - this is needed for apache spark integration.
* [JVMCBC-1032](https://issues.couchbase.com/browse/JVMCBC-1032): Added (volatile) support for Rate/Quota Limits. This is needed for Couchbase Capella.
* [JVMCBC-1039](https://issues.couchbase.com/browse/JVMCBC-1039): Included `httpStatus` in Query and Analytics Error Context, as well as the `vbucket` in the KV error context. This helps with debugging.

### [](#version-3-2-3-2-november-2021)Version 3.2.3 (2 November 2021)

Version 3.2.3 is the fourth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/java/3.2.3/Couchbase-Java-Client-3.2.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.3/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.3**
* com.couchbase.client:**core-io:2.2.3**
* io.projectreactor:**reactor-core:3.4.9**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 51\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.3   | OpenTelemetry 1.3.0       | Committed     |
| tracing-opentracing   | 1.0.3   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.3   | OpenTelemetry 1.3.0-alpha | Volatile      |
| metrics-micrometer    | 0.2.3   | Micrometer 1.7.0          | Volatile      |

#### [](#improvements-47)Improvements

* [JVMCBC-1026](https://issues.couchbase.com/browse/JVMCBC-1026): Support for error map v2 has been added to ensure the config can be parsed without failure.

### [](#version-3-2-2-6-october-2021)Version 3.2.2 (6 October 2021)

Version 3.2.2 is the third release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/java/3.2.2/Couchbase-Java-Client-3.2.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.2**
* com.couchbase.client:**core-io:2.2.2**
* io.projectreactor:**reactor-core:3.4.9**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 52\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.2   | OpenTelemetry 1.3.0       | Committed     |
| tracing-opentracing   | 1.0.2   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.2   | OpenTelemetry 1.3.0-alpha | Volatile      |
| metrics-micrometer    | 0.2.2   | Micrometer 1.7.0          | Volatile      |

#### [](#improvements-48)Improvements

* [JCBC-1872](https://issues.couchbase.com/browse/JCBC-1872): Bring `NodeLocatorHelper` to SDK 3 from 2.
* [JCBC-1875](https://issues.couchbase.com/browse/JCBC-1875): Document and polish Eventing Management API.
* [JVMCBC-1015](https://issues.couchbase.com/browse/JVMCBC-1015): Improve client side error message when TLS is enforced on the server side.
* [JVMCBC-1016](https://issues.couchbase.com/browse/JVMCBC-1016): Gracefully handle more invalid connection string cases.
* [JVMCBC-1022](https://issues.couchbase.com/browse/JVMCBC-1022): Batch-Log messages in DefaultEventBus. Now events which are overflowing are not directly logged to stderr but rather batched up and logged at interval. Note that this implies some "loss of precision", as not all dropped events are logged - one event per type is preserved.

#### [](#bugs-13)Bugs

* [JVMCBC-1017](https://issues.couchbase.com/browse/JVMCBC-1017): Fixed issue with Threshold Logging Tracing not working due to `RequestContext` not being set.
* [JCBC-1873](https://issues.couchbase.com/browse/JCBC-1873): Rename EventingFunction to `validate_ssl_certificates` to conform to spec.
* [JVMCBC-1020](https://issues.couchbase.com/browse/JVMCBC-1020): Added `target` property to `QueryRequest` and ensured it is honored for prepare and execute, so they are both run on the same node. This fix removes need for `TargetedQueryRequest`.

### [](#version-3-2-1-1-september-2021)Version 3.2.1 (1 September 2021)

Version 3.2.1 is the second release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/java/3.2.1/Couchbase-Java-Client-3.2.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.1/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.1**
* com.couchbase.client:**core-io:2.2.1**
* io.projectreactor:**reactor-core:3.4.9**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 53\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.1   | OpenTelemetry 1.3.0       | Committed     |
| tracing-opentracing   | 1.0.1   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.1   | OpenTelemetry 1.3.0-alpha | Volatile      |
| metrics-micrometer    | 0.2.1   | Micrometer 1.7.0          | Volatile      |

#### [](#known-issues)Known Issues

* [JVMCBC-1017](https://issues.couchbase.com/browse/JVMCBC-1017): The `ThresholdLoggingTracer` will not record any request and will not log them into the log file. If you rely on this functionality please use 3.1.7 as only 3.2.0 and 3.2.1 are affected. This issue will be addressed in 3.2.2.

#### [](#bug-fixes-15)Bug Fixes

* [JVMCBC-1002](https://issues.couchbase.com/browse/JVMCBC-1002): Default log level reverted to INFO.
* [JVMCBC-1007](https://issues.couchbase.com/browse/JVMCBC-1007): `LoggingMeter` was incorrectly marked as Volatile in SDK 3.2 — now fixed.
* [JCBC-1850](https://issues.couchbase.com/browse/JCBC-1850): Fixed `NullPointerException` with `OpenTracing`.

#### [](#improvements-49)Improvements

* [JCBC-1732](https://issues.couchbase.com/browse/JCBC-1732): Eventing Management API added.
* [JCBC-1852](https://issues.couchbase.com/browse/JCBC-1852): FLE: Optionally read @Encrypted POJO properties from unencrypted JSON fields.
* [JCBC-1858](https://issues.couchbase.com/browse/JCBC-1858): Added convenience method for getting raw JSON bytes from `LookupInResult`.
* [JCBC-1859](https://issues.couchbase.com/browse/JCBC-1859): Allow to create `CollectionSpec` for default scope.
* [JCBC-1868](https://issues.couchbase.com/browse/JCBC-1868): Make `JsonValueModule` compatible with Jackson < 2.8.
* [JVMCBC-1010](https://issues.couchbase.com/browse/JVMCBC-1010): Maintenance dependency bump.
* [JVMCBC-990](https://issues.couchbase.com/browse/JVMCBC-990): Fixed `WaitUntilReady` timing out with 6.0.x and unhealthy seed nodes.
* [JVMCBC-999](https://issues.couchbase.com/browse/JVMCBC-999): Properly map server query timeout while streaming.
* [JVMCBC-1004](https://issues.couchbase.com/browse/JVMCBC-1004): Configure and apply default log level for `ConsoleLogger`.
* [JVMCBC-1005](https://issues.couchbase.com/browse/JVMCBC-1005): Allow to export Context as Map.
* [JVMCBC-1006](https://issues.couchbase.com/browse/JVMCBC-1006): `ErrorContext` must be included in message.

### [](#version-3-2-0-20-july-2021)Version 3.2.0 (20 July 2021)

Version 3.2.0 is the first release of the 3.2 series. It promotes to GA support for the scopes and collections provided by Couchbase Server 7.0, and also OpenTelemetry.

[Download](https://packages.couchbase.com/clients/java/3.2.0/Couchbase-Java-Client-3.2.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.2.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.2.0**
* com.couchbase.client:**core-io:2.2.0**
* io.projectreactor:**reactor-core:3.4.6**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 54\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 1.0.0   | OpenTelemetry 1.3.0       | Committed     |
| tracing-opentracing   | 1.0.0   | OpenTracing 0.33.0        | Committed     |
| metrics-opentelemetry | 0.2.0   | OpenTelemetry 1.3.0-alpha | Volatile      |
| metrics-micrometer    | 0.2.0   | Micrometer 1.7.0          | Volatile      |

#### [](#known-issues-2)Known Issues

* [JVMCBC-1017](https://issues.couchbase.com/browse/JVMCBC-1017): The `ThresholdLoggingTracer` will not record any request and will not log them into the log file. If you rely on this functionality please use 3.1.7 as only 3.2.0 and 3.2.1 are affected. This issue will be addressed in 3.2.2.

#### [](#bug-fixes-16)Bug Fixes

* [JVMCBC-949](https://issues.couchbase.com/browse/JVMCBC-949): Opening a non-default collection on an memcached bucket now fails fast.
* [JVMCBC-983](https://issues.couchbase.com/browse/JVMCBC-983): Ignore slow subscribers on certain Flux intervals.
* [JCBC-1822](https://issues.couchbase.com/browse/JCBC-1822): `BatchHelper` now supports MDS deployments.

#### [](#interface-changes)Interface Changes

All interface changes are to interfaces that are currently in beta and marked `@Stability.Volatile` or `@Stability.Uncommitted`.

* [JVMCBC-978](https://issues.couchbase.com/browse/JVMCBC-978): Rename `AggregatingMeter` to `LoggingMeter`.
* [JVMCBC-934](https://issues.couchbase.com/browse/JVMCBC-934): Threshold and Orphan output is now in new format.
* [JVMCBC-979](https://issues.couchbase.com/browse/JVMCBC-979): Rename `ThresholdRequestTracer` to `ThresholdLoggingTracer`.
* [JCBC-1823](https://issues.couchbase.com/browse/JCBC-1823): Promote collection APIs from Volatile to Committed.
* [JCBC-1844](https://issues.couchbase.com/browse/JCBC-1844): Promote `BatchHelper` from Volatile to Uncommitted.

#### [](#improvement-2)Improvement

* [JVMCBC-980](https://issues.couchbase.com/browse/JVMCBC-980): Add exception wrappers to Tracers and Meters.
* [JVMCBC-987](https://issues.couchbase.com/browse/JVMCBC-987): Allow supplying an SDK2-compatible memcached hashing strategy.
* [JVMCBC-988](https://issues.couchbase.com/browse/JVMCBC-988): Map Query Error 13014 to `AuthenticationException`.
* [JVMCBC-989](https://issues.couchbase.com/browse/JVMCBC-989): Add timeout\_ms to threshold logging tracer output.
* [JVMCBC-991](https://issues.couchbase.com/browse/JVMCBC-991): Optimize metric dispatching.
* [JVMCBC-992](https://issues.couchbase.com/browse/JVMCBC-992): Cache NodeIdentifier in NodeInfo.
* [JVMCBC-993](https://issues.couchbase.com/browse/JVMCBC-993): Optimize early discard of events which are not going to be logged.
* [JVMCBC-996](https://issues.couchbase.com/browse/JVMCBC-996): Throw `FeatureNotAvailableException` if scope level queries are not available.
* [JVMCBC-997](https://issues.couchbase.com/browse/JVMCBC-997): Duplicate attributes from dispatch\_to\_server to improve tracing.
* [JVMCBC-998](https://issues.couchbase.com/browse/JVMCBC-998): Performance: Do not set tracing spans if not needed.
* [JVMCBC-981](https://issues.couchbase.com/browse/JVMCBC-981): Support CoreHttpClient requests to manager service.
* [JVMCBC-984](https://issues.couchbase.com/browse/JVMCBC-984): Dependency bump: Netty 4.1.63 to 4.1.65, micrometer 1.6.6 to 1.7.0.
* [JCBC-1242](https://issues.couchbase.com/browse/JCBC-1242), [JCBC-1837](https://issues.couchbase.com/browse/JCBC-1837): Add OSGi bundle.
* [JCBC-1787](https://issues.couchbase.com/browse/JCBC-1787): Validate expiry instants.
* [JCBC-1838](https://issues.couchbase.com/browse/JCBC-1838): Add support for SDK2-compatible `LegacyTranscoder`.
* [JCBC-1841](https://issues.couchbase.com/browse/JCBC-1841): Update OpenTelemetry to 1.3.0.

## [](#java-sdk-3-1-releases)Java SDK 3.1 Releases

### [](#version-3-1-8-1-march-2022)Version 3.1.8 (1 March 2022)

Version 3.1.8 is the ninth release of the 3.1 series, bringing stabilizations over 3.1.7.

[Download](https://packages.couchbase.com/clients/java/3.1.8/Couchbase-Java-Client-3.1.8.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.8/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.8/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.8**
* com.couchbase.client:**core-io:2.1.8**
* io.projectreactor:**reactor-core:3.4.15**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 55\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 0.3.8   | OpenTelemetry 1.2.0       | Volatile      |
| tracing-opentracing   | 0.3.8   | OpenTracing 0.33.0        | Volatile      |
| metrics-opentelemetry | 0.1.8   | OpenTelemetry 1.2.0-alpha | Volatile      |
| metrics-micrometer    | 0.1.8   | Micrometer 1.6.6          | Volatile      |

#### [](#bug-fixes-17)Bug Fixes

* [JVMCBC-1067](https://issues.couchbase.com/browse/JVMCBC-1067): Internal and external maintenance dependencies are updated to their latest available bugfix releases (including Netty to 4.1.74.Final).
* [JVMCBC-1046](https://issues.couchbase.com/browse/JVMCBC-1046): Added fix to not load the global config if a node is not in the seed node list anymore.
* [JVMCBC-1006](https://issues.couchbase.com/browse/JVMCBC-1006): `ErrorContext` is now included in the message of a `CouchbaseException`.
* [JCBC-1895](https://issues.couchbase.com/browse/JVMCBC-1895): Fixed an issue where `lookupInResult.contentAs(0, Boolean.class)` was throwing a `DecodingFailureException` on a Sub-Document exists operation.
* [JCBC-1896](https://issues.couchbase.com/browse/JVMCBC-1896): Fixed an issue where `JsonValueSerializerWrapper` was unable to support decoding via TypeRef.

### [](#version-3-1-7-11-august-2021)Version 3.1.7 (11 August 2021)

Version 3.1.7 is the eigth release of the 3.1 series, bringing stabilizations and enhancements over 3.1.6.

[Download](https://packages.couchbase.com/clients/java/3.1.7/Couchbase-Java-Client-3.1.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.7/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.7/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.7**
* com.couchbase.client:**core-io:2.1.7**
* io.projectreactor:**reactor-core:3.4.6**
* org.reactivestreams:**reactive-streams:1.0.3**

Optional artifacts on top of this SDK version are tested for the following compatibilities:

__Table 56\. Optional Artifact Version Compatibility__
| Artifact              | Version | Built Against             | API Stability |
| --------------------- | ------- | ------------------------- | ------------- |
| tracing-opentelemetry | 0.3.7   | OpenTelemetry 1.2.0       | Volatile      |
| tracing-opentracing   | 0.3.7   | OpenTracing 0.33.0        | Volatile      |
| metrics-opentelemetry | 0.1.7   | OpenTelemetry 1.2.0-alpha | Volatile      |
| metrics-micrometer    | 0.1.7   | Micrometer 1.6.6          | Volatile      |

#### [](#bug-fixes-18)Bug Fixes

* [JVMCBC-949](https://issues.couchbase.com/browse/JVMCBC-949): Opening a non-default collection on an memcached bucket now fails fast.
* [JVMCBC-983](https://issues.couchbase.com/browse/JVMCBC-983): Ignore slow subscribers on certain Flux intervals.
* [JCBC-1822](https://issues.couchbase.com/browse/JCBC-1822): `BatchHelper` now supports MDS deployments.
* [JCBC-1850](https://issues.couchbase.com/browse/JCBC-1850): Ignore null values for attributed in OpenTelemetry and OpenTracing.
* [JVMCBC-990](https://issues.couchbase.com/browse/JVMCBC-990): Gracefully handle cluster-level WaitUntilReady against clusters < 6.5.

#### [](#improvements-50)Improvements

* [JVMCBC-996](https://issues.couchbase.com/browse/JVMCBC-996): Throw `FeatureNotAvailableException` if scope level queries are not available.
* [JVMCBC-988](https://issues.couchbase.com/browse/JVMCBC-988): Query error code 13014 is now mapped to `AuthenticationException`.
* [JCBC-1838](https://issues.couchbase.com/browse/JCBC-1838): Add support for SDK2-compatible `LegacyTranscoder`.
* [JVMCBC-987](https://issues.couchbase.com/browse/JVMCBC-987): Allow supplying an SDK2-compatible memcached hashing strategy.
* [JVMCBC-999](https://issues.couchbase.com/browse/JVMCBC-999): Properly map server query timeout while streaming.

### [](#version-3-1-6-4-june-2021)Version 3.1.6 (4 June 2021)

Version 3.1.6 is the seventh release of the 3.1 series, bringing stabilizations and enhancements over 3.1.5.

[Download](https://packages.couchbase.com/clients/java/3.1.6/Couchbase-Java-Client-3.1.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.6/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.6/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.6**
* com.couchbase.client:**core-io:2.1.6**
* io.projectreactor:**reactor-core:3.4.6**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-19)Bug Fixes

* [JCBC-1676](https://issues.couchbase.com/browse/JCBC-1676): Bucket creation now succeeds against Community Edition 6.5 and above.
* [JVMCBC-972](https://issues.couchbase.com/browse/JVMCBC-972): Only open one GCCCP connection per node.

#### [](#improvements-51)Improvements

* [JCBC-1808](https://issues.couchbase.com/browse/JCBC-1808): Updated tracing and metrics module dependencies.
* [JCBC-1649](https://issues.couchbase.com/browse/JCBC-1649): Update analytics management API to support compound dataverse names.
* [JCBC-1815](https://issues.couchbase.com/browse/JCBC-1815): Improve error context for BatchHelper.
* [JVMCBC-939](https://issues.couchbase.com/browse/JVMCBC-939): Improve no collection access handling.
* [JVMCBC-974](https://issues.couchbase.com/browse/JVMCBC-974): Restructure AggregatingMeter output format.
* [JVMCBC-975](https://issues.couchbase.com/browse/JVMCBC-975): Further improve wait until ready diagnostics.
* [JVMCBC-977](https://issues.couchbase.com/browse/JVMCBC-977): Improve bucket configuration handling (revEpoch).

### [](#version-3-1-5-6-may-2021)Version 3.1.5 (6 May 2021)

Version 3.1.5 is the sixth release of the 3.1 series, bringing stabilizations and enhancements over 3.1.4.

[Download](https://packages.couchbase.com/clients/java/3.1.5/Couchbase-Java-Client-3.1.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.5/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.5/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.5**
* com.couchbase.client:**core-io:2.1.5**
* io.projectreactor:**reactor-core:3.4.5**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-20)Bug Fixes

* [JCBC-1804](https://issues.couchbase.com/browse/JCBC-1804): Ensure `contentAsObject/Array()` works with a custom JsonSerializer.
* [JVMCBC-965](https://issues.couchbase.com/browse/JVMCBC-965): Better error logging during bucket failures, which helps with troubleshooting.
* [JVMCBC-963](https://issues.couchbase.com/browse/JVMCBC-963): Add better retry handling for local and global bucket config fetch failures, making it more resilient.
* [JVMCBC-967](https://issues.couchbase.com/browse/JVMCBC-967): Work around and fix a `OverflowException` with `PersistTo`/`ReplicateTo`, caused by Reactor.

#### [](#improvements-52)Improvements

* [JVMCBC-958](https://issues.couchbase.com/browse/JVMCBC-958): Improve the performance of individual collection ID fetches, speeding up the time of bootstrap whan a lot of collections are opened.
* [JCBC-1756](https://issues.couchbase.com/browse/JCBC-1756): Adds volatile support for preserving the expiry on certain mutation operations.
* [JVMCBC-959](https://issues.couchbase.com/browse/JVMCBC-959): Allow `IoEnvironment` config to be overridden by system properties.
* [JCBC-1801](https://issues.couchbase.com/browse/JCBC-1801): Allow to create a `SearchIndex` from a JSON definition.
* [JVMCBC-962](https://issues.couchbase.com/browse/JVMCBC-962): Add (internal, volatile) request callback functionality.
* [JCBC-1733](https://issues.couchbase.com/browse/JCBC-1733): Add support for collections to `SearchOptions`.

### [](#version-3-1-4-7-april-2021)Version 3.1.4 (7 April 2021)

Version 3.1.4 is the fifth release of the 3.1 series, bringing stabilizations and enhancements over 3.1.3.

[Download](https://packages.couchbase.com/clients/java/3.1.4/Couchbase-Java-Client-3.1.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.4/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.4/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.4**
* com.couchbase.client:**core-io:2.1.4**
* io.projectreactor:**reactor-core:3.4.4**
* org.reactivestreams:**reactive-streams:1.0.3**

> [!WARNING]
> Due to protocol level changes, Java SDK 3.1.4 and later are not compatible with _pre-release_ versions of Couchbase Server 7.0\.

#### [](#bug-fixes-21)Bug Fixes

* [JCBC-1798](https://issues.couchbase.com/browse/JCBC-1798): Fixes ViewResult.metaData() throwing Exception when debug=true.
* [JVMCBC-940](https://issues.couchbase.com/browse/JVMCBC-940): Better error handling of collection ID fetch failures.
* [JVMCBC-948](https://issues.couchbase.com/browse/JVMCBC-948): CAS is only usable with Sub-Document when using StoreSemantics.REPLACE. This server-side restriction is now also checked client-side, and a `InvalidArgumentException` raised.
* [JVMCBC-950](https://issues.couchbase.com/browse/JVMCBC-950): waitUntilReady is now more resilient to just-created buckets.
* [JVMCBC-954](https://issues.couchbase.com/browse/JVMCBC-954): More resilient handling of rebalances.

#### [](#improvements-53)Improvements

* [JCBC-1786](https://issues.couchbase.com/browse/JCBC-1786): Transcoders now allow contentAs(Object.class). Java Map and List collections are used to represent JSON objects and arrays.
* [JCBC-1795](https://issues.couchbase.com/browse/JCBC-1795): Allow `MutateInSpec.remove("")`, which removes the entire document.
* [JVMCBC-936](https://issues.couchbase.com/browse/JVMCBC-936): Allow customizing TLS cipher list.
* [JVMCBC-941](https://issues.couchbase.com/browse/JVMCBC-941): Support modified protocol for collections in Couchbase Server 7.0 (in beta).
* [JVMCBC-943](https://issues.couchbase.com/browse/JVMCBC-943): Apply OpenTelemetry best practices.
* [JVMCBC-944](https://issues.couchbase.com/browse/JVMCBC-944): Add implementation version to OpenTelemetry APIs.
* [JVMCBC-947](https://issues.couchbase.com/browse/JVMCBC-947): Remove request counter metric.
* [JVMCBC-951](https://issues.couchbase.com/browse/JVMCBC-951): Move GetAny/AllReplicas into core.
* [JVMCBC-955](https://issues.couchbase.com/browse/JVMCBC-955): Distinguish between CAS mismatch and DML failure on query error.

### [](#version-3-1-3-2-march-2021)Version 3.1.3 (2 March 2021)

Version 3.1.3 is the fourth release of the 3.1 series, bringing stabilizations and enhancements over 3.1.2.

[Download](https://packages.couchbase.com/clients/java/3.1.3/Couchbase-Java-Client-3.1.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.3/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.3/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.3**
* com.couchbase.client:**core-io:2.1.3**
* io.projectreactor:**reactor-core:3.4.3**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-54)Improvements

* [JCBC-1776](https://issues.couchbase.com/browse/JCBC-1776), [JVMCBC-924](https://issues.couchbase.com/browse/JVMCBC-924), [JVMCBC-925](https://issues.couchbase.com/browse/JVMCBC-925): Updated dependencies: OpenTelemetry to 1.0.0, Netty dependency to 4.1.59, netty-tcnative-boringssl-static to 2.0.36, Reactor to 2.4.3, Jackson to 2.12.1.
* [JCBC-1774](https://issues.couchbase.com/browse/JCBC-1774): Added pre-flight sanity check before using a JacksonJsonSerializer found on the classpath.
* [JVMCBC-919](https://issues.couchbase.com/browse/JVMCBC-919): Support for Project Reactor BlockHound integration.
* [JVMCBC-926](https://issues.couchbase.com/browse/JVMCBC-926): Performance: Replace new byte\[\] full copies with ByteBufUtil.getBytes.
* [JVMCBC-927](https://issues.couchbase.com/browse/JVMCBC-927): Performance: Improve performance of metrics hot code path.

#### [](#bugs-14)Bugs

* [JVMCBC-930](https://issues.couchbase.com/browse/JVMCBC-930): Threshold and Orphan Reporting now report the correct time units.
* [JVMCBC-932](https://issues.couchbase.com/browse/JVMCBC-932): Fixed a memory leak when OrphanReporter is disabled.
* [JVMCBC-933](https://issues.couchbase.com/browse/JVMCBC-933): ThresholdRequestTracer and OrphanReporter now use bounded queues.

#### [](#internal-improvements)Internal Improvements

* [JVMCBC-912](https://issues.couchbase.com/browse/JVMCBC-912): Refactor property loading.
* [JVMCBC-918](https://issues.couchbase.com/browse/JVMCBC-918): Move ProjectionsApplier into core.
* [JVMCBC-920](https://issues.couchbase.com/browse/JVMCBC-920): Move MutationState logic to core.
* [JVMCBC-921](https://issues.couchbase.com/browse/JVMCBC-921): Add OpenTelemetry attributes for spans.
* [JVMCBC-929](https://issues.couchbase.com/browse/JVMCBC-929): Retain stability annotations at runtime.

### [](#version-3-1-2-2-february-2021)Version 3.1.2 (2 February 2021)

Version 3.1.2 is the third release of the 3.1 series, bringing stabilizations and enhancements over 3.1.1.

[Download](https://packages.couchbase.com/clients/java/3.1.2/Couchbase-Java-Client-3.1.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.2/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.2**
* com.couchbase.client:**core-io:2.1.2**
* io.projectreactor:**reactor-core:3.4.1**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#api-affecting)API Affecting

* [JCBC-1763](https://issues.couchbase.com/browse/JCBC-1763): CollectionManager::getScope is now deprecated, in favour of using getAllScopes.

#### [](#enhancements)Enhancements

* [JVMCBC-915](https://issues.couchbase.com/browse/JVMCBC-915): As a performance optimization, loading a collection now only fetches the information required for that collection, rather than the full collection manifest.
* [JVMCBC-916](https://issues.couchbase.com/browse/JVMCBC-916): Any send HTTP request will send a hostname if hostnames are used, rather than IP, leading to consistent hostname use across the system.

### [](#version-3-1-1-12-january-2021)Version 3.1.1 (12 January 2021)

Version 3.1.1 is the second release of the 3.1 series, bringing stabilizations and enhancements over 3.1.0.

[Download](https://packages.couchbase.com/clients/java/3.1.1/Couchbase-Java-Client-3.1.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.1/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.1/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.1**
* com.couchbase.client:**core-io:2.1.1**
* io.projectreactor:**reactor-core:3.4.1**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#api-affecting-2)API Affecting

* [JVMCBC-906](https://issues.couchbase.com/browse/JVMCBC-906): Removed Tracer as a _mandatory_ argument from `OpenTelemetrySpan`. (The OpenTelemetry module is marked `@Stability.Volatile`, indicating that there may be API-breaking changes. The volatility arises from the underlying `OpenTelemetry` library itself being at a beta/volatile level.)

#### [](#bugs-15)Bugs

* [JVMCBC-909](https://issues.couchbase.com/browse/JVMCBC-909): Retry opening the bucket until timeout when it is not found, to allow for it not yet being created.
* [JVMCBC-910](https://issues.couchbase.com/browse/JVMCBC-910): WaitUntilReady will now wait if bucket not present yet, before it starts to time out.
* [JVMCBC-911](https://issues.couchbase.com/browse/JVMCBC-911), [JCBC-1728](https://issues.couchbase.com/browse/JCBC-1728): Certain collection-related error codes have changed.
* [JCBC-1730](https://issues.couchbase.com/browse/JCBC-1730): Support for collections added to `BatchHelper`.
* [JCBC-1747](https://issues.couchbase.com/browse/JCBC-1747): Prepared non-adhoc queries on scopes were failing, as query\_context was not being passed to the individual prepare and/or execute statements. This has now been fixed, and scope-level queries are working as expected.

#### [](#enhancements-2)Enhancements

* [JVMCBC-907](https://issues.couchbase.com/browse/JVMCBC-907): The Orphan Reporter can now be disabled.
* [JVMCBC-908](https://issues.couchbase.com/browse/JVMCBC-908): Updated OpenTelemetry to 0.13.
* [JCBC-1749](https://issues.couchbase.com/browse/JCBC-1749): Escape the scope for scope-level queries now enabled, as a fix in the server means that this works.
* [JCBC-1746](https://issues.couchbase.com/browse/JCBC-1746): Expose partition information from the query management API on `QueryIndex` class.

### [](#version-3-1-0-2-december-2020)Version 3.1.0 (2 December 2020)

Version 3.1.0 is the first GA release of the 3.1 series, bringing stabilizations and enhancements over 3.0.10 and the 3.0 SDK, and adding features to support Couchbase Server 6.6 and 7.0β.

[Download](https://packages.couchbase.com/clients/java/3.1.0/Couchbase-Java-Client-3.1.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.1.0/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.1.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.1.0**
* com.couchbase.client:**core-io:2.1.0**
* io.projectreactor:**reactor-core:3.4.0**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-3)Enhancements

* [JCBC-1731](https://issues.couchbase.com/browse/JCBC-1731): Experimental support for Metrics (`Meter`) and the internals have been reworked around the `RequestTracer`. The new metrics implementation is disabled by default but will be enabled in the future. We encourage you to try it out and provide feedback, please see the documentation section on tracing and metrics for further information.
* [JCBC-1646](https://issues.couchbase.com/browse/JCBC-1646): The minimum durability level can now be configured on the `BucketManager`.
* [JVMCBC-904](https://issues.couchbase.com/browse/JVMCBC-904): Internal and external dependencies have been updated, including project reactor to `3.4.0`.
* [JVMCBC-905](https://issues.couchbase.com/browse/JVMCBC-905): It is now possible to disable TLS hostname verification as part of the `SecurityConfig`.
* [JVMCBC-901](https://issues.couchbase.com/browse/JVMCBC-901): Support for transactions with [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) queries has been added to the core subsystem so that the upper transaction dependency can make use of it.

In addition to the tickets outlined below, different interfaces have been elevated from `Uncomitted` or `Volatile` to `Comitted`. These include:

* Expiry Key/Value read and write APIs that take an `Instant`.
* Geo-Polygon Search
* Search Flex-Index Option
* Search Disable-Scoring Option

## [](#java-sdk-3-0-releases)Java SDK 3.0 Releases

### [](#version-3-0-10-3-november-2020)Version 3.0.10 (3 November 2020)

Version 3.0.10 is a maintenance release, bringing enhancements over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.10/Couchbase-Java-Client-3.0.10.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.10/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.11/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.10**
* com.couchbase.client:**core-io:2.0.11**
* io.projectreactor:**reactor-core:3.3.9.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-4)Enhancements

* [JVMCBC-898](https://issues.couchbase.com/browse/JVMCBC-898): Added fallback for lastDispatchedTo in context, to improve debuggability.
* [JVMCBC-899](https://issues.couchbase.com/browse/JVMCBC-899): Updated OpenTelemetry to 0.9.1.

### [](#version-3-0-9-7-october-2020)Version 3.0.9 (7 October 2020)

Version 3.0.9 is a bugfix release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.9/Couchbase-Java-Client-3.0.9.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.9/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.10/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.9**
* com.couchbase.client:**core-io:2.0.10**
* io.projectreactor:**reactor-core:3.3.9.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#api-affecting-3)API Affecting

* [JCBC-1716](https://issues.couchbase.com/browse/JCBC-1716): The Analytics getPendingMutations API had a return value (`Map<String, Long>`) that did not reflect what was returned from the server. The return value has been changed to `Map<String, Map<String, Long>>` accordingly. As the getPendingMutations method was previously uncallable due to the resulting deserialization failure, we believe this API change - though technically breaking - will not impact any users, and we have kept the API version at 3.x.

#### [](#bug-fixes-22)Bug Fixes

* [JCBC-1713](https://issues.couchbase.com/browse/JCBC-1713): Improve LDAP auth failure handling.
* [JCBC-1718](https://issues.couchbase.com/browse/JCBC-1718): `Expiry` fixed for `touch` and `getAndTouch` methods.
* [JVMCBC-885](https://issues.couchbase.com/browse/JVMCBC-885): Allow overriding of `BestEffortRetryStrategy`.
* [JVMCBC-889](https://issues.couchbase.com/browse/JVMCBC-889): Make sure WaitUntilReady always times out.
* [JVMCBC-890](https://issues.couchbase.com/browse/JVMCBC-890): Enforce only negotiate PLAIN when using TLS with PasswordAuthenticator.
* [JVMCBC-892](https://issues.couchbase.com/browse/JVMCBC-892): Service pool idle time check must happen more often.
* [JVMCBC-894](https://issues.couchbase.com/browse/JVMCBC-894): BatchHelper: handle success case with no body gracefully.
* [JVMCBC-872](https://issues.couchbase.com/browse/JVMCBC-872): Subdoc 'no access' error code is now reported correctly. This helps users to identify and fix permissions errors for system XATTRs.

#### [](#enhancements-5)Enhancements

* [JCBC-1651](https://issues.couchbase.com/browse/JCBC-1651): Geopolygon search support.
* [JCBC-1652](https://issues.couchbase.com/browse/JCBC-1652): Added Options To Use FTS Hints (Flex Index).
* [JCBC-1695](https://issues.couchbase.com/browse/JCBC-1695): Added support to pass Score as FTS parameter.
* [JCBC-1707](https://issues.couchbase.com/browse/JCBC-1707): Retrofited Geo Search Queries to allow Coordinate Usage.
* [JCBC-1709](https://issues.couchbase.com/browse/JCBC-1709): Allow to access ReactiveScope from Scope.
* [JCBC-1712](https://issues.couchbase.com/browse/JCBC-1712): Clarified Javadoc lockTime on getAndLock.
* [JCBC-1715](https://issues.couchbase.com/browse/JCBC-1715): Allow to provide custom http headers for the `RawManager`.
* [JCBC-1717](https://issues.couchbase.com/browse/JCBC-1717): Support for targeting requests to a given node. This allows to always send QueryRequests related to a given transaction to the same query node.
* [JVMCBC-888](https://issues.couchbase.com/browse/JVMCBC-888), [JVMCBC-893](https://issues.couchbase.com/browse/JVMCBC-893): Dependency bumps: Netty to 4.1.52.Final, OpenTelemetry to 0.8.
* [JVMCBC-886](https://issues.couchbase.com/browse/JVMCBC-886): Improve LDAP auth failure handling.
* [JVMCBC-896](https://issues.couchbase.com/browse/JVMCBC-896): Fast dispatch pooled requests.

### [](#version-3-0-8-31-august-2020)Version 3.0.8 (31 August 2020)

Version 3.0.8 is a bugfix release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.8/Couchbase-Java-Client-3.0.8.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.8/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.9/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.8**
* com.couchbase.client:**core-io:2.0.9**
* io.projectreactor:**reactor-core:3.3.9.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-6)Enhancements

* [JCBC-1705](https://issues.couchbase.com/browse/JCBC-1705): A (uncomitted) API has been added which allows to very efficiently perform bulk fetch and bulk exists operations. See the `BatchHelper` class for more details.
* [JCBC-1684](https://issues.couchbase.com/browse/JCBC-1684): The `PingOptions` services can now be configured through a vararg, making it easier to use.
* [JCBC-1691](https://issues.couchbase.com/browse/JCBC-1691): A (uncomitted) API has been added which allows sending all kinds of requests to the cluster manager (called raw manager API).
* [JVMCBC-883](https://issues.couchbase.com/browse/JVMCBC-883): The client is now a little less verbose when performing a DNS SRV request and the underlying JDK operation times out.
* [JVMCBC-879](https://issues.couchbase.com/browse/JVMCBC-879): Updated internal and external dependencies to their latest maintenance releases.
* [JVMCBC-871](https://issues.couchbase.com/browse/JVMCBC-871): On the `IoConfig` it is now possible to `captureTraffic()` with empty arguments, implying that all traffic will be captured.
* [JVMCBC-874](https://issues.couchbase.com/browse/JVMCBC-874): When dealing with unknown collections, the SDK now returns a more user friendly retry reason when it can (outdated manifest vs. collection not found).
* [JVMCBC-875](https://issues.couchbase.com/browse/JVMCBC-875): On the request timeout exception, the retry reasons are now accessible directly.
* [JCBC-1693](https://issues.couchbase.com/browse/JCBC-1693): The `UserManager` API has been extended to support collections and scopes (needs at least Server 7.0 to be usable).
* [JCBC-1660](https://issues.couchbase.com/browse/JCBC-1660): Support for scope-level SQL++ queries has been added (needs at least Server 7.0 to be usable).
* [JCBC-1658](https://issues.couchbase.com/browse/JCBC-1658): Support for scope-level analytics queries has been added (needs at least Server 7.0 to be usable).

#### [](#bug-fixes-23)Bug Fixes

* [JCBC-1696](https://issues.couchbase.com/browse/JCBC-1696): When adding the option `withExpiry(true)` to `GetOptions`, it is now possible to use a custom transcoder which is JSON compatible.
* [JVMCBC-805](https://issues.couchbase.com/browse/JVMCBC-805): The client now handles bootstrapping against nodes much better which do not have the data service enabled (in an MDS setup).
* [JVMCBC-882](https://issues.couchbase.com/browse/JVMCBC-882): A bug has been fixed where when bootstrapping against a node with no data service enabled, the endpoint would not be cleaned up and would keep trying to reconnect.
* [JVMCBC-872](https://issues.couchbase.com/browse/JVMCBC-872): The client now more explicitly handles an error response code (`NO_ACCESS`) when a subdocument request is performed against a system xattr.
* [JVMCBC-873](https://issues.couchbase.com/browse/JVMCBC-873): Durability information is now properly unwrapped from an optional when exported and dumped (for example as part of an exception).
* [JVMCBC-880](https://issues.couchbase.com/browse/JVMCBC-880): The client now trackes multiple parallel bucket open attempts (against different buckets) in a better way, making sure that an internal state is only switched when all those bucket open attempts have completed (and not just the first one).
* [JVMCBC-878](https://issues.couchbase.com/browse/JVMCBC-878): `EndpointDiagnostics` had the local and remote hostnames mixed up, they now show up in the correct order.

### [](#version-3-0-7-4-august-2020)Version 3.0.7 (4 August 2020)

Version 3.0.7 is the eighth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.7/Couchbase-Java-Client-3.0.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.7/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.8/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.7**
* com.couchbase.client:**core-io:2.0.8**
* io.projectreactor:**reactor-core:3.3.8.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#api-affecting-4)API Affecting

* [JCBC-1681](https://issues.couchbase.com/browse/JCBC-1681): Removed cas from `IncrementOptions` and `DecrementOptions`. CAS is not supported by the underlying protocol and should not have been exposed in these options.
* [JCBC-1625](https://issues.couchbase.com/browse/JCBC-1625): Deprecated `maxTTL` on BucketSettings in favor of `maxExpiry`.

#### [](#bug-fixes-24)Bug Fixes

* [JCBC-1647](https://issues.couchbase.com/browse/JCBC-1647): Deprecated `EjectionPolicy` in favor of `EvictionPolicyType`. And added the "noEviction" and "nruEviction" policies used by ephemeral buckets. This fixed a but where the BucketManager didn't recognize ephemeral bucket ejection values. Users can now set a non-default ejection policy when creating an ephemeral bucket.
* [JCBC-1668](https://issues.couchbase.com/browse/JCBC-1668): Fixes an NPE when `toString` or `fieldsAs` is called when no fields are present in the result. In this case just null should now be returned, instead of a NPE deep down in the Jackson serializer stack.
* [JVMCBC-870](https://issues.couchbase.com/browse/JVMCBC-870): A bug in the chunk response parser prohibited responses meant that View reduce responses were never completed, and as a result timed out on the user side. The completion of view results with reduce enabled has now been fixed.

#### [](#enhancements-7)Enhancements

* [JCBC-1661](https://issues.couchbase.com/browse/JCBC-1661), [JCBC-1665](https://issues.couchbase.com/browse/JCBC-1665): Building on the expiry improvements in the previous release, this adds a new `expiryTime()` method that returns expiry as an `Instant`, which better expresses the concept than the `Duration` returned by `expiry()`. The latter will be deprecated in a future release. Similarly, everywhere a `Duration`\-based expiry could be provided previously, an overload has been added to take an `Instant`\-based expiry.
* [JCBC-1666](https://issues.couchbase.com/browse/JCBC-1666): Made `bucket.scope("_default").collection("_default")` behave just like `bucket.defaultCollection()`. `AsyncScope.collection()` now no longer refreshes collection map for default collection.
* [JCBC-1670](https://issues.couchbase.com/browse/JCBC-1670): Added WaitUntilReadyOptions.serviceTypes() overload that accepts varargs.
* [JVMCBC-867](https://issues.couchbase.com/browse/JVMCBC-867): Performance improvement: do not grab ByteBuf slice when extracting server response time.
* [JVMCBC-869](https://issues.couchbase.com/browse/JVMCBC-869): Maintenance dependency bump: Netty → 4.1.51, Jackson → 2.11.1, Reactor → 3.3.7, OpenTelemetry → 0.6.0.

### [](#version-3-0-6-14-july-2020)Version 3.0.6 (14 July 2020)

Version 3.0.6 is the seventh release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.6/Couchbase-Java-Client-3.0.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.6/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.7/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.6**
* com.couchbase.client:**core-io:2.0.7**
* io.projectreactor:**reactor-core:3.3.5.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-8)Enhancements

* [JCBC-1645](https://issues.couchbase.com/browse/JCBC-1645): Specifying document expiries has been made significantly easier. Expiries are supplied as a `Duration`. The new behaviour is that if that duration is less than 50 years, then it will be interpreted as being a relative timestamp from the current time. E.g. `Duration.ofDays(35)` will expire in 35 days time. (Previously, a `Duration` longer than 30 days would be interpreted as being an epoch time. Unless this epoch time occurred in the future then it would expire immediately. In order to preserve compatibility for users that worked around this behaviour, any `Duration` longer than 50 years will continue to be interpreted as an epoch time.)
* [JCBC-1632](https://issues.couchbase.com/browse/JCBC-1632): Bootstrapping is now fully pipelined for performance, building on the improvements in the previous release.
* [JVMCBC-865](https://issues.couchbase.com/browse/JVMCBC-865): Changed the default idle timeout to 4.5s for http connections, to support performance improvements in query service.

#### [](#bug-fixes-25)Bug Fixes

* [JCBC-1662](https://issues.couchbase.com/browse/JCBC-1662): `MutateInMacro` for CRC32 is fixed.
* [JCBC-1664](https://issues.couchbase.com/browse/JCBC-1664): `viewQuery` with `ViewOptions.viewOptions().keys(keys)` was returning a bad\_request error. This is now fixed.
* [JVMCBC-849](https://issues.couchbase.com/browse/JVMCBC-849): Redundant global loading exceptions no longer propagated — now logged at `debug` level.
* [JVMCBC-856](https://issues.couchbase.com/browse/JVMCBC-856): A just-opened connection in pool no longer gets cleaned up prematurely .
* [JVMCBC-858](https://issues.couchbase.com/browse/JVMCBC-858): Channel writeAndFlush failures are no longer ignored.
* [JVMCBC-862](https://issues.couchbase.com/browse/JVMCBC-862): Race condition with node identifier change on bootstrap identified. New logic and some changes to the config provider code ensures that retry and resubscribe picks up fresh seed nodes.
* [JVMCBC-863](https://issues.couchbase.com/browse/JVMCBC-863): Bucket-Level ping report no longer includes other view and KV services buckets.
* [JVMCBC-866](https://issues.couchbase.com/browse/JVMCBC-866): Trailing : no longer added to IPv6 addresses without \[\]. 'invalid IPv6 address' warnings now no longer produced when trying to connect to a valid Ipv6 address thus specified.

### [](#version-3-0-5-2-june-2020)Version 3.0.5 (2 June 2020)

Version 3.0.5 is the sixth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.5/Couchbase-Java-Client-3.0.5.zip) | [API Reference](http://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.5/) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.6/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.5**
* com.couchbase.client:**core-io:2.0.6**
* io.projectreactor:**reactor-core:3.3.5.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-9)Enhancements

* [JVMCBC-852](http://issues.couchbase.com/browse/JVMCBC-852): Bumped Reactor to 3.3.5, Netty to 4.1.50.Final, and Jackson to 2.11.0.
* [JVMCBC-693](https://issues.couchbase.com/browse/JVMCBC-693): For performance, the KV bootstrap sequence is now partially pipelined.

In addition, there are internal revisions to support the forthcoming Field Level Encryption (FLE) support. This will be available in a separate library for Enterprise Edition subscribers.

#### [](#bug-fixes-26)Bug Fixes

* [JVMCBC-851](http://issues.couchbase.com/browse/JVMCBC-851): Reactive getAllReplicas methods will now honor a provided custom transcoder.
* [JVMCBC-849](http://issues.couchbase.com/browse/JVMCBC-849): Duplicate global loading exceptions are now swallowed to remove redundant warnings from logging (this was a cosmetic-only issue).

### [](#version-3-0-4-7-may-2020)Version 3.0.4 (7 May 2020)

Version 3.0.4 is the fifth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.4/Couchbase-Java-Client-3.0.4.zip) | [API Reference](http://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.4/) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.5/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.4**
* com.couchbase.client:**core-io:2.0.5**
* io.projectreactor:**reactor-core:3.3.4.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-10)Enhancements

* [JVMCBC-841](http://issues.couchbase.com/browse/JVMCBC-841): Bumped Netty dependency to 2.0.30, and reactor to 3.3.4

#### [](#bug-fixes-27)Bug Fixes

* [JVMCBC-845](http://issues.couchbase.com/browse/JVMCBC-845): If a rebalance is stopped in the middle, an edge case occasionally causes KV ops to time out as the fast forward map is chosen over the retry. The behavior has now been changed so that the client will try the old and new servers to make sure the operation eventually gets dispatched to the right node.
* [JCBC-1626](http://issues.couchbase.com/browse/JCBC-1626): If bucket is not flushable, a `BucketNotFlushableException` is now raised.

### [](#version-3-0-3-7-april-2020)Version 3.0.3 (7 April 2020)

Version 3.0.3 is the fourth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.3/Couchbase-Java-Client-3.0.3.zip) | [API Reference](http://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.3/) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.4/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.3**
* com.couchbase.client:**core-io:2.0.4**
* io.projectreactor:**reactor-core:3.3.3.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.2**

#### [](#enhancements-11)Enhancements

* [JCBC-1603](http://issues.couchbase.com/browse/JCBC-1603), [JCBC-1606](http://issues.couchbase.com/browse/JCBC-1606): Exposed API to set the CollectionsExample TTL. CreateCollection CollectionSpec now includes `MaxTTL`.
* [JCBC-1617](http://issues.couchbase.com/browse/JCBC-1617): Attempting to work with the collection manager on clusters where CollectionsExample are not available (or enabled as a DP) will now result in a `FeatureNotAvailable` failure.
* [JVMCBC-830](http://issues.couchbase.com/browse/JVMCBC-830): Added more convenient overloads for SecurityConfig and CertAuth. These overloads initialize both the SecurityConfig and the CertificateAuthenticator directly from a KeyStore or TrustStore.
* [JVMCBC-831](http://issues.couchbase.com/browse/JVMCBC-831): Improves timeout for waitUntilReady — the `waitUntilReady` helper should now throw a proper timeout exception.
* [JVMCBC-832](http://issues.couchbase.com/browse/JVMCBC-832): Added support for multiple ports per hostname in the connection string — without having to use the explicit SeedNode set overload.
* [JVMCBC-835](http://issues.couchbase.com/browse/JVMCBC-835): Using "localhost:8091" as a connection string would set the kv bootstrap port to 8091, which is not desired behavior. To prevent this from happening again, the code now checks for this condition, fails fast, and also provides guidance on what the connection string should look like instead.
* [JVMCBC-836](http://issues.couchbase.com/browse/JVMCBC-836): Enabled Unordered Execution by Default.
* [JVMCBC-837](http://issues.couchbase.com/browse/JVMCBC-837): Updates OpenTelemetry to 0.3 (beta).

#### [](#bug-fixes-28)Bug Fixes

* [JCBC-1618](http://issues.couchbase.com/browse/JCBC-1618): Named fields in SearchRows results are now deserialized.
* [JVMCBC-834](http://issues.couchbase.com/browse/JVMCBC-834): 'CollectionNotFoundException' now triggers a retry, and if no collection refresh is currently in progress it will proactively trigger a new one. Now Docs created under custom collection should no longer raise an exception when a collection has been created in the meantime, but the collection is not found as no refresh is in progress.
* [JVMCBC-826](http://issues.couchbase.com/browse/JVMCBC-826): A NullPointerException was occuring when LDAP is enabled. The code now explicitly fails the connection with a descriptive error message instructing the user what to do next (either use TLS which is preferred) or enable PLAIN on the password authenticator (insecure).
* [JVMCBC-827](http://issues.couchbase.com/browse/JVMCBC-827): Search query results row\_hit typo resulted in 0 being returned for total rows. This has now been fixed.
* [JVMCBC-828](http://issues.couchbase.com/browse/JVMCBC-828): Omit internal config request in orphan reporting.
* [JVMCBC-839](http://issues.couchbase.com/browse/JVMCBC-839): Bootstrap will now correctly use the mapped port if alternate addr is present.

### [](#version-3-0-2-3-march-2020)Version 3.0.2 (3 March 2020)

Version 3.0.2 is the third release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.2/Couchbase-Java-Client-3.0.2.zip) | [API Reference](http://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.2/) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.3/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.2**
* com.couchbase.client:**core-io:2.0.3**
* io.projectreactor:**reactor-core:3.3.1.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.2**

#### [](#enhancements-12)Enhancements

* [JCBC-1588](http://issues.couchbase.com/browse/JCBC-1588): Give TypeRef overload of JsonSerializer a default "unsupported" impl, making it easier for applications to implement custom JsonSerializers.
* [JVMCBC-813](http://issues.couchbase.com/browse/JVMCBC-813): Improved error message for bucket is missing.
* [JVMCBC-815](http://issues.couchbase.com/browse/JVMCBC-815): Check if key exceeds size limits.
* [JVMCBC-818](http://issues.couchbase.com/browse/JVMCBC-818): Trimmed netty stack in connect failures for more readable output.
* [JVMCBC-819](http://issues.couchbase.com/browse/JVMCBC-819): Distinguished bucket not found in select bucket failures.
* [JVMCBC-823](http://issues.couchbase.com/browse/JVMCBC-823): Added a global component to the core id.
* [JVMCBC-825](http://issues.couchbase.com/browse/JVMCBC-825): Support added for new VATTR HELLO flag.

#### [](#bug-fixes-29)Bug Fixes

* [JCBC-1587](http://issues.couchbase.com/browse/JCBC-1587): Exists no longer returns wrong value if executed right after remove.
* [JCBC-1600](http://issues.couchbase.com/browse/JCBC-1600): Using expiry together with document flags on a Sub-Document `mutateIn` no longer causes an incorrect flags field to be sent.
* [JCBC-1604](http://issues.couchbase.com/browse/JCBC-1604): Properly clear cache when repreparing/retrying query.
* [JVMCBC-824](http://issues.couchbase.com/browse/JVMCBC-824): Native Netty transports not included, resulting in fallback to default implementation. Only affected 2.0.2 core release.

### [](#version-3-0-1-5-february-2020)Version 3.0.1 (5 February 2020)

Version 3.0.1 is the second release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/java/3.0.1/Couchbase-Java-Client-3.0.1.zip) | [API Reference](http://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.1/) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.1**
* com.couchbase.client:**core-io:2.0.2**
* io.projectreactor:**reactor-core:3.3.1.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.2**

#### [](#enhancements-13)Enhancements

* [JCBC-1578](http://issues.couchbase.com/browse/JCBC-1578): Added support for Java Object Serialization as a custom `Transcoder`.
* [JVMCBC-808](http://issues.couchbase.com/browse/JVMCBC-808): The internal packaged `netty` dependency has been reduced to the minimum amount of artifacts needed, trimming the resulting jar size a little.

#### [](#bug-fixes-30)Bug Fixes

* [JCBC-1574](http://issues.couchbase.com/browse/JCBC-1574): `JsonObject/Array.put(String,Object)` now supports writing generic Maps and Lists.
* [JCBC-1580](http://issues.couchbase.com/browse/JCBC-1580): The code for get projections had an import for unbundled jackson which prevented it from working in an environment where no unbundled jackson is on the classpath. This no longer occurs.
* [JCBC-1582](http://issues.couchbase.com/browse/JCBC-1582): The client context ID is now propagated into the `PREPARE` query if needed.
* [JVMCBC-806](http://issues.couchbase.com/browse/JVMCBC-806): TLS: remote hostname and port are passed down to the SSL engine, making sure that hostname validation works as expected.
* [JCBC-1575](http://issues.couchbase.com/browse/JCBC-1575): Bucket Management: BucketSettings load does now recognize numReplicas properly.

#### [](#known-issues-3)Known Issues

* [JVMCBC-805](http://issues.couchbase.com/browse/JVMCBC-805): When bootstrapping against a non-KV node the KV socket is not cleaned up properly. As a workaround (and as we recommend in general), please only bootstrap against nodes which have the KV service enabled. Or maintain a list of KV nodes in [DNS SRV](../howtos/managing-connections.md#using-dns-srv-records).

### [](#version-3-0-0-10-january-2020)Version 3.0.0 (10 January 2020)

This is the first GA release of the third generation Java SDK.

[Download](https://packages.couchbase.com/clients/java/3.0.0/Couchbase-Java-Client-3.0.0.zip) | [API Reference](http://docs.couchbase.com/sdk-api/couchbase-java-client-3.0.0/) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**java-client:3.0.0**
* com.couchbase.client:**core-io:2.0.0**
* io.projectreactor:**reactor-core:3.3.1.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.2**

#### [](#enhancements-14)Enhancements

The following list describes the API changes between 3.0.0 beta.2 and 3.0.0 GA.

* [JCBC-1563](http://issues.couchbase.com/browse/JCBC-1563): Added the reactive API to the view index manager.
* [JVMCBC-776](http://issues.couchbase.com/browse/JVMCBC-776): Added support for server-side KV tracing statistics.
* [JCBC-1522](http://issues.couchbase.com/browse/JCBC-1522): All data commands have been instrumented to be included in RTO (Response Time Observability).
* [JCBC-1566](http://issues.couchbase.com/browse/JCBC-1566), [JCBC-1568](http://issues.couchbase.com/browse/JCBC-1568): The Search API has been slightly improved to align with the SDK RFC.
* [JCBC-1599](http://issues.couchbase.com/browse/JCBC-1599): Bucket, Scope and Collection instances are now cached so repeated open attempts produce less garbage and happen quicker.
* [JVMCBC-785](http://issues.couchbase.com/browse/JVMCBC-785), [JVMCBC-786](http://issues.couchbase.com/browse/JVMCBC-786), [JVMCBC-675](http://issues.couchbase.com/browse/JVMCBC-675): View, Search, Analytics, and Query retryable error codes are now retried as part of the configured retry strategy.
* [JCBC-1561](http://issues.couchbase.com/browse/JCBC-1561), [JCBC-1562](http://issues.couchbase.com/browse/JCBC-1562): Added Option overloads to collection and search index managers.
* [JVMCBC-787](http://issues.couchbase.com/browse/JVMCBC-787), [JVMCBC-788](http://issues.couchbase.com/browse/JVMCBC-788): View requests and KV collection requests are now short-circuited against unsupported clusters.
* [JCBC-1552](http://issues.couchbase.com/browse/JCBC-1552): Added support for Java 9 automatic module names.
* [JCBC-1554](http://issues.couchbase.com/browse/JCBC-1554): `JsonArry` and `JsonObject` now support `toArray` in addition to `toString`.
* [JCBC-1545](http://issues.couchbase.com/browse/JCBC-1545): The `ping` command has been reintroduced to the cluster and bucket level APIs.
* [JCBC-1518](http://issues.couchbase.com/browse/JCBC-1518): An internal server error from the KV engine is now properly mapped to the exception equivalent.
* [JVMCBC-779](http://issues.couchbase.com/browse/JVMCBC-779): It is now possible to customize the event loop thread count instead of having to provide a new event loop itself.
* [JVMCBC-767](http://issues.couchbase.com/browse/JVMCBC-767): A new `ConfigIdleRedialTimeout` has been introduced which recycles idle HTTP streaming connections.
* [JVMCBC-782](http://issues.couchbase.com/browse/JVMCBC-782): The orphan response reporter (as part of RTO) has been ported to SDK 3 from SDK 2 and is now enabled by default.
* [JVMCBC-784](http://issues.couchbase.com/browse/JVMCBC-784): Idle HTTP connections are now closed after 30 seconds.
* [JVMCBC-773](http://issues.couchbase.com/browse/JVMCBC-773): SASL PLAIN is now not negotiated by default on non-TLS connections to prevent downgrade attacks out of the box.
* [JVMCBC-795](http://issues.couchbase.com/browse/JVMCBC-795): Requests are now failed fast if it can be determined that the service is not available on the cluster.
* [JVMCBC-790](http://issues.couchbase.com/browse/JVMCBC-790): The concept of backpressure has been re-introduced but in slightly different form.
* [JVMCBC-](http://issues.couchbase.com/browse/JVMCBC-): The circuit breaker now has a customizable completion callback.

#### [](#bug-fixes-31)Bug Fixes

The following list describes the API changes between 3.0.0 beta.2 and 3.0.0 GA.

* [JCBC-1550](http://issues.couchbase.com/browse/JCBC-1550): The owned environment in the `Cluster` is now properly shutdown on disconnect.
* [JCBC-1517](http://issues.couchbase.com/browse/JCBC-1517), [JCBC-1566](http://issues.couchbase.com/browse/JCBC-1566): All reactive APIs are now deferred and will not execute I/O side effects when not subscribed to.
* [JCBC-1539](http://issues.couchbase.com/browse/JCBC-1539): A bug has been fixed where the IoConfig.networkResolution could not be set through a system property.
* [JVMCBC-793](http://issues.couchbase.com/browse/JVMCBC-793): Various fixes have been made around DNS SRV bootstrapping that make it more robust, including fixing a bug that prevented it from working properly.
* [JCBC-1524](http://issues.couchbase.com/browse/JCBC-1524): The projections on `get` have been refactored, the test suite expanded, and a couple of issues fixed along the way.
* [JCBC-1531](http://issues.couchbase.com/browse/JCBC-1531): The QueryIndexManager now only returns GSI indexes.
* [JVMCBC-802](http://issues.couchbase.com/browse/JVMCBC-802): A bug has been fixed where a non-existing view in an existing design document would not cause an exception.
* [JCBC-1565](http://issues.couchbase.com/browse/JCBC-1565): Views now use the right default View timeout instead of the Analytics one.
* [JVMCBC-789](http://issues.couchbase.com/browse/JVMCBC-789): Performing operations while initially loading the collection map is now handled gracefully.

#### [](#known-issues-4)Known Issues

* [JVMCBC-805](http://issues.couchbase.com/browse/JVMCBC-805): When bootstrapping against a non-KV node the KV socket is not cleaned up properly. As a workaround (an we recommend in general) please only bootstrap against nodes which have the KV service enabled.

#### [](#api-changes)API Changes

The following list describes the API changes between 3.0.0 beta.2 and 3.0.0 GA. Since SDK 3 is a complete rewrite over SDK 2, the individual changes between them are not listed here. Please refer to the [migration guide](migrating-sdk-code-to-3.n.md) for this.

* [JCBC-1533](http://issues.couchbase.com/browse/JCBC-1533), [JCBC-1534](http://issues.couchbase.com/browse/JCBC-1534), [JCBC-1535](http://issues.couchbase.com/browse/JCBC-1535), [JCBC-1541](http://issues.couchbase.com/browse/JCBC-1541), [JCBC-1542](http://issues.couchbase.com/browse/JCBC-1542): Exceptions have been consolidated, renamed, and overall aligned with the latest RFC.
* [JCBC-1536](http://issues.couchbase.com/browse/JCBC-1536): `SeedNodes` have been moved out of the `ClusterOptions` into a `Cluster#connect()` overload.
* [JCBC-1540](http://issues.couchbase.com/browse/JCBC-1540): `MajorityAndPersistOnMaster` has been renamed to `MajorityAndPersistToActive` on the durability enum.
* [JCBC-1545](http://issues.couchbase.com/browse/JCBC-1545): The diagnostics API has been reworked on all levels.
* [JCBC-1551](http://issues.couchbase.com/browse/JCBC-1551): The `empty` constructors are gone from `JsonObject` and `JsonArray` since they duplicate `create`.

### [](#pre-releases)Pre-releases

Numerous _Alpha_ and _Beta_ releases were made in the run-up to the 3.0 release, and although unsupported, the release notes and download links are retained for archive purposes [here](3.0-pre-release-notes.md).

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/EOL/), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).