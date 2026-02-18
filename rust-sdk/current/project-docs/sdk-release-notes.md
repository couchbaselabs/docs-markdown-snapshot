---
title: SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Couchbase Rust Client.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/rust-sdk/current/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Couchbase Rust Client. 

> [!IMPORTANT]
> Developer Preview
> 
> This SDK is a Developer Preview, providing early access before the generally available (GA) release is ready. It enables you to play with the APIs to get a sense of how they work. Preview Mode features and their use are subject to Couchbase’s “Non-GA Offering Supplemental Terms” set forth in the [License Agreement](https://www.couchbase.com/LA08242020). Preview Mode features may not be functionally complete and are not intended for production use. They are intended for development and testing purposes only.

Version 1.0 of the Rust SDK implements the 3.8 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

## [](#installation)Installation

* The Couchbase Rust SDK 1.0 Client supports Rust 1.90+.

More details of the installation process are in the [full installation guide](sdk-full-installation.md). In most cases, given the above prerequisites, it’s a simple matter of the following:

```none
cargo add couchbase
```

### [](#verifying-artifacts)Verifying Artifacts

Starting with version 3.8.2, Couchbase JVM SDK artifacts are signed with [this GPG key](../../../java-sdk/current/project-docs/%5Fattachments/gpg-keys/181C7A4E908890A2D768365742BDEBD30D10C992.asc).

Fingerprint

```none
CB SDK Robot <cb-sdk-robot@couchbase.com>
181C 7A4E 9088 90A2 D768  3657 42BD EBD3 0D10 C992
```

## [](#latest-release)Rust SDK 1.0 Releases

Version 1.0 of the Rust SDK implements the 3.8 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

Binary compatibility is not guaranteed for any Rust SDK release, and you should rebuild your application when changing the SDK.