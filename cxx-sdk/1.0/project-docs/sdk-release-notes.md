[View original HTML](/cxx-sdk/1.0/project-docs/sdk-release-notes.html)

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

## [](#latest-release)C++ SDK 1.0 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-1-0-7-24-april-2025)Version 1.0.7 (24 April 2025)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.7) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.5...1.0.7)

#### [](#downloads)Downloads

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
| Ubuntu 20.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.7-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.jammy.x86%5F64.tar)               |
| Ubuntu 20.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.7-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.jammy.aarch64.tar)                |
| Ubuntu 22.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.7-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.noble.x86%5F64.tar)                 |
| Ubuntu 22.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.7-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.7-1.noble.aarch64.tar)                  |
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

#### [](#downloads-2)Downloads

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
| Ubuntu 20.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.6-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.jammy.x86%5F64.tar)               |
| Ubuntu 20.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.6-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.jammy.aarch64.tar)                |
| Ubuntu 22.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.6-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.noble.x86%5F64.tar)                 |
| Ubuntu 22.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.6-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.6-1.noble.aarch64.tar)                  |
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

#### [](#downloads-3)Downloads

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
| Ubuntu 20.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.5-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.jammy.x86%5F64.tar)               |
| Ubuntu 20.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.5-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.jammy.aarch64.tar)                |
| Ubuntu 22.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.5-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.noble.x86%5F64.tar)                 |
| Ubuntu 22.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.5-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-1.noble.aarch64.tar)                  |
| Alpine Linux 3.19    | x86\_64      | [couchbase-cxx-client-1.0.5-r1-x86\_64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-x86%5F64-alpine-3.19.tar) |
| Alpine Linux 3.19    | aarch64      | [couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.19.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.19.tar)  |
| Alpine Linux 3.20    | x86\_64      | [couchbase-cxx-client-1.0.5-r1-x86\_64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-x86%5F64-alpine-3.20.tar) |
| Alpine Linux 3.20    | aarch64      | [couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.20.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.5-r1-aarch64-alpine-3.20.tar)  |

#### [](#fixes-3)Fixes

* [CXXCBC-633](https://jira.issues.couchbase.com/browse/CXXCBC-633): In a case of timeout, when the total deadline of the DNS-SRV request has been reached, the library will now report a timeout error code, and not the latest abort as it was doing.
* Server group replica reads are now exposed in `transaction_context` ([#704](https://github.com/couchbase/couchbase-cxx-client/pull/704)).

#### [](#build-and-test-infrastructure)Build and Test Infrastructure

* Minor improvements ([#706](https://github.com/couchbase/couchbase-cxx-client/pull/706)).
* [CXXCBC-640](https://jira.issues.couchbase.com/browse/CXXCBC-640): Debug symbols are no longer forced for release builds ([#708](https://github.com/couchbase/couchbase-cxx-client/pull/708)).
* [CXXCBC-638](https://jira.issues.couchbase.com/browse/CXXCBC-638): Switched SDK to use bundled `fmtlib` for `spdlog` ([#705](https://github.com/couchbase/couchbase-cxx-client/pull/705)).
* Updated `spdlog` to `1.15.0` ([#709](https://github.com/couchbase/couchbase-cxx-client/pull/709)).

### [](#version-1-0-4-22-november-2024)Version 1.0.4 (22 November 2024)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.4) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.3...1.0.4)

#### [](#downloads-4)Downloads

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
| Ubuntu 20.04 (Jammy) | x86\_64      | [couchbase-cxx-client-1.0.4-1.jammy.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.jammy.x86%5F64.tar)               |
| Ubuntu 20.04 (Jammy) | aarch64      | [couchbase-cxx-client-1.0.4-1.jammy.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.jammy.aarch64.tar)                |
| Ubuntu 22.04 (Noble) | x86\_64      | [couchbase-cxx-client-1.0.4-1.el8.x86\_64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.noble.x86%5F64.tar)                 |
| Ubuntu 22.04 (Noble) | aarch64      | [couchbase-cxx-client-1.0.4-1.el8.aarch64.tar](https://packages.couchbase.com/clients/cxx/couchbase-cxx-client-1.0.4-1.noble.aarch64.tar)                  |
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

#### [](#build-and-test-infrastructure-2)Build and Test Infrastructure

* Updates for YUM/RPM builders ([#691](https://github.com/couchbase/couchbase-cxx-client/pull/691)).
* Debian/Ubuntu packaging scripts added ([#694](https://github.com/couchbase/couchbase-cxx-client/pull/694)).
* Fixed packaging scripts on MacOS ([#698](https://github.com/couchbase/couchbase-cxx-client/pull/698)).
* Added scripts to produce APK files for Alpine Linux ([#685](https://github.com/couchbase/couchbase-cxx-client/pull/685)).

### [](#version-1-0-3-22-october-2024)Version 1.0.3 (22 October 2024)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.3) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.2...1.0.3)

#### [](#downloads-5)Downloads

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

#### [](#build-and-test-infrastructure-3)Build and Test Infrastructure

* [CXXCBC-303](https://jira.issues.couchbase.com/browse/CXXCBC-303): Fixed RPM for AmazonLinux ([#663](https://github.com/couchbase/couchbase-cxx-client/pull/663)).
* [CXXCBC-303](https://jira.issues.couchbase.com/browse/CXXCBC-303): Fixed RPM for RHEL 8 ([#664](https://github.com/couchbase/couchbase-cxx-client/pull/664)).
* Use timestamp from the tag for reproducible tarballs ([#665](https://github.com/couchbase/couchbase-cxx-client/pull/665)).
* Updated list of RPM-based platforms ([#676](https://github.com/couchbase/couchbase-cxx-client/pull/676)).

### [](#version-1-0-2-23-september-2024)Version 1.0.2 (23 September 2024)

This is a maintenance release of the 1.0 C++ SDK.

[API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client-1.0.2) | [Full Changelog](https://github.com/couchbase/couchbase-cxx-client/compare/1.0.1...1.0.2)

#### [](#downloads-6)Downloads

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

#### [](#build-and-test-infrastructure-4)Build and Test Infrastructure

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

#### [](#build-and-tests-fixes)Build and Tests Fixes

* Add cmake task to generate tarball ([#596](https://github.com/couchbase/couchbase-cxx-client/pull/596)).
* Do not refer to core headers in public API ([#599](https://github.com/couchbase/couchbase-cxx-client/pull/599)).
* Cleanup `attempt_context` implementation ([#586](https://github.com/couchbase/couchbase-cxx-client/pull/586)).
* Do not use default parameters for virtual functions in transactions ([#588](https://github.com/couchbase/couchbase-cxx-client/pull/588)).
* Do not fetch config if no sessions in the bucket ([#573](https://github.com/couchbase/couchbase-cxx-client/pull/573)).
* Improve test stability ([#563](https://github.com/couchbase/couchbase-cxx-client/pull/563), [#613](https://github.com/couchbase/couchbase-cxx-client/pull/613)).

## [](#older-versions)Older Versions

Release Notes for the developer preview releases before the 1.0.0 release can be found on [GitHub](https://github.com/couchbaselabs/couchbase-cxx-client/releases).