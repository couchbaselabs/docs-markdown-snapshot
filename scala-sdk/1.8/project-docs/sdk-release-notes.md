---
title: SDK Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Scala Client.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/1.8/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-04-17T05:26:26.225Z
link: xref:1.8@scala-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.8/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Scala Client. 

> Release notes, installation instructions, and download archive for the Couchbase Scala Client. 

Version 1.8 of the Scala SDK implements the 3.7 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

## [](#installation)Installation

* The Scala SDK is tested against LTS versions of Oracle JDK and OpenJDK — see the [compatibility docs](compatibility.md#jdk-compat).
* The Couchbase Scala SDK 1.8 Client supports Scala 2.12, 2.13, and 3.3 through 3.7 (inclusive).

More details of the installation process are in the [full installation guide](sdk-full-installation.md). In most cases, given the above prerequisites, it's a simple matter of the following for your favorite build tool:

* Scala Build Tool (SBT)
* Gradle
* Maven

```sbt
libraryDependencies += "com.couchbase.client" %% "scala-client" % "1.8.3"
```

This will automatically use the correct build for your Scala version.

For Scala 2.13 or Scala 3.3 through 3.7, include the following in your `build.gradle`:

```groovy
dependencies {
    compile group: 'com.couchbase.client', name: 'scala-client_3', version: '1.8.3'
}
```

For Scala 2.12, refer to the full [Installation page](sdk-full-installation.md).

For Scala 2.13 or Scala 3.3 through 3.7, include the following in your Maven `pom.xml`:

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>scala-client_3</artifactId>
        <version>1.8.3</version>
    </dependency>
</dependencies>
```

For Scala 2.12, refer to the full [Installation page](sdk-full-installation.md).

### [](#verifying-artifacts)Verifying Artifacts

Starting with version 3.8.2, Couchbase JVM SDK artifacts are signed with [this GPG key](../../../java-sdk/current/project-docs/%5Fattachments/gpg-keys/181C7A4E908890A2D768365742BDEBD30D10C992.asc).

Fingerprint

```none
CB SDK Robot <cb-sdk-robot@couchbase.com>
181C 7A4E 9088 90A2 D768  3657 42BD EBD3 0D10 C992
```

## [](#latest-release)Scala SDK 3.11 Releases

Version 3.11 of the Scala SDK implement the 3.9 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

> [!NOTE]
> From 3.9.0 on, all Couchbase JVM SDKs have an aligned version number to make it easier to users to track changes. So the version jumped from 1.8.x to 3.9.x. While this is technically an increase in the major, the Scala 2 versions of the SDK have only one very small breaking change made to the API, to remove a long-deprecated transactions method. All other functionality works unchanged and users can upgrade existing applications without issue.

The major new feature starting in the 3.9 series is the addition of a new version of the SDK, built for Scala 3\. The Scala 3 version of the SDK has some API differences, documented on [migrating to Scala 3](#project-docs:migrating-to-scala-3.adoc). But we expect the majority of Scala 2 applications will be able to migrate to Scala 3 and the Scala 3 version of the SDK with no-to-minimal differences. Note that the API reference links below are for the Scala 2.12 version of the SDK.

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

Binary compatibility is not guaranteed for any Scala SDK release, and you should rebuild your application when changing the SDK.

### [](#version-3-11-2-13-april-2026)Version 3.11.2 (13 April 2026)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.11.2/com/couchbase/client/scala/index.html) | [Core API Reference](https://docs.couchbase.com/sdk-api/couchbase-core-io-3.11.2/)

This maintenance release upgrades Netty and Jackson to the latest versions.

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements)Improvements

* [JVMCBC-1726](https://jira.issues.couchbase.com/browse/JVMCBC-1726): Upgraded Netty from to `4.2.9` to `4.2.12`.
* [JVMCBC-1723](https://jira.issues.couchbase.com/browse/JVMCBC-1723): Upgraded Jackson from `2.20.1` to `2.21.2`.

### [](#version-3-11-1-16-february-2026)Version 3.11.1 (16 February 2026)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.11.1/com/couchbase/client/scala/index.html) | [Core API Reference](https://docs.couchbase.com/sdk-api/couchbase-core-io-3.11.1/)

This critical release fixes a regression in `3.11.0` that caused documents inserted in transactions to expire immediately.

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes)Bug Fixes

* [JVMCBC-1712](https://jira.issues.couchbase.com/browse/JVMCBC-1712): Document inserted in transactions no longer expire immediately. This fixes a regression in `3.11.0`.

### [](#version-3-11-0-04-february-2026)Version 3.11.0 (04 February 2026)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.11.0/com/couchbase/client/scala/index.html) | [Core API Reference](https://docs.couchbase.com/sdk-api/couchbase-core-io-3.11.0/)

> [!CAUTION]
> This version has [a serious bug that causes documents inserted in transactions to expire immediately](https://jira.issues.couchbase.com/browse/JVMCBC-1712). We recommend upgrading directly to `3.11.1`.

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-2)Bug Fixes

* [JVMCBC-1705](https://jira.issues.couchbase.com/browse/JVMCBC-1705): Fixed an issue that could cause the transaction cleanup task to terminate unexpectedly, leaving the SDK unable to clean up incomplete transactions.

#### [](#improvements-2)Improvements

* [JVMCBC-1708](https://jira.issues.couchbase.com/browse/JVMCBC-1708): Upgraded `OpenTelemetry` from `1.31.0` to `1.57.0`.
* [JVMCBC-1692](https://jira.issues.couchbase.com/browse/JVMCBC-1692): SQL++ statements are now excluded from tracing spans unless the query has parameters.
* [SCBC-501](https://jira.issues.couchbase.com/browse/SCBC-501): Developers who want to use the latest [OpenTelemetry semantic conventions for database client spans](https://opentelemetry.io/docs/specs/semconv/db/database-spans/)can now opt in by setting the `OTEL_SEMCONV_STABILITY_OPT_IN` environment variable to `database` (or `database/dup` to create duplicate spans using both old and new conventions). Alternatively, you can opt in via the `observabilitySemanticConventions` client setting, which has a higher precedence than the environment variable.
* [JVMCBC-1635](https://jira.issues.couchbase.com/browse/JVMCBC-1635): Upgraded Netty from `4.1.130` to `4.2.9`.  
> [!TIP]  
> Netty 4.2 introduces a new memory allocator called `AdaptiveByteBufAllocator`. By default, this version of the Couchbase SDK continues using the tried and true `PooledByteBufAllocator`. However, the default may change in a future minor version. If you want to use the new allocator now, set the Java system property `com.couchbase.client.core.deps.io.netty.allocator.type` to `adaptive`. On the other hand, if you want to insulate your project from possible future changes to the default allocator, set that property to `pooled`.

## [](#scala-sdk-3-10-releases)Scala SDK 3.10 Releases

### [](#version-3-10-1-14-january-2026)Version 3.10.1 (14 January 2026)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.10.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.10.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-3)Bug Fixes

* [JVMCBC-1709](https://jira.issues.couchbase.com/browse/JVMCBC-1709): Enabling TLS inside an OSGi container no longer causes `java.lang.ClassNotFoundException: javax.net.ssl.TrustManagerFactory not found by core-io`.

#### [](#improvements-3)Improvements

* [JVMCBC-1707](https://jira.issues.couchbase.com/browse/JVMCBC-1707): Upgraded `Netty` from `4.1.128` to `4.1.130`.
* [SCBC-500](https://jira.issues.couchbase.com/browse/SCBC-500): Deprecated the Views API.  
> [!NOTE]  
> Server-side support for Views has been deprecated since Couchbase Server 7.0, and will be removed in a future server release.

### [](#version-3-10-0-11-november-2025)Version 3.10.0 (11 November 2025)

Version 3.10.0 is the first release of the 3.10 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.10.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.10.0/)

Note that the API reference is for the Scala 2.12 version of the SDK. The Scala 3 version of the SDK has some API differences, documented on [migrating to Scala 3](#project-docs:migrating-to-scala-3.adoc).

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

##### [](#bug-fixes-4)Bug Fixes

* [JVMCBC-1696](https://couchbasecloud.atlassian.net/browse/JVMCBC-1696): The client no longer makes bucketful KV connections to nodes that aren't hosting the bucket, ensuring that unconnected endpoints don't cause SDC health check to fail.
* [JVMCBC-1697](https://couchbasecloud.atlassian.net/browse/JVMCBC-1697): Fixed a problem that caused the SDK to use more bandwidth than necessary when polling Couchbase Server 7.6 and later, for cluster topology updates when the topology is in a steady state.

##### [](#improvements-4)Improvements

* [JVMCBC-1693](https://couchbasecloud.atlassian.net/browse/JVMCBC-1693): The SDK now tracks server cluster topology changes more efficiently, and no longer sends redundant "get topology" requests during failover and rebalance.
* [JVMCBC-1699](https://couchbasecloud.atlassian.net/browse/JVMCBC-1699): If the bootstrap address resolution task does not complete before the cluster is disconnected, the task now terminates gracefully instead of logging a scary warning.
* [JVMCBC-1700](https://couchbasecloud.atlassian.net/browse/JVMCBC-1700): Upgraded to `Jackson` `2.20.1`.
* [JVMCBC-1704](https://couchbasecloud.atlassian.net/browse/JVMCBC-1704): Upgraded `Netty` from `4.1.127` to `4.1.128`.

##### [](#new-features)New Features

* [SBC-496](https://couchbasecloud.atlassian.net/browse/SCBC-496): Support mTLS Certs Refresh (without restart).
* [JVMCBC-1679](https://couchbasecloud.atlassian.net/browse/JVMCBC-1679): Support for short lived mTLS certs refresh without application restart. Added new `cluster.authenticator(Authenticator)` method for updating the authenticator used by a cluster. Useful for scenarios where you want to refresh credentials without restarting your app.
* [JVMCBC-1689](https://couchbasecloud.atlassian.net/browse/JVMCBC-1689): Added `JwtAuthenticator`.

## [](#scala-sdk-3-9-releases)Scala SDK 3.9 Releases

Version 3.9 of the Scala SDK implements the 3.8 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

> [!NOTE]
> From 3.9.0 on, all Couchbase JVM SDKs have an aligned version number to make it easier to users to track changes. So the version has jumped from 1.8.x to 3.9.x. While this is technically an increase in the major, the Scala 2 versions of the SDK have only one very small breaking change made to the API, to remove a long-deprecated transactions method. All other functionality works unchanged and users can upgrade existing applications without issue.

The major new feature in the 3.9 series is the addition of a new version of the SDK, built for Scala 3\. The Scala 3 version of the SDK has some API differences, documented on [migrating to Scala 3](#project-docs:migrating-to-scala-3.adoc). But we expect the majority of Scala 2 applications will be able to migrate to Scala 3 and the Scala 3 version of the SDK with no-to-minimal differences.

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

Binary compatibility is not guaranteed for any Scala SDK release, and you should rebuild your application when changing the SDK.

### [](#version-3-9-2-10-october-2025)Version 3.9.2 (10 October 2025)

Version 3.9.2 is the second maintenance release of the 3.9 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.9.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.9.2/)

Note that the API reference is for the Scala 2.12 version of the SDK. The Scala 3 version of the SDK has some API differences, documented on [migrating to Scala 3](#project-docs:migrating-to-scala-3.adoc).

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-5)Bug Fixes

* [SCBC-495](https://couchbasecloud.atlassian.net/browse/SCBC-495): `cluster.disconnect()` now cleanly shuts down, including waiting for the thread pool to exit.

#### [](#improvements-5)Improvements

* [JVMCBC-1694](https://couchbasecloud.atlassian.net/browse/JVMCBC-1694): Updated `Netty` to `4.1.127`.

### [](#version-3-9-1-5-september-2025)Version 3.9.1 (5 September 2025)

Version 3.9.1 is the first maintenance release of the 3.9 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.9.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.9.1/)

Note that the API reference is for the Scala 2.12 version of the SDK. The Scala 3 version of the SDK has some API differences, documented on [migrating to Scala 3](#project-docs:migrating-to-scala-3.adoc).

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-6)Bug Fixes

* [SCBC-492](https://couchbasecloud.atlassian.net/browse/SCBC-492): Fixed a regression that caused `getAllReplica` and `lookupInAllReplica` operations to fail unless explicitly passed a timeout.

#### [](#improvements-6)Improvements

* [JVMCBC-1677](https://couchbasecloud.atlassian.net/browse/JVMCBC-1677): The BOM (`couchbase-client-bom`) now includes the `scala-client_3` artifact.
* [JVMCBC-1678](https://couchbasecloud.atlassian.net/browse/JVMCBC-1678): Upgraded `Netty` to `4.1.124`.
* [JVMCBC-1680](https://couchbasecloud.atlassian.net/browse/JVMCBC-1680): When parsing cluster topology into a `ClusterTopology` object, the original JSON is now retained, so it can be re-parsed with different parameters later.

### [](#version-3-9-0-5-august-2025)Version 3.9.0 (5 August 2025)

Version 3.9.0 is the first release of the 3.9 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-3.9.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.9.0/)

Note that the API reference is for the Scala 2.12 version of the SDK. The Scala 3 version of the SDK has some API differences, documented on [migrating to Scala 3](#project-docs:migrating-to-scala-3.adoc).

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#behavioral-changes)Behavioral Changes

* [JVMCBC-1660](https://couchbasecloud.atlassian.net/browse/JVMCBC-1660): The "auto" network selection heuristic has been changed to fall back to the "external" network if the "external" network is present. Previously, if there was no exact match between an address in the connection string and an address in the cluster topology reported by the server, the SDK would select the "default" network. Now, if there is no match and an "external" network is present, the SDK selects the "external" network.  
If this change causes the SDK to select the incorrect network for your deployment, use the [io.networkResolution](../ref/client-settings.md#io.networkResolution) client setting to configure the SDK to use the "default" network.

#### [](#bug-fixes-7)Bug Fixes

* [SCBC-491](https://couchbasecloud.atlassian.net/browse/SCBC-491): Fixed a regression in 1.6.2 where attempting to manage unscoped (cluster-level) eventing functions throws a `NullPointerException`.
* [JVMCBC-1656](https://couchbasecloud.atlassian.net/browse/JVMCBC-1656): Fixed an issue that could prevent the SDK from periodically updating its list of KV node addresses. This could occur if the addresses in the connection string (or DNS SRV record) differ from the server's self-reported address as they appear in the admin UI. This issue can lead to `UnknownHostException` messages in the SDK logs. To resolve the issue, the SDK now feeds both "global" and "bucket" topology info into the same funnel, so the SDK can update its list of node addresses from either source.
* [JVMCBC-1662](https://couchbasecloud.atlassian.net/browse/JVMCBC-1662): Fixed an issue that prevented the SDK from honoring the "preferred server group" option inside transactions.
* [JVMCBC-1664](https://couchbasecloud.atlassian.net/browse/JVMCBC-1664): Exceptionally long-running analytics queries no longer throw `ArrayIndexOutOfBoundsException`.
* [JVMCBC-1671](https://couchbasecloud.atlassian.net/browse/JVMCBC-1671): All expected attributes are now included in transactions metrics exported by the SDK.

#### [](#improvements-7)Improvements

* [JVMCBC-1639](https://couchbasecloud.atlassian.net/browse/JVMCBC-1639): We've adopted a mono-versioning strategy for the Couchbase JVM client libraries. The Scala and Kotlin SDKs, along with the core library and optional modules, are now aligned with the Java SDK at version 3.9.0.  
Although this is a technically a major version bump for some components, in this exceptional case it does not indicate a breaking change. The goal of this alignment is twofold: to minimize confusion about which versions are compatible with each other, and to enable a more disciplined branch management strategy where patch releases contain only low-risk bug fixes.
* [JVMCBC-1607](https://couchbasecloud.atlassian.net/browse/JVMCBC-1607): Improved how the SDK logs information about trusted TLS certificates on startup. It now logs up to 5 certificates at `INFO` level, and the full list at `DEBUG` level. Previously, the SDK logged the full list at `INFO` level, which could prevent other interesting configuration info from being included in the log, depending on how logging was configured.
* [JVMCBC-1612](https://couchbasecloud.atlassian.net/browse/JVMCBC-1612): The SDK is now more aggressive about detecting dead or half-open KV connections. It closes a connection if there is no incoming traffic for the duration specified by `io.configIdleRedialTimeout` (default value: 5 minutes), and sends a `NOOP` request if there is no incoming traffic for half that duration.
* [JVMCBC-1648](https://couchbasecloud.atlassian.net/browse/JVMCBC-1648): Upgraded `Jackson` from `2.17.3` to `2.19.2`.
* [JVMCBC-1651](https://couchbasecloud.atlassian.net/browse/JVMCBC-1651): Improved internal support for sub-document replica reads against upcoming server versions.
* [JVMCBC-1652](https://couchbasecloud.atlassian.net/browse/JVMCBC-1652): Shading the Couchbase SDK no longer causes it report a version number of `0.0.0`.
* [JVMCBC-1657](https://couchbasecloud.atlassian.net/browse/JVMCBC-1657): Improved the backpressure implementation for reactive SQL++, Analytics, and Full-Text Search queries. The SDK now requires less memory to buffer results if the consumer cannot keep up with the producer.
* [JVMCBC-1658](https://couchbasecloud.atlassian.net/browse/JVMCBC-1658): When the SDK removes uninteresting Netty stack frames from stack traces, it now also applies the filtering to suppressed exceptions. This improves stack trace readability in some cases when Project Reactor debugging is enabled.

#### [](#new-features-2)New Features

* [SCBC-483](https://couchbasecloud.atlassian.net/browse/SCBC-483): A Full-Text Search vector query now has an optional "prefilter" parameter. This is a non-vector query that the server executes first to get an intermediate result. Then it executes the vector query on the intermediate result to get the final result.
* [JVMCBC-1637](https://couchbasecloud.atlassian.net/browse/JVMCBC-1637): A Bill of Materials (BOM) for Couchbase JVM clients is now available. It specifies compatible versions of the Java, Scala, and Kotlin clients, as well as the optional metrics and tracing components. <https://central.sonatype.com/artifact/com.couchbase.client/couchbase-client-bom>.

## [](#scala-sdk-1-8-releases)Scala SDK 1.8 Releases

Version 1.8 of the Scala SDK implements the 3.7 [SDK API](compatibility.md#api-version).

### [](#version-1-8-3-11-july-2025)Version 1.8.3 (11 July 2025)

Version 1.8.3 is the third maintenance release of the 1.8 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.8.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-8)Bug Fixes

* [JVMCBC-1654](https://couchbasecloud.atlassian.net/browse/JVMCBC-1654): FIxed a bug that prevented `Collection.getAnyReplica()`, `getAllReplicas()`, `lookupInAnyReplica()`, `lookupInAllReplicas()`, `scan()`, `[Reactive]BatchHelper.exists()`, and `getIfExists()` from timing out if the bucket does not exist or is not accessible.

### [](#version-1-8-2-4-june-2025)Version 1.8.2 (4 June 2025)

Version 1.8.2 is the second maintenance release of the 1.8 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.8.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-9)Bug Fixes

* [SCBC-487](https://couchbasecloud.atlassian.net/browse/SCBC-487): The `flexIndex` parameter in `TransactionQueryOptions` is now correctly passed to the server.

#### [](#improvements-8)Improvements

* [SCBC-486](https://couchbasecloud.atlassian.net/browse/SCBC-486): Case class constructors made public again, for all input case classes that are part of the public interface.
* [JVMCBC-1647](https://couchbasecloud.atlassian.net/browse/JVMCBC-1647): Upgraded `Jackson` from `2.17.2` to `2.17.3`.

### [](#version-1-8-1-9-may-2025)Version 1.8.1 (9 May 2025)

Version 1.8.1 is the first maintenance release of the 1.8 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.8.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-10)Bug Fixes

* [SCBC-485](https://couchbasecloud.atlassian.net/browse/SCBC-485): `SearchQuery.toString()` has not been returning the query JSON since Scala SDK 1.4.5\. This regression has now been fixed.

#### [](#improvements-9)Improvements

* [JVMCBC-1631](https://couchbasecloud.atlassian.net/browse/JVMCBC-1631): Updated `Netty` to `4.1.119`.

### [](#version-1-8-0-9-april-2025)Version 1.8.0 (9 April 2025)

Version 1.8.0 is the first release of the 1.8 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.8.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#new-features-3)New Features

* [SCBC-459](https://couchbasecloud.atlassian.net/browse/SCBC-459): Allow to restrict replica set to selected server group. This feature allows the implementation of network optimization when traffic cost between server groups is higher than in the local group. In this case the application might select preferred server group in the connection options, and later opt-in for local operations during replica reads.
* [JVMCBC-1602](https://couchbasecloud.atlassian.net/browse/JVMCBC-1602:): Application Telemetry improvements.

## [](#scala-sdk-1-7-releases)Scala SDK 1.7 Releases

Version 1.7 of the Scala SDK implements the 3.6 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-7-9-11-march-2025)Version 1.7.9 (11 March 2025)

Version 1.7.9 is the ninth maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.9/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.9/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-10)Improvements

* [JVMCBC-1614](https://couchbasecloud.atlassian.net/browse/JVMCBC-1614): Added `ServiceType.id()`
* [JVMCBC-1615](https://couchbasecloud.atlassian.net/browse/JVMCBC-1615): Moved `nodeUUID` from `NodeIdentifier` to `HostAndServicePorts`.
* [JVMCBC-1616](https://couchbasecloud.atlassian.net/browse/JVMCBC-1616)Upgraded Netty to `4.1.118`.

### [](#version-1-7-8-11-february-2025)Version 1.7.8 (11 February 2025)

Version 1.7.8 is the eighth maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.8/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.8/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-11)Improvements

* [JVMCBC-1609](https://jira.issues.couchbase.com/browse/JVMCBC-1609): Added experimental client settings for tuning socket send/receive buffer size and channel outbound buffer high/low-water marks.

  * `io.sendBuffer`
  * `io.receiveBuffer`
  * `io.lowWaterMark`
  * `io.highWaterMark`  
  > [!NOTE]  
  > We do not currently recommend configuring these settings unless you are working with Couchbase technical support to diagnose a network performance issue.

### [](#version-1-7-7-08-january-2025)Version 1.7.7 (08 January 2025)

Version 1.7.7 is the seventh maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.7/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.7/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-11)Bug Fixes

* [JVMCBC-1592](https://jira.issues.couchbase.com/browse/JVMCBC-1592): When fetching fresh cluster topology information for a bucket, the SDK now dispatches the request to a random eligible node instead of using a round-robin algorithm. Randomizing the node selection avoids a pathological condition where if the number of open buckets is equal to the number of nodes, and one of the nodes is degraded, the config refresh attempt for a particular bucket would fail repeatedly because it was always sent to the degraded node.
* [SCBC-474](https://jira.issues.couchbase.com/browse/SCBC-474): Fixed a regression introduced in Scala SDK 1.4.3 that caused `JsonArray` and `JsonObject` to no longer be handled correctly when used as parameters in `QueryOptions`, and in `SearchOptions.raw`.

#### [](#improvements-12)Improvements

* [JVMCBC-1585](https://jira.issues.couchbase.com/browse/JVMCBC-1585): When a thread executing `clusterOrScope.queryStreaming()` is interrupted, the thrown `CancellationException` now has the original `InterruptedException` as its cause.

### [](#version-1-7-6-04-december-2024)Version 1.7.6 (04 December 2024)

Version 1.7.6 is the sixth maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.6/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.6/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-12)Bug Fixes

* [JVMCBC-1583](https://jira.issues.couchbase.com/browse/JVMCBC-1583): Fixed a race condition that could cause the SDK to continuously attempt to reconnect to a node, even after the node is rebalanced out of the cluster.

#### [](#improvements-13)Improvements

* [JVMCBC-1560](https://jira.issues.couchbase.com/browse/JVMCBC-1560): Added cluster UUID and name to metrics and spans.
* [JVMCBC-1582](https://jira.issues.couchbase.com/browse/JVMCBC-1582): Upgraded `Netty` from `4.1.112` to `4.1.115`.
* [SCBC-471](https://jira.issues.couchbase.com/browse/SCBC-471): Updated dependencies.

### [](#version-1-7-5-06-november-2024)Version 1.7.5 (06 November 2024)

Version 1.7.5 is the fifth maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.5/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.5/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-13)Bug Fixes

* [JVMCBC-1572](https://jira.issues.couchbase.com/browse/JVMCBC-1572): Due to a regression in 3.7.1, using a secure connection would cause `waitUntilReady()` to not wait, and would cause `ping()` to report failures even when nothing was wrong. The issue that caused these problems is now fixed.
* [JVMCBC-1577](https://jira.issues.couchbase.com/browse/JVMCBC-1577): Due to a regression in 3.7.1, sometimes a request made shortly after calling `Cluster.connect()` would fail with a message that said the service is not available in the cluster, even if the service was actually available. This no longer happens.
* [JVMCBC-1579](https://jira.issues.couchbase.com/browse/JVMCBC-1579): Deprecated `com.couchbase.client.core.node.NodeIdentifier` in favor of `com.couchbase.client.core.topology.NodeIdentifier`.

#### [](#improvements-14)Improvements

* [JVMCBC-1576](https://jira.issues.couchbase.com/browse/JVMCBC-1576): Bumped `protobuf` version from `3.23.2` to `3.25.5`.

### [](#version-1-7-4-08-october-2024)Version 1.7.4 (08 October 2024)

Version 1.7.4 is the fourth maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.4/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.4/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bug-fixes-14)Bug Fixes

* [JVMCBC-1570](https://jira.issues.couchbase.com/browse/JVMCBC-1570): The SDK was producing an incorrect partition map in `CouchbaseBucketConfig`, for buckets with >= 2 replicas. This has now been fixed.

#### [](#improvements-15)Improvements

* [JVMCBC-1573](https://jira.issues.couchbase.com/browse/JVMCBC-1573): `ExtParallelUnstaging` was producing more threads than required, leading to OOM when many concurrent transactions were executed. This has been rewritten to produce only the necessary number of threads are produced for each transaction.

### [](#version-1-7-3-23-september-2024)Version 1.7.3 (23 September 2024)

Version 1.7.3 is the third maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.9**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-16)Improvements

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

### [](#version-1-7-2-13-august-2024)Version 1.7.2 (13 August 2024)

Version 1.7.2 is the second maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-17)Improvements

* [JVMCBC-1547](https://issues.couchbase.com/browse/JVMCBC-1547): Updated DnsJava to 3.6.0.
* [JCBC-2157](https://issues.couchbase.com/browse/JCBC-2157): Transaction settings are now configurable using the same callback pattern used by other environment settings. Here's an example of the new syntax:  
```scala  
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

#### [](#bug-fixes-15)Bug Fixes

* [SCBC-462](https://issues.couchbase.com/browse/SCBC-462), [SCBC-469](https://issues.couchbase.com/browse/SCBC-469): Now uses the correct internal transaction protocol identifier when interacting with other transactions — allowing Scala to continue sharing the core JVM implementation, but not having to follow implementation in lockstep with the Java SDK.

### [](#version-1-7-1-23-july-2024)Version 1.7.1 (23 July 2024)

Version 1.7.1 is the first maintenance release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.7.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-18)Improvements

* [JVMCBC-1523](https://issues.couchbase.com/browse/JVMCBC-1523): Upgraded `org.iq80.snappy` from 0.4 to 0.5.
* [JCBC-1528](https://issues.couchbase.com/browse/JCBC-1528): Provided default values for tags for Micrometer.
* [JCBC-1532](https://issues.couchbase.com/browse/JCBC-1532): Upgraded Jackson from 2.17.0 to 2.17.1.
* [JVMCBC-1540](https://issues.couchbase.com/browse/JVMCBC-1540): Improved compatibility with Spring Data Couchbase by reversing an internal API change present in Couchbase Java SDK 3.6.2 and 3.7.0\. This API change prevented upgrading to the latest Couchbase SDK, independently of the Spring Data Couchbase version.
* [JVMCBC-1544](https://issues.couchbase.com/browse/JVMCBC-1544): The `upsertIndex()` call now prevents vector indexes from being created on server versions before version 7.6.0, which do not support these index types.

#### [](#bugfixes)Bugfixes

* [JVMCBC-1530](https://issues.couchbase.com/browse/JVMCBC-1530): Deprecated the `com.couchbase.client.core.error.QueryException` class. This exception is from the SDK 3 API's beta development, and has never been thrown in a GA version of a Couchbase SDK.
* [JVMCBC-1534](https://issues.couchbase.com/browse/JVMCBC-1534): Fixed possible `DURABILITY_INVALID_LEVEL` if `Durability.NONE` is used with transactions.

### [](#version-1-7-0-15-june-2024)Version 1.7.0 (15 June 2024)

Version 1.7.0 is the first release of the 1.7 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.7.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.7.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-19)Improvements

* [SCBC-461](https://issues.couchbase.com/browse/SCBC-461): Adds support for base64-encoded vectors in `VectorQuery`.

#### [](#bugfixes-2)Bugfixes

* [SCBC-428](https://issues.couchbase.com/browse/SCBC-428): Fixed a regression introduced in version 3.4.5 that caused a Full-Text Search `BooleanQuery` to throw `InvalidArgumentException: Compound query has no child query` unless all three of "must", "should", and "mustNot" were specified.
* [SCBC-463](https://issues.couchbase.com/browse/SCBC-463): Using a `MatchPhraseQuery` no longer results in an error.

## [](#scala-sdk-1-6-releases)Scala SDK 1.6 Releases

Version 1.6 of the Scala SDK implements the 3.5 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-6-3-19-august-2024)Version 1.6.3 (19 August 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.6.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-20)Improvements

* [JVMCBC-1532](https://issues.couchbase.com/browse/JVMCBC-1532): Upgraded Jackson to 2.17.2.

### [](#version-1-6-2-29-april-2024)Version 1.6.2 (29 April 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.6.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-21)Improvements

* [SCBC-450](https://issues.couchbase.com/browse/SCBC-450), [JVMCBC-1508](https://issues.couchbase.com/browse/JVMCBC-1508), and [JVMCBC-1509](https://issues.couchbase.com/browse/JVMCBC-1509): Upgraded dependencies.

#### [](#bugfixes-3)Bugfixes

* [JVMCBC-1506](https://issues.couchbase.com/browse/JVMCBC-1506): Reduced the rate at which messages appear in the server's `http_access.log` when a user provides valid credentials but does not have permission to access the bucket.
* [JVMCBC-1512](https://issues.couchbase.com/browse/JVMCBC-1512): Updated Service in Cluster Configuration if only the port is changed.

### [](#version-1-6-1-5-april-2024)Version 1.6.1 (5 April 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.6.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-22)Improvements

* [JVMCBC-1477](https://issues.couchbase.com/browse/JVMCBC-1477): Reduced the rate at which messages appear in the server's `http_access.log` when invalid credentials are provided resulting in 401 errors. Issues resulting in 403 errors will be handled in a future release.
* [JVMCBC-1498](https://issues.couchbase.com/browse/JVMCBC-1498): The fields of a `SearchRow` from a Full-Text Search result are now included in the output of `SearchRow.toString()`.
* [JVMCBC-1499](https://issues.couchbase.com/browse/JVMCBC-1499): Disabled DNS SRV caching. The SDK now responds quicker to DNS changes in dynamic environments like Kubernetes.
* [JVMCBC-1500](https://issues.couchbase.com/browse/JVMCBC-1500): Added `EventingFunctionLanguageCompatibility.VERSION_7_2_0`.

### [](#version-1-6-0-11-march-2024)Version 1.6.0 (11 March 2024)

Version 1.6.0 is the first release of the 1.6 series. The SDK now supports Vector Search, with Server 7.6 (self-managed or Capella).

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.6.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.6.3**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-23)Improvements

* [SCBC-444](https://issues.couchbase.com/browse/SCBC-444): Added support for vector search, a new feature in Couchbase Server 7.6\. This API is currently at `@Volatile` level.
* [SCBC-454](https://issues.couchbase.com/browse/SCBC-454): `ScopeSearchIndexManager` and its Async/Reactive variants are now part of the committed public API.
* [JVMCBC-1487](https://issues.couchbase.com/browse/JVMCBC-1487): Upgraded reactor-core from 3.5.8 to 3.6.3.
* [JVMCBC-1488](https://issues.couchbase.com/browse/JVMCBC-1488): Upgraded Jackson from 2.16.0 to 2.16.1.
* [JVMCBC-1489](https://issues.couchbase.com/browse/JVMCBC-1489): Upgraded Netty from 4.1.101 to 4.1.107.
* [JVMCBC-1491](https://issues.couchbase.com/browse/JVMCBC-xxxx): `Collection.scan()` methods are not part of the SDK's committed API. These methods do range-scans of documentIds. This feature requires Couchbase Server 7.6 or later.
* [JVMCBC-1493](https://issues.couchbase.com/browse/JVMCBC-xxxx): `Collection.lookupInAnyReplica()` and `Collection.lookupInAllReplicas()` are now part of the SDK's committed API. These methods do sub-document lookups against replicas. This feature requires Couchbase Server 7.6 or later.

#### [](#bugfixes-4)Bugfixes

* [JVMCBC-1480](https://issues.couchbase.com/browse/JVMCBC-1480): `couchbase2:` should use exponential backoff when bypassing `BestEffortRetryStrategy`.
* [JVMCBC-1494](https://issues.couchbase.com/browse/JVMCBC-1494): If you specify `min=1` for a Full-Text Search disjunction query, the SDK now always sends the value to the server. Previously, the SDK assumed `1` was the default value, and omitted the parameter in that case.

## [](#scala-sdk-1-5-releases)Scala SDK 1.5 Releases

Version 1.5 of the Scala SDK implements the 3.4 [SDK API](compatibility.md#api-version), and includes support for the `couchbase2://` connection protocol — please see [Cloud Native Gateway](../howtos/managing-connections.md#cloud-native-gateway) for more information. See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-5-3-6-february-2024)Version 1.5.3 (6 February 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.5.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-24)Improvements

* [SCBC-414](https://issues.couchbase.com/browse/SCBC-414): All forms of `getAnyReplica()` and `getAllReplicas()` will now use the `Transcoder` provided as an option.
* [SCBC-443](https://issues.couchbase.com/browse/SCBC-443): Transactions now have a third, `Future`\-based API.
* [SCBC-445](https://issues.couchbase.com/browse/SCBC-445): `maxExpiry(Duration(-1, TimeUnit.SECONDS))` can now be used to specify that a collection has no expiry, overriding whatever is set on the bucket.
* [SCBC-446](https://issues.couchbase.com/browse/SCBC-446): Added support for `scope.search()` and `scope.searchIndexes()`, for querying and managing FTS scoped indexes.
* [SCBC-448](https://issues.couchbase.com/browse/SCBC-448): All functionality is now present for `SearchIndexManager`.
* [JVMCBC-1460](https://issues.couchbase.com/browse/JVMCBC-1460): `couchbase2` now supports compressing data between the SDK and the server.
* [JVMCBC-1464](https://issues.couchbase.com/browse/JVMCBC-1464): The `metrics-opentelemetry` package is now aligned with the same `OpenTelemetry` version as `tracing-opentelemetry`.
* [JVMCBC-1468](https://issues.couchbase.com/browse/JVMCBC-1468): `Cluster.connect` now validates that connection strings using the `couchbase2` scheme have exactly one host. (Previously, hosts after the first were silently ignored.).
* [JVMCBC-1470](https://issues.couchbase.com/browse/JVMCBC-1470): Improved support for Full Text Search in `couchbase2` mode.
* [JVMCBC-1472](https://issues.couchbase.com/browse/JVMCBC-1472): `couchbase2` errors will now include diagnostic information when CNG is running with the `--debug` flag.

#### [](#bugfixes-5)Bugfixes

* [SCBC-430](https://issues.couchbase.com/browse/SCBC-430): `lookupInAnyReplica()` and `lookupInAllReplicas()` will now raise `DocumentUnretrievableException` if all replicas fail.
* [SCBC-449](https://issues.couchbase.com/browse/SCBC-449): The SDK now correctly serializes an FTS index during index creation.
* [JVMCBC-1475](https://issues.couchbase.com/browse/JVMCBC-1475): Accessing the terms of a `TermFacet` result no longer throws `NullPointerException` if the target field is absent from all documents.

### [](#version-1-5-2-5-january-2024)Version 1.5.2 (5 January 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.5.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.2/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bugfixes-6)Bugfixes

* [SCBC-441](https://issues.couchbase.com/browse/SCBC-441): Transactional queries were sending `ScanConsistency` when in `NOT_BOUNDED` mode, as set by `core-io`. The desired behavior is for the default transactional query `ScanConsistency` to be `not-set`, and this fix ensures that there should now be no `QueryScanConsistency` by default.
* [JVMCBC-1455](https://issues.couchbase.com/browse/JVMCBC-1455): Fixed compatibility with `couchbase2://` endpoints by upgrading internal GRPC dependency. All couchbase2 protocol users should upgrade to this release.
* [JVMCBC-1463](https://issues.couchbase.com/browse/JVMCBC-1463): Fixed compatibility between `couchbase2://` endpoints and the `tracing-opentelemetry` module.

### [](#version-1-5-1-8-december-2023)Version 1.5.1 (8 December 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.5.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.1/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-25)Improvements

* [JVMCBC-1435](https://issues.couchbase.com/browse/JVMCBC-1435), [JVMCBC-1436](https://issues.couchbase.com/browse/JVMCBC-1436): Upgraded Netty and Jackson dependencies.
* [JVMCBC-1440](https://issues.couchbase.com/browse/JVMCBC-1440): Adding `DocumentNotLockedException` supporting future Couchbase Server versions that will return an error code when unlocking a document that is not locked.
* [SCBC-438](https://issues.couchbase.com/browse/SCBC-438): Added new overloads for `Transactions.run` that take `TransactionOptions` directly.

#### [](#bugfixes-7)Bugfixes

* [JVMCBC-1433](https://issues.couchbase.com/browse/JVMCBC-1433): The SDK can now connect to Memcached buckets whose names contain the percent (`%`) character. (We'd like to take this opportunity to remind everyone that Memcached buckets are deprecated in favor of Ephemeral buckets.)
* [JVMCBC-1437](https://issues.couchbase.com/browse/JVMCBC-1437): With Couchbase Server versions that support updating a collection's max expiry, it's now possible to clear the expiry by passing `Duration.ZERO` for the new value.
* [JVMCBC-1441](https://issues.couchbase.com/browse/JVMCBC-1441): The SDK now handles an additional error case for `IndexNotFoundException`.
* [JVMCBC-1442](https://issues.couchbase.com/browse/JVMCBC-1442): Fixed a dependency issue with `tracing-opentelemetry` module.
* [SCBC-435](https://issues.couchbase.com/browse/SCBC-435): Upgraded the Scala build versions, to allow compiling with JDK 21.
* [SCBC-436](https://issues.couchbase.com/browse/SCBC-436): `CollectionManager.createCollection(CollectionSpec)` now correctly passes expiry.

### [](#version-1-5-0-21-november-2023)Version 1.5.0 (21 November 2023)

Version 1.5.0 is the first release of the 1.5 series.

The SDK now supports distributed ACID transactions natively.

The SDK now supports the new couchbase2 protocol, which is upcoming in future Couchbase Server versions. It can be enabled through using a connection string starting with `couchbase2://`. Please see [Cloud Native Gateway](../howtos/managing-connections.md#cloud-native-gateway) for more information.

The SDK now directly depends on SLF4J, which may impact some users — see below for details.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.5.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.0/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#api-impacting)API Impacting

* [JVMCBC-1319](https://issues.couchbase.com/browse/JVMCBC-1319): BEHAVIORAL CHANGE  
As [previously announced](https://www.couchbase.com/forums/t/embracing-slf4j-in-couchbase-java-sdk-3-5/36474), the SLF4J API is now a required dependency, and the SDK does all logging through SLF4J. The following client settings for customizing logging behavior are deprecated, and no longer have any effect:

  * `logger.disableSlf4J`
  * `logger.fallbackToConsole`
  * `logger.consoleLoggerFormatter`  
  If your project does not already use SLF4J, please follow the announcement link for details and a mini-migration guide.

#### [](#improvements-26)Improvements

* [SCBC-432](https://issues.couchbase.com/browse/SCBC-432). Support added for distributed ACID transactions.
* [JVMCBC-1402](https://issues.couchbase.com/browse/JVMCBC-1402), [JVMCBC-1410](https://issues.couchbase.com/browse/JVMCBC-1410): Upgraded Netty from 4.1.96 to 4.1.100, and upgraded `OpenTelemetry` dependency.
* [JVMCBC-1430](https://issues.couchbase.com/browse/JVMCBC-1430): Optimization: removed creation of unnecessary metrics labels when default `LoggingMeter` is used.
* [JVMCBC-1391](https://issues.couchbase.com/browse/JVMCBC-1391): The Bucket Manager API is now forward-compatible with future versions of Couchbase Server that might support storage engine types other than "magma" and "couchstore".
* [JVMCBC-1327](https://issues.couchbase.com/browse/JVMCBC-1327): Improved support for failover handling in future server versions.

#### [](#bugfixes-8)Bugfixes

* [JVMCBC-1264](https://issues.couchbase.com/browse/JVMCBC-1264): DNS SRV lookups now honor the DNS search path. This enables DNS SRV resolution in Kubernetes environments where the `*-srv` hostname advertised by the Couchbase Operator is a partial name that must be resolved using a suffix from the DNS search path.
* [JVMCBC-1426](https://issues.couchbase.com/browse/JVMCBC-1426): When Couchbase Server is too busy to start a new KV range scan, the SDK now retries instead of throwing a `CouchbaseException`.
* [SCBC-433](https://issues.couchbase.com/browse/SCBC-433): Fix a regression in getAllScopes.

## [](#scala-sdk-1-4-releases)Scala SDK 1.4 Releases

Version 1.4 of the Scala SDK implements the 3.4 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-4-11-4-october-2023)Version 1.4.11 (4 October 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.11/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.11/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-27)Improvements

* [JCBC-2046](https://issues.couchbase.com/browse/JCBC-2046): With thanks to community member [Marcin Grzejszczak](https://github.com/marcingrzejszczak) for the contribution, support for Micrometer Observation has been added to all JVM SDKs via the new `tracing-micrometer-observation` module.
* [JVMCBC-1327](https://issues.couchbase.com/browse/JVMCBC-1327): Internal improvements to support upcoming faster failover and config push features.

#### [](#bugfixes-9)Bugfixes

* [JVMCBC-1364](https://issues.couchbase.com/browse/JVMCBC-1364): Fixed decoding of certain niche sub-document errors, so they no longer raise a `DecodingFailureException`.
* [SCBC-424](https://issues.couchbase.com/browse/SCBC-424): `ConflictResolution` field is now correctly sent on creating a bucket.

### [](#version-1-4-10-6-september-2023)Version 1.4.10 (6 September 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.10/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.10/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.8**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-28)Improvements

* [JVMCBC-1367](https://issues.couchbase.com/browse/JVMCBC-1367): The `db.couchbase.operations` metric now has `db.name` (bucket), `db.couchbase.scope`, `db.couchbase.collection` and `outcome` labels (tags). This new feature is at Stability.Volatile, and may change before it is promoted to Stability.Committed in a future release.
* [JVMCBC-1311](https://issues.couchbase.com/browse/JVMCBC-1311), [JVMCBC-1352](https://issues.couchbase.com/browse/JVMCBC-1352): Upgraded dependencies.
* [SCBC-419](https://issues.couchbase.com/browse/SCBC-419): Support deserializing `Float`.

#### [](#bugfixes-10)Bugfixes

* [JVMCBC-1350](https://issues.couchbase.com/browse/JVMCBC-1350): `lookupInAnyReplica` now throws `FeatureNotAvailableException` if the server does not support the feature.
* [JVMCBC-1351](https://issues.couchbase.com/browse/JVMCBC-1351): `lookupInAnyReplica` no longer hangs when too many operations are specified.
* [JVMCBC-1353](https://issues.couchbase.com/browse/JVMCBC-1353): Removed the unrelocated `io.opentracing` classes that accidentally slipped into version 2.4.9 of the Couchbase `core-io` library.
* [JVMCBC-1361](https://issues.couchbase.com/browse/JVMCBC-1361): When the SDK receives multiple cluster map versions at the same time, it is now more careful about applying only the most recent version. Before this change, there was a brief window where the SDK could apply an obsolete cluster map. If this happened, the SDK would temporarily dispatch requests to incorrect or non-existent nodes. This condition was typically short-lived, and healed the next time the SDK polled for an updated cluster map, or dispatched a KV request to the wrong node.
* [JVMCBC-1368](https://issues.couchbase.com/browse/JVMCBC-1368): Fixed a rare `java.lang.ArithmeticException: / by zero` exception in `RoundRobinSelectionStrategy.select` that could occur during rebalance.
* [SCBC-420](https://issues.couchbase.com/browse/SCBC-420): Scope-level queries will now work correctly (they now send the `query_context` parameter).

### [](#version-1-4-9-2-august-2023)Version 1.4.9 (2 August 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.9/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.9/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-29)Improvements

* [JVMCBC-1339](https://issues.couchbase.com/browse/JVMCBC-1339): When KV traffic capture is enabled, each `ReadTrafficCapturedEvent` now contains a single protocol frame, and the human-readable frame description is more accurate.
* [JVMCBC-1320](https://issues.couchbase.com/browse/JVMCBC-1320): The `waitUntilReady` method is now more aggressive about retrying failed pings. Also, waiting for a desired state of `DEGRADED` no longer fails when the client is fully connected to the cluster.
* [JVMCBC-1343](https://issues.couchbase.com/browse/JVMCBC-1343): Reduced the default value for the `io.idleHttpConnectionTimeout` client setting to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures.

### [](#version-1-4-8-19-july-2023)Version 1.4.8 (19 July 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.8/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.8/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-30)Improvements

* [SCBC-406](https://issues.couchbase.com/browse/SCBC-406): Upcoming Couchbase server release 7.6 will support having SQL++ queries read from replicas, in scenarios where the active is unavailable (such as failover). This improves availability, though users should be aware that they may be reading stale data. The option is activated with `scope.query("…​", QueryOptions().useReplica(true))`, and is disabled by default. It will only work against 7.6 and above: against older server versions, it will return a `Failure(FeatureNotAvailableException)`.
* [JVMCBC-1322](https://issues.couchbase.com/browse/JVMCBC-1322): The `waitUntilReady()` method now logs additional diagnostic information to the `com.couchbase.core.WaitUntilReady` logging category at `DEBUG` level.

### [](#version-1-4-7-12-june-2023)Version 1.4.7 (12 June 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.7/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.7/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-31)Improvements

* [JVMCBC-1290](https://issues.couchbase.com/browse/JVMCBC-1290): For compatibility with other modern Couchbase SDKs, certificate verification can now be disabled using the connection string parameter: `tls_verify=none`. This config property is introduced at stability level `Volatile`, meaning it may change in a patch release without notice.
* [JVMCBC-1278](https://issues.couchbase.com/browse/JVMCBC-1278), [JVMCBC-1310](https://issues.couchbase.com/browse/JVMCBC-1310), [JVMCBC-1313](https://issues.couchbase.com/browse/JVMCBC-1313): Dependencies updated.

#### [](#bugs)Bugs

* [JVMCBC-1288](https://issues.couchbase.com/browse/JVMCBC-1288): Fixed a regression in Couchbase Java SDK 3.4.5 and Scala SDK 1.4 .5 that prevented Full-Text Search result rows from including an explanation when requested.
* [JVMCBC-1292](https://issues.couchbase.com/browse/JVMCBC-1292): Removed `META-INF/versions/9/module-info.class` from the `core-io` jar. This file was associated with an improperly repackaged dependency, and never should have been there.

### [](#version-1-4-6-4-may-2023)Version 1.4.6 (4 May 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.6/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.6/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#bugs-2)Bugs

* [JVMCBC-1275](https://issues.couchbase.com/browse/JVMCBC-1275): Fixed a regression in Couchbase Java SDK 3.4.5 and Scala SDK 1.4.5 that caused Full Text Search `term` queries to throw `NullPointerException` unless `prefixLength` and `fuzziness` were specified.
* [JVMCBC-1285](https://issues.couchbase.com/browse/JVMCBC-1285): Fixed a regression in Couchbase Java SDK 3.4.5 and Scala SDK 1.4.5 that caused Full-Text Search queries to fail to report the locations of some terms. Specifically, any location that did not have `arrayPositions` was omitted from the results.

### [](#version-1-4-5-13-april-2023)Version 1.4.5 (13 April 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.5/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.5/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-32)Improvements

* [JVMCBC-1223](https://issues.couchbase.com/browse/JVMCBC-1223): Adds a `RetryReason.AUTHENTICATION_ERROR` at `Uncommitted` API stability level. A custom `RetryStrategy` can use this new, more granular information to distinguish if a connection problem is down to an authentication issue.
* [SCBC-392](https://issues.couchbase.com/browse/SCBC-392), [SCBC-394](https://issues.couchbase.com/browse/SCBC-394): Internal improvements to further align Scala with the Java implementation for Full Text Search.

#### [](#bugs-3)Bugs

* [JVMCBC-1252](https://issues.couchbase.com/browse/JVMCBC-1252): Orphaned "observe" operations will no longer occasionally contain a `total_duration_us` field equal to 0.
* [JVMCBC-1255](https://issues.couchbase.com/browse/JVMCBC-1255): If you were subscribing to the event bus and printing all the events, you may have noticed `Event.toString()` throwing a `NullPointerException` if the event context is null. `Event.toString()` now handles null contexts more gracefully, and no longer throws this exception.

### [](#version-1-4-4-8-march-2023)Version 1.4.4 (8 March 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.4/com/couchbase/client/scala/index.html) [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.4/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-33)Improvements

* [SCBC-383](https://issues.couchbase.com/browse/SCBC-383), [SCBC-391](https://issues.couchbase.com/browse/SCBC-391): Adding `CollectionQueryIndexManager`, allowing query index management at the collection level via `collection.queryIndexes()`.
* [JVMCBC-1237](https://issues.couchbase.com/browse/JVMCBC-1237): Added "network" as an alias for the "io.networkResolution" connection string parameter. For example, the connection string "couchbase://example.com?network=external" is now equivalent to "couchbase://example.com?io.networkResolution=external". This was done for compatibility with other Couchbase SDKs that use "network" as the name of this parameter.

#### [](#bugs-4)Bugs

* [JVMCBC-1232](https://issues.couchbase.com/browse/JVMCBC-1232): `Cluster.connect()` now rejects connection strings that have no addresses (like "couchbase://"). Before this change, it would accept the invalid connection string, and subsequent operations would fail with a misleading error message: "The cluster does not support cluster-level queries".
* [JVMCBC-1234](https://issues.couchbase.com/browse/JVMCBC-1234): Fixed a regression in Java SDK 3.4.3 and Scala SDK 1.4.3 that caused SQL++ query result metadata to always include metrics, regardless of the "metrics" query option.

### [](#version-1-4-3-9-february-2023)Version 1.4.3 (9 February 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.3/)

The supported and tested dependencies for this release are:

* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-34)Improvements

* [SCBC-384](https://issues.couchbase.com/browse/SCBC-384), [SCBC-385](https://issues.couchbase.com/browse/SCBC-385), [SCBC-386](https://issues.couchbase.com/browse/SCBC-386) [SCBC-387](https://issues.couchbase.com/browse/SCBC-387): Internally, the JVM SDKs are being aligned to share the same implementation of multiple pieces of functionality. This should not impact end-users, but will ensure conformity of behavior and performance between all JVM SDKs, going forwards.
* [JVMCBC-1181](https://issues.couchbase.com/browse/JVMCBC-1181): It is now possible to authenticate over secure connections even if the JVM does not support the SASL PLAIN authentication mechanisms.
* [JVMCBC-1184](https://issues.couchbase.com/browse/JVMCBC-1184): Updated dependencies.
* [JVMCBC-1213](https://issues.couchbase.com/browse/JVMCBC-1213): If too many operations are specified in a single sub-document lookup, the exception message now indicates why the operation failed.

#### [](#bug-fixes-16)Bug Fixes

* [JVMCBC-1160](https://issues.couchbase.com/browse/JVMCBC-1160): When a sub-document path has a syntax error or is inappropriate for an operation, the SDK now raises `PathInvalidException`. Prior to this change, it would raise a generic `CouchbaseException` with the message "Unexpected SubDocument response code".
* [SCBC-388](https://issues.couchbase.com/browse/SCBC-388): If expiry has not been requested on a KV get operation, then expiry fields in `GetResult` are now `None`, as expected.

### [](#version-1-4-2-16-january-2023)Version 1.4.2 (16 January 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.4.2**
* com.couchbase.client:**core-io:2.4.2**
* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-35)Improvements

* [JVMCBC-1175](https://issues.couchbase.com/browse/JVMCBC-1175): The SDK now includes native libraries for IO and TLS that can enhance performance on `aarch_64` architectures like Graviton and Apple Silicon. Previously, native libraries were included only for `x86_64` architectures. Native libraries for IO and TLS are enabled by default. If you need to disable native IO, set the `ioEnvironment.enableNativeIo` client setting to false. To disable native TLS, set the `security.enableNativeTls` client setting to false.

#### [](#bugs-5)Bugs

* [JVMCBC-1161](https://issues.couchbase.com/browse/JVMCBC-1161): Fixed a minor issue where `cluster.disconnect()` could occasionally timeout due to a race condition.
* [JVMCBC-1176](https://issues.couchbase.com/browse/JVMCBC-1176): Setting `security.enableNativeTls` to false now prevents the SDK from even attempting to load the native TLS library. (Prior to this change, the SDK would load the library and just not use it.) In addition to saving a bit of memory, this prevents the JVM from segfaulting on Alpine Linux where glibc is not available.
* [JVMCBC-1180](https://issues.couchbase.com/browse/JVMCBC-1180): Supporting in transactions a future version of Couchbase Server that requires query\_context be sent in all queries.
* [JVMCBC-1174](https://issues.couchbase.com/browse/JVMCBC-1174): Fixed a regression that prevented native TLS from being used regardless of whether the `security.enableNativeTls` client setting was set to true.

### [](#version-1-4-1-7-december-2022)Version 1.4.1 (7 December 2022)

Version 1.4.1 is the second release of the 1.4 series. The headline change is support for the KV range scan feature (`collection.scan()`), added at @Stability.Volatile level. This feature will be available in a future version of Couchbase Server.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.1/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.4.1**
* com.couchbase.client:**core-io:2.4.1**
* io.projectreactor:**reactor-core:3.5.0**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-36)Improvements

* [JVMCBC-1163](https://issues.couchbase.com/browse/JVMCBC-1163): Dependencies have been updated.
* [JVMCBC-1156](https://issues.couchbase.com/browse/JVMCBC-1156): The traffic tracing functionality has been enhanced to perform Wireshark-style dissection of portions of the KV protocol.
* [SCBC-377](https://issues.couchbase.com/browse/SCBC-377): KV range scan functionality (`collection.scan()`) added at @Stability.Volatile level.
* [SCBC-382](https://issues.couchbase.com/browse/SCBC-382): `Cluster.connect` now throws an `IllegalArgumentException` if you pass a pre-built `ClusterEnvironment` and a connection string incompatible with the environment. Before this change, the connection string scheme and parameters were always silently ignored when connecting with a pre-built cluster environment.

  * A pre-built environment without TLS enabled is incompatible with a connection string that specifies the secure `couchases` scheme.
  * A pre-built environment is incompatible with a connection string that has parameters.

#### [](#bugs-6)Bugs

* [JVMCBC-1157](https://issues.couchbase.com/browse/JVMCBC-1157): The SDK no longer rejects a `PersistTo` requirement in a bucket using the Magma storage engine. Before this change, the SDK would refuse the request because it misidentified Magma buckets as ephemeral (unable to persist documents).
* [JVMCBC-1167](https://issues.couchbase.com/browse/JVMCBC-1167): If you call `CancellationErrorContext.getWaitUntilReadyContext()` on an error context that didn't come from a "wait until ready" request, the method is now guaranteed to return null instead of sometimes throwing a `ClassCastException`.
* [SCBC-380](https://issues.couchbase.com/browse/SCBC-380): Bucket creation and update can now be used with Couchbase Server Community Edition 7.X.

### [](#version-1-4-0-24-october-2022)Version 1.4.0 (24 October 2022)

Version 1.4.0 is the first release of the 1.4 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.4.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.4.0**
* com.couchbase.client:**core-io:2.4.0**
* io.projectreactor:**reactor-core:3.4.24**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-37)Improvements

* [JVMCBC-1102](https://issues.couchbase.com/browse/JVMCBC-1102): Added support for serverless execution environments including AWS Lambda.
* [SCBC-371](https://issues.couchbase.com/browse/SCBC-371): Added support for configuration profiles, which allow you to quickly configure an environment for common use-cases. In particular, this makes it easy to apply timeouts appropriate for WAN (Internet) development, such as developing against a remote Couchbase Capella instance. Example usage: `val env = ClusterEnvironment.builder.applyProfile(ClusterEnvironment.WanDevelopmentProfile).build.get`.
* [SCBC-374](https://issues.couchbase.com/browse/SCBC-374), [JVMCBC-1154](https://issues.couchbase.com/browse/JVMCBC-1154): Bump dependencies.
* [SCBC-375](https://issues.couchbase.com/browse/SCBC-375): Changed `AuthenticationFailureException` error message to indicate that bucket hibernation is now a potential cause. Bucket hibernation is a feature coming in a future Couchbase release.
* [SCBC-376](https://issues.couchbase.com/browse/SCBC-376), [JVMCBC-1144](https://issues.couchbase.com/browse/JVMCBC-1144): If your Couchbase Server cluster's root certificate is signed by a well-known certificate authority whose certificate is included in the JVM's trust store, it's no longer necessary to configure the certificate in the securityConfig settings.

#### [](#removals)Removals

* [SCBC-372](https://issues.couchbase.com/browse/SCBC-372): We have made the difficult decision to remove the build for Scala 2.11\. Scala 2.11's last release was in November 2017, and supporting this legacy version is now impeding our ability to also support 2.12, 2.13 and in future Scala 3\. Scala 2.11 users should continue to use the previous release (1.3.4) and are strongly recommended to upgrade to Scala 2.12 or 2.13, both of which are fully supported. Scala 2.11 has never been officially supported for the Couchbase Scala SDK, but it was previously possible for developers to build it themselves.

#### [](#bugs-7)Bugs

* [JVMCBC-1141](https://issues.couchbase.com/browse/JVMCBC-1141): Provide required OpenTelemetry span attributes.
* [JVMCBC-1155](https://issues.couchbase.com/browse/JVMCBC-1155): Make sure targeted round robin request keeps retrying if no config is available.

## [](#scala-sdk-1-3-releases)Scala SDK 1.3 Releases

Version 1.3 of the Scala SDK implements the 3.3 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-3-4-9-september-2022)Version 1.3.4 (9 September 2022)

Version 1.3.4 is the fifth release of the 1.3 series, and is a maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.3.4/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.4/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.3.4**
* com.couchbase.client:**core-io:2.3.4**
* io.projectreactor:**reactor-core:3.4.22**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-38)Improvements

* [JVMCBC-1131](https://issues.couchbase.com/browse/JVMCBC-1131): Added ability to track the number of created instances. Users can now set to hard-fail if too many instances are created.
* [JVMCBC-1134](https://issues.couchbase.com/browse/JVMCBC-1134): Updated `MemcachedProtocol::decodeStatus` to be inlineable.
* [JVMCBC-1135](https://issues.couchbase.com/browse/JVMCBC-1135): Moved `Core#reconfiguration` off IO threads.
* [JVMCBC-1143](https://issues.couchbase.com/browse/JVMCBC-1143): Failed telemetry spans will now record their exception and error status.
* [JVMCBC-1145](https://issues.couchbase.com/browse/JVMCBC-1145): Updated maintenance dependencies.

#### [](#bug-fixes-17)Bug Fixes

* [SCBC-367](https://issues.couchbase.com/browse/SCBC-367): Fixed issue where a `NullPointerException` was thrown for a non-existent FTS index.

### [](#version-1-3-3-2-august-2022)Version 1.3.3 (2 August 2022)

Version 1.3.3 is the fourth release of the 1.3 series, and is a maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.3.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.3/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.3.3**
* com.couchbase.client:**core-io:2.3.3**
* io.projectreactor:**reactor-core:3.4.21**
* org.reactivestreams:**reactive-streams:1.0.4**

#### [](#improvements-39)Improvements

* [JVMCBC-1116](https://issues.couchbase.com/browse/JVMCBC-1116): Dependency versions have been increased.

#### [](#bug-fixes-18)Bug Fixes

* [JVMCBC-1119](https://issues.couchbase.com/browse/JVMCBC-1119): The num (kv) nodesExt to equal number of nodes check can lead to otherwise healthy clusters being flagged as not ready. The check has been removed, and now the \` Bucket `waitUntilReady` will not timeout on these edge cases.
* [JVMCBC-1120](https://issues.couchbase.com/browse/JVMCBC-1120): `ClusterConfig#allNodeAddresses` now takes global config into account — avoiding the triggering of some unnecessary reconfigurations.
* [JVMCBC-1112](https://issues.couchbase.com/browse/JVMCBC-1112): Deprecated Reactor Processors have been replaced.
* [JVMCBC-1115](https://issues.couchbase.com/browse/JVMCBC-1115): The SDK now allows for configurations with _only_ TLS ports.

### [](#version-1-3-2-6-july-2022)Version 1.3.2 (6 July 2022)

Version 1.3.2 is the third release of the 1.3 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.3.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.3.2**
* com.couchbase.client:**core-io:2.3.2**
* io.projectreactor:**reactor-core:3.4.17**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-19)Bug Fixes

* [JVMCBC-1103](https://issues.couchbase.com/browse/JVMCBC-1103): To reduce overhead, the `MAX_PARALLEL_FETCH` value in `KeyValueBucketRefresher` has been updated to only fetch one config per poll interval.
* [JVMCBC-1104](https://issues.couchbase.com/browse/JVMCBC-1104): Fixed issue where the global refresher did not honor the config poll interval.

### [](#version-1-3-1-8-june-2022)Version 1.3.1 (8 June 2022)

Version 1.3.1 is the second release of the 1.3 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.3.1/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.1/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.3.1**
* com.couchbase.client:**core-io:2.3.1**
* io.projectreactor:**reactor-core:3.4.17**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-40)Improvements

* [JVMCBC-1089](https://issues.couchbase.com/browse/JVMCBC-1089): SDK users can now customize the `ConsoleLogger` format.
* [JVMCBC-1093](https://issues.couchbase.com/browse/JVMCBC-1093): Previously, when a DNS SRV lookup failure occured, the SDK logged this as a `WARNING` along with a stack trace. The lookup failure is typically harmless, so the log message has now been downgraded to `INFO` level, without a stack trace.
* [JVMCBC-1088](https://issues.couchbase.com/browse/JVMCBC-1088): Updated Netty to version `4.1.77.Final`.

### [](#version-1-3-0-26-april-2022)Version 1.3.0 (26 April 2022)

Version 1.3.0 is the first release of the 1.3 series.

The two headline changes in this release:

* Supports the new functionality of Couchbase Server 7.1.
* Bundles the public server security certificates for Couchbase Capella, to make it easier for users to get started with Capella.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.3.0/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.3.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.3.0**
* com.couchbase.client:**core-io:2.3.0**
* io.projectreactor:**reactor-core:3.4.17**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-41)Improvements

* [SCBC-352](https://issues.couchbase.com/browse/SCBC-352): Scala SDK now bundles the public Capella CA certificate.
* [JVMCBC-1074](https://issues.couchbase.com/browse/JVMCBC-1074): When trying to connect to Capella without enabling TLS, an exception will be returned stating that TLS is required (instead of an `UnknownHostException`).
* [JVMCBC-1076](https://issues.couchbase.com/browse/JVMCBC-1076): Deprecated `Event.createdAt()` in favor of a version that returns an `Instant`.
* [JVMCBC-1078](https://issues.couchbase.com/browse/JVMCBC-1078): The SDK now allows you to customize the `schedulerThreadCount`.
* [JVMCBC-1079](https://issues.couchbase.com/browse/JVMCBC-1079): Added `ConnectionString` SDK 3 compatibility attributes.
* [JVMCBC-1082](https://issues.couchbase.com/browse/JVMCBC-1082): Updated maintenance dependencies.
* [JVMCBC-1085](https://issues.couchbase.com/browse/JVMCBC-1085): The last connect attempt failure is now stored and exposed through `Diagnostics`.

#### [](#bugs-8)Bugs

* [SCBC-350](https://issues.couchbase.com/browse/SCBC-350): `NOT_STORED` is now correctly handled as `DocAlreadyExists` when inserting a document.
* [SCBC-353](https://issues.couchbase.com/browse/SCBC-353): Fixed issue where incorrect `GetAllIndexes` response is returned on the default collection.
* [JVMCBC-1077](https://issues.couchbase.com/browse/JVMCBC-1077): Shutting down a `ClusterEnvironment` now correctly stops a `Meter` owned by the cluster. This plugs a resource leak where `LoggingMeter` worker threads would never be stopped.

## [](#scala-sdk-1-2-releases)Scala SDK 1.2 Releases

Version 1.2 of the Scala SDK implements the 3.2 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-2-6-2-march-2022)Version 1.2.6 (2 March 2022)

There are no changes at the Scala SDK layer in this release, but there are bugfixes and improvements in the underlying core-io library.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.2.6/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.6/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.2.6**
* com.couchbase.client:**core-io:2.2.6**
* io.projectreactor:**reactor-core:3.4.14**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bugs-9)Bugs

* [JVMCBC-1060](https://issues.couchbase.com/browse/JVMCBC-1060): Fixed an issue where rate limited exceptions were not thrown for `SearchIndexManager` errors.
* [JVMCBC-1071](https://issues.couchbase.com/browse/JVMCBC-1071): The SDK now ensures that negative values are not sent to the `ValueRecorder`.

#### [](#new-features-4)New Features

* [JVMCBC-1057](https://issues.couchbase.com/browse/JVMCBC-1057): Added core infrastructure for the Backup service. Users can now make custom HTTP requests to the Backup service.
* [JVMCBC-1064](https://issues.couchbase.com/browse/JVMCBC-1064): When implementing a custom `RetryStrategy`, a new overload of `RetryAction.noRetry` lets you specify an exception translator for converting the default request cancellation exception into your preferred exception class.

#### [](#improvements-42)Improvements

* [JVMCBC-1065](https://issues.couchbase.com/browse/JVMCBC-1065): `RetryReason.allowsNonIdempotentRetry()` is now public, so you can call it from a custom `RetryStrategy`.
* [JVMCBC-1066](https://issues.couchbase.com/browse/JVMCBC-1066): When `SecurityConfig.Builder.trustCertificate(Path)` is given a file containing more than one certificate, it now trusts all the certificates instead of just the first one. Likewise, the result of `SecurityConfig.decodeCertificates(List<String>)` now includes all certificates in each string, not just the first certificate in each string.
* [JVMCBC-1068](https://issues.couchbase.com/browse/JVMCBC-1068): Added explicit handling of `FeatureNotAvailable` for Magma on CE.
* [JVMCBC-1069](https://issues.couchbase.com/browse/JVMCBC-1069): Added explicit handling of `FeatureNotAvailable` for Query CE.

### [](#version-1-2-5-2-february-2022)Version 1.2.5 (2 February 2022)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.2.5/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.5/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.2.5**
* com.couchbase.client:**core-io:2.2.5**
* io.projectreactor:**reactor-core:3.4.14**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bugs-10)Bugs

* [SCBC-339](https://issues.couchbase.com/browse/SCBC-339): `QueryIndexManager` `watchIndexes` now refreshes on every try.
* [JVMCBC-1046](https://issues.couchbase.com/browse/JVMCBC-1046): Do not load global config if node not in seed node list anymore.
* [JVMCBC-1058](https://issues.couchbase.com/browse/JVMCBC-1058): When a non-default scope or collection is being created with memcached buckets, the correct `FeatureNotAvailableException` is now thrown.

#### [](#improvements-43)Improvements

* [SCBC-341](https://issues.couchbase.com/browse/SCBC-341): Removed the Azure link type from the analytics management API, due to a change in the underlying server API. (Note that this interface is marked `@Stability.Volatile`, indicating that it can change.)
* [SCBC-315](https://issues.couchbase.com/browse/SCBC-315): Custom conflict resolution added to the bucket management API.
* [SCBC-319](https://issues.couchbase.com/browse/SCBC-319): FTS options now include `IncludeLocations` and Operator.
* [SCBC-333](https://issues.couchbase.com/browse/SCBC-333): Query API now supports preserving TTL.
* [SCBC-335](https://issues.couchbase.com/browse/SCBC-335): Index management API now supports managing indexes for a collection.
* [SCBC-342](https://issues.couchbase.com/browse/SCBC-342): Send configured user timeout to search.
* [JVMCBC-1037](https://issues.couchbase.com/browse/JVMCBC-1037): Avoid `whenComplete` closure for timeout cancellation. This is a small internal performance optimisation.
* [JVMCBC-1045](https://issues.couchbase.com/browse/JVMCBC-1045): Added an internal watchdog that updates the cluster configuration if the number of nodes changes.
* [JVMCBC-1048](https://issues.couchbase.com/browse/JVMCBC-1048): Always set `RequestContext` on `RequestSpan`.
* [JVMCBC-1056](https://issues.couchbase.com/browse/JVMCBC-1056): Log more info on unexpected endpoint disconnect.
* [JVMCBC-1059](https://issues.couchbase.com/browse/JVMCBC-1059): Handles any `retry:true` field in a query error result by retrying it.
* [JVMCBC-1055](https://issues.couchbase.com/browse/JVMCBC-1055), [JVMCBC-1047](https://issues.couchbase.com/browse/JVMCBC-1047), [JVMCBC-1051](https://issues.couchbase.com/browse/JVMCBC-1051): Updating dependencies. Netty goes from 4.1.72.Final to 4.1.73.Final. Jackson from 2.13.0 to 2.13.1\. Reactor from 3.4.12 to 3.4.14\. log4j (an optional dependency) from 2.15.0 to 2.17.1.

### [](#version-1-2-4-9-december-2021)Version 1.2.4 (9 December 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.2.4/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.4/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.2.4**
* com.couchbase.client:**core-io:2.2.4**
* io.projectreactor:**reactor-core:3.4.12**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-44)Improvements

* [SCBC-334](https://issues.couchbase.com/browse/SCBC-334): Bucket Management API - Added Storage Option for Magma.
* [JVMCBC-1033](https://issues.couchbase.com/browse/JVMCBC-1033), [JVMCBC-1034](https://issues.couchbase.com/browse/JVMCBC-1034): Updated internal and external dependencies to their latest bugfix versions. Also updated OpenTelemetry to 1.7.x.
* [JVMCBC-1035](https://issues.couchbase.com/browse/JVMCBC-1035): Made the (internal) subDocumentField is now serializable. This is needed for Apache Spark integration.
* [JVMCBC-1032](https://issues.couchbase.com/browse/JVMCBC-1032): Adde (volatile) support for Rate/Quota Limits. This is needed for Couchbase Capella.
* [JVMCBC-1039](https://issues.couchbase.com/browse/JVMCBC-1039): Included httpStatus in Query and Analytics Error Context, as well as the vbucket in the KV error context. This helps with debugging.

### [](#version-1-2-3-2-november-2021)Version 1.2.3 (2 November 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.2.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.3/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.2.3**
* com.couchbase.client:**core-io:2.2.3**
* io.projectreactor:**reactor-core:3.4.9**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-45)Improvements

* [JVMCBC-1026](https://issues.couchbase.com/browse/JVMCBC-1026): Added support for Error Map v2.
* [SCBC-326](https://issues.couchbase.com/browse/SCBC-326): Added `LookupInResult.contentAsBytes()`.
* [SCBC-324](https://issues.couchbase.com/browse/SCBC-324); [SCBC-337](https://issues.couchbase.com/browse/SCBC-337)Updated dependencies.

### [](#version-1-2-2-6-october-2021)Version 1.2.2 (6 October 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.2.2/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.2.2/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.2.2**
* com.couchbase.client:**core-io:2.2.2**
* io.projectreactor:**reactor-core:3.4.9**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-46)Improvements

* [SCBC-265](https://issues.couchbase.com/browse/SCBC-265): Added an eventing management API.
* [SCBC-332](https://issues.couchbase.com/browse/SCBC-332): Fixes to `JsonObject` and `JsonArray`: improvements to the API for Safe transformations, `fromSeq`, fixed some conversion issues.
* [JVMCBC-1015](https://issues.couchbase.com/browse/JVMCBC-1015): Improved client side error message when TLS is enforced on the server side.
* [JVMCBC-1016](https://issues.couchbase.com/browse/JVMCBC-1016): Gracefully handle more invalid connection string cases.
* [JVMCBC-1022](https://issues.couchbase.com/browse/JVMCBC-1022): Batch-Log messages in DefaultEventBus. Now events which are overflowing are not directly logged to stderr but rather batched up and logged at interval. Note that this implies some "loss of precision", as not all dropped events are logged - one event per type is preserved.

#### [](#interface-affecting)Interface Affecting

* [SCBC-331](https://issues.couchbase.com/browse/SCBC-331): Promoted Manager interfaces to committed.

#### [](#bugs-11)Bugs

* [SCBC-330](https://issues.couchbase.com/browse/SCBC-330): Ensured that JsonObjectSafe is recursive.
* [JVMCBC-1017](https://issues.couchbase.com/browse/JVMCBC-1017): Fixed issue with Threshold Logging Tracing not working due to RequestContext not being set.
* [JVMCBC-1020](https://issues.couchbase.com/browse/JVMCBC-1020): Added `target` property to QueryRequest and ensured it is honored for prepare and execute, so they are both run on the same node. This fix removes need for `TargetedQueryRequest`.

### [](#version-1-2-1-1-september-2021)Version 1.2.1 (1 September 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.2.1/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.2.1**
* com.couchbase.client:**core-io:2.2.1**
* io.projectreactor:**reactor-core:3.4.9**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-47)Improvements

* [SCBC-328](https://issues.couchbase.com/browse/SCBC-328): Update collections compat dependency.
* [SCBC-325](https://issues.couchbase.com/browse/SCBC-325): Add serialization support for Apache Spark.
* [SCBC-329](https://issues.couchbase.com/browse/SCBC-329): Expose all builder methods on SecurityConfig.
* [JVMCBC-1010](https://issues.couchbase.com/browse/JVMCBC-1010): Maintenance dependency bump.
* [JVMCBC-990](https://issues.couchbase.com/browse/JVMCBC-990): WaitUntilReady timing out with 6.0.x and unhealthy seed nodes.
* [JVMCBC-999](https://issues.couchbase.com/browse/JVMCBC-999): Properly map server query timeout while streaming.
* [JVMCBC-1004](https://issues.couchbase.com/browse/JVMCBC-1004): Configure and apply default log level for ConsoleLogger.
* [JVMCBC-1005](https://issues.couchbase.com/browse/JVMCBC-1005): Allow to export Context as Map.
* [JVMCBC-1006](https://issues.couchbase.com/browse/JVMCBC-1006): ErrorContext must be included in message.

#### [](#bug-fixes-20)Bug fixes

* [JVMCBC-1002](https://issues.couchbase.com/browse/JVMCBC-1002): Default log level reverted to INFO.
* [JVMCBC-1007](https://issues.couchbase.com/browse/JVMCBC-1007): LoggingMeter incorrectly marked as Volatile in SDK 3.2.

### [](#version-1-2-0-20-july-2021)Version 1.2.0 (20 July 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.2.0/com/couchbase/client/scala/index.html)

Version 1.2.0 is the first GA release of the 1.2 series, promoting to GA support for the scopes and collections provided by Couchbase Server 7.0, and also OpenTelemetry. In addition, a supported release for Scala 2.13 is now provided.

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.2.0**
* com.couchbase.client:**core-io:2.2.0**
* io.projectreactor:**reactor-core:3.4.6**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvement)Improvement

* [SCBC-217](https://issues.couchbase.com/browse/SCBC-217): Provide a published and officially supported Scala 2.13 build.
* [SCBC-231](https://issues.couchbase.com/browse/SCBC-231): Update analytics management API to support compound dataverse names.
* [SCBC-232](https://issues.couchbase.com/browse/SCBC-232): Manage remote analytics links.
* [SCBC-240](https://issues.couchbase.com/browse/SCBC-240): Add analytics support for collections.
* [SCBC-309](https://issues.couchbase.com/browse/SCBC-309): Map Query Error 13014 to AuthenticationException.
* [SCBC-205](https://issues.couchbase.com/browse/SCBC-205): Provide a Scala version of the Travel Sample Application backend.
* [JVMCBC-980](https://issues.couchbase.com/browse/JVMCBC-980): Add exception wrappers to Tracers and Meters.
* [JVMCBC-987](https://issues.couchbase.com/browse/JVMCBC-987): Allow supplying an SDK2-compatible memcached hashing strategy.
* [JVMCBC-988](https://issues.couchbase.com/browse/JVMCBC-988): Map Query Error 13014 to AuthenticationException.
* [JVMCBC-989](https://issues.couchbase.com/browse/JVMCBC-989): Add timeout\_ms to threshold logging tracer output.
* [JVMCBC-991](https://issues.couchbase.com/browse/JVMCBC-991): Optimize metric dispatching.
* [JVMCBC-992](https://issues.couchbase.com/browse/JVMCBC-992): Cache NodeIdentifier in NodeInfo.
* [JVMCBC-993](https://issues.couchbase.com/browse/JVMCBC-993): Optimize early discard of events which are not going to be logged.
* [JVMCBC-996](https://issues.couchbase.com/browse/JVMCBC-996): Throw FeatureNotAvailableException if scope level queries are not available.
* [JVMCBC-997](https://issues.couchbase.com/browse/JVMCBC-997): Duplicate attributes from dispatch\_to\_server to improve tracing.
* [JVMCBC-998](https://issues.couchbase.com/browse/JVMCBC-998): Performance: Do not set tracing spans if not needed.
* [JVMCBC-981](https://issues.couchbase.com/browse/JVMCBC-981): Support CoreHttpClient requests to manager service.
* [JVMCBC-984](https://issues.couchbase.com/browse/JVMCBC-984): Dependency bump: Netty 4.1.63 to 4.1.65, micrometer 1.6.6 to 1.7.0.
* [JCBC-1242](https://issues.couchbase.com/browse/JCBC-1242), [JCBC-1837](https://issues.couchbase.com/browse/JCBC-1837): Add OSGi bundle.
* [JCBC-1787](https://issues.couchbase.com/browse/JCBC-1787): Validate expiry instants.
* [JCBC-1838](https://issues.couchbase.com/browse/JCBC-1838): Add support for SDK2-compatible LegacyTranscoder.
* [JCBC-1841](https://issues.couchbase.com/browse/JCBC-1841): Update OpenTelemetry to 1.3.0.

#### [](#interface-changes)Interface Changes

All interface changes are to interfaces that are currently in beta and marked @Stability.Volatile or @Stability.Uncommitted.

* [JVMCBC-978](https://issues.couchbase.com/browse/JVMCBC-978): Rename AggregatingMeter to LoggingMeter.
* [JVMCBC-934](https://issues.couchbase.com/browse/JVMCBC-934): Threshold and Orphan output is now in new format.
* [JVMCBC-979](https://issues.couchbase.com/browse/JVMCBC-979): Rename ThresholdRequestTracer to ThresholdLoggingTracer
* [SCBC-297](https://issues.couchbase.com/browse/SCBC-297): Promote collection APIs from Volatile to Committed.

#### [](#bug-fixes-21)Bug Fixes

* [SCBC-270](https://issues.couchbase.com/browse/SCBC-270): Add redundant error handling for collection manager errors.
* [SCBC-296](https://issues.couchbase.com/browse/SCBC-296): JsonArraySafe should create an object wrapping a JsonObject.
* [JVMCBC-949](https://issues.couchbase.com/browse/JVMCBC-949): Opening a non-default collection on an memcached bucket now fails fast.
* [JVMCBC-983](https://issues.couchbase.com/browse/JVMCBC-983): Ignore slow subscribers on certain Flux intervals.

## [](#scala-sdk-1-1-releases)Scala SDK 1.1 Releases

Version 1.1 of the Scala SDK implements the 3.1 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-1-8-1-march-2022)Version 1.1.8 (1 March 2022)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.8/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.8**
* com.couchbase.client:**core-io:2.1.8**
* io.projectreactor:**reactor-core:3.4.15**
* org.reactivestreams:**reactive-streams:1.0.3**

### [](#bug-fixes-22)Bug Fixes

* [JVMCBC-1067](https://issues.couchbase.com/browse/JVMCBC-1067): Internal and external maintenance dependencies are updated to their latest available bugfix releases (including Netty to 4.1.74.Final).
* [JVMCBC-1046](https://issues.couchbase.com/browse/JVMCBC-1046): Added fix to not load the global config if a node is not in the seed node list anymore.
* [JVMCBC-1006](https://issues.couchbase.com/browse/JVMCBC-1006): `ErrorContext` is now included in the message of a `CouchbaseException`.

### [](#version-1-1-7-11-august-2021)Version 1.1.7 (11 August 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.7/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.7**
* com.couchbase.client:**core-io:2.1.7**
* io.projectreactor:**reactor-core:3.4.6**
* org.reactivestreams:**reactive-streams:1.0.3**

### [](#bug-fixes-23)Bug Fixes

* [JVMCBC-949](https://issues.couchbase.com/browse/JVMCBC-949): Opening a non-default collection on an memcached bucket now fails fast.
* [JVMCBC-983](https://issues.couchbase.com/browse/JVMCBC-983): Slow subscribers are now ignored on certain Flux intervals.
* [JVMCBC-990](https://issues.couchbase.com/browse/JVMCBC-990): The SDK now gracefully handles cluster-level WaitUntilReady against clusters < 6.5.
* [SCBC-296](https://issues.couchbase.com/browse/SCBC-296): Fixes a `JsonArraySafe` bug.

#### [](#improvements-48)Improvements

* [JVMCBC-996](https://issues.couchbase.com/browse/JVMCBC-996): Throw `FeatureNotAvailableException` if scope level queries are not available.
* [JVMCBC-988](https://issues.couchbase.com/browse/JVMCBC-988): Query error code 13014 is now mapped to `AuthenticationException`.
* [JVMCBC-987](https://issues.couchbase.com/browse/JVMCBC-987): Allow supplying an SDK2-compatible memcached hashing strategy.
* [JVMCBC-999](https://issues.couchbase.com/browse/JVMCBC-999): Properly map server query timeout while streaming.

### [](#improvements-49)Improvements

### [](#version-1-1-6-4-june-2021)Version 1.1.6 (4 June 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.6/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.6**
* com.couchbase.client:**core-io:2.1.6**
* io.projectreactor:**reactor-core:3.4.6**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-24)Bug Fixes

* [JVMCBC-972](https://issues.couchbase.com/browse/JVMCBC-972): Only open one GCCCP connection per node.

#### [](#improvements-50)Improvements

* [SCBC-237](https://issues.couchbase.com/browse/SCBC-237): Added `ThresholdRequestTracerConfig` and support for it in `ClusterEnvironment`.
* [SCBC-286](https://issues.couchbase.com/browse/SCBC-286): Added `AggregatingMeterConfig`, and allow the core `meter` property to be customized via `ClusterEnvironment`.
* [JVMCBC-939](https://issues.couchbase.com/browse/JVMCBC-939): Improve no collection access handling.
* [JVMCBC-974](https://issues.couchbase.com/browse/JVMCBC-974): Restructure AggregatingMeter output format.
* [JVMCBC-975](https://issues.couchbase.com/browse/JVMCBC-975): Further improve wait until ready diagnostics.
* [JVMCBC-977](https://issues.couchbase.com/browse/JVMCBC-977): Improve bucket configuration handling (revEpoch).

### [](#version-1-1-5-6-may-2021)Version 1.1.5 (6 May 2021)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.5/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.5**
* com.couchbase.client:**core-io:2.1.5**
* io.projectreactor:**reactor-core:3.4.5**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-51)Improvements

* [SCBC-266](https://issues.couchbase.com/browse/SCBC-266): Add FTS support for collections.
* [SCBC-281](https://issues.couchbase.com/browse/SCBC-281): Add Support to Preserve TTL.

### [](#version-1-1-4-7-april-2021)Version 1.1.4 (7 April 2021)

While there are no changes specific to the Scala SDK in this release, it does inherit fixes from the underlying core-io release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.4/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.4**
* com.couchbase.client:**core-io:2.1.4**
* io.projectreactor:**reactor-core:3.4.4**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-25)Bug Fixes

* [JCBC-1798](https://issues.couchbase.com/browse/JCBC-1798): Fixes ViewResult.metaData() throwing Exception when debug=true.

#### [](#improvements-52)Improvements

* [JCBC-1786](https://issues.couchbase.com/browse/JCBC-1786): Transcoders now allow contentAs(Object.class). Java Map and List collections are used to represent JSON objects and arrays.
* [JCBC-1795](https://issues.couchbase.com/browse/JCBC-1795): Allow `MutateInSpec.remove("")`, which removes the entire document.

### [](#version-1-1-3-2-march-2021)Version 1.1.3 (2 March 2021)

Version 1.1.3 is the fourth release of the 1.1 series, bringing stabilizations and enhancements over 1.1.2.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.3/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.3**
* com.couchbase.client:**core-io:2.1.3**
* io.projectreactor:**reactor-core:3.4.3**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#improvements-53)Improvements

* [SCBC-285](https://issues.couchbase.com/browse/SCBC-285): Expose property loading on environment.
* [JVMCBC-924](https://issues.couchbase.com/browse/JVMCBC-924), [JVMCBC-925](https://issues.couchbase.com/browse/JVMCBC-925): Updated dependencies: Netty to 4.1.59, netty-tcnative-boringssl-static to 2.0.36, Reactor to 2.4.3, Jackson to 2.12.1.
* [JVMCBC-919](https://issues.couchbase.com/browse/JVMCBC-919): Support for Project Reactor BlockHound integration.
* [JVMCBC-926](https://issues.couchbase.com/browse/JVMCBC-926): Performance: Replace new byte\[\] full copies with ByteBufUtil.getBytes.
* [JVMCBC-927](https://issues.couchbase.com/browse/JVMCBC-927): Performance: Improve performance of metrics hot code path.

#### [](#bugs-12)Bugs

* [JVMCBC-930](https://issues.couchbase.com/browse/JVMCBC-930): Threshold and Orphan Reporting now report the correct time units.
* [JVMCBC-932](https://issues.couchbase.com/browse/JVMCBC-932): Fixed a memory leak when OrphanReporter is disabled.
* [JVMCBC-933](https://issues.couchbase.com/browse/JVMCBC-933): ThresholdRequestTracer and OrphanReporter now use bounded queues.

#### [](#internal-improvements)Internal Improvements

* [JVMCBC-912](https://issues.couchbase.com/browse/JVMCBC-912): Refactor property loading.
* [JVMCBC-918](https://issues.couchbase.com/browse/JVMCBC-918): Move ProjectionsApplier into core.
* [JVMCBC-920](https://issues.couchbase.com/browse/JVMCBC-920): Move MutationState logic to core.
* [JVMCBC-921](https://issues.couchbase.com/browse/JVMCBC-921): Add OpenTelemetry attributes for spans.
* [JVMCBC-929](https://issues.couchbase.com/browse/JVMCBC-929): Retain stability annotations at runtime.
* [SCBC-284](https://issues.couchbase.com/browse/SCBC-284): Expose package-level APIs for Spark interop.

### [](#version-1-1-2-2-february-2020)Version 1.1.2 (2 February 2020)

Version 1.1.2 is the third release of the 1.1 series, bringing stabilizations and enhancements over 1.1.1.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.2/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.2**
* com.couchbase.client:**core-io:2.1.2**
* io.projectreactor:**reactor-core:3.4.1**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bugs-13)Bugs

* [SCBC-282](https://issues.couchbase.com/browse/SCBC-282): Collection map is no longer refreshed when using the default scope and default collection.

#### [](#api-affecting)API Affecting

* [SCBC-288](https://issues.couchbase.com/browse/SCBC-288): CollectionManager::getScope is now deprecated, in favour of using getAllScopes.

#### [](#enhancements)Enhancements

* [JVMCBC-915](https://issues.couchbase.com/browse/JVMCBC-915): As a performance optimization, loading a collection now only fetches the information required for that collection, rather than the full collection manifest.
* [JVMCBC-916](https://issues.couchbase.com/browse/JVMCBC-916): Any send HTTP request will send a hostname if hostnames are used, rather than IP, leading to consistent hostname use across the system.

### [](#version-1-1-1-12-january-2020)Version 1.1.1 (12 January 2020)

Version 1.1.1 is the second release of the 1.1 series, bringing stabilizations and enhancements over 1.1.

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.1/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.1**
* com.couchbase.client:**core-io:2.1.1**
* io.projectreactor:**reactor-core:3.4.1**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bugs-14)Bugs

* [JVMCBC-909](https://issues.couchbase.com/browse/JVMCBC-909): Retry opening the bucket until timeout when it is not found, to allow for it not yet being created.
* [JVMCBC-910](https://issues.couchbase.com/browse/JVMCBC-910): WaitUntilReady will now wait if bucket not present yet, before it starts to time out.
* [SCBC-274](https://issues.couchbase.com/browse/SCBC-274): Prepared non-adhoc queries on scopes were failing, as query\_context was not being passed to the individual prepare and/or execute statements. This has now been fixed, and scope-level queries are working as expected.

#### [](#enhancements-2)Enhancements

* [SCBC-273](https://issues.couchbase.com/browse/SCBC-273): Exposed partition information from the query management API on `QueryIndex` class.
* [SCBC-275](https://issues.couchbase.com/browse/SCBC-275): Escape the scope for scope-level queries now enabled, as a fix in the server means that this works.

### [](#version-1-1-0-2-december-2020)Version 1.1.0 (2 December 2020)

Version 1.1.0 is the first GA release of the 1.1 series, bringing stabilizations and enhancements over 1.0.10 and the 1.0 SDK, and adding features to support Couchbase Server 6.6 and 7.0β.

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-scala-client-1.1.0/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.1.0**
* com.couchbase.client:**core-io:2.1.0**
* io.projectreactor:**reactor-core:3.4.0**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-3)Enhancements

* [SCBC-241](https://issues.couchbase.com/browse/SCBC-241): Refactored Document Expiry Duration.
* [SCBC-253](https://issues.couchbase.com/browse/SCBC-253): Added disableScoring parameter for Search.
* [SCBC-229](https://issues.couchbase.com/browse/SCBC-229): The minimum durability level can now be configured on the `BucketManager`.

### [](#version-1-0-10-3-november-2020)Version 1.0.10 (3 November 2020)

Version 1.0.10 is a maintenance release, bringing enhancements over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.10/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.10**
* com.couchbase.client:**core-io:2.0.11**
* io.projectreactor:**reactor-core:3.3.9.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-4)Enhancements

* [JVMCBC-898](https://issues.couchbase.com/browse/JVMCBC-898): Added fallback for lastDispatchedTo in context, to improve debuggability.
* [JVMCBC-899](https://issues.couchbase.com/browse/JVMCBC-899): Updated OpenTelemetry to 0.9.1.
* [SCBC-252](https://issues.couchbase.com/browse/SCBC-252): Enhanced user management for collections/RBAC, to support future 7.0 release.

## [](#scala-sdk-1-0-releases)Scala SDK 1.0 Releases

Version 1.0 of the Scala SDK implements the 3.0 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

### [](#version-1-0-9-7-october-2020)Version 1.0.9 (7 October 2020)

Version 1.0.9 is a maintenance release, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.9/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.9**
* com.couchbase.client:**core-io:2.0.10**
* io.projectreactor:**reactor-core:3.3.9.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-26)Bug Fixes

* [SCBC-254](https://issues.couchbase.com/browse/SCBC-254): Fixed a decode error (allocstall) on BucketSettings with certain long values sent from particular server versions by swapping out upickle for JsonObject decoding.
* [SCBC-257](https://issues.couchbase.com/browse/SCBC-257): Fixed FTS serialization issues.
* [JVMCBC-885](https://issues.couchbase.com/browse/JVMCBC-885): Allow overriding of `BestEffortRetryStrategy`.
* [JVMCBC-889](https://issues.couchbase.com/browse/JVMCBC-889): Make sure WaitUntilReady always times out.
* [JVMCBC-890](https://issues.couchbase.com/browse/JVMCBC-890): Enforce only negotiate PLAIN when using TLS with PasswordAuthenticator.
* [JVMCBC-892](https://issues.couchbase.com/browse/JVMCBC-892): Service pool idle time check now happen more often.
* [JVMCBC-894](https://issues.couchbase.com/browse/JVMCBC-894): BatchHelper: handle success case with no body gracefully.
* [JVMCBC-872](https://issues.couchbase.com/browse/JVMCBC-872): Subdoc 'no access' error code is now reported correctly. This helps users to identify and fix permissions errors for system XATTRs.

#### [](#enhancements-5)Enhancements

* [SCBC-233](https://issues.couchbase.com/browse/SCBC-233): Geopolygon search support.
* [SCBC-234](https://issues.couchbase.com/browse/SCBC-234): Added support for FTS hints (flex index).
* [SCBC-236](https://issues.couchbase.com/browse/SCBC-236): Added ephemeral bucket management support.
* [SCBC-238](https://issues.couchbase.com/browse/SCBC-238): Added N1QL support for collections, via new `Scope.query` method.
* [SCBC-249](https://issues.couchbase.com/browse/SCBC-249): Added GetResult.expiryTime(), which returns an Instant vs GetResult.expiry()'s Duration.
* [JVMCBC-888](https://issues.couchbase.com/browse/JVMCBC-888), [JVMCBC-893](https://issues.couchbase.com/browse/JVMCBC-893): Dependency bumps: Netty to 4.1.52.Final, OpenTelemetry to 0.8.
* [JVMCBC-886](https://issues.couchbase.com/browse/JVMCBC-886): Improved LDAP auth failure handling.
* [JVMCBC-896](https://issues.couchbase.com/browse/JVMCBC-896): Fast dispatch pooled requests.

### [](#version-1-0-8-1-september-2020)Version 1.0.8 (1 September 2020)

Version 1.0.8 is the ninth release of the Scala SDK, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.8/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.8**
* com.couchbase.client:**core-io:2.0.9**
* io.projectreactor:**reactor-core:3.3.9.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-27)Bug Fixes

* [JVMCBC-805](https://issues.couchbase.com/browse/JVMCBC-805): The client now handles bootstrapping against nodes much better which do not have the data service enabled (in an MDS setup).
* [JVMCBC-882](https://issues.couchbase.com/browse/JVMCBC-882): A bug has been fixed where when bootstrapping against a node with no data service enabled, the endpoint would not be cleaned up and would keep trying to reconnect.
* [JVMCBC-872](https://issues.couchbase.com/browse/JVMCBC-872): The client now more explicitly handles an error response code (`NO_ACCESS`) when a subdocument request is performed against a system xattr.
* [JVMCBC-873](https://issues.couchbase.com/browse/JVMCBC-873): Durability information is now properly unwrapped from an optional when exported and dumped (for example as part of an exception).
* [JVMCBC-880](https://issues.couchbase.com/browse/JVMCBC-880): The client now trackes multiple parallel bucket open attempts (against different buckets) in a better way, making sure that an internal state is only switched when all those bucket open attempts have completed (and not just the first one).
* [JVMCBC-878](https://issues.couchbase.com/browse/JVMCBC-878): `EndpointDiagnostics` had the local and remote hostnames mixed up, they now show up in the correct order.

#### [](#enhancements-6)Enhancements

* [JVMCBC-883](https://issues.couchbase.com/browse/JVMCBC-883): The client is now a little less verbose when performing a DNS SRV request and the underlying JDK operation times out.
* [JVMCBC-879](https://issues.couchbase.com/browse/JVMCBC-879): Updated internal and external dependencies to their latest maintenance releases.
* [JVMCBC-874](https://issues.couchbase.com/browse/JVMCBC-874): When dealing with unknown collections, the SDK now returns a more user friendly retry reason when it can (outdated manifest vs. collection not found).
* [JVMCBC-875](https://issues.couchbase.com/browse/JVMCBC-875): On the request timeout exception, the retry reasons are now accessible directly.

### [](#version-1-0-7-4-august-2020)Version 1.0.7 (4 August 2020)

Version 1.0.7 is the eighth release of the Scala SDK, bringing enhancements, and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.7/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.7**
* com.couchbase.client:**core-io:2.0.8**
* io.projectreactor:**reactor-core:3.3.8.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#bug-fixes-28)Bug Fixes

* [SCBC-247](https://issues.couchbase.com/browse/SCBC-247): Removed cas from `IncrementOptions` and `DecrementOptions`. CAS is not supported by the underlying protocol and should not have been exposed in these options.
* [JVMCBC-870](https://issues.couchbase.com/browse/JVMCBC-870): A bug in the chunk response parser prohibited responses meant that View reduce responses were never completed, and as a result timed out on the user side. The completion of view results with reduce enabled has now been fixed.

#### [](#enhancements-7)Enhancements

* [JVMCBC-867](https://issues.couchbase.com/browse/JVMCBC-867): Performance improvement: do not grab ByteBuf slice when extracting server response time.
* [JVMCBC-869](https://issues.couchbase.com/browse/JVMCBC-869): Maintenance dependency bump: Netty → 4.1.51, Jackson → 2.11.1, Reactor → 3.3.7, OpenTelemetry → 0.6.0, Reactor Scala Extensions → 0.7.1.

### [](#version-1-0-6-14-july-2020)Version 1.0.6 (14 July 2020)

Version 1.0.6 is the seventh release of the Scala SDK.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.6/com/couchbase/client/scala/index.html)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.6**
* com.couchbase.client:**core-io:2.0.7**
* io.projectreactor:**reactor-core:3.3.5.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-8)Enhancements

* [JVMCBC-865](https://issues.couchbase.com/browse/JVMCBC-865): Change the default idle timeout to 4.5s for http connections, to support performance improvements in query service.

#### [](#bug-fixes-29)Bug Fixes

* [SCBC-244](https://issues.couchbase.com/browse/SCBC-244): ViewQuery with keys does not work.
* [JVMCBC-849](https://issues.couchbase.com/browse/JVMCBC-849): Redundant global loading exceptions no longer propagated — now logged at `debug` level.
* [JVMCBC-856](https://issues.couchbase.com/browse/JVMCBC-856): A just-opened connection in pool no longer gets cleaned up prematurely .
* [JVMCBC-858](https://issues.couchbase.com/browse/JVMCBC-858): Channel writeAndFlush failures are no longer ignored.
* [JVMCBC-862](https://issues.couchbase.com/browse/JVMCBC-862): Race condition with node identifier change on bootstrap identified. New logic and some changes to the config provider code ensures that retry and resubscribe picks up fresh seed nodes.
* [JVMCBC-863](https://issues.couchbase.com/browse/JVMCBC-863): Bucket-Level ping report no longer includes other view and KV services buckets.
* [JVMCBC-866](https://issues.couchbase.com/browse/JVMCBC-866): Trailing : no longer added to IPv6 addresses without \[\]. 'invalid IPv6 address' warnings now no longer produced when trying to connect to a valid Ipv6 address thus specified.

### [](#version-1-0-5-2-june-2020)Version 1.0.5 (2 June 2020)

Version 1.0.5 is the sixth release of the Scala SDK. It brings no new changes to the Scala client itself, but inherits enhancements and bugfixes over the last stable release from the core-io dependency.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.5/com/couchbase/client/scala/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.5/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.5**
* com.couchbase.client:**core-io:2.0.6**
* io.projectreactor:**reactor-core:3.3.5.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-9)Enhancements

* [JVMCBC-852](http://issues.couchbase.com/browse/JVMCBC-852): Bumped Reactor to 3.3.5, Netty to 4.1.50.Final, and Jackson to 2.11.0.
* [JVMCBC-693](https://issues.couchbase.com/browse/JVMCBC-693): For performance, the KV bootstrap sequence is now partially pipelined.

#### [](#bug-fixes-30)Bug Fixes

* [JVMCBC-849](http://issues.couchbase.com/browse/JVMCBC-849): Duplicate global loading exceptions are now swallowed to remove redundant warnings from logging (this was a cosmetic-only issue).

### [](#version-1-0-4-7-may-2020)Version 1.0.4 (7 May 2020)

Version 1.0.4 is the fifth release of the Scala SDK. It brings no new changes to the Scala client itself, but inherits enhancements and bugfixes over the last stable release from the core-io dependency.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.4/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.5/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.4**
* com.couchbase.client:**core-io:2.0.5**
* io.projectreactor:**reactor-core:3.3.4.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.3**

#### [](#enhancements-10)Enhancements

* [JVMCBC-841](http://issues.couchbase.com/browse/JVMCBC-841): Bumped Netty dependency to 2.0.30, and reactor to 3.3.4.

#### [](#bug-fixes-31)Bug Fixes

* [JVMCBC-845](http://issues.couchbase.com/browse/JVMCBC-845): If a rebalance is stopped in the middle, an edge case occasionally causes KV ops to time out as the fast forward map is chosen over the retry. The behavior has now been changed so that the client will try the old and new servers to make sure the operation eventually gets dispatched to the right node.

### [](#version-1-0-3-7-april-2020)Version 1.0.3 (7 April 2020)

Version 1.0.3 is the fourth release of the Scala SDK. It brings no new changes to the Scala client itself, but inherits enhancements and bugfixes over the last stable release from the core-io dependency.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.3/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.4/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.3**
* com.couchbase.client:**core-io:2.0.4**
* io.projectreactor:**reactor-core:3.3.1.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.2**

#### [](#enhancements-11)Enhancements

* [JVMCBC-830](http://issues.couchbase.com/browse/JVMCBC-830): Added more convenient overloads for SecurityConfig and CertAuth. These overloads initialize both the SecurityConfig and the CertificateAuthenticator directly from a KeyStore or TrustStore.
* [JVMCBC-831](http://issues.couchbase.com/browse/JVMCBC-831): Improves timeout for waitUntilReady — the `waitUntilReady` helper should now throw a proper timeout exception.
* [JVMCBC-832](http://issues.couchbase.com/browse/JVMCBC-832): Added support for multiple ports per hostname in the connection string — without having to use the explicit SeedNode set overload.
* [JVMCBC-835](http://issues.couchbase.com/browse/JVMCBC-835): Using "localhost:8091" as a connection string would set the kv bootstrap port to 8091, which is not desired behavior. To prevent this from happening again, the code now checks for this condition, fails fast, and also provides guidance on what the connection string should look like instead.
* [JVMCBC-836](http://issues.couchbase.com/browse/JVMCBC-836): Enabled Unordered Execution by Default.
* [JVMCBC-837](http://issues.couchbase.com/browse/JVMCBC-837): Updates OpenTelemetry to 0.3 (beta).
* [JVMCBC-839](http://issues.couchbase.com/browse/JVMCBC-839): Bootstrap will now correctly use the mapped port if alternate addr is present.

#### [](#bug-fixes-32)Bug Fixes

* [JVMCBC-834](http://issues.couchbase.com/browse/JVMCBC-834): 'CollectionNotFoundException' now triggers a retry, and if no collection refresh is currently in progress it will proactively trigger a new one. Now Docs created under custom collection should no longer raise an exception when a collection has been created in the meantime, but the collection is not found as no refresh is in progress.
* [JVMCBC-826](http://issues.couchbase.com/browse/JVMCBC-826): A NullPointerException was occuring when LDAP is enabled. The code now explicitly fails the connection with a descriptive error message instructing the user what to do next (either use TLS which is preferred) or enable PLAIN on the password authenticator (insecure).
* [JVMCBC-827](http://issues.couchbase.com/browse/JVMCBC-827): Search query results row\_hit typo resulted in 0 being returned for total rows. This has now been fixed.
* [JVMCBC-828](http://issues.couchbase.com/browse/JVMCBC-828): Omit internal config request in orphan reporting.

### [](#version-1-0-2-3-march-2020)Version 1.0.2 (3 March 2020)

Version 1.0.2 is the third release of the Scala SDK, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client-1.0.2/scaladocs/com/couchbase/client/scala/index.html) | [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.0.3/)

The supported and tested dependencies for this release are:

* com.couchbase.client:**scala-client:1.0.2**
* com.couchbase.client:**core-io:2.0.3**
* io.projectreactor:**reactor-core:3.3.1.RELEASE**
* org.reactivestreams:**reactive-streams:1.0.2**

#### [](#enhancements-12)Enhancements

* [JVMCBC-813](http://issues.couchbase.com/browse/JVMCBC-813): Improved error message for bucket is missing.
* [JVMCBC-815](http://issues.couchbase.com/browse/JVMCBC-815): Check if key exceeds size limits.
* [JVMCBC-818](http://issues.couchbase.com/browse/JVMCBC-818): Trimmed netty stack in connect failures for more readable output.
* [JVMCBC-819](http://issues.couchbase.com/browse/JVMCBC-819): Distinguished bucket not found in select bucket failures.
* [JVMCBC-823](http://issues.couchbase.com/browse/JVMCBC-823): Added a global component to the core id.
* [JVMCBC-825](http://issues.couchbase.com/browse/JVMCBC-825): Support added for new VATTR HELLO flag.
* [SCBC-43](http://issues.couchbase.com/browse/SCBC-43): With huge thanks to our community, who submitted the patch, it is now possible to build versions of the SDK for 2.11 and 2.13\. Couchbase only officially provides, tests and supports a Scala 2.12 build currently, but users are welcome to build their own jars for 2.11 or 2.13 following the [README instructions](https://github.com/couchbase/couchbase-jvm-clients).

#### [](#bug-fixes-33)Bug Fixes

* [SCBC-200](http://issues.couchbase.com/browse/SCBC-200): Dependencies now correctly shaded.
* [SCBC-207](http://issues.couchbase.com/browse/SCBC-207): Exists no longer returns wrong value if executed right after remove.
* [SCBC-216](http://issues.couchbase.com/browse/SCBC-216): Properly clear cache when repreparing/retrying query.
* [JVMCBC-824](http://issues.couchbase.com/browse/JVMCBC-824): Native Netty transports not included, resulting in fallback to default implementation. This was a regression in the 2.0.2 core-io release.
* [JCBC-1600](http://issues.couchbase.com/browse/JCBC-1600): Using expiry together with document flags on a Sub-Document `mutateIn` no longer causes an incorrect flags field to be sent.

### [](#version-1-0-1-5th-february-2020)Version 1.0.1 (5th February 2020)

Version 1.0.1 is the second release of the 1.0 series, bringing new features, enhancements, and bugfixes over the last stable release.

#### [](#stability-enhancements-bug-fixes)Stability Enhancements & Bug Fixes

* [SCBC-192](https://issues.couchbase.com/browse/SCBC-192): All scaladoc warnings fixed.
* [SCBC-193](https://issues.couchbase.com/browse/SCBC-193): When creating buckets, numReplicas can now be specified.

#### [](#new-features-enhancements)New Features & Enhancements

* [SCBC-190](https://issues.couchbase.com/browse/SCBC-190): Exposed enableDnsSrv parameter on `IoConfig()`, allowing DNS SRV to be used.
* [SCBC-204](https://issues.couchbase.com/browse/SCBC-204): Added support for new server flag `createAsDeleted` — for internal use only.
* [SCBC-201](https://issues.couchbase.com/browse/SCBC-201): Exposed Java core environment through Scala ClusterEnvironment, allowing the event-bus to be accessed.
* [SCBC-198](https://issues.couchbase.com/browse/SCBC-198): Exposed environment getter through cluster. This allows a constructed environment to be shutdown without having to maintain a reference to it.

### [](#version-1-0-0-17th-january-2020)Version 1.0.0 (17th January 2020)

This is the first General Availability (GA) release of the new Couchbase Scala SDK. It brings a large number of improvements, bug-fixes and API changes from the previous beta release.

#### [](#stability-enhancements-bug-fixes-2)Stability Enhancements & Bug Fixes

* [SCBC-147](https://issues.couchbase.com/browse/SCBC-147): QueryIndexManager should return only GSI indexes
* [SCBC-151](https://issues.couchbase.com/browse/SCBC-151): Make sure all reactive ops are deferred; this ensures that `collection.reactive.remove(…​)` won't perform a remove until the SMono is subscribed to
* [SCBC-154](https://issues.couchbase.com/browse/SCBC-154): Make UserManager handle pre-LDAP clusters
* [SCBC-157](https://issues.couchbase.com/browse/SCBC-157): Handle projections of objects inside arrays correctly
* [SCBC-158](https://issues.couchbase.com/browse/SCBC-158): Handle 'too many set inserts' internal error while converting JSON to case classes
* [SCBC-163](https://issues.couchbase.com/browse/SCBC-163): ViewQuery does not send request
* [SCBC-167](https://issues.couchbase.com/browse/SCBC-167): Fix FTS consistentWith
* [SCBC-174](https://issues.couchbase.com/browse/SCBC-174): ReactiveCollection KV operations now do ClientVerified Observe check
* [SCBC-182](https://issues.couchbase.com/browse/SCBC-182): QueryOptions missing setters

#### [](#new-features-enhancements-2)New Features & Enhancements

* [SCBC-190](https://issues.couchbase.com/browse/SCBC-190): Expose enableDnsSrv parameter on `IoConfig()`, allowing DNS SRV to be used
* [SCBC-192](https://issues.couchbase.com/browse/SCBC-192): All scaladoc warnings fixed
* [SCBC-204](https://issues.couchbase.com/browse/SCBC-204): Add support for new server flag `createAsDeleted`, for internal use only

#### [](#api-changes)API Changes

* [SCBC-159](https://issues.couchbase.com/browse/SCBC-159): Fix semantics of datastructures so they behave more like Scala collections
* [SCBC-162](https://issues.couchbase.com/browse/SCBC-162): All ReactiveBinaryCollection methods should return SMono
* [SCBC-164](https://issues.couchbase.com/browse/SCBC-164): Align with latest view RFC
* [SCBC-136](https://issues.couchbase.com/browse/SCBC-136): Track all Java environment changes
* [SCBC-138](https://issues.couchbase.com/browse/SCBC-138): Replace management API Scala exceptions with core ones
* [SCBC-139](https://issues.couchbase.com/browse/SCBC-139): GetSelecter is using incorrect exceptions
* [SCBC-155](https://issues.couchbase.com/browse/SCBC-155): Rename \*master to \*active throughout
* [SCBC-187](https://issues.couchbase.com/browse/SCBC-187): Remove scopeExists and collectionExists from CollectionManager
* [SCBC-188](https://issues.couchbase.com/browse/SCBC-188): Align UserAndMetadata with latest RFC