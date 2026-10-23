---
title: Operational Insights SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Go Operational Insights Client.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Go Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-go/edit/release/1.0/modules/project-docs/pages/operational-insights-sdk-release-notes.adoc
  xref: xref:go-operational-insights-sdk:project-docs:operational-insights-sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-operational-insights-sdk/current/project-docs/operational-insights-sdk-release-notes.html)

# Operational Insights SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Go Operational Insights Client. 

Version 1.0 of the Go Operational Insights SDK implements the 1.0 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md) for more information on feature compatibility with different versions of Operational Insights.

## [](#installation)Installation

See the [Full Installation](sdk-full-installation.md) guide for details.

## [](#latest-release)Go Operational Insights SDK 1.0 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#v1.0.1)Version 1.0.1 (20 October 2026)

#### [](#new-features-and-behavioral-changes)New Features and Behavioral Changes

* [GOCO-58](https://jira.issues.couchbase.com/browse/GOCO-58): The SDK's HTTP client now rejects all redirects and fast-fails instead.

#### [](#fixed-issues)Fixed Issues

* [GOCO-59](https://jira.issues.couchbase.com/browse/GOCO-59): Fixed an issue where request URLs for IPv6 hosts were built without surrounding the address in square brackets (e.g. `::1:55908` instead of `[::1]:55908`). This caused connections to fail when the application's `go.mod` declared Go 1.26 or newer, since `urlstrictcolons=1` is the default from Go 1.26 (see [Go 1.26 GODEBUG settings](https://go.dev/doc/godebug#go-126)).

### [](#v1.0.0)Version 1.0.0 (15 October 2026)

[API Reference](https://pkg.go.dev/github.com/couchbase/gocbinsights)

This is the first General Availability (GA) release of the new Operational Insights Go SDK.

## [](#previous-sdks)Previous SDKs

See the [Analytics SDK release notes](../../../go-analytics-sdk/current/project-docs/analytics-sdk-release-notes.md) for earlier developments.