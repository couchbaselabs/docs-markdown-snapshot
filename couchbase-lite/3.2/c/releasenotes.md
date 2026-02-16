[View original HTML](/couchbase-lite/3.2/c/releasenotes.html)

## [](#maint-3-2-4)3.2.4 — June 2025

Version 3.2.4 for C delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-7004 — Add API to Access the TLSIdentity Used by CBLURLEndpointListener](https://jira.issues.couchbase.com/browse/CBL-7004)

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-7006 — Blobs Not Downloaded on Update with Delta Sync in Peer-to-Peer Replication](https://jira.issues.couchbase.com/browse/CBL-7006)
* [CBL-7048 — Anonymous TLSIdentity Not Regenerated on Listener Restart](https://jira.issues.couchbase.com/browse/CBL-7048)
* [CBL-7046 — Crash When CBLKeyPair\_PublicKeyDigest or PublicKeyData Fails to Retrieve External Public Key](https://jira.issues.couchbase.com/browse/CBL-7046)
* [CBL-7044 — Add Missing mbedTLS Error Domain](https://jira.issues.couchbase.com/browse/CBL-7044)
* [CBL-7041 — Invalid or Inconsistent Certificate Locality Key Name](https://jira.issues.couchbase.com/browse/CBL-7041)
* [CBL-6999 — Missing Implementation of CBLReplicator\_ServerCertificate for Accessing Server TLS Certificate](https://jira.issues.couchbase.com/browse/CBL-6999)
* [CBL-6975 — CreateIdentity with Persistent Key Crashes Inside Autorelease Pool on iOS ](https://jira.issues.couchbase.com/browse/CBL-6975)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-3)3.2.3 — April 2025

Version 3.2.3 for C delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-6953 — Support Android with 16 KB page size](https://jira.issues.couchbase.com/browse/CBL-6953)
* [CBL-6817 — Allow the document from the same collection but different collection instance to be saved or deleted](https://jira.issues.couchbase.com/browse/CBL-6817)

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-6886 — Replicator should stop on a SQLite disk-full error](https://jira.issues.couchbase.com/browse/CBL-6886)
* [CBL-6883 — Error when creating a partial value index with compound expressions](https://jira.issues.couchbase.com/browse/CBL-6883)
* [CBL-6820 — ListenerCertificateAuthenticator callback not working with certificate chain](https://jira.issues.couchbase.com/browse/CBL-6820)

### [](#known-issues-2)Known Issues

* [CBL-6951 — Cannot create URLEndpoint with database name containing dot](https://jira.issues.couchbase.com/browse/CBL-6951)

### [](#deprecations-2)Deprecations

None for this release

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-2)3.2.2 — March 2025

Version 3.2.2 for C delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-5185 - Support for Partial Indexes in Value and Full-Text Indexes](https://jira.issues.couchbase.com/browse/CBL-5185)
* [CBL-6451 - LogSink API for Configuring Couchbase Lite Logging](https://jira.issues.couchbase.com/browse/CBL-6451)

### [](#issues-and-resolutions-3)Issues and Resolutions

* [CBL-6534 - No Such Table Error When Upgrading from 3.1.9 to 3.2.1](https://jira.issues.couchbase.com/browse/CBL-6534)
* [CBL-6822 - Replicator may hang while stopping the housekeeper task during stop](https://jira.issues.couchbase.com/browse/CBL-6822)

* [CBL-6669 - CBLArrayIndexConfiguration.path requires null terminated char](https://jira.issues.couchbase.com/browse/CBL-6669)
* [CBL-6678 - Log directory is not automatically created](https://jira.issues.couchbase.com/browse/CBL-6678)

### [](#known-issues-3)Known Issues

None for this release

### [](#deprecations-3)Deprecations

* [CBL-6679 - Deprecated: Database.log API for Configuring Couchbase Lite Logging — Use LogSink API Instead](https://jira.issues.couchbase.com/browse/CBL-6679)

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-1)3.2.1 — November 2024

Version 3.2.1 for C delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

* [CBL-5169 - Support for Unnest Query and Array Index](https://jira.issues.couchbase.com/browse/CBL-5169)
* [CBL-6303 - Add ability to disable mmap usage](https://jira.issues.couchbase.com/browse/CBL-6303)

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

Version 3.2.0 for C delivers the following features and enhancements:

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

* [CBL-5266 - Include Privacy Manifest in the released library](https://issues.couchbase.com/browse/CBL-5266)
* [CBL-5208 - Implement Collection’s database property](https://issues.couchbase.com/browse/CBL-5208)
* [CBL-5202 - Implementation Collection’s full-name property](https://issues.couchbase.com/browse/CBL-5202)
* [CBL-5380 - Update iOS Target Version to 12](https://issues.couchbase.com/browse/CBL-5380)

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

* [CBL-4291 - Fixed crash in createUserAgentHeader on Android](https://issues.couchbase.com/browse/CBL-4291)
* [CBL-4282 - Fixed fleece headers listed in iOS framework module map files are not correct](https://issues.couchbase.com/browse/CBL-4282)
* [CBL-4248 - Fixed UserAgent contains some extra / debug string](https://issues.couchbase.com/browse/CBL-4248)
* [CBL-5666 - Fixed Invalidated context may be used in query observer callback](https://issues.couchbase.com/browse/CBL-5666)
* [CBL-4348 - Fixed missing nullable marks in CBLReplicatorConfiguration’s property encryption callbacks](https://issues.couchbase.com/browse/CBL-4348)

### [](#known-issues-5)Known Issues

None for this release

### [](#deprecations-5)Deprecations

No new deprecations for GA release

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------ |

## [](#maint-3-2-0-beta-3)3.2.0 — August 2024

Version 3.2.0 Beta 3 for C delivers the following features and enhancements:

### [](#enhancements-6)Enhancements

* [CBL-5202 - Implement Collection’s full-name property](https://issues.couchbase.com/browse/CBL-5202)
* [CBL-5208 - Implement Collection’s database property](https://issues.couchbase.com/browse/CBL-5208)
* [CBL-5380 - Update iOS Target Version to 12](https://issues.couchbase.com/browse/CBL-5380)

* [CBL-5241 - Upsert performance is degraded when the number of docs is increased](https://issues.couchbase.com/browse/CBL-5241)
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

* [CBL-4248 - Fixed UserAgent contains some extra / debug string](https://issues.couchbase.com/browse/CBL-4248)
* [CBL-4282 - Fixed fleece headers listed in iOS framework module map files are not correct](https://issues.couchbase.com/browse/CBL-4282)
* [CBL-4291 - Fixed crash in createUserAgentHeader on Android](https://issues.couchbase.com/browse/CBL-4291)
* [CBL-4348 - Fixed missing nullable marks in CBLReplicatorConfiguration’s property encryption callbacks](https://issues.couchbase.com/browse/CBL-4348)

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
* [CBL-4306 - DatabaseChange and DatabaseChangeListener are deprecated](https://issues.couchbase.com/browse/CBL-4306)
* [CBL-4304 - Database’s Document APIs are deprecated](https://issues.couchbase.com/browse/CBL-4304)

|  | For an overview of the latest features offered in Couchbase Lite 3.2.0 Beta 3, see [New in 3.2](../cbl-whatsnew.md) |
|  | ------------------------------------------------------------------------------------------------------------------- |