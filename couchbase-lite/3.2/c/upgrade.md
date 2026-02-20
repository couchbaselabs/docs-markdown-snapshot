---
title: Upgrade
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/c/pages/upgrade.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.2@couchbase-lite:c:upgrade.adoc[]
---

[View original HTML](/couchbase-lite/3.2/c/upgrade.html)

# Upgrade

## [](#3-2-3-upgrade)3.2.4 Upgrade

The action will take place automatically and can lead to some delay in the database becoming available for use in your application.

In addition, if you are syncing with a 3.2.4 Sync Gateway, you should be aware of the significant configuration enhancements introduced and their impact. See [Upgrading Sync Gateway](../../../sync-gateway/current/upgrading.md) for more details. This is a one-way conversion.

## [](#downgrading-couchbase-lite)Downgrading Couchbase Lite

### [](#downgrading-between-major-releases)Downgrading Between Major Releases

**No Downgrade Support** \- Downgrades between major versions of Couchbase Lite (CBL) are not supported. Once you upgrade to a new major version, downgrading to a previous major version may lead to incompatibility issues.

For example, Upgrading from CBL 2.x.x to CBL 3.x.x does not guarantee the ability to revert to CBL 2.x.x.

### [](#downgrading-between-minor-releases)Downgrading Between Minor Releases

**Conditional Downgrade Support** \- Downgrade support for minor releases is considered on a case-by-case basis. The release notes for each minor version will clarify whether downgrades are supported.

For example, if a new minor version such as CBL 3.1.0 is released the release notes will specify whether downgrading to CBL 3.0.x is supported.

### [](#downgrading-between-patch-releases)Downgrading Between Patch Releases

**Full Downgrade Support** \- Downgrades between patch releases are supported. Users can safely downgrade between different patch versions within the same minor release.

For example, if you’re running CBL 3.1.6 you can downgrade to CBL 3.1.4 or CBL 3.1.3 without issues.

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](#c:gs-prereqs.adoc)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.