---
title: Ottoman ODM Release Notes and Archives
description: Release notes, installation instructions, and download archive for
  the Ottoman ODM.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/project-docs/pages/ottoman-release-notes.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.3@nodejs-sdk:project-docs:ottoman-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/project-docs/ottoman-release-notes.html)

# Ottoman ODM Release Notes and Archives

> Release notes, installation instructions, and download archive for the Ottoman ODM. 

These pages cover the 2._x_ versions of the Ottoman ODM.

The Ottoman ODM will run on any [supported LTS version of Node.js](https://github.com/nodejs/Release).

## [](#version-2-5-8-9-july-2026)Version 2.5.8 (9 July 2026)

Version 2.5.8 is a patch release of the Ottoman ODM. This release updates vulnurable dependencies.

```console
$ npm install ottoman@2.5.8
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues)Fixed Issues

* Bumped project dependencies with reported vulnurabilities.

## [](#version-2-5-7-24-june-2026)Version 2.5.7 (24 June 2026)

Version 2.5.7 is a patch release of the Ottoman ODM. This release bumps the underlying Couchbase SDK to `v4.7.1`, and updates vulnurable dependencies.

```console
$ npm install ottoman@2.5.7
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-2)Fixed Issues

* Bumped underlying Couchbase SDK version to latest (4.7.1).
* Bumped other project dependencies with reported vulnurabilities.

## [](#version-2-5-6-7-april-2026)Version 2.5.6 (7 April 2026)

Version 2.5.6 is a patch release of the Ottoman ODM. This release bumps the underlying Couchbase SDK to `v4.7.0`, and updates vulnurable dependencies.

```console
$ npm install ottoman@2.5.6
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-3)Fixed Issues

* Bumped underlying Couchbase SDK version to latest (4.7.0).
* Bumped other project dependencies with reported vulnurabilities.

## [](#version-2-5-5-4-march-2026)Version 2.5.5 (4 March 2026)

Version 2.5.5 is a patch release of the Ottoman ODM. This release adds telemetry for tracking installs. It does not change the package's codebase or any functionality.

```console
$ npm install ottoman@2.5.5
```

[Ottoman installation](https://ottomanjs.com/#installation)

## [](#version-2-5-4-23-february-2026)Version 2.5.4 (23 February 2026)

Version 2.5.4 is a patch release of the Ottoman ODM. This release bumps the underlying Couchbase SDK to `v4.6.1`, and updates vulnurable dependencies.

```console
$ npm install ottoman@2.5.4
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-4)Fixed Issues

* Bumped underlying Couchbase SDK version to latest (4.6.1).
* Bumped other project dependencies with reported vulnurabilities.

## [](#version-2-5-3-20-october-2025)Version 2.5.3 (20 October 2025)

Version 2.5.3 is a patch release of the Ottoman ODM. This release bumps the underlying Couchbase SDK to `v4.6.0`.

```console
$ npm install ottoman@2.5.3
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-5)Fixed Issues

* Preserve null/undefined values instead of casting to unix timestamp in [#804](https://github.com/couchbaselabs/node-ottoman/pull/804)
* Bumped underlying Couchbase SDK version to latest.

## [](#version-2-5-2-16-may-2025)Version 2.5.2 (16 May 2025)

Version 2.5.2 is a patch release of the Ottoman ODM. This release bumps the underlying Couchbase SDK to `v4.4.6`.

```console
$ npm install ottoman@2.5.2
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-6)Fixed Issues

* Bump underlying Couchbase SDK version to latest.

## [](#version-2-5-1-22-november-2024)Version 2.5.1 (22 November 2024)

Version 2.5.1 is a patch release of the Ottoman ODM. This release adds asynchronous batch processing to ensure performant batch writes.

