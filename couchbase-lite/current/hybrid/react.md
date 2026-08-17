---
title: React Native
description: Couchbase Lite for React Native is a fully enterprise-supported,
  TypeScript-friendly Native Module that brings Couchbase Lite's embedded NoSQL
  database and data sync capabilities to React Native and Expo applications with
  full TypeScript/JavaScript support.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/hybrid/pages/react.adoc
  xref: xref:couchbase-lite:hybrid:react.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/hybrid/react.html)

# React Native

## [](#overview)Overview

Couchbase Lite for React Native enables developers to build fast, responsive mobile apps with local data storage, powerful querying, and secure data sync with Capella App Services or Sync Gateway, all with a modern TypeScript/JavaScript developer experience. It provides local data storage, SQL++ querying, and bi-directional data sync with Capella App Services or Sync Gateway.

> [!NOTE]
> Couchbase Lite for React Native has graduated from a community project to a fully enterprise-supported offering. You must have a [Couchbase Lite Enterprise license](https://www.couchbase.com/pricing/) to use this plugin.

The plugin uses React Native's Turbo Module architecture. Developers write in TypeScript/JavaScript while the plugin runs the underlying database operations natively on device.

## [](#platform-support)Platform Support

| Environment | Support Status |
| ----------- | -------------- |
| iOS         | Supported      |
| Android     | Supported      |
| Web         | Not supported  |
| Windows     | Not supported  |

## [](#capabilities)Capabilities

Couchbase Lite for React Native has near-complete feature parity with other Couchbase Lite platform implementations.

SQL++ Query Language

Write expressive queries using SQL++, with support for indexes, built-in functions, and Full-Text Search (FTS).

Data Sync

Sync data bi-directionally with Capella App Services or {sgw}.

Blob Handling

Store and sync binary data, including images and PDFs.

Real-time Change Notifications

Listen for changes to documents, collections, queries, and replication status.

Database Encryption

Encrypt local databases at rest.

Pre-built Databases

Bundle a pre-populated database with your app to reduce initial sync time and bandwidth on first launch.

## [](#limitations)Limitations

The following Couchbase Lite features are not currently supported in this plugin:

* **Vector Search** — not yet available on this platform.
* **Peer-to-Peer Sync** — the plugin does not include a platform-specific peer discovery mechanism.

## [](#get-started)Get Started

Use the following resources to get started with Couchbase Lite for React Native:

* [Prerequisites and Installation](https://cbl-reactnative.dev/category/start-here) — environment requirements and initial setup.
* [Migration Guide](https://cbl-reactnative.dev/Guides/Migration/migration-guide-v1) — upgrade instructions for projects moving from version 1.0.x.
* [Full Plugin Documentation](https://cbl-reactnative.dev/) — API reference, guides, and examples.
* [Example App](https://github.com/couchbase-examples/expo-cbl-travel) — a hands-on Expo demonstration project.

> [!NOTE]
> Couchbase recommends Expo for React Native development. Expo reduces setup complexity and provides a managed workflow that's compatible with this plugin.