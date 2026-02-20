---
title: CLI Reference
description: Couchbase Server command-line interface (CLI) tools are provided to
  manage and monitor clusters, servers, vBuckets, XDCR, and so on.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cli-intro.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:cli:cli-intro.adoc[]
---

[View original HTML](/server/7.2/cli/cli-intro.html)

# CLI Reference

> Couchbase Server command-line interface (CLI) tools are provided to manage and monitor clusters, servers, vBuckets, XDCR, and so on. 

By default, the CLI tools are installed into the following locations on each platform:

| Operating System | Directory Locations                                                                                                                                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Linux            | _/opt/couchbase/bin_, _/opt/couchbase/bin/install_, and _/opt/couchbase/bin/tools_                                                                                                                                                             |
| Windows          | _C:\\Program Files\\couchbase\\server\\bin_, _C:\\Program Files\\couchbase\\server\\bin\\install_, and _C:\\Program Files\\couchbase\\server\\bin\\tools_.                                                                                     |
| Mac OS X         | _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin_ _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/tools_ _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/install_ |

## [](#managing-diagnostics)Managing diagnostics

The command-line interface provides commands to start, stop, and report status for log collection. You can collect diagnostics through the command-line interface by using either the [couchbase-cli](cbcli/couchbase-cli.md) tool or the [cbcollect\_info](cbcollect-info-tool.md) cbcollect\_info tool.

## [](#server-tools-packages)Server Tools Packages

For convenience, the following EE Server utilities are also available in a tools package that you can download — [cbimport](../tools/cbimport.md), [cbexport](../tools/cbexport.md), and [cbbackupmgr](../backup-restore/cbbackupmgr.md). This allows developers, testers, and others to use the tools from machines on which Couchbase Server is not installed.

Download the command line tools package for your platform through the following links:

* <https://packages.couchbase.com/releases/7.2.2/couchbase-server-tools%5F7.2.2-linux%5Fx86%5F64.tar.gz>
* <https://packages.couchbase.com/releases/7.2.2/couchbase-server-tools%5F7.2.2-linux%5Faarch64.tar.gz>
* <https://packages.couchbase.com/releases/7.2.2/couchbase-server-tools%5F7.2.2-macos%5Fx86%5F64.zip>
* <https://packages.couchbase.com/releases/7.2.2/couchbase-server-tools%5F7.2.2-macos%5Farm64.zip>
* <https://packages.couchbase.com/releases/7.2.2/couchbase-server-tools%5F7.2.2-windows%5Famd64.zip>

Unzip or untar the packages, and the binaries are ready to run. For example:

```console
wget https://packages.couchbase.com/releases/7.2.2/couchbase-server-tools_7.2.2-linux_x86_64.tar.gz
tar -xf couchbase-server-tools_7.2.2-linux_x86_64.tar.gz
```

Each package also contains a `README` file, and a copy of the software license.

Note that on Windows, a recent Microsoft Visual C Redistributable must already have been installed. Download the latest Visual C Redistributable from [Microsoft Visual C++ Redistributable latest supported downloads](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

## [](#version-compatibility)Version Compatibility

The versions of the utilities are the same as the Couchbase Server versions that the utilities are from.

The 7.2.2 `cbimport`, `cbexport`, and `cbbackupmgr` utilities can be run against the following Couchbase Server versions:

* 7.2.x
* 7.1.x
* 7.0.x