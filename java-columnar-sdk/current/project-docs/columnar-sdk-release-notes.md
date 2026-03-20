---
title: Columnar SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Capella Columnar Java Client.
editUrl: https://github.com/couchbase/docs-columnar-sdk-java/edit/release/1.0/modules/project-docs/pages/columnar-sdk-release-notes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:java-columnar-sdk:project-docs:columnar-sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-columnar-sdk/current/project-docs/columnar-sdk-release-notes.html)

# Columnar SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Capella Columnar Java Client. 

Version 1.0 of the Java columnar SDK implements the 1.0 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Capella columnar.

## [](#installation)Installation

See the [Maven Coordinates](sdk-full-installation.md) guide for details.

## [](#latest-release)Java Columnar SDK 1.0 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#v1.0.7)Version 1.0.7 (07 January 2025)

Regular maintenance release to update dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.7/com.couchbase.columnar.client.java/module-summary.html)

#### [](#improvements)Improvements

* [JCO-24](https://jira.issues.couchbase.com/browse/JCO-24): The SDK is now annotated with [JSpecify](https://jspecify.dev) nullability annotations, so compatible IDEs and tools can warn about potential null pointer exceptions.

### [](#v1.0.6)Version 1.0.6 (05 December 2024)

Regular maintenance release to update dependency versions.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.6/com.couchbase.columnar.client.java/module-summary.html)

### [](#v1.0.5)Version 1.0.5 (06 November 2024)

This regular maintenance release updates dependency versions, and picks up bug fixes from the Couchbase `core-io` library.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.5/com.couchbase.columnar.client.java/module-summary.html)

#### [](#bug-fixes)Bug Fixes

* [JVMCBC-1577](https://jira.issues.couchbase.com/browse/JVMCBC-1577): Sometimes a request made shortly after calling `Cluster.newInstance()` would fail with a message that said the service is not available in the cluster, even if the service was actually available. This no longer happens.

### [](#v1.0.0)Version 1.0.0 (11 October 2024)

This is the first General Availability (GA) release of the new Couchbase Columnar Java SDK. It supports executing queries against Capella Columnar clusters, with additional features planned for future releases.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.0/com.couchbase.columnar.client.java/module-summary.html)