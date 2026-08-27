---
title: Analytics SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Enterprise Analytics Python Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.1/modules/project-docs/pages/analytics-sdk-release-notes.adoc
  xref: xref:python-analytics-sdk:project-docs:analytics-sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-analytics-sdk/current/project-docs/analytics-sdk-release-notes.html)

# Analytics SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Enterprise Analytics Python Client. 

Version 1.1 of the Python Analytics SDK implements the 1.1 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Enterprise Analytics.

## [](#installation)Installation

See the [Full Installation](sdk-full-installation.md) guide for details.

## [](#latest-release)Python Analytics SDK 1.1 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#v1.1.0)Version 1.1.0 (26 June 2026)

This is the first release of the 1.1 series Analytics Python SDK.

The 1.1 Analytics SDKs add support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results, eliminating the need for long-running server connections (compatible with Couchbase Enterprise Analytics Server 2.2).

[API Reference](https://docs.couchbase.com/sdk-api/analytics-python-client-1.1.0/)

## [](#python-analytics-sdk-1-0-releases)Python Analytics SDK 1.0 Releases

### [](#v1.0.0)Version 1.0.0 (12 August 2025)

This is the first General Availability (GA) release of the new Analytics Python SDK. It supports executing queries against Enterprise Analytics clusters, with additional features planned for future releases.

[API Reference](https://docs.couchbase.com/sdk-api/analytics-python-client-1.0.0/)