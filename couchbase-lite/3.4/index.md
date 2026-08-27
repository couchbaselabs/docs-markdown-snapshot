---
title: Introduction
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/ROOT/pages/index.adoc
  xref: xref:3.4@couchbase-lite::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/index.html)

# Introduction

## Couchbase Lite

Couchbase Lite is an embedded NoSQL JSON document database designed for mobile and edge devices. It enables applications to store, sync, and query data locally—even without network connectivity.

You can use Couchbase Lite as a standalone embedded database within your mobile apps, or with Sync Gateway and Couchbase Server to provide a complete cloud to edge synchronized solution.

#### Why Use Couchbase Lite?

* _Offline-first_: Works without a constant internet connection.
* _Local-first architecture_: Reduces cloud dependency and latency.
* _Secure sync_: Bi-directional sync with Cloud and Edge using [Sync Gateway](../../sync-gateway/current/introduction.md).
* _Cross-platform SDKs_: [Android](#platform-resources), [iOS](#platform-resources), [.NET](#platform-resources), [C](#platform-resources), and [community JavaScript](#platform-resources).
* Flexible JSON format speeds development and upgrades.
* Vector search on device for offline-first AI and RAG applications.
* Develop faster with SQL++ and easy to use APIs.
* OOTB peer-to-peer capabilities for data sync between devices.

#### Key Capabilities

* SQL++ querying and full CRUD support.
* Peer-to-peer and cloud sync options.
* Vector search for AI and semantic use cases.
* Built-in secure local storage and encryption.
* Revision control and conflict resolution.
* Lightweight footprint for constrained environments.

| Platform              | Language and Resources                                          |
| --------------------- | --------------------------------------------------------------- |
| Android               | [Java](java/quickstart.md), [Kotlin](android/kotlin.md)         |
| iOS                   | [Swift](swift/quickstart.md), [Objective-C](objc/quickstart.md) |
| .NET                  | [.NET](csharp/quickstart.md)                                    |
| C and C++             | [C and C++](c/quickstart.md)                                    |
| React Native          | [React Native](https://cbl-reactnative.dev/)                    |
| Ionic _(Community)_   | [Community resources ](https://cbl-ionic.dev/)                  |
| Flutter _(Community)_ | [Community resources](https://cbl-dart.dev/)                    |

> [!NOTE]
> The community maintains the React Native, Ionic and Flutter integrations. Couchbase does not officially support them. See [Support model](https://docs.couchbase.com/cloud/third-party/integrations.html#support-model) for more information on community support.