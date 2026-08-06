---
title: Analytics SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Enterprise Analytics Java Client.
editUrl: https://github.com/couchbase/docs-analytics-sdk-java/edit/release/1.1/modules/project-docs/pages/analytics-sdk-release-notes.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:java-analytics-sdk:project-docs:analytics-sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-analytics-sdk/current/project-docs/analytics-sdk-release-notes.html)

# Analytics SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Enterprise Analytics Java Client. 

Version 1.1 of the Java Analytics SDK implements the 1.1 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Enterprise Analytics.

## [](#installation)Installation

See the [Maven Coordinates](sdk-full-installation.md) guide for details.

## [](#latest-release)Java Analytics SDK 1.1 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#v1.1.0)Version 1.1.0 (26 June 2026)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-analytics-java-client-1.0.0)

This is the first release of the 1.1 Analytics Java SDK dotminor.

The 1.1 Analytics SDKs add support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results, eliminating the need for long-running server connections (compatible with Couchbase Enterprise Analytics Server 2.2).

## [](#java-analytics-sdk-1-0-releases)Java Analytics SDK 1.0 Releases

### [](#v1.0.0)Version 1.0.0 (10 July 2025)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-analytics-java-client-1.0.0)

This is the first General Availability (GA) release of the new Analytics Java SDK. It supports executing queries against Enterprise Analytics clusters, with additional features planned for future releases.