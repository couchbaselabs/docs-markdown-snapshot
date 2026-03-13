---
title: SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Couchbase Rust Client.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-03-13T03:41:17.220Z
link: xref:rust-sdk:project-docs:sdk-release-notes.adoc[]
---

[View original HTML](/rust-sdk/current/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Couchbase Rust Client. 

Version 1.0 of the Rust SDK implements the 3.9 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

## [](#installation)Installation

* The Couchbase Rust SDK 1.0 Client supports Rust 1.90+.

More details of the installation process are in the [full installation guide](sdk-full-installation.md). In most cases, given the above prerequisites, it’s a simple matter of the following:

```none
cargo add couchbase
```

## [](#latest-release)Rust SDK 1.0 Releases

Version 1.0 of the Rust SDK implements the 3.9 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

Binary compatibility is not guaranteed for any Rust SDK release, and you should rebuild your application when changing the SDK.

### [](#version-1-0-0-12-march-2026)Version 1.0.0 (12 March 2026)

Initial GA release.