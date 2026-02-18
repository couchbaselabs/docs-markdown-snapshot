---
title: Columnar SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Capella Columnar Python Client.
editUrl: https://github.com/couchbase/docs-columnar-sdk-python/edit/release/1.0/modules/project-docs/pages/columnar-sdk-release-notes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/python-columnar-sdk/current/project-docs/columnar-sdk-release-notes.html)

# Columnar SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Capella Columnar Python Client. 

Version 1.0 of the Java columnar SDK implements the 1.0 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Capella columnar.

## [](#installation)Installation

See the [Full Installation](sdk-full-installation.md) guide for details.

## [](#latest-release)Python Columnar SDK 1.0 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-1-0-1-10-october-2025)Version 1.0.1 (10 October 2025)

Version 1.0.1 is the next patch release of the first generation Couchbase Columnar Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase-columnar==1.0.1
```

**API Docs:** <https://docs.couchbase.com/sdk-api/columnar-python-client-1.0.1/>

#### [](#enhancements)Enhancements

* [PYCO-42](https://jira.issues.couchbase.com/browse/PYCO-42): Added support for Python 3.13.
* [PYCO-86](https://jira.issues.couchbase.com/browse/PYCO-86): Updated SDK to more recent C++ core.
* [PYCO-88](https://jira.issues.couchbase.com/browse/PYCO-88): Stopped publishing wheel for EOL Python 3.8.
* [PYCO-90](https://jira.issues.couchbase.com/browse/PYCO-90): Improved `ColumnarError` `_repr_()`.

#### [](#fixes)Fixes

* [PYCO-44](https://jira.issues.couchbase.com/browse/PYCO-44), [PYCO-84](https://jira.issues.couchbase.com/browse/PYCO-84): Fixed dispatch timer to cancel after request has been successfully sent to server.
* [PYCO-83](https://jira.issues.couchbase.com/browse/PYCO-83), [PYCO-85](https://jira.issues.couchbase.com/browse/PYCO-85): Fixed potential crash during scaling scenarios.
* [PYCO-89](https://jira.issues.couchbase.com/browse/PYCO-89): The internal `QueryOperationCanceledError` is no longer raised. Instead, `ColumnarError` is raised.

### [](#version-1-0-0-11-october-2024)Version 1.0.0 (11 October 2024)

This is the first General Availability (GA) release of the new Couchbase Columnar Python SDK. It supports executing queries against Capella Columnar clusters, with additional features planned for future releases.

[API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client-1.0.0/)