---
title: Compatibility Guide
description: Quarkus Couchbase 1.1 needs Quarkus 3.20 or newer.
editUrl: https://github.com/couchbase/docs-quarkus-extension/edit/release/1.1/modules/ROOT/pages/compatibility.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.1@quarkus-extension::compatibility.adoc[]
---

[View original HTML](/quarkus-extension/1.1/compatibility.html)

# Compatibility Guide

Each Quarkus Couchbase release is built for a specific Couchbase Java SDK version, and the version is preset for you (see the [release notes](release-notes.md)):

__Table 1\. Compatibility Matrix__
| Quarkus Couchbase | 1.0.0 | 1.1.0 |
| ----------------- | ----- | ----- |
| Java SDK          | 3.7.7 | 3.8.0 |
| Quarkus version   | 3.15+ | 3.20+ |

## [](#platform-compatibility)Platform Compatibility

Quarkus Couchbase requires JDK 17 or newer. See the [JDK Version Compatibility listing](../../java-sdk/current/project-docs/compatibility.md#jdk-version-compatibility) in the Java SDK docs for specific LTS implementations supported.

See the [Java SDK Compatibility Guide](../../java-sdk/current/project-docs/compatibility.md) for wider compatibility of the Java SDK. We recommend using SDKMAN to manage versions of JVM and associated tools during development.