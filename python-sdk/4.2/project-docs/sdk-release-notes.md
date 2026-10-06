---
title: SDK Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Python Client.
pubDate: 2026-10-06T04:29:29.001Z
meta:
  component:
    title: Python SDK
    version: "4.2"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.2/modules/project-docs/pages/sdk-release-notes.adoc
  xref: xref:4.2@python-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.2/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Python Client. 

Couchbase Python SDK 4.x is built upon the Couchbase C++ SDK, and SDK 3.x is built upon LCB (libcouchbase), but both conform to the [SDK API 3.x](compatibility.md#api-version). The move to the Couchbase C++ SDK facilitates the introduction of [distributed ACID transactions](../howtos/distributed-acid-transactions-from-the-sdk.md).

> [!NOTE]
> Because the Python SDK is written primarily in C using the CPython API, the official SDK will not work on PyPy.

## [](#installation)Installation

The full installation instructions that were previously on this page can now be found [here](sdk-full-installation.md).

## [](#python-sdk-4-2-releases)Python SDK 4.2 Releases

### [](#version-4-2-1-18-april-2024)Version 4.2.1 (18 April 2024)

Version 4.2.1 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```console
$ python3 -m pip install couchbase==4.2.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.2.1/>

#### [](#fixes)Fixes

* [PYCBC-1575](https://issues.couchbase.com/browse/PYCBC-1575): Added missing logic to handle alternate addresses when bootstrapping.
* [PYCBC-1532](https://issues.couchbase.com/browse/PYCBC-1532), [PYCBC-1566](https://issues.couchbase.com/browse/PYCBC-1566), [PYCBC-1589](https://issues.couchbase.com/browse/PYCBC-1589): Fixed floating point exception if recieved config with empty vBucket map.
* [PYCBC-1590](https://issues.couchbase.com/browse/PYCBC-1590): Fixed Python logger shutdown process.

#### [](#enhancements)Enhancements

* [PYCBC-1584](https://issues.couchbase.com/browse/PYCBC-1584): Added support for scoped eventing functions.

#### [](#underlying-c-sdk-core-changes)Underlying C++ SDK Core Changes

##### [](#enhancements-2)Enhancements

* [CXXCBC-470](https://issues.couchbase.com/browse/CXXCBC-470): Distinguish between 'unset' and 'off' query\_profile ([#551](https://github.com/couchbaselabs/couchbase-cxx-client/pull/551)).
* [CXXCBC-489](https://issues.couchbase.com/browse/CXXCBC-489): Added support for scoped eventing functions ([#548](https://github.com/couchbaselabs/couchbase-cxx-client/pull/548), ([#554](https://github.com/couchbaselabs/couchbase-cxx-client/pull/554))).

##### [](#fixes-2)Fixes

* [CXXCBC-30](https://issues.couchbase.com/browse/CXXCBC-30): Fixed inconsistent behavior when using subdoc opcodes ([#559](https://github.com/couchbaselabs/couchbase-cxx-client/pull/559)).
* [CXXCBC-487](https://issues.couchbase.com/browse/CXXCBC-487): Added logic during bootstrap to check if alternate addressing is being used ([#545](https://github.com/couchbaselabs/couchbase-cxx-client/pull/545)).
* [CXXCBC-492](https://issues.couchbase.com/browse/CXXCBC-492): Updated collection\_component get\_collection\_id to use retry strategy ([#552](https://github.com/couchbaselabs/couchbase-cxx-client/pull/552)).
* [CXXCBC-494](https://issues.couchbase.com/browse/CXXCBC-494): Fixed memory issue in range scan implementation ([#549](https://github.com/couchbaselabs/couchbase-cxx-client/pull/549)).
* [CXXCBC-503](https://issues.couchbase.com/browse/CXXCBC-503): Added logic to ignore configuration if it contains an empty vBucket map ([#556](https://github.com/couchbaselabs/couchbase-cxx-client/pull/556), [#558](https://github.com/couchbaselabs/couchbase-cxx-client/pull/558)).

### [](#version-4-2-0-14-march-2024)Version 4.2.0 (14 March 2024)

Version 4.2.0 is second minor release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.2.0 release adds support for Vector Search, KV Range Scans, and faster failover when using the SDK with Couchbase Server 7.6.0.

```console
$ python3 -m pip install couchbase==4.2.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.2.0/>

#### [](#known-issues)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Python SDK that contains C++ SDK 1.0.0-dp.15 (or later).

#### [](#behavioral-change)Behavioral Change

It's important to use `Cluster.searchQuery()` / `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes. Method `Scope.search_query()` is now deprecated and will be removed in a future release. Method `Scope.search_query()` will _not_ work with scoped indexes.

#### [](#enhancements-3)Enhancements

* [PYCBC-1548](https://issues.couchbase.com/browse/PYCBC-1548): Added support for Vector Search.
* [PYCBC-1565](https://issues.couchbase.com/browse/PYCBC-1565): Updated C++ core for transactions metadata bucket improvements.
* [PYCBC-1572](https://issues.couchbase.com/browse/PYCBC-1572): Updated search API for SDK API 3.5 support. Included deprecation of `scope.search_query()`.

#### [](#underlying-c-sdk-core-changes-2)Underlying C++ SDK Core Changes

* [CXXCBC-336](https://issues.couchbase.com/browse/CXXCBC-336): Updated DNS config to not fallback to 8.8.8.8 if SDK cannot obtain system DNS server ([#533](https://github.com/couchbaselabs/couchbase-cxx-client/pull/533)).
* [CXXCBC-461](https://issues.couchbase.com/browse/CXXCBC-461): Updated ping operation to not send to nodes that have not completed bootstrap ([#540](https://github.com/couchbaselabs/couchbase-cxx-client/pull/540)).
* [CXXCBC-462](https://issues.couchbase.com/browse/CXXCBC-462): Fixed hanging when specifying a custom metadata collection via the public API & expose errors ([#532](https://github.com/couchbaselabs/couchbase-cxx-client/pull/532)).
* [CXXCBC-479](https://issues.couchbase.com/browse/CXXCBC-479): Fixed capabilities check for replica `LookupIn` operations ([#537](https://github.com/couchbaselabs/couchbase-cxx-client/pull/537)).
* [CXXCBC-480](https://issues.couchbase.com/browse/CXXCBC-480): Fixed capabilities check for replica LookupIn operations ([#539](https://github.com/couchbaselabs/couchbase-cxx-client/pull/539)).
* [CXXCBC-481](https://issues.couchbase.com/browse/CXXCBC-481): Fixed potential crash when parsing search result hits ([#541](https://github.com/couchbaselabs/couchbase-cxx-client/pull/541)).
* [CXXCBC-482](https://issues.couchbase.com/browse/CXXCBC-482): Update range scan orchestrator to use best effort retry strategy by default ([#542](https://github.com/couchbaselabs/couchbase-cxx-client/pull/542)).

## [](#python-sdk-4-1-releases)Python SDK 4.1 Releases

### [](#version-4-1-12-1-march-2024)Version 4.1.12 (1 March 2024)

Version 4.1.12 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```console
$ python3 -m pip install couchbase==4.1.12
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.12/>

#### [](#known-issues-2)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Python SDK that contains C++ SDK 1.0.0-dp.15 (or later).

#### [](#fixes-3)Fixes

* [PYCBC-1555](https://issues.couchbase.com/browse/PYCBC-1555): Fixed bootstrap `select_bucket` logic to handle non-KV node.

#### [](#enhancements-4)Enhancements

* [PYCBC-1375](https://issues.couchbase.com/browse/PYCBC-1375): Updated Query Index Management Create Index Key Encoding.
* [PYCBC-1550](https://issues.couchbase.com/browse/PYCBC-1550): Added support for Scoped Search Indexes.
* [PYCBC-1523](https://issues.couchbase.com/browse/PYCBC-1523): Updated configuration logic when 0xd response is received.
* [PYCBC-1525](https://issues.couchbase.com/browse/PYCBC-1525): Added support for `LookupIn` and `MutateIn` macros.
* [PYCBC-1560](https://issues.couchbase.com/browse/PYCBC-1560): Updated `ViewQueryOptions` to include `full_set` and `raw` options.

#### [](#underlying-c-sdk-core-changes-3)Underlying C++ SDK Core Changes

* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Updated config polling to not use session that is not bootstrapped ([#528](https://github.com/couchbaselabs/couchbase-cxx-client/pull/528)).
* [CXXCBC-345](https://issues.couchbase.com/browse/CXXCBC-345): Added range scan improvements and resolved concurrency issues ([#525](https://github.com/couchbaselabs/couchbase-cxx-client/pull/525)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query operation to return `feature_not_available` if query preserve expiry is specified but is not supported on the server([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).
* [CXXCBC-431](https://issues.couchbase.com/browse/CXXCBC-431): Added check for history retention bucket capability in collection create/update ([#502](https://github.com/couchbaselabs/couchbase-cxx-client/pull/502), [#505](https://github.com/couchbaselabs/couchbase-cxx-client/pull/505)).
* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): Updated bootstrap logic to use addresses from the config to bootstrap bucket ([#516](https://github.com/couchbaselabs/couchbase-cxx-client/pull/516)).
* [CXXCBC-450](https://issues.couchbase.com/browse/CXXCBC-450): Updated bootstrap logic to reset bootstrap handler before re-bootstrap ([#524](https://github.com/couchbaselabs/couchbase-cxx-client/pull/524)).

  * We do not want any actions from old bootstrap handler once the session decided to re-bootstrap. For example, bucket could not be selected, but we might still get configuration responses before socket reset.
* [CXXCBC-452](https://issues.couchbase.com/browse/CXXCBC-452): Updated capabilities and fail fast when selected feature is not available. ([#522](https://github.com/couchbaselabs/couchbase-cxx-client/pull/522), [#513](https://github.com/couchbaselabs/couchbase-cxx-client/pull/513)).
* [CXXCBC-456](https://issues.couchbase.com/browse/CXXCBC-456): Updated configuration logic when 0x0d (`EConfigOnly`) status code is received to have the SDK request new configuration and send current operation to retry orchestrator ([#523](https://github.com/couchbaselabs/couchbase-cxx-client/pull/523)).

### [](#version-4-1-11-1-february-2024)Version 4.1.11 (1 February 2024)

Version 4.1.11 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.11
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.11/>

#### [](#enhancements-5)Enhancements

* [PYCBC-1549](https://issues.couchbase.com/browse/PYCBC-1549): Added support for `maxTTL` value of -1 for collection "no expiry".

#### [](#underlying-c-sdk-core-changes-4)Underlying C++ SDK Core Changes

* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Reduced network traffic when polling for cluster configuration ([#504](https://github.com/couchbaselabs/couchbase-cxx-client/pull/504)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query response to return `feature_not_available` when query preserve expiry is not supported ([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).
* [CXXCBC-422](https://issues.couchbase.com/browse/CXXCBC-422): Added insufficient credentials error code to common query error code conversion ([#511](https://github.com/couchbaselabs/couchbase-cxx-client/pull/511)).
* [CXXCBC-431](https://issues.couchbase.com/browse/CXXCBC-431): Added check for history retention bucket capability for collection create/update ([#502](https://github.com/couchbaselabs/couchbase-cxx-client/pull/502), [#505](https://github.com/couchbaselabs/couchbase-cxx-client/pull/505)).
* [CXXCBC-446](https://issues.couchbase.com/browse/CXXCBC-446): Improved log formatting ([#506](https://github.com/couchbaselabs/couchbase-cxx-client/pull/506), [#508](https://github.com/couchbaselabs/couchbase-cxx-client/pull/508), [#509](https://github.com/couchbaselabs/couchbase-cxx-client/pull/509)).

### [](#version-4-1-10-3-january-2024)Version 4.1.10 (3 January 2024)

Version 4.1.10 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.10
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.10/>

#### [](#enhancements-6)Enhancements

* [PYCBC-1499](https://issues.couchbase.com/browse/PYCBC-1499): Added improvements for Faster Failover and Config Push.
* [PYCBC-1545](https://issues.couchbase.com/browse/PYCBC-1545): Added support for new KV error code to raise `DocumentNotLockedException`.

#### [](#underlying-c-sdk-core-changes-5)Underlying C++ SDK Core Changes

* [CXXCBC-100](https://issues.couchbase.com/browse/CXXCBC-100): Added support for using a timeout with `ping` operation ([#486](https://github.com/couchbaselabs/couchbase-cxx-client/pull/486)).
* [CXXCBC-368](https://issues.couchbase.com/browse/CXXCBC-368): Added support for subscribing to clustermap notifications to speedup failover ([#490](https://github.com/couchbaselabs/couchbase-cxx-client/pull/490)).
* [CXXCBC-391](https://issues.couchbase.com/browse/CXXCBC-391): Fixed transactions API inconsistencies ([#482](https://github.com/couchbaselabs/couchbase-cxx-client/pull/482)).
* [CXXCBC-403](https://issues.couchbase.com/browse/CXXCBC-403): Updated `not_my_vbucket` KV response to allow retries ([#480](https://github.com/couchbaselabs/couchbase-cxx-client/pull/480)).
* [CXXCBC-404](https://issues.couchbase.com/browse/CXXCBC-404): Fixed `unlock` operations to expose `KV_LOCKED` status as `cas_mismatch` ([#479](https://github.com/couchbaselabs/couchbase-cxx-client/pull/479)).
* [CXXCBC-409](https://issues.couchbase.com/browse/CXXCBC-409): Added handling for `index does not exist` query error ([#492](https://github.com/couchbaselabs/couchbase-cxx-client/pull/492)).
* [CXXCBC-419](https://issues.couchbase.com/browse/CXXCBC-419): Updated MCBP protocol parser to start with clean state ([#496](https://github.com/couchbaselabs/couchbase-cxx-client/pull/496)).

### [](#version-4-1-9-14-november-2023)Version 4.1.9 (14 November 2023)

Version 4.1.9 is the next patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.1.9 release removes the `OpenSSL` dependency for published wheels and added _musllinux_ wheels for supported alpine environments.

```bash
$ python3 -m pip install couchbase==4.1.9
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.9/>

#### [](#behavioral-change-2)Behavioral Change

The Couchbase Python SDK now publishes wheels that statically link against `BoringSSL`. The change removes the `OpenSSL` requirement from the SDK when using a published wheel. If building the SDK from source, the build will default to dynamically linking with the system provided `OpenSSL`. Build options are available if wanting to build from source and statically link against `BoringSSL`. Also, published wheels dynamically link against `stdlibs` where previously the default was to statically link against `stdlibs`. Build options are available if wanting to build from source and statically link against `stdlibs`.

#### [](#fixes-4)Fixes

* [PYCBC-1538](https://issues.couchbase.com/browse/PYCBC-1538): Fixed `get` with projections to not fail with `InvalidArgumentException` when projecting on more than 16 fields.
* [PYCBC-1534](https://issues.couchbase.com/browse/PYCBC-1534): Fixed `MutateIn` replace operation to not fail if path is empty.
* [PYCBC-1531](https://issues.couchbase.com/browse/PYCBC-1531): Fixed `CollectionQueryIndexManager` to raise `InvalidArgumentException` when `scope_name` or `collection_name` options are set.
* [PYCBC-1521](https://issues.couchbase.com/browse/PYCBC-1521): Fixed streaming APIs to use cluster timeout values from `ClusterTimeoutOptions` if provided.

#### [](#enhancements-7)Enhancements

* [PYCBC-1536](https://issues.couchbase.com/browse/PYCBC-1536): Updated MANIFEST.in to only include necessary files for source install.
* [PYCBC-1520](https://issues.couchbase.com/browse/PYCBC-1518), [PYCBC-1518](https://issues.couchbase.com/browse/PYCBC-1520): Updated published wheels to statically link against BoringSSL.
* [PYCBC-1515](https://issues.couchbase.com/browse/PYCBC-1515): Added support for bucket settings for 'no dedup' feature.
* [PYCBC-1512](https://issues.couchbase.com/browse/PYCBC-1512): Reduced default HTTP Idle Timeout.
* [PYCBC-1495](https://issues.couchbase.com/browse/PYCBC-1495): Updated wheels and build to dynamically link against stdlibs by default.

#### [](#underlying-c-sdk-core-changes-6)Underlying C++ SDK Core Changes

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

### [](#version-4-1-8-25-august-2023)Version 4.1.8 (25 August 2023)

Version 4.1.8 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.8
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.8/>

#### [](#behavioral-change-3)Behavioral Change

The Couchbase Python SDK no longer provides Python 3.7 wheels as Python 3.7 has reached [end-of-life](https://peps.python.org/pep-0537/#lifespan). See [Python Version Compatibility](https://docs.couchbase.com/python-sdk/current/project-docs/compatibility.html#python-version-compat) for details.

#### [](#fixes-5)Fixes

* [PYCBC-1514](https://issues.couchbase.com/browse/PYCBC-1514): Fixed parsing of `LookupIn` options if provided for lookup-in operations.

#### [](#enhancements-8)Enhancements

* [PYCBC-1497](https://issues.couchbase.com/browse/PYCBC-1497): Added support for Sub-Document Read from Replica.

#### [](#underlying-c-sdk-core-changes-7)Underlying C++ SDK Core Changes

* [CXXCBC-362](https://issues.couchbase.com/browse/CXXCBC-362): Removed node hostname port stripping logic from config parsing ([#438](https://github.com/couchbaselabs/couchbase-cxx-client/pull/438)).
* [CXXCBC-340](https://issues.couchbase.com/browse/CXXCBC-340): Added support for Query Read from Replica ([#435](https://github.com/couchbaselabs/couchbase-cxx-client/pull/435)).
* [CXXCBC-341](https://issues.couchbase.com/browse/CXXCBC-341), [CXXCBC-365](https://issues.couchbase.com/browse/CXXCBC-365): Added support for Sub-Document Read from Replica ([#436](https://github.com/couchbaselabs/couchbase-cxx-client/pull/436), [#441](https://github.com/couchbaselabs/couchbase-cxx-client/pull/441), [#443](https://github.com/couchbaselabs/couchbase-cxx-client/pull/443)).

### [](#version-4-1-7-8-august-2023)Version 4.1.7 (8 August 2023)

Version 4.1.7 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.7
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.7/>

#### [](#behavioral-change-4)Behavioral Change

Since Python 3.7 has reached [end-of-life](https://peps.python.org/pep-0537/#lifespan), the Couchbase Python SDK will no longer provide Python 3.7 wheels in future releases (>4.1.7). See [Python Version Compatibility](https://docs.couchbase.com/python-sdk/current/project-docs/compatibility.html#python-version-compat) for details.

#### [](#fixes-6)Fixes

* [PYCBC-1502](https://issues.couchbase.com/browse/PYCBC-1502): Added `PasswordAuthenticator` validation.

#### [](#enhancements-9)Enhancements

* [PYCBC-1496](https://issues.couchbase.com/browse/PYCBC-1496): Added support for Query with Read from Replica.
* [PYCBC-1419](https://issues.couchbase.com/browse/PYCBC-1419): Added support for Native KV Range Scans.
* [PYCBC-1504](https://issues.couchbase.com/browse/PYCBC-1505); [PYCBC-1505](https://issues.couchbase.com/browse/PYCBC-1505): Updated API documentation to provide correct information on `LockMode`.
* [PYCBC-1510](https://issues.couchbase.com/browse/PYCBC-1510): Updated CONTRIBUTING.md to improve contributing guidelines.
* [PYCBC-1095](https://issues.couchbase.com/browse/PYCBC-1095): Added Subdoc mutate-in deletions with a blank path.

#### [](#underlying-c-sdk-core-changes-8)Underlying C++ SDK Core Changes

* [CXXCBC-349](https://issues.couchbase.com/browse/CXXCBC-349): Allow to pass trust certificate by value ([#430](https://github.com/couchbaselabs/couchbase-cxx-client/pull/430)).

  * The change affects TLS v1.0 and v1.1 which are now disabled by default.
* [CXXCBC-343](https://issues.couchbase.com/browse/CXXCBC-343): Continue bootsrap if DNS-SRV resolution fails ([#422](https://github.com/couchbaselabs/couchbase-cxx-client/pull/422)).
* [CXXCBC-340](https://issues.couchbase.com/browse/CXXCBC-340): Support Query with Read from Replica ([#429](https://github.com/couchbaselabs/couchbase-cxx-client/pull/429)).
* [CXXCBC-339](https://issues.couchbase.com/browse/CXXCBC-339): Disabled older TLS protocols ([#418](https://github.com/couchbaselabs/couchbase-cxx-client/pull/418)).
* [CXXCBC-333](https://issues.couchbase.com/browse/CXXCBC-333): Fixed parsing 'resolv.conf' on Linux. ([#416](https://github.com/couchbaselabs/couchbase-cxx-client/pull/416)).

  * The library might not ignore trailing characters when reading nameserver address from the file.
* [CXXCBC-242](https://issues.couchbase.com/browse/CXXCBC-242): SDK Support for Native KV Range Scans ([#419](https://github.com/couchbaselabs/couchbase-cxx-client/pull/419), [#423](https://github.com/couchbaselabs/couchbase-cxx-client/pull/423), [#424](https://github.com/couchbaselabs/couchbase-cxx-client/pull/424), [#426](https://github.com/couchbaselabs/couchbase-cxx-client/pull/426), [#428](https://github.com/couchbaselabs/couchbase-cxx-client/pull/428), [#431](https://github.com/couchbaselabs/couchbase-cxx-client/pull/431), [#432](https://github.com/couchbaselabs/couchbase-cxx-client/pull/432), [#433](https://github.com/couchbaselabs/couchbase-cxx-client/pull/433), [#434](https://github.com/couchbaselabs/couchbase-cxx-client/pull/434)).

### [](#version-4-1-6-13-july-2023)Version 4.1.6 (13 July 2023)

Version 4.1.6 is the sixth patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.1.6 release adds support for Python 3.11 and significantly reduces the size of published _manylinux_ wheels.

```bash
$ python3 -m pip install couchbase==4.1.6
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.6/>

#### [](#fixes-7)Fixes

* [PYCBC-1500](https://issues.couchbase.com/browse/PYCBC-1500): Added `max_expiry` to `CollectionSpec` for collections returned in `get_all_scopes()` result.

#### [](#enhancements-10)Enhancements

* [PYCBC-1473](https://issues.couchbase.com/browse/PYCBC-1473): Added Support for Python 3.11.
* [PYCBC-1459](https://issues.couchbase.com/browse/PYCBC-1459): Reduced size of manylinux wheels.
* [PYCBC-1494](https://issues.couchbase.com/browse/PYCBC-1494): Updated API docs to include binary `multiOptions`.
* [PYCBC-1498](https://issues.couchbase.com/browse/PYCBC-1498): Updated connection tests to only use valid mixed environment format.

### [](#version-4-1-5-8-june-2023)Version 4.1.5 (8 June 2023)

Version `4.1.5` is the fifth patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.5
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.5/>

#### [](#behavioral-change-5)Behavioral Change

Accessing content from an Exist operation with the `` LookupInResult’s `content_as `` method now returns a boolean. This boolean is `True` if the path exists, `False` otherwise. Prior to this change the SDK raised a `DocumentNotFoundException` if the path existed or `PathNotFoundException` if the path didn't exist. The behavioral change aligns the Python SDK with Couchbase's [CRUD RFC](https://github.com/couchbaselabs/sdk-rfcs/blob/master/rfc/0053-sdk3-crud.md).

#### [](#fixes-8)Fixes

* [PYCBC-1480](https://issues.couchbase.com/browse/PYCBC-1480): Fixed subdocument read operations to allow for null values.
* [PYCBC-1486](https://issues.couchbase.com/browse/PYCBC-1486): Fixed broken imports for search `GeoBoundingBoxQuery`, `GeoDistanceQuery`, and `GeoPolygonQuery`.
* [PYCBC-1487](https://issues.couchbase.com/browse/PYCBC-1487): Updated Transcoders to be able to decode value when `flags=0`.
* [PYCBC-1490](https://issues.couchbase.com/browse/PYCBC-1490): Fixed `InternalServerFailureException` when executing a `Regex` Search query.
* [PYCBC-1493](https://issues.couchbase.com/browse/PYCBC-1493): Updated search operations to correctly pass MutationState to C++ core.

#### [](#enhancements-11)Enhancements

* [PYCBC-1488](https://issues.couchbase.com/browse/PYCBC-1488): Added `dump_configuration` to `ClusterOptions`.
* [PYCBC-1479](https://issues.couchbase.com/browse/PYCBC-1479): Bundled Mozilla certificates with the library. Source: <https://curl.se/docs/caextract.html>. Use the `disable_mozilla_ca_certificates` connection string option to disable the bundled certificates. See [Secure Connections](https://docs.couchbase.com/python-sdk/current/howtos/managing-connections.html#ssl) for more details.

#### [](#underlying-c-sdk-core-changes-9)Underlying C++ SDK Core Changes

* [CXXCBC-328](https://issues.couchbase.com/browse/CXXCBC-328): Fix socket reconnection during rebalance process ([#406](https://github.com/couchbaselabs/couchbase-cxx-client/pull/406)).

  * Several improvements have been implemented to make the library resilient to rapid topology changes when both DNS-SRV bootstrap is being used along with alternative addresses. The changes include:

    * Taking into account alternative hostname and ports during detection of added/removed nodes on configuration update.
    * Replacing node index tracking with hostname/port matching when restarting the connections — this way the library ensures that no duplicate connections will be left, or live connections replaced by restarted session.
    * Improved logging of critical events during rebalance: restarting, preservation, and removing connections.

### [](#version-4-1-4-9-may-2023)Version 4.1.4 (9 May 2023)

Version `4.1.4` is the fourth patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.4
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.4/>

#### [](#fixes-9)Fixes

* [PYCBC-1469](https://issues.couchbase.com/browse/PYCBC-1469): Added check to determine if Python interpreter is finalizing prior to logging.
* [PYCBC-1471](https://issues.couchbase.com/browse/PYCBC-1471): Fixed `acouchbase` streaming API blocking behavior while when executing queries.
* [PYCBC-1474](https://issues.couchbase.com/browse/PYCBC-1474): Fixed transaction error handling.
* [PYCBC-1475](https://issues.couchbase.com/browse/PYCBC-1475): Updated exception classes to allow first positional arg to be a string message.
* [PYCBC-1477](https://issues.couchbase.com/browse/PYCBC-1477): Fixed potential crash in certain scenarios that use `MutationState`.

#### [](#enhancements-12)Enhancements

* [PYCBC-1468](https://issues.couchbase.com/browse/PYCBC-1468): Added replica read operations to API docs.
* [PYCBC-1472](https://issues.couchbase.com/browse/PYCBC-1472): Updated API Docs to indicate expiry option should be a timedelta.
* [PYCBC-1478](https://issues.couchbase.com/browse/PYCBC-1478): Added missing bootstrap timeouts to WAN Config Profile.

#### [](#underlying-c-sdk-core-changes-10)Underlying C++ SDK Core Changes

* [CXXCBC-31](https://issues.couchbase.com/browse/CXXCBC-31): Allow the use of schemaless connection strings (e.g. `"cb1.example.com,cb2.example.com"`) ([#394](https://github.com/couchbaselabs/couchbase-cxx-client/pull/394)).
* [CXXCBC-320](https://issues.couchbase.com/browse/CXXCBC-320): Negative expiry in atr was leaving docs in a stuck state — this has been fixed, with expiry atr now becoming an `int32_t`([#393](https://github.com/couchbaselabs/couchbase-cxx-client/pull/393)).
* [CXXCBC-318](https://issues.couchbase.com/browse/CXXCBC-318): Always try TCP if UDP fails in DNS-SRV resolver ([#390](https://github.com/couchbaselabs/couchbase-cxx-client/pull/390)).
* [CXXCBC-145](https://issues.couchbase.com/browse/CXXCBC-145): Search query request raw option now used ([#380](https://github.com/couchbaselabs/couchbase-cxx-client/pull/380)).
* [CXXCBC-144](https://issues.couchbase.com/browse/CXXCBC-144): Search query on collections now no longer requires `scope_name`, as it can be inferred from the index ([#379](https://github.com/couchbaselabs/couchbase-cxx-client/pull/379)).

### [](#version-4-1-3-9-march-2023)Version 4.1.3 (9 March 2023)

Version `4.1.3` is the third patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.3
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.3/>

#### [](#fixes-10)Fixes

* [PYCBC-1443](https://issues.couchbase.com/browse/PYCBC-1443): Fixed ssl import error.
* [PYCBC-1446](https://issues.couchbase.com/browse/PYCBC-1446): Updated API Documentation.
* [PYCBC-1455](https://issues.couchbase.com/browse/PYCBC-1455): Fixed build issue for Fedora 37 (gcc 12).

#### [](#enhancements-13)Enhancements

* [PYCBC-1431](https://issues.couchbase.com/browse/PYCBC-1431): Updated the SDK to handle new `query_context` changes.
* [PYCBC-1444](https://issues.couchbase.com/browse/PYCBC-1444): Improved CertificateAuthenticator parameter validation.
* [PYCBC-1445](https://issues.couchbase.com/browse/PYCBC-1445): Updated the SDK to only populate `allowed_sasl_mechanisms` if user explicitly chooses.

### [](#version-4-1-2-9-february-2023)Version 4.1.2 (9 February 2023)

Version `4.1.2` is the second patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the `4.1.2` release provides improved performance for key-value operations.

```bash
$ python3 -m pip install couchbase==4.1.2
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.2/>

#### [](#fixes-11)Fixes

* [PYCBC-1433](https://issues.couchbase.com/browse/PYCBC-1433): Fixed initialization of legacy durability options in C++ bindings.
* [PYCBC-1434](https://issues.couchbase.com/browse/PYCBC-1434): Added Python SDK and Python version to C++ `user_agent` option.
* [PYCBC-1441](https://issues.couchbase.com/browse/PYCBC-1441): Fixed inconsistencies when handling of `MutationState` in streaming APIs.

#### [](#enhancements-14)Enhancements

* [PYCBC-1371](https://issues.couchbase.com/browse/PYCBC-1371): Implemented `ChangePassword` feature in user management API.
* [PYCBC-1436](https://issues.couchbase.com/browse/PYCBC-1436): Updated pre-commit iSort Revision.
* [PYCBC-1440](https://issues.couchbase.com/browse/PYCBC-1440): Updated logging to get latest from C++ client.
* [PYCBC-1438](https://issues.couchbase.com/browse/PYCBC-1438): Updated Test Suite/Framework.

### [](#version-4-1-1-14-december-2022)Version 4.1.1 (14 December 2022)

Version `4.1.1` is the first patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.1/>

#### [](#fixes-12)Fixes

* [PYCBC-1428](https://issues.couchbase.com/browse/PYCBC-1428): Fixed view query `ViewOrdering` to allow user specified ordering to be applied.
* [PYCBC-1429](https://issues.couchbase.com/browse/PYCBC-1429): Fixed defaults for boolean options in N1QL query `QueryOptions`.

### [](#version-4-1-0-3-november-2022)Version 4.1.0 (3 November 2022)

Version `4.1.0` is the first minor release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.0/>

#### [](#fixes-13)Fixes

* [PYCBC-1420](https://issues.couchbase.com/browse/PYCBC-1420): Fixed potential `InternalSDKException` for replica read operations.

#### [](#enhancements-15)Enhancements

* [PYCBC-1402](https://issues.couchbase.com/browse/PYCBC-1402): Added support for using PYCBC\_LOG\_LEVEL to create console logger.
* [PYCBC-1417](https://issues.couchbase.com/browse/PYCBC-1417): Updated authentication error message for Bucket Hibernation.
* [PYCBC-1422](https://issues.couchbase.com/browse/PYCBC-1422): Updated Couchbase++ version to incorporate latest changes.
* [PYCBC-1167](https://issues.couchbase.com/browse/PYCBC-1167): Added support for Serverless Execution Environments.
* [PYCBC-1423](https://issues.couchbase.com/browse/PYCBC-1423): Added durability improvements.

## [](#python-sdk-4-0-releases)Python SDK 4.0 Releases

### [](#version-4-0-5-7-october-2022)Version 4.0.5 (7 October 2022)

Version `4.0.5` is the fifth patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.0.5
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.5/>

#### [](#fixes-14)Fixes

* [PYCBC-1312](https://issues.couchbase.com/browse/PYCBC-1312); [PYCBC-1407](https://issues.couchbase.com/browse/PYCBC-1407): Fixed crash related to closing a cluster connection.
* [PYCBC-1409](https://issues.couchbase.com/browse/PYCBC-1409): Updated to version of Couchbase++ client that correctly closes HTTP connections.
* [PYCBC-1413](https://issues.couchbase.com/browse/PYCBC-1413): Fixed possible streaming API exceptions when executing in threaded environment.
* [PYCBC-1415](https://issues.couchbase.com/browse/PYCBC-1415): Updated async APIs to use correct future chaining method for read KV operations.
* [PYCBC-1416](https://issues.couchbase.com/browse/PYCBC-1416): Fixed `txcouchbase` search API.

#### [](#enhancements-16)Enhancements

* [PYCBC-1405](https://issues.couchbase.com/browse/PYCBC-1405): Updated legacy durability to use the internal Couchbase++ client API.
* [PYCBC-1406](https://issues.couchbase.com/browse/PYCBC-1406): Updated replica reads to use the internal Couchbase++ client API.
* [PYCBC-1411](https://issues.couchbase.com/browse/PYCBC-1411): Added support for LDAP authentication.

### [](#version-4-0-4-8-september-2022)Version 4.0.4 (8 September 2022)

Version `4.0.4` is the fourth patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the `4.0.4` release added legacy durability to mutation operations, tracing, and metrics.

```bash
$ python3 -m pip install couchbase==4.0.4
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.4/>

#### [](#fixes-15)Fixes

* [PYCBC-1398](https://issues.couchbase.com/browse/PYCBC-1398): Fixed potential crash when accessing `error_context` from a `base_exception` object.

#### [](#enhancements-17)Enhancements

* [PYCBC-1261](https://issues.couchbase.com/browse/PYCBC-1261): Added Tracing API, including the ability to use an external tracer such as OpenTelemetry.
* [PYCBC-1276](https://issues.couchbase.com/browse/PYCBC-1276): Added legacy durability to mutation operations. This allows the use of client durability within operations that allow for a durability option.
* [PYCBC-1399](https://issues.couchbase.com/browse/PYCBC-1399): Added Metrics API — users can now provide a custom meter for logging metrics.
* [PYCBC-1391](https://issues.couchbase.com/browse/PYCBC-1391): Removed `_raw_metrics` property from streaming API Metrics result objects.
* [PYCBC-1392](https://issues.couchbase.com/browse/PYCBC-1392): Updated `collection.exists()` logic to align with a recent change in the underlying Couchbase++ client. Users will no longer see an error if a document doesn't exist, instead the `resp.exists()` method will be needed to determine whether a document is there or not.
* [PYCBC-1395](https://issues.couchbase.com/browse/PYCBC-1395): Updated build deferred index logic to align with recent change in Couchbase++ client.

### [](#version-4-0-3-2-august-2022)Version 4.0.3 (2 August 2022)

Version `4.0.3` is the third patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the `4.0.3` release added key-value replica read operations and improved memory performance.

```bash
$ python3 -m pip install couchbase==4.0.3
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.3/>

#### [](#fixes-16)Fixes

* [PYCBC-1201](https://issues.couchbase.com/browse/PYCBC-1201); [PYCBC-1282](https://issues.couchbase.com/browse/PYCBC-1282); [PYCBC-1382](https://issues.couchbase.com/browse/PYCBC-1382)Fixed memory leak in key-value Result objects.
* [PYCBC-1383](https://issues.couchbase.com/browse/PYCBC-1383): Fixed memory leak in key-value Exception objects.
* [PYCBC-1386](https://issues.couchbase.com/browse/PYCBC-1386): Fixed OpenSSL discovery for MacOS M1 platforms.
* [PYCBC-1389](https://issues.couchbase.com/browse/PYCBC-1389): Removed typing-extensions dependency.
* [PYCBC-1390](https://issues.couchbase.com/browse/PYCBC-1390): Fixed Search query results to forward metrics for user access.

#### [](#enhancements-18)Enhancements

* [PYCBC-1257](https://issues.couchbase.com/browse/PYCBC-1257): Added replica reads.
* [PYCBC-1385](https://issues.couchbase.com/browse/PYCBC-1385): Updated Couchbase++ version.
* [PYCBC-1137](https://issues.couchbase.com/browse/PYCBC-1137): Deprecated the `CounterResult` CAS property.

#### [](#known-issues-3)Known Issues

* [PYCBC-1261](https://issues.couchbase.com/browse/PYCBC-1261): Distributed tracing is not yet supported.
* [PYCBC-1276](https://issues.couchbase.com/browse/PYCBC-1276): Legacy durability operations are not yet supported.
* [PYCBC-1290](https://issues.couchbase.com/browse/PYCBC-1290): Transactions for `txcouchbase` are not yet supported.
* [PYCBC-1321](https://issues.couchbase.com/browse/PYCBC-1321): API docs for `txcouchbase` API are not yet available.

### [](#version-4-0-2-29-june-2022)Version 4.0.2 (29 June 2022)

Version `4.0.2` is the second patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the `4.0.2` release provides manylinux wheels which significantly improves the installation process on Linux platforms.

```console
$ python3 -m pip install couchbase==4.0.2
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.2/>

#### [](#fixes-17)Fixes

* [PYCBC-1370](https://issues.couchbase.com/browse/PYCBC-1370): Added environment variables to direct CMake to use specified Python3 version.
* [PYCBC-1374](https://issues.couchbase.com/browse/PYCBC-1374): Added option to dynamically link `stdc++` libs.

#### [](#enhancements-19)Enhancements

* [PYCBC-628](https://issues.couchbase.com/browse/PYCBC-628); [PYCBC-1330](https://issues.couchbase.com/browse/PYCBC-1330); [PYCBC-1367](https://issues.couchbase.com/browse/PYCBC-1367): Added manylinux wheels.
* [PYCBC-1232](https://issues.couchbase.com/browse/PYCBC-1232); [PYCBC-1368](https://issues.couchbase.com/browse/PYCBC-1368): Created custom spdlog sink for pass-through logging to python logging.
* [PYCBC-1373](https://issues.couchbase.com/browse/PYCBC-1373): Provided example Linux build system Dockerfiles.
* [PYCBC-1332](https://issues.couchbase.com/browse/PYCBC-1332): Added formatting and linting to CI pipeline.

#### [](#known-issues-4)Known Issues

* [PYCBC-1257](https://issues.couchbase.com/browse/PYCBC-1257): Replica reads are not yet supported.
* [PYCBC-1261](https://issues.couchbase.com/browse/PYCBC-1261): Distributed tracing is not yet supported.
* [PYCBC-1276](https://issues.couchbase.com/browse/PYCBC-1276): Legacy durability operations are not yet supported.
* [PYCBC-1290](https://issues.couchbase.com/browse/PYCBC-1290): Transactions for txcouchbase are not yet supported.
* [PYCBC-1321](https://issues.couchbase.com/browse/PYCBC-1321): API docs for txcouchbase API are not yet available.

### [](#version-4-0-1-9-june-2022)Version 4.0.1 (9 June 2022)

Version 4.0.1 is the first patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.0.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.1/>

#### [](#fixes-18)Fixes

* [PYCBC-1324](https://issues.couchbase.com/browse/PYCBC-1324): Fixed N1QL Query options `scan_wait/scan_cap` misspelling.
* [PYCBC-1335](https://issues.couchbase.com/browse/PYCBC-1335): Fixed issue where positional and named parameters were not used in `TransactionQueryOptions`.
* [PYCBC-1336](https://issues.couchbase.com/browse/PYCBC-1336): Fixed crash when using `ViewOptions` keys parameter.
* [PYCBC-1342](https://issues.couchbase.com/browse/PYCBC-1342): Fixed the txcouchbase API Bucket Management API.
* [PYCBC-1343](https://issues.couchbase.com/browse/PYCBC-1343): Fixed the txcouchbase Collection Management API.

#### [](#enhancements-20)Enhancements

* [PYCBC-1328](https://issues.couchbase.com/browse/PYCBC-1328)Implemented txcouchbase test suite.
* [PYCBC-1320](https://issues.couchbase.com/browse/PYCBC-1320): Added acouchbase core API Docs.
* [PYCBC-1329](https://issues.couchbase.com/browse/PYCBC-1329): Cleaned up the acouchbase API test suite.
* [PYCBC-1331](https://issues.couchbase.com/browse/PYCBC-1331): Updated streaming API options tests to validate all parameters.
* [PYCBC-1333](https://issues.couchbase.com/browse/PYCBC-1333): Updated README, API docs for 4.0.1 release.
* [PYCBC-1334](https://issues.couchbase.com/browse/PYCBC-1334): Cleaned up couchbase API test suite.
* [PYCBC-1358](https://issues.couchbase.com/browse/PYCBC-1358): Updated Windows wheel to dynamically link against OpenSSL.

#### [](#known-issues-5)Known Issues

* [PYCBC-1232](https://issues.couchbase.com/browse/PYCBC-1232): Core IO logging is not forwarded through to Python.
* [PYCBC-1257](https://issues.couchbase.com/browse/PYCBC-1257): Replica reads are not yet supported.
* [PYCBC-1261](https://issues.couchbase.com/browse/PYCBC-1261): Distributed tracing is not yet supported.
* [PYCBC-1276](https://issues.couchbase.com/browse/PYCBC-1276): Legacy durability operations are not yet supported.
* [PYCBC-1290](https://issues.couchbase.com/browse/PYCBC-1290): Transactions for txcouchbase are not yet supported.
* [PYCBC-1321](https://issues.couchbase.com/browse/PYCBC-1321): API docs for txcouchbase API are not yet available.

### [](#version-4-0-0-6-may-2022)Version 4.0.0 (6 May 2022)

Version 4.0.0 is the first major release of the next generation Python SDK, built on the the Couchbase C++ library — featuring multi-document distributed ACID transactions, and bringing a number of improvements to the SDK.

```console
$ python3 -m pip install couchbase==4.0.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/>

#### [](#new-features)New Features

* Support for distributed transactions has now been implemented.
* Reimplemented the library using the Couchbase C++ SDK.
* Improved alignment between couchbase, acouchbase and txcouchbase APIs.
* Support for Python versions 3.7 - 3.10.
* Improved API documentation.

#### [](#fixes-19)Fixes

* [PYCBC-849](https://issues.couchbase.com/browse/PYCBC-849): Implemented wait until ready.
* [PYCBC-1146](https://issues.couchbase.com/browse/PYCBC-1146): Aligned multi key-value methods with couchbase API.
* [PYCBC-1280](https://issues.couchbase.com/browse/PYCBC-1280): Fixed implementation of the `CertificateAuthenticator`.
* [PYCBC-1296](https://issues.couchbase.com/browse/PYCBC-1296): Updated `SearchRow` to not print locations when not included.

#### [](#known-issues-6)Known Issues

* [PYCBC-1232](https://issues.couchbase.com/browse/PYCBC-1232): Core IO logging is not forwarded through to Python.
* [PYCBC-1257](https://issues.couchbase.com/browse/PYCBC-1257): Replica reads are not yet supported.
* [PYCBC-1261](https://issues.couchbase.com/browse/PYCBC-1261): Distributed tracing is not yet supported.
* [PYCBC-1276](https://issues.couchbase.com/browse/PYCBC-1276): Legacy durability operations are not yet supported.
* [PYCBC-1290](https://issues.couchbase.com/browse/PYCBC-1290): Transactions for txcouchbase are not yet supported.
* [PYCBC-1319](https://issues.couchbase.com/browse/PYCBC-1319): Management APIs for txcouchbase are not yet supported.
* [PYCBC-1320](https://issues.couchbase.com/browse/PYCBC-1320): API docs for acouchbase API are not yet available.
* [PYCBC-1321](https://issues.couchbase.com/browse/PYCBC-1321): API docs for txcouchbase API are not yet available.
* [PYCBC-1322](https://issues.couchbase.com/browse/PYCBC-1322): Scoped transactional queries currently throw a `TransactionFailed` error.

## [](#older-releases)Older Releases

For documentation on older releases please refer to the [archived 3.x release notes](https://docs-archive.couchbase.com/python-sdk/3.2/project-docs/sdk-release-notes.html) page.