---
title: SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Couchbase Rust Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/project-docs/pages/sdk-release-notes.adoc
  xref: xref:rust-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Couchbase Rust Client. 

Version 1.0 of the Rust SDK implements the 3.9 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

## [](#installation)Installation

* The Couchbase Rust SDK 1.0 Client supports Rust 1.90+.

More details of the installation process are in the [full installation guide](sdk-full-installation.md). In most cases, given the above prerequisites, it's a simple matter of the following:

```none
cargo add couchbase
```

## [](#latest-release)Rust SDK 1.0 Releases

Version 1.0 of the Rust SDK implements the 3.9 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

Binary compatibility is not guaranteed for any Rust SDK release, and you should rebuild your application when changing the SDK.

### [](#version-1-0-2-11-august-2026)Version 1.0.2 (11 August 2026)

Version 1.0.2 is a maintenance release for the Rust SDK 1.0.

[API Documentation](https://docs.rs/couchbase/1.0.2/couchbase/)

#### [](#new-features-and-behavioral-changes)New Features and Behavioral Changes

* [RSCBC-282](https://jira.issues.couchbase.com/browse/RSCBC-282): Updated key-value error messages to include the underlying cause of the error, giving more context to warnings such as `failed to read frame`.

#### [](#fixed-issues)Fixed issues

* [RSCBC-281](https://jira.issues.couchbase.com/browse/RSCBC-281): Fixed an issue where an error was logged whilst closing connections during a graceful shutdown.
* [RSCBC-289](https://jira.issues.couchbase.com/browse/RSCBC-289): Fixed an issue where connections to a service could fail over TLS after earlier connections had succeeded. TLS session resumption is now disabled.

### [](#version-1-0-1-9-april-2026)Version 1.0.1 (9 April 2026)

Version 1.0.1 is a maintenance release for the Rust SDK 1.0.

[API Documentation](https://docs.rs/couchbase/1.0.1/couchbase/)

#### [](#new-features-and-behavioral-changes-2)New Features and Behavioral Changes

* [RSCBC-270](https://jira.issues.couchbase.com/browse/RSCBC-270): Updated queries to automatically retry when query engine errors indicate to do so.
* [RSCBC-272](https://jira.issues.couchbase.com/browse/RSCBC-272): Updated logging output.

#### [](#fixed-issues-2)Fixed issues

* [RSCBC-267](https://jira.issues.couchbase.com/browse/RSCBC-267): Fixed an issue where a node unexpectedly going down could lead to a connection storm.
* [RSCBC-268](https://jira.issues.couchbase.com/browse/RSCBC-268): Fixed an issue where metrics were missing the `db.system.name` field.

### [](#version-1-0-0-12-march-2026)Version 1.0.0 (12 March 2026)

Initial GA release.