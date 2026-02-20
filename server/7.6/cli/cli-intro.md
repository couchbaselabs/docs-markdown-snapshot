---
title: CLI Reference
description: The command-line interface (CLI) tools let you manage and monitor
  your Couchbase Server installation including clusters, servers, vBuckets, and
  XDCR.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cli-intro.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:cli:cli-intro.adoc[]
---

[View original HTML](/server/7.6/cli/cli-intro.html)

# CLI Reference

> The command-line interface (CLI) tools let you manage and monitor your Couchbase Server installation including clusters, servers, vBuckets, and XDCR. 

The Couchbase Server installation process installs the command-line tools. After installation, the location of these tools depends on your platform:

| Operating System | Directory Locations                                                                                                                                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux            | /opt/couchbase/bin /opt/couchbase/bin/install /opt/couchbase/bin/tools                                                                                                                                                                   |
| Windows          | C:\\Program Files\\couchbase\\server\\bin C:\\Program Files\\couchbase\\server\\bin\\install C:\\Program Files\\couchbase\\server\\bin\\tools                                                                                            |
| Mac OS X         | /Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin /Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/tools /Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/install |

## [](#managing-diagnostics)Managing Diagnostics

The command-line interface provides commands to start, stop, and report status for log collection. You can collect diagnostics through the command-line interface by using the [couchbase-cli](cbcli/couchbase-cli.md) or the [cbcollect\_info](cbcollect-info-tool.md) tool.

## [](#server-tools-packages)Server Tools Packages

For convenience, Couchbase provides the Server developer tools package and the Server admin tools package.

### [](#server-developer-tools-package)Server Developer Tools Package

The Server developer tools package lets you install the following EE Server utilities on the systems where you have not installed Couchbase Server:

* [cbbackupmgr](../backup-restore/cbbackupmgr.md)
* [cbexport](../tools/cbexport.md)
* [cbimport](../tools/cbimport.md)
* [cbq](cbq-tool.md)

Download the command line tools package for your platform from the following links:

* Linux: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-dev-tools-7.6.8-linux%5Fx86%5F64.tar.gz>
* Linux aarch64: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-dev-tools-7.6.8-linux%5Faarch64.tar.gz>
* macOS: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-dev-tools-7.6.8-macos%5Fx86%5F64.zip>
* macOS arm64: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-dev-tools-7.6.8-macos%5Farm64.zip>
* Windows: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-dev-tools-7.6.8-windows%5Famd64.zip>

Unzip or untar the packages, and the binaries are ready to run. For example:

```console
wget https://packages.couchbase.com/releases/7.6.8/couchbase-server-dev-tools-7.6.8-linux_x86_64.tar.gz

tar -xf couchbase-server-dev-tools-7.6.8-linux_x86_64.tar.gz
```

Each package also contains a `README` file and a copy of the software license.

> [!NOTE]
> On Windows, you must have a recent version of the Microsoft Visual C++ Redistributable runtime libraries installed. If you do not have these libraries installed, download them from [Microsoft Visual C++ Redistributable latest supported downloads](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

### [](#server-admin-tools-package)Server Admin Tools Package

The Server admin tools package lets you install the following Server utilities on the systems where you have not installed Couchbase Server:

* [cbbackupmgr](../backup-restore/cbbackupmgr.md)
* [cbc](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5F2cbc.html)
* [cbdatarecovery](../tools/cbdatarecovery.md)
* [cbexport](../tools/cbexport.md)
* [cbimport](../tools/cbimport.md)
* [cbq](cbq-tool.md)
* [cbstats](cbstats-intro.md)
* [couchbase-cli](cbcli/couchbase-cli.md)
* [mcstat](mcstat.md)
* [mctimings](mctimings.md)
* [mctestauth](mctestauth.md)

Download the command line tools package for your platform from the following links:

* Linux: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-admin-tools-7.6.8-linux%5Fx86%5F64.tar.gz>
* Linux aarch64: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-admin-tools-7.6.8-linux%5Faarch64.tar.gz>
* macOS: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-admin-tools-7.6.8-macos%5Fx86%5F64.zip>
* macOS arm64: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-admin-tools-7.6.8-macos%5Farm64.zip>
* Windows: <https://packages.couchbase.com/releases/7.6.8/couchbase-server-admin-tools-7.6.8-windows%5Famd64.zip>

Unzip or untar the packages, and the binaries are ready to run. For example:

```console
wget https://packages.couchbase.com/releases/7.6.8/couchbase-server-admin-tools-7.6.8-linux_x86_64.tar.gz

tar -xf couchbase-server-admin-tools-7.6.8-linux_x86_64.tar.gz
```

Each package also contains a `README` file and a copy of the software license.

> [!NOTE]
> On Windows, you must have a recent version of the Microsoft Visual C++ Redistributable runtime libraries installed. If you do not have these libraries installed, download them from [Microsoft Visual C++ Redistributable latest supported downloads](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).

## [](#version-compatibility)Version Compatibility

The versions of the utilities installed by the tools package are the same as the corresponding Couchbase Server installation package.

For the Server developer tools package, the 7.6.8 version of the utilities `cbimport`, `cbexport`, `cbbackupmgr`, and `cbq` are compatible with the following Couchbase Server versions:

* 7.6.0, 7.6.1, 7.6.2, 7.6.3
* 7.2.x
* 7.1.x
* 7.0.x

You can download and use the latest version of the utilities (`cbimport`, `cbexport`, `cbbackupmgr`, and `cbq`) with earlier Couchbase Server versions.

For the Server admin tools package, do the following:

* Use the `--version` option to get the version of the utility. However, for the `cbc` utility, use the `cbc version` option.
* `couchbase-cli` is a utility for administering the Couchbase cluster. Make sure that the versions of `couchbase-cli` and the Couchbase cluster match.
* For all utilities, a feature that exists in a latest Server version only is not supported by an earlier version utility.