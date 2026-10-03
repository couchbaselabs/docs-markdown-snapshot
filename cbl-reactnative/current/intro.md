---
title: Couchbase Lite for React Native
description: Couchbase Lite is an embedded, document-style NoSQL database that
  is syncable and makes it easy to build offline-enabled applications.
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Lite React Native
    version: "1.1"
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-react-native/edit/release/1.1/modules/ROOT/pages/intro.adoc
  xref: xref:cbl-reactnative::intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cbl-reactnative/current/intro.html)

# Couchbase Lite for React Native

Couchbase Lite for React Native is a Native Module implementation of Couchbase Lite for React Native using Typescript. It has feature parity with Couchbase Lite implementations for other platforms, with a few exceptions.

Version 1.1 adds official React Native New Architecture support through TurboModules.

More information on React Native - Native Modules can be found here: [React Native Docs](https://reactnative.dev/docs/legacy/native-modules-intro)

> [!NOTE]
> Couchbase Lite for React Native has officially graduated from a community project to a fully Enterprise-Supported offering

Install via npm: [@couchbase/couchbase-lite-react-native](https://www.npmjs.com/package/@couchbase/couchbase-lite-react-native) — see [Install](start-here/install.md) for full setup.

The version of this Native Module is based on supporting Couchbase Lite Enterprise for iOS and Android. A [license](https://www.couchbase.com/pricing/) is required to use Couchbase Lite Enterprise edition.

## [](#features)Features

* Offline First
* Documents

  * Schemaless
  * Stored in efficient binary format
* Blobs

  * Store and sync binary data, for example JPGs or PDFs
* Queries

  * SQL++ Query Language
  * Extension of familiar SQL for JSON-like data
  * Many built-in functions

    * Full-Text Search
    * Indexing
* Data Sync

  * [Couchbase Capella App Servcies](https://www.couchbase.com/products/capella) \- Sync your data from your mobile app to the Cloud
  * Remote On-Premise via [Sync Gateway](https://www.couchbase.com/products/sync-gateway)
* Change Notifications for

  * Documents
  * Collections
  * Queries
  * Replication
* Encryption

  * Full Database
* Pre-built Databases

  * Bundle a pre-populated database with your app to reduce initial sync time and bandwidth on first launch
* React Native New Architecture

  * TurboModule support for iOS and Android
* Logging

  * Console, file, and custom log sinks
  * React Native wrapper logs can be forwarded to file and custom sinks

> [!NOTE]
> This plugin only works with iOS and Android platforms. Web, Windows, and macOS support is not available — see [Platform Support](product-notes/compatibility.md#platform-support).

## [](#version-compatibility)Version Compatibility

Couchbase Lite for React Native is versioned separately from Couchbase Lite. Each version is built on a specific version of the Couchbase Lite Enterprise SDKs for iOS and Android:

| React Native Plugin | Couchbase Lite Swift Enterprise (iOS) | Couchbase Lite Android Enterprise |
| ------------------- | ------------------------------------- | --------------------------------- |
| 1.1.x               | 3.3.3                                 | 3.3.3                             |
| 1.0.x               | 3.3.0                                 | 3.3.0                             |

For React Native and platform requirements, see [Compatibility](product-notes/compatibility.md).

## [](#upgrading)Upgrading?

If you are upgrading from 1.0.x to 1.1, see the [Version 1.1 Migration Guide](guides/migration/v1.1.md).

If you are upgrading from 0.6.x, see the [Version 1.0 Migration Guide](guides/migration/v1.md) for detailed instructions on upgrading to version 1.0.

> [!NOTE]
> Migrating from 0.6.x directly to 1.1? Follow both guides in order — complete the [Version 1.0 Migration Guide](guides/migration/v1.md) first, then the [Version 1.1 Migration Guide](guides/migration/v1.1.md).

## [](#limitations)Limitations

Some of the features supported by other platform implementations of Couchbase Lite are currently not supported:

* Vector Search

  * Not yet available on this platform.
* Peer-to-Peer Sync

  * There is no "platform" specific code built into the plugin to allow you to find other peers.