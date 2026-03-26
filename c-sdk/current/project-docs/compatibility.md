---
title: Compatibility of Couchbase Features, Couchbase Server Versions, and the
  Couchbase C SDK
description: Features available in different SDK versions, and compatibility
  between Server and SDK. Plus notes on Cloud, networks, and AWS Lambda.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/project-docs/pages/compatibility.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:c-sdk:project-docs:compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/project-docs/compatibility.html)

# Compatibility of Couchbase Features, Couchbase Server Versions, and the Couchbase C SDK

> Features available in different SDK versions, and compatibility between Server and SDK. Plus notes on Cloud, networks, and AWS Lambda. 

## [](#couchbase-versionsdk-version-matrix)Couchbase Version/SDK Version Matrix

Couchbase SDKs are tested against a variety of different environments to ensure both backward and forward compatibility with different versions of Couchbase Server. The matrix below denotes the version of Couchbase Server, the version of the C SDK and whether the SDK is:

* ✖ **Unsupported**: This combination is not tested, and is not within the scope of technical support if you have purchased a support agreement.
* ◎ **Compatible**: This combination has been tested previously, and should be compatible. This combination is not recommended by our technical support organization. It is best to upgrade either the SDK or the Couchbase version you are using.
* ✔ **Supported**:This combination is subject to ongoing quality assurance, and is fully supported by our technical support organization.

__Table 1\. Recommended SDK per Server Version Matrix__
|                    | SDK 3.0, 3.1 | 3.2   | 3.3     |
| ------------------ | ------------ | ----- | ------- |
| **Server 6.0**     | **✔**        | **✔** | **✔**   |
| **Server 6.5-6.6** | **✔**        | **✔** | **✔**   |
| **Server 7.0**     | **◎**        | **✔** | **✔**   |
| **Server 7.1-8.0** | **✖**        | **✖** | **✔** ① |

① The C SDK 3.3.12+ is compatible with Server 7.6 - 8.0, but does not contain APIs for some of the [newer features](../../../server/7.6/introduction/whats-new.md), specifically LCB 3.3.x does not contain APIs for Vector Search, Scoped Search Indexes, KV Range Scan, or Sub-Doc Read-from-Replica.

