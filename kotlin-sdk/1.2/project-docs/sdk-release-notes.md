---
title: SDK Release Notes
description: Release notes for the Couchbase Kotlin Client.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/release/1.2/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:1.2@kotlin-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.2/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes for the Couchbase Kotlin Client. 

Unresolved directive in sdk-release-notes.adoc - include::{version-common}@sdk:pages:partial$signed.adoc\[tag=signed\]

(3.8.2 is the JVM core of Kotlin SDK 1.5.2.)

## [](#latest-release)Kotlin SDK 1.5 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#v1.5.3)Version 1.5.3 (11 July 2025)

Regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.5.3/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.3/)

#### [](#bug-fixes)Bug Fixes

* [JVMCBC-1654](https://couchbasecloud.atlassian.net/browse/JVMCBC-1654): FIxed a bug that prevented `Collection.getAnyReplica()`, `getAllReplicas()`, `lookupInAnyReplica()`, `lookupInAllReplicas()`, `scan()`, `[Reactive]BatchHelper.exists()`, and `getIfExists()` from timing out if the bucket does not exist or is not accessible.

### [](#v1.5.2)Version 1.5.2 (4 June 2025)

Regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.5.2/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.2/)

#### [](#improvements)Improvements

* [JVMCBC-1647](https://couchbasecloud.atlassian.net/browse/JVMCBC-1647): Upgraded `Jackson` from `2.17.2` to `2.17.3`.

### [](#v1.5.1)Version 1.5.1 (9 May 2025)

Regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.5.1/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.1/)

#### [](#improvements-2)Improvements

