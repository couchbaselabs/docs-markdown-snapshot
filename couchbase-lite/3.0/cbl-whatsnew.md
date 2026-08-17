---
title: What&#8217;s New
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/ROOT/pages/cbl-whatsnew.adoc
  xref: xref:3.0@couchbase-lite::cbl-whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/cbl-whatsnew.html)

# What&#8217;s New

> [!NOTE]
> Couchbase Lite 3.0 introduces some breaking changes.  
> If you are upgrading from 2.x, please refer to the appropriate upgrade page — see: [Upgrading](#lbl-upgrade)

## [](#release-3-0-february-2022)Release 3.0 (February 2022)

Couchbase Lite Release 3.0 introduces enhanced platform support with the introduction of:

* Couchbase Lite for C — extending your apps beyond mobile to the IoT application space
* Couchbase Lite for Android now offers a new, fully supported, out-of-the-box, idiomatic api for Kotlin
* SQL++ for Mobile (also referred to as N1QL) --supporting the emerging SQL for JSON technology, SQL++.

### [](#new-features)New Features

#### [](#couchbase-lite-for-c)Couchbase Lite for C

_Couchbase Lite_ now has an officially supported **C API**, which builds on the success of the well-received engineering labs _C API for Couchbase Lite_.

The C API now includes support for Enterprise-grade features like database encryption. This optimized implementation is ensured feature parity with our other Couchbase Lite platforms and is supported on a wide-range of mobile and desktop platforms — see: [Supported Platforms](c/supported-os.md).

The ease of building language bindings on top of the C API means application developers can build for edge and embedded IoT devices using their preferred languages to harness the power of Couchbase Lite.

Read More . . . [Couchbase Lite for C](c/quickstart.md)

#### [](#kotlin-support-in-android)Kotlin Support in Android

_Couchbase Lite for Android_ delivers an idiomatic Kotlin API out-of-the-box. This enables seamless integration with Android apps developed in Kotlin without the need for custom extensions.

Kotlin developers can now build apps using [common Kotlin Patterns](https://developer.android.com/kotlin/common-patterns) and use familiar Kotlin features such as:

* Nullability annotations
* Named parameters
* Kotlin Flows

Java support and functionality continues for Android. You can choose whether to use the Kotlin extensions API or continue using the Java api.

Read More . . . [Couchbase Lite for Kotlin](android/kotlin.md)

#### [](#sqln1ql-query-strings)SQL++/N1QL Query Strings

Couchbase Lite's SQL++ for Mobile query API vastly simplifies the integration of Couchbase Lite within hybrid/cross platform apps.

N1QL for Mobile is an implementation of the emerging SQL-for-JSON query language specification (SQL++). It provides native, hybrid and cross-platform mobile app developers with a consistent, convenient and flexible interface to query JSON documents within the embedded database using a SQL-based syntax. This means developers can reuse queries across platforms, reducing development, testing and maintenance costs.

Read More . . . [Swift](swift/query-n1ql-mobile.md) | [Objective-C](objc/query-n1ql-mobile.md) | [Java](java/query-n1ql-mobile.md) | [Android](android/query-n1ql-mobile.md) | [.Net](csharp/query-n1ql-mobile.md) | [C](c/query-n1ql-mobile.md)

### [](#other-changes)Other Changes

Release Notes

[Swift](swift/releasenotes.md) | [Objective-C](objc/releasenotes.md) | [Java](java/releasenotes.md) | [Android](android/releasenotes.md) | [.Net](csharp/releasenotes.md) | [C](c/releasenotes.md)

### [](#lbl-upgrade)Upgrading

Related Couchbase Lite content

[Android](android/upgrade.md) | [C#](csharp/upgrade.md) | [Java](java/upgrade.md) | [Objective-C](objc/upgrade.md) | [Swift](swift/upgrade.md)

## [](#maintenance-releases)Maintenance Releases

### [](#3-0-1-march-2022)3.0.1 (March 2022)

Couchbase Lite Release 3.0.1 introduces fixes and enhancements for:  
[C](c/releasenotes.md)| [Objective-C](objc/releasenotes.md)| [Swift](swift/releasenotes.md)

### [](#3-0-2-august-2022)3.0.2 (August 2022)

Couchbase Lite Release 3.0.2 introduces fixes and enhancements for:  
[Android](android/releasenotes.md#maint-3-0-2)| [C](c/releasenotes.md#maint-3-0-2)| [C#](csharp/releasenotes.md#maint-3-0-2)| [Java](java/releasenotes.md#maint-3-0-2)| [Objective-C](objc/releasenotes.md#maint-3-0-2)| [Swift](swift/releasenotes.md#maint-3-0-2)