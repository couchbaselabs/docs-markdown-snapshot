---
title: SDK Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Ruby Client.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.6/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.6@ruby-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.6/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Ruby Client. 

This page covers installation of the 3.x versions of the Couchbase Ruby SDK, and release notes for all 3.x versions.

## [](#sdk-installation)SDK Installation

Ruby SDK supports MRI Ruby versions 3.1, 3.2, and 3.3\. The source package is available through <https://rubygems.org/gems/couchbase> and can be installed with:

```console
gem install couchbase
```

Note that `--pre` is necessary when the SDK in Beta/Preview phase — `gem install --pre couchbase` — otherwise the latest stable release will be installed.

In addition to rubygems.org, we also maintain official gem repositories, where we publish not only source version of the package, but also precompiled binaries for Linux and MacOS.

To use official repository, it have to be registered in the `.gemrc` file:

```bash
gem sources --add https://packages.couchbase.com/clients/ruby/
```

The repository could be also specified in `Gemfile` for bundler. And in this case the source would be applied only for Couchbase SDK library:

```ruby
gem "couchbase", "3.6.0", :source => "https://packages.couchbase.com/clients/ruby/"
```

Or run in terminal:

```bash
gem install couchbase --clear-sources --source https://packages.couchbase.com/clients/ruby/
```

And finally, it is possible to download the package and install from the file. In the notes below, we specify tables with links to every release package along with precompiled binaries.

```bash
wget https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0-x86_64-linux.gem
gem install couchbase-3.6.0-x86_64-linux.gem
```

The URL structure is:

```shell
https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0-%{platform}.gem
```

where "platform" placeholder can take values: `arm64-darwin`, `x86_64-darwin`, `x86_64-linux`, `x86_64-linux-musl`. To see platform string the following command:

```bash
ruby -rrbconfig -e 'puts RbConfig::CONFIG["platform"]'
```

## [](#latest-release)Ruby SDK 3.6 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-3-6-0-2-june-2025)Version 3.6.0 (2 June 2025)

```bash
gem install couchbase -v 3.6.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.6.0/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.7...3.6.0) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.6.0)

#### [](#download-links)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.6.0.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0.sha256sum)                            |
| Source Archive       | [couchbase-3.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0.gem)                                        |
| Linux x86\_64        | [couchbase-3.6.0-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0-x86%5F64-linux.gem)           |
| Linux arm64          | [couchbase-3.6.0-aarch64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0-aarch64-linux.gem)            |
| Linux x86\_64 (musl) | [couchbase-3.6.0-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0-x86%5F64-linux-musl.gem) |
| macOS x86\_64        | [couchbase-3.6.0-x86\_64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0-x86%5F64-darwin.gem)         |
| macOS arm64          | [couchbase-3.6.0-arm64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.6.0/couchbase-3.6.0-arm64-darwin.gem)              |

#### [](#new-features)New Features

* [RCBC-516](https://issues.couchbase.com/browse/516): Include `storage_backend` in `get_bucket/get_all_buckets` results ([#173](https://github.com/couchbase/couchbase-ruby-client/pull/173)).
* [RCBC-510](https://issues.couchbase.com/browse/510): Added `BucketSettings#num_vbuckets` ([#174](https://github.com/couchbase/couchbase-ruby-client/pull/174)).

#### [](#fixes)Fixes

* [RCBC-511](https://issues.couchbase.com/browse/511): Updated core to pick up improved user lock/unlock error messages & logs ([#177](https://github.com/couchbase/couchbase-ruby-client/pull/177)).
* Updated core to 1.1.0\. Release notes: [C++ SDK 1.1.0](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-1-0-01-june-2025).

## [](#ruby-sdk-3-5-releases)Ruby SDK 3.5 Releases

### [](#version-3-5-7-31-march-2025)Version 3.5.7 (31 March 2025)

```bash
gem install couchbase -v 3.5.7
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.7/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.6...3.5.7) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.7)

#### [](#download-links-2)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.7.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.7/couchbase-3.5.7.sha256sum)                            |
| Source Archive       | [couchbase-3.5.7.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.7/couchbase-3.5.7.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.7-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.7/couchbase-3.5.7-x86%5F64-linux.gem)           |
| Linux arm64          | [couchbase-3.5.7-aarch64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.7/couchbase-3.5.7-aarch64-linux.gem)            |
| Linux x86\_64 (musl) | [couchbase-3.5.7-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.7/couchbase-3.5.7-x86%5F64-linux-musl.gem) |
| macOS x86\_64        | [couchbase-3.5.7-x86\_64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.7/couchbase-3.5.7-x86%5F64-darwin.gem)         |
| macOS arm64          | [couchbase-3.5.7-arm64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.7/couchbase-3.5.7-arm64-darwin.gem)              |

#### [](#fixes-2)Fixes

* [RCBC-514](https://issues.couchbase.com/browse/RCBC-514): Added support for Ruby 3.4 and Linux/arm64 ([#170](https://github.com/couchbase/couchbase-ruby-client/pull/)).
* [RCBC-515](https://issues.couchbase.com/browse/RCBC-515): Enforce `CMAKE_POLICY_VERSION_MINIMUM` to be `3.5` for `snappy` and `cmake` `4.x` ([#172](https://github.com/couchbase/couchbase-ruby-client/pull/172)).

### [](#version-3-5-6-18-march-2025)Version 3.5.6 (18 March 2025)

```bash
gem install couchbase -v 3.5.6
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.6/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.5...3.5.6) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.6)

#### [](#download-links-3)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.6.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.6/couchbase-3.5.6.sha256sum)                            |
| Source Archive       | [couchbase-3.5.6.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.6/couchbase-3.5.6.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.6-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.6/couchbase-3.5.6-x86%5F64-linux.gem)           |
| Linux x86\_64 (musl) | [couchbase-3.5.6-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.6/couchbase-3.5.6-x86%5F64-linux-musl.gem) |
| macOS x86\_64        | [couchbase-3.5.6-x86\_64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.6/couchbase-3.5.6-x86%5F64-darwin.gem)         |
| macOS arm64          | [couchbase-3.5.6-arm64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.6/couchbase-3.5.6-arm64-darwin.gem)              |

#### [](#fixes-3)Fixes

* [RCBC-512](https://issues.couchbase.com/browse/RCBC-512): Invoke fork hooks to protect SDK internal state ([#165](https://github.com/couchbase/couchbase-ruby-client/pull/156)).
* Updated core to 1.0.6\. Release notes: [C++ SDK 1.0.6](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-6-12-march-2025).

### [](#version-3-5-5-28-january-2025)Version 3.5.5 (28 January 2025)

```bash
gem install couchbase -v 3.5.5
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.5/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.4...3.5.5) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.5)

#### [](#download-links-4)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.5.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.5/couchbase-3.5.5.sha256sum)                            |
| Source Archive       | [couchbase-3.5.5.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.5/couchbase-3.5.5.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.5-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.5/couchbase-3.5.5-x86%5F64-linux.gem)           |
| Linux x86\_64 (musl) | [couchbase-3.5.5-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.5/couchbase-3.5.5-x86%5F64-linux-musl.gem) |
| macOS x86\_64        | [couchbase-3.5.5-x86\_64-darwin-20.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.5/couchbase-3.5.5-x86%5F64-darwin.gem)      |
| macOS arm64          | [couchbase-3.5.5-arm64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.5/couchbase-3.5.5-arm64-darwin.gem)              |

#### [](#fixes-4)Fixes

* [RCBC-487](https://issues.couchbase.com/browse/RCBC-487): New APIs added to allow getting KV documents from a preferred server group. This feature allows the implementation of network optimization when traffic cost between server groups is higher than in the local group. In this case the application might select preferred server group in the connection options, and later opt-in for local operations during replica reads ([#163](https://github.com/couchbase/couchbase-ruby-client/pull/163)).
* [RCBC-504](https://issues.couchbase.com/browse/RCBC-504): Updated core and version generation ([#162](https://github.com/couchbase/couchbase-ruby-client/pull/162)).
* Updated core to 1.0.5\. Release notes: [C++ SDK 1.0.5](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-5-24-january-2025).

### [](#version-3-5-4-22-october-2024)Version 3.5.4 (22 October 2024)

```bash
gem install couchbase -v 3.5.4
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.4/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.3...3.5.4) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.4)

#### [](#download-links-5)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.4.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.4/couchbase-3.5.4.sha256sum)                            |
| Source Archive       | [couchbase-3.5.4.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.4/couchbase-3.5.4.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.4-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.4/couchbase-3.5.4-x86%5F64-linux.gem)           |
| Linux x86\_64 (musl) | [couchbase-3.5.4-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.4/couchbase-3.5.4-x86%5F64-linux-musl.gem) |
| macOS x86\_64        | [couchbase-3.5.4-x86\_64-darwin-20.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.4/couchbase-3.5.4-x86%5F64-darwin.gem)      |
| macOS arm64          | [couchbase-3.5.4-arm64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.4/couchbase-3.5.4-arm64-darwin.gem)              |

#### [](#fixes-5)Fixes

