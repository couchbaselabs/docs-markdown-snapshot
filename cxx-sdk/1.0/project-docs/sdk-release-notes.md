---
title: SDK Release Notes
description: Release notes, brief installation instructions, and download
  archive for the Couchbase C&#43;&#43; Client.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-04-08T05:18:32.349Z
link: xref:1.0@cxx-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.0/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, brief installation instructions, and download archive for the Couchbase C++ Client. 

Version 1.0 of the C++ SDK implements the 3.6 [SDK API](compatibility.md#api-version). See the [compatibility pages](#compatibility.html#couchbase-feature-availability-matrix) for more information on feature compatibility with different versions of Couchbase Server.

## [](#installation)Installation

### [](#prerequisites)Prerequisites

Check that you have the dependencies installed:

* C++ 17 compiler
* [CMake](https://cmake.org/) version 3.19 or newer

Supprted Operating Systems are listed on the [compatibility page](compatibility.md#platform-compatibility).

More details of the installation process are in the [full installation guide](sdk-full-installation.md).

[CPM.cmake](https://github.com/cpm-cmake/CPM.cmake) is the recommended way to include the library in your project. You need to include the following command in your `CMakeLists.txt`.

```cmake
CPMAddPackage(
  NAME
  couchbase_cxx_client
  GIT_TAG
  1.0.7
  VERSION
  1.0.7
  GITHUB_REPOSITORY
  "couchbase/couchbase-cxx-client"
  OPTIONS
  "COUCHBASE_CXX_CLIENT_STATIC_BORINGSSL ON")
```

## [](#latest-release)C++ SDK 1.3 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-1-3-1-20-march-2026)Version 1.3.1 (20 March 2026)

This is the second GA release of the 1.3 C++ SDK.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.3.1/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.3.0...1.3.1)

#### [](#downloads)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.3.1.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.3.1.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.3.1-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.3.1-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 10  | x86\_64      | [couchbase-cxx-client-1.3.1-1.el10.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.el10.x86%5F64.tar)                 |
| Enterprise Linux 10  | aarch64      | [couchbase-cxx-client-1.3.1-1.el10.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.el10.aarch64.tar)                  |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.3.1-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.3.1-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.3.1-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.3.1-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.el8.aarch64.tar)                    |
| Debian 13 (Trixie)   | x86\_64      | [couchbase-cxx-client-1.3.1-1.trixie.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.trixie.x86%5F64.tar)             |
| Debian 13 (Trixie)   | aarch64      | [couchbase-cxx-client-1.3.1-1.trixie.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.trixie.aarch64.tar)              |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.3.1-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.3.1-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.bookworm.aarch64.tar)          |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.3.1-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.3.1-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.noble.aarch64.tar)                  |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.3.1-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.3.1-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-1.jammy.aarch64.tar)                |
| Alpine Linux 3.23    | x86\_64      | [couchbase-cxx-client-1.3.1-r1-x86\_64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-x86%5F64-alpine-3.23.tar) |
| Alpine Linux 3.23    | aarch64      | [couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.23.tar)  |
| Alpine Linux 3.22    | x86\_64      | [couchbase-cxx-client-1.3.1-r1-x86\_64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-x86%5F64-alpine-3.22.tar) |
| Alpine Linux 3.22    | aarch64      | [couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.22.tar)  |
| Alpine Linux 3.21    | x86\_64      | [couchbase-cxx-client-1.3.1-r1-x86\_64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-x86%5F64-alpine-3.21.tar) |
| Alpine Linux 3.21    | aarch64      | [couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.21.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.3.1-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.1-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes-and-enhancements)Fixes and Enhancements

* [CXXCBC-774](https://jira.issues.couchbase.com/browse/CXXCBC-774): Fixed incorrect use of `std::move` on `const Document&` — Changed `upsert()`, `insert()`, and `replace()` signatures to take `Document` by value. This correctly supports move semantics for rvalues while maintaining backward compatibility for lvalues.
* [CXXCBC-775](https://jira.issues.couchbase.com/browse/CXXCBC-775): Integrated the `system_metrics` library and added a new `cbc sysinfo` command to the `cbc` tool. This is part of the effort to make the C++ SDK self-contained for FIT testing.
* **Mozilla Certificate Parsing** — Updated the regex for parsing the header date of Mozilla certificates from curl.se to ensure correct certificate handling and added a warning if the header date is not found.

### [](#version-1-3-0-11-march-2026)Version 1.3.0 (11 March 2026)

This is the first GA release of the 1.3 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.3.0) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.2.0...1.3.0)

#### [](#downloads-2)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.3.0.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.3.0.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.3.0-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.3.0-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 10  | x86\_64      | [couchbase-cxx-client-1.3.0-1.el10.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.el10.x86%5F64.tar)                 |
| Enterprise Linux 10  | aarch64      | [couchbase-cxx-client-1.3.0-1.el10.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.el10.aarch64.tar)                  |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.3.0-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.3.0-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.3.0-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.3.0-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.el8.aarch64.tar)                    |
| Debian 13 (Trixie)   | x86\_64      | [couchbase-cxx-client-1.3.0-1.trixie.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.trixie.x86%5F64.tar)             |
| Debian 13 (Trixie)   | aarch64      | [couchbase-cxx-client-1.3.0-1.trixie.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.trixie.aarch64.tar)              |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.3.0-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.3.0-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.bookworm.aarch64.tar)          |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.3.0-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.3.0-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.noble.aarch64.tar)                  |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.3.0-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.3.0-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-1.jammy.aarch64.tar)                |
| Alpine Linux 3.23    | x86\_64      | [couchbase-cxx-client-1.3.0-r1-x86\_64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-x86%5F64-alpine-3.23.tar) |
| Alpine Linux 3.23    | aarch64      | [couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.23.tar)  |
| Alpine Linux 3.22    | x86\_64      | [couchbase-cxx-client-1.3.0-r1-x86\_64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-x86%5F64-alpine-3.22.tar) |
| Alpine Linux 3.22    | aarch64      | [couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.22.tar)  |
| Alpine Linux 3.21    | x86\_64      | [couchbase-cxx-client-1.3.0-r1-x86\_64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-x86%5F64-alpine-3.21.tar) |
| Alpine Linux 3.21    | aarch64      | [couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.21.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.3.0-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.3.0-r1-aarch64-alpine-3.20.tar)  |

#### [](#new-features)New Features

