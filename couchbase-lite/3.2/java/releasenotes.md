[View original HTML](/couchbase-lite/3.2/java/releasenotes.html)

## [](#maint-3-2-4)3.2.4 — June 2025

Version 3.2.4 for Java delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-6978 — Stopping a Replicator should stop all Conflict Resolutions](https://jira.issues.couchbase.com/browse/CBL-6978)

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-7006 — Blobs Not Downloaded on Update with Delta Sync in Peer-to-Peer Replication](https://jira.issues.couchbase.com/browse/CBL-7006)
* [CBL-7015 — Invalid or Inconsistent Certificate Locality Key Name](https://jira.issues.couchbase.com/browse/CBL-7015)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-3)3.2.3 — April 2025

Version 3.2.3 for Java delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-6884 — Support 16 KB page size](https://jira.issues.couchbase.com/browse/CBL-6884)

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-6886 — Replicator should stop on a SQLite disk-full error](https://jira.issues.couchbase.com/browse/CBL-6886)
* [CBL-6883 — Error when creating a partial value index with compound expressions](https://jira.issues.couchbase.com/browse/CBL-6883)
* [CBL-6820 — ListenerCertificateAuthenticator callback not working with certificate chain](https://jira.issues.couchbase.com/browse/CBL-6820)

### [](#known-issues-2)Known Issues

None for this release

### [](#deprecations-2)Deprecations

None for this release

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-2)3.2.2 — March 2025

Version 3.2.2 for Java delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-5185 - Support for Partial Indexes in Value and Full-Text Indexes](https://jira.issues.couchbase.com/browse/CBL-5185)
* [CBL-6451 - LogSink API for Configuring Couchbase Lite Logging](https://jira.issues.couchbase.com/browse/CBL-6451)

### [](#issues-and-resolutions-3)Issues and Resolutions

* [CBL-6534 - No Such Table Error When Upgrading from 3.1.9 to 3.2.1](https://jira.issues.couchbase.com/browse/CBL-6534)
* [CBL-6822 - Replicator may hang while stopping the housekeeper task during stop](https://jira.issues.couchbase.com/browse/CBL-6822)

### [](#known-issues-3)Known Issues

None for this release

### [](#deprecations-3)Deprecations

* [CBL-6679 - Deprecated: Database.log API for Configuring Couchbase Lite Logging — Use LogSink API Instead](https://jira.issues.couchbase.com/browse/CBL-6679)

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-1)3.2.1 — November 2024

Version 3.2.1 for Java delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

* [CBL-5169 - Support for Unnest Query and Array Index](https://jira.issues.couchbase.com/browse/CBL-5169)
* [CBL-6303 - Add ability to disable mmap usage](https://jira.issues.couchbase.com/browse/CBL-6303)

* [CBL-6074 - Replace Java Finalizer with Cleaner Using Phantom Reference](https://jira.issues.couchbase.com/browse/CBL-6074)

### [](#issues-and-resolutions-4)Issues and Resolutions

* [CBL-6131 - Fixed race creating the expiration column in a collection table](https://jira.issues.couchbase.com/browse/CBL-6131)
* [CBL-6245 - Fixed query parser regression related to brackets](https://jira.issues.couchbase.com/browse/CBL-6245)
* [CBL-6378 - Crash when calling onWebSocketGotTLSCertificate callback after the connection is closed](https://jira.issues.couchbase.com/browse/CBL-6378)

### [](#known-issues-4)Known Issues

None for this release

### [](#deprecations-4)Deprecations

No new deprecations for GA release

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-0)3.2.0 — August 2024

Version 3.2.0 for Java delivers the following features and enhancements:

### [](#downgrade-support)Downgrade Support

Downgrades from 3.2.x to any other version of Couchbase Lite are not supported.

### [](#enhancements-5)Enhancements

* [CBL-5287 - Enable Prediction Function in SQL++](https://issues.couchbase.com/browse/CBL-5287)
* [CBL-5634 - NoRev enhancement with Replacement Rev in pull replication](https://issues.couchbase.com/browse/CBL-5634)
* [CBL-5687 - Update replication protocol doc per ReplacementRev changes](https://issues.couchbase.com/browse/CBL-5687)
* [CBL-4412 - Enhance checkpoint resolution algorithm when local and remote checkpoint are mismatched](https://issues.couchbase.com/browse/CBL-4412)
* [CBL-5346 - Logging Replicator reasons of state change](https://issues.couchbase.com/browse/CBL-5346)
* [CBL-283 - Support Date Format other than ISO 8601 in SQL++](https://issues.couchbase.com/browse/CBL-283)
* [CBL-68 - DATE\_DIFF\_MILLIS(date1, date2, part)](https://issues.couchbase.com/browse/CBL-68)
* [CBL-67 - DATE\_ADD\_STR(date1, n, part)](https://issues.couchbase.com/browse/CBL-67)
* [CBL-66 - DATE\_ADD\_MILLIS(date1, n, part)](https://issues.couchbase.com/browse/CBL-66)
* [CBL-65 - MILLIS\_TO\_UTC(date1 \[, fmt](https://issues.couchbase.com/browse/CBL-65))\]
* [CBL-64 - MILLIS\_TO\_TZ(date1, tz \[, fmt](https://issues.couchbase.com/browse/CBL-64))\]
* [CBL-62 - STR\_TO\_TZ(date1, tz)](https://issues.couchbase.com/browse/CBL-62)
* [CBL-61 - MILLIS\_TO\_STR(date1 \[, fmt ](https://issues.couchbase.com/browse/CBL-61))\]
* [CBL-60 - DATE\_DIFF\_STR(date1, date2, part)](https://issues.couchbase.com/browse/CBL-60)

* [CBL-4451 - Native Support for Mac ARM](https://issues.couchbase.com/browse/CBL-4451)
* [CBL-5213 - Implement Proxy Authenticator API for Android / Java](https://issues.couchbase.com/browse/CBL-5213)
* [CBL-5207 - Implement Collection’s database property](https://issues.couchbase.com/browse/CBL-5207)
* [CBL-5201 - Implementation Collection’s full-name property](https://issues.couchbase.com/browse/CBL-5201)
* [CBL-5683 - Database.getDefaultCollection should not be nullable](https://issues.couchbase.com/browse/CBL-5683)
* [CBL-5535 - Update OkHTTP to 4.12](https://issues.couchbase.com/browse/CBL-5535)
* [CBL-4435 - Replicator.close() stops state updates](https://issues.couchbase.com/browse/CBL-4435)
* [CBL-4725 - Remove deprecated C4QueryOptions](https://issues.couchbase.com/browse/CBL-4725)
* [CBL-4897 - Revise zipfile production](https://issues.couchbase.com/browse/CBL-4897)
* [CBL-5361 - Control the JNI library’s publication of symbols](https://issues.couchbase.com/browse/CBL-5361)
* [CBL-5847 - Dates in Parameters can now be encoded](https://issues.couchbase.com/browse/CBL-5487)

### [](#issues-and-resolutions-5)Issues and Resolutions

* [CBL-3846 - Fixed corrupt Revision Data error when saving documents](https://issues.couchbase.com/browse/CBL-3846)
* [CBL-4247 - Fixed Replicator binary logs with collections cannot be decoded](https://issues.couchbase.com/browse/CBL-4247)
* [CBL-4326 - Fixed opening the upgraded database from 2.8 to 3.0.2 is slow](https://issues.couchbase.com/browse/CBL-4326)
* [CBL-4334 - Fixed Data getting corrupted during collection replication](https://issues.couchbase.com/browse/CBL-4334)
* [CBL-4390 - Fixed The URL Scheme the HTTP Message is incorrect when using proxy](https://issues.couchbase.com/browse/CBL-4390)
* [CBL-4391 - Fixed Stop replicator could cause 'database is locked' error when saving a document](https://issues.couchbase.com/browse/CBL-4391)
* [CBL-4413 - Fixed Compaction could cause "database is locked" error when the replicator attempts to save its checkpoint at the same time](https://issues.couchbase.com/browse/CBL-4413)
* [CBL-4470 - Fixed FLTimestamp\_ToString() could return a slice with a wrong size](https://issues.couchbase.com/browse/CBL-4470)
* [CBL-4493 - Fixed Couchbase Lite C - Flutter plugin (dart language bindings) replication not resuming when internet reconnected](https://issues.couchbase.com/browse/CBL-4493)
* [CBL-4499 - Fixed Replicator may get stuck when there is an error of "Invalid delta"](https://issues.couchbase.com/browse/CBL-4499)
* [CBL-4506 - Fixed Replicator starts up slow for big database](https://issues.couchbase.com/browse/CBL-4506)
* [CBL-4536 - Fixed error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4536)
* [CBL-4547 - Allow DictKeys to cache shared keys from query results](https://issues.couchbase.com/browse/CBL-4547)
* [CBL-4568 - Fixed URLEndpointListener.getURLs returns an empty list on Android v>=11](https://issues.couchbase.com/browse/CBL-4568)
* [CBL-4639 - Use FTS match() in the WHERE clause of LEFT OUTER JOINS Not Returning Correct Result](https://issues.couchbase.com/browse/CBL-4639)
* [CBL-4750 - Fixed c4queryenum\_next crashes with FTS](https://issues.couchbase.com/browse/CBL-4750)
* [CBL-4801 - Fixed opening an old db is slow in V3.1 the first time](https://issues.couchbase.com/browse/CBL-4801)
* [CBL-4802 - Fixed websocket implementation unable to handle continuation fragments](https://issues.couchbase.com/browse/CBL-4802)
* [CBL-4838 - Fixed Attachments/Blobs got deleted after compaction&re-sync](https://issues.couchbase.com/browse/CBL-4838)
* [CBL-4913 - Fixed regression in pull of blobs/legacy attachment handling](https://issues.couchbase.com/browse/CBL-4913)
* [CBL-5082 - Fixed crash in setting Housekeeper::\_doExpiration()](https://issues.couchbase.com/browse/CBL-5082)
* [CBL-5033 - Fixed Puller revoked docs should queue with other revs](https://issues.couchbase.com/browse/CBL-5033)
* [CBL-5044 - Don’t capture backtrace for OutOfRange error FLDictIterator\_Next](https://issues.couchbase.com/browse/CBL-5044)
* [CBL-5307 - Correctly updating remote revision when pulling the existing revision](https://issues.couchbase.com/browse/CBL-5307)
* [CBL-5332 - Fixed crash during document expiration](https://issues.couchbase.com/browse/CBL-5332)
* [CBL-5335 - Fixed array\_agg failures](https://issues.couchbase.com/browse/CBL-5335)
* [CBL-5336 - Over the bound of FLDicIterator should be banned](https://issues.couchbase.com/browse/CBL-5336)
* [CBL-5377 - Fixed MILLIS\_TO\_STRING is returning UTC instead of local time zone](https://issues.couchbase.com/browse/CBL-5377)
* [CBL-5449 - Fixed Attachments flag is dropped when applying delta to incoming rev](https://issues.couchbase.com/browse/CBL-5449)
* [CBL-5515 - Fixed Result alias can’t be used elsewhere in query](https://issues.couchbase.com/browse/CBL-5515)
* [CBL-5540 - Fixed pthread\_mutex\_lock called on a destroyed mutex](https://issues.couchbase.com/browse/CBL-5540)
* [CBL-5587 - Fixed Remote rev KeepBody flag could be cleared accidentally](https://issues.couchbase.com/browse/CBL-5587)
* [CBL-5589 - Fixed N1QL Parser has exponential slowdown for redundant parentheses](https://issues.couchbase.com/browse/CBL-5589)
* [CBL-5646 - Fixed Null dereference crash in gotHTTPResponse](https://issues.couchbase.com/browse/CBL-5646)
* [CBL-5724 - Fixed Replicator syncs from beginning when using prebuilt dbs synced from SG](https://issues.couchbase.com/browse/CBL-5724)

* [CBL-5280 - Fixed not releasing LocalRefs on callbacks.](https://issues.couchbase.com/browse/CBL-5280)
* [CBL-5225 - Fixed ReplicatedDocument getters do not comply with the spec](https://issues.couchbase.com/browse/CBL-5225)
* [CBL-5310 - Fixed concurrent modification during iteration](https://issues.couchbase.com/browse/CBL-5310)
* [CBL-5584 - Fixed NativeC4QueryObserver.free should disable the listener before freeing it](https://issues.couchbase.com/browse/CBL-5584)
* [CBL-5513 - Query.setParameters should throw](https://issues.couchbase.com/browse/CBL-5513)
* [CBL-5512 - toJSON should throw](https://issues.couchbase.com/browse/CBL-5512)
* [CBL-4782 - Stop treating all connection failures as Server Errors](https://issues.couchbase.com/browse/CBL-4782)
* [CBL-4298 - Fixed Work Manager Replication thows on Replication complete](https://issues.couchbase.com/browse/CBL-4298)
* [CBL-4294- ReplicatorConfiguration.setAuthenticator should allow a null argument](https://issues.couchbase.com/browse/CBL-4294)
* [CBL-4992 - Fixed Null is a legal revId in createC4DocumentChange](https://issues.couchbase.com/browse/CBL-4992)
* [CBL-4990 - Fixed CollectionChangeNotifier.getChanges() prematurely signals end of changes](https://issues.couchbase.com/browse/CBL-4990)
* [CBL-4988 - Map LiteCore log domain "Changes" to LogDomain.DATABASE](https://issues.couchbase.com/browse/CBL-4988)
* [CBL-5037 - Allow empty Domain list for Console Logger](https://issues.couchbase.com/browse/CBL-5037)
* [CBL-4797 - Database.exists should support the default directory](https://issues.couchbase.com/browse/CBL-4797)
* [CBL-5486 - Fixed native crash in objects derived from ResultSet](https://issues.couchbase.com/browse/CBL-5486)
* [CBL-4841 - Fixed logic bug in Conflict Resolver](https://issues.couchbase.com/browse/CBL-4841)
* [CBL-4837 - Lower the max size on the ClientTask thread pool to 8](https://issues.couchbase.com/browse/CBL-4837)
* [CBL-5853 - Dictionary and Array should allow adding self](https://issues.couchbase.com/browse/CBL-5853)
* [CBL-5455 - Fixed Result.toJSON is annotated @NonNull, but can return null](https://issues.couchbase.com/browse/CBL-5455)

### [](#known-issues-5)Known Issues

None for this release

### [](#deprecations-5)Deprecations

No new deprecations for GA release

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-0)3.2.0 — August 2024

Version 3.2.0 Beta 2 for Java delivers the following features and enhancements:

### [](#enhancements-6)Enhancements

* [CBL-5213 - Implement Proxy Authenticator API for Android / Java](https://issues.couchbase.com/browse/CBL-5213)
* [CBL-5207 - Implement Collection’s database property](https://issues.couchbase.com/browse/CBL-5207)
* [CBL-5201 - Implementation of Collection’s full-name property](https://issues.couchbase.com/browse/CBL-5201)
* [CBL-5361 - Control the JNI library’s publication of symbols](https://issues.couchbase.com/browse/CBL-5361)
* [CBL-5270 - Ensure that c4queryobs\_\* functions axre called under the database-exclusive lock](https://issues.couchbase.com/browse/CBL-5270)
* [CBL-4897 - Revise zipfile production](https://issues.couchbase.com/browse/CBL-4897)

* [CBL-5241 - Upsert performance is degraded when the number of docs is increased](https://issues.couchbase.com/browse/CBL-5241)
* [CBL-5379 - Update iOS Target Version to 12](https://issues.couchbase.com/browse/CBL-5379)
* [CBL-5287 - Enable Prediction Function in SQL++ Parser](https://issues.couchbase.com/browse/CBL-5287)
* [CBL-283 - Date Format other than ISO 8601](https://issues.couchbase.com/browse/CBL-283)
* [CBL-68 - DATE\_DIFF\_MILLIS(date1, date2, part)](https://issues.couchbase.com/browse/CBL-68)
* [CBL-67 - DATE\_ADD\_STR(date1, n, part)](https://issues.couchbase.com/browse/CBL-67)
* [CBL-66 - DATE\_ADD\_MILLIS(date1, n, part)](https://issues.couchbase.com/browse/CBL-66)
* [CBL-65 - MILLIS\_TO\_UTC(date1 \[, fmt](https://issues.couchbase.com/browse/CBL-65))\]
* [CBL-64 - MILLIS\_TO\_TZ(date1, tz \[, fmt](https://issues.couchbase.com/browse/CBL-64))\]
* [CBL-62 - STR\_TO\_TZ(date1, tz)](https://issues.couchbase.com/browse/CBL-62)
* [CBL-61 - MILLIS\_TO\_STR(date1 \[, fmt ](https://issues.couchbase.com/browse/CBL-61))\]
* [CBL-60 - DATE\_DIFF\_STR(date1, date2, part)](https://issues.couchbase.com/browse/CBL-60)

### [](#issues-and-resolutions-6)Issues and Resolutions

* [CBL-5280 - Fixed not releasing LocalRefs on callbacks.](https://issues.couchbase.com/browse/CBL-5280)
* [CBL-5310 - Fix concurrent modification during iteration](https://issues.couchbase.com/browse/CBL-5310)
* [CBL-5037 - Allow empty Domain list for Console Logger](https://issues.couchbase.com/browse/CBL-5037)
* [CBL-5225 - Fix ReplicatedDocument getters do not comply with the spec](https://issues.couchbase.com/browse/CBL-5225)
* [CBL-4992 - Beryllium: Null is a legal revId in createC4DocumentChange](https://issues.couchbase.com/browse/CBL-4992)
* [CBL-4990 - Fix Beryllium: CollectionChangeNotifier.getChanges() prematurely signals end of changes](https://issues.couchbase.com/browse/CBL-4990)
* [CBL-4988 - Beryllium: Map LiteCore log domain "Changes" to LogDomain.DATABASE](https://issues.couchbase.com/browse/CBL-4988)
* [CBL-4986 - Remap Changes LiteCore Log Domain to Database Domain](https://issues.couchbase.com/browse/CBL-4986)
* [CBL-5455 - FixResult.toJSON is annotated @NonNull, but can return null](https://issues.couchbase.com/browse/CBL-5455)
* [CBL-4841 - Fix Logic bug in Conflict Resolver](https://issues.couchbase.com/browse/CBL-4841)
* [CBL-4742 - Stop treating all connection failures as Server Errors](https://issues.couchbase.com/browse/CBL-4742)
* [CBL-4797 - Database.exists should support the default directory](https://issues.couchbase.com/browse/CBL-4797)
* [CBL-4294 - ReplicatorConfiguration.setAuthenticator should allow a null argument](https://issues.couchbase.com/browse/CBL-4294)
* [CBL-4837 - Lower the max size on the ClientTask thread pool to 8](https://issues.couchbase.com/browse/CBL-4837)
* [CBL-4298 - Work Manager Replication thows on Replication complete (Beryllium)](https://issues.couchbase.com/browse/CBL-4298)

* [CBL-5336 - Over the bound of FLDicIterator should be banned](https://issues.couchbase.com/browse/CBL-5336)
* [CBL-5335 - array\_agg seem to fail under some circumstances](https://issues.couchbase.com/browse/CBL-5335)
* [CBL-5332 - Crash during document expiration](https://issues.couchbase.com/browse/CBL-5332)
* [CBL-5307 - Updating remote revision when pulling the existing revision](https://issues.couchbase.com/browse/CBL-5307)
* [CBL-5044 - Don’t capture backtrace for OutOfRange error FLDictIterator\_Next](https://issues.couchbase.com/browse/CBL-5044)
* [CBL-5033 - Puller revoked docs should queue with other revs](https://issues.couchbase.com/browse/CBL-5033)
* [CBL-5020 - Fixed cannot read digest file: /libs/macos/aarch64/lib/libLiteCoreJNI.dylib.MD5 exception](https://issues.couchbase.com/browse/CBL-5020)
* [CBL-5449 - Port - Attachments flag is dropped when applying delta to incoming rev](https://issues.couchbase.com/browse/CBL-5449)
* [CBL-4536 - Error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4536)
* [CBL-4506 - Investigate Replicator starts up slow for big database](https://issues.couchbase.com/browse/CBL-4506)
* [CBL-4499 - Replicator may get stuck when there is an error of "Invalid delta"](https://issues.couchbase.com/browse/CBL-4499)
* [CBL-4493 - Couchbase Lite C - Flutter plugin (dart language bindings) replication not resuming when internet reconnected](https://issues.couchbase.com/browse/CBL-4493)
* [CBL-4802 - Websocket implementation unable to handle continuation fragments](https://issues.couchbase.com/browse/CBL-4802)
* [CBL-4801 - Open an old db is slow in V3.1 first time](https://issues.couchbase.com/browse/CBL-4801)
* [CBL-4390 - The URL Scheme the HTTP Message is incorrect when using proxy](https://issues.couchbase.com/browse/CBL-4390)
* [CBL-4247 - Replicator binary logs with collections cannot be decoded](https://issues.couchbase.com/browse/CBL-4247)
* [CBL-4245 - Update sockcpp to cbl-3663](https://issues.couchbase.com/browse/CBL-4245)
* [CBL-4600 - Doc update c4repl\_start](https://issues.couchbase.com/browse/CBL-4600)
* [CBL-4568 - URLEndpointListener.getURLs returns an empty list on Android v>=11](https://issues.couchbase.com/browse/CBL-4568)
* [CBL-4334 - Data getting corrupted during collection replication](https://issues.couchbase.com/browse/CBL-4334)
* [CBL-4326 - Opening the upgraded database from 2.8 to 3.0.2 is slow](https://issues.couchbase.com/browse/CBL-4326)
* [CBL-4413 - Compaction could cause "database is locked" error when the replicator attempts to save its checkpoint at the same time](https://issues.couchbase.com/browse/CBL-4413)
* [CBL-4391 - Stop replicator could cause 'database is locked' error when saving a document](https://issues.couchbase.com/browse/CBL-4391)
* [CBL-4913 - Regression in pull of blobs/legacy attachment handling](https://issues.couchbase.com/browse/CBL-4913)
* [CBL-4547 - Allow DictKeys to cache shared keys from query results](https://issues.couchbase.com/browse/CBL-4547)
* [CBL-4750 - c4queryenum\_next crashes with FTS](https://issues.couchbase.com/browse/CBL-4750)
* [CBL-4639 - Use FTS match() in the WHERE clause of LEFT OUTER JOINS Not Returning Correct Result](https://issues.couchbase.com/browse/CBL-4639)
* [CBL-4838 - Attachments/Blobs got deleted after compaction&re-sync](https://issues.couchbase.com/browse/CBL-4838)
* [CBL-4470 - FLTimestamp\_ToString() could return a slice with a wrong size](https://issues.couchbase.com/browse/CBL-4470)
* [Uninitialized struct](https://issues.couchbase.com/browse/CBL-4424)
* [CBL-3836 - Corrupt Revision Data error when saving documents](https://issues.couchbase.com/browse/CBL-3836)

### [](#known-issues-6)Known Issues

None for this release

### [](#deprecations-6)Deprecations

* [CBL-5491 - Default’s MAX\_ATTEMPT\_WAIT\_TIME and USE\_PLAIN\_TEXT are deprecated](https://issues.couchbase.com/browse/CBL-5491)
* [CBL-4316 - Replicator’s getPendingDocumentIds() and isDocumentPending(String id) are deprecated](https://issues.couchbase.com/browse/CBL-4316)
* [CBL-4315 - ReplicatorConfiguration’s filters and conflict resolver properties are deprecated](https://issues.couchbase.com/browse/CBL-4315)
* [CBL-4314 - ReplicatorConfiguration APIs with Database object are deprecated ](https://issues.couchbase.com/browse/CBL-4314)
* [CBL-4313 - MessageEndpointListenerConfiguration APIs using Database object are deprecated](https://issues.couchbase.com/browse/CBL-4313)
* [CBL-4312 - URLEndpointListenerConfiguration APIs using Database object are deprecated](https://issues.couchbase.com/browse/CBL-4312)
* [CBL-4311 - QueryBuilder : isNullOrMissing() and notNullOrMissing() are deprecated](https://issues.couchbase.com/browse/CBL-4311)
* [CBL-4310 - QueryBuilder : FullTextFunction’s rank(String index) and match(String index, String query) are deprecated](https://issues.couchbase.com/browse/CBL-4310)
* [CBL-4309 - QueryBuilder : DataSource’s database() is deprecated](https://issues.couchbase.com/browse/CBL-4309)
* [CBL-4307 - DocumentChange’s database property is deprecated](https://issues.couchbase.com/browse/CBL-4307)
* [CBL-4306 - DatabaseChange and DatabaseChangeListener are deprecated](https://issues.couchbase.com/browse/CBL-4306)
* [CBL-4305 - Database’s removeChangeListener() is deprecated](https://issues.couchbase.com/browse/CBL-4305)
* [CBL-4304 - Database’s Document APIs are deprecated](https://issues.couchbase.com/browse/CBL-4304)
* [CBL-4264 - Increased security: store BasicAuthenticator password as a char\[](https://issues.couchbase.com/browse/CBL-4264) and zero before release\]
* [CBL-4262 - ReplicatorConfiguration.setPinnedServerCertificate should take a Certificate](https://issues.couchbase.com/browse/CBL-4262)
* [CBL-3963 - Remove Deprecated ReplicatorConfiguration.ReplicatorType](https://issues.couchbase.com/browse/CBL-3963)
* [CBL-1727 - Improved naming for AbstractReplicatorConfiguration.ReplicatorType](https://issues.couchbase.com/browse/CBL-1727)
* [CBL-4263 - The public type ReplicatorConfiguration.ReplicatorType is not visible from Kotlin](https://issues.couchbase.com/browse/CBL-4263)

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0 Beta 2, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------------- |