* Updated core to 1.0.3 ([#161](https://github.com/couchbase/couchbase-ruby-client/pull/161)). Release notes: [C++ SDK 1.0.3](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-3-22-october-2024).
* Added CI scripts for Rocky Linux ([#159](https://github.com/couchbase/couchbase-ruby-client/pull/159)).

### [](#version-3-5-3-27-august-2024)Version 3.5.3 (27 August 2024)

```bash
gem install couchbase -v 3.5.3
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.3/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.2...3.5.3) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.3)

#### [](#download-links-6)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.3.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.3/couchbase-3.5.3.sha256sum)                            |
| Source Archive       | [couchbase-3.5.3.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.3/couchbase-3.5.3.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.3-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.3/couchbase-3.5.3-x86%5F64-linux.gem)           |
| Linux x86\_64 (musl) | [couchbase-3.5.3-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.3/couchbase-3.5.3-x86%5F64-linux-musl.gem) |
| macOS x86\_64        | [couchbase-3.5.3-x86\_64-darwin-20.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.3/couchbase-3.5.3-x86%5F64-darwin.gem)      |
| macOS arm64          | [couchbase-3.5.3-arm64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.3/couchbase-3.5.3-arm64-darwin.gem)              |

#### [](#fixes-6)Fixes

* [RCBC-496](https://issues.couchbase.com/browse/RCBC-496): Removed `googletest` from release package ([#154](https://github.com/couchbase/couchbase-ruby-client/pull/154)).
* Updated core to 1.0.1 ([#157](https://github.com/couchbase/couchbase-ruby-client/pull/157)). Release notes: [C++ SDK 1.0.1](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-1-22-august-2024).

### [](#version-3-5-2-25-july-2024)Version 3.5.2 (25 July 2024)

```bash
gem install couchbase -v 3.5.2
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.2/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.1...3.5.2) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.2)

#### [](#download-links-7)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.2.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.2/couchbase-3.5.2.sha256sum)                            |
| Source Archive       | [couchbase-3.5.2.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.2/couchbase-3.5.2.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.2-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.2/couchbase-3.5.2-x86%5F64-linux.gem)           |
| Linux x86\_64 (musl) | [couchbase-3.5.2-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.2/couchbase-3.5.2-x86%5F64-linux-musl.gem) |
| macOS                | [couchbase-3.5.2-x86\_64-darwin-20.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.2/couchbase-3.5.2-x86%5F64-darwin-20.gem)   |

#### [](#improvements)Improvements

* [RCBC-489](https://issues.couchbase.com/browse/RCBC-489): Support added for base64 encoded vector types ([#146](https://github.com/couchbase/couchbase-ruby-client/pull/146)).

#### [](#fixes-7)Fixes

* [RCBC-490](https://issues.couchbase.com/browse/RCBC-490), [RCBC-492](https://issues.couchbase.com/browse/RCBC-492): Raise `Error::InvalidArgument` for invalid search queries ([#145](https://github.com/couchbase/couchbase-ruby-client/pull/145), [#147](https://github.com/couchbase/couchbase-ruby-client/pull/147), [#148](https://github.com/couchbase/couchbase-ruby-client/pull/148)).
* Updated core to 1.0.0 ([#152](https://github.com/couchbase/couchbase-ruby-client/pull/152)). Release notes: [C++ SDK 1.0.0](https://docs.couchbase.com/cxx-sdk/current/project-docs/sdk-release-notes.html#version-1-0-0-26-june-2024).

### [](#version-3-5-1-23-april-2024)Version 3.5.1 (23 April 2024)

```bash
gem install couchbase -v 3.5.1
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.1/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.5.0...3.5.1) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.1)

#### [](#download-links-8)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.1.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.1/couchbase-3.5.1.sha256sum)                            |
| Source Archive       | [couchbase-3.5.1.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.1/couchbase-3.5.1.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.1-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.1/couchbase-3.5.1-x86%5F64-linux.gem)           |
| Linux x86\_64 (musl) | [couchbase-3.5.1-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.1/couchbase-3.5.1-x86%5F64-linux-musl.gem) |
| macOS 11 x84\_64     | [couchbase-3.5.1-x86\_64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.1/couchbase-3.5.1-x86%5F64-darwin.gem)         |
| macOS 13 arm64       | [couchbase-3.5.1-arm64-darwin.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.1/couchbase-3.5.1-arm64-darwin.gem)              |

#### [](#improvements-2)Improvements

* [RCBC-482](https://issues.couchbase.com/browse/RCBC-482): Only expand MutateIn macros when the relevant symbols are used as values (#141).

#### [](#bug-fixes)Bug Fixes

* [RCBC-476](https://issues.couchbase.com/browse/RCBC-476): `FeatureNotAvailable` message for `couhbase2://` `ping` and `diagnostics` (#139).

#### [](#underlying-c-sdk-core-changes)Underlying C++ SDK Core Changes

##### [](#enhancements)Enhancements

* [CXXCBC-489](https://issues.couchbase.com/browse/CXXCBC-489): Added support for scoped eventing functions ([#548](https://github.com/couchbaselabs/couchbase-cxx-client/pull/548), [#554](https://github.com/couchbaselabs/couchbase-cxx-client/pull/554)).
* [CXXCBC-470](https://issues.couchbase.com/browse/CXXCBC-470): Distinguish between 'unset' and 'off' `query_profile` ([#551](https://github.com/couchbaselabs/couchbase-cxx-client/pull/551)).

##### [](#fixes-8)Fixes

* [CXXCBC-487](https://issues.couchbase.com/browse/CXXCBC-487): Added logic during bootstrap to check if alternate addressing is being used ([#545](https://github.com/couchbaselabs/couchbase-cxx-client/pull/545)).
* [CXXCBC-503](https://issues.couchbase.com/browse/CXXCBC-503): Added logic to ignore configuration if it contains an empty vBucket map ([#556](https://github.com/couchbaselabs/couchbase-cxx-client/pull/556), [#558](https://github.com/couchbaselabs/couchbase-cxx-client/pull/558)).
* [CXXCBC-30](https://issues.couchbase.com/browse/CXXCBC-30): Fixed inconsistent behaviour when using subdoc opcodes incorrectly ([#559](https://github.com/couchbaselabs/couchbase-cxx-client/pull/559)).
* [CXXCBC-492](https://issues.couchbase.com/browse/CXXCBC-492): Updated collection\_component get\_collection\_id to use retry strategy ([#552](https://github.com/couchbaselabs/couchbase-cxx-client/pull/552)).
* [CXXCBC-494](https://issues.couchbase.com/browse/CXXCBC-494): Fixed memory issue in range scan implementation ([#549](https://github.com/couchbaselabs/couchbase-cxx-client/pull/549)).
* Always attempt to extract common query code if error has not been set ([#561](https://github.com/couchbaselabs/couchbase-cxx-client/pull/561)). This fixes quota/rate limit checks for older servers.

##### [](#build-and-tests-fixes)Build and Tests Fixes

* [CXXCBC-502](https://issues.couchbase.com/browse/CXXCBC-502): Apply `/bigobj` for SDK objects only ([#550](https://github.com/couchbaselabs/couchbase-cxx-client/pull/550)). Avoid using global `add_definitions()` as it might leak to non-C++ languages (like `ASM_NASM` on Windows).

### [](#version-3-5-0-17-march-2024)Version 3.5.0 (17 March 2024)

```bash
gem install couchbase -v 3.5.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.5.0/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.4.5...3.5.0) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.5.0)

#### [](#known-issues)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the Ruby SDK that contains C++ SDK 1.0.0-dp.15 (or later).

#### [](#improvements-3)Improvements

* [RCBC-469](https://issues.couchbase.com/browse/RCBC-469): Support added for Scoped Search Indexes ([#132](https://github.com/couchbase/couchbase-ruby-client/pull/132)).
* [RCBC-467](https://issues.couchbase.com/browse/RCBC-467): Added support for Vector search ([#131](https://github.com/couchbase/couchbase-ruby-client/pull/131)).
* [RCBC-468](https://issues.couchbase.com/browse/RCBC-468): Support added for `maxTTL` value of -1 for collection 'no expiry' ([#130](https://github.com/couchbase/couchbase-ruby-client/pull/130)).
* [RCBC-410](https://issues.couchbase.com/browse/RCBC-410), [RCBC-458](https://issues.couchbase.com/browse/RCBC-458): Added support for the `couchbase2` protocol ([#126](https://github.com/couchbase/couchbase-ruby-client/pull/126), [#127](https://github.com/couchbase/couchbase-ruby-client/pull/127)).
* [RCBC-472](https://issues.couchbase.com/browse/RCBC-472): Ping now returns result for management service when specified in options ([#134](https://github.com/couchbase/couchbase-ruby-client/pull/134)).
* [RCBC-463](https://issues.couchbase.com/browse/RCBC-463): Adedd `DocumentNotLocked` error to corresponds with the C++ error code `couchbase::errc::key_value::document_not_locked`([#128](https://github.com/couchbase/couchbase-ruby-client/pull/128)).

#### [](#bug-fixes-2)Bug Fixes

* Ensure that truncating keys in CouchbaseStore preserves the validity of their encoding ([#125](https://github.com/couchbase/couchbase-ruby-client/pull/125)).
* [RCBC-461](https://issues.couchbase.com/browse/RCBC-461): `extract_expiry_time` is now called in the setter instead of the constructor, so that the expiry is sent to the backend in the correct format, and there should no longer be an `ArgumentError`([#124](https://github.com/couchbase/couchbase-ruby-client/pull/124)).

#### [](#build-and-test-improvements)Build and Test Improvements

* [RCBC-464](https://issues.couchbase.com/browse/RCBC-464): Improved stability of management tests ([#133](https://github.com/couchbase/couchbase-ruby-client/pull/133)).
* Migrated most of the build and test tasks to GitHub Actions.

#### [](#underlying-c-sdk-core-changes-2)Underlying C++ SDK Core Changes

##### [](#changes-in-couchbase-c-sdk-1-0-0-dp-14)Changes in Couchbase C++ SDK 1.0.0-dp.14

Fixes

* [CXXCBC-482](https://issues.couchbase.com/browse/CXXCBC-482): Updated range scan orchestrator to use best effort retry strategy by default ([#542](https://github.com/couchbaselabs/couchbase-cxx-client/pull/542)).
* [CXXCBC-481](https://issues.couchbase.com/browse/CXXCBC-481): Fixed potential crash when parsing search result hits ([#541](https://github.com/couchbaselabs/couchbase-cxx-client/pull/541)).
* [CXXCBC-461](https://issues.couchbase.com/browse/CXXCBC-461): Updated ping operation to not send to nodes that have not completed bootstrap ([#540](https://github.com/couchbaselabs/couchbase-cxx-client/pull/540)).
* [CXXCBC-462](https://issues.couchbase.com/browse/CXXCBC-462): Fixed hanging when specifying a custom metadata collection via the public API & expose errors ([#532](https://github.com/couchbaselabs/couchbase-cxx-client/pull/532)).
* [CXXCBC-480](https://issues.couchbase.com/browse/CXXCBC-480): Fixed capabilities check for replica LookupIn operations ([#539](https://github.com/couchbaselabs/couchbase-cxx-client/pull/539)).
* [CXXCBC-479](https://issues.couchbase.com/browse/CXXCBC-479): Fixed capabilities check for replica `LookupIn` operations ([#537](https://github.com/couchbaselabs/couchbase-cxx-client/pull/537)).
* [CXXCBC-336](https://issues.couchbase.com/browse/CXXCBC-336): Updated DNS config to not fallback to 8.8.8.8 if SDK cannot obtain system DNS server ([#533](https://github.com/couchbaselabs/couchbase-cxx-client/pull/533)).

##### [](#changes-in-couchbase-c-sdk-1-0-0-dp-13)Changes in Couchbase C++ SDK 1.0.0-dp.13

New features and enhancements

* [CXXCBC-456](https://issues.couchbase.com/browse/CXXCBC-456): Updated configuration logic when 0x0d (`EConfigOnly`) status code is received to have the SDK request new configuration and send current operation to retry orchestrator ([#523](https://github.com/couchbaselabs/couchbase-cxx-client/pull/523)).
* [CXXCBC-191](https://issues.couchbase.com/browse/CXXCBC-191): Index Key Encoding ([#519](https://github.com/couchbaselabs/couchbase-cxx-client/pull/519)) — in line with the [rfc](https://github.com/couchbaselabs/sdk-rfcs/blob/master/rfc/0054-sdk3-management-apis.md), the `fields` paramaeter is now remamed to keys in the Public API’s `create_index()`, and each index key provided to `create_index()` is encoded by surrounding them with backticks.

Fixes

* [CXXCBC-345](https://issues.couchbase.com/browse/CXXCBC-345): Added range scan improvements and resolved concurrency issues ([#525](https://github.com/couchbaselabs/couchbase-cxx-client/pull/525)).
* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Updated config polling to not use session that is not bootstrapped ([#528](https://github.com/couchbaselabs/couchbase-cxx-client/pull/528)).
* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): Updated bootstrap logic to use addresses from the config to bootstrap bucket ([#516](https://github.com/couchbaselabs/couchbase-cxx-client/pull/516)).
* [CXXCBC-450](https://issues.couchbase.com/browse/CXXCBC-450): Updated bootstrap logic to reset bootstrap handler before re-bootstrap ([#524](https://github.com/couchbaselabs/couchbase-cxx-client/pull/524)).

  * We do not want any actions from the old bootstrap handler once the session decided to re-bootstrap. For example, bucket could not be selected, but we might still get configuration responses before socket reset.
* [CXXCBC-452](https://issues.couchbase.com/browse/CXXCBC-452): Updated capabilities and fail fast when selected feature is not available ([#522](https://github.com/couchbaselabs/couchbase-cxx-client/pull/522), [#513](https://github.com/couchbaselabs/couchbase-cxx-client/pull/513)).
* [CXXCBC-431](https://issues.couchbase.com/browse/CXXCBC-431): Added check for history retention bucket capability in collection create/update ([#502](https://github.com/couchbaselabs/couchbase-cxx-client/pull/502), [#505](https://github.com/couchbaselabs/couchbase-cxx-client/pull/505)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query operation to return `feature_not_available` if query preserve expiry is specified but is not supported on the server([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).

##### [](#changes-in-couchbase-c-sdk-1-0-0-dp-12)Changes in Couchbase C++ SDK 1.0.0-dp.12

New features and enhancements

* [CXXCBC-401](https://issues.couchbase.com/browse/CXXCBC-401): Added ping & diagnostics to public API ([#498](https://github.com/couchbaselabs/couchbase-cxx-client/pull/498), [#503](https://github.com/couchbaselabs/couchbase-cxx-client/pull/503)).
* [CXXCBC-346](https://issues.couchbase.com/browse/CXXCBC-346): Support added for `maxTTL` value of -1 for collection 'no expiry' ([#500](https://github.com/couchbaselabs/couchbase-cxx-client/pull/500)).
* [CXXCBC-442](https://issues.couchbase.com/browse/CXXCBC-442): Transcoder support - which was previously limited in the SDK to `JSON` and `RawBinary` transcoders — has now been extended to `raw_json` and `raw_string` transcoders ([#514](https://github.com/couchbaselabs/couchbase-cxx-client/pull/514)).
* [CXXCBC-440](https://issues.couchbase.com/browse/CXXCBC-440): Support added for Scoped Search Indexes ([#512](https://github.com/couchbaselabs/couchbase-cxx-client/pull/512), [#513](https://github.com/couchbaselabs/couchbase-cxx-client/pull/513)).

Fixes

* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Updated config polling to not use session that is not bootstrapped, to reduce network traffic when polling for cluster configuration ([#504](https://github.com/couchbaselabs/couchbase-cxx-client/pull/504), [#528](https://github.com/couchbaselabs/couchbase-cxx-client/pull/528)).
* [CXXCBC-422](https://issues.couchbase.com/browse/CXXCBC-422): Added insufficient credentials error code to common query error code conversion ([#511](https://github.com/couchbaselabs/couchbase-cxx-client/pull/511)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query operation to return `feature_not_available` if query preserve expiry is specified but is not supported on the server([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).
* [CXXCBC-426](https://issues.couchbase.com/browse/CXXCBC-426): Under testing, a get with very large projection was returning fields outside of the projection. This has been fixed, with the projections now set correctly, and the SDK should fall back to a full-doc fetch and return a valid projected result ([#499](https://github.com/couchbaselabs/couchbase-cxx-client/pull/499)).

##### [](#changes-in-couchbase-c-sdk-1-0-0-dp-11)Changes in Couchbase C++ SDK 1.0.0-dp.11

Fixes

* [CXXCBC-404](https://issues.couchbase.com/browse/CXXCBC-404): Fixed `unlock` operations to expose `KV_LOCKED` status as `cas_mismatch` ([#479](https://github.com/couchbaselabs/couchbase-cxx-client/pull/479)).
* [CXXCBC-403](https://issues.couchbase.com/browse/CXXCBC-403): Updated `not_my_vbucket` KV response to allow retries ([#480](https://github.com/couchbaselabs/couchbase-cxx-client/pull/480)).
* [CXXCBC-368](https://issues.couchbase.com/browse/CXXCBC-368): Added support for subscribing to clustermap notifications to speed up failover ([#490](https://github.com/couchbaselabs/couchbase-cxx-client/pull/490)).
* [CXXCBC-419](https://issues.couchbase.com/browse/CXXCBC-419): Updated MCBP protocol parser to start with clean state. Fixes protocol parsing issues when bootstrap sequence is being retried ([#496](https://github.com/couchbaselabs/couchbase-cxx-client/pull/496)).
* [CXXCBC-409](https://issues.couchbase.com/browse/CXXCBC-409): Added handling for `index does not exist` query error ([#492](https://github.com/couchbaselabs/couchbase-cxx-client/pull/492)).
* [CXXCBC-412](https://issues.couchbase.com/browse/CXXCBC-412): Added support for the `document_not_locked` (0x0e) KV status, mapping it to the `errc::key_value::document_not_locked` error code ([#491](https://github.com/couchbaselabs/couchbase-cxx-client/pull/491)).

##### [](#changes-in-couchbase-c-sdk-1-0-0-dp-10)Changes in Couchbase C++ SDK 1.0.0-dp.10

Fixes

* [CXXCBC-383](https://issues.couchbase.com/browse/CXXCBC-383): The `subdoc_doc_too_deep` (0xc4) KV status now returns a\`path\_too\_deep\` error code ([#455](https://github.com/couchbaselabs/couchbase-cxx-client/pull/455)).
* [CXXCBC-382](https://issues.couchbase.com/browse/CXXCBC-382): Fixed `raw_binary_transcoder` so that \`get\`s on binary data are now possible.. ([#459](https://github.com/couchbaselabs/couchbase-cxx-client/pull/459)).
* [CXXCBC-387](https://issues.couchbase.com/browse/CXXCBC-387): Optimising tags for `noop_tracer` and cache formatted `mbcp_session` endpoints ([#461](https://github.com/couchbaselabs/couchbase-cxx-client/pull/461), [#462](https://github.com/couchbaselabs/couchbase-cxx-client/pull/462), [#464](https://github.com/couchbaselabs/couchbase-cxx-client/pull/464))..
* Added more information to diagnose timeouts on NMV responses ([#475](https://github.com/couchbaselabs/couchbase-cxx-client/pull/475)).

#### [](#download-links-9)Download Links

| Platform             | File                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            | [couchbase-3.5.0.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.5.0/couchbase-3.5.0.sha256sum)                            |
| Source Archive       | [couchbase-3.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.0/couchbase-3.5.0.gem)                                        |
| Linux x86\_64        | [couchbase-3.5.0-x86\_64-linux.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.0/couchbase-3.5.0-x86%5F64-linux.gem)           |
| Linux x86\_64 (musl) | [couchbase-3.5.0-x86\_64-linux-musl.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.0/couchbase-3.5.0-x86%5F64-linux-musl.gem) |
| macOS 11 x84\_64     | [couchbase-3.5.0-x86\_64-darwin-20.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.0/couchbase-3.5.0-x86%5F64-darwin-20.gem)   |
| macOS 13 arm64       | [couchbase-3.5.0-arm64-darwin-22.gem](https://packages.couchbase.com/clients/ruby/sdk-3.5.0/couchbase-3.5.0-arm64-darwin-22.gem)        |

## [](#ruby-sdk-3-4-releases)Ruby SDK 3.4 Releases

### [](#version-3-4-5-10-october-2023)Version 3.4.5 (10 October 2023)

```bash
gem install couchbase -v 3.4.5
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.4.5/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.4.4...3.4.5) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.4.5)

#### [](#improvements-4)Improvements

* [RCBC-450](https://issues.couchbase.com/browse/RCBC-450): Subdoc exists was returning `nil` for content. It should now return the value of the content: true if result is success, or false if path-not-found ([#120](http://github.com/couchbase/couchbase-ruby-client/pull/120)).
* [RCBC-453](https://issues.couchbase.com/browse/RCBC-453): Added support history retention in collection and bucket management ([#119](http://github.com/couchbase/couchbase-ruby-client/pull/119)).

#### [](#underlying-c-sdk-core-changes-3)Underlying C++ SDK Core Changes

* [CXXCBC-376](https://issues.couchbase.com/browse/CXXCBC-376): Changed what 'create' and 'update' bucket operations send to the server. Unrequired `BucketSettings` fields are now set to optional, and are not sent unless the settings are explicitly specified. ([#451](https://github.com/couchbaselabs/couchbase-cxx-client/pull/451)).
* [CXXCBC-374](https://issues.couchbase.com/browse/CXXCBC-374): The SDK should now return a 'bucket\_exists' error when the bucket already exists during a 'create' operation. ([#449](https://github.com/couchbaselabs/couchbase-cxx-client/pull/449)).
* [CXXCBC-359](https://issues.couchbase.com/browse/CXXCBC-359): Reduced the default timeout for idle HTTP connections to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures. ([#448](https://github.com/couchbaselabs/couchbase-cxx-client/pull/448)).
* [CXXCBC-367](https://issues.couchbase.com/browse/CXXCBC-367), [CXXCBC-370](https://issues.couchbase.com/browse/CXXCBC-370): Added history retention settings to buckets/collection management ([#446](https://github.com/couchbaselabs/couchbase-cxx-client/pull/446)).
* [CXXCBC-119](https://issues.couchbase.com/browse/CXXCBC-119): Return booleans for subdocument 'exists' operation, instead of error code ([#444](https://github.com/couchbaselabs/couchbase-cxx-client/pull/444), [#452](https://github.com/couchbaselabs/couchbase-cxx-client/pull/452)).
* Detect `collection_not_found` error in `update_collection` response ([#450](https://github.com/couchbaselabs/couchbase-cxx-client/pull/450)).

#### [](#download-links-10)Download Links

| Platform             | Ruby ABI | File                                                                                                                                                |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            |          | [couchbase-3.4.5.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5.sha256sum)                                        |
| Source Archive       |          | [couchbase-3.4.5.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5.gem)                                                    |
| Linux x86\_64        | 3.2.0    | [couchbase-3.4.5-x86\_64-linux-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-linux-3.2.0.gem)           |
| Linux x86\_64        | 3.1.0    | [couchbase-3.4.5-x86\_64-linux-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-linux-3.1.0.gem)           |
| Linux x86\_64        | 3.0.0    | [couchbase-3.4.5-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-linux-3.0.0.gem)           |
| Linux x86\_64 (musl) | 3.2.0    | [couchbase-3.4.5-x86\_64-linux-musl-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-linux-musl-3.2.0.gem) |
| Linux x86\_64 (musl) | 3.1.0    | [couchbase-3.4.5-x86\_64-linux-musl-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-linux-musl-3.1.0.gem) |
| macOS 10.15 x84\_64  | 3.2.0    | [couchbase-3.4.5-x86\_64-darwin-19-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-darwin-19-3.2.0.gem)   |
| macOS 10.15 x84\_64  | 3.0.0    | [couchbase-3.4.5-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-darwin-19-3.0.0.gem)   |
| macOS 11 x84\_64     | 3.2.0    | [couchbase-3.4.5-x86\_64-darwin-20-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-darwin-20-3.2.0.gem)   |
| macOS 11 x84\_64     | 3.1.0    | [couchbase-3.4.5-x86\_64-darwin-20-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-darwin-20-3.1.0.gem)   |
| macOS 11 x84\_64     | 3.0.0    | [couchbase-3.4.5-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-x86%5F64-darwin-20-3.0.0.gem)   |
| macOS 11 M1          | 3.2.0    | [couchbase-3.4.5-arm64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.5/couchbase-3.4.5-arm64-darwin-20-3.0.0.gem)        |

### [](#version-3-4-4-21-august-2023)Version 3.4.4 (21 August 2023)

```bash
gem install couchbase -v 3.4.4
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.4.4/index.html) | [Full Changelog](https://github.com/couchbase/couchbase-ruby-client/compare/3.4.3...3.4.4) | [Rubygems](https://rubygems.org/gems/couchbase/versions/3.4.4)

#### [](#improvements-5)Improvements

* [RCBC-441](https://issues.couchbase.com/browse/RCBC-441) interpret Integer as milliseconds in duration context ([#110](http://github.com/couchbase/couchbase-ruby-client/pull/110), [#111](http://github.com/couchbase/couchbase-ruby-client/pull/111)).
* [RCBC-442](https://issues.couchbase.com/browse/RCBC-442) Support query with Read from Replica ([#112](http://github.com/couchbase/couchbase-ruby-client/pull/112)).
* [RCBC-391](https://issues.couchbase.com/browse/RCBC-391) SDK Support for Native KV Range Scans ([#113](http://github.com/couchbase/couchbase-ruby-client/pull/113), [#117](http://github.com/couchbase/couchbase-ruby-client/pull/117)).
* [RCBC-443](https://issues.couchbase.com/browse/RCBC-443) Support for Subdocument Read from Replica ([#116](http://github.com/couchbase/couchbase-ruby-client/pull/116)).
* [RCBC-451](https://issues.couchbase.com/browse/RCBC-451), [RCBC-451](https://issues.couchbase.com/browse/RCBC-452): Expose any specific `lookup_in` spec errors ([#118](http://github.com/couchbase/couchbase-ruby-client/pull/118)).

#### [](#underlying-c-sdk-core-changes-4)Underlying C++ SDK Core Changes

* [CXXCBC-333](https://issues.couchbase.com/browse/CXXCBC-333): Fixed parsing 'resolv.conf' on Linux ([#416](https://github.com/couchbaselabs/couchbase-cxx-client/pull/416)).

  * The library might not ignore trailing characters when reading nameserver address from the file.
* [CXXCBC-335](https://issues.couchbase.com/browse/CXXCBC-335): Now logging connection options for visibility ([#417](https://github.com/couchbaselabs/couchbase-cxx-client/pull/417)).
* [CXXCBC-343](https://issues.couchbase.com/browse/CXXCBC-343): Continue bootsrap if DNS-SRV resolution fails ([#422](https://github.com/couchbaselabs/couchbase-cxx-client/pull/422)).
* [CXXCBC-242](https://issues.couchbase.com/browse/CXXCBC-242): SDK Support for Native KV Range Scans ([#419](https://github.com/couchbaselabs/couchbase-cxx-client/pull/419), [#423](https://github.com/couchbaselabs/couchbase-cxx-client/pull/423), [#424](https://github.com/couchbaselabs/couchbase-cxx-client/pull/424), [#426](https://github.com/couchbaselabs/couchbase-cxx-client/pull/426), [#428](https://github.com/couchbaselabs/couchbase-cxx-client/pull/428), [#431](https://github.com/couchbaselabs/couchbase-cxx-client/pull/431), [#432](https://github.com/couchbaselabs/couchbase-cxx-client/pull/432), [#433](https://github.com/couchbaselabs/couchbase-cxx-client/pull/433), [#434](https://github.com/couchbaselabs/couchbase-cxx-client/pull/434)).
* [CXXCBC-339](https://issues.couchbase.com/browse/CXXCBC-339): Disable older TLS protocols ([#418](https://github.com/couchbaselabs/couchbase-cxx-client/pull/418)).
* [CXXCBC-346](https://issues.couchbase.com/browse/CXXCBC-346): Protocol communication can now be logged in a separate file ([#425](https://github.com/couchbaselabs/couchbase-cxx-client/pull/425)).  
```ruby  
Couchbase::Backend.enable_protocol_logger_to_save_network_traffic_to_file("/tmp/cb.log")  
```
* [CXXCBC-350](https://issues.couchbase.com/browse/CXXCBC-350): Collection ID was resolved on a per-request basis — which could result in situations where results from a single scan can originate from more than one collection. This could happen if a collection was dropped and then immediately recreated with the same name. We now resolve collection ID before performing any scan operations ([#433](https://github.com/couchbaselabs/couchbase-cxx-client/pull/433)).

#### [](#download-links-11)Download Links

| Platform             | Ruby ABI | File                                                                                                                                                |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            |          | [couchbase-3.4.4.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4.sha256sum)                                        |
| Source Archive       |          | [couchbase-3.4.4.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4.gem)                                                    |
| Linux x86\_64        | 3.2.0    | [couchbase-3.4.4-x86\_64-linux-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-linux-3.2.0.gem)           |
| Linux x86\_64        | 3.1.0    | [couchbase-3.4.4-x86\_64-linux-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-linux-3.1.0.gem)           |
| Linux x86\_64        | 3.0.0    | [couchbase-3.4.4-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-linux-3.0.0.gem)           |
| Linux x86\_64 (musl) | 3.2.0    | [couchbase-3.4.4-x86\_64-linux-musl-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-linux-musl-3.2.0.gem) |
| Linux x86\_64 (musl) | 3.1.0    | [couchbase-3.4.4-x86\_64-linux-musl-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-linux-musl-3.1.0.gem) |
| Linux x86\_64 (musl) | 3.0.0    | [couchbase-3.4.4-x86\_64-linux-musl-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-linux-musl-3.0.0.gem) |
| macOS 10.15 x84\_64  | 3.2.0    | [couchbase-3.4.4-x86\_64-darwin-19-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-darwin-19-3.2.0.gem)   |
| macOS 10.15 x84\_64  | 3.0.0    | [couchbase-3.4.4-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-darwin-19-3.0.0.gem)   |
| macOS 11 x84\_64     | 3.2.0    | [couchbase-3.4.4-x86\_64-darwin-20-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-darwin-20-3.2.0.gem)   |
| macOS 11 x84\_64     | 3.1.0    | [couchbase-3.4.4-x86\_64-darwin-20-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-darwin-20-3.1.0.gem)   |
| macOS 11 x84\_64     | 3.0.0    | [couchbase-3.4.4-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-x86%5F64-darwin-20-3.0.0.gem)   |
| macOS 11 M1          | 3.2.0    | [couchbase-3.4.4-arm64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.4/couchbase-3.4.4-arm64-darwin-20-3.0.0.gem)        |

### [](#version-3-4-3-17-may-2023)Version 3.4.3 (17 May 2023)

```bash
gem install couchbase -v 3.4.3
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.4.3/index.html)

#### [](#improvements-6)Improvements

* [RCBC-420](https://issues.couchbase.com/browse/RCBC-420): Implemented support for `RawJsonTranscoder`, `RawBinaryTranscoder`, and `RawStringTranscoder`, and checking flags when decoding document content ([#93](https://github.com/couchbase/couchbase-ruby-client/pull/93)).
* [RCBC-427](https://issues.couchbase.com/browse/RCBC-427): Add missing query index management options — `scope_name`, `collection_name`, and `index_name` for `#create_primary` method. Replaced `ArgumentError` with `InvalidArgument` error when `scope_name` and `collection_name` are used in the CollectionQueryIndexManager ([#92](https://github.com/couchbase/couchbase-ruby-client/pull/92)).
* [RCBC-436](https://issues.couchbase.com/browse/RCBC-436): To support LDAP authentication, always use PLAIN SASL mechanism with TLS connections ([#103](https://github.com/couchbase/couchbase-ruby-client/pull/103), [CXXCBC-296](https://issues.couchbase.com/browse/CXXCBC-296)).
* Fix the durability level always being set to `none` in the C++ core ([#99](https://github.com/couchbase/couchbase-ruby-client/pull/99)).
* Added constructor for `SearchRowLocation`([#95](https://github.com/couchbase/couchbase-ruby-client/pull/95)).
* Changed `attr` to `attr_reader`([#104](https://github.com/couchbase/couchbase-ruby-client/pull/104)).

#### [](#underlying-c-sdk-core-changes-5)Underlying C++ SDK Core Changes

* [CXXCBC-324](https://issues.couchbase.com/browse/CXXCBC-324): Port and network name now checked on session restart, improving performance during rebalance ([#401](https://github.com/couchbaselabs/couchbase-cxx-client/pull/401)).
* [CXXCBC-323](https://issues.couchbase.com/browse/CXXCBC-323): `bootstrap_timeout` and `resolve_timeout` can now be used in the connection string ([#400](https://github.com/couchbaselabs/couchbase-cxx-client/pull/400)).
* [CXXCBC-327](https://issues.couchbase.com/browse/CXXCBC-327): Bundled Mozilla certificates with the library ([#405](https://github.com/couchbaselabs/couchbase-cxx-client/pull/405), [#408](https://github.com/couchbaselabs/couchbase-cxx-client/pull/408)). Source: <https://curl.se/docs/caextract.html>. Use the `disable_mozilla_ca_certificates` connection string option to disable the bundled certificates. Use the following script to inspect the certificates' metadata:  
```ruby  
Couchbase::BUILD_INFO[:cxx_client].select{|k, _| k =~ /mozilla/}  
# =>  
# {:mozilla_ca_bundle_date=>"Tue Jan 10 04:12:06 2023 GMT",  
#  :mozilla_ca_bundle_embedded=>true,  
#  :mozilla_ca_bundle_sha256=>"fb1ecd641d0a02c01bc9036d513cb658bbda62a75e246bedbc01764560a639f0",  
#  :mozilla_ca_bundle_size=>137}  
```
* Introduced connection string option `dump_configuration` for debugging ([#398](https://github.com/couchbaselabs/couchbase-cxx-client/pull/398)). It logs cluster configuration at trace level.

#### [](#download-links-12)Download Links

| Platform             | Ruby ABI | File                                                                                                                                                |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            |          | [couchbase-3.4.3.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3.sha256sum)                                        |
| Source Archive       |          | [couchbase-3.4.3.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3.gem)                                                    |
| Linux x86\_64        | 3.2.0    | [couchbase-3.4.3-x86\_64-linux-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-linux-3.2.0.gem)           |
| Linux x86\_64        | 3.1.0    | [couchbase-3.4.3-x86\_64-linux-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-linux-3.1.0.gem)           |
| Linux x86\_64        | 3.0.0    | [couchbase-3.4.3-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-linux-3.0.0.gem)           |
| Linux x86\_64 (musl) | 3.2.0    | [couchbase-3.4.3-x86\_64-linux-musl-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-linux-musl-3.2.0.gem) |
| Linux x86\_64 (musl) | 3.1.0    | [couchbase-3.4.3-x86\_64-linux-musl-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-linux-musl-3.1.0.gem) |
| Linux x86\_64 (musl) | 3.0.0    | [couchbase-3.4.3-x86\_64-linux-musl-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-linux-musl-3.0.0.gem) |
| macOS 10.15 x84\_64  | 3.2.0    | [couchbase-3.4.3-x86\_64-darwin-19-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-darwin-19-3.2.0.gem)   |
| macOS 10.15 x84\_64  | 3.0.0    | [couchbase-3.4.3-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-darwin-19-3.0.0.gem)   |
| macOS 11 x84\_64     | 3.2.0    | [couchbase-3.4.3-x86\_64-darwin-20-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-darwin-20-3.2.0.gem)   |
| macOS 11 x84\_64     | 3.1.0    | [couchbase-3.4.3-x86\_64-darwin-20-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-darwin-20-3.1.0.gem)   |
| macOS 11 x84\_64     | 3.0.0    | [couchbase-3.4.3-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-x86%5F64-darwin-20-3.0.0.gem)   |
| macOS 11 M1          | 3.2.0    | [couchbase-3.4.3-arm64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.3/couchbase-3.4.3-arm64-darwin-20-3.0.0.gem)        |

### [](#version-3-4-2-12-april-2023)Version 3.4.2 (12 April 2023)

```bash
gem install couchbase -v 3.4.2
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.4.2/index.html)

#### [](#improvements-7)Improvements

* [RCBC-419](https://issues.couchbase.com/browse/RCBC-419): Accept `Couchbase::Configuration` object on `Couchbase::Cluster.connect`([#85](https://github.com/couchbase/couchbase-ruby-client/pull/85)).
* [RCBC-418](https://issues.couchbase.com/browse/RCBC-418): Add durability to append and prepend options ([#88](https://github.com/couchbase/couchbase-ruby-client/pull/88)).
* [RCBC-422](https://issues.couchbase.com/browse/RCBC-422): Cleanup search options ([#89](https://github.com/couchbase/couchbase-ruby-client/pull/89)).

#### [](#underlying-c-sdk-core-changes-6)Underlying C++ SDK Core Changes

* [CXXCBC-31](https://issues.couchbase.com/browse/CXXCBC-31): Allow the use of schemaless connection strings (e.g. `"cb1.example.com,cb2.example.com"`) ([#394](https://github.com/couchbaselabs/couchbase-cxx-client/pull/395)).
* [CXXCBC-318](https://issues.couchbase.com/browse/CXXCBC-318): Always try TCP if UDP fails in DNS-SRV resolver ([#390](https://github.com/couchbaselabs/couchbase-cxx-client/pull/390)).

#### [](#download-links-13)Download Links

| Platform             | Ruby ABI | File                                                                                                                                                |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            |          | [couchbase-3.4.2.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2.sha256sum)                                        |
| Source Archive       |          | [couchbase-3.4.2.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2.gem)                                                    |
| Linux x86\_64        | 3.2.0    | [couchbase-3.4.2-x86\_64-linux-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-linux-3.2.0.gem)           |
| Linux x86\_64        | 3.1.0    | [couchbase-3.4.2-x86\_64-linux-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-linux-3.1.0.gem)           |
| Linux x86\_64        | 3.0.0    | [couchbase-3.4.2-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-linux-3.0.0.gem)           |
| Linux x86\_64 (musl) | 3.2.0    | [couchbase-3.4.2-x86\_64-linux-musl-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-linux-musl-3.2.0.gem) |
| Linux x86\_64 (musl) | 3.1.0    | [couchbase-3.4.2-x86\_64-linux-musl-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-linux-musl-3.1.0.gem) |
| Linux x86\_64 (musl) | 3.0.0    | [couchbase-3.4.2-x86\_64-linux-musl-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-linux-musl-3.0.0.gem) |
| macOS 10.15 x84\_64  | 3.2.0    | [couchbase-3.4.2-x86\_64-darwin-19-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-darwin-19-3.2.0.gem)   |
| macOS 10.15 x84\_64  | 3.0.0    | [couchbase-3.4.2-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-darwin-19-3.0.0.gem)   |
| macOS 11 x84\_64     | 3.2.0    | [couchbase-3.4.2-x86\_64-darwin-20-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-darwin-20-3.2.0.gem)   |
| macOS 11 x84\_64     | 3.1.0    | [couchbase-3.4.2-x86\_64-darwin-20-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-darwin-20-3.1.0.gem)   |
| macOS 11 x84\_64     | 3.0.0    | [couchbase-3.4.2-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-x86%5F64-darwin-20-3.0.0.gem)   |
| macOS 11 M1          | 3.2.0    | [couchbase-3.4.2-arm64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.2/couchbase-3.4.2-arm64-darwin-20-3.0.0.gem)        |

### [](#version-3-4-1-20-march-2023)Version 3.4.1 (20 March 2023)

```bash
gem install couchbase -v 3.4.1
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.4.1/index.html)

#### [](#improvements-8)Improvements

* [RCBC-396](https://issues.couchbase.com/browse/RCBC-396): Query index management is now available on `Collection` class as `Collection#query_indexes`. `scope_name` and `collection_name` in `QueryIndexManager` are now deprected ([#75](https://github.com/couchbase/couchbase-ruby-client/pull/75)).

#### [](#underlying-c-sdk-core-changes-7)Underlying C++ SDK Core Changes

* Improved build with OpenSSL on CentOS 7 ([#382](https://github.com/couchbaselabs/couchbase-cxx-client/pull/382)).
* [CXXCBC-144](https://issues.couchbase.com/browse/CXXCBC-144): Search query on collections no longer requires you to pass in the scope name — it is inferred from the index ([#379](https://github.com/couchbaselabs/couchbase-cxx-client/pull/379)).
* [CXXCBC-145](https://issues.couchbase.com/browse/CXXCBC-145): Search query request, raw option added ([#380](https://github.com/couchbaselabs/couchbase-cxx-client/pull/380)).

#### [](#download-links-14)Download Links

| Platform             | Ruby ABI | File                                                                                                                                                |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            |          | [couchbase-3.4.1.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1.sha256sum)                                        |
| Source Archive       |          | [couchbase-3.4.1.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1.gem)                                                    |
| Linux x86\_64        | 3.2.0    | [couchbase-3.4.1-x86\_64-linux-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-linux-3.2.0.gem)           |
| Linux x86\_64        | 3.1.0    | [couchbase-3.4.1-x86\_64-linux-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-linux-3.1.0.gem)           |
| Linux x86\_64        | 3.0.0    | [couchbase-3.4.1-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-linux-3.0.0.gem)           |
| Linux x86\_64 (musl) | 3.2.0    | [couchbase-3.4.1-x86\_64-linux-musl-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-linux-musl-3.2.0.gem) |
| Linux x86\_64 (musl) | 3.1.0    | [couchbase-3.4.1-x86\_64-linux-musl-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-linux-musl-3.1.0.gem) |
| Linux x86\_64 (musl) | 3.0.0    | [couchbase-3.4.1-x86\_64-linux-musl-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-linux-musl-3.0.0.gem) |
| macOS 10.15 x84\_64  | 3.2.0    | [couchbase-3.4.1-x86\_64-darwin-19-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-darwin-19-3.2.0.gem)   |
| macOS 10.15 x84\_64  | 3.0.0    | [couchbase-3.4.1-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-darwin-19-3.0.0.gem)   |
| macOS 11 x84\_64     | 3.2.0    | [couchbase-3.4.1-x86\_64-darwin-20-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-darwin-20-3.2.0.gem)   |
| macOS 11 x84\_64     | 3.1.0    | [couchbase-3.4.1-x86\_64-darwin-20-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-darwin-20-3.1.0.gem)   |
| macOS 11 x84\_64     | 3.0.0    | [couchbase-3.4.1-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-x86%5F64-darwin-20-3.0.0.gem)   |
| macOS 11 M1          | 3.2.0    | [couchbase-3.4.1-arm64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.1/couchbase-3.4.1-arm64-darwin-20-3.0.0.gem)        |

### [](#version-3-4-0-19-february-2023)Version 3.4.0 (19 February 2023)

```bash
gem install couchbase -v 3.4.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.4.0/index.html)

#### [](#improvements-9)Improvements

* [RCBC-378](https://issues.couchbase.com/browse/RCBC-378): Implement change password for `Management::User` class. ([#65](https://github.com/couchbase/couchbase-ruby-client/pull/65))
* [RCBC-388](https://issues.couchbase.com/browse/RCBC-388): Add Configuration Profiles. At the moment one profile is defined `"wan_development"`, and it could be applied using `Options::Cluster#apply_profile`. ([#55](https://github.com/couchbase/couchbase-ruby-client/pull/55))
* [RCBC-263](https://issues.couchbase.com/browse/RCBC-263): Implement legacy durability. See options `:persist_to` and `:replicate_to` of mutations. ([#49](https://github.com/couchbase/couchbase-ruby-client/pull/49))
* [RCBC-387](https://issues.couchbase.com/browse/RCBC-387): Implement replica reads with `Collection#get_any_replica` and `Couchbase#get_all_replicas` ([#48](https://github.com/couchbase/couchbase-ruby-client/pull/48))
* [RCBC-375](https://issues.couchbase.com/browse/RCBC-375): Implement log forwarding. See documentation of method `Couchbase.set_logger` and classes `Couchbase::Utils::GenericLoggerAdapter`, `Couchbase::Utils::GenericLoggerAdapter` ([#45](https://github.com/couchbase/couchbase-ruby-client/pull/45))
* [RCBC-371](https://issues.couchbase.com/browse/RCBC-371): Return id for `*_multi` results. ([#40](https://github.com/couchbase/couchbase-ruby-client/pull/40))
* [RCBC-393](https://issues.couchbase.com/browse/RCBC-393): Fix type conversion for query metrics. ([#62](https://github.com/couchbase/couchbase-ruby-client/pull/62))
* [RCBC-398](https://issues.couchbase.com/browse/RCBC-398): Add `ClusterRegistry` to allow custom connection string handlers. ([#68](https://github.com/couchbase/couchbase-ruby-client/pull/68))
* [RCBC-366](https://issues.couchbase.com/browse/RCBC-366): Allow to override default timeouts through `Options::Cluster` ([#37](https://github.com/couchbase/couchbase-ruby-client/pull/37))
* [RCBC-399](https://issues.couchbase.com/browse/RCBC-399): Add default options objects as class constants. ([#69](https://github.com/couchbase/couchbase-ruby-client/pull/69))

#### [](#underlying-c-sdk-core)Underlying C++ SDK Core

#### [](#notable-changes-in-c-sdk-1-0-0-dp-4)Notable Changes in C++ SDK 1.0.0-dp.4

* [CXXCBC-275](https://issues.couchbase.com/browse/CXXCBC-275): Update implementation query context fields passed to the server. In future versions of the server versions it will become mandatory to specify context of the statement (bucket, scope and collection). This change ensures that both future and current server releases supported transparently.
* [CXXCBC-296](https://issues.couchbase.com/browse/CXXCBC-296): Force PLAIN SASL auth if TLS enabled. Using SCRAM SASL mechanisms over TLS protocol is unnecesary complication, that slows down initial connection bootstrap and potentially limits server ability to improve security and evolve credentials management.
* [CXXCBC-295](https://issues.couchbase.com/browse/CXXCBC-295): The `get with projections` opration should not fail if one of the the paths is missing in the document, because the semantics is "get the partial document" and not "get individual fields" like in `lookup_in` operation.
* [CXXCBC-294](https://issues.couchbase.com/browse/CXXCBC-294): In the Public API, if `get` operation requested to return expiry time, zero expiry should not be interpreted as absolute expiry timestamp (zero seconds from UNIX epoch), but rather as absense of the expiry.
* [CXXCBC-291](https://issues.couchbase.com/browse/CXXCBC-291): Allow to disable mutation tokens for Key/Value mutations (use `enable_mutation_tokens` in connection string).
* Resource management and performance improvements:

  * Fix tracer and meter ref-counting ([#370](https://github.com/couchbaselabs/couchbase-cxx-client/pull/370))
  * Replace `minstd_rand` with `mt19937_64`, as it gives less collisions ([#356](https://github.com/couchbaselabs/couchbase-cxx-client/pull/356))
  * [CXXCBC-285](https://issues.couchbase.com/browse/CXXCBC-285): Write to sockets from IO threads, to eliminate potential race conditions. ([#348](https://github.com/couchbaselabs/couchbase-cxx-client/pull/348))
  * Eliminate looping transform in `mcbp_parser::next` ([#347](https://github.com/couchbaselabs/couchbase-cxx-client/pull/347))
  * [CXXCBC-205](https://issues.couchbase.com/browse/CXXCBC-295): Use thread-local UUID generator ([#340](https://github.com/couchbaselabs/couchbase-cxx-client/pull/340))
  * [CXXCBC-293](https://issues.couchbase.com/browse/CXXCBC-293): Performance improvements:

    * Speed up UUID serialization to string ([#346](https://github.com/couchbaselabs/couchbase-cxx-client/pull/346))
    * Don’t allow to copy `mcbp_message` objects ([#345](https://github.com/couchbaselabs/couchbase-cxx-client/pull/345))
    * Avoid extra allocation and initialization ([#344](https://github.com/couchbaselabs/couchbase-cxx-client/pull/344))
* Build system fixes:

  * Fix build with gcc-13 ([#372](https://github.com/couchbaselabs/couchbase-cxx-client/pull/372))
  * Fix gcc 12 issue ([#367](https://github.com/couchbaselabs/couchbase-cxx-client/pull/367))
* Enhancements:

  * Include bucketless KV service when ping is requested. ([#339](https://github.com/couchbaselabs/couchbase-cxx-client/pull/339))
  * Include OS name in SDK identifier ([#349](https://github.com/couchbaselabs/couchbase-cxx-client/pull/349))

#### [](#notable-changes-in-c-sdk-1-0-0-dp-3)Notable changes in C++ SDK 1.0.0-dp.3

* [CXXCBC-276](https://issues.couchbase.com/CXXCBC-276): Use interval from the options for config poll, which previous was hard-coded to 2.5 seconds. ([#336](https://github.com/couchbaselabs/couchbase-cxx-client/pull/336))

#### [](#notable-changes-in-c-sdk-1-0-0-dp-2)Notable changes in C++ SDK 1.0.0-dp.2

* [CXXCBC-242](https://issues.couchbase.com/browse/CXXCBC-242): Drain waiting commands list on MCBP session close ([#321](https://github.com/couchbaselabs/couchbase-cxx-client/pull/321))
* [CXXCBC-271](https://issues.couchbase.com/browse/CXXCBC-271): Fix `get_all_replicas` behaviour: do not propagate error if result set is not empty, while the last response has failed. ([#322](https://github.com/couchbaselabs/couchbase-cxx-client/pull/322))

#### [](#notable-changes-in-c-sdk-1-0-0-dp-1)Notable changes in C++ SDK 1.0.0-dp.1

* [CXXCBC-142](https://issues.couchbase.com/browse/CXXCBC-142): Update SRV resolution for Windows ([#303](https://github.com/couchbaselabs/couchbase-cxx-client/pull/303))
* [CXXCBC-172](https://issues.couchbase.com/browse/CXXCBC-172): Refresh DNS SRV when cluster uncontactable ([#275](https://github.com/couchbaselabs/couchbase-cxx-client/pull/275), [#290](https://github.com/couchbaselabs/couchbase-cxx-client/pull/290))
* [CXXCBC-234](https://issues.couchbase.com/browse/CXXCBC-234): Error message for bucket hibernation and update error message for authentication\_failure. ([#280](https://github.com/couchbaselabs/couchbase-cxx-client/pull/290), [#285](https://github.com/couchbaselabs/couchbase-cxx-client/pull/285))
* [CXXCBC-235](https://issues.couchbase.com/browse/CXXCBC-235): Load system CAs when the trust certificate is not provided and do not fail if trust certificate is not specified ([#283](https://github.com/couchbaselabs/couchbase-cxx-client/pull/283), [#281](https://github.com/couchbaselabs/couchbase-cxx-client/pull/281))
* [CXXCBC-245](https://issues.couchbase.com/browse/CXXCBC-245): Fix encoding of durability frame ([#277](https://github.com/couchbaselabs/couchbase-cxx-client/pull/277))
* [CXXCBC-246](https://issues.couchbase.com/browse/CXXCBC-246): Convert `not_stored` code to `document_exists` ([#278](https://github.com/couchbaselabs/couchbase-cxx-client/pull/278))
* [CXXCBC-251](https://issues.couchbase.com/browse/CXXCBC-251): Fix snappy decompression for `get_replica` ([#296](https://github.com/couchbaselabs/couchbase-cxx-client/pull/296))
* [CXXCBC-253](https://issues.couchbase.com/browse/CXXCBC-253): `query_options` not setting `scope_qualifier` ([#300](https://github.com/couchbaselabs/couchbase-cxx-client/pull/300))
* [SDKQE-2761](https://issues.couchbase.com/browse/SDKQE-2761): Fix failures in serverless mode ([#274](https://github.com/couchbaselabs/couchbase-cxx-client/pull/274))
* Don’t log expected warnings in DNS resolver ([#294](https://github.com/couchbaselabs/couchbase-cxx-client/pull/294))

##### [](#resource-management-and-performance-fixes)Resource management and performance fixes

* [CXXCBC-225](https://issues.couchbase.com/browse/CXXCBC-225): Don’t throw exceptions when socket options cannot be set ([#270](https://github.com/couchbaselabs/couchbase-cxx-client/pull/270))

##### [](#build-system-fixes)Build system fixes

* Move away from `reinterpret_pointer_cast<>` for MacOS build issue ([#288](https://github.com/couchbaselabs/couchbase-cxx-client/pull/288))
* Improve OpenSSL detection on Windows ([#272](https://github.com/couchbaselabs/couchbase-cxx-client/pull/272))

#### [](#notable-changes-in-c-sdk-1-0-0-beta-3)Notable changes in C++ SDK 1.0.0-beta.3

* [CXXCBC-221](https://issues.couchbase.com/browse/CXXCBC-221): Support for configuration profiles ([#268](https://github.com/couchbaselabs/couchbase-cxx-client/pull/268))
* [CXXCBC-218](https://issues.couchbase.com/browse/CXXCBC-218): allow to check if subdoc result field has value ([#263](https://github.com/couchbaselabs/couchbase-cxx-client/pull/263))
* [CXXCBC-199](https://issues.couchbase.com/browse/CXXCBC-199): Always set `kv_collection_outdated` retry reason on unknown collection error ([#223](https://github.com/couchbaselabs/couchbase-cxx-client/pull/223))
* [CXXCBC-203](https://issues.couchbase.com/browse/CXXCBC-203): disable clustermap nofication by default ([#233](https://github.com/couchbaselabs/couchbase-cxx-client/pull/233))
* [CXXCBC-159](https://issues.couchbase.com/browse/CXXCBC-159): Increment/decrement should not have `preserve_expiry` ([#201](https://github.com/couchbaselabs/couchbase-cxx-client/pull/201))
* [CXXCBC-55](https://issues.couchbase.com/browse/CXXCBC-55): External Tracing and Metrics support with OpenTelemetry support ([#228](https://github.com/couchbaselabs/couchbase-cxx-client/pull/228), [#231](https://github.com/couchbaselabs/couchbase-cxx-client/pull/231))
* [CXXCBC-54](https://issues.couchbase.com/browse/CXXCBC-54): Add log forwarding ([#206](https://github.com/couchbaselabs/couchbase-cxx-client/pull/206))

##### [](#bug-fixes-3)Bug fixes

* [CXXCBC-134](https://issues.couchbase.com/browse/CXXCBC-134): Close http\_session before conecting to next endpoint ([#213](https://github.com/couchbaselabs/couchbase-cxx-client/pull/213))
* [CXXCBC-179](https://issues.couchbase.com/browse/CXXCBC-179): fix parsing responses with chunked meta trailer ([#191](https://github.com/couchbaselabs/couchbase-cxx-client/pull/191))
* [CXXCBC-170](https://issues.couchbase.com/browse/CXXCBC-170): add extra check for missing CA for TLS connections ([#197](https://github.com/couchbaselabs/couchbase-cxx-client/pull/197))
* [CXXCBC-182](https://issues.couchbase.com/browse/CXXCBC-182): add extra check for keywords in query index fields ([#196](https://github.com/couchbaselabs/couchbase-cxx-client/pull/196))
* [CXXCBC-173](https://issues.couchbase.com/browse/CXXCBC-173): complete streaming lexer even if pointer didn’t match ([#195](https://github.com/couchbaselabs/couchbase-cxx-client/pull/195))
* [CXXCBC-212](https://issues.couchbase.com/browse/CXXCBC-212): reprepare and retry query on 4040, 4050 and 4070 ([#257](https://github.com/couchbaselabs/couchbase-cxx-client/pull/257))
* [CXXCBC-174](https://issues.couchbase.com/browse/CXXCBC-174): reduce scope of the http request lock ([#259](https://github.com/couchbaselabs/couchbase-cxx-client/pull/259))
* [CXXCBC-176](https://issues.couchbase.com/browse/CXXCBC-176): ignore 'is\_primary' for named primary indexes when dropping ([#202](https://github.com/couchbaselabs/couchbase-cxx-client/pull/202))
* Return subdocument error context from future-based subdoc methods ([#258](https://github.com/couchbaselabs/couchbase-cxx-client/pull/258))

#### [](#download-links-15)Download Links

| Platform             | Ruby ABI | File                                                                                                                                                |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums            |          | [couchbase-3.4.0.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0.sha256sum)                                        |
| Source Archive       |          | [couchbase-3.4.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0.gem)                                                    |
| Linux x86\_64        | 3.2.0    | [couchbase-3.4.0-x86\_64-linux-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-linux-3.2.0.gem)           |
| Linux x86\_64        | 3.1.0    | [couchbase-3.4.0-x86\_64-linux-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-linux-3.1.0.gem)           |
| Linux x86\_64        | 3.0.0    | [couchbase-3.4.0-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-linux-3.0.0.gem)           |
| Linux x86\_64 (musl) | 3.2.0    | [couchbase-3.4.0-x86\_64-linux-musl-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-linux-musl-3.2.0.gem) |
| Linux x86\_64 (musl) | 3.1.0    | [couchbase-3.4.0-x86\_64-linux-musl-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-linux-musl-3.1.0.gem) |
| Linux x86\_64 (musl) | 3.0.0    | [couchbase-3.4.0-x86\_64-linux-musl-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-linux-musl-3.0.0.gem) |
| macOS 10.15 x84\_64  | 3.2.0    | [couchbase-3.4.0-x86\_64-darwin-19-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-darwin-19-3.2.0.gem)   |
| macOS 10.15 x84\_64  | 3.0.0    | [couchbase-3.4.0-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-darwin-19-3.0.0.gem)   |
| macOS 11 x84\_64     | 3.2.0    | [couchbase-3.4.0-x86\_64-darwin-20-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-darwin-20-3.2.0.gem)   |
| macOS 11 x84\_64     | 3.1.0    | [couchbase-3.4.0-x86\_64-darwin-20-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-darwin-20-3.1.0.gem)   |
| macOS 11 x84\_64     | 3.0.0    | [couchbase-3.4.0-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-x86%5F64-darwin-20-3.0.0.gem)   |
| macOS 11 M1          | 3.2.0    | [couchbase-3.4.0-arm64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.4.0/couchbase-3.4.0-arm64-darwin-20-3.0.0.gem)        |

## [](#ruby-sdk-3-3-releases)Ruby SDK 3.3 Releases

### [](#version-3-3-0-5-may-2022)Version 3.3.0 (5 May 2022)

This is the first GA release of the 3.3 series.

```bash
gem install couchbase -v 3.3.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.3.0/index.html)

Improvements:

* [RCBC-338](https://issues.couchbase.com/browse/RCBC-338): Added new options for the search API. You can now add the `operator` and `include_locations` properties to all search queries.
* [RCBC-358](https://issues.couchbase.com/browse/RCBC-358), [RCBC-346](https://issues.couchbase.com/browse/RCBC-346): Added new options for the bucket API. The SDK now allows you to configure the custom conflict resolution storage backend for new buckets.
* [RCBC-345](https://issues.couchbase.com/browse/RCBC-345): We now support preserving expiry for the query API.
* [RCBC-343](https://issues.couchbase.com/browse/RCBC-343): SSL peer is now verified by default.
* Added support for Ruby 3.1.
* Dropped support for Ruby 2.5 and 2.6.

Fixes:

* [RCBC-358](https://issues.couchbase.com/browse/RCBC-358): The SDK now initializes search locations only if they are returned by the server.

| Platform            | Ruby ABI | File                                                                                                                                              |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.3.0.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.3.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0.gem)                                                  |
| Linux x86\_64       | 3.1.0    | [couchbase-3.3.0-x86\_64-linux-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-linux-3.1.0.gem)         |
| Linux x86\_64       | 3.0.0    | [couchbase-3.3.0-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-linux-3.0.0.gem)         |
| Linux x86\_64       | 2.7.0    | [couchbase-3.3.0-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-linux-2.7.0.gem)         |
| macOS 10.15 x84\_64 | 3.1.0    | [couchbase-3.3.0-x86\_64-darwin-19-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-darwin-19-3.1.0.gem) |
| macOS 10.15 x84\_64 | 3.0.0    | [couchbase-3.3.0-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-darwin-19-3.0.0.gem) |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.3.0-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 11 x84\_64    | 3.1.0    | [couchbase-3.3.0-x86\_64-darwin-20-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-darwin-20-3.1.0.gem) |
| macOS 11 x84\_64    | 3.0.0    | [couchbase-3.3.0-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-darwin-20-3.0.0.gem) |
| macOS 11 x84\_64    | 2.7.0    | [couchbase-3.3.0-x86\_64-darwin-20-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.3.0/couchbase-3.3.0-x86%5F64-darwin-20-2.7.0.gem) |

## [](#ruby-sdk-3-2-releases)Ruby SDK 3.2 Releases

### [](#version-3-2-0-4-august-2021)Version 3.2.0 (4 August 2021)

This is the first GA release of the 3.2 series.

```bash
gem install couchbase -v 3.2.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.2.0/index.html)

* [RCBC-301](https://issues.couchbase.com/browse/RCBC-301): Implemented metrics. This feature is enabled by default; it can be disabled in the connection string with `enable_metrics=false`, or programmatically:  
```ruby  
options = Cluster::ClusterOptions.new  
options.enable_metrics = false  
```  
Extra options:  
```ruby  
options = Cluster::ClusterOptions.new  
options.metrics_emit_interval = 60_000 # in milliseconds, default 10 minutes  
```
* [RCBC-234](https://issues.couchbase.com/browse/RCBC-234): Implemented tracing. This feature is enabled by default; it can be disabled in the connection string with `enable_tracing=false`, or programmatically:  
```ruby  
options = Cluster::ClusterOptions.new  
options.enable_tracing = false  
```  
Extra options:  
```ruby  
options = Cluster::ClusterOptions.new  
options.orphaned_emit_interval = 600_000 # in milliseconds  
options.orphaned_sample_size = 64  
options.threshold_emit_interval = 600_00 # in milliseconds  
options.threshold_sample_size = 64  
options.key_value_threshold = 500 # in milliseconds  
options.query_threshold = 1_000 # in milliseconds  
options.view_threshold = 1_000 # in milliseconds  
options.search_threshold = 1_000 # in milliseconds  
options.analytics_threshold = 1_000 # in milliseconds  
options.management_threshold = 1_000 # in milliseconds  
```
* [RCBC-318](https://issues.couchbase.com/browse/RCBC-318): Parse and use `revEpoch` field in configuration for improved bucket configuration handling.
* [RCBC-324](https://issues.couchbase.com/browse/RCBC-324): Query error code 13014 is now mapped to an `AuthenticationFailure` exception.
* [RCBC-227](https://issues.couchbase.com/browse/RCBC-227): Remote links for analytics can now be managed from the SDK, enabling connection to an external dataset such as an AWS S3 bucket.
* [RCBC-283](https://issues.couchbase.com/browse/RCBC-283): Added Collections support for Search queries.
* [RCBC-311](https://issues.couchbase.com/browse/RCBC-311): Fixed scope qualifer encoding for analtyics to work with latest decoding.
* Dropped support of Ruby 2.5.
* Many smaller fixes and improvements.

| Platform            | Ruby ABI | File                                                                                                                                              |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.2.0.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.2.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0.gem)                                                  |
| Linux x86\_64       | 3.0.0    | [couchbase-3.2.0-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-linux-3.0.0.gem)         |
| Linux x86\_64       | 2.7.0    | [couchbase-3.2.0-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-linux-2.7.0.gem)         |
| Linux x86\_64       | 2.6.0    | [couchbase-3.2.0-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-linux-2.6.0.gem)         |
| Linux x86\_64       | 2.5.0    | [couchbase-3.2.0-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-linux-2.5.0.gem)         |
| macOS 10.15 x84\_64 | 3.0.0    | [couchbase-3.2.0-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-19-3.0.0.gem) |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.2.0-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.2.0-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-19-2.6.0.gem) |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.2.0-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-19-2.5.0.gem) |
| macOS 11 x84\_64    | 3.0.0    | [couchbase-3.2.0-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-20-3.0.0.gem) |
| macOS 11 x84\_64    | 2.7.0    | [couchbase-3.2.0-x86\_64-darwin-20-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-20-2.7.0.gem) |
| macOS 11 x84\_64    | 2.6.0    | [couchbase-3.2.0-x86\_64-darwin-20-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-20-2.6.0.gem) |
| macOS 11 x84\_64    | 2.5.0    | [couchbase-3.2.0-x86\_64-darwin-20-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-x86%5F64-darwin-20-2.5.0.gem) |
| macOS 11 Universal  | 2.6.0    | [couchbase-3.2.0-universal-darwin-20.gem](https://packages.couchbase.com/clients/ruby/sdk-3.2.0/couchbase-3.2.0-universal-darwin-20.gem)          |

## [](#ruby-sdk-3-1-releases)Ruby SDK 3.1 Releases

### [](#version-3-1-1-8-april-2021)Version 3.1.1 (8 April 2021)

This is the second GA release of 3.1 series.

```bash
gem install couchbase -v 3.1.1
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.1.1/index.html)

* [RCBC-309](https://issues.couchbase.com/browse/RCBC-309): Allow subdocument remove operation with empty path.
* [RCBC-316](https://issues.couchbase.com/browse/RCBC-316): Fix exceptions for collections manager.
* [RCBC-315](https://issues.couchbase.com/browse/RCBC-315): Raise `CasMismatch` exception only when query returns code `12009` with `"CAS mismatch"` in message.
* [RCBC-298](https://issues.couchbase.com/browse/RCBC-298): Support preserving expiration for mutations. `Collection#replace`, `Collection#upsert`, and `Collection#mutate_in` methods now accept new boolean option `preserve_expiry` which determines whether the server will update expiration for existing documents (`false` by default).  
In the following example, the server will not reset expiration if the document already exists, and only use `100` seconds if the document has to be created.  
```ruby  
collection.upsert(doc_id, {answer: 43},  
    Options::Upsert(expiry: 100, preserve_expiry: true))  
```
* [RCBC-317](https://issues.couchbase.com/browse/RCBC-317): Allow to disable snappy compression with `enable_compression=false` in connection string.

| Platform            | Ruby ABI | File                                                                                                                                              |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.1.1.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.1.1.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1.gem)                                                  |
| Linux x86\_64       | 3.0.0    | [couchbase-3.1.1-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-linux-3.0.0.gem)         |
| Linux x86\_64       | 2.7.0    | [couchbase-3.1.1-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-linux-2.7.0.gem)         |
| Linux x86\_64       | 2.6.0    | [couchbase-3.1.1-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-linux-2.6.0.gem)         |
| Linux x86\_64       | 2.5.0    | [couchbase-3.1.1-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-linux-2.5.0.gem)         |
| macOS 10.15 x84\_64 | 3.0.0    | [couchbase-3.1.1-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-19-3.0.0.gem) |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.1.1-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.1.1-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-19-2.6.0.gem) |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.1.1-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-19-2.5.0.gem) |
| macOS 11 x84\_64    | 3.0.0    | [couchbase-3.1.1-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-20-3.0.0.gem) |
| macOS 11 x84\_64    | 2.7.0    | [couchbase-3.1.1-x86\_64-darwin-20-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-20-2.7.0.gem) |
| macOS 11 x84\_64    | 2.6.0    | [couchbase-3.1.1-x86\_64-darwin-20-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-20-2.6.0.gem) |
| macOS 11 x84\_64    | 2.5.0    | [couchbase-3.1.1-x86\_64-darwin-20-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-20-2.5.0.gem) |
| macOS 11 Universal  | 2.6.0    | [couchbase-3.1.1-x86\_64-darwin-20.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.1/couchbase-3.1.1-x86%5F64-darwin-20.gem)             |

### [](#version-3-1-0-24-march-2021)Version 3.1.0 (24 March 2021)

This is the first GA release of 3.1 series.

```bash
gem install couchbase -v 3.1.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.1.0/index.html)

* [RCBC-314](https://issues.couchbase.com/browse/RCBC-314): Fixed class resolution for Analytics at scope level.
* [RCBC-276](https://issues.couchbase.com/browse/RCBC-276): Marked `create_as_deleted` of subdocument API as private.
* [RCBC-287](https://issues.couchbase.com/browse/RCBC-287): Updated URLs of endpoints for Collections management API.
* [RCBC-303](https://issues.couchbase.com/browse/RCBC-303): Deprecated `CollectionManager#get_scope`; instead the application should use `CollectionManager#get_scopes` and iterate/filter the results.
* [RCBC-313](https://issues.couchbase.com/browse/RCBC-313): Send collection name as value on network level for `0xbb` (`GET_COLLECTION_ID`) command.
* [RCBC-302](https://issues.couchbase.com/browse/RCBC-302): Allow to disable configuration push from server (using `enable_clustermap_notification=false` in the connection string).
* [RCBC-307](https://issues.couchbase.com/browse/RCBC-307): Allow to disable unordered execution of commands (using `enable_unordered_execution=false` in the connection string).
* The library does not keep GVL lock durng IO anymore. It releases lock when scheduling a command, and acquires it back once the command is completed. This change allows runtime to use fibers or threads, and do something useful while the operation is in progress.

| Platform            | Ruby ABI | File                                                                                                                                              |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.1.0.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.1.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0.gem)                                                  |
| Linux x86\_64       | 3.0.0    | [couchbase-3.1.0-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-linux-3.0.0.gem)         |
| Linux x86\_64       | 2.7.0    | [couchbase-3.1.0-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-linux-2.7.0.gem)         |
| Linux x86\_64       | 2.6.0    | [couchbase-3.1.0-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-linux-2.6.0.gem)         |
| Linux x86\_64       | 2.5.0    | [couchbase-3.1.0-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-linux-2.5.0.gem)         |
| macOS 10.15 x84\_64 | 3.0.0    | [couchbase-3.1.0-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-19-3.0.0.gem) |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.1.0-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.1.0-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-19-2.6.0.gem) |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.1.0-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-19-2.5.0.gem) |
| macOS 11 x84\_64    | 3.0.0    | [couchbase-3.1.0-x86\_64-darwin-20-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-20-3.0.0.gem) |
| macOS 11 x84\_64    | 2.7.0    | [couchbase-3.1.0-x86\_64-darwin-20-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-20-2.7.0.gem) |
| macOS 11 x84\_64    | 2.6.0    | [couchbase-3.1.0-x86\_64-darwin-20-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-20-2.6.0.gem) |
| macOS 11 x84\_64    | 2.5.0    | [couchbase-3.1.0-x86\_64-darwin-20-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.1.0/couchbase-3.1.0-x86%5F64-darwin-20-2.5.0.gem) |

## [](#ruby-sdk-3-0-releases)Ruby SDK 3.0 Releases

### [](#version-3-0-3-3-february-2021)Version 3.0.3 (3 February 2021)

```bash
gem install couchbase -v 3.0.3
```

This is the fourth GA release of 3.0 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.3/index.html)

* [RCBC-226](https://issues.couchbase.com/browse/RCBC-226): Add minimal durability setting in bucket manager.
* [RCBC-238](https://issues.couchbase.com/browse/RCBC-238): Refactored expiration (TTL) options:

  * It accepts `Time` instance in addition to `Duration` (`#in_seconds`);
  * When `Integer` is passed, it implicitly converts to epoch time to resolve disambiguation.
* [RCBC-291](https://issues.couchbase.com/browse/RCBC-291): Implementation of `ActiveSupport::Cache::Store` interface. To enable it, put the following lines into application configuration section:

```ruby
config.cache_store = :couchbase_store, {
  connection_string: "couchbase://localhost",
  username: "app_cache_user",
  password: "s3cret",
  bucket: "app_cache"
}
```

* [RCBC-292](https://issues.couchbase.com/browse/RCBC-292): Swap bytes in CAS for compatiblity. Now the value of CAS matches the representation in other services (e.g. Query).
* [RCBC-300](https://issues.couchbase.com/browse/RCBC-300): Allow the enforcement of PLAIN SASL mechanism. This is necessary when LDAP authentication is enabled, but the SDK does not use client certification to authenticate.
* [RCBC-237](https://issues.couchbase.com/browse/RCBC-237): Added collections support for analytics. `Scope#analytics_query` automatically sets scope qualifier. Also, it is now possible to provide custom qualifier in the options.
* Status of single operation now accessible on result object of `get_multi`, `upsert_multi`, and `remove_multi` operations.
* Error context objects now accessible on exceptions (via `#context` method).

| Platform            | Ruby ABI | File                                                                                                                                                 |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.0.3.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3.sha256sum)                                         |
| Source Archive      |          | [couchbase-3.0.3.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3.gem)                                                     |
| Linux x86\_64       | 3.0.0    | [couchbase-3.0.3-x86\_64-linux-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-linux-3.0.0.gem)            |
| Linux x86\_64       | 2.7.0    | [couchbase-3.0.3-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-linux-2.7.0.gem)            |
| Linux x86\_64       | 2.6.0    | [couchbase-3.0.3-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-linux-2.6.0.gem)            |
| Linux x86\_64       | 2.5.0    | [couchbase-3.0.3-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-linux-2.5.0.gem)            |
| macOS 11 Universal  | 2.6.0    | [couchbase-3.0.3-universal-darwin-20-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-universal-darwin-20-2.6.0.gem) |
| macOS 10.15 x84\_64 | 3.0.0    | [couchbase-3.0.3-x86\_64-darwin-19-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-19-3.0.0.gem)    |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.0.3-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-19-2.7.0.gem)    |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.0.3-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-19-2.6.0.gem)    |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.0.3-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-19-2.5.0.gem)    |
| macOS 10.13 x84\_64 | 3.0.0    | [couchbase-3.0.3-x86\_64-darwin-17-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-17-3.0.0.gem)    |
| macOS 10.13 x84\_64 | 2.7.0    | [couchbase-3.0.3-x86\_64-darwin-17-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-17-2.7.0.gem)    |
| macOS 10.13 x84\_64 | 2.6.0    | [couchbase-3.0.3-x86\_64-darwin-17-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-17-2.6.0.gem)    |
| macOS 10.13 x84\_64 | 2.5.0    | [couchbase-3.0.3-x86\_64-darwin-17-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.3/couchbase-3.0.3-x86%5F64-darwin-17-2.5.0.gem)    |

### [](#version-3-0-2-3-november-2020)Version 3.0.2 (3 November 2020)

This is the third GA release of 3.0 series.

```bash
gem install couchbase -v 3.0.2
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.2/index.html)

* [RCBC-281](https://issues.couchbase.com/browse/RCBC-281): Implemented batching API for several data operations. (Read docs for [Collection#get\_multi](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.2/Couchbase/Collection.html#get%5Fmulti-instance%5Fmethod), [Collection#upsert\_multi](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.2/Couchbase/Collection.html#upsert%5Fmulti-instance%5Fmethod), and [Collection#remove\_multi](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.2/Couchbase/Collection.html#remove%5Fmulti-instance%5Fmethod)).
* [RCBC-223](https://issues.couchbase.com/browse/RCBC-223), [RCBC-253](https://issues.couchbase.com/browse/RCBC-253): Implemented ping and diagnostics APIs.
* [RCBC-278](https://issues.couchbase.com/browse/RCBC-278): Exposed getter and setter for log level, for example, `Couchbase.log_level = :trace` will switch logger to maximum verbosity. (details in [Couchbase](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.2/Couchbase.html#log%5Flevel=-class%5Fmethod) module documentation).
* [RCBC-277](https://issues.couchbase.com/browse/RCBC-277): Implemented append/prepend for binary collection (more in [BinaryCollection](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.2/Couchbase/BinaryCollection.html) documentation).
* [RCBC-276](https://issues.couchbase.com/browse/RCBC-276): Support for `create_as_deleted` option for `Collection#mutate_in` to create document in tombstone state.
* Build, test, and documentation improvements.

| Platform            | Ruby ABI | File                                                                                                                                              |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.0.2.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.0.2.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2.gem)                                                  |
| Linux x86\_64       | 2.7.0    | [couchbase-3.0.2-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-linux-2.7.0.gem)         |
| Linux x86\_64       | 2.6.0    | [couchbase-3.0.2-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-linux-2.6.0.gem)         |
| Linux x86\_64       | 2.5.0    | [couchbase-3.0.2-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-linux-2.5.0.gem)         |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.0.2-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.0.2-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-darwin-19-2.6.0.gem) |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.0.2-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-darwin-19-2.5.0.gem) |
| macOS 10.13 x84\_64 | 2.7.0    | [couchbase-3.0.2-x86\_64-darwin-17-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-darwin-17-2.7.0.gem) |
| macOS 10.13 x84\_64 | 2.6.0    | [couchbase-3.0.2-x86\_64-darwin-17-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-darwin-17-2.6.0.gem) |
| macOS 10.13 x84\_64 | 2.5.0    | [couchbase-3.0.2-x86\_64-darwin-17-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.2/couchbase-3.0.2-x86%5F64-darwin-17-2.5.0.gem) |

### [](#version-3-0-1-5-october-2020)Version 3.0.1 (5 October 2020)

This is the second GA release.

```bash
gem install couchbase -v 3.0.1
```

* [RCBC-219](https://issues.couchbase.com/browse/RCBC-219), [RCBC-252](https://issues.couchbase.com/browse/RCBC-252): Implemented diagnostics API.
* [RCBC-272](https://issues.couchbase.com/browse/RCBC-272): Allow disabling of scoring in Full-Text Search results.
* [RCBC-229](https://issues.couchbase.com/browse/RCBC-229): Geopolygon Search support.
* [RCBC-271](https://issues.couchbase.com/browse/RCBC-271): Enhanced user management for collections.
* [RCBC-230](https://issues.couchbase.com/browse/RCBC-230): Added query option for flex index.
* [RCBC-233](https://issues.couchbase.com/browse/RCBC-233): Updated eviction policy types (now it covers ephemeral buckets).
* [RCBC-274](https://issues.couchbase.com/browse/RCBC-274): Skip non-kv nodes when switching networks (fixes warnings in Cloud environment).
* [RCBC-266](https://issues.couchbase.com/browse/RCBC-266): Deprecated `GetResult.expiry`.
* Fixed Query prepared statements cache for older servers.
* Build and test system improvements.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.1/index.html)

| Platform            | Ruby ABI | File                                                                                                                                              |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.0.1.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.0.1.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1.gem)                                                  |
| Linux x86\_64       | 2.7.0    | [couchbase-3.0.1-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-linux-2.7.0.gem)         |
| Linux x86\_64       | 2.6.0    | [couchbase-3.0.1-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-linux-2.6.0.gem)         |
| Linux x86\_64       | 2.5.0    | [couchbase-3.0.1-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-linux-2.5.0.gem)         |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.0.1-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.0.1-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-darwin-19-2.6.0.gem) |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.0.1-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-darwin-19-2.5.0.gem) |
| macOS 10.13 x84\_64 | 2.7.0    | [couchbase-3.0.1-x86\_64-darwin-17-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-darwin-17-2.7.0.gem) |
| macOS 10.13 x84\_64 | 2.6.0    | [couchbase-3.0.1-x86\_64-darwin-17-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-darwin-17-2.6.0.gem) |
| macOS 10.13 x84\_64 | 2.5.0    | [couchbase-3.0.1-x86\_64-darwin-17-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.1/couchbase-3.0.1-x86%5F64-darwin-17-2.5.0.gem) |

### [](#version-3-0-0-8-september-2020)Version 3.0.0 (8 September 2020)

This is the first GA release.

```bash
gem install couchbase -v 3.0.0
```

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.0/index.html)

| Platform            | Ruby ABI | File                                                                                                                                              |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.0.0.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.0.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0.gem)                                                  |
| Linux x86\_64       | 2.7.0    | [couchbase-3.0.0-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-linux-2.7.0.gem)         |
| Linux x86\_64       | 2.6.0    | [couchbase-3.0.0-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-linux-2.6.0.gem)         |
| Linux x86\_64       | 2.5.0    | [couchbase-3.0.0-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-linux-2.5.0.gem)         |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.0.0-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.0.0-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-darwin-19-2.6.0.gem) |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.0.0-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-darwin-19-2.5.0.gem) |
| macOS 10.13 x84\_64 | 2.7.0    | [couchbase-3.0.0-x86\_64-darwin-17-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-darwin-17-2.7.0.gem) |
| macOS 10.13 x84\_64 | 2.6.0    | [couchbase-3.0.0-x86\_64-darwin-17-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-darwin-17-2.6.0.gem) |
| macOS 10.13 x84\_64 | 2.5.0    | [couchbase-3.0.0-x86\_64-darwin-17-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0/couchbase-3.0.0-x86%5F64-darwin-17-2.5.0.gem) |

### [](#version-3-0-0-beta-1-7-august-2020)Version 3.0.0.beta.1 (7 August 2020)

This is the first beta release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client-3.0.0.beta.1/index.html)

| Platform            | Ruby ABI | File                                                                                                                                                                   |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums           |          | [couchbase-3.0.0.beta.1.sha256sum](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1.sha256sum)                                      |
| Source Archive      |          | [couchbase-3.0.0.beta.1.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1.gem)                                                  |
| Linux x86\_64       | 2.7.0    | [couchbase-3.0.0.beta.1-x86\_64-linux-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-linux-2.7.0.gem)         |
| Linux x86\_64       | 2.6.0    | [couchbase-3.0.0.beta.1-x86\_64-linux-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-linux-2.6.0.gem)         |
| Linux x86\_64       | 2.5.0    | [couchbase-3.0.0.beta.1-x86\_64-linux-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-linux-2.5.0.gem)         |
| macOS 10.15 x84\_64 | 2.7.0    | [couchbase-3.0.0.beta.1-x86\_64-darwin-19-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-darwin-19-2.7.0.gem) |
| macOS 10.15 x84\_64 | 2.6.0    | [couchbase-3.0.0.beta.1-x86\_64-darwin-19-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-darwin-19-2.6.0.gem) |
| macOS 10.15 x84\_64 | 2.5.0    | [couchbase-3.0.0.beta.1-x86\_64-darwin-19-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-darwin-19-2.5.0.gem) |
| macOS 10.13 x84\_64 | 2.7.0    | [couchbase-3.0.0.beta.1-x86\_64-darwin-17-2.7.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-darwin-17-2.7.0.gem) |
| macOS 10.13 x84\_64 | 2.6.0    | [couchbase-3.0.0.beta.1-x86\_64-darwin-17-2.6.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-darwin-17-2.6.0.gem) |
| macOS 10.13 x84\_64 | 2.5.0    | [couchbase-3.0.0.beta.1-x86\_64-darwin-17-2.5.0.gem](https://packages.couchbase.com/clients/ruby/sdk-3.0.0.beta.1/couchbase-3.0.0.beta.1-x86%5F64-darwin-17-2.5.0.gem) |

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).