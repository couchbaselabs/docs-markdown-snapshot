---
title: Couchbase Quarkus Release Notes
description: Release notes for the Couchbase Quarkus Java Extension.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Quarkus Java Extension
    version: "1.5"
antora:
  editUrl: https://github.com/couchbase/docs-quarkus-extension/edit/release/1.5/modules/ROOT/pages/release-notes.adoc
  xref: xref:quarkus-extension::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/quarkus-extension/current/release-notes.html)

# Couchbase Quarkus Release Notes

> Release notes for the Couchbase Quarkus Java Extension. 

## [](#couchbase-quarkus-1-5-releases)Couchbase Quarkus 1.5 Releases

### [](#version-1-5-0-30-october-2026)Version 1.5.0 (30 October 2026)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.5.0/index.html)

#### [](#new-features)New Features

* Added `ClusterEnvironmentCustomizer`. A CDI bean that implements it can set any `ClusterEnvironment` option that has no `quarkus.couchbase.*` property. For example, it can make the Reactive API publish results on an application scheduler with `publishOnScheduler`.

#### [](#improvements)Improvements

* Upgraded to Couchbase Java SDK `3.13.0`.
* Upgraded to `Quarkus` `3.40.1`. Quarkus Couchbase 1.5 needs Quarkus 3.40 or newer.
* Upgraded to Netty `4.1.138.Final` and Jackson `2.21.7` through Quarkus, which fix their published CVEs.
* Native mode now uses the Netty native-image configuration that ships with the Java SDK, instead of a copy kept in the extension.
* The DevService TestContainer now retries a failed start, up to 3 attempts.

## [](#couchbase-quarkus-1-4-releases)Couchbase Quarkus 1.4 Releases

### [](#version-1-4-1-8-july-2026)Version 1.4.1 (8 July 2026)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.4.1/index.html)

#### [](#improvements-2)Improvements

* Upgraded to `Quarkus` `3.36.3` (addresses [CVE-2026-50559](https://nvd.nist.gov/vuln/detail/CVE-2026-50559))

### [](#version-1-4-0-5-june-2026)Version 1.4.0 (5 June 2026)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.4.0/index.html)

#### [](#new-features-2)New Features

* Added an injectable `Bucket` bean.

#### [](#improvements-3)Improvements

* DevService TestContainer now ignores the connection-string (connection-string must _not_ be set in order to start the Couchbase container, as it's auto-contigured).
* Upgraded to `Quarkus` `3.36.0`.

## [](#couchbase-quarkus-1-3-releases)Couchbase Quarkus 1.3 Releases

### [](#version-1-3-0-27-february-2026)Version 1.3.0 (27 February 2026)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.3.0/index.html)

#### [](#new-features-3)New Features

* Added support for Dynamic Ports when using TestContainers.

#### [](#improvements-4)Improvements

* Upgraded to Couchbase Java SDK `3.10.1`.

## [](#couchbase-quarkus-1-2-releases)Couchbase Quarkus 1.2 Releases

### [](#version-1-2-0-24-october-2025)Version 1.2.0 (24 October 2025)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.2.0/index.html)

#### [](#new-features-4)New Features

* Added support for TLS connections in native-mode, either to Capella using the packaged certificate, or using a path to a custom certificate.

#### [](#improvements-5)Improvements

* Upgraded to Couchbase Java SDK `3.9.2`.
* Added additional security configuration options.

## [](#couchbase-quarkus-1-1-releases)Couchbase Quarkus 1.1 Releases

### [](#version-1-1-0-14-may-2025)Version 1.1.0 (14 May 2025)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.1.0/index.html)

#### [](#new-features-5)New Features

* Added a configuration item for `preferredServerGroup` to the `application.properties` file.

#### [](#improvements-6)Improvements

* Upgraded Couchbase Java SDK from `3.7.7` → `3.8.0`.
* Upgraded `metrics-micrometer` from `0.7.6` → `0.8.0`.
* Upgraded Quarkus from `3.17.5` → `3.20.0`.
* Upgraded `@ConfigMapping` to use the new `@ConfigRoot` (removed `AlegacyConfigRoot=true` compiler argument).
* Removed Graal compiler arguments from `native-image.properties` in favor of a `BuildStep`.

## [](#couchbase-quarkus-1-0-releases)Couchbase Quarkus 1.0 Releases

### [](#version-1-0-0-17-january-2025)Version 1.0.0 (17 January 2025)

[API Reference](https://javadoc.io/doc/io.quarkiverse.couchbase/quarkus-couchbase/1.0.0/index.html)

Initial GA release.