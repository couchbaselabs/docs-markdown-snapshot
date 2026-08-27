---
title: Columnar SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Capella Columnar Node.js Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-columnar-sdk-nodejs/edit/release/1.0/modules/project-docs/pages/columnar-sdk-release-notes.adoc
  xref: xref:nodejs-columnar-sdk:project-docs:columnar-sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-columnar-sdk/current/project-docs/columnar-sdk-release-notes.html)

# Columnar SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Capella Columnar Node.js Client. 

Version 1.0 of the Node.js Columnar SDK implements the 1.0 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Capella columnar.

## [](#installation)Installation

See the [Full Installation](sdk-full-installation.md) guide for details.

## [](#latest-release)Node.js Columnar SDK 1.0 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-1-0-1-10-october-2025)Version 1.0.1 (10 October 2025)

Version 1.0.1 is the next patch release of the first generation Couchbase Columnar Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase-columnar@1.0.1
```

**API Docs:** <https://docs.couchbase.com/sdk-api/columnar-nodejs-client-1.0.1/>

#### [](#enhancements)Enhancements

* [JSCO-55](https://jira.issues.couchbase.com/browse/JSCO-55): Added support for Node.js 22.
* [JSCO-56](https://jira.issues.couchbase.com/browse/JSCO-56): Added support for Node.js 24.
* [JSCO-58](https://jira.issues.couchbase.com/browse/JSCO-58): Added support for building binary with sanitzers.
* [JSCO-60](https://jira.issues.couchbase.com/browse/JSCO-60): Updated SDK to more recent C++ core.

#### [](#fixes)Fixes

* [JSCO-61](https://jira.issues.couchbase.com/browse/JSCO-61): The internal `OperationCanceledError` is no longer raised. Instead, `ColumnarError` is raised.

#### [](#known-issues)Known Issues

* [JSCO-36](https://jira.issues.couchbase.com/browse/JSCO-36): Logging hooks are not yet implemented.

### [](#version-1-0-0-11-october-2024)Version 1.0.0 (11 October 2024)

This is the first General Availability (GA) release of the new Couchbase Columnar Node.js SDK. It supports executing queries against Capella Columnar clusters, with additional features planned for future releases.

[API Reference](https://docs.couchbase.com/sdk-api/columnar-nodejs-client-1.0.0)

#### [](#known-issues-2)Known Issues

* [JSCO-36](https://jira.issues.couchbase.com/browse/JSCO-36): Logging hooks are not yet implemented.