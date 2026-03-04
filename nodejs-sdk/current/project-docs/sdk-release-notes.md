---
title: SDK Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Node.js Client.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.6/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-03-04T03:42:46.143Z
link: xref:nodejs-sdk:project-docs:sdk-release-notes.adoc[]
---

[View original HTML](/nodejs-sdk/current/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Node.js Client. 

These pages cover the 4._x_ and 3._x_ versions of the Couchbase Node.js SDK (both matching the 3.x SDK API, see the [compatibility page](compatibility.md#api-version)).

For release notes, download links, and installation methods for 2.6 and earlier releases of the Couchbase Node.js Client, please see the [2.x Node.js Release Notes & Download Archive](https://docs-archive.couchbase.com/nodejs-sdk/2.6/sdk-release-notes.html).

The Couchbase Node.js Client will run on any [supported LTS version of Node.js](https://github.com/nodejs/Release).

To install an older version, specify the version directly with npm. For example, to install version 4.5.0:

```console
$ npm install couchbase@4.5.0
```

## [](#latest-release)Node.js SDK 4.6 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-4-6-1-20-february-2026)Version 4.6.1 (20 February 2026)

Version 4.6.1 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.6.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-node-client-4.6.1/>

#### [](#enhancements)Enhancements

[JSCBC-1345](https://jira.issues.couchbase.com/browse/JSCBC-1345): Updated ESLint to `9.39.2`.

[JSCBC-1382](https://jira.issues.couchbase.com/browse/JSCBC-1382): Improved build scripts.

[JSCBC-1387](https://jira.issues.couchbase.com/browse/JSCBC-1387): Upgrade to `cmake-js` to `8.0`.

#### [](#known-issues)Known Issues

[JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.

[JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes)Underlying C++ SDK Core Changes

* [CXXCBC-768](https://jira.issues.couchbase.com/browse/CXXCBC-768): Prevent DNS-SRV refresh loop on `bucket_not_found` bootstrap errors ([#897](https://github.com/couchbase/couchbase-cxx-client/pull/897)).

### [](#version-4-6-0-29-september-2025)Version 4.6.0 (29 September 2025)

Version 4.6.0 is the next minor release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably the 4.6.0 release adds support for Vector Search pre-filters.

```bash
$ npm install couchbase@4.6.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-node-client-4.6.0/>

#### [](#behavioral-changes)Behavioral Changes

For operations that allow an expiry to be specifed, using a Unix timestamp (e.g. `Math.floor(Date.now() / 1000) + 100 // 100 seconds`) as an absolute value is not supported. If an absolute value is to be used, it should be `Date` object. Otherwise the expiry is interpreted as a number that represents the relative seconds from now.

The "auto" network selection heuristic in the underyling C++ core has been changed to fall back to the "external" network if the "external" network is present. Previously, if there was no exact match between an address in the connection string and an address in the cluster topology reported by the server, the SDK would select the "default" network. Now, if there is no match and an "external" network is present, the SDK selects the "external" network.

#### [](#enhancements-2)Enhancements

* [JSCBC-1329](https://jira.issues.couchbase.com/browse/JSCBC-1329): Added support "access\_deleted" for replica reads.
* [JSCBC-1330](https://jira.issues.couchbase.com/browse/JSCBC-1330): Updated supported bucket & storage types.
* [JSCBC-1342](https://jira.issues.couchbase.com/browse/JSCBC-1342): Added support for Vector Search pre-filters.
* [JSCBC-1353](https://jira.issues.couchbase.com/browse/JSCBC-1353): Updated operational SDK prevent connection to Analytics 2.0 Cluster.
* [JSCBC-1354](https://jira.issues.couchbase.com/browse/JSCBC-1354): Updated bucket management tests to handle new `numVBuckets` setting.
* [JSCBC-1358](https://jira.issues.couchbase.com/browse/JSCBC-1358): Updated SDK build setup to include C++ core changes.
* [JSCBC-1359](https://jira.issues.couchbase.com/browse/JSCBC-1359): Added Graviton 3 and 4 executors to test pipeline matrices.
* [JSCBC-1362](https://jira.issues.couchbase.com/browse/JSCBC-1362), [JSCBC-1363](https://jira.issues.couchbase.com/browse/JSCBC-1363): Added tracing, orphan and metrics configuration to `ConnectOptions`.

#### [](#fixes)Fixes

* [JSCBC-1357](https://jira.issues.couchbase.com/browse/JSCBC-1357): Fixed how client handles KV expiry.

#### [](#known-issues-2)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-2)Underlying C++ SDK Core Changes

##### [](#new-features)New Features

* [CXXCBC-653](https://jira.issues.couchbase.com/browse/CXXCBC-653): Added support "access\_deleted" for Replica Reads ([#821](https://github.com/couchbase/couchbase-cxx-client/pull/821)).
* [CXXCBC-639](https://jira.issues.couchbase.com/browse/CXXCBC-639): Added support of building both static and shared libraries ([#707](https://github.com/couchbase/couchbase-cxx-client/pull/707), [#825](https://github.com/couchbase/couchbase-cxx-client/pull/825)).
* [CXXCBC-692](https://jira.issues.couchbase.com/browse/CXXCBC-692): The SDK now prevents connection to Enterprise Analytics cluster ([#792](https://github.com/couchbase/couchbase-cxx-client/pull/792), [#807](https://github.com/couchbase/couchbase-cxx-client/pull/807), [#810](https://github.com/couchbase/couchbase-cxx-client/pull/810)).
* [CXXCBC-693](https://jira.issues.couchbase.com/browse/CXXCBC-693): Do not return an error if/when `indexDefs` are empty/null. Instead return w/ an empty list of index definitions ([#800](https://github.com/couchbase/couchbase-cxx-client/pull/800)).
* [CXXCBC-698](https://jira.issues.couchbase.com/browse/CXXCBC-698): Added `flex_index` to `transaction_query_options` ([#773](https://github.com/couchbase/couchbase-cxx-client/pull/773)).
* [CXXCBC-699](https://jira.issues.couchbase.com/browse/CXXCBC-699): Added support of randomization of bootstrap nodes ([#777](https://github.com/couchbase/couchbase-cxx-client/pull/777)).
* [CXXCBC-707](https://jira.issues.couchbase.com/browse/CXXCBC-707): Updated network selection heuristic. The logic is improved in certain cloud-specific cases ([#809](https://github.com/couchbase/couchbase-cxx-client/pull/809)).

##### [](#fixes-and-enhancements)Fixes and Enhancements

* [CXXCBC-651](https://jira.issues.couchbase.com/browse/CXXCBC-651): Added preserving cached node labels after generating report in app telemetry meter ([#802](https://github.com/couchbase/couchbase-cxx-client/pull/802)).
* [CXXCBC-695](https://jira.issues.couchbase.com/browse/CXXCBC-695): Always return unwrapped `doc_exists` from transactions insert (<https://github.com/couchbase/couchbase-cxx-client/pull/771>.\[#771.\]).
* [CXXCBC-704](https://jira.issues.couchbase.com/browse/CXXCBC-704): Added handling `document_unretrievable` from `get_multi` individual fetch ([#782](https://github.com/couchbase/couchbase-cxx-client/pull/782), [#785](https://github.com/couchbase/couchbase-cxx-client/pull/785)).
* [CXXCBC-706](https://jira.issues.couchbase.com/browse/CXXCBC-706): Added closing of half-baked cluster object if connection fails ([#783](https://github.com/couchbase/couchbase-cxx-client/pull/783)).
* [CXXCBC-709](https://jira.issues.couchbase.com/browse/CXXCBC-709): Fix `exists()` in transactions `get_multi` result ([#786](https://github.com/couchbase/couchbase-cxx-client/pull/786)).
* [CXXCBC-715](https://jira.issues.couchbase.com/browse/CXXCBC-715): Fixed Hard Failover Intermittent Crash in HTTP connection manager ([#818](https://github.com/couchbase/couchbase-cxx-client/pull/818)).
* [CXXCBC-721](https://jira.issues.couchbase.com/browse/CXXCBC-721): Added caching of `FeatureNotAvailable` transactions operation failure for `get_replica*` operations ([#823](https://github.com/couchbase/couchbase-cxx-client/pull/823)).
* [CXXCBC-726](https://jira.issues.couchbase.com/browse/CXXCBC-726): Added KV scan timeout to cluster options ([#830](https://github.com/couchbase/couchbase-cxx-client/pull/830)).
* [CXXCBC-733](https://jira.issues.couchbase.com/browse/CXXCBC-733): Fixed build with BoringSSL ([#839](https://github.com/couchbase/couchbase-cxx-client/pull/839)).

## [](#node-js-sdk-4-5-releases)Node.js SDK 4.5 Releases

### [](#version-4-5-1-29-september-2025)Version 4.5.1 (29 September 2025)

Version 4.5.1 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.5.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-node-client-4.5.1/>

#### [](#enhancements-3)Enhancements

* [JSCBC-1359](https://jira.issues.couchbase.com/browse/JSCBC-1359): Added Graviton 3 and 4 executors to test pipeline matrices.

#### [](#known-issues-3)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-3)Underlying C++ SDK Core Changes

##### [](#new-features-2)New Features

* [CXXCBC-699](https://jira.issues.couchbase.com/browse/CXXCBC-699): Added support of randomization of bootstrap nodes ([#778](https://github.com/couchbase/couchbase-cxx-client/pull/778)).

##### [](#fixes-and-enhancements-2)Fixes and Enhancements

* [CXXCBC-651](https://jira.issues.couchbase.com/browse/CXXCBC-651): Preserve cached node labels after generating report in app telemetry meter ([#804](https://github.com/couchbase/couchbase-cxx-client/pull/804)).
* [CXXCBC-693](https://jira.issues.couchbase.com/browse/CXXCBC-693): Do not return an error if/when `indexDefs` are empty/null. Instead return w/ an empty list of index definitions ([#801](https://github.com/couchbase/couchbase-cxx-client/pull/801)).
* [CXXCBC-709](https://jira.issues.couchbase.com/browse/CXXCBC-709): Fix `exists()` in transactions `get_multi` result ([#787](https://github.com/couchbase/couchbase-cxx-client/pull/787)).
* [CXXCBC-715](https://jira.issues.couchbase.com/browse/CXXCBC-715): Fixed intermittent crash during hard failover in HTTP connection manager ([\[#817](https://github.com/couchbase/couchbase-cxx-client/pull/817)).

### [](#version-4-5-0-02-june-2025)Version 4.5.0 (02 June 2025)

Version 4.5.0 is the next minor release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably the 4.5.0 release adds support for transactional Zone Aware Replica Reads and transactional GetMulti.

```bash
$ npm install couchbase@4.5.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-node-client-4.5.0/>

#### [](#enhancements-4)Enhancements

* [JSCBC-1273](https://jira.issues.couchbase.com/browse/JSCBC-1273): Added support for Node.js v22.
* [JSCBC-1300](https://jira.issues.couchbase.com/browse/JSCBC-1300), [JSCBC-1324](https://jira.issues.couchbase.com/browse/JSCBC-1324): Added support for SDK Telemetry Collection in Server.
* [JSCBC-1316](https://jira.issues.couchbase.com/browse/JSCBC-1316), [JSCBC-1317](https://jira.issues.couchbase.com/browse/JSCBC-1317): Added support for Transactional Zone Aware Read from Replica.
* [JSCBC-1327](https://jira.issues.couchbase.com/browse/JSCBC-1327), [JSCBC-1351](https://jira.issues.couchbase.com/browse/JSCBC-1347): Added support for transactions ExtGetMulti (aka Enhanced Read Committed Isolation).
* [JSCBC-1331](https://jira.issues.couchbase.com/browse/JSCBC-1331): Improved SDK error messages for account lock/unlock feature.
* [JSCBC-1340](https://jira.issues.couchbase.com/browse/JSCBC-1340): Converted `retry_reasons` representation in error to human-readable strings.
* [JSCBC-1343](https://jira.issues.couchbase.com/browse/JSCBC-1343): Fixed error context types to include missing fields specified in the RFC.
* [JSCBC-1347](https://jira.issues.couchbase.com/browse/JSCBC-1347): Added experimental use of the Electron runtime.

#### [](#fixes-2)Fixes

* [JSCBC-1301](https://jira.issues.couchbase.com/browse/JSCBC-1301), [JSCBC-1303](https://jira.issues.couchbase.com/browse/JSCBC-1303), [JSCBC-1334](https://jira.issues.couchbase.com/browse/JSCBC-1334), [JSCBC-1339](https://jira.issues.couchbase.com/browse/JSCBC-1339): Fixed StreamablePromise API to allow the returned promise to be awaited after a delay.
* [JSCBC-1322](https://jira.issues.couchbase.com/browse/JSCBC-1322), [JSCBC-1332](https://jira.issues.couchbase.com/browse/JSCBC-1332): Fixed subdoc operations from crashing if no specs are provided.
* [JSCBC-1325](https://jira.issues.couchbase.com/browse/JSCBC-1325): Fixed prebuild script to allow space-delimited options.
* [JSCBC-1333](https://jira.issues.couchbase.com/browse/JSCBC-1333): Fixed typo in ServerGroup test suite.
* [JSCBC-1335](https://jira.issues.couchbase.com/browse/JSCBC-1335): CAS is no longer ignored for append/prepend operations.
* [JSCBC-1341](https://jira.issues.couchbase.com/browse/JSCBC-1341): Console logger is now disabled when the file logger specified.
* [JSCBC-1344](https://jira.issues.couchbase.com/browse/JSCBC-1344): Fixed collection management `createCollection` operation to omit `maxExpiry` if not set.
* [JSCBC-1350](https://jira.issues.couchbase.com/browse/JSCBC-1350): Fixed transactional errors raised to application to be in line with the transactions RFC.

#### [](#known-issues-4)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-4)Underlying C++ SDK Core Changes

##### [](#new-features-3)New Features

* [CXXCBC-605](https://jira.issues.couchbase.com/browse/CXXCBC-605): Added custom log callback functionality ([#743](https://github.com/couchbase/couchbase-cxx-client/pull/743)).
* [CXXCBC-626](https://jira.issues.couchbase.com/browse/CXXCBC-626): Application Service Telemetry, for future Server releases ([#712](https://github.com/couchbase/couchbase-cxx-client/pull/712), [#719](https://github.com/couchbase/couchbase-cxx-client/pull/719), [#739](https://github.com/couchbase/couchbase-cxx-client/pull/739), [#750](https://github.com/couchbase/couchbase-cxx-client/pull/750)).
* [CXXCBC-654](https://jira.issues.couchbase.com/browse/CXXCBC-654): Added `num_vbuckets` to `bucket_settings` ([#746](https://github.com/couchbase/couchbase-cxx-client/pull/746)).
* [CXXCBC-665](https://jira.issues.couchbase.com/browse/CXXCBC-665): The SDK will now always return partial results for `*_all_replica` operations if some `get_replica` requests succeeded ([#742](https://github.com/couchbase/couchbase-cxx-client/pull/742)).
* [CXXCBC-672](https://jira.issues.couchbase.com/browse/CXXCBC-672): Added `add_named_parameter` and `add_positional_parameter` to query/analytics options ([#762](https://github.com/couchbase/couchbase-cxx-client/pull/762)).
* [CXXCBC-684](https://jira.issues.couchbase.com/browse/CXXCBC-684): The SDK now allows the setting of both named and positional parameters for queries — previously named parameters would be cleared if positional parameters were set ([#759](https://github.com/couchbase/couchbase-cxx-client/pull/759)).

##### [](#fixes-and-enhancements-3)Fixes and Enhancements

* [CXXCBC-646](https://jira.issues.couchbase.com/browse/CXXCBC-646): For performance reasons, the bucket configuration is now stored as shared pointer, and this is copied into the handler instead of the entire configuration ([#715](https://github.com/couchbase/couchbase-cxx-client/pull/715), [#720](https://github.com/couchbase/couchbase-cxx-client/pull/720)).
* [CXXCBC-657](https://jira.issues.couchbase.com/browse/CXXCBC-657): For subdoc operations, if no specs are provided then an `invalid_argument` error is raised instead of crashing on an assert ([#727](https://github.com/couchbase/couchbase-cxx-client/pull/727)).
* [CXXCBC-660](https://jira.issues.couchbase.com/browse/CXXCBC-660): Fixed potential race condition in the logger ([#722](https://github.com/couchbase/couchbase-cxx-client/pull/722)).
* [CXXCBC-661](https://jira.issues.couchbase.com/browse/CXXCBC-661): Reconnect cluster object on fork ([#724](https://github.com/couchbase/couchbase-cxx-client/pull/724)).
* [CXXCBC-694](https://jira.issues.couchbase.com/browse/CXXCBC-694): Handle case where requestID is missing from query response payload ([#768](https://github.com/couchbase/couchbase-cxx-client/pull/768)).

##### [](#transactions)Transactions

* [CXXCBC-645](https://jira.issues.couchbase.com/browse/CXXCBC-645), [CXXCBC-687](https://jira.issues.couchbase.com/browse/CXXCBC-687), [CXXCBC-689](https://jira.issues.couchbase.com/browse/CXXCBC-689): Implemented `get_multi_*` APIs for transactions ([#761](https://github.com/couchbase/couchbase-cxx-client/pull/761), [#764](https://github.com/couchbase/couchbase-cxx-client/pull/764), [#766](https://github.com/couchbase/couchbase-cxx-client/pull/766)).
* [CXXCBC-649](https://jira.issues.couchbase.com/browse/CXXCBC-649): Implemented `ExtReplaceBodyWithXattr` ([#752](https://github.com/couchbase/couchbase-cxx-client/pull/752)).
* [CXXCBC-681](https://jira.issues.couchbase.com/browse/CXXCBC-681): No longer storing entire `transaction_get_result` in staged mutations, reducing memory use ([#757](https://github.com/couchbase/couchbase-cxx-client/pull/757)).
* [CXXCBC-682](https://jira.issues.couchbase.com/browse/CXXCBC-682): Transaction replace/insert result now includes post-op content ([#756](https://github.com/couchbase/couchbase-cxx-client/pull/756)).
* [CXXCBC-683](https://jira.issues.couchbase.com/browse/CXXCBC-683): Transactions replace now uses CAS from given `TransactionsGetResult` when the document is a staged insert ([#763](https://github.com/couchbase/couchbase-cxx-client/pull/763)).
* [CXXCBC-688](https://jira.issues.couchbase.com/browse/CXXCBC-688): Don’t convert Public API TOF from lambda to Core API’s TOF, rely on internal state ([#765](https://github.com/couchbase/couchbase-cxx-client/pull/765)).
* [CXXCBC-690](https://jira.issues.couchbase.com/browse/CXXCBC-690): Don’t move `staged_mutation` item when capturing it in `commit_doc` lambdas ([#767](https://github.com/couchbase/couchbase-cxx-client/pull/767)).

## [](#node-js-sdk-4-4-releases)Node.js SDK 4.4 Releases

### [](#version-4-4-6-15-may-2025)Version 4.4.6 (15 May 2025)

Version 4.4.6 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.4.6
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-node-client-4.4.6/>

#### [](#enhancements-5)Enhancements

* [JSCBC-1347](https://jira.issues.couchbase.com/browse/JSCBC-1347): Added experimental use of the Electron runtime.
* [JSCBC-1348](https://jira.issues.couchbase.com/browse/JSCBC-1348): Updated transaction errors to provide more information in error messages.

#### [](#fixes-3)Fixes

* [JSCBC-1335](https://jira.issues.couchbase.com/browse/JSCBC-1335): CAS is no longer ignored for append/prepend operations.
* [JSCBC-1341](https://jira.issues.couchbase.com/browse/JSCBC-1341): Console logger is now disabled when the file logger is specified.
* [JSCBC-1344](https://jira.issues.couchbase.com/browse/JSCBC-1344): Fixed collection management `createCollection` operation to omit `maxExpiry` if not set.

#### [](#known-issues-5)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-5)Underlying C++ SDK Core Changes

##### [](#fixes-4)Fixes

* [CXXCBC-666](https://jira.issues.couchbase.com/browse/CXXCBC-666): The `pkg-config` file now returns the full path for the lib dir, instead of the relative path ([#736](https://github.com/couchbase/couchbase-cxx-client/pull/736)).
* [CXXCBC-667](https://jira.issues.couchbase.com/browse/CXXCBC-667): Core implementation of prepend/append now encodes the CAS value ([#738](https://github.com/couchbase/couchbase-cxx-client/pull/738)).
* [CXXCBC-671](https://jira.issues.couchbase.com/browse/CXXCBC-671): Updated snappy to support `CMake` `4.0` ([#745](https://github.com/couchbase/couchbase-cxx-client/pull/745)).

### [](#version-4-4-5-28-january-2025)Version 4.4.5 (28 January 2025)

Version 4.4.5 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@4.4.5
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-node-client-4.4.5/>

#### [](#enhancements-6)Enhancements

* [JSCBC-1308](https://jira.issues.couchbase.com/browse/JSCBC-1308), [JSCBC-1309](https://jira.issues.couchbase.com/browse/JSCBC-1309), [JSCBC-1310](https://jira.issues.couchbase.com/browse/JSCBC-1310), [JSCBC-1313](https://jira.issues.couchbase.com/browse/JSCBC-1313), [JSCBC-1314](https://jira.issues.couchbase.com/browse/JSCBC-1314), [JSCBC-1315](https://jira.issues.couchbase.com/browse/JSCBC-1315): Added improvments to CI integration tests.

#### [](#fixes-5)Fixes

* [JSCBC-1258](https://jira.issues.couchbase.com/browse/JSCBC-1258): Fixed cluster string representation to prevent printing out username and password.
* [JSCBC-1307](https://jira.issues.couchbase.com/browse/JSCBC-1307): Fixed SubDoc `MutateIn.decrement` to decrement instead of increment.
* [JSCBC-1311](https://jira.issues.couchbase.com/browse/JSCBC-1311), [JSCBC-1312](https://jira.issues.couchbase.com/browse/JSCBC-1312): Fixed `PromiseHelper` utility to prevent uncaught exception.
* [JSCBC-1318](https://jira.issues.couchbase.com/browse/JSCBC-1318): Fixed `LookupIn` replica methods to have correct option type and return type.

#### [](#known-issues-6)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-6)Underlying C++ SDK Core Changes

##### [](#enhancements-7)Enhancements

* [CXXCBC-638](https://jira.issues.couchbase.com/browse/CXXCBC-638): Switched SDK to use bundled `fmtlib` for `spdlog` ([#705](https://github.com/couchbase/couchbase-cxx-client/pull/705)).
* [CXXCBC-640](https://jira.issues.couchbase.com/browse/CXXCBC-640): Debug symbols are no longer forced for release builds ([#708](https://github.com/couchbase/couchbase-cxx-client/pull/708)).

##### [](#fixes-6)Fixes

* [CXXCBC-633](https://jira.issues.couchbase.com/browse/CXXCBC-633): In a case of timeout, when the total deadline of the DNS-SRV request has been reached, the library will now report a timeout error code, and not the latest abort as it was doing.

### [](#version-4-4-4-25-november-2024)Version 4.4.4 (25 November 2024)

Version 4.4.4 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.4.4
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-node-client-4.4.4/>

#### [](#enhancements-8)Enhancements

* [JSCBC-1261](https://jira.issues.couchbase.com/browse/JSCBC-1261): Support added for Binary Objects in Transactions.
* [JSCBC-1282](https://jira.issues.couchbase.com/browse/JSCBC-1282): Updated user management API to use C++ core.
* [JSCBC-1283](https://jira.issues.couchbase.com/browse/JSCBC-1283): Updated analytics index management API to use C++ core.
* [JSCBC-1284](https://jira.issues.couchbase.com/browse/JSCBC-1284): Added SDK3 Raw Transcoders.
* [JSCBC-1287](https://jira.issues.couchbase.com/browse/JSCBC-1287): Improved testing for User management APIs.
* [JSCBC-1288](https://jira.issues.couchbase.com/browse/JSCBC-1288): Improved testing for Analytics index management.
* [JSCBC-1302](https://jira.issues.couchbase.com/browse/JSCBC-1302): Unit tests added for the `PromiseHelper` utility class.
* [JSCBC-1304](https://jira.issues.couchbase.com/browse/JSCBC-1304): Updated user agent extra passed to C++ core.
* [JSCBC-1305](https://jira.issues.couchbase.com/browse/JSCBC-1305): Binary transactions can now use the `RawBinaryTranscoder`.
* [JSCBC-1297](https://jira.issues.couchbase.com/browse/JSCBC-1297), [JSCBC-1306](https://jira.issues.couchbase.com/browse/JSCBC-1306): Updated API Reference and README.

#### [](#fixes-7)Fixes

* [JSCBC-1286](https://jira.issues.couchbase.com/browse/JSCBC-1286): Added KV `RangeScan` to API Reference.
* [JSCBC-1289](https://jira.issues.couchbase.com/browse/JSCBC-1289): Analytics index management link connect/disconnect updated to match RFC.
* [JSCBC-1290](https://jira.issues.couchbase.com/browse/JSCBC-1290), [JSCBC-1291](https://jira.issues.couchbase.com/browse/JSCBC-1291), [JSCBC-1292](https://jira.issues.couchbase.com/browse/JSCBC-1292): Analytics index management link APIs now correctly return `InvalidArgumentError` rather than `CouchbaseError`.
* [JSCBC-1294](https://jira.issues.couchbase.com/browse/JSCBC-1294): User management APIs now correctly return `InvalidArgumentError` rather than `CouchbaseError`.
* [JSCBC-1295](https://jira.issues.couchbase.com/browse/JSCBC-1295): User management’s `upsertUser` was not being properly applied to all members of any groups passed to it. This has now been fixed.
* [JSCBC-1296](https://jira.issues.couchbase.com/browse/JSCBC-1296): User management `` getUser’s `passwordChanged `` field for an external user war returning an `Invalid Date`. The internal logic for this has been updated, with an undefined field now allowed, and the problem is fixed.
* [JSCBC-1298](https://jira.issues.couchbase.com/browse/JSCBC-1298): Removing the chained `promise.then().callback()` in `PromiseHelper` will now prevent the double invocation of the callback.

#### [](#known-issues-7)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.
* [JSCBC-1311](http://jira.issues.couchbase.com/browse/JSCBC-1311): `PromiseHelper` utility can trigger uncaught exception.

#### [](#underlying-c-sdk-core-changes-7)Underlying C++ SDK Core Changes

##### [](#fixes-8)Fixes

* [CXXCBC-611](https://jira.issues.couchbase.com/browse/CXXCBC-611), [CXXCBC-612](https://jira.issues.couchbase.com/browse/CXXCBC-612): The C++ SDK now follows RFC naming for metric operation names ([#695](https://github.com/couchbase/couchbase-cxx-client/pull/695)).
* [CXXCBC-615](https://jira.issues.couchbase.com/browse/CXXCBC-615): The C++ SDK now exposes `insert_raw` and `replace_raw` in the core transactions attempt context ([#686](https://github.com/couchbase/couchbase-cxx-client/pull/686)).
* [CXXCBC-620](https://jira.issues.couchbase.com/browse/CXXCBC-620): Updated core `analytics_link_get_all` to follow the RFC ([#687](https://github.com/couchbase/couchbase-cxx-client/pull/687)).
* [CXXCBC-624](https://jira.issues.couchbase.com/browse/CXXCBC-624): Fixed user agent ID generation ([#692](https://github.com/couchbase/couchbase-cxx-client/pull/692)).
* [CXXCBC-632](https://jira.issues.couchbase.com/browse/CXXCBC-632): A crash on testing against Analytics nodes under rebalance was caused by the assumption that Analytics would always send meta fields in its response. This has now been fixed, and the behoavior should not recur ([#699](https://github.com/couchbase/couchbase-cxx-client/pull/699)).

### [](#version-4-4-3-22-october-2024)Version 4.4.3 (22 October 2024)

Version 4.4.3 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.4.3
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.4.3/)

#### [](#fixes-9)Fixes

* [JSCBC-1281](https://jira.issues.couchbase.com/browse/JSCBC-1281): Updated C++ core to include fix to allow detection of dysfunctional node.

#### [](#enhancements-9)Enhancements

* [JSCBC-1280](https://jira.issues.couchbase.com/browse/JSCBC-1280): Added ability to use C++ core file logger.

#### [](#known-issues-8)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-8)Underlying C++ SDK Core Changes

##### [](#enhancements-10)Enhancements

* [CXXCBC-552](http://jira.issues.couchbase.com/browse/CXXCBC-582): Cleaned up network selection options ([#677](https://github.com/couchbase/couchbase-cxx-client/pull/677), [#682](https://github.com/couchbase/couchbase-cxx-client/pull/682)). Added cluster labels and system tag to spans. Added cluster labels, keyspace, and outcome to metrics.

##### [](#fixes-10)Fixes

* [CXXCBC-311](http://jira.issues.couchbase.com/browse/CXXCBC-311): Ensure SDK encodes URIs ([#674](https://github.com/couchbase/couchbase-cxx-client/pull/674)).
* [CXXCBC-599](http://jira.issues.couchbase.com/browse/CXXCBC-599): Updated allowed connection string options ([#668](https://github.com/couchbase/couchbase-cxx-client/pull/668)).
* [CXXCBC-606](http://jira.issues.couchbase.com/browse/CXXCBC-606): Fixed detection of dysfunctional node ([#673](https://github.com/couchbase/couchbase-cxx-client/pull/673)).
* [CXXCBC-614](http://jira.issues.couchbase.com/browse/CXXCBC-614): Fixed memory leak in `observe_poll` ([#679](https://github.com/couchbase/couchbase-cxx-client/pull/679)).

### [](#version-4-4-2-24-september-2024)Version 4.4.2 (24 September 2024)

Version 4.4.2 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.4.2
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.4.2/)

#### [](#fixes-11)Fixes

* [JSCBC-1252](https://jira.issues.couchbase.com/browse/JSCBC-1252): Fixed `npm install` failure after checking out couchnode for local development.

#### [](#enhancements-11)Enhancements

* [JSCBC-1272](https://jira.issues.couchbase.com/browse/JSCBC-1272): Updated prebuild processing to only allow supported runtimes.
* [JSCBC-1279](https://jira.issues.couchbase.com/browse/JSCBC-1279): Updated prebuild scripts.

#### [](#known-issues-9)Known Issues

* [JSCBC-1011](http://jira.issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://jira.issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-9)Underlying C++ SDK Core Changes

##### [](#fixes-12)Fixes

* [CXXCBC-577](http://jira.issues.couchbase.com/browse/CXXCBC-577), [CXXCBC-552](http://jira.issues.couchbase.com/browse/CXXCBC-552), & [CXXCBC-576](http://jira.issues.couchbase.com/browse/CXXCBC-576): See [C++ 1.0.2 release notes](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-2-23-september-2024).

### [](#version-4-4-1-23-august-2024)Version 4.4.1 (23 August 2024)

Version 4.4.1 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably the 4.4.1 release adds support for Alpine ARM environments (See the [OS Compatibility docs for details](compatibility.md#os-compatibility)).

```bash
$ npm install couchbase@4.4.1
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.4.1/)

#### [](#enhancements-12)Enhancements

* [JSCBC-1268](https://issues.couchbase.com/browse/JSCBC-1268): Added Support for Alpine ARM Prebuilds.

#### [](#known-issues-10)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-10)Underlying C++ SDK Core Changes

##### [](#enhancements-13)Enhancements

* Improved logging of DNS client ([#634](https://github.com/couchbase/couchbase-cxx-client/pull/634)).
* [CXXCBC-568](https://issues.couchbase.com/browse/CXXCBC-568/): Cancel deferred operations when closing HTTP session manager ([#643](https://github.com/couchbase/couchbase-cxx-client/pull/643)).

##### [](#fixes-13)Fixes

* [CXXCBC-531](https://issues.couchbase.com/browse/CXXCBC-531/): Fixed memory leak in range scan implementation ([#645](https://github.com/couchbase/couchbase-cxx-client/pull/645), [#610](https://github.com/couchbase/couchbase-cxx-client/pull/610)).
* [CXXCBC-572](https://issues.couchbase.com/browse/CXXCBC-572/): Always initialize service\_type ([#610](https://github.com/couchbase/couchbase-cxx-client/pull/610)).
* [CXXCBC-569](https://issues.couchbase.com/browse/CXXCBC-569/): Resolved cycle in shared pointers for `transaction_context`([#641](https://github.com/couchbase/couchbase-cxx-client/pull/641)).
* [CXXCBC-550](https://issues.couchbase.com/browse/CXXCBC-550/): Fixed use-after-move issue in command handler ([#628](https://github.com/couchbase/couchbase-cxx-client/pull/628)).
* Fixed behaviour when reading is complete before returning HTTP streaming resp ([#624](https://github.com/couchbase/couchbase-cxx-client/pull/624)).

### [](#version-4-4-0-27-june-2024)Version 4.4.0 (27 June 2024)

Version 4.4.0 is next minor release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably the 4.4.0 release adds support for base64 encoded vector types when using the SDK with Couchbase Server 7.6.2.

```bash
$ npm install couchbase@4.4.0
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.4.0/)

#### [](#fixes-14)Fixes

* [JSCBC-1263](https://issues.couchbase.com/browse/JSCBC-1263): Fixed `VectorQuery` validation to prevent empty `fieldName`.

#### [](#enhancements-14)Enhancements

* [JSCBC-1262](https://issues.couchbase.com/browse/JSCBC-1262): Added support for base64 encoded vector types.

#### [](#known-issues-11)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-11)Underlying C++ SDK Core Changes

##### [](#enhancements-15)Enhancements

* [CXXCBC-381](https://issues.couchbase.com/browse/CXXCBC-381): Updated `transactions_context` and `attempt_context` to use `std::shared_ptr` ([#590](https://github.com/couchbaselabs/couchbase-cxx-client/pull/590)).

##### [](#fixes-15)Fixes

* [CXXCBC-445](https://issues.couchbase.com/browse/CXXCBC-445): Updated HTTP session logic to return `request_canceled` on IO error ([#568](https://github.com/couchbaselabs/couchbase-cxx-client/pull/568)).
* [CXXCBC-511](https://issues.couchbase.com/browse/CXXCBC-511): Updated HTTP session logic to prevent use of session if idle timer has expired ([#565](https://github.com/couchbaselabs/couchbase-cxx-client/pull/565)).
* [CXXCBC-517](https://issues.couchbase.com/browse/CXXCBC-517): Added HTTP session retries when client fails to resolve hostnames ([#589](https://github.com/couchbaselabs/couchbase-cxx-client/pull/589)).
* [CXXCBC-518](https://issues.couchbase.com/browse/CXXCBC-518): Fixed preferred node logic to handle alternate addresses ([#574](https://github.com/couchbaselabs/couchbase-cxx-client/pull/574)).
* [CXXCBC-523](https://issues.couchbase.com/browse/CXXCBC-523): Cleaned up config log output when `dump_configuration` is enabled ([#577](https://github.com/couchbaselabs/couchbase-cxx-client/pull/577)).
* Fixed config poll to skip config fetch if bucket does not have any sessions ([#573](https://github.com/couchbaselabs/couchbase-cxx-client/pull/573)).
* Cleaned up `attempt_context_impl` implementation ([#586](https://github.com/couchbaselabs/couchbase-cxx-client/pull/586)).

## [](#node-js-sdk-4-3-releases)Node.js SDK 4.3 Releases

### [](#version-4-3-1-18-april-2024)Version 4.3.1 (18 April 2024)

Version 4.3.1 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.3.1
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.3.1/)

#### [](#behavioral-change)Behavioral Change

For operations that allow an expiry to be specifed, using a Unix timestamp (e.g. `Math.floor(Date.now() / 1000) + 100 // 100 seconds`) as an absolute value is not supported. The expiry is interpreted as a number that represents the relative seconds from now.

Version 4.6.0 addresses this behavioral change by allowing an absolute expiry to be represented by a `Date`.

#### [](#fixes-16)Fixes

* [JSCBC-1243](https://issues.couchbase.com/browse/JSCBC-1243): Fixed how the SDK handles binary documents within a transactions lambda.
* [JSCBC-1245](https://issues.couchbase.com/browse/JSCBC-1245): Fixed how the SDK handles the expiry value for mutation operations (if available for that operation).

#### [](#enhancements-16)Enhancements

* [JSCBC-1253](https://issues.couchbase.com/browse/JSCBC-1253): Added support for scoped eventing functions.

#### [](#known-issues-12)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-12)Underlying C++ SDK Core Changes

##### [](#enhancements-17)Enhancements

* [CXXCBC-470](https://issues.couchbase.com/browse/CXXCBC-470): Distinguish between 'unset' and 'off' query\_profile ([#551](https://github.com/couchbaselabs/couchbase-cxx-client/pull/551)).
* [CXXCBC-489](https://issues.couchbase.com/browse/CXXCBC-489): Added support for scoped eventing functions ([#548](https://github.com/couchbaselabs/couchbase-cxx-client/pull/548), ([#554](https://github.com/couchbaselabs/couchbase-cxx-client/pull/554))).

##### [](#fixes-17)Fixes

* [CXXCBC-30](https://issues.couchbase.com/browse/CXXCBC-30): Fixed inconsistent behavior when using subdoc opcodes ([#559](https://github.com/couchbaselabs/couchbase-cxx-client/pull/559)).
* [CXXCBC-487](https://issues.couchbase.com/browse/CXXCBC-487): Added logic during bootstrap to check if alternate addressing is being used ([#545](https://github.com/couchbaselabs/couchbase-cxx-client/pull/545)).
* [CXXCBC-492](https://issues.couchbase.com/browse/CXXCBC-492): Updated collection\_component get\_collection\_id to use retry strategy ([#552](https://github.com/couchbaselabs/couchbase-cxx-client/pull/552)).
* [CXXCBC-494](https://issues.couchbase.com/browse/CXXCBC-494): Fixed memory issue in range scan implementation ([#549](https://github.com/couchbaselabs/couchbase-cxx-client/pull/549)).
* [CXXCBC-503](https://issues.couchbase.com/browse/CXXCBC-503): Added logic to ignore configuration if it contains an empty vBucket map ([#556](https://github.com/couchbaselabs/couchbase-cxx-client/pull/556), [#558](https://github.com/couchbaselabs/couchbase-cxx-client/pull/558)).

### [](#version-4-3-0-14-march-2024)Version 4.3.0 (14 March 2024)

Version 4.3.0 is third minor release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably the 4.3.0 release adds support for Vector Search, KV Range Scans, and faster failover when using the SDK with Couchbase Server 7.6.0.

```bash
$ npm install couchbase@4.3.0
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.3.0/)

#### [](#known-issues-13)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Node.js SDK that contains C++ 1.0.0-dp.15 (or later).

#### [](#enhancements-18)Enhancements

* [JSCBC-1226](https://issues.couchbase.com/browse/JSCBC-1226): Added support for Vector Search.
* [JSCBC-1241](https://issues.couchbase.com/browse/JSCBC-1241): Updated C++ core for transactions metadata bucket improvements.
* [JSCBC-1251](https://issues.couchbase.com/browse/JSCBC-1251): Updated search API for SDK API 3.5 support.

#### [](#known-issues-14)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Node.js SDK that contains C++ 1.0.0-dp.15 (or later).
* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-13)Underlying C++ SDK Core Changes

* [CXXCBC-336](https://issues.couchbase.com/browse/CXXCBC-336): Updated DNS config to not fallback to 8.8.8.8 if SDK cannot obtain system DNS server ([#533](https://github.com/couchbaselabs/couchbase-cxx-client/pull/533)).
* [CXXCBC-461](https://issues.couchbase.com/browse/CXXCBC-461): Updated ping operation to not send to nodes that have not completed bootstrap ([#540](https://github.com/couchbaselabs/couchbase-cxx-client/pull/540)).
* [CXXCBC-462](https://issues.couchbase.com/browse/CXXCBC-462): Fixed hanging when specifying a custom metadata collection via the public API & expose errors ([#532](https://github.com/couchbaselabs/couchbase-cxx-client/pull/532)).
* [CXXCBC-479](https://issues.couchbase.com/browse/CXXCBC-479): Fixed capabilities check for replica LookupIn operations ([#537](https://github.com/couchbaselabs/couchbase-cxx-client/pull/537)).
* [CXXCBC-480](https://issues.couchbase.com/browse/CXXCBC-480): Fixed capabilities check for replica LookupIn operations ([#539](https://github.com/couchbaselabs/couchbase-cxx-client/pull/539)).
* [CXXCBC-481](https://issues.couchbase.com/browse/CXXCBC-481): Fixed potential crash when parsing search result hits ([#541](https://github.com/couchbaselabs/couchbase-cxx-client/pull/541)).
* [CXXCBC-482](https://issues.couchbase.com/browse/CXXCBC-482): Update range scan orchestrator to use best effort retry strategy by default ([#542](https://github.com/couchbaselabs/couchbase-cxx-client/pull/542)).

## [](#node-js-sdk-4-2-releases)Node.js SDK 4.2 Releases

### [](#version-4-2-11-1-march-2024)Version 4.2.11 (1 March 2024)

Version 4.2.11 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.11
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.11/)

#### [](#fixes-18)Fixes

* [JSCBC-1193](https://issues.couchbase.com/browse/JSCBC-1193): Fixed mutateIn sub-document \`MutateInMacro\`s.
* [JSCBC-1202](https://issues.couchbase.com/browse/JSCBC-1202): Updated `ViewQueryOptions` to include `full_set` and `raw` options.

#### [](#enhancements-19)Enhancements

* [JSCBC-1081](https://issues.couchbase.com/browse/JSCBC-1081): Updated Query Index Management Create Index Key Encoding.
* [JSCBC-1233](https://issues.couchbase.com/browse/JSCBC-1233): Added support for Scoped Search Indexes.
* [JSCBC-1195](https://issues.couchbase.com/browse/JSCBC-1195): Updated configuration logic when 0xd response is received.
* [JSCBC-1214](https://issues.couchbase.com/browse/JSCBC-1214): Fixed `ViewRow` parsing when handling results from C++ core.
* [JSCBC-1238](https://issues.couchbase.com/browse/JSCBC-1238): Updated view index management API to use C++ core.

#### [](#known-issues-15)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Node.js SDK that contains C++ 1.0.0-dp.15 (or later).
* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-14)Underlying C++ SDK Core Changes

* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Updated config polling to not use session that is not bootstrapped ([#528](https://github.com/couchbaselabs/couchbase-cxx-client/pull/528)).
* [CXXCBC-345](https://issues.couchbase.com/browse/CXXCBC-345): Added range scan improvements and resolved concurrency issues ([#525](https://github.com/couchbaselabs/couchbase-cxx-client/pull/525)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query operation to return `feature_not_available` if query preserve expiry is specified but is not supported on the server([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).
* [CXXCBC-431](https://issues.couchbase.com/browse/CXXCBC-431): Added check for history retention bucket capability in collection create/update ([#502](https://github.com/couchbaselabs/couchbase-cxx-client/pull/502), [#505](https://github.com/couchbaselabs/couchbase-cxx-client/pull/505)).
* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): Updated bootstrap logic to use addresses from the config to bootstrap bucket ([#516](https://github.com/couchbaselabs/couchbase-cxx-client/pull/516)).
* [CXXCBC-450](https://issues.couchbase.com/browse/CXXCBC-450): Updated bootstrap logic to reset bootstrap handler before re-bootstrap ([#524](https://github.com/couchbaselabs/couchbase-cxx-client/pull/524)).

  * We do not want any actions from old bootstrap handler once the session decided to re-bootstrap. For example, bucket could not be selected, but we might still get configuration responses before socket reset.
* [CXXCBC-452](https://issues.couchbase.com/browse/CXXCBC-452): Updated capabilities and fail fast when selected feature is not available. ([#522](https://github.com/couchbaselabs/couchbase-cxx-client/pull/522), [#513](https://github.com/couchbaselabs/couchbase-cxx-client/pull/513)).
* [CXXCBC-456](https://issues.couchbase.com/browse/CXXCBC-456): Updated configuration logic when 0x0d (`EConfigOnly`) status code is received to have the SDK request new configuration and send current operation to retry orchestrator ([#523](https://github.com/couchbaselabs/couchbase-cxx-client/pull/523)).

### [](#version-4-2-10-2-february-2024)Version 4.2.10 (2 February 2024)

Version 4.2.10 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.10
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.10/)

#### [](#enhancements-20)Enhancements

* [JSCBC-1227](https://issues.couchbase.com/browse/JSCBC-1227): Added support for `maxTTL` value of -1 for collection "no expiry".

#### [](#known-issues-16)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-15)Underlying C++ SDK Core Changes

* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Reduced network traffic when polling for cluster configuration ([#504](https://github.com/couchbaselabs/couchbase-cxx-client/pull/504)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query response to return `feature_not_available` when query preserve expiry is not supported ([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).
* [CXXCBC-422](https://issues.couchbase.com/browse/CXXCBC-422): Added insufficient credentials error code to common query error code conversion ([#511](https://github.com/couchbaselabs/couchbase-cxx-client/pull/511)).
* [CXXCBC-431](https://issues.couchbase.com/browse/CXXCBC-431): Added check for history retention bucket capability for collection create/update ([#502](https://github.com/couchbaselabs/couchbase-cxx-client/pull/502), [#505](https://github.com/couchbaselabs/couchbase-cxx-client/pull/505)).
* [CXXCBC-446](https://issues.couchbase.com/browse/CXXCBC-446): Improved log formatting ([#506](https://github.com/couchbaselabs/couchbase-cxx-client/pull/506), [#508](https://github.com/couchbaselabs/couchbase-cxx-client/pull/508), [#509](https://github.com/couchbaselabs/couchbase-cxx-client/pull/509)).

### [](#version-4-2-9-3-january-2024)Version 4.2.9 (3 January 2024)

Version 4.2.9 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.9
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.9/)

#### [](#enhancements-21)Enhancements

* [JSCBC-1163](https://issues.couchbase.com/browse/JSCBC-1163): Added improvements for Faster Failover and Config Push.
* [JSCBC-1221](https://issues.couchbase.com/browse/JSCBC-1221): Added support for new KV error code to raise `DocumentNotLockedError`.

#### [](#known-issues-17)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-16)Underlying C++ SDK Core Changes

* [CXXCBC-100](https://issues.couchbase.com/browse/CXXCBC-100): Added support for using a timeout with `ping` operation ([#486](https://github.com/couchbaselabs/couchbase-cxx-client/pull/486)).
* [CXXCBC-368](https://issues.couchbase.com/browse/CXXCBC-368): Added support for subscribing to clustermap notifications to speedup failover ([#490](https://github.com/couchbaselabs/couchbase-cxx-client/pull/490)).
* [CXXCBC-391](https://issues.couchbase.com/browse/CXXCBC-391): Fixed transactions API inconsistencies ([#482](https://github.com/couchbaselabs/couchbase-cxx-client/pull/482)).
* [CXXCBC-403](https://issues.couchbase.com/browse/CXXCBC-403): Updated `not_my_vbucket` KV response to allow retries ([#480](https://github.com/couchbaselabs/couchbase-cxx-client/pull/480)).
* [CXXCBC-404](https://issues.couchbase.com/browse/CXXCBC-404): Fixed `unlock` operations to expose `KV_LOCKED` status as `cas_mismatch` ([#479](https://github.com/couchbaselabs/couchbase-cxx-client/pull/479)).
* [CXXCBC-409](https://issues.couchbase.com/browse/CXXCBC-409): Added handling for `index does not exist` query error ([#492](https://github.com/couchbaselabs/couchbase-cxx-client/pull/492)).
* [CXXCBC-419](https://issues.couchbase.com/browse/CXXCBC-419): Updated MCBP protocol parser to start with clean state ([#496](https://github.com/couchbaselabs/couchbase-cxx-client/pull/496)).

### [](#version-4-2-8-15-november-2023)Version 4.2.8 (15 November 2023)

Version 4.2.8 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably, the 4.2.8 release removes the `OpenSSL` dependency for published prebuilds.

```bash
$ npm install couchbase@4.2.8
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.8/)

#### [](#behavioral-change-2)Behavioral Change

The Couchbase Node.js SDK now publishes prebuilt binaries that statically link against BoringSSL. The change removes the `OpenSSL` requirement from the SDK when using a published prebuild. If building the SDK from source, the build will default to statically linking with the `OpenSSL` provided from the Node.js version being used. Build options are availalbe if wanting to build from source and statically link against BoringSSL.

#### [](#fixes-19)Fixes

* [JSCBC-1187](https://issues.couchbase.com/browse/JSCBC-1187): Fixed connstr `trust_store_path` override if `trustStorePath` is not provided in `ConnectOptions`.
* [JSCBC-1194](https://issues.couchbase.com/browse/JSCBC-1194): Fixed transactions `QueryMode` KV insert.

#### [](#enhancements-22)Enhancements

* [JSCBC-1203](https://issues.couchbase.com/browse/JSCBC-1203): Updated published source tarball to only include necessary files for source install.
* [JSCBC-1200](https://issues.couchbase.com/browse/JSCBC-1200): Updated published prebuilds to statically link against BoringSSL.
* [JSCBC-1189](https://issues.couchbase.com/browse/JSCBC-1189): Fixed CRUD tests that have callback.
* [JSCBC-1185](https://issues.couchbase.com/browse/JSCBC-1185): Added support for bucket settings for 'no dedup' feature.
* [JSCBC-1179](https://issues.couchbase.com/browse/JSCBC-1179): Reduced default HTTP Idle Timeout.
* [JSCBC-1016](https://issues.couchbase.com/browse/JSCBC-1016): Removed subdocument exists workaround.

#### [](#known-issues-18)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

#### [](#underlying-c-sdk-core-changes-17)Underlying C++ SDK Core Changes

* [CXXCBC-387](https://issues.couchbase.com/browse/CXXCBC-387): Optimising tags for `noop_tracer` and cache formatted `mbcp_session` endpoints ([#461](https://github.com/couchbaselabs/couchbase-cxx-client/pull/461), [#462](https://github.com/couchbaselabs/couchbase-cxx-client/pull/462), [#464](https://github.com/couchbaselabs/couchbase-cxx-client/pull/464)).
* [CXXCBC-383](https://issues.couchbase.com/browse/CXXCBC-383): Map `subdoc_doc_too_deep` KV status to `path_too_deep` error code ([#455](https://github.com/couchbaselabs/couchbase-cxx-client/pull/455)).
* [CXXCBC-377](https://issues.couchbase.com/browse/CXXCBC-377): Implement `ExtParallelUnstaging` in transactions ([#457](https://github.com/couchbaselabs/couchbase-cxx-client/pull/457)).
* [CXXCBC-386](https://issues.couchbase.com/browse/CXXCBC-386): Allow option to statically link against BoringSSL ([#458](https://github.com/couchbaselabs/couchbase-cxx-client/pull/458), [#465](https://github.com/couchbaselabs/couchbase-cxx-client/pull/465), [#471](https://github.com/couchbaselabs/couchbase-cxx-client/pull/471), [#474](https://github.com/couchbaselabs/couchbase-cxx-client/pull/474), [#478](https://github.com/couchbaselabs/couchbase-cxx-client/pull/478)).
* [CXXCBC-376](https://issues.couchbase.com/browse/CXXCBC-376): Revisit what 'create' and 'update' bucket operations send to the server. Make optional bucket settings fields optional, and do not send anything unless the settings explicitly specified ([#451](https://github.com/couchbaselabs/couchbase-cxx-client/pull/451)).
* [CXXCBC-374](https://issues.couchbase.com/browse/CXXCBC-374): Return 'bucket\_exists' error when the bucket already exists during 'create' operation ([#449](https://github.com/couchbaselabs/couchbase-cxx-client/pull/449)).
* [CXXCBC-359](https://issues.couchbase.com/browse/CXXCBC-359): Reduced the default timeout for idle HTTP connections to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures ([#448](https://github.com/couchbaselabs/couchbase-cxx-client/pull/448)).
* [CXXCBC-367](https://issues.couchbase.com/browse/CXXCBC-367); [CXXCBC-370](https://issues.couchbase.com/browse/CXXCBC-370): Added history retention settings to buckets/collection management ([#446](https://github.com/couchbaselabs/couchbase-cxx-client/pull/446)).
* [CXXCBC-119](https://issues.couchbase.com/browse/CXXCBC-119): Return booleans for subdocument 'exists' operation instead of error code ([#444](https://github.com/couchbaselabs/couchbase-cxx-client/pull/444), [#452](https://github.com/couchbaselabs/couchbase-cxx-client/pull/452)).
* Add more information to diagnose timeouts on NMVB responses ([#475](https://github.com/couchbaselabs/couchbase-cxx-client/pull/475)).

### [](#version-4-2-7-25-august-2023)Version 4.2.7 (25 August 2023)

Version 4.2.7 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.7
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.7/)

#### [](#enhancements-23)Enhancements

* [JSCBC-1162](https://issues.couchbase.com/browse/JSCBC-1162): Added support for Sub-Document Read from Replica.

#### [](#underlying-c-sdk-core-changes-18)Underlying C++ SDK Core Changes

* [CXXCBC-362](https://issues.couchbase.com/browse/CXXCBC-362): Removed node hostname port stripping logic from config parsing ([#438](https://github.com/couchbaselabs/couchbase-cxx-client/pull/438)).
* [CXXCBC-340](https://issues.couchbase.com/browse/CXXCBC-340): Added support for Query Read from Replica ([#435](https://github.com/couchbaselabs/couchbase-cxx-client/pull/435)).
* [CXXCBC-341](https://issues.couchbase.com/browse/CXXCBC-341), [CXXCBC-365](https://issues.couchbase.com/browse/CXXCBC-365): Added support for Sub-Document Read from Replica ([#436](https://github.com/couchbaselabs/couchbase-cxx-client/pull/436), [#441](https://github.com/couchbaselabs/couchbase-cxx-client/pull/441), [#443](https://github.com/couchbaselabs/couchbase-cxx-client/pull/443)).

#### [](#known-issues-19)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-2-6-8-august-2023)Version 4.2.6 (8 August 2023)

Version 4.2.6 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.6
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.6/)

#### [](#fixes-20)Fixes

* [JSCBC-1160](https://issues.couchbase.com/browse/JSCBC-1160): Fixed WAN Config profile to use system defaults for DNS configuration.
* [JSCBC-1174](https://issues.couchbase.com/browse/JSCBC-1174): Fixed Node.js v18 linux prebuilds to use glibc 2.28.

#### [](#enhancements-24)Enhancements

* [JSCBC-1104](https://issues.couchbase.com/browse/JSCBC-1104): Added support for Native KV Range Scans.
* [JSCBC-1161](https://issues.couchbase.com/browse/JSCBC-1161): Added support for Query with Read from Replica.
* [JSCBC-1177](https://issues.couchbase.com/browse/JSCBC-1177): Added CONTRIBUTING.md to provide contributing guidelines.

#### [](#underlying-c-sdk-core-changes-19)Underlying C++ SDK Core Changes

* [CXXCBC-349](https://issues.couchbase.com/browse/CXXCBC-349): Allow to pass trust certificate by value ([#430](https://github.com/couchbaselabs/couchbase-cxx-client/pull/430)).

  * The change affects TLS v1.0 and v1.1 which are now disabled by default.
* [CXXCBC-343](https://issues.couchbase.com/browse/CXXCBC-343): Continue bootsrap if DNS-SRV resolution fails ([#422](https://github.com/couchbaselabs/couchbase-cxx-client/pull/422)).
* [CXXCBC-340](https://issues.couchbase.com/browse/CXXCBC-340): Support Query with Read from Replica ([#429](https://github.com/couchbaselabs/couchbase-cxx-client/pull/429)).
* [CXXCBC-339](https://issues.couchbase.com/browse/CXXCBC-339): Disabled older TLS protocols ([#418](https://github.com/couchbaselabs/couchbase-cxx-client/pull/418)).
* [CXXCBC-333](https://issues.couchbase.com/browse/CXXCBC-333): Fixed parsing 'resolv.conf' on Linux. ([#416](https://github.com/couchbaselabs/couchbase-cxx-client/pull/416)).

  * The library might not ignore trailing characters when reading nameserver address from the file.
* [CXXCBC-242](https://issues.couchbase.com/browse/CXXCBC-242): SDK Support for Native KV Range Scans ([#419](https://github.com/couchbaselabs/couchbase-cxx-client/pull/419), [#423](https://github.com/couchbaselabs/couchbase-cxx-client/pull/423), [#424](https://github.com/couchbaselabs/couchbase-cxx-client/pull/424), [#426](https://github.com/couchbaselabs/couchbase-cxx-client/pull/426), [#428](https://github.com/couchbaselabs/couchbase-cxx-client/pull/428), [#431](https://github.com/couchbaselabs/couchbase-cxx-client/pull/431), [#432](https://github.com/couchbaselabs/couchbase-cxx-client/pull/432), [#433](https://github.com/couchbaselabs/couchbase-cxx-client/pull/433), [#434](https://github.com/couchbaselabs/couchbase-cxx-client/pull/434)).

#### [](#known-issues-20)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-2-5-11-july-2023)Version 4.2.5 (11 July 2023)

Version 4.2.5 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably the 4.2.5 release adds support for Node.js v18 and v20, and reduces the size of prebuilt binaries.

```bash
$ npm install couchbase@4.2.5
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.5/)

#### [](#enhancements-25)Enhancements

* [JSCBC-1109](https://issues.couchbase.com/browse/JSCBC-1109): Reduced the size of prebuilt binaries.
* [JSCBC-1149](https://issues.couchbase.com/browse/JSCBC-1149): Updated build system to download Node.js headers when using cmake-js >= v7.0.
* [JSCBC-1150](https://issues.couchbase.com/browse/JSCBC-1150): Updated Windows build system to download node.lib when using cmake-js >= v7.0.
* [JSCBC-1152](https://issues.couchbase.com/browse/JSCBC-1152): Added support for Node.js v18.
* [JSCBC-1170](https://issues.couchbase.com/browse/JSCBC-1170): Added support for Node.js v20.

#### [](#known-issues-21)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-2-4-26-may-2023)Version 4.2.4 (26 May 2023)

Version 4.2.4 is the next patch release of the fourth generation Node.js SDK.

```bash
$ npm install couchbase@4.2.4
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.4/)

#### [](#enhancements-26)Enhancements

* [JSCBC-1158](https://issues.couchbase.com/browse/JSCBC-1158): Bundled Mozilla certificates with the library. Source: <https://curl.se/docs/caextract.html>. Use the `disable_mozilla_ca_certificates` connection string option to disable the bundled certificates. See [Secure Connections](https://docs.couchbase.com/nodejs-sdk/current/howtos/managing-connections.html#ssl) for more details.

#### [](#underlying-c-sdk-core-changes-20)Underlying C++ SDK Core Changes

* [CXXCBC-328](https://issues.couchbase.com/browse/CXXCBC-328): Fix socket reconnection during rebalance process ([#406](https://github.com/couchbaselabs/couchbase-cxx-client/pull/406)).

  * Several improvements have been implemented to make the library resilient to rapid topology changes when both DNS-SRV bootstrap is being used along with alternative addresses. The changes include:

    * Taking into account alternative hostname and ports during detection of added/removed nodes on configuration update.
    * Replacing node index tracking with hostname/port matching when restarting the connections — this way the library ensures that no duplicate connections will be left, or live connections replaced by restarted session.
    * Improved logging of critial events during rebalance: restarting, preservation, and removing connections.

#### [](#known-issues-22)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-2-3-9-may-2023)Version 4.2.3 (9 May 2023)

Version 4.2.3 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.3
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.3/)

#### [](#enhancements-27)Enhancements

* [JSCBC-1154](https://issues.couchbase.com/browse/JSCBC-1154): Exposed C++ client metadata (open SSL info, txns info, etc.) as `cbppMetadata`, for use by client applications — particularly useful when working through environment setup issues.

#### [](#underlying-c-sdk-core-changes-21)Underlying C++ SDK Core Changes

* [CXXCBC-324](https://issues.couchbase.com/browse/CXXCBC-324): Port and network name now checked on session restart, improving performance during rebalance ([#401](https://github.com/couchbaselabs/couchbase-cxx-client/pull/401)).
* [CXXCBC-323](https://issues.couchbase.com/browse/CXXCBC-323): `bootstrap_timeout` and `resolve_timeout` can now be used in the connection string ([#400](https://github.com/couchbaselabs/couchbase-cxx-client/pull/400)).
* Introduce `dump_configuration` for debugging: ([#398](https://github.com/couchbaselabs/couchbase-cxx-client/pull/398)).
* [CXXCBC-31](https://issues.couchbase.com/browse/CXXCBC-31): Allow the use of schemaless connection strings (e.g. `"cb1.example.com,cb2.example.com"`) ([#394](https://github.com/couchbaselabs/couchbase-cxx-client/pull/394)).
* [CXXCBC-320](https://issues.couchbase.com/browse/CXXCBC-320): Negative expiry in atr was leaving docs in a stuck state — this has been fixed, with expiry atr now becoming an `int32_t`([#393](https://github.com/couchbaselabs/couchbase-cxx-client/pull/393)).
* [CXXCBC-318](https://issues.couchbase.com/browse/CXXCBC-318): Always try TCP if UDP fails in DNS-SRV resolver ([#390](https://github.com/couchbaselabs/couchbase-cxx-client/pull/390)).
* [CXXCBC-145](https://issues.couchbase.com/browse/CXXCBC-145): Search query request raw option now used ([#380](https://github.com/couchbaselabs/couchbase-cxx-client/pull/380)).
* [CXXCBC-144](https://issues.couchbase.com/browse/CXXCBC-144): Search query on collections now no longer requires `scope_name`, as it can be inferred from the index ([#379](https://github.com/couchbaselabs/couchbase-cxx-client/pull/379)).

#### [](#known-issues-23)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-2-2-9-march-2023)Version 4.2.2 (9 March 2023)

Version 4.2.2 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.2
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.2/)

#### [](#fixes-21)Fixes

* [JSCBC-1141](https://issues.couchbase.com/browse/JSCBC-1141): Fixed Query Index Management `watchIndexes` to raise `QueryIndexNotFound` if provided index(es) not found.

#### [](#enhancements-28)Enhancements

* [JSCBC-1118](https://issues.couchbase.com/browse/JSCBC-1118): Updated the SDK to handle new `query_context` changes.
* [JSCBC-1137](https://issues.couchbase.com/browse/JSCBC-1137): Created `CppClusterCredentials` and `CppDnsConfig` interfaces for use in connecting.
* [JSCBC-1129](https://issues.couchbase.com/browse/JSCBC-1129): Updated the SDK to only populate `allowed_sasl_mechanisms` if user explicitly chooses.

#### [](#known-issues-24)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-2-1-8-february-2023)Version 4.2.1 (8 February 2023)

Version 4.2.1 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements. Most notably the 4.2.1 release provides improved performance for key-value operations.

```bash
$ npm install couchbase@4.2.1
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.1/)

#### [](#fixes-22)Fixes

* [JSCBC-1106](https://issues.couchbase.com/browse/JSCBC-1106): Changed search response `fields` and `explain` to be object types.
* [JSCBC-1117](https://issues.couchbase.com/browse/JSCBC-1117): Fixed how callback is handled when passed to key-value operations if no options object is provided.
* [JSCBC-1124](https://issues.couchbase.com/browse/JSCBC-1124): Fixed configuration profile implementation.
* [JSCBC-1126](https://issues.couchbase.com/browse/JSCBC-1126): Added mutation token to MutateInResult.

#### [](#enhancements-29)Enhancements

* [JSCBC-1079](https://issues.couchbase.com/browse/JSCBC-1079): Implemented `ChangePassword` feature in user management API.
* [JSCBC-1123](https://issues.couchbase.com/browse/JSCBC-1123): Updated C++ core to include patch fixing OpenSSL and multithreading.

#### [](#known-issues-25)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-2-0-3-november-2022)Version 4.2.0 (3 November 2022)

Version 4.2.0 is the next minor release of the fourth generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@4.2.0
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.2.0/)

#### [](#fixes-23)Fixes

* [JSCBC-1105](https://issues.couchbase.com/browse/JSCBC-1105): Fixed crash caused when undefined named parameter provided in query options.
* [JSCBC-1107](https://issues.couchbase.com/browse/JSCBC-1107): Fixed mutation token construction.
* [JSCBC-1108](https://issues.couchbase.com/browse/JSCBC-1108): Added support for consistentWith query option.

#### [](#enhancements-30)Enhancements

* [JSCBC-926](https://issues.couchbase.com/browse/JSCBC-926): Added Support for Serverless Execution Environments
* [JSCBC-1006](https://issues.couchbase.com/browse/JSCBC-1006): Removed collection exists operation workaround.

#### [](#known-issues-26)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

## [](#node-js-sdk-4-1-releases)Node.js SDK 4.1 Releases

### [](#version-4-1-3-6-october-2022)Version 4.1.3 (6 October 2022)

Version 4.1.3 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@4.1.3
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.1.3/)

#### [](#fixes-24)Fixes

* [JSCBC-1094](https://issues.couchbase.com/browse/JSCBC-1094): Added transactions exception bindings.
* [JSCBC-1098](https://issues.couchbase.com/browse/JSCBC-1098): Fixed incorrect Authentication Error Type raised.
* [JSCBC-1101](https://issues.couchbase.com/browse/JSCBC-1101): Fixed `CreateBucket`/`GetBucket` APIs to match spec.

#### [](#enhancements-31)Enhancements

* [JSCBC-1099](https://issues.couchbase.com/browse/JSCBC-1099): Updated Node.js SDK to included latests Couchbase++ client changes.
* [JSCBC-1100](https://issues.couchbase.com/browse/JSCBC-1100): Added support for Configuration Profiles.
* [JSCBC-1041](https://issues.couchbase.com/browse/JSCBC-1041): Added support for replica reads.
* [JSCBC-1042](https://issues.couchbase.com/browse/JSCBC-1042): Added support for legacy durable operations.
* [JSCBC-1096](https://issues.couchbase.com/browse/JSCBC-1096): Added support for LDAP authentication.

#### [](#known-issues-27)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.

### [](#version-4-1-2-4-august-2022)Version 4.1.2 (4 August 2022)

Version 4.1.2 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@4.1.2
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.1.2/)

#### [](#new-features-4)New Features

* [JSCBC-1088](http://issues.couchbase.com/browse/JSCBC-1088): Switched to using NAPI prebuilds rather than Node.js version specific prebuilds. This enables prebuild compatibility with a wider range of Node.js versions, including Node.js 18 and in-development versions such as Node.js 19.

#### [](#fixed-issues)Fixed Issues

* [JSCBC-1092](http://issues.couchbase.com/browse/JSCBC-1092): Fixed queries being executed as prepared instead of adhoc by default.
* [JSCBC-1054](http://issues.couchbase.com/browse/JSCBC-1054): Fixed issue with UTF-8 handling of binary documents.
* Updated to latest dependencies.

#### [](#known-issues-28)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.
* [JSCBC-1041](http://issues.couchbase.com/browse/JSCBC-1041): Replica reads are not yet supported.
* [JSCBC-1042](http://issues.couchbase.com/browse/JSCBC-1042): Legacy durability operations are not yet supported.

### [](#version-4-1-1-13-june-2022)Version 4.1.1 (13 June 2022)

Version 4.1.1 is the next patch release of the fourth generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@4.1.1
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.1.1/)

#### [](#fixed-issues-2)Fixed Issues

* Updated to latest dependencies.

#### [](#known-issues-29)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.
* [JSCBC-1041](http://issues.couchbase.com/browse/JSCBC-1041): Replica reads are not yet supported.
* [JSCBC-1042](http://issues.couchbase.com/browse/JSCBC-1042): Legacy durability operations are not yet supported.

### [](#version-4-1-0-28-april-2022)Version 4.1.0 (28 April 2022)

Version 4.1.0 is the next minor release of the fourth generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@4.1.0
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.1.0/)

#### [](#new-features-5)New Features

* [JSCBC-956](http://issues.couchbase.com/browse/JSCBC-956): Added ability to manage collection query indexes.

#### [](#fixed-issues-3)Fixed Issues

* [JSCBC-1045](http://issues.couchbase.com/browse/JSCBC-1045): Added missing mutate\_in path flag values from C++ library.
* [JSCBC-1044](http://issues.couchbase.com/browse/JSCBC-1044): Fixed issue with double-encoding of search queries.
* [JSCBC-1067](http://issues.couchbase.com/browse/JSCBC-1067): Fixed issue with query parameters being double-encoded.
* [JSCBC-1058](http://issues.couchbase.com/browse/JSCBC-1058): Switched to using auto-generated bindings.
* Fixed issue with durable operations not using user timeouts.
* Fixed issue with creating indexes with no conditions.
* Mark all new SDK 3.4 APIs as committed.
* Updated to latest dependencies.
* Various minor fixes.

#### [](#known-issues-30)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.
* [JSCBC-1041](http://issues.couchbase.com/browse/JSCBC-1041): Replica reads are not yet supported.
* [JSCBC-1042](http://issues.couchbase.com/browse/JSCBC-1042): Legacy durability operations are not yet supported.

## [](#node-js-sdk-4-0-releases)Node.js SDK 4.0 Releases

### [](#version-4-0-0-18-february-2022)Version 4.0.0 (18 February 2022)

Version 4.0.0 is the first major release of the next generation Node.js SDK, built on the Couchbase C++ library — featuring multi-document distributed ACID transactions, and bringing a number of improvements related to internal connection behaviour.

```console
$ npm install couchbase@4.0.0
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-4.0.0/)

#### [](#new-features-6)New Features

* Cluster options are now sectioned into individual options blocks.
* Support for distributed transactions has now been implemented.
* Reimplemented the library using C++ SDK.

#### [](#fixed-issues-4)Fixed Issues

* [JSCBC-878](http://issues.couchbase.com/browse/JSCBC-878): Diagnostics functions now returned fully typed results.
* [JSCBC-1007](http://issues.couchbase.com/browse/JSCBC-1007): first\_error\_message/first\_error\_code are no longer available on error contexts.
* Search scan consistency included RequestPlus in error and it has now been removed.
* Performing a GET operation against a locked document now retries internally.
* The view query reduce option used to take a string in error, and now takes a boolean.
* Following with Node.js EOL, v12 is now the minimum version.

#### [](#known-issues-31)Known Issues

* [JSCBC-1011](http://issues.couchbase.com/browse/JSCBC-1011): Core IO logging is not forwarded through to Node.js.
* [JSCBC-1040](http://issues.couchbase.com/browse/JSCBC-1040): Distributed tracing is not yet supported.
* [JSCBC-1041](http://issues.couchbase.com/browse/JSCBC-1041): Replica reads are not yet supported.
* [JSCBC-1042](http://issues.couchbase.com/browse/JSCBC-1042): Legacy durability operations are not yet supported.
* [JSCBC-1044](https://issues.couchbase.com/browse/JSCBC-1044): Double-encoding issue when performing search queries.

## [](#node-js-sdk-3-2-releases)Node.js SDK 3.2 Releases

### [](#version-3-2-7-8-february-2023)Version 3.2.7 (8 February 2023)

Version 3.2.7 is the next patch release of the third generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@3.2.7
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.7/)

#### [](#enhancements-32)Enhancements

* [JSCBC-1120](https://issues.couchbase.com/browse/JSCBC-1120): Updated libcouchbase dependency to 3.3.4

### [](#version-3-2-6-9-november-2022)Version 3.2.6 (9 November 2022)

Version 3.2.6 is the next patch release of the third generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@3.2.6
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.6/)

#### [](#fixes-25)Fixes

* [JSCBC-1113](https://issues.couchbase.com/browse/JSCBC-1113): Fixed Segfault when connecting to Capella with Ottoman

### [](#version-3-2-5-3-november-2022)Version 3.2.5 (3 November 2022)

Version 3.2.5 is the next patch release of the third generation Node.js SDK, bringing a number of improvements.

```bash
$ npm install couchbase@3.2.5
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.5/)

#### [](#fixes-26)Fixes

* [JSCBC-971](https://issues.couchbase.com/browse/JSCBC-971): Fixed bucket manager `minDurabilityLevel` parsing failure on Couchbase Server 6.5.
* [JSCBC-976](https://issues.couchbase.com/browse/JSCBC-976): Fixed searchIndexes.getIndexedDocumentsCount() result.
* [JSCBC-986](https://issues.couchbase.com/browse/JSCBC-986): Added missing durability level option for binary operations.
* [JSCBC-1018](https://issues.couchbase.com/browse/JSCBC-1018): Updated to the latest libcouchbase version.
* [JSCBC-1019](https://issues.couchbase.com/browse/JSCBC-1019): Updated dependancies to pick up critical fixes.
* [JSCBC-1046](https://issues.couchbase.com/browse/JSCBC-1046): Fixed build system for Windows environments.

#### [](#enhancements-33)Enhancements

* [JSCBC-969](https://issues.couchbase.com/browse/JSCBC-969): Updated FTS Rate Limit Parsing.
* [JSCBC-982](https://issues.couchbase.com/browse/JSCBC-982): Resolved vulnerability in dependencies (prebuild-install/simple-get).
* [JSCBC-1020](https://issues.couchbase.com/browse/JSCBC-1020): Setup black duck scans for v3 after v4 ships to master.
* [JSCBC-718](https://issues.couchbase.com/browse/JSCBC-718): Added support for Linux Alpine OS.

### [](#version-3-2-4-17-december-2021)Version 3.2.4 (17 December 2021)

Version 3.2.4 is the next patch release of the third generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@3.2.4
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.4/)

#### [](#fixed-issues-5)Fixed Issues

* [JSCBC-923](http://issues.couchbase.com/browse/JSCBC-923): Implemented FTS `includeLocations` and match operators.
* [JSCBC-919](http://issues.couchbase.com/browse/JSCBC-919): Added support for XDCR custom conflict resolution.
* [JSCBC-955](http://issues.couchbase.com/browse/JSCBC-955): Implemented `storageBackend` option in bucket management.
* [JSCBC-921](http://issues.couchbase.com/browse/JSCBC-921): Added support for rate and quota limiting errors.
* [JSCBC-967](http://issues.couchbase.com/browse/JSCBC-967): Use correct arguments indices for options.
* Fixed crash that could occur during the shutdown of the Node.js runtime.
* Improved handling of initial connection process.
* Improved some tests to work more reliably.

### [](#version-3-2-3-5-october-2021)Version 3.2.3 (5 October 2021)

Version 3.2.3 is the next patch release of the third generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@3.2.3
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.3/modules.html)

#### [](#new-features-7)New Features

* [JSCBC-930](http://issues.couchbase.com/browse/JSCBC-930): Added support for AWS Graviton2.

#### [](#fixed-issues-6)Fixed Issues

* [JSCBC-954](http://issues.couchbase.com/browse/JSCBC-954): Fixed `getAllScopes` using the incorrect method.
* [JSCBC-952](http://issues.couchbase.com/browse/JSCBC-952): Updated the tsconfig targeting to use the pre-defined Node 10 target, which will avoid various unnecessary polyfills.
* [JSCBC-951](http://issues.couchbase.com/browse/JSCBC-951): Fixed view query serialization of booleans.

### [](#version-3-2-2-16-sept-2021)Version 3.2.2 (16 Sept 2021)

Version 3.2.2 is the next patch release of the third generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@3.2.2
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.2/modules.html)

#### [](#new-features-8)New Features

* [JSCBC-805](http://issues.couchbase.com/browse/JSCBC-805): Users can now manage the Couchbase Eventing Service from the Node.js SDK client.
* [JSCBC-894](http://issues.couchbase.com/browse/JSCBC-894): Updated SSL failure error messaging to improve debugging experience.

#### [](#fixed-issues-7)Fixed Issues

* [JSCBC-937](http://issues.couchbase.com/browse/JSCBC-937): Fixed segfault during connection GC.
* [JSCBC-938](http://issues.couchbase.com/browse/JSCBC-938): Fixed segfault during v8 interpreter shutdown.
* [JSCBC-939](http://issues.couchbase.com/browse/JSCBC-939): Fixed segfault related to logging after shutdown.
* [JSCBC-949](http://issues.couchbase.com/browse/JSCBC-949): Fixed query getAllIndexes and watchIndexes to work with collection indexes.
* [JSCBC-948](http://issues.couchbase.com/browse/JSCBC-948): Corrected issue with diagnostics calls failing on brand new connections.
* [JSCBC-945](http://issues.couchbase.com/browse/JSCBC-945): Fixed some methods failing to parse optional callbacks correctly.
* Updated libcouchbase to include the following fixes: [CCBC-1494](https://issues.couchbase.com/browse/CCBC-1494), [CCBC-1487](https://issues.couchbase.com/browse/CCBC-1487), [CCBC-1488](https://issues.couchbase.com/browse/CCBC-1488).

### [](#version-3-2-1-26-aug-2021)Version 3.2.1 (26 Aug 2021)

Version 3.2.1 is the next patch release of the third generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@3.2.1
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.1/modules.html)

#### [](#new-features-9)New Features

* [JSCBC-744](http://issues.couchbase.com/browse/JSCBC-744): Added support for worker threads.

#### [](#fixed-issues-8)Fixed Issues

* [JSCBC-910](http://issues.couchbase.com/browse/JSCBC-910): Fixed segfault on connection GC.
* [JSCBC-933](http://issues.couchbase.com/browse/JSCBC-933): Fixed issue with null/undefined logger callbacks.
* [JSCBC-918](http://issues.couchbase.com/browse/JSCBC-918): Fixed issue with `watchIndexes` not returning.
* [JSCBC-913](http://issues.couchbase.com/browse/JSCBC-913): Fixed issue with incorrect role names being returned from user management APIs.
* [JSCBC-911](http://issues.couchbase.com/browse/JSCBC-911): Fixed `MutateInSpec.insert` options not being optional.
* [JSCBC-905](http://issues.couchbase.com/browse/JSCBC-905): Fixed drop collection returning `FeatureNotAvailable` in error.
* Updated all dependencies to latest versions.
* Updated to libcouchbase 3.2.1.

### [](#version-3-2-0-21-july-2021)Version 3.2.0 (21 July 2021)

Version 3.2.0 is the next minor release of the third generation Node.js SDK, bringing a number of improvements.

```console
$ npm install couchbase@3.2.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client-3.2.0/modules.html)

#### [](#new-features-10)New Features

* [JSCBC-883](http://issues.couchbase.com/browse/JSCBC-883): Reimplemented the library with TypeScript.
* [JSCBC-806](http://issues.couchbase.com/browse/JSCBC-806): Added ability to specify collections to search query.
* [JSCBC-886](http://issues.couchbase.com/browse/JSCBC-886): Added ability to specify raw search query options.
* [JSCBC-770](http://issues.couchbase.com/browse/JSCBC-770), [JSCBC-838](http://issues.couchbase.com/browse/JSCBC-838): Implemented metrics and tracing.
* [JSCBC-707](http://issues.couchbase.com/browse/JSCBC-707): Added test to confirm query streaming works properly.
* [JSCBC-900](http://issues.couchbase.com/browse/JSCBC-900): Fixed issue with some search query options.
* [JSCBC-901](http://issues.couchbase.com/browse/JSCBC-901): Added workaround for deferring HTTP operations.
* [JSCBC-858](http://issues.couchbase.com/browse/JSCBC-858): Fixed issue where FeatureNotAvailable was thrown in error.
* [JSCBC-903](http://issues.couchbase.com/browse/JSCBC-903): Fixed issue with incorrect subdocument macro value.
* [JSCBC-832](http://issues.couchbase.com/browse/JSCBC-832): Implemented preserveExpiry functionality.
* [JSCBC-762](http://issues.couchbase.com/browse/JSCBC-762): Added support for managing analytics remote links.
* [JSCBC-763](http://issues.couchbase.com/browse/JSCBC-763): Added support for compound data-verse names.

#### [](#fixed-issues-9)Fixed Issues

* [JSCBC-870](http://issues.couchbase.com/browse/JSCBC-870): Updated mutateIn to use StoreSemantics.
* [JSCBC-876](http://issues.couchbase.com/browse/JSCBC-876): Fixed BucketSettings evictionPolicy naming.
* [JSCBC-871](http://issues.couchbase.com/browse/JSCBC-871): Fixed issue where unhandled exceptions could be thrown.
* [JSCBC-860](http://issues.couchbase.com/browse/JSCBC-860): Fixed issue with flushEnabled not being retrieved correctly.
* [JSCBC-829](http://issues.couchbase.com/browse/JSCBC-829): Fixed segfault on failed management operations.
* [JSCBC-825](http://issues.couchbase.com/browse/JSCBC-825): Fixed definition of search facets in queries.
* [JSCBC-873](http://issues.couchbase.com/browse/JSCBC-873): Renamed GetResult.expiry to GetResult.expiryTime to match spec.
* [JSCBC-869](http://issues.couchbase.com/browse/JSCBC-869): Updated Unlock not to return a Result, it is never valid.
* [JSCBC-872](http://issues.couchbase.com/browse/JSCBC-872): Updated CouchbaseSet remove to use the correct CAS.
* [JSCBC-875](http://issues.couchbase.com/browse/JSCBC-875): Fixed watchIndexes using the wrong argument number.
* [JSCBC-836](http://issues.couchbase.com/browse/JSCBC-836): Fixed property name for configuring bucket replica count.
* [JSCBC-863](http://issues.couchbase.com/browse/JSCBC-863): Added additional tests for cas mismatch errors.
* [JSCBC-864](http://issues.couchbase.com/browse/JSCBC-864): Fixed issue with error handling in LookupIn and MutateIn.
* [JSCBC-862](http://issues.couchbase.com/browse/JSCBC-862): Fixed export typo causing failed query index manager construction.
* [JSCBC-882](http://issues.couchbase.com/browse/JSCBC-882): Added missing getAllScopes method to CollectionManager.
* [JSCBC-811](http://issues.couchbase.com/browse/JSCBC-811): Updated scopes/collections APIs to match latest specification.
* Added deprecation warning to calling Cluster constructor.
* Fixed deprecation warning caused by callback invocation.
* Added Mac arm64 config to allow test builds with M1.
* Fixed issue where bucket manager tests would fail in error.
* Fixed issue with test cleanup handling.
* Refactored LookupInMacro / MutateInMacro to work better with TypeScript.
* Fixed HTTP errors not containing context in some cases.
* Fixed some IndexMissing errors appearing as undefined errors.
* Fixed UserManager parsing of User objects.
* Fixed UserManager parsing of ldapGroupReference field.
* Fixed chaining of the MutationState.add method.
* Refactored all tests to properly pass lint checks with Typescript.
* Rewrote documentation to integrate with Typescript.
* Switched to using typedoc rather than jsdoc.
* Deprecated Node.js 8 support as it is now EOL.
* Updated all dependencies to latest versions.
* Updated to the latest Typescript version.
* Updated to libcouchbase 3.2.0.

## [](#node-js-sdk-3-1-releases)Node.js SDK 3.1 Releases

### [](#version-3-1-3-5-may-2021)Version 3.1.3 (5 May 2021)

Version 3.1.3 is a patch release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.1.3
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.1.3/)

#### [](#fixed-issues-10)Fixed Issues

* [JSCBC-884](http://issues.couchbase.com/browse/JSCBC-884): Fixed a number of memory access issues.
* [JSCBC-881](http://issues.couchbase.com/browse/JSCBC-881): Fixed memory leak due to missing cell dereferences.
* Updated to libcouchbase 3.1.2.
* Updated all dependencies to latest versions.

### [](#version-3-1-2-9-april-2021)Version 3.1.2 (9 April 2021)

Version 3.1.2 is a release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.1.2
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.1.2/)

#### [](#fixed-issues-11)Fixed Issues

* [JSCBC-856](http://issues.couchbase.com/browse/JSCBC-856): Fixed memory leak with trace span management.
* [JSCBC-850](http://issues.couchbase.com/browse/JSCBC-850): Fixed some connection options not propagating to bucket connections.
* [JSCBC-849](http://issues.couchbase.com/browse/JSCBC-849): Fixed some query errors returning the incorrect errors.
* Updated to libcouchbase 3.1.0.
* Updated all dependencies to latest versions.

### [](#version-3-1-1-13-january-2021)Version 3.1.1 (13 January 2021)

Version 3.1.1 is a release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.1.1
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.1.1/)

#### [](#fixed-issues-12)Fixed Issues

* [JSCBC-835](http://issues.couchbase.com/browse/JSCBC-835): Deprecated maxTTL in favor of maxExpiry.
* [JSCBC-834](http://issues.couchbase.com/browse/JSCBC-834): Fixed createCollection not working with default expiry.
* [JSCBC-824](http://issues.couchbase.com/browse/JSCBC-824): Added missing options docs for Increment/Decrement.
* [JSCBC-828](http://issues.couchbase.com/browse/JSCBC-828): Fixed view-query 0 limit queries.
* [JSCBC-823](http://issues.couchbase.com/browse/JSCBC-823): Fixed serialization of views docid fields.
* [JSCBC-822](http://issues.couchbase.com/browse/JSCBC-822): Fixed view ordering behaviour.
* Updated to libcouchbase 3.0.7.
* Updated all dependencies to latest versions.

### [](#version-3-1-0-2-december-2020)Version 3.1.0 (2 December 2020)

Version 3.1.0 is a minor release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release, and adding features to support Couchbase Server 6.6.

```console
$ npm install couchbase@3.1.0
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.1.0/)

#### [](#new-features-11)New Features

* [JSCBC-761](http://issues.couchbase.com/browse/JSCBC-761): Added support for specifying minimum bucket durability.
* [JSCBC-787](http://issues.couchbase.com/browse/JSCBC-787): Added option to disable search scoring.

#### [](#fixed-issues-13)Fixed Issues

* [JSCBC-820](http://issues.couchbase.com/browse/JSCBC-820): Reduced calls to debug.extend.
* [JSCBC-772](http://issues.couchbase.com/browse/JSCBC-772): Added missing partition information to query indexes.
* [JSCBC-818](http://issues.couchbase.com/browse/JSCBC-818): Fixed issue where analytics query context was not sent.
* [JSCBC-812](http://issues.couchbase.com/browse/JSCBC-812): Updated CollectionManager to throw errors when collections are not supported.
* [JSCBC-816](http://issues.couchbase.com/browse/JSCBC-816): Fix cluster errors not propagating for http methods.
* [JSCBC-815](http://issues.couchbase.com/browse/JSCBC-815): Fixed seg-fault due to re-using consumed va\_list.
* Various documentation updates.
* Updated typescript definitions file.
* Updated all dependencies to latest versions.

## [](#node-js-sdk-3-0-releases)Node.js SDK 3.0 Releases

### [](#version-3-0-7-6-november-2020)Version 3.0.7 (6 November 2020)

Version 3.0.7 is a release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.0.7
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.7/)

#### [](#new-features-12)New Features

* [JSCBC-773](http://issues.couchbase.com/browse/JSCBC-773): Added query collections support.
* [JSCBC-803](http://issues.couchbase.com/browse/JSCBC-803): Added support for pinging at a cluster level.

#### [](#fixed-issues-14)Fixed Issues

* [JSCBC-692](http://issues.couchbase.com/browse/JSCBC-692): Updated transcoders to bubble errors.
* [JSCBC-799](http://issues.couchbase.com/browse/JSCBC-799): Improved error handling for deferred operations.
* [JSCBC-756](http://issues.couchbase.com/browse/JSCBC-756): Updated xattr helpers to be consistent.
* [JSCBC-755](http://issues.couchbase.com/browse/JSCBC-755): Added support for multi-value sub-document array ops.
* [JSCBC-821](http://issues.couchbase.com/browse/JSCBC-821): Added missing MutationState implementation.
* [JSCBC-797](http://issues.couchbase.com/browse/JSCBC-797): Resolved a number of typescript typings errors.
* [JSCBC-724](http://issues.couchbase.com/browse/JSCBC-724): Added a test case to confirm queries also cancel.
* Added docs and types generation to `make check`.
* Various minor documentation updates.
* Updated to libcouchbase 3.0.6
* Updated all dependencies to latest versions.

### [](#version-3-0-6-3-september-2020)Version 3.0.6 (3 September 2020)

Version 3.0.6 is a release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.0.6
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.6/)

#### [](#new-features-13)New Features

* [JSCBC-786](http://issues.couchbase.com/browse/JSCBC-786): Added uncommitted collections support for user management.
* [JSCBC-743](http://issues.couchbase.com/browse/JSCBC-743): Added high-level options for basic configuration.
* [JSCBC-788](http://issues.couchbase.com/browse/JSCBC-788): Added high-level options for specifying certificates.
* [JSCBC-686](http://issues.couchbase.com/browse/JSCBC-686): Added auto generation of TypeScript types using JSDoc.

#### [](#fixed-issues-15)Fixed Issues

* [JSCBC-784](http://issues.couchbase.com/browse/JSCBC-784): Fixed some results using value instead of content.
* [JSCBC-758](http://issues.couchbase.com/browse/JSCBC-758): Improved view scan consistency handling.
* Updated to libcouchbase 3.0.4.
* Updated all dependencies to latest versions.
* Various minor documentation updates.
* Various other minor fixes.

### [](#version-3-0-5-6-august-2020)Version 3.0.5 (6 August 2020)

Version 3.0.5 is a release of the third generation Node.js SDK.

```console
$ npm install couchbase@3.0.5
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.5/)

#### [](#fixed-issues-16)Fixed Issues

* Updated all dependencies to latest versions.
* Various minor documentation fixes.

### [](#version-3-0-4-17-june-2020)Version 3.0.4 (17 June 2020)

Version 3.0.4 is a release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.0.4
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.4/)

#### [](#fixed-issues-17)Fixed Issues

* [JSCBC-759](http://issues.couchbase.com/browse/JSCBC-759): Fixed binary data being interpreted as UTF-8.

### [](#version-3-0-3-14-june-2020)Version 3.0.3 (14 June 2020)

Version 3.0.3 is a release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.0.3
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.3/)

#### [](#fixed-issues-18)Fixed Issues

* [JSCBC-702](http://issues.couchbase.com/browse/JSCBC-702): Fixed MaxExpiry not being specifiable when creating a collection.
* [JSCBC-757](http://issues.couchbase.com/browse/JSCBC-757): Fixed CreateCollection parameters not matching specification.
* [JSCBC-698](http://issues.couchbase.com/browse/JSCBC-698): Fixed MutateIn placeholders not being handled correctly.
* [JSCBC-751](http://issues.couchbase.com/browse/JSCBC-751): Fixed documentation of SearchIndexManager.
* [JSCBC-754](http://issues.couchbase.com/browse/JSCBC-754): Don’t swap in a bucket name when none is used.
* Updated all dependencies to latest versions.
* Updated to libcouchbase 3.0.2
* Various other minor fixes.

#### [](#known-issues-32)Known Issues

* [JSCBC-759](http://issues.couchbase.com/browse/JSCBC-759): Buffer objects containing non-UTF8 data can become mangled when inserting them into a bucket or collection. This has been corrected in 3.0.4.

### [](#version-3-0-2-7-may-2020)Version 3.0.2 (7 May 2020)

Version 3.0.2 is a release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.0.2
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.2/)

#### [](#fixed-issues-19)Fixed Issues

* [JSCBC-715](http://issues.couchbase.com/browse/JSCBC-715): Fixed issue with sending highlight option with Search queries.
* [JSCBC-727](http://issues.couchbase.com/browse/JSCBC-727): Fixed views API to use correct casing on parameter names.
* [JSCBC-676](http://issues.couchbase.com/browse/JSCBC-676): Fixed view queries to return expected row object data.
* [JSCBC-728](http://issues.couchbase.com/browse/JSCBC-728): Fixed user management sometimes failing to deserialize users.
* [JSCBC-729](http://issues.couchbase.com/browse/JSCBC-729): Fixed user management user upsert not sending roles.
* [JSCBC-730](http://issues.couchbase.com/browse/JSCBC-730): Fixed lookupIn method to return content not results.
* [JSCBC-714](http://issues.couchbase.com/browse/JSCBC-714): Fixed mutateIn not including counter results in return object.
* [JSCBC-700](http://issues.couchbase.com/browse/JSCBC-700): Fixed issue with analytics named parameters causing query failures.
* [JSCBC-701](http://issues.couchbase.com/browse/JSCBC-701): Fixed custom search query timeouts causing query failures.
* Updated all dependencies to latest versions.
* Updated to libcouchbase 3.0.1
* Various other minor fixes.

#### [](#known-issues-33)Known Issues

* [JSCBC-759](http://issues.couchbase.com/browse/JSCBC-759): Buffer objects containing non-UTF8 data can become mangled when inserting them into a bucket or collection. This has been corrected in 3.0.4.

### [](#version-3-0-1-20-march-2020)Version 3.0.1 (20 March 2020)

Version 3.0.1 is the second release of the third generation Node.js SDK, bringing enhancements and bugfixes over the last stable release.

```console
$ npm install couchbase@3.0.1
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.1/)

#### [](#new-features-14)New Features

* Updated to libcouchbase 3.0.1

#### [](#fixed-issues-20)Fixed Issues

* [JSCBC-669](http://issues.couchbase.com/browse/JSCBC-669): Fixed CAS not being returned in some cases.
* [JSCBC-682](http://issues.couchbase.com/browse/JSCBC-682): Fixed N1QL parameter options parsing.
* [JSCBC-666](http://issues.couchbase.com/browse/JSCBC-666): Fixed ConjunctionSearchQuery not being able to add queries.
* [JSCBC-665](http://issues.couchbase.com/browse/JSCBC-665): Fixed search query not using the correct indexes.
* [JSCBC-677](http://issues.couchbase.com/browse/JSCBC-677): Fixed search query consistency not being set in some cases.
* [JSCBC-668](http://issues.couchbase.com/browse/JSCBC-668): Fixed an UnhandledPromiseRejection error which could occur.
* [JSCBC-673](http://issues.couchbase.com/browse/JSCBC-673): Improved handling of cluster closing.
* [JSCBC-711](http://issues.couchbase.com/browse/JSCBC-711): Fixed a case where closing connections could trigger a segfault.
* [JSCBC-695](http://issues.couchbase.com/browse/JSCBC-695): Fixed issue with the use of custom connection string options.
* [JSCBC-683](http://issues.couchbase.com/browse/JSCBC-683): Fixed inconsistent metrics data from query service.
* Updated to latest version of all dependencies.
* Adjusted prebuilt binaries to match currently support Node.js versions.

#### [](#known-issues-34)Known Issues

* [JSCBC-759](http://issues.couchbase.com/browse/JSCBC-759): Buffer objects containing non-UTF8 data can become mangled when inserting them into a bucket or collection. This has been corrected in 3.0.4.

### [](#version-3-0-0-20-january-2020)Version 3.0.0 (20 January 2020)

This is the first GA release of the third generation Node.js SDK.

```console
$ npm install couchbase@3.0.0
```

[API Reference](http://docs.couchbase.com/sdk-api/couchbase-node-client-3.0.0/)

#### [](#new-features-15)New Features

* Updated to libcouchbase 3.0.0

#### [](#fixed-issues-21)Fixed Issues

* [JSCBC-653](http://issues.couchbase.com/browse/JSCBC-653): Fixed transcoding in getReplica and getAndTouch.
* [JSCBC-650](http://issues.couchbase.com/browse/JSCBC-650): Improved stream wrappers to support both events and async/await.
* [JSCBC-657](http://issues.couchbase.com/browse/JSCBC-657): Fixed some error double-translation issues.
* [JSCBC-652](http://issues.couchbase.com/browse/JSCBC-652): Fixed issue with data structures exist checks.
* [JSCBC-655](http://issues.couchbase.com/browse/JSCBC-655): Fixed search query constructors not being exported.
* [JSCBC-656](http://issues.couchbase.com/browse/JSCBC-656): Renamed QueryProfile to QueryProfileMode.
* [JSCBC-639](http://issues.couchbase.com/browse/JSCBC-639): Updated tests to reflect updated libcouchbase behaviour.
* [JSCBC-654](http://issues.couchbase.com/browse/JSCBC-654): Updated to the latest mock to resolve test issue.
* [JSCBC-647](http://issues.couchbase.com/browse/JSCBC-647): Marked all error contexts as uncommitted.
* [JSCBC-596](http://issues.couchbase.com/browse/JSCBC-596): Marked defaultScope, scope, and collection methods uncommitted.

#### [](#known-issues-35)Known Issues

* [JSCBC-759](http://issues.couchbase.com/browse/JSCBC-759): Buffer objects containing non-UTF8 data can become mangled when inserting them into a bucket or collection. This has been corrected in 3.0.4.

### [](#pre-releases)Pre-releases

Numerous _Alpha_ and _Beta_ releases were made in the run-up to the 3.0 release, and although unsupported, the release notes and download links are retained for archive purposes [here](3.0-pre-release-notes.md).

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).