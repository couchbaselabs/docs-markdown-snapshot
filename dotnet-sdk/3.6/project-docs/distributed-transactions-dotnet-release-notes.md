[View original HTML](/dotnet-sdk/3.6/project-docs/distributed-transactions-dotnet-release-notes.html)

Couchbase Distributed ACID Transactions is distributed as a separate library for the .NET SDK. This page features the release notes for that library — for release notes, download links, and installation methods for the latest 3.x .NET SDK releases, see [the current Release Notes page](sdk-release-notes.md).

## [](#using-distributed-transactions)Using Distributed Transactions

See the [Distributed ACID Transactions concept doc](#7.1@server:learn:data/transactions.adoc) in the server documentation for details of how Couchbase implements transactions. The [Distributed Transactions HOWTO doc](../howtos/distributed-acid-transactions-from-the-sdk.md) walks you through all aspects of working with Distributed Transactions.

## [](#version-1-1-0-29-oct-2021)Version 1.1.0 (29 Oct 2021)

This is the first release of Query support in .NET Distributed ACID Transactions.

Along with Query support, this release includes

* Tracing and Telemetry support via IRequestTracer
* Custom Metadata Collection support
* Support for KV operations in any order on the same document.

### [](#known-issues)Known Issues

* This release is focused on features and correctness, and has not been optimized for performance issues.
* In order to prevent race conditions regarding out-of-order operations on the same document in-process, `AttemptContext` operations run inside the `Transactions.Run` lambda do not execute in parallel, even if run with `Task.Run`.

## [](#version-1-0-0-30-apr-2021)Version 1.0.0 (30 Apr 2021)

This is the first General Availability (GA) release of .NET Distributed ACID Transactions 1.0.0 for Couchbase Server 6.6.

Requires Couchbase Server 6.6.1 or above and Couchbase .NET client 3.1.4 or above. It is recommended you use the package on NuGet.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase.Transactions-1.0.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-transactions-dotnet-1.0.0) | [Nuget](https://www.nuget.org/packages/Couchbase.Transactions/1.0.0)

### [](#known-issues-2)Known Issues

* Initial release has not been extensively profiled for memory/CPU usage or other performance issues.

## [](#pre-releases)Pre-releases

Numerous _Alpha_ and _Beta_ releases were made in the run-up to the 1.0 release, and although unsupported, the release notes and download links are retained for archive purposes [here](distributed-transactions-dotnet-1.0-pre-release-notes.md).