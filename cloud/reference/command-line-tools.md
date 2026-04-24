---
title: Command Line Tools
description: Use Couchbase command line tools to import and export data, manage
  backups, and interact with your cluster from the command line.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/reference/pages/command-line-tools.adoc
pubDate: 2026-04-24T05:30:11.901Z
link: xref:cloud:reference:command-line-tools.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/reference/command-line-tools.html)

# Command Line Tools

> Use Couchbase command line tools to import and export data, manage backups, and interact with your cluster from the command line. 

Couchbase Server includes a suite of command line tools, available as a separate package for Couchbase Capella. Couchbase command line tools for Capella include [cbimport and cbexport](#couchbase-cli-tools), [cbbackupmgr](#couchbase-cli-tools), [cbdatarecovery](#couchbase-cli-tools), and [cbq](#couchbase-cli-tools), as well as [Couchbase Shell (cbsh)](#cb-shell) and [cbc Tools](#cbc-tools).

## [](#cb-shell)Couchbase Shell

Couchbase Shell (`cbsh`) is an interactive command-line tool for working with Couchbase Server and Capella operational clusters.

Use `cbsh` to:

* Run SQL++ queries against your cluster.
* Import and export data in multiple formats.
* Manage documents, buckets, scopes, and collections.
* Manage Capella clusters, projects, and credentials.
* Perform vector searches.

To download, install, and get started with `cbsh`, see the [Couchbase Shell Documentation](https://couchbase.sh/docs/).

## [](#couchbase-cli-tools)Couchbase Command Line Tools

The following command line tools are included in the Couchbase Server command line tools package:

[cbimport and cbexport](../connect/cli-import-export.md)

Import and export data in JSON and CSV format. `cbimport` supports importing from files or URLs; `cbexport` supports exporting to files.

[cbbackupmgr](../clusters/cli-backup-restore.md)

Back up and restore data from Couchbase Server and Capella clusters. `cbbackupmgr` supports full and incremental backups, as well as point-in-time restore.

[cbdatarecovery](../../server/current/tools/cbdatarecovery.md)

Recover data from offline or failed-over nodes.

[cbq](../n1ql/n1ql-intro/cbq.md)

An interactive shell for running SQL++ queries against Couchbase Server and Capella clusters.

### [](#download-and-install-command-line-tools)Download and Install Command Line Tools

Download the command line tools package that corresponds to the server version you're using.

> [!NOTE]
> While command line tools for 7.6.X are not forward compatible with 8.0.X, command line tools for 8.0.X are backward compatible with 7.6.X.

* Couchbase Server 8.0.X
* Couchbase Server 7.6.X

Linux

<https://packages.couchbase.com/releases/8.0.1/couchbase-server-dev-tools-8.0.1-linux%5Fx86%5F64.tar.gz>

Linux aarch64

<https://packages.couchbase.com/releases/8.0.1/couchbase-server-dev-tools-8.0.1-linux%5Faarch64.tar.gz>

macOS x86

<https://packages.couchbase.com/releases/8.0.1/couchbase-server-dev-tools-8.0.1-macos%5Fx86%5F64.zip>

macOS arm64

<https://packages.couchbase.com/releases/8.0.1/couchbase-server-dev-tools-8.0.1-macos%5Farm64.zip>

Windows

<https://packages.couchbase.com/releases/8.0.1/couchbase-server-dev-tools-8.0.1-windows%5Famd64.zip>

> [!TIP]
> On Windows, you need a recent Microsoft Visual C++ Redistributable installed. Download the latest Visual C++ Redistributable from [Microsoft Visual C++ Redistributable latest supported downloads](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

Unzip or untar the packages, and the binaries are ready to run. The extracted package also contains a `README` file and the software licenses.

For example, for Linux x86\_64:

```console
$ wget https://packages.couchbase.com/releases/8.0.1/couchbase-server-dev-tools_8.0.1-linux_x86_64.tar.gz
```

```console
$ tar -xf couchbase-server-dev-tools_8.0.1-linux_x86_64.tar.gz
```

```console
$ ls -1
bin
couchbase-server-dev-tools_8.0.1-linux_x86_64.tar.gz
lib
LICENSE.txt
NOTICES.txt
README.txt
share
```

```console
$ cd bin
```

```console
$ ls -1
cbbackupmgr
cbdatarecovery
cbexport
cbimport
cbq
```

```console
$ ./cbimport --version
cbimport version 8.0.1-4792 (983714b2)
```

```console
$ ./cbexport --version
cbexport version 8.0.1-4792 (983714b2)
```

```console
$ ./cbbackupmgr --version
cbbackupmgr version 8.0.1-4792 (983714b2)
```

```console
$ ./cbdatarecovery --version
cbdatarecovery version 8.0.1-4792 (983714b2)
```

```console
$ ./cbq --version
 GO VERSION : go1.25.5
 SHELL VERSION : 8.0.1-4792

 Use N1QL queries select version(); or select min_version(); to display server version.
```

Linux

<https://packages.couchbase.com/releases/7.6.11/couchbase-server-dev-tools-7.6.11-linux%5Fx86%5F64.tar.gz>

Linux aarch64

<https://packages.couchbase.com/releases/7.6.11/couchbase-server-dev-tools-7.6.11-linux%5Faarch64.tar.gz>

macOS x86

<https://packages.couchbase.com/releases/7.6.11/couchbase-server-dev-tools-7.6.11-macos%5Fx86%5F64.zip>

macOS arm64

<https://packages.couchbase.com/releases/7.6.11/couchbase-server-dev-tools-7.6.11-macos%5Farm64.zip>

Windows

<https://packages.couchbase.com/releases/7.6.11/couchbase-server-dev-tools-7.6.11-windows%5Famd64.zip>

> [!TIP]
> On Windows, you need a recent Microsoft Visual C++ Redistributable installed. Download the latest Visual C++ Redistributable from [Microsoft Visual C++ Redistributable latest supported downloads](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

Unzip or untar the packages, and the binaries are ready to run. The extracted package also contains a `README` file and the software licenses.

For example, for Linux x86\_64:

```console
$ wget https://packages.couchbase.com/releases/7.6.11/couchbase-server-dev-tools_7.6.11-linux_x86_64.tar.gz
```

```console
$ tar -xf couchbase-server-dev-tools_7.6.11-linux_x86_64.tar.gz
```

```console
$ ls -1
bin
couchbase-server-dev-tools_7.6.11-linux_x86_64.tar.gz
lib
LICENSE.txt
NOTICES.txt
README.txt
share
```

```console
$ cd bin
```

```console
$ ls -1
cbbackupmgr
cbdatarecovery
cbexport
cbimport
cbq
```

```console
$ ./cbimport --version
cbimport version 7.6.11-8495 (e9a7a0ae)
```

```console
$ ./cbexport --version
cbexport version 7.6.11-8495 (e9a7a0ae)
```

```console
$ ./cbbackupmgr --version
cbbackupmgr version 7.6.11-8495 (e9a7a0ae)
```

```console
$ ./cbdatarecovery --version
cbdatarecovery version 7.6.11-8495 (e9a7a0ae)
```

```console
$ ./cbq --version
 GO VERSION : go1.25.8
 SHELL VERSION : 7.6.11-8495

 Use N1QL queries select version(); or select min_version(); to display server version.
```

## [](#cbc-tools)cbc Tools

The Couchbase C SDK, `libcouchbase`, includes a small set of command line tools. For more information, see [cbc Tools](../../c-sdk/current/hello-world/cbc.md#cbc-tools).

## [](#see-also)See Also

Couchbase also offers plugins and extensions for popular IDEs, so you can work with your Capella cluster directly from your development environment. For a full list of available integrations, see [Integrations, Connectors, and Tools](../third-party/integrations.md#ide-integrations).

### [](#next-steps)Next Steps

To start using command line tools, do the following:

1. [Copy the connection string](../get-started/connect.md) for your cluster.
2. [Configure cluster access](../clusters/manage-database-users.md) by creating cluster access credentials.  
You'll need the username and password for the cluster credentials to connect to the cluster.
3. [Add your IP address](../clusters/allow-ip-address.md) to the cluster's list of allowed IPs.