---
title: Compatibility
description: Platform compatibility, and features available in different SDK
  versions, and compatibility between Server and SDK. Plus notes on Cloud,
  networks, and AWS Lambda.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/project-docs/pages/compatibility.adoc
  xref: xref:4.4@python-sdk:project-docs:compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.4/project-docs/compatibility.html)

# Compatibility

> Platform compatibility, and features available in different SDK versions, and compatibility between Server and SDK. Plus notes on Cloud, networks, and AWS Lambda. 

The Couchbase Python SDK aims to run on any [supported Python version](https://devguide.python.org/versions/#supported-versions) in security or maintenance status — see the table below for [supported versions](#python-version-compat).

## [](#platform-compatibility)Platform Compatibility

### [](#python-version-compatibility)Python Version Compatibility

The Couchbase Python SDK aims to support [Python versions](https://devguide.python.org/versions/#supported-versions) in security or bug-fix (a.k.a. maintenance) status. The table below indicates the Python SDK version where support of a version of Python was added. Python versions that have reached their [End-of-Life date](https://endoflife.date/python) are not supported.

Because the Python SDK is written primarily in C using the CPython API, the official SDK will not work on PyPy.

Other Python versions and implementations might work but are _not tested and are not supported_. Please make sure you run on one of the latest patch releases, since they provide stability improvements and security fixes in general.

__Supported Python Versions__
| Python Version                                            | Support EOL   | Couchbase SDK Versions Supported |
| --------------------------------------------------------- | ------------- | -------------------------------- |
| [3.9](https://www.python.org/dev/peps/pep-0596/#lifespan) | until 2025-10 | from 3.0.0                       |
| [3.10](https://peps.python.org/pep-0619/#lifespan)        | until 2026-10 | from 4.0.0                       |
| [3.11](https://peps.python.org/pep-0664/#lifespan)        | until 2027-10 | from 4.1.6                       |
| [3.12](https://peps.python.org/pep-0693/#lifespan)        | until 2028-10 | from 4.3.2                       |
| [3.13](https://peps.python.org/pep-0719/#lifespan)        | until 2029-10 | from 4.3.4                       |

### [](#os-compatibility)OS Compatibility

The Python SDK is built on top of the C++ SDK, which is tested and supported on the following platforms:

### GNU/Linux

* Amazon Linux 2 & AL2023.
* Red Hat Enterprise Linux 8 & 9;
* Oracle Linux 8 & 9.
* Ubuntu (LTS) 22.04 (_Jammy_) & 24.04 (_Noble_).
* Debian 11 (_Bullseye_) & Debian 12 (_Bookworm_).
* SUSE Enterprise Linux 12 & 15.
* Alpine Linux 3.18.

### Microsoft Windows

* Microsoft Windows 10 & 11;
* Windows Server 2019 & 2022.

### Mac OS X

The current and previous two releases of OS X. At time of writing (April 2025): 15 (Sequoia), 14 (Sonoma), and 13 (Ventura). M1 ARM architecture is fully supported in the Python SDK.

### ARM Processor Support

AWS Amazon Graviton2, Apple M1 ARM processors, and ARMv8 on Ubuntu.

### [](#network-requirements)Network Requirements

Couchbase SDKs are developed to be run in an environment with local area network (LAN) like throughput and latencies. While there is no technical issue that prevents the use across a wide area network (WAN), SDKs have certain thresholds around timeouts and behaviors to recover that will not be the same once the higher latency and possible bandwidth constraints and congestion of a WAN is introduced. Couchbase tests for correctness under LAN like conditions. For this reason, only LAN-like network environments are officially supported.

Couchbase does document, for purposes of convenience when developing and performing basic operational work, what may need to be tuned when network throughputs and latencies are higher. If you encounter issues, even with these tunables, you should attempt the same workload from a supported, LAN-like environment.

#### [](#serverless-environments)Serverless Environments

Recent SDKs offer better resilience in handling errors that may occur when running your application in serverless environments, in particular when processes are frozen or thawed, and a rebalance is required. This means official support for AWS Lambda, Azure Functions, and GCP Functions.

> [!NOTE]
> When **DNS SRV** records are used to connect to the SDK it is possible for the underlying addresses to change (i.e. the cluster could move). The SDK will detect this and react accordingly so that your application can continue to work correctly.

### [](#ssl-library)SSL Library

The Python SDK binaries are statically link against `BoringSSL`, and there is no need to separately install any SSL library.

## [](#couchbase-server-compatibility)Couchbase Server Compatibility

Couchbase SDKs are tested against a variety of different environments to ensure both backward and forward compatibility with different versions of Couchbase Server.

### [](#couchbase-versionsdk-version-matrix)Couchbase Version/SDK Version Matrix

The matrix below denotes the version of Couchbase Server, the version of the Python SDK and whether the SDK is:

* ✖ **Unsupported**: This combination is not tested, and is not within the scope of technical support if you have purchased a support agreement.
* ◎ **Compatible**: This combination has been tested previously, and should be compatible. This combination is not recommended by our technical support organization. It is best to upgrade either the SDK or the Couchbase version you are using.
* ✔ **Supported**: This combination is subject to ongoing quality assurance, and is fully supported by our technical support organization.

__Recommended SDK per Server Version Matrix__
|                      | 4.0, 4.1 | 4.2 - 4.3 | 4.4   |
| -------------------- | -------- | --------- | ----- |
| **Server 7.0 - 7.2** | **✔**    | **✔**     | **✔** |
| **Server 7.6**       | **✔**    | **✔**     | **✔** |

Note the [End of Life dates](https://www.couchbase.com/support-policy) for Couchbase Server and SDK versions. See the notes there for Support details.

### [](#capella-compatibility)Capella Compatibility

The Python SDK is fully compatible with Couchbase Capella, our fully-hosted database-as-a-service. To make development easier, the Python SDK includes the Capella client certificate ready installed.

Note, Capella is offered as a fully provisioned service, so the underlying version of Couchbase Server changes over time. For this reason, compatibility information between Capella and the SDK is available [on the Capella compatibility page](../../../cloud/reference/sdk-compatibility.md).

### [](#couchbase-new-feature-availability-matrix)Couchbase New Feature Availability Matrix

__Couchbase Server and SDK Supported Version Matrix__
|                                                                      | Server 7.0, 7.1   | Server 7.2     | Server 7.6 |
| -------------------------------------------------------------------- | ----------------- | -------------- | ---------- |
| Enhanced Durability                                                  | All SDK versions  |                |            |
| Durable Writes                                                       | Since 3.0         |                |            |
| Analytics                                                            | Since 2.6         |                |            |
| Collections                                                          | Since 3.0.10      |                |            |
| Scope-Level SQL++ (formerly N1QL) Queries & all Collections features | Since SDK 3.2.0   |                |            |
| Request Tracing                                                      | Since SDK 3.2.0   |                |            |
| Distributed ACID Transactions                                        | Since SDK 4.0     |                |            |
| Cloud Native Gateway                                                 | Not Yet Supported |                |            |
| Vector Search                                                        | N/A               | From SDK 4.2.0 |            |

### [](#api-version)API Version

This release of the SDK is written to version 3.7 of the SDK API specification (and matching the features available in Couchbase 7.6.6 and earlier). For most developers, just using the latest version will be all that matters, and few will need to look at another of our SDKs. Just for those few that do, the table below shows each Couchbase SDK release version that matches the API version (and a table that covers the earliest versions of the 3.x SDK API can be found in documentation for earlier versions of the SDK).

Whilst these two numbers match for the .NET SDK, this is not the case for the others, as version numbers for individual SDKs are bumped up in line with [Semantic Versioning](https://semver.org/) — check the [release notes](#sdk-release-notes) of each SDK for individual details.

__SDK API Versions__
|                                                                    | API 3.3       | API 3.4   | API 3.5 | API 3.6 | API 3.7 |
| ------------------------------------------------------------------ | ------------- | --------- | ------- | ------- | ------- |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)        | 3.3           | 3.4       | 3.5     | 3.6     | 3.7     |
| [C (libcouchbase)](../../../c-sdk/current/hello-world/overview.md) | 3.3.0 - 3.3.2 | 3.3.3 ①   | N/A ②   | N/A ②   | N/A ②   |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)            | \-            | \-        | \-      | 1.0     | 1.1     |
| [Go](../../../go-sdk/current/hello-world/overview.md)              | 2.5           | 2.6 & 2.7 | 2.8     | 2.9     | 2.10    |
| [Java](../../../java-sdk/current/hello-world/overview.md)          | 3.3           | 3.4 & 3.5 | 3.6     | 3.7     | 3.8     |
| [Kotlin](../../../kotlin-sdk/current/hello-world/overview.md)      | 1.0           | 1.1 & 1.2 | 1.3     | 1.4     | 1.5     |
| [Node.js](../../../nodejs-sdk/current/hello-world/overview.md)     | 4.1           | 4.2       | 4.3     | 4.4     | 4.5     |
| [PHP](../../../php-sdk/current/hello-world/overview.md)            | 4.0           | 4.1       | 4.2     | 4.2.2   | 4.3     |
| [Python](../../current/hello-world/overview.md)                    | 4.0           | 4.1       | 4.2     | 4.3     | 4.4     |
| [Ruby](../../../ruby-sdk/current/hello-world/overview.md)          | 3.3           | 3.4       | 3.5     | 3.5.2   | 3.6     |
| [Scala](../../../scala-sdk/current/hello-world/overview.md)        | 1.3           | 1.4 & 1.5 | 1.6     | 1.7     | 1.8     |

| **1** | Excludes DNS SRV refresh support in Serverless Environments.                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | For most purposes better productivity and functionality can be found in our [C++ SDK](../../../cxx-sdk/current/hello-world/overview.md). |

**SDK API 3.7**: Introduced support for KV reads from preferred server groups. The .NET SDK has been updated to support the latest Transactions specification — and the library is now incorporated within the .NET SDK. A new `getMulti()` interface batch reads with read committed isolation. Additionally, the Java SDK now includes a Quarkus extension with GraalVM support.

**SDK API 3.6**: Introduced support for base 64 encoded vector types alongside Server 7.6.2 (and Capella). General Availability of our C++ SDK — now available as a supported, stand-alone SDK, this SDK is also the core of our Node.js, PHP, Python, and Ruby SDKs.

**SDK API 3.5**: Introduced support for Vector Search alongside Server 7.6 (and Capella). Adds scoped indexes to Search (for Vector Seach and traditional FTS). Read from Replica for Query and Sub-Doc operations. KV Range Scan for querying documents through the Data Service, even if you don't know the document IDs (for use cases that require relatively low concurrency and tolerate relatively high latency). Transactions now implemented as a native library in all SDKs (except libcouchbase).

**SDK API 3.4**: Introduced support for ARM v8 on Ubuntu 20.04, Transactions on Spring Data Couchbase, and compatibility with running in serverless environments, such as AWS λ. The `couchbase2://` connection string was introduced in Go 2.7, Java 3.5, Kotlin 1.2, and Scala 1.5, for Cloud Native Gateway with [Couchbase Autonomous Operator](../../../operator/current/overview.md) (from CAO 2.6.1).

**SDK API 3.3**: Introduced alongside Couchbase Server 7.1, adds Management API for Eventing and Index Management for Scopes & Collections; extends Bucket Management API to support Custom Conflict Resolution and Storage Options; adds new platform support for Linux Alpine OS, Apple M1, and AWS Graviton2; provides improved error messages for better error handling; and an upgraded Spark Connector that runs on Spark 3.0 & 3.1 Platform.

**SDK API 3.2**: Introduced alongside Couchbase Server 7.0, provides features in support of Scopes and Collections, extends capabilities around Open Telemetry API to instrument telemetry data, enhanced client side field level encryption to add an additional layer of security to protect sensitive data, adds new platform support such as Ubuntu 20.04 LTS.

**SDK API 3.1**: Introduced alongside Couchbase Server 6.6, focuses on Bucket Management API, adds capabilities around Full Text Search features such-as Geo-Polygon support, Flex Index, and Scoring.

**SDK API 3.0**: Introduced alongside Couchbase Server 6.5, is a major overhaul from its predecessor, has simplified surface area, removed long-standing bugs and deprecated/removed old API, introduces new programming languages Scala and Ruby, written in anticipation to support Scopes and Collections.

## [](#sdk-api-stability)SDK API Stability

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