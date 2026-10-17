---
title: Couchbase Lite JavaScript Release Notes
description: Couchbase Lite JavaScript release notes
pubDate: 2026-10-17T04:21:50.088Z
meta:
  component:
    title: Couchbase Lite JavaScript
    version: "1.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/releasenotes.adoc
  xref: xref:couchbase-lite-javascript::releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/releasenotes.html)

# Couchbase Lite JavaScript Release Notes

## [](#maint-1-0-3)1.0.3 — October 2026

Version 1.0.3 for Couchbase Lite JavaScript delivers the following fixes and enhancements:

### [](#enhancements)Enhancements

None for this release.

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-8849 — Query change listener not notified when query parameters change](https://jira.issues.couchbase.com/browse/CBL-8849)
* [CBL-8850 — EXISTS with a subquery throws an internal TypeError](https://jira.issues.couchbase.com/browse/CBL-8850)
* [CBL-8851 — Invalid index declarations throw internal errors or create unintended indexes](https://jira.issues.couchbase.com/browse/CBL-8851)
* [CBL-8852 — Query change listeners do not deliver an initial result](https://jira.issues.couchbase.com/browse/CBL-8852)
* [CBL-8853 — The package's browser and require entry points do not work](https://jira.issues.couchbase.com/browse/CBL-8853)
* [CBL-8855 — Database.addCloseListener reports an incorrect newVersion when the database is upgraded](https://jira.issues.couchbase.com/browse/CBL-8855)
* [CBL-8857 — \_default collection is silently dropped as soon as any collection is declared](https://jira.issues.couchbase.com/browse/CBL-8857)
* [CBL-8880 — Database.open() fails with a raw IndexedDB ConstraintError when two indexes are declared on the same property](https://jira.issues.couchbase.com/browse/CBL-8880)
* [CBL-8953 — Queries on a unique: true index fail with a SchemaError](https://jira.issues.couchbase.com/browse/CBL-8953)
* [CBL-8961 — COUNT(expr) counts every row instead of ignoring NULL and MISSING](https://jira.issues.couchbase.com/browse/CBL-8961)

#### [](#known-issues)Known Issues

None for this release.

### [](#breaking-changes)Breaking Changes

None for this release.

### [](#deprecations)Deprecations

None for this release.

## [](#maint-1-0-2)1.0.2 — September 2026

Version 1.0.2 for Couchbase Lite JavaScript delivers the following enhancements:

### [](#enhancements-2)Enhancements

* [CBL-8124 — Omit the Authorization header on the session request when no Basic credentials are configured](https://jira.issues.couchbase.com/browse/CBL-8124)
* [CBL-8240 — Add support for bearer token credentials in the replicator configuration](https://jira.issues.couchbase.com/browse/CBL-8240)
* [CBL-8354 — Authenticate Basic and Bearer credentials through the Sync Gateway session endpoint in all environments](https://jira.issues.couchbase.com/browse/CBL-8354)
* [CBL-8723 — Add support for session ID credentials in the replicator configuration](https://jira.issues.couchbase.com/browse/CBL-8723)
* [CBL-8871 — Accept either rev or \_rev as the checkpoint revision from the server](https://jira.issues.couchbase.com/browse/CBL-8871)

### [](#issues-and-resolutions-2)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

None for this release.

#### [](#known-issues-2)Known Issues

None for this release.

### [](#breaking-changes-2)Breaking Changes

None for this release.

### [](#deprecations-2)Deprecations

None for this release.

## [](#maint-1-0-1)1.0.1 — June 2026

Version 1.0.1 for Couchbase Lite JavaScript delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-7649 — Database.exists() doesn't exist](https://jira.issues.couchbase.com/browse/CBL-7649)
* [CBL-7942 — Continuous replicator should retry after network errors](https://jira.issues.couchbase.com/browse/CBL-7942)

### [](#issues-and-resolutions-3)Issues and Resolutions

#### [](#fixed-issues-3)Fixed Issues

* [CBL-7647 — Query results don't have Blobs](https://jira.issues.couchbase.com/browse/CBL-7647)
* [CBL-7648 — ReplicatorConfig.database is not type-compatible with Database<CustomConfig>](https://jira.issues.couchbase.com/browse/CBL-7648)
* [CBL-7920 — JS replicator does not send PINGs, leading to timeouts](https://jira.issues.couchbase.com/browse/CBL-7920)
* [CBL-7921 — Replicator 'continuous' property is inconsistent with other platforms](https://jira.issues.couchbase.com/browse/CBL-7921)

#### [](#known-issues-3)Known Issues

None for this release.

### [](#breaking-changes-3)Breaking Changes

None for this release.

### [](#deprecations-3)Deprecations

None for this release.

## [](#maint-1-0-0)1.0.0 — November 2025

Version 1.0.0 for Couchbase Lite JavaScript delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

None for this release.

### [](#issues-and-resolutions-4)Issues and Resolutions

#### [](#fixed-issues-4)Fixed Issues

None for this release.

#### [](#known-issues-4)Known Issues

* [CBL-7593 — date\_diff\_str behavior inconsistent with server](https://jira.issues.couchbase.com/browse/CBL-7593)
* [CBL-7647 — Query results don't have Blobs](https://jira.issues.couchbase.com/browse/CBL-7647)
* [CBL-7648 — ReplicatorConfig.database is not type-compatible with Database<CustomConfig>](https://jira.issues.couchbase.com/browse/CBL-7648)
* [CBL-7649 — Database.exists() doesn't exist](https://jira.issues.couchbase.com/browse/CBL-7649)

### [](#breaking-changes-4)Breaking Changes

None for this release.

### [](#deprecations-4)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite JavaScript, see [What's New](whats-new.md).

## [](#related-content)Related Content

### [](#)

Product Information

* [Compatibility](compatibility.md)
* [Supported Browsers](supported-browsers.md)

.

### [](#-2)

Getting Started

* [Install](gs-install.md)
* [Databases](database.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.