* [CXXCBC-691](https://jira.issues.couchbase.com/browse/CXXCBC-691): **OpenTelemetry Support** — Added initial `OpenTelemetry` support with tracing and metrics export via OTLP HTTP. The SDK now exposes spans and metrics following OpenTelemetry conventions. The feature can be enabled with `-DCOUCHBASE_CXX_CLIENT_BUILD_OPENTELEMETRY=ON` at build time.
* [CXXCBC-740](https://jira.issues.couchbase.com/browse/CXXCBC-740): **JWT Authentication** — Added JWT-based authentication support via `jwt_authenticator`. The authenticator can refresh tokens automatically and supports reauthentication when tokens become stale.
* [CXXCBC-745](https://jira.issues.couchbase.com/browse/CXXCBC-745): **Lazy Connections Mode** — Added new `enable_lazy_connections` option that delays opening KV connections until the first operation is executed, reducing initial connection overhead.
* [CXXCBC-739](https://jira.issues.couchbase.com/browse/CXXCBC-739): **mTLS Certificate Refresh** — Added support for refreshing TLS certificates without restarting the application. Certificates can now be updated via `cluster::update_credentials()`, and new TLS sessions will use the updated certificates.
* [CXXCBC-751](https://jira.issues.couchbase.com/browse/CXXCBC-751): **cbc-get Replica Support** — Added `--replica` flag to `cbc-get` tool to fetch documents from replica nodes.
* [CXXCBC-754](https://jira.issues.couchbase.com/browse/CXXCBC-754): **cbc-config Tool** — Added new `cbc-config` tool to dump cluster configuration to `stdout` for debugging.

#### [](#improvements)Improvements

* [CXXCBC-719](https://jira.issues.couchbase.com/browse/CXXCBC-719): **Enhanced Tracing** — Added top-level spans in the Public API for all KV and HTTP operations, providing better observability into operation lifecycle.
* [CXXCBC-750](https://jira.issues.couchbase.com/browse/CXXCBC-750): **Internal Tracer for Wrapper SDKs** — Added internal tracer interface (`tracer_wrapper::wrapped()`) for use by wrapper SDKs that want to integrate with the SDK's tracing.
* [CXXCBC-742](https://jira.issues.couchbase.com/browse/CXXCBC-742): **cbc-query Improvements** — Enhanced error reporting with JSON-encoded error context for query failures.
* [CXXCBC-771](https://jira.issues.couchbase.com/browse/CXXCBC-771): **Credentials Update Restrictions** — `cluster::update_credentials()` now prevents switching between authenticator types (e.g., password to certificate) to avoid unexpected behavior.
* [CXXCBC-768](https://jira.issues.couchbase.com/browse/CXXCBC-768): **DNS-SRV Refresh Fix** — Fixed an issue where `bucket_not_found` errors during bootstrap would trigger unnecessary DNS-SRV record refresh loops.
* [CXXCBC-767](https://jira.issues.couchbase.com/browse/CXXCBC-767): Implemented `AuthStale` handling and JWT reauthentication support.

#### [](#bug-fixes)Bug Fixes

* [CXXCBC-769](https://jira.issues.couchbase.com/browse/CXXCBC-769), [CXXCBC-770](https://jira.issues.couchbase.com/browse/CXXCBC-770), [CXXCBC-756](https://jira.issues.couchbase.com/browse/CXXCBC-756), [CXXCBC-761](https://jira.issues.couchbase.com/browse/CXXCBC-761), [CXXCBC-755](https://jira.issues.couchbase.com/browse/CXXCBC-755): Various OpenTelemetry integration fixes and improvements.
* [CXXCBC-763](https://jira.issues.couchbase.com/browse/CXXCBC-763): Fixed `set_authenticator` not applying updated cert/key pairs to new TLS sessions.
* Fixed build issues on macOS 14 with gcc-15 (missing `std::quick_exit`).
* [CXXCBC-732](https://jira.issues.couchbase.com/browse/CXXCBC-732): Fixed memory leaks in concurrent fixed queue reporting.
* [CXXCBC-743](https://jira.issues.couchbase.com/browse/CXXCBC-743): Fixed HTTP command handler signature to properly handle decoded response types.
* [CXXCBC-766](https://jira.issues.couchbase.com/browse/CXXCBC-766): Fixed OpenSSL headers priority in BoringSSL builds.

#### [](#deprecations)Deprecations

* [CXXCBC-752](https://jira.issues.couchbase.com/browse/CXXCBC-752): MapReduce Views are now deprecated. Use Query with SQL++ instead.
* [CXXCBC-740](https://jira.issues.couchbase.com/browse/CXXCBC-740): `jwt_authenticator` is marked as `@uncommitted` and may change in future releases.

## [](#c-sdk-1-2-releases)C++ SDK 1.2 Releases

### [](#version-1-2-2-19-february-2026)Version 1.2.2 (19 February 2026)

This is a second patch release of the 1.2 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.2.2) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.2.1...1.2.2)

#### [](#downloads-3)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.2.2.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.2.2.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.2.2-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.2.2-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 10  | x86\_64      | [couchbase-cxx-client-1.2.2-1.el10.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.el10.x86%5F64.tar)                 |
| Enterprise Linux 10  | aarch64      | [couchbase-cxx-client-1.2.2-1.el10.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.el10.aarch64.tar)                  |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.2.2-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.2.2-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.2.2-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.2.2-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.el8.aarch64.tar)                    |
| Debian 13 (Trixie)   | x86\_64      | [couchbase-cxx-client-1.2.2-1.trixie.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.trixie.x86%5F64.tar)             |
| Debian 13 (Trixie)   | aarch64      | [couchbase-cxx-client-1.2.2-1.trixie.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.trixie.aarch64.tar)              |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.2.2-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.2.2-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.bookworm.aarch64.tar)          |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.2.2-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.2.2-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.noble.aarch64.tar)                  |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.2.2-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.2.2-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-1.jammy.aarch64.tar)                |
| Alpine Linux 3.23    | x86\_64      | [couchbase-cxx-client-1.2.2-r1-x86\_64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-x86%5F64-alpine-3.23.tar) |
| Alpine Linux 3.23    | aarch64      | [couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.23.tar)  |
| Alpine Linux 3.22    | x86\_64      | [couchbase-cxx-client-1.2.2-r1-x86\_64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-x86%5F64-alpine-3.22.tar) |
| Alpine Linux 3.22    | aarch64      | [couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.22.tar)  |
| Alpine Linux 3.21    | x86\_64      | [couchbase-cxx-client-1.2.2-r1-x86\_64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-x86%5F64-alpine-3.21.tar) |
| Alpine Linux 3.21    | aarch64      | [couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.21.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.2.2-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.2-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes-and-enhancements-2)Fixes and Enhancements

* [CXXCBC-768](https://jira.issues.couchbase.com/browse/CXXCBC-768): Prevent DNS-SRV refresh loop on `bucket_not_found` bootstrap errors ([#897](https://github.com/couchbase/couchbase-cxx-client/pull/897)).

### [](#version-1-2-1-23-january-2026)Version 1.2.1 (23 January 2026)

This is a first patch release of the 1.2 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.2.1) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.2.0...1.2.1)

#### [](#downloads-4)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.2.1.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.2.1.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.2.1-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.2.1-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 10  | x86\_64      | [couchbase-cxx-client-1.2.1-1.el10.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.el10.x86%5F64.tar)                 |
| Enterprise Linux 10  | aarch64      | [couchbase-cxx-client-1.2.1-1.el10.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.el10.aarch64.tar)                  |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.2.1-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.2.1-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.2.1-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.2.1-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.el8.aarch64.tar)                    |
| Debian 13 (Trixie)   | x86\_64      | [couchbase-cxx-client-1.2.1-1.trixie.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.trixie.x86%5F64.tar)             |
| Debian 13 (Trixie)   | aarch64      | [couchbase-cxx-client-1.2.1-1.trixie.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.trixie.aarch64.tar)              |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.2.1-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.2.1-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.bookworm.aarch64.tar)          |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.2.1-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.2.1-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.noble.aarch64.tar)                  |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.2.1-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.2.1-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-1.jammy.aarch64.tar)                |
| Alpine Linux 3.23    | x86\_64      | [couchbase-cxx-client-1.2.1-r1-x86\_64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-x86%5F64-alpine-3.23.tar) |
| Alpine Linux 3.23    | aarch64      | [couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.23.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.23.tar)  |
| Alpine Linux 3.22    | x86\_64      | [couchbase-cxx-client-1.2.1-r1-x86\_64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-x86%5F64-alpine-3.22.tar) |
| Alpine Linux 3.22    | aarch64      | [couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.22.tar)  |
| Alpine Linux 3.21    | x86\_64      | [couchbase-cxx-client-1.2.1-r1-x86\_64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-x86%5F64-alpine-3.21.tar) |
| Alpine Linux 3.21    | aarch64      | [couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.21.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.2.1-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.1-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes-and-enhancements-3)Fixes and Enhancements

* [CXXCBC-766](https://jira.issues.couchbase.com/browse/CXXCBC-766): Make sure BoringSSL headers take priority over system distribution ([#889](https://github.com/couchbase/couchbase-cxx-client/pull/889)).

### [](#version-1-2-0-26-september-2025)Version 1.2.0 (26 September 2025)

This is a first GA release of the 1.2 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.2.0) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.1.0...1.2.0)

#### [](#downloads-5)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.2.0.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.2.0.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.2.0-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.2.0-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 10  | x86\_64      | [couchbase-cxx-client-1.2.0-1.el10.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.el10.x86%5F64.tar)                 |
| Enterprise Linux 10  | aarch64      | [couchbase-cxx-client-1.2.0-1.el10.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.el10.aarch64.tar)                  |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.2.0-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.2.0-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.2.0-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.2.0-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.el8.aarch64.tar)                    |
| Debian 13 (Trixie)   | x86\_64      | [couchbase-cxx-client-1.2.0-1.trixie.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.trixie.x86%5F64.tar)             |
| Debian 13 (Trixie)   | aarch64      | [couchbase-cxx-client-1.2.0-1.trixie.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.trixie.aarch64.tar)              |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.2.0-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.2.0-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.bookworm.aarch64.tar)          |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.2.0-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.2.0-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.noble.aarch64.tar)                  |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.2.0-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.2.0-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-1.jammy.aarch64.tar)                |
| Alpine Linux 3.22    | x86\_64      | [couchbase-cxx-client-1.2.0-r1-x86\_64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-x86%5F64-alpine-3.22.tar) |
| Alpine Linux 3.22    | aarch64      | [couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.22.tar)  |
| Alpine Linux 3.21    | x86\_64      | [couchbase-cxx-client-1.2.0-r1-x86\_64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-x86%5F64-alpine-3.21.tar) |
| Alpine Linux 3.21    | aarch64      | [couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.21.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.2.0-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.20.tar)  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.2.0-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.2.0-r1-aarch64-alpine-3.19.tar)  |

#### [](#new-features-2)New Features

* [CXXCBC-567](https://jira.issues.couchbase.com/browse/CXXCBC-567): Added support for field-level encryption library ([#791](https://github.com/couchbase/couchbase-cxx-client/pull/791)).
* [CXXCBC-713](https://jira.issues.couchbase.com/browse/CXXCBC-713), [CXXCBC-729](https://jira.issues.couchbase.com/browse/CXXCBC-729): Added `cbc-keygen`, a tool to generate keys for specific vBucket ([#799](https://github.com/couchbase/couchbase-cxx-client/pull/799), [#833](https://github.com/couchbase/couchbase-cxx-client/pull/833)).
* [CXXCBC-656](https://jira.issues.couchbase.com/browse/CXXCBC-656): Added `cbc-remove` and `cbc-upsert` tools ([#781](https://github.com/couchbase/couchbase-cxx-client/pull/781)).
* [CXXCBC-653](https://jira.issues.couchbase.com/browse/CXXCBC-653): Added support "access\_deleted" for Replica Reads ([#821](https://github.com/couchbase/couchbase-cxx-client/pull/821)).
* [CXXCBC-639](https://jira.issues.couchbase.com/browse/CXXCBC-639): Added support of building both static and shared libraries ([#707](https://github.com/couchbase/couchbase-cxx-client/pull/707)).
* [CXXCBC-698](https://jira.issues.couchbase.com/browse/CXXCBC-698): Added `flex_index` to `transaction_query_options` ([#773](https://github.com/couchbase/couchbase-cxx-client/pull/773)).
* [CXXCBC-675](https://jira.issues.couchbase.com/browse/CXXCBC-675): Added support vector search prefilter ([#775](https://github.com/couchbase/couchbase-cxx-client/pull/775)).
* [CXXCBC-699](https://jira.issues.couchbase.com/browse/CXXCBC-699): Added support of randomization of bootstrap nodes ([#777](https://github.com/couchbase/couchbase-cxx-client/pull/777)). By default the SDK would shuffle node list (including list received via DNS-SRV request). To disable this behavior use `preserve_bootstrap_nodes_order` option.
* [CXXCBC-711](https://jira.issues.couchbase.com/browse/CXXCBC-711): Promoted `scope_search_index_manager` to committed API ([#793](https://github.com/couchbase/couchbase-cxx-client/pull/793)).
* [CXXCBC-692](https://jira.issues.couchbase.com/browse/CXXCBC-692): The SDK now prevents connection to Enterprise Analytics cluster ([#792](https://github.com/couchbase/couchbase-cxx-client/pull/792), [#807](https://github.com/couchbase/couchbase-cxx-client/pull/807), [#810](https://github.com/couchbase/couchbase-cxx-client/pull/810)). There is a set of specialized SDKs for Enterprise Analytics clusters.
* [CXXCBC-707](https://jira.issues.couchbase.com/browse/CXXCBC-707): Updated network selection heuristic ([#809](https://github.com/couchbase/couchbase-cxx-client/pull/809)). The logic is improved in certain cloud-specific cases.

#### [](#fixes-and-enhancements-4)Fixes and Enhancements

* [CXXCBC-715](https://jira.issues.couchbase.com/browse/CXXCBC-715): Fixed Hard Failover Intermittent Crash in HTTP connection manager ([#818](https://github.com/couchbase/couchbase-cxx-client/pull/818)).
* [CXXCBC-693](https://jira.issues.couchbase.com/browse/CXXCBC-693): Handle empty/null `` indexDef`s for `search_index_get_all `` ([#800](https://github.com/couchbase/couchbase-cxx-client/pull/800)).
* [CXXCBC-726](https://jira.issues.couchbase.com/browse/CXXCBC-726): Added KV scan timeout to cluster options ([#830](https://github.com/couchbase/couchbase-cxx-client/pull/830)).
* [CXXCBC-721](https://jira.issues.couchbase.com/browse/CXXCBC-721): Added caching of `FeatureNotAvailable` transactions operation failure for `get_replica*` operations ([#823](https://github.com/couchbase/couchbase-cxx-client/pull/823)).
* [CXXCBC-696](https://jira.issues.couchbase.com/browse/CXXCBC-696): Use the external exception field to determine transaction operation error code in Public API ([#770](https://github.com/couchbase/couchbase-cxx-client/pull/770)).
* [CXXCBC-695](https://jira.issues.couchbase.com/browse/CXXCBC-695): Always return unwrapped `doc_exists` from transactions insert ([#771](https://github.com/couchbase/couchbase-cxx-client/pull/771)).
* [CXXCBC-700](https://jira.issues.couchbase.com/browse/CXXCBC-700): Updated `wan_development` profile for public API ([#774](https://github.com/couchbase/couchbase-cxx-client/pull/774)).
* [CXXCBC-704](https://jira.issues.couchbase.com/browse/CXXCBC-704): Added handling `document_unretrievable` from `get_multi` individual fetch ([#782](https://github.com/couchbase/couchbase-cxx-client/pull/782), [#785](https://github.com/couchbase/couchbase-cxx-client/pull/785)).
* [CXXCBC-709](https://jira.issues.couchbase.com/browse/CXXCBC-709): Fixed `exists()` in transactions `get_multi` result ([#786](https://github.com/couchbase/couchbase-cxx-client/pull/786)).
* [CXXCBC-651](https://jira.issues.couchbase.com/browse/CXXCBC-651): Added preserving cached node labels after generating report in app telemetry meter ([#802](https://github.com/couchbase/couchbase-cxx-client/pull/802)).
* [CXXCBC-706](https://jira.issues.couchbase.com/browse/CXXCBC-706): Added closing of half-baked cluster object if connection fails ([#783](https://github.com/couchbase/couchbase-cxx-client/pull/783)).

#### [](#build-and-test-infrastructure)Build and Test Infrastructure

* [CXXCBC-733](https://jira.issues.couchbase.com/browse/CXXCBC-733): Fixed build with BoringSSL ([#839](https://github.com/couchbase/couchbase-cxx-client/pull/839)).
* Improved stability of update collection max expiry tests ([#838](https://github.com/couchbase/couchbase-cxx-client/pull/838)).
* [CXXCBC-731](https://jira.issues.couchbase.com/browse/CXXCBC-731): Fixed usage of the `wan_development` profile in tests when required ([#835](https://github.com/couchbase/couchbase-cxx-client/pull/835)).
* [CXXCBC-728](https://jira.issues.couchbase.com/browse/CXXCBC-728): Removed handling for eventing handler headers bug ([#832](https://github.com/couchbase/couchbase-cxx-client/pull/832)).
* [CXXCBC-724](https://jira.issues.couchbase.com/browse/CXXCBC-724): Added eventing tests to handle Morpheus error behavior ([#828](https://github.com/couchbase/couchbase-cxx-client/pull/828), [#824](https://github.com/couchbase/couchbase-cxx-client/pull/824)).
* [CXXCBC-639](https://jira.issues.couchbase.com/browse/CXXCBC-639): Build system adjustments ([#825](https://github.com/couchbase/couchbase-cxx-client/pull/825)).
* Added labels to all tests ([#820](https://github.com/couchbase/couchbase-cxx-client/pull/820)).
* Added test improvements (memcached buckets & cleanup search index) ([#819](https://github.com/couchbase/couchbase-cxx-client/pull/819)).
* Added logging of local TCP ports ([#814](https://github.com/couchbase/couchbase-cxx-client/pull/814)).
* Updated llhttp to 9.3.0 and cli11 to 2.5.0 ([#811](https://github.com/couchbase/couchbase-cxx-client/pull/811)).
* Updated asio to 1.34.2 ([#776](https://github.com/couchbase/couchbase-cxx-client/pull/776)).
* Updated CPM.cmake to 0.42.0 ([#794](https://github.com/couchbase/couchbase-cxx-client/pull/794)).
* [CXXCBC-712](https://jira.issues.couchbase.com/browse/CXXCBC-712): Fixed build with CPM ([#795](https://github.com/couchbase/couchbase-cxx-client/pull/795)).
* Fixed building tests with system OpenSSL on MacOS ([#798](https://github.com/couchbase/couchbase-cxx-client/pull/798)).
* [CXXCBC-693](https://jira.issues.couchbase.com/browse/CXXCBC-693): Fixed clang-tidy `else-after-return` error ([#803](https://github.com/couchbase/couchbase-cxx-client/pull/803)).
* Fixed gcc `maybe-uninitialized` warning with `std::nullopt` ([#816](https://github.com/couchbase/couchbase-cxx-client/pull/816)).
* Github Actions:

  * Updated trigger rules ([#779](https://github.com/couchbase/couchbase-cxx-client/pull/779)), including release branches;
  * Removed windows-2019 runner & added windows-2025 ([#790](https://github.com/couchbase/couchbase-cxx-client/pull/790));
  * Updated linters workflow ([#808](https://github.com/couchbase/couchbase-cxx-client/pull/808)).

## [](#c-sdk-1-1-releases)C++ SDK 1.1 Releases

### [](#version-1-1-1-18-september-2025)Version 1.1.1 (18 September 2025)

This is a second GA release of the 1.1 C++ SDK. It contains features and fixes backported from 1.2.0.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.1.1) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.1.0...1.1.1)

#### [](#downloads-6)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.1.1.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.1.1.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.1.1-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.1.1-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.1.1-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.1.1-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.1.1-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.1.1-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.el8.aarch64.tar)                    |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.1.1-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.1.1-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.bookworm.aarch64.tar)          |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.1.1-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.1.1-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.jammy.aarch64.tar)                |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.1.1-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.1.1-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-1.noble.aarch64.tar)                  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.1.1-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.19.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.1.1-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.20.tar)  |
| Alpine Linux 3.21    | x86\_64      | [couchbase-cxx-client-1.1.1-r1-x86\_64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-x86%5F64-alpine-3.21.tar) |
| Alpine Linux 3.21    | aarch64      | [couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.21.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.21.tar)  |
| Alpine Linux 3.22    | x86\_64      | [couchbase-cxx-client-1.1.1-r1-x86\_64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-x86%5F64-alpine-3.22.tar) |
| Alpine Linux 3.22    | aarch64      | [couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.22.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.1-r1-aarch64-alpine-3.22.tar)  |

#### [](#new-features-3)New Features

* [CXXCBC-699](https://jira.issues.couchbase.com/browse/CXXCBC-699): By default the SDK will now shuffle the node list (including lists received via DNS-SRV request). To disable this behavior use the `preserve_bootstrap_nodes_order` option ([#778](https://github.com/couchbase/couchbase-cxx-client/pull/778)).

#### [](#fixes-and-enhancements-5)Fixes and Enhancements

* [CXXCBC-715](https://jira.issues.couchbase.com/browse/CXXCBC-715): An HTTP workload could potentially use an invalid node index to access a node in the config in scenarios to where a node in the cluster has been failed over. This potential intermittent crash during hard failover has now been fixed ([#817](https://github.com/couchbase/couchbase-cxx-client/pull/817)).
* [CXXCBC-651](https://jira.issues.couchbase.com/browse/CXXCBC-651): Cached node labels are now preserved after generating reports in app telemetry meter ([#804](https://github.com/couchbase/couchbase-cxx-client/pull/804)).
* [CXXCBC-693](https://jira.issues.couchbase.com/browse/CXXCBC-693): Fixed clang-tidy else-after-return error ([#805](https://github.com/couchbase/couchbase-cxx-client/pull/805)). Now correctly handle empty/null `indexDefs` for `search_index_get_all` ([801](https://github.com/couchbase/couchbase-cxx-client/pull/801)). The client will no longer return an error if/when `indexDefs` are empty/null — instead returning an empty list of index definitions.
* [CXXCBC-709](https://jira.issues.couchbase.com/browse/CXXCBC-709): Fixed a bug in the getter that was always returning `false` for `exists()` in transactions `get_multi` result ([#787](https://github.com/couchbase/couchbase-cxx-client/pull/787)).
* [CXXCBC-696](https://jira.issues.couchbase.com/browse/CXXCBC-696): The client now uses the external exception field to determine transaction operation error code in the Public API ([#772](https://github.com/couchbase/couchbase-cxx-client/pull/772)).
* [CXXCBC-712](https://jira.issues.couchbase.com/browse/CXXCBC-712): Fixed build issue with CPM ([#797](https://github.com/couchbase/couchbase-cxx-client/pull/797))

### [](#version-1-1-0-01-june-2025)Version 1.1.0 (01 June 2025)

This is a first GA release of the 1.1 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.1.0) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.5...1.1.0)

#### [](#downloads-7)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.1.0.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.1.0.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.1.0-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.1.0-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.1.0-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.1.0-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.1.0-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.1.0-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.el8.aarch64.tar)                    |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.1.0-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.1.0-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.bookworm.aarch64.tar)          |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.1.0-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.1.0-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.jammy.aarch64.tar)                |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.1.0-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.1.0-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-1.noble.aarch64.tar)                  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.1.0-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.1.0-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-r1-aarch64-alpine-3.19.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.1.0-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.1.0-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.1.0-r1-aarch64-alpine-3.20.tar)  |

#### [](#new-features-4)New Features

* [CXXCBC-672](https://jira.issues.couchbase.com/browse/CXXCBC-672): Added `add_named_parameter` and `add_positional_parameter` to query/analytics options ([#762](https://github.com/couchbase/couchbase-cxx-client/pull/762)).
* [CXXCBC-684](https://jira.issues.couchbase.com/browse/CXXCBC-684): The SDK now allows the setting of both named and positional parameters for queries — previously named parameters would be cleared if positional parameters were set ([#759](https://github.com/couchbase/couchbase-cxx-client/pull/759)).
* [CXXCBC-654](https://jira.issues.couchbase.com/browse/CXXCBC-654): Added `num_vbuckets` to `bucket_settings` ([#746](https://github.com/couchbase/couchbase-cxx-client/pull/746)).
* [CXXCBC-605](https://jira.issues.couchbase.com/browse/CXXCBC-605): Added custom log callback functionality ([#743](https://github.com/couchbase/couchbase-cxx-client/pull/743)).
* [CXXCBC-665](https://jira.issues.couchbase.com/browse/CXXCBC-665): The SDK will now always return partial results for `*_all_replica` operations if some `get_replica` requests succeeded ([#742](https://github.com/couchbase/couchbase-cxx-client/pull/742)).
* [CXXCBC-626](https://jira.issues.couchbase.com/browse/CXXCBC-626): Application Service Telemetry, for future Server releases ([#712](https://github.com/couchbase/couchbase-cxx-client/pull/712), [#719](https://github.com/couchbase/couchbase-cxx-client/pull/719), [#739](https://github.com/couchbase/couchbase-cxx-client/pull/739), [#750](https://github.com/couchbase/couchbase-cxx-client/pull/750)).

#### [](#fixes-and-enhancements-6)Fixes and Enhancements

* [CXXCBC-694](https://jira.issues.couchbase.com/browse/CXXCBC-694): Handle case where requestID is missing from query response payload ([#768](https://github.com/couchbase/couchbase-cxx-client/pull/768)).
* Added CAS to core append/prepend ([#737](https://github.com/couchbase/couchbase-cxx-client/pull/737)).
* [CXXCBC-657](https://jira.issues.couchbase.com/browse/CXXCBC-657): For subdoc operations, if no specs are provided then an `invalid_argument` error is raised instead of crashing on an assert ([#727](https://github.com/couchbase/couchbase-cxx-client/pull/727)).
* [CXXCBC-661](https://jira.issues.couchbase.com/browse/CXXCBC-661): Reconnect cluster object on fork ([#724](https://github.com/couchbase/couchbase-cxx-client/pull/724)).
* [CXXCBC-660](https://jira.issues.couchbase.com/browse/CXXCBC-660): Fixed potential race condition in the logger ([#722](https://github.com/couchbase/couchbase-cxx-client/pull/722)).
* [CXXCBC-646](https://jira.issues.couchbase.com/browse/CXXCBC-646): For performance reasons, the bucket configuration is now stored as shared pointer, and this is copied into the handler instead of the entire configuration ([#715](https://github.com/couchbase/couchbase-cxx-client/pull/715), [#720](https://github.com/couchbase/couchbase-cxx-client/pull/720)).

#### [](#transactions)Transactions

* [CXXCBC-688](https://jira.issues.couchbase.com/browse/CXXCBC-688): Don't convert Public API TOF from lambda to Core API's TOF, rely on internal state ([#765](https://github.com/couchbase/couchbase-cxx-client/pull/765)).
* [CXXCBC-690](https://jira.issues.couchbase.com/browse/CXXCBC-690): Don't move `staged_mutation` item when capturing it in `commit_doc` lambdas ([#767](https://github.com/couchbase/couchbase-cxx-client/pull/767)).
* [CXXCBC-683](https://jira.issues.couchbase.com/browse/CXXCBC-683): Transactions replace now uses CAS from given `TransactionsGetResult` when the document is a staged insert ([#763](https://github.com/couchbase/couchbase-cxx-client/pull/763)).
* [CXXCBC-682](https://jira.issues.couchbase.com/browse/CXXCBC-682): Transaction replace/insert result now includes post-op content ([#756](https://github.com/couchbase/couchbase-cxx-client/pull/756)).
* [CXXCBC-645](https://jira.issues.couchbase.com/browse/CXXCBC-645), [CXXCBC-689](https://jira.issues.couchbase.com/browse/CXXCBC-689), [CXXCBC-687](https://jira.issues.couchbase.com/browse/CXXCBC-687): Implemented `get_multi_*` APIs for transactions ([#761](https://github.com/couchbase/couchbase-cxx-client/pull/761), [#764](https://github.com/couchbase/couchbase-cxx-client/pull/764), [#766](https://github.com/couchbase/couchbase-cxx-client/pull/766)).
* [CXXCBC-681](https://jira.issues.couchbase.com/browse/CXXCBC-681): No longer storing entire `transaction_get_result` in staged mutations, reducing memory use ([#757](https://github.com/couchbase/couchbase-cxx-client/pull/757)).
* [CXXCBC-649](https://jira.issues.couchbase.com/browse/CXXCBC-649): Implemented `ExtReplaceBodyWithXattr` ([#752](https://github.com/couchbase/couchbase-cxx-client/pull/752)).

#### [](#build-and-tests-fixes)Build and Tests Fixes

* [CXXCBC-671](https://jira.issues.couchbase.com/browse/CXXCBC-671): Updated `snappy` to support `CMake` `4.0`([#744](https://github.com/couchbase/couchbase-cxx-client/pull/744)).
* [CXXCBC-666](https://jira.issues.couchbase.com/browse/CXXCBC-666): Fixed `pkg-config` file — `couchbase_cxx_client.pc` have to use absolute path for `libdir`. ([#735](https://github.com/couchbase/couchbase-cxx-client/pull/735)).
* [CXXCBC-673](https://jira.issues.couchbase.com/browse/CXXCBC-673): Updated query integration tests to compare decoded rows ([#747](https://github.com/couchbase/couchbase-cxx-client/pull/747)).

## [](#c-sdk-1-0-releases)C++ SDK 1.0 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-1-0-7-24-april-2025)Version 1.0.7 (24 April 2025)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.7) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.5...1.0.7)

#### [](#downloads-8)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.0.7.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.0.7.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.0.7-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.0.7-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.0.7-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.0.7-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.0.7-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.0.7-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.el8.aarch64.tar)                    |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.0.7-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.0.7-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.bookworm.aarch64.tar)          |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.7-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.7-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.jammy.aarch64.tar)                |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.7-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.7-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.noble.aarch64.tar)                  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.0.7-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.0.7-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-r1-aarch64-alpine-3.19.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.0.7-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.0.7-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes)Fixes

* [CXXCBC-666](https://jira.issues.couchbase.com/browse/CXXCBC-666): Fixed `pkg-config` file to return absolute path for libdir ([#736](https://github.com/couchbase/couchbase-cxx-client/736)).
* [CXXCBC-667](https://jira.issues.couchbase.com/browse/CXXCBC-667): Core implementation of prepend/append no longer ignores encoded CAS value ([#738](https://github.com/couchbase/couchbase-cxx-client/738)).
* [CXXCBC-671](https://jira.issues.couchbase.com/browse/CXXCBC-671): Updated snappy to support `CMake` `4.0` ([#745](https://github.com/couchbase/couchbase-cxx-client/745)).

### [](#version-1-0-6-12-march-2025)Version 1.0.6 (12 March 2025)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.6) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.5...1.0.6)

#### [](#downloads-9)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.0.6.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.0.6.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.0.6-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.0.6-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.0.6-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.0.6-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.0.6-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.0.6-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.el8.aarch64.tar)                    |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.0.6-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.0.6-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.bookworm.aarch64.tar)          |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.6-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.6-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.jammy.aarch64.tar)                |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.6-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.6-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.noble.aarch64.tar)                  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.0.6-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.0.6-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-r1-aarch64-alpine-3.19.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.0.6-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.0.6-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes-2)Fixes

* [CXXCBC-633](https://jira.issues.couchbase.com/browse/CXXCBC-633): In a case of timeout, when the total deadline of the DNS-SRV request has been reached, the library will now report a timeout error code, and not the latest abort as it was doing.
* [CXXCBC-646](https://jira.issues.couchbase.com/browse/CXXCBC-646): For performance reasons, the SDK now stores bucket configuration as a shared pointer ([#713](https://github.com/couchbase/couchbase-cxx-client/pull/713), [#721](https://github.com/couchbase/couchbase-cxx-client/pull/721)).
* [CXXCBC-660](https://jira.issues.couchbase.com/browse/CXXCBC-660): Fixed potential race condition in the logger ([#723](https://github.com/couchbase/couchbase-cxx-client/pull/723)).
* [CXXCBC-661](https://jira.issues.couchbase.com/browse/CXXCBC-661): The child process now reconnects all of its instances on fork — previously, certain exceptions could cause this not to happen ([#725](https://github.com/couchbase/couchbase-cxx-client/pull/725)).

### [](#version-1-0-5-24-january-2025)Version 1.0.5 (24 January 2025)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.5) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.4...1.0.5)

#### [](#downloads-10)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.0.5.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.0.5.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.0.5-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.0.5-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.0.5-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.0.5-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.0.5-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.0.5-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.el8.aarch64.tar)                    |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.0.5-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.0.5-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.bookworm.aarch64.tar)          |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.5-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.5-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.jammy.aarch64.tar)                |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.5-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.5-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.noble.aarch64.tar)                  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.0.5-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.19.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.0.5-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes-3)Fixes

* [CXXCBC-633](https://jira.issues.couchbase.com/browse/CXXCBC-633): In a case of timeout, when the total deadline of the DNS-SRV request has been reached, the library will now report a timeout error code, and not the latest abort as it was doing.
* Server group replica reads are now exposed in `transaction_context` ([#704](https://github.com/couchbase/couchbase-cxx-client/pull/704)).

#### [](#build-and-test-infrastructure-2)Build and Test Infrastructure

* Minor improvements ([#706](https://github.com/couchbase/couchbase-cxx-client/pull/706)).
* [CXXCBC-640](https://jira.issues.couchbase.com/browse/CXXCBC-640): Debug symbols are no longer forced for release builds ([#708](https://github.com/couchbase/couchbase-cxx-client/pull/708)).
* [CXXCBC-638](https://jira.issues.couchbase.com/browse/CXXCBC-638): Switched SDK to use bundled `fmtlib` for `spdlog` ([#705](https://github.com/couchbase/couchbase-cxx-client/pull/705)).
* Updated `spdlog` to `1.15.0` ([#709](https://github.com/couchbase/couchbase-cxx-client/pull/709)).

### [](#version-1-0-4-22-november-2024)Version 1.0.4 (22 November 2024)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.4) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.3...1.0.4)

#### [](#downloads-11)Downloads

| Platform             | Architecture | File                                                                                                                                                       |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | Any          | [couchbase-cxx-client-1.0.4.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4.sha256.txt)                                  |
| Source Archive       | Any          | [couchbase-cxx-client-1.0.4.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4.tar.gz)                                          |
| Amazon Linux 2023    | x86\_64      | [couchbase-cxx-client-1.0.4-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.amzn2023.x86%5F64.tar)         |
| Amazon Linux 2023    | aarch64      | [couchbase-cxx-client-1.0.4-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.amzn2023.aarch64.tar)          |
| Enterprise Linux 9   | x86\_64      | [couchbase-cxx-client-1.0.4-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.el9.x86%5F64.tar)                   |
| Enterprise Linux 9   | aarch64      | [couchbase-cxx-client-1.0.4-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.el9.aarch64.tar)                    |
| Enterprise Linux 8   | x86\_64      | [couchbase-cxx-client-1.0.4-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.el8.x86%5F64.tar)                   |
| Enterprise Linux 8   | aarch64      | [couchbase-cxx-client-1.0.4-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.el8.aarch64.tar)                    |
| Debian 12 (Bookworm) | x86\_64      | [couchbase-cxx-client-1.0.4-1.bookworm.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.bookworm.x86%5F64.tar)         |
| Debian 12 (Bookworm) | aarch64      | [couchbase-cxx-client-1.0.4-1.bookworm.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.bookworm.aarch64.tar)          |
| Ubuntu 22.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.4-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.jammy.x86%5F64.tar)               |
| Ubuntu 22.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.4-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.jammy.aarch64.tar)                |
| Ubuntu 24.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.4-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.noble.x86%5F64.tar)                 |
| Ubuntu 24.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.4-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.noble.aarch64.tar)                  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.0.4-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.0.4-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-r1-aarch64-alpine-3.19.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.0.4-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.0.4-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes-4)Fixes

* [CXXCBC-620](https://jira.issues.couchbase.com/browse/CXXCBC-620): Updated core `analytics_link_get_all` to follow the RFC ([#687](https://github.com/couchbase/couchbase-cxx-client/pull/687)).
* [CXXCBC-615](https://jira.issues.couchbase.com/browse/CXXCBC-615): Exposed `insert_raw` and `replace_raw` in core transactions attempt context ([#686](https://github.com/couchbase/couchbase-cxx-client/pull/686)).
* [CXXCBC-622](https://jira.issues.couchbase.com/browse/CXXCBC-622): Updated `OpenTelemetry` metrics integration to use GA Metrics API ([#688](https://github.com/couchbase/couchbase-cxx-client/pull/688)).
* [CXXCBC-627](https://jira.issues.couchbase.com/browse/CXXCBC-627): A preformance degradation was discovered to be caused by work done in the error function, even if the operation had been successful. The internal conversion work is now only carried out in response to error conditions ([#693](https://github.com/couchbase/couchbase-cxx-client/pull/693)).
* [CXXCBC-624](https://jira.issues.couchbase.com/browse/CXXCBC-624): Fixed user agent ID generation ([#692](https://github.com/couchbase/couchbase-cxx-client/pull/692)).
* [CXXCBC-611](https://jira.issues.couchbase.com/browse/CXXCBC-611), [CXXCBC-612](https://jira.issues.couchbase.com/browse/CXXCBC-612): Updated metric operation names to follow RFC naming ([#695](https://github.com/couchbase/couchbase-cxx-client/pull/695)).
* [CXXCBC-632](https://jira.issues.couchbase.com/browse/CXXCBC-632): A crash on testing against Analytics nodes under rebalance was caused by the assumption that Analytics would always send meta fields in its response. This has now been fixed, and the behoavior should not recur ([#699](https://github.com/couchbase/couchbase-cxx-client/pull/699)).
* URI encoding for `user_upsert` ([#700](https://github.com/couchbase/couchbase-cxx-client/pull/700)).

#### [](#features)Features

* [CXXCBC-609](https://jira.issues.couchbase.com/browse/CXXCBC-609): Exposed `parent_span` in Public API options ([#690](https://github.com/couchbase/couchbase-cxx-client/pull/690)).

#### [](#build-and-test-infrastructure-3)Build and Test Infrastructure

* Updates for YUM/RPM builders ([#691](https://github.com/couchbase/couchbase-cxx-client/pull/691)).
* Debian/Ubuntu packaging scripts added ([#694](https://github.com/couchbase/couchbase-cxx-client/pull/694)).
* Fixed packaging scripts on MacOS ([#698](https://github.com/couchbase/couchbase-cxx-client/pull/698)).
* Added scripts to produce APK files for Alpine Linux ([#685](https://github.com/couchbase/couchbase-cxx-client/pull/685)).

### [](#version-1-0-3-22-october-2024)Version 1.0.3 (22 October 2024)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.3) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.2...1.0.3)

#### [](#downloads-12)Downloads

| Platform           | Architecture | File                                                                                                                                               |
| ------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums          | Any          | [couchbase-cxx-client-1.0.3.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3.sha256.txt)                          |
| Source Archive     | Any          | [couchbase-cxx-client-1.0.3.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3.tar.gz)                                  |
| Amazon Linux 2023  | x86\_64      | [couchbase-cxx-client-1.0.3-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3-1.amzn2023.x86%5F64.tar) |
| Amazon Linux 2023  | aarch64      | [couchbase-cxx-client-1.0.3-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3-1.amzn2023.aarch64.tar)  |
| Enterprise Linux 9 | x86\_64      | [couchbase-cxx-client-1.0.3-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3-1.el9.x86%5F64.tar)           |
| Enterprise Linux 9 | aarch64      | [couchbase-cxx-client-1.0.3-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3-1.el9.aarch64.tar)            |
| Enterprise Linux 8 | x86\_64      | [couchbase-cxx-client-1.0.3-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3-1.el8.x86%5F64.tar)           |
| Enterprise Linux 8 | aarch64      | [couchbase-cxx-client-1.0.3-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.3-1.el8.aarch64.tar)            |

#### [](#fixes-5)Fixes

* [CXXCBC-599](https://jira.issues.couchbase.com/browse/CXXCBC-599): Updated allowed connection string options ([#668](https://github.com/couchbase/couchbase-cxx-client/pull/668)).
* [CXXCBC-311](https://jira.issues.couchbase.com/browse/CXXCBC-311): SDKs must encode URIs ([#674](https://github.com/couchbase/couchbase-cxx-client/pull/674)).
* [CXXCBC-606](https://jira.issues.couchbase.com/browse/CXXCBC-606): Fixed detection of dysfunctional node ([#673](https://github.com/couchbase/couchbase-cxx-client/pull/673)).
* [CXXCBC-574](https://jira.issues.couchbase.com/browse/CXXCBC-574): Fixed memory leak when open fails in public API ([#649](https://github.com/couchbase/couchbase-cxx-client/pull/649)).
* [CXXCBC-614](https://jira.issues.couchbase.com/browse/CXXCBC-614): Fixed memory leak in `observe_poll` ([#679](https://github.com/couchbase/couchbase-cxx-client/pull/679)).
* Added missing template parameters to fix compiler warnings ([#671](https://github.com/couchbase/couchbase-cxx-client/pull/671)).

#### [](#features-2)Features

* Allow to query current log level ([#672](https://github.com/couchbase/couchbase-cxx-client/pull/672)).
* [CXXCBC-582](https://jira.issues.couchbase.com/browse/CXXCBC-582): Added cluster labels & system tag in spans ([#682](https://github.com/couchbase/couchbase-cxx-client/pull/682)).
* [CXXCBC-582](https://jira.issues.couchbase.com/browse/CXXCBC-582): Added cluster labels, keyspace & outcome in metrics ([#677](https://github.com/couchbase/couchbase-cxx-client/pull/677)).

#### [](#columnar-changes)Columnar changes

* [CXXCBC-598](https://jira.issues.couchbase.com/browse/CXXCBC-598): Propagate bootstrap errors to HTTP operations ([#666](https://github.com/couchbase/couchbase-cxx-client/pull/666)).
* [CXXCBC-602](https://jira.issues.couchbase.com/browse/CXXCBC-602): Report first non-retriable code/message in query error ([#667](https://github.com/couchbase/couchbase-cxx-client/pull/667)).
* [CXXCBC-604](https://jira.issues.couchbase.com/browse/CXXCBC-604): Apply raw options last ([#669](https://github.com/couchbase/couchbase-cxx-client/pull/669)).
* [CXXCBC-616](https://jira.issues.couchbase.com/browse/CXXCBC-616): Report retry information when receiving a timeout from the HTTP component ([#681](https://github.com/couchbase/couchbase-cxx-client/pull/681)).
* [CXXCBC-600](https://jira.issues.couchbase.com/browse/CXXCBC-600): Reduced `origin::to_json` output for Columnar builds ([#678](https://github.com/couchbase/couchbase-cxx-client/pull/678)).

#### [](#build-and-test-infrastructure-4)Build and Test Infrastructure

* [CXXCBC-303](https://jira.issues.couchbase.com/browse/CXXCBC-303): Fixed RPM for AmazonLinux ([#663](https://github.com/couchbase/couchbase-cxx-client/pull/663)).
* [CXXCBC-303](https://jira.issues.couchbase.com/browse/CXXCBC-303): Fixed RPM for RHEL 8 ([#664](https://github.com/couchbase/couchbase-cxx-client/pull/664)).
* Use timestamp from the tag for reproducible tarballs ([#665](https://github.com/couchbase/couchbase-cxx-client/pull/665)).
* Updated list of RPM-based platforms ([#676](https://github.com/couchbase/couchbase-cxx-client/pull/676)).

### [](#version-1-0-2-23-september-2024)Version 1.0.2 (23 September 2024)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.2) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.1...1.0.2)

#### [](#downloads-13)Downloads

| Platform           | Architecture | File                                                                                                                                               |
| ------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums          | Any          | [couchbase-cxx-client-1.0.2.sha256.txt](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2.sha256.txt)                          |
| Source Archive     | Any          | [couchbase-cxx-client-1.0.2.tar.gz](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2.tar.gz)                                  |
| Amazon Linux 2023  | x86\_64      | [couchbase-cxx-client-1.0.2-1.amzn2023.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2-1.amzn2023.x86%5F64.tar) |
| Amazon Linux 2023  | aarch64      | [couchbase-cxx-client-1.0.2-1.amzn2023.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2-1.amzn2023.aarch64.tar)  |
| Enterprise Linux 9 | x86\_64      | [couchbase-cxx-client-1.0.2-1.el9.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2-1.el9.x86%5F64.tar)           |
| Enterprise Linux 9 | aarch64      | [couchbase-cxx-client-1.0.2-1.el9.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2-1.el9.aarch64.tar)            |
| Enterprise Linux 8 | x86\_64      | [couchbase-cxx-client-1.0.2-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2-1.el8.x86%5F64.tar)           |
| Enterprise Linux 8 | aarch64      | [couchbase-cxx-client-1.0.2-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.2-1.el8.aarch64.tar)            |

#### [](#fixes-6)Fixes

* [CXXCBC-577](http://jira.issues.couchbase.com/browse/CXXCBC-577): Reduced duplicated code in `http_component` ([#657](https://github.com/couchbase/couchbase-cxx-client/pull/657)).
* [CXXCBC-593](http://jira.issues.couchbase.com/browse/CXXCBC-593): Configuration profile are now applied as the last step — taking priority over all other defaults and options ([#655](https://github.com/couchbase/couchbase-cxx-client/pull/655)).
* [CXXCBC-552](http://jira.issues.couchbase.com/browse/CXXCBC-552): Cleaned up network selection options (, by deprecating `behavior_options#network()` in favor to `network_options#preferred_network()` [#651](https://github.com/couchbase/couchbase-cxx-client/pull/651)).
* [CXXCBC-576](http://jira.issues.couchbase.com/browse/CXXCBC-576): When `cluster.close()` is called, all in-progress HTTP operations should now be cancelled ([#648](https://github.com/couchbase/couchbase-cxx-client/pull/648)).
* Updated code samples in API reference ([#653](https://github.com/couchbase/couchbase-cxx-client/pull/653)).

#### [](#columnar-changes-2)Columnar changes

* [CXXCBC-577](http://jira.issues.couchbase.com/browse/CXXCBC-577): Added Columnar database management operations.
* [CXXCBC-588](http://jira.issues.couchbase.com/browse/CXXCBC-588): Updated timeout sent to server on each Columnar query retry ([#654](https://github.com/couchbase/couchbase-cxx-client/pull/654)).
* [CXXCBC-580](http://jira.issues.couchbase.com/browse/CXXCBC-580): SDK now reports last error when timing out on Columnar query retries ([#650](https://github.com/couchbase/couchbase-cxx-client/pull/650)).

#### [](#build-and-test-infrastructure-5)Build and Test Infrastructure

* [CXXCBC-303](http://jira.issues.couchbase.com/browse/CXXCBC-303): Updated build scripts to produce RPM packages ([#660](https://github.com/couchbase/couchbase-cxx-client/pull/660)).
* [CXXCBC-597](http://jira.issues.couchbase.com/browse/CXXCBC-597): SDK now use static library for ASIO; updated it to 1.31.0 ([#658](https://github.com/couchbase/couchbase-cxx-client/pull/658)).
* [CXXCBC-596](http://jira.issues.couchbase.com/browse/CXXCBC-596): No longer include `tao_json_serializer.hxx` by default ([#656](https://github.com/couchbase/couchbase-cxx-client/pull/656)).
* Include `<string>` in `string_hex.h` ([#652](https://github.com/couchbase/couchbase-cxx-client/pull/652)).

### [](#version-1-0-1-22-august-2024)Version 1.0.1 (22 August 2024)

This is the first maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.1) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.0...1.0.1)

#### [](#enhancements)Enhancements

* [CXXCBC-564](https://issues.couchbase.com/browse/CXXCBC-564/): Allow to specify all operations (Get, Replace, Delete, Insert, and Query) in pillowfight workload ([#640](https://github.com/couchbase/couchbase-cxx-client/pull/640)).
* Improve logging of DNS client ([#634](https://github.com/couchbase/couchbase-cxx-client/pull/634)).
* [CXXCBC-568](https://issues.couchbase.com/browse/CXXCBC-568/): Cancel deferred operations when closing HTTP session manager ([#643](https://github.com/couchbase/couchbase-cxx-client/pull/643)).

#### [](#fixes-7)Fixes

* [CXXCBC-531](https://issues.couchbase.com/browse/CXXCBC-531/): Fixed memory leak in range scan implementation ([#645](https://github.com/couchbase/couchbase-cxx-client/pull/645), [#610](https://github.com/couchbase/couchbase-cxx-client/pull/610)).
* [CXXCBC-573](https://issues.couchbase.com/browse/CXXCBC-573/): Avoid uninitialized reads in the logger test ([#610](https://github.com/couchbase/couchbase-cxx-client/pull/610)).
* [CXXCBC-572](https://issues.couchbase.com/browse/CXXCBC-572/): Always initialize service\_type ([#610](https://github.com/couchbase/couchbase-cxx-client/pull/610)).
* [CXXCBC-569](https://issues.couchbase.com/browse/CXXCBC-569/): Resolved cycle in shared pointers for `transaction_context`([#641](https://github.com/couchbase/couchbase-cxx-client/pull/641)).
* [CXXCBC-550](https://issues.couchbase.com/browse/CXXCBC-550/): Fixed use-after-move issue in command handler ([#628](https://github.com/couchbase/couchbase-cxx-client/pull/628)).
* Fixed build of Ruby wrapper on Windows ([#636](https://github.com/couchbase/couchbase-cxx-client/pull/636)).
* Fixed behaviour when reading is complete before returning HTTP streaming resp ([#624](https://github.com/couchbase/couchbase-cxx-client/pull/624)).

#### [](#columnar-changes-3)Columnar changes

In this release a new build mode for Columnar has been introduced. The CMake flag `-DCOUCHBASE_CXX_CLIENT_COLUMNAR` will produce a special version of the library that is optimized for usage with Columnar deployments.

* Add initial Columnar core implementation ([#616](https://github.com/couchbase/couchbase-cxx-client/pull/616)).
* [CXXCBC-525](https://issues.couchbase.com/browse/CXXCBC-525/): Open cluster connection in background ([#621](https://github.com/couchbase/couchbase-cxx-client/pull/621)).
* Use `open_in_background` when creating test cluster in Columnar mode ([#625](https://github.com/couchbase/couchbase-cxx-client/pull/625)).
* [CXXCBC-542](https://issues.couchbase.com/browse/CXXCBC-542/): Richer error information from Columnar core ([#626](https://github.com/couchbase/couchbase-cxx-client/pull/626)).
* Updated columnar log message, enabling `dispatch_timeout` if in connection string ([#627](https://github.com/couchbase/couchbase-cxx-client/pull/627)).
* Add helper method for serializing `ctx` into columnar error message ([#632](https://github.com/couchbase/couchbase-cxx-client/pull/632)).
* Add Columnar query positional params ([#635](https://github.com/couchbase/couchbase-cxx-client/pull/635)).
* [CXXCBC-543](https://issues.couchbase.com/browse/CXXCBC-543/): Added retries for columnar query ([#637](https://github.com/couchbase/couchbase-cxx-client/pull/637)).
* [CXXCBC-562](https://issues.couchbase.com/browse/CXXCBC-562/): Provided HTTP session manager with updated cluster ([#638](https://github.com/couchbase/couchbase-cxx-client/pull/638)).
* [CXXCBC-556](https://issues.couchbase.com/browse/CXXCBC-556/): Added versioned Columnar query endpoint ([#639](https://github.com/couchbase/couchbase-cxx-client/pull/639)).
* [CXXCBC-557](https://issues.couchbase.com/browse/CXXCBC-557/): Added global columnar timeout config ([#642](https://github.com/couchbase/couchbase-cxx-client/pull/642)).

### [](#version-1-0-0-26-june-2024)Version 1.0.0 (26 June 2024)

This is the first GA release of the C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.0) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.0-dp.15…​1.0.0)

#### [](#enhancements-2)Enhancements

* [CXXCBC-509](https://issues.couchbase.com/browse/CXXCBC-509): Allow to restrict replica set to selected server group. This feature allows to implement network optimization when traffic cost between server groups is higher than in the local group. In this case the application might select preferred server group in the connection options, and later opt-in for local operations during replica reads. Related tickets: [CXXCBC-546](https://issues.couchbase.com/browse/CXXCBC-546), [CXXCBC-513](https://issues.couchbase.com/browse/CXXCBC-513), ([#614](https://github.com/couchbase/couchbase-cxx-client/pull/614), [#593](https://github.com/couchbase/couchbase-cxx-client/pull/593), [#587](https://github.com/couchbase/couchbase-cxx-client/pull/587), [#571](https://github.com/couchbase/couchbase-cxx-client/pull/571), [#566](https://github.com/couchbase/couchbase-cxx-client/pull/566)).
* [CXXCBC-530](https://issues.couchbase.com/browse/CXXCBC-530): Include 'min' parameter when encoding disjunction FTS queries ([#604](https://github.com/couchbase/couchbase-cxx-client/pull/604)).
* [CXXCBC-394](https://issues.couchbase.com/browse/CXXCBC-394): Hide `tao::json` where it is possible. We still have taocpp/json headers in places where default JSON transcoder is being used.
* [CXXCBC-449](https://issues.couchbase.com/browse/CXXCBC-449): Do not expose ASIO in public API.
* [CXXCBC-381](https://issues.couchbase.com/browse/CXXCBC-381): Use `std::shared_ptr` for `transactions_context` and `attempt_context` ([#590](https://github.com/couchbase/couchbase-cxx-client/pull/590)).
* [CXXCBC-510](https://issues.couchbase.com/browse/CXXCBC-510): Support binary objects in transactions. This changes allows to use transcoders in transactions API ([#576](https://github.com/couchbase/couchbase-cxx-client/pull/576)).
* Improvements in Vector Search:

  * Add invalid argument check ([#578](https://github.com/couchbase/couchbase-cxx-client/pull/578)).
  * [CXXCBC-514](https://issues.couchbase.com/browse/CXXCBC-514): Support for base64 encoded vector types (\[[#575](https://github.com/couchbase/couchbase-cxx-client/pull/575)).
  * [CXXCBC-516](https://issues.couchbase.com/browse/CXXCBC-516): Return `feature_not_available` when upserting vector search index to incompatible cluster ([#572](https://github.com/couchbase/couchbase-cxx-client/pull/572)).
* [CXXCBC-407](https://issues.couchbase.com/browse/CXXCBC-407): Allow to use 0 as a max expiry for new collections ([#569](https://github.com/couchbase/couchbase-cxx-client/pull/569)).
* [CXXCBC-496](https://issues.couchbase.com/browse/CXXCBC-496): Convert C++ Public API Error handling to use `couchbase::error`. Related tickets: [CXXCBC-492](https://issues.couchbase.com/browse/CXXCBC-492), [CXXCBC-498](https://issues.couchbase.com/browse/CXXCBC-498), [CXXCBC-499](https://issues.couchbase.com/browse/CXXCBC-499), [CXXCBC-500](https://issues.couchbase.com/browse/CXXCBC-500), [CXXCBC-508](https://issues.couchbase.com/browse/CXXCBC-508), [CXXCBC-526](https://issues.couchbase.com/browse/CXXCBC-526)([#570](https://github.com/couchbase/couchbase-cxx-client/pull/570), [#557](https://github.com/couchbase/couchbase-cxx-client/pull/557), [#562](https://github.com/couchbase/couchbase-cxx-client/pull/562), [#560](https://github.com/couchbase/couchbase-cxx-client/pull/560), [#564](https://github.com/couchbase/couchbase-cxx-client/pull/564), [#567](https://github.com/couchbase/couchbase-cxx-client/pull/567), [#603](https://github.com/couchbase/couchbase-cxx-client/pull/603), [#597](https://github.com/couchbase/couchbase-cxx-client/pull/597), [#595](https://github.com/couchbase/couchbase-cxx-client/pull/595), [#594](https://github.com/couchbase/couchbase-cxx-client/pull/594)).
* Update stability levels for API 3.6 level. Remove deprecated `search_query` ([#602](https://github.com/couchbase/couchbase-cxx-client/pull/602)).

#### [](#fixes-8)Fixes

* [CXXCBC-517](https://issues.couchbase.com/browse/CXXCBC-517): Add HTTP session retries when SDK fails to resolve hostnames ([#589](https://github.com/couchbase/couchbase-cxx-client/pull/589)).
* [CXXCBC-445](https://issues.couchbase.com/browse/CXXCBC-445): Return `request_canceled` on IO error in HTTP session ([#568](https://github.com/couchbase/couchbase-cxx-client/pull/568)).
* [CXXCBC-511](https://issues.couchbase.com/browse/CXXCBC-511): Prevent use of HTTP session if idle timer has expired ([#565](https://github.com/couchbase/couchbase-cxx-client/pull/565)).
* [CXXCBC-523](https://issues.couchbase.com/browse/CXXCBC-523): Clean up `dump_configuration` config output ([#577](https://github.com/couchbase/couchbase-cxx-client/pull/577)).
* [CXXCBC-531](https://issues.couchbase.com/browse/CXXCBC-531): Fix deadlock in cluster destructor (public API) ([#608](https://github.com/couchbase/couchbase-cxx-client/pull/608)).
* [CXXCBC-534](https://issues.couchbase.com/browse/CXXCBC-534): Fix callbacks to avoid `bad_function_call` exception ([#606](https://github.com/couchbase/couchbase-cxx-client/pull/606)).
* [CXXCBC-518](https://issues.couchbase.com/browse/CXXCBC-518): Handle alternate addresses when locating `preferred_node` ([#574](https://github.com/couchbase/couchbase-cxx-client/pull/574)).

#### [](#build-and-tests-fixes-2)Build and Tests Fixes

* Add cmake task to generate tarball ([#596](https://github.com/couchbase/couchbase-cxx-client/pull/596)).
* Do not refer to core headers in public API ([#599](https://github.com/couchbase/couchbase-cxx-client/pull/599)).
* Cleanup `attempt_context` implementation ([#586](https://github.com/couchbase/couchbase-cxx-client/pull/586)).
* Do not use default parameters for virtual functions in transactions ([#588](https://github.com/couchbase/couchbase-cxx-client/pull/588)).
* Do not fetch config if no sessions in the bucket ([#573](https://github.com/couchbase/couchbase-cxx-client/pull/573)).
* Improve test stability ([#563](https://github.com/couchbase/couchbase-cxx-client/pull/563), [#613](https://github.com/couchbase/couchbase-cxx-client/pull/613)).

## [](#older-versions)Older Versions

Release Notes for the developer preview releases before the 1.0.0 release can be found on [GitHub](https://github.com/couchbaselabs/couchbase-cxx-client/releases).