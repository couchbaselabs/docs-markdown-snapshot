---
title: Command Line Tools
description: Use Couchbase command line tools to import and export large amounts
  of data, and manage ad hoc backups.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/reference/pages/command-line-tools.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:reference:command-line-tools.adoc[]
---

[View original HTML](/cloud/reference/command-line-tools.html)

# Command Line Tools

> Use Couchbase command line tools to import and export large amounts of data, and manage ad hoc backups. 

Couchbase Server includes a suite of command line tools, available as a separate package for Couchbase Capella. Couchbase command line tools for Capella include [cbimport and cb export](../connect/cli-import-export.md), [cbbackupmgr](../clusters/cli-backup-restore.md), [cbdatarecovery](../../server/current/tools/cbdatarecovery.md)and [cbq](../n1ql/n1ql-intro/cbq.md).

## [](#download-and-install-the-couchbase-command-line-tools)Download and Install the Couchbase Command Line Tools

Download the version of the command line tools package for your platform through the following links:

Linux

<https://packages.couchbase.com/releases/7.6.6/couchbase-server-dev-tools-7.6.6-linux%5Fx86%5F64.tar.gz>

Linux aarch64

<https://packages.couchbase.com/releases/7.6.6/couchbase-server-dev-tools-7.6.6-linux%5Faarch64.tar.gz>

macOS

<https://packages.couchbase.com/releases/7.6.6/couchbase-server-dev-tools-7.6.6-macos%5Fx86%5F64.zip>

macOS arm64

<https://packages.couchbase.com/releases/7.6.6/couchbase-server-dev-tools-7.6.6-macos%5Farm64.zip>

Windows

<https://packages.couchbase.com/releases/7.6.6/couchbase-server-dev-tools-7.6.6-windows%5Famd64.zip>

Unzip or untar the packages, and the binaries are ready to run. The zipped package also contains a `README` file, and a copy of the software licenses.

For example, for Linux x86\_64:

```console
$ mkdir capella_server_tools_7.6.6
```

```console
$ cd capella_server_tools_7.6.6
```

```console
$ wget https://packages.couchbase.com/releases/7.6.6/couchbase-server-dev-tools_7.6.6-linux_x86_64.tar.gz
```

```console
$ tar -xf couchbase-server-dev-tools_7.6.6-linux_x86_64.tar.gz
```

```console
$ ls -1
bin
couchbase-server-dev-tools_7.6.6-linux_x86_64.tar.gz
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
cbimport version 7.6.6-4200 (192d7500)
```

```console
$ ./cbexport --version
cbexport version 7.6.6-4200 (192d7500)
```

```console
$ ./cbbackupmgr --version
cbbackupmgr version 7.6.6-4200 (192d7500)
```

```console
$ ./cbdatarecovery --version
cbdatarecovery version 7.6.6-4200 (192d7500)
```

```console
$ ./cbq --version
 GO VERSION : go1.22.2
 SHELL VERSION : 7.6.6-4200

 Use N1QL queries select version(); or select min_version(); to display server version.
```

> [!TIP]
> On Windows, you will need to have a recent Microsoft Visual C++ Redistributable already installed. Download the latest Visual C++ Redistributable from [Microsoft Visual C++ Redistributable latest supported downloads](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

### [](#apple-m1-silicon)Apple M1 Silicon

The macOS x86 binaries can be used on Apple Silicon Macs with Rosetta installed. If your Apple Silicon Mac does not already have Rosetta installed, you can install it from the command line, using:

```console
softwareupdate --install-rosetta
```

## [](#other-cli-tools)Other CLI Tools

The Couchbase C SDK, `libcouchbase`, also includes some command line tools. For more information about these command line tools, see [cbc Tools](../../c-sdk/current/hello-world/cbc.md#cbc-tools).

### [](#couchbase-shell-cbsh)Couchbase Shell (cbsh)

Couchbase Shell (cbsh) is an interactive command-line tool for working with Couchbase Server and Capella clusters.

Use cbsh to:

* Extract, transform, and load different data formats.
* Export data as JSON or CSV.
* Import data from SQLite.
* Generate data.
* Check the status of your indexes.

To download, install, and get started with cbsh, see the [Couchbase Shell Documentation](https://couchbase.sh/docs/).

### [](#ide-plugins)IDE Plugins

For more information about IDE plugins, see the [Third Party Integrations page](../third-party/integrations.md#ide-integrations).

## [](#next-steps)Next Steps

To start using the command line tools, you must do the following:

* [Copy the connection string](../get-started/connect.md) for your cluster.
* [Configure cluster access](../clusters/manage-database-users.md) by creating cluster access credentials. You’ll need the username and password for the cluster credentials to connect to the cluster.
* [Add your IP address](../clusters/allow-ip-address.md) to the cluster’s list of allowed IPs.

You can do all of this from a single location using the Connect page in the Capella UI. See [Connect To Your Cluster](../get-started/connect.md) and follow the instructions for the CLI tools.