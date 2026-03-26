---
title: Release Notes
description: Couchbase Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@sync-gateway::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/release-notes.html)

# Release Notes

Quicklinks

[Release 3.0](../3.0/release-notes.md) | [Release 2.8](../2.8/release-notes.md) | [Archived documentation](https://docs-archive.couchbase.com/home/index.html)

> Couchbase Sync Gateway  
> This content describes the key features and changes implemented by release 3.1.12 of Couchbase Sync Gateway

> [!CAUTION]
> One Way Upgrade
> 
> The migration to 3.x configuration is a ONE WAY process — see: [Upgrading](upgrading.md) for more.

## [](#maint-latest)3.1.12 — February 2025

Version 3.1.12 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-12)Fixed Issues

None for this release

### [](#enhancements)Enhancements

* [CBG-4349 - Restore single entry skipped sequence list](https://jira.issues.couchbase.com/browse/CBG-4349)
* [CBG-4360 - Use UNIX timestamp on reverted skipped list entry](https://jira.issues.couchbase.com/browse/CBG-4360)

### [](#known-issues)Known Issues

None for this release.

### [](#deprecations)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-11september-2024)3.1.11 — September 2024

Version 3.1.11 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-11)Fixed Issues

* [CBG-3953 - Avoid timeout on creating indexes asynchronously](https://jira.issues.couchbase.com/browse/CBG-3953)
* [CBG-3966 - Fixed error where collection appears to be linked to 2 DBs after update](https://jira.issues.couchbase.com/browse/CBG-3966)
* [CBG-4004 - Fixed DeleteRole doesnt trigger history calculation for named collections](https://jira.issues.couchbase.com/browse/CBG-4004)
* [CBG-4016 - nextSequenceGreaterThan now updates to current \_sync:seq before releasing sequences](https://jira.issues.couchbase.com/browse/CBG-4016)
* [CBG-4022 - Fixed race condition between config poll and dbconfig update](https://jira.issues.couchbase.com/browse/CBG-4022)
* [CBG-4029 - Fixed Users dynamically computed roles not getting invalidated after a resync](https://jira.issues.couchbase.com/browse/CBG-4029)
* [CBG-4073 - Fixed panic in CheckpointHash function for bucket UUID call](https://jira.issues.couchbase.com/browse/CBG-4073)
* [CBG-4107 - Fix error behavior in removeCorruptConfigIfExists where the database wasn't unloaded/removed](https://jira.issues.couchbase.com/browse/CBG-4107)
* [CBG-4127 - Decouple client request context from lazy-init OIDC discovery sync process](https://jira.issues.couchbase.com/browse/CBG-4127)
* [CBG-4173 - Fixed corrupt DB config handling doesn't remove the config when longer present in the bucket](https://jira.issues.couchbase.com/browse/CBG-4173)
* [CBG-4221 - Pending unused sequences shouldn't update high cache sequence](https://jira.issues.couchbase.com/browse/CBG-4221)
* [CBG-4218 - Duplicated sequences can cause SGW to be unresponsive](https://jira.issues.couchbase.com/browse/CBG-4218)

### [](#enhancements-2)Enhancements

* [CBG-3983 - sgcollect\_info: Switch to runtime config endpoint to determine logFilePath](https://jira.issues.couchbase.com/browse/CBG-3983)
* [CBG-4028 - Failure to perform on-demand import results in not found/noRev](https://jira.issues.couchbase.com/browse/CBG-4028)
* [CBG-4035 - Skipped Sequence Optimisations](https://jira.issues.couchbase.com/browse/CBG-4035)
* [CBG-4036 - Detect and handle \_sync:seq rollback in sequence allocator](https://jira.issues.couchbase.com/browse/CBG-4036)
* [CBG-4082 - Lower config mismatch logging to debug](https://jira.issues.couchbase.com/browse/CBG-4082)
* [CBG-4145 - Improvements to the "could not verify JWT" error logging](https://jira.issues.couchbase.com/browse/CBG-4145)
* [CBG-4162 - Log the origin of setting metadata ID when updating a dbconfig](https://jira.issues.couchbase.com/browse/CBG-4162)

### [](#known-issues-2)Known Issues

None for this release.

### [](#deprecations-2)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-8july-2024)3.1.8 — July 2024

Version 3.1.8 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-8)Fixed Issues

* [CBG-3951 - Fixed Users API for database with default metadataID can return other db users in the bucket](https://issues.couchbase.com/browse/CBG-3951)
* [CBG-3955 - Fixed updating import\_filter and sync\_filter to empty string does not work for named collection](https://issues.couchbase.com/browse/CBG-3955)
* [CBG-3990 - Fixed Documents may not be imported when collection added to an existing db](https://issues.couchbase.com/browse/CBG-3990)
* [CBG-4009 - All config updates now supported during async initialization](https://issues.couchbase.com/browse/CBG-4009)

### [](#enhancements-3)Enhancements

* [CBG-3879 - Recovery from cas mismatch on metadata documents when using xattrConfig now possible](https://issues.couchbase.com/browse/CBG-3879)
* [CBG-3946 - Bucket and collection now provided when returning an error about inability to create collections](https://issues.couchbase.com/browse/CBG-3946)
* [CBG-3959 - Include collection set in resync status](https://issues.couchbase.com/browse/CBG-3959)
* [CBG-3964 - Check/wait for principal doc index readiness in resync w/ regenerate sequences](https://issues.couchbase.com/browse/CBG-3964)
* [CBG-3965 - Do not regenerate principal seqs unless resync is running on default collection](https://issues.couchbase.com/browse/CBG-3965)
* [CBG-3967 - Add a reason for why a database is offline in /\_all\_dbs](https://issues.couchbase.com/browse/CBG-3967)
* [CBG-4020 - Add initialization active property to DbSummary](https://issues.couchbase.com/browse/CBG-4020)

### [](#known-issues-3)Known Issues

None for this release.

### [](#deprecations-3)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-6may-2024)3.1.6 — May 2024

Version 3.1.6 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-6)Fixed Issues

* [CBG-3683 - Fixed PANIC error when closing channel cache after Mutation feed fails to start inside StartOnlineProcesses](https://issues.couchbase.com/browse/CBG-3683)
* [CBG-3828 - Fixed sgcollect windows doesn't collect stderr / stdout](https://issues.couchbase.com/browse/CBG-3828)
* [CBG-3845 - Fixed updateSeq must happen after DCP callback invocation](https://issues.couchbase.com/browse/CBG-3845)
* [CBG-3878 - Fixed UnmarshalDocumentSyncDataFromFeed doesn't return any present user xattrs if sync data doesn't exist on the doc](https://issues.couchbase.com/browse/CBG-3878)
* [CBG-3906 - Fixed logging for GetDatabaseConfigs verbose and ambiguous](https://issues.couchbase.com/browse/CBG-3906)

### [](#enhancements-4)Enhancements

* [CBG-3826 - Warn if there is a large number of skipped sequences](https://issues.couchbase.com/browse/CBG-3826)
* [CBG-3860 - Reduce EOF logging from go-blip](https://issues.couchbase.com/browse/CBG-3860)
* [CBG-3876 - Tweak logging around import of JSON but not JSON object docs](https://issues.couchbase.com/browse/CBG-3876)

### [](#known-issues-4)Known Issues

None for this release.

### [](#deprecations-4)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-5april-2024)3.1.5 — April 2024

Version 3.1.5 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-5)Fixed Issues

* [CBG-3885 - Fixed OIDC-auth causes admin\_channels/admin\_roles loss](https://issues.couchbase.com/browse/CBG-3885)
* [CBG-3887 - Fixed sgcollect\_info fails to upload to s3](https://issues.couchbase.com/browse/CBG-3887)
* [CBG-3029 - Fixed sg\_collect fails to get SGW config](https://issues.couchbase.com/browse/CBG-3029)
* [CBG-3611 - Fixed PUT to \_user/<username> does not override omitted fields](https://issues.couchbase.com/browse/CBG-3611)
* [CBG-3699 - Fixed error from handleChangesResponse not handled correctly](https://issues.couchbase.com/browse/CBG-3699)
* [CBG-3723 - Fixed TCP\_NODELAY does not work for TLS connections](https://issues.couchbase.com/browse/CBG-3723)
* [CBG-3725 - Fixed import DCP rollback unsuccessful in data migration cases](https://issues.couchbase.com/browse/CBG-3725)
* [CBG-3744 - Fixed fetchAndLoadDatabase NewDatabaseContext race](https://issues.couchbase.com/browse/CBG-3744)
* [CBG-3760 - Fixed sgcollect\_info not collecting trace logging](https://issues.couchbase.com/browse/CBG-3760)
* [CBG-3761 - Fixed user API Ignore read-only fields if values unchanged](https://issues.couchbase.com/browse/CBG-3761)
* [CBG-3774 - Fixed incorrect log key used for log message inside DocChanged function](https://issues.couchbase.com/browse/CBG-3774)
* [CBG-3777 - Fixed kv\_pool\_size on import feed can be non zero](https://issues.couchbase.com/browse/CBG-3777)
* [CBG-3793 - Perform allow\_dbconfig\_env\_vars check in getAuthScopeHandleCreateDB](https://issues.couchbase.com/browse/CBG-3793)
* [CBG-3812 - Fixed sg\_collect fails to get SGW config](https://issues.couchbase.com/browse/CBG-3812)

### [](#enhancements-5)Enhancements

* [CBG-3682 - sgcollect can upload zips in excess of 2GB](https://issues.couchbase.com/browse/CBG-3682)
* [CBG-3749 - Better logging around config registry operations](https://issues.couchbase.com/browse/CBG-3749)
* [CBG-3762 - BLIP context ID now included in \_blipsync response](https://issues.couchbase.com/browse/CBG-3762)
* [CBG-3776 - There is now a configurable revs parallelism limit](https://issues.couchbase.com/browse/CBG-3776)

### [](#known-issues-5)Known Issues

* [CBG-3614 - DCP node list/alternate adddresses do not refresh after cluster topology change](https://issues.couchbase.com/browse/CBG-3614)

### [](#deprecations-5)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-3december-2023)3.1.3 — December 2023

Version 3.1.3 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-3)Fixed Issues

* [CBG-3639 - Fixed InjectJSONProperties not escaping string values.](https://issues.couchbase.com/browse/CBG-3639)
* [CBG-3643 - Fix incorrect usage of PreserveExpiry with an expiry and no doc flags.](https://issues.couchbase.com/browse/CBG-3643)
* [CBG-3659 - cbgt fix to avoid file system writes.](https://issues.couchbase.com/browse/CBG-3659)

### [](#enhancements-6)Enhancements

* [CBG-3685 - CORS max\_age now configurable on a database level.](https://issues.couchbase.com/browse/CBG-3685)

### [](#known-issues-6)Known Issues

None for this release.

### [](#deprecations-6)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-2november-2023)3.1.2 — November 2023

Version 3.1.2 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-2)Fixed Issues

* [CBG-3560 - Inherited channels from roles are not checked when running changes feed filtered to a channel](https://issues.couchbase.com/browse/CBG-3560)
* [CBG-3554 - Increasing memory usage when failing to apply a database config from the bucket](https://issues.couchbase.com/browse/CBG-3554)
* [CBG-3550 - Retry limit not set for operations requiring non-SDK retry](https://issues.couchbase.com/browse/CBG-3550)
* [CBG-3465 - Config migration should consider use\_xattr\_config](https://issues.couchbase.com/browse/CBG-3465)
* [CBG-3462 - Sync Gateway should not use 3.0 config when 3.1 config is present](https://issues.couchbase.com/browse/CBG-3462)
* [CBG-3454 - Per-db log settings should take precedence over bootstrap](https://issues.couchbase.com/browse/CBG-3454)
* [CBG-3450 - DCP rollback should force checkpoint persistence](https://issues.couchbase.com/browse/CBG-3450)
* [CBG-3426 - Explicit check on xattr length to avoid panics](https://issues.couchbase.com/browse/CBG-3426)
* [CBG-3405- Investigate the default scope/collection requiring resync after upgrade](https://issues.couchbase.com/browse/CBG-3405)
* [CBG-3404 - Hook up the reset resync code to a parameter that is pssed into the resync endpoint](https://issues.couchbase.com/browse/CBG-3404)
* [CBG-3403 -Handle rollback error for resync operations](https://issues.couchbase.com/browse/CBG-3403)
* [CBG-3398 - Pick up gocb fix for bootstrapping against non KV nodes](https://issues.couchbase.com/browse/CBG-3398)
* [CBG-3397 - SG warning when client's maxHistory for a rev is exceeded on push](https://issues.couchbase.com/browse/CBG-3397)
* [CBG-3383- Invalid error handling state for async db online](https://issues.couchbase.com/browse/CBG-3383)
* [CBG-3350 - SGW 3.1.1 using 50-75% more memory compared to 3.1.0](https://issues.couchbase.com/browse/CBG-3350)
* [CBG-3330 -buildRevokedFeed query iteration fails when no documents processed](https://issues.couchbase.com/browse/CBG-3330)
* [CBG-3329 - Revision Cache, Replications with purge\_on\_removal and meta.xattrs for channel assignment not purging/syncing consistently](https://issues.couchbase.com/browse/CBG-3329)
* [CBG-3197 - Cannot update db config from implicit '\_default' scope to explicit '\_default' scope](https://issues.couchbase.com/browse/CBG-3197)

### [](#enhancements-7)Enhancements

* [CBG-3557 - Improve behavior when allocating sequence much lower than existing doc seq](https://issues.couchbase.com/browse/CBG-3557)
* [CBG-3509 - Add opt-out for config env var expansion for db configs](https://issues.couchbase.com/browse/CBG-3509)
* [CBG-3495 - Detect and provide metrics for duplicate database names in bootstrap polling](https://issues.couchbase.com/browse/CBG-3495)
* [CBG-3494 - Enforce "bucket" field match in DbConfig](https://issues.couchbase.com/browse/CBG-3494)
* [CBG-3457 - Prevent minor version downgrade](https://issues.couchbase.com/browse/CBG-3457)
* [CBG-3432 - Move KeyDCP changes and cache logging to KeyChanges and Key Cache](https://issues.couchbase.com/browse/CBG-3432)
* [CBG-3430 - Deterministic databsae/bucket bootstrapping](https://issues.couchbase.com/browse/CBG-3430)
* [CBG-3362 - Silence metrics requests](https://issues.couchbase.com/browse/CBG-3362)
* [CBG-3361 - Add basic ping/healthcheck endpointr](https://issues.couchbase.com/browse/CBG-3361)
* [CBG-3360 - Tune console log collation buffer size when writing to a file](https://issues.couchbase.com/browse/CBG-3360)
* [CBG-3359 - Per-db console log settins](https://issues.couchbase.com/browse/CBG-3359)

### [](#known-issues-7)Known Issues

None for this release.

### [](#deprecations-7)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-1july-2023)3.1.1 — July 2023

Version 3.1.1 of Sync Gateway delivers the following features and enhancements:

### [](#maint-3-1-1)Fixed Issues

* [CBG-3143 - Investigate waiting request\_plus changes feeds not waking up for released sequence batches](https://issues.couchbase.com/browse/CBG-3143)
* [CBG-3131 - Panic during on demand import for get request](https://issues.couchbase.com/browse/CBG-3131)
* [CBG-3129 - JWTLastUpdated should only be modified when claim-based access changes](https://issues.couchbase.com/browse/CBG-3129)
* [CBG-3123 - Avoid panic in updateCalculatedStats for offline databases](https://issues.couchbase.com/browse/CBG-3123)
* [CBG-3103 - Initial OIDC setup fails for keyspace request](https://issues.couchbase.com/browse/CBG-3103)
* [CBG-3091 - Backport TestReconnectReplicator fix](https://issues.couchbase.com/browse/CBG-3091)
* [CBG-3052 - cbgt panics when setting up import feed for server versions < 7.0](https://issues.couchbase.com/browse/CBG-3052)
* [CBG-3039 - proveAttachment incompatibility between 3.0.x and 2.8.x](https://issues.couchbase.com/browse/CBG-3039)
* [CBG-3036 - Replicator will not reconnect when max\_back\_off != 0](https://issues.couchbase.com/browse/CBG-3036)
* [CBG-3033 - Import still starts when an offline database is created](https://issues.couchbase.com/browse/CBG-3033)
* [CBG-3032 - CE Import feed starting from vb highseqno instead of zero](https://issues.couchbase.com/browse/CBG-3032)
* [CBG-3030 - Panic inside Mutable1xBody for nil shallow copy](https://issues.couchbase.com/browse/CBG-3030)
* [CBG-2913 - /db/ routing does not work with default collection that coexists with named collection](https://issues.couchbase.com/browse/CBG-2913)

### [](#enhancements-8)Enhancements

* [CBG-3147 - Avoid unnecessary resync on upgrade to 3.1](https://issues.couchbase.com/browse/CBG-3147)
* [CBG-3118 - Shared bucket access=false without autoimport=false explicitly specified will panic](https://issues.couchbase.com/browse/CBG-3118)
* [CBG-3109 - Remove confusing log line about non SG indexes](https://issues.couchbase.com/browse/CBG-3109)
* [CBG-3042 - Attachment compaction code erroneously sets failOnRollback](https://issues.couchbase.com/browse/CBG-3042)
* [CBG-3041 - Streamline database creation when using many collections](https://issues.couchbase.com/browse/CBG-3041)
* [CBG-3040 - Suppress OnFeedError logging on database close](https://issues.couchbase.com/browse/CBG-3040)
* [CBG-3038 - cbgt importlistener leaves open a connection to a bucket after database is deleted](https://issues.couchbase.com/browse/CBG-3038)
* [CBG-3037 - Retry to insert config when write fails](https://issues.couchbase.com/browse/CBG-3037)
* [CBG-3034 - Improve handling for deleted collection](https://issues.couchbase.com/browse/CBG-3034)
* [CBG-3031 - Allow one-shot replications to wait for DCP to catch up on changes feed](https://issues.couchbase.com/browse/CBG-3031)
* [CBG-3023 - cbgt cluster connection fails with HTTP polling enabled and TLS disabled](https://issues.couchbase.com/browse/CBG-3023)

### [](#known-issues-8)Known Issues

None for this release.

### [](#deprecations-8)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#3-1-0april-2023)3.1.0 — April 2023

Version 3.1.0 of Sync Gateway delivers the following features and enhancements:

### [](#scopes-and-collections)Scopes and Collections

> [!CAUTION]
> Sync Gateway 3.0.x introduces some breaking changes. If you are upgrading from 2.x, please refer to the [Upgrading](upgrading.md) page. Users should be able to upgrade to 3.1.x from 3.0.x without manual intervention.

* **New support for Scopes and Collections**  
Couchbase has introduced support for Scopes and Collections for self-managed cloud-to-edge deployments only in [Couchbase Lite 3.1.0](../../couchbase-lite/current/index.md) and [Sync Gateway 3.1.0](introduction.md). This release won't cause any issues with existing apps, as it's compatible with older versions. If you have an app that uses bucket-based APIs, you can still upgrade to 3.1, but please note that this API is now deprecated. For more information, see [Scopes and Collections Configuration for Sync Gateway](scopes-and-collections-config.md).
* **Improved Data Organization and Access Control for Scopes and Collections**  
Couchbase Mobile now offers Scopes and Collections, allowing more efficient and scalable data organisation within a bucket. This also introduces an improved method of defining and enforcing data [Access Control](access-control-concepts.md) more granularly. Multi-tenant apps will also experience better scalability and independent data lifecycle management.
* **Improved metadata isolation for Scopes and Collections**  
Sync Gateway 3.1.0 has improved metadata isolation. The system data maintained by Sync Gateway is now stored in the `_default` Scope/Collection, while both the `_default` and user-defined Scope/Collection can be used for application data. For more information, examples and use cases, see [Scopes and Collections Support in Couchbase Mobile for Edge Applications](https://www.couchbase.com/blog/scopes-collections-couchbase-mobile/).
* **Collection-Level Sync Functions and Scoped User Associations**  
The [Sync Functions](sync-function.md) now work on a Collection level, and additional optional fields have been added to the database configurations to support this update. Each database is designed to support only one Scope. Users can be associated with that Scope and shared across multiple Collections.
* **Enhanced Collection Synchronization and Local Data Storage with Couchbase Lite Client**  
With Couchbase Lite client replications, you can synchronize one or multiple Collections within a specific scope. The Couchbase Lite client also will store data locally in a scope not synchronized with the remote Sync Gateway.

> [!NOTE]
> You can define 1 custom scope per database with up to 1000 custom collections. If you don't specify a custom scope and collection, any documents you create will be saved in the default scope and collection.

Read the full [3.1 release notes](release-notes.md).

### [](#maint-3-1-0)Fixed Issues

* [CBG-2731 - AccessLock not being released when a PUSH replication is ongoing](https://issues.couchbase.com/browse/CBG-2731)
* [CBG-2556 - Inefficient sequence parsing during ISGR checkpointing](https://issues.couchbase.com/browse/CBG-2556)
* [CBG-2248 - Config admin API doesn't use Etags when config comes from JSON](https://issues.couchbase.com/browse/CBG-2248)
* [CBG-2247 - Etags should be quoted](https://issues.couchbase.com/browse/CBG-2247)
* [CBG-2208 - Index compaction failing due to not found handling](https://issues.couchbase.com/browse/CBG-2208)
* [CBG-2183 - Revocation of non-existent role causes replication panic](https://issues.couchbase.com/browse/CBG-2183)
* [CBG-2174 - Periodic high response times on REST API due to persistent config polling](https://issues.couchbase.com/browse/CBG-2174)
* [CBG-2134 - Guest user is not initialised with access to public channel ("!")](https://issues.couchbase.com/browse/CBG-2134)
* [CBG-2119 - Update DisablePasswordAuth to False does not work](https://issues.couchbase.com/browse/CBG-2119)
* [CBG-2102 - Admin auth credentials not verified when using x.509 auth between SG and CBS](https://issues.couchbase.com/browse/CBG-2102)
* [CBG-2101 - User endpoint: missing first user if name\_only=false](https://issues.couchbase.com/browse/CBG-2101)
* [CBG-2065 - Update golang.org/x/text to 0.3.3+ CVE-2020-14040 in SGW 2.8.x](https://issues.couchbase.com/browse/CBG-2065)
* [CBG-2059 - HTTP logs incorrectly redact document name if the database name contains it](https://issues.couchbase.com/browse/CBG-2059)
* [CBG-2058 - Compaction w/ import and xattrs enabled can panic](https://issues.couchbase.com/browse/CBG-2058)
* [CBG-2048 - Update nhooyr.io/websocket gin-gonic/gin CVE-2020-28483](https://issues.couchbase.com/browse/CBG-2048)
* [CBG-2030 - \_user endpoint pagination causes query error](https://issues.couchbase.com/browse/CBG-2030)
* [CBG-2010 - CBL revpos handling causes attachment fetch per write for docs with attachments](https://issues.couchbase.com/browse/CBG-2010)

### [](#enhancements-9)Enhancements

* [CBG-2729 - Info-level logging when a remote webhook filter is empty](https://issues.couchbase.com/browse/CBG-2729)
* [CBG-2721 - Add a flag to sg-collect collection to delete zip once uploaded](https://issues.couchbase.com/browse/CBG-2721)
* [CBG-2689 - Add sync\_function\_exception\_count stat](https://issues.couchbase.com/browse/CBG-2689)
* [CBG-2660 - Use MaxInt64 for high sequence queries](https://issues.couchbase.com/browse/CBG-2660)
* [CBG-2559 - Move history to end of marshalled SyncData](https://issues.couchbase.com/browse/CBG-2559)
* [CBG-2510 - Docs not being tombstoned with replication DocID filter](https://issues.couchbase.com/browse/CBG-2510)
* [CBG-2450 - Leading null character in document ID causes ISGR to terminate pull replication](https://issues.couchbase.com/browse/CBG-2450)
* [CBG-2418 - Make a Runtime Database Config to explicitly track if a database is suspended](https://issues.couchbase.com/browse/CBG-2418)
* [CBG-2362 - Identify whether SG is running in persistent config mode (or not) via REST API](https://issues.couchbase.com/browse/CBG-2362)
* [CBG-2177 - Maintain long-lived bucket connections for persistent config](https://issues.couchbase.com/browse/CBG-2177)
* [CBG-2138 - Inform client they need to contact another SGW](https://issues.couchbase.com/browse/CBG-2138)
* [CBG-2137 - Support downloading meta(data) from S3 and resuming the bucket](https://issues.couchbase.com/browse/CBG-2137)
* [CBG-2136 - Support uploading meta(data) to S3 for hibernation](https://issues.couchbase.com/browse/CBG-2136)
* [CBG-2135 - Add API to stop/start access to a given bucket for hibernation](https://issues.couchbase.com/browse/CBG-2135)
* [CBG-2064 - Allow mapping OIDC claims to user roles/channels](https://issues.couchbase.com/browse/CBG-2064)
* [CBG-2047 - Update client-golang to 1.11.1+ CVE-2022-21698](https://issues.couchbase.com/browse/CBG-2047)
* [CBG-2027 - User API Enhancements - include details and limit](https://issues.couchbase.com/browse/CBG-2027)
* [CBG-2026 - Option to disable basic auth on public REST API](https://issues.couchbase.com/browse/CBG-2026)
* [CBG-2017 - Handle removed buckets in background persistent config update polling](https://issues.couchbase.com/browse/CBG-2017)
* [CBG-1969 - Support CBL clients that don't increment revpos when attachment body changes](https://issues.couchbase.com/browse/CBG-1969)

### [](#known-issues-9)Known Issues

* [CBG-798 - Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com/browse/CBG-798)

### [](#deprecations-9)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.1, see [New in 3.1](whatsnew.md).

## [](#upgrading)Upgrading

For more on upgrading — see: [Upgrading](upgrading.md)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)