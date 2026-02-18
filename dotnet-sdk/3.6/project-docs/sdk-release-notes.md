---
title: Couchbase .NET SDK Release Notes and Archives
description: Release notes and download archive for the Couchbase .NET Client.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/dotnet-sdk/3.6/project-docs/sdk-release-notes.html)

# Couchbase .NET SDK Release Notes and Archives

> Release notes and download archive for the Couchbase .NET Client. 

These pages cover the 3._x_ versions of the Couchbase .NET SDK. For release notes, download links, and installation methods for 2.7 and earlier releases of the Couchbase .NET Client, please see the [2.x .NET Release Notes & Download Archive](https://docs-archive.couchbase.com/dotnet-sdk/2.7/sdk-release-notes.html).

The full installation instructions that were previously on this page can now be found [here](sdk-full-installation.md).

## [](#latest-release).NET SDK 3.7 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-3-7-2)Version 3.7.2

[Download](https://packages.couchbase.com/clients/net/3.7/Couchbase-Net-Client-3.7.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.7.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.7.2)

#### [](#fixed-issues)Fixed Issues

* [NCBC-4027](https://couchbasecloud.atlassian.net/browse/NCBC-4027): `ForceIpAsTargetHost` is now `false` by default. This is in line with most production needs, and will prevent hostname verification failing (since TLS certificates are tied to the hostname).
* [NCBC-3715](https://couchbasecloud.atlassian.net/browse/NCBC-3715): For Cloud Native Gateway \[CNG\]: Subdoc Mutation Array now handles `removeBrackets` bool properly.
* [NCBC-4017](https://couchbasecloud.atlassian.net/browse/NCBC-4017): `ReplaceAsync` CAS field is now properly set on the operation.

#### [](#improvements)Improvements

* [NCBC-4026](https://couchbasecloud.atlassian.net/browse/NCBC-4026): Upgraded `Grpc.Net.Client` and other related `Grpc` dependencies, owing to [CVE-2023-32731](https://nvd.nist.gov/vuln/detail/CVE-2023-32731) ([GHSA-cfgp-2977-2fmm](https://osv.dev/vulnerability/GHSA-cfgp-2977-2fmm))
* [NCBC-4008](https://couchbasecloud.atlassian.net/browse/NCBC-4008): CNG: Some new `BucketSettings` fields have been added to the request.
* [NCBC-4016](https://couchbasecloud.atlassian.net/browse/NCBC-4016): CNG: Passing `null` content for `Insert`, `Replace`, or `Upsert` now throws `InvalidArgumentException`.
* [NCBC-4025](https://couchbasecloud.atlassian.net/browse/NCBC-4025): `Append` and `Prepend` now write the CAS field to the operation.

### [](#version-3-7-1-7-may-2025)Version 3.7.1 (7 May 2025)

[Download](https://packages.couchbase.com/clients/net/3.7/Couchbase-Net-Client-3.7.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.7.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.7.1)

#### [](#fixed-issues-2)Fixed Issues

* [NCBC-4002](https://couchbasecloud.atlassian.net/browse/NCBC-4002): Fixed an issue specific to .NET Framework when streaming HTTP results larger than 2GB, causing an OOM error (`Cannot write more bytes to the buffer than the configured maximum buffer size`).

#### [](#improvements-2)Improvements

* [NCBC-3992](https://couchbasecloud.atlassian.net/browse/NCBC-3992): `KvIgnoreRemoteCertificateNameMismatch = true` was clearing other `RemoteCertificateChainErrors`. Further validation has been added, and this no longer occurs.  
> [!IMPORTANT]  
> For use with SSL and certificates which contain the hostname (versus an IP address), with SDK 3.7.1, set `ForceIpAsTargetHost = false` as a `ClusterOption`(this is the default setting from release 3.7.2).
* [NCBC-4006](https://couchbasecloud.atlassian.net/browse/NCBC-4006), [NCBC-4010](https://couchbasecloud.atlassian.net/browse/NCBC-4010): Improvements on error handling in the Transactions API.

#### [](#new-features)New Features

* [NCBC-4005](https://couchbasecloud.atlassian.net/browse/NCBC-4005): Implemented `ExtParallelUnstaging` in the integrated Transactions API.

### [](#version-3-7-0-7-april-2025)Version 3.7.0 (7 April 2025)

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.7.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.7.0) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.7.0)

#### [](#fixed-issues-3)Fixed Issues

* [NCBC-3932](https://couchbasecloud.atlassian.net/browse/NCBC-3932): Prevented maximum buffer size exceeded when fetching large datasets with Query.
* [NCBC-3978](https://couchbasecloud.atlassian.net/browse/NCBC-3978): Resolved Query Error Deserialization with `Custom System.Text.Json` Options.

#### [](#improvements-3)Improvements

* [NCBC-3975](https://couchbasecloud.atlassian.net/browse/NCBC-3975): Clarified error message for server version where `RangeScan` is unsupported.
* [NCBC-3899](https://couchbasecloud.atlassian.net/browse/NCBC-3899): Improved `RetryHandler` signaling in `ChannelConnectionPool`.
* [NCBC-3976](https://couchbasecloud.atlassian.net/browse/NCBC-3976): Adjusted default values for `RangeScan` batch configuration.
* [NCBC-3946](https://couchbasecloud.atlassian.net/browse/NCBC-3946): Upgraded `Snappier` compression library to version `1.2.0`.
* [NCBC-3945](https://couchbasecloud.atlassian.net/browse/NCBC-3945): Enabled Value-Based Equality for `ScopeSpec` and `CollectionSpec`.

#### [](#new-features-2)New Features

* [NCBC-3902](https://couchbasecloud.atlassian.net/browse/NCBC-3902): Introduced `TryLookupIn` for graceful handling of `NOT_FOUND`.

## [](#net-sdk-3-6-releases).NET SDK 3.6 Releases

### [](#version-3-6-6-10-march-2025)Version 3.6.6 (10 March 2025)

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.6.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.6.6) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.6.6)

#### [](#fixed-issues-4)Fixed Issues

* [NCBC-3885](https://couchbasecloud.atlassian.net/browse/NCBC-3885): System certificate store should continue to be used in default TLS/SSL configuration.
* [NCBC-3964](https://jira.issues.couchbase.com/browse/NCBC-3964): Fixed issue where queries were not evenly distributed amongst Query Nodes.

#### [](#improvements-4)Improvements

* [NCBC-3945](https://couchbasecloud.atlassian.net/browse/NCBC-3945): Make `ScopeSpec` and `CollectionSpec` instance equality determinable.
* [NCBC-3948](https://couchbasecloud.atlassian.net/browse/NCBC-3948): Add new `TryGetRawParameter` to `ClusterOptions`.

### [](#version-3-6-5-17-january-2025)Version 3.6.5 (17 January 2025)

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.6.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.6.5) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.6.5)

#### [](#fixed-issues-5)Fixed Issues

* [NCBC-3906](https://couchbasecloud.atlassian.net/browse/NCBC-3906): A missing `ConfigureAwait False` in `AttemptContext` was causing a build error. This has now been fixed.

#### [](#improvements-5)Improvements

* [NCBC-3920](https://couchbasecloud.atlassian.net/browse/NCBC-3920): Renamed `Couchbase.Integrated.Transactions` to `Couchbase.Client.Transactions`.
* [NCBC-3919](https://couchbasecloud.atlassian.net/browse/NCBC-3919): A final refactor of the transactions integration to match the initial commit for `ExtThreadSafety`, `ExtSdkIntegration`, and others.
* [NCBC-3916](https://couchbasecloud.atlassian.net/browse/NCBC-3916): `ExtThreadSafety` implementation into integrated transactions library.
* [NCBC-3915](https://couchbasecloud.atlassian.net/browse/NCBC-3915): Allow `TransactionConfig` to configured via `ClusterOptions`.
* [NCBC-3913](https://couchbasecloud.atlassian.net/browse/NCBC-3913): Improvements and bug fixes to the `Cleaner` for transactions.
* [NCBC-3912](https://couchbasecloud.atlassian.net/browse/NCBC-3912): Renamed parameter to Error Constructor from `err` to `cause`.
* [NCBC-3897](https://couchbasecloud.atlassian.net/browse/NCBC-3897): Added `PreferReturns` support for `LookupIn`, for internal use, to improve subdoc performance for transactions.
* [NCBC-3845](https://couchbasecloud.atlassian.net/browse/NCBC-3845): Added `ReadOnlySequence` and `IBufferWriter` support to `ITypeSerializer`.

### [](#version-3-6-4-8-november-2024)Version 3.6.4 (8 November 2024)

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.6.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.6.4) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.6.4)

#### [](#fixed-issues-6)Fixed Issues

[NCBC-3840](https://couchbasecloud.atlassian.net/browse/NCBC-3840): \[Rider IDE\] `:nq` is not a valid format specifier notice now correctly uses Debugger Display reference.

[NCBC-3878](https://couchbasecloud.atlassian.net/browse/NCBC-3878): Randomized seed order of hosts enabled in the Connection string

\+ NOTE: Random seed order must be enabled with `?random_seed_nodes=true` in the connection string. This will be the default in a future release.

[NCBC-3879](https://couchbasecloud.atlassian.net/browse/NCBC-3879): .NET SDK was setting span attributes directly on the operation’s span, rather than on the despatch span. Attributes have now been added to the `DispatchSpan` for Query and KV operations, but not removed from the operation’s span in order not to break user queries that target those specific traces.

\+ **DEPRECATION NOTICE**: In 3.7.0, these attributes should be removed from the operation’s span.

[NCBC-3883](https://couchbasecloud.atlassian.net/browse/NCBC-3883): Updated `System.Text.Json` dependency, owing to a security vulnerability.

#### [](#improvements-6)Improvements

[NCBC-3851](https://couchbasecloud.atlassian.net/browse/NCBC-3851): More Contextual labels have been added to metrics, as part of improvements to the observability spec.

### [](#version-3-6-3-19-september-2024)Version 3.6.3 (19 September 2024)

Version 3.6.3 is a hotfix release. Some NuGet packages were upgraded as a result of high impact security issues, [NCBC-3839](https://jira.issues.couchbase.com/browse/NCBC-3839). These should not impact any users of CouchbaseNetClient, as they are backward compatible updates. However, if you find an incompatibility, you can add a direct reference to the old version of those packages as a dependency in your own project.

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.6.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.6.3) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.6.3)

#### [](#fixed-issues-7)Fixed Issues

* [NCBC-3863](https://jira.issues.couchbase.com/browse/NCBC-3863): Performance problems and timeouts fixes during rebalance when the cluster contains non-KV nodes.
* [NCBC-3832](https://jira.issues.couchbase.com/browse/NCBC-3832): Query timeout set to exceed 100 seconds is now respected.
* [NCBC-3818](https://jira.issues.couchbase.com/browse/NCBC-3818): `QueryErrorContext` `Statement` parameter is now set properly.
* [NCBC-3842](https://jira.issues.couchbase.com/browse/NCBC-3842): Newtonsoft deserializing UTF8 surrogate pairs fixed for exceptions and buffer overflow.
* [NCBC-3849](https://jira.issues.couchbase.com/browse/NCBC-3849): Orphaned responses now sent to metrics for untraced operations.
* [NCBC-3850](https://jira.issues.couchbase.com/browse/NCBC-3850): Timeouts now recorded to metrics in `ClusterNode.ExecuteOp`.
* [NCBC-3852](https://jira.issues.couchbase.com/browse/NCBC-3852): `TryReadMutationToken` header length check.
* [NCBC-3854](https://jira.issues.couchbase.com/browse/NCBC-3854): Improvements made for `LightweightStopwatch` unit test.
* [NCBC-3876](https://jira.issues.couchbase.com/browse/NCBC-3876): `CancellationTokenSource` is not disposed when returned to pool on legacy frameworks.

#### [](#improvements-7)Improvements

* [NCBC-3839](https://jira.issues.couchbase.com/browse/NCBC-3839): Updated packages based on BlackDuck scan.
* [NCBC-3710](https://jira.issues.couchbase.com/browse/NCBC-3710): Included operation outcome tag in operation metrics.
* [NCBC-3837](https://jira.issues.couchbase.com/browse/NCBC-3837): Provide easy configuration to exclude duplicative metrics from `OpenTelemetry`.

### [](#version-3-6-2-22-july-2024)Version 3.6.2 (22 July 2024)

Version 3.6.2 is a hotfix release. Microsoft disclosed a CVE affecting their `System.Text.Json` (STJ) library on the 9th of July, 2024\. This release upgrades STJ to the patched version in our SDK.

* [Microsoft CVE on GitHub](https://github.com/advisories/GHSA-hh2w-p6rv-4g7w)

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.6.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.6.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.6.2)

#### [](#fixed-issues-8)Fixed Issues

* [NCBC-3817](https://issues.couchbase.com/browse/NCBC-3817): Vulnerability in `System.Text.Json` 8.0.0 is fixed.

#### [](#improvements-8)Improvements

* [NCBC-3821](https://issues.couchbase.com/browse/NCBC-3821): Updated `CouchbaseNetClientReleasedVerison` to 3.6.2.
* [NCBC-3726](https://issues.couchbase.com/browse/NCBC-3726): Applied some miscellaneous performance optimizations to transcoders.
* [NCBC-3795](https://issues.couchbase.com/browse/NCBC-3795): Reduced duplicate operation handling code in `ClusterNode`.

### [](#version-3-6-1-3-july-2024)Version 3.6.1 (3 July 2024)

Version 3.6.1 is a hotfix release.

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.6.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.6.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.6.1)

#### [](#fixed-issues-9)Fixed Issues

* [NCBC-3791](https://issues.couchbase.com/browse/NCBC-3791): `BucketConfig` version used to be compared against the latest applied config, not the latest one received.
* [NCBC-3698](https://issues.couchbase.com/browse/NCBC-3698): Manually setting `ScopeName` and/or `CollectionName` in the `CollectionQueryIndexManager` API’s options will now throw an `InvalidArgumentException`. Previously, the SDK was ignoring the `ScopeName` and `CollectionName` in options, instead of throwing `InvalidArgumentException` as per RFC.
* [NCBC-3780](https://issues.couchbase.com/browse/NCBC-3780): Transactions: `QueryContext` is now copied when retrying `SingleQueryTransactions`.

#### [](#improvement)Improvement

* [NCBC-3798](https://issues.couchbase.com/browse/NCBC-3798): VectorSearch: Passing in empty vectors now throws InvalidArgumentException

### [](#version-3-6-0-13-june-2024)Version 3.6.0 (13 June 2024)

Version 3.6.0 is the first release of the 3.6 series.

[Download](https://packages.couchbase.com/clients/net/3.6/Couchbase-Net-Client-3.6.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.6.0) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.6.0)

#### [](#known-issues)Known Issues

* There is an edge case that can cause high CPU usage against Couchbase Server 7.6 and later. Users are advised to upgrade to 3.6.1.

#### [](#fixed-issues-10)Fixed Issues

* [NCBC-3572](https://issues.couchbase.com/browse/NCBC-3572): For management services, `CancellationTokens` are now more accurate to the operation’s lifetime.
* [NCBC-3702](https://issues.couchbase.com/browse/NCBC-3702): Stellar client: Use `DefaultSerializer` as default at Cluster level
* [NCBC-3760](https://issues.couchbase.com/browse/NCBC-3760): Fixed an issue regarding passing an `X509CertificateFactory` in `ClusterOptions`.
* [NCBC-3768](https://issues.couchbase.com/browse/NCBC-3768): Aligned Boolean search API to RFC.
* [NCBC-3775](https://issues.couchbase.com/browse/NCBC-3775): `IndexAlreadyExists` is now properly thrown.
* [NCBC-3785](https://issues.couchbase.com/browse/NCBC-3785): Transactions: `DocumentMetadata` deserialization fixed.
* [NCBC-3789](https://issues.couchbase.com/browse/NCBC-3789): Updated Release version tag in SDK `Directory.Build.Props`.
* [NCBC-3794](https://issues.couchbase.com/browse/NCBC-3794): Removed infinite loop in `ConfigPushHandler`, which was causing high CPU usage.

#### [](#new-feature)New Feature

* [NCBC-3788](https://issues.couchbase.com/browse/NCBC-3788): Support added for base64 encoded vector types.

#### [](#improvements-9)Improvements

* [NCBC-3771](https://issues.couchbase.com/browse/NCBC-3771): Refactored `RetryOrcestrator` for Data Service operations to be clearer.
* [NCBC-3792](https://issues.couchbase.com/browse/NCBC-3792): Optimize for larger InFlightOperationSet for high latency connections.
* [NCBC-3796](https://issues.couchbase.com/browse/NCBC-3796): Updated local build version to 3.6.0.
* [NCBC-3797](https://issues.couchbase.com/browse/NCBC-3797): Updated \`VectorSearch’s InterfaceStability to Committed.

## [](#net-sdk-3-5-releases).NET SDK 3.5 Releases

### [](#version-3-5-3-23-july-2024)Version 3.5.3 (23 July 2024)

Version 3.5.3 is the fourth release of the 3.5 series.

[Download](https://packages.couchbase.com/clients/net/3.5/Couchbase-Net-Client-3.5.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.5.3) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.5.3)

#### [](#fixed-issues-11)Fixed Issues

Microsoft disclosed a CVE affecting their System.Text.Json (STJ) library on the 9th of July 2024\. This release upgrades STJ to the patched version in our SDK.

* [Microsoft CVE on GitHub](https://github.com/advisories/GHSA-hh2w-p6rv-4g7w)
* [NCBC-3817](https://issues.couchbase.com/browse/NCBC-3817): Upgrade `System.Text.Json` to patched version.

This release also backports fixes brought to `ConfigPushHandler` in releases 3.6.0 and 3.6.1:

* [NCBC-3811](https://issues.couchbase.com/browse/NCBC-3811): Backports ConfigPushHandler fixes to 3.5 branch (See also [NCBC-3791](https://issues.couchbase.com/browse/NCBC-3791), [NCBC-3794](https://issues.couchbase.com/browse/NCBC-3794)).

### [](#version-3-5-2-3-may-2024)Version 3.5.2 (3 May 2024)

Version 3.5.2 is the third release of the 3.5 series.

[Download](https://packages.couchbase.com/clients/net/3.5/Couchbase-Net-Client-3.5.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.5.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.5.2)

> [!NOTE]
> Owing to [NCBC-3794](https://issues.couchbase.com/browse/NCBC-3794), it is recommended that all customers using Server 7.6 or later upgrade to SDK 3.5.3, or SDK 3.6.2 or later, immediately.

#### [](#fixed-issues-12)Fixed Issues

* [NCBC-3745](https://issues.couchbase.com/browse/NCBC-3745): `MultiplexingConnection` will throw a `SocketNotAvailableException` if disposed.
* [NCBC-3756](https://issues.couchbase.com/browse/NCBC-3756): Handle empty `VBucketMap` in server config.
* [NCBC-3758](https://issues.couchbase.com/browse/NCBC-3758): Fixed regression where `PersistentQueue` was not dequeueing items in original FIFO order.
* [NCBC-3764](https://issues.couchbase.com/browse/NCBC-3764): Fixed issue where `GetAnyReplica` / `TaskHelpers.WhenAnySuccessful` could potentially cause deadlocks using the .NET Framework.
* [NCBC-3769](https://issues.couchbase.com/browse/NCBC-3769): SDK will now adapt to new cluster topology if only a port has changed (as in some Alternate Address configurations).
* [NCBC-3772](https://issues.couchbase.com/browse/NCBC-3772): Fixed a regression where configs were being applied to buckets they did not belong to, including cluster-level config.

#### [](#new-features-and-behavioral-changes)New Features and Behavioral Changes

* [NCBC-1622](https://issues.couchbase.com/browse/NCBC-1622): Snappy Compression — using the Snappier library — is now merged into the main SDK.
* [NCBC-3738](https://issues.couchbase.com/browse/NCBC-3738): Support added for scoped eventing functions.
* [NCBC-3746](https://issues.couchbase.com/browse/NCBC-3746): Performance optimizations added to `ArrayExtensions`.
* [NCBC-3759](https://issues.couchbase.com/browse/NCBC-3759): `ExceptionDispatchInfo` was being used to capture and rethrow the `Exception` stack trace at the time the exception was originally caught. `ClusterContext` bootstrap is now used to track per-node bootstrap errors, using `ExceptionDispatchInfo` instead of `Exception`. This may result in more accurate stack traces now or in future runtimes.
* [NCBC-3770](https://issues.couchbase.com/browse/NCBC-3770): Reduced the amount of `DEBUG` logging around Config Push — the additional information is now logged at `TRACE` level.

### [](#version-3-5-1-16-apr-2024)Version 3.5.1 (16 Apr 2024)

Version 3.5.1 is the second release of the 3.5 series.

[Download](https://packages.couchbase.com/clients/net/3.5/Couchbase-Net-Client-3.5.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.5.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.5.1)

#### [](#fixed-issues-13)Fixed Issues

* [NCBC-3690](https://issues.couchbase.com/browse/NCBC-3690): FIT Management: Implement Scoped Search Index Management.
* [NCBC-3699](https://issues.couchbase.com/browse/NCBC-3699): FIT Query: QueryOptionTest failures fixed.
* [NCBC-3700](https://issues.couchbase.com/browse/NCBC-3700): FIT KV: New Subdoc errors fixed.
* [NCBC-3703](https://issues.couchbase.com/browse/NCBC-3703): FIT Stellar: InvalidArgument and DocumentTooDeep now handled.
* [NCBC-3716](https://issues.couchbase.com/browse/NCBC-3716): Fixed a regression in KV throughput against Trinity during rebalances.
* [NCBC-3720](https://issues.couchbase.com/browse/NCBC-3720): `ClusterChangeMapNotification` was reported in logs and errors in place of KV ops — this has been fixed, and `SET/Upsert` is now correctly reported.
* [NCBC-3721](https://issues.couchbase.com/browse/NCBC-3721): Fixed a regression in 3.5.0 which would not allow building a Cluster with `LoggingMeter` disabled.
* [NCBC-3724](https://issues.couchbase.com/browse/NCBC-3724): Fixed a known issue with Snappier implementation in the SDK preventing bootstrap .NET with SDK v3.4.10 onwards against server v7.6.0.
* [NCBC-3725](https://issues.couchbase.com/browse/NCBC-3725): Fixed a bug where `ConfigPushHandler` wasn’t performing well under massive config push spam.
* [NCBC-3727](https://issues.couchbase.com/browse/NCBC-3727): When Faster Failover with ClustermapChangeNotification is enabled, config polling was short circuited, causing the SDK to rebootstrap because it thinks that it cannot connect to the cluster with the current nodes list. This behavior has been fixed.
* [NCBC-3732](https://issues.couchbase.com/browse/NCBC-3732): Fixed logic bug that was causing the `ConfigPushHandler` to skip all new clustermap config revision.
* [NCBC-3734](https://issues.couchbase.com/browse/NCBC-3734): The NRE was causing config revisions to be skipped which meant retries for `NotMyVBucket` were happening multiple times using the same config revision.
* [NCBC-3737](https://issues.couchbase.com/browse/NCBC-3737): `KvNotMyBucket` retried with old config.
* [NCBC-3742](https://issues.couchbase.com/browse/NCBC-3742): Reduced push config spam in ConfigPushHandler.
* [NCBC-3747](https://issues.couchbase.com/browse/NCBC-3747): When CB Server 7.2 sends a cluster map changed notification, it is sent with a JSON body containing the new map. After deserializing, we were not replacing `$HOST` with the correct values, causing the in-memory map to become corrupt and subsequent operations to timeout. This has been fixed, and now after deserializing a pushed notification with a cluster map the SDK replaces `$HOST` with the endpoint, and applies any overridden network resolution settings. This matches the behavior when we receive a `BucketConfig` back from an explicit request.
* [NCBC-3752](https://issues.couchbase.com/browse/NCBC-3752): Fixed a race condition affecting `KeyMapper` being updated out of sync with `CurrentConfig`.
* [NCBC-3753](https://issues.couchbase.com/browse/NCBC-3753): The SDK will now only publish a config if it’s a higher revision than the current one.
* [NCBC-3749](https://issues.couchbase.com/browse/NCBC-3749): Log the `ConfigVersion` used by an operation throughout the SDK.
* [NCBC-3723](https://issues.couchbase.com/browse/NCBC-3723): Fixed a `NullReferenceException` in `ConfigPushHandler`, which meant the code could jump to the error handling and log/exit instead of processing the config.
* [NCBC-3740](https://issues.couchbase.com/browse/NCBC-3740): When Faster Failover is available, a `GetClusterMap` request is no longer the only response to `NotMyVBucket`.
* [NCBC-3722](https://issues.couchbase.com/browse/NCBC-3722): Fixed an `IndexOutOfBounds` error processing cluster map during `ConfigUpdateAsync`.
* [NCBC-3719](https://issues.couchbase.com/browse/NCBC-3719): There is a bug in the server, and an Unlock operation with an invalid Cas returns `Locked` instead of `CasMismatch` status. The SDK now handles this as a `CasMismatch`.

#### [](#new-features-and-behavioral-changes-2)New Features and Behavioral Changes

* [NCBC-3739](https://issues.couchbase.com/browse/NCBC-3739): A `GetConfigMap` begin sent is generally a high priority because it indicates server configuration is outdated due to failover or rebalance. Added a method (which currently only applies to the default `ChannelConnectionPool`) which allows an operation to be jumped to the front of the line to be sent. It randomly selects the connection from the pool to provide distribution rather than relying on the queue to distribute.
* [NCBC-3744](https://issues.couchbase.com/browse/NCBC-3744): Moved `ConfigPushHandler` from `ClusterNode` to `CouchbaseBucket`.
* [NCBC-3748](https://issues.couchbase.com/browse/NCBC-3748): Tracking basic metrics for `ClusterMapChangeNotification`.
* [NCBC-3751](https://issues.couchbase.com/browse/NCBC-3751): Every Scope and Collection fetch was being logged in `DEBUG` mode, adding spam to the logs and roughly doubling the log size. We have now hanged logging there, and also for when waiting for polling, to `TRACE`. for a config.

### [](#version-3-5-0-11-mar-2024-do-not-use-use-3-5-1-instead)Version 3.5.0 (11 Mar 2024) DO NOT USE - USE 3.5.1 INSTEAD

Version 3.5.0 is the first release of the 3.5 series. A number of regressions means that it is not recommended for use — release notes are retained here for reference, as they apply to all subsequent releases.

[Download](https://packages.couchbase.com/clients/net/3.5/Couchbase-Net-Client-3.5.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.5.0) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.5.0)

#### [](#fixed-issues-14)Fixed Issues

* [NCBC-2901](https://issues.couchbase.com/browse/NCBC-2901): Fixed the percentiles printed by `LoggingMeter` to comply with the RFC.
* [NCBC-3058](https://issues.couchbase.com/browse/NCBC-3058): Eliminated the `App.Metrics` dependency and implemented a better approach for tracking logging meter histograms.
* [NCBC-3314](https://issues.couchbase.com/browse/NCBC-3314): Renamed `SubdocExceptionException` to `SubdocException`.
* [NCBC-3336](https://issues.couchbase.com/browse/NCBC-3336): Made it possible to get a `collection_id` from a `QueryIndex` object. Fixed the creation of named primary indexes. Added a conditional field to `QueryIndex`.
* [NCBC-3564](https://issues.couchbase.com/browse/NCBC-3564): No error is thrown if the cluster or the bucket authorization fails.
* [NCBC-3604](https://issues.couchbase.com/browse/NCBC-3604): Removed `Term` field from `TermRangeQuery`.
* [NCBC-3612](https://issues.couchbase.com/browse/NCBC-3612): Added an exception handling when calling `ContentAs` on an `Exist` spec.
* [NCBC-3624](https://issues.couchbase.com/browse/NCBC-3624): When the vector search query options have a value of `k < 1`, .NET throws a `CouchbaseException` instead of the expected `InvalidArgumentException`.
* [NCBC-3633](https://issues.couchbase.com/browse/NCBC-3633): `SubdocMutation Replace/Remove` uses `OpCode.Set` and `OpCode.Delete` when an empty path is passed.
* [NCBC-3635](https://issues.couchbase.com/browse/NCBC-3635): Added a `ReadOnlyCollection<Exception>` public backing field to contain the inner exceptions of the `AggregateException` field.
* [NCBC-3637](https://issues.couchbase.com/browse/NCBC-3637): Updated `AsyncStreamState` to handle all responses enumerated in the RFC for `RangeScan`.
* [NCBC-3645](https://issues.couchbase.com/browse/NCBC-3645): Fixed error thrown against maximum allowed path length.
* [NCBC-3646](https://issues.couchbase.com/browse/NCBC-3646): `LookupInAnyReplica` and `LookupInAllReplicas` now throw a `FeatureNotAvailable` error on servers that do not support `subdoc.ReplicaRead`.
* [NCBC-3649](https://issues.couchbase.com/browse/NCBC-3649): Index now updates directly into the response body to prevent unnecessary heap application or memory copy.
* [NCBC-3657](https://issues.couchbase.com/browse/NCBC-3657): `LookupInSpec.Get()` now returns `GetFull` when the given path is empty.
* [NCBC-3661](https://issues.couchbase.com/browse/NCBC-3661): Ensures that a node with the management service is selected so that `NullReferenceException` is not thrown.
* [NCBC-3664](https://issues.couchbase.com/browse/NCBC-3664): Set the expiry of `GetResult` to `DateTime.MaxValue` when the `secondsUntilExpiry` returned spec is 0.
* [NCBC-3666](https://issues.couchbase.com/browse/NCBC-3666): Added a backing field for `Key` in `OperationBase`. Added a `byte[] EncodedKey` field to automatically encode and check the size of the `Key` when creating an operation.
* [NCBC-3676](https://issues.couchbase.com/browse/NCBC-3676): Enumeration now uses the `RetryHandler` to read ahead. It then caches the results and enumerates them first if they are successful.
* [NCBC-3679](https://issues.couchbase.com/browse/NCBC-3679): Fixed a bug in `QueryErrorContext` where the `DebuggerDisplay` message had an invalid value of `:ns` instead of `,ns`.
* [NCBC-3686](https://issues.couchbase.com/browse/NCBC-3686): Throws an exception before sending the request if no vectors are provided.
* [NCBC-3696](https://issues.couchbase.com/browse/NCBC-3696): Fixed a bug in `SearchIndexManager` for scoped indexes.
* [NCBC-3701](https://issues.couchbase.com/browse/NCBC-3701): Added missing API overloads to comply with the RFC.
* [NCBC-3705](https://issues.couchbase.com/browse/NCBC-3705): Fixed spelling error in `ClusterOptions` code comments.
* [NCBC-3709](https://issues.couchbase.com/browse/NCBC-3709): Updated KV operation metrics to post a single duration for each operation, instead of one duration for each individual retry. The operation count no longer includes retries.

#### [](#new-features-and-behavioral-changes-3)New Features and Behavioral Changes

* [NCBC-3673](https://issues.couchbase.com/browse/NCBC-3673): If the server does not support vector search or `ScopedSearchIndexes`, a `FeatureNotAvailable` error is thrown.
* [NCBC-3620](https://issues.couchbase.com/browse/NCBC-3620): Removed unused imports and unnecessary full qualified namespaces. Moved local functions under the return keyword. Made constants private. Updated local functions from camel case to pascal case.
* [NCBC-3617](https://issues.couchbase.com/browse/NCBC-3617): Added protostellar support for a new scheme for connecting to the gateway.
* [NCBC-3667](https://issues.couchbase.com/browse/NCBC-3667): If the SDK receives a `retry-now` response, it retries the operation.
* [NCBC-3671](https://issues.couchbase.com/browse/NCBC-3671): If the server cannot find the given index, it throws an `IndexNotFoundException` error.
* [NCBC-3648](https://issues.couchbase.com/browse/NCBC-3648): Improved the memory handling of large operation responses.
* [NCBC-3554](https://issues.couchbase.com/browse/NCBC-3554): Added retry handling to protostellar.
* [NCBC-3597](https://issues.couchbase.com/browse/NCBC-3597): Removed `Couchbase.Stellar` and `Couchbase.NetClient` from `Couchbase.csproj`.
* [NCBC-3601](https://issues.couchbase.com/browse/NCBC-3601): Added toggling between a `StellarCluster` creation and a regular `Cluster` creation based on the schema detected when `Cluster.ConnectAsync` is called.
* [NCBC-3602](https://issues.couchbase.com/browse/NCBC-3602): Fixed a bug where an error is thrown if a CAS of zero is sent to CNG or protostellar.
* [NCBC-3655](https://issues.couchbase.com/browse/NCBC-3655): Added `StellarQueryClient` so that failed queries can be retried.
* [NCBC-3670](https://issues.couchbase.com/browse/NCBC-3670): Removed `InvalidArgument` fail-fast for `LookupinAnyReplica`.
* [NCBC-3672](https://issues.couchbase.com/browse/NCBC-3672): Fixed failing vector search tests.

## [](#net-sdk-3-4-releases).NET SDK 3.4 Releases

### [](#version-3-4-15)Version 3.4.15 (09 Feb 2024)

Version 3.4.15 is the sixteenth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.15.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.15) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.15)

#### [](#known-issues-2)Known Issues

* [NCBC-3716](https://issues.couchbase.com/browse/NCBC-3716): If you are using Capella or Server versions 7.6.0+, we strongly encourage you to upgrade to SDK v3.5.1+. While this version will continue be compatible and supported with server 7.6 (and newer instances of Capella, using 7.6), you may encounter timeout exceptions during rebalances under KV high workload.

#### [](#breaking-changes)Breaking Changes

* [NCBC-3599](https://issues.couchbase.com/browse/NCBC-3599): The `initial` parameter of Increment and Decrement operations is now unset by default. This means the SDK will throw a `DocumentNotFoundException` upon calling Increment or Decrement with a non-existing key without providing an initial value.

Example:

* `await collection.Binary.IncrementAsync("thisKeyDoesNotExist").ConfigureAwait(false);` → Now throws `DocumentNotFoundException`
* `await collection.Binary.IncrementAsync("thisKeyDoesNotExist", options ⇒ options.Initial(0)).ConfigureAwait(false);` → Creates the document with counter at 0

#### [](#fixed-issues-15)Fixed Issues

* [NCBC-3599](https://issues.couchbase.com/browse/NCBC-3599): Fixed SDK bugs related to Nullability of Increment, Decrement, and related options.
* [NCBC-3565](https://issues.couchbase.com/browse/NCBC-3565): Added error handling for "index does not exist" query error.

#### [](#new-features-and-behavioral-changes-4)New Features and Behavioral Changes

* [NCBC-3579](https://issues.couchbase.com/browse/NCBC-3579): Support `DocumentNotLocked` exception when `collection.Unlock()` is called on a document that is not locked.
* [NCBC-3606](https://issues.couchbase.com/browse/NCBC-3606): Added SDK Support for Scoped Search Indexes.
* [NCBC-3596](https://issues.couchbase.com/browse/NCBC-3596): Support added for `maxTTL` value of -1, for collection "no expiry".

### [](#version-3-4-14)Version 3.4.14 (18 Jan 2024)

Version 3.4.14 is the fifteenth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.14.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.14) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.14)

#### [](#known-issues-3)Known Issues

* [NCBC-3716](https://issues.couchbase.com/browse/NCBC-3716): If you are using Capella or Server versions 7.6.0+, we strongly encourage you to upgrade to SDK v3.5.1+. While this version will continue be compatible and supported with server 7.6 (and newer instances of Capella, using 7.6), you may encounter timeout exceptions during rebalances under KV high workload.

#### [](#fixed-issues-16)Fixed Issues

* [NCBC-3434](https://issues.couchbase.com/browse/NCBC-3434): A regression introduced in a recent release prevented `WaitUntilReady` from pinging nodes — this has been fixed, and `WaitUntilReady` now correctly detects state.
* [NCBC-3503](https://issues.couchbase.com/browse/NCBC-3503): There was a possibility of `ClusterVersionProvider.GetVersionAsync` failing, if nodes have no `ManagementUri`, owing to randomized node order. This has been fixed, and `GetRandomManagementUri()` should never now throw `NullReferenceException`.

#### [](#new-features-and-behavioral-changes-5)New Features and Behavioral Changes

* [NCBC-3530](https://issues.couchbase.com/browse/NCBC-3530): Made the `ConnectionString` class now accept `couchbase2` schema.
* [NCBC-3532](https://issues.couchbase.com/browse/NCBC-3532): Added `AsReadOnly` record to Index APIs options.
* [NCBC-3538](https://issues.couchbase.com/browse/NCBC-3538): Improved recovery time in Config Push to 300ms.
* [NCBC-3541](https://issues.couchbase.com/browse/NCBC-3541): Added `AsReadOnly` record to Bucket Management APIs options.
* [NCBC-3551](https://issues.couchbase.com/browse/NCBC-3551): Added `AsReadOnly` record to Collection Management APIs options.
* [NCBC-3568](https://issues.couchbase.com/browse/NCBC-3568): Added `AsReadOnly` Record to GetAllScopesOptions.
* [NCBC-3516](https://issues.couchbase.com/browse/NCBC-3516): Made fallback usage of `DefaultSerializer` trimmable.
* [NCBC-3518](https://issues.couchbase.com/browse/NCBC-3518): Removed internal transcoder dependencies on `DefaultSerializer`.

### [](#version-3-4-13)Version 3.4.13 (09 Nov 2023)

Version 3.4.13 is the fourteenth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.13.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.13) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.13)

#### [](#known-issues-4)Known Issues

* [NCBC-3716](https://issues.couchbase.com/browse/NCBC-3716): If you are using Capella or Server versions 7.6.0+, we strongly encourage you to upgrade to SDK v3.5.1+. While this version will continue be compatible and supported with server 7.6 (and newer instances of Capella, using 7.6), you may encounter timeout exceptions during rebalances under KV high workload.

#### [](#fixed-issues-17)Fixed Issues

* [NCBC-3397](https://issues.couchbase.com/browse/NCBC-3397): `IOperation.Elapsed` was not correctly counting duration between retries — the stopwatch field of `IOperation/OperationBase` is stopped in `HandleOperationCompleted()` and never re-started. This has now been fixed, and the `Elapsed` field of `OperationBase` now correctly increments with the stopwatch time after each retry cycle.
* [NCBC-3498](https://issues.couchbase.com/browse/NCBC-3498): Added code documentation to `PersistentList` as the internals use reference comparisons, but there is no guarantee that internally the document might be reloaded by the database. The documention instructs users to override the `Object.Equals` method on their POCOs so that that values of the objects will be compared and not the objects' reference.
* [NCBC-3510](https://issues.couchbase.com/browse/NCBC-3510): Fixed a regression in Config Push Notification / Faster Failover performance. Config Push notifications are now handled by a single thread per node in a LIFO manner, and skip out of date push notifications, as well as providing more logging around config updates to help troubleshoot in the future. Additionally, `GetClusterConfig` asks for the old version, not the pushed version.
* [NCBC-3526](https://issues.couchbase.com/browse/NCBC-3526): The Search Service’s `` NumericRangeQuery’s `MaxInclusive `` property was defaulting to `false`. It now defaults to `true`, in line with the [rfc](https://github.com/couchbaselabs/sdk-rfcs/blob/master/rfc/0052-sdk3-full-text-search.md#numericrangequery).
* [NCBC-3543](https://issues.couchbase.com/browse/NCBC-3543): `DefaultSerializer` will now correctly handle Unicode surrogate pairs on buffer boundaries.

#### [](#new-features-and-behavioral-changes-6)New Features and Behavioral Changes

* [NCBC-3472](https://issues.couchbase.com/browse/NCBC-3472): Support added to bucket settings for [change history](../../../server/7.2/learn/data/change-history.md#understanding-change-history) feature.
* [NCBC-3502](https://issues.couchbase.com/browse/NCBC-3502), [NCBC-3506](https://issues.couchbase.com/browse/NCBC-3506): Merging `couchbase-net-stellar` into `couchbase-net-client`, for upcoming Cloud Native Gateway support.
* [NCBC-3481](https://issues.couchbase.com/browse/NCBC-3481): The legacy `Enum.GetValues(Type)` overload is not AOT-compatible. Added conditional compilation to use the Enum.GetValues<TEnum>() overload on .NET 6 and later.
* [NCBC-3487](https://issues.couchbase.com/browse/NCBC-3487): Reduced reliance on `SerializeWithFallback`, which is incompatible with trimming and `NativeAOT`.
* [NCBC-3488](https://issues.couchbase.com/browse/NCBC-3488): Delaying creation of `CollectionQueryIndexManager`, which will allow it to be left off the DI container, and trimmed out of the output executable if unused.
* [NCBC-3489](https://issues.couchbase.com/browse/NCBC-3489): Implemented an in-flight operation limit to provide backpressure. The previous design allowed a single connection from the connection pool to collect a large number of in-flight operations, rather than ensuring a more even spread of operations across connections in the pool. This potentially allowed small operation may be blocked waiting for large operation to pass over the network socket. A more even spread of operations doesn’t guarantee this will be the case, but does make it more likely.
* [NCBC-3508](https://issues.couchbase.com/browse/NCBC-3508): Support HTTP response streaming in legacy .NET runtimes

  * .NET 4 consumers may opt-in to HTTP response streaming so long as they ensure they properly dispose of any returned `XXXResult` objects rather than leaving them dangling and potentially causing a connection leak. If they do choose this behavior then `System.IOException` cases previously addressed by [NCBC-3433](https://issues.couchbase.com/browse/NCBC-3433) should not occur due to the new pattern for disposing of `HttpClient`.
  * .NET 6 and newer consumers may now choose to opt-out of HTTP response streaming if desired.
* [NCBC-3539](https://issues.couchbase.com/browse/NCBC-3539): `System.Text.Json` is now used to deserialize document expiry — for improved performance and compatiblity with trimming and `NativeAOT`.
* [NCBC-3545](https://issues.couchbase.com/browse/NCBC-3545): Fixes a regression introduced in 3.4.12 where a `ClusterNode` might be disposed and then reused, which causes an exception to be raised. This issue is raised if the cluster is configured to use Alternate Addressing, but not DNS-SRV.

### [](#version-3-4-12)Version 3.4.12 (04 Oct 2023)

Version 3.4.12 is the thirteenth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.12.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.12) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.12)

#### [](#known-issues-5)Known Issues

* [NCBC-3716](https://issues.couchbase.com/browse/NCBC-3716): If you are using Capella or Server versions 7.6.0+, we strongly encourage you to upgrade to SDK v3.5.1+. While this version will continue be compatible and supported with server 7.6 (and newer instances of Capella, using 7.6), you may encounter timeout exceptions during rebalances under KV high workload.

#### [](#fixed-issues-18)Fixed Issues

* [NCBC-3490](https://issues.couchbase.com/browse/NCBC-3490): When a request includes a CAS, `MutateIn` should now throw a `CasMismatch` exception if the status is `KeyExists`. Otherwise, for `KeyExists`, it will continue to throw `DocumentExistsException`.
* [NCBC-3493](https://issues.couchbase.com/browse/NCBC-3493): When a Private Link is enabled, the SDK was not properly using the provided config and all of the VBuckets were mapped to the same node. This could cause a recurring `KvNotMyVBucket`, which would eventually become an `AmbiguousTimeoutException` thrown to the user. This behavior has now been fixed — changes have been made so that `NetworkResolution` is propagated to `BucketConfig`, duplicate nodes not added to nodes list, and entries in `LookupDictionary` are only made for nodes with actual ports.
* [NCBC-3496](https://issues.couchbase.com/browse/NCBC-3496): `WaitUntilReady` should now use the cluster map and not the `ServiceType` enum by default — removing spurious error messages about services which are not being used.
* [NCBC-3455](https://issues.couchbase.com/browse/NCBC-3455): During a `MultiLookup`, the SDK should now correctly throw `DocumentUnretrievableException` in `LookupInAnyReplica`, for key not found.
* [NCBC-3465](https://issues.couchbase.com/browse/NCBC-3465): Exist specs in `LookupInResults` was not returning `ContentAs` — it now returns bool Exist value serialized as `T` when calling `LookupinResult.ContentAs<T>()`, as per RFC.
* [NCBC-3473](https://issues.couchbase.com/browse/NCBC-3473): `GetInAnyReplica` could fail when it should have been successful, throwing `DocumentUnretrievable` — it should now return the first _successful_ operation (unless all fail).
* [NCBC-3484](https://issues.couchbase.com/browse/NCBC-3484), [NCBC-3485](https://issues.couchbase.com/browse/NCBC-3485), [NCBC-3486](https://issues.couchbase.com/browse/NCBC-3486): Several bugs in LookupInAny and LookupInAllReplicas have been fixed.

#### [](#new-features-and-behavioral-changes-7)New Features and Behavioral Changes

* [NCBC-3494](https://issues.couchbase.com/browse/NCBC-3494): Added a client-side check for `TooManySpecs` in `LookupIn`.
* [NCBC-3387](https://issues.couchbase.com/browse/NCBC-3387): Removed internal keword from `ICollectionQueryIndexManager`, facilitatiing better testing.
* [NCBC-3479](https://issues.couchbase.com/browse/NCBC-3479): Added trimming and AOT annotations to Analytics and Search clients.
* [NCBC-3492](https://issues.couchbase.com/browse/NCBC-3492): When an `EConfigOnly (0xd)` response is received, the SDK assumes that this _may_ mean a stale config, and so fetches a new config and publishes it for processing.
* [NCBC-3495](https://issues.couchbase.com/browse/NCBC-3495): Moved `LookupInAllReplicasAsync` and `LookupInAnyReplicaAsync` into `ICouchbaseCollection`.
* [NCBC-3497](https://issues.couchbase.com/browse/NCBC-3497): Added additional DEBUG logging `ConnectionFactory.CreateAndConnectAsync`, to aid TLS troubleshooting.

### [](#version-3-4-11)Version 3.4.11 (12 Sept 2023)

Version 3.4.11 is the twelfth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.11.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.11) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.11)

#### [](#known-issues-6)Known Issues

* [NCBC-3716](https://issues.couchbase.com/browse/NCBC-3716): If you are using Capella or Server versions 7.6.0+, we strongly encourage you to upgrade to SDK v3.5.1+. While this version will continue be compatible and supported with server 7.6 (and newer instances of Capella, using 7.6), you may encounter timeout exceptions during rebalances under KV high workload.

#### [](#fixed-issues-19)Fixed Issues

* [NCBC-3446](https://issues.couchbase.com/browse/NCBC-3446): When passed as `readonly(true)`, Readonly Query was accepting `UPDATE` query and was updating the document in collection, when it should have failed. This should no longer occur.
* [NCBC-3448](https://issues.couchbase.com/browse/NCBC-3448): `IndexNotFoundException` was not raised when `QueryIndexManager.watchIndex` was called with a non-existent index — this has been fixed, and the correct exception should now be thrown.
* [NCBC-3460](https://issues.couchbase.com/browse/NCBC-3460): Fixed a bug where a null reference exception was sometimes occurring when bootstrapping a Memcached bucket.
* [NCBC-3467](https://issues.couchbase.com/browse/NCBC-3467): Fixed a regression in lambda-based sub doc API, due to `LookupInResult` changes.

#### [](#new-features-and-behavioral-changes-8)New Features and Behavioral Changes

* [NCBC-3449](https://issues.couchbase.com/browse/NCBC-3449): The SDK was throwing a `NullReferenceException` for the `ITypeSerializer` when setting a Transcoder in the Options due to erroneous logic in `CouchbaseCollection`. Transcoders are now used for deserialization, and RawBinary/RawString Transcoders now initialise the `DefaultSerializer` when instantiated (like for JsonTranscoder) which, along with changed logic in `CouchbaseCollection` when returning `LookupInResults`, means that this no longer occurs.
* [NCBC-3466](https://issues.couchbase.com/browse/NCBC-3466): Improvements for internal testing.
* [NCBC-3482](https://issues.couchbase.com/browse/NCBC-3482): Faster Failover/Push config is now ensabled by default.
* [NCBC-3130](https://issues.couchbase.com/browse/NCBC-3130): For improved performance and trimmability, `OrphanReporter` has been rewritten to serialize POCOs using a `JsonSerializerContext` rather than using LINQ objects from Newtonsoft.
* [NCBC-3402](https://issues.couchbase.com/browse/NCBC-3402): Improved trimming support for internal DI.
* [NCBC-3404](https://issues.couchbase.com/browse/NCBC-3404): Replaced `Newtonsoft.Json` with `System.Text.Json`, using source generated `JsonSerializerContext`, for Eventing management. This is now compatible with trimming and AOT compilation, and should also provide performance benefits. Use System.Text.Json for Eventing Management
* [NCBC-3405](https://issues.couchbase.com/browse/NCBC-3405): Added trimming annotations to `LoggingMeter`.
* [NCBC-3420](https://issues.couchbase.com/browse/NCBC-3420): The `DefaultSerializer` was used to deserialize query plans — for consistency, this now uses `System.Text.Json`.
* [NCBC-3453](https://issues.couchbase.com/browse/NCBC-3453): Reduced the default value for the `IdleHttpConnectionTimeout` client setting to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures.
* [NCBC-3471](https://issues.couchbase.com/browse/NCBC-3471): Microsoft DI Extensions (`Couchbase.Extensions.DependencyInjection`) are now more compatible with trimming and AOT compilation. The changes also help application start up speed in non-AOT cases.

### [](#version-3-4-10)Version 3.4.10 (03 Aug 2023)

> [!WARNING]
> v3.4.10 is incompatible with Server 7.6 and later — do not use. This version of the SDK has been deprecated; use 3.4.11 or greater. Details can be found in [NCBC-3724](https://issues.couchbase.com/browse/NCBC-3724).

Version 3.4.10 is the eleventh release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.10.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.10) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.10)

#### [](#fixed-issues-20)Fixed Issues

* [NCBC-3424](https://issues.couchbase.com/browse/NCBC-3424): Future server versions will add an extra item to the features list returned, which effects the parsing of the body. This change prepares for the effects of those flexible framing extras.
* [NCBC-3445](https://issues.couchbase.com/browse/NCBC-3445): At some point, `SubDocMultiPathFailureDeleted` was added as a special case of `SubDocMultiPathFailure`, but from an SDK point of view they should be handled them similarly. This change ensures that when doing a `LookupIn` against a Tombstone with `AccessDeleted` flag set, `SubDocMultiPathFailureDeleted` response status should not throw, and should be treated the same as `SubDocMultiPathFailure`.

#### [](#new-features-and-behavioral-changes-9)New Features and Behavioral Changes

* [NCBC-3423](https://issues.couchbase.com/browse/NCBC-3423): Added `GetClusterConfigWithKnownVersion` support to Hello.
* [NCBC-3425](https://issues.couchbase.com/browse/NCBC-3425): Added a `HELLO` flag called `DedupeNotMyVbucketClustermap`.
* [NCBC-3427](https://issues.couchbase.com/browse/NCBC-3427): Added `SnappyEverywhere` flag support, in preparation for the .NET SDK supporting Compression.
* [NCBC-3428](https://issues.couchbase.com/browse/NCBC-3428): Added `ClustermapChangeNotificationBrief` flag support to subscribe to configuration notifications, where available.
* [NCBC-3429](https://issues.couchbase.com/browse/NCBC-3429): Added support for Duplex mode flag to Hello, for Unordered Execution.
* [NCBC-3430](https://issues.couchbase.com/browse/NCBC-3430): Added `ClustermapChangeNotification` flag support.
* [NCBC-3421](https://issues.couchbase.com/browse/NCBC-3421): Deserializing K/V operations with the `DefaultSerializer` was allocating an excessive number of buffers for each operation. This change introduces a reusable pool of text readers which reads directly from the memory buffer without stream-related overhead or intermediate buffers. This results in a performance gain and a significant reduction in heap allocations when deserializing from a memory buffer.
* [NCBC-3432](https://issues.couchbase.com/browse/NCBC-3432): Added additional logging at the IO level to capture more details of exceptions thrown when sockets are opened.
* [NCBC-3438](https://issues.couchbase.com/browse/NCBC-3438): Several of the listed dependencies for the .NET 6 target were unnecessary, as those packages are now included in the .NET framework and we’re not targeting a higher version. We have removed these NuGet dependencies for the .NET 6 Target, which will reduce restore time and size for consumers.

### [](#version-3-4-9)Version 3.4.9 (20 July 2023)

Version 3.4.9 is the tenth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.9.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.9) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.9)

#### [](#fixed-issues-21)Fixed Issues

* [NCBC-3367](https://issues.couchbase.com/browse/NCBC-3367): The SDK was returning `QueryIndexes` with null values for Bucket/Scope/Collection names (BucketName should return the Keyspace value when null). Added BucketName field with backing field for conditionally returning either BucketNameField or Keyspace.
* [NCBC-3417](https://issues.couchbase.com/browse/NCBC-3417): `MutateIn` was modifying global Transcoder setting; nothing registered as a Singleton should be mutable and changes have been made to ensure that this can no longer happen.
* [NCBC-3433](https://issues.couchbase.com/browse/NCBC-3433): Fixed regression in 3.4.8 which could cause `IOException` if Query has no content.

#### [](#new-features-and-behavioral-changes-10)New Features and Behavioral Changes

* [NCBC-3412](https://issues.couchbase.com/browse/NCBC-3412): Support Query with Read from Replica
* [NCBC-3418](https://issues.couchbase.com/browse/NCBC-3418): Experimental support for HTTP2 when using the Query service
* [NCBC-3351](https://issues.couchbase.com/browse/NCBC-3351): SDKs must encode URIs
* [NCBC-3437](https://issues.couchbase.com/browse/NCBC-3437): Add .NET 4.8 back to .NET SDK unit and integration tests
* [NCBC-3384](https://issues.couchbase.com/browse/NCBC-3384): Resolve all compiler warnings
* [NCBC-3386](https://issues.couchbase.com/browse/NCBC-3386): Add conditional support for TLS 1.3 for .NET 6.0 and higher
* [NCBC-3401](https://issues.couchbase.com/browse/NCBC-3401): Scan: Implement latest RFC revision (#9)
* [NCBC-3403](https://issues.couchbase.com/browse/NCBC-3403): Improve memory usage of SearchClient

### [](#version-3-4-8)Version 3.4.8 (12 June 2023)

Version 3.4.8 is the ninth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.8.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.8) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.8)

#### [](#fixed-issues-22)Fixed Issues

* [NCBC-3392](https://issues.couchbase.com/browse/NCBC-3392): Scan: `RangeScanCreate` operation did not receive the `MutationTokens` from the `ScanOptions`, as `ConsistentWit` was not sent in RangeScanCreate packets. This has been remedied, and `MutationState` tokens are now sent in `RangeScanCreate` packets.
* [NCBC-3395](https://issues.couchbase.com/browse/NCBC-3395): Scan: Sampling Scan Limit parameter must be < 0\. An `InvalidArgumentException` is now thrown when creating a `SamplingScan` with Limit < 0.
* [NCBC-3399](https://issues.couchbase.com/browse/NCBC-3399): Fixed edge case in bootstrapping around NRE in `PruneNodes`.

#### [](#new-features-and-behavioral-changes-11)New Features and Behavioral Changes

* [NCBC-3391](https://issues.couchbase.com/browse/NCBC-3391): Scan: Implemented `PrefixScan` helper method.

### [](#version-3-4-7)Version 3.4.7 (07 June 2023)

Version 3.4.7 is the eighth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.7) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.7)

#### [](#fixed-issues-23)Fixed Issues

* [NCBC-3350](https://issues.couchbase.com/browse/NCBC-3350): `NotMyVBucket` will no longer result in `TaskCancellationException`.
* [NCBC-3376](https://issues.couchbase.com/browse/NCBC-3376): Correct timeout response will now be returned during a rebalance.
* [NCBC-3379](https://issues.couchbase.com/browse/NCBC-3379): OpenTelemetry tracing was losing track of the parent span in cases where the parent span was not sampled, resulting in orphaned spans and increased trace volume. By capturing the `ExecutionContext`, if any, when queuing operations on the `ChannelConnectionPool`, and sending the operations on the captured context, the spans are now correctly sampled.
* [NCBC-3380](https://issues.couchbase.com/browse/NCBC-3380): When `IOperation.ExtractBody` is called it should always dispose of the returned IMemoryOwner, generally with a using statement; . Failure to do so will cause the buffer to be garbage collected rather than returned to the ArrayPool — which can lead to memory holes and decreased GC efficiency. This has no been fixed, and should no longer occur.
* [NCBC-3382](https://issues.couchbase.com/browse/NCBC-3382): Streaming support now working correctly for Analytics, Query, and Views.
* [NCBC-3383](https://issues.couchbase.com/browse/NCBC-3383): Couchbase.ServiceNotAvailableException: Service n1ql is either not configured or cannot be reached.
* [NCBC-3390](https://issues.couchbase.com/browse/NCBC-3390): Get Cluster Map operations were linked to the bootstrap trace, cusing erroneous large traces. A check has been added which fixes this.
* [NCBC-3392](https://issues.couchbase.com/browse/NCBC-3392): Scan: Use `ConsistentWith` MutationTokens for `RangeScanCreate` Operation.
* [NCBC-3393](https://issues.couchbase.com/browse/NCBC-3393): Fixed regression where `OperationCanceledException` continues after rebalance completes.

#### [](#new-features-and-behavioral-changes-12)New Features and Behavioral Changes

* [NCBC-3391](https://issues.couchbase.com/browse/NCBC-3391): Scan: Implemented `PrefixScan` helper method.
* [NCBC-2394](https://issues.couchbase.com/browse/NCBC-2394): Query 4040 is now handled like 4050, _et al_ — e.g. prepared statement cache for it is removed and transparent reprepare is performed.
* [NCBC-3354](https://issues.couchbase.com/browse/NCBC-3354): Changed logging to use `LoggerMessage` in Channel classes. Added `ChannelConnectionEvent` in LoggingEvents.
* [NCBC-3378](https://issues.couchbase.com/browse/NCBC-3378): Improve `GET_CID` use in `CouchbaseBucket`.
* [NCBC-3381](https://issues.couchbase.com/browse/NCBC-3381): Removed `ClusterNodesChanged` and `VBucketMapChanged` (which are only used internally) from `BucketConfig`.

### [](#version-3-4-6)Version 3.4.6 (12 May 2023)

Version 3.4.6 is the seventh release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.6) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.6)

#### [](#fixed-issues-24)Fixed Issues

* [NCBC-3300](https://issues.couchbase.com/browse/NCBC-3300): SamplingScan: Fixed bug in limiting option
* [NCBC-3301](https://issues.couchbase.com/browse/NCBC-3301): SamplingScan: Fixed bug where requesting too few documents returned incorrect responses.
* [NCBC-3345](https://issues.couchbase.com/browse/NCBC-3345): In the latest development server versions, 0xD is occasionally returned by the server.

#### [](#new-features-and-behavioral-changes-13)New Features and Behavioral Changes

* [NCBC-3273](https://issues.couchbase.com/browse/NCBC-3273): Added SDK Support for Native KV Range Scans.
* [NCBC-3364](https://issues.couchbase.com/browse/NCBC-3364): Improved hot-path performance in `ClusterContext.GetOrCreateBucketAsync`.

### [](#version-3-4-5)Version 3.4.5 (20 April 2023)

Version 3.4.5 is the sixth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.5) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.5)

#### [](#fixed-issues-25)Fixed Issues

* [NCBC-3334](https://issues.couchbase.com/browse/NCBC-3334): `KvNotMyVBucket` errors after add node + rebalance.
* [NCBC-3337](https://issues.couchbase.com/browse/NCBC-3337): NullReferenceException when bootstrapping against a non-existent bucket.
* [NCBC-3347](https://issues.couchbase.com/browse/NCBC-3347): IGetResult shouldn’t have an internal Status property.
* [NCBC-3360](https://issues.couchbase.com/browse/NCBC-3360): Fix QueryContext bug in QueryIndexManager.
* [NCBC-3362](https://issues.couchbase.com/browse/NCBC-3362): SDK writes to \_default collection when intended collection is dropped.
* [NCBC-3363](https://issues.couchbase.com/browse/NCBC-3363): SubDoc SuccessDeleted not treated as Success.
* [NCBC-3365](https://issues.couchbase.com/browse/NCBC-3365): Change Search Metadata setters from internal to public.
* [NCBC-3369](https://issues.couchbase.com/browse/NCBC-3369): Ensure ClusterNode list matches Cluster config after rebalance up/down.
* [NCBC-3372](https://issues.couchbase.com/browse/NCBC-3372): Removed/rebalanced out node continues to be hit with http requests.

#### [](#new-features-and-behavioral-changes-14)New Features and Behavioral Changes

* [NCBC-3220](https://issues.couchbase.com/browse/NCBC-3220): Properly map server query timeout while streaming (1080).
* [NCBC-3308](https://issues.couchbase.com/browse/NCBC-3308): Scan: Refactor sorting/merging into non-blocking implementation.
* [NCBC-3332](https://issues.couchbase.com/browse/NCBC-3332): Protostellar: Implement KV SubDoc.
* [NCBC-3355](https://issues.couchbase.com/browse/NCBC-3355): Update FIT performer.
* [NCBC-3274](https://issues.couchbase.com/browse/NCBC-3274): Add public API for KV Range Scan.
* [NCBC-3370](https://issues.couchbase.com/browse/NCBC-3370): Lock on sync object instead of nodes list.

### [](#version-3-4-4)Version 3.4.4 (10 March 2023)

Version 3.4.4 is the fifth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.4) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.4)

#### [](#fixed-issues-26)Fixed Issues

* [NCBC-3340](https://issues.couchbase.com/browse/NCBC-3340): When an op timed out, the socket connection was closed and then recreated. With a large number of unexpected timeouts, many sockets could be left in `TIME_WAIT`. Making `ChannelConnectionProcessor` reuse connections after timeout should reduce the number of file descripters and local ports left open.
* [NCBC-3356](https://issues.couchbase.com/browse/NCBC-3356): Cluster level `query_context`, which is not supported by Server versions earlier than 7.0, has been removed for these versions.
* [NCBC-3343](https://issues.couchbase.com/browse/NCBC-3343): Fixed a bug where `SelectBucket` may not be called on the internal node used as the bootstrapping endpoint. This resulted in a `BucketNotConnected` error for certain ops — which will now no longer occur.

#### [](#new-features-and-behavioral-changes-15)New Features and Behavioral Changes

* [NCBC-3309](https://issues.couchbase.com/browse/NCBC-3309): Handled `query_context` changes by adding to every index manager request.
* [NCBC-3348](https://issues.couchbase.com/browse/NCBC-3348): When ConnectionString hosts are null, the SDK now throws an exception, with a more explicit error message.
* [NCBC-3353](https://issues.couchbase.com/browse/NCBC-3353): Removed build targets for out-of-support versions of .NET Framework.

### [](#version-3-4-3)Version 3.4.3 (08 February 2023)

Version 3.4.3 is the fourth release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.3) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.3)

#### [](#fixed-issues-27)Fixed Issues

* [NCBC-3316](https://issues.couchbase.com/browse/NCBC-3316): Scan: Refactored operation parsing, so `RangeScanContinue.OnNext()` doesn’t get called after the first batch of a partition has been consumed.
* [NCBC-3329](https://issues.couchbase.com/browse/NCBC-3329): `NamedBucketProxyGenerator` and `NamedCollectionProxyGenerator` caches were not thread-safe during start up. This applies primarily to unit testing scenarios — most MVC applications were not affected, as it doesn’t affect anything once the DI container is configured, because startup DI registration is single-threaded.
* [NCBC-3331](https://issues.couchbase.com/browse/NCBC-3331): Retrying Named Prepared Queries from the SDK — added an example of a custom `RetryStrategy` for the case where you do not want the named prepared statement to be retried, and want a fast-fail in that specific case and tests for named parameters.

#### [](#new-features-and-behavioral-changes-16)New Features and Behavioral Changes

* [NCBC-1999](https://issues.couchbase.com/browse/NCBC-1999): Added a `TryGetAsync` method to handle the case where `KeyNotFound` is returned by the server — for improved performance over throwing an exception.
* [NCBC-3293](https://issues.couchbase.com/browse/NCBC-3293): Handle case where a response contains a document that exceeds 8120b \[_sic_\] — provided a test to show that large documents are correctly parsed and returned to the caller.
* [NCBC-3307](https://issues.couchbase.com/browse/NCBC-3307): Scan: Implemented `BatchByteLimit`, `BatchItemLimit`, and `BatchTimeLimit`.
* [NCBC-3318](https://issues.couchbase.com/browse/NCBC-3318): Protostellar: Exposed KV operation option values publicly, via read-only record copy.
* [NCBC-3326](https://issues.couchbase.com/browse/NCBC-3326): Encode Duration was tracked twice for the Threshold Tracing — as `RequestSpan` was disposed more than once. This has now been fixed, and the correct value should be returned.

### [](#version-3-4-2)Version 3.4.2 (13 January 2023)

Version 3.4.2 is the third release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.2)

#### [](#fixed-issues-28)Fixed Issues

* [NCBC-3269](https://issues.couchbase.com/browse/NCBC-3269): InternalServerFailureException error message caught in SDK Query Response
* [NCBC-3297](https://issues.couchbase.com/browse/NCBC-3297): KV Range Scan breaks with NCBC-2167
* [NCBC-3305](https://issues.couchbase.com/browse/NCBC-3305): Pickup latest range scan RFC changes
* [NCBC-3310](https://issues.couchbase.com/browse/NCBC-3310): Scan: Fix RangeScanContinue parsing offset
* [NCBC-3313](https://issues.couchbase.com/browse/NCBC-3313): Sub-Document LookupInAsync.Exists throws SubdocException when path not found

### [](#version-3-4-1)Version 3.4.1 (09 December 2022)

Version 3.4.1 is the second release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.1)

#### [](#fixed-issues-29)Fixed Issues

* [NCBC-3204](https://issues.couchbase.com/browse/NCBC-3204): CombinationTest failure: Test\_GetAndLockAsync\_Locked
* [NCBC-3283](https://issues.couchbase.com/browse/NCBC-3283): Search: Min function throws an exception if the argument is > 0
* [NCBC-3295](https://issues.couchbase.com/browse/NCBC-3295): KeyNotFound / DocumentNotFound should not trigger the Circuit Breaker
* [NCBC-3296](https://issues.couchbase.com/browse/NCBC-3296): PopulateCID caches Exceptions forever
* [NCBC-3298](https://issues.couchbase.com/browse/NCBC-3298): "couchbases://" Does not automatically enable TLS in SDK 3.4
* [NCBC-3304](https://issues.couchbase.com/browse/NCBC-3304): ObjectDisposedException on GET command during rebalance

#### [](#new-features-and-behavioral-changes-17)New Features and Behavioral Changes

* [NCBC-2167](https://issues.couchbase.com/browse/NCBC-2167): Refactor operation callback handling and exception mapping

### [](#version-3-4-0)Version 3.4.0 (10 November 2022)

Version 3.4.0 is the first release of the 3.4 series.

[Download](https://packages.couchbase.com/clients/net/3.4/Couchbase-Net-Client-3.4.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.4.0) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.4.0)

#### [](#fixed-issues-30)Fixed Issues

* [NCBC-3246](https://issues.couchbase.com/browse/NCBC-3246): EndpointDiagnostics.State always returns "Authenticating" for KV and not implemented per RFC
* [NCBC-3266](https://issues.couchbase.com/browse/NCBC-3266): A timeout may have a status of "success"
* [NCBC-3281](https://issues.couchbase.com/browse/NCBC-3281): Erroneous time reported in timeout log message.
* [NCBC-3286](https://issues.couchbase.com/browse/NCBC-3286): RetryHandler does not apply backoff when a request is not AlwaysRetry.

#### [](#new-features-and-behavioral-changes-18)New Features and Behavioral Changes

* [NCBC-3271](https://issues.couchbase.com/browse/NCBC-3271): Error Message for Bucket Hibernation

## [](#net-sdk-3-3-releases).NET SDK 3.3 Releases

### [](#version-3-3-6)Version 3.3.6 (06 October 2022)

Version 3.3.6 is the seventh release of the 3.3 series.

[Download](https://packages.couchbase.com/clients/net/3.3/Couchbase-Net-Client-3.3.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.3.6) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.3.6)

#### [](#fixed-issues-31)Fixed Issues

* [NCBC-3265](https://issues.couchbase.com/browse/NCBC-3265): Ensure SDK can bootstrap from a non-data-service node.
* [NCBC-3270](https://issues.couchbase.com/browse/NCBC-3270): Make `Increment` and `Decrement` take unsigned long delta, per the RFC.

#### [](#new-features-and-behavioral-changes-19)New Features and Behavioral Changes

* [NCBC-3258](https://issues.couchbase.com/browse/NCBC-3258): Changed `QueryRequest` from /query to /query/service.
* [NCBC-3263](https://issues.couchbase.com/browse/NCBC-3263): Support For Configuration Profiles added.
* [NCBC-2953](https://issues.couchbase.com/browse/NCBC-2953): Support for Serverless/Lambda Execution Environments.
* [NCBC-3261](https://issues.couchbase.com/browse/NCBC-3261): Where possible, we now use `ArrayPool` instead of `MemoryPool`.
* [NCBC-3264](https://issues.couchbase.com/browse/NCBC-3264): Improved performance of lambda processing for subdoc operations.
* [NCBC-3267](https://issues.couchbase.com/browse/NCBC-3267): When creating snapshot packages in Jenkins, the latest tag is now always used as a base for the snapshot name.
* [NCBC-3268](https://issues.couchbase.com/browse/NCBC-3268): `Session State` GA readiness.

### [](#version-3-3-5)Version 3.3.5 (16 September 2022)

Version 3.3.5 is the sixth release of the 3.3 series.

[Download](https://packages.couchbase.com/clients/net/3.3/Couchbase-Net-Client-3.3.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.3.5) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.3.5)

#### [](#fixed-issues-32)Fixed Issues

* [NCBC-3256](https://issues.couchbase.com/browse/NCBC-3256): Fixed issue where `Search.MetaData.TimeTook` was being parsed as ticks, not nanoseconds.
* [NCBC-3257](https://issues.couchbase.com/browse/NCBC-3257): Fixed a bug where operations failed on memcached bucket types.

### [](#version-3-3-4)Version 3.3.4 (02 August 2022)

Version 3.3.4 is the fifth release of the 3.3 series.

[Download](https://packages.couchbase.com/clients/net/3.3/Couchbase-Net-Client-3.3.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.3.4) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.3.4)

#### [](#fixed-issues-33)Fixed Issues

* [NCBC-3248](https://issues.couchbase.com/browse/NCBC-3248): Fixed issue where bootstrap did not continue after an `AuthenticationFailureException`.
* [NCBC-3252](https://issues.couchbase.com/browse/NCBC-3252): Fixed issue where the wrong error message was returned when bootstrapping a bucket.

#### [](#new-features-and-behavioral-changes-20)New Features and Behavioral Changes

* [NCBC-3193](https://issues.couchbase.com/browse/NCBC-3193): Removed erroneous `InvalidArgumentException` when TLS is enabled with defaults.
* [NCBC-3253](https://issues.couchbase.com/browse/NCBC-3253): This fixes an issue in Couchbase Server 6.5 FTS which fails when values of 0 are provided for "fuzziness" or "prefix\_length".

### [](#version-3-3-3)Version 3.3.3 (11 July 2022)

Version 3.3.3 is the fourth release of the 3.3 series.

[Download](https://packages.couchbase.com/clients/net/3.3/Couchbase-Net-Client-3.3.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.3.3) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.3.3)

#### [](#fixed-issues-34)Fixed Issues

* [NCBC-3010](https://issues.couchbase.com/browse/NCBC-3010): `BucketNotFoundException` incorrectly raised when there is no database running.
* [NCBC-3191](https://issues.couchbase.com/browse/NCBC-3191): `EventingFunctionManager` throws wrong exception for compilation failure.
* [NCBC-3214](https://issues.couchbase.com/browse/NCBC-3214): Fixed NuGet packaging issues causing problems with dependencies for some users.
* [NCBC-3231](https://issues.couchbase.com/browse/NCBC-3231): MutateIn throws `CAS` error instead of `KeyExists` when doc exists and `StoreSemantics.Insert`.
* [NCBC-3239](https://issues.couchbase.com/browse/NCBC-3239): `NullReferenceException` when bootstrapping fails and a mangement API call is made.
* [NCBC-3240](https://issues.couchbase.com/browse/NCBC-3240): `WaitUntilReadyAsync` fails when it cannot connect to a cluster before timeout.
* [NCBC-3241](https://issues.couchbase.com/browse/NCBC-3241): `QueryIndexManager` throws generic exception as opposed to `IndexNotFoundException`.

#### [](#new-features-and-behavioral-changes-21)New Features and Behavioral Changes

* [NCBC-3166](https://issues.couchbase.com/browse/NCBC-3166): Added performance best practices in API Docs.
* [NCBC-3224](https://issues.couchbase.com/browse/NCBC-3224): Flagged `ErrorContext` as uncommitted.
* [NCBC-3242](https://issues.couchbase.com/browse/NCBC-3242): Updated `Newtonsoft.JSON` to version `13.0.1` or later.
* [NCBC-2953](https://issues.couchbase.com/browse/NCBC-2953): Added support for Serverless/Lambda Execution Environments

### [](#version-3-3-2)Version 3.3.2 (16 June 2022)

Version 3.3.2 is the third release of the 3.3 series.

[Download](https://packages.couchbase.com/clients/net/3.3/Couchbase-Net-Client-3.3.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.3.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.3.2)

#### [](#fixed-issues-35)Fixed Issues

* [NCBC-3067](https://issues.couchbase.com/browse/NCBC-3067): GetAndLockAsync times out instead of throwing DocumentLockedException.
* [NCBC-3195](https://issues.couchbase.com/browse/NCBC-3195): N1QL queries with the default serializer don't read DateTimeOffset correctly.
* [NCBC-3197](https://issues.couchbase.com/browse/NCBC-3197): FailFast Retry Strategy May Result in Infinite Processing Loop for Query, Views, Analytics, Search requests.
* [NCBC-3198](https://issues.couchbase.com/browse/NCBC-3198): Blocked Task when Helo is called on a nonresponsive socket.
* [NCBC-3199](https://issues.couchbase.com/browse/NCBC-3199): Timeout log message uses misleading Operation.Timeout.
* [NCBC-3200](https://issues.couchbase.com/browse/NCBC-3200): Unlock returns DocumentLockedException.
* [NCBC-3201](https://issues.couchbase.com/browse/NCBC-3201): Remove bootstrap endpoint comparison from network resolution.
* [NCBC-3203](https://issues.couchbase.com/browse/NCBC-3203): NotMyVbucket exception while in mixed mode (CB 6.5 & 7.X).
* [NCBC-3205](https://issues.couchbase.com/browse/NCBC-3205): A locked status is mapped to temporary failure.
* [NCBC-3206](https://issues.couchbase.com/browse/NCBC-3206): DI provider caches bad bootstrap results.
* [NCBC-3216](https://issues.couchbase.com/browse/NCBC-3216): LoggingMeterReport can crash the process in the timer.
* [NCBC-3217](https://issues.couchbase.com/browse/NCBC-3217): InternalSerializationContext throws a NotSupportedException when the object graph contains JObject.
* [NCBC-3218](https://issues.couchbase.com/browse/NCBC-3218): Redacted<T> doesn't close tags properly.
* [NCBC-3225](https://issues.couchbase.com/browse/NCBC-3225): QueryOptions.MaxServerParallelism should be serialized as a string.
* [NCBC-3226](https://issues.couchbase.com/browse/NCBC-3226): Opaque is written to packet in NBO making WireShark tracing difficult.
* [NCBC-3227](https://issues.couchbase.com/browse/NCBC-3227): Opaque is reused during retries making debugging difficult.
* [NCBC-3232](https://issues.couchbase.com/browse/NCBC-3232): Ensure collections are enabled for all connections.
* [NCBC-3236](https://issues.couchbase.com/browse/NCBC-3236): Issues with KV and NMVB against pre 6.5 cluster.

#### [](#new-features-and-behavioral-changes-22)New Features and Behavioral Changes

* [NCBC-1973](https://issues.couchbase.com/browse/NCBC-1973): .NET Doc on Error Handling for SDK 3 v1.
* [NCBC-3186](https://issues.couchbase.com/browse/NCBC-3186): Review .NET SDK Snippets in VSCode.
* [NCBC-3189](https://issues.couchbase.com/browse/NCBC-3189): Mark IEventingFunctionManager as Uncommitted.
* [NCBC-3202](https://issues.couchbase.com/browse/NCBC-3202): Dead Link in Repo.
* [NCBC-3223](https://issues.couchbase.com/browse/NCBC-3223): Flag RetryReason as Volatile.
* [NCBC-3002](https://issues.couchbase.com/browse/NCBC-3002): Validate: Document accessed after Locking should raise DocumentLockedException or Timeout?.
* [NCBC-3028](https://issues.couchbase.com/browse/NCBC-3028): Upgrade App.Metrics to mitigate security scan warnings.
* [NCBC-3038](https://issues.couchbase.com/browse/NCBC-3038): Add retry reasons to ErrorContext.
* [NCBC-3078](https://issues.couchbase.com/browse/NCBC-3078): Mark synchronous methods in data structures as obsolete.
* [NCBC-3168](https://issues.couchbase.com/browse/NCBC-3168): Add exception to debug log in CircuitBreaker.
* [NCBC-3188](https://issues.couchbase.com/browse/NCBC-3188): Add retry reasons to ErrorContext for UnAmbiguousTimeouts.
* [NCBC-3207](https://issues.couchbase.com/browse/NCBC-3207): Remove dependency on Crc32.NET in Transactions.
* [NCBC-3208](https://issues.couchbase.com/browse/NCBC-3208): Review all SDK and verify if new SQL++ Feature introduced in 7.1.1(Include MISSING) will work as expected without any change in the code.
* [NCBC-3228](https://issues.couchbase.com/browse/NCBC-3228): Make BestEffortRetryStrategy.RetryAfter virtual so it can be overridden.
* [NCBC-3229](https://issues.couchbase.com/browse/NCBC-3229): Add 30s lock limit for GetAndLock API docs.
* [NCBC-3152](https://issues.couchbase.com/browse/NCBC-3152): Improved code documention for KV API.

### [](#version-3-3-1)Version 3.3.1 (03 May 2022)

Version 3.3.1 is the second release of the 3.3 series.

[Download](https://packages.couchbase.com/clients/net/3.3/Couchbase-Net-Client-3.3.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.3.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.3.1)

#### [](#fixed-issues-36)Fixed Issues

* [NCBC-3192](https://issues.couchbase.com/browse/NCBC-3192): Fixed erroneous `InvalidArgumentException` with default TLS settings.

### [](#version-3-3-0-27-april-2022)Version 3.3.0 (27 April 2022)

> [!WARNING]
> This version introduces an issue, [NCBC-3192](https://issues.couchbase.com/browse/NCBC-3192), which impacts TLS/SSL. Please use [version 3.3.1](#version-3-3-1) instead.

Version 3.3.0 is the first release of the 3.3 series (delisted from NuGet 4/28/2022).

[Download](https://packages.couchbase.com/clients/net/3.3/Couchbase-Net-Client-3.3.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.3.0)

#### [](#special-note)Special Note

* During a rebalance upgrade from 6.x (or any earlier version) to 7x, in mixed mode (where you are communicating with Couchbase Server whilst some but not all nodes are upgraded), there is a known issue where data may be written to the wrong location. The solution is to either upgrade to 3.2.9 or greater, or to pause application processing so there are no writes until you have upgraded all nodes. If you encounter a similar situation during migration and need help with mitigation, please contact our support team.

#### [](#fixed-issues-37)Fixed Issues

* [NCBC-2847](https://issues.couchbase.com/browse/NCBC-2847), [NCBC-3123](https://issues.couchbase.com/browse/NCBC-3123), [NCBC-3115](https://issues.couchbase.com/browse/NCBC-3115), [NCBC-3124](https://issues.couchbase.com/browse/NCBC-3124), [NCBC-3151](https://issues.couchbase.com/browse/NCBC-3151), [NCBC-3179](https://issues.couchbase.com/browse/NCBC-3179), [NCBC-3000](https://issues.couchbase.com/browse/NCBC-3000): Made it simpler to diagnose failures by ensuring that various exceptions including `AuthenticationFailureException`, `BucketNotFoundException`, `EventingFunctionNotFoundException`, FTS exceptions, `ScopeNotFoundException`, `BucketExistsException`, `AuthenticationFailedException` are correctly thrown.
* [NCBC-3164](https://issues.couchbase.com/browse/NCBC-3164), [NCBC-3177](https://issues.couchbase.com/browse/NCBC-3177): Fix bugs where NullReferenceException were thrown in SendAsync (because the OperationBuilder has not been set for a NOOP) and rebalancing (when the cluster map was missing an alternate address).
* [NCBC-3190](https://issues.couchbase.com/browse/NCBC-3190): Fixed bug where CreateDataverseAsync failed when passed an empty TimeSpan.

#### [](#new-features-and-behavioral-changes-23)New Features and Behavioral Changes

* [NCBC-3173](https://issues.couchbase.com/browse/NCBC-3173), [NCBC-3182](https://issues.couchbase.com/browse/NCBC-3182): Bundle Capella CA cert with SDK, and use it by default. (Note: fix is .NET 5+ only)
* [NCBC-2870](https://issues.couchbase.com/browse/NCBC-2870): Added OpenTelemetry 1.2.0 AggregatingMeter Otel integration.
* [NCBC-3082](https://issues.couchbase.com/browse/NCBC-3082): Support parameterized N1QL queries using string interpolation in .NET 6
* [NCBC-3180](https://issues.couchbase.com/browse/NCBC-3180): Fixed `GetAllIndexes` response on default collection.
* [NCBC-3043](https://issues.couchbase.com/browse/NCBC-3043): Made `ChannelConnectionPool` the default. This was added in 3.1.2, and is now the default, replacing `DataFlowConnectionPool`. (To revert to the previous connection pool set `ClusterOptions.Experiments.ChannelConnectionPools` to false.)
* [NCBC-3079](https://issues.couchbase.com/browse/NCBC-3079): Improved logging performance in hot paths.
* [NCBC-3126](https://issues.couchbase.com/browse/NCBC-3126): Reduce heap allocations deserializing vBucket maps.
* [NCBC-3132](https://issues.couchbase.com/browse/NCBC-3132), [NCBC-3134](https://issues.couchbase.com/browse/NCBC-3134), [NCBC-3137](https://issues.couchbase.com/browse/NCBC-3137): Switched to `` System.Text.Json `for exception error contexts, `OperationSpec.ToString ``, `ClusterVersionProvider`
* [NCBC-3138](https://issues.couchbase.com/browse/NCBC-3138): Support both Newtonsoft and System.Text.Json\` for DiagnosticReport

## [](#net-sdk-3-2-releases).NET SDK 3.2 Releases

### [](#version-3-2-9-4-april-2022)Version 3.2.9 (4 April 2022)

Version 3.2.9 is the ninth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.9.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.9) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.9)

#### [](#special-note-2)Special Note

* During a rebalance upgrade from 6.x (or any earlier version) to 7x, in mixed mode (where you are communicating with Couchbase Server whilst some but not all nodes are upgraded), there is a known issue where data may be written to the wrong location. The solution is to either upgrade to 3.2.9, or to pause application processing so there are no writes until you have upgraded all nodes. If you encounter a similar situation during migration and need help with mitigation, please contact our support team.
* Between bug fixes and performance improvements, the `ChannelConnectionPool` will be made the default in a future release. Give it a try now with `ClusterOptions.Experiments.ChannelConnectionPools = true;`

#### [](#fixed-issues-38)Fixed Issues

* [NCBC-3174](https://issues.couchbase.com/browse/NCBC-3174): Out of Retries misclassified as Operation Timed Out
* [NCBC-3176](https://issues.couchbase.com/browse/NCBC-3176): ExponentialBackoff only ever increases globally
* [NCBC-2994](https://issues.couchbase.com/browse/NCBC-2994): Trace listener leaks spans when an exception is thrown
* [NCBC-3076](https://issues.couchbase.com/browse/NCBC-3076): NullReferenceException when tracing span has no parent
* [NCBC-3111](https://issues.couchbase.com/browse/NCBC-3111): PingReport output should not include last\_activity\_us
* [NCBC-3122](https://issues.couchbase.com/browse/NCBC-3122): Duplicate view exception types for DesignDocumentNotFound
* [NCBC-3127](https://issues.couchbase.com/browse/NCBC-3127): Search query ConsistentWith uses bucket name instead of index name for scan vector key
* [NCBC-3149](https://issues.couchbase.com/browse/NCBC-3149): Synchronize bucket creation to avoid Object Disposed Exceptions
* [NCBC-3160](https://issues.couchbase.com/browse/NCBC-3160): Wrong host was used for lookup
* [NCBC-3163](https://issues.couchbase.com/browse/NCBC-3163): Bucket name escaping in QueryIndexManager.GetAllIndexesAsync
* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-3172](https://issues.couchbase.com/browse/NCBC-3172): .NET SDK fails to connect to correct node in custom port (cluster\_run) multi-node setup

#### [](#new-features-and-behavioral-changes-24)New Features and Behavioral Changes

* [NCBC-3099](https://issues.couchbase.com/browse/NCBC-3099): Clean up uses of ToString() on primitives to be sure we use InvariantCulture.
* [NCBC-3125](https://issues.couchbase.com/browse/NCBC-3125): Use System.Text.Json for bucket management
* [NCBC-3133](https://issues.couchbase.com/browse/NCBC-3133): Use System.Text.Json to serialize OperationResult and OperationResult<T>.ToString()
* [NCBC-3150](https://issues.couchbase.com/browse/NCBC-3150): Improve error messages in views and FTS
* [NCBC-3168](https://issues.couchbase.com/browse/NCBC-3168): Add exception to debug log in CircuitBreaker

### [](#version-3-2-8-2-march-2022)Version 3.2.8 (2 March 2022)

Version 3.2.8 is the eighth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.8.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.8) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.8)

> [!NOTE]
> .NET Core 2.1 support has been dropped from the SDK, as of 3.2.5\. This corresponds to Microsoft’s decision to EOL .NET Core 2.1 on August 21, 2021\.

#### [](#known-issues-7)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-39)Fixed Issues

* [NCBC-3091](https://issues.couchbase.com/browse/NCBC-3091): NRE GetDocumentFromReplicaAsync when EndPoint is null v3.2.X
* [NCBC-3110](https://issues.couchbase.com/browse/NCBC-3110): PingReport does not honor token or default timeout
* [NCBC-3114](https://issues.couchbase.com/browse/NCBC-3114): Json Converters not used for some EventingFunctionSetting fields
* [NCBC-3119](https://issues.couchbase.com/browse/NCBC-3119): MutateIn does not use registered ITranscoder or ITypeSerializer

#### [](#new-features-and-behavioral-changes-25)New Features and Behavioral Changes

* [NCBC-3103](https://issues.couchbase.com/browse/NCBC-3103): Integrate Transactions into couchbase-net-client repo
* [NCBC-3105](https://issues.couchbase.com/browse/NCBC-3105): Build and package Couchbase.Transactions with CouchbaseNetClient
* [NCBC-2176](https://issues.couchbase.com/browse/NCBC-2176): 3.0 API Migration guide
* [NCBC-2711](https://issues.couchbase.com/browse/NCBC-2711): Build DocFx site in Jenkins during release pipeline.
* [NCBC-3112](https://issues.couchbase.com/browse/NCBC-3112): Update integration tests to work with System.Text.Json
* [NCBC-3012](https://issues.couchbase.com/browse/NCBC-3012): Review GitHub protocol security and replace git://
* [NCBC-3017](https://issues.couchbase.com/browse/NCBC-3017): Expose key/value metrics for instrumentation and observability
* [NCBC-3060](https://issues.couchbase.com/browse/NCBC-3060): Reduce heap allocations for ClusterNode.SendAsync
* [NCBC-3081](https://issues.couchbase.com/browse/NCBC-3081): Reuse CancellationTokenSources which have not timed out
* [NCBC-3113](https://issues.couchbase.com/browse/NCBC-3113): Update DataStructures to be compatible with System.Text.Json
* [NCBC-3120](https://issues.couchbase.com/browse/NCBC-3120): Use System.Text.Json to serialize QueryOptions

### [](#version-3-2-7-1-february-2022)Version 3.2.7 (1 February 2022)

Version 3.2.7 is the seventh release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.7) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.7)

> [!NOTE]
> .NET Core 2.1 support has been dropped from the SDK, as of 3.2.5\. This corresponds to Microsoft’s decision to EOL .NET Core 2.1 on August 21, 2021\.

#### [](#known-issues-8)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-40)Fixed Issues

* [NCBC-3085](https://issues.couchbase.com/browse/NCBC-3085): Fixed potential issue with `Random.Next` returning only zero, by using `RandomNumberGenerator.GetInt32` if available.
* [NCBC-3086](https://issues.couchbase.com/browse/NCBC-3086): Improved error handling in QueryIndexManager.
* [NCBC-3090](https://issues.couchbase.com/browse/NCBC-3090): Fixed TaskCancellationException in EventingFunctionManager.
* [NCBC-3092](https://issues.couchbase.com/browse/NCBC-3092): Resolve DNS for each connection rather than node bootstrap.
* [NCBC-3095](https://issues.couchbase.com/browse/NCBC-3095): Modified to shutdown the Bootstrapper loop on Dispose, avoiding an indefinite loop.
* [NCBC-3096](https://issues.couchbase.com/browse/NCBC-3096): Cleaned up `CancellationTokenSource` handling in ConfigHandler.
* [NCBC-3100](https://issues.couchbase.com/browse/NCBC-3100): Included `LastDispatchedFrom` and `LastDispatchedTo` in `IErrorContext` implementations.
* [NCBC-3102](https://issues.couchbase.com/browse/NCBC-3102): Fixed a bug where the `RemoteHost` tag was assigned the value of LocalHost when an Orphaned report is generated.
* [NCBC-3107](https://issues.couchbase.com/browse/NCBC-3107): Escape keyspace values with backticks only if missing, fixing an error where `IQueryIndexManager` didn’t accept some bucket names.
* [NCBC-3109](https://issues.couchbase.com/browse/NCBC-3109): Fixed issue with Quota Limited Exceptions not being thrown for some Management apis.

#### [](#new-features-and-behavioral-changes-26)New Features and Behavioral Changes

* [NCBC-2964](https://issues.couchbase.com/browse/NCBC-2964): Added `QueryOptions.PreserveExpiry`
* [NCBC-2973](https://issues.couchbase.com/browse/NCBC-2973): Enhanced Index Management API with ability to manage indexes for a collection or scope.
* [NCBC-3035](https://issues.couchbase.com/browse/NCBC-3035): Improved performance of EnumExtensions method calls.
* [NCBC-3036](https://issues.couchbase.com/browse/NCBC-3036): Added tracing spans for improved Observability of compression/decompression performance.
* [NCBC-3059](https://issues.couchbase.com/browse/NCBC-3059): Reduced heap allocations surrounding OperationCancellationRegistration.
* [NCBC-3063](https://issues.couchbase.com/browse/NCBC-3063): Replaced Stopwatch in AsyncState with a lightweight approach.
* [NCBC-3089](https://issues.couchbase.com/browse/NCBC-3089): Added clone method to QueryOptions to avoid reuse and potential threading issues.
* [NCBC-3097](https://issues.couchbase.com/browse/NCBC-3097): Reduced risk of odd behaviors during connection pool scale down with use of `TaskCreationOptions.RunContinuationsAsynchronously`.

### [](#version-3-2-6-12-january-2022)Version 3.2.6 (12 January 2022)

Version 3.2.6 is the sixth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.6) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.6)

> [!NOTE]
> .NET Core 2.1 support has been dropped from the SDK, as of 3.2.5\. This corresponds to Microsoft’s decision to EOL .NET Core 2.1 on August 21, 2021\.

#### [](#known-issues-9)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-41)Fixed Issues

* [NCBC-2647](https://issues.couchbase.com/browse/NCBC-2647): `CreatePrimaryIndexAsync` throws exceptions / ignores `IgnoreIfExists`.
* [NCBC-2829](https://issues.couchbase.com/browse/NCBC-2829): NoOp operations can fail with an `ObjectDisposedException` on MultiplexingConnection.
* [NCBC-2977](https://issues.couchbase.com/browse/NCBC-2977): When you cannot connect to a bucket you may recieve a Memcached bucket error.
* [NCBC-2980](https://issues.couchbase.com/browse/NCBC-2980): Threshold Logging report is missing server duration(s).
* [NCBC-2981](https://issues.couchbase.com/browse/NCBC-2981): Threshold Logging report is missing timeout.
* [NCBC-2999](https://issues.couchbase.com/browse/NCBC-2999): Subdocument Operation `LookupInAsync` must throw `PathNotFoundException`.
* [NCBC-3008](https://issues.couchbase.com/browse/NCBC-3008): `RequestTooBigException` should be `ValueTooLargeException`.
* [NCBC-3047](https://issues.couchbase.com/browse/NCBC-3047): Tracing is not stopped when the cluster is disposed.
* [NCBC-3050](https://issues.couchbase.com/browse/NCBC-3050): Exception iterating over a DataStructures dictionary.
* [NCBC-3057](https://issues.couchbase.com/browse/NCBC-3057): Incorrect and inefficient db.couchbase.service span tags.
* [NCBC-3061](https://issues.couchbase.com/browse/NCBC-3061): PersistentDictionary should use a replace operation when setting `Item: key`.
* [NCBC-3062](https://issues.couchbase.com/browse/NCBC-3062): Don’t set `MaxIdleTime` on `ServicePoint` in .NET Core 3.1.
* [NCBC-3072](https://issues.couchbase.com/browse/NCBC-3072): `CollectionManager.GetAllScopesAsync` throws on success.
* [NCBC-3073](https://issues.couchbase.com/browse/NCBC-3073): PersistentDictionary. TryGetValue does not properly map path not found error.

#### [](#new-features-and-behavioral-changes-27)New Features and Behavioral Changes

* [NCBC-3029](https://issues.couchbase.com/browse/NCBC-3029): Create basic implementation of `SystemTextJsonSerializer`.
* [NCBC-3066](https://issues.couchbase.com/browse/NCBC-3066): Develop Key/Value API tests.
* [NCBC-3069](https://issues.couchbase.com/browse/NCBC-3069): Add project with basic tests.
* [NCBC-3001](https://issues.couchbase.com/browse/NCBC-3001): log message formatting opCode and endpoint parameters are swapped.
* [NCBC-3037](https://issues.couchbase.com/browse/NCBC-3037): Add additional unit testing to Rate Limiting code.
* [NCBC-3056](https://issues.couchbase.com/browse/NCBC-3056): Ignore null reference exception in global config resolution is server version is earlier than 6.5.
* [NCBC-2692](https://issues.couchbase.com/browse/NCBC-2692): Management APIs should provide detailed responses to errors (ban `EnsureStatusCode`).
* [NCBC-2937](https://issues.couchbase.com/browse/NCBC-2937): Support for .NET 6.0.
* [NCBC-2946](https://issues.couchbase.com/browse/NCBC-2946): Bucket Management API — Add Custom Conflict Resolution to the enumeration for Conflict Resolution Type.
* [NCBC-2947](https://issues.couchbase.com/browse/NCBC-2947): ARM — Support for Apple Silicon.
* [NCBC-2950](https://issues.couchbase.com/browse/NCBC-2950): Extend FTS options to set IncludeLocations and Operator.
* [NCBC-2956](https://issues.couchbase.com/browse/NCBC-2956): Support for AWS AWS Graviton2.
* [NCBC-2971](https://issues.couchbase.com/browse/NCBC-2971): Bucket Management API — Add Storage Option.
* [NCBC-3003](https://issues.couchbase.com/browse/NCBC-3003): InternalServerFailureException.
* [NCBC-3033](https://issues.couchbase.com/browse/NCBC-3033): Remove finalizer from OperationBase.
* [NCBC-3046](https://issues.couchbase.com/browse/NCBC-3046): Reduce tracing related heap allocations.
* [NCBC-3049](https://issues.couchbase.com/browse/NCBC-3049): Sporadic logging failures in unit tests.
* [NCBC-3053](https://issues.couchbase.com/browse/NCBC-3053): Add lambda to options in `Cluster.ConnectAsync` overload.
* [NCBC-3064](https://issues.couchbase.com/browse/NCBC-3064): Construct Activity objects using parent `ActivityContext`.
* [NCBC-3070](https://issues.couchbase.com/browse/NCBC-3070): Add API documentation to source files in Sub-Doc API.
* [NCBC-3080](https://issues.couchbase.com/browse/NCBC-3080): Use C# LangVersion 10.

### [](#version-3-2-5-10-december-2021)Version 3.2.5 (10 December 2021)

Version 3.2.5 is the fifth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.5) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.5)

> [!NOTE]
> .NET Core 2.1 support has been dropped from the SDK, as of 3.2.5\. This corresponds to Microsoft’s decision to EOL .NET Core 2.1 on August 21, 2021\.

#### [](#known-issues-10)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-42)Fixed Issues

* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): Fixed TimeoutExceptions after rebound in Failover/Eject tests.
* [NCBC-2983](https://issues.couchbase.com/browse/NCBC-2983): Allowed query timeouts to exceed 100ms.
* [NCBC-2991](https://issues.couchbase.com/browse/NCBC-2991): Fixed compatibility with DI NET 6.0 - added support for named bucket/collection DI.
* [NCBC-2993](https://issues.couchbase.com/browse/NCBC-2993): Rewrote CancellationTokenPair to dispose the linked CancellationTokenSource during GC, avoiding memory leaks.
* [NCBC-2995](https://issues.couchbase.com/browse/NCBC-2995): Fixed slow memory leak in OrphanReporter.
* [NCBC-3005](https://issues.couchbase.com/browse/NCBC-3005): Fixed GetCidByName failure with "Not connected to any bucket", by ensuring the operation is routed to KV node.
* [NCBC-3007](https://issues.couchbase.com/browse/NCBC-3007): Improved logging around connection pool scale down, for deeper inspection of DataFlowConnectionPool behavior.
* [NCBC-3009](https://issues.couchbase.com/browse/NCBC-3009): Addressed sync-over-async deadlocks.
* [NCBC-3013](https://issues.couchbase.com/browse/NCBC-3013): Keep connections alive after send is canceled. This fixes issue where canceling K/V operations while waiting on network send killed the connection.
* [NCBC-3018](https://issues.couchbase.com/browse/NCBC-3018): Fix background worker edge case where error "Comparing the same configs is not allowed" was hit.
* [NCBC-3021](https://issues.couchbase.com/browse/NCBC-3021): Fixed regression with legacy Memcached buckets.
* [NCBC-3045](https://issues.couchbase.com/browse/NCBC-3045): Fixed Fix WaitUntilReadyAsync for FTS.

#### [](#new-features-and-behavioral-changes-28)New Features and Behavioral Changes.

* [NCBC-3041](https://issues.couchbase.com/browse/NCBC-3041); [NCBC-2996](https://issues.couchbase.com/browse/NCBC-2996); [NCBC-3031](https://issues.couchbase.com/browse/NCBC-3031): Work on updating .NET targets. Removed unneeded .netstandard2.0 target from DI project. Made code changes to prepare for .NET 6\. Added .NET 5 Target.
* [NCBC-2948](https://issues.couchbase.com/browse/NCBC-2948): Added special error handling for rate and quota limits.
* [NCBC-2600](https://issues.couchbase.com/browse/NCBC-2600): Set default query HTTP Idle timeout to 4.5s, to avoid premature IOException when connecting with default values.
* [NCBC-3004](https://issues.couchbase.com/browse/NCBC-3004): Added log warning when socket disconnects from cluster
* [NCBC-3019](https://issues.couchbase.com/browse/NCBC-3019): Enabled SSL cipher configuration.
* [NCBC-3020](https://issues.couchbase.com/browse/NCBC-3020): Added support for custom deserializers for GET projections.
* [NCBC-3022](https://issues.couchbase.com/browse/NCBC-3022): Improved lock contention getting collection CIDs.
* [NCBC-3023](https://issues.couchbase.com/browse/NCBC-3023): Enabled nullable annotations to serializer/transcoder.
* [NCBC-3025](https://issues.couchbase.com/browse/NCBC-3025): Cleaned up project files and NuGet dependencies.
* [NCBC-3034](https://issues.couchbase.com/browse/NCBC-3034): Reduced blocking in async methods in data structures, resulting in more efficient thread utilization.
* [NCBC-3044](https://issues.couchbase.com/browse/NCBC-3044): Fixes to problematic OpenTelemetry tracing registration. A consumer may now register with an OpenTelemetry provider which is being managed outside the SDK.

### [](#version-3-2-4-2-november-2021)Version 3.2.4 (2 November 2021)

Version 3.2.4 is the fourth release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.4) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.4)

#### [](#known-issues-11)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests.

#### [](#fixed-issues-43)Fixed Issues

* [NCBC-2974](https://issues.couchbase.com/browse/NCBC-2974): When `GetCid` failed, an infinite loop could be triggered, causing the `CidLock` to time out. The regression that caused this in the previous release has now been fixed.
* [NCBC-2989](https://issues.couchbase.com/browse/NCBC-2989): Fixed side effects related to singleton `CouchbaseHttpClient`. Now each consuming service can safely manipulate the \`HttpClient’s timeout and connection ID headers and such without affecting other services.

#### [](#new-features-and-behavioral-changes-29)New Features and Behavioral Changes.

* [NCBC-2979](https://issues.couchbase.com/browse/NCBC-2979): Added support for Error Map v2.
* [NCBC-2987](https://issues.couchbase.com/browse/NCBC-2987): Updated NuGet package info.
* [NCBC-2477](https://issues.couchbase.com/browse/NCBC-2477): Replaced `HttpClientHandler` with `SocketsHttpHandler`.
* [NCBC-2859](https://issues.couchbase.com/browse/NCBC-2859): Completed Field Level Encryption implementation, adding RSA support for legacy upgrade scenarios.
* [NCBC-2865](https://issues.couchbase.com/browse/NCBC-2865): Added new `revEpoch` field, allowing server to provide higher level guidance for current, correct bucket configuration.
* [NCBC-2992](https://issues.couchbase.com/browse/NCBC-2992): Renamed `BucketBase.BucketConfig` to `BucketBase.CurrentConfig` for clarity. Renamed `BucketConfigExtensions.IsNewer()` to `BucketConfigExtensions.IsNewerThan()`.

### [](#version-3-2-3-6-october-2021)Version 3.2.3 (6 October 2021)

Version 3.2.3 is the third release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.3) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.3)

#### [](#known-issues-12)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests.

#### [](#fixed-issues-44)Fixed Issues

* [NCBC-2965](https://issues.couchbase.com/browse/NCBC-2965): Don’t capture ExecutionContext for long-running tasks/timers, as this could cause memory leaks.
* [NCBC-2966](https://issues.couchbase.com/browse/NCBC-2966): Allow ILoggerFactory from the DI container to be overridden.
* [NCBC-2967](https://issues.couchbase.com/browse/NCBC-2967): Rewrite OrphanReporter to avoid blocking calls.
* [NCBC-2968](https://issues.couchbase.com/browse/NCBC-2968): Use correct service type name in query context.
* [NCBC-2969](https://issues.couchbase.com/browse/NCBC-2969): Fix auto-repair of the ChannelConnectionPool after a node outage.

#### [](#new-features-and-behavioral-changes-30)New Features and Behavioral Changes.

* [NCBC-2949](https://issues.couchbase.com/browse/NCBC-2949): Improve client side error message when TLS is enforced on the server side
* [NCBC-2961](https://issues.couchbase.com/browse/NCBC-2961): Optimize performance of the internal EscapeIfRequired routine.
* [NCBC-2963](https://issues.couchbase.com/browse/NCBC-2963): Support Dependency Injection of Named Scopes/Collections.
* [NCBC-2970](https://issues.couchbase.com/browse/NCBC-2970): Optimize performance of queuing operation completion by more than 50% by using `UnsafeQueueUserWorkItem`.
* [NCBC-2962](https://issues.couchbase.com/browse/NCBC-2962): Add Lambda overloads for Query and Analytics at the Scope level.

### [](#version-3-2-2-15-september-2021)Version 3.2.2 (15 September 2021)

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.2)

This is a re-release of 3.2.1 with exactly the same commits due to a packaging bug in 3.2.1\. The only difference is the version and package fix.

#### [](#known-issues-13)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

### [](#version-3-2-1-9-september-2021-do-not-use-use-3-2-2-instead)Version 3.2.1 (9 September 2021) DO NOT USE - USE 3.2.2 INSTEAD

Version 3.2.1 is the second release of the 3.2 series.

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.1)

#### [](#known-issues-14)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests.

#### [](#new-features-and-behavioral-changes-31)New Features and Behavioral Changes.

* [NCBC-2697](https://issues.couchbase.com/browse/NCBC-2697): The Eventing Service can now be managed from the SDK. Users can create, delete, publish, pause, and select Eventing Functions.
* [NCBC-2959](https://issues.couchbase.com/browse/NCBC-2959): By default SDK3 sends the IP as the target host during TLS/SSL authentication — unlike SDK2 which sends either the hostname or IP address, depending on the returned server configuration. A new flag, `ForceIpAsTargetHost`, has been introduced to allow SDK3 to mimic SDK2 behavior.

### [](#version-3-2-0-26-july-2021)Version 3.2.0 (26 July 2021)

Version 3.2.0 is the first release of the 3.2 series, featuring collections and scopes

[Download](https://packages.couchbase.com/clients/net/3.2/Couchbase-Net-Client-3.2.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.2.0) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.2.0)

#### [](#known-issues-15)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests.

#### [](#fixed-issues-45)Fixed Issues

* [NCBC-2660](https://issues.couchbase.com/browse/NCBC-2660): After a failure that causes the circuit breaker to open, such as full send queue, new operation will immediately fail with CircuitBreakerException. The retry orchestrator now retries in this situation, preventing silent failure.
* [NCBC-2730](https://issues.couchbase.com/browse/NCBC-2730): Expose Partition Information in Query Management API.
* [NCBC-2841](https://issues.couchbase.com/browse/NCBC-2841): Construct `query_context` in Analytics queries correctly, fixing a bug with datasets that required escaping with backticks.
* [NCBC-2853](https://issues.couchbase.com/browse/NCBC-2853): After a `not_my_vbucket` exception during a rebalance, use a Fast-forward map, if available, to locate the correct vbucket.
* [NCBC-2880](https://issues.couchbase.com/browse/NCBC-2880): Analytics fix and refactor to improve testability.
* [NCBC-2890](https://issues.couchbase.com/browse/NCBC-2890): Enable and collect server duration for tracing.
* [NCBC-2891](https://issues.couchbase.com/browse/NCBC-2891): Fixes a bug where the CID for the default Scope/Collection was not passed to some 7.0beta server versions.
* [NCBC-2894](https://issues.couchbase.com/browse/NCBC-2894): Remove unsupported CAS setting from Increment/DecrementOptions
* [NCBC-2929](https://issues.couchbase.com/browse/NCBC-2929), [NCBC-2899](https://issues.couchbase.com/browse/NCBC-2899): Correct Logging Meter emit\_interval to output every 600 seconds.
* [NCBC-2903](https://issues.couchbase.com/browse/NCBC-2903): Remove reference to AggregatingMeter, which has been superseded by LoggingMeter.
* [NCBC-2900](https://issues.couchbase.com/browse/NCBC-2900), [NCBC-2902](https://issues.couchbase.com/browse/NCBC-2902), [NCBC-2904](https://issues.couchbase.com/browse/NCBC-2904): Align LoggingMeter Output Format with RFC, adding percentile values and setting JSON output to terse by default, instead of pretty.
* [NCBC-2905](https://issues.couchbase.com/browse/NCBC-2905), [NCBC-2906](https://issues.couchbase.com/browse/NCBC-2906), [NCBC-2907](https://issues.couchbase.com/browse/NCBC-2907), [NCBC-2908](https://issues.couchbase.com/browse/NCBC-2908): Align ThresholdLoggingTracer Output with RFC, and enable by default. Now correctly omits null fields in JSON output, includes timeout.
* [NCBC-2916](https://issues.couchbase.com/browse/NCBC-2916): Add "operation" property to allow LoggingMeterReport output to be split by opcode.
* [NCBC-2928](https://issues.couchbase.com/browse/NCBC-2928): Align Threshold Logger output with KV Tracer Output spec.
* [NCBC-2921](https://issues.couchbase.com/browse/NCBC-2921): Fix a bug where the quota.rawRAM size may over/under flow the Int32 size of the BucketSettings.RamQuotaMB field when the JSON is parsed.
* [NCBC-2924](https://issues.couchbase.com/browse/NCBC-2924): Fix a bug where Date Time Offsets were always coverted to local time zone, by passing DateParseHandling from SerializerSettings to the DefaultStreamingJsonReader.
* [NCBC-2927](https://issues.couchbase.com/browse/NCBC-2927): Requests and responses will be handled in an Out-of-Order manner by default.
* [NCBC-2930](https://issues.couchbase.com/browse/NCBC-2930): Update Collection and Scope error parsing
* [NCBC-2931](https://issues.couchbase.com/browse/NCBC-2931): Fixes a bug where when the Collection id changes, those changes were not picked up causing an operation timeout.
* [NCBC-2933](https://issues.couchbase.com/browse/NCBC-2933), [NCBC-2934](https://issues.couchbase.com/browse/NCBC-2934): Unit Test improvements and fixes to Jenkins Pipeline.

#### [](#new-features-and-behavioral-changes-32)New Features and Behavioral Changes.

* [NCBC-2869](https://issues.couchbase.com/browse/NCBC-2869): Provide OpenTelemetry tracing module, allowing export via any of the OpenTelemetry exporters such as ZipKin, Jaeger, etc.
* [NCBC-2893](https://issues.couchbase.com/browse/NCBC-2893): Allow a parent span to added to the options for each service or operation for tracing.
* [NCBC-2856](https://issues.couchbase.com/browse/NCBC-2856), [NCBC-2923](https://issues.couchbase.com/browse/NCBC-2923): Add Orphaned Response Logging to SDK.
* [NCBC-2911](https://issues.couchbase.com/browse/NCBC-2911): Travel Sample App added, with examples of Collections and Scopes across Query, KV, and Search.
* [NCBC-2926](https://issues.couchbase.com/browse/NCBC-2926): Add license to footer of all files in Couchbase project
* [NCBC-2574](https://issues.couchbase.com/browse/NCBC-2574), [NCBC-2575](https://issues.couchbase.com/browse/NCBC-2575): Analytics management: manage Remote Links, support compound dataverse names.
* [NCBC-2581](https://issues.couchbase.com/browse/NCBC-2581), [NCBC-2800](https://issues.couchbase.com/browse/NCBC-2800): Provide tracing for the .NET SDK based upon RFC 67 Extended SDK Observability. Implements Threshold Logger, LoggingMeter for latency metrics.
* [NCBC-2585](https://issues.couchbase.com/browse/NCBC-2585), [NCBC-2717](https://issues.couchbase.com/browse/NCBC-2717): Add build Support for .NET 5.0 and Ubuntu 20.04 LTS
* [NCBC-2892](https://issues.couchbase.com/browse/NCBC-2892), [NCBC-2886](https://issues.couchbase.com/browse/NCBC-2886), [NCBC-2889](https://issues.couchbase.com/browse/NCBC-2889): Update and correct links for 3.2.0 release.
* [NCBC-2699](https://issues.couchbase.com/browse/NCBC-2699), [NCBC-2777](https://issues.couchbase.com/browse/NCBC-2777): Provide a framework for client-side encryption of sensitive fields in JSON documents using Field Level Encryption.
* [NCBC-2790](https://issues.couchbase.com/browse/NCBC-2790): Replace, Upsert and MutateIn support `PersistTtl` in servers >= 7.0 which keeps subsequent calls from modifying the original TTL value on update.
* [NCBC-2807](https://issues.couchbase.com/browse/NCBC-2807): Deprecate Collection Manager `GetScope()` in favour of `GetAllScopes()`
* [NCBC-2846](https://issues.couchbase.com/browse/NCBC-2846): Distinguish between CAS mismatch and DML failure on query error.
* [NCBC-2912](https://issues.couchbase.com/browse/NCBC-2912), [NCBC-2917](https://issues.couchbase.com/browse/NCBC-2917): Ensure that a server response 13014 is also recognized as an authentication failure by the query parser.
* [NCBC-2932](https://issues.couchbase.com/browse/NCBC-2932): Add Cause field on Query.Error for Transactions Query support.

## [](#net-sdk-3-1-releases).NET SDK 3.1 Releases

### [](#version-3-1-7-02-june-2021)Version 3.1.7 (02 June 2021)

Version 3.1.7 is the eighth release of the 3.1 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.1/Couchbase-Net-Client-3.1.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.7) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.7)

#### [](#known-issues-16)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests.
* [NCBC-2891](https://issues.couchbase.com/browse/NCBC-2891): Send 0x0 for default scope/collections for certain Server 7.0 beta versions.

#### [](#fixed-issues-46)Fixed Issues

* [NCBC-2879](https://issues.couchbase.com/browse/NCBC-2879): Combi test failure fixed by only running tests with `CollectionTests.CollectionIdChanged_RetriesAuto` on servers which support collections and the newer management URI structure.
* [NCBC-2888](https://issues.couchbase.com/browse/NCBC-2888): Converting null literal or possible null value to non-nullable type — a rare compile time error for certain environments fixed by using `var` instead of `TValue`.

#### [](#new-features-and-behavioral-changes-33)New Features and Behavioral Changes.

* [NCBC-2698](https://issues.couchbase.com/browse/NCBC-2698): Added FTS Support for Collections.
* [NCBC-2881](https://issues.couchbase.com/browse/NCBC-2881): Use Hello to determine if collections are available now no longer leaves exception in DEBUG level log.
* [NCBC-2887](https://issues.couchbase.com/browse/NCBC-2887): Previously the CID value of 0 could be appended to the key if the default scope/collection was being used. Now, this is checked for, and we don’t send the CID with the key in this case, as it is not required by the server.

### [](#version-3-1-6-24-may-2021)Version 3.1.6 (24 May 2021)

Version 3.1.6 is the seveneth release of the 3.1 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.1/Couchbase-Net-Client-3.1.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.6) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.6)

#### [](#known-issues-17)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests.

#### [](#fixed-issues-47)Fixed Issues

* [NCBC-2881](https://issues.couchbase.com/browse/NCBC-2881): The SDK now uses Hello to determine if collections are available, giving improved accuracy over the heuristic method.
* [NCBC-2877](https://issues.couchbase.com/browse/NCBC-2877): Collection GIT\_CID Eaccess error fix.

### [](#version-3-1-5-13-may-2021)Version 3.1.5 (13 May 2021)

Version 3.1.5 is the sixth release of the 3.1 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.1/Couchbase-Net-Client-3.1.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.5) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.5)

#### [](#known-issues-18)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests

#### [](#fixed-issues-48)Fixed Issues

* [NCBC-2551](https://issues.couchbase.com/browse/NCBC-2551): GetAllBucketsAsync always throws ArgumentNullException
* [NCBC-2860](https://issues.couchbase.com/browse/NCBC-2860): Configuration revisions should be parsed and compared with 64-bit precision.
* [NCBC-2864](https://issues.couchbase.com/browse/NCBC-2864): Unknown default collection regression
* [NCBC-2867](https://issues.couchbase.com/browse/NCBC-2867): ConfigHandler dead locks in K8 when delete pod is used
* [NCBC-2871](https://issues.couchbase.com/browse/NCBC-2871): NRE in BucketManager and UserManager part 2
* [NCBC-2876](https://issues.couchbase.com/browse/NCBC-2876): Upserting to <7.0 clusters does not upsert the content

#### [](#new-features-and-behavioral-changes-34)New Features and Behavioral Changes.

* [NCBC-2862](https://issues.couchbase.com/browse/NCBC-2862): Log message on timeout appears to lack instance
* [NCBC-2866](https://issues.couchbase.com/browse/NCBC-2866): Exception: Non-default Scopes and Collections not supported on this server version.
* [NCBC-2839](https://issues.couchbase.com/browse/NCBC-2839): SDK API changes due to protocol level changes to get\_collection\_id
* [NCBC-2858](https://issues.couchbase.com/browse/NCBC-2858): Move collection id fetch into the operation call on the collection

### [](#version-3-1-4-8-april-2021)Version 3.1.4 (8 April 2021)

Version 3.1.4 is the fifth release of the 3.1 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.1/Couchbase-Net-Client-3.1.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.4) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.4)

#### [](#known-issues-19)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2851](https://issues.couchbase.com/browse/NCBC-2851): TimeoutExceptions continue after rebound in Failover/Eject tests

#### [](#fixed-issues-49)Fixed Issues

* [NCBC-2720](https://issues.couchbase.com/browse/NCBC-2720): Change QueryMetrics Property from ElaspedTime to ElapsedTime
* [NCBC-2831](https://issues.couchbase.com/browse/NCBC-2831): MutateIn is not throwing and classifying sub-doc errors correctly.

#### [](#new-features-and-behavioral-changes-35)New Features and Behavioral Changes.

* [NCBC-2828](https://issues.couchbase.com/browse/NCBC-2828): Cleanup sub-doc operation public API surface
* [NCBC-2842](https://issues.couchbase.com/browse/NCBC-2842): Add Couchbase.Core.Exceptions.TimeoutException
* [NCBC-2843](https://issues.couchbase.com/browse/NCBC-2843): K/V CancellationToken expiration does not include IErrorContext
* [NCBC-2844](https://issues.couchbase.com/browse/NCBC-2844): Make Query.ReadOnly obsolete and replace w/QueryOptions.Readonly
* [NCBC-2845](https://issues.couchbase.com/browse/NCBC-2845): Allow default IRetryStrategy to be overridden

### [](#version-3-1-3-3-march-2021)Version 3.1.3 (3 March 2021)

Version 3.1.3 is the fourth release of the 3.1 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.1/Couchbase-Net-Client-3.1.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.3) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.3)

#### [](#known-issues-20)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-50)Fixed Issues

* [NCBC-2801](https://issues.couchbase.com/browse/NCBC-2801): `NodeAdapter` incorrectly shows N1QL service is not available.
* [NCBC-2817](https://issues.couchbase.com/browse/NCBC-2817): `LookupInAsync` and `MutateInAsync` builder extensions should accept null options.
* [NCBC-2823](https://issues.couchbase.com/browse/NCBC-2823): Make `ClusterOptions.NetworkResolution` read/write.
* [NCBC-2826](https://issues.couchbase.com/browse/NCBC-2826): Collection Id outdated exception on K-V ops.
* [NCBC-2827](https://issues.couchbase.com/browse/NCBC-2827): `GET_CID` and `GET_SID` do not correctly retry if Scope/Collection not found.
* [NCBC-2811](https://issues.couchbase.com/browse/NCBC-2811): Cache default scope/collection allocation.
* [NCBC-2812](https://issues.couchbase.com/browse/NCBC-2812): Throw `UnsupportedException` if non-default scopes/cols are used in pre-7.0 clusters.

#### [](#new-features-and-behavioral-changes-36)New Features and Behavioral Changes

* [NCBC-2813](https://issues.couchbase.com/browse/NCBC-2813): Cleanup `IOperation` and `OperationBase` code.
* [NCBC-2815](https://issues.couchbase.com/browse/NCBC-2815): Replace `AsyncMutex` with `SemaphoreSlim`.
* [NCBC-2818](https://issues.couchbase.com/browse/NCBC-2818): Queue operation completions on the global queue.
* [NCBC-2819](https://issues.couchbase.com/browse/NCBC-2819): Enable `NetworkResolution` via the connection string.
* [NCBC-2833](https://issues.couchbase.com/browse/NCBC-2833): Remove Type parameter from `UnlockAsync`.

### [](#version-3-1-2-4-february-2021)Version 3.1.2 (4 February 2021)

Version 3.1.2 is the third release of the 3.1 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.1/Couchbase-Net-Client-3.1.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.2)

#### [](#known-issues-21)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-51)Fixed Issues

* [NCBC-2763](https://issues.couchbase.com/browse/NCBC-2763): MutationToken throwing ArgumentNullException on static initialization.
* [NCBC-2766](https://issues.couchbase.com/browse/NCBC-2766): CreateScopeAsync not creating collections in ScopeSpec.
* [NCBC-2767](https://issues.couchbase.com/browse/NCBC-2767): ScopeNotFoundException when trying to get Scope after creating it.
* [NCBC-2784](https://issues.couchbase.com/browse/NCBC-2784): Getting a collection right after creating it throws CollectionNotFoundException.
* [NCBC-2794](https://issues.couchbase.com/browse/NCBC-2794): PackageIconUrl is still being used and blocks package creation.
* [NCBC-2797](https://issues.couchbase.com/browse/NCBC-2797): Hot upgrade failure from 6.6.0 to 6.6.1 using SDK v3.1.2.
* [NCBC-2798](https://issues.couchbase.com/browse/NCBC-2798): ThrowIfBootstrapFailed called twice in GetAsync.
* [NCBC-2804](https://issues.couchbase.com/browse/NCBC-2804): Non-JSON transcoders cannot be mixed with requests for document expiry.
* [NCBC-2810](https://issues.couchbase.com/browse/NCBC-2810): On pre-7.0 clusters default scopes/collections may not load.

#### [](#new-features-and-behavioral-changes-37)New Features and Behavioral Changes

* [NCBC-2791](https://issues.couchbase.com/browse/NCBC-2791): GetResult uses AddMilliseconds instead of AddSeconds for expiry.
* [NCBC-2796](https://issues.couchbase.com/browse/NCBC-2796): SUBDOC\_MULTI\_PATH\_FAILURE\_DELETED throwing PathInvalid.
* [NCBC-2770](https://issues.couchbase.com/browse/NCBC-2770): Add experimental connection pool based on System.Threading.Channels.
* [NCBC-2772](https://issues.couchbase.com/browse/NCBC-2772): Cleanup key/value cancellation token and timeout handling.
* [NCBC-2776](https://issues.couchbase.com/browse/NCBC-2776): Change SlicedMemoryOwner to a structure.
* [NCBC-2789](https://issues.couchbase.com/browse/NCBC-2789): Unable to override the remote name mismatch error with custom validation.
* [NCBC-2793](https://issues.couchbase.com/browse/NCBC-2793): Address misc compiler warnings.
* [NCBC-2802](https://issues.couchbase.com/browse/NCBC-2802): Port sub-doc lambda extensions from SDK 2.x.
* [NCBC-2805](https://issues.couchbase.com/browse/NCBC-2805): Optimize in-flight operation cleanup method.
* [NCBC-2808](https://issues.couchbase.com/browse/NCBC-2808): Use ValueTask and IValueTaskSource for OperationBase.Completed.
* [NCBC-2809](https://issues.couchbase.com/browse/NCBC-2809): Use ValueTask for new ScopeAsync/CollectionAsync methods.

### [](#version-3-1-1-13-january-2021)Version 3.1.1 (13 January 2021)

Version 3.1.1 is the second release of the 3.1 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.1/Couchbase-Net-Client-3.1.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.1)

#### [](#known-issues-22)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-52)Fixed Issues

* [NCBC-2565](https://issues.couchbase.com/browse/NCBC-2565): WaitUntilReady failure for 6.5.
* [NCBC-2660](https://issues.couchbase.com/browse/NCBC-2660), [NCBC-2935](https://issues.couchbase.com/browse/NCBC-2935): Operations are now retried if they hit an open circuit breaker.
* [NCBC-2693](https://issues.couchbase.com/browse/NCBC-2693): MutationToken.GetHashCode() implementation looks suspect.
* [NCBC-2694](https://issues.couchbase.com/browse/NCBC-2694): Removed unnecessary linked CancellationToken.
* [NCBC-2726](https://issues.couchbase.com/browse/NCBC-2726): Cannot read empty response bodies.
* [NCBC-2741](https://issues.couchbase.com/browse/NCBC-2741): If the send queue is full when requeuing after connection cleanup, the operation is dropped.
* [NCBC-2746](https://issues.couchbase.com/browse/NCBC-2746): using mutate in to update an existing value to null causes an IllegalArgumentException.
* [NCBC-2751](https://issues.couchbase.com/browse/NCBC-2751): Use ConfigureAwait(false) on awaited task in DnsClientDnsResolver.
* [NCBC-2756](https://issues.couchbase.com/browse/NCBC-2756): Do not allow empty hosts in ConnectionString.
* [NCBC-2760](https://issues.couchbase.com/browse/NCBC-2760): MultiMutation duplicates specs on Retry, causing SUBDOC\_INVALID\_COMBO.
* [NCBC-2761](https://issues.couchbase.com/browse/NCBC-2761): MutateIn is not setting Cas, ignoring MutateInOptions.CasValue, resulting in a default of 0 which always overwrites.
* [NCBC-2762](https://issues.couchbase.com/browse/NCBC-2762): Threshold trace logging leaks memory.
* [NCBC-2764](https://issues.couchbase.com/browse/NCBC-2764): Expiration of TimeSpan.Zero is being sent to server as 1 second expiration.
* [NCBC-2778](https://issues.couchbase.com/browse/NCBC-2778): Throw CasMismatchException when CAS mismatch occurs.
* [NCBC-2780](https://issues.couchbase.com/browse/NCBC-2780): Fix unit tests relying on obsolete Expiry method.
* [NCBC-2781](https://issues.couchbase.com/browse/NCBC-2781): Make replica commands use CancellationToken.
* [NCBC-2782](https://issues.couchbase.com/browse/NCBC-2782): Replica methods randomly completed with NotMyVBucket.

#### [](#new-features-and-behavioral-changes-38)New Features and Behavioral Changes.

* [NCBC-2716](https://issues.couchbase.com/browse/NCBC-2716): Collections Analytics Test Changes.
* [NCBC-2747](https://issues.couchbase.com/browse/NCBC-2747): Add KvSendQueueCapacity to ClusterOptions for tuning.
* [NCBC-2748](https://issues.couchbase.com/browse/NCBC-2748): netcore3.0 target id deprecated and cannot be used with `dotnet pack`.
* [NCBC-2785](https://issues.couchbase.com/browse/NCBC-2785): ArgumentOutOfRangeException if GetResult.Expiry called on GET operation.
* [NCBC-2788](https://issues.couchbase.com/browse/NCBC-2788): `UserManagerTests.Test_UserInheritsCollectionAwareRoles` fails in combi tests.
* [NCBC-2653](https://issues.couchbase.com/browse/NCBC-2653): Unnecessary allocation in classes implementing IOperation.
* [NCBC-2661](https://issues.couchbase.com/browse/NCBC-2661): CouchbaseBucket is doing ad hoc retrying if CollectionOutdatedException.
* [NCBC-2677](https://issues.couchbase.com/browse/NCBC-2677): Docs: Threshold Logging and Orphan Response Logging.
* [NCBC-2722](https://issues.couchbase.com/browse/NCBC-2722): Improve performance of `WriteKey` using `stackalloc`.
* [NCBC-2723](https://issues.couchbase.com/browse/NCBC-2723): Reduce async/await around circuit breakers on K/V ops.
* [NCBC-2724](https://issues.couchbase.com/browse/NCBC-2724): Reduce task continuations related to K/V timeouts.
* [NCBC-2725](https://issues.couchbase.com/browse/NCBC-2725): Improve logic around ITypeTranscoder instantiations.
* [NCBC-2727](https://issues.couchbase.com/browse/NCBC-2727): Improve log redaction performance.
* [NCBC-2728](https://issues.couchbase.com/browse/NCBC-2728): Improve LEB128 encoding performance.
* [NCBC-2729](https://issues.couchbase.com/browse/NCBC-2729): Reduce task continuations on k/v GET operations.
* [NCBC-2731](https://issues.couchbase.com/browse/NCBC-2731): Reduce JSON serialization heap allocations.
* [NCBC-2732](https://issues.couchbase.com/browse/NCBC-2732): ConfigHandler processing is blocking a thread from the thread pool.
* [NCBC-2733](https://issues.couchbase.com/browse/NCBC-2733): Improve efficiency of ErrorCode lookup in ErrorMap.
* [NCBC-2734](https://issues.couchbase.com/browse/NCBC-2734): Improve CancellationTokenSource handling in RetryOrchestrator.
* [NCBC-2735](https://issues.couchbase.com/browse/NCBC-2735): Optimize OperationBuilder performance.
* [NCBC-2736](https://issues.couchbase.com/browse/NCBC-2736): Optimize key/value operation flag handling.
* [NCBC-2737](https://issues.couchbase.com/browse/NCBC-2737): Use a static client description for spans.
* [NCBC-2738](https://issues.couchbase.com/browse/NCBC-2738): Improve performance building connection tags for K/V operation spans.
* [NCBC-2740](https://issues.couchbase.com/browse/NCBC-2740): Optimize performance when request tracing is disabled.
* [NCBC-2742](https://issues.couchbase.com/browse/NCBC-2742): Reduce debug logging heap allocations on critical K/V path.
* [NCBC-2743](https://issues.couchbase.com/browse/NCBC-2743): Reduce Task ContingentProperties heap allocations.
* [NCBC-2744](https://issues.couchbase.com/browse/NCBC-2744): Enable reporting of test results in Jenkins.
* [NCBC-2745](https://issues.couchbase.com/browse/NCBC-2745): Reduce lambda-related heap allocations for K/V operation completions.
* [NCBC-2749](https://issues.couchbase.com/browse/NCBC-2749): Use Stopwatch to track connection idle time.
* [NCBC-2750](https://issues.couchbase.com/browse/NCBC-2750): Use spans in MultiplexingConnection.ParseReceivedData.
* [NCBC-2752](https://issues.couchbase.com/browse/NCBC-2752): Improve ToTtl performance.
* [NCBC-2753](https://issues.couchbase.com/browse/NCBC-2753): Allow BucketBase.RetryAsync to be inlined.
* [NCBC-2754](https://issues.couchbase.com/browse/NCBC-2754): Use Span<byte> for VBucketKeyMapper.GetIndex
* [NCBC-2755](https://issues.couchbase.com/browse/NCBC-2755): Use ThrowHelper to improve inlining.
* [NCBC-2757](https://issues.couchbase.com/browse/NCBC-2757): SkipLocalsInit when writing document keys to operations.
* [NCBC-2758](https://issues.couchbase.com/browse/NCBC-2758): Use .NET provided encoding of strings to spans when available.
* [NCBC-2765](https://issues.couchbase.com/browse/NCBC-2765): Improve buffer handling in MultiplexingConnection receive.
* [NCBC-2768](https://issues.couchbase.com/browse/NCBC-2768): Improve precision of UnixMillisecondsConverter.
* [NCBC-2769](https://issues.couchbase.com/browse/NCBC-2769): Avoid heap allocations for default K/V operations.
* [NCBC-2773](https://issues.couchbase.com/browse/NCBC-2773): Simplify AsyncState handling of Opaque.
* [NCBC-2774](https://issues.couchbase.com/browse/NCBC-2774): Make OperationBuilderPool tunable.
* [NCBC-2775](https://issues.couchbase.com/browse/NCBC-2775): Improve array handling performance throughout the SDK.

### [](#version-3-1-0-2-december-2020)Version 3.1.0 (2 December 2020)

This is the first GA release of the 3.1 series, bringing enhancements and bugfixes over the 3.0 releases, and adding features to support Couchbase Server 6.6.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.1.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.1.0) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.1.0)

#### [](#known-issues-23)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-53)Fixed Issues

* [NCBC-2643](https://issues.couchbase.com/browse/NCBC-2643): `DataFlowConnectionPool` was creating unbounded connections in certain situations, such as pinging for a buckets which had not yet been created. This fix resolves the issue, although the number of connections will go up still but then trend back down, as they are in a `TIME_WAIT` state and it takes a little time for them to be reclaimed.
* [NCBC-2660](https://issues.couchbase.com/browse/NCBC-2660): Operations were not retried if they hit an open circuit breaker (`CircuitBreakerException`); the retry orchestrator will now retry these failures.
* [NCBC-2686](https://issues.couchbase.com/browse/NCBC-2686): Facet result missing fields added to Search.
* [NCBC-2705](https://issues.couchbase.com/browse/NCBC-2705): `RawBinaryTranscoder` was using invalid DataFormat. It will now simply pass the body of the packet back to the consumer as it should.
* [NCBC-2706](https://issues.couchbase.com/browse/NCBC-2706): A JSON string stored in Couchbase was generating an error when read as a string via `result.ContentAs<string>()`. The packet is now converted into a UTF8 string if the type of T is a string in `JsonTranscoder`, so if you write a POCO to Couchbase reading it as a string now works as expected.
* [NCBC-2708](https://issues.couchbase.com/browse/NCBC-2708): Sub-Document API Transcoder `InvalidOperationExceptions` are no longer thrown when a DataFormat mismatch occurs.

#### [](#new-features-and-behavioral-changes-39)New Features and Behavioral Changes.

* [NCBC-2386](https://issues.couchbase.com/browse/NCBC-2386): Non-JSON & transcoders code samples added to developer documentation.
* [NCBC-2418](https://issues.couchbase.com/browse/NCBC-2418): `maxTTL` can now be set via the `CollectionSpec.MaxExpiry` property.
* [NCBC-2572](https://issues.couchbase.com/browse/NCBC-2572): Durability can now be set on the bucket, for Couchbase Server 6.6 and up.
* [NCBC-2589](https://issues.couchbase.com/browse/NCBC-2589): Document Expiry Duration works as expected with offsets and with absolute time stamps.
* [NCBC-2622](https://issues.couchbase.com/browse/NCBC-2622): GetResult.expiry() is deprecated. Please use `GetResult.ExpiryTime` over `Expiry` as it accurately depicts the `TTL` of the document.
* [NCBC-2627](https://issues.couchbase.com/browse/NCBC-2627), [NCBC-2631](https://issues.couchbase.com/browse/NCBC-2631): FTS _Score_ parameter added to allow avoidance of scoring from Server 6.6.
* [NCBC-2679](https://issues.couchbase.com/browse/NCBC-2679): A better opcode is used for basic Get scenarios, which will allow the server to return compressed documents once compression support is added to the .NET SDK.
* [NCBC-2709](https://issues.couchbase.com/browse/NCBC-2709): A minor optimization in all key-value operations following improved performance of bootstrap test.
* [NCBC-2715](https://issues.couchbase.com/browse/NCBC-2715): Added `InterfaceStabilityAttribute` for API interface stability.

## [](#net-sdk-3-0-releases).NET SDK 3.0 Releases

### [](#version-3-0-7-3-november-2020)Version 3.0.7 (3 November 2020)

Version 3.0.7 is the eighth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.7.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.7) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.7)

#### [](#known-issues-24)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-54)Fixed Issues

* [NCBC-2641](https://issues.couchbase.com/browse/NCBC-2641): ConfigHandler has already been started.
* [NCBC-2651](https://issues.couchbase.com/browse/NCBC-2651): IncrementOptions and DecrementOptions are missing Expiry.
* [NCBC-2655](https://issues.couchbase.com/browse/NCBC-2655): Bucket WaitUntilReadyAsync running into NullReferenceException.
* [NCBC-2656](https://issues.couchbase.com/browse/NCBC-2656): Serialization/Transcoding Errors Are Unhandled.
* [NCBC-2660](https://issues.couchbase.com/browse/NCBC-2660): Operations are not retried if they hit an open circuit breaker.
* [NCBC-2669](https://issues.couchbase.com/browse/NCBC-2669): Upsert/Insert null with MutateIn fails with Invalid arguments (0x0004).
* [NCBC-2685](https://issues.couchbase.com/browse/NCBC-2685): AccessDeleted not supported properly on MutateIn.

#### [](#new-features-and-behavioral-changes-40)New Features and Behavioral Changes.

* [NCBC-2670](https://issues.couchbase.com/browse/NCBC-2670): Collections - RBAC Collections - .net tests
* [NCBC-2569](https://issues.couchbase.com/browse/NCBC-2569): .NET Logging page
* [NCBC-2580](https://issues.couchbase.com/browse/NCBC-2580): Add Ephemeral Bucket Management Support
* [NCBC-2664](https://issues.couchbase.com/browse/NCBC-2664): Operations are silently ignored if the send queue is full
* [NCBC-2668](https://issues.couchbase.com/browse/NCBC-2668): Add RawBinaryTranscoder
* [NCBC-2675](https://issues.couchbase.com/browse/NCBC-2675): Optimize VBucketKeyMapper.GetIndex
* [NCBC-2680](https://issues.couchbase.com/browse/NCBC-2680): Share ServerFeatures on IConnection
* [NCBC-2688](https://issues.couchbase.com/browse/NCBC-2688): Make synchronous Analytics query methods obsolete

### [](#version-3-0-6-13-october-2020)Version 3.0.6 (13 October 2020)

Version 3.0.6 is the seventh release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.6.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.6) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.6)

#### [](#known-issues-25)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-55)Fixed Issues

* [NCBC-2187](https://issues.couchbase.com/browse/NCBC-2187): CollectionManager - 400: Not allowed on this version of cluster (verify).
* [NCBC-2604](https://issues.couchbase.com/browse/NCBC-2604): exception.IsRetryable() in docs.
* [NCBC-2619](https://issues.couchbase.com/browse/NCBC-2619): Update KV samples.
* [NCBC-2638](https://issues.couchbase.com/browse/NCBC-2638): Intermittent InvalidOperationException in Dependency Injection.
* [NCBC-2639](https://issues.couchbase.com/browse/NCBC-2639): Upsert-and-remove doesn’t work.
* [NCBC-2652](https://issues.couchbase.com/browse/NCBC-2652): Operations gets stuck in retry loop until timeout.
* [NCBC-2657](https://issues.couchbase.com/browse/NCBC-2657): Exceptions Aren’t Thrown For N1QL Errors After Results.
* [NCBC-2659](https://issues.couchbase.com/browse/NCBC-2659): Fix strong naming for Couchbase.Extensions.DependencyInjection.
* [NCBC-2662](https://issues.couchbase.com/browse/NCBC-2662): Correct DI security for named buckets on .NET Core.
* [NCBC-2671](https://issues.couchbase.com/browse/NCBC-2671): KV Throughput drop after failover-rebalance

#### [](#new-features-and-behavioral-changes-41)New Features and Behavioral Changes.

* [NCBC-2033](https://issues.couchbase.com/browse/NCBC-2033): 3.0 API Query snippets in concept doc.
* [NCBC-2321](https://issues.couchbase.com/browse/NCBC-2321): Update documents to SDK 3.0 Beta interface.
* [NCBC-2472](https://issues.couchbase.com/browse/NCBC-2472): Ensure connection string supports options table defined in RFC.
* [NCBC-2298](https://issues.couchbase.com/browse/NCBC-2298): CancellationToken and CancellationTokenSource management needed.
* [NCBC-2557](https://issues.couchbase.com/browse/NCBC-2557): Improve cancellation and timeouts.
* [NCBC-2573](https://issues.couchbase.com/browse/NCBC-2573): Add support for CreateAsDeleted.
* [NCBC-2576](https://issues.couchbase.com/browse/NCBC-2576): Geopolygon search support.
* [NCBC-2577](https://issues.couchbase.com/browse/NCBC-2577): Add Options To Use FTS Hints (Flex Index).

### [](#version-3-0-5-1-september-2020)Version 3.0.5 (1 September 2020)

Version 3.0.5 is the sixth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.5.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.5) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.5)

#### [](#known-issues-26)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.

#### [](#fixed-issues-56)Fixed Issues

* [NCBC-2504](https://issues.couchbase.com/browse/NCBC-2504): Intermittent ViewQuery failures after rebound Rb2OutEpt-HYBRID
* [NCBC-2559](https://issues.couchbase.com/browse/NCBC-2559): Test\_BootStrap\_Error\_Propagates\_To\_View\_Operations fails w/BucketNotFoundException
* [NCBC-2561](https://issues.couchbase.com/browse/NCBC-2561): CreateAndDropIndex and Test\_QueryManager conflict
* [NCBC-2625](https://issues.couchbase.com/browse/NCBC-2625): Ensure new NodeAdapter is assigned to ClusterNode on change
* [NCBC-2634](https://issues.couchbase.com/browse/NCBC-2634): Expiry returned with entire document when ContentAs invoked
* [NCBC-2405](https://issues.couchbase.com/browse/NCBC-2405): SDK3 DOC on User Auth options
* [NCBC-2541](https://issues.couchbase.com/browse/NCBC-2541): WaitUntilReady() doc code sample
* [NCBC-2603](https://issues.couchbase.com/browse/NCBC-2603): Missing snippets & sections in Managing Connections doc
* [NCBC-2623](https://issues.couchbase.com/browse/NCBC-2623): Implement Threshold Logging features of RTO
* [NCBC-2636](https://issues.couchbase.com/browse/NCBC-2636): Test max limitations of collections and scopes
* [NCBC-2637](https://issues.couchbase.com/browse/NCBC-2637): Split Couchbase.IntegrationTests into seperate projects for Management and main API
* [NCBC-2427](https://issues.couchbase.com/browse/NCBC-2427): Verify that out-of-order K/V request/responses are supported
* [NCBC-2584](https://issues.couchbase.com/browse/NCBC-2584): Add N1QL Support for Collections
* [NCBC-2630](https://issues.couchbase.com/browse/NCBC-2630): Enhance User Management for Collections/RBAC

### [](#version-3-0-4-5-august-2020)Version 3.0.4 (5 August 2020)

Version 3.0.4 is the fifth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.4.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.4) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.4)

#### [](#known-issues-27)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2187](https://issues.couchbase.com/browse/NCBC-2187): CollectionManager — 400: Not allowed on this version of cluster.

#### [](#fixed-issues-57)Fixed Issues

* [NCBC-2605](https://issues.couchbase.com/browse/NCBC-2605): Expiration less than 1000ms creates a doc with an infinite lifespan
* [NCBC-2608](https://issues.couchbase.com/browse/NCBC-2608): Connection fails if first node in connection string array is unavailable.
* [NCBC-2620](https://issues.couchbase.com/browse/NCBC-2620): Expiry not being set by MutateIn
* [NCBC-2621](https://issues.couchbase.com/browse/NCBC-2621): Ensure the CName field is set per operation
* [NCBC-2601](https://issues.couchbase.com/browse/NCBC-2601): SUBDOC\_XATTR\_INVALID\_FLAG\_COMBO when mixing MutationMacro and XAttr

#### [](#new-features-and-behavioral-changes-42)New Features and Behavioral Changes.

* [NCBC-2441](https://issues.couchbase.com/browse/NCBC-2441): Implement tracing using OpenTelemetry for FTS
* [NCBC-2442](https://issues.couchbase.com/browse/NCBC-2442): Implement tracing using OpenTelemetry for KV
* [NCBC-2443](https://issues.couchbase.com/browse/NCBC-2443): Implement tracing using OpenTelemetry for Analytics
* [NCBC-2444](https://issues.couchbase.com/browse/NCBC-2444): Implement tracing using OpenTelemetry for Views
* [NCBC-2579](https://issues.couchbase.com/browse/NCBC-2579): Implement tracing of spans for all services towards Response Time Observability for SDK 3.0
* [NCBC-2583](https://issues.couchbase.com/browse/NCBC-2583): Add support for looking up certificates via Cert Store
* [NCBC-2602](https://issues.couchbase.com/browse/NCBC-2602): Add Support for MutateIn.SetDocument
* [NCBC-2609](https://issues.couchbase.com/browse/NCBC-2609): Add PublicKey to AssemblyInfo for DI when building release packages
* [NCBC-2617](https://issues.couchbase.com/browse/NCBC-2617): When signing make friend assemblies use public key

### [](#version-3-0-3-14-july-2020)Version 3.0.3 (14 July 2020)

Version 3.0.3 is the fourth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.3.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.3) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.3)

#### [](#known-issues-28)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2187](https://issues.couchbase.com/browse/NCBC-2187): CollectionManager — 400: Not allowed on this version of cluster.

#### [](#fixed-issues-58)Fixed Issues

* [NCBC-2588](https://issues.couchbase.com/browse/NCBC-2588): LookupIn should re-order subdoc requests so that XATTRs come first.
* [NCBC-2450](https://issues.couchbase.com/browse/NCBC-2450): KV failure after removing entry point node for pre-MH server
* [NCBC-2501](https://issues.couchbase.com/browse/NCBC-2501): latency detected in FoEptRb-SubDoc after rebound never recovers
* [NCBC-2502](https://issues.couchbase.com/browse/NCBC-2502): latency detected in FoEptEject-SUBDOC after rebound never recovers
* [NCBC-2503](https://issues.couchbase.com/browse/NCBC-2503): Latency detected for FoRbAnalytics-CBAS after rebound never recovers
* [NCBC-2545](https://issues.couchbase.com/browse/NCBC-2545): Hello World example in the docs repo doesn't build.
* [NCBC-2553](https://issues.couchbase.com/browse/NCBC-2553): Remove authzid from Sasl Negotiation
* [NCBC-2563](https://issues.couchbase.com/browse/NCBC-2563): StreamingQueryResult fails to populate errors on InternalServerError
* [NCBC-2587](https://issues.couchbase.com/browse/NCBC-2587): LookupInSpecBuilder allows only a single XATTR per request.
* [NCBC-2592](https://issues.couchbase.com/browse/NCBC-2592): Fix custom circuit breaker not being injected
* [NCBC-1836](https://issues.couchbase.com/browse/NCBC-1836): CAS samples

#### [](#new-features-and-behavioral-changes-43)New Features and Behavioral Changes.

* [NCBC-2542](https://issues.couchbase.com/browse/NCBC-2542): OpenTelemetry tracing extension
* [NCBC-2593](https://issues.couchbase.com/browse/NCBC-2593): Update install and start docs to reflect .NET Standard/Core support
* [NCBC-2594](https://issues.couchbase.com/browse/NCBC-2594): Update version number on release notes
* [NCBC-2595](https://issues.couchbase.com/browse/NCBC-2595): Indent code on error handling page so that it is readable.
* [NCBC-2227](https://issues.couchbase.com/browse/NCBC-2227): Author Managing Connections documentation
* [NCBC-2170](https://issues.couchbase.com/browse/NCBC-2170): Implement tracing using OpenTelemetry for Query
* [NCBC-2519](https://issues.couchbase.com/browse/NCBC-2519): Review docs for update items, identify/file issues
* [NCBC-2598](https://issues.couchbase.com/browse/NCBC-2598): Misc SDK improvements for Transactions
* [NCBC-2591](https://issues.couchbase.com/browse/NCBC-2591): Allow registration of custom services

### [](#version-3-0-2-20-june-2020)Version 3.0.2 (20 June 2020)

Version 3.0.2 is the third release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.2.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.2) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.2)

#### [](#known-issues-29)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2187](https://issues.couchbase.com/browse/NCBC-2187): CollectionManager — 400: Not allowed on this version of cluster.

#### [](#fixed-issues-59)Fixed Issues

* [NCBC-2436](https://issues.couchbase.com/browse/NCBC-2436): User connstr example in migration guide
* [NCBC-2459](https://issues.couchbase.com/browse/NCBC-2459): Remove QueryOptions from StartUsing.cs in docs
* [NCBC-2487](https://issues.couchbase.com/browse/NCBC-2487): NRE when bootstrapping - BucketConfigExtensions.ReplacePlaceholderWithBootstrapHost
* [NCBC-2506](https://issues.couchbase.com/browse/NCBC-2506): Connection attempt failed / timeout exception with Cloud and .NET SDK 3.0.1
* [NCBC-2508](https://issues.couchbase.com/browse/NCBC-2508): Alternate Addresses are not handled correctly in sdk3
* [NCBC-2512](https://issues.couchbase.com/browse/NCBC-2512): Additional debug logging and improvements
* [NCBC-2525](https://issues.couchbase.com/browse/NCBC-2525): Connection pool does not scale up to minimum connections after a temporary network failure.
* [NCBC-2526](https://issues.couchbase.com/browse/NCBC-2526): requests wait forever while cluster is unreachable
* [NCBC-2537](https://issues.couchbase.com/browse/NCBC-2537): Orphaned nodes when bootstrapping with a Memcached and a Couchbase bucket
* [NCBC-2538](https://issues.couchbase.com/browse/NCBC-2538): Analytics failures after failover/rebalance of the ept node
* [NCBC-2540](https://issues.couchbase.com/browse/NCBC-2540): Enumerating query results from SELECT RAW queries throws an exception
* [NCBC-2546](https://issues.couchbase.com/browse/NCBC-2546): Retry all exceptions with the IRetriable marker interface
* [NCBC-2548](https://issues.couchbase.com/browse/NCBC-2548): Ensure all operations attempt retrys when NMVB status is returned by server
* [NCBC-2549](https://issues.couchbase.com/browse/NCBC-2549): Subdoc failures after restarting CB server
* [NCBC-2552](https://issues.couchbase.com/browse/NCBC-2552): Intermittent cluster connection failures with CB Server <6.5
* [NCBC-2555](https://issues.couchbase.com/browse/NCBC-2555): Memcached and SSL results in "The handshake failed due to an unexpected packet format."
* [NCBC-2556](https://issues.couchbase.com/browse/NCBC-2556): Capture thrown exception and log the error when bootstrapping
* [NCBC-2558](https://issues.couchbase.com/browse/NCBC-2558): Couchbase.Extensions.DependencyInjection Failing On .NET Core 3.1

#### [](#new-features-and-behavioral-changes-44)New Features and Behavioral Changes.

* [NCBC-2202](https://issues.couchbase.com/browse/NCBC-2202): Integration tests need to configure tests to run based on server version
* [NCBC-2237](https://issues.couchbase.com/browse/NCBC-2237): PLAIN must not be enabled by default on non-tls connections
* [NCBC-2404](https://issues.couchbase.com/browse/NCBC-2404): ConnectAsync throws ArgumentNullException when cluster cannot be reached
* [NCBC-2530](https://issues.couchbase.com/browse/NCBC-2530): Provide navigation properties to get from ICouchbaseCollection back to ICluster
* [NCBC-2533](https://issues.couchbase.com/browse/NCBC-2533): Provide access to ITypeSerializer on ICluster for Linq2Couchbase
* [NCBC-2544](https://issues.couchbase.com/browse/NCBC-2544): Add additional DEBUG logging info and ContextIds
* [NCBC-2463](https://issues.couchbase.com/browse/NCBC-2463): Document documentation .NET
* [NCBC-2469](https://issues.couchbase.com/browse/NCBC-2469): Make nightly Jenkins builds work
* [NCBC-2495](https://issues.couchbase.com/browse/NCBC-2495): Update NuGet API Key in deployment pipeline on Jenkins
* [NCBC-2509](https://issues.couchbase.com/browse/NCBC-2509): CreateAndConnectAsync ONLY creates CouchbaseBuckets (not MemCache or Ephemeral)
* [NCBC-2517](https://issues.couchbase.com/browse/NCBC-2517): DependencyInjection project refactoring
* [NCBC-2523](https://issues.couchbase.com/browse/NCBC-2523): Port ClusterVersion from sdk2 to sdk3
* [NCBC-2527](https://issues.couchbase.com/browse/NCBC-2527): Update DnsClient to 1.3.2
* [NCBC-2529](https://issues.couchbase.com/browse/NCBC-2529): CB Cloud: non-KV nodes fail when used for bootstraping
* [NCBC-2534](https://issues.couchbase.com/browse/NCBC-2534): .NET Collections Functional Testing
* [NCBC-2539](https://issues.couchbase.com/browse/NCBC-2539): Port UnixMillisecondsConverter from sdk2 to sdk3
* [NCBC-2482](https://issues.couchbase.com/browse/NCBC-2482): Couchbase.IntegrationTests.Services.Search.SearchIndexManagerTests.TestSearchManager
* [NCBC-2483](https://issues.couchbase.com/browse/NCBC-2483): Couchbase.IntegrationTests.UserManagerTests.Test\_UserManager
* [NCBC-2484](https://issues.couchbase.com/browse/NCBC-2484): Couchbase.IntegrationTests.BucketManagerTests.Test\_BucketManager
* [NCBC-2485](https://issues.couchbase.com/browse/NCBC-2485): Couchbase.IntegrationTests.Diagnostics.PingReportTests.Can\_Get\_PingReport\_With\_ReportId
* [NCBC-2486](https://issues.couchbase.com/browse/NCBC-2486): Couchbase.IntegrationTests.CollectionManagerTests.Test\_CollectionManager
* [NCBC-2489](https://issues.couchbase.com/browse/NCBC-2489): Couchbase.IntegrationTests.ClusterTests.Test\_Open\_More\_Than\_One\_Bucket
* [NCBC-2490](https://issues.couchbase.com/browse/NCBC-2490): Couchbase.ServiceNotAvailableException : Service views not available.
* [NCBC-2518](https://issues.couchbase.com/browse/NCBC-2518): HttpStreamingConfigListener should continue running after all streams break.
* [NCBC-2524](https://issues.couchbase.com/browse/NCBC-2524): Couchbase.IntegrationTests.ClusterTests.Test\_WaitUntilReadyAsync
* [NCBC-2531](https://issues.couchbase.com/browse/NCBC-2531): Implement OpenTelemetry Stub in CouchbaseNetClient
* [NCBC-2532](https://issues.couchbase.com/browse/NCBC-2532): Remove existing OpenTracing dependency

### [](#version-3-0-1-13-may-2020)Version 3.0.1 (13 May 2020)

Version 3.0.1 is the second release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.1.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.1) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.1)

#### [](#known-issues-30)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2187](https://issues.couchbase.com/browse/NCBC-2187): CollectionManager — 400: Not allowed on this version of cluster.

#### [](#fixed-issues-60)Fixed Issues

* [NCBC-2033](https://issues.couchbase.com/browse/NCBC-2033): 3.0 API Query snippets in concept doc
* [NCBC-2204](https://issues.couchbase.com/browse/NCBC-2204): Improve exception when bootstrapping fails
* [NCBC-2301](https://issues.couchbase.com/browse/NCBC-2301): 3.0 Logging / Collecting Info page
* [NCBC-2303](https://issues.couchbase.com/browse/NCBC-2303): Client Settings page for SDK 3.0
* [NCBC-2388](https://issues.couchbase.com/browse/NCBC-2388): Ensure that prepared statements that are previously created are not retried
* [NCBC-2435](https://issues.couchbase.com/browse/NCBC-2435): Connstr not taking username properly
* [NCBC-2439](https://issues.couchbase.com/browse/NCBC-2439): improve formatting on exception context
* [NCBC-2451](https://issues.couchbase.com/browse/NCBC-2451): QueryPreparedStatementFailure in situational tests with MH
* [NCBC-2454](https://issues.couchbase.com/browse/NCBC-2454): EndPoint may be null during SendAsync
* [NCBC-2456](https://issues.couchbase.com/browse/NCBC-2456): Transient NodeNotAvailableException rebalance under kv load
* [NCBC-2458](https://issues.couchbase.com/browse/NCBC-2458): QueryAsync(String statement) does not exist
* [NCBC-2460](https://issues.couchbase.com/browse/NCBC-2460): .NET Core App 3.x targets require consumers add reference to Microsoft.Bcl.AsyncInterfaces
* [NCBC-2462](https://issues.couchbase.com/browse/NCBC-2462): ConnectAsync is failing "Cannot resolve DNS for localhost"
* [NCBC-2466](https://issues.couchbase.com/browse/NCBC-2466): Ensure TaskCancelationExceptions are rethrown
* [NCBC-2467](https://issues.couchbase.com/browse/NCBC-2467): CLONE - Ensure TaskCancelationExceptions are rethrown
* [NCBC-2468](https://issues.couchbase.com/browse/NCBC-2468): System.ArgumentException: ReadResult does not contain valid MutationToken
* [NCBC-2473](https://issues.couchbase.com/browse/NCBC-2473): Incorrect Verbiage for NuGet Package
* [NCBC-2475](https://issues.couchbase.com/browse/NCBC-2475): GetNodes() sometimes returns no results, incorrectly.
* [NCBC-2479](https://issues.couchbase.com/browse/NCBC-2479): Point config.json for combination tests back at localhost
* [NCBC-2480](https://issues.couchbase.com/browse/NCBC-2480): SocketException: Cannot bind to address in SslConnectionTests
* [NCBC-2481](https://issues.couchbase.com/browse/NCBC-2481): KV operations don’t respect IgnoreCertificateNameMismatch
* [NCBC-2488](https://issues.couchbase.com/browse/NCBC-2488): Couchbase.IntegrationTests.BootstrapFailedTests.Test\_BootStrap\_Error\_Propagates\_To\_View\_Operations \[FAIL\]
* [NCBC-2493](https://issues.couchbase.com/browse/NCBC-2493): Improve error logging and handling for Query
* [NCBC-2497](https://issues.couchbase.com/browse/NCBC-2497): SetKeepAlive fails on Windows

#### [](#new-features-and-behavioral-changes-45)New Features and Behavioral Changes.

* [NCBC-2304](https://issues.couchbase.com/browse/NCBC-2304): Managing Connections - SDK3
* [NCBC-2464](https://issues.couchbase.com/browse/NCBC-2464): Build/deploy the .NET Dependency Injection extension for SDK 3.0
* [NCBC-2478](https://issues.couchbase.com/browse/NCBC-2478): Cluster.ConnectAsync throws PlatformNotSupportedException
* [NCBC-2492](https://issues.couchbase.com/browse/NCBC-2492): Log warning when TCPKeepAlive cannot be enabled
* [NCBC-2494](https://issues.couchbase.com/browse/NCBC-2494): Fix TCPKeepAlive to work on non Windows Platform

### [](#version-3-0-0-31-march-2020)Version 3.0.0 (31 March 2020)

This is the first GA release of the third generation .NET SDK.

[Download](https://packages.couchbase.com/clients/net/3.0/Couchbase-Net-Client-3.0.0.zip) | [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client-3.0.0) | [Nuget](https://www.nuget.org/packages/CouchbaseNetClient/3.0.0)

This is the first GA release of the third generation .NET SDK.

This release features significant changes to the API, simplifies the programming model, adds support for newer Durability Requirements and enables simple extension for features coming in future Couchbase Server releases. See the [Migration Guide](migrating-sdk-code-to-3.n.md) for help with migrating from .NET SDK 2.x.

#### [](#known-issues-31)Known Issues

* [NCBC-3171](https://issues.couchbase.com/browse/NCBC-3171): Documents may be written to the wrong location in a mixed-mode cluster set-up. See the [Special Note](#special-note) for more details.
* [NCBC-2187](https://issues.couchbase.com/browse/NCBC-2187): CollectionManager — 400: Not allowed on this version of cluster.

#### [](#fixed-issues-61)Fixed Issues

* [NCBC-2149](https://issues.couchbase.com/browse/NCBC-2149): ConfigConext throws NullReferenceException when processing new cluster maps
* [NCBC-2153](https://issues.couchbase.com/browse/NCBC-2153): Fix failing integration tests for SDK3
* [NCBC-2166](https://issues.couchbase.com/browse/NCBC-2166): Authentication Errors after adding nodes to cluster
* [NCBC-2168](https://issues.couchbase.com/browse/NCBC-2168): QueryException does not provide textual details coming from the server
* [NCBC-2199](https://issues.couchbase.com/browse/NCBC-2199): Missing string interpolation sign in CouchbaseBucket
* [NCBC-2213](https://issues.couchbase.com/browse/NCBC-2213): N1QL situational test failure - Rb1SwapQuery
* [NCBC-2214](https://issues.couchbase.com/browse/NCBC-2214): N1QL situational test failure - SvcRestartQuery
* [NCBC-2217](https://issues.couchbase.com/browse/NCBC-2217): Deserialization issues with GetAsync<T>
* [NCBC-2219](https://issues.couchbase.com/browse/NCBC-2219): Cluster instantiation using ClusterOptions ignores WithServers servers
* [NCBC-2222](https://issues.couchbase.com/browse/NCBC-2222): AuthenticationFailure thrown when accessing bucket while combination testing
* [NCBC-2230](https://issues.couchbase.com/browse/NCBC-2230): QueryException missing XxxxContext
* [NCBC-2241](https://issues.couchbase.com/browse/NCBC-2241): Defer bootstrapping errors on buckets to first operation
* [NCBC-2266](https://issues.couchbase.com/browse/NCBC-2266): UserManager#AvailableRolesAsync must be called getRoles
* [NCBC-2268](https://issues.couchbase.com/browse/NCBC-2268): CollectionManager does not align with RFC
* [NCBC-2273](https://issues.couchbase.com/browse/NCBC-2273): Incorrect ScopeMissingException
* [NCBC-2274](https://issues.couchbase.com/browse/NCBC-2274): Can’t connect to two buckets from one cluster object
* [NCBC-2277](https://issues.couchbase.com/browse/NCBC-2277): SearchOptions does not map query parameters
* [NCBC-2282](https://issues.couchbase.com/browse/NCBC-2282): fix test and implementation of positional params
* [NCBC-2286](https://issues.couchbase.com/browse/NCBC-2286): Make all options have no "With" prefix
* [NCBC-2288](https://issues.couchbase.com/browse/NCBC-2288): MutateIn ContentAs() functionality missing
* [NCBC-2290](https://issues.couchbase.com/browse/NCBC-2290): Add Timeout to all options classes in BucketManager
* [NCBC-2306](https://issues.couchbase.com/browse/NCBC-2306): Match RFC requirement for Rows property for query services
* [NCBC-2307](https://issues.couchbase.com/browse/NCBC-2307): Cannot query using any type other than dynamic
* [NCBC-2308](https://issues.couchbase.com/browse/NCBC-2308): N1QL query situational failure
* [NCBC-2309](https://issues.couchbase.com/browse/NCBC-2309): Hybrid/view query errors with situational testing
* [NCBC-2316](https://issues.couchbase.com/browse/NCBC-2316): Ensure view request get default timeout if not supplied
* [NCBC-2324](https://issues.couchbase.com/browse/NCBC-2324): Random KeyNotFoundException in LogManagerTests.Test\_LogLevel\_Debug
* [NCBC-2350](https://issues.couchbase.com/browse/NCBC-2350): SearchOptions.Raw is unused, and throws an NRE
* [NCBC-2351](https://issues.couchbase.com/browse/NCBC-2351): View timeout is not applied to view query string
* [NCBC-2352](https://issues.couchbase.com/browse/NCBC-2352): Cleanup Service Exceptions Hiding Context
* [NCBC-2353](https://issues.couchbase.com/browse/NCBC-2353): Cleanup .NET SDK 3 Build Warnings
* [NCBC-2354](https://issues.couchbase.com/browse/NCBC-2354): Most Integration Tests Failing
* [NCBC-2365](https://issues.couchbase.com/browse/NCBC-2365): Ensure Exists checks if deleted is true then exists returns false
* [NCBC-2366](https://issues.couchbase.com/browse/NCBC-2366): AnalyticsManager does not exist
* [NCBC-2367](https://issues.couchbase.com/browse/NCBC-2367): Methods in ClusterNode have unused "connections" parameter
* [NCBC-2369](https://issues.couchbase.com/browse/NCBC-2369): Ping diagnostics are not accurately reporting ping times
* [NCBC-2372](https://issues.couchbase.com/browse/NCBC-2372): NRE thrown while initializing cluster
* [NCBC-2384](https://issues.couchbase.com/browse/NCBC-2384): SSL connections cannot find node for K/V operations
* [NCBC-2389](https://issues.couchbase.com/browse/NCBC-2389): ClusterNode must be associated with a bucket once a bucket has been opened
* [NCBC-2397](https://issues.couchbase.com/browse/NCBC-2397): OPS pulses between zero and the expected performance
* [NCBC-2402](https://issues.couchbase.com/browse/NCBC-2402): Add ConfigureAwait(false) to all asynchronous code
* [NCBC-2407](https://issues.couchbase.com/browse/NCBC-2407): Couchbase.ServiceNotAvailableException: Service n1ql not available
* [NCBC-2416](https://issues.couchbase.com/browse/NCBC-2416): ViewQuery failure/hanging
* [NCBC-2421](https://issues.couchbase.com/browse/NCBC-2421): Remove default to NotBounded in FTS
* [NCBC-2422](https://issues.couchbase.com/browse/NCBC-2422): Error replacing dead connections on N1QL Failover rebalance
* [NCBC-2426](https://issues.couchbase.com/browse/NCBC-2426): Service Restart failure - replacing dead connections failure
* [NCBC-2429](https://issues.couchbase.com/browse/NCBC-2429): Should be MaxHttpConnections instead of MaxHttpConnection
* [NCBC-2446](https://issues.couchbase.com/browse/NCBC-2446): Ensure bootstrapping continues after BucketNotConnected on pre-6.5 servers
* [NCBC-2448](https://issues.couchbase.com/browse/NCBC-2448): unpublish concurrent document mutations
* [NCBC-2183](https://issues.couchbase.com/browse/NCBC-2183): Exists must use "getMeta" (0xa0) instead of Observe
* [NCBC-2410](https://issues.couchbase.com/browse/NCBC-2410): LookupInResult has NotImplementedException for some methods
* [NCBC-2412](https://issues.couchbase.com/browse/NCBC-2412): Cluster.AnaytlicsIndexes throws NotImplementedException
* [NCBC-2414](https://issues.couchbase.com/browse/NCBC-2414): Connection terminated when packet exceeds NetworkStream buffer size
* [NCBC-2415](https://issues.couchbase.com/browse/NCBC-2415): error CS0649: Field 'SubDocSingularBase<T>.CurrentSpec' is null
* [NCBC-2430](https://issues.couchbase.com/browse/NCBC-2430): HttpMaxConnections renaming breaks DI unit tests
* [NCBC-2431](https://issues.couchbase.com/browse/NCBC-2431): Failed DNS resolution throws NullReferenceException
* [NCBC-2433](https://issues.couchbase.com/browse/NCBC-2433): Fix failing tests involving MaxHttpConnection
* [NCBC-2305](https://issues.couchbase.com/browse/NCBC-2305): RequestId, ClientContextId, and Signature Lost After N1QL Query Enumeration
* [NCBC-2358](https://issues.couchbase.com/browse/NCBC-2358): Timeout is not written to the packet when using Durability

#### [](#new-features-and-behavioral-changes-46)New Features and Behavioral Changes.

* [NCBC-2315](https://issues.couchbase.com/browse/NCBC-2315): Improve logging for each service request
* [NCBC-2325](https://issues.couchbase.com/browse/NCBC-2325): Add SCRAM-SHA Sasl Authentication
* [NCBC-1863](https://issues.couchbase.com/browse/NCBC-1863): Add Flushing or Deleting a Collection logic
* [NCBC-1870](https://issues.couchbase.com/browse/NCBC-1870): Support Log Redaction
* [NCBC-1915](https://issues.couchbase.com/browse/NCBC-1915): Add new consistency API to SDK 3.0
* [NCBC-2151](https://issues.couchbase.com/browse/NCBC-2151): Migrating from SDK 2 to 3.0
* [NCBC-2169](https://issues.couchbase.com/browse/NCBC-2169): Migrating from SDK 2 to 3.0
* [NCBC-2209](https://issues.couchbase.com/browse/NCBC-2209): Add Converters/Transcoders per RFC
* [NCBC-2220](https://issues.couchbase.com/browse/NCBC-2220): Ensure ClusterOptions properties are integrated into SDK
* [NCBC-2234](https://issues.couchbase.com/browse/NCBC-2234): Mark all ErrorContexts as Uncomitted
* [NCBC-2302](https://issues.couchbase.com/browse/NCBC-2302): Getting Started Tidy Up
* [NCBC-2413](https://issues.couchbase.com/browse/NCBC-2413): Add XxxErrorContext information to K/V
* [NCBC-2417](https://issues.couchbase.com/browse/NCBC-2417): Remove all Singular Sub-Document classes
* [NCBC-1799](https://issues.couchbase.com/browse/NCBC-1799): Analytics client needs to support streaming results
* [NCBC-1989](https://issues.couchbase.com/browse/NCBC-1989): Add connection pooling
* [NCBC-2244](https://issues.couchbase.com/browse/NCBC-2244): WaitUntilReady not available at the cluster and bucket levels
* [NCBC-2245](https://issues.couchbase.com/browse/NCBC-2245): Cluster-level ping missing
* [NCBC-2260](https://issues.couchbase.com/browse/NCBC-2260): Tighten OperationSpec for lookupIn and mutateIn
* [NCBC-2293](https://issues.couchbase.com/browse/NCBC-2293): Remove deprecated ErrorAttribute enum
* [NCBC-2297](https://issues.couchbase.com/browse/NCBC-2297): Decrease API surface surrounding K/V operations/connections
* [NCBC-2299](https://issues.couchbase.com/browse/NCBC-2299): Implement non-streaming fallback for N1QL queries
* [NCBC-2300](https://issues.couchbase.com/browse/NCBC-2300): Support custom stream deserializers for view queries
* [NCBC-2310](https://issues.couchbase.com/browse/NCBC-2310): Make IQueryResult implementations internal
* [NCBC-2312](https://issues.couchbase.com/browse/NCBC-2312): Make IServiceResult.RetryReason read only
* [NCBC-2313](https://issues.couchbase.com/browse/NCBC-2313): Align StreamAlreadyReadException with other Couchbase exceptions
* [NCBC-2314](https://issues.couchbase.com/browse/NCBC-2314): Implement non-streaming fallback for view queries
* [NCBC-2318](https://issues.couchbase.com/browse/NCBC-2318): Refactor view queries to be strongly typed
* [NCBC-2319](https://issues.couchbase.com/browse/NCBC-2319): Implement non-streaming fallback for analytics queries
* [NCBC-2320](https://issues.couchbase.com/browse/NCBC-2320): Cleanup K/V classes in root namespace
* [NCBC-2322](https://issues.couchbase.com/browse/NCBC-2322): Enable symbol packages and SourceLink for debugging
* [NCBC-2323](https://issues.couchbase.com/browse/NCBC-2323): Enable C# 8 nullable ref types for buckets/scopes/collections
* [NCBC-2327](https://issues.couchbase.com/browse/NCBC-2327): Create Lightweight DI system for Couchbase SDK
* [NCBC-2328](https://issues.couchbase.com/browse/NCBC-2328): Update Cluster and Bucket to use DI for Logging
* [NCBC-2329](https://issues.couchbase.com/browse/NCBC-2329): Update RetryOrchestrator to use DI for logging
* [NCBC-2330](https://issues.couchbase.com/browse/NCBC-2330): Make transaction/serializer/mapper configurable via DI
* [NCBC-2331](https://issues.couchbase.com/browse/NCBC-2331): Use DI for Scope and Collection logging
* [NCBC-2332](https://issues.couchbase.com/browse/NCBC-2332): Remove default constructor added to BucketBase (CS8618 warning)
* [NCBC-2334](https://issues.couchbase.com/browse/NCBC-2334): All integration tests fail, cannot bootstrap
* [NCBC-2336](https://issues.couchbase.com/browse/NCBC-2336): Use DI for CouchbaseHttpClient
* [NCBC-2337](https://issues.couchbase.com/browse/NCBC-2337): Remove ClusterContext requirement from service clients
* [NCBC-2338](https://issues.couchbase.com/browse/NCBC-2338): Use DI for service clients and their loggers
* [NCBC-2340](https://issues.couchbase.com/browse/NCBC-2340): Use DI for logging in configuration handlers
* [NCBC-2341](https://issues.couchbase.com/browse/NCBC-2341): Use DI for OrphanedResponseLogger logging
* [NCBC-2343](https://issues.couchbase.com/browse/NCBC-2343): Use DI for logging in data structures
* [NCBC-2344](https://issues.couchbase.com/browse/NCBC-2344): Use DI for logging in managers
* [NCBC-2345](https://issues.couchbase.com/browse/NCBC-2345): Use DI for logging in DNS resolver
* [NCBC-2346](https://issues.couchbase.com/browse/NCBC-2346): Use DI for logging in GetResult
* [NCBC-2347](https://issues.couchbase.com/browse/NCBC-2347): Use DI for logging in QueryUriTesters
* [NCBC-2348](https://issues.couchbase.com/browse/NCBC-2348): Use DI for VBucket and ErrorMap logging
* [NCBC-2349](https://issues.couchbase.com/browse/NCBC-2349): Enable Nullable Ref Types in ClusterOptions
* [NCBC-2355](https://issues.couchbase.com/browse/NCBC-2355): Support deserialization of ClusterOptions from configuration
* [NCBC-2356](https://issues.couchbase.com/browse/NCBC-2356): Move content services directory to root in Couchbase.UnitTests
* [NCBC-2357](https://issues.couchbase.com/browse/NCBC-2357): Enable nullable ref types for XxxOptions classes
* [NCBC-2359](https://issues.couchbase.com/browse/NCBC-2359): Use DNS resolver for IP address resolution
* [NCBC-2360](https://issues.couchbase.com/browse/NCBC-2360): Use DNS resolver in Ketama key mapper and ClusterContext
* [NCBC-2362](https://issues.couchbase.com/browse/NCBC-2362): Make ConfigChanged handling async
* [NCBC-2363](https://issues.couchbase.com/browse/NCBC-2363): Use DNS resolver for VBucketServerMap.IPEndPoints
* [NCBC-2364](https://issues.couchbase.com/browse/NCBC-2364): Enable null reference types for K/V specs/results
* [NCBC-2368](https://issues.couchbase.com/browse/NCBC-2368): Remove Servers From ClusterOptions
* [NCBC-2370](https://issues.couchbase.com/browse/NCBC-2370): Support custom port numbers in ConnectionString
* [NCBC-2371](https://issues.couchbase.com/browse/NCBC-2371): Make BucketConfig and other config serialization classes internal
* [NCBC-2373](https://issues.couchbase.com/browse/NCBC-2373): Implement abstraction layer for connection pool implementations
* [NCBC-2374](https://issues.couchbase.com/browse/NCBC-2374): Replace TKey with string parameter in persistent collections
* [NCBC-2376](https://issues.couchbase.com/browse/NCBC-2376): Cleanup BootstrapUri on ClusterNode
* [NCBC-2377](https://issues.couchbase.com/browse/NCBC-2377): Implement auto scaling on connection pools
* [NCBC-2378](https://issues.couchbase.com/browse/NCBC-2378): Add log redaction to DataFlowConnectionPool
* [NCBC-2379](https://issues.couchbase.com/browse/NCBC-2379): Respect couchbases scheme for DNS SRV lookup
* [NCBC-2380](https://issues.couchbase.com/browse/NCBC-2380): ClusterOptions MgmtPort and EnableTls cleanup
* [NCBC-2381](https://issues.couchbase.com/browse/NCBC-2381): Cleanup IConnection interface
* [NCBC-2382](https://issues.couchbase.com/browse/NCBC-2382): Support multiplexing on SslConnection
* [NCBC-2383](https://issues.couchbase.com/browse/NCBC-2383): NodeAdapter is null on non-bootstrap nodes
* [NCBC-2387](https://issues.couchbase.com/browse/NCBC-2387): Reduce heap allocations related to K/V operation response handling
* [NCBC-2391](https://issues.couchbase.com/browse/NCBC-2391): Include XML documentation in NuGet package
* [NCBC-2392](https://issues.couchbase.com/browse/NCBC-2392): Reduce heap allocations around MultiplexingConnection async state
* [NCBC-2393](https://issues.couchbase.com/browse/NCBC-2393): Align QueryScanConsistency with the RFC
* [NCBC-2398](https://issues.couchbase.com/browse/NCBC-2398): Change ICollection interface to ICouchbaseCollection interface
* [NCBC-2399](https://issues.couchbase.com/browse/NCBC-2399): Add bootstrap service
* [NCBC-2408](https://issues.couchbase.com/browse/NCBC-2408): Add BucketContext or equivalent for cohesion and less coupling
* [NCBC-2409](https://issues.couchbase.com/browse/NCBC-2409): Route nodes into service specific CouchbaseNodeCollections
* [NCBC-2425](https://issues.couchbase.com/browse/NCBC-2425): Reduce heap allocations calling BucketAsync

### [](#pre-releases)Pre-releases

Numerous _Alpha_ and _Beta_ releases were made in the run-up to the 3.0 release, and although unsupported, the release notes and download links are retained for archive purposes [here](3.0-pre-release-notes.md).

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).

Distributed ACID Transactions, now incorporated within the .NET SDK, was previously available as a separate library. Release notes for the legacy transactions library can be found in the [docs archive](https://docs-archive.couchbase.com/dotnet-sdk/3.3/project-docs/distributed-transactions-dotnet-release-notes.html).