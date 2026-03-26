---
title: Couchbase Distributed ACID Transactions for .NET SDK Pre-release Archive
  Release Notes
description: Historic release notes archive for the 1.0 pre-GA (Alpha &amp;
  Beta) Couchbase .NET Distributed ACID Transactions Releases.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/project-docs/pages/distributed-transactions-dotnet-1.0-pre-release-notes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.6@dotnet-sdk:project-docs:distributed-transactions-dotnet-1.0-pre-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.6/project-docs/distributed-transactions-dotnet-1.0-pre-release-notes.html)

# Couchbase Distributed ACID Transactions for .NET SDK Pre-release Archive Release Notes

> Release notes archive for the 1.0 Alpha & Beta Couchbase .NET Distributed ACID Transactions Releases. 

Couchbase Distributed ACID Transactions is distributed as a separate library for the .NET SDK.

In the run-up to the Couchbase .NET Distributed ACID Transactions 1.0 API releases, several αλφα and βετα releases were made. Their release notes are maintained here for archive purposes. The 1.0 series release notes proper can be found [here](distributed-transactions-dotnet-release-notes.md), and howto documentation can be found [here](../howtos/distributed-acid-transactions-from-the-sdk.md). Please note that none of the pre-releases listed below are supported; all _supported_ (GA) releases can be found [here](sdk-release-notes.md).

> [!WARNING]
> These are the pre-release α & β Release Notes maintained purely for archive and information purposes. These releases are unsupported. Supported (GA) releases can be found on the [.NET Transactions Release Notes page](distributed-transactions-dotnet-release-notes.md).

## [](#version-1-0-0-beta-1-3-november-2020)Version 1.0.0.beta.1 (3 November 2020)

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase.Transactions-1.0.0-beta.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-transactions-dotnet-1.0.0-beta.1) | [Nuget](https://www.nuget.org/packages/Couchbase.Transactions/1.0.0-beta.1)

### [](#known-issues)Known Issues

* Early beta has not been profiled for memory/cpu usage or other performance issues.
* Logging is minimal and tracing is not implemented.

### [](#fixed-issues)Fixed Issues

* [TXNN-51](https://issues.couchbase.com/browse/TXNN-51): Fixup CheckWriteWriteConflict implementation.
* [TXNN-33](https://issues.couchbase.com/browse/TXNN-33): preExistingStagedInsertFoundOneFailureTryingToGet Failure.
* [TXNN-38](https://issues.couchbase.com/browse/TXNN-38): Transactions leave out transaction metadata on the documents.
* [TXNN-40](https://issues.couchbase.com/browse/TXNN-40): Transaction Insert and rollback leaves behind an empty document.
* [TXNN-41](https://issues.couchbase.com/browse/TXNN-41): Transaction cannot perform two replaces on same document.
* [TXNN-42](https://issues.couchbase.com/browse/TXNN-42): MultiThreaded transaction does not delete a document if another thread updates it.
* [TXNN-48](https://issues.couchbase.com/browse/TXNN-48): StandardTest.insertStagesBackupMetadata fails because FitPerformer thinks it doesn't support AccessDeleted.
* [TXNN-52](https://issues.couchbase.com/browse/TXNN-52): Cleanup leaves sentinel for ATR entry, rather than removing entry.
* [TXNN-47](https://issues.couchbase.com/browse/TXNN-47): TXNN Fit Performer needs to implement Cleanup hooks.

### [](#new-features-and-behavioral-changes)New Features and Behavioral Changes.

* [TXNN-26](https://issues.couchbase.com/browse/TXNN-26): Get and GetOptional do the same thing and have the same return type.
* [TXNN-43](https://issues.couchbase.com/browse/TXNN-43): Transaction get throws Nullreference exception instead of DocumentNotFound.

## [](#version-1-0-0-alpha-1-13-october-2020)Version 1.0.0.alpha.1 (13 October 2020)

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase.Transactions-1.0.0-alpha.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-transactions-dotnet-1.0.0-alpha.1) | [Nuget](https://www.nuget.org/packages/Couchbase.Transactions/1.0.0-alpha.1)

### [](#fixed-issues-2)Fixed Issues

* [TXNN-15](https://issues.couchbase.com/browse/TXNN-15): Implement transaction Cleanup.
* [TXNN-16](https://issues.couchbase.com/browse/TXNN-16): Error Raising / Handling per spec.
* [TXNN-18](https://issues.couchbase.com/browse/TXNN-18): Using outdated ATR Ids.
* [TXNN-20](https://issues.couchbase.com/browse/TXNN-20): Should throw TransactionOperationFailed on individual op failure.
* [TXNN-28](https://issues.couchbase.com/browse/TXNN-28): Rename any awaitable methods that return Task to XxxAsync part 2.
* [TXNN-29](https://issues.couchbase.com/browse/TXNN-29): TransactionResult has a MutationToken but not a MutationState.
* [TXNN-30](https://issues.couchbase.com/browse/TXNN-30): Add UnstagingComplete to TransactionResult.

### [](#new-features-and-behavioral-changes-2)New Features and Behavioral Changes

* [TXNN-3](https://issues.couchbase.com/browse/TXNN-3): API stub for transactions.
* [TXNN-36](https://issues.couchbase.com/browse/TXNN-36): Rename to XXXAsync, part 3.
* [TXNN-1](https://issues.couchbase.com/browse/TXNN-1): Test Performer Bringup.
* [TXNN-2](https://issues.couchbase.com/browse/TXNN-2): Transactions API Implementation.
* [TXNN-4](https://issues.couchbase.com/browse/TXNN-4): Implement txn API: Get/Replace/Remove.
* [TXNN-5](https://issues.couchbase.com/browse/TXNN-5): Implement txn API: Core Loop.
* [TXNN-6](https://issues.couchbase.com/browse/TXNN-6): Implement txn API: Implement Rollback.
* [TXNN-11](https://issues.couchbase.com/browse/TXNN-11): Create Demo App in C#/.NET.
* [TXNN-13](https://issues.couchbase.com/browse/TXNN-13): Author C#/.NET documentation for Txns.
* [TXNN-22](https://issues.couchbase.com/browse/TXNN-22): Implement cleanup post transaction.
* [TXNN-7](https://issues.couchbase.com/browse/TXNN-7): Implement ExpirationOvertimeMode.
* [TXNN-34](https://issues.couchbase.com/browse/TXNN-34): Make Couchbase.FitPerformer a friend assembly.
* [TXNN-10](https://issues.couchbase.com/browse/TXNN-10): Update transactions-fit-performer to latest couchbase-transactions-dotnet.
* [TXNN-25](https://issues.couchbase.com/browse/TXNN-25): Rename any awaitable methods that return Task to XxxAsync.
* [TXNN-35](https://issues.couchbase.com/browse/TXNN-35): Various refactorings to remove compiler warnings in FitPerformer.
* [TXNN-17](https://issues.couchbase.com/browse/TXNN-17): Finish implementing CheckWriteWrite.
* [TXNN-37](https://issues.couchbase.com/browse/TXNN-37): Add ILoggerFactory to TransactionsConfig.