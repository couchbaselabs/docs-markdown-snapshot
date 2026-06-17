---
title: Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Go Client.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-06-17T06:07:18.814Z
link: xref:2.11@go-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.11/project-docs/sdk-release-notes.html)

# Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Go Client. 

These pages cover the 2.x versions of the Couchbase Go SDK (3.x SDK API). For release notes, download links, and installation methods for 1.6 and earlier releases of the Couchbase Go Client, please see the [1.x Go Release Notes & Download Archive](https://docs-archive.couchbase.com/go-sdk/1.6/relnotes-go-sdk.html).

Version 2.11 of the Go SDK implements the 3.8 [SDK API](compatibility.md#api-version). See the [compatibility pages](compatibility.md#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

## [](#sdk-installation)SDK Installation

```console
$ go get github.com/couchbase/gocb/v2@v2.11.1
```

> [!NOTE]
> In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), we support both the current, and the previous, versions of Go. Older versions may work, but are not supported.

### [](#api-documentation)API Documentation

The most current and up to date API Documentation is always available through the [godoc website](https://pkg.go.dev/github.com/couchbase/gocb/v2).

## [](#latest-release)Go SDK 2.12 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-2-12-4-16-june-2026)Version 2.12.4 (16 June 2026)

Version 2.12.4 is a maintenance release for the Go SDK 2.12.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.12.4?tab=doc)

#### [](#fixed-issues)Fixed issues

* [GOCBC-1824](https://jira.issues.couchbase.com/browse/GOCBC-1824): Resolved a data race in `Collection.Scan` when `ScanOptions.Concurrency` is set to a value greater than 1.
* [GOCBC-1816](https://jira.issues.couchbase.com/browse/GOCBC-1816): Resolved a data race during when `Cluster.Close` is called while operations are ongoing, due to how the meter was accessed internally.
* [GOCBC-1821](https://jira.issues.couchbase.com/browse/GOCBC-1816): Fixed the value of `ScanTermMaximum`, which had been encoded incorrectly. This could lead to documents missing from a scan result when document keys include nonstandard unicode characters. `ScanTermMaximum` is now equivalent to `utf8.MaxRune`.
* [GOCBC-1828](https://jira.issues.couchbase.com/browse/GOCBC-1828): Fixed an issue with `Collection.Scan` where any fatal errors from initial vBucket scans, could either be returned immediately, or via `ScanResult.Err` depending on goroutine scheduling. Now they are consistently returned immediately by `Collection.Scan`.
* [GOCBC-1835](https://jira.issues.couchbase.com/browse/GOCBC-1835): Fixed an issue when an already cancelled `context.Context` is provided to an operation where the operation may still succeed. It is now guaranteed that the operation will fail with `ErrRequestCanceled`.

### [](#version-2-12-3-20-may-2026)Version 2.12.3 (20 May 2026)

Version 2.12.3 is a maintenance release for the Go SDK 2.12.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.12.3?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes)New Features and Behavioral Changes

* [GOCBC-1815](https://jira.issues.couchbase.com/browse/GOCBC-1815): When `snappy.Decode` fails a warning was emitted, but no information included on what went wrong. This warning is now updated to include the command, opaque, status and, datatype. (If redaction is enabled then the key if redacted.)

#### [](#fixed-issues-2)Fixed Issues

* [GOCBC-1812](https://jira.issues.couchbase.com/browse/GOCBC-1812): Fixed an issue where `WaitUntilReady` can fail with `ErrRequestCanceled` during the initial network resolution when the seed endpoints don't match either the 'default' or 'external' network's endpoints. In that case, existing connections are dropped, cancelling the in-progress bootstrap, but this does not indicate an error.

### [](#version-2-12-2-23-april-2026)Version 2.12.2 (23 April 2026)

Version 2.12.2 is a maintenance release for the Go SDK 2.12.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.12.2?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#fixed-issues-3)Fixed Issues

* [GOCBC-1803](https://jira.issues.couchbase.com/browse/GOCBC-1803): Reverted a behavioral change, where a non-empty username, but an empty password, result in a timeout instead of a `ErrAuthenticationFailure` (for example, in `WaitUntilReady`).
* [GOCBC-1805](https://jira.issues.couchbase.com/browse/GOCBC-1805): Updated to the latest version of the `couchbase2` protocol, which resolves an issue where the latest `gocb` and `goprotostellar` versions were incompatible.
* [GOCBC-1807](https://jira.issues.couchbase.com/browse/GOCBC-1807): Fixed an issue where the internal TLS configuration is not preserved when using `SetAuthenticator`, which resulted in subsequent connections attempting to connect to TLS ports without TLS enabled, and failing.
* [GOCBC-1808](https://jira.issues.couchbase.com/browse/GOCBC-1808): Resolved an issue with `SetAuthenticator` where the references to existing KV connections were being lost. Existing connections were still active, but orphaned. This resulted in failing operations until new connections were established.
* [GOCBC-1809](https://jira.issues.couchbase.com/browse/GOCBC-1809): Fixed a deadlock that happens when `SetAuthenticator` is called with a `JWTAuthenticator` and authentication fails. Resolved a panic that could occur when `SetAuthenticator` is called with a `JWTAuthenticator` and the SDK is in the process of dialing a KV connection.

### [](#version-2-12-1-23-march-2026)Version 2.12.1 (23 March 2026)

Version 2.12.1 is a maintenance release for the Go SDK 2.12.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.12.1?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#fixed-issues-4)Fixed issues

* [GOCBC-1796](https://jira.issues.couchbase.com/browse/GOCBC-1796): Fixed a rare "send on closed channel" panic that could occur during a transactions `BulkGet` operation when documents were being fetched concurrently.
* [GOCBC-1799](https://jira.issues.couchbase.com/browse/GOCBC-1799): Fixed issue where concurrent calls to `Cluster.Bucket` could race and result in multiple bucket agents being opened internally, which would leak even after `Cluster.Close` is called.

### [](#version-2-12-0-19-february-2026)Version 2.12.0 (19 February 2026)

Version 2.12.0 is the first release in the Go SDK 2.12 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.12.0?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-2)New Features and Behavioral Changes

* [GOCBC-1769](https://jira.issues.couchbase.com/browse/GOCBC-1769): Added support for mTLS certificate refresh without restart.
* [GOCBC-1775](https://jira.issues.couchbase.com/browse/GOCBC-1775): Deprecated support for MapReduce Views.
* [GOCBC-1776](https://jira.issues.couchbase.com/browse/GOCBC-1776): Added support for OpenTelemetry semantic conventions.

#### [](#fixed-issues-5)Fixed Issues

* [GOCBC-1782](https://jira.issues.couchbase.com/browse/GOCBC-1782): Fixed issue where specified scope was ignored when creating group. it is now possible to specify role scope when creating a group.

## [](#go-sdk-2-11-releases)Go SDK 2.11 Releases

### [](#version-2-11-3-18-february-2026)Version 2.11.3 (18 February 2026)

Version 2.11.3 is a maintenance release for the Go SDK 2.11.

#### [](#fixed-issues-6)Fixed Issues

* [GOCBC-1788](https://jira.issues.couchbase.com/browse/GOCBC-1788): Fixed issue where app telemetry could panic when multiple nodes share an address (e.g. a load balanced environment).

### [](#version-2-11-2-21-january-2026)Version 2.11.2 (21 January 2026)

Version 2.11.2 is a maintenance release for the Go SDK 2.11.

#### [](#new-features-and-behavioral-changes-3)New Features and Behavioral Changes

* [GOCBC-1780](https://jira.issues.couchbase.com/browse/GOCBC-1780): Updated dependencies.

#### [](#fixed-issues-7)Fixed Issues

* [GOCBC-1774](https://jira.issues.couchbase.com/browse/GOCBC-1774): Fixed issue where get projections with > 16 would not correctly rebuild the projection.
* [GOCBC-1778](https://jira.issues.couchbase.com/browse/GOCBC-1778): Fixed issue where it was not able to reset durability level to none using `UpdateBucket`.

### [](#version-2-11-1-18-september-2025)Version 2.11.1 (18 September 2025)

Version 2.11.1 is a maintenance release for the Go SDK 2.11.

#### [](#fixed-issues-8)Fixed Issues

* [GOCBC-1764](https://jira.issues.couchbase.com/browse/GOCBC-1764): Non-TLS connections are not possible with the `couchbase2://` scheme. TLS is now always enabled when the `couchbase2://` scheme is used, and the system certificate pool is used by default if no certificate options are specified.
* [GOCBC-1762](https://jira.issues.couchbase.com/browse/GOCBC-1762): Improved logging for `WaitUntilReady` when no bootstrap error is found before a config is seen, to make it clearer that there was no error.
* [GOCBC-1765](https://jira.issues.couchbase.com/browse/GOCBC-1765): Improved error message when the `couchbase2://` scheme is used in a connection string with a bucket.

### [](#version-2-11-0-26-august-2025)Version 2.11.0 (26 August 2025)

Version 2.11.0 is the first release in the Go SDK 2.11 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.11.0?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-4)New Features and Behavioral Changes

* [GOCBC-1633](https://jira.issues.couchbase.com/browse/GOCBC-1633), [GOCBC-1739](https://jira.issues.couchbase.com/browse/GOCBC-1739): Added support for binary objects in transactions.
* [GOCBC-1692](https://jira.issues.couchbase.com/browse/GOCBC-1692): Added missing fields to orphan reporter output.
* [GOCBC-1693](https://jira.issues.couchbase.com/browse/GOCBC-1693): Updated app telemetry to contain latency for orphaned responses.
* [GOCBC-1703](https://jira.issues.couchbase.com/browse/GOCBC-1703): Updated replica reads in transactions.
* [GOCBC-1716](https://jira.issues.couchbase.com/browse/GOCBC-1716): Added support for FTS like pre-filters while doing vector search.
* [GOCBC-1759](https://jira.issues.couchbase.com/browse/GOCBC-1759): Updated FTS `BooleanQuery` to accept a variadic parameter to allow a list of queries to be specified.

#### [](#fixed-issues-9)Fixed Issues

* [GOCBC-1669](https://jira.issues.couchbase.com/browse/GOCBC-1669): Fixed issue where management operations had the incorrect metrics/span value for the `db.couchbase.service` attribute.
* [GOCBC-1723](https://jira.issues.couchbase.com/browse/GOCBC-1723): Fixed issue where the incorrect error was returned for not locked in `couchbase2` mode.
* [GOCBC-1730](https://jira.issues.couchbase.com/browse/GOCBC-1730): Fixed issue where `alt_node` was always reported for KV app telemetry.
* [GOCBC-1742](https://jira.issues.couchbase.com/browse/GOCBC-1742): Fixed issue where `ErrDocumentExists` was wrapped in a `TransactionOperationFailedError` when it should not have been.
* [GOCBC-1746](https://jira.issues.couchbase.com/browse/GOCBC-1746): Fixed issue where SRV record refresh would not correctly reset internal SDK state.

#### [](#api-breaking-fixed-issues)API breaking fixed Issues

* [GOCBC-1758](https://jira.issues.couchbase.com/browse/GOCBC-1758): Fixed issue where FTS `TermRangeQuery` was requiring (and sending in the payload) a `term` attribute. This led to the query always being executed as a `TermQuery`, and a `TermRangeQuery` never being executed.

## [](#go-sdk-2-10-releases)Go SDK 2.10 Releases

### [](#version-2-10-1-21-july-2025)Version 2.10.1 (21 July 2025)

Version 2.10.1 is a maintenance release for the Go SDK 2.10.

#### [](#fixed-issues-10)Fixed Issues

* [GOCBC-1724](https://jira.issues.couchbase.com/browse/GOCBC-1724): Fixed issue where `Append` and `Prepend` could panic in `couchbase2` mode if a retry occured.
* [GOCBC-1735](https://jira.issues.couchbase.com/browse/GOCBC-1735): Fixed issue where Eventing function `QueryConsistency` was sent as the incorrect type on the wire.
* [GOCBC-1737](https://jira.issues.couchbase.com/browse/GOCBC-1737): Fixed issue where reading search results could panic in `couchbase2` mode.
* [GOCBC-1743](https://jira.issues.couchbase.com/browse/GOCBC-1743): Fixed issue where `GetMulti` read skew resolution could nil pointer.
* [GOCBC-1745](https://jira.issues.couchbase.com/browse/GOCBC-1745): Fixed issue where SRV record refresh would never match existing addresses being used.
* [GOCBC-1747](https://jira.issues.couchbase.com/browse/GOCBC-1747): Fixed issue where SRV record refresh would fail when cluster config pushes were active.

### [](#version-2-10-0-17-april-2025)Version 2.10.0 (17 April 2025)

Version 2.10.0 is the first release in the Go SDK 2.10 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.10.0?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-5)New Features and Behavioral Changes

* [GOCBC-1278](https://jira.issues.couchbase.com/browse/GOCBC-1278): Added transactions support for `ExtReplaceBodyWithXattr`.
* [GOCBC-1311](https://jira.issues.couchbase.com/browse/GOCBC-1311): Added transactions support for `ExtThreadSafety`.
* [GOCBC-1430](https://jira.issues.couchbase.com/browse/GOCBC-1430): Updated path to `/whoami` rather than `/` for pinging the management service.
* [GOCBC-1676](https://jira.issues.couchbase.com/browse/GOCBC-1676): Added support for application telemetry.
* [GOCBC-1687](https://jira.issues.couchbase.com/browse/GOCBC-1687): Replaced usages of deprecated http transport dial functions.
* [GOCBC-1688](https://jira.issues.couchbase.com/browse/GOCBC-1688): Replaced usages of deprecated `ioutil` functions.
* [GOCBC-1701](https://jira.issues.couchbase.com/browse/GOCBC-1701): Added transactions support for `ExtGetMulti`.
* [GOCBC-1704](https://jira.issues.couchbase.com/browse/GOCBC-1704): Added transactions support for specifying `NumVBuckets` in `BucketSettings`.
* [GOCBC-1706](https://jira.issues.couchbase.com/browse/GOCBC-1706): Added support to the core for Columnar via a new Columnar Agent.
* [GOCBC-1707](https://jira.issues.couchbase.com/browse/GOCBC-1707): Updated minimum compatible Go version to 1.21.
* [GOCBC-1713](https://jira.issues.couchbase.com/browse/GOCBC-1713): Updated bucket management operations to convert HTTP status code 400 into `ErrInvalidArgument`.

#### [](#fixed-issues-11)Fixed Issues

* [GOCBC-1648](https://jira.issues.couchbase.com/browse/GOCBC-1648): Fixed issue where `highlight.fields` would be sent in a search request payload even when the option wasn't specified.
* [GOCBC-1712](https://jira.issues.couchbase.com/browse/GOCBC-1712): Fixed issue where `Append` and `Prepend` would return `ErrDocExists` rather than `ErrCasMismatch`.
* [GOCBC-1715](https://jira.issues.couchbase.com/browse/GOCBC-1715): Fixed issue where `LoggingMeter` logged `emit_interval_s` as nanoseconds rather than seconds.

## [](#go-sdk-2-9-releases)Go SDK 2.9 Releases

### [](#version-2-9-4-21-february-2025)Version 2.9.4 (21 February 2025)

Version 2.9.4 is a maintenance release for the Go SDK 2.9.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.9.4?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#fixed-issues-12)Fixed Issues

* [GOCBC-1696](https://jira.issues.couchbase.com/browse/GOCBC-1696): Fixed an issue where scope-level SQL++ queries would fail if the scope or bucket names contained a period character (`.`).

### [](#version-2-9-3-26-november-2024)Version 2.9.3 (26 November 2024)

Version 2.9.3 is a maintenance release for the Go SDK 2.9.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.9.3?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-6)New Features and Behavioral Changes

* [GOCBC-1656](https://jira.issues.couchbase.com/browse/GOCBC-1656): Added support for zone-aware replica reads to transactions, at API stability level **uncommitted**.
* [GOCBC-1658](https://jira.issues.couchbase.com/browse/GOCBC-1658): Added more contextual labels to metrics.
* [GOCBC-1674](https://jira.issues.couchbase.com/browse/GOCBC-1674): Added support for `max_perhost_http_connections` connection string parameter.
* [GOCBC-1677](https://jira.issues.couchbase.com/browse/GOCBC-1677): vbucket id is now included in trace level dispatch logs, to aid debugging issues where `NotMyVbucket` is received.
* [GOCBC-1680](https://jira.issues.couchbase.com/browse/GOCBC-1680): Improved retry handling for http operations.

### [](#version-2-9-2-25-september-2024)Version 2.9.2 (25 September 2024)

Version 2.9.2 is a maintenance release for the Go SDK 2.9.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.9.2?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-7)New Features and Behavioral Changes

* [GOCBC-1632](https://jira.issues.couchbase.com/browse/GOCBC-1632): Added support for zone-aware replica reads, at API stability level **uncommitted**.
* [GOCBC-1657](https://jira.issues.couchbase.com/browse/GOCBC-1657): Updated tracing when using the `couchbase2` scheme, to send traces to the server over gRPC.

#### [](#fixed-issues-13)Fixed Issues

* [GOCBC-1655](https://jira.issues.couchbase.com/browse/GOCBC-1655): Fixed the error messages for some connection string parameter parsing errors, where the message was not referring to the correct parameter.
* [GOCBC-1660](https://jira.issues.couchbase.com/browse/GOCBC-1660): Fixed a possible data race that occurred because the value of a lock was being logged at debug-level.

### [](#version-2-9-1-18-july-2024)Version 2.9.1 (18 July 2024)

Version 2.9.1 is a maintenance release for the Go SDK 2.9.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.9.1?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-8)New Features and Behavioral Changes

* [GOCBC-1640](https://issues.couchbase.com/browse/GOCBC-1640): Adjusted logging levels when logging about receiving cluster configs older than the SDK already has.

#### [](#fixed-issues-14)Fixed Issues

* [GOCBC-1625](https://issues.couchbase.com/browse/GOCBC-1625): Fixed issue where a data race could occur when requests were retried concurrently with being cancelled.
* [GOCBC-1643](https://issues.couchbase.com/browse/GOCBC-1643): Fixed issue where couchbase2 mode did not wait for operations to complete on close.

### [](#version-2-9-0-18-june-2024)Version 2.9.0 (18 June 2024)

Version 2.9.0 is the first release in the Go SDK 2.9 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.9.0?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-9)New Features and Behavioral Changes

* [GOCBC-1626](https://issues.couchbase.com/browse/GOCBC-1626): Addressed an issue where performing operations after calling cluster.Close (or calling close twice) would lead to a panic. On close the SDK will now cancel all in flight operations and block waiting for them to complete/be cancelled. All operations will now fast fail if called after close.
* [GOCBC-1631](https://issues.couchbase.com/browse/GOCBC-1631): Added handling to treat memcached scope not found errors the same as collection not found errors.
* [GOCBC-1634](https://issues.couchbase.com/browse/GOCBC-1634): Added support for base64 encoded vector queries.
* [GOCBC-1642](https://issues.couchbase.com/browse/GOCBC-1642): Moved vector search API support level to committed.

#### [](#fixed-issues-15)Fixed Issues

* [GOCBC-1625](https://issues.couchbase.com/browse/GOCBC-1625): Fixed issue where SDK could not receive large (> 4MB) documents in `couchbase2` mode.
* [GOCBC-1636](https://issues.couchbase.com/browse/GOCBC-1636): Fixed issue where a race accessing config watchers could occur on agent close.

## [](#go-sdk-2-8-releases)Go SDK 2.8 Releases

### [](#version-2-8-1-18-april-2024)Version 2.8.1 (18 April 2024)

Version 2.8.1 is a maintenance release for the Go SDK 2.8.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.8.1?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-10)New Features and Behavioral Changes

* [GOCBC-1520](https://issues.couchbase.com/browse/GOCBC-1520): Added `MaxConcurrency` to `ScanOptions` at API stability level uncommitted.
* [GOCBC-1578](https://issues.couchbase.com/browse/GOCBC-1578): Made port optional in connection string for `couchbase2` mode, now defaults to 18908.
* [GOCBC-1615](https://issues.couchbase.com/browse/GOCBC-1615): Updated SCRAM client to relax some validation checks, in line with SCRAM RFC 7677.
* [GOCBC-1623](https://issues.couchbase.com/browse/GOCBC-1623): Added support for `Scope` level eventing functions at API stability level uncommitted.

#### [](#fixed-issues-16)Fixed Issues

* [GOCBC-1617](https://issues.couchbase.com/browse/GOCBC-1617): Fixed issue where service not available errors were not always retried in `couchbase2` mode.
* [GOCBC-1617](https://issues.couchbase.com/browse/GOCBC-1617): Fixed issue where the degraded cluster target state for `WaitUntilReady` would check all services by default, rather than only those available on the cluster.

### [](#version-2-8-0-12-march-2024)Version 2.8.0 (12 March 2024)

Version 2.8.0 is the first release in the Go SDK 2.8 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.8.0?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-11)New Features and Behavioral Changes

* [GOCBC-1577](https://issues.couchbase.com/browse/GOCBC-1577): Added support for vector search.
* [GOCBC-1578](https://issues.couchbase.com/browse/GOCBC-1578): Updated connection parsing to default to port 18098 if not specified when `couchbase2` scheme is used.
* [GOCBC-1608](https://issues.couchbase.com/browse/GOCBC-1608): Return `ErrFeatureNotAvailable` if requested search capabilities aren't available.
* [GOCBC-1614](https://issues.couchbase.com/browse/GOCBC-1614): Updated SDK API volatility levels:

  * Moved Collection range scan to committed,
  * Moved Query read from replica to committed,
  * Moved LookupIn read from replica to committed,
  * Move Bucket History Retention Settings to committed,
  * Moved UserManager Change Password to committed,
  * Moved Scope level Search and SearchIndexes to committed,
  * Moved Vector Search to uncommitted.

#### [](#fixed-issues-17)Fixed Issues

* [GOCBC-1582](https://issues.couchbase.com/browse/GOCBC-1582): Fixed issue where `math.MaxUint32` was causing an error when used with `fmt.Errorf`.

#### [](#breaking-fixes)Breaking Fixes

* [GOCBC-1482](https://issues.couchbase.com/browse/GOCBC-1482): Fixed issue where there was inconsistency in whether Couchbase error types were returned as pointers across services, now all Couchbase errors are returned as pointers. Improved the string output for `TimeoutError`. We expect this to have a minimal impact but may impact some users who are using `errors.As` or directly type asserting errors.
* [GOCBC-1575](https://issues.couchbase.com/browse/GOCBC-1575): Improved the interface for `BucketSetting` `HistoryRetentionCollectionDefault` field to use a constant value rather than a bool pointer.

## [](#go-sdk-2-7-releases)Go SDK 2.7 Releases

### [](#version-2-7-2-20-february-2024)Version 2.7.2 (20 February 2024)

Version 2.7.2 is a maintenance release for the Go SDK 2.7.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.7.2?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-12)New Features and Behavioral Changes

* [GOCBC-1470](https://issues.couchbase.com/browse/GOCBC-1470): Added a V2 Collection management API, accessed via `Bucket.CollectionsV2()`, which has improved method signatures for `CreateCollection`, `UpdateCollection`, and `DropCollection`.
* [GOCBC-1580](https://issues.couchbase.com/browse/GOCBC-1580): Exposed constants for the `unit` setting of `SearchSortGeoDistance`.
* [GOCBC-1584](https://issues.couchbase.com/browse/GOCBC-1584): Added support for compressing data between the SDK and server in `couchbase2` mode.
* [GOCBC-1585](https://issues.couchbase.com/browse/GOCBC-1585): Exposed non-idempotent requests that fail because of the socket closing while they are in-flight to the retry orchestrator (`SocketCloseInFlightRetryReason` retry reason).
* [GOCBC-1590](https://issues.couchbase.com/browse/GOCBC-1590): Added support for `FlushBucket` in `couchbase2` mode.
* [GOCBC-1591](https://issues.couchbase.com/browse/GOCBC-1591): Added support for `Scope.Search()` and `Scope.SearchIndexes()` for querying and managing scoped search indexes.

#### [](#fixed-issues-18)Fixed Issues

* [GOCBC-1367](https://issues.couchbase.com/browse/GOCBC-1367): Fixed issue where `ExpiryTime` in `GetResult` had the epoch value instead of zero time (`time.Time{}`) when the document has no expiry.
* [GOCBC-1599](https://issues.couchbase.com/browse/GOCBC-1599): Fixed issue where the `DropIndex` search management operation was not converting server errors to any of the known error values (e.g. `ErrIndexNotFound`) where applicable.

### [](#version-2-7-1-17-january-2024)Version 2.7.1 (17 January 2024)

Version 2.7.1 is a maintenance release for the Go SDK 2.7.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.7.1?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-13)New Features and Behavioral Changes

* [GOCBC-1494](https://issues.couchbase.com/browse/GOCBC-1494): Improvements to Query error handling. Added handling for some additional Query error codes.
* [GOCBC-1549](https://issues.couchbase.com/browse/GOCBC-1549): Added the ability to specify both positional and named parameters in queries.
* [GOCBC-1558](https://issues.couchbase.com/browse/GOCBC-1558): Added the `ErrDocumentNotLocked` error which is returned when KV responds with a `NOT_LOCKED` status.
* [GOCBC-1561](https://issues.couchbase.com/browse/GOCBC-1561): The SDK now displays the error description from the KV error map when an unknown KV status is received.
* [GOCBC-1579](https://issues.couchbase.com/browse/GOCBC-1579): Added support for `MaxExpiry` value of -1 ('No Expiry') in collection management operations.
* [GOCBC-1560](https://issues.couchbase.com/browse/GOCBC-1560): Added support in the `couchbase2` mode for history retention settings in the bucket management API.
* [GOCBC-1562](https://issues.couchbase.com/browse/GOCBC-1562): Added support for `UpdateCollection` in the `couchbase2` mode.

#### [](#fixed-issues-19)Fixed Issues

* [GOCBC-1573](https://issues.couchbase.com/browse/GOCBC-1573): Fixed issue where the SDK's prepared query cache was not differentiating between queries which have the same statement but are in a different query context.
* [GOCBC-1581](https://issues.couchbase.com/browse/GOCBC-1581): Fixed issue where the partition counts in `SearchMetrics` were not populated.
* [GOCBC-1588](https://issues.couchbase.com/browse/GOCBC-1588): Fixed issue with the `couchbase2` mode where Conjunction, Disjunction, and Boolean search queries always failed with an 'invalid query' error.

### [](#version-2-7-0-21-november-2023)Version 2.7.0 (21 November 2023)

Version 2.7.0 is the first release in the Go SDK 2.7 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.7.0?tab=doc)

Tracing and metrics with the `couchbase2` scheme should be considered stability level **volatile** at this time.

#### [](#new-features-and-behavioral-changes-14)New Features and Behavioral Changes

* [GOCBC-1322](https://issues.couchbase.com/browse/GOCBC-1322): Added RangeScan support as API stability volatile.
* [GOCBC-1391](https://issues.couchbase.com/browse/GOCBC-1391): Deprecated the use of `CollectionName` and `ScopeName` for query index options blocks, use `collection.QueryIndexes()` instead.
* [GOCBC-1394](https://issues.couchbase.com/browse/GOCBC-1394): Updated requests against HTTP APIs to always encode URIs.
* [GOCBC-1397](https://issues.couchbase.com/browse/GOCBC-1397): Added support for the `couchbase2://` protocol.
* [GOCBC-1414](https://issues.couchbase.com/browse/GOCBC-1414): The SDK no longer works with Go versions below 1.19, due to versions enforced by dependencies.
* [GOCBC-1434](https://issues.couchbase.com/browse/GOCBC-1434): Added `LookupInAnyReplica` and `LookupInAllReplicas` support as API stability volatile.
* [GOCBC-1436](https://issues.couchbase.com/browse/GOCBC-1436): Added `UseReplica` to `QueryOptions` as API stability uncommitted.
* [GOCBC-1439](https://issues.couchbase.com/browse/GOCBC-1439): Added support for Config Push Negotiation and faster failover.
* [GOCBC-1454](https://issues.couchbase.com/browse/GOCBC-1454): Added support for JSON marshalling/unmarshalling of search indexes.
* [GOCBC-1457](https://issues.couchbase.com/browse/GOCBC-1457): Reduced the default timeout for idle HTTP connections to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures
* [GOCBC-1459](https://issues.couchbase.com/browse/GOCBC-1459): Added support for history retention settings to bucket and collections managers, at API stability uncommitted.
* [GOCBC-1461](https://issues.couchbase.com/browse/GOCBC-1461): Updated `ExistsSpec` response to handle `ContentAt` better:

  * Assign true if the path does exists
  * Assign false if the path does not exist
  * Return an error for all other statuses
* [GOCBC-1540](https://issues.couchbase.com/browse/GOCBC-1540): Added support for `ErrDocumentTooDeep` which is only used in `couchbase2` mode, equivalent to `ErrPathTooDeep`.

#### [](#fixed-issues-20)Fixed Issues

* [GOCBC-1471](https://issues.couchbase.com/browse/GOCBC-1471): Fixed issue where calling `.Bucket` immediately after `.Connect` could lead to the config poller failing to stop.
* [GOCBC-1479](https://issues.couchbase.com/browse/GOCBC-1479): Fixed issue where a cluster config fetched as a part of bootstrap would be applied even if select bucket failed.
* [GOCBC-1460](https://issues.couchbase.com/browse/GOCBC-1460): Fixed issue where a path mismatch status code was not converted to `ErrPathMismatch`.

#### [](#breaking-fixes-2)Breaking Fixes

* [GOCBC-1530](https://issues.couchbase.com/browse/GOCBC-1530): Fixed issue where `Append` and `Prepend` could directly return a `gocbcore.ErrNotStored` error, this is now translated to a `gocb.ErrDocumentNotFound` error.
* [GOCBC-1545](https://issues.couchbase.com/browse/GOCBC-1545): Fixed issue where `Projections` as a part of a `Get` operation would return any path level errors, these are now silently ignored.

## [](#go-sdk-2-6-releases)Go SDK 2.6 Releases

### [](#version-2-6-5-18-october-2023)Version 2.6.5 (18 October 2023)

Version 2.6.5 is a maintenance release for the Go SDK 2.6.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.6.5?tab=doc)

#### [](#new-features-and-behavioral-changes-15)New Features and Behavioral Changes

* [GOCBC-1489](https://issues.couchbase.com/browse/GOCBC-1489): Exposed `ErrCircuitBreakOpen` as API stability uncommitted.

#### [](#fixed-issues-21)Fixed Issues

* [GOCBC-1485](https://issues.couchbase.com/browse/GOCBC-1485): Fixed issue where operations queue for collection id refresh would not be dequeued on refresh.
* [GOCBC-1493](https://issues.couchbase.com/browse/GOCBC-1493): Fixed issue where key value operation transcoding errors would be swallowed by the SDK.

### [](#version-2-6-4-26-september-2023)Version 2.6.4 (26 September 2023)

Version 2.6.4 is a maintenance release for the Go SDK 2.6.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.6.4?tab=doc)

#### [](#new-features-and-behavioral-changes-16)New Features and Behavioral Changes

* [GOCBC-1479](https://issues.couchbase.com/browse/GOCBC-1479): Cluster configs fetched during bootstrap are now only applied if select bucket succeeds.

### [](#version-2-6-3-18-april-2023)Version 2.6.3 (18 April 2023)

Version 2.6.3 is a maintenance release for the Go SDK 2.6.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.6.3?tab=doc)

#### [](#new-features-and-behavioral-changes-17)New Features and Behavioral Changes

* [GOCBC-1403](https://issues.couchbase.com/browse/GOCBC-1403): Updated CCCP polling to start running on startup rather than waiting for memcached connections to fetch a cluster config.

#### [](#fixed-issues-22)Fixed Issues

* [GOCBC-1400](https://issues.couchbase.com/browse/GOCBC-1400): Fixed issue where connection string parsing was missing some timeout values.
* [GOCBC-1402](https://issues.couchbase.com/browse/GOCBC-1402): Fixed issue where wan-development config profile was missing some timeout values.

### [](#version-2-6-2-23-march-2023)Version 2.6.2 (23 March 2023)

Version 2.6.2 is a maintenance release for the Go SDK 2.6.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.6.2?tab=doc)

#### [](#new-features-and-behavioral-changes-18)New Features and Behavioral Changes

* [GOCBC-1392](https://issues.couchbase.com/browse/GOCBC-1392): Added support for `NumReplicas` to create (primary) index options.
* [GOCBC-1393](https://issues.couchbase.com/browse/GOCBC-1393): Updated behaviour for when queries are retried when enhanced prepared statements are used (i.e. prepared statements against server version >= 6.5.0). When an error is translated to a `QueryPreparedStatementFailureRetryReason` it will invalidate the prepared statement cache entry and attempt to reprepare the statement.
* [GOCBC-1395](https://issues.couchbase.com/browse/GOCBC-1395): Improved timeout error handling for http based services - if we know that an operation has already timed out then we will now immediately return a timeout error. Retry reason context is now carried throughout the lifetime of an entire prepared statement request.

### [](#version-2-6-1-22-february-2023)Version 2.6.1 (22 February 2023)

Version 2.6.1 is a maintenance release for the Go SDK 2.6.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.6.1?tab=doc)

#### [](#new-features-and-behavioral-changes-19)New Features and Behavioral Changes

* [GOCBC-1322](https://issues.couchbase.com/browse/GOCBC-1322): Added volatile support for kv range scan.
* [GOCBC-1373](https://issues.couchbase.com/browse/GOCBC-1373):

  * Added uncommitted support for `CollectionQueryIndexManager`.
  * Added support for sending `query_context` when `Scope` is set on `TransactionQueryyOptions`.
  * Added support for handling query error code 1197 as feature not available.

#### [](#fixed-issues-23)Fixed Issues

* [GOCBC-1376](https://issues.couchbase.com/browse/GOCBC-1376): Fixed issue where lost cleanup would log an incorrectly formatted log line, leading to spamming the log.
* [GOCBC-1387](https://issues.couchbase.com/browse/GOCBC-1387): Fixed issue where an edge case could trigger a race between releasing connection buffers and reading on the connection — leading to a panic.

### [](#version-2-6-0-20-october-2022)Version 2.6.0 (20 October 2022)

Version 2.6.0 is the first release in the Go SDK 2.6 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.6.0?tab=doc)

#### [](#new-features-and-behavioral-changes-20)New Features and Behavioral Changes

* [GOCBC-1159](https://issues.couchbase.com/browse/GOCBC-1159): Added support for refreshing the DNS SRV record when cluster becomes uncontactable, if applicable.
* [GOCBC-1284](https://issues.couchbase.com/browse/GOCBC-1284), [GOCBC-1328](https://issues.couchbase.com/browse/GOCBC-1328), [GOCBC-1331](https://issues.couchbase.com/browse/GOCBC-1331): Significant refactoring work to kv bootstrap, including pipelining fetching a config from the cluster.
* [GOCBC-1316](https://issues.couchbase.com/browse/GOCBC-1316): Added support for transactions `ExtInsertExisting` \- allowing `ErrDocumentExists` to be be ignored in transactional inserts.
* [GOCBC-1341](https://issues.couchbase.com/browse/GOCBC-1341): Added volatile level API support for `ConfigProfile`.
* [GOCBC-1352](https://issues.couchbase.com/browse/GOCBC-1352): Added support for trusting the system cert store when TLS is enabled with no `CertPool` registered and `SkipVerify` not set.
* [GOCBC-1356](https://issues.couchbase.com/browse/GOCBC-1356): Updated the behaviour when `MutateIn` or `Insert` returns `NOT_STORED` from the server to return a `ErrDocumentExists`.

#### [](#fixed-issues-24)Fixed Issues

* [GOCBC-1347](https://issues.couchbase.com/browse/GOCBC-1347): Fixed issue where a nil agent value could cause logging `TransactionATRLocation` to log a panic.
* [GOCBC-1348](https://issues.couchbase.com/browse/GOCBC-1348): Fixed issue where a race on creating a client record could lead to a panic.

## [](#go-sdk-2-5-releases)Go SDK 2.5 Releases

### [](#version-2-5-4-27-october-2022)Version 2.5.4 (27 October 2022)

Version 2.5.4 is a maintenance release for the Go SDK 2.5.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.5.4?tab=doc)

#### [](#fixed-issues-25)Fixed Issues

* [GOCBC-1347](https://issues.couchbase.com/browse/GOCBC-1347): Fixed issue where a nil agent value could cause logging `TransactionATRLocation` to log a panic.
* [GOCBC-1348](https://issues.couchbase.com/browse/GOCBC-1348): Fixed issue where a race on creating a client record could lead to a panic.

### [](#version-2-5-3-21-september-2022)Version 2.5.3 (21 September 2022)

Version 2.5.3 is a maintenance release for the Go SDK 2.5.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.5.3?tab=doc)

#### [](#fixed-issues-26)Fixed Issues

* [GOCBC-1338](https://issues.couchbase.com/browse/GOCBC-1338): Fixed issue where `lazyCircuitBreaker` was not using 64-bit aligned values.

#### [](#known-issues)Known Issues

* [GOCBC-1347](https://issues.couchbase.com/browse/GOCBC-1347): Known issue where a nil agent value could cause logging `TransactionATRLocation` to log a panic.
* [GOCBC-1348](https://issues.couchbase.com/browse/GOCBC-1348): Known issue where a race on creating a client record can lead to a panic.

### [](#version-2-5-2-20-july-2022)Version 2.5.2 (20 July 2022)

Version 2.5.2 is a maintenance release for the Go SDK 2.5.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.5.2?tab=doc)

#### [](#new-features-and-behavioral-changes-21)New Features and Behavioral Changes

* [GOCBC-1246](https://issues.couchbase.com/browse/GOCBC-1246): Added uncomitted stability support for `TransactionLogger` to `TransactionResult`.
* [GOCBC-1314](https://issues.couchbase.com/browse/GOCBC-1314): Improved logging in the lost transactions process.
* [GOCBC-1318](https://issues.couchbase.com/browse/GOCBC-1318): Changed `WaitUntilReady` to always wait for any explicitly defined services to be online.

#### [](#fixed-issues-27)Fixed Issues

* [GOCBC-1320](https://issues.couchbase.com/browse/GOCBC-1320): Fixed issue where vbucket hashing function wasn't masking out the 16th bit of the key.

### [](#version-2-5-1-22-june-2022)Version 2.5.1 (22 June 2022)

Version 2.5.1 is a maintenance release for the Go SDK 2.5.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.5.1?tab=doc)

#### [](#new-features-and-behavioral-changes-22)New Features and Behavioral Changes

* [GOCBC-1159](https://issues.couchbase.com/browse/GOCBC-1159): Improved support for serverless environments.
* [GOCBC-1250](https://issues.couchbase.com/browse/GOCBC-1250): Added support for single query transactions via `QueryOptions` `AsTransaction`.
* [GOCBC-1298](https://issues.couchbase.com/browse/GOCBC-1298): Masked the underlying error reason for `TransactionOperationFailedError`.
* [GOCBC-1213](https://issues.couchbase.com/browse/GOCBC-1213): Added uncommitted API level support for `UserManager` `ChangePassword`.

#### [](#fixed-issues-28)Fixed Issues

* [GOCBC-1300](https://issues.couchbase.com/browse/GOCBC-1300): Fixed issue where transactions lost cleanup would not remove deleted collections from the cleanup list.
* [GOCBC-1304](https://issues.couchbase.com/browse/GOCBC-1304): Fixed issue where transactions lost cleanup could temporarily block further responses being processed for a connection.

### [](#version-2-5-0-28-april-2022)Version 2.5.0 (28 April 2022)

Version 2.5.0 is the first release in the Go SDK 2.5 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.5.0?tab=doc)

#### [](#new-features-and-behavioral-changes-23)New Features and Behavioral Changes

* [GOCBC-1125](https://issues.couchbase.com/browse/GOCBC-1125): Deprecated `Cas` on Binary Append and Prepend as the server does not support this. Usage of `Cas` on these operations will now return an error.
* [GOCBC-1203](https://issues.couchbase.com/browse/GOCBC-1203): Added `CompressionOptions` to `ClusterOptions`, defaulting to compression being enabled.
* [GOCBC-1255](https://issues.couchbase.com/browse/GOCBC-1255): Deprecated `AggregatingMeterOptions` and `NewAggregatingMeter`.
* [GOCBC-1265](https://issues.couchbase.com/browse/GOCBC-1265): Bundle Capella CA certificate with the SDK.
* [TXNG-1253](https://issues.couchbase.com/browse/GOCBC-1253): Removed `ServerDurationDisabled` from `ThresholdLoggingOptions`.

#### [](#fixed-issues-29)Fixed Issues

* [GOCBC-1267](https://issues.couchbase.com/browse/GOCBC-1267): Fixed issue where `GetAllIndexes` could incorrectly omit the default collection.

## [](#go-sdk-2-4-releases)Go SDK 2.4 Releases

### [](#version-2-4-1-16-march-2022)Version 2.4.1 (16 March 2022)

Version 2.4.1 is a maintenance release for the Go SDK 2.4.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.4.1?tab=doc)

#### [](#new-features-and-behavioral-changes-24)New Features and Behavioral Changes

* [GOCBC-1221](https://issues.couchbase.com/browse/GOCBC-1221): Added support for handling any `retry:true` field in a query error result by retrying it.
* [GOCBC-1228](https://issues.couchbase.com/browse/GOCBC-1228): Updated the query used within `BuildDeferredIndexes` in `QueryIndexManager`.
* [GOCBC-1244](https://issues.couchbase.com/browse/GOCBC-1244): Updated SDK dependencies.
* [GOCBC-1254](https://issues.couchbase.com/browse/GOCBC-1254): Added `NewLoggingMeter` and `LoggingMeterOptions` for creating the `LoggingMeter`. `AggregatingMeterOptions` and `NewAggregatingMeter` will be deprecated in the next dot minor release.

#### [](#fixed-issues-30)Fixed Issues

* [GOCBC-1248](https://issues.couchbase.com/browse/GOCBC-1248): Fixed issue where a hard close of a memdclient during a graceful close could trigger a panic.
* [GOCBC-1251](https://issues.couchbase.com/browse/GOCBC-1251): Fixed issue where `SearchOptions` `ConsistentWith` was using an incorrect key within the JSON payload.
* [GOCBC-1256](https://issues.couchbase.com/browse/GOCBC-1256): Fixed issue where config polling could fallback to using the http poller, when no http addresses are registered for use.
* [GOCBC-1258](https://issues.couchbase.com/browse/GOCBC-1258): Fixed issue where log redaction tags were not closed correctly.

### [](#version-2-4-0-16-february-2022)Version 2.4.0 (16 February 2022)

Version 2.4.0 is the first release in the Go SDK 2.4 series, adding multi-document distributed ACID transactions.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.4.0?tab=doc)

#### [](#new-features-and-behavioral-changes-25)New Features and Behavioral Changes

* [GOCBC-1172](https://issues.couchbase.com/browse/GOCBC-1172): Added uncommitted API stability support for Query option `PreserveExpiry`.
* [GOCBC-1176](https://issues.couchbase.com/browse/GOCBC-1176): Added uncommitted API stability support for collections to query index manager.
* [GOCBC-1239](https://issues.couchbase.com/browse/GOCBC-1239): Added `DurabilityLevelUnknown` as default durability level.
* [TXNG-127](https://issues.couchbase.com/browse/GOCBC-TXNG-127): Integrated transactions into the SDK.

#### [](#fixed-issues-31)Fixed Issues

* [GOCBC-1240](https://issues.couchbase.com/browse/GOCBC-1240): Fixed issue where `MutateIn` was not setting durability level.

## [](#go-sdk-2-3-releases)Go SDK 2.3 Releases

### [](#version-2-3-5-14-december-2021)Version 2.3.5 (14 December 2021)

Version 2.3.5 is a maintenance release for the Go SDK 2.3.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.3.5?tab=doc)

#### [](#new-features-and-behavioral-changes-26)New Features and Behavioral Changes

* [GOCBC-1152](https://issues.couchbase.com/browse/GOCBC-1152): Added uncommitted API stability support for custom conflict resolution to `BucketSettings`.
* [GOCBC-1156](https://issues.couchbase.com/browse/GOCBC-1156); Added volatile API stability support for `includeLocations` to `SearchOptions` and `Operator` to search `MatchQuery`.
* [GOCBC-1175](https://issues.couchbase.com/browse/GOCBC-1175): Added uncommitted API stability support for `storageBackend` to `BucketSettings`.
* [GOCBC-1196](https://issues.couchbase.com/browse/GOCBC-1196): Added the `ErrorText` of the response body field to `AnalyticsError`, `SearchError`, `ManagementError`, and `ViewError`, to allow easier debugging and error handling. Renamed the `ResponseBody` of the `QueryError` to be `ErrorText` and contain only the error text. Added the `StatusCode` of the response to `AnalyticsError`, `QueryError`, `ManagementError`, and `ViewError`.
* [GOCBC-1200](https://issues.couchbase.com/browse/GOCBC-1200): Renamed `ErrRateLimiting` and `ErrQuotaLimiting` to `ErrRateLimited` and `ErrQuotaLimited`. Note: this is a breaking change, it not expected to impact any users.

#### [](#fixed-issues-32)Fixed Issues

* [GOCBC-1202](https://issues.couchbase.com/browse/GOCBC-1202):
* [GOCBC-1211](https://issues.couchbase.com/browse/GOCBC-1211): Fixed issues relating to rate limit error message parsing.
* [GOCBC-1210](https://issues.couchbase.com/browse/GOCBC-1210): Fixed issue where a quota limit error was returned rather than rate limit error for key value response status code 0x32.

### [](#version-2-3-4-16-november-2021)Version 2.3.4 (16 November 2021)

Version 2.3.4 is a maintenance release for the Go SDK 2.3.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.3.4?tab=doc)

#### [](#new-features-and-behavioral-changes-27)New Features and Behavioral Changes

* [GOCBC-1179](https://issues.couchbase.com/browse/GOCBC-1179): Added support to attempt graceful closing of connections.
* [GOCBC-1154](https://issues.couchbase.com/browse/GOCBC-1154); [GOCBC-1184](https://issues.couchbase.com/browse/GOCBC-1184): Added RateLimitFailure and QuotaLimitFailure support for Couchbase Capella.
* [GOCBC-1193](https://issues.couchbase.com/browse/GOCBC-1193): Added the ResponseBody field to QueryError, to allow easier debugging and error handling.

#### [](#fixed-issues-33)Fixed Issues

* [GOCBC-1185](https://issues.couchbase.com/browse/GOCBC-1185): Fixed an issue with Queue and Set retrying during pop and remove operations.
* [GOCBC-1186](https://issues.couchbase.com/browse/GOCBC-1186): Fixed issue where logging meter could cause a deadlock on closing the cluster object.
* [GOCBC-1187](https://issues.couchbase.com/browse/GOCBC-1187): Fixed issue where logging meter could log a service/operation pair which has no operations.
* [GOCBC-1194](https://issues.couchbase.com/browse/GOCBC-1194): Changed ordering of route config bootstrapping, to check all seed nodes for the default network type first. This fixed an issue with stuck deployments using the Eventing service, after upgrade to server 7.0.2.

### [](#version-2-3-3-19-october-2021)Version 2.3.3 (19 October 2021)

Version 2.3.3 is a maintenance release for the Go SDK 2.3.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.3.3?tab=doc)

#### [](#new-features-and-behavioral-changes-28)New Features and Behavioral Changes

* [GOCBC-1178](https://issues.couchbase.com/browse/GOCBC-1178): We no longer remove poller controller watcher from cluster config updates.

#### [](#fixed-issues-34)Fixed Issues

* [GOCBC-1177](https://issues.couchbase.com/browse/GOCBC-1177): Fixed issue where a connection being closed by the server during bootstrap could cause the SDK to loop reconnect without backoff.
* [GOCBC-1183](https://issues.couchbase.com/browse/GOCBC-1183): Fixed issue where SSL certificates were be not verified when no root CAs were provided.

### [](#version-2-3-2-21-september-2021)Version 2.3.2 (21 September 2021)

Version 2.3.2 is a maintenance release for the Go SDK 2.3.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.3.2?tab=doc)

#### [](#new-features-and-behavioral-changes-29)New Features and Behavioral Changes

* [GOCBC-1009](https://issues.couchbase.com/browse/GOCBC-1009): Add support for Eventing function management.
* [GOCBC-1166](https://issues.couchbase.com/browse/GOCBC-1166): Check error codes and fallback to parsing messages in query index management.

#### [](#fixed-issues-35)Fixed Issues

* [GOCBC-1168](https://issues.couchbase.com/browse/GOCBC-1168): Fixed issue where cluster level HTTP operations could hang indefinitely.
* [GOCBC-1170](https://issues.couchbase.com/browse/GOCBC-1170): Fixed issue where Search `ScanConsistency` was sending an incorrect value for `NotBounded`.

### [](#version-2-3-1-17-august-2021)Version 2.3.1 (17 August 2021)

Version 2.3.1 is a maintenance release for the Go SDK 2.3.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.3.1?tab=doc)

#### [](#fixed-issues-36)Fixed Issues

* [GOCBC-1140](https://issues.couchbase.com/browse/GOCBC-1140): Fixed issue where `ViewOptions` would return an error when using `group_level`.
* [GOCBC-1144](https://issues.couchbase.com/browse/GOCBC-1144): Added missing `min` function to `Disjunction` search query.
* [GOCBC-1147](https://issues.couchbase.com/browse/GOCBC-1147): Fixed issue where an error occuring whilst fetching the error map during bootstrap could cause an indefinite hang.
* [GOCBC-1149](https://issues.couchbase.com/browse/GOCBC-1149): Fixed issue where `GetAllScopes` would panic on HTTP request send failure.

## [](#go-sdk-2-2-releases)Go SDK 2.2 Releases

### [](#version-2-2-5-17-august-2021)Version 2.2.5 (17 August 2021)

Version 2.2.5 is a maintenance release for the Go SDK 2.2.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.2.5?tab=doc)

#### [](#fixed-issues-37)Fixed Issues

* [GOCBC-1147](https://issues.couchbase.com/browse/GOCBC-1147): Fixed issue where an error occuring whilst fetching the error map during bootstrap could cause an indefinite hang.
* [GOCBC-1149](https://issues.couchbase.com/browse/GOCBC-1149): Fixed issue where `GetAllScopes` would panic on HTTP request send failure.

### [](#version-2-3-0-15-july-2021)Version 2.3.0 (15 July 2021)

Version 2.3.0 is the first release in the Go SDK 2.3 series.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.3.0?tab=doc)

#### [](#new-features-and-behavioral-changes-30)New Features and Behavioral Changes

* [GOCBC-935](https://issues.couchbase.com/browse/GOCBC-935): Added support for Analytics remote and external link management.
* [GOCBC-936](https://issues.couchbase.com/browse/GOCBC-936): Added support for compound dataverse names to Analytics management.
* [GOCBC-940](https://issues.couchbase.com/browse/GOCBC-940):
* [GOCBC-1096](https://issues.couchbase.com/browse/GOCBC-1096): Updated the tracing interface, and made it API stability level committed.
* [GOCBC-1037](https://issues.couchbase.com/browse/GOCBC-1037): Added support for `PreserveExpiry` option to key value operations.
* [GOCBC-1044](https://issues.couchbase.com/browse/GOCBC-1044): Added support for meter interface, and default `LoggingMeter` implementation.
* [GOCBC-1063](https://issues.couchbase.com/browse/GOCBC-1063): Added uncommitted support for `context.Context` to options blocks.
* [GOCBC-1077](https://issues.couchbase.com/browse/GOCBC-1077): Updated errors returned on Query error code return of 12009.
* [GOCBC-1130](https://issues.couchbase.com/browse/GOCBC-1130): Updated Query error handling to return an authentication error on error code 13104.

#### [](#fixed-issues-38)Fixed Issues

* [GOCBC-1095](https://issues.couchbase.com/browse/GOCBC-1095): Fixed issue where View error contents were being parsed incorrectly.
* [GOCBC-1100](https://issues.couchbase.com/browse/GOCBC-1100): Fixed issue where the Search metrics `took` field was being parsed incorrectly.
* [GOCBC-1106](https://issues.couchbase.com/browse/GOCBC-1106): Fixed issue where a Search response containing a `hits` field but the field being `null` would lead to an error.
* [GOCBC-1111](https://issues.couchbase.com/browse/GOCBC-1111): Fixed issue where any errors returned from the Search service were not being propagated through the SDK.
* [GOCBC-1127](https://issues.couchbase.com/browse/GOCBC-1127): Fixed issue where Query errors were sometimes not being parsed correctly.
* [GOCBC-1132](https://issues.couchbase.com/browse/GOCBC-1132): Fixed issue where benchmarks would not compile.

### [](#version-2-2-4-15-june-2021)Version 2.2.4 (15 June 2021)

Version 2.2.4 is a maintenance release for the Go SDK 2.2.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.2.4?tab=doc)

#### [](#fixed-issues-39)Fixed Issues

* [GOCBC-1095](https://issues.couchbase.com/browse/GOCBC-1095): Fixed issue where errors returned from views was parsed incorrectly.
* [GOCBC-1102](https://issues.couchbase.com/browse/GOCBC-1102): Fixed issue where `WaitUntilReady` would never recover if one of the HTTP based services returned an error.
* [GOCBC-1106](https://issues.couchbase.com/browse/GOCBC-1106): Fixed issue where `hits` being `null` in a search response would leave to an internal error.
* [GOCBC-1111](https://issues.couchbase.com/browse/GOCBC-1111); [GOCBC-1112](https://issues.couchbase.com/browse/GOCBC-1112): Fixed issue where parsing search errors was using the incorrect field.
* [GOCBC-1100](https://issues.couchbase.com/browse/GOCBC-1100): Fixed issue where the `took` field in search metrics was parsed incorrectly.

### [](#version-2-2-3-20-april-2021)Version 2.2.3 (20 April 2021)

Version 2.2.3 is a maintenance release for the Go SDK 2.2.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.2.3?tab=doc)

#### [](#new-features-and-behavioral-changes-31)New Features and Behavioral Changes

* [GOCBC-1071](https://issues.couchbase.com/browse/GOCBC-1071): Updated SDK to use new protocol level changes for get collection id.
* [GOCBC-1068](https://issues.couchbase.com/browse/GOCBC-1068): Dropped log level to warn for when applying a cluster config object is preempted.
* [GOCBC-1079](https://issues.couchbase.com/browse/GOCBC-1079): During bootstrap don't retry authentication if the error is request cancelled.
* [GOCBC-1081](https://issues.couchbase.com/browse/GOCBC-1081): During CCCP polling don't retry request if the error is request cancelled.

#### [](#fixed-issues-40)Fixed Issues

* [GOCBC-1074](https://issues.couchbase.com/browse/GOCBC-1074): Fixed issue where threshold log tracer was missing fields in log output.
* [GOCBC-1080](https://issues.couchbase.com/browse/GOCBC-1080): Fixed issue where SDK would always rebuild connections on first cluster config fetched against server 7.0.
* [GOCBC-1082](https://issues.couchbase.com/browse/GOCBC-1082): Fixed issue where bootstrapping a node during an SDK wide reconnect would cause a delay in connecting to that node.
* [GOCBC-1088](https://issues.couchbase.com/browse/GOCBC-1088): Fixed issue where the poller controller could deadlock if a node reported a bucket not found at the same time as CCCP successfully fetched a cluster config for the first time.

### [](#version-2-2-2-16-march-2021)Version 2.2.2 (16 March 2021)

Version 2.2.2 is a maintenance release for the Go SDK 2.2.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.2.2?tab=doc)

#### [](#new-features-and-behavioral-changes-32)New Features and Behavioral Changes

* [GOCBC-1010](https://issues.couchbase.com/browse/GOCBC-1010): Added uncommitted support for collections to `SearchOptions`.
* [GOCBC-1024](https://issues.couchbase.com/browse/GOCBC-1024): Added partition information to `QueryIndex`.
* [GOCBC-1056](https://issues.couchbase.com/browse/GOCBC-1056): Various performance enhancements to improve CPU usage.
* [GOCBC-1068](https://issues.couchbase.com/browse/GOCBC-1068): Dropped log level to warn for when applying a cluster config object is preempted.

#### [](#fixed-issues-41)Fixed Issues

* [GOCBC-1070](https://issues.couchbase.com/browse/GOCBC-1070): Fixed issue where `BucketManager` `FlushBucket` didn't return `ErrBucketNotFound` when the bucket doesn't exist.
* [GOCBC-1066](https://issues.couchbase.com/browse/GOCBC-1066): Fixed issue where shutting down cluster config polling could lead to a panic.

### [](#version-2-2-1-16-february-2021)Version 2.2.1 (16 February 2021)

Version 2.2.1 is a maintenance release for the Go SDK 2.2.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.2.1?tab=doc)

#### [](#new-features-and-behavioral-changes-33)New Features and Behavioral Changes

* [GOCBC-1017](https://issues.couchbase.com/browse/GOCBC-1017): Updated server endpoints for collections manager.
* [GOCBC-1040](https://issues.couchbase.com/browse/GOCBC-1040): Updated json serialization of errors to include the underlying cause.
* [GOCBC-1054](https://issues.couchbase.com/browse/GOCBC-1054): Updated `MutateIn` to allow a blank path with `RemoveSpec`.

#### [](#fixed-issues-42)Fixed Issues

* [GOCBC-1047](https://issues.couchbase.com/browse/GOCBC-1047): Fixed issue where `GetAllScopes` was not setting the max expiry value for any collections.
* [GOCBC-1052](https://issues.couchbase.com/browse/GOCBC-1052): Fixed issue where `GetAllDesignDocuments` was ignoring the provided `namespace`.
* [GOCBC-1061](https://issues.couchbase.com/browse/GOCBC-1061): Fixed issue where an extra, empty, origin was added to user roles on fetching the user.

### [](#version-2-2-0-15-december-2020)Version 2.2.0 (15 December 2020)

Version 2.2.0 is the first release in the Go SDK 2.2 series. It brings enhancements and bug fixes over 2.1.8, and improves compatibility with Server 6.6 and with 7.0β.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.2.0?tab=doc)

#### [](#new-features-and-behavioral-changes-34)New Features and Behavioral Changes

* [GOCBC-869](https://issues.couchbase.com/browse/GOCBC-869): `BucketSettings` `MaxTTL` field deprecated in favour of `MaxExpiry`.
* [GOCBC-934](https://issues.couchbase.com/browse/GOCBC-934): Added support for bucket level durability settings in `BucketManager`.
* [GOCBC-948](https://issues.couchbase.com/browse/GOCBC-948): Changed document expiry durations so that expiry lengths of > 30 days sent as unix timestamps (now + expiry).
* [GOCBC-934](https://issues.couchbase.com/browse/GOCBC-934): Added support for bucket level durability settings in `BucketManager`.
* [GOCBC-963](https://issues.couchbase.com/browse/GOCBC-963): `GetResult` `Expiry` function deprecated in favour of `ExpiryTime`.
* [GOCBC-972](https://issues.couchbase.com/browse/GOCBC-972): Added support for `Score` to `SearchOptions`.
* [GOCBC-1014](https://issues.couchbase.com/browse/GOCBC-1014): Updated search `GeoPolygon` support to API stability committed.
* [GOCBC-1015](https://issues.couchbase.com/browse/GOCBC-1015): Updated `QueryOptions` `FlexIndex` support to API stability committed.
* [GOCBC-1026](https://issues.couchbase.com/browse/GOCBC-1026): Updated `BucketSettings` ephemeral eviction policies support to API stability committed.

#### [](#fixed-issues-43)Fixed Issues

* [GOCBC-1022](https://issues.couchbase.com/browse/GOCBC-1022): Fixed issue where having multiple buckets open could cause view requests to be sent to an incorrect bucket.
* [GOCBC-1021](https://issues.couchbase.com/browse/GOCBC-1021): Fixed issue where having multiple buckets open could cause view manager requests to be sent to an incorrect bucket.
* [GOCBC-1028](https://issues.couchbase.com/browse/GOCBC-1028): Fixed issue where bootstrapping against a non-kv node could never successfully fully connect.

## [](#go-sdk-2-1-releases)Go SDK 2.1 Releases

### [](#version-2-1-8-17-november-2020)Version 2.1.8 (17 November 2020)

Version 2.1.8 is a maintenance release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.8?tab=doc)

#### [](#new-features-and-behavioral-changes-35)New Features and Behavioral Changes

* [GOCBC-937](https://issues.couchbase.com/browse/GOCBC-937): Added uncommitted support for `GeoPolygon` search queries.
* [GOCBC-1005](https://issues.couchbase.com/browse/GOCBC-1005): Added document id to key value errors.
* [GOCBC-1006](https://issues.couchbase.com/browse/GOCBC-1006): Changed the log level for retry strategy retries from info to debug.

#### [](#fixed-issues-44)Fixed Issues

* [GOCBC-1007](https://issues.couchbase.com/browse/GOCBC-1007): Fixed issue some operations were being incorrectly sent to the retry orchestrator on errors.

### [](#version-2-1-7-20-october-2020)Version 2.1.7 (20 October 2020)

Version 2.1.7 is a maintenance release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.7?tab=doc)

#### [](#new-features-and-behavioral-changes-36)New Features and Behavioral Changes

* [GOCBC-938](https://issues.couchbase.com/browse/GOCBC-938): Added uncommitted support for `FlexIndex` to `QueryOptions`.
* [GOCBC-942](https://issues.couchbase.com/browse/GOCBC-942): Added uncommitted support for `Scope` level queries.
* [GOCBC-944](https://issues.couchbase.com/browse/GOCBC-944): Added uncommitted support for `Scope` level analytics queries.
* [GOCBC-944](https://issues.couchbase.com/browse/GOCBC-944): Added uncommitted support for `User` collections level RBAC.
* [GOCBC-994](https://issues.couchbase.com/browse/GOCBC-994): Fixed issue where nil values used in subdoc `MutateIn` operations would be rejected by the server. These values are now coerced into JSON `null` values before sending.
* [GOCBC-1001](https://issues.couchbase.com/browse/GOCBC-1001): Added missing `Terms`, `DateRanges`, and `NumericRanges` fields to `SearchFacetResult`.

#### [](#fixed-issues-45)Fixed Issues

* [GOCBC-977](https://issues.couchbase.com/browse/GOCBC-977): Fixed issue where analytics `GetPendingMutations` was looking for the incorrect data structure in the HTTP response body.
* [GOCBC-990](https://issues.couchbase.com/browse/GOCBC-990): Fixed issue where enhanced durability timeout adaptive algorithm was incorrect.
* [GOCBC-991](https://issues.couchbase.com/browse/GOCBC-991): Fixed issue where authentication mechanisms were not correctly iterated on bootstrap.
* [GOCBC-996](https://issues.couchbase.com/browse/GOCBC-996): Fixed issue where the `Map` datastructure was using invalid paths for `At` and `Exists`.

### [](#version-2-1-6-15-september-2020)Version 2.1.6 (15 September 2020)

Version 2.1.6 is a maintenance release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.6?tab=doc)

#### [](#new-features-and-behavioral-changes-37)New Features and Behavioral Changes

* [GOCBC-979](https://issues.couchbase.com/browse/GOCBC-979): Add ExpiryTime to GetResult, providing the point in time at which a document will expire.

#### [](#fixed-issues-46)Fixed Issues

* [GOCBC-969](https://issues.couchbase.com/browse/GOCBC-969): Fixed issue where the SDK would attempt to parse query metrics even if they weren't present.
* [GOCBC-976](https://issues.couchbase.com/browse/GOCBC-976): Fixed issue where custom transcoders were not supported for performing a get request with expiry.
* [GOCBC-978](https://issues.couchbase.com/browse/GOCBC-978): Fixed issue where it was possible for more than one request to trigger switching from unknown to pending state for a given collection.
* [GOCBC-981](https://issues.couchbase.com/browse/GOCBC-981): Fixed issue where setting the `network` connection string property to `default` would be discarded.

### [](#version-2-1-5-18-august-2020)Version 2.1.5 (18 August 2020)

Version 2.1.5 is a maintenance release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.5?tab=doc)

#### [](#new-features-and-behavioral-changes-38)New Features and Behavioral Changes

* [GOCBC-926](https://issues.couchbase.com/browse/GOCBC-926): Added a new `Cluster` level option to set which authentication mechanisms to use.
* [GOCBC-962](https://issues.couchbase.com/browse/GOCBC-962): Exposed the `ThresholdLogTracer` and corresponding options so that threshold logging can be configured. The threshold logger can then be set on the `Cluster` level options as `Tracer`. Note: The threshold logger is the default tracer used by the SDK.

#### [](#fixed-issues-47)Fixed Issues

* [GOCBC-718](https://issues.couchbase.com/browse/GOCBC-718): Fixed issue where errors would be silently swallwed when performing JSON unmarshalling of search and view queries. Unmarshalling errors will now be surfaced by the `result.Err()` function after iterating results.
* [GOCBC-950](https://issues.couchbase.com/browse/GOCBC-950): Fixed issue where the SDK was not performing HELLO with the JSON feature enabled, leading to some KV error message context being lost.
* [GOCBC-968](https://issues.couchbase.com/browse/GOCBC-968): Fixed issue where n1ql indexes were being created using prepared statements.

### [](#version-2-1-4-21-july-2020)Version 2.1.4 (21 July 2020)

Version 2.1.4 is a maintenance release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.4?tab=doc)

#### [](#new-features-and-behavioral-changes-39)New Features and Behavioral Changes

* [GOCBC-889](https://issues.couchbase.com/browse/GOCBC-889): Added support for remaining service types to `WaitUntilReadyOptions`.
* [GOCBC-932](https://issues.couchbase.com/browse/GOCBC-932): Added support for ephemeral bucket eviction types in the `BucketManager`.
* [GOCBC-951](https://issues.couchbase.com/browse/GOCBC-951): Adjusted the default max idle http connection timeout to be 4.5s from unlimited.

#### [](#fixed-issues-48)Fixed Issues

* [GOCBC-925](https://issues.couchbase.com/browse/GOCBC-925): Fixed issue where errors could not be accessed for queries responding with a HTTP 200 status code but containing errors. Any errors that are included in the query response when the status code is 200 will now be surfaced through the result `Err` call.
* [GOCBC-928](https://issues.couchbase.com/browse/GOCBC-928): Fixed issue where enhanced durability could be incorrectly flagged as unsupported.
* [GOCBC-931](https://issues.couchbase.com/browse/GOCBC-931): Fixed issue where enhanced durability timeouts were being sent as seconds rather than milliseconds.
* [GOCBC-945](https://issues.couchbase.com/browse/GOCBC-945): Fixed issue where ephemeral buckets could not be created using the `BucketManager`.
* [GOCBC-946](https://issues.couchbase.com/browse/GOCBC-946): Fixed issue where `MaxTTL` was being sent as nanoseconds rather than seconds when creating buckets using the `BucketManager`.
* [GOCBC-955](https://issues.couchbase.com/browse/GOCBC-955): Fixed issue where xattrs were being reordered when being moved to the front of the list in subdoc operations.

### [](#version-2-1-3-1-july-2020)Version 2.1.3 (1 July 2020)

Version 2.1.3 is an off-cadence release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.3?tab=doc)

#### [](#fixed-issues-49)Fixed Issues

* [GOCBC-941](https://issues.couchbase.com/browse/GOCBC-941): Fixed issue where `WaitUntilReady` at the `Cluster` level would always timeout.

### [](#version-2-1-2-16-june-2020)Version 2.1.2 (16 June 2020)

Version 2.1.2 is a maintenance release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.2?tab=doc)

#### [](#new-features-and-behavioral-changes-40)New Features and Behavioral Changes

* [GOCBC-907](https://issues.couchbase.com/browse/GOCBC-907): Enhance search query errors to include the index name and error text from the server.
* [GOCBC-913](https://issues.couchbase.com/browse/GOCBC-913): Ensure that only available services are used for Ping if no services specified.
* [GOCBC-923](https://issues.couchbase.com/browse/GOCBC-923): Updated const declarations to add types to improve API reference.

#### [](#fixed-issues-50)Fixed Issues

* [GOCBC-879](https://issues.couchbase.com/browse/GOCBC-879), [GOCBC-890](https://issues.couchbase.com/browse/GOCBC-890): Fixed issue causing `Cluster` level operations to return errors when performed before underlying cluster or bucket connections are ready. These operations (query, search, analytics, views, management APIs) will now behave like key value operations - waiting for connections to be ready before they are sent. The [WaitUntilReady](https://docs.couchbase.com/go-sdk/2.1/howtos/managing-connections.html#waiting-for-bootstrap-completion) call can still be used for verifying that connections are ready.
* [GOCBC-891](https://issues.couchbase.com/browse/GOCBC-891): Fixed issue where the `Name` property of a `Role` was being sent as the incorrect json field name.
* [GOCBC-897](https://issues.couchbase.com/browse/GOCBC-897): Fixed issue where operations with incredible short timeouts (timing out before operation sent) could cause a data race.
* [GOCBC-900](https://issues.couchbase.com/browse/GOCBC-900): Fixed issue where `IgnoreIfExists` option was being ignored for query index management.
* [GOCBC-906](https://issues.couchbase.com/browse/GOCBC-906): Fixed issue where enhanced durability could be incorrectly set as unsupported on early operations.
* [GOCBC-914](https://issues.couchbase.com/browse/GOCBC-914): Fixed issue where operations using named collections could be sent with an incorrect collection ID in queued before the collection is known.

### [](#known-issues-2)Known issues

* [GOCBC-941](https://issues.couchbase.com/browse/GOCBC-941): Performing `Cluster` level `WaitUntilReady` never completes within the timeout. This issue was introduced whilst fixing the behaviour for operations at the `Cluster` level when the `WaitUntilReady` call is not used. The workaround for this is to not use the `Cluster` level `WaitUntilReady` call, `Cluster` level operations will now be queued until the SDK has connected and setup anyway.

### [](#version-2-1-1-19-may-2020)Version 2.1.1 (19 May 2020)

Version 2.1.1 is a maintenance release for the Go SDK 2.1.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.1?tab=doc)

#### [](#new-features-and-behavioral-changes-41)New Features and Behavioral Changes

* [GOCBC-778](https://issues.couchbase.com/browse/GOCBC-778): Updated legacy durability polling to use a backoff rather than a fixed interval.
* [GOCBC-824](https://issues.couchbase.com/browse/GOCBC-824): Enhanced timeout errors to contain more information and match up with the [Response Time Observability RFC](https://github.com/couchbaselabs/sdk-rfcs/blob/master/rfc/0035-rto.md).
* [GOCBC-828](https://issues.couchbase.com/browse/GOCBC-828): Added `MaxExpiry` to the `CollectionSpec`.
* [GOCBC-870](https://issues.couchbase.com/browse/GOCBC-870): Updated `GetAllIndexes` to only fetch GSI indexes.
* [GOCBC-884](https://issues.couchbase.com/browse/GOCBC-884): Improved logging to always log the cluster config when fetched.
* [GOCBC-888](https://issues.couchbase.com/browse/GOCBC-888): Re-enabled HTTP dispatch traces.

#### [](#fixed-issues-51)Fixed Issues

* [GOCBC-691](https://issues.couchbase.com/browse/GOCBC-691): Fixed issue where operations on unknown collections (when using 6.5 developer preview) are not automatically retried.
* [GOCBC-757](https://issues.couchbase.com/browse/GOCBC-757): Fixed issue where an array of arrays could cause a failure when using `Get` with `Projections`.
* [GOCBC-882](https://issues.couchbase.com/browse/GOCBC-882): Fixed issue where an invalid cluster config would trigger a shutdown of the underlying core SDK causing operations to fail.
* [GOCBC-884](https://issues.couchbase.com/browse/GOCBC-884): Fixed issue where `UpsertUser` sent an invalid request if a role was specified with no bucket.

#### [](#known-issues-3)Known issues

* [GOCBC-879](https://issues.couchbase.com/browse/GOCBC-879), [GOCBC-890](https://issues.couchbase.com/browse/GOCBC-890): Performing `Cluster` level operations (query, search, management APIs) before underlying cluster or bucket connections are ready causes errors to be returned. To mitigate this the `err := WaitUntilReady(time.Duration, WaitUntilReadyOptions)` operation can be used on either `Cluster` or `Bucket` which will either:

  1. Return no error if connections are setup and ready for use
  2. Return a `TimeoutError` if connections are not ready within the specified time limit.

### [](#version-2-1-0-21-april-2020)Version 2.1.0 (21 April 2020)

Version 2.1.0 is a maintenance release for the Go SDK 2.0.0\. This release contains updating to a new major release of the core part of the SDK.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.1.0?tab=doc)

#### [](#new-features-and-behavioral-changes-42)New Features and Behavioral Changes

* [GOCBC-843](https://issues.couchbase.com/browse/GOCBC-843): Updated to the new version of gocbcore. This change includes a key behavioral change of no longer reporting non-configuration related connect time errors.
* [GOCBC-845](https://issues.couchbase.com/browse/GOCBC-845): Add support for the `WaitForReady` operation, support waiting for the KeyValue service to be ready.

## [](#go-sdk-2-0-releases)Go SDK 2.0 Releases

### [](#version-2-0-4-21-april-2020)Version 2.0.4 (21 April 2020)

Version 2.0.4 is a maintenance release for the Go SDK 2.0.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.0.4?tab=doc)

#### [](#new-features-and-behavioral-changes-43)New Features and Behavioral Changes

* [GOCBC-844](https://issues.couchbase.com/browse/GOCBC-844): Updated to the latest version of gocbconnstr.

#### [](#fixed-issues-52)Fixed Issues

* [GOCBC-838](https://issues.couchbase.com/browse/GOCBC-838): Fixed issue where HTTP endpoints were being used when SSL is enabled.
* [GOCBC-851](https://issues.couchbase.com/browse/GOCBC-851): Fixed issue where `ServerName` was not being set on the `tls.Config` when SSL was use.
* [GOCBC-853](https://issues.couchbase.com/browse/GOCBC-853): Fixed issue where using `PasswordAuthenticator` with a root CA and SSL would cause a panic.
* [GOCBC-831](https://issues.couchbase.com/browse/GOCBC-831): Fixed issue where search consistency options were not being set in the request payload.

### [](#version-2-0-3-17-march-2020)Version 2.0.3 (17 March 2020)

Version 2.0.3 is a maintenance release for the Go SDK 2.0.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.0.3?tab=doc)

#### [](#new-features-and-behavioral-changes-44)New Features and Behavioral Changes

* [GOCBC-662](https://issues.couchbase.com/browse/GOCBC-662): The server requires that any subdoc xattr ops are at the beginning of the ops list. If the user provides an ops list containing subdoc xattr ops out of order, the SDK will now reorder it for them and then reorder it back again when it gets the result. This ensures that `ContentAt` works as expected.
* [GOCBC-700](https://issues.couchbase.com/browse/GOCBC-700): Made improvements to errors returned from management operations. They now provide more contextual information.
* [GOCBC-716](https://issues.couchbase.com/browse/GOCBC-716): SDK now returns a `FlushNotEnabled` error if bucket flush not enabled.
* [GOCBC-719](https://issues.couchbase.com/browse/GOCBC-719): SDK now consistently creates tracing spans for all HTTP requests.
* [GOCBC-728](https://issues.couchbase.com/browse/GOCBC-728): Added cluster level Ping operation.
* [GOCBC-807](https://issues.couchbase.com/browse/GOCBC-807): Updated best effort retry strategy to use an exponential backoff calculator.
* [GOCBC-820](https://issues.couchbase.com/browse/GOCBC-820): Removed `context.Context` from search index manager operations. Note that whilst this is a breaking change it was deemed best to break it and make sure any users who are using it know that they are using unused functionality.

#### [](#fixed-issues-53)Fixed Issues

* [GOCBC-814](https://issues.couchbase.com/browse/GOCBC-814): Fixed issue where search was looking for incorrect field in the JSON response.
* [GOCBC-817](https://issues.couchbase.com/browse/GOCBC-817): Fixed issue where opening a bucket with the same name twice led to incorrect behaviour on both buckets.

### [](#version-2-0-2-21-february-2020)Version 2.0.2 (21 February 2020)

Version 2.0.2 is an off-cycle release for the Go SDK 2.0.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.0.2?tab=doc)

#### [](#new-features-and-behavioral-changes-45)New Features and Behavioral Changes

* [GOCBC-805](https://issues.couchbase.com/browse/GOCBC-805): Updated timeout behavior across the SDK to be consistent. If an operation level timeout is provided then it is used, otherwise the respective global timeout is used.

#### [](#fixed-issues-54)Fixed Issues

* [GOCBC-804](https://issues.couchbase.com/browse/GOCBC-804): Fixed issue with timeouts not being respected for HTTP requests, leading to them never timing out.

### [](#version-2-0-1-19-february-2020)Version 2.0.1 (19 February 2020)

Version 2.0.1 is a maintenance release for the Go SDK 2.0.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.0.1?tab=doc)

#### [](#new-features-and-behavioral-changes-46)New Features and Behavioral Changes

* [GOCBC-775](https://issues.couchbase.com/browse/GOCBC-775): Improve error message for when performing cluster level operations with no connections available.
* [GOCBC-776](https://issues.couchbase.com/browse/GOCBC-776): Added support for KVDurableTimeout.
* [GOCBC-786](https://issues.couchbase.com/browse/GOCBC-786): Improve error messages for the UserManager GetUser function.

#### [](#fixed-issues-55)Fixed Issues

* [GOCBC-701](https://issues.couchbase.com/browse/GOCBC-701): Fixed issue with enhanced prepared statements not being used.
* [GOCBC-702](https://issues.couchbase.com/browse/GOCBC-702): Fixed issue with CA root certificates not being able to be provided.
* [GOCBC-759](https://issues.couchbase.com/browse/GOCBC-759): Fixed issue with streaming results for HTTP based services timing out unexpectedly.
* [GOCBC-772](https://issues.couchbase.com/browse/GOCBC-772): Fixed issue with many of the management API functions timing out immediately.
* [GOCBC-773](https://issues.couchbase.com/browse/GOCBC-773): Fixed issue with queries that do not return rows (e.g. mutations) causing errors.
* [GOCBC-777](https://issues.couchbase.com/browse/GOCBC-777): Fixed issue with failing operations causing nil pointers.
* [GOCBC-783](https://issues.couchbase.com/browse/GOCBC-783): Fixed issue with Exists returning incorrectly if the document was recently deleted.
* [GOCBC-784](https://issues.couchbase.com/browse/GOCBC-784): Fixed issue with Unlock returning a doc not found error instead of cas mismatch.
* [GOCBC-787](https://issues.couchbase.com/browse/GOCBC-787): Fixed issue with some (xattr related) subdoc operations sending invalid packets.
* [GOCBC-789](https://issues.couchbase.com/browse/GOCBC-789): Fixed issue with search index manager FreezePlan function using an invalid HTTP method.
* [GOCBC-790](https://issues.couchbase.com/browse/GOCBC-790): Fixed issue with user manager sometimes parsing user role origins incorrectly.
* [GOCBC-796](https://issues.couchbase.com/browse/GOCBC-796): Fixed issue with cccp poller hanging if the get cluster config op timed out.

### [](#version-2-0-0-18-january-2020)Version 2.0.0 (18 January 2020)

Version 2.0.0 is the first release for the Go SDK 2.0.0.

[API Documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.0.0?tab=doc)

#### [](#new-features-and-behavioral-changes-47)New Features and Behavioral Changes

* [GOCBC-510](https://issues.couchbase.com/browse/GOCBC-510): Dropped support for connecting using the http scheme.
* [GOCBC-534](https://issues.couchbase.com/browse/GOCBC-534): Added support for retry handling.
* [GOCBC-652](https://issues.couchbase.com/browse/GOCBC-552): Added support for circuit breakers.
* [GOCBC-655](https://issues.couchbase.com/browse/GOCBC-655): Added support for enhanced timeout errors providing more information about operations which timeout.
* [GOCBC-656](https://issues.couchbase.com/browse/GOCBC-656): Added support for threshold logging tracer.
* [GOCBC-680](https://issues.couchbase.com/browse/GOCBC-680): Updated how we expose and handle errors.
* [GOCBC-694](https://issues.couchbase.com/browse/GOCBC-694): A large number of updates including: How query and analytics results are iterated. Minor renaming of various types. Moving search facets, sorting, and queries to a search subpackage. Removing serializers.
* [GOCBC-740](https://issues.couchbase.com/browse/GOCBC-740): Updated expiry options to be `time.Duration`.
* [GOCBC-760](https://issues.couchbase.com/browse/GOCBC-760): Moved authenticator to ClusterOptions.

### [](#pre-releases)Pre-releases

Numerous _Alpha_ and _Beta_ releases were made in the run-up to the 2.0 release, and although unsupported, the release notes and download links are retained for archive purposes [here](3.0-pre-release-notes.md).

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).