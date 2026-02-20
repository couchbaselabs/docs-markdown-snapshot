---
title: Browser and CLI Access
description: Web and command line interfaces to Couchbase Server are available.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/hello-world/pages/cbc.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:c-sdk:hello-world:cbc.adoc[]
---

[View original HTML](/c-sdk/current/hello-world/cbc.html)

# Browser and CLI Access

> Web and command line interfaces to Couchbase Server are available. Installation of the cbc command line tools is covered here, and links are given to the man pages, for full usage instuctions. The Web console is documented in the Server docs. 

Web and command line interfaces to Couchbase Server are available. The cbc command line tools are a part of libcouchbase, with installation documented below, whilst Web console access is provided in Couchbase Server — [see links](#couchbase-web-console-document-query-access).

## [](#command-line)Command Line

You can access documents in Couchbase using command line interfaces. Libcouchbase (LCB), our C SDK, includes the `cbc` tools. This is in addition to the [command line tools](../../../server/current/cli/cli-intro.md) integrated into Couchbase Server to manage the cluster and to collect diagnostics.

A version of LCB ships with some releases of Couchbase Server, but here we are assuming you want to install the command line tools on a client machine, or to acquire the latest version. To install the cbc command line tools, install _libcouchbase_:

If you already have LCB installed, then [skip ahead to our summary of tools included on cbc](#cbc-tools).

## [](#platform-support-and-installation)Platform support and installation

The Couchbase C SDK can be installed via apt or yum repositories on GNU/Linux; homebrew on Mac OS X; and [binary archives for Microsoft Windows](#install-windows). It may also be [built from source](https://github.com/couchbase/libcouchbase) on any of the platforms mentioned above, and more.

## [](#installing-on-gnulinux)Installing on GNU/Linux

The various Linux distributions contain the following packages:

* `**libcouchbase3**`: The core library package.
* `**libcouchbase-dev**` (or `**libcouchbase-devel**`): The development package, required if building SDKs which depend on the C SDK.
* `**libcouchbase3-tools**`: The command line utilities (`**cbc**` and others).
* `**libcouchbase3-libevent**`: Optional but recommended component for I/O performance. Can also be used to integrate with libevent (see [Asynchronous Programming](../howtos/concurrent-async-apis.md)).
* `**libcouchbase3-libev**`: Optional, for use with applications that make use of event loop integration with libev (see [Asynchronous Programming](../howtos/concurrent-async-apis.md)). To install the C SDK from a static binary package or by manually configuring the repositories, you can use the following procedures.

### [](#configuring-yum-repositories-centos-redhat)Configuring yum repositories (CentOS, Redhat)

This section assumes you know how to add an external [yum](http://yum.baseurl.org/) repository and Linux quick start explains the steps it will perform on your distribution. To configure the repository:

1. Find the appropriate repository location for your distribution in the following table.

| Version             | Architecture | Repository                                                          |
| ------------------- | ------------ | ------------------------------------------------------------------- |
| Amazon Linux 2023   | 64-bit       | https://packages.couchbase.com/clients/c/repos/rpm/amzn2023/x86\_64 |
| Amazon Linux 2      | AArch64      | https://packages.couchbase.com/clients/c/repos/rpm/amzn2/aarch64    |
| Amazon Linux 2      | 64-bit       | https://packages.couchbase.com/clients/c/repos/rpm/amzn2/x86\_64    |
| Enterprise Linux 8  | 64-bit       | https://packages.couchbase.com/clients/c/repos/rpm/el8/x86\_64      |
| Enterprise Linux 9  | 64-bit       | https://packages.couchbase.com/clients/c/repos/rpm/el9/x86\_64      |
| Enterprise Linux 10 | 64-bit       | https://packages.couchbase.com/clients/c/repos/rpm/el10/x86\_64     |

1. Create a `couchbase.repo` file in your `/etc/yum.repos.d` directory. It should look similar to the following:

```toml
[couchbase]
enabled = 1
name = libcouchbase package for centos10 x86_64
baseurl = https://packages.couchbase.com/clients/c/repos/rpm/el10/x86_64
gpgcheck = 1
gpgkey = https://packages.couchbase.com/clients/c/repos/rpm/couchbase.key
```

### [](#configuring-apt-repositories-debian-ubuntu)Configuring APT repositories (Debian, Ubuntu)

This section assumes some knowledge of [apt](https://wiki.debian.org/Apt) and Linux quick start explains the steps it will perform on your distribution. To configure the repository:

1. Download the Couchbase GPG key from <https://packages.couchbase.com/clients/c/repos/deb/couchbase.key>
2. Add the key to the list of trusted package keys. Use the `apt-key add` command. For example, `apt-key add couchbase.key`.
3. Create a couchbase.list file in `/etc/apt/sources.list.d`. The file should contain the repository for your distribution. Repositories are available for the following distributions:

| Distribution           | Repository Entry                                                                       |
| ---------------------- | -------------------------------------------------------------------------------------- |
| Ubuntu 22.04 ("jammy") | deb https://packages.couchbase.com/clients/c/repos/deb/ubuntu2204 jammy jammy/main     |
| Ubuntu 24.04 ("noble") | deb https://packages.couchbase.com/clients/c/repos/deb/ubuntu2404 noble noble/main     |
| Debian 11 ("bullseye") | deb https://packages.couchbase.com/clients/c/repos/deb/debian11 bullseye bullseye/main |
| Debian 12 ("bookworm") | deb https://packages.couchbase.com/clients/c/repos/deb/debian12 bookworm bookworm/main |

Note that only Ubuntu LTS (long term support) releases are supported. You may try to use an LTS repository for a non-LTS version, but success is not guaranteed.

Now that you have the repository configured, refresh the cache then check to see that you have been successful:

```console
$ sudo apt update
```

```console
$ sudo apt search libcouchbase
```

You should see something like:

```console
libcouchbase-dbg - library for the Couchbase protocol, debug symbols
libcouchbase-dev - library for the Couchbase protocol, development files
libcouchbase3 - library for the Couchbase protocol, core files
libcouchbase3-libev - library for the Couchbase protocol (libev backend)
libcouchbase3-libevent - library for the Couchbase protocol (libevent backend)
libcouchbase3-tools - library for the Couchbase protocol
```

Now, install `libcouchbase3`, and any other packages that you need for development:

```console
$ sudo apt install libcouchbase3 libcouchbase-dev libcouchbase3-tools libcouchbase-dbg libcouchbase3-libev libcouchbase3-libevent
```

For CentOS and Red Hat, the equivalent commands are:

```console
$ sudo yum check-update
```

```console
$ sudo yum search libcouchbase
```

### [](#installing-binary-packages-without-a-repository)Installing binary packages without a repository

You can install standalone packages by downloading a tarball containing the necessary binary packages for your platform.

**Installing RPMs**

The following commands show steps to execute on **CentOS 7** box. For other RPM-based distributions — such as Amazon Linux 2023 — the steps are the same or similar.

```console
$ curl -O https://packages.couchbase.com/clients/c/libcouchbase-3.3.12_centos7_x86_64.tar
```

```console
$ tar xf libcouchbase-3.3.12_centos7_x86_64.tar
```

```console
$ cd libcouchbase-3.3.12_centos7_x86_64
```

```console
$ sudo yum install -y libcouchbase3{-tools,-libevent,}-3.3.12*.rpm libcouchbase-devel-*.rpm
```

```console
> ...
> Installed:
>   libcouchbase-devel.x86_64 0:3.3.12-1.el7
>   libcouchbase3.x86_64 0:3.3.12-1.el7
>   libcouchbase3-libevent.x86_64 0:3.3.12-1.el7
>   libcouchbase3-tools.x86_64 0:3.3.12-1.el7
> ...
>
> Complete!
```

**Installing DEBs**

The following commands show steps to execute on **Debian 10 (buster)** box, see table below for other DEB-based distributions.

```console
$ curl -O https://packages.couchbase.com/clients/c/libcouchbase-3.3.1_debian10_buster_amd64.tar
```

```console
$ tar xf libcouchbase-3.3.1_debian10_buster_amd64.tar
```

```console
$ cd libcouchbase-3.3.1_debian10_buster_amd64
```

```console
$ sudo apt install libevent-core-2.1
```

```console
$ sudo dpkg -i libcouchbase3{-tools,-libevent,}_3.3.1*.deb libcouchbase-dev*.deb
```

```console
$ sudo dpkg -i libcouchbase3{-tools,-libevent,}_3.2.0*.deb libcouchbase-dev*.deb
> Selecting previously unselected package libcouchbase3-tools.
> (Reading database ... 7177 files and directories currently installed.)
> Preparing to unpack libcouchbase3-tools_3.2.0-1_amd64.deb ...
> Unpacking libcouchbase3-tools (3.2.0-1) ...
> Selecting previously unselected package libcouchbase3-libevent:amd64.
> Preparing to unpack libcouchbase3-libevent_3.2.0-1_amd64.deb ...
> Unpacking libcouchbase3-libevent:amd64 (3.2.0-1) ...
> Selecting previously unselected package libcouchbase3:amd64.
> Preparing to unpack libcouchbase3_3.2.0-1_amd64.deb ...
> Unpacking libcouchbase3:amd64 (3.2.0-1) ...
> Selecting previously unselected package libcouchbase-dev:amd64.
> Preparing to unpack libcouchbase-dev_3.2.0-1_amd64.deb ...
> Unpacking libcouchbase-dev:amd64 (3.2.0-1) ...
> Setting up libcouchbase3:amd64 (3.2.0-1) ...
> Setting up libcouchbase-dev:amd64 (3.2.0-1) ...
> Setting up libcouchbase3-libevent:amd64 (3.2.0-1) ...
> Setting up libcouchbase3-tools (3.2.0-1) ...
> Processing triggers for libc-bin (2.28-10) ...
```

## [](#installation-from-source)Installation from source

You may install the library from source either by downloading a source archive, or by checking out the [git repository](https://github.com/couchbase/libcouchbase). Follow the instructions in the archive’s [README](https://github.com/couchbase/libcouchbase/blob/master/README.markdown) for further instructions.

## [](#installation-on-mac-os-x)Installation on Mac OS X

To install the library on Mac OS X, first install the de-facto package manager for OS X: [homebrew](https://brew.sh/). Once _homebrew_ is configured:

```console
$ brew update # get list of latest packages
```

```console
$ brew install libcouchbase
```

To install development files and command line tools on Mac OS, follow the instructions for [installing from source](https://github.com/couchbase/libcouchbase/blob/master/README.markdown#building-on-unix-like-systems).

## [](#install-windows)Windows Installation

Windows binary packages can be found as downloads for each version listed below. Included are the header files, release and debug variants of the DLLs and import libraries, and release and debug variants of the command line tools. Note that the C SDK does not have any preferred installation path, and it is up to you to determine where to place `libcouchbase.dll`.

Be sure to select the proper package for the compiler and architecture your application is using. Binaries are linked from the release notes page for each libcouchbase release — we strongly recommend [downloading the latest release](../project-docs/sdk-release-notes.md#latest-release).

> [!NOTE]
> If there are no binaries available for your Visual Studio version, then using a binary from any other Visual Studio version is _likely_ to work. Most of the issues related to mixing Visual Studio binary versions involve changing and incompatible C APIs or incompatible C Runtime (CRT) objects and functions. Since the Couchbase C SDK does not expose a C API, and since it does not directly expose any CRT functionality, it should be safe for use so long as your application can link to the library at compile-time. The windows runtime linker will ensure that each binary is using the appropriate version of the Visual C Runtime (`MSVCRT.DLL`).

If for some reason you cannot use any of the prebuilt Windows binaries, follow the instructions in [_installation from source_ (above)](#installation-from-source) to build on Windows.

## [](#verifying-installed-package)Verifying Installed Package

The easiest way to verify installed package is to check its version using cbc tools. It requires package **libcouchbase3-tools** installed on Linux systems, for Windows **cbc.exe** included in the zip archive. To verify the client run **cbc version** (**cbc.exe version** on Windows). It shows version along with git commit numbers. Then it prints default directory where IO plugins installed and enumerates the currently installed and available plugins. After that it reports whether OpenSSL linked to this particular version of libcouchbase, and displays the version number if it is accessible.

```console
$ cbc version
cbc:
  Runtime: Version=3.2.0, Changeset=c712686af5825f2f05c89112e555cd09906aa727
  Headers: Version=3.2.0, Changeset=c712686af5825f2f05c89112e555cd09906aa727
  Build Timestamp: 2021-07-20 09:31:59
  Default plugin directory: /usr/lib64/libcouchbase
  IO: Default=libevent, Current=libevent, Accessible=libevent,select
  SSL Runtime: OpenSSL 1.1.1g FIPS  21 Apr 2020
  SSL Headers: OpenSSL 1.1.1g FIPS  21 Apr 2020
  Snappy: 1.1.8
  Tracing: SUPPORTED
  System: Linux-4.15.0-91-generic; x86_64
  CC: GNU 8.4.1; -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fno-strict-aliasing -ggdb3 -pthread
  CXX: GNU 8.4.1; -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fno-strict-aliasing -ggdb3 -pthread
```

## [](#cbc-tools)cbc Tools

The `cbc` tools are documented in their respective `man` pages. Links to online versions in the latest API docs are provided below. They are fairly stable utilities, and do not tend to change across LCB versions, however, you can see all recent updates [on their GitHub page](https://github.com/couchbase/libcouchbase/tree/master/doc/man).

* [cbc](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/md%5Fdoc%5F2cbc.html): `cbc` is a utility for communicating with a Couchbase cluster.
* [cbcrc](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/md%5Fdoc%5F2cbcrc.html): `cbcrc` is an optional configuration file used to provide default values for the `cbc` and `cbc-pillowfight` utilities.
* [cbc-subdoc](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/md%5Fdoc%5F2cbc-subdoc.html): `cbc-subdoc` runs an interactive shell with commands from subdocument API.
* [cbc-pillowfight](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/md%5Fdoc%5F2cbc-pillowfight.html): `cbc-pillowfight` is a stress test for Couchbase Client and Cluster. It creates a specified number of threads each looping and performing get and set operations within the cluster.
* [cbc-n1qlback](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/md%5Fdoc%5F2cbc-n1qlback.html): `cbc-n1qlback` creates a specified number of threads each executing a set of user defined queries.

## [](#couchbase-web-console-document-query-access)Couchbase Web Console Document & Query Access

You can use the Couchbase Web Console to view, edit, and create JSON documents up to 256KB in size — see the [Couchbase Web Console](../../../server/current/manage/manage-ui/manage-ui.md) in the Server docs.

You can also use the [Query Workbench](../../../server/current/tools/query-workbench.md) to issue SQL++ (formerly N1QL) queries using the web console.