---
title: Couchbase Lite for React Native Release Notes
description: Couchbase Lite for React Native
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Lite React Native
    version: "1.1"
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-react-native/edit/release/1.1/modules/product-notes/pages/release-notes.adoc
  xref: xref:cbl-reactnative:product-notes:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cbl-reactnative/current/product-notes/release-notes.html)

# Couchbase Lite for React Native Release Notes

## [](#maint-1-1-1)1.1.1 — October 2026

Version 1.1.1 for React Native delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-8900 — Support legacy attachments in Document.getBlob()](https://jira.issues.couchbase.com/browse/CBL-8900)

### [](#fixed-issues)Fixed Issues

* [CBL-8896 — iOS build fails with use\_frameworks!](https://jira.issues.couchbase.com/browse/CBL-8896)
* [CBL-8897 — Android build fails on Gradle 9](https://jira.issues.couchbase.com/browse/CBL-8897)
* [CBL-8898 — Android build fails because the logging module rejects nullable values from ReadableMap.toHashMap()](https://jira.issues.couchbase.com/browse/CBL-8898)
* [CBL-8920 — Replicator errors expose only a localized message without the error code and domain](https://jira.issues.couchbase.com/browse/CBL-8920)
* [CBL-8949 — App crashes on iOS when ReplicatorConfiguration heartbeat, maxAttempts or maxAttemptWaitTime is negative](https://jira.issues.couchbase.com/browse/CBL-8949)
* [CBL-8958 — Replication filter crashes the app on iOS and receives wrong data on Android when the document has a Blob](https://jira.issues.couchbase.com/browse/CBL-8958)

### [](#known-issues)Known Issues

None for this release

### [](#breaking-changes)Breaking Changes

None for this release

### [](#deprecations)Deprecations

None for this release

## [](#maint-1-1-0)1.1.0 — June 2026

Version 1.1.0 for React Native delivers the following features and enhancements:

### [](#new-features)New Features

* Official React Native New Architecture / TurboModule support for iOS and Android native modules.
* Improved file logging: React Native wrapper diagnostics can now be forwarded into configured file and custom log sinks.
* React Native-originated log lines are prefixed with `RN ::LEVEL::` so they are easy to distinguish from native Couchbase Lite log output.
* `LogSinks.write()` API for writing app-authored messages into the Couchbase Lite logging pipeline.
* `FileSystem.getFilesInDirectory(path)` API for listing files in a directory, useful when discovering generated log files.

### [](#improvements-and-fixes)Improvements and Fixes

* Updated Couchbase Lite Android and iOS Enterprise SDKs to 3.3.3.
* Improved listener reliability for collection, query, and replicator events on the New Architecture event path.
* Replicator event payloads now include error fields where applicable.
* Document expiration handling now supports clearing expiration with `null` and uses stricter UTC ISO-8601 parsing.
* Delete operations using `ConcurrencyControl.FAIL_ON_CONFLICT` now honor revision IDs more consistently.
* Android replicator filters can use JavaScript arrow functions in the V8 evaluation path.

### [](#repository-updates)Repository Updates

* Official npm package: [@couchbase/couchbase-lite-react-native](https://www.npmjs.com/package/@couchbase/couchbase-lite-react-native)
* The legacy `cbl-reactnative` package is superseded; new installs and upgrades should use the scoped package
* Main React Native repository: [couchbase/couchbase-lite-react-native](https://github.com/couchbase/couchbase-lite-react-native)
* Shared JavaScript library repository: [couchbase/couchbase-lite-js-common](https://github.com/couchbase/couchbase-lite-js-common)

### [](#migration-from-1-0-x)Migration from 1.0.x

* Existing application-level APIs remain largely compatible.
* Enable React Native New Architecture to use the TurboModule implementation.
* Review logging setup if you want React Native wrapper logs included in file or custom log sinks.

See [Migration Guide](../guides/migration/v1.1.md) for detailed instructions.

## [](#maint-1-0-0)1.0.0 — December 2025

Version 1.0.0 for React Native delivers the following features and enhancements:

### [](#new-features-2)New Features

* Log Sink API - Console, File, and Custom log sinks with configurable levels and domains
* LogDomain.ALL - New domain to enable all log categories at once
* Listener Token Management - New `ListenerToken` class with `token.remove()` API
* Collection Change Listeners - Monitor all documents in a collection
* Document Change Listeners - Monitor specific documents by ID
* Query Change Listeners (Live Queries) - Real-time query results
* Replicator Status Change Listeners - Monitor replication state and progress
* Replicator Document Change Listeners - Track individual document replication
* New ReplicatorConfiguration API - Collections passed during initialization using CollectionConfiguration
* Collection.fullName() method - Get fully qualified collection name (scope.collection)
* Couchbase Lite 3.3.0 - Updated iOS and Android SDKs to Couchbase Lite 3.3.0

### [](#breaking-changes-2)Breaking Changes

* TypeScript: ListenerToken type changed from string to ListenerToken object (affects explicitly typed code only)

### [](#deprecated-apis)Deprecated APIs

These APIs remain available for backward compatibility:

* Database.setLogLevel() - Use LogSinks.setConsole() instead. Note: Old and new logging APIs cannot be used in tandem.
* config.addCollection(collection) - Pass CollectionConfiguration array in constructor instead
* removeChangeListener() methods - Use token.remove() instead
* ListenerToken type changed from string to ListenerToken object (TypeScript breaking change for explicitly typed code)

### [](#bug-fixes)Bug Fixes

* Fixed encryption key crash when key not required
* Fixed Kotlin import paths and enhanced logging methods
* Improved blob data validation and array handling
* Fixed custom delete issues

### [](#migration-from-0-6-x)Migration from 0.6.x

1. Replace Database.setLogLevel() with LogSinks.setConsole() (required - APIs cannot be mixed)
2. Update ReplicatorConfiguration to use new constructor pattern (recommended)
3. Update listener cleanup to use token.remove() (recommended)
4. Update TypeScript code that explicitly typed tokens as string to use ListenerToken (required for TypeScript)

See [Migration Guide](../guides/migration/v1.md) for detailed instructions.