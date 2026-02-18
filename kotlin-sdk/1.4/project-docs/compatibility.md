---
title: Compatibility
description: Platform compatibility, and features available in different SDK
  versions, and compatibility between Server and SDK. Plus notes on Cloud,
  networks, and AWS Lambda.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.4/modules/project-docs/pages/compatibility.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/kotlin-sdk/1.4/project-docs/compatibility.html)

# Compatibility

> Platform compatibility, and features available in different SDK versions, and compatibility between Server and SDK. Plus notes on Cloud, networks, and AWS Lambda. 

The Kotlin SDK requires Java 8 or later (_Java 21 is recommended_), and Kotlin 1.6.20 or later.

## [](#platform-compatibility)Platform Compatibility

### [](#jdk-version-compatibility)JDK Version Compatibility

The Kotlin SDK is tested with Oracle JDK and OpenJDK. Other JDK implementations might work but are not tested and are unsupported. We recommend running the latest LTS version (i.e. at the time of writing JDK 21) with the highest patch version available.

The following JDK releases are supported:

* [OpenJDK 21 with HotSpot JVM](https://adoptium.net/) (recommended)
* [OpenJDK 17 with HotSpot JVM](https://adoptium.net/)
* [Oracle JDK 17](https://www.oracle.com/java/technologies/downloads/#jdk17)
* [OpenJDK 11](https://adoptium.net/) (Hotspot recommended) or [Oracle JDK 11](https://www.oracle.com/java/technologies/downloads/#jdk11)
* [OpenJDK 1.8 with HotSpot JVM](https://adoptium.net/)
* [Oracle JDK 1.8](https://www.oracle.com/java/technologies/downloads/#java8)

Please make sure you run on one of the latest patch releases, since they provide stability improvements and security fixes in general.

### [](#os-compatibility)OS Compatibility

In general, the JVM eliminates concerns about underlying OS compatibility, and Couchbase JVM SDKs can be expected to run on all of the Operating Systems supported by [Couchbase Server](../../../server/7.6/install/install-platforms.md).

The Kotlin SDK is tested and supported on the following OSs and platforms:

### GNU/Linux

* Amazon Linux 2 & AL2023.
* Red Hat Enterprise Linux 8 & 9;
* Oracle Linux 8 & 9.
* Ubuntu (LTS) 20.04 (_Focal_) & 22.04 (_Jammy_).
* Debian 10 (_Buster_), 11 (_Bullseye_), and Debian 12 (_Bookworm_).
* SUSE Enterprise Linux 12 & 15
* Alpine Linux 3.18 (_Oracle JDK only_) — but see [workaround note below](#alpine-linux-compatibility).

### Microsoft Windows

* Microsoft Windows 10 & 11;
* Windows Server 2019 & 2022.

### Mac OS X

The current and previous two releases of OS X. At time of writing (June 2024): 14 (Sonoma), 13 (Ventura), and 12 (Monterey). M1 ARM architecture is fully supported in the Scala SDK.

### ARM Processor Support

AWS Amazon Graviton2, Apple M1 ARM processors, and ARMv8 on Ubuntu 20.04+ (from SDK 1.4).

The JVM SDKs should also be expected to run on other commonly-available GNU/Linux distributions which support an appropriate JDK, but not all combinations can be tested — notable exceptions are listed below.

#### [](#alpine-linux-compatibility)Alpine Linux Compatibility

The [Netty](https://netty.io) I/O library used by our JVM SDKs supports native optimizations to achieve higher throughput and lower latency — which the SDK enables by default. Those modules are compiled against `glibc` and Alpine Linux uses `musl` instead — so the Kotlin SDK is unable to complete bootstrapping on this platform.

Because Alpine Linux does not have the `glibc` support needed, we highly recommend that you seek an alternative distribution where possible. If that is not a option, then a possible workaround that can be applied is as follows:

* Disable the native IO:  
```none  
val cluster = Cluster.connect(...) {  
    ioEnvironment {  
        enableNativeIo = false  
    }  
}  
```
* Disable it in Netty itself via the following system property:  
```none
-Dcom.couchbase.client.core.deps.io.netty.transport.noNative=true  
```

The downside of these workarounds is potentially reduced performance, which can be determined through benchmarking and profiling.

### [](#network-requirements)Network Requirements

Couchbase SDKs are developed to be run in an environment with local area network (LAN) like throughput and latencies. While there is no technical issue that prevents the use across a wide area network (WAN), SDKs have certain thresholds around timeouts and behaviors to recover that will not be the same once the higher latency and possible bandwidth constraints and congestion of a WAN is introduced. Couchbase tests for correctness under LAN like conditions. For this reason, only LAN-like network environments are officially supported.

Couchbase does document, for purposes of convenience when developing and performing basic operational work, what may need to be tuned when network throughputs and latencies are higher. If you encounter issues, even with these tunables, you should attempt the same workload from a supported, LAN-like environment.

#### [](#serverless-environments)Serverless Environments

Recent SDKs offer better resilience in handling errors that may occur when running your application in serverless environments, in particular when processes are frozen or thawed, and a rebalance is required. This means official support for AWS Lambda, Azure Functions, and GCP Functions.

> [!NOTE]
> When **DNS SRV** records are used to connect to the SDK it is possible for the underlying addresses to change (i.e. the cluster could move). The SDK will detect this and react accordingly so that your application can continue to work correctly.

## [](#couchbase-server-compatibility)Couchbase Server Compatibility

Couchbase SDKs are tested against a variety of different environments to ensure both backward and forward compatibility with different versions of Couchbase Server.

### [](#couchbase-versionsdk-version-matrix)Couchbase Version/SDK Version Matrix

The matrix below denotes the version of Couchbase Server, the version of the Scala SDK and whether the SDK is:

* ✖ **Unsupported**: This combination is not tested, and is not within the scope of technical support if you have purchased a support agreement.
* ◎ **Compatible**: This combination has been tested previously, and should be compatible. This combination is not recommended by our technical support organization. It is best to upgrade either the SDK or the Couchbase version you are using.
* ✔ **Supported**: This combination is subject to ongoing quality assurance, and is fully supported by our technical support organization.

__Recommended SDK per Server Version Matrix__
|                      | 1.0   | 1.1, 1.2 | 1.3, 1.4 |
| -------------------- | ----- | -------- | -------- |
| **Server 7.0 - 7.2** | **✔** | **✔**    | **✔**    |
| **Server 7.6**       | **✔** | **✔**    | **✔**    |

Note the [End of Life dates](https://www.couchbase.com/support-policy) for Couchbase Server and SDK versions. See the notes there for Support details.

### [](#capella-compatibility)Capella Compatibility

The Couchbase Scala SDK is fully compatible with Couchbase Capella, our fully-hosted database-as-a-service. To make development easier, the SDK includes the Capella client certificate ready installed.

Note, Capella is offered as a fully provisioned service, so the underlying version of Couchbase Server changes over time. For this reason, compatibility information between Capella and the SDK is available [on the Capella compatibility page](../../../cloud/reference/sdk-compatibility.md).

### [](#couchbase-new-feature-availability-matrix)Couchbase New Feature Availability Matrix

__Couchbase Server and SDK Supported Version Matrix__
|                                                                      | Server 7.0 & 7.1 | Server 7.2                                                                                          | Server 7.6 |
| -------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------- | ---------- |
| Enhanced Durability                                                  | All SDK versions |                                                                                                     |            |
| Durable Writes                                                       | Since 1.0        |                                                                                                     |            |
| Analytics                                                            | Since 1.0        |                                                                                                     |            |
| Collections                                                          | Since 1.0        |                                                                                                     |            |
| Scope-Level SQL++ (formerly N1QL) Queries & all Collections features | Since SDK 1.2.0  |                                                                                                     |            |
| Request Tracing                                                      | Since SDK 1.0    |                                                                                                     |            |
| Cloud Native Gateway                                                 | Not Supported    | From SDK 1.2.0 (with [Couchbase Autonomous Operator](../../../operator/current/overview.md) 2.6.1+) |            |
| Vector Search                                                        | N/A              | From SDK 1.3.0 (includes base64-encoded from SDK 1.4.0)                                             |            |

### [](#spring-data-couchbase-compatibility)Spring Data Couchbase Compatibility

[Spring Data Couchbase](https://projects.spring.io/spring-data-couchbase/) uses the Java SDK underneath and as a result is also provides different compatibilities with Couchbase Server. The following table provides an overview.

__Recommended Spring Data Couchbase per Server Version Matrix__
|                      | SDC 4.3 - 4.4         | SDC 5.0 - 5.2                      |
| -------------------- | --------------------- | ---------------------------------- |
| _Status →_           | _Maintenance Support_ | _New Features, Active Development_ |
| **Server 7.0 - 7.6** | **Compatible**        | **Recommended**                    |

> [!NOTE]
> Check the Spring Data Couchbase’s compile dependencies — older versions may link an out-of-date version of the SDK in their dependencies list, although a supported version should be in the `updates`. Please make sure that you are using a supported version of the Couchbase Scala SDK, prefereably the latest version, which will contain any available bug fixes. Using the latest Spring Data Couchbase should ensure that this is so.

### [](#api-version)API Version

This release of the SDK is written to version 3.6 of the SDK API specification (and matching the features available in Couchbase 7.6.2 and earlier). For most developers, just using the latest version will be all that matters, and few will need to look at another of our SDKs. Just for those few that do, the table below shows each Couchbase SDK release version that matches the API version (and a table that covers the earliest versions of the 3.x SDK API can be found in documentation for earlier versions of the SDK).

Whilst these two numbers match for the .NET SDK, this is not the case for the others, as version numbers for individual SDKs are bumped up in line with [Semantic Versioning](https://semver.org/) — check the [release notes](#sdk-release-notes) of each SDK for individual details.

__SDK API Versions__
|                                                                    | API 3.2   | API 3.3       | API 3.4   | API 3.5 | API 3.6 |
| ------------------------------------------------------------------ | --------- | ------------- | --------- | ------- | ------- |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)        | 3.2       | 3.3           | 3.4       | 3.5     | 3.6     |
| [C (libcouchbase)](../../../c-sdk/current/hello-world/overview.md) | 3.2       | 3.3.0 - 3.3.2 | 3.3.3 ①   | N/A ②   | N/A ②   |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)            | \-        | \-            | \-        | \-      | 1.0     |
| [Go](../../../go-sdk/current/hello-world/overview.md)              | 2.3 & 2.4 | 2.5           | 2.6 & 2.7 | 2.8     | 2.9     |
| [Java](../../../java-sdk/current/hello-world/overview.md)          | 3.2       | 3.3           | 3.4 & 3.5 | 3.6     | 3.7     |
| [Kotlin](../../current/hello-world/overview.md)                    | \-        | 1.0           | 1.1 & 1.2 | 1.3     | 1.4     |
| [Node.js](../../../nodejs-sdk/current/hello-world/overview.md)     | 3.2 & 4.0 | 4.1           | 4.2       | 4.3     | 4.4     |
| [PHP](../../../php-sdk/current/hello-world/overview.md)            | 3.2       | 4.0           | 4.1       | 4.2     | 4.2.2   |
| [Python](../../../python-sdk/current/hello-world/overview.md)      | 3.2       | 4.0           | 4.1       | 4.2     | 4.3     |
| [Ruby](../../../ruby-sdk/current/hello-world/overview.md)          | 3.2       | 3.3           | 3.4       | 3.5     | 3.5.2   |
| [Scala](../../../scala-sdk/current/hello-world/overview.md)        | 1.2       | 1.3           | 1.4 & 1.5 | 1.6     | 1.7     |

| **1** | Excludes DNS SRV refresh support in Serverless Environments.                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | For most purposes better productivity and functionality can be found in our [C++ SDK](../../../cxx-sdk/current/hello-world/overview.md). |

**SDK API 3.6**: Introduced support for base 64 encoded vector types alongside Server 7.6.2 (and Capella). General Availability of our C++ SDK — now available as a supported, stand-alone SDK, this SDK is also the core of our Node.js, PHP, Python, and Ruby SDKs.

**SDK API 3.5**: Introduced support for Vector Search alongside Server 7.6 (and Capella). Adds scoped indexes to Search (for Vector Seach and traditional FTS). Read from Replica for Query and Sub-Doc operations. KV Range Scan for querying documents through the Data Service, even if you don’t know the document IDs (for use cases that require relatively low concurrency and tolerate relatively high latency). Transactions now implemented as a native library in all SDKs (except libcouchbase).

**SDK API 3.4**: Introduced support for ARM v8 on Ubuntu 20.04, Transactions on Spring Data Couchbase, and compatibility with running in serverless environments, such as AWS λ. The `couchbase2://` connection string was introduced in Go 2.7, Java 3.5, Kotlin 1.2, and Scala 1.5, for Cloud Native Gateway with [Couchbase Autonomous Operator](../../../operator/current/overview.md) (from CAO 2.6.1).

**SDK API 3.3**: Introduced alongside Couchbase Server 7.1, adds Management API for Eventing and Index Management for Scopes & Collections; extends Bucket Management API to support Custom Conflict Resolution and Storage Options; adds new platform support for Linux Alpine OS, Apple M1, and AWS Graviton2; provides improved error messages for better error handling; and an upgraded Spark Connector that runs on Spark 3.0 & 3.1 Platform.

**SDK API 3.2**: Introduced alongside Couchbase Server 7.0, provides features in support of Scopes and Collections, extends capabilities around Open Telemetry API to instrument telemetry data, enhanced client side field level encryption to add an additional layer of security to protect sensitive data, adds new platform support such as Ubuntu 20.04 LTS.

**SDK API 3.1**: Introduced alongside Couchbase Server 6.6, focuses on Bucket Management API, adds capabilities around Full Text Search features such-as Geo-Polygon support, Flex Index, and Scoring.

**SDK API 3.0**: Introduced alongside Couchbase Server 6.5, is a major overhaul from its predecessor, has simplified surface area, removed long-standing bugs and deprecated/removed old API, introduces new programming languages Scala and Ruby, written in anticipation to support Scopes and Collections.

## [](#sdk-api-stability)SDK API Stability

### [](#interface-stability)Interface Stability

Couchbase SDKs indicate the stability of an API through documentation. Since there are different meanings when developers mention stability, we mean **interface stability**: how likely the interface is to change or be removed entirely. A stable interface is one that is guaranteed not to change between versions, meaning that you may use an API of a given SDK version and be assured that the given API will retain the same parameters and behavior in subsequent versions. An unstable interface is one which may appear to work or behave in a specific way within a given SDK version, but may change in its behavior or arguments in future SDK versions, causing odd application behavior or compiler/API usage errors. **Implementation stability** is implied to be more reliable at higher levels, but all are tested to the level that is appropriate for their stability.

Couchbase uses three interface stability classifiers. You may find these classifiers appended as annotations or comments within documentation for each API:

* **Committed**: This stability level is used to indicate the most stable interfaces that are guaranteed to be supported and remain stable between SDK versions. This is the default — unless otherwise stated in the documentation, each API has **Committed** status.
* **Uncommitted**: This level is used to indicate APIs that are _unlikely_ to change, but _may_ still change as final consensus on their behavior has not yet been reached. _Uncommitted_ APIs usually end up becoming stable APIs.
* **Volatile**: This level is used to indicate experimental APIs that are still in flux and may likely be changed. It may also be used to indicate inherently private APIs that may be exposed, but "YMMV" (your mileage may vary) principles apply. _Volatile_ APIs typically end up being promoted to _Uncommitted_ after undergoing some modifications.

APIs that are marked as _Committed_ have a stable implementation. _Uncommitted_ and _Volatile_ APIs should be stable within the bounds of any known and often documented issues, but Couchbase has not made a commitment to these APIs and may not respond to reported defects with the same priority.

Additionally, take note of the following interface labels:

* **Deprecated**: Any API marked deprecated may be removed in the next major version released. Couchbase recommends migrating from the deprecated API to the replacement as soon as possible. In rare instances, deprecated API may be rendered non-functional in a dot-minor release when the API cannot continue to be supported.
* **Internal**: This level is used to indicate you should not rely on this API as it is not intended for use outside the module, even to other Couchbase components.

### [](#older-sdk-versions)Older SDK Versions

Documentation on older, unsupported versions of the SDK — that have reached end-of-life — can be found in the [archive](https://docs-archive.couchbase.com/home/index.html).