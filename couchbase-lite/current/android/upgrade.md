---
title: Upgrade
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/upgrade.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite:android:upgrade.adoc[]
---

[View original HTML](/couchbase-lite/current/android/upgrade.html)

# Upgrade

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases automatically re-index on initial database open.  
> This can result in a delay before the database is usable.

## [](#4-0-0-upgrade)4.0.0 Upgrade

Couchbase Lite 4.0 introduces significant architectural changes, most notably the migration from revision trees to version vectors for document versioning.

### [](#major-changes-in-4-0-0)Major Changes in 4.0.0

**Version Vector Architecture**: CBL 4.0.0 replaces the revision tree system with version vectors, providing improved performance, scalability, and conflict resolution. Documents now use version-based revision IDs in the format `<timestamp>@<source-id>` instead of the previous `<generation>-<document-hash>` format.

**Enhanced Conflict Resolution**: The default conflict resolution strategy changes from `most active wins` to `last write wins` based on hybrid logical timestamps, providing more intuitive and predictable conflict resolution behavior.

**New Document Properties**: a new `timestamp` property is available on Document objects, providing direct access to the document’s logical timestamp as a `long` value representing nanoseconds since the Unix epoch.

### [](#database-compatibility-40)Database Compatibility

**Automatic Upgrade from 3.x**: CBL 4.0.0 databases are compatible with CBL 3.1 and 3.2 databases. When opening a 3.1 or 3.2 database with CBL 4.0.0, documents are automatically upgraded to use version vectors when they’re updated and saved.

**No Configuration Required**: CBL 4.0.0 enables version vectors by default - the feature requires no API configuration.

### [](#synchronization-compatibility-40)Synchronization Compatibility

**Sync Gateway Requirements**: CBL 4.0.0 requires Sync Gateway 4.x or later for synchronization. Attempting to sync with Sync Gateway versions prior to 4.x results in replication errors with appropriate error messages indicating the incompatibility.

**Peer-to-Peer Compatibility**: CBL 4.0.0 can only perform peer-to-peer synchronization with other CBL 4.x instances using either `URLEndpointListener` or `URLMessageEndpointListener`. Sync attempts with CBL 3.x peers fail with appropriate error messages.

## [](#downgrading-couchbase-lite)Downgrading Couchbase Lite

### [](#downgrading-between-major-releases)Downgrading Between Major Releases

**No Downgrade Support** \- Couchbase Lite (CBL) does not support downgrades between major versions. Once you upgrade to a new major version, attempting to downgrade to a previous major version creates incompatibility issues. For example, upgrading from CBL 3.x.x to CBL 4.x.x does not allow you to revert to CBL 3.x.x.

### [](#downgrading-between-minor-releases)Downgrading Between Minor Releases

**Conditional Downgrade Support** \- Downgrade support for minor releases is considered on a case-by-case basis. The release notes for each minor version clarify whether downgrades receive support.

For example, when a new minor version such as CBL 3.1.0 becomes available, the release notes specify whether reverting to CBL 3.0.x receives support.

### [](#downgrading-between-patch-releases)Downgrading Between Patch Releases

**Full Downgrade Support** \- Downgrades between patch releases are supported. Users can safely downgrade between different patch versions within the same minor release.

For example, if you’re running CBL 3.1.6 you can downgrade to CBL 3.1.4 or CBL 3.1.3 without issues.

## [](#related-content)Related Content

### [](#)

How to

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.