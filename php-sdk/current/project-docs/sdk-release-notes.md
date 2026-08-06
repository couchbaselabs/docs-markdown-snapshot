---
title: SDK Release Notes
description: Release notes for the Couchbase PHP Client.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.5/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:php-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes for the Couchbase PHP Client. 

These pages cover the 4.x versions of the Couchbase PHP SDK.

For download instructions, see the [installation page](sdk-full-installation.md).

> [!TIP]
> PECL Packages
> 
> The download packages given on the [Release Notes page](#latest-release) are officially supported. The source tarball found on <https://pecl.php.net/> at <https://pecl.php.net/package/couchbase> is also the same one as the one linked [here](#latest-release).
> 
> However the Windows binaries at <https://pecl.php.net/> are produced there, not through Couchbase's CI/CD pipeline, and are not necessarily the same as the Couchbase-produced binaries.

## [](#latest-release)PHP SDK 4.5 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

PHP SDK 4.5 is written to [version 3.9 of the SDK API specification](compatibility.md#api-version)(and matching the features available in Couchbase 8.0.0 and earlier).

### [](#version-4-5-0-1-april-2026)Version 4.5.0 (1 April 2026)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.5.0)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.4.0...4.5.0)| [Composer (Library)](https://packagist.org/packages/couchbase/couchbase#4.5.0)| [Composer (OpenTelemetry integration)](https://packagist.org/packages/couchbase/couchbase-opentelemetry#4.5.0)

```bash
composer require ext-couchbase:4.5.0
composer require couchbase/couchbase:4.5.0
composer require couchbase/couchbase-opentelemetry:4.5.0
```

composer.json

```json
"require": {
    "ext-couchbase": "4.5.0",
    "couchbase/couchbase-opentelemetry": "4.5.0",
    "couchbase/couchbase": "4.5.0"
}
```

#### [](#new-features-and-enhancements)New features and Enhancements

* [PCBC-1040](https://jira.issues.couchbase.com/browse/PCBC-1040): Tracing — include child spans created by the C++ core ([#249](https://github.com/couchbase/couchbase-php-client/pull/249)).
* [PCBC-1039](https://jira.issues.couchbase.com/browse/PCBC-1039): Added `MeterException` ([#248](https://github.com/couchbase/couchbase-php-client/pull/248)).
* [PCBC-1038](https://jira.issues.couchbase.com/browse/PCBC-1038), [PCBC-1039](https://jira.issues.couchbase.com/browse/PCBC-1039): Added tracing and metrics instrumentation for management operations ([#244](https://github.com/couchbase/couchbase-php-client/pull/244)).
* [PCBC-1039](https://jira.issues.couchbase.com/browse/PCBC-1039): Added `LoggingMeter` implementation ([#246](https://github.com/couchbase/couchbase-php-client/pull/246)).
* [PCBC-1038](https://jira.issues.couchbase.com/browse/PCBC-1038): Added `ThresholdLoggingTracer` implementation ([#245](https://github.com/couchbase/couchbase-php-client/pull/245)).
* [PCBC-1038](https://jira.issues.couchbase.com/browse/PCBC-1038), [PCBC-1039](https://jira.issues.couchbase.com/browse/PCBC-1039): Added tracing and metrics instrumentation for non-management operations ([#241](https://github.com/couchbase/couchbase-php-client/pull/241)).
* [PCBC-1050](https://jira.issues.couchbase.com/browse/PCBC-1050): Added missing manager accessors in Cluster, Bucket, and Collection interfaces ([#243](https://github.com/couchbase/couchbase-php-client/pull/243)).
* [PCBC-1048](https://jira.issues.couchbase.com/browse/PCBC-1048): Updated all KV operations to use C++ Core API ([#239](https://github.com/couchbase/couchbase-php-client/pull/239)).
* [PCBC-1033](https://jira.issues.couchbase.com/browse/PCBC-1033): JWT Based authentication added ([#236](https://github.com/couchbase/couchbase-php-client/pull/236)).
* [PCBC-1032](https://jira.issues.couchbase.com/browse/PCBC-1032), [PCBC-1041](https://jira.issues.couchbase.com/browse/PCBC-1041): Added support for mTLS Cert Refresh and exposed `idleHttpConnectionTimeout` ([#233](https://github.com/couchbase/couchbase-php-client/pull/233)).
* [PCBC-1035](https://jira.issues.couchbase.com/browse/PCBC-1035): Added lazy connections with options — this is to optimize the number of KV connections ([#235](https://github.com/couchbase/couchbase-php-client/pull/235)).
* [PCBC-1015](https://jira.issues.couchbase.com/browse/PCBC-1015): SDK Telemetry Collection for Server. OpenTelemetry integration is available as composer package `couchbase/couchbase-opentelemetry`.
* Updated core to `1.3.1` ([#250](https://github.com/couchbase/couchbase-php-client/pull/250)).

#### [](#bug-fixes)Bug fixes

* [PCBC-1053](https://jira.issues.couchbase.com/browse/PCBC-1053): Fixed CC compiler flags bleeding into `CMAKE_C_COMPILER` on macOS ([#251](https://github.com/couchbase/couchbase-php-client/pull/251)).
* [PCBC-1052](https://jira.issues.couchbase.com/browse/PCBC-1052): Initialize timeout to null in search/collection management options blocks ([#247](https://github.com/couchbase/couchbase-php-client/pull/247)).
* [PCBC-1034](https://jira.issues.couchbase.com/browse/PCBC-1034): Binary `CasMismatch` test fix.

#### [](#build-improvements)Build improvements

* [PCBC-1054](https://jira.issues.couchbase.com/browse/PCBC-1054): Updated CI matrix. Bumped PHP versions and Alpine images ([#252](https://github.com/couchbase/couchbase-php-client/pull/252)). Dropped support for PHP 8.1, added support for PHP 8.5.
* [PCBC-1049](https://jira.issues.couchbase.com/browse/PCBC-1049): Added 8.0 to server test version matrix ([#242](https://github.com/couchbase/couchbase-php-client/pull/242)).
* [PCBC-1047](https://jira.issues.couchbase.com/browse/PCBC-1047): GHA macos13 runners have been retired.
* removed intl from setup php ([#234](https://github.com/couchbase/couchbase-php-client/pull/234)).

#### [](#deprecations)Deprecations

* [PCBC-1043](https://jira.issues.couchbase.com/browse/PCBC-1043): Deprecated support for MapReduce Views (which is also now deprecated in Couchbase Server).

#### [](#download-links)Download Links

| Checksum |                |         |     | [couchbase-4.5.0.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.5.0.sha256.txt)                                              |
| -------- | -------------- | ------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Source   |                |         |     | [couchbase-4.5.0.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0.tgz)                                                            |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64        | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64        | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-linux-x86%5F64.tgz)         |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.5.0-php82-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php82-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.5.0-php83-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php83-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.5.0-php84-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php84-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.5 | NTS | [couchbase-4.5.0-php85-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php85-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-macos-x86%5F64.tgz)         |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-macos-x86%5F64.tgz)         |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-macos-x86%5F64.tgz)         |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-macos-x86%5F64.tgz)         |
| MacOS    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-macos-x86%5F64.tgz)         |
| MacOS    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-macos-x86%5F64.tgz)         |
| MacOS    | x86\_64        | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-macos-x86%5F64.tgz)         |
| MacOS    | x86\_64        | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-macos-x86%5F64.tgz)         |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-macos-arm64.tgz)              |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-macos-arm64.tgz)              |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-macos-arm64.tgz)              |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-macos-arm64.tgz)              |
| MacOS    | arm64          | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-macos-arm64.tgz)              |
| MacOS    | arm64          | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-macos-arm64.tgz)              |
| MacOS    | arm64          | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-macos-arm64.tgz)              |
| MacOS    | arm64          | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-macos-arm64.tgz)              |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-windows-x64.zip)              |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-windows-x64.zip)              |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-windows-x64.zip)              |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-windows-x64.zip)              |
| Windows  | x86\_64        | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-windows-x64.zip)              |
| Windows  | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-windows-x64.zip)              |
| Windows  | x86\_64        | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-windows-x64.zip)              |
| Windows  | x86\_64        | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-windows-x64.zip)              |

ABI-safe binaries that expose all internal APIs as `\Couchbase\Extension_4_5_0`, which allows the loading of different versions of the library at the same time.

The extension file is named `couchbase_4_5_0.so` (`couchbase_4_5_0.dll`).

| Linux   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-linux-x86%5F64-abi.tgz)         |
| ------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-linux-x86%5F64-abi.tgz)         |
| Linux   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-linux-x86%5F64-abi.tgz)         |
| Linux   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-linux-x86%5F64-abi.tgz)         |
| Linux   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-linux-x86%5F64-abi.tgz)         |
| Linux   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-linux-x86%5F64-abi.tgz)         |
| Linux   | x86\_64        | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-linux-x86%5F64-abi.tgz)         |
| Linux   | x86\_64        | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-linux-x86%5F64-abi.tgz)         |
| Linux   | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.5.0-php82-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php82-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.5.0-php83-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php83-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.5.0-php84-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php84-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.5 | NTS | [couchbase-4.5.0-php85-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php85-nts-linux-musl-x86%5F64-abi.tgz) |
| MacOS   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-macos-x86%5F64-abi.tgz)         |
| MacOS   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-macos-x86%5F64-abi.tgz)         |
| MacOS   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-macos-x86%5F64-abi.tgz)         |
| MacOS   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-macos-x86%5F64-abi.tgz)         |
| MacOS   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-macos-x86%5F64-abi.tgz)         |
| MacOS   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-macos-x86%5F64-abi.tgz)         |
| MacOS   | x86\_64        | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-macos-x86%5F64-abi.tgz)         |
| MacOS   | x86\_64        | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-macos-x86%5F64-abi.tgz)         |
| MacOS   | arm64          | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-macos-arm64-abi.tgz)              |
| MacOS   | arm64          | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-macos-arm64-abi.tgz)              |
| MacOS   | arm64          | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-macos-arm64-abi.tgz)              |
| MacOS   | arm64          | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-macos-arm64-abi.tgz)              |
| MacOS   | arm64          | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-macos-arm64-abi.tgz)              |
| MacOS   | arm64          | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-macos-arm64-abi.tgz)              |
| MacOS   | arm64          | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-macos-arm64-abi.tgz)              |
| MacOS   | arm64          | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-macos-arm64-abi.tgz)              |
| Windows | x86\_64        | PHP 8.2 | NTS | [couchbase-4.5.0-php8.2-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-nts-windows-x64-abi.zip)              |
| Windows | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.5.0-php8.2-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.2-zts-windows-x64-abi.zip)              |
| Windows | x86\_64        | PHP 8.3 | NTS | [couchbase-4.5.0-php8.3-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-nts-windows-x64-abi.zip)              |
| Windows | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.5.0-php8.3-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.3-zts-windows-x64-abi.zip)              |
| Windows | x86\_64        | PHP 8.4 | NTS | [couchbase-4.5.0-php8.4-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-nts-windows-x64-abi.zip)              |
| Windows | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.5.0-php8.4-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.4-zts-windows-x64-abi.zip)              |
| Windows | x86\_64        | PHP 8.5 | NTS | [couchbase-4.5.0-php8.5-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-nts-windows-x64-abi.zip)              |
| Windows | x86\_64        | PHP 8.5 | ZTS | [couchbase-4.5.0-php8.5-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.5.0-php8.5-zts-windows-x64-abi.zip)              |

## [](#php-sdk-4-4-releases)PHP SDK 4.4 Releases

### [](#version-4-4-0-29-september-2024)Version 4.4.0 (29 September 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.4.0)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.3.0...4.4.0)

#### [](#enhancements)Enhancements

* [PCBC-1026](https://jira.issues.couchbase.com/browse/PCBC-1026): Implemented FTS vector search pre-filters.
* [PCBC-1030](https://jira.issues.couchbase.com/browse/PCBC-1030): Fixed how SDK handles KV Expiry ([#226](https://github.com/couchbase/couchbase-php-client/pull/226)).
* Updated core to 1.2.0\. Release notes: [C++ SDK 1.2.0](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-2-0-26-september-2025).

#### [](#build-and-test-infrastructure-improvements)Build and Test Infrastructure Improvements

* [PCBC-1031](https://jira.issues.couchbase.com/browse/PCBC-1031): Fixed build with debug version of PHP 8.5.
* Github Actions: install VS2019 tools for building on windows 2022 ([#225](https://github.com/couchbase/couchbase-php-client/pull/225)).

#### [](#download-links-2)Download Links

| Checksum |                |         |     | [couchbase-4.4.0.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.4.0.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.4.0.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-windows-x64.zip)                |

ABI-safe binaries that expose all internal APIs as `\Couchbase\Extension_4_4_0`, which allows the loading of different versions of the library at the same time.

The extension file is named `couchbase_4_4_0.so` (`couchbase_4_4_0.dll`).

| Linux   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-linux-x86%5F64-abi.tgz)           |
| ------- | -------------- | ------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-linux-musl-x86%5F64-abi.tgz) |
| MacOS   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | arm64          | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-macos-arm64-abi.tgz)                |
| Windows | x86\_64        | PHP 8.1 | NTS | [couchbase-4.4.0-php8.1-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.4.0-php8.1-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.1-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | NTS | [couchbase-4.4.0-php8.2-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.4.0-php8.2-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.2-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | NTS | [couchbase-4.4.0-php8.3-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.4.0-php8.3-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.3-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | NTS | [couchbase-4.4.0-php8.4-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.4.0-php8.4-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.4.0-php8.4-zts-windows-x64-abi.zip)                |

## [](#php-sdk-4-3-releases)PHP SDK 4.3 Releases

### [](#version-4-3-0-12-june-2024)Version 4.3.0 (12 June 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.3.0)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.7...4.3.0)

#### [](#enhancements-2)Enhancements

* Updated core to 1.1.0\. Release notes: [C++ SDK 1.1.0](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-1-0-01-june-2025).
* [PCBC-1023](https://jira.issues.couchbase.com/browse/PCBC-1023): Added `numVBuckets` to BucketSettings ([#210](https://github.com/couchbase/couchbase-php-client/pull/210)).
* [PCBC-1024](https://jira.issues.couchbase.com/browse/PCBC-1024): Improved SDK error messages for account lock/unlock feature ([#211](https://github.com/couchbase/couchbase-php-client/pull/211)).
* [PCBC-1020](https://jira.issues.couchbase.com/browse/PCBC-1020): Implemented `getMulti()` and `getMultiReplicasFromPreferredServerGroup()` for transactions ([#213](https://github.com/couchbase/couchbase-php-client/pull/213)).

#### [](#fixes)Fixes

* [PCBC-1025](https://jira.issues.couchbase.com/browse/PCBC-1025): Added CAS to `append()`/`prepend()` ([#208](https://github.com/couchbase/couchbase-php-client/pull/208)).

#### [](#download-links-3)Download Links

| Checksum |                |         |     | [couchbase-4.3.0.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.3.0.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.3.0.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-windows-x64.zip)                |

ABI-safe binaries that expose all internal APIs as `\Couchbase\Extension_4_3_0`, which allows the loading of different versions of the library at the same time.

The extension file is named `couchbase_4_3_0.so` (`couchbase_4_3_0.dll`).

| Linux   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-linux-x86%5F64-abi.tgz)           |
| ------- | -------------- | ------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-linux-musl-x86%5F64-abi.tgz) |
| MacOS   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | arm64          | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-macos-arm64-abi.tgz)                |
| Windows | x86\_64        | PHP 8.1 | NTS | [couchbase-4.3.0-php8.1-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.3.0-php8.1-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.1-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | NTS | [couchbase-4.3.0-php8.2-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.3.0-php8.2-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.2-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | NTS | [couchbase-4.3.0-php8.3-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.3.0-php8.3-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.3-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | NTS | [couchbase-4.3.0-php8.4-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.3.0-php8.4-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.3.0-php8.4-zts-windows-x64-abi.zip)                |

## [](#php-sdk-4-2-releases)PHP SDK 4.2 Releases

### [](#version-4-2-7-18-march-2025)Version 4.2.7 (18 March 2025)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.7)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.6...4.2.7)

#### [](#fixes-2)Fixes

* Updated core to 1.0.6 ([#206](https://github.com/couchbase/couchbase-php-client/pull/206)). Release notes: [C++ SDK 1.0.6](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-6-12-march-2025).

#### [](#download-links-4)Download Links

| Checksum |                |         |     | [couchbase-4.2.7.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.2.7.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.7.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-windows-x64.zip)                |

ABI-safe binaries that expose all internal APIs as `\Couchbase\Extension_4_2_7`, which allows the loading of different versions of the library at the same time.

The extension file is named `couchbase_4_2_7.so` (`couchbase_4_2_7.dll`).

| Linux   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-linux-x86%5F64-abi.tgz)           |
| ------- | -------------- | ------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-linux-musl-x86%5F64-abi.tgz) |
| MacOS   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | arm64          | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-macos-arm64-abi.tgz)                |
| Windows | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.7-php8.1-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.7-php8.1-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.1-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.7-php8.2-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.7-php8.2-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.2-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.7-php8.3-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.7-php8.3-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.3-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.7-php8.4-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.7-php8.4-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.7-php8.4-zts-windows-x64-abi.zip)                |

### [](#version-4-2-6-29-january-2025)Version 4.2.6 (29 January 2025)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.6)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.5...4.2.6)

#### [](#enhancements-3)Enhancements

* [PCBC-992](https://jira.issues.couchbase.com/browse/PCBC-992): New APIs added to allow getting KV documents from a preferred server group. This feature allows the implementation of network optimization when traffic cost between server groups is higher than in the local group. In this case the application might select preferred server group in the connection options, and later opt-in for local operations during replica reads ([#201](https://github.com/couchbase/couchbase-php-client/pull/201)).

#### [](#fixes-3)Fixes

* [PCBC-1018](https://jira.issues.couchbase.com/browse/PCBC-1018): In some cases, when the extension was configured aggressively close persistent connections (e.g. with `couchbase.max_persistent=0` and `couchbase.persistent_timeout=0`), the connections might be considered expired and scheduled for destruction even if the application has references to them. This patch changes this behavior to skip such actions and destroy them later, when the reference counter reaches zero ([#200](https://github.com/couchbase/couchbase-php-client/pull/200)).
* [PCBC-1016](https://jira.issues.couchbase.com/browse/PCBC-1016): Fixed `trustCertificate` option that was ignored previously ([#195](https://github.com/couchbase/couchbase-php-client/pull/195)).
* Updated core to 1.0.5 ([#203](https://github.com/couchbase/couchbase-php-client/pull/203)). Release notes: [C++ SDK 1.0.5](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-5-24-january-2025).
* Fixed PHP 8.4 deprecation warnings ([#198](https://github.com/couchbase/couchbase-php-client/pull/198)).
* Fixed Undefined constant error ([#196](https://github.com/couchbase/couchbase-php-client/pull/196)).

#### [](#download-links-5)Download Links

| Checksum |                |         |     | [couchbase-4.2.6.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.2.6.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.6.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-windows-x64.zip)                |

ABI-safe binaries that expose all internal APIs as `\Couchbase\Extension_4_2_6`, which allows the loading of different versions of the library at the same time.

The extension file is named `couchbase_4_2_6.so` (`couchbase_4_2_6.dll`).

| Linux   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-linux-x86%5F64-abi.tgz)           |
| ------- | -------------- | ------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-linux-musl-x86%5F64-abi.tgz) |
| MacOS   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | arm64          | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-macos-arm64-abi.tgz)                |
| Windows | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.6-php8.1-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.6-php8.1-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.1-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.6-php8.2-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.6-php8.2-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.2-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.6-php8.3-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.6-php8.3-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.3-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.6-php8.4-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.6-php8.4-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.6-php8.4-zts-windows-x64-abi.zip)                |

### [](#version-4-2-5-22-november-2024)Version 4.2.5 (22 November 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.5)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.4...4.2.5)

#### [](#enhancements-4)Enhancements

* Core updated to 1.0.4\. Release notes: [C++ SDK 1.0.4](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-4-22-november-2024).
* [PCBC-1004](https://issues.couchbase.com/browse/PCBC-1004): Insert ABI version tag into PHP extension namespace ([#187](https://github.com/couchbase/couchbase-php-client/pull/187)). At this moment this feature is optional and does not break existing ABI. The extension namespace will become versioned by default from 4.3.0.  
Prebuild binaries with `-abi` suffix have version tag in the extension name, and in the namespaces of the visible API, as is shown with the following demo:  
```console  
$ wget \  
    https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-linux-x86_64.tgz \  
    https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-linux-x86_64-abi.tgz  
$ for t in *.tgz; do tar zxf $t; done  
$ php \
        -d extension=$(realpath couchbase-4.2.5-php8.3-nts-linux-x86_64-abi/couchbase_4_2_5.so) \
        -d extension=$(realpath couchbase-4.2.5-php8.3-nts-linux-x86_64/couchbase.so) \
        -i \
    | grep couchbase  
couchbase  
couchbase => enabled  
couchbase_extension_abi => unspecified  
couchbase_extension_version => 4.2.5  
couchbase_extension_revision => c9704a8aa5ca50475c5fe8ee64166fa164cbd43e  
couchbase_client_revision => 5355b0fdc221d87f0d6adbbf7e7f8826d819ea22  
couchbase_4_2_5  
couchbase => enabled  
couchbase_extension_abi => 4_2_5  
couchbase_extension_version => 4.2.5  
couchbase_extension_revision => c9704a8aa5ca50475c5fe8ee64166fa164cbd43e  
couchbase_client_revision => 5355b0fdc221d87f0d6adbbf7e7f8826d819ea22  
...  
$ php \
        -d extension=$(realpath couchbase-4.2.5-php8.3-nts-linux-x86_64-abi/couchbase_4_2_5.so) \
        --re couchbase_4_2_5 \
    | grep createConnection  
Function [ <internal:couchbase_4_2_5> function Couchbase\Extension_4_2_5\createConnection ] {  
$ php \
        -d extension=$(realpath couchbase-4.2.5-php8.3-nts-linux-x86_64/couchbase.so) \
        --re couchbase \
    | grep createConnection  
Function [ <internal:couchbase> function Couchbase\Extension\createConnection ] {  
```

#### [](#fixes-4)Fixes

* [PCBC-975](https://issues.couchbase.com/browse/PCBC-975): Fixed expiry with `upsertMulti`. The option is now applied to all documents.
* [PCBC-1017](https://issues.couchbase.com/browse/PCBC-1017): Updated user agent generation. It now uses the common SDK format.

#### [](#download-links-6)Download Links

| Checksum |                |         |     | [couchbase-4.2.5.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.2.5.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.5.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-windows-x64.zip)                |

As noted above, from this release we also publish ABI-safe binaries that expose all internal APIs as `\Couchbase\Extension_4_2_5`, which allows the loading of different versions of the library at the same time.

The extension file is also renamed to `couchbase_4_2_5.so`(`couchbase_4_2_5.dll`).

| Linux   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-linux-x86%5F64-abi.tgz)           |
| ------- | -------------- | ------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-linux-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-linux-x86%5F64-abi.tgz)           |
| Linux   | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-linux-musl-x86%5F64-abi.tgz) |
| Linux   | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-linux-musl-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-linux-musl-x86%5F64-abi.tgz) |
| MacOS   | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-macos-x86%5F64-abi.tgz)           |
| MacOS   | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-macos-x86\_64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-macos-x86%5F64-abi.tgz)           |
| MacOS   | arm64          | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-macos-arm64-abi.tgz)                |
| MacOS   | arm64          | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-macos-arm64-abi.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-macos-arm64-abi.tgz)                |
| Windows | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.5-php8.1-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.5-php8.1-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.1-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.5-php8.2-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.5-php8.2-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.2-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.5-php8.3-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.5-php8.3-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.3-zts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | NTS | [couchbase-4.2.5-php8.4-nts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-nts-windows-x64-abi.zip)                |
| Windows | x86\_64        | PHP 8.4 | ZTS | [couchbase-4.2.5-php8.4-zts-windows-x64-abi.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.5-php8.4-zts-windows-x64-abi.zip)                |

### [](#version-4-2-4-22-october-2024)Version 4.2.4 (22 October 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.4)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.3...4.2.4)

#### [](#enhancements-5)Enhancements

* [PCBC-832](https://issues.couchbase.com/browse/PCBC-832): Management API - Analytics Management ([#177](https://github.com/couchbase/couchbase-php-client/pull/177)).
* Core updated to 1.0.3\. Release notes: [C++ SDK 1.0.3](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-3-22-october-2024).

#### [](#fixes-5)Fixes

* [PCBC-1009](https://jira.issues.couchbase.com/browse/PCBC-1009): `IS_RESOURCE` has been removed from function signatures of the extension, so that they compile with 8.4.
* [PCBC-1010](https://jira.issues.couchbase.com/browse/PCBC-1010): implicit marking of certain parameters as nullable has now been deprecated. Use explicit nullable types where applicable to avoid deprecation warning in PHP 8.4.
* Fixed `SearchQuery` API docs link in API reference.

#### [](#download-links-7)Download Links

| Checksum |                |         |     | [couchbase-4.2.4.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.2.4.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.4.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.4-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.4-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.4-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.4-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.4-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.4-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.4-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.4-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.4-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.4-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.4-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.4-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.4-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.4-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.4-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.4-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.4-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.4-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.4-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.4-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.4-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.4-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.4-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.4-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.4-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.4-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.4-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.4-php8.3-zts-windows-x64.zip)                |

### [](#version-4-2-3-27-august-2024)Version 4.2.3 (27 August 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.3)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.2...4.2.3)

#### [](#enhancements-6)Enhancements

* Core updated to 1.0.1\. Release notes: [C++ SDK 1.0.1](../../../cxx-sdk/current/project-docs/sdk-release-notes.md#version-1-0-1-22-august-2024).

#### [](#download-links-8)Download Links

| Checksum |                |         |     | [couchbase-4.2.3.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.2.3.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.3.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.3-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.3-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.3-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.3-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.3-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.3-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.3-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.3-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.3-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.3-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.3-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.3-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.3-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.3-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.3-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.3-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.3-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.3-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.3-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.3-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.3-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.3-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.3-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.3-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.3-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.3-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.3-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.3-php8.3-zts-windows-x64.zip)                |

### [](#version-4-2-2-24-july-2024)Version 4.2.2 (24 July 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.2)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.1...4.2.2)

#### [](#fixes-6)Fixes

* [PCBC-997](https://issues.couchbase.com/browse/PCBC-997): Excluded C++ files, tests, and development scripts, so that Packagist will not install them to the application `./vendor` directory [#172](https://github.com/couchbase/couchbase-php-client/pull/172)).
* [PCBC-991](https://issues.couchbase.com/browse/PCBC-991): Added consistency utility for testing ([#168](https://github.com/couchbase/couchbase-php-client/pull/168)).
* [PCBC-989](https://issues.couchbase.com/browse/PCBC-989): Rollback to `cmake` 3.19 ([#167](https://github.com/couchbase/couchbase-php-client/pull/167)).
* [PCBC-988](https://issues.couchbase.com/browse/PCBC-988): Fixed type annotation for `JsonSerializable` implementations ([#166](https://github.com/couchbase/couchbase-php-client/pull/166)).

#### [](#enhancements-7)Enhancements

* [PCBC-994](https://issues.couchbase.com/browse/PCBC-994): Support for base64 encoded vector types added ([#169](https://github.com/couchbase/couchbase-php-client/pull/169), [#170](https://github.com/couchbase/couchbase-php-client/pull/170)).
* Core updated to 1.0.0\. Release notes: [C++ SDK 1.0.0](https://docs.couchbase.com/cxx-sdk/current/project-docs/sdk-release-notes.html#version-1-0-0-26-june-2024)

#### [](#download-links-9)Download Links

| Checksum |                |         |     | [couchbase-4.2.2.sha256.txt](https://packages.couchbase.com/clients/php/couchbase-4.2.2.sha256.txt)                                                |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.2.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.2-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.2-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.2-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.2-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.2-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.2-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.2-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.2-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.2-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.2-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.2-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.2-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.2-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.2-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.2-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.2-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.2-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.2-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.2-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.2-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.2-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.2-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.2-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.2-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.2-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.2-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.2-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.2-php8.3-zts-windows-x64.zip)                |

\>>>>>>> ddeee36208e40a12e338c5eaba15ffad262cf27e

### [](#version-4-2-1-23-april-2024)Version 4.2.1 (23 April 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.1)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.2.0...4.2.1)

#### [](#enhancements-8)Enhancements

* [PCBC-859](https://issues.couchbase.com/browse/PCBC-859): Updated build scripts and instructions for Windows ([#158](https://github.com/couchbase/couchbase-php-client/pull/158), [#164](https://github.com/couchbase/couchbase-php-client/pull/164)).
* [PCBC-984](https://issues.couchbase.com/browse/PCBC-984), [PCBC-987](https://issues.couchbase.com/browse/PCBC-987): Improved compatiblity with `pcntl_fork()` ([#157](https://github.com/couchbase/couchbase-php-client/pull/157), [#162](https://github.com/couchbase/couchbase-php-client/pull/162)).

#### [](#fixes-7)Fixes

* [PCBC-987](https://issues.couchbase.com/browse/PCBC-987): Fixed consistency vector encoding for FTS ([#163](https://github.com/couchbase/couchbase-php-client/pull/163)).
* [PCBC-985](https://issues.couchbase.com/browse/PCBC-985): Use system DNS config by default, and disable DNS-SRV if system does not provide DNS server ([#159](https://github.com/couchbase/couchbase-php-client/pull/159)).

#### [](#notable-changes-in-core-c)Notable changes in core C++

##### [](#enhancements-9)Enhancements

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
* Add feature check for scoped analyze\_document in tests ([#555](https://github.com/couchbaselabs/couchbase-cxx-client/pull/555))

#### [](#download-links-10)Download Links

| Checksum |                |         |     | [couchbase-4.2.1.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.2.1.sha256sum)                                                  |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.1.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.1-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.1-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.1-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.1-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.1-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.1-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.1-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.1-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.1-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.1-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.1-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.1-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.1-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.1-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.1-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.1-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.1-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.1-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.1-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.1-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.1-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-zts-macos-arm64.tgz)                |
| Windows  | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.1-php8.1-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.1-php8.1-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.1-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.1-php8.2-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.1-php8.2-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.2-zts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.1-php8.3-nts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-nts-windows-x64.zip)                |
| Windows  | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.1-php8.3-zts-windows-x64.zip](https://packages.couchbase.com/clients/php/couchbase-4.2.1-php8.3-zts-windows-x64.zip)                |

### [](#version-4-2-0-17-march-2024)Version 4.2.0 (17 March 2024)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.2.0)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.1.6...4.2.0)

#### [](#known-issues)Known Issues

* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): This version of the SDK will not be able to connect to a cluster utilizing alternate addressing. The recommendation is to wait to upgrade to a version of the PHP SDK that contains C++ 1.0.0-dp.15 (or later).

#### [](#enhancements-10)Enhancements

* [PCBC-979](https://issues.couchbase.com/browse/PCBC-979): Added static helpers to `SearchQuery` types ([#149](https://github.com/couchbase/couchbase-php-client/pull/149)).
* [PCBC-970](https://issues.couchbase.com/browse/PCBC-970): SDK support added for Scoped Search Indexes ([#147](https://github.com/couchbase/couchbase-php-client/pull/147)).
* [PCBC-968](https://issues.couchbase.com/browse/PCBC-968): Support addd for `maxTTL` value of -1 for collection 'no expiry' ([#144](https://github.com/couchbase/couchbase-php-client/pull/144)).
* [PCBC-967](https://issues.couchbase.com/browse/PCBC-967): Support added for vector search ([#143](https://github.com/couchbase/couchbase-php-client/pull/143)).
* [PCBC-965](https://issues.couchbase.com/browse/PCBC-965): Adedd `DocumentNotLocked` error to corresponds with the C++ error code `couchbase::errc::key_value::document_not_locked`([#142](https://github.com/couchbase/couchbase-php-client/pull/142)).
* [PCBC-960](https://issues.couchbase.com/browse/PCBC-960): Merge protostellar branch to master, in preparation for `couchbase2` protocol ([#138](https://github.com/couchbase/couchbase-php-client/pull/138), [#153](https://github.com/couchbase/couchbase-php-client/pull/153)).

#### [](#fixes-9)Fixes

* [PCBC-964](https://issues.couchbase.com/browse/PCBC-964): The SDK no longer fires the close operation asynchronously, instead it will now wait until the core instance is completely destroyed Wait until the core connection is closed ([#141](https://github.com/couchbase/couchbase-php-client/pull/141)).
* [PCBC-972](https://issues.couchbase.com/browse/PCBC-972): Fixed C++ detection on MacOS X, so that the SDK now installs correctly on Sonoma ([#145](https://github.com/couchbase/couchbase-php-client/pull/145)).
* Added missing `use` statement in class `DecrementOptions` ([#146](https://github.com/couchbase/couchbase-php-client/pull/146)).
* Updated core and renamed `query_index_create` fields to keys ([#148](https://github.com/couchbase/couchbase-php-client/pull/148)).

#### [](#notable-changes-in-core-c-2)Notable changes in core C++

##### [](#since-1-0-0-dp-14)Since 1.0.0-dp.14

Fixes

* [CXXCBC-482](https://issues.couchbase.com/browse/CXXCBC-482): Updated range scan orchestrator to use best effort retry strategy by default ([#542](https://github.com/couchbaselabs/couchbase-cxx-client/pull/542)).
* [CXXCBC-481](https://issues.couchbase.com/browse/CXXCBC-481): Fixed potential crash when parsing search result hits ([#541](https://github.com/couchbaselabs/couchbase-cxx-client/pull/541)).
* [CXXCBC-461](https://issues.couchbase.com/browse/CXXCBC-461): Updated ping operation to not send to nodes that have not completed bootstrap ([#540](https://github.com/couchbaselabs/couchbase-cxx-client/pull/540)).
* [CXXCBC-480](https://issues.couchbase.com/browse/CXXCBC-480): Fixed capabilities check for replica LookupIn operations ([#539](https://github.com/couchbaselabs/couchbase-cxx-client/pull/539)).
* [CXXCBC-479](https://issues.couchbase.com/browse/CXXCBC-479): Fixed capabilities check for replica `LookupIn` operations ([#537](https://github.com/couchbaselabs/couchbase-cxx-client/pull/537)).
* [CXXCBC-336](https://issues.couchbase.com/browse/CXXCBC-336): Updated DNS config to not fallback to 8.8.8.8 if SDK cannot obtain system DNS server ([#533](https://github.com/couchbaselabs/couchbase-cxx-client/pull/533)).

##### [](#since-1-0-0-dp-13)Since 1.0.0-dp.13

New features and enhancements

* [CXXCBC-456](https://issues.couchbase.com/browse/CXXCBC-456): Updated configuration logic when 0x0d (`EConfigOnly`) status code is received to have the SDK request new configuration and send current operation to retry orchestrator ([#523](https://github.com/couchbaselabs/couchbase-cxx-client/pull/523)).
* [CXXCBC-191](https://issues.couchbase.com/browse/CXXCBC-191): Index Key Encoding ([#519](https://github.com/couchbaselabs/couchbase-cxx-client/pull/519)) — in line with the [rfc](https://github.com/couchbaselabs/sdk-rfcs/blob/master/rfc/0054-sdk3-management-apis.md), the `fields` paramaeter is now remamed to keys in the Public API's `create_index()`, and each index key provided to `create_index()` is encoded by surrounding them with backticks.
* Added `full_set` option to view query options ([#517](https://github.com/couchbaselabs/couchbase-cxx-client/pull/517)).

Fixes

* [CXXCBC-345](https://issues.couchbase.com/browse/CXXCBC-345): Added range scan improvements and resolved concurrency issues ([#525](https://github.com/couchbaselabs/couchbase-cxx-client/pull/525)).
* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Updated config polling to not use session that is not bootstrapped ([#528](https://github.com/couchbaselabs/couchbase-cxx-client/pull/528)).
* [CXXCBC-447](https://issues.couchbase.com/browse/CXXCBC-447): Updated bootstrap logic to use addresses from the config to bootstrap bucket ([#516](https://github.com/couchbaselabs/couchbase-cxx-client/pull/516)).
* [CXXCBC-450](https://issues.couchbase.com/browse/CXXCBC-450): Updated bootstrap logic to reset bootstrap handler before re-bootstrap ([#524](https://github.com/couchbaselabs/couchbase-cxx-client/pull/524)).

  * We do not want any actions from the old bootstrap handler once the session decided to re-bootstrap. For example, bucket could not be selected, but we might still get configuration responses before socket reset.
* [CXXCBC-452](https://issues.couchbase.com/browse/CXXCBC-452): Updated capabilities and fail fast when selected feature is not available ([#522](https://github.com/couchbaselabs/couchbase-cxx-client/pull/522), [#513](https://github.com/couchbaselabs/couchbase-cxx-client/pull/513)).
* [CXXCBC-431](https://issues.couchbase.com/browse/CXXCBC-431): Added check for history retention bucket capability in collection create/update ([#502](https://github.com/couchbaselabs/couchbase-cxx-client/pull/502), [#505](https://github.com/couchbaselabs/couchbase-cxx-client/pull/505)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query operation to return `feature_not_available` if query preserve expiry is specified but is not supported on the server([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).

##### [](#since-1-0-0-dp-12)Since 1.0.0-dp.12

New features and enhancements

* [CXXCBC-346](https://issues.couchbase.com/browse/CXXCBC-346): Support added for `maxTTL` value of -1 for collection 'no expiry' ([#500](https://github.com/couchbaselabs/couchbase-cxx-client/pull/500)).
* [CXXCBC-442](https://issues.couchbase.com/browse/CXXCBC-442): Transcoder support - which was previously limited in the SDK to `JSON` and `RawBinary` transcoders — has now been extended to `raw_json` and `raw_string` transcoders ([#514](https://github.com/couchbaselabs/couchbase-cxx-client/pull/514), [#515](https://github.com/couchbaselabs/couchbase-cxx-client/pull/515)).
* [CXXCBC-440](https://issues.couchbase.com/browse/CXXCBC-440): Support added for Scoped Search Indexes ([#512](https://github.com/couchbaselabs/couchbase-cxx-client/pull/512), [#513](https://github.com/couchbaselabs/couchbase-cxx-client/pull/513)).

Fixes

* [CXXCBC-284](https://issues.couchbase.com/browse/CXXCBC-284): Updated config polling to not use session that is not bootstrapped, to reduce network traffic when polling for cluster configuration ([#504](https://github.com/couchbaselabs/couchbase-cxx-client/pull/504), [#528](https://github.com/couchbaselabs/couchbase-cxx-client/pull/528)).
* [CXXCBC-422](https://issues.couchbase.com/browse/CXXCBC-422): Added insufficient credentials error code to common query error code conversion ([#511](https://github.com/couchbaselabs/couchbase-cxx-client/pull/511)).
* [CXXCBC-421](https://issues.couchbase.com/browse/CXXCBC-421): Updated query operation to return `feature_not_available` if query preserve expiry is specified but is not supported on the server([#510](https://github.com/couchbaselabs/couchbase-cxx-client/pull/510)).
* [CXXCBC-426](https://issues.couchbase.com/browse/CXXCBC-426): Under testing, a get with very large projection was returning fields outside of the projection. This has been fixed, with the projections now set correctly, and the SDK should fall back to a full-doc fetch and return a valid projected result ([#499](https://github.com/couchbaselabs/couchbase-cxx-client/pull/499)).

##### [](#since-1-0-0-dp-11)Since 1.0.0-dp.11

Fixes

* [CXXCBC-404](https://issues.couchbase.com/browse/CXXCBC-404): Fixed `unlock` operations to expose `KV_LOCKED` status as `cas_mismatch` ([#479](https://github.com/couchbaselabs/couchbase-cxx-client/pull/479)).
* [CXXCBC-403](https://issues.couchbase.com/browse/CXXCBC-403): Updated `not_my_vbucket` KV response to allow retries ([#480](https://github.com/couchbaselabs/couchbase-cxx-client/pull/480)).
* [CXXCBC-368](https://issues.couchbase.com/browse/CXXCBC-368): Added support for subscribing to clustermap notifications to speed up failover ([#490](https://github.com/couchbaselabs/couchbase-cxx-client/pull/490)).
* [CXXCBC-419](https://issues.couchbase.com/browse/CXXCBC-419): Updated MCBP protocol parser to start with clean state. Fixes protocol parsing issues when bootstrap sequence is being retried ([#496](https://github.com/couchbaselabs/couchbase-cxx-client/pull/496)).
* [CXXCBC-409](https://issues.couchbase.com/browse/CXXCBC-409): Added handling for `index does not exist` query error ([#492](https://github.com/couchbaselabs/couchbase-cxx-client/pull/492)).
* [CXXCBC-391](https://issues.couchbase.com/browse/CXXCBC-391): Fixed transactions API inconsistencies ([#482](https://github.com/couchbaselabs/couchbase-cxx-client/pull/482)):
* Removed `kv_timeout`,
* Renamed `expiration_time` to `timeout`.

New features and enhancements

* [CXXCBC-100](https://issues.couchbase.com/browse/CXXCBC-100): Added ability to set timeout for ping ([#486](https://github.com/couchbaselabs/couchbase-cxx-client/pull/486)).
* [CXXCBC-412](https://issues.couchbase.com/browse/CXXCBC-412): Added support for the `document_not_locked` (0x0e) KV status, mapping it to the `errc::key_value::document_not_locked` error code ([#491](https://github.com/couchbaselabs/couchbase-cxx-client/pull/491)).

##### [](#since-1-0-0-dp-10)Since 1.0.0-dp.10

Fixes

* [CXXCBC-383](https://issues.couchbase.com/browse/CXXCBC-383): The `subdoc_doc_too_deep` (0xc4) KV status now returns a\`path\_too\_deep\` error code ([#455](https://github.com/couchbaselabs/couchbase-cxx-client/pull/455)).

New features and enhancements

* [CXXCBC-377](https://issues.couchbase.com/browse/CXXCBC-377): Implemented `ExtParallelUnstaging` in transactions ([#457](https://github.com/couchbaselabs/couchbase-cxx-client/pull/457)).
* [CXXCBC-363](https://issues.couchbase.com/browse/CXXCBC-363): Added examples for bulk operations ([#442](https://github.com/couchbaselabs/couchbase-cxx-client/pull/442)).
* Added more information to diagnose timeouts on NMV responses ([#475](https://github.com/couchbaselabs/couchbase-cxx-client/pull/475)).

#### [](#download-links-11)Download Links

| Checksum |                |         |     | [couchbase-4.2.0.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.2.0.sha256sum)                                                  |
| -------- | -------------- | ------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source   |                |         |     | [couchbase-4.2.0.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0.tgz)                                                              |
| Linux    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.0-php8.1-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.1-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.0-php8.1-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.1-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.0-php8.2-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.2-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.0-php8.2-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.2-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.0-php8.3-nts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.3-nts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.0-php8.3-zts-linux-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.3-zts-linux-x86%5F64.tgz)           |
| Linux    | x86\_64 (musl) | PHP 8.1 | NTS | [couchbase-4.2.0-php8.1-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.1-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.2 | NTS | [couchbase-4.2.0-php8.2-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.2-nts-linux-musl-x86%5F64.tgz) |
| Linux    | x86\_64 (musl) | PHP 8.3 | NTS | [couchbase-4.2.0-php8.3-nts-linux-musl-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.3-nts-linux-musl-x86%5F64.tgz) |
| MacOS    | x86\_64        | PHP 8.1 | NTS | [couchbase-4.2.0-php8.1-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.1-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.1 | ZTS | [couchbase-4.2.0-php8.1-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.1-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | NTS | [couchbase-4.2.0-php8.2-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.2-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.2 | ZTS | [couchbase-4.2.0-php8.2-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.2-zts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | NTS | [couchbase-4.2.0-php8.3-nts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.3-nts-macos-x86%5F64.tgz)           |
| MacOS    | x86\_64        | PHP 8.3 | ZTS | [couchbase-4.2.0-php8.3-zts-macos-x86\_64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.3-zts-macos-x86%5F64.tgz)           |
| MacOS    | arm64          | PHP 8.1 | NTS | [couchbase-4.2.0-php8.1-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.1-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.1 | ZTS | [couchbase-4.2.0-php8.1-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.1-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | NTS | [couchbase-4.2.0-php8.2-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.2-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.2 | ZTS | [couchbase-4.2.0-php8.2-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.2-zts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | NTS | [couchbase-4.2.0-php8.3-nts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.3-nts-macos-arm64.tgz)                |
| MacOS    | arm64          | PHP 8.3 | ZTS | [couchbase-4.2.0-php8.3-zts-macos-arm64.tgz](https://packages.couchbase.com/clients/php/couchbase-4.2.0-php8.3-zts-macos-arm64.tgz)                |

## [](#php-sdk-4-1-releases)PHP SDK 4.1 Releases

### [](#version-4-1-6-10-october-2023)Version 4.1.6 (10 October 2023)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.1.6)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.1.5...4.1.6)

| Source   | [couchbase-4.1.6.tgz](https://packages.couchbase.com/clients/php/couchbase-4.1.6.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.1.6.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.1.6.sha256sum) |

#### [](#enhancements-11)Enhancements

* [PCBC-956](https://issues.couchbase.com/browse/PCBC-956): Updated wrapper-side bucket settings — to now use new `BucketSettings` optional fields in underlying C++ core ([#132](https://github.com/couchbase/couchbase-php-client/pull/132)).
* [PCBC-950](https://issues.couchbase.com/browse/PCBC-950): Added support to bucket settings for no dedup feature ([#131](https://github.com/couchbase/couchbase-php-client/pull/131)).
* [PCBC-955](https://issues.couchbase.com/browse/PCBC-955): Preventing trailing garbage in encoded CAS value ([#134](https://github.com/couchbase/couchbase-php-client/pull/134)).
* Updates to support PHP 8.3: `zend_bool` was removed from 8.3.

#### [](#underlying-c-sdk-core-changes)Underlying C++ SDK Core Changes

* [CXXCBC-376](https://issues.couchbase.com/browse/CXXCBC-376): Changed what 'create' and 'update' bucket operations send to the server. Unrequired `BucketSettings` fields are now set to optional, and are not sent unless the settings are explicitly specified. ([#451](https://github.com/couchbaselabs/couchbase-cxx-client/pull/451)).
* [CXXCBC-374](https://issues.couchbase.com/browse/CXXCBC-374): The SDK should now return a 'bucket\_exists' error when the bucket already exists during a 'create' operation. ([#449](https://github.com/couchbaselabs/couchbase-cxx-client/pull/449)).
* [CXXCBC-359](https://issues.couchbase.com/browse/CXXCBC-359): Reduced the default timeout for idle HTTP connections to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures. ([#448](https://github.com/couchbaselabs/couchbase-cxx-client/pull/448)).
* [CXXCBC-367](https://issues.couchbase.com/browse/CXXCBC-367), [CXXCBC-370](https://issues.couchbase.com/browse/CXXCBC-370): Added history retention settings to buckets/collection management ([#446](https://github.com/couchbaselabs/couchbase-cxx-client/pull/446)).
* [CXXCBC-119](https://issues.couchbase.com/browse/CXXCBC-119): Return booleans for subdocument 'exists' operation, instead of error code ([#444](https://github.com/couchbaselabs/couchbase-cxx-client/pull/444), [#452](https://github.com/couchbaselabs/couchbase-cxx-client/pull/452)).
* Detect `collection_not_found` error in `update_collection` response ([#450](https://github.com/couchbaselabs/couchbase-cxx-client/pull/450)).

### [](#version-4-1-5-21-august-2023)Version 4.1.5 (21 August 2023)

[API documentation](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.1.5)| [Full Changelog](https://github.com/couchbase/couchbase-php-client/compare/4.1.4...4.1.5)

| Source   | [couchbase-4.1.5.tgz](https://packages.couchbase.com/clients/php/couchbase-4.1.5.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.1.5.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.1.5.sha256sum) |

#### [](#enhancements-12)Enhancements

* [PCBC-939](https://issues.couchbase.com/browse/PCBC-939): Added support for query with Read from Replica ([#118](https://github.com/couchbaselabs/couchbase-cxx-client/pull/118)).
* [PCBC-831](https://issues.couchbase.com/browse/PCBC-831): Implemented search index management ([#115](https://github.com/couchbaselabs/couchbase-cxx-client/pull/115)).
* [PCBC-945](https://issues.couchbase.com/browse/PCBC-945): Expiry options for increment/decrement are now exposed, as they were before 4.0.0 ([#120](https://github.com/couchbaselabs/couchbase-cxx-client/pull/120)).
* [PCBC-937](https://issues.couchbase.com/browse/PCBC-937): Fixed `removeMulti`, which now correctly removes documents ([#123](https://github.com/couchbaselabs/couchbase-cxx-client/pull/123)).
* [PCBC-938](https://issues.couchbase.com/browse/PCBC-938): Override exception constructor in PHP Extension, which allows to initialize context in derived classes ([#117](https://github.com/couchbaselabs/couchbase-cxx-client/pull/117)).
* [PCBC-940](https://issues.couchbase.com/browse/PCBC-940): Added support for subdoc Read from Replica ([#121](https://github.com/couchbaselabs/couchbase-cxx-client/pull/121)).
* [PCBC-884](https://issues.couchbase.com/browse/PCBC-884): Added support for Native KV range scans ([#122](https://github.com/couchbaselabs/couchbase-cxx-client/pull/122), [#127](https://github.com/couchbaselabs/couchbase-cxx-client/pull/127)).

#### [](#underlying-c-sdk-core)Underlying C++ SDK Core

* [CXXCBC-333](https://issues.couchbase.com/browse/CXXCBC-333): Fixed parsing 'resolv.conf' on Linux ([#416](https://github.com/couchbaselabs/couchbase-cxx-client/pull/416)).

  * The library might not ignore trailing characters when reading nameserver address from the file.
* [CXXCBC-335](https://issues.couchbase.com/browse/CXXCBC-335): now logging connection options for visibility ([#417](https://github.com/couchbaselabs/couchbase-cxx-client/pull/417)).
* [CXXCBC-343](https://issues.couchbase.com/browse/CXXCBC-343): Continue bootsrap if DNS-SRV resolution fails ([#422](https://github.com/couchbaselabs/couchbase-cxx-client/pull/422)).
* [CXXCBC-242](https://issues.couchbase.com/browse/CXXCBC-242): SDK Support for Native KV Range Scans ([#419](https://github.com/couchbaselabs/couchbase-cxx-client/pull/419), [#423](https://github.com/couchbaselabs/couchbase-cxx-client/pull/423), [#424](https://github.com/couchbaselabs/couchbase-cxx-client/pull/424), [#426](https://github.com/couchbaselabs/couchbase-cxx-client/pull/426), [#428](https://github.com/couchbaselabs/couchbase-cxx-client/pull/428), [#431](https://github.com/couchbaselabs/couchbase-cxx-client/pull/431), [#432](https://github.com/couchbaselabs/couchbase-cxx-client/pull/432), [#433](https://github.com/couchbaselabs/couchbase-cxx-client/pull/433), [#434](https://github.com/couchbaselabs/couchbase-cxx-client/pull/434)).
* [CXXCBC-339](https://issues.couchbase.com/browse/CXXCBC-339): Disable older TLS protocols ([#418](https://github.com/couchbaselabs/couchbase-cxx-client/pull/418)).

### [](#version-4-1-4-26-may-2023)Version 4.1.4 (26 May 2023)

API documentation: <https://docs.couchbase.com/sdk-api/couchbase-php-client-4.1.4>

| Source   | [couchbase-4.1.4.tgz](https://packages.couchbase.com/clients/php/couchbase-4.1.4.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.1.4.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.1.4.sha256sum) |

#### [](#enhancements-13)Enhancements

* Added `couchbase::` namespace to `durability_level`, which fixes using Sync Durability. ([#102](https://github.com/couchbase/couchbase-php-client/pull/102))
* [PCBC-934](https://issues.couchbase.com/browse/PCBC-934): Fixed setting timeout for transactions.

#### [](#underlying-c-sdk-core-2)Underlying C++ SDK Core

* [CXXCBC-327](https://issues.couchbase.com/browse/CXXCBC-327): Bundled Mozilla certificates with the library ([#405](https://github.com/couchbaselabs/couchbase-cxx-client/pull/405), [#408](https://github.com/couchbaselabs/couchbase-cxx-client/pull/408)). Source: <https://curl.se/docs/caextract.html>. Use the `disable_mozilla_ca_certificates` connection string option to disable the bundled certificates.
* [CXXCBC-324](https://issues.couchbase.com/browse/CXXCBC-324): Port and network name now checked on session restart, improving performance during rebalance ([#401](https://github.com/couchbaselabs/couchbase-cxx-client/pull/401)).
* [CXXCBC-323](https://issues.couchbase.com/browse/CXXCBC-323): `bootstrap_timeout` and `resolve_timeout` can now be used in the connection string ([#400](https://github.com/couchbaselabs/couchbase-cxx-client/pull/400)).
* Introduced `dump_configuration` option for debugging. ([#398](https://github.com/couchbaselabs/couchbase-cxx-client/pull/398)) It logs cluster configuration at trace level.

### [](#version-4-1-3-13-april-2023)Version 4.1.3 (13 April 2023)

API documentation: <https://docs.couchbase.com/sdk-api/couchbase-php-client-4.1.3>

| Source   | [couchbase-4.1.3.tgz](https://packages.couchbase.com/clients/php/couchbase-4.1.3.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.1.3.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.1.3.sha256sum) |

#### [](#enhancements-14)Enhancements

* [PCBC-915](https://issues.couchbase.com/browse/PCBC-915): Fixed incorrect handling of timestamps as expiry in mutation options ([#88](https://github.com/couchbase/couchbase-php-client/pull/88)).
* [PCBC-828](https://issues.couchbase.com/browse/PCBC-828): Implemented collection management ([#89](https://github.com/couchbase/couchbase-php-client/pull/89)).
* [PCBC-918](https://issues.couchbase.com/browse/PCBC-918): Extra attributes in `ExistsResult` (`deleted`, `expiry`, `flags`, and `sequenceNumber`) are now optional ([#95](https://github.com/couchbase/couchbase-php-client/pull/95)).

#### [](#underlying-c-sdk-core-3)Underlying C++ SDK Core

* [CXXCBC-31](https://issues.couchbase.com/browse/CXXCBC-31): Allow the use of schemaless connection strings (e.g. `"cb1.example.com,cb2.example.com"`) ([#394](https://github.com/couchbaselabs/couchbase-cxx-client/pull/395)).
* [CXXCBC-318](https://issues.couchbase.com/browse/CXXCBC-318): Always try TCP if UDP fails in DNS-SRV resolver ([#390](https://github.com/couchbaselabs/couchbase-cxx-client/pull/390)).
* [CXXCBC-320](https://issues.couchbase.com/browse/CXXCBC-320): Negative expiry in atr was leaving docs in a stuck state — this has been fixed, with expiry atr now becoming an `int32_t`([#393](https://github.com/couchbaselabs/couchbase-cxx-client/pull/393)).
* [CXXCBC-310](https://issues.couchbase.com/browse/CXXCBC-310): Improved shutdown of the `LostTxnCleanup` thread ([#389](https://github.com/couchbaselabs/couchbase-cxx-client/pull/389)).

### [](#version-4-1-2-20-march-2023)Version 4.1.2 (20 March 2023)

API documentation: <https://docs.couchbase.com/sdk-api/couchbase-php-client-4.1.2>

| Source   | [couchbase-4.1.2.tgz](https://packages.couchbase.com/clients/php/couchbase-4.1.2.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.1.2.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.1.2.sha256sum) |

#### [](#enhancements-15)Enhancements

* [PCBC-888](https://issues.couchbase.com/browse/PCBC-888): Added new method `Collection#queryIndexes` that allows to manage query indexes defined for the collection ([#68](https://github.com/couchbase/couchbase-php-client/pull/68)).
* Added optional context to `CouchbaseException` constructor ([#85](https://github.com/couchbase/couchbase-php-client/pull/85)).

#### [](#underlying-c-sdk-core-4)Underlying C++ SDK Core

* [CXXCBC-144](https://issues.couchbase.com/browse/CXXCBC-144): Search query on collections no longer requires you to pass in the scope name — it is inferred from the index ([#379](https://github.com/couchbaselabs/couchbase-cxx-client/pull/379)).
* [CXXCBC-145](https://issues.couchbase.com/browse/CXXCBC-145): Search query request, raw option added ([#380](https://github.com/couchbaselabs/couchbase-cxx-client/pull/380)).
* [CXXCBC-194](https://issues.couchbase.com/browse/CXXCBC-194): The SDK now supports the `ExtThreadSafe` transaction extension ([#374](https://github.com/couchbaselabs/couchbase-cxx-client/pull/374), [#376](https://github.com/couchbaselabs/couchbase-cxx-client/pull/376)).
* [CXXCBC-316](https://issues.couchbase.com/browse/CXXCBC-316): When a document is removed in a transaction, and then a call made to `get_optional`, we expect to just get an empty optional. However, the handling was raising a `transaction_operation_failed`This has been fixed, and an `empty optional` will now be returned ([#385](https://github.com/couchbaselabs/couchbase-cxx-client/pull/385)).
* [CXXCBC-310](https://issues.couchbase.com/browse/CXXCBC-310): Fixed race condition in transaction\_context state machine ([#386](https://github.com/couchbaselabs/couchbase-cxx-client/pull/386), [#378](https://github.com/couchbaselabs/couchbase-cxx-client/pull/378)).

### [](#version-4-1-1-22-february-2023)Version 4.1.1 (22 February 2023)

API documentation: <https://docs.couchbase.com/sdk-api/couchbase-php-client-4.1.1>

| Source   | [couchbase-4.1.1.tgz](https://packages.couchbase.com/clients/php/couchbase-4.1.1.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.1.1.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.1.1.sha256sum) |

#### [](#enhancements-16)Enhancements

* [PCBC-869](https://issues.couchbase.com/browse/PCBC-869): Implemented `changePassword` for management API ([#55](https://github.com/couchbase/couchbase-php-client/pull/55), [#56](https://github.com/couchbase/couchbase-php-client/pull/56))
* [PCBC-891](https://issues.couchbase.com/browse/PCBC-891): Append extension version info to HELLO indentifier ([#58](https://github.com/couchbase/couchbase-php-client/pull/58))
* [PCBC-901](https://issues.couchbase.com/browse/PCBC-901): Attach error details to management exceptions ([#71](https://github.com/couchbase/couchbase-php-client/pull/71))
* Increase required PHP version up to 8.0 ([#76](https://github.com/couchbase/couchbase-php-client/pull/76))

#### [](#fixes-10)Fixes

* [PCBC-890](https://issues.couchbase.com/browse/PCBC-890): Scope must implement ScopeInterface ([#57](https://github.com/couchbase/couchbase-php-client/pull/57))
* [PCBC-899](https://issues.couchbase.com/browse/PCBC-899): Ensure the connection will be closed on error ([#70](https://github.com/couchbase/couchbase-php-client/pull/70))
* [PCBC-900](https://issues.couchbase.com/browse/PCBC-900): Don't set "function" property on exceptions. ([#74](https://github.com/couchbase/couchbase-php-client/pull/74))
* [PCBC-905](https://issues.couchbase.com/browse/PCBC-905): Don't dereference empty optional if option is not set ([#75](https://github.com/couchbase/couchbase-php-client/pull/75))
* [PCBC-907](https://issues.couchbase.com/browse/PCBC-907): Assign meta to view query result ([#79](https://github.com/couchbase/couchbase-php-client/pull/79))
* Fix missing header for GCC 13 ([#63](https://github.com/couchbase/couchbase-php-client/pull/63))

#### [](#underlying-c-sdk-core-5)Underlying C++ SDK Core

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
    * Don't allow to copy `mcbp_message` objects ([#345](https://github.com/couchbaselabs/couchbase-cxx-client/pull/345))
    * Avoid extra allocation and initialization ([#344](https://github.com/couchbaselabs/couchbase-cxx-client/pull/344))
* Build system fixes:

  * Fix build with gcc-13 ([#372](https://github.com/couchbaselabs/couchbase-cxx-client/pull/372))
  * Fix gcc 12 issue ([#367](https://github.com/couchbaselabs/couchbase-cxx-client/pull/367))
* Enhancements:

  * Include bucketless KV service when ping is requested. ([#339](https://github.com/couchbaselabs/couchbase-cxx-client/pull/339))
  * Include OS name in SDK identifier ([#349](https://github.com/couchbaselabs/couchbase-cxx-client/pull/349))

### [](#version-4-1-0-20-january-2023)Version 4.1.0 (20 January 2023)

Version 4.1.0 brings a number of improvements related to internal connection behavior.

API documentation: <https://docs.couchbase.com/sdk-api/couchbase-php-client-4.1.0>

| Source   | [couchbase-4.0.0.tgz](https://packages.couchbase.com/clients/php/couchbase-4.1.0.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.0.0.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.1.0.sha256sum) |

#### [](#new-features)New Features

* [PCBC-824](https://issues.couchbase.com/browse/PCBC-824): Implemented replica reads.
* [PCBC-630](https://issues.couchbase.com/browse/PCBC-630): Implemented legacy durability for mutations (replicateTo/persistTo options)
* [PCBC-880](https://issues.couchbase.com/browse/PCBC-880): Support for configuration profiles

#### [](#fixes-11)Fixes

* [PCBC-889](https://issues.couchbase.com/browse/PCBC-889): Fixed behaviour of 'skip' SearchOption.
* Bug fixes: logger and build improvements

#### [](#caveats)Caveats

There are no pre-built binaries for the Windows platform of PHP SDK 4.1.0\. But there are steps in [WINDOWS.md](https://github.com/couchbase/couchbase-php-client/blob/4.1.0/WINDOWS.md), that describe how to build an extension along with PHP interpreter.

## [](#php-sdk-4-0-releases)PHP SDK 4.0 Releases

PHP SDK 4.0 is written to [version 3.3 of the SDK API specification](compatibility.md#api-version)(and matching the features available in Couchbase 7.1 and earlier).

### [](#version-4-0-0-11-may-2022)Version 4.0.0 (11 May 2022)

Version 4.0.0 is the first major release of the next generation PHP SDK, built on the Couchbase++ library — featuring multi-document distributed ACID transactions, and bringing a number of improvements related to internal connection behavior.

API documentation: <https://docs.couchbase.com/sdk-api/couchbase-php-client-4.0.0>

| Source   | [couchbase-4.0.0.tgz](https://packages.couchbase.com/clients/php/couchbase-4.0.0.tgz)             |
| -------- | ------------------------------------------------------------------------------------------------- |
| Checksum | [couchbase-4.0.0.sha256sum](https://packages.couchbase.com/clients/php/couchbase-4.0.0.sha256sum) |

#### [](#new-features-2)New Features

* [PCBC-806](https://issues.couchbase.com/browse/PCBC-806): Migrated core to Couchbase++.
* [PCBC-797](https://issues.couchbase.com/browse/PCBC-797): Updated the Query Index management API to use scopes and collections.
* [PCBC-836](https://issues.couchbase.com/browse/PCBC-836): Added support for the Transactions API.

#### [](#caveats-2)Caveats

There are no pre-built binaries for the Windows platform of PHP SDK 4.0.0\. But there are steps in [WINDOWS.md](https://github.com/couchbase/couchbase-php-client/blob/4.0.0/WINDOWS.md), that describe how to build an extension along with PHP interpreter.

## [](#older-releases)Older Releases

See:

* The [3.x PHP Release Notes & Download Archive](https://docs-archive.couchbase.com/php-sdk/3.2/project-docs/sdk-release-notes.html).
* Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/php-sdk/2.6/sdk-release-notes.html).