---
title: SDK Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Python Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.3/modules/project-docs/pages/sdk-release-notes.adoc
  xref: xref:4.3@python-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.3/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Python Client. 

Couchbase Python SDK 4.x is built upon the Couchbase C++ SDK, and SDK 3.x is built upon LCB (libcouchbase), but both conform to the [SDK API 3.x](compatibility.md#api-version). The move to the Couchbase C++ SDK facilitates the introduction of [distributed ACID transactions](../howtos/distributed-acid-transactions-from-the-sdk.md).

> [!NOTE]
> Because the Python SDK is written primarily in C using the CPython API, the official SDK will not work on PyPy.

## [](#installation)Installation

The full installation instructions that were previously on this page can now be found [here](sdk-full-installation.md).

## [](#latest-release)Python SDK 4.6 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-4-6-2-17-june-2026)Version 4.6.2 (17 June 2026)

Version 4.6.2 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.6.2
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.6.2/>

#### [](#enhancements)Enhancements

[PYCBC-1767](https://jira.issues.couchbase.com/browse/PYCBC-1767): Updated no-op observability path to use `nullcontext`.

[PYCBC-1771](https://jira.issues.couchbase.com/browse/PYCBC-1771): Cleaned up `txcouchbase` `ObservableRequestHandler` context manager creation.

[PYCBC-1774](https://jira.issues.couchbase.com/browse/PYCBC-1774): Added cancellation/close support to the C-extension streaming result so cancelled streams release their worker thread promptly.

[PYCBC-1779](https://jira.issues.couchbase.com/browse/PYCBC-1779): Removed `asyncio.QueueEmpty` unreachable exception blocks.

#### [](#fixes)Fixes

[PYCBC-1770](https://jira.issues.couchbase.com/browse/PYCBC-1770): Fixed Collection Management `create_collection` and `drop_collection` overload path that did not correctly set options.

[PYCBC-1773](https://jira.issues.couchbase.com/browse/PYCBC-1773): Fixed streaming operations to handle `asyncio.CancelledError` / `BaseException`.

[PYCBC-1778](https://jira.issues.couchbase.com/browse/PYCBC-1778): Fixed how client handles KV range scan with `consistent_with` and `ScanResult.expiry_time` options.

#### [](#underlying-c-sdk-core-changes)Underlying C++ SDK Core Changes

##### [](#fixes-and-enhancements)Fixes and Enhancements

[CXXCBC-785](https://jira.issues.couchbase.com/browse/CXXCBC-785): Projected get requesting more than 16 paths no longer fails when one of the requested paths does not exist in the document and missing paths are now skipped rather than aborting the whole projection.

[CXXCBC-823](https://jira.issues.couchbase.com/browse/CXXCBC-823): Fixed http\_session manager `check_in()` to remove sessions from the pending/idle session maps when a session is not connected, and updated each session's `on_stop()` to remove itself from all session maps.

[CXXCBC-828](https://jira.issues.couchbase.com/browse/CXXCBC-828): Replaced inline `std::regex` construction with `std::string::find()` when building errors from server response text in collection and scope management operations.

[CXXCBC-829](https://jira.issues.couchbase.com/browse/CXXCBC-829): Added `utils::contains_string(input, substr, ignore_case = false)`, a substring match with optional ASCII-only case folding and no `std::locale` dependency, and replaced the remaining `std::regex_search` calls with it.

[CXXCBC-839](https://jira.issues.couchbase.com/browse/CXXCBC-839): Push configuration notifications are now filtered strictly by session bucket binding.

### [](#version-4-6-1-29-april-2026)Version 4.6.1 (29 April 2026)

Version 4.6.1 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.6.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.6.1/>

#### [](#enhancements-2)Enhancements

* [PYCBC-1752](https://issues.couchbase.com/browse/PYCBC-1752): Added `ClusterOption` to enable lazy connections in C++ core.
* [PYCBC-1761](https://jira.issues.couchbase.com/browse/PYCBC-1761), [PYCBC-1762](https://jira.issues.couchbase.com/browse/PYCBC-1762), [PYCBC-1763](https://jira.issues.couchbase.com/browse/PYCBC-1763), [PYCBC-1764](https://jira.issues.couchbase.com/browse/PYCBC-1764), [PYCBC-1765](https://jira.issues.couchbase.com/browse/PYCBC-1765): Observability Improvements. The SDK has improved performance for both default observability (`ThresholdLogging` and `MeterLogging`) and non-observability (tracing and metrics disabled) use cases.

#### [](#fixes-2)Fixes

* [PYCBC-1753](https://issues.couchbase.com/browse/PYCBC-1753): Updated SDK to pass `scope_name` or `bucket_name` when using scoped search indexes.
* [PYCBC-1758](https://issues.couchbase.com/browse/PYCBC-1758): Updated SDK to propagate all `ClusterOptions` to the C++ core.
* [PYCBC-1759](https://issues.couchbase.com/browse/PYCBC-1759): Fixed compounding encoding span attribute propagation for multi operations.

### [](#version-4-6-0-31-march-2026)Version 4.6.0 (31 March 2026)

Version 4.6.0 is a minor release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.6.0 release adds observability support (with the ability to integrate with OpenTelemetry) and adds support for Python 3.14 — see [Python Version Compatibility](compatibility.md#python-version-compat) for details of supported Python versions.

```bash
$ python3 -m pip install couchbase==4.6.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.6.0/>

#### [](#behavioral-changes)Behavioral Changes

The Couchbase Python SDK no longer provides Python 3.9 wheels as Python 3.9 reached [end-of-life](https://peps.python.org/pep-0596/#lifespan) in October 2025\. See [Python Version Compatibility](compatibility.md#python-version-compat) for details on supported Python versions.

Multi operations that allow for durability no longer allow client and server durability to be mixed across operations. If durability is specified for a multi operation, any per-key-options must use the same durability type (either client or server durability).

All APIs (`acouchbase`, `couchbase`, and `txcouchbase`) no longer allow a cluster that has been closed to be reconnected. Any attempt to use a closed cluster will raise an exception. In order to establish a new connection after closing a cluster, a new cluster instance must be created.

The `QueryIndexManagement` `create_index()` API no longer allows `fields` to be used to specify index keys. The `keys` field must be used to indicate the keys to use in the index.

#### [](#enhancements-3)Enhancements

* [PYCBC-1700](https://jira.issues.couchbase.com/browse/PYCBC-1700), [PYCBC-1724](https://jira.issues.couchbase.com/browse/PYCBC-1724): Added support for Python 3.14.
* [PYCBC-1701](https://jira.issues.couchbase.com/browse/PYCBC-1701): Dropped support for Python 3.9.
* [PYCBC-1714](https://jira.issues.couchbase.com/browse/PYCBC-1714): Added support mTLS Certs Refresh (without restart).
* [PYCBC-1715](https://jira.issues.couchbase.com/browse/PYCBC-1715): Added support for JWT based authentication in Operational SDKs.
* [PYCBC-1718](https://jira.issues.couchbase.com/browse/PYCBC-1718), [PYCBC-1723](https://jira.issues.couchbase.com/browse/PYCBC-1722), [PYCBC-1721](https://jira.issues.couchbase.com/browse/PYCBC-1722), [PYCBC-1722](https://jira.issues.couchbase.com/browse/PYCBC-1722), [PYCBC-1728](https://jira.issues.couchbase.com/browse/PYCBC-1722), [PYCBC-1750](https://jira.issues.couchbase.com/browse/PYCBC-1750): Added Observability Support. The SDK now natively supports Tracing, Metrics, and `OTel` Integration.
* [PYCBC-1727](https://jira.issues.couchbase.com/browse/PYCBC-1727): Deprecated support for MapReduce Views (which is also now deprecated in Couchbase Server).
* [PYCBC-1730](https://jira.issues.couchbase.com/browse/PYCBC-1730), [PYCBC-1731](https://jira.issues.couchbase.com/browse/PYCBC-1731), [PYCBC-1733](https://jira.issues.couchbase.com/browse/PYCBC-1733), [PYCBC-1734](https://jira.issues.couchbase.com/browse/PYCBC-1734), [PYCBC-1735](https://jira.issues.couchbase.com/browse/PYCBC-1735), [PYCBC-1736](https://jira.issues.couchbase.com/browse/PYCBC-1736), [PYCBC-1737](https://jira.issues.couchbase.com/browse/PYCBC-1737), [PYCBC-1738](https://jira.issues.couchbase.com/browse/PYCBC-1738), [PYCBC-1739](https://jira.issues.couchbase.com/browse/PYCBC-1739), [PYCBC-1740](https://jira.issues.couchbase.com/browse/PYCBC-1740), [PYCBC-1742](https://jira.issues.couchbase.com/browse/PYCBC-1742), [PYCBC-1743](https://jira.issues.couchbase.com/browse/PYCBC-1743), [PYCBC-1756](https://jira.issues.couchbase.com/browse/PYCBC-1756): Migrated internal SDK APIs away from Wrapper decorators.
* [PYCBC-1745](https://jira.issues.couchbase.com/browse/PYCBC-1745), [PYCBC-1747](https://jira.issues.couchbase.com/browse/PYCBC-1747): Use C++ Templating System for SDK C-Extension.
* [PYCBC-1754](https://jira.issues.couchbase.com/browse/PYCBC-1754): Added Logging Improvements.
* [PYCBC-1755](https://jira.issues.couchbase.com/browse/PYCBC-1755): Updated `JSONType` type hint to adhere to static typing standards.

#### [](#fixes-3)Fixes

* [PYCBC-1725](https://jira.issues.couchbase.com/browse/PYCBC-1725): Fixed decoding to be deferred until result is accessed by `*Result` object.
* [PYCBC-1744](https://jira.issues.couchbase.com/browse/PYCBC-1744): Fixed cluster instances across all APIs to not allow reconnect after close.

#### [](#known-issues)Known Issues

* [PYCBC-1758](https://issues.couchbase.com/browse/PYCBC-1758): This version of the SDK does not propagate a small number of `ClusterOptions` to the C++ core. This is fixed in the next patch release (4.6.1).
* [PYCBC-1753](https://issues.couchbase.com/browse/PYCBC-1753): In 4.6.0, the Python Client is not passing `scope_name` or `bucket_name` when using scoped search indexes. This is fixed in the next patch release (4.6.1).

#### [](#underlying-c-sdk-core-changes-2)Underlying C++ SDK Core Changes

* [CXXCBC-732](https://jira.issues.couchbase.com/browse/CXXCBC-732): Fixed memory leaks in concurrent fixed queue reporting.
* [CXXCBC-739](https://jira.issues.couchbase.com/browse/CXXCBC-739): **mTLS Certificate Refresh** — Added support for refreshing TLS certificates without restarting the application. Certificates can now be updated via `cluster::update_credentials()` and new TLS sessions will use the updated certificates.
* [CXXCBC-740](https://jira.issues.couchbase.com/browse/CXXCBC-740): **JWT Authentication** — Added JWT-based authentication support via `jwt_authenticator`. The authenticator can refresh tokens automatically and supports reauthentication when tokens become stale.
* [CXXCBC-745](https://jira.issues.couchbase.com/browse/CXXCBC-745): **Lazy Connections Mode** — Added new `enable_lazy_connections` option that delays opening KV connections until the first operation is executed, reducing initial connection overhead.
* [CXXCBC-750](https://jira.issues.couchbase.com/browse/CXXCBC-750): **Internal Tracer for Wrapper SDKs** — Added internal tracer interface (`tracer_wrapper::wrapped()`) for use by wrapper SDKs that want to integrate with the SDK's tracing.
* [CXXCBC-752](https://jira.issues.couchbase.com/browse/CXXCBC-752): MapReduce Views are now deprecated. Use Query with SQL++ instead.
* [CXXCBC-763](https://jira.issues.couchbase.com/browse/CXXCBC-763): Fixed `set_authenticator` not applying updated cert/key pairs to new TLS sessions.
* [CXXCBC-766](https://jira.issues.couchbase.com/browse/CXXCBC-766): Fixed `OpenSSL` headers priority in `BoringSSL` builds.
* [CXXCBC-767](https://jira.issues.couchbase.com/browse/CXXCBC-767): Implemented `AuthStale` handling and JWT reauthentication support.
* [CXXCBC-768](https://jira.issues.couchbase.com/browse/CXXCBC-768): **DNS-SRV Refresh Fix** — Fixed an issue where `bucket_not_found` errors during bootstrap would trigger unnecessary DNS-SRV record refresh loops.
* [CXXCBC-771](https://jira.issues.couchbase.com/browse/CXXCBC-771): **Credentials Update Restrictions** — `cluster::update_credentials()` now prevents switching between authenticator types (e.g., password to certificate) to avoid unexpected behavior.
* **Mozilla Certificate Parsing** — Updated the regex for parsing the header date of Mozilla certificates from curl.se to ensure correct certificate handling and added a warning if the header date is not found.

## [](#python-sdk-4-5-releases)Python SDK 4.5 Releases

### [](#version-4-5-0-29-september-2025)Version 4.5.0 (29 September 2025)

Version 4.5.0 is a minor release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.5.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.5.0/>

#### [](#behavioral-changes-2)Behavioral Changes

The Couchbase Python SDK will stop providing Python 3.9 wheels in a future release as Python 3.9 will reach [end-of-life](https://peps.python.org/pep-0596/#lifespan) in October 2025\. See [Python Version Compatibility](compatibility.md#python-version-compat) for details on supported Python versions.

The "auto" network selection heuristic in the underyling C++ core has been changed to fall back to the "external" network if the "external" network is present. Previously, if there was no exact match between an address in the connection string and an address in the cluster topology reported by the server, the SDK would select the "default" network. Now, if there is no match and an "external" network is present, the SDK selects the "external" network.

#### [](#enhancements-4)Enhancements

* [PYCBC-1641](https://jira.issues.couchbase.com/browse/PYCBC-1641): Updated development dependencies.
* [PYCBC-1666](https://jira.issues.couchbase.com/browse/PYCBC-1666): Added support "access\_deleted" for replica reads.
* [PYCBC-1667](https://jira.issues.couchbase.com/browse/PYCBC-1667): Updated supported bucket & storage types.
* [PYCBC-1668](https://jira.issues.couchbase.com/browse/PYCBC-1668): Improved error messages for account lock/unlock feature.
* [PYCBC-1689](https://jira.issues.couchbase.com/browse/PYCBC-1689): Updated operational SDK prevent connection to Analytics 2.0 Cluster
* [PYCBC-1690](https://jira.issues.couchbase.com/browse/PYCBC-1690): Added `_repr_()` and `_str_()` methods for search queries.
* [PYCBC-1691](https://jira.issues.couchbase.com/browse/PYCBC-1691): Updated `ConjunctionQuery` and `DisjunctionQuery` to allow list of queries as input.
* [PYCBC-1693](https://jira.issues.couchbase.com/browse/PYCBC-1693): Added `CollectionQueryIndexManager` to API reference.
* [PYCBC-1699](https://jira.issues.couchbase.com/browse/PYCBC-1699): Updated SDK build setup to include C++ core changes.
* [PYCBC-1703](https://jira.issues.couchbase.com/browse/PYCBC-1703): Added Graviton 3 and 4 executors to test pipeline matrices.
* [PYCBC-1698](https://jira.issues.couchbase.com/browse/PYCBC-1698), [PYCBC-1704](https://jira.issues.couchbase.com/browse/PYCBC-1704): Improved Jenkins Integration Tests.
* [PYCBC-1711](https://jira.issues.couchbase.com/browse/PYCBC-1711): Updated bucket creation to not set `bucketType`, `replicaIndex`, `flushEnabled` unless set by the user.

#### [](#fixes-4)Fixes

* [PYCBC-1694](https://jira.issues.couchbase.com/browse/PYCBC-1694): Fixed boolean search queries to allow `should.min=0`.
* [PYCBC-1705](https://jira.issues.couchbase.com/browse/PYCBC-1705): Fixed encryption import order and exceptions.

#### [](#underlying-c-sdk-core-changes-3)Underlying C++ SDK Core Changes

##### [](#new-features)New Features

* [CXXCBC-653](https://jira.issues.couchbase.com/browse/CXXCBC-653): Added support "access\_deleted" for Replica Reads ([#821](https://github.com/couchbase/couchbase-cxx-client/pull/821)).
* [CXXCBC-639](https://jira.issues.couchbase.com/browse/CXXCBC-639): Added support of building both static and shared libraries ([#707](https://github.com/couchbase/couchbase-cxx-client/pull/707), [#825](https://github.com/couchbase/couchbase-cxx-client/pull/825)).
* [CXXCBC-692](https://jira.issues.couchbase.com/browse/CXXCBC-692): The SDK now prevents connection to Enterprise Analytics cluster ([#792](https://github.com/couchbase/couchbase-cxx-client/pull/792), [#807](https://github.com/couchbase/couchbase-cxx-client/pull/807), [#810](https://github.com/couchbase/couchbase-cxx-client/pull/810)).
* [CXXCBC-693](https://jira.issues.couchbase.com/browse/CXXCBC-693): Do not return an error if/when `indexDefs` are empty/null. Instead return w/ an empty list of index definitions ([#800](https://github.com/couchbase/couchbase-cxx-client/pull/800)).
* [CXXCBC-698](https://jira.issues.couchbase.com/browse/CXXCBC-698): Added `flex_index` to `transaction_query_options` ([#773](https://github.com/couchbase/couchbase-cxx-client/pull/773)).
* [CXXCBC-699](https://jira.issues.couchbase.com/browse/CXXCBC-699): Added support of randomization of bootstrap nodes ([#777](https://github.com/couchbase/couchbase-cxx-client/pull/777)).
* [CXXCBC-707](https://jira.issues.couchbase.com/browse/CXXCBC-707): Updated network selection heuristic. The logic is improved in certain cloud-specific cases ([#809](https://github.com/couchbase/couchbase-cxx-client/pull/809)).

##### [](#fixes-and-enhancements-2)Fixes and Enhancements

* [CXXCBC-651](https://jira.issues.couchbase.com/browse/CXXCBC-651): Added preserving cached node labels after generating report in app telemetry meter ([#802](https://github.com/couchbase/couchbase-cxx-client/pull/802)).
* [CXXCBC-695](https://jira.issues.couchbase.com/browse/CXXCBC-695): Always return unwrapped `doc_exists` from transactions insert (<https://github.com/couchbase/couchbase-cxx-client/pull/771>.\[#771.\]).
* [CXXCBC-704](https://jira.issues.couchbase.com/browse/CXXCBC-704): Added handling `document_unretrievable` from `get_multi` individual fetch ([#782](https://github.com/couchbase/couchbase-cxx-client/pull/782), [#785](https://github.com/couchbase/couchbase-cxx-client/pull/785)).
* [CXXCBC-706](https://jira.issues.couchbase.com/browse/CXXCBC-706): Added closing of half-baked cluster object if connection fails ([#783](https://github.com/couchbase/couchbase-cxx-client/pull/783)).
* [CXXCBC-709](https://jira.issues.couchbase.com/browse/CXXCBC-709): Fix `exists()` in transactions `get_multi` result ([#786](https://github.com/couchbase/couchbase-cxx-client/pull/786)).
* [CXXCBC-715](https://jira.issues.couchbase.com/browse/CXXCBC-715): Fixed Hard Failover Intermittent Crash in HTTP connection manager ([#818](https://github.com/couchbase/couchbase-cxx-client/pull/818)).
* [CXXCBC-721](https://jira.issues.couchbase.com/browse/CXXCBC-721): Added caching of `FeatureNotAvailable` transactions operation failure for `get_replica*` operations ([#823](https://github.com/couchbase/couchbase-cxx-client/pull/823)).
* [CXXCBC-726](https://jira.issues.couchbase.com/browse/CXXCBC-726): Added KV scan timeout to cluster options ([#830](https://github.com/couchbase/couchbase-cxx-client/pull/830)).
* [CXXCBC-733](https://jira.issues.couchbase.com/browse/CXXCBC-733): Fixed build with BoringSSL ([#839](https://github.com/couchbase/couchbase-cxx-client/pull/839)).

## [](#python-sdk-4-4-releases)Python SDK 4.4 Releases

### [](#version-4-4-1-29-september-2025)Version 4.4.1 (29 September 2025)

Version 4.4.1 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.4.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.4.1/>

#### [](#enhancements-5)Enhancements

* [PYCBC-1699](https://jira.issues.couchbase.com/browse/PYCBC-1699): Updated SDK build setup to include C++ core changes.
* [PYCBC-1703](https://jira.issues.couchbase.com/browse/PYCBC-1703): Added Graviton 3 and 4 executors to test pipeline matrices.

#### [](#fixes-5)Fixes

* [PYCBC-1705](https://jira.issues.couchbase.com/browse/PYCBC-1705): Fixed encryption import order and exceptions.

#### [](#underlying-c-sdk-core-changes-4)Underlying C++ SDK Core Changes

##### [](#new-features-2)New Features

* [CXXCBC-699](https://jira.issues.couchbase.com/browse/CXXCBC-699): Added support of randomization of bootstrap nodes ([#778](https://github.com/couchbase/couchbase-cxx-client/pull/778)).

##### [](#fixes-and-enhancements-3)Fixes and Enhancements

* [CXXCBC-651](https://jira.issues.couchbase.com/browse/CXXCBC-651): Preserve cached node labels after generating report in app telemetry meter ([#804](https://github.com/couchbase/couchbase-cxx-client/pull/804)).
* [CXXCBC-693](https://jira.issues.couchbase.com/browse/CXXCBC-693): Do not return an error if/when `indexDefs` are empty/null. Instead return w/ an empty list of index definitions ([#801](https://github.com/couchbase/couchbase-cxx-client/pull/801)).
* [CXXCBC-709](https://jira.issues.couchbase.com/browse/CXXCBC-709): Fix `exists()` in transactions `get_multi` result ([#787](https://github.com/couchbase/couchbase-cxx-client/pull/787)).
* [CXXCBC-715](https://jira.issues.couchbase.com/browse/CXXCBC-715): Fixed intermittent crash during hard failover in HTTP connection manager ([\[#817](https://github.com/couchbase/couchbase-cxx-client/pull/817)).

### [](#version-4-4-0-02-june-2025)Version 4.4.0 (02 June 2025)

Version 4.4.0 is the minor release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.4.0 release adds support for Vector Search pre-filters, transactional Zone Aware Replica Reads and transactional GetMulti.

```bash
$ python3 -m pip install couchbase==4.4.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.4.0/>

#### [](#enhancements-6)Enhancements

* [PYCBC-1594](https://jira.issues.couchbase.com/browse/PYCBC-1594), [PYCBC-1647](https://jira.issues.couchbase.com/browse/PYCBC-1647): Added support for Zone Aware Read from Replica.
* [PYCBC-1634](https://jira.issues.couchbase.com/browse/PYCBC-1634): Added support for SDK Telemetry Collection in Server.
* [PYCBC-1657](https://jira.issues.couchbase.com/browse/PYCBC-1657), [PYCBC-1685](https://jira.issues.couchbase.com/browse/PYCBC-1685): Added support for transactions `ExtGetMulti` (aka Enhanced Read Committed Isolation).
* [PYCBC-1668](https://jira.issues.couchbase.com/browse/PYCBC-1668): Improved SDK error messages for account lock/unlock feature.
* [PYCBC-1676](https://jira.issues.couchbase.com/browse/PYCBC-1676): Fixed async query examples to use async (`acouchbase`) API instead of blocking API.
* [PYCBC-1678](https://jira.issues.couchbase.com/browse/PYCBC-1678): Pinned `setup_requires` cmake version.
* [PYCBC-1680](https://jira.issues.couchbase.com/browse/PYCBC-1680): Added support for Vector Search pre-filters.
* [PYCBC-1681](https://jira.issues.couchbase.com/browse/PYCBC-1681): Updated `VectorQuery` validation to raise `InvalidArgumentException` when base64 vector string is empty.
* [PYCBC-1682](https://jira.issues.couchbase.com/browse/PYCBC-1682): Updated storage backend to be the server default when creating buckets.

#### [](#fixes-6)Fixes

* [PYCBC-1674](https://jira.issues.couchbase.com/browse/PYCBC-1674): `get_replica_from_preferred_server_group` was trying to access a \_ctx attribute on AttemptContextLogic that no longer exists. This has been fixed, and it no longer raises an `AttributeError`.
* [PYCBC-1675](https://jira.issues.couchbase.com/browse/PYCBC-1675): CAS is no longer ignored for append/prepend operations.
* [PYCBC-1679](https://jira.issues.couchbase.com/browse/PYCBC-1679): Console logger is now disabled when the file logger specified.
* [PYCBC-1683](https://jira.issues.couchbase.com/browse/PYCBC-1683): Fixed search range queries to follow RFC.
* [PYCBC-1685](https://jira.issues.couchbase.com/browse/PYCBC-1685): Removed timeout logic when waiting for C++ core HTTP response.

#### [](#underlying-c-sdk-core-changes-5)Underlying C++ SDK Core Changes

##### [](#new-features-3)New Features

* [CXXCBC-605](https://jira.issues.couchbase.com/browse/CXXCBC-605): Added custom log callback functionality ([#743](https://github.com/couchbase/couchbase-cxx-client/pull/743)).
* [CXXCBC-626](https://jira.issues.couchbase.com/browse/CXXCBC-626): Application Service Telemetry, for future Server releases ([#712](https://github.com/couchbase/couchbase-cxx-client/pull/712), [#719](https://github.com/couchbase/couchbase-cxx-client/pull/719), [#739](https://github.com/couchbase/couchbase-cxx-client/pull/739), [#750](https://github.com/couchbase/couchbase-cxx-client/pull/750)).
* [CXXCBC-654](https://jira.issues.couchbase.com/browse/CXXCBC-654): Added `num_vbuckets` to `bucket_settings` ([#746](https://github.com/couchbase/couchbase-cxx-client/pull/746)).
* [CXXCBC-665](https://jira.issues.couchbase.com/browse/CXXCBC-665): The SDK will now always return partial results for `*_all_replica` operations if some `get_replica` requests succeeded ([#742](https://github.com/couchbase/couchbase-cxx-client/pull/742)).
* [CXXCBC-672](https://jira.issues.couchbase.com/browse/CXXCBC-672): Added `add_named_parameter` and `add_positional_parameter` to query/analytics options ([#762](https://github.com/couchbase/couchbase-cxx-client/pull/762)).
* [CXXCBC-684](https://jira.issues.couchbase.com/browse/CXXCBC-684): The SDK now allows the setting of both named and positional parameters for queries — previously named parameters would be cleared if positional parameters were set ([#759](https://github.com/couchbase/couchbase-cxx-client/pull/759)).

##### [](#fixes-and-enhancements-4)Fixes and Enhancements

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
* [CXXCBC-688](https://jira.issues.couchbase.com/browse/CXXCBC-688): Don't convert Public API TOF from lambda to Core API's TOF, rely on internal state ([#765](https://github.com/couchbase/couchbase-cxx-client/pull/765)).
* [CXXCBC-690](https://jira.issues.couchbase.com/browse/CXXCBC-690): Don't move `staged_mutation` item when capturing it in `commit_doc` lambdas ([#767](https://github.com/couchbase/couchbase-cxx-client/pull/767)).

## [](#python-sdk-4-3-releases)Python SDK 4.3 Releases

### [](#version-4-3-6-15-may-2025)Version 4.3.6 (15 May 2025)

Version 4.3.6 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```console
$ python3 -m pip install couchbase==4.3.6
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.3.6/>

#### [](#enhancements-7)Enhancements

* [PYCBC-1676](https://jira.issues.couchbase.com/browse/PYCBC-1676): Fixed async query examples to use async (`acouchbase`) API instead of blocking API.
* [PYCBC-1678](https://jira.issues.couchbase.com/browse/PYCBC-1678): Pinned `setup_requires` cmake version.
* [PYCBC-1681](https://jira.issues.couchbase.com/browse/PYCBC-1681): Updated `VectorQuery` validation to raise `InvalidArgumentException` when base64 vector string is empty.

#### [](#fixes-7)Fixes

* [PYCBC-1674](https://jira.issues.couchbase.com/browse/PYCBC-1674): Fixed transactional `get_replica_from_preferred_server_group` from raising `AttributeError`.
* [PYCBC-1675](https://jira.issues.couchbase.com/browse/PYCBC-1675): CAS is no longer ignored for append/prepend operations.
* [PYCBC-1679](https://jira.issues.couchbase.com/browse/PYCBC-1679): Console logger is now disabled when the file logger is specified.
* [PYCBC-1683](https://jira.issues.couchbase.com/browse/PYCBC-1683): Fixed search range queries to follow RFC.
* [PYCBC-1685](https://jira.issues.couchbase.com/browse/PYCBC-1685): Removed timeout logic when waiting for C++ core HTTP response.

#### [](#underlying-c-sdk-core-changes-6)Underlying C++ SDK Core Changes

##### [](#fixes-8)Fixes

* [CXXCBC-666](https://jira.issues.couchbase.com/browse/CXXCBC-666): The `pkg-config` file now returns the full path for the lib dir, instead of the relative path ([#736](https://github.com/couchbase/couchbase-cxx-client/pull/736)).
* [CXXCBC-667](https://jira.issues.couchbase.com/browse/CXXCBC-667): Core implementation of prepend/append now encodes the CAS value ([#738](https://github.com/couchbase/couchbase-cxx-client/pull/738)).
* [CXXCBC-671](https://jira.issues.couchbase.com/browse/CXXCBC-671): Updated snappy to support `CMake` `4.0` ([#745](https://github.com/couchbase/couchbase-cxx-client/pull/745)).

### [](#version-4-3-5-28-january-2025)Version 4.3.5 (28 January 2025)

Version 4.3.5 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```console
$ python3 -m pip install couchbase==4.3.5
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.3.5/>

#### [](#enhancements-8)Enhancements

* [PYCBC-1643](https://jira.issues.couchbase.com/browse/PYCBC-1643): Updated build system logic when finding Python 3 version.
* [PYCBC-1644](https://jira.issues.couchbase.com/browse/PYCBC-1644): Updateed GoCAVES download URL to use arm64 version when appropriate (CI improvement).
* [PYCBC-1646](https://jira.issues.couchbase.com/browse/PYCBC-1646): Migrated transactions to use `transaction_context`.
* [PYCBC-1648](https://jira.issues.couchbase.com/browse/PYCBC-1648): Added `update_collection` & settings classes to Collection Management API reference.

#### [](#fixes-9)Fixes

* [PYCBC-1649](https://jira.issues.couchbase.com/browse/PYCBC-1649): Fixed a memory leak when creating `TransactionGetResult`.

#### [](#underlying-c-sdk-core-changes-7)Underlying C++ SDK Core Changes

##### [](#enhancements-9)Enhancements

* [CXXCBC-638](https://jira.issues.couchbase.com/browse/CXXCBC-638): Switched SDK to use bundled `fmtlib` for `spdlog` ([#705](https://github.com/couchbase/couchbase-cxx-client/pull/705)).
* [CXXCBC-640](https://jira.issues.couchbase.com/browse/CXXCBC-640): Debug symbols are no longer forced for release builds ([#708](https://github.com/couchbase/couchbase-cxx-client/pull/708)).

##### [](#fixes-10)Fixes

* [CXXCBC-633](https://jira.issues.couchbase.com/browse/CXXCBC-633): In a case of timeout, when the total deadline of the DNS-SRV request has been reached, the library will now report a timeout error code, and not the latest abort as it was doing.

### [](#version-4-3-4-25-november-2024)Version 4.3.4 (25 November 2024)

Version 4.3.4 is the next patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.3.4 release adds support for Python 3.13 — see [Python Version Compatibility](compatibility.md#python-version-compat) for details of supported Python versions.

```console
$ python3 -m pip install couchbase==4.3.4
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.3.4/>

#### [](#behavioral-change)Behavioral Change

The Couchbase Python SDK no longer provides Python 3.8 wheels as Python 3.8 has reached [end-of-life](https://peps.python.org/pep-0569/#lifespann). See [Python Version Compatibility](compatibility.md#python-version-compat) for details on supported Python versions.

#### [](#enhancements-10)Enhancements

* [PYCBC-1595](https://jira.issues.couchbase.com/browse/PYCBC-1595): Added support for Binary Objects in Transactions.
* [PYCBC-1613](https://jira.issues.couchbase.com/browse/PYCBC-1613): Added Python 3.13 Support.
* [PYCBC-1635](https://jira.issues.couchbase.com/browse/PYCBC-1635): Removed support for publishing Python 3.8 wheels.
* [PYCBC-1639](https://jira.issues.couchbase.com/browse/PYCBC-1639): Updated user agent extra passed to C++ core.
* [PYCBC-1640](https://jira.issues.couchbase.com/browse/PYCBC-1640): Added acouchbase utility tests.

#### [](#fixes-11)Fixes

* [PYCBC-1631](https://jira.issues.couchbase.com/browse/PYCBC-1631): Fixed transaction hangs when logging is set to `DEBUG`.
* [PYCBC-1636](https://jira.issues.couchbase.com/browse/PYCBC-1636): Fixed acouchbase API to properly handle `BaseException`.

#### [](#underlying-c-sdk-core-changes-8)Underlying C++ SDK Core Changes

##### [](#fixes-12)Fixes

* [CXXCBC-611](https://jira.issues.couchbase.com/browse/CXXCBC-611), [CXXCBC-612](https://jira.issues.couchbase.com/browse/CXXCBC-612): The C++ SDK now follows RFC naming for metric operation names ([#695](https://github.com/couchbase/couchbase-cxx-client/pull/695)).
* [CXXCBC-615](https://jira.issues.couchbase.com/browse/CXXCBC-615): The C++ SDK now exposes `insert_raw` and `replace_raw` in the core transactions attempt context ([#686](https://github.com/couchbase/couchbase-cxx-client/pull/686)).
* [CXXCBC-620](https://jira.issues.couchbase.com/browse/CXXCBC-620): Updated core `analytics_link_get_all` to follow the RFC ([#687](https://github.com/couchbase/couchbase-cxx-client/pull/687)).
* [CXXCBC-624](https://jira.issues.couchbase.com/browse/CXXCBC-624): Fixed user agent ID generation ([#692](https://github.com/couchbase/couchbase-cxx-client/pull/692)).
* [CXXCBC-632](https://jira.issues.couchbase.com/browse/CXXCBC-632): A crash on testing against Analytics nodes under rebalance was caused by the assumption that Analytics would always send meta fields in its response. This has now been fixed, and the behoavior should not recur ([#699](https://github.com/couchbase/couchbase-cxx-client/pull/699)).

### [](#version-4-3-3-22-october-2024)Version 4.3.3 (22 October 2024)

Version 4.3.3 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```console
$ python3 -m pip install couchbase==4.3.3
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.3.3/>

#### [](#behavioral-change-2)Behavioral Change

The Couchbase Python SDK will stop providing Python 3.8 wheels with the next release (4.3.4) as Python 3.8 has reached [end-of-life](https://peps.python.org/pep-0569/#lifespann). See [Python Version Compatibility](compatibility.md#python-version-compat) for details on supported Python versions.

#### [](#enhancements-11)Enhancements

* [PYCBC-1456](https://jira.issues.couchbase.com/browse/PYCBC-1456): Ensure SDK encodes URIs.
* [PYCBC-1619](https://jira.issues.couchbase.com/browse/PYCBC-1619): Added ability to use C++ core file logger.
* [PYCBC-1625](https://jira.issues.couchbase.com/browse/PYCBC-1625): Updated multi methods to `COMMITTED`.

#### [](#fixes-13)Fixes

* [PYCBC-1569](https://jira.issues.couchbase.com/browse/PYCBC-1569): Added mechanism to do binary increment/decrement without initial value.
* [PYCBC-1628](https://jira.issues.couchbase.com/browse/PYCBC-1628): Fixed typo in `InvalidArgumentException` message when invalid authentication `kwargs` are provided.
* [PYCBC-1629](https://jira.issues.couchbase.com/browse/PYCBC-1629): Fixed subdocument `array_addunique` to follow the [RFC](https://github.com/couchbaselabs/sdk-rfcs/blob/master/rfc/0053-sdk3-crud.md#mutatein).

#### [](#underlying-c-sdk-core-changes-9)Underlying C++ SDK Core Changes

##### [](#enhancements-12)Enhancements

* [CXXCBC-552](http://jira.issues.couchbase.com/browse/CXXCBC-582): Cleaned up network selection options ([#677](https://github.com/couchbase/couchbase-cxx-client/pull/677), [#682](https://github.com/couchbase/couchbase-cxx-client/pull/682)). Added cluster labels and system tag to spans. Added cluster labels, keyspace, and outcome to metrics.

##### [](#fixes-14)Fixes

* [CXXCBC-311](http://jira.issues.couchbase.com/browse/CXXCBC-311): Ensure SDK encodes URIs ([#674](https://github.com/couchbase/couchbase-cxx-client/pull/674)).
* [CXXCBC-599](http://jira.issues.couchbase.com/browse/CXXCBC-599): Updated allowed connection string options ([#668](https://github.com/couchbase/couchbase-cxx-client/pull/668)).
* [CXXCBC-606](http://jira.issues.couchbase.com/browse/CXXCBC-606): Fixed detection of dysfunctional node ([#673](https://github.com/couchbase/couchbase-cxx-client/pull/673)).
* [CXXCBC-614](http://jira.issues.couchbase.com/browse/CXXCBC-614): Fixed memory leak in `observe_poll` ([#679](https://github.com/couchbase/couchbase-cxx-client/pull/679)).

### [](#version-4-3-2-24-september-2024)Version 4.3.2 (24 September 2024)

Version 4.3.2 is the next patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.3.2 release adds support for Python 3.12 — see [Python Version Compatibility](compatibility.md#python-version-compat) for details of supported Python versions.

```console
$ python3 -m pip install couchbase==4.3.2
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.3.2/>

#### [](#behavioral-change-3)Behavioral Change

The Couchbase Python SDK will soon stop providing Python 3.8 wheels as Python 3.8 reaches [end-of-life](https://peps.python.org/pep-0569/#lifespann) in October 2024\. See [Python Version Compatibility](compatibility.md#python-version-compat) for details of supported Python versions.

#### [](#enhancements-13)Enhancements

* [PYCBC-1563](https://jira.issues.couchbase.com/browse/PYCBC-1563): Added Python 3.12 Support.

#### [](#underlying-c-sdk-core-changes-10)Underlying C++ SDK Core Changes

##### [](#fixes-15)Fixes

* [CXXCBC-577](http://jira.issues.couchbase.com/browse/CXXCBC-577), [CXXCBC-552](http://jira.issues.couchbase.com/browse/CXXCBC-552), & [CXXCBC-576](http://jira.issues.couchbase.com/browse/CXXCBC-576): See [C++ 1.0.2 release notes](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-2-23-september-2024).

### [](#version-4-3-1-26-august-2024)Version 4.3.1 (26 August 2024)

Version 4.3.1 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```console
$ python3 -m pip install couchbase==4.3.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.3.1/>

#### [](#fixes-16)Fixes

* [PYCBC-1612](https://issues.couchbase.com/browse/PYCBC-1612): Fixed multi-mutation operations to honor durability when passed in options.

#### [](#underlying-c-sdk-core-changes-11)Underlying C++ SDK Core Changes

##### [](#enhancements-14)Enhancements

* Improve logging of DNS client ([#634](https://github.com/couchbase/couchbase-cxx-client/pull/634)).
* [CXXCBC-568](https://issues.couchbase.com/browse/CXXCBC-568/): Cancel deferred operations when closing HTTP session manager ([#643](https://github.com/couchbase/couchbase-cxx-client/pull/643)).

##### [](#fixes-17)Fixes

* [CXXCBC-531](https://issues.couchbase.com/browse/CXXCBC-531/): Fixed memory leak in range scan implementation ([#645](https://github.com/couchbase/couchbase-cxx-client/pull/645), [#610](https://github.com/couchbase/couchbase-cxx-client/pull/610)).
* [CXXCBC-572](https://issues.couchbase.com/browse/CXXCBC-572/): Always initialize service\_type ([#610](https://github.com/couchbase/couchbase-cxx-client/pull/610)).
* [CXXCBC-569](https://issues.couchbase.com/browse/CXXCBC-569/): Resolved cycle in shared pointers for `transaction_context`([#641](https://github.com/couchbase/couchbase-cxx-client/pull/641)).
* [CXXCBC-550](https://issues.couchbase.com/browse/CXXCBC-550/): Fixed use-after-move issue in command handler ([#628](https://github.com/couchbase/couchbase-cxx-client/pull/628)).
* Fixed behaviour when reading is complete before returning HTTP streaming resp ([#624](https://github.com/couchbase/couchbase-cxx-client/pull/624)).

### [](#version-4-3-0-27-june-2024)Version 4.3.0 (27 June 2024)

Version 4.3.0 is next minor release of the fourth generation Python SDK, bringing a number of improvements. Most notably the 4.3.0 release adds support for base64 encoded vector types when using the SDK with Couchbase Server 7.6.2.

```console
$ python3 -m pip install couchbase==4.3.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.3.0/>

#### [](#fixes-18)Fixes

* [PYCBC-1596](https://issues.couchbase.com/browse/PYCBC-1596): Fixed `AnalyticsStatus` Enum values.
* [PYCBC-1603](https://issues.couchbase.com/browse/PYCBC-1603): Fixed `VectorQuery` validation to prevent empty `field_name`.

#### [](#enhancements-15)Enhancements

* [PYCBC-1597](https://issues.couchbase.com/browse/PYCBC-1597): Added Support for base64 encoded vector types.
* [PYCBC-1588](https://issues.couchbase.com/browse/PYCBC-1588): Added support for importing FTS index from JSON.

#### [](#underlying-c-sdk-core-changes-12)Underlying C++ SDK Core Changes

##### [](#enhancements-16)Enhancements

* [CXXCBC-381](https://issues.couchbase.com/browse/CXXCBC-381): Updated `transactions_context` and `attempt_context` to use `std::shared_ptr` ([#590](https://github.com/couchbaselabs/couchbase-cxx-client/pull/590)).

##### [](#fixes-19)Fixes

* [CXXCBC-445](https://issues.couchbase.com/browse/CXXCBC-445): Updated HTTP session logic to return `request_canceled` on IO error ([#568](https://github.com/couchbaselabs/couchbase-cxx-client/pull/568)).
* [CXXCBC-511](https://issues.couchbase.com/browse/CXXCBC-511): Updated HTTP session logic to prevent use of session if idle timer has expired ([#565](https://github.com/couchbaselabs/couchbase-cxx-client/pull/565)).
* [CXXCBC-517](https://issues.couchbase.com/browse/CXXCBC-517): Added HTTP session retries when client fails to resolve hostnames ([#589](https://github.com/couchbaselabs/couchbase-cxx-client/pull/589)).
* [CXXCBC-518](https://issues.couchbase.com/browse/CXXCBC-518): Fixed preferred node logic to handle alternate addresses ([#574](https://github.com/couchbaselabs/couchbase-cxx-client/pull/574)).
* [CXXCBC-523](https://issues.couchbase.com/browse/CXXCBC-523): Cleaned up config log output when `dump_configuration` is enabled ([#577](https://github.com/couchbaselabs/couchbase-cxx-client/pull/577)).
* Fixed config poll to skip config fetch if bucket does not have any sessions ([#573](https://github.com/couchbaselabs/couchbase-cxx-client/pull/573)).
* Cleaned up `attempt_context_impl` implementation ([#586](https://github.com/couchbaselabs/couchbase-cxx-client/pull/586)).

## [](#python-sdk-4-2-releases)Python SDK 4.2 Releases

### [](#version-4-2-1-18-april-2024)Version 4.2.1 (18 April 2024)

Version 4.2.1 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```console
$ python3 -m pip install couchbase==4.2.1
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.2.1/>

#### [](#fixes-20)Fixes

* [PYCBC-1575](https://issues.couchbase.com/browse/PYCBC-1575): Added missing logic to handle alternate addresses when bootstrapping.
* [PYCBC-1532](https://issues.couchbase.com/browse/PYCBC-1532), [PYCBC-1566](https://issues.couchbase.com/browse/PYCBC-1566), [PYCBC-1589](https://issues.couchbase.com/browse/PYCBC-1589): Fixed floating point exception if recieved config with empty vBucket map.
* [PYCBC-1590](https://issues.couchbase.com/browse/PYCBC-1590): Fixed Python logger shutdown process.

#### [](#enhancements-17)Enhancements

* [PYCBC-1584](https://issues.couchbase.com/browse/PYCBC-1584): Added support for scoped eventing functions.

#### [](#underlying-c-sdk-core-changes-13)Underlying C++ SDK Core Changes

##### [](#enhancements-18)Enhancements

* [CXXCBC-470](https://issues.couchbase.com/browse/CXXCBC-470): Distinguish between 'unset' and 'off' query\_profile ([#551](https://github.com/couchbaselabs/couchbase-cxx-client/pull/551)).
* [CXXCBC-489](https://issues.couchbase.com/browse/CXXCBC-489): Added support for scoped eventing functions ([#548](https://github.com/couchbaselabs/couchbase-cxx-client/pull/548), ([#554](https://github.com/couchbaselabs/couchbase-cxx-client/pull/554))).

##### [](#fixes-21)Fixes

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

#### [](#known-issues-2)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Python SDK that contains C++ SDK 1.0.0-dp.15 (or later).

#### [](#behavioral-change-4)Behavioral Change

It's important to use `Cluster.searchQuery()` / `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes. Method `Scope.search_query()` is now deprecated and will be removed in a future release. Method `Scope.search_query()` will _not_ work with scoped indexes.

#### [](#enhancements-19)Enhancements

* [PYCBC-1548](https://issues.couchbase.com/browse/PYCBC-1548): Added support for Vector Search.
* [PYCBC-1565](https://issues.couchbase.com/browse/PYCBC-1565): Updated C++ core for transactions metadata bucket improvements.
* [PYCBC-1572](https://issues.couchbase.com/browse/PYCBC-1572): Updated search API for SDK API 3.5 support. Included deprecation of `scope.search_query()`.

#### [](#underlying-c-sdk-core-changes-14)Underlying C++ SDK Core Changes

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

#### [](#known-issues-3)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Python SDK that contains C++ SDK 1.0.0-dp.15 (or later).

#### [](#fixes-22)Fixes

* [PYCBC-1555](https://issues.couchbase.com/browse/PYCBC-1555): Fixed bootstrap `select_bucket` logic to handle non-KV node.

#### [](#enhancements-20)Enhancements

* [PYCBC-1375](https://issues.couchbase.com/browse/PYCBC-1375): Updated Query Index Management Create Index Key Encoding.
* [PYCBC-1550](https://issues.couchbase.com/browse/PYCBC-1550): Added support for Scoped Search Indexes.
* [PYCBC-1523](https://issues.couchbase.com/browse/PYCBC-1523): Updated configuration logic when 0xd response is received.
* [PYCBC-1525](https://issues.couchbase.com/browse/PYCBC-1525): Added support for `LookupIn` and `MutateIn` macros.
* [PYCBC-1560](https://issues.couchbase.com/browse/PYCBC-1560): Updated `ViewQueryOptions` to include `full_set` and `raw` options.

#### [](#underlying-c-sdk-core-changes-15)Underlying C++ SDK Core Changes

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

#### [](#enhancements-21)Enhancements

* [PYCBC-1549](https://issues.couchbase.com/browse/PYCBC-1549): Added support for `maxTTL` value of -1 for collection "no expiry".

#### [](#underlying-c-sdk-core-changes-16)Underlying C++ SDK Core Changes

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

#### [](#enhancements-22)Enhancements

* [PYCBC-1499](https://issues.couchbase.com/browse/PYCBC-1499): Added improvements for Faster Failover and Config Push.
* [PYCBC-1545](https://issues.couchbase.com/browse/PYCBC-1545): Added support for new KV error code to raise `DocumentNotLockedException`.

#### [](#underlying-c-sdk-core-changes-17)Underlying C++ SDK Core Changes

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

#### [](#behavioral-change-5)Behavioral Change

The Couchbase Python SDK now publishes wheels that statically link against `BoringSSL`. The change removes the `OpenSSL` requirement from the SDK when using a published wheel. If building the SDK from source, the build will default to dynamically linking with the system provided `OpenSSL`. Build options are available if wanting to build from source and statically link against `BoringSSL`. Also, published wheels dynamically link against `stdlibs` where previously the default was to statically link against `stdlibs`. Build options are available if wanting to build from source and statically link against `stdlibs`.

#### [](#fixes-23)Fixes

* [PYCBC-1538](https://issues.couchbase.com/browse/PYCBC-1538): Fixed `get` with projections to not fail with `InvalidArgumentException` when projecting on more than 16 fields.
* [PYCBC-1534](https://issues.couchbase.com/browse/PYCBC-1534): Fixed `MutateIn` replace operation to not fail if path is empty.
* [PYCBC-1531](https://issues.couchbase.com/browse/PYCBC-1531): Fixed `CollectionQueryIndexManager` to raise `InvalidArgumentException` when `scope_name` or `collection_name` options are set.
* [PYCBC-1521](https://issues.couchbase.com/browse/PYCBC-1521): Fixed streaming APIs to use cluster timeout values from `ClusterTimeoutOptions` if provided.

#### [](#enhancements-23)Enhancements

* [PYCBC-1536](https://issues.couchbase.com/browse/PYCBC-1536): Updated MANIFEST.in to only include necessary files for source install.
* [PYCBC-1520](https://issues.couchbase.com/browse/PYCBC-1518), [PYCBC-1518](https://issues.couchbase.com/browse/PYCBC-1520): Updated published wheels to statically link against BoringSSL.
* [PYCBC-1515](https://issues.couchbase.com/browse/PYCBC-1515): Added support for bucket settings for 'no dedup' feature.
* [PYCBC-1512](https://issues.couchbase.com/browse/PYCBC-1512): Reduced default HTTP Idle Timeout.
* [PYCBC-1495](https://issues.couchbase.com/browse/PYCBC-1495): Updated wheels and build to dynamically link against stdlibs by default.

#### [](#underlying-c-sdk-core-changes-18)Underlying C++ SDK Core Changes

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

#### [](#behavioral-change-6)Behavioral Change

The Couchbase Python SDK no longer provides Python 3.7 wheels as Python 3.7 has reached [end-of-life](https://peps.python.org/pep-0537/#lifespan). See [Python Version Compatibility](https://docs.couchbase.com/python-sdk/current/project-docs/compatibility.html#python-version-compat) for details.

#### [](#fixes-24)Fixes

* [PYCBC-1514](https://issues.couchbase.com/browse/PYCBC-1514): Fixed parsing of `LookupIn` options if provided for lookup-in operations.

#### [](#enhancements-24)Enhancements

* [PYCBC-1497](https://issues.couchbase.com/browse/PYCBC-1497): Added support for Sub-Document Read from Replica.

#### [](#underlying-c-sdk-core-changes-19)Underlying C++ SDK Core Changes

* [CXXCBC-362](https://issues.couchbase.com/browse/CXXCBC-362): Removed node hostname port stripping logic from config parsing ([#438](https://github.com/couchbaselabs/couchbase-cxx-client/pull/438)).
* [CXXCBC-340](https://issues.couchbase.com/browse/CXXCBC-340): Added support for Query Read from Replica ([#435](https://github.com/couchbaselabs/couchbase-cxx-client/pull/435)).
* [CXXCBC-341](https://issues.couchbase.com/browse/CXXCBC-341), [CXXCBC-365](https://issues.couchbase.com/browse/CXXCBC-365): Added support for Sub-Document Read from Replica ([#436](https://github.com/couchbaselabs/couchbase-cxx-client/pull/436), [#441](https://github.com/couchbaselabs/couchbase-cxx-client/pull/441), [#443](https://github.com/couchbaselabs/couchbase-cxx-client/pull/443)).

### [](#version-4-1-7-8-august-2023)Version 4.1.7 (8 August 2023)

Version 4.1.7 is the next patch release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.7
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.7/>

#### [](#behavioral-change-7)Behavioral Change

Since Python 3.7 has reached [end-of-life](https://peps.python.org/pep-0537/#lifespan), the Couchbase Python SDK will no longer provide Python 3.7 wheels in future releases (>4.1.7). See [Python Version Compatibility](https://docs.couchbase.com/python-sdk/current/project-docs/compatibility.html#python-version-compat) for details.

#### [](#fixes-25)Fixes

* [PYCBC-1502](https://issues.couchbase.com/browse/PYCBC-1502): Added `PasswordAuthenticator` validation.

#### [](#enhancements-25)Enhancements

* [PYCBC-1496](https://issues.couchbase.com/browse/PYCBC-1496): Added support for Query with Read from Replica.
* [PYCBC-1419](https://issues.couchbase.com/browse/PYCBC-1419): Added support for Native KV Range Scans.
* [PYCBC-1504](https://issues.couchbase.com/browse/PYCBC-1505); [PYCBC-1505](https://issues.couchbase.com/browse/PYCBC-1505): Updated API documentation to provide correct information on `LockMode`.
* [PYCBC-1510](https://issues.couchbase.com/browse/PYCBC-1510): Updated CONTRIBUTING.md to improve contributing guidelines.
* [PYCBC-1095](https://issues.couchbase.com/browse/PYCBC-1095): Added Subdoc mutate-in deletions with a blank path.

#### [](#underlying-c-sdk-core-changes-20)Underlying C++ SDK Core Changes

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

#### [](#fixes-26)Fixes

* [PYCBC-1500](https://issues.couchbase.com/browse/PYCBC-1500): Added `max_expiry` to `CollectionSpec` for collections returned in `get_all_scopes()` result.

#### [](#enhancements-26)Enhancements

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

#### [](#behavioral-change-8)Behavioral Change

Accessing content from an Exist operation with the `` LookupInResult’s `content_as `` method now returns a boolean. This boolean is `True` if the path exists, `False` otherwise. Prior to this change the SDK raised a `DocumentNotFoundException` if the path existed or `PathNotFoundException` if the path didn't exist. The behavioral change aligns the Python SDK with Couchbase's [CRUD RFC](https://github.com/couchbaselabs/sdk-rfcs/blob/master/rfc/0053-sdk3-crud.md).

#### [](#fixes-27)Fixes

* [PYCBC-1480](https://issues.couchbase.com/browse/PYCBC-1480): Fixed subdocument read operations to allow for null values.
* [PYCBC-1486](https://issues.couchbase.com/browse/PYCBC-1486): Fixed broken imports for search `GeoBoundingBoxQuery`, `GeoDistanceQuery`, and `GeoPolygonQuery`.
* [PYCBC-1487](https://issues.couchbase.com/browse/PYCBC-1487): Updated Transcoders to be able to decode value when `flags=0`.
* [PYCBC-1490](https://issues.couchbase.com/browse/PYCBC-1490): Fixed `InternalServerFailureException` when executing a `Regex` Search query.
* [PYCBC-1493](https://issues.couchbase.com/browse/PYCBC-1493): Updated search operations to correctly pass MutationState to C++ core.

#### [](#enhancements-27)Enhancements

* [PYCBC-1488](https://issues.couchbase.com/browse/PYCBC-1488): Added `dump_configuration` to `ClusterOptions`.
* [PYCBC-1479](https://issues.couchbase.com/browse/PYCBC-1479): Bundled Mozilla certificates with the library. Source: <https://curl.se/docs/caextract.html>. Use the `disable_mozilla_ca_certificates` connection string option to disable the bundled certificates. See [Secure Connections](https://docs.couchbase.com/python-sdk/current/howtos/managing-connections.html#ssl) for more details.

#### [](#underlying-c-sdk-core-changes-21)Underlying C++ SDK Core Changes

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

#### [](#fixes-28)Fixes

* [PYCBC-1469](https://issues.couchbase.com/browse/PYCBC-1469): Added check to determine if Python interpreter is finalizing prior to logging.
* [PYCBC-1471](https://issues.couchbase.com/browse/PYCBC-1471): Fixed `acouchbase` streaming API blocking behavior while when executing queries.
* [PYCBC-1474](https://issues.couchbase.com/browse/PYCBC-1474): Fixed transaction error handling.
* [PYCBC-1475](https://issues.couchbase.com/browse/PYCBC-1475): Updated exception classes to allow first positional arg to be a string message.
* [PYCBC-1477](https://issues.couchbase.com/browse/PYCBC-1477): Fixed potential crash in certain scenarios that use `MutationState`.

#### [](#enhancements-28)Enhancements

* [PYCBC-1468](https://issues.couchbase.com/browse/PYCBC-1468): Added replica read operations to API docs.
* [PYCBC-1472](https://issues.couchbase.com/browse/PYCBC-1472): Updated API Docs to indicate expiry option should be a timedelta.
* [PYCBC-1478](https://issues.couchbase.com/browse/PYCBC-1478): Added missing bootstrap timeouts to WAN Config Profile.

#### [](#underlying-c-sdk-core-changes-22)Underlying C++ SDK Core Changes

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

#### [](#fixes-29)Fixes

* [PYCBC-1443](https://issues.couchbase.com/browse/PYCBC-1443): Fixed ssl import error.
* [PYCBC-1446](https://issues.couchbase.com/browse/PYCBC-1446): Updated API Documentation.
* [PYCBC-1455](https://issues.couchbase.com/browse/PYCBC-1455): Fixed build issue for Fedora 37 (gcc 12).

#### [](#enhancements-29)Enhancements

* [PYCBC-1431](https://issues.couchbase.com/browse/PYCBC-1431): Updated the SDK to handle new `query_context` changes.
* [PYCBC-1444](https://issues.couchbase.com/browse/PYCBC-1444): Improved CertificateAuthenticator parameter validation.
* [PYCBC-1445](https://issues.couchbase.com/browse/PYCBC-1445): Updated the SDK to only populate `allowed_sasl_mechanisms` if user explicitly chooses.

### [](#version-4-1-2-9-february-2023)Version 4.1.2 (9 February 2023)

Version `4.1.2` is the second patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the `4.1.2` release provides improved performance for key-value operations.

```bash
$ python3 -m pip install couchbase==4.1.2
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.2/>

#### [](#fixes-30)Fixes

* [PYCBC-1433](https://issues.couchbase.com/browse/PYCBC-1433): Fixed initialization of legacy durability options in C++ bindings.
* [PYCBC-1434](https://issues.couchbase.com/browse/PYCBC-1434): Added Python SDK and Python version to C++ `user_agent` option.
* [PYCBC-1441](https://issues.couchbase.com/browse/PYCBC-1441): Fixed inconsistencies when handling of `MutationState` in streaming APIs.

#### [](#enhancements-30)Enhancements

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

#### [](#fixes-31)Fixes

* [PYCBC-1428](https://issues.couchbase.com/browse/PYCBC-1428): Fixed view query `ViewOrdering` to allow user specified ordering to be applied.
* [PYCBC-1429](https://issues.couchbase.com/browse/PYCBC-1429): Fixed defaults for boolean options in N1QL query `QueryOptions`.

### [](#version-4-1-0-3-november-2022)Version 4.1.0 (3 November 2022)

Version `4.1.0` is the first minor release of the fourth generation Python SDK, bringing a number of improvements.

```bash
$ python3 -m pip install couchbase==4.1.0
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.1.0/>

#### [](#fixes-32)Fixes

* [PYCBC-1420](https://issues.couchbase.com/browse/PYCBC-1420): Fixed potential `InternalSDKException` for replica read operations.

#### [](#enhancements-31)Enhancements

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

#### [](#fixes-33)Fixes

* [PYCBC-1312](https://issues.couchbase.com/browse/PYCBC-1312); [PYCBC-1407](https://issues.couchbase.com/browse/PYCBC-1407): Fixed crash related to closing a cluster connection.
* [PYCBC-1409](https://issues.couchbase.com/browse/PYCBC-1409): Updated to version of Couchbase++ client that correctly closes HTTP connections.
* [PYCBC-1413](https://issues.couchbase.com/browse/PYCBC-1413): Fixed possible streaming API exceptions when executing in threaded environment.
* [PYCBC-1415](https://issues.couchbase.com/browse/PYCBC-1415): Updated async APIs to use correct future chaining method for read KV operations.
* [PYCBC-1416](https://issues.couchbase.com/browse/PYCBC-1416): Fixed `txcouchbase` search API.

#### [](#enhancements-32)Enhancements

* [PYCBC-1405](https://issues.couchbase.com/browse/PYCBC-1405): Updated legacy durability to use the internal Couchbase++ client API.
* [PYCBC-1406](https://issues.couchbase.com/browse/PYCBC-1406): Updated replica reads to use the internal Couchbase++ client API.
* [PYCBC-1411](https://issues.couchbase.com/browse/PYCBC-1411): Added support for LDAP authentication.

### [](#version-4-0-4-8-september-2022)Version 4.0.4 (8 September 2022)

Version `4.0.4` is the fourth patch release of the fourth generation Python SDK, bringing a number of improvements. Most notably the `4.0.4` release added legacy durability to mutation operations, tracing, and metrics.

```bash
$ python3 -m pip install couchbase==4.0.4
```

**API Docs:** <http://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.4/>

#### [](#fixes-34)Fixes

* [PYCBC-1398](https://issues.couchbase.com/browse/PYCBC-1398): Fixed potential crash when accessing `error_context` from a `base_exception` object.

#### [](#enhancements-33)Enhancements

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

#### [](#fixes-35)Fixes

* [PYCBC-1201](https://issues.couchbase.com/browse/PYCBC-1201); [PYCBC-1282](https://issues.couchbase.com/browse/PYCBC-1282); [PYCBC-1382](https://issues.couchbase.com/browse/PYCBC-1382)Fixed memory leak in key-value Result objects.
* [PYCBC-1383](https://issues.couchbase.com/browse/PYCBC-1383): Fixed memory leak in key-value Exception objects.
* [PYCBC-1386](https://issues.couchbase.com/browse/PYCBC-1386): Fixed OpenSSL discovery for MacOS M1 platforms.
* [PYCBC-1389](https://issues.couchbase.com/browse/PYCBC-1389): Removed typing-extensions dependency.
* [PYCBC-1390](https://issues.couchbase.com/browse/PYCBC-1390): Fixed Search query results to forward metrics for user access.

#### [](#enhancements-34)Enhancements

* [PYCBC-1257](https://issues.couchbase.com/browse/PYCBC-1257): Added replica reads.
* [PYCBC-1385](https://issues.couchbase.com/browse/PYCBC-1385): Updated Couchbase++ version.
* [PYCBC-1137](https://issues.couchbase.com/browse/PYCBC-1137): Deprecated the `CounterResult` CAS property.

#### [](#known-issues-4)Known Issues

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

#### [](#fixes-36)Fixes

* [PYCBC-1370](https://issues.couchbase.com/browse/PYCBC-1370): Added environment variables to direct CMake to use specified Python3 version.
* [PYCBC-1374](https://issues.couchbase.com/browse/PYCBC-1374): Added option to dynamically link `stdc++` libs.

#### [](#enhancements-35)Enhancements

* [PYCBC-628](https://issues.couchbase.com/browse/PYCBC-628); [PYCBC-1330](https://issues.couchbase.com/browse/PYCBC-1330); [PYCBC-1367](https://issues.couchbase.com/browse/PYCBC-1367): Added manylinux wheels.
* [PYCBC-1232](https://issues.couchbase.com/browse/PYCBC-1232); [PYCBC-1368](https://issues.couchbase.com/browse/PYCBC-1368): Created custom spdlog sink for pass-through logging to python logging.
* [PYCBC-1373](https://issues.couchbase.com/browse/PYCBC-1373): Provided example Linux build system Dockerfiles.
* [PYCBC-1332](https://issues.couchbase.com/browse/PYCBC-1332): Added formatting and linting to CI pipeline.

#### [](#known-issues-5)Known Issues

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

#### [](#fixes-37)Fixes

* [PYCBC-1324](https://issues.couchbase.com/browse/PYCBC-1324): Fixed N1QL Query options `scan_wait/scan_cap` misspelling.
* [PYCBC-1335](https://issues.couchbase.com/browse/PYCBC-1335): Fixed issue where positional and named parameters were not used in `TransactionQueryOptions`.
* [PYCBC-1336](https://issues.couchbase.com/browse/PYCBC-1336): Fixed crash when using `ViewOptions` keys parameter.
* [PYCBC-1342](https://issues.couchbase.com/browse/PYCBC-1342): Fixed the txcouchbase API Bucket Management API.
* [PYCBC-1343](https://issues.couchbase.com/browse/PYCBC-1343): Fixed the txcouchbase Collection Management API.

#### [](#enhancements-36)Enhancements

* [PYCBC-1328](https://issues.couchbase.com/browse/PYCBC-1328)Implemented txcouchbase test suite.
* [PYCBC-1320](https://issues.couchbase.com/browse/PYCBC-1320): Added acouchbase core API Docs.
* [PYCBC-1329](https://issues.couchbase.com/browse/PYCBC-1329): Cleaned up the acouchbase API test suite.
* [PYCBC-1331](https://issues.couchbase.com/browse/PYCBC-1331): Updated streaming API options tests to validate all parameters.
* [PYCBC-1333](https://issues.couchbase.com/browse/PYCBC-1333): Updated README, API docs for 4.0.1 release.
* [PYCBC-1334](https://issues.couchbase.com/browse/PYCBC-1334): Cleaned up couchbase API test suite.
* [PYCBC-1358](https://issues.couchbase.com/browse/PYCBC-1358): Updated Windows wheel to dynamically link against OpenSSL.

#### [](#known-issues-6)Known Issues

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

#### [](#new-features-4)New Features

* Support for distributed transactions has now been implemented.
* Reimplemented the library using the Couchbase C++ SDK.
* Improved alignment between couchbase, acouchbase and txcouchbase APIs.
* Support for Python versions 3.7 - 3.10.
* Improved API documentation.

#### [](#fixes-38)Fixes

* [PYCBC-849](https://issues.couchbase.com/browse/PYCBC-849): Implemented wait until ready.
* [PYCBC-1146](https://issues.couchbase.com/browse/PYCBC-1146): Aligned multi key-value methods with couchbase API.
* [PYCBC-1280](https://issues.couchbase.com/browse/PYCBC-1280): Fixed implementation of the `CertificateAuthenticator`.
* [PYCBC-1296](https://issues.couchbase.com/browse/PYCBC-1296): Updated `SearchRow` to not print locations when not included.

#### [](#known-issues-7)Known Issues

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