---
title: SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Couchbase Rust Client.
pubDate: 2026-10-16T07:26:40.932Z
meta:
  component:
    title: Rust SDK
    version: "1.1"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.1/modules/project-docs/pages/sdk-release-notes.adoc
  xref: xref:rust-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Couchbase Rust Client. 

Version 1.1 of the Rust SDK implements the 3.10 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

## [](#installation)Installation

* The Couchbase Rust SDK 1.1 Client supports Rust 1.88+.

More details of the installation process are in the [full installation guide](sdk-full-installation.md). In most cases, given the above prerequisites, it's a simple matter of the following:

```none
cargo add couchbase
```

## [](#latest-release)Rust SDK 1.1 Releases

Version 1.1 of the Rust SDK implements the 3.10 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

Binary compatibility is not guaranteed for any Rust SDK release, and you should rebuild your application when changing the SDK.

### [](#version-1-1-0-7-october-2026)Version 1.1.0 (7 October 2026)

Version 1.1.0 is the first release of the Rust SDK 1.1, implementing the 3.10 SDK API. It adds reads from a specific replica, Score Fusion for hybrid Search, and log redaction.

[API Documentation](https://docs.rs/couchbase/1.1.0/couchbase/)

#### [](#new-features-and-behavioral-changes)New Features and Behavioral Changes

* [RSCBC-302](https://jira.issues.couchbase.com/browse/RSCBC-302): Added `Collection::get_replica`, which reads a document from a specific replica, chosen with a `GetReplicaStrategy`. For example, `GetReplicaStrategy::from_index(ReplicaIndex::First, None)` reads from the first replica.
* [RSCBC-309](https://jira.issues.couchbase.com/browse/RSCBC-309): Added log redaction, enabled with `ClusterOptions::log_redaction(true)`. When enabled, the SDK wraps sensitive values in its log output in tags, so that a tool such as [cblogredaction](https://docs.couchbase.com/server/current/cli/cbcli/cblogredaction.html) can strip or hash them. Redaction is process-wide, and applies to log messages only, not to tracing span fields or metric events.
* [RSCBC-275](https://jira.issues.couchbase.com/browse/RSCBC-275): Added Cargo features for finer control over dependencies: `logging-meter` (the `LoggingMeter`), `threshold-logging-tracer` (the `ThresholdLoggingTracer`), and `dns-srv` (DNS SRV bootstrap and `DnsOptions`, via `hickory-resolver`). All three are enabled by default. If you build with `default-features = false`, enable these features explicitly to keep using them.
* [RSCBC-285](https://jira.issues.couchbase.com/browse/RSCBC-285): Field names passed to `create_index` are no longer escaped by the SDK, so nested paths such as `d.firstName` now index the nested field. Escape field names that need it yourself, using backticks.
* [RSCBC-286](https://jira.issues.couchbase.com/browse/RSCBC-286): Query error code 2120 is now reported as an authentication failure.
* [RSCBC-313](https://jira.issues.couchbase.com/browse/RSCBC-313): The crates now declare a minimum supported Rust version (`rust-version`) of `1.88`.

#### [](#fixed-issues)Fixed issues

* [RSCBC-312](https://jira.issues.couchbase.com/browse/RSCBC-312): Fixed an issue where the query tracing span in query index management operations was not emitted under the `couchbase::tracing` target.

## [](#rust-sdk-1-0-releases)Rust SDK 1.0 Releases

### [](#version-1-0-3-15-september-2026)Version 1.0.3 (15 September 2026)

Version 1.0.3 is a maintenance release for the Rust SDK 1.0.

[API Documentation](https://docs.rs/couchbase/1.0.3/couchbase/)

#### [](#new-features-and-behavioral-changes-2)New Features and Behavioral Changes

* [RSCBC-303](https://jira.issues.couchbase.com/browse/RSCBC-303): Updated the `hickory-resolver` dependency to `0.26.1`.

#### [](#fixed-issues-2)Fixed issues

* [RSCBC-301](https://jira.issues.couchbase.com/browse/RSCBC-301): Fixed an issue where the SDK did not send its client name during the memcached HELO negotiation.

### [](#version-1-0-2-11-august-2026)Version 1.0.2 (11 August 2026)

Version 1.0.2 is a maintenance release for the Rust SDK 1.0.

[API Documentation](https://docs.rs/couchbase/1.0.2/couchbase/)

#### [](#new-features-and-behavioral-changes-3)New Features and Behavioral Changes

* [RSCBC-282](https://jira.issues.couchbase.com/browse/RSCBC-282): Updated key-value error messages to include the underlying cause of the error, giving more context to warnings such as `failed to read frame`.

#### [](#fixed-issues-3)Fixed issues

* [RSCBC-281](https://jira.issues.couchbase.com/browse/RSCBC-281): Fixed an issue where an error was logged whilst closing connections during a graceful shutdown.
* [RSCBC-289](https://jira.issues.couchbase.com/browse/RSCBC-289): Fixed an issue where connections to a service could fail over TLS after earlier connections had succeeded. TLS session resumption is now disabled.

### [](#version-1-0-1-9-april-2026)Version 1.0.1 (9 April 2026)

Version 1.0.1 is a maintenance release for the Rust SDK 1.0.

[API Documentation](https://docs.rs/couchbase/1.0.1/couchbase/)

#### [](#new-features-and-behavioral-changes-4)New Features and Behavioral Changes

* [RSCBC-270](https://jira.issues.couchbase.com/browse/RSCBC-270): Updated queries to automatically retry when query engine errors indicate to do so.
* [RSCBC-272](https://jira.issues.couchbase.com/browse/RSCBC-272): Updated logging output.

#### [](#fixed-issues-4)Fixed issues

* [RSCBC-267](https://jira.issues.couchbase.com/browse/RSCBC-267): Fixed an issue where a node unexpectedly going down could lead to a connection storm.
* [RSCBC-268](https://jira.issues.couchbase.com/browse/RSCBC-268): Fixed an issue where metrics were missing the `db.system.name` field.

### [](#version-1-0-0-12-march-2026)Version 1.0.0 (12 March 2026)

Initial GA release.