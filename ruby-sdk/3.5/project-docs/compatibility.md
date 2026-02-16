[View original HTML](/ruby-sdk/3.5/project-docs/compatibility.html)

> Platform compatibility, and features available in different SDK versions, and compatibility between Server and SDK. Plus notes on Cloud, networks, and AWS Lambda. 

The Couchbase Ruby SDK supports MRI Ruby versions 3.0, 3.1, 3.2, and 3.3 — see the table below for [supported versions and dates](#ruby-version-compatibility).

## [](#platform-compatibility)Platform Compatibility

### [](#ruby-version-compatibility)Ruby Version Compatibility

The Couchbase Ruby SDK aims to support [all supported versions](https://www.ruby-lang.org/en/downloads/branches/) of Ruby. The table below indicates the Ruby SDK version where support of a version of Ruby was added. Ruby versions that have reached their [End-of-Life date](https://www.ruby-lang.org/en/downloads/branches/) are not supported.

__Supported Ruby Versions__
| Ruby Version | Support EOL                      | Couchbase SDK Versions Supported |
| ------------ | -------------------------------- | -------------------------------- |
| 3.0          | until 2024-03-31                 | from 3.1.0                       |
| 3.1          | until 2025-03-31                 | from 3.3.0                       |
| 3.2          | until 2026-03-31                 | from 3.4.0                       |
| 3.3          | until 2026-03-31 (expected, TBC) | from 3.5.0                       |

### [](#os-compatibility)OS Compatibility

In general, the SDK can be expected to run on all of the Operating Systems supported by [Couchbase Server](../../../server/7.6/install/install-platforms.md).

However, the Ruby SDK is tested and supported specifically on the following OSs and platforms:

### GNU/Linux

* Amazon Linux 2 & AL2023.
* Red Hat Enterprise Linux 8 & 9;
* Oracle Linux 8 & 9.
* Ubuntu (LTS) 20.04 (_Focal_) & 22.04 (_Jammy_).
* Debian 10 (_Buster_), 11 (_Bullseye_), and Debian 12 (_Bookworm_).
* SUSE Enterprise Linux 12 & 15.
* Alpine Linux 3.18.

### Microsoft Windows

* Microsoft Windows 10 & 11;
* Windows Server 2019 & 2022.

### Mac OS X

The current and previous two releases of OS X. At time of writing (March 2024): 14 (Sonoma), 13 (Ventura), and 12 (Monterey). M1 ARM architecture is fully supported in the Ruby SDK.

### ARM Processor Support

AWS Amazon Graviton2, Apple M1 ARM processors, and ARMv8 on Ubuntu 20.04+ (from SDK 3.4).

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$network-requirements.adoc\[\]

## [](#couchbase-server-compatibility)Couchbase Server Compatibility

Couchbase SDKs are tested against a variety of different environments to ensure both backward and forward compatibility with different versions of Couchbase Server.

### [](#couchbase-versionsdk-version-matrix)Couchbase Version/SDK Version Matrix

The matrix below denotes the version of Couchbase Server, the version of the Ruby SDK and whether the SDK is:

* ✖ **Unsupported**: This combination is not tested, and is not within the scope of technical support if you have purchased a support agreement.
* ◎ **Compatible**: This combination has been tested previously, and should be compatible. This combination is not recommended by our technical support organization. It is best to upgrade either the SDK or the Couchbase version you are using.
* ✔ **Supported**: This combination is subject to ongoing quality assurance, and is fully supported by our technical support organization.

__Recommended SDK per Server Version Matrix__
|                      | 3.2 - 3.4 | 3.5   |
| -------------------- | --------- | ----- |
| **Server 7.0 - 7.2** | **✔**     | **✔** |
| **Server 7.6**       | **✔**     | **✔** |

Note the [End of Life dates](https://www.couchbase.com/support-policy) for Couchbase Server and SDK versions. See the notes there for Support details.

### [](#capella-compatibility)Capella Compatibility

The Couchbase Ruby SDK is fully compatible with Couchbase Capella, our fully-hosted database-as-a-service. To make development easier, the SDK includes the Capella client certificate ready installed.

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$capella.adoc\[\]

### [](#couchbase-new-feature-availability-matrix)Couchbase New Feature Availability Matrix

__Couchbase Server and SDK Supported Version Matrix__
|                                                                      | Server 7.0 & 7.1  | Server 7.2     | Server 7.6 |
| -------------------------------------------------------------------- | ----------------- | -------------- | ---------- |
| Enhanced Durability                                                  | All SDK versions  |                |            |
| Durable Writes                                                       | Since 3.0         |                |            |
| Analytics                                                            | Since 2.6         |                |            |
| Collections                                                          | Since 3.0.3       |                |            |
| Scope-Level SQL++ (formerly N1QL) Queries & all Collections features | Since SDK 3.2.0   |                |            |
| Request Tracing                                                      | Since SDK 3.2.0   |                |            |
| Distributed ACID Transactions                                        | Not Yet Supported |                |            |
| Cloud Native Gateway                                                 | Not Yet Supported |                |            |
| Vector Search                                                        | N/A               | From SDK 3.5.0 |            |

### [](#api-version)API Version

This release of the SDK is written to version 3.5 of the SDK API specification (and matching the features available in Couchbase 7.6 and earlier). For most developers, just using the latest version will be all that matters, and few will need to look at another of our SDKs. Just for those few that do, the table below shows each Couchbase SDK release version that matches the API version (and a table that covers the earliest versions of the 3.x SDK API can be found in documentation for earlier versions of the SDK).

Whilst these two numbers match for the .NET SDK, this is not the case for the others, as version numbers for individual SDKs are bumped up in line with [Semantic Versioning](https://semver.org/) — check the [release notes](#sdk-release-notes) of each SDK for individual details.

__SDK API Versions__
|                                                                    | API 3.2   | API 3.3       | API 3.4   | API 3.5 | API 3.6 |
| ------------------------------------------------------------------ | --------- | ------------- | --------- | ------- | ------- |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)        | 3.2       | 3.3           | 3.4       | 3.5     | 3.6     |
| [C (libcouchbase)](../../../c-sdk/current/hello-world/overview.md) | 3.2       | 3.3.0 - 3.3.2 | 3.3.3 ①   | N/A ②   | N/A ②   |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)            | \-        | \-            | \-        | \-      | 1.0     |
| [Go](../../../go-sdk/current/hello-world/overview.md)              | 2.3 & 2.4 | 2.5           | 2.6 & 2.7 | 2.8     | 2.9     |
| [Java](../../../java-sdk/current/hello-world/overview.md)          | 3.2       | 3.3           | 3.4 & 3.5 | 3.6     | 3.7     |
| [Kotlin](../../../kotlin-sdk/current/hello-world/overview.md)      | \-        | 1.0           | 1.1 & 1.2 | 1.3     | 1.4     |
| [Node.js](../../../nodejs-sdk/current/hello-world/overview.md)     | 3.2 & 4.0 | 4.1           | 4.2       | 4.3     | 4.4     |
| [PHP](../../../php-sdk/current/hello-world/overview.md)            | 3.2       | 4.0           | 4.1       | 4.2     | 4.2.2   |
| [Python](../../../python-sdk/current/hello-world/overview.md)      | 3.2       | 4.0           | 4.1       | 4.2     | 4.3     |
| [Ruby](../../current/hello-world/overview.md)                      | 3.2       | 3.3           | 3.4       | 3.5     | 3.5.2   |
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

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$interface-stability-pars.adoc\[\]

### [](#older-sdk-versions)Older SDK Versions

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$archive.adoc\[\]