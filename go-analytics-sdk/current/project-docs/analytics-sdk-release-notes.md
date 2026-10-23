---
title: Enterprise Analytics SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Go Analytics Client for Operational Insights.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Go Analytics SDK
    version: "1.1"
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-go/edit/release/1.1/modules/project-docs/pages/analytics-sdk-release-notes.adoc
  xref: xref:go-analytics-sdk:project-docs:analytics-sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-analytics-sdk/current/project-docs/analytics-sdk-release-notes.html)

# Enterprise Analytics SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Go Analytics Client for Operational Insights. 

Version 1.1 of the Go Analytics SDK implements the 1.1 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Operational Insights.

## [](#installation)Installation

See the [Full Installation](sdk-full-installation.md) guide for details.

## [](#latest-release)Go Analytics SDK 1.1 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#v1.1.1)Version 1.1.1 (21 October 2026)

#### [](#new-features-and-behavioral-changes)New Features and Behavioral Changes

* [GOCO-58](https://jira.issues.couchbase.com/browse/GOCO-58): The SDK's HTTP client now rejects all redirects and fast-fails instead.

#### [](#fixed-issues)Fixed Issues

* [GOCO-59](https://jira.issues.couchbase.com/browse/GOCO-59): Fixed an issue where request URLs for IPv6 hosts were built without surrounding the address in square brackets (e.g. `::1:55908` instead of `[::1]:55908`). This caused connections to fail when the application's `go.mod` declared Go 1.26 or newer, since `urlstrictcolons=1` is the default from Go 1.26 (see [Go 1.26 GODEBUG settings](https://go.dev/doc/godebug#go-126)).

### [](#v1.1.0)Version 1.1.0 (26 June 2026)

This is the first release of the 1.1 Analytics Go SDK dotminor.

The 1.1 Analytics SDKs add support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results, eliminating the need for long-running server connections (compatible with Couchbase Enterprise Analytics Server 2.2 — now known as Operational Insights Enterprise 2.2).

## [](#go-analytics-sdk-1-0-releases)Go Analytics SDK 1.0 Releases

### [](#v1.0.0)Version 1.0.0 (10 July 2025)

This is the first General Availability (GA) release of the new Analytics Go SDK. It supports executing queries against Operational Insights (formerly known as Enterprise Analytics) clusters, with additional features planned for future releases.

[API Reference](https://pkg.go.dev/github.com/couchbase/gocbanalytics)