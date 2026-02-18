---
title: Preparing for Couchbase Lite JavaScript
description: Prerequisites for the installation of Couchbase Lite JavaScript
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/gs-prereqs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite-javascript/current/gs-prereqs.html)

# Preparing for Couchbase Lite JavaScript

> Description — _Prerequisites for the installation of Couchbase Lite JavaScript_  
> _Abstract — Laying out the prerequisites and preparatory steps before installing Couchbase Lite JavaScript_  

## [](#browser-compatibility)Browser Compatibility

The Couchbase Lite JavaScript SDK is compatible with all major modern browsers, including Safari, Chrome, Firefox, and Microsoft Edge, across both desktop and mobile platforms. It uses IndexedDB as the underlying storage engine to ensure reliable offline persistence and performance.

Compatibility has been verified on the following browser versions (and newer):

* Safari 17+
* Chrome 142+
* Firefox 144+

> [!NOTE]
> Sync behaviour may be limited in private browsing modes (especially Chrome).

The SDK also runs seamlessly in Progressive Web App (PWA) environments, enabling installable, native-like usage scenarios.

## [](#prerequisites)Prerequisites

A modern ES2022+ JavaScript environment is needed for execution as the SDK uses promises and async/await features. Node.js 22+ is also required for development and build tooling.

If you are using Sync Gateway or App Services as a backend for your browser-based applications, you should enable CORS before you can synchronize data:

* For App Services, see [CORS Configuration for App Services](https://docs.couchbase.com/cloud/app-services/deployment/cors-configuration-for-app-services.html)
* The CORS configuration should be done in the [Sync Gateway Bootstrap Configuration](../../sync-gateway/current/configuration/configuration-schema-bootstrap.md#lbl-schema).

> [!IMPORTANT]
> Users must be on Sync Gateway 3.3.1 or 4.0.1 and above to sync data with the JavaScript SDK.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](#)
* [Install](gs-install.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.