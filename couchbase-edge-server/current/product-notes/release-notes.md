---
title: Release Notes
pubDate: 2026-10-13T04:35:53.698Z
meta:
  component:
    title: Couchbase Edge Server
    version: "1.1"
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/product-notes/pages/release-notes.adoc
  xref: xref:couchbase-edge-server:product-notes:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/product-notes/release-notes.html)

# Release Notes

## [](#maint-latest)1.1.1 — October 2026

Version 1.1.1 of Couchbase Edge Server delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-8479 — Require password authentication for admin users](https://jira.issues.couchbase.com/browse/CBL-8479)
* [CBL-8480 — Support Organization and Organizational Unit verification for client certificates](https://jira.issues.couchbase.com/browse/CBL-8480)
* [CBL-8506 — Disallow setting both auth and an Authorization header in a replication](https://jira.issues.couchbase.com/browse/CBL-8506)
* [CBL-8556 — Support enable\_user\_access\_control per database](https://jira.issues.couchbase.com/browse/CBL-8556)
* [CBL-8699 — Support session authentication for replication from Couchbase Lite for JavaScript](https://jira.issues.couchbase.com/browse/CBL-8699)
* [CBL-8911 — Named query parameters in the URL aren't URL-decoded](https://jira.issues.couchbase.com/browse/CBL-8911)

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-8554 — FROM \_ is misinterpreted in queries on non-default collections](https://jira.issues.couchbase.com/browse/CBL-8554)
* [CBL-8990 — Console log output doesn't follow the configured log levels](https://jira.issues.couchbase.com/browse/CBL-8990)
* [CBL-8948 — Document properties are dropped when their value matches a top-level \_ property](https://jira.issues.couchbase.com/browse/CBL-8948)
* [CBL-8862 — Replication with a PEM client certificate key fails with "PK - Invalid key tag or value"](https://jira.issues.couchbase.com/browse/CBL-8862)
* [CBL-8637 — Session authentication to Sync Gateway doesn't work when using auth.session\_cookie](https://jira.issues.couchbase.com/browse/CBL-8637)
* [CBL-9012 — Unredacted HTTP headers included in logs when verbose websocket logging enabled](https://jira.issues.couchbase.com/browse/CBL-9012)
* [CBL-9027 — Session cookie included in logs when verbose or info logging enabled](https://jira.issues.couchbase.com/browse/CBL-9027)

#### [](#known-issues)Known Issues

None for this release.

### [](#breaking-changes)Breaking Changes

None for this release.

### [](#deprecations)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Edge Server 1.1, see [New In 1.1](../introduction/whats-new.md)

## [](#maint-1-1-0)1.1.0 — June 2026

Version 1.1.0 of Couchbase Edge Server delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

None for this release.

### [](#issues-and-resolutions-2)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

* [CBL-8298 — Edge server logs not persisted if edge-server restarted](https://jira.issues.couchbase.com/browse/CBL-8298)
* [CBL-8365 — mTLS authentication between Edge Servers fails with mbedTLS error](https://jira.issues.couchbase.com/browse/CBL-8365)

#### [](#known-issues-2)Known Issues

None for this release.

### [](#breaking-changes-2)Breaking Changes

None for this release.

### [](#deprecations-2)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Edge Server 1.1, see [New In 1.1](../introduction/whats-new.md)

## [](#see-also)See Also

* [Product Notes](product-notes-landing.md)
* [Product Compatibility](compatibility.md)
* [Supported Platforms](supported-platforms.md)