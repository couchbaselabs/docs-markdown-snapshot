---
title: Couchbase Quarkus Release Notes
description: Release notes for the Couchbase Quarkus Java Extension.
editUrl: https://github.com/couchbase/docs-quarkus-extension/edit/release/1.2/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:quarkus-extension::release-notes.adoc[]
---

[View original HTML](/quarkus-extension/current/release-notes.html)

# Couchbase Quarkus Release Notes

> Release notes for the Couchbase Quarkus Java Extension. 

## [](#couchbase-quarkus-1-2-releases)Couchbase Quarkus 1.2 Releases

### [](#version-1-2-0-24-october-2025)Version 1.2.0 (24 October 2025)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.2.0/index.html)

#### [](#new-features)New Features

* Added support for TLS connections in native-mode, either to Capella using the packaged certificate, or using a path to a custom certificate.

#### [](#improvements)Improvements

* Upgraded to Couchbase Java SDK `3.9.2`.
* Added additional security configuration options.

## [](#couchbase-quarkus-1-1-releases)Couchbase Quarkus 1.1 Releases

### [](#version-1-1-0-14-may-2025)Version 1.1.0 (14 May 2025)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.1.0/index.html)

#### [](#new-features-2)New Features

* Added a configuration item for `preferredServerGroup` to the `application.properties` file.

#### [](#improvements-2)Improvements

* Upgraded Couchbase Java SDK from 3.7.7 → 3.8.0
* Upgraded `metrics-micrometer` from 0.7.6 → 0.8.0
* Upgraded Quarkus from 3.17.5 → 3.20.0
* Upgraded `@ConfigMapping` to use the new `@ConfigRoot` (removed `AlegacyConfigRoot=true` compiler argument)
* Removed Graal compiler arguments from `native-image.properties` in favor of a `BuildStep`.

## [](#couchbase-quarkus-1-0-releases)Couchbase Quarkus 1.0 Releases

### [](#version-1-0-0-17-january-2025)Version 1.0.0 (17 January 2025)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.0.0/index.html)

Initial GA release.