```console
$ npm install ottoman@2.5.1
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-7)Fixed Issues

* Replaced synchronous batch processing with asynchronous batch processing: [#790](https://github.com/couchbaselabs/node-ottoman/issues/790).

## [](#version-2-5-0-10-june-2024)Version 2.5.0 (10 June 2024)

Version 2.5.0 is a minor release of the Ottoman ODM. This release adds support for Transactions, fixes the issues listed below, and upgrades several underlying dependencies including the Couchbase SDK.

```console
$ npm install ottoman@2.5.0
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#new-features)New Features

* Adds Ottoman support for [Couchbase Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md).

### [](#fixed-issues-8)Fixed Issues

* Bumped `couchbase` dependency to `v4.3.1`.
* [#748](https://github.com/couchbaselabs/node-ottoman/issues/748), [#754](https://github.com/couchbaselabs/node-ottoman/issues/754), [#755](https://github.com/couchbaselabs/node-ottoman/issues/755), [#760](https://github.com/couchbaselabs/node-ottoman/issues/760): Minor documentation fixes.

## [](#version-2-4-0-23-january-2024)Version 2.4.0 (23 January 2024)

Version 2.4.0 is a minor release of the Ottoman ODM. This release adds support for Full Text Search, fixes an issue listed below, and upgrades several underlying dependencies.

```console
$ npm install ottoman@2.4.0
```

[Ottoman installation](https://ottomanjs.com/docs/intro#installation)

### [](#new-features-2)New Features

* Adds Ottoman support for [Couchbase Full Text Search](../../../server/current/search/search.md).

### [](#fixed-issues-9)Fixed Issues

* [#742](https://github.com/couchbaselabs/node-ottoman/issues/742): Fixed depopulating for nested objects.

## [](#version-2-3-4-1-august-2023)Version 2.3.4 (1 August 2023)

Version 2.3.4 is a patch release of the Ottoman ODM. This release upgrades several underlying dependencies and fixes a number of issues listed below.

```console
$ npm install ottoman@2.3.4
```

[Ottoman installation](https://ottomanjs.com/docs/intro#installation)

### [](#fixed-issues-10)Fixed Issues

* [#724](https://github.com/couchbaselabs/node-ottoman/issues/724): Added `undefined` to `stringType` Validator.
* [#726](https://github.com/couchbaselabs/node-ottoman/issues/726): Updated Merge Doc Behavior.
* [#728](https://github.com/couchbaselabs/node-ottoman/issues/728): Fixed query while using arrays indexes, e.g. `array[-1]` (last element).

## [](#version-2-3-3-4-april-2023)Version 2.3.3 (4 April 2023)

Version 2.3.3 is a patch release of the Ottoman ODM. This release fixes an issue with the ArrayType options to prevent them from being set to `undefined`.

```console
$ npm install ottoman@2.3.3
```

[Ottoman installation](https://ottomanjs.com/docs/intro#installation)

### [](#fixed-issues-11)Fixed Issues

* `ArrayType` not handling options correctly.

## [](#version-2-3-2-2-march-2023)Version 2.3.2 (2 March 2023)

Version 2.3.2 is a patch release of the Ottoman ODM. This release adds fixes and dependency upgrades. Ottoman can now be used by TypeScript users without setting the `skipLibCheck` flag. This release also adds documentation for automatic UUID generation.

```console
$ npm install ottoman@2.3.2
```

[Ottoman installation](https://ottomanjs.com/docs/intro#installation)

### [](#fixed-issues-12)Fixed Issues

* TypeScript no longer needs `skipLibCheck` flag.

## [](#version-2-3-1-2-march-2023)Version 2.3.1 (2 March 2023)

_Please do not use version 2.3.1._

## [](#version-2-3-0-19-december-2022)Version 2.3.0 (19 December 2022)

Version 2.3.0 is a minor release of the Ottoman ODM. This release adds fixes and dependency upgrades, including a major version upgrade to the `couchbase` dependency.

```console
$ npm install ottoman@2.3.0
```

[Ottoman installation](https://ottomanjs.com/docs/intro#installation)

### [](#fixed-issues-13)Fixed Issues

* Bumped `couchbase` dependency to `v4.2.0`.

### [](#important-configuration-change)Important Configuration Change

* This release includes a **major version bump** to the Couchbase dependency, and with it a specific change to handling SSL/TLS connections. If you were previously skipping certificate checking with the parameter `?ssl=no_verify` in your connection string, you'll need to update it to `?tls_verify=none`. More information can be found in [this article](https://developer.couchbase.com/tutorial-nodejs-tls-connection#tls-authentication-without-certificate-checking).

## [](#version-2-2-2-9-november-2022)Version 2.2.2 (9 November 2022)

Version 2.2.2 is a patch release of the Ottoman ODM. This release adds minor fixes and dependency upgrades, including a patch version upgrade to the `couchbase` dependency.

```console
$ npm install ottoman@2.2.2
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-14)Fixed Issues

* Bumped `couchbase` dependency to `v3.2.6`.

## [](#version-2-2-1-22-june-2022)Version 2.2.1 (22 June 2022)

Version 2.2.1 is a patch release of the Ottoman ODM. This release adds minor fixes, and a number of dependency upgrades.

```console
$ npm install ottoman@2.2.1
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#fixed-issues-15)Fixed Issues

* Updated index naming to include the model's name.
* `options.strict` is now set to true by default.
* A `DocumentNotFound` error is thrown for documents with a different model.
* Updated regex to ensure a clean index name.

## [](#version-2-2-0-29-march-2022)Version 2.2.0 (29 March 2022)

Version 2.2.0 is a minor release of the Ottoman ODM. This release adds two new features, and a number of dependency upgrades.

```console
$ npm install ottoman@2.2.0
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#new-features-3)New Features

* Ottoman: added support to allow `modelKey` to be a nested field.
* Hooks: trigger embed schema hooks.

## [](#version-2-1-0-7-feb-2022)Version 2.1.0 (7 Feb 2022)

Version 2.1.0 is a minor release of the Ottoman Object Document Mapper(ODM) library, bringing a number of improvements, and support for Couchbase Node.js SDK 3.2.4.

```console
$ npm install ottoman@2.1.0
```

[Ottoman installation](https://ottomanjs.com/#installation)

### [](#new-features-4)New Features

* Added ability to set `keyGeneratorDelimiter` to an empty string to use ID as key with no delimiter.
* Updated Couchbase Node.js SDK to version 3.2.4.

### [](#fixed-issues-16)Fixed Issues

* Fixed model inconsistency in find method.
* Bumped `shelljs` and `follow-redirects` dependencies.

### [](#documentation-fixes)Documentation Fixes

* Reword v1 docs note.

## [](#version-2-0-0-30-sept-2021)Version 2.0.0 (30 Sept 2021)

This is the first GA release of the Ottoman Object Document Mapper(ODM) library.

```console
$ npm install ottoman@2.0.0
```

[Ottoman page](https://ottomanjs.com/#installation)

### [](#new-features-5)New Features

* Exposed various SDK types to use directly from Ottoman.
* Added start option `ignoreWatchIndexes`. The `start()` function will wait for indexes by default, but this can be disabled by setting `ignoreWatchIndexes` to true.
* Enforced referenced document option.
* Ottoman now returns the document id reference if it doesn't exist.
* Added event to listen for index readiness.
* Added examples for find methods and bulk operations.
* Improved from clause value escape behavior in the QueryBuilder.
* Upgraded embedded Couchbase SDK to version `3.2.2`.

### [](#fixed-issues-17)Fixed Issues

* Refactored lean and populate code.
* Fixed broken links.
* Fixed model links for statics methods.

### [](#documentation-fixes-2)Documentation Fixes

* Fixed typo in the major word.
* Updated quickstart example.
* Updated getting started example.
* Updated docs for async connect function.
* Added metrics to Ottoman vs NodeJS SDK documentation.
* Updated FAQ benefits section.
* Fixed broken links to new sdk docs.
* Downgraded typedoc.
* Added api documentation for namespace.
* Update FAQ page.