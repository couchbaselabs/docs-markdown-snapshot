---
title: Compatibility Guide
description: Quarkus Couchbase 1.1 needs Quarkus 3.20 or newer.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-quarkus-extension/edit/release/1.3/modules/ROOT/pages/compatibility.adoc
  xref: xref:1.3@quarkus-extension::compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/quarkus-extension/1.3/compatibility.html)

# Compatibility Guide

Each Quarkus Couchbase release is built for a specific Quarkus and Couchbase Java SDK version, and the version is preset for you (see the [release notes](release-notes.md)):

__Compatibility Matrix__
| Quarkus Couchbase | 1.0.0  | 1.1.0  | 1.2.0  | 1.3.0  |
| ----------------- | ------ | ------ | ------ | ------ |
| Java SDK          | 3.7.7  | 3.8.0  | 3.9.2  | 3.10.1 |
| Quarkus version   | 3.17.5 | 3.20.0 | 3.28.4 | 3.32.1 |

## [](#platform-compatibility)Platform Compatibility

Quarkus Couchbase requires JDK 17 or newer. See the [JDK Version Compatibility listing](../../java-sdk/current/project-docs/compatibility.md#jdk-version-compatibility) in the Java SDK docs for specific LTS implementations supported.

See the [Java SDK Compatibility Guide](../../java-sdk/current/project-docs/compatibility.md) for wider compatibility of the Java SDK. We recommend using SDKMAN to manage versions of JVM and associated tools during development.