* [JVMCBC-1631](https://couchbasecloud.atlassian.net/browse/JVMCBC-1631): Updated `Netty` to `4.1.119`.

### [](#v1.5.0)Version 1.5.0 (9 April 2025)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.5.0/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.8.0/)

#### [](#new-features)New Features

* [KCBC-190](https://jira.issues.couchbase.com/browse/KCBC-190): New APIs added to allow getting KV documents from a preferred server group. This feature allows the implementation of network optimization when traffic cost between server groups is higher than in the local group. In this case the application might select preferred server group in the connection options, and later opt-in for local operations during replica reads.
* [KCBC-189](https://jira.issues.couchbase.com/browse/KCBC-189): `KotlinxSerializationJsonSerializer` is now part of the SDK's stable API, with full support for nullable types and contextual serializers.  
> [!WARNING]  
> The stable version of this class is not binary compatible with the experimental version. If you were already using `KotlinxSerializationJsonSerializer`, you will need to recompile your project.
* [JVMCBC-1602](https://couchbasecloud.atlassian.net/browse/JVMCBC-1602:): Application Telemetry improvements.

#### [](#improvements-3)Improvements

* [KCBC-187](https://jira.issues.couchbase.com/browse/KCBC-187): The bucket management API now supports specifying the number of VBuckets for a Magma bucket (requires Couchbase Server 8.0 or later).
* [KCBC-184](https://jira.issues.couchbase.com/browse/KCBC-184): Added transaction methods `getMulti` and `getMultiReplicasFromPreferredServerGroup` for getting a batch of documents with minimal read skew.

## [](#kotlin-sdk-1-4-releases)Kotlin SDK 1.4 Releases

### [](#v1.4.9)Version 1.4.9 (11 March 2025)

Regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.9/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.9/)

#### [](#improvements-4)Improvements

* [JVMCBC-1616](https://couchbasecloud.atlassian.net/browse/JVMCBC-1616)Upgraded Netty from `4.1.15` to `4.1.118`.

### [](#v1.4.8)Version 1.4.8 (11 February 2025)

Regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.8/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.8/)

#### [](#improvements-5)Improvements

* [KCBC-163](https://jira.issues.couchbase.com/browse/KCBC-163): When using Couchbase Server 7.6.2 or later, you can now specify a "preferred server group" for replica reads. To use this feature, configure the cluster environment with a `preferredServerGroup` name. The following `Collection` methods now have an optional `readPreference` parameter:

  * `getAnyReplica`
  * `getAllReplicas`
  * `lookupInAnyReplica`
  * `lookupInAllReplicas`  
  When calling these methods, pass `readPreference = ReadPreference.preferredServerGroup()` to limit the results to replicas in the configured server group.  
  Example usage:  
  ```kotlin  
  val cluster = Cluster.connect(connectionString, username, password) {  
      preferredServerGroup = "Group 1"  
  }  
  val collection = cluster.bucket("myBucket").defaultCollection()  
  runBlocking {  
      val result = collection.getAnyReplica(  
          "myDocumentId",  
          readPreference = ReadPreference.preferredServerGroup()  
      )  
      println(result)  
  }  
  ```
* [KCBC-178](https://jira.issues.couchbase.com/browse/KCBC-178): `CouchbaseHttpClient` can now send `PATCH` requests.
* [KCBC-180](https://jira.issues.couchbase.com/browse/KCBC-180): The experimental `KotlinxSerializationJsonSerilaizer` can now serialize and deserialize documents, query parameters, and query result rows that have a JSON null at the root.
* [KCBC-179](https://jira.issues.couchbase.com/browse/KCBC-179): Deprecated the existing methods for specifying SQL++ query parameters, and added new methods that preserve parameter type information required by some `JsonSerializer` implementations. This will be increasingly important as we add better support for `kotlinx.serialization` in the future.  
Prior to this change, using the experimental `KotlinxSerializationJsonSerializer` as the serializer for a parameterized SQL++ query resulted in `kotlinx.serialization.SerializationException: Serializer for class 'Object' is not found.`  
Here are some examples of the old (deprecated) and new way of specifying query parameters:

**Named parameters**  
```kotlin  
// DEPRECATED  
parameters = QueryParameters.named(  
    "name" to "Fido",  
    "data" to MyDataClass(),  
)  
// REPLACEMENT  
parameters = QueryParameters.named {  
    param("name", "Fido")  
    param("data", MyDataClass())  
}  
```

**Positional parameters**  
```kotlin  
// DEPRECATED  
parameters = QueryParameters.positional(  
    listOf(  
        "Fido",  
        MyDataClass(),  
    )  
)  
// REPLACEMENT  
parameters = QueryParameters.positional {  
    param("Fido")  
    param(MyDataClass())  
}  
```

### [](#v1.4.7)Version 1.4.7 (08 January 2025)

Regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.7/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.7/)

#### [](#bug-fixes-2)Bug Fixes

* [JVMCBC-1592](https://jira.issues.couchbase.com/browse/JVMCBC-1592): When fetching fresh cluster topology information for a bucket, the SDK now dispatches the request to a random eligible node instead of using a round-robin algorithm. Randomizing the node selection avoids a pathological condition where if the number of open buckets is equal to the number of nodes, and one of the nodes is degraded, the config refresh attempt for a particular bucket would fail repeatedly because it was always sent to the degraded node.

### [](#v1.4.6)Version 1.4.6 (04 December 2024)

This regular maintenance release updates dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.6/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.6/)

#### [](#bug-fixes-3)Bug Fixes

* [JVMCBC-1583](https://jira.issues.couchbase.com/browse/JVMCBC-1583): Fixed a race condition that could cause the SDK to continuously attempt to reconnect to a node, even after the node is rebalanced out of the cluster.

#### [](#improvements-6)Improvements

* [JVMCBC-1560](https://jira.issues.couchbase.com/browse/JVMCBC-1560): Added cluster UUID and name to metrics and spans.
* [JVMCBC-1582](https://jira.issues.couchbase.com/browse/JVMCBC-1582): Upgraded `Netty` from `4.1.112` to `4.1.115`.

### [](#v1.4.5)Version 1.4.5 (06 November 2024)

This regular maintenance release updates dependency versions, and picks up bug fixes from the Couchbase `core-io` library.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.5/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.5/)

#### [](#bug-fixes-4)Bug Fixes

* [JVMCBC-1572](https://jira.issues.couchbase.com/browse/JVMCBC-1572): Due to a regression in Kotlin SDK `1.4.1`, using a secure connection would cause `waitUntilReady()` to not wait, and would cause `ping()` to report failures even when nothing was wrong. The issue that caused these problems is now fixed.
* [JVMCBC-1577](https://jira.issues.couchbase.com/browse/JVMCBC-1577): Due to a regression in Kotlin SDK `1.4.1`, sometimes a request made shortly after calling `Cluster.connect()` would fail with a message that said the service is not available in the cluster, even if the service was actually available. This no longer happens.
* [JVMCBC-1579](https://jira.issues.couchbase.com/browse/JVMCBC-1579): Deprecated `com.couchbase.client.core.node.NodeIdentifier` in favor of `com.couchbase.client.core.topology.NodeIdentifier`.

### [](#v1.4.4)Version 1.4.4 (08 October 2024)

This regular maintenance release adds an experimental API for Couchbase transactions, and updates dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.4/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.4/)

#### [](#bug-fixes-5)Bug Fixes

* [JVMCBC-1570](https://jira.issues.couchbase.com/browse/JVMCBC-1570): The SDK was producing an incorrect partition map in `CouchbaseBucketConfig`, for buckets with >= 2 replicas. This has now been fixed.

#### [](#improvements-7)Improvements

* [KCBC-96](https://jira.issues.couchbase.com/browse/KCBC-96): Added experimental API for Couchbase transactions. This is a new [Kotlin-flavored candy shell](https://www.couchbase.com/forums/t/kotlin-sdk-1-4-4-adds-experimental-support-for-couchbase-transactions/39307) on the same Couchbase transactions engine used by the Java SDK.  
> [!WARNING]  
> The Kotlin transactions API is still "volatile", meaning it could change without notice as we refine it based on your feedback.

### [](#v1.4.3)Version 1.4.3 (23 September 2024)

This regular maintenance release updates dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.3/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.3/)

#### [](#improvements-8)Improvements

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

### [](#v1.4.2)Version 1.4.2 (13 August 2024)

This regular maintenance release updates dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.2/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-3.7.2/)

#### [](#improvements-9)Improvements

* [JVMCBC-1547](https://issues.couchbase.com/browse/JVMCBC-1547): Updated DnsJava to 3.6.0.

### [](#v1.4.1)Version 1.4.1 (23 July 2024)

This regular maintenance release updates dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.1/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.7.1/)

#### [](#improvements-10)Improvements

* [JVMCBC-1523](https://issues.couchbase.com/browse/JVMCBC-1523): Upgraded `org.iq80.snappy` from 0.4 to 0.5.
* [JVMCBC-1532](https://issues.couchbase.com/browse/JVMCBC-1532): Upgraded Jackson from 2.17.0 to 2.17.2.
* [JVMCBC-1544](https://issues.couchbase.com/browse/JVMCBC-1544): `SearchIndexManager.upsertIndex()` now prevents vector indexes from being created on server versions before version 7.6.0, which do not support these index types.

### [](#v1.4.0)Version 1.4.0 (15 June 2024)

This version promotes vector search to the committed API, and adds support for specifying a vector as a Base64-encoded sequence of little-endian IEEE 754 floats.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.0/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.7.0/)

#### [](#improvements-11)Improvements

* [KCBC-165](https://issues.couchbase.com/browse/KCBC-165): Adds support for base64-encoded vectors in `VectorQuery`.

## [](#kotlin-sdk-1-3-releases)Kotlin SDK 1.3 Releases

### [](#v1.3.2)Version 1.3.2 (29 April 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.3.2/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.2/)

#### [](#improvements-12)Improvements

* [JVMCBC-1508](https://issues.couchbase.com/browse/JVMCBC-1508)Upgraded Netty dependency.
* [JVMCBC-1509](https://issues.couchbase.com/browse/JVMCBC-1509)Upgraded Jackson dependency.

#### [](#bugfixes)Bugfixes

* [JVMCBC-1506](https://issues.couchbase.com/browse/JVMCBC-1506)Reduced the rate at which messages appear in the server's `http_access.log` when a user provides valid credentials but does not have permission to access the bucket.
* [JVMCBC-1512](https://issues.couchbase.com/browse/JVMCBC-1512)Correctly adapt to server cluster topology changes when a service migrates from one port to another on the same host.

### [](#v1.3.1)Version 1.3.1 (5 April 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.3.1/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.1/)

#### [](#improvements-13)Improvements

* [JVMCBC-1477](https://issues.couchbase.com/browse/JVMCBC-1477)Reduced the rate at which messages appear in the server's `http_access.log` when invalid credentials are provided resulting in 401 errors. Issues resulting in 403 errors will be handled in a future release.
* [JVMCBC-1499](https://issues.couchbase.com/browse/JVMCBC-1499)Disabled DNS SRV caching. The SDK now responds quicker to DNS changes in dynamic environments like Kubernetes.

### [](#v1.3.0)Version 1.3.0 (11 March 2024)

This version adds support for new features in Couchbase Server 7.6: vector search, KV range scan, and sub-document read from replica.

Additionally, several methods that were previously "volatile" or "uncommitted" are now part of the SDK's "committed" (stable) public API.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.3.0/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.6.0/)

#### [](#improvements-14)Improvements

* [KCBC-145](https://issues.couchbase.com/browse/KCBC-145): Added support for vector search, a new feature in Couchbase Server 7.6\. This API is currently at `@Stability.Uncommitted` level.
* [JVMCBC-1491](https://issues.couchbase.com/browse/JVMCBC-1491): Added support for KV range scan, a new feature in Couchbase Server 7.6\. The `Collection.scanDocuments()` and `Collection.scanIds()` methods are now part of the SDK's committed public API.
* [JVMCBC-1493](https://issues.couchbase.com/browse/JVMCBC-1493): Added support for Sub-Document read from replica, a new feature in Couchbase Server 7.6\. The `Collection.lookupInAnyReplica()` and `Collection.lookupInAllReplicas()` methods are now part of the SDK's committed public API.
* [KCBC-147](https://issues.couchbase.com/browse/KCBC-147): `Scope.searchIndexes()` is now part of the committed public API.
* [KCBC-157](https://issues.couchbase.com/browse/KCBC-157): `UserManager.changePassword()` is now part of the committed public API.
* [KCBC-158](https://issues.couchbase.com/browse/KCBC-158): `SearchIndexManager` is now part of the committed public API.
* [JVMCBC-1487](https://issues.couchbase.com/browse/JVMCBC-1487): Upgraded reactor-core from 3.5.8 to 3.6.3.
* [JVMCBC-1488](https://issues.couchbase.com/browse/JVMCBC-1488): Upgraded Jackson from 2.16.0 to 2.16.1.
* [JVMCBC-1489](https://issues.couchbase.com/browse/JVMCBC-1489): Upgraded Netty from 4.1.101 to 4.1.107.

#### [](#bugfixes-2)Bugfixes

* [JVMCBC-1480](https://issues.couchbase.com/browse/JVMCBC-1480): `couchbase2:` should do exponential backoff when `BestEffortRetryStrategy` is used.
* [JVMCBC-1494](https://issues.couchbase.com/browse/JVMCBC-1494): If you specify `min=1` for a Full-Text Search disjunction query, the SDK now always sends the value to the server. Previously, the SDK assumed `1` was the default value, and omitted the parameter in that case.

## [](#kotlin-sdk-1-2-releases)Kotlin SDK 1.2 Releases

### [](#v1.2.3)Version 1.2.3 (6 February 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.2.3/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.3/)

#### [](#improvements-15)Improvements

* [KCBC-146](https://issues.couchbase.com/browse/KCBC-146) Collection manager improvements:

  * Added a special max expiry duration, `CollectionSpec.NEVER_EXPIRE` (equal to -1 seconds), that can be used with Couchbase Server 7.6 and later to indicate documents in a collection should never expire, regardless of the bucket's max expiry.
  * Updated the API reference documentation to clarify that a collection max expiry of `0.seconds` (or null, depending on context) means the collection's actual max expiry is always the same as the bucket's max expiry.
* [JVMCBC-1460](https://issues.couchbase.com/browse/JVMCBC-1460) `couchbase2` now supports compressing data between the SDK and the server.
* [JVMCBC-1464](https://issues.couchbase.com/browse/JVMCBC-1464)The `metrics-opentelemetry` package is now aligned with the same `OpenTelemetry` version as `tracing-opentelemetry`.
* [JVMCBC-1468](https://issues.couchbase.com/browse/JVMCBC-1468) `Cluster.connect` now validates that connection strings using the `couchbase2` scheme have exactly one host. (Previously, hosts after the first were silently ignored.).
* [JVMCBC-1470](https://issues.couchbase.com/browse/JVMCBC-1470)Improved support for Full Text Search in `couchbase2` mode.
* [JVMCBC-1472](https://issues.couchbase.com/browse/JVMCBC-1472) `couchbase2` errors will now include diagnostic information when CNG is running with the `--debug` flag.

#### [](#bugfixes-3)Bugfixes

* [JVMCBC-1475](https://issues.couchbase.com/browse/JVMCBC-1475)Accessing the terms of a `TermFacet` result no longer throws `NullPointerException` if the target field is absent from all documents.

### [](#v1.2.2)Version 1.2.2 (5 January 2024)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.2.2/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.2/)

#### [](#improvements-16)Improvements

* [KCBC-141](https://issues.couchbase.com/browse/KCBC-141): Added new `QueryMetadata.signatureBytes` property. The value is a byte array containing the signature encoded as JSON (`QueryMetadata.signature` failed if the signature was not a JSON Object). Deprecated `QueryMetadata.signature` in favor of `signatureBytes`.

#### [](#bugfixes-4)Bugfixes

* [JVMCBC-1455](https://issues.couchbase.com/browse/JVMCBC-1455): Fixed compatibility with `couchbase2://` endpoints by upgrading internal GRPC dependency. All couchbase2 protocol users should upgrade to this release.
* [JVMCBC-1463](https://issues.couchbase.com/browse/JVMCBC-1463): Fixed compatibility between `couchbase2://` endpoints and the `tracing-opentelemetry` module.

### [](#v1.2.1)Version 1.2.1 (8 December 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.2.1/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.1/)

#### [](#improvements-17)Improvements

* [JVMCBC-1435](https://issues.couchbase.com/browse/JVMCBC-1435), [JVMCBC-1436](https://issues.couchbase.com/browse/JVMCBC-1436): Upgraded Netty and Jackson dependencies.
* [JVMCBC-1440](https://issues.couchbase.com/browse/JVMCBC-1440): Adding `DocumentNotLockedException` supporting future Couchbase Server versions that will return an error code when unlocking a document that is not locked.

#### [](#bugfixes-5)Bugfixes

* [JVMCBC-1433](https://issues.couchbase.com/browse/JVMCBC-1433): The SDK can now connect to Memcached buckets whose names contain the percent (`%`) character. (We'd like to take this opportunity to remind everyone that Memcached buckets are deprecated in favor of Ephemeral buckets.)
* [JVMCBC-1437](https://issues.couchbase.com/browse/JVMCBC-1437): With Couchbase Server versions that support updating a collection's max expiry, it's now possible to clear the expiry by passing `Duration.ZERO` for the new value.
* [JVMCBC-1441](https://issues.couchbase.com/browse/JVMCBC-1441): The SDK now handles an additional error case for `IndexNotFoundException`.
* [JVMCBC-1442](https://issues.couchbase.com/browse/JVMCBC-1442): Fixed a dependency issue with `tracing-opentelemetry` module.

### [](#v1.2.0)Version 1.2.0 (21 November 2023)

Version 1.2.0 is the first release of the 1.2 series.

The SDK now supports the new couchbase2 protocol, which is upcoming in future Couchbase Server versions. It can be enabled through using a connection string starting with `couchbase2://`. Please see [Cloud Native Gateway](../howtos/connecting.md#cloud-native-gateway) for more information.

The SDK now directly depends on SLF4J, which may impact some users — see below for details.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.2.0/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.5.0/)

#### [](#api-impacting)API Impacting

When upgrading from a previous version of the SDK, please be aware of this behavioral change:

> [!CAUTION]
> [JVMCBC-1319](https://issues.couchbase.com/browse/JVMCBC-1319): As [previously announced](https://www.couchbase.com/forums/t/embracing-slf4j-in-couchbase-java-sdk-3-5/36474), the SLF4J API is now a required dependency, and the SDK does all logging through SLF4J. The following client settings for customizing logging behavior are deprecated, and no longer have any effect:
> 
> * `logger.disableSlf4J`
> * `logger.fallbackToConsole`
> * `logger.consoleLoggerFormatter`
> 
> If your project does not already use SLF4J, please follow the announcement link for details and a mini-migration guide.

#### [](#improvements-18)Improvements

* [KCBC-132](https://issues.couchbase.com/browse/KCBC-132): `BucketManager` and `CollectionManager` now know about the history preservation settings added in Couchbase Server 7.2.  
`CollectionManager` has a new `updateCollection` method for changing the settings of an existing collection. Note that updating a collection's `maxExpiry` setting requires Couchbase Server 7.6.
* [JVMCBC-1402](https://issues.couchbase.com/browse/JVMCBC-1402), [JVMCBC-1410](https://issues.couchbase.com/browse/JVMCBC-1410): Upgraded Netty from 4.1.96 to 4.1.100, and upgraded `OpenTelemetry` dependency.
* [JVMCBC-1430](https://issues.couchbase.com/browse/JVMCBC-1430): Optimization: removed creation of unnecessary metrics labels when default `LoggingMeter` is used.
* [JVMCBC-1391](https://issues.couchbase.com/browse/JVMCBC-1391): The Bucket Manager API is now forward-compatible with future versions of Couchbase Server that might support storage engine types other than "magma" and "couchstore".
* [JVMCBC-1327](https://issues.couchbase.com/browse/JVMCBC-1327): Improved support for failover handling in future server versions.

#### [](#bugfixes-6)Bugfixes

* [KCBC-139](https://issues.couchbase.com/browse/KCBC-139): When using `BucketManager` with Couchbase Server Community Edition, specifying a bucket creation argument not supported by Community Edition now always results in a `FeatureNotAvailableException`. Previously, this exception was thrown only if the argument differed from the default.
* [JVMCBC-1264](https://issues.couchbase.com/browse/JVMCBC-1264): DNS SRV lookups now honor the DNS search path. This enables DNS SRV resolution in Kubernetes environments where the `*-srv` hostname advertised by the Couchbase Operator is a partial name that must be resolved using a suffix from the DNS search path.
* [JVMCBC-1426](https://issues.couchbase.com/browse/JVMCBC-1426): When Couchbase Server is too busy to start a new KV range scan, the SDK now retries instead of throwing a `CouchbaseException`.

## [](#kotlin-sdk-1-1-releases)Kotlin SDK 1.1 Releases

### [](#v1.1.11)Version 1.1.11 (4 October 2023)

This is a regular maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.11/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.11/)

#### [](#improvements-19)Improvements

* [JCBC-2046](https://issues.couchbase.com/browse/JCBC-2046): With thanks to community member [Marcin Grzejszczak](https://github.com/marcingrzejszczak) for the contribution, support for Micrometer Observation has been added to all JVM SDKs via the new `tracing-micrometer-observation` module.
* [JVMCBC-1327](https://issues.couchbase.com/browse/JVMCBC-1327): Internal improvements to support upcoming faster failover and config push features.

#### [](#bugfixes-7)Bugfixes

* [JVMCBC-1364](https://issues.couchbase.com/browse/JVMCBC-1364): Fixed decoding of certain niche sub-document errors, so they no longer raise a `DecodingFailureException`.

### [](#v1.1.10)Version 1.1.10 (6 September 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.10/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.10/)

#### [](#improvements-20)Improvements

* [JVMCBC-1367](https://issues.couchbase.com/browse/JVMCBC-1367): The `db.couchbase.operations` metric now has `db.name` (bucket), `db.couchbase.scope`, `db.couchbase.collection` and `outcome` labels (tags). This new feature is at Stability.Volatile, and may change before it is promoted to Stability.Committed in a future release.
* [JVMCBC-1311](https://issues.couchbase.com/browse/JVMCBC-1311), [JVMCBC-1352](https://issues.couchbase.com/browse/JVMCBC-1352): Upgraded dependencies.

#### [](#bugfixes-8)Bugfixes

* [JVMCBC-1350](https://issues.couchbase.com/browse/JVMCBC-1350): `lookupInAnyReplica` now throws `FeatureNotAvailableException` if the server does not support the feature.
* [JVMCBC-1351](https://issues.couchbase.com/browse/JVMCBC-1351): `lookupInAnyReplica` no longer hangs when too many operations are specified.
* [JVMCBC-1353](https://issues.couchbase.com/browse/JVMCBC-1353): Removed the unrelocated `io.opentracing` classes that accidentally slipped into version 2.4.9 of the Couchbase `core-io` library.
* [JVMCBC-1361](https://issues.couchbase.com/browse/JVMCBC-1361): When the SDK receives multiple cluster map versions at the same time, it is now more careful about applying only the most recent version. Before this change, there was a brief window where the SDK could apply an obsolete cluster map. If this happened, the SDK would temporarily dispatch requests to incorrect or non-existent nodes. This condition was typically short-lived, and healed the next time the SDK polled for an updated cluster map, or dispatched a KV request to the wrong node.
* [JVMCBC-1368](https://issues.couchbase.com/browse/JVMCBC-1368): Fixed a rare `java.lang.ArithmeticException: / by zero` exception in `RoundRobinSelectionStrategy.select` that could occur during rebalance.

### [](#v1.1.9)Version 1.1.9 (2 August 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.9/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.9/)

#### [](#improvements-21)Improvements

* [JVMCBC-1339](https://issues.couchbase.com/browse/JVMCBC-1339): When KV traffic capture is enabled, each `ReadTrafficCapturedEvent` now contains a single protocol frame, and the human-readable frame description is more accurate.
* [JVMCBC-1320](https://issues.couchbase.com/browse/JVMCBC-1320): The `waitUntilReady` method is now more aggressive about retrying failed pings. Also, waiting for a desired state of `DEGRADED` no longer fails when the client is fully connected to the cluster.
* [JVMCBC-1343](https://issues.couchbase.com/browse/JVMCBC-1343): Reduced the default value for the `io.idleHttpConnectionTimeout` client setting to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures.

### [](#v1.1.8)Version 1.1.8 (19 July 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.8/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.8/)

#### [](#improvements-22)Improvements

* [JVMCBC-1322](https://issues.couchbase.com/browse/JVMCBC-1322): The `waitUntilReady()` method now logs additional diagnostic information to the `com.couchbase.core.WaitUntilReady` logging category at `DEBUG` level.

### [](#v1.1.7)Version 1.1.7 (12 June 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.7/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.7/)

This release refines the sub-document counter methods, and adds a new connection string parameter for disabling TLS certificate verification.

#### [](#improvements-23)Improvements

* [KCBC-123](https://issues.couchbase.com/browse/KCBC-123): Added new versions of `MutateInSpec.incrementAndGet` and `decrementAndGet` without a `delta` parameter ("increment/decrement" implies the delta is 1). Added a `MutateInSpec.addAndGet` method that takes a delta. Deprecated the old increment/decrement methods that take a delta, in favor of the new `addAndGet` method.
* [JVMCBC-1290](https://issues.couchbase.com/browse/JVMCBC-1290): Added a new client setting, `security.enableCertificateVerification`, which defaults to true. This setting allows disabling TLS certificate verification in development environments where configuring the CA certificate to trust is not practical. Setting this to false is equivalent to configuring the environment to use `InsecureTrustManager.INSTANCE`. For compatibility with other modern Couchbase SDKs, certificate verification can now be disabled using the connection string parameter `tls_verify=none`. This feature is introduced at stability level `Volatile`, meaning it may change in a patch release without notice.
* [JVMCBC-1278](https://issues.couchbase.com/browse/JVMCBC-1278), [JVMCBC-1310](https://issues.couchbase.com/browse/JVMCBC-1310), [JVMCBC-1313](https://issues.couchbase.com/browse/JVMCBC-1313): Dependencies updated.

### [](#v1.1.6)Version 1.1.6 (4 May 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.6/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.6/)

This is a regular maintenance release, with no notable changes apart from depedency version bumps.

### [](#v1.1.5)Version 1.1.5 (12 April 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.5/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.5/)

This is a regular maintenance release.

#### [](#improvements-24)Improvements

* [JVMCBC-1223](https://issues.couchbase.com/browse/JVMCBC-1223): Adds a `RetryReason.AUTHENTICATION_ERROR` at `Uncommitted` API stability level. A custom `RetryStrategy` can use this new, more granular information to distinguish if a connection problem is down to an authentication issue.

#### [](#bug-fixes-6)Bug Fixes

* [KCBC-118](https://issues.couchbase.com/browse/KCBC-118): Accessing the result of a sub-document lookupIn `exists` command now throws an appropriate exception (instead of returning false) in more cases where it's not possible to determine whether the field exists:

  * If the document is not JSON, `DocumentNotJsonException` is thrown.
  * If a user without the `SystemXattrRead` permission attempts to check the existence of a system XATTR, `XattrNoAccessException` is thrown.
* [JVMCBC-1252](https://issues.couchbase.com/browse/JVMCBC-1252): Orphaned "observe" operations will no longer occasionally contain a `total_duration_us` field equal to 0.
* [JVMCBC-1255](https://issues.couchbase.com/browse/JVMCBC-1255): If you were subscribing to the event bus and printing all the events, you may have noticed `Event.toString()` throwing a `NullPointerException` if the event context is null. `Event.toString()` now handles null contexts more gracefully, and no longer throws this exception.

### [](#v1.1.4)Version 1.1.4 (8 March 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.4/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.4/)

This is a regular maintenance release.

#### [](#improvements-25)Improvements

* [JVMCBC-1237](https://issues.couchbase.com/browse/JVMCBC-1237): Added "network" as an alias for the "io.networkResolution" connection string parameter. For example, the connection string "couchbase://example.com?network=external" is now equivalent to "couchbase://example.com?io.networkResolution=external". This was done for compatibility with other Couchbase SDKs that use "network" as the name of this parameter.

#### [](#bug-fixes-7)Bug Fixes

* [JVMCBC-1232](https://issues.couchbase.com/browse/JVMCBC-1232): `Cluster.connect()` now rejects connection strings that have no addresses (like "couchbase://"). Before this change, it would accept the invalid connection string, and subsequent operations would fail with a misleading error message: "The cluster does not support cluster-level queries".

### [](#v1.1.3)Version 1.1.3 (9 February 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.3/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.3/)

This is a regular maintenance release.

#### [](#improvements-26)Improvements

* [JVMCBC-1181](https://issues.couchbase.com/browse/JVMCBC-1181): It is now possible to authenticate over secure connections even if the JVM does not support the SASL PLAIN authentication mechanism.
* [JVMCBC-1184](https://issues.couchbase.com/browse/JVMCBC-1184): Updated dependencies.

#### [](#bug-fixes-8)Bug Fixes

* [JVMCBC-1160](https://issues.couchbase.com/browse/JVMCBC-1160): When a sub-document path has a syntax error or is inappropriate for an operation, the SDK now throws `PathInvalidException`. Prior to this change, it would throw a generic `CouchbaseException` with the message "Unexpected SubDocument response code".

### [](#v1.1.2)Version 1.1.2 (16 January 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.2/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.2/)

This is a regular maintenance release.

#### [](#improvements-27)Improvements

* [JVMCBC-1175](https://issues.couchbase.com/browse/JVMCBC-1175): The SDK now includes native libraries for IO and TLS that can enhance performance on `aarch_64` architectures like Graviton and Apple Silicon. Previously, native libraries were included only for `x86_64` architectures. Native libraries for IO and TLS are enabled by default. If you need to disable native IO, set the `ioEnvironment.enableNativeIo` client setting to false. To disable native TLS, set the `security.enableNativeTls` client setting to false.

#### [](#bug-fixes-9)Bug Fixes

* [JVMCBC-1161](https://issues.couchbase.com/browse/JVMCBC-1161): Fixed a minor issue where `cluster.disconnect()` could occasionally time out due to a race condition.
* [JVMCBC-1176](https://issues.couchbase.com/browse/JVMCBC-1176): Setting `security.enableNativeTls` to false now prevents the SDK from even attempting to load the native TLS library. (Prior to this change, the SDK would load the library and just not use it.) In addition to saving a bit of memory, this prevents the JVM from segfaulting on Alpine Linux where glibc is not available.
* [JVMCBC-1174](https://issues.couchbase.com/browse/JVMCBC-1174): Fixed a regression that prevented native TLS from being used regardless of whether the `security.enableNativeTls` client setting was set to true.

### [](#v1.1.1)Version 1.1.1 (7 December 2022)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.1/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.1/)

#### [](#improvements-28)Improvements

* [JVMCBC-1163](https://issues.couchbase.com/browse/JVMCBC-1163): Dependencies have been updated.
* [JVMCBC-1156](https://issues.couchbase.com/browse/JVMCBC-1156): The traffic tracing functionality has been enhanced to perform Wireshark-style dissection of portions of the KV protocol.
* [JCBC-2021](https://issues.couchbase.com/browse/JCBC-2021): Diagnostics for an endpoint now include the state of the endpoint's circuit breaker.

#### [](#bug-fixes-10)Bug Fixes

* [KCBC-107](https://issues.couchbase.com/browse/KCBC-107): The logging configuration DSL property `enableDiagnosticContext` is now mutable.
* [JVMCBC-1157](https://issues.couchbase.com/browse/JVMCBC-1157): The SDK no longer rejects a `PersistTo` requirement in a bucket using the Magma storage engine. Before this change, the SDK would refuse the request because it misidentified Magma buckets as ephemeral (unable to persist documents).
* [JVMCBC-1167](https://issues.couchbase.com/browse/JVMCBC-1167): If you call `CancellationErrorContext.getWaitUntilReadyContext()` on an error context that didn't come from a "wait until ready" request, the method is now guaranteed to return null instead of sometimes throwing a `ClassCastException`.
* [JVMCBC-1178](https://issues.couchbase.com/browse/JVMCBC-1178): Fixed a memory leak in `ManagerMessageHandler`.

### [](#v1.1.0)Version 1.1.0 (24 October 2022)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.1.0/index.html)| [Core API Reference](http://docs.couchbase.com/sdk-api/couchbase-core-io-2.4.0/)

#### [](#improvements-29)Improvements

* [JVMCBC-1102](https://issues.couchbase.com/browse/JVMCBC-1102): Added support for serverless execution environments including AWS Lambda.
* [KCBC-101](https://issues.couchbase.com/browse/KCBC-101): Added an experimental JSON serializer backed by `kotlinx.serialization`. See this [sample code](https://github.com/couchbase/couchbase-jvm-clients/blob/c9ffa30f56294a0b82721bfa42f91e7bc7021bae/kotlin-client/src/main/kotlin/com/couchbase/client/kotlin/samples/KotlinxSerializationSamples.kt#L30-L43) for usage and caveats.
* [KCBC-102](https://issues.couchbase.com/browse/KCBC-102): Added support for configuration profiles, which allow you to quickly configure an environment for common use-cases. In particular, this makes it easy to apply timeouts appropriate for WAN (Internet) development, such as developing against a remote Couchbase Capella instance. Example usage:  
```kotlin  
val cluster = Cluster.connect(  
    connectionString, username, password  
) {  
    applyProfile("wan-development")  
}  
```
* [KCBC-105](https://issues.couchbase.com/browse/KCBC-105), [JVMCBC-1144](https://issues.couchbase.com/browse/JVMCBC-1144): If your Couchbase Server cluster's root certificate is signed by a well-known certificate authority whose certificate is included in the JVM's trust store, it's no longer necessary to configure the certificate in the securityConfig settings.
* [KCBC-104](https://issues.couchbase.com/browse/KCBC-104): Changed `AuthenticationFailureException` error message to indicate that bucket hibernation is now a potential cause. Bucket hibernation is a feature coming in a future Couchbase release.
* [JVMCBC-1154](https://issues.couchbase.com/browse/JVMCBC-1154): Bumped dependencies.

#### [](#bug-fixes-11)Bug Fixes

* [JVMCBC-1141](https://issues.couchbase.com/browse/JVMCBC-1141): Provide required OpenTelemetry span attributes.
* [JVMCBC-1155](https://issues.couchbase.com/browse/JVMCBC-1155): Make sure targeted round-robin request keeps retrying if no config is available.

## [](#kotlin-sdk-1-0-releases)Kotlin SDK 1.0 Releases

### [](#v1.0.4)Version 1.0.4 (9 September 2022)

This maintenance release adds more cluster management APIs, and updates dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.0.4/index.html)

#### [](#improvements-30)Improvements

* [KCBC-94](https://issues.couchbase.com/browse/KCBC-94): `UserManager` has a new `changePassword` function that lets you change the password of the currently authenticated user.
* [KCBC-99](https://issues.couchbase.com/browse/KCBC-99): `Bucket` has a new `collections` property of type `CollectionManager`. You can use the collection manager to create and delete scopes and collections. (Requires Couchbase Server 7.0 or later.)
* [KCBC-100](https://issues.couchbase.com/browse/KCBC-100): Added two new global config properties to help diagnose leaked Cluster instances. `Cluster.maxAllowedInstances` is the number of connected Cluster instances that may exist at the same time. Calling `Cluster.connect` after this limit is reached will either fail or log a warning, depending on the value of the new `Cluster.failIfInstanceLimitReached` property. The default values log a warning if more than 1 Cluster is connected at a time.
* [JVMCBC-1134](https://issues.couchbase.com/browse/JVMCBC-1134): Updated `MemcachedProtocol::decodeStatus` to be inlineable.
* [JVMCBC-1135](https://issues.couchbase.com/browse/JVMCBC-1135): Moved `Core#reconfiguration` off IO threads.
* [JVMCBC-1143](https://issues.couchbase.com/browse/JVMCBC-1143): Failed telemetry spans will now record their exception and error status.
* [JVMCBC-1145](https://issues.couchbase.com/browse/JVMCBC-1145): Updated maintenance dependencies.

### [](#v1.0.3)Version 1.0.3 (2 August 2022)

Maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.0.3/index.html)

#### [](#improvements-31)Improvements

* [JVMCBC-1116](https://issues.couchbase.com/browse/JVMCBC-1116): Dependency versions have been increased.

#### [](#bug-fixes-12)Bug Fixes

* [JVMCBC-1119](https://issues.couchbase.com/browse/JVMCBC-1119): The num (kv) nodesExt to equal number of nodes check can lead to otherwise healthy clusters being flagged as not ready. The check has been removed, and now `bucket.waitUntilReady` will not time out on these edge cases.
* [JVMCBC-1120](https://issues.couchbase.com/browse/JVMCBC-1120): `ClusterConfig#allNodeAddresses` now takes global config into account — avoiding the triggering of some unnecessary reconfigurations.
* [JVMCBC-1112](https://issues.couchbase.com/browse/JVMCBC-1112): Deprecated Reactor Processors have been replaced.
* [JVMCBC-1115](https://issues.couchbase.com/browse/JVMCBC-1115): The SDK now allows for configurations with _only_ TLS ports.

### [](#v1.0.2)Version 1.0.2 (6 July 2022)

Maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.0.2/index.html)

#### [](#bug-fixes-13)Bug Fixes

* [JVMCBC-1103](https://issues.couchbase.com/browse/JVMCBC-1103): To reduce overhead, the `MAX_PARALLEL_FETCH` value in `KeyValueBucketRefresher` has been updated to only fetch one config per poll interval.
* [JVMCBC-1104](https://issues.couchbase.com/browse/JVMCBC-1104): Fixed issue where the global refresher did not honor the config poll interval.

### [](#v1.0.1)Version 1.0.1 (8 June 2022)

Maintenance release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.0.1/index.html)

#### [](#improvements-32)Improvements

* [KCBC-79](https://issues.couchbase.com/browse/KCBC-79): `JacksonJsonSerializer` now accepts the jackson `ObjectMapper` which for example makes it easier to use out of the box with Spring Boot.
* [JVMCBC-1093](https://issues.couchbase.com/browse/JVMCBC-1093): Previously, when a DNS SRV lookup failure occurred, the SDK logged this as a `WARNING` along with a stack trace. The lookup failure is typically harmless, so the log message has now been downgraded to `INFO` level, without a stack trace.
* [JVMCBC-1088](https://issues.couchbase.com/browse/JVMCBC-1088): Updated Netty to version `4.1.77.Final`.

### [](#v1.0.0)Version 1.0.0 (3 May 2022)

Initial GA release.