Note the [End of Life dates](https://www.couchbase.com/support-policy/EOL/) for Couchbase Server and SDK versions. See the notes there for Support details.

### [](#capella-compatibility)Capella Compatibility

At time of release, the Couchbase 3.3 C SDK is fully compatible with Couchbase Capella, our fully-hosted database-as-a-service. Note, LCB does not bundle the Capella Client Certificate, follow the [instructions](../../../server/current/guides/connect.md#tls) to download and install the certificate from Capella, then the guide to [secure connections with LCB](../howtos/managing-connections.md#ssl).

Note, Capella is offered as a fully provisioned service, so the underlying version of Couchbase Server changes over time. For this reason, compatibility information between Capella and the SDK is available [on the Capella compatibility page](../../../cloud/reference/sdk-compatibility.md).

## [](#platform-compatibility)Platform Compatibility

Libcouchbase (the C SDK) is tested and supported on the following platforms:

### GNU/Linux

* Amazon Linux 2 & 2023
* Red Hat Enterprise Linux 7, 8, 9 (from LCB 3.3.5), & 10 (from LCB 3.3.18)
* CentOS 7
* Ubuntu (LTS) 22.04 (_Jammy_ — from LCB 3.3.3) & 24.04 (_Noble_ — from 3.3.13)
* Debian 11 (_Bullseye_), and (since LCB 3.13) Debian 12 (_Bookworm_).
* Alpine Linux (Since LCB 3.2.5)

> [!NOTE]
> Some of the OS versions listed above were supported at time of LCB 3.3 release, but have since gone End of Life, so are no longer supported. See the [release notes page](sdk-release-notes.md#latest-release) for the platforms built with the latest release.

### Microsoft Windows

Any MS-supported version compatible with Visual Studio 2015 (VC14), 2017 (VC15), 2019 (VC16), or 2022 (VC17).

### Mac OS X

The current and previous two releases of OS X. At time of writing (December 2023): 15 (Sequoia), 14 (Sonoma), and 13 (Ventura). M1 ARM architecture is fully supported in the 3.3 C SDK.

Although installable or compilable on many other platforms, we cannot provide support for untested combinations.

### [](#arm-processor-support)ARM Processor Support

Libcouchbase (C SDK) 3.3 supports AWS Amazon Graviton2 and Apple M1 ARM processors.

## [](#couchbase-new-feature-availability-matrix)Couchbase New Feature Availability Matrix

__Table 2\. Couchbase Server and SDK Supported Version Matrix__
|                                                      | Server 6.0       | Server 6.5 & 6.6                      | Server 7.0 - 8.0 |
| ---------------------------------------------------- | ---------------- | ------------------------------------- | ---------------- |
| Enhanced Durability                                  | All SDK versions |                                       |                  |
| Durable Writes                                       | Not Supported    | Since 3.0                             |                  |
| Analytics                                            | Since 2.10       |                                       |                  |
| Collections                                          | Not Supported    | Developer Preview in 6.5-6.6, SDK 3.0 | Since 3.0.6      |
| Scope-Level SQL++ Queries & all Collections features | Not Supported    | Since SDK 3.2.0                       |                  |
| Request Tracing                                      | Not Supported    | Since SDK 3.0.2                       |                  |

### [](#network-requirements)Network Requirements

Couchbase SDKs are developed to be run in an environment with local area network (LAN) like throughput and latencies. While there is no technical issue that prevents the use across a wide area network (WAN), SDKs have certain thresholds around timeouts and behaviors to recover that will not be the same once the higher latency and possible bandwidth constraints and congestion of a WAN is introduced. Couchbase tests for correctness under LAN like conditions. For this reason, only LAN-like network environments are officially supported.

Couchbase does document, for purposes of convenience when developing and performing basic operational work, what may need to be tuned when network throughputs and latencies are higher. If you encounter issues, even with these tunables, you should attempt the same workload from a supported, LAN-like environment.

#### [](#serverless-environments)Serverless Environments

Recent SDKs offer better resilience in handling errors that may occur when running your application in serverless environments, in particular when processes are frozen or thawed, and a rebalance is required. This means official support for AWS Lambda, Azure Functions, and GCP Functions.

> [!NOTE]
> When **DNS SRV** records are used to connect to the SDK it is possible for the underlying addresses to change (i.e. the cluster could move). The SDK will detect this and react accordingly so that your application can continue to work correctly.

Couchbase SDKs indicate the stability of an API through documentation. Since there are different meanings when developers mention stability, we mean **interface stability**: how likely the interface is to change or be removed entirely. A stable interface is one that is guaranteed not to change between versions, meaning that you may use an API of a given SDK version and be assured that the given API will retain the same parameters and behavior in subsequent versions. An unstable interface is one which may appear to work or behave in a specific way within a given SDK version, but may change in its behavior or arguments in future SDK versions, causing odd application behavior or compiler/API usage errors. **Implementation stability** is implied to be more reliable at higher levels, but all are tested to the level that is appropriate for their stability.

Couchbase uses three interface stability classifiers. You may find these classifiers appended as annotations or comments within documentation for each API:

* **Committed**: This stability level is used to indicate the most stable interfaces that are guaranteed to be supported and remain stable between SDK versions. This is the default — unless otherwise stated in the documentation, each API has **Committed** status.
* **Uncommitted**: This level is used to indicate APIs that are _unlikely_ to change, but _may_ still change as final consensus on their behavior has not yet been reached. _Uncommitted_ APIs usually end up becoming stable APIs.
* **Volatile**: This level is used to indicate experimental APIs that are still in flux and may likely be changed. It may also be used to indicate inherently private APIs that may be exposed, but "YMMV" (your mileage may vary) principles apply. _Volatile_ APIs typically end up being promoted to _Uncommitted_ after undergoing some modifications.

APIs that are marked as _Committed_ have a stable implementation. _Uncommitted_ and _Volatile_ APIs should be stable within the bounds of any known and often documented issues, but Couchbase has not made a commitment to these APIs and may not respond to reported defects with the same priority.

Additionally, take note of the following interface labels:

* **Deprecated**: Any API marked deprecated may be removed in the next major version released. Couchbase recommends migrating from the deprecated API to the replacement as soon as possible. In rare instances, deprecated API may be rendered non-functional in a dot-minor release when the API cannot continue to be supported.
* **Internal**: This level is used to indicate you should not rely on this API as it is not intended for use outside the module, even to other Couchbase components.

This release of the SDK is written to version 3.3 of the SDK API specification (and matching the features available in Couchbase 8.0 and earlier). For most developers, just using the latest version will be all that matters, and few will need to look at another of our SDKs. Just for those few that do, the table below shows each Couchbase SDK release version that matches the API version (and a table that covers the earliest versions of the 3.x SDK API can be found in documentation for earlier versions of the SDK).

Whilst these two numbers match for the .NET SDK, this is not the case for the others, as version numbers for individual SDKs are bumped up in line with [Semantic Versioning](https://semver.org/) — check the [release notes](#sdk-release-notes) of each SDK for individual details.

__Table 3\. SDK API Versions__
|                                                                | API 3.3       | API 3.4   | API 3.5 | API 3.6 | API 3.7 | API 3.8      |
| -------------------------------------------------------------- | ------------- | --------- | ------- | ------- | ------- | ------------ |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)    | 3.3           | 3.4       | 3.5     | 3.6     | 3.7     | 3.8          |
| [C (libcouchbase)](../hello-world/overview.md)                 | 3.3.0 - 3.3.2 | 3.3.3 ①   | N/A ②   | N/A ②   | N/A ②   | N/A ②        |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)        | \-            | \-        | \-      | 1.0     | 1.1     | 1.2          |
| [Go](../../../go-sdk/current/hello-world/overview.md)          | 2.5           | 2.6 & 2.7 | 2.8     | 2.9     | 2.10    | 2.11         |
| [Java](../../../java-sdk/current/hello-world/overview.md)      | 3.3           | 3.4 & 3.5 | 3.6     | 3.7     | 3.8     | 3.9 & 3.10   |
| [Kotlin](../../../kotlin-sdk/current/hello-world/overview.md)  | 1.0           | 1.1 & 1.2 | 1.3     | 1.4     | 1.5     | 3.9 & 3.10 ③ |
| [Node.js](../../../nodejs-sdk/current/hello-world/overview.md) | 4.1           | 4.2       | 4.3     | 4.4     | 4.5     | 4.6          |
| [PHP](../../../php-sdk/current/hello-world/overview.md)        | 4.0           | 4.1       | 4.2     | 4.2.2   | 4.3     | 4.4          |
| [Python](../../../python-sdk/current/hello-world/overview.md)  | 4.0           | 4.1       | 4.2     | 4.3     | 4.4     | 4.5          |
| [Ruby](../../../ruby-sdk/current/hello-world/overview.md)      | 3.3           | 3.4       | 3.5     | 3.5.2   | 3.6     | 3.7          |
| [Rust](../../../rust-sdk/current/hello-world/overview.md)      | \-            | \-        | \-      | \-      | \-      | 1.0          |
| [Scala](../../../scala-sdk/current/hello-world/overview.md)    | 1.3           | 1.4 & 1.5 | 1.6     | 1.7     | 1.8     | 3.9 & 3.10 ③ |

| **1** | Excludes DNS SRV refresh support in Serverless Environments.                                                                                                                                              |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | For most purposes better productivity and functionality can be found in our [C++ SDK](../../../cxx-sdk/current/hello-world/overview.md).                                                                  |
| **3** | With the Java 3.9 release, the other JVM SDKs hosted in the Java SDK monorepo adopted common release versions. This includes a number of other artifacts, as can be seen referenced in the release notes. |

**SDK API 3.8**: Introduced alongside Couchbase Server 8.0, which adds support for 128 vBuckets on Magma. Server 8.0 introduced vector query using Global Secondary Indexes (GSI), the Query Service index — using either a fast Hyperscale index, or a composite index to combine scalar queries with semantic search.

**SDK API 3.7**: Introduced support for KV reads from preferred server groups. The .NET SDK has been updated to support the latest Transactions specification — and the library is now incorporated within the .NET SDK. A new `getMulti()` interface batch reads with read committed isolation. Additionally, the Java SDK now includes a Quarkus extension with GraalVM support.

**SDK API 3.6**: Introduced support for base 64 encoded vector types alongside Server 7.6.2 (and Capella). General Availability of our C++ SDK — now available as a supported, stand-alone SDK, this SDK is also the core of our Node.js, PHP, Python, and Ruby SDKs.

**SDK API 3.5**: Introduced support for Vector Search alongside Server 7.6 (and Capella). Adds scoped indexes to Search (for Vector Seach and traditional FTS). Read from Replica for Query and Sub-Doc operations. KV Range Scan for querying documents through the Data Service, even if you don't know the document IDs (for use cases that require relatively low concurrency and tolerate relatively high latency). Transactions now implemented as a native library in all SDKs (except libcouchbase).

**SDK API 3.4**: Introduced support for ARM v8 on Ubuntu 20.04, Transactions on Spring Data Couchbase, and compatibility with running in serverless environments, such as AWS λ. The `couchbase2://` connection string was introduced in Go 2.7, Java 3.5, Kotlin 1.2, and Scala 1.5, for Cloud Native Gateway with [Couchbase Autonomous Operator](../../../operator/current/overview.md) (from CAO 2.6.1).

**SDK API 3.3**: Introduced alongside Couchbase Server 7.1, adds Management API for Eventing and Index Management for Scopes & Collections; extends Bucket Management API to support Custom Conflict Resolution and Storage Options; adds new platform support for Linux Alpine OS, Apple M1, and AWS Graviton2; provides improved error messages for better error handling; and an upgraded Spark Connector that runs on Spark 3.0 & 3.1 Platform.

**SDK API 3.2**: Introduced alongside Couchbase Server 7.0, provides features in support of Scopes and Collections, extends capabilities around Open Telemetry API to instrument telemetry data, enhanced client side field level encryption to add an additional layer of security to protect sensitive data, adds new platform support such as Ubuntu 20.04 LTS.

**SDK API 3.1**: Introduced alongside Couchbase Server 6.6, focuses on Bucket Management API, adds capabilities around Full Text Search features such-as Geo-Polygon support, Flex Index, and Scoring.

**SDK API 3.0**: Introduced alongside Couchbase Server 6.5, is a major overhaul from its predecessor, has simplified surface area, removed long-standing bugs and deprecated/removed old API, introduces new programming languages Scala and Ruby, written in anticipation to support Scopes and Collections.

Documentation on older, unsupported versions of the SDK — that have reached end-of-life — can be found in the [archive](https://docs-archive.couchbase.com/home/index.html).