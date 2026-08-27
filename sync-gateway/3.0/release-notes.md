---
title: Release Notes
description: Couchbase Sync Gateway
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/release-notes.adoc
  xref: xref:3.0@sync-gateway::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/release-notes.html)

# Release Notes

Quicklinks

[Release 2.8](#2.8@sync-gateway::release-notes.adoc) | [Release 2.7](#2.7@sync-gateway::release-notes.adoc) | [Release 2.6](#2.6@sync-gateway::release-notes.adoc) | [Release 2.5](#2.5@sync-gateway::release-notes.adoc) | [Release 2.1](#2.1@sync-gateway::release-notes.adoc) | [Release 2.0](#2.0@sync-gateway::release-notes.adoc)

> Couchbase Sync Gateway  
> This content describes the key features and changes implemented by release 3.0.0 of Couchbase Sync Gateway

> [!CAUTION]
> One Way Upgrade
> 
> The migration to 3.0 configuration is a ONE WAY process — see: [Upgrading](upgrading.md) for more.

## [](#maint-3-0-9)3.0.9 — Oct 2023

### [](#enhancements)Enhancements

* [CBG-3431 -- Deterministic database/bucket bootstrapping ](https://issues.couchbase.com/browse/CBG-3431)
* [CBG-3428 -- Enforce "bucket" field match in DbConfig](https://issues.couchbase.com/browse/CBG-3428)
* [CBG-3409 -- Add basic ping/healthcheck endpoint ](https://issues.couchbase.com/browse/CBG-3409)
* [CBG-3407 -- Tune console log collation buffer size when writing to a file](https://issues.couchbase.com/browse/CBG-3407)

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBG-3477 -- warning when client's maxHistory for a rev is exceeded on push](https://issues.couchbase.com/browse/CBG-3477)
* [CBG-3415 -- Replicator will not reconnect when max\_back\_off != 0](https://issues.couchbase.com/browse/CBG-3415)
* [CBG-3412 -- Panic inside Mutable1xBody for nil shallow copy](https://issues.couchbase.com/browse/CBG-3412)
* [CBG-3406 -- Hook up the reset resync code to a parameter that is passed into the resync endpoint](https://issues.couchbase.com/browse/CBG-3406)
* [CBG-3240 -- Explicit check on xattr length to avoid panics](https://issues.couchbase.com/browse/CBG-3240)
* [CBG-3239 -- Revocation feed errors cause MultiChangesFeed to close ](https://issues.couchbase.com/browse/CBG-3239)

#### [](#known-issues)Known Issues

None for this release

#### [](#deprecations)Deprecations

None for this release

## [](#maint-3-0-8)3.0.8 — June 2023

### [](#enhancements-2)Enhancements

* [CBG-2855 -- 3.0.8 Oneshot replications should wait for DCP to catch up on changes feed](https://issues.couchbase.com/browse/CBG-2855)

### [](#issues-and-resolutions-2)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

* [CBG-2968 -- 3.0.8 proveAttachment incompatibility between 3.0.x and 2.8.x](https://issues.couchbase.com/browse/CBG-2968)

#### [](#known-issues-2)Known Issues

None for this release

## [](#maint-3-0-5)3.0.5 — February 2023

### [](#enhancements-3)Enhancements

* [ CBG-2673 -- Upgrade Go to 1.19 ](https://issues.couchbase.com/browse/CBG-2673)
* [ CBG-2674 -- Upgrade golang.org/x/text to latest version ](https://issues.couchbase.com/browse/CBG-2674)
* [ CBG-2700 -- Use MaxInt64 for high sequence queries ](https://issues.couchbase.com/browse/CBG-2700)
* [ CBG-2608 -- Update websocket implementation ](https://issues.couchbase.com/browse/CBG-2608)
* [ CBG-2610 -- Lower log level for expected BLIP websocket close errors ](https://issues.couchbase.com/browse/CBG-2610)

### [](#issues-and-resolutions-3)Issues and Resolutions

#### [](#fixed-issues-3)Fixed Issues

* [ CBG-2705 -- ISGR Sequence checkpointing maintains unnessesary entries ](https://issues.couchbase.com/browse/CBG-2705)
* [ CBG-2707 -- Compact expected/processed when safe seq unchanged ](https://issues.couchbase.com/browse/CBG-2707)
* [ CBG-2612 -- Performance decrease in Replicate and SGReplicate tests ](https://issues.couchbase.com/browse/CBG-2612)
* [ CBG-2614 -- E2E Push: websocket reset by peer ](https://issues.couchbase.com/browse/CBG-2614)
* [ CBG-2591 -- Inefficient sequence parsing during ISGR checkpointing ](https://issues.couchbase.com/browse/CBG-2591)
* [ CBG-2601 -- ISGR processedSeqs/expectedSeq mismatch based on JSON string ](https://issues.couchbase.com/browse/CBG-2601)
* [ CBG-2602 -- Anonymous read-only access should support pull replications ](https://issues.couchbase.com/browse/CBG-2602)
* [ CBG-2708 -- GetAttachment rev processing race ](https://issues.couchbase.com/browse/CBG-2708)

#### [](#known-issues-3)Known Issues

* [ CBG-798 -- Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com/browse/CBG-798)

## [](#3-0-4october-2022)3.0.4 — October 2022

### [](#maint-3-0-4)Enhancements

* [CBG-2468 \[3.0.4 Backport\] Maintain long-lived bucket connections for persistent config](https://issues.couchbase.com/browse/CBG-2468)
* [CBG-2467 \[3.0.4 Backport\] Update UserHasDocAccess to check most recent rather than rev](https://issues.couchbase.com/browse/CBG-2467)
* [CBG-2225 \[Backport 3.0.4\] Add cluster aware functionality to resync operation](https://issues.couchbase.com/browse/CBG-2225)

### [](#issues-and-resolutions-4)Issues and Resolutions

#### [](#fixed-issues-4)Fixed Issues

* [CBG-2448 \[3.0.4 Backport\] Background manager cluster aware terminator race condition](https://issues.couchbase.com/browse/CBG-2448)
* [CBG-2419 \[3.0.4 Backport\] Reloading the database while it has a replicator defined on it causes a panic](https://issues.couchbase.com/browse/CBG-2419)
* [CBG-2231 \[3.0.4 Backport\] SGW panics on startup with mutual TLS enabled and invalid bootstrap config](https://issues.couchbase.com/browse/CBG-2231)
* [CBG-2209 \[3.0.4 backport\] Index compaction failing due to not found handling](https://issues.couchbase.com/browse/CBG-2209)
* [CBG-2202 Backport - Create User: Key length exceeds 251](https://issues.couchbase.com/browse/CBG-2202)
* [CBG-2186 \[3.0.4 Backport\] Revocation of non-existent role causes replication panic](https://issues.couchbase.com/browse/CBG-2186)
* [CBG-2179 \[3.0.4 Backport\] Periodic high response times on REST API due to persistent config polling](https://issues.couchbase.com/browse/CBG-2179)

#### [](#known-issues-4)Known Issues

* [CBG-798 Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com/browse/CBG-798)

## [](#maint-3-0-3)3.0.3 — June 2022

Version 3.0.3 of sync gateway delivers a number of fixes and enhancements. .Version 3.0.3 replaces v3.0.0

> [!IMPORTANT]
> This version of sync gateway includes fixes for several critical issues from v3.0.0\. Therefore v3.0.0 is replaced by v3.0.3\. If you are using v3.0.0 we strongly recommend upgrading to v3.0.3.

### [](#enhancements-4)Enhancements

* [CBG-2032 Prevent use of internal underscore properties](https://issues.couchbase.com/browse/CBG-2032)
* [CBG-2035 Handle removed buckets in background persistent config update polling](https://issues.couchbase.com/browse/CBG-2035)
* [CBG-2069 Support CBL clients that don't increment revpos when attachment body changes](https://issues.couchbase.com/browse/CBG-2069)
* [CBG-2078 Option to make GUEST access read-only](https://issues.couchbase.com/browse/CBG-2078)

### [](#issues-and-resolutions-3-0-3)Issues and Resolutions

#### [](#fixed-issues-5)Fixed Issues

* [CBG-1953 Console logging not being enabled when only a log key set](https://issues.couchbase.com/browse/CBG-1953)
* [CBG-1996 Implementation for supporting top-level properties with an underscore prefix](https://issues.couchbase.com/browse/CBG-1996)
* [CBG-1998 Fix race condition caused when getting user roles](https://issues.couchbase.com/browse/CBG-1998)
* [CBG-1999 Unable to upsert replication config username or password independently](https://issues.couchbase.com/browse/CBG-1999)
* [CBG-2000 One shot sub changes request does not decrement NumPullReplActiveOneShot stat when completed](https://issues.couchbase.com/browse/CBG-2000)
* [CBG-2011 CBL revpos handling causes attachment fetch per write for docs with attachments](https://issues.couchbase.com/browse/CBG-2011)
* [CBG-2011 \_user endpoint pagination causes query error](https://issues.couchbase.com/browse/CBG-2031)
* [CBG-2055 Mutating a document with an attachment on over CBL causes the attachment to be deleted from the bucket](https://issues.couchbase.com/browse/CBG-2055)
* [CBG-2072 crc32c values with leading zeros trigger unnecessary import](https://issues.couchbase.com/browse/CBG-2072)

## [](#lbl-rel300)Release 3.0.0 — February 2022

Quicklinks

[New Features](#new-features-300) **|** [Enhancements](#improvements-300) **|** [Issues and Resolutions](#issues-and-resolutions-300) **|** [Support Notices](#support-notices-300)

> [!IMPORTANT]
> Replaced by v3.0.3
> 
> Version 3.0.3 includes fixes for several critical issues found in 3.0.0\. Therefore v3.0.0 is replaced by v3.0.3\. We strongly encourage upgrading to v3.0.3.

### [](#new-features-300)New Features

#### [](#centralized-persistent-modular-configuration)Centralized Persistent Modular Configuration

_Centralized Persistent Modular Configuration is a core enhancement that makes it simpler for administrators to configure and manage the Sync Gateway._

This enhancement removes reliance on monolithic JSON configuration files whilst providing a modular and _cluster-aware_ approach to Sync Gateway node configuration.

Basic startup configuration settings bootstrap your Sync Gateway nodes and securely connect them to a Couchbase Server. Configuration of cluster-wide Sync Gateway databases, access control policies and inter-Sync Gateway replications is then provided using the Admin REST API.

[Read More …​](whatsnew.md#centralized-persistent-modular-configuration)

#### [](#secure-administration)Secure Administration

_This major enhancement complements the introduction of the centralized persistent configuration by introducing secure administration of a cluster through the Admin REST API._

The Admin REST API now enforces authentication and role-based access control by default.

[Read More …​](whatsnew.md#secure-administration)

#### [](#tls-encryption-enabled-by-default)TLS Encryption Enabled by Default

_The default enabling of secure TLS connections for all Couchbase Server,side communication ensures that all such communication is encrypted; enforcing and encouraging security best practices._

[Read More …​](whatsnew.md#tls-encryption-enabled-by-default)

#### [](#user-defined-extended-attributesxattrs-for-access-control)User Defined Extended Attributes(XAttrs) for Access Control

_Use extended attributes (metadata) to avoid the need to embed sensitive access grant information such as channels and roles within document bodies._

This key architectural enhancement enforces separation of concerns by providing you the option to use Extended Attributes (XATTRs) to specify channel access grants outside of your document bodies.

[Read More …​](whatsnew.md#user-defined-extended-attributesxattrs-for-access-control)

#### [](#auto-purge-on-channel-access-revocation-in-inter-sync-gateway-replication)Auto-Purge on Channel Access Revocation in Inter-Sync Gateway Replication

_This enhancement to inter-Sync Gateway replication technology helps with the enforcement of data privacy and governance in complex workflows._

[Read More …​](whatsnew.md#auto-purge-on-channel-access-revocation-in-inter-sync-gateway-replication)

#### [](#use-environment-variables-in-configuration-file)Use Environment Variables in Configuration File

Sync Gateway configuration is extended to allow the use of defined _environment variables_ as substitution values inside the configuration file. This allows users to determine, pick-up and substitute appropriate values during Sync Gateway start-up.

[Read More …​](whatsnew.md#use-environment-variables-in-configuration-file)

### [](#improvements-300)Enhancements

#### [](#compacting)Compacting

Attachments added post 3.0 are automatically removed from the bucket upon reference removal, document delete or document purge.  
The [{db}/\_compact](rest-api-admin.md#/Database%5FManagement/post%5F%5Fdb%5F%5F%5Fcompact) API includes an option to remove any redundant pre-3.0 attachments — see: [Revisions — Compacting](revisions.md#compacting).

#### [](#resync)Resync

The `_resync` process has been enhanced to better handle large datasets, minimizing timeout and out-of-memory issues. The process now runs asynchronously, uses query pagination and supports sequence regeneration.

#### [](#other-enhancements)Other Enhancements

* [CBG-1760](https://issues.couchbase.com//browse/CBG-1760) — [Error upfront when the configured logFilePath is not writable](https://issues.couchbase.com//browse/CBG-1760)
* [CBG-1705](https://issues.couchbase.com//browse/CBG-1705) — [Release 'view op' on results close](https://issues.couchbase.com//browse/CBG-1705)
* [CBG-1672](https://issues.couchbase.com//browse/CBG-1672) — [Return 422 status for unprocessible deltas instead of 404 to use non-delta retry handling](https://issues.couchbase.com//browse/CBG-1672)
* [CBG-1664](https://issues.couchbase.com//browse/CBG-1664) — [Validate javascript syntax in DbConfig.validate()](https://issues.couchbase.com//browse/CBG-1664)
* [CBG-1643](https://issues.couchbase.com//browse/CBG-1643) — [Add additional context for gocb errors when using self-signed cert](https://issues.couchbase.com//browse/CBG-1643)
* [CBG-1590](https://issues.couchbase.com//browse/CBG-1590) — [Retrieve existing doc metadata prior to calling downloadOrVerifyAttachments](https://issues.couchbase.com//browse/CBG-1590)
* [CBG-1558](https://issues.couchbase.com//browse/CBG-1558) — [panic after failed unmarshal in GetDeepMutableBody](https://issues.couchbase.com//browse/CBG-1558)
* [CBG-1473](https://issues.couchbase.com//browse/CBG-1473) — [Enable log redaction by default](https://issues.couchbase.com//browse/CBG-1473)
* [CBG-1424](https://issues.couchbase.com//browse/CBG-1424) — [discoverInterfaceName should resolve hostnames before trying to find network interface stats using IP addresses](https://issues.couchbase.com//browse/CBG-1424)
* [CBG-1391](https://issues.couchbase.com//browse/CBG-1391) — [Treat existing cbgt index as recoverable error](https://issues.couchbase.com//browse/CBG-1391)
* [CBG-1390](https://issues.couchbase.com//browse/CBG-1390) — [Add warning threshold for excessively large number of channels per user](https://issues.couchbase.com//browse/CBG-1390)
* [CBG-1359](https://issues.couchbase.com//browse/CBG-1359) — [Increase default minimum TLS version TLS1.2](https://issues.couchbase.com//browse/CBG-1359)
* [CBG-1343](https://issues.couchbase.com//browse/CBG-1343) — [Increase initial wait time for index creation retry](https://issues.couchbase.com//browse/CBG-1343)
* [CBG-1342](https://issues.couchbase.com//browse/CBG-1342) — [Avoid retry on 'duplicate index name' index creation error](https://issues.couchbase.com//browse/CBG-1342)
* [CBG-1326](https://issues.couchbase.com//browse/CBG-1326) — [Log if channels expand to a smaller set than requested](https://issues.couchbase.com//browse/CBG-1326)
* [CBG-1301](https://issues.couchbase.com//browse/CBG-1301) — [Persistent Config](https://issues.couchbase.com//browse/CBG-1301)
* [CBG-1284](https://issues.couchbase.com//browse/CBG-1284) — [Mobile Attachment Cleanup](https://issues.couchbase.com//browse/CBG-1284)
* [CBG-1282](https://issues.couchbase.com//browse/CBG-1282) — [XATTRS Access Grants](https://issues.couchbase.com//browse/CBG-1282)
* [CBG-1280](https://issues.couchbase.com//browse/CBG-1280) — [Channel Access Revocation](https://issues.couchbase.com//browse/CBG-1280)
* [CBG-1273](https://issues.couchbase.com//browse/CBG-1273) — [Add Prometheus alert examples](https://issues.couchbase.com//browse/CBG-1273)
* [CBG-1253](https://issues.couchbase.com//browse/CBG-1253) — [Add USE INDEX to index readiness queries](https://issues.couchbase.com//browse/CBG-1253)
* [CBG-1251](https://issues.couchbase.com//browse/CBG-1251) — [Support Apple (M1) Silicon](https://issues.couchbase.com//browse/CBG-1251)
* [CBG-1245](https://issues.couchbase.com//browse/CBG-1245) — [Include channel name in validfrom logging](https://issues.couchbase.com//browse/CBG-1245)
* [CBG-1217](https://issues.couchbase.com//browse/CBG-1217) — [Ensure change listener goroutines terminates (both Tap and DCP feeds) before the server is stopped](https://issues.couchbase.com//browse/CBG-1217)
* [CBG-1170](https://issues.couchbase.com//browse/CBG-1170) — [Upgrade to go 1.15](https://issues.couchbase.com//browse/CBG-1170)
* [CBG-1127](https://issues.couchbase.com//browse/CBG-1127) — [Treat resurrected tombstones as non-conflict when no shared history](https://issues.couchbase.com//browse/CBG-1127)
* [CBG-949](https://issues.couchbase.com//browse/CBG-949) — [Improve error when non-upgradable HTTP request is sent to \_blipsync endpoint](https://issues.couchbase.com//browse/CBG-949)
* [CBG-841](https://issues.couchbase.com//browse/CBG-841) — [Force users to opt in to accepting unsigned tokens from providers in SG's provider config.](https://issues.couchbase.com//browse/CBG-841)
* [CBG-715](https://issues.couchbase.com//browse/CBG-715) — [High CPU usage in high volume basic auth scenarios](https://issues.couchbase.com//browse/CBG-715)
* [CBG-641](https://issues.couchbase.com//browse/CBG-641) — [Admin API Auth](https://issues.couchbase.com//browse/CBG-641)
* [CBG-551](https://issues.couchbase.com//browse/CBG-551) — [Avoid storing \_removed:true revision bodies in the revision cache](https://issues.couchbase.com//browse/CBG-551)

### [](#issues-and-resolutions-300)Issues and Resolutions

#### [](#known-issues-5)Known Issues

* [CBG-798](https://issues.couchbase.com//browse/CBG-798) — [Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com//browse/CBG-798)

#### [](#fixed-issues-6)Fixed Issues

* [CBG-1439](https://issues.couchbase.com//browse/CBG-1439) — [database.abandoned\_seqs stat is unused](https://issues.couchbase.com//browse/CBG-1439)
* [CBG-1438](https://issues.couchbase.com//browse/CBG-1438) — [SgwIntStat.SetIfMax incorrectly sums old and new values](https://issues.couchbase.com//browse/CBG-1438)
* [CBG-1428](https://issues.couchbase.com//browse/CBG-1428) — [ISGR should ignore \_removed:true bodies when purgeOnRemoval is disabled](https://issues.couchbase.com//browse/CBG-1428)
* [CBG-1427](https://issues.couchbase.com//browse/CBG-1427) — [ISGR should not try sending a delta when deltaSrc is a tombstone](https://issues.couchbase.com//browse/CBG-1427)
* [CBG-1412](https://issues.couchbase.com//browse/CBG-1412) — [JSON strings in some responses not being correctly escaped](https://issues.couchbase.com//browse/CBG-1412)
* [CBG-1388](https://issues.couchbase.com//browse/CBG-1388) — [sg\_collect does not package archived log files (\*.log.gz)](https://issues.couchbase.com//browse/CBG-1388)
* [CBG-1376](https://issues.couchbase.com//browse/CBG-1376) — [Some Delta Sync errors logged at WARN level should be DEBUG](https://issues.couchbase.com//browse/CBG-1376)
* [CBG-1339](https://issues.couchbase.com//browse/CBG-1339) — [Creating mobile tombstone for existing CBS tombstone causes loop](https://issues.couchbase.com//browse/CBG-1339)
* [CBG-1335](https://issues.couchbase.com//browse/CBG-1335) — [Mutating \_rev on localDocument in conflict resolver results in merge error](https://issues.couchbase.com//browse/CBG-1335)
* [CBG-1325](https://issues.couchbase.com//browse/CBG-1325) — [Incorrect email validation (too strict)](https://issues.couchbase.com//browse/CBG-1325)
* [CBG-1304](https://issues.couchbase.com//browse/CBG-1304) — [ISGR: Pull replications incompatible with active-side allow\_conflicts=false](https://issues.couchbase.com//browse/CBG-1304)
* [CBG-1246](https://issues.couchbase.com//browse/CBG-1246) — [Changes limit incorrectly applied in case of CBG-946](https://issues.couchbase.com//browse/CBG-1246)
* [CBG-1231](https://issues.couchbase.com//browse/CBG-1231) — [Prevent import cfg startup races](https://issues.couchbase.com//browse/CBG-1231)
* [CBG-1200](https://issues.couchbase.com//browse/CBG-1200) — [Calling DELETE on a non-existent document creates a tombstone with empty body](https://issues.couchbase.com//browse/CBG-1200)
* [CBG-1172](https://issues.couchbase.com//browse/CBG-1172) — [ISGR credentials with characters requiring URL encoding cause blipsync to fail](https://issues.couchbase.com//browse/CBG-1172)
* [CBG-1161](https://issues.couchbase.com//browse/CBG-1161) — [DefaultPurgeInterval specified in days and used as though in hours](https://issues.couchbase.com//browse/CBG-1161)
* [CBG-1113](https://issues.couchbase.com//browse/CBG-1113) — [CBL1.x/Websocket based changes feeds leak goroutine on disconnect](https://issues.couchbase.com//browse/CBG-1113)
* [CBG-789](https://issues.couchbase.com//browse/CBG-789) — [Updating a blob with new data does not update SG's metadata on sync](https://issues.couchbase.com//browse/CBG-789)

### [](#api-and-configuration-changes)API and Configuration Changes

This release introduces significant configuration and persistent API changes; some of which may be breaking changes if they impact a feature you rely on — see the items identified in:attribute: value [Table 1](#tbl-breaking) | [Table 2](#tbl-deprecated) | [Table 3](#tbl-dropped).

#### [](#breaks-compatibility)Breaks compatibility

__Table 1\. Breaks compatibility__
| Feature                                                                                                                                                                                                                                                                                                                          | Link                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| enable\_shared\_bucket\_access — enabled by default The change _ought to be_ transparent to the user, **if**: Doc metadata is smaller than 1MB There is no reliance on inspecting doc metadata using the \_sync property in a document on the server side Old documents are automatically migrated to the xattr metadata format. | [enable\_shared\_bucket\_access](configuration-properties-legacy.md#databases-this%5Fdb-enable%5Fshared%5Fbucket%5Faccess) |
| Enforce TLS by default                                                                                                                                                                                                                                                                                                           | [Couchbase Server Connection](#secure-sgw-access.html#lbl-cbs-comms)                                                       |

#### [](#deprecated)Deprecated

__Table 2\. Deprecated__
| Feature                                          | Link                                                                                         |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| allow\_conflicts confg                           | [allow\_conflicts](configuration-properties-legacy.md#databases-this%5Fdb-allow%5Fconflicts) |
| enable\_shared\_bucket\_access — disabled option |                                                                                              |
| Facebook User Auth Config                        | [facebook](configuration-properties-legacy.md#facebook)                                      |
| Google User Auth Config                          | [Google](configuration-properties-legacy.md#facebook)                                        |
| Logging API                                      |                                                                                              |

#### [](#dropped-or-removed)Dropped or removed

__Table 3\. Dropped or removed__
| Feature                                                      | Link                                                                                                                       |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| admin UI                                                     |                                                                                                                            |
| configServer property                                        | [configserver](configuration-properties-legacy.md#configServer)                                                            |
| databases.this\_db.cache.channel\_cache\_expiry              | [channel\_cache\_expiry](configuration-properties-legacy.md#databases-this%5Fdb-cache-channel%5Fcache%5Fexpiry)            |
| databases.this\_db.feed\_type                                | [feed\_type](configuration-properties-legacy.md#databases-this%5Fdb-feed%5Ftype)                                           |
| logging.default config section                               |                                                                                                                            |
| databases.this\_db.cache.channel\_cache\_max\_length         | [channel\_cache\_max\_length](configuration-properties-legacy.md#databases-this%5Fdb-cache-channel%5Fcache%5Fmax%5Flength) |
| databases.this\_db.cache.channel\_cache\_min\_length         | [channel\_cache\_min\_length](configuration-properties-legacy.md#databases-this%5Fdb-cache-channel%5Fcache%5Fmin%5Flength) |
| databases.this\_db.cache.enable\_star\_channel               | [enable\_star\_channel](configuration-properties-legacy.md#databases-this%5Fdb-cache-enable%5Fstar%5Fchannel)              |
| databases.this\_db.cache.max\_num\_pending                   | [max\_num\_pending](configuration-properties-legacy.md#databases-this%5Fdb-cache-max%5Fnum%5Fpending)                      |
| databases.this\_db.cache.max\_wait\_pending                  | [db-cache-max\_wait\_pending](configuration-properties-legacy.md#databases-this%5Fdb-cache-max%5Fwait%5Fpending)           |
| databases.this\_db.cache.max\_wait\_skipped                  | [max\_num\_skipped](configuration-properties-legacy.md#databases-this%5Fdb-cache-max%5Fwait%5Fskipped)                     |
| old cache config values: databases.this\_db.rev\_cache\_size | [rev\_cache\_size](configuration-properties-legacy.md#databases-this%5Fdb-rev%5Fcache%5Fsize)                              |
| SG-Replicate                                                 |                                                                                                                            |
| walrus mode                                                  | [server](configuration-properties-legacy.md#databases-this%5Fdb-server)                                                    |

### [](#support-notices-300)Support Notices

This section documents any support-related notes, constraints and changes

#### [](#deprecation-notices)Deprecation Notices

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release. You should plan to move to an alternative, supported, solution as soon as practical.

#### [](#upgrading)Upgrading

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