---
title: Release Notes
description: Couchbase Sync Gateway
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/release-notes.adoc
  xref: xref:2.8@sync-gateway::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/release-notes.html)

# Release Notes

Release Note from Previous Releases

[Release 2.7](#2.7@sync-gateway::release-notes.adoc) | [Release 2.6](#2.6@sync-gateway::release-notes.adoc) | [Release 2.5](#2.5@sync-gateway::release-notes.adoc) | [Release 2.1](#2.1@sync-gateway::release-notes.adoc) | [Release 2.0](#2.0@sync-gateway::release-notes.adoc)

> Couchbase Sync Gateway  
> This content describes the key features and changes implemented by release 2.8 of Couchbase Sync Gateway

## [](#lbl-rel284)2.8.4 — February 2023

### [](#enhancements)Enhancements

* [ CBG-2698 -- Add conflictIncludesRev support for ](https://issues.couchbase.com/browse/CBG-2698)
* [ CBG-2607 -- Update websocket implementation ](https://issues.couchbase.com/browse/CBG-2607)
* [ CBG-2609 -- Lower log level for expected BLIP websocket close "errors" ](https://issues.couchbase.com/browse/CBG-2609)

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [ CBG-2066 -- Update golang.org/x/text to 0.3.3+ CVE-2020-14040 ](https://issues.couchbase.com/browse/CBG-2066)
* [ CBG-2704 -- ISGR Sequence checkpointing maintains unnessesary entries ](https://issues.couchbase.com/browse/CBG-2704)
* [ CBG-2706 -- Compact expected/processed when safe seq unchanged ](https://issues.couchbase.com/browse/CBG-2706)
* [ CBG-2611 -- Performance decrease in Replicate and SGReplicate tests ](https://issues.couchbase.com/browse/CBG-2611)
* [ CBG-2613 -- E2E Push: websocket reset by peer ](https://issues.couchbase.com/browse/CBG-2613)
* [ CBG-2600 -- ISGR processedSeqs/expectedSeq mismatch based on JSON string ](https://issues.couchbase.com/browse/CBG-2600)

#### [](#known-issues)Known Issues

* [ CBG-798 -- Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com/browse/CBG-798)

## [](#lbl-rel283)Release 2.8.3 (October 2021)

> [!TIP]
> Users of earlier Sync Gateway releases should plan to upgrade to this release at the earliest opportunity.

### [](#issues-and-resolutions-283)Issues and Resolutions

#### [](#enhancements-2)Enhancements

* [CBG-1665](https://issues.couchbase.com//browse/CBG-1665) — [Limit the number of open N1QL connections](https://issues.couchbase.com//browse/CBG-1665)
* [CBG-1444](https://issues.couchbase.com//browse/CBG-1444) — [\- discoverInterfaceName should resolve hostnames before trying to find network interface stats using IP addresses](https://issues.couchbase.com//browse/CBG-1444)

#### [](#known-issues-2)Known Issues

* [CBG-798](https://issues.couchbase.com/browse/CBG-798) — [Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com/browse/CBG-798)

#### [](#fixed-issues-2)Fixed Issues

* [CBG-1725](https://issues.couchbase.com//browse/CBG-1725) — [ISGR Pull checkpoint sequences unreliable](https://issues.couchbase.com//browse/CBG-1725)
* [CBG-1724](https://issues.couchbase.com//browse/CBG-1724) — [Incorrect email validation (too strict)](https://issues.couchbase.com//browse/CBG-1724)
* [CBG-1723](https://issues.couchbase.com//browse/CBG-1723) — [CBL1.x/Websocket based changes feeds leak goroutine on disconnect](https://issues.couchbase.com//browse/CBG-1723)
* [CBG-1717](https://issues.couchbase.com//browse/CBG-1717) — [norev message sequence has wrong property name](https://issues.couchbase.com//browse/CBG-1717)
* [CBG-1696](https://issues.couchbase.com//browse/CBG-1696) — [Empty query results when using bypass channel cache](https://issues.couchbase.com//browse/CBG-1696)
* [CBG-1543](https://issues.couchbase.com//browse/CBG-1543) — [Metrics API port should not serve public API routes](https://issues.couchbase.com//browse/CBG-1543)
* [CBG-1454](https://issues.couchbase.com//browse/CBG-1454) — [ISGR: filtered push replication replicates channel removal revisions](https://issues.couchbase.com//browse/CBG-1454)
* [CBG-1451](https://issues.couchbase.com//browse/CBG-1451) — [SgwIntStat.SetIfMax incorrectly sums old and new values](https://issues.couchbase.com//browse/CBG-1451)
* [CBG-1379](https://issues.couchbase.com//browse/CBG-1379) — [Retry OIDC client initialization when the provider is not reachable ](https://issues.couchbase.com//browse/CBG-1379)
* [CBG-1362](https://issues.couchbase.com//browse/CBG-1362) — [Fix cacert-only handling for DCP connection](https://issues.couchbase.com//browse/CBG-1362)

## [](#lbl-rel282)Release 2.8.2 (March 2021)

> [!TIP]
> Users of 2.8.1 should upgrade to this release at the earliest opportunity.

### [](#issues-and-resolutions-282)Issues and Resolutions

Release 2.8.2 fixes an issue that could result in Sync Gateway entering an infinite loop when creating a mobile tombstone, if a Couchbase Server tombstone already exists for that key.

#### [](#known-issues-3)Known Issues

| Issue Ref.                                               | Summary                                                                                                                        |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [CBG-798](https://issues.couchbase.com/browse/CBG-798)   | [Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com/browse/CBG-798) |
| [CBG-1127](https://issues.couchbase.com/browse/CBG-1127) | [Treat resurrected tombstones as non-conflict when no shared history](https://issues.couchbase.com/browse/CBG-1127)            |

#### [](#fixed-issues-3)Fixed Issues

| Issue Ref.                                               | Summary                                                                                                          |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [CBG-1341](https://issues.couchbase.com/browse/CBG-1341) | [Creating mobile tombstone for existing CBS tombstone causes loop](https://issues.couchbase.com/browse/CBG-1341) |

## [](#lbl-rel281)Release 2.8.1 (February 2021)

[New Features](#new-features-281) **|** [Enhancements](#improvements-281) **|** [Issues and Resolutions](#issues-and-resolutions-281)

> [!NOTE]
> Release 2.8.1 has now been superseded by [Release 2.8.2 (March 2021)](#lbl-rel282). Users of 2.8.1 should upgrade to 2.8.2 as soon as practicable.

### [](#new-features-281)New Features

Metrics REST API

Release 2.8.1 sees the transition to general availability of Couchbase Sync Gateway's Metrics REST API, which was introduced as a _developer preview_ in release 2.8.0.

This feature exposes Sync Gateway's extensive stats in both JSON and Prometheus-compatible format. For more on how to enable the integration of Sync Gateway's metrics with one of the most popular monitoring and alerting solutions — see: [Prometheus Integration](../current/deploy/stats-prometheus.md) and [Metrics REST API](../current/rest-api/rest-api-metrics.md).

### [](#improvements-281)Enhancements

#### [](#configuration-changes)Configuration Changes

##### [](#custom-response-headers)Custom Response Headers

It is now possible to remove product versions from Sync Gateway responses using the `hide_product_versions` setting in the Config file. This customization of responses avoids revealing the version of the Sync Gateway to HTTP requests to the root path — see: [Hide Product Version in Headers](#{sgw-pg-config-properties}.adoc#hide%5Fproduct%5Fversion) and [CBG-1235](https://issues.couchbase.com/browse/CBG-1235)

##### [](#connection-string-overrides)Connection String Overrides

It is now possible to use the server connection string to override the current heuristic-driven behavior for selecting internal/external networking matches — see: [Couchbase Server Connection String](#{sgw-pg-config-properties}.adoc#databases-this%5Fdb-server) and [CBG-1276](https://issues.couchbase.com/browse/CBG-1276)

#### [](#other-enhancements)Other Enhancements

| Issue                                                    | Summary                                                                                                                                          |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [CBG-1152](https://issues.couchbase.com/browse/CBG-1152) | [2.8.1 Backport — Additional logging context for SGR2 checkpointing](https://issues.couchbase.com/browse/CBG-1152)                               |
| [CBG-1235](https://issues.couchbase.com/browse/CBG-1235) | [2.8.x Backport — Customizable HTTP response to ""/"" (suppress headers)"](https://issues.couchbase.com/browse/CBG-1235)                         |
| [CBG-1254](https://issues.couchbase.com/browse/CBG-1254) | [2.8.1 Backport — CBG-1244 - Add a new rev option for document\_changed event handler](https://issues.couchbase.com/browse/CBG-1254)             |
| [CBG-1267](https://issues.couchbase.com/browse/CBG-1267) | [2.8.1 Backport — CBG-1151 - Exit early from DocChange after running callback for \_sync:cfg docs](https://issues.couchbase.com/browse/CBG-1267) |
| [CBG-1270](https://issues.couchbase.com/browse/CBG-1270) | [2.8.1 Backport — CBG-1253 - Add USE INDEX to index readiness queries](https://issues.couchbase.com/browse/CBG-1270)                             |
| [CBG-1274](https://issues.couchbase.com/browse/CBG-1274) | [2.8.1-backport — Add Prometheus alert examples](https://issues.couchbase.com/browse/CBG-1274)                                                   |
| [CBG-1276](https://issues.couchbase.com/browse/CBG-1276) | [Implement network connstr flag for cbdatasource alt address shims](https://issues.couchbase.com/browse/CBG-1276)                                |

### [](#issues-and-resolutions-281)Issues and Resolutions

#### [](#known-issues-4)Known Issues

| Issue Ref.                                               | Summary                                                                                                                        |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [CBG-798](https://issues.couchbase.com/browse/CBG-798)   | [Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port](https://issues.couchbase.com/browse/CBG-798) |
| [CBG-1127](https://issues.couchbase.com/browse/CBG-1127) | [Treat resurrected tombstones as non-conflict when no shared history](https://issues.couchbase.com/browse/CBG-1127)            |

#### [](#fixed-issues-4)Fixed Issues

| Issue Ref.                                               | Summary                                                                                                                                                               |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CBG-1203](https://issues.couchbase.com/browse/CBG-1203) | [2.8.1 Backport CBG-1194 - sgcollect\_info not collecting system information](https://issues.couchbase.com/browse/CBG-1203)                                           |
| [CBG-1234](https://issues.couchbase.com/browse/CBG-1234) | [2.8.1 Backport — CBG-1231 - Prevent import cfg startup races](https://issues.couchbase.com/browse/CBG-1234)                                                          |
| [CBG-1252](https://issues.couchbase.com/browse/CBG-1252) | [2.8.1 Backport — CBG-1246 - Changes limit incorrectly applied in case of CBG-946](https://issues.couchbase.com/browse/CBG-1252)                                      |
| [CBG-1263](https://issues.couchbase.com/browse/CBG-1263) | [2.8.1 Backport CBG-1222 - Pre-2.8 cbgt index definitions not being removed post-upgrade](https://issues.couchbase.com/browse/CBG-1263)                               |
| [CBG-1265](https://issues.couchbase.com/browse/CBG-1265) | [2.8.1 Backport — CBG-1163 - Missing document in changes feed when using a compound sequence number as since parameter](https://issues.couchbase.com/browse/CBG-1265) |
| [CBG-1311](https://issues.couchbase.com/browse/CBG-1311) | [2.8.1 Backport ISGR: Pull replications incompatible with active-side allow\_conflicts=false](https://issues.couchbase.com/browse/CBG-1311)                           |

## [](#lbl-rel280)Release 2.8.0 (October 2020)

[New Features](#new-features-280) **|** [Enhancements](#improvements-280) **|** [Issues and Resolutions](#issues-and-resolutions-280) **|** [Support Notices](#support-notices-280) **|** [Related Content](#related-content)

### [](#new-features-280)New Features

#### [](#inter-syncgateway-replication)Inter-Sync Gateway Replication

Couchbase Sync Gateway's _[Inter-Sync Gateway Replication![glossary icon](images/icons/glossaryIconImage2.png)](glossary.md#inter-sync-gateway-replication)_ feature supports _[cloud-to-edge![glossary icon](images/icons/glossaryIconImage2.png)](glossary.md#cloud-to-edge) synchronization_ use cases, where data changes must be synchronized between a centralized cloud cluster and a large number of edge clusters whilst still enforcing fine grained access control. This is an increasingly important enterprise-level requirement.

Read More . . . [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)

#### [](#prometheus-monitoring-support-developer-preview)Prometheus Monitoring Support (Developer Preview)

This release gives developers the chance to try-out Couchbase Sync Gateway's new metrics API, which exposes stats in a Prometheus compatible format. This enables the integration of Sync Gateway's metrics with one of the most popular monitoring and alerting solutions, without resorting to external data transformation.

Read More . . . [Metrics REST API](../current/rest-api/rest-api-metrics.md)

### [](#improvements-280)Enhancements

#### [](#configuration-changes-2)Configuration Changes

Sync Gateway 2.8 introduces a number of configuration file changes made to accommodate the Inter-sync-gateway replication feature.

Replication

The database property has a new sub-property `replications`, which is used to associate an inter-Sync Gateway replication with a 'local' database.

The top level `replications` configuration property and its sub-properties is deprecated. Instead, use the `database.replication` property (as above) to define replications, unless you specifically need to use the pre-2.8 version with SG Replicate.

Note that any given database can still have multiple replications configured. Also, that inter-Sync Gateway replication does not support replication between two remote hosts via a third Sync Gateway; at least one database must be local.

See: [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

#### [](#api-changes)API Changes

This release introduces two new endpoints to the Admin Rest API.

* `_replication` \- used to initialize Inter-Sync Gateway Replication
* `_replicationStatus` \- used to set or query the status of a replication

The `_replicate` and `_active_tasks` endpoints are both deprecated, as they are replaced by the above.

See: [Admin REST API](../current/rest-api/rest-api-admin.md)

#### [](#other-enhancements-2)Other Enhancements

* [CBG-1022](https://issues.couchbase.com/browse/CBG-1022) — Require replication to be stopped prior to upsert
* [CBG-921](https://issues.couchbase.com/browse/CBG-921) — Ignore transaction ATR documents during DCP processing
* [CBG-905](https://issues.couchbase.com/browse/CBG-905) — Support using custom OIDC claim as Sync Gateway username
* [CBG-880](https://issues.couchbase.com/browse/CBG-880) — Python 3 support for sgcollect
* [CBG-877](https://issues.couchbase.com/browse/CBG-877) — Remove inappropriate logging warning related JSON parsing from ReadJSONFromMIME when request body is empty
* [CBG-876](https://issues.couchbase.com/browse/CBG-876) — Include Bearer prefix when sending token base authentication request in OIDC E2E tests
* [CBG-864](https://issues.couchbase.com/browse/CBG-864) — Improve addJSON-related error handling
* [CBG-821](https://issues.couchbase.com/browse/CBG-821) — Limit on channel queries triggered by 2.x replication
* [CBG-820](https://issues.couchbase.com/browse/CBG-820) — Add state for OIDC auth code authentication
* [CBG-803](https://issues.couchbase.com/browse/CBG-803) — Support for OIDC provider config refresh
* [CBG-802](https://issues.couchbase.com/browse/CBG-802) — Being able to configure OIDC Test Provider with HTTPS
* [CBG-801](https://issues.couchbase.com/browse/CBG-801) — Auto-generated OIDC callback URL should include provider when non-default
* [CBG-800](https://issues.couchbase.com/browse/CBG-800) — OnDemandImportForWrite bypasses migrate handling
* [CBG-752](https://issues.couchbase.com/browse/CBG-752) — sgcollect: Re-gzip rotated logfiles post-redaction, clean up intermediate extracted files
* [CBG-751](https://issues.couchbase.com/browse/CBG-751) — Improve REST-based sgcollect\_info options validation
* [CBG-719](https://issues.couchbase.com/browse/CBG-719) — Update OIDC library
* [CBG-714](https://issues.couchbase.com/browse/CBG-714) — Log warning on ignored, invalid channel data
* [CBG-709](https://issues.couchbase.com/browse/CBG-709) — Inter-Sync Gateway Replication
* [CBG-697](https://issues.couchbase.com/browse/CBG-697) — SGW startup routine could use more retry logic while CBS warms up
* [CBG-688](https://issues.couchbase.com/browse/CBG-688) — Improve logging for x.509 connection errors
* [CBG-673](https://issues.couchbase.com/browse/CBG-673) — Include USE INDEX hint with channel queries
* [CBG-665](https://issues.couchbase.com/browse/CBG-665) — Make trace level logging a typical file logger
* [CBG-664](https://issues.couchbase.com/browse/CBG-664) — Enhance trace logging for blip messages
* [CBG-658](https://issues.couchbase.com/browse/CBG-658) — Optimize LogKey string lookup
* [CBG-653](https://issues.couchbase.com/browse/CBG-653) — Add 'norev' BLIP handler to log detailed error information
* [CBG-640](https://issues.couchbase.com/browse/CBG-640) — Wrong content type for \_user and \_role
* [CBG-633](https://issues.couchbase.com/browse/CBG-633) — Clean up duplicate db definitions in blipHandler/blipSyncContext
* [CBG-630](https://issues.couchbase.com/browse/CBG-630) — Validate whether multiple databases connect to the same bucket
* [CBG-624](https://issues.couchbase.com/browse/CBG-624) — Add database config option for HttpOnly cookies
* [CBG-622](https://issues.couchbase.com/browse/CBG-622) — Use secure cookies when SG is configured to listen over TLS
* [CBG-600](https://issues.couchbase.com/browse/CBG-600) — sgcollect\_info TMPDIR setting should be a real argument
* [CBG-585](https://issues.couchbase.com/browse/CBG-585) — Avoid log redaction cost via UD/MD/SD when log-level disabled
* [CBG-581](https://issues.couchbase.com/browse/CBG-581) — Write simple JSON HTTP responses directly as raw bytes
* [CBG-437](https://issues.couchbase.com/browse/CBG-437) — Return error when receiving deltas for deltaSrc revisions which are tombstoned

### [](#issues-and-resolutions-280)Issues and Resolutions

#### [](#known-issues-5)Known Issues

* [CBG-1127](https://issues.couchbase.com/browse/CBG-1127) — Treat resurrected tombstones as non-conflict when no shared history
* [CBG-798](https://issues.couchbase.com/browse/CBG-798) — Sync Gateway requires Couchbase Server nodes to use the same SSL memcached port

#### [](#fixed-issues-5)Fixed Issues

* [CBG-1072](https://issues.couchbase.com/browse/CBG-1072) — CAS race can result in unordered recentSequences
* [CBG-983](https://issues.couchbase.com/browse/CBG-983) — \_all\_docs with keys parameter not returning revID
* [CBG-951](https://issues.couchbase.com/browse/CBG-951) — Deleted documents should set \_deleted:true for import filter function
* [CBG-946](https://issues.couchbase.com/browse/CBG-946) — Repeated change entries on access grant to doc's previous channel
* [CBG-926](https://issues.couchbase.com/browse/CBG-926) — User name not being logged for initial HTTP request
* [CBG-819](https://issues.couchbase.com/browse/CBG-819) — Generate empty delta as {} instead of null
* [CBG-812](https://issues.couchbase.com/browse/CBG-812) — Running compact when UseViews=true causes an infinite loop
* [CBG-744](https://issues.couchbase.com/browse/CBG-744) — OldDoc body in sync function for tombstone resurrections does not contain \_deleted=true
* [CBG-743](https://issues.couchbase.com/browse/CBG-743) — Doc body in sync function contains \_deleted=false
* [CBG-741](https://issues.couchbase.com/browse/CBG-741) — 403 Attachment's doc not being synced during CBL replication
* [CBG-731](https://issues.couchbase.com/browse/CBG-731) — Channels query performance degradation when using limit
* [CBG-727](https://issues.couchbase.com/browse/CBG-727) — Panic when connecting to non-standard memcached port using couchbase(s):// scheme
* [CBG-695](https://issues.couchbase.com/browse/CBG-695) — Alternate addresses are always used if defined instead of applying heuristic
* [CBG-661](https://issues.couchbase.com/browse/CBG-661) — Errors from REST API produce invalid JSON

### [](#support-notices-280)Support Notices

This section documents any support-related notes, constraints and changes

#### [](#deprecation-notices)Deprecation Notices

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release. You should plan to move to an alternative, supported, solution as soon as practical.

##### [](#sgreplicate-replication-protocol)SG Replicate replication protocol

SG Replicate is deprecated in Sync Gateway version 2.8\. You should plan your transition to inter-Sync Gateway replication now to avoid potential issues when this functionality is removed — see [CBG-904](https://issues.couchbase.com/browse/CBG-904?src=confmacro)

The functionality of SG Replicate remains unchanged, unless explicitly stated in these release notes and-or in the appropriate documentation section. Refer to [Upgrade Sync Gateway](../current/upgrading.md) for more information on upgrading from SG Replicate to Inter-Sync Gateway replication.

##### [](#configuration-deprecations)Configuration deprecations

[CBG-904](https://issues.couchbase.com/browse/CBG-904) — The SG Replicate configuration method is deprecated at version 2.8.

Replications configured at the configuration file's root level will continue to function, but you should configure new replications under the appropriate database using the `databases.{dbname}.replications.{replication_id}` property.

##### [](#rest-api-deprecations)REST API Deprecations

[CBG-904](https://issues.couchbase.com/browse/CBG-904) These SG Replicate REST endpoints are deprecated:

* `_active_tasks` — superseded by new monitoring endpoint
* `_replicate` — superseded by the `_replication` endpoint

##### [](#operating-systems)Operating Systems

Support for Microsoft Windows 2012 (64-bit) is deprecated

#### [](#other-notices)Other Notices

##### [](#minimum-version-for-inter-sync-gateway-replication)Minimum Version for Inter-Sync Gateway Replication

In order to support inter-Sync Gateway replication's new features (2.8), all nodes in the active cluster must be running Sync Gateway 2.8+.

##### [](#replication-between-two-remote-databases)Replication between two remote databases

Replication between two remote databases is no longer supported. However, root level replications (which by definition, use SG Replicate) will continue to support remote replications, albeit in the now deprecated feature.

##### [](#pushing-to-pre-2-8-targets)Pushing to pre-2.8 targets

* Push replications do not support a pre-2.8 target with `"allow_conflicts": false` set; the target must use `"allow_conflicts": true` for a replication to work.
* Push replications do not use Delta Sync when pushing to a pre-2.8 target

##### [](#support-is-added-for)Support is added for:

* Red Hat Enterprise Linux 8
* CentOS 8

### [](#upgrading)Upgrading

In order to support inter-Sync Gateway replication's new features (2.8), all nodes in the active cluster must be running Sync Gateway 2.8+.

The version of inter-Sync Gateway replication useable depends on the combination of Sync Gateway versions running on the active and passive nodes — see: [Example 1](#availability-of-sg-replicate-versions).

Example 1\. Availability of Inter-Sync Gateway replication versions

Available for use on an active node

* Pre-Sync Gateway 2.8 — only SG Replicate is available
* Sync Gateway 2.8+ — you may run inter-Sync Gateway (2.8+), or the pre-2.8 SG Replicate (deprecated)

SG versions compatible as a passive node

* Pre-2.8 (SG Replicate) can target any inter-Sync Gateway replication version
* 2.8+ inter-Sync Gateway replications can only target other inter-Sync Gateway replications

For more on upgrading — see: [Upgrade Sync Gateway](../current/upgrading.md)

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)