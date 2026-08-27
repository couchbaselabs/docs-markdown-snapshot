---
title: Release Notes
description: Couchbase Sync Gateway
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/release-notes.adoc
  xref: xref:3.2@sync-gateway::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.2/release-notes.html)

# Release Notes

Quicklinks

[Release 3.1](../3.1/release-notes.md) | [Release 3.0](../3.0/release-notes.md) | [Release 2.8](#2.8@sync-gateway::release-notes.adoc) | [Archived documentation](https://docs-archive.couchbase.com/home/index.html)

> Couchbase Sync Gateway  
> This content describes the key features and changes implemented by release 3.2.6 of Couchbase Sync Gateway

> [!CAUTION]
> One Way Upgrade
> 
> The migration to 3.x configuration is a ONE WAY process — see: [Upgrading](upgrading.md) for more.

## [](#maint-latest)3.2.8 — June 2026

> [!IMPORTANT]
> If you use OIDC-based authentication for deployments and manage users through the Sync Gateway Admin REST API, upgrade to this release to receive critical fixes.

### [](#maint-3-2-8)Fixed Issues

* [CBG-5008 — /\_ping (and all endpoints) acquire ServerContext.lock.RLock and blocks if the write lock is acquired](https://jira.issues.couchbase.com/browse/CBG-5008)

### [](#enhancements)Enhancements

None for this release.

### [](#known-issues)Known Issues

None for this release.

### [](#deprecations)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-7november-2025)3.2.7 — November 2025

### [](#maint-3-2-7)Fixed Issues

* [CBG-4940 - SG 3.x erroneously reports it can support Version Vector replication (affects CBL and ISGR >= v4)](https://jira.issues.couchbase.com/browse/CBG-4940)
* [CBG-4694 - calling GET /db/\_session/sessionID returns invalidated session](https://jira.issues.couchbase.com/browse/CBG-4694)

### [](#enhancements-2)Enhancements

* [CBG-4971 - Allow cookieless authentication from cbl-js](https://jira.issues.couchbase.com/browse/CBG-4971)

### [](#known-issues-2)Known Issues

None for this release.

### [](#deprecations-2)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-6july-2025)3.2.6 — July 2025

### [](#maint-3-2-6)Fixed Issues

* Improved sgcollect execution and output

### [](#enhancements-3)Enhancements

None for this release.

### [](#known-issues-3)Known Issues

None for this release.

### [](#deprecations-3)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-5june-2025)3.2.5 — June 2025

### [](#maint-3-2-5)Fixed Issues

* [CBG-4620 - Documents created with \_attachments property in value fail to sync](https://jira.issues.couchbase.com/browse/CBG-4620)
* [CBG-4655 - Server MgmtRequest panics on request failure](https://jira.issues.couchbase.com/browse/CBG-4655)
* [CBG-4663 - Resync performance degrades over time](https://jira.issues.couchbase.com/browse/CBG-4663)

### [](#enhancements-4)Enhancements

* [CBG-4656 - Include the blip correlation ID in go-blip logging](https://jira.issues.couchbase.com/browse/CBG-4656)
* [CBG-4659 - Prevent JavaScript stack overflow](https://jira.issues.couchbase.com/browse/CBG-4659)

### [](#known-issues-4)Known Issues

None for this release.

### [](#deprecations-4)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-4april-2025)3.2.4 — April 2025

### [](#maint-3-2-4)Fixed Issues

* [CBG-4325 - sgcollect\_info: logs duplicated or repeated](https://jira.issues.couchbase.com/browse/CBG-4325)
* [CBG-4382 - Empty files for high memory heap profiles](https://jira.issues.couchbase.com/browse/CBG-4382)
* [CBG-4537 - ISGR fatal connection errors leak a stats reporter goroutine](https://jira.issues.couchbase.com/browse/CBG-4537)
* [CBG-4571 - Audit events for database audit are enabled when no per-db audit logging config is set](https://jira.issues.couchbase.com/browse/CBG-4571)
* [CBG-4573 - Blip leaks nextFrameToSend goroutines if non ack'd messages are queued](https://jira.issues.couchbase.com/browse/CBG-4573)
* [CBG-4598 - Caching DCP feed does not utilize network connstr option](https://jira.issues.couchbase.com/browse/CBG-4598)

### [](#enhancements-5)Enhancements

* [CBG-4189 - Add metric for Assertions](https://jira.issues.couchbase.com/browse/CBG-4189)
* [CBG-4543 - Avoid retention of DCP sync.Pool instances during import processing](https://jira.issues.couchbase.com/browse/CBG-4543)
* [CBG-4551 - Skip revcache insertion on import operations](https://jira.issues.couchbase.com/browse/CBG-4551)
* [CBG-4583 - Upper bound on number of sequences to release for nextSequenceGreaterThan](https://jira.issues.couchbase.com/browse/CBG-4583)
* [CBG-4590 - New stat for value of last sequence allocated (or batched) by SG node](https://jira.issues.couchbase.com/browse/CBG-4590)

### [](#known-issues-5)Known Issues

None for this release.

### [](#deprecations-5)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-3march-2025)3.2.3 — March 2025

### [](#maint-3-2-3)Fixed Issues

* [CBG-4198 - ISGR replicators reaching max\_backoff with a reconnection error will not transition to stop](https://jira.issues.couchbase.com/browse/CBG-4198)
* [CBG-4463 - Leaking/duplicate status reporters across ISGR reconnection can cause 409 conflcts](https://jira.issues.couchbase.com/browse/CBG-4463)
* [CBG-4374 - http continuous changes requests no longer flush output](https://jira.issues.couchbase.com/browse/CBG-4374)
* [CBG-4425 - Resync collections processing is nil while no documents have been processed](https://jira.issues.couchbase.com/browse/CBG-4425)
* [CBG-4446 - changes feed error will not cause blip clients to disconnect](https://jira.issues.couchbase.com/browse/CBG-4446)
* [CBG-4517 - Support bucket names containing . character](https://jira.issues.couchbase.com/browse/CBG-4517)

### [](#enhancements-6)Enhancements

* [CBG-4314 - Release unused sequences in db.UpdatePrincipal](https://jira.issues.couchbase.com/browse/CBG-4314)
* [CBG-4342 - Add createdAt / updatedAt timestamps to written configs](https://jira.issues.couchbase.com/browse/CBG-4342)
* [CBG-4368 - Retain minimum number of recent sequences during compaction](https://jira.issues.couchbase.com/browse/CBG-4368)
* [CBG-4377 - Create unsupported option for sending change in a channel filter on channel filter removal](https://jira.issues.couchbase.com/browse/CBG-4377)
* [CBG-4392 - Provide cluster uuid at a top level endpoint](https://jira.issues.couchbase.com/browse/CBG-4392)
* [CBG-4393 - Improve observability of errors where collection has been deleted](https://jira.issues.couchbase.com/browse/CBG-4393)
* [CBG-4464 - Increase index creation retry time](https://jira.issues.couchbase.com/browse/CBG-4464)
* [CBG-4465 - Add a stat to track the amount of errors that happen when trying to bring a database online](https://jira.issues.couchbase.com/browse/CBG-4465)
* [CBG-4476 - Uptake GOCBC-1659 panic fix](https://jira.issues.couchbase.com/browse/CBG-4476)
* [CBG-4515 - Improve observability errors for online processes](https://jira.issues.couchbase.com/browse/CBG-4515)

### [](#known-issues-6)Known Issues

None for this release.

### [](#deprecations-6)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-2february-2025)3.2.2 — February 2025

### [](#maint-3-2-2)Fixed Issues

* [CBG-4310 - Missing cbgt janitor kick in cbgt rollback.](https://jira.issues.couchbase.com/browse/CBG-4310)
* [CBG-4398 - Restore single entry skipped sequence list.](https://jira.issues.couchbase.com/browse/CBG-4398)
* [CBG-4436 - Count scheduled compaction runs as idle KV/Query ops.](https://jira.issues.couchbase.com/browse/CBG-4436)
* [CBG-4482 - Db state is stuck in starting after failure in StartOnlineProcesses.](https://jira.issues.couchbase.com/browse/CBG-4482)
* [CBG-4488 - Deadlock in revision cache with Get and a demand import.](https://jira.issues.couchbase.com/browse/CBG-4488)
* [CBG-4495 - Skip revcache insertion for on-demand imports.](https://jira.issues.couchbase.com/browse/CBG-4495)

### [](#enhancements-7)Enhancements

None for this release.

### [](#known-issues-7)Known Issues

None for this release.

### [](#deprecations-7)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-1october-2024)3.2.1 — October 2024

### [](#maint-3-2-1)Fixed Issues

* [CBG-4075 - Timeout error will release document sequence as unused](https://jira.issues.couchbase.com/browse/CBG-4075)
* [CBG-4089 - Make config polling more resilient to timeout errors](https://jira.issues.couchbase.com/browse/CBG-4089)
* [CBG-4165 - rotated\_logs\_size\_limit not used by ConsoleLogger's FileOutput](https://jira.issues.couchbase.com/browse/CBG-4165)
* [CBG-4243 - Default log file permissions changed from 644 to 600](https://jira.issues.couchbase.com/browse/CBG-4243)

### [](#enhancements-8)Enhancements

* [CBG-3825 - Memory-based rev cache size](https://jira.issues.couchbase.com/browse/CBG-3825)
* [CBG-4150 - Index optimizations for large number of collections](https://jira.issues.couchbase.com/browse/CBG-4150)
* [CBG-4151 - Memory-based rev cache size tuning](https://jira.issues.couchbase.com/browse/CBG-4151)
* [CBG-4170 - Stat for rev cache current capacity](https://jira.issues.couchbase.com/browse/CBG-4170)
* [CBG-4174 - Force disconnection of blip clients on database close](https://jira.issues.couchbase.com/browse/CBG-4174)
* [CBG-4176 - Improved Auth Failed Logging](https://jira.issues.couchbase.com/browse/CBG-4176)
* [CBG-4190 - Add metrics related to audit logging](https://jira.issues.couchbase.com/browse/CBG-4190)
* [CBG-4196 - Check for context cancellation in buildRevokedFeed if no docs require revocation](https://jira.issues.couchbase.com/browse/CBG-4196)
* [CBG-4201 - Add missing logging for ChangesOptions for Changes requests](https://jira.issues.couchbase.com/browse/CBG-4201)
* [CBG-4294 - Resolve pattern matching for rocky and alma linux to fall into rhel pathways](https://jira.issues.couchbase.com/browse/CBG-4294)

### [](#known-issues-8)Known Issues

None for this release.

### [](#deprecations-8)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

## [](#3-2-0september-2024)3.2.0 — September 2024

> [!WARNING]
> Do not deploy Eventing/Sync Gateway until all SGW nodes are at version 3.2\. For older Sync Gateway versions that do not write import XATTRs, Eventing functions may encounter infinite recursions and duplicate mutations if deployed in a mixed mode SGW environment. This can only happen during a mixed mode of SGW with a 3.2 version and an older version during an upgrade and a new Eventing/Sync Gateway function is deployed.

### [](#audit-logging-for-sync-gateway)Audit Logging for Sync Gateway

Couchbase now provides Audit Logging support for Sync Gateway. Audit Logging provides tools for administrators to track operational irregularities and to support regulatory and security compliance standards.

For more information on new features and enhancements in this release, see [New In 3.2](whatsnew.md).

Version 3.2.0 of Sync Gateway also delivers the following features and enhancements:

### [](#maint-3-2-0)Fixed Issues

* [CBG-2905 - Fixed repeated attempts to connect to inexistent buckets are done after removing a database and bucket](https://jira.issues.couchbase.com/browse/CBG-2905)
* [CBG-2909 - Fixed import still starts when an offline database is created](https://jira.issues.couchbase.com/browse/CBG-2909)
* [CBG-2911 - Fixed /db/ routing does not work with default collection that coexists with named collection](https://jira.issues.couchbase.com/browse/CBG-2911)
* [CBG-2944 - Fixed proveAttachment incompatibility between 3.0.x and 2.8.x](https://jira.issues.couchbase.com/browse/CBG-2944)
* [CBG-2973 - Fixed Panic inside Mutable1xBody for nil shallow copy](https://jira.issues.couchbase.com/browse/CBG-2973)
* [CBG-2983 - Fixed cbgt importlistener leaves open a connection to a bucket after database is deleted](https://jira.issues.couchbase.com/browse/CBG-2983)
* [CBG-2998 - Fixed cbgt cluster connection fails with HTTP polling enabled and TLS disabled](https://jira.issues.couchbase.com/browse/CBG-2998)
* [CBG-3022 - Fixed replicator will not reconnect when max\_back\_off != 0](https://jira.issues.couchbase.com/browse/CBG-3022)
* [CBG-3024 - Fixed CE Import feed starting from vb highseqno instead of zero](https://jira.issues.couchbase.com/browse/CBG-3024)
* [CBG-3043 - Fixed cbgt panics when setting up import feed for server versions < 7.0](https://jira.issues.couchbase.com/browse/CBG-3043)
* [CBG-3102 - Fixed initial OIDC setup fails for keyspace request](https://jira.issues.couchbase.com/browse/CBG-3102)
* [CBG-3195 - Fixed simultaneous role grant + subChanges will cause role grant to not be recognized](https://jira.issues.couchbase.com/browse/CBG-3195)
* [CBG-3196 - Fixed cannot update db config from implicit \_default scope to explicit \_default scope](https://jira.issues.couchbase.com/browse/CBG-3196)
* [CBG-3553 - Fixed increasing memory usage when failing to apply a database config from the bucket](https://jira.issues.couchbase.com/browse/CBG-3553)
* [CBG-3688 - Fixed kv\_pool\_size on import feed can be non zero](https://jira.issues.couchbase.com/browse/CBG-3688)
* [CBG-3817 - Fixed collection appears to be linked to 2 DBs after update error](https://jira.issues.couchbase.com/browse/CBG-3817)
* [CBG-3820 - Drop logging volume for pending insertions and doc not found logging](https://jira.issues.couchbase.com/browse/CBG-3820)
* [CBG-3835 - Tweak logging around import of JSON but not JSON object docs](https://jira.issues.couchbase.com/browse/CBG-3835)
* [CBG-3844 - updateSeq must happen after DCP callback invocation](https://jira.issues.couchbase.com/browse/CBG-3844)
* [CBG-3856 - Fixed GET /db RBAC permissions missing for Sync Gateway Architect](https://jira.issues.couchbase.com/browse/CBG-3856)
* [CBG-3867 - Prevent ISGR creation with empty ID](https://jira.issues.couchbase.com/browse/CBG-3867)
* [CBG-3869 - Fixed UnmarshalDocumentSyncDataFromFeed doesn't return any present user xattrs if sync data doesn't exist on the doc](https://jira.issues.couchbase.com/browse/CBG-3869)
* [CBG-3882 - Fixed sgcollect\_info fails to upload to s3](https://jira.issues.couchbase.com/browse/CBG-3882)
* [CBG-3883 - Fixed OIDC-auth causes admin\_channels/admin\_roles loss](https://jira.issues.couchbase.com/browse/CBG-3883)
* [CBG-3888 - Fixed sgcollect\_info TypeError when task execution timeout occurs](https://jira.issues.couchbase.com/browse/CBG-3888)
* [CBG-3920 - Fixed not found handling for DCP purge](https://jira.issues.couchbase.com/browse/CBG-3920)
* [CBG-3941 - Avoid timeout on creating indexes asynchronously](https://jira.issues.couchbase.com/browse/CBG-3941)
* [CBG-3950 - Fixed database with default db can see users matching other databases in the bucket](https://jira.issues.couchbase.com/browse/CBG-3950)
* [CBG-3968 - Include scope with collections in resync status](https://jira.issues.couchbase.com/browse/CBG-3968)
* [CBG-3988 - Fixed documents may not be imported when collection added to an existing db](https://jira.issues.couchbase.com/browse/CBG-3988)
* [CBG-3996 - Fixed sgcollect doesn't work on mac distributions](https://jira.issues.couchbase.com/browse/CBG-3996)
* [CBG-4003 - Fixed DeleteRole doesnt trigger history calculation for named collections](https://jira.issues.couchbase.com/browse/CBG-4003)
* [CBG-4015 - Fixed nextSequenceGreaterThan should update to current \_sync:seq before releasing sequences](https://jira.issues.couchbase.com/browse/CBG-4015)
* [CBG-4025 - Fixed users roles are not getting invalidated after a resync](https://jira.issues.couchbase.com/browse/CBG-4025)
* [CBG-4055 - Fixed incorrect types listed in API docs for all\_docs query parameters](https://jira.issues.couchbase.com/browse/CBG-4055)
* [CBG-4070 - Fixed panic in CheckpointHash function for bucket UUID call](https://jira.issues.couchbase.com/browse/CBG-4070)
* [CBG-4105 - Fixed corrupt DB config handling doesn't remove the config when longer present in the bucket](https://jira.issues.couchbase.com/browse/CBG-4105)
* [CBG-4106 - Fixed if we error in removeCorruptConfigIfExists we don't unload/remove database](https://jira.issues.couchbase.com/browse/CBG-4106)
* [CBG-4128 - Decouple client request context from lazy-init OIDC discovery sync process](https://jira.issues.couchbase.com/browse/CBG-4128)
* [CBG-4136 - API Docs: Limit scopes configuration to only one entry](https://jira.issues.couchbase.com/browse/CBG-4136)
* [CBG-4221 - Pending unused sequences shouldn't update high cache sequence](https://jira.issues.couchbase.com/browse/CBG-4221)
* [CBG-4218 - Fixed duplicated sequences can cause SGW to be unresponsive](https://jira.issues.couchbase.com/browse/CBG-4218)

### [](#enhancements-9)Enhancements

* [CBG-2807 - Allow DB Scoped CORS config](https://jira.issues.couchbase.com/browse/CBG-2807)
* [CBG-2837 - Streamline database creation when using many collections](https://jira.issues.couchbase.com/browse/CBG-2837)
* [CBG-2853 - Allow one-shot replications to wait for DCP to catch up on changes feed](https://jira.issues.couchbase.com/browse/CBG-2853)
* [CBG-2895 - Add replication connection limit](https://jira.issues.couchbase.com/browse/CBG-2895)
* [CBG-2898 - Add num\_replications\_rejected\_limit stat for replication connection limit](https://jira.issues.couchbase.com/browse/CBG-2898)
* [CBG-2904 - Retry to insert config when write fails](https://jira.issues.couchbase.com/browse/CBG-2904)
* [CBG-2927 - Add total\_sync\_time stat](https://jira.issues.couchbase.com/browse/CBG-2927)
* [CBG-2929 - Add public\_rest\_bytes\_written stat](https://jira.issues.couchbase.com/browse/CBG-2929)
* [CBG-2932 - Add num\_public\_rest\_requests stat](https://jira.issues.couchbase.com/browse/CBG-2932)
* [CBG-2938 - Suppress OnFeedError logging on database close](https://jira.issues.couchbase.com/browse/CBG-2938)
* [CBG-2977 - Improve handling for deleted collection](https://jira.issues.couchbase.com/browse/CBG-2977)
* [CBG-3101 - Use Scope().Query() for N1QL in cases where CB Server supports it](https://jira.issues.couchbase.com/browse/CBG-3101)
* [CBG-3157 - Improve handling for docs mutated during one-shot replication](https://jira.issues.couchbase.com/browse/CBG-3157)
* [CBG-3163 - Add public\_rest\_bytes\_read stat](https://jira.issues.couchbase.com/browse/CBG-3163)
* [CBG-3520 - Updating import\_filter and sync\_filter to empty string does not work for named collection](https://jira.issues.couchbase.com/browse/CBG-3520)
* [CBG-3537 - Reduce EOF logging from go-blip](https://jira.issues.couchbase.com/browse/CBG-3537)
* [CBG-3563 - Automatic profile collection when exceeding memory thresholds](https://jira.issues.couchbase.com/browse/CBG-3563)
* [CBG-3585 - Log bucket and groupID during config search](https://jira.issues.couchbase.com/browse/CBG-3585)
* [CBG-3613 - docker: switch current working directory to a writeable directory](https://jira.issues.couchbase.com/browse/CBG-3613)
* [CBG-3640 - Change default SG config to use persistent config](https://jira.issues.couchbase.com/browse/CBG-3640)
* [CBG-3696 - Empty user\_xattr\_key doesnt clear db config field](https://jira.issues.couchbase.com/browse/CBG-3696)
* [CBG-3768 - Avoid writing back the document body during import unless required](https://jira.issues.couchbase.com/browse/CBG-3768)
* [CBG-3780 - Additional Platform Support](https://jira.issues.couchbase.com/browse/CBG-3780)
* [CBG-3795 - Deprecate enable\_star\_channel config option](https://jira.issues.couchbase.com/browse/CBG-3795)
* [CBG-3813 - sgcollect windows now collects stderr / stdout](https://jira.issues.couchbase.com/browse/CBG-3813)
* [CBG-3819 - Declare VOLUME in dockerfile](https://jira.issues.couchbase.com/browse/CBG-3819)
* [CBG-3822 - Audit Logging](https://jira.issues.couchbase.com/browse/CBG-3822)
* [CBG-3823 - Warn when releasing a large number of unused sequences](https://jira.issues.couchbase.com/browse/CBG-3823)
* [CBG-3824 - Optimize storage of skipped sequences](https://jira.issues.couchbase.com/browse/CBG-3824)
* [CBG-3837 - Don't perform per-document logging when processing an unused sequence range](https://jira.issues.couchbase.com/browse/CBG-3837)
* [CBG-3839 - Detect and handle \_sync:seq rollback in sequence allocator](https://jira.issues.couchbase.com/browse/CBG-3839)
* [CBG-3843 - Include collection set in resync status](https://jira.issues.couchbase.com/browse/CBG-3843)
* [CBG-3847 - Log \_sync:seq on database start](https://jira.issues.couchbase.com/browse/CBG-3847)
* [CBG-3849 - Recovery from cas mismatch on metadata documents when using xattrConfig](https://jira.issues.couchbase.com/browse/CBG-3849)
* [CBG-3850 - Optimise releaseUnusedSequenceRange](https://jira.issues.couchbase.com/browse/CBG-3850)
* [CBG-3857 - log DB starting in http status message 503](https://jira.issues.couchbase.com/browse/CBG-3857)
* [CBG-3896 - Compatibility enhancements for eventing source bucket mutations](https://jira.issues.couchbase.com/browse/CBG-3896)
* [CBG-3905 - Logging for GetDatabaseConfigs verbose and ambiguous](https://jira.issues.couchbase.com/browse/CBG-3905)
* [CBG-3925 - Add log rotation interval](https://jira.issues.couchbase.com/browse/CBG-3925)
* [CBG-3938 - sgcollect\_info: Switch to runtime config endpoint to determine logFilePath](https://jira.issues.couchbase.com/browse/CBG-3938)
* [CBG-3942 - Provide bucket and collection when returning an error about inability to create collections](https://jira.issues.couchbase.com/browse/CBG-3942)
* [CBG-3957 - Add a reason for why a database is offline in /\_all\_dbs](https://jira.issues.couchbase.com/browse/CBG-3957)
* [CBG-3960 - Add stats for norev and replacement rev replication messages](https://jira.issues.couchbase.com/browse/CBG-3960)
* [CBG-3962 - Do not regenerate principal seqs unless resync is running on default collection](https://jira.issues.couchbase.com/browse/CBG-3962)
* [CBG-3963 - Check/wait for principal doc index readiness in resync w/ regenerate sequences](https://jira.issues.couchbase.com/browse/CBG-3963)
* [CBG-4013 - Removal of per collection rev cache](https://jira.issues.couchbase.com/browse/CBG-4013)
* [CBG-4019 - Add initialization active property to DbSummary](https://jira.issues.couchbase.com/browse/CBG-4019)
* [CBG-4027 - Failure to perform on-demand import should result in not found/noRev](https://jira.issues.couchbase.com/browse/CBG-4027)
* [CBG-4072 - Uptake gocb enhancement to lower config mismatch logging to debug](https://jira.issues.couchbase.com/browse/CBG-4072)
* [CBG-4074 - update to golang.org/x/crypto:v0.25.0](https://jira.issues.couchbase.com/browse/CBG-4074)
* [CBG-4163 - Log the origin of setting metadata ID when updating a dbconfig](https://jira.issues.couchbase.com/browse/CBG-4163)
* [CBG-4172 - Improve "could not verify JWT" error logging](https://jira.issues.couchbase.com/browse/CBG-4172)

### [](#known-issues-9)Known Issues

None for this release.

### [](#deprecations-9)Deprecations

* [CBG-3795 - Deprecate enable\_star\_channel config option](https://jira.issues.couchbase.com/browse/CBG-3795)

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.2, see [New in 3.2](whatsnew.md).

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