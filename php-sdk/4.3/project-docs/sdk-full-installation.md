---
title: Full Installation
description: Installation instructions, and download archive for the Couchbase PHP Client.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.3/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.3@php-sdk:project-docs:sdk-full-installation.adoc[]
---

[View original HTML](/php-sdk/4.3/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions, and download archive for the Couchbase PHP Client. 

For release notes, download links, and installation methods for [earlier releases of the Couchbase PHP Client](#older-releases), see below.

The Couchbase PHP SDK generally tracks PHP’s own [supported versions](https://www.php.net/supported-versions.php), and recommends the most recent "Active Support" version, except as specified in our documentation and especially the [release notes](sdk-release-notes.md).

As of June 2024, these versions are PHP 8.3 (Latest Active Support), 8.2 (Active Support), and 8.1 (Security Support) — see the table below for [supported versions and dates](#php-version-compatibility).

## [](#sdk-installation)SDK Installation

### [](#installing-on-mac-and-linux-systems)Installing on Mac and Linux systems

Before installing the PHP SDK, the following dependencies must be installed. We recommend using OS specific utilities such as `brew`, `apt-get`, and similar package management utilities (depending on your environment):

* cmake >= 3.20.0+
* c++ compiler >= std\_17
* openssl >= 1.1+

For more details regarding platform support refer to the [Compatibility page](compatibility.md#os-compatibility).

> [!IMPORTANT]
> When installing OpenSSL via `brew install` on **macOS**, the command will not be sufficient to be able to build. The easiest way to fix this is to add the `OPENSSL_ROOT_DIR` env variable to your exports (e.g., .zshenv).
> 
> ```console
> $ export OPENSSL_ROOT_DIR=/usr/local/opt/openssl/
> ```
> 
> If you have any issues setting this up, see the tips mentioned when you run `brew info openssl`.

Now, install the Couchbase PHP SDK through your PHP distribution’s `pecl` command:

```console
$ pecl install couchbase
```

Or install from the Couchbase repository:

```console
$ pecl install https://packages.couchbase.com/clients/php/couchbase-4.0.0.tgz
```

Then follow the [post-installation steps](#post-installation).

> [!IMPORTANT]
> New SDK Versions on Old Operating System Versions
> 
> This SDK runs on top of the C++ core, Couchbase++, which requires a C++ 17 compiler, such as GCC 8.0, or more recent versions.
> 
> Older versions of Debian and Ubuntu ship with an older version of GCC — and RHEL and CentOS also lack a supported version of PHP.
> 
> Workarounds are available for installing a newer build chain for RHEL and CentOS with [EPEL](https://fedoraproject.org/wiki/EPEL), but this may not be within your company’s policy, so also take a look at container options.

#### [](#alpine-linux)Alpine Linux

**Alpine Linux** is very slim and uses `musl libc` and the `apk` package manager. As a result, the installation is a little different from other Unix-Like systems, and `pecl` equivalent packages are used instead.

Using `apk`, you would install your preferred `php` version, install `libcouchbase`, and then install the equivalent `pecl` package for the version of `php` that you’re using.

```console
$ apk add php81
$ apk add php81-pecl-couchbase
```

Then follow the [post-installation steps](#post-installation).

### [](#installing-on-microsoft-windows)Installing on Microsoft Windows

When using Microsoft Windows, instead of using PECL, download the pre-built binary package matching your environment. You may also download the [php-couchbase source code](https://github.com/couchbase/php-couchbase) for the SDK and build it directly in your environment if you have a complete build toolchain.

From [PHP SDK version 4.2.1](sdk-release-notes.md#version-4-2-1-23-april-2024)Windows binaries are available to download — see the [Release Notes page](sdk-release-notes.md) for links to the binary built for your preferred PHP version.

For older versions of the PHP 4.x SDK, there are no pre-built binaries for the Windows platform. Instead, you will need to follow [these steps](https://github.com/couchbase/couchbase-php-client/blob/4.0.0/WINDOWS.md) to build an extension along with the PHP interpreter. We recommend always running the latest version of the SDK.

### [](#post-installation)Post Installation for All Platforms

Once the PHP SDK has been installed, you need to specify that the PHP interpreter should load the Couchbase PHP SDK as an extension. To do this:

1. Locate your `php.ini` file. This can be done using the command `php --ini`  
```console  
$ php --ini  
Configuration File (php.ini) Path: /usr/local/etc/php/8.1  
Loaded Configuration File:         /usr/local/etc/php/8.1/php.ini  
Scan for additional .ini files in: /usr/local/etc/php/8.1/conf.d  
Additional .ini files parsed:      (none)  
```
2. Insert a line in the `php.ini` file specifying the extension to be loaded; this should be in the `[PHP]` section. If you don’t know where that is, simply search for existing commented or uncommented `extension=` entries in the file.  
```ini  
extension=json      ; not needed with PHP 8.0.0+  
extension=couchbase  
```  
> [!NOTE]  
> On PHP version 7.2.0 and up, simply using the extension name is preferred. Previously, you might have used `couchbase.so` or `couchbase.dll`, depending on your platform.

### [](#php-composer)PHP Composer

Once the PHP extension is installed, it may be used as any other PHP library through composer as posted at [packagist.org](https://packagist.org/packages/couchbase/couchbase).

Ensure that you have installed [Composer](https://getcomposer.org/doc/00-intro.md) successfully — you can verify your installation with:

```console
$ composer --version
Composer version 2.3.5 2022-04-13 16:43:00
```

To add Couchbase to your project’s dependency list, simply update your `composer.json` file with the following dependencies:

```json
"require": {
  ...
  "ext-couchbase": "^4.0",
  "couchbase/couchbase": "^4.0"
}
```

Run `composer update` to lock the change in the generated `composer.lock` file.

### [](#note-on-extension-dependencies)Note on Extension Dependencies

The Couchbase SDK depends on the [JSON extension](https://www.php.net/manual/en/json.installation.php), which must be loaded before the SDK. However, it is already included on PHP 8.0.0+ as a core extension.

## [](#older-releases)Older Releases

See:

* The [3.x PHP Release Notes & Download Archive](https://docs-archive.couchbase.com/php-sdk/3.2/project-docs/sdk-release-notes.html).
* Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/php-sdk/2.6/sdk-release-notes.html).