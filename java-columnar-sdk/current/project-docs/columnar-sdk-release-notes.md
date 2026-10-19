---
title: Columnar SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Capella Columnar Java Client for Operational Insights
  (Capella).
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Java Columnar SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-columnar-sdk-java/edit/release/1.0/modules/project-docs/pages/columnar-sdk-release-notes.adoc
  xref: xref:java-columnar-sdk:project-docs:columnar-sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-columnar-sdk/current/project-docs/columnar-sdk-release-notes.html)

# Columnar SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Capella Columnar Java Client for Operational Insights (Capella). 

Version 1.0 of the Java columnar SDK implements the 1.0 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Operational Insights (Capella).

## [](#installation)Installation

See the [Maven Coordinates](sdk-full-installation.md) guide for details.

> [!NOTE]
> Version Number Bumps
> 
> From 3.9.0 on, all Couchbase JVM SDKs have an aligned version number to make it easier to users to track changes, including the Columnar SDKs. So the version jumped from 1.1.x to 3.9.x. While this is technically an increase in the major, all functionality works unchanged and users can upgrade existing applications without issue.
> 
> These subsequent releases are regular maintenance release to update dependency versions. The API references can be found here:
> 
> [1.0.0](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.0/com.couchbase.columnar.client.java/module-summary.html)| [1.0.1](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.1/com.couchbase.columnar.client.java/module-summary.html)| [1.0.2](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.2/com.couchbase.columnar.client.java/module-summary.html)| [1.0.3](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.3/com.couchbase.columnar.client.java/module-summary.html)| [1.0.4](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.4/com.couchbase.columnar.client.java/module-summary.html)| [1.0.5](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.5/com.couchbase.columnar.client.java/module-summary.html)| [1.0.6](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.6/com.couchbase.columnar.client.java/module-summary.html)| [1.0.7](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.7/com.couchbase.columnar.client.java/module-summary.html)| [1.0.8](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.8/com.couchbase.columnar.client.java/module-summary.html)| [1.0.9](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.9/com.couchbase.columnar.client.java/module-summary.html)| [3.9.0](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.9.0/com.couchbase.columnar.client.java/module-summary.html)| [3.9.1](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.9.1/com.couchbase.columnar.client.java/module-summary.html)| [3.9.2](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.9.2/com.couchbase.columnar.client.java/module-summary.html)| [3.9.3](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.9.3/com.couchbase.columnar.client.java/module-summary.html)| [3.10.0](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.10.0/com.couchbase.columnar.client.java/module-summary.html)| [3.10.1](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.10.1/com.couchbase.columnar.client.java/module-summary.html)| [3.11.0](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.11.0/com.couchbase.columnar.client.java/module-summary.html)| [3.11.1](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.11.1/com.couchbase.columnar.client.java/module-summary.html)| [3.12.0](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.12.0/com.couchbase.columnar.client.java/module-summary.html)| [3.12.1](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.12.1/com.couchbase.columnar.client.java/module-summary.html)| [3.12.2](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.12.2/com.couchbase.columnar.client.java/module-summary.html)| [3.12.3](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.12.3/com.couchbase.columnar.client.java/module-summary.html)| [3.13.0](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-3.13.0/com.couchbase.columnar.client.java/module-summary.html)

## [](#latest-release)Java Columnar SDK Releases

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

This is the first General Availability (GA) release of the new Couchbase Columnar Java SDK. It supports executing queries against Operational Insights (Capella) clusters, with additional features planned for future releases.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client-1.0.0/com.couchbase.columnar.client.java/module-summary.html)