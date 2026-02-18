---
title: Compatibility
description: Couchbase Lite JavaScript -- platform and version compatibility information
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/compatibility.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite-javascript/current/compatibility.html)

# Compatibility

> Description — _Couchbase Lite JavaScript — platform and version compatibility information_  
> _Abstract — This content identifies the compatibility of Couchbase Lite JavaScript with Sync Gateway and Capella App Services, together with the browsers upon which it is supported._  
> Related Content — [Release Notes](releasenotes.md) | [Known Limitations](known-limitations.md) | [Supported Browsers](supported-browsers.md) | [What’s New](whats-new.md)

## [](#overview)Overview

This page provides compatibility information for Couchbase Lite JavaScript 1.0, including supported browsers, backend server versions, framework compatibility, and feature limitations.

For specific deployment constraints and backend compatibility requirements, see [Known Limitations](known-limitations.md).

> [!IMPORTANT]
> Users must be on Sync Gateway 3.3.1 or 4.0.1 and above to sync data with the JavaScript SDK. CORS configuration is required — see [Prerequisites](gs-prereqs.md#prerequisites).

## [](#sync-gateway-compatibility)Sync Gateway Compatibility

The table below summarizes the compatible versions of Couchbase Lite JavaScript with Sync Gateway.

__Table 1\. Sync Gateway and Couchbase Lite JavaScript Compatibility Matrix__
| Sync Gateway Versions ↓ | Couchbase Lite JavaScript → |
| ----------------------- | --------------------------- |
| 1.0.0                   |                             |
| 3.2.0 and earlier       | ![no](_images/no.png)       |
| 3.3.0                   | ![no](_images/no.png)       |
| 3.3.1                   | ![yes](_images/yes.png)     |
| 4.0.0                   | ![no](_images/no.png)       |
| 4.0.1 and above         | ![yes](_images/yes.png)     |

## [](#browser-compatibility)Browser Compatibility

See [Supported Browsers](supported-browsers.md) for detailed browser version requirements and feature support matrices.

**Desktop Browsers:** Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

**Mobile Browsers:** iOS Safari 14+, Android Chrome 90+, Android Firefox 88+

**Progressive Web Apps (PWA):** Full support for installable web applications with Service Worker integration

> [!IMPORTANT]
> Couchbase Lite JavaScript does not currently work with Couchbase Lite Edge Server. Use Sync Gateway or Capella App Services for data synchronization.

## [](#related-content)Related Content

### [](#)

Product Information

* [Release Notes](releasenotes.md)
* [Known Limitations](known-limitations.md)
* [Supported Browsers](supported-browsers.md)

.

### [](#-2)

Getting Started

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Databases](database.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.