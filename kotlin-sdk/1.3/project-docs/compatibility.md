---
title: Compatibility
description: Platform compatibility, and features available in different SDK
  versions, and compatibility between Server and SDK. Plus notes on Cloud,
  networks, and AWS Lambda.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.3/modules/project-docs/pages/compatibility.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.3@kotlin-sdk:project-docs:compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.3/project-docs/compatibility.html)

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

The current and previous two releases of OS X. At time of writing (March 2024): 14 (Sonoma), 13 (Ventura), and 12 (Monterey). M1 ARM architecture is fully supported in the Scala SDK.

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

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$network-requirements.adoc\[\]

## [](#couchbase-server-compatibility)Couchbase Server Compatibility

Couchbase SDKs are tested against a variety of different environments to ensure both backward and forward compatibility with different versions of Couchbase Server.

### [](#couchbase-versionsdk-version-matrix)Couchbase Version/SDK Version Matrix

The matrix below denotes the version of Couchbase Server, the version of the Scala SDK and whether the SDK is:

* ✖ **Unsupported**: This combination is not tested, and is not within the scope of technical support if you have purchased a support agreement.
* ◎ **Compatible**: This combination has been tested previously, and should be compatible. This combination is not recommended by our technical support organization. It is best to upgrade either the SDK or the Couchbase version you are using.
* ✔ **Supported**: This combination is subject to ongoing quality assurance, and is fully supported by our technical support organization.

__Recommended SDK per Server Version Matrix__
|                      | 1.0   | 1.1, 1.2 | 1.3   |
| -------------------- | ----- | -------- | ----- |
| **Server 7.0 - 7.2** | **✔** | **✔**    | **✔** |
| **Server 7.6**       | **✔** | **✔**    | **✔** |

Note the [End of Life dates](https://www.couchbase.com/support-policy) for Couchbase Server and SDK versions. See the notes there for Support details.

### [](#capella-compatibility)Capella Compatibility

The Couchbase Scala SDK is fully compatible with Couchbase Capella, our fully-hosted database-as-a-service. To make development easier, the SDK includes the Capella client certificate ready installed.

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$capella.adoc\[\]

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
| Vector Search                                                        | N/A              | From SDK 1.3.0                                                                                      |            |

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

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$api-version.adoc\[\]

## [](#sdk-api-stability)SDK API Stability

### [](#interface-stability)Interface Stability

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$interface-stability-pars.adoc\[\]

### [](#older-sdk-versions)Older SDK Versions

Unresolved include directive in modules/project-docs/pages/compatibility.adoc - include::7.5@sdk:shared:partial$archive.adoc\[\]