---
title: SDK Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase C Client, libcouchbase (LCB).
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/project-docs/pages/sdk-release-notes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:c-sdk:project-docs:sdk-release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/project-docs/sdk-release-notes.html)

# SDK Release Notes

> Release notes, installation instructions, and download archive for the Couchbase C Client, libcouchbase (LCB). 

These pages cover the 3.x versions of the Couchbase C SDK. For release notes, download links, and installation methods for 2.10 and earlier releases of the Couchbase C Client, please see the [2.x C Release Notes & Download Archive](#2.10@c-sdk::sdk-release-notes.adoc).

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

You may install the library from source either by downloading a source archive, or by checking out the [git repository](https://github.com/couchbase/libcouchbase). Follow the instructions in the archive's [README](https://github.com/couchbase/libcouchbase/blob/master/README.markdown) for further instructions.

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

Be sure to select the proper package for the compiler and architecture your application is using. Binaries are linked from the release notes page for each libcouchbase release — we strongly recommend [downloading the latest release](#latest-release).

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

## [](#latest-release)C SDK 3.3 Releases

We always recommend using the latest version of the SDK — it contains all of the latest security patches and support for new and upcoming features. All patch releases for each dot minor release should be API compatible, and safe to upgrade; any changes to expected behavior are noted in the release notes that follow.

### [](#version-3-3-18-10-september-2025)Version 3.3.18 (10 September 2025)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/index.html)

This is a maintenance release.

* [CCBC-1672](https://issues.couchbase.com/browse/CCBC-1672): Fixed a protocol violation on new connections. In certain cases, extra bytes could be sent at the start of a new connection. Most of the time, this caused the server to drop the connection and the client would reconnect automatically, so users did not notice. However, in rare cases the server would accept the data as valid, leading to protocol issues. This has been corrected so that invalid data is properly discarded and connections stay consistent.
* [CCBC-1671](https://issues.couchbase.com/browse/CCBC-1671): Sending requests to all replica nodes for strategy "ANY". This change makes implementation of `get_any_replica` behave the same way as other SDKs.

  * The old behavior: "get any replica" would send requests sequentially one by one. So that the next request will be dispatched only when previous fails.
  * The new behavior: "get any replica" send requests to active and replica nodes simulaneously and returns only first response to the user, discarding everything else.
* [CCBC-1669](https://issues.couchbase.com/browse/CCBC-1669): `get_all_replicas` will no longer fail if all possible nodes are not available — and now only fail if no nodes are available.
* [CCBC-1668](https://issues.couchbase.com/browse/CCBC-1668): The client has stopped assuming that missing active node means none available for a replica read. With this change reading a replica will be more reliable during failover and rebalance events.
* [CCBC-1667](https://issues.couchbase.com/browse/CCBC-1667): No longer scheduling a config update during instance termination. This change fixes use-after-free during `lcb_destroy`.
* [CCBC-1674](https://issues.couchbase.com/browse/CCBC-1674): No longer using non-owning spans to release memory with `NETBUF_LIBC_PROXY`. This fixes use-after-free for build with `NETBUF_LIBC_PROXY` when snappy compression is enabled. This is a special build when caching allocator is replaced with just libc malloc. It is used only during development and testing, and never enabled in production.
* [CCBC-1673](https://issues.couchbase.com/browse/CCBC-1673): No longer returning block with `deallocs` as free in `find_free_block` of the `netbuf` subsystem.
* Raised minimum `cmake` version to 3.17.
* Log local port to make it easier to correlate with the Server logs.

#### [](#downloads)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.18.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18.sha256.txt)                                             |
| Source Archive                | Any          | [libcouchbase-3.3.18.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.18\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2023             | aarch64      | [libcouchbase-3.3.18\_amzn2023\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Famzn2023%5Faarch64.tar)                  |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.18\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Famzn2%5Fx86%5F64.tar)                       |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.18\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Famzn2%5Faarch64.tar)                        |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.18\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | aarch64      | [libcouchbase-3.3.18\_rhel8\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Frhel8%5Faarch64.tar)                        |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.18\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Frhel9%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | aarch64      | [libcouchbase-3.3.18\_rhel9\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Frhel9%5Faarch64.tar)                        |
| Enterprise Linux 10           | x86\_64      | [libcouchbase-3.3.18\_rhel10\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Frhel10%5Fx86%5F64.tar)                     |
| Enterprise Linux 10           | aarch64      | [libcouchbase-3.3.18\_rhel10\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Frhel10%5Faarch64.tar)                      |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.18\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | aarch64      | [libcouchbase-3.3.18\_ubuntu2204\_jammy\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fubuntu2204%5Fjammy%5Farm64.tar)   |
| Ubuntu 24.04 (noble)          | x86\_64      | [libcouchbase-3.3.18\_ubuntu2404\_noble\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fubuntu2404%5Fnoble%5Famd64.tar)   |
| Ubuntu 24.04 (noble)          | aarch64      | [libcouchbase-3.3.18\_ubuntu2404\_noble\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fubuntu2404%5Fnoble%5Farm64.tar)   |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.18\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Debian 11 (bullseye)          | aarch64      | [libcouchbase-3.3.18\_debian11\_bullseye\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fdebian11%5Fbullseye%5Farm64.tar) |
| Debian 12 (bookworm)          | x86\_64      | [libcouchbase-3.3.18\_debian12\_bookworm\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fdebian12%5Fbookworm%5Famd64.tar) |
| Debian 12 (bookworm)          | aarch64      | [libcouchbase-3.3.18\_debian12\_bookworm\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fdebian12%5Fbookworm%5Farm64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.18\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.18\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.18\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2022 (VC17)     | x86\_64      | [libcouchbase-3.3.18\_vc17\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc17%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.18\_vc14\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc14%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.18\_vc15\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc15%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.18\_vc16\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc16%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2022 TLS (VC17) | x86\_64      | [libcouchbase-3.3.18\_vc17\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.18%5Fvc17%5Famd64%5Fopenssl3.zip)         |

### [](#version-3-3-17-11-june-2025)Version 3.3.17 (11 June 2025)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.17/index.html)

This is a maintenance release.

* [CCBC-1666](https://issues.couchbase.com/browse/CCBC-1666): Configuration manager was not correctly handling `LCB_ERR_REQUEST_CANCELED` during instance destruction. With completion-based IO (`libuv`, Windows `IOCP`), the library could try to schedule a configuration update on an already deallocated pipeline and cause a use-after-free condition. To fix the issue, the configuration manager has now been updated to handle `LCB_ERR_REQUEST_CANCELED` and return without issuing a new request.

#### [](#downloads-2)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.17.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17.sha256.txt)                                             |
| Source Archive                | Any          | [libcouchbase-3.3.17.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.17\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.17\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.17\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | aarch64      | [libcouchbase-3.3.17\_rhel8\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Frhel8%5Faarch64.tar)                        |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.17\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Frhel9%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | aarch64      | [libcouchbase-3.3.17\_rhel9\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Frhel9%5Faarch64.tar)                        |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.17\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | aarch64      | [libcouchbase-3.3.17\_ubuntu2204\_jammy\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fubuntu2204%5Fjammy%5Farm64.tar)   |
| Ubuntu 24.04 (noble)          | x86\_64      | [libcouchbase-3.3.17\_ubuntu2404\_noble\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fubuntu2404%5Fnoble%5Famd64.tar)   |
| Ubuntu 24.04 (noble)          | aarch64      | [libcouchbase-3.3.17\_ubuntu2404\_noble\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fubuntu2404%5Fnoble%5Farm64.tar)   |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.17\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Debian 11 (bullseye)          | aarch64      | [libcouchbase-3.3.17\_debian11\_bullseye\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fdebian11%5Fbullseye%5Farm64.tar) |
| Debian 12 (bookworm)          | x86\_64      | [libcouchbase-3.3.17\_debian12\_bookworm\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fdebian12%5Fbookworm%5Famd64.tar) |
| Debian 12 (bookworm)          | aarch64      | [libcouchbase-3.3.17\_debian12\_bookworm\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fdebian12%5Fbookworm%5Farm64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.17\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.17\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.17\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2022 (VC17)     | x86\_64      | [libcouchbase-3.3.17\_vc17\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc17%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.17\_vc14\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc14%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.17\_vc15\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc15%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.17\_vc16\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc16%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2022 TLS (VC17) | x86\_64      | [libcouchbase-3.3.17\_vc17\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.17%5Fvc17%5Famd64%5Fopenssl3.zip)         |

### [](#version-3-3-16-01-june-2025)Version 3.3.16 (01 June 2025)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.16/index.html)

This is a maintenance release and includes several bugs fixes and stability improvements. Most notably it brings enhancements in "Faster Failover" algorithm implementation that is supported by the recent server releases.

* [CCBC-1664](https://issues.couchbase.com/browse/CCBC-1664): Register read event watcher for KV socket if duplex is enabled. Fixes missing configuration updates on newer server versions (7.6.5+).
* [CCBC-1662](https://issues.couchbase.com/browse/CCBC-1662): Ignore server-side notification during bootstrap. Libcouchbase reports protocol error and stop bootstrapping the connection if the server sends configuration notification during the initial handshake.
* Define `LCB_CC_STRING` for MS VS 17 to fix packaging scripts.
* [CCBC-1658](https://issues.couchbase.com/browse/CCBC-1658): Added support for encrypted TLS keys. The key password should be specified in connection options with `lcb_createopts_tls_key_password()`.

#### [](#downloads-3)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.16.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16.sha256.txt)                                             |
| Source Archive                | Any          | [libcouchbase-3.3.16.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.16\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.16\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.16\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | aarch64      | [libcouchbase-3.3.16\_rhel8\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Frhel8%5Faarch64.tar)                        |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.16\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Frhel9%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | aarch64      | [libcouchbase-3.3.16\_rhel9\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Frhel9%5Faarch64.tar)                        |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.16\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | aarch64      | [libcouchbase-3.3.16\_ubuntu2204\_jammy\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fubuntu2204%5Fjammy%5Farm64.tar)   |
| Ubuntu 24.04 (noble)          | x86\_64      | [libcouchbase-3.3.16\_ubuntu2404\_noble\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fubuntu2404%5Fnoble%5Famd64.tar)   |
| Ubuntu 24.04 (noble)          | aarch64      | [libcouchbase-3.3.16\_ubuntu2404\_noble\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fubuntu2404%5Fnoble%5Farm64.tar)   |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.16\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Debian 11 (bullseye)          | aarch64      | [libcouchbase-3.3.16\_debian11\_bullseye\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fdebian11%5Fbullseye%5Farm64.tar) |
| Debian 12 (bookworm)          | x86\_64      | [libcouchbase-3.3.16\_debian12\_bookworm\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fdebian12%5Fbookworm%5Famd64.tar) |
| Debian 12 (bookworm)          | aarch64      | [libcouchbase-3.3.16\_debian12\_bookworm\_arm64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fdebian12%5Fbookworm%5Farm64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.16\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.16\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.16\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2022 (VC17)     | x86\_64      | [libcouchbase-3.3.16\_vc17\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc17%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.16\_vc14\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc14%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.16\_vc15\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc15%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.16\_vc16\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc16%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2022 TLS (VC17) | x86\_64      | [libcouchbase-3.3.16\_vc17\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.16%5Fvc17%5Famd64%5Fopenssl3.zip)         |

### [](#version-3-3-15-14-december-2024)Version 3.3.15 (14 December 2024)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.15/index.html)

* [CCBC-1652](https://issues.couchbase.com/browse/CCBC-1652): Allow to force SASL when client certificate is being used.
* Windows binaries now linked with OpenSSL 3.

#### [](#downloads-4)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.15.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15.sha256.txt)                                             |
| Source Archive                | Any          | [libcouchbase-3.3.15.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.15\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.15\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.15\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.15\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.15\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Ubuntu 24.04 (noble)          | x86\_64      | [libcouchbase-3.3.15\_ubuntu2404\_noble\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fubuntu2404%5Fnoble%5Famd64.tar)   |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.15\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Debian 12 (bookworm)          | x86\_64      | [libcouchbase-3.3.15\_debian12\_bookworm\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fdebian12%5Fbookworm%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.15\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.15\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.15\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2022 (VC17)     | x86\_64      | [libcouchbase-3.3.15\_vc17\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc17%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.15\_vc14\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc14%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.15\_vc15\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc15%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.15\_vc16\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc16%5Famd64%5Fopenssl3.zip)         |
| Visual Studio 2022 TLS (VC17) | x86\_64      | [libcouchbase-3.3.15\_vc17\_amd64\_openssl3.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.15%5Fvc17%5Famd64%5Fopenssl3.zip)         |

### [](#version-3-3-14-12-november-2024)Version 3.3.14 (12 November 2024)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.14/index.html)

* [CCBC-1653](https://jira.issues.couchbase.com/browse/CCBC-1653): Libcouchbase now correctly honors the timeout setting for Analytics query, when it is changed to a non-default value.
* [CCBC-1651](https://jira.issues.couchbase.com/browse/CCBC-1651): Previously, the library did not release memory of the packets that never got a chance to be flushed to the network buffer, if libcouchbase was still trying to connect sockets. This has been fixed, so that purged packets get their memory released, it thus fixes a memory leak in case of network issues.
* [CCBC-1646](https://jira.issues.couchbase.com/browse/CCBC-1646): Implemented Server groups for replica reads — allow to restrict replica set to a selected server group. This feature allows to implement network optimization when traffic cost between server groups is higher than in the local group. In this case the application might select preferred server group in the connection options, and later opt-in for local operations during replica reads.
* [CCBC-1555](https://jira.issues.couchbase.com/browse/CCBC-1555): Removed extra prefix in tapset probes.
* [CCBC-1598](https://jira.issues.couchbase.com/browse/CCBC-1598): Fixed documentation issues for cbc tools.
* Fixed tests on 7.6 Server.

#### [](#downloads-5)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.14.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14.sha256.txt)                                             |
| Source Archive                | Any          | [libcouchbase-3.3.14.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.14\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.14\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.14\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.14\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.14\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Ubuntu 24.04 (noble)          | x86\_64      | [libcouchbase-3.3.14\_ubuntu2404\_noble\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fubuntu2404%5Fnoble%5Famd64.tar)   |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.14\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Debian 12 (bookworm)          | x86\_64      | [libcouchbase-3.3.14\_debian12\_bookworm\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fdebian12%5Fbookworm%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.14\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.14\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.14\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.14\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.14\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.14\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.14%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-13-13-september-2024)Version 3.3.13 (13 September 2024)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.13/index.html)

* [CCBC-1647](https://jira.issues.couchbase.com/browse/CCBC-1647): Server-side query timeout (status 1080) is now handled correctly.
* [CCBC-1643](https://jira.issues.couchbase.com/browse/CCBC-1643): Fixed memory leak of pending buffers in IO context.
* [CCBC-1645](https://jira.issues.couchbase.com/browse/CCBC-1645): Explicit initialization for `OpenSSL` is no longer required (from version 1.1+), and has been removed.
* Fix build with `-DLCB_DUMP_PACKETS=ON`.
* Fix `pkg-config` for MacOS.

#### [](#downloads-6)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.13.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.13.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.13\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.13\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.13\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.13\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.13\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Ubuntu 24.04 (noble)          | x86\_64      | [libcouchbase-3.3.13\_ubuntu2404\_noble\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fubuntu2404%5Fnoble%5Famd64.tar)   |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.13\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Debian 12 (bookworm)          | x86\_64      | [libcouchbase-3.3.13\_debian12\_bookworm\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fdebian12%5Fbookworm%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.13\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.13\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.13\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.13\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.13\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.13\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.13%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-12-2-march-2024)Version 3.3.12 (2 March 2024)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.12/index.html)

* [CCBC-1636](https://issues.couchbase.com/browse/CCBC-1636): The library was not deallocating the old packet after setting the collection ID field in the copy. `mcreq_renew_packet()` requires the caller to deallocate original copy, otherwise the memory will be only released by pipeline destructor. This has been addressed, and old packets are now deallocated when the collection ID is updated, freeing up memory.
* [CCBC-1634](https://issues.couchbase.com/browse/CCBC-1634): Fixed the reporting of unresponsive nodes in `lcb_ping()`.

  * No longer retrying NOOP commands, as they might be routed to different pipeline, instead fail fast NOOPs to reflect network issues more precisely.
  * Now using pipeline address as ping entry identifier instead of socket address, as socket may not exist (not connected), owing to network failures.
  * `lcb_ping` must still now report, even when overall status is not `LCB_SUCCESS`, so `cbc-ping` should still try to print report instead of just printing overall status code.
* [CCBC-1630](https://issues.couchbase.com/browse/CCBC-1630): Check collection id before storing packet to pipeline. Every time `check_collection_id()` is invoked, the caller should ensure that this function potentially is rewriting the packet, if it decides to insert/update an encoded collection ID. This will help to avoid problems when running in mixed mode — during an upgrade rebalance from Server 6.6 to 7.2, for instance.
* [CCBC-1627](https://issues.couchbase.com/browse/CCBC-1627): Fixed `bodylen` value when `ffextlen` (flexible frame extra length) is not zero.

#### [](#downloads-7)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.12.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.12.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.12\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.12\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.12\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.12\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.12\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.12\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.12\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.12\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.12\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.12\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.12\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.12\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.12\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.12\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.12\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.12\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.12\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.12\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.12\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.12%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-11-21-december-2023)Version 3.3.11 (21 December 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.11/index.html)

* [CCBC-1618](https://issues.couchbase.com/browse/CCBC-1618): Updated query error codes for dynamic authenticator. This is an update to the internal interface, that allows more granular detection of stale authentication conditions for the Query Service.
* Prevent full rebuild on every run of `cmake`. The SDK no longer renders the built timestamp into the header, but instead only uses it in the object file.

#### [](#downloads-8)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.11.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.11.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.11\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.11\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.11\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.11\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.11\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.11\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.11\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.11\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.11\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.11\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.11\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.11\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.11\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.11\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.11\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.11\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.11\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.11\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.11\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.11%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-10-10-october-2023)Version 3.3.10 (10 October 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.10/index.html)

* [CCBC-1616](https://issues.couchbase.com/browse/CCBC-1616): A `wait_for_config` check is now applied for all pipelines. Previously, the `lcb_wait` function would wait for the pending configuration updates, but didn't do it if the configuration update operation was being retried. Now, the operation also will not wait for pending configuration updates, rather it will return from `lcb_wait` as soon as the operation completes.

  * The old behaviour still works when `wait_for_config=true` is passed in the connection string (or `LCB_CNTL_WAIT_FOR_CONFIG` is set to non-zero value): in this case the library will wait for the configuration.
  * This setting does not affect the mode when the event loop is executed by the application, and without `lcb_wait`.

#### [](#downloads-9)Downloads

| Platform                      | Architecture | File                                                                                                                                                 |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.10.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.10.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.10\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.10\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.10\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.10\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.10\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.10\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.10\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.10\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.10\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.10\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.10\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.10\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.10\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.10\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.10\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.10\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.10\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.10\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.10\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.10%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-9-22-september-2023)Version 3.3.9 (22 September 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.9/index.html)

* [CCBC-1608](https://issues.couchbase.com/browse/CCBC-1608): Reduced the default timeout for idle HTTP connections to 1 second. The previous default (4.5 seconds) was too close to the 5-second server-side timeout, and could lead to spurious request failures.
* [CCBC-1615](https://issues.couchbase.com/browse/CCBC-1615): Handle rate limit codes during bootstrap.
* [CCBC-1612](https://issues.couchbase.com/browse/CCBC-1612): Improved recovery time during rebalance for upcoming Server releases. In faster failover mode:

  * The CCCP provider will not be throttleed.
  * In case of network errors the configuration will be refreshed, to speed up the recovery process during failover.
* [CCBC-1611](https://issues.couchbase.com/browse/CCBC-1611): To handle `0x0d` (`ECONFIG_ONLY`) status code — we now treat this status code as a signal to refresh the configuration. The new or failed over nodes are set into config-only mode, where all data operations will be failed with code `0x0d`. It is possible that the SDK might be using stale configuration and send requests to the node that is not part of the cluster any more, so to work around this the library will update the configuration and retry the operation.
* [CCBC-1610](https://issues.couchbase.com/browse/CCBC-1610): Fixed a memory issues when setting collection id in the cluster with mixed server versions, where some of the nodes do not support collections (such as in a swap rebalance upgrade).

#### [](#downloads-10)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.9.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.9.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.9\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.9\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.9\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.9\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.9\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.9\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.9\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.9\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.9\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.9\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.9\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.9\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.9\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.9\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.9\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.9\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.9\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.9\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.9\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.9%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-8-16-august-2023)Version 3.3.8 (16 August 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.8/index.html)

* [CCBC-1584](https://issues.couchbase.com/browse/CCBC-1584): Updated documentation on how to use collections with pillowfight.
* [CCBC-1607](https://issues.couchbase.com/browse/CCBC-1607): Fixed collection id encoding in mixed cluster, so that SDK will now work in a mixed environment of collection aware and non-collection aware Server nodes (e.g. 6.6 and 7.0 during an upgrade).
* [CCBC-1602](https://issues.couchbase.com/browse/CCBC-1602): Implemented Faster Failover. This implements the set of protocol optimizations that help the SDK to save network traffic when tracking cluster topology. The feature will be only activated if the server supports it — which is planned for a future Server release.
* [CCBC-1603](https://issues.couchbase.com/browse/CCBC-1603): Do not log if logger is not accessible in `iotssl_log_errors`.
* [CCBC-1599](https://issues.couchbase.com/browse/CCBC-1599): Account NUL-byte when format IPv6 address (fixes potential invalid memory access).

#### [](#downloads-11)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.8.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.8.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8.tar.gz)                                                    |
| Amazon Linux 2023             | x86\_64      | [libcouchbase-3.3.8\_amzn2023\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Famzn2023%5Fx86%5F64.tar)                 |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.8\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.8\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.8\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.8\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.8\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.8\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.8\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.8\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.8\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.8\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.8\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.8\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.8\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.8\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.8\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.8\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.8\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.8\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.8%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-7-11-may-2023)Version 3.3.7 (11 May 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.7/index.html)

* [CCBC-1596](https://issues.couchbase.com/browse/CCBC-1596): Replace unsafe `sprintf` with `snprintf`.
* [CCBC-1597](https://issues.couchbase.com/browse/CCBC-1597): Update threading example, reduce global state.

  * `Json::Reader` uses static global variable, this patch replaces calls to it with `Json::CharReaderBuilder`, which is re-entrant.
  * Constants for tracing system defined as mutable static strings, this patch replaces it with const static strings.
  * Updated examples for thread-safe usage is updated to SDK3 API and added them to the build pipeline

#### [](#downloads-12)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.7.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.7.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.7\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.7\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.7\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.7\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.7\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.7\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.7\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.7\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.7\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.7\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.7\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.7\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.7\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.7\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.7\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.7\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.7\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.7\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.7%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-6-26-april-2023)Version 3.3.6 (26 April 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.6/index.html)

* [CCBC-1590](https://issues.couchbase.com/browse/CCBC-1590): Always pick random node for HTTP services.

It helps with certain edge cases, when the application might spawn a lot of processes, perform queries, so that first queries will be directed to the same node due to the absense of `srand()` call in the library.

* [CCBC-1592](https://issues.couchbase.com/browse/CCBC-1592): Allow to generate more randomized bodies in pillowfight.

By default cbc-pillowfight pre-generates only one document body per selected size. New option `--random-body-pool-size`allows to control how many documents will be generated (default is 100).

This fixes behaviour in the corner case when `--min-size` equals `--max-size` and allow still have many random bodies in this case.

* [CCBC-1595](https://issues.couchbase.com/browse/CCBC-1595): Fix building of the subdocument operation when `--subdoc` switch for pillowfight was used.
* pillowfight: use separate exptime switch for GET.

Do not share the same value of expiry for get operations. Also it does not turn `GET` into `GET_WITH_TOUCH` if the `--get-expiry` is not being used.

* [CCBC-1596](https://issues.couchbase.com/browse/CCBC-1596): Fix various compiler warnings.

#### [](#downloads-13)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.6.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.6.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.6\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.6\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.6\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.6\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.6\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.6\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.6\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.6\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.6\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.6\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.6\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.6\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.6\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.6\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.6\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.6\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.6\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.6\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.6%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-5-9-march-2023)Version 3.3.5 (9 March 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.5/index.html)

* [CCBC-1545](https://issues.couchbase.com/browse/CCBC-1545): Handle `LCB_ERR_REQUEST_CANCELED` in ping callback. If the instance is being destroyed, while the operations in flight, all these operations will be cancelled with error code `LCB_ERR_REQUEST_CANCELED`. Ping implementation should handle this error code and not assume any of the objects (except response) to be in a valid state.
* [CCBC-1586](https://issues.couchbase.com/browse/CCBC-1586): Force SASL PLAIN for TLS connections.
* [CCBC-1589](https://issues.couchbase.com/browse/CCBC-1589): Apply authenticator when passed to `lcb_create`.
* [CCBC-1585](https://issues.couchbase.com/browse/CCBC-1585): Fix build for GCC 13.
* [CCBC-1587](https://issues.couchbase.com/browse/CCBC-1587): Allow to disable uninstall target.

#### [](#downloads-14)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.5.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.5.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.5\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.5\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.5\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.3.5\_rhel8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Frhel8%5Fx86%5F64.tar)                       |
| Enterprise Linux 9            | x86\_64      | [libcouchbase-3.3.5\_rhel9\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Frhel9%5Fx86%5F64.tar)                       |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.5\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.5\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.5\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.5\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.5\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.5\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.5\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.5\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.5\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.5\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.5\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.5\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.5\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.5%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-4-8-february-2023)Version 3.3.4 (8 February 2023)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.4/index.html)

* [CCBC-1583](https://issues.couchbase.com/browse/CCBC-1583): Collections support is disabled in 3.x SDKs if the configuration does not have collections capabilities. Now, it is also disabled when a KV node does not negotiate collection support in HELLO flags. This should help with clusters in mixed mode (with both 6.x and 7.x Server versions) during an upgrade.

#### [](#downloads-15)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.4.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.4.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.4\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.4\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.4\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fcentos7%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.4\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.4\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.4\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.4\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.4\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.4\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.4\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.4\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.4\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.4\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.4\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.4\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.4\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.4%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-3-9-september-2022)Version 3.3.3 (9 September 2022)

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.3/index.html)

* [CCBC-1565](https://issues.couchbase.com/browse/CCBC-1565): load system CAs when the trust certificate is not provided

When the user has not set any root ca provider but is using TLS then we should trust both the system store and the Capella root CA.

* [CCBC-1564](https://issues.couchbase.com/browse/CCBC-1564): update error message for authentication failure
* [CCBC-1568](https://issues.couchbase.com/browse/CCBC-1568): skip logging for closed SSL IO contexts

OpenSSL might still invoke IO callbacks after the actual context has been closed. This more likely could happen with libuv-style IO.

This patch ensures that once socket context has been closed, its pointer in SSL object will be erased.

* Added cbc-bucket-list command to list all buckets.

#### [](#downloads-16)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.3.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.3.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.3\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.3\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.3\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fcentos7%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.3\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.3\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.3\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Ubuntu 22.04 (jammy)          | x86\_64      | [libcouchbase-3.3.3\_ubuntu2204\_jammy\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fubuntu2204%5Fjammy%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.3\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.3\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.3\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.3\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.3\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.3\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.3\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.3\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.3\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.3%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-2-25-august-2022)Version 3.3.2 (25 August 2022)

Version 3.3.2 is the third release of the 3.3 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.2/index.html)

#### [](#bug-fixes)Bug Fixes

* [CCBC-1559](https://issues.couchbase.com/browse/CCBC-1559): `cbc-n1qlback`: give time to IO loop in case of failure.

In scenarios where all query nodes suddenly fail over and/or are removed from the cluster, all requests in `cbc-n1qlback` will start failing. Because libcouchbase knows that the latest config does not have any query nodes, it rejects all queries immediately. The single-threaded nature of libcouchbase does not allow the IO loop to run in background, and the code in the tool does not run `lcb_wait` in case of failure.

As a fix, we run `lcb_tick_nowait` in case of failure, which is enough for libcouchbase to give IO loop a chance to check for any pending events and invoke corresponding callbacks.

#### [](#improvements)Improvements

* [CCBC-1552](https://issues.couchbase.com/browse/CCBC-1552): Libcouchbase may now be built with an external `jsoncpp` library.
* [CCBC-1557](https://issues.couchbase.com/browse/CCBC-1557): Allow caching cluster-level configurations.

The library will cache cluster-level configurations only if the `config_cache=` connection string option is set to directory (ends with '/' symbol), otherwise it will cache only buckets configurations (note that in this case the application should use unique cache name for each bucket, otherwise the library will ignore cache if the bucket name will not match).

#### [](#downloads-17)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.2.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.2.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.2\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.2\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.2\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fcentos7%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.2\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.2\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.2\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.2\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.2\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.2\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.2\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.2\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.2\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.2\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.2\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.2\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.2%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-1-25-may-2022)Version 3.3.1 (25 May 2022)

Version 3.3.1 is the second release of the 3.3 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.1/index.html)

> [!NOTE]
> CentOS 7 RPMs depend on OpenSSL 1.1, which is available in EPEL. Make sure that the `epel-release` package is installed in the system (`yum install epel-release`).

#### [](#bug-fixes-2)Bug Fixes

* [CCBC-1550](https://issues.couchbase.com/browse/CCBC-1550): Fixed RPM packages for CentOS 7, now they will require OpenSSL 1.1 during build. Also build script will not automatically define `LCB_NO_SSL` option if OpenSSL is not found. For builds without TLS support, this option must be explicitly defined.
* [CCBC-1546](https://issues.couchbase.com/browse/CCBC-1546): cbc-pillowfight: add `--rand-space-per-thread` to allow threads to work from different rand numbers.

#### [](#downloads-18)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.1.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.1.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.1\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.1\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.1\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fcentos7%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.1\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.1\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.1\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.1\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.1\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.1\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.1\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.1\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.1\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.1\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.1\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.1\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.1%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-3-0-9-may-2022)Version 3.3.0 (9 May 2022)

Version 3.3.0 is the first release of the 3.3 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.0/index.html)

#### [](#new-features)New Features

* [CCBC-1540](https://issues.couchbase.com/browse/CCBC-1540): The SDK now bundles the Capella CA certificate automatically.

#### [](#bug-fixes-3)Bug Fixes

* [CCBC-1538](https://issues.couchbase.com/browse/CCBC-1538): The SDK now uses a 64-bit integer to store time in the IOCP plugin.
* [CCBC-1526](https://issues.couchbase.com/browse/CCBC-1526): The SDK no longer validates the length of collection specifier. This will be checked on the server-side.
* [CCBC-1527](https://issues.couchbase.com/browse/CCBC-1527): Fixed issue where `Pillowfight` was leaking a large number of memory allocations, which occured during startup. Pillowfight will now deallocate all memory during shutdown.

#### [](#downloads-19)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.3.0.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.3.0.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.3.0\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.3.0\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.3.0\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fcentos7%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.3.0\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.3.0\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.3.0\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.3.0\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.3.0\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.3.0\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.3.0\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.3.0\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.3.0\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.3.0\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.3.0\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.3.0\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.3.0%5Fvc16%5Famd64%5Fopenssl.zip)           |

## [](#c-sdk-3-2-releases)C SDK 3.2 Releases

### [](#version-3-2-4-26-november-2021)Version 3.2.4 (26 November 2021)

Version 3.2.4 is the fifth release of the 3.2 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.2.4/index.html)

* [CCBC-1522](https://issues.couchbase.com/browse/CCBC-1522): Filter `DnsQuery` results on Windows by type: only use records with `DNS_TYPE_SRV` type.
* [CCBC-1521](https://issues.couchbase.com/browse/CCBC-1521): Fixed bootstrap process when client certificate is used. We always pipeline error map request with `HELLO` request, and usually await for `hello`+`error_map` responses, because after that goes SASL authentication (and then optional selection of the bucket) which cannot be completely pipelined. But in case of client certificate, we might terminate bootstrap process too early if the bootstrap process does not require immediate selection of the bucket.
* [CCBC-1432](https://issues.couchbase.com/browse/CCBC-1432)Support for rate limiting error codes: `LCB_ERR_RATE_LIMITED` and `LCB_ERR_QUOTA_LIMITED`.
* [CCBC-1514](https://issues.couchbase.com/browse/CCBC-1514): Do not translate unknown error with "item-only" attribute into `LCB_ERR_CAS_MISMATCH`.
* [CCBC-1515](https://issues.couchbase.com/browse/CCBC-1515): Performance optimization: replace `sstream` with string `append()`. Only if list of IO vectors supplied for value in mutation operations.

#### [](#downloads-20)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.2.4.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.2.4.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.2.4\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.2.4\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.2.4\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.2.4\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.2.4\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.2.4\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.2.4\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.2.4\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.2.4\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.2.4\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.2.4\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.2.4\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.2.4\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.2.4\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.2.4\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.2.4\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.4%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-2-3-20-october-2021)Version 3.2.3 (20 October 2021)

Version 3.2.3 is the fourth release of the 3.2 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.2.3/index.html)

* [CCBC-1484](https://issues.couchbase.com/browse/CCBC-1484): Fixed tracing tags in accordance to RFC.
* [CCBC-1510](https://issues.couchbase.com/browse/CCBC-1510): Fixed key length calculation for exists/get/touch/unlock.
* [CCBC-1495](https://issues.couchbase.com/browse/CCBC-1495): Fixed payload encoding in query index management helpers. Query index management helpers now explicitly declared deperecated.
* [CCBC-1506](https://issues.couchbase.com/browse/CCBC-1506): Duration values now accepted golang style encoding. Connection string and `lcb_cntl_string` now can parse strings with duration encoded in golang style, e.g. `analytics_timeout=5s42us`. The result still converted into 32-bit value with microsecond resolution.
* Improved test coverage, stability and documentation.

#### [](#downloads-21)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.2.3.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.2.3.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3.tar.gz)                                                    |
| Amazon Linux 2                | aarch64      | [libcouchbase-3.2.3\_amzn2\_aarch64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Famzn2%5Faarch64.tar)                        |
| Amazon Linux 2                | x86\_64      | [libcouchbase-3.2.3\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x86\_64      | [libcouchbase-3.2.3\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x86\_64      | [libcouchbase-3.2.3\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x86\_64      | [libcouchbase-3.2.3\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x86\_64      | [libcouchbase-3.2.3\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x86\_64      | [libcouchbase-3.2.3\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x86\_64      | [libcouchbase-3.2.3\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x86\_64      | [libcouchbase-3.2.3\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x86\_64      | [libcouchbase-3.2.3\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x86\_64      | [libcouchbase-3.2.3\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x86\_64      | [libcouchbase-3.2.3\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x86\_64      | [libcouchbase-3.2.3\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x86\_64      | [libcouchbase-3.2.3\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x86\_64      | [libcouchbase-3.2.3\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x86\_64      | [libcouchbase-3.2.3\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.3%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-2-2-23-september-2021)Version 3.2.2 (23 September 2021)

Version 3.2.2 is the third release of the 3.2 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.2.2/index.html)

* [CCBC-1485](https://issues.couchbase.com/browse/CCBC-1485): Allow disabling tracer for connected instance.
* [CCBC-1472](https://issues.couchbase.com/browse/CCBC-1472): Fix handling in case of invalid responses by ensuring strict JSON parsing mode for query meta.
* [CCBC-1494](https://issues.couchbase.com/browse/CCBC-1494): Disconnect logger after `lcb_destroy` invoked to avoid double free errors for some IO backends.
* [CCBC-1457](https://issues.couchbase.com/browse/CCBC-1457): Improve error message when server enforces TLS encryption
* [CCBC-1489](https://issues.couchbase.com/browse/CCBC-1489): Fixed get\_and\_touch to use the correct expiry.
* [CCBC-1487](https://issues.couchbase.com/browse/CCBC-1487): Fixed issue with completion IO where `retryq` erased already sent packets.
* [CCBC-1488](https://issues.couchbase.com/browse/CCBC-1488): Fixed incorrect refcounting in `Connstart`, where an error state followed by cancellation caused an error.
* [CCBC-1479](https://issues.couchbase.com/browse/CCBC-1479): Initialize fields of custom tracer struct, fixing issues during destruction.
* [CCBC-1478](https://issues.couchbase.com/browse/CCBC-1478): Fix issue where successful query returning no results triggered retry when run readonly, resulting in a timeout error.
* [CCBC-1216](https://issues.couchbase.com/browse/CCBC-1216): Implement user impersonation API, for use-cases where SDK performs work on behalf of an application.
* Improved test coverage and stability.

#### [](#downloads-22)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.2.2.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.2.2.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.2.2\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.2.2\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.2.2\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.2.2\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.2.2\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.2.2\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.2.2\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.2.2\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)          | x64          | [libcouchbase-3.2.2\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.2.2\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.2.2\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.2.2\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.2.2\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.2.2\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x64          | [libcouchbase-3.2.2\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.2%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-2-1-20-august-2021)Version 3.2.1 (20 August 2021)

Version 3.2.1 is the second release of the 3.2 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.2.1/index.html)

* [CCBC-1429](https://issues.couchbase.com/browse/CCBC-1429): Fixed positional parameters for query/analtyics:

  * Reverts behaviour `lcb_cmdquery_positional_param` and `lcb_cmdanalytics_positional_param` to append single JSON-encoded value to arguments array.
  * Introduces new functions — `lcb_cmdquery_positional_params` and `lcb_cmdanalytics_positional_params` — that accept all positional arguments at once as JSON-encoded array.
  * Document that old functions will emit compiler warning from 3.3.0 release, and will be removed later.
* [CCBC-1428](https://issues.couchbase.com/browse/CCBC-1428): Clear callback upon error in `lcb_search`.
* [CCBC-1454](https://issues.couchbase.com/browse/CCBC-1454): Fixed compiler warning in `lcb_getreplica`.
* [CCBC-1453](https://issues.couchbase.com/browse/CCBC-1453): Refactored local name caching in `lcbio_cache_local_name` to simplify the code and eliminate compiler warnings.
* [CCBC-1451](https://issues.couchbase.com/browse/CCBC-1451): Fixed strdup usage, in some cases the compiler might choose `strdup` to return `int` instead of `char *` which might lead to memory issues.
* [CCBC-1448](https://issues.couchbase.com/browse/CCBC-1448): Fixed cmake macro for examples. The macro `ADD_EXAMPLE` now correctly updates header directories for generated target.
* [CCBC-1445](https://issues.couchbase.com/browse/CCBC-1445): Always invoke callbacks for pending HTTP operations. When destroying `lcb_INSTANCE` make sure that all HTTP requests (views, query, search, analytics) will have their callbacks invoked.
* [CCBC-1438](https://issues.couchbase.com/browse/CCBC-1438): Fixed frame size for mutations with durability. Counter, Store and Subdoc mutations were sending incorrect frame size of durability encoding, which led to rejection of the command by the server.

#### [](#downloads-23)Downloads

| Platform                               | Architecture | File                                                                                                                                               |
| -------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                              | Any          | [libcouchbase-3.2.1.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1.sha256sum)                                              |
| Source Archive                         | Any          | [libcouchbase-3.2.1.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1.tar.gz)                                                    |
| Amazon Linux 2                         | x64          | [libcouchbase-3.2.1\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Famzn2%5Fx86%5F64.tar)                       |
| Red Hat Enterprise Linux 7             | x64          | [libcouchbase-3.2.1\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fcentos7%5Fx86%5F64.tar)                   |
| Red Hat Enterprise Linux 8             | x64          | [libcouchbase-3.2.1\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)                  | x64          | [libcouchbase-3.2.1\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)                  | x64          | [libcouchbase-3.2.1\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)                   | x64          | [libcouchbase-3.2.1\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)                     | x64          | [libcouchbase-3.2.1\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)                     | x64          | [libcouchbase-3.2.1\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Debian 11 (bullseye)                   | x64          | [libcouchbase-3.2.1\_debian11\_bullseye\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fdebian11%5Fbullseye%5Famd64.tar) |
| Windows (Visual Studio 2015, VC14)     | x64          | [libcouchbase-3.2.1\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fvc14%5Famd64.zip)                              |
| Windows (Visual Studio 2017, VC15)     | x64          | [libcouchbase-3.2.1\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fvc15%5Famd64.zip)                              |
| Windows (Visual Studio 2019, VC16)     | x64          | [libcouchbase-3.2.1\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fvc16%5Famd64.zip)                              |
| Windows (Visual Studio 2015 TLS, VC14) | x64          | [libcouchbase-3.2.1\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Windows (Visual Studio 2017 TLS, VC15) | x64          | [libcouchbase-3.2.1\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Windows (Visual Studio 2019 TLS, VC16) | x64          | [libcouchbase-3.2.1\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.1%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-2-0-20-july-2021)Version 3.2.0 (20 July 2021)

Version 3.2.0 is the first release of the 3.2 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.2.0/index.html)

* [CCBC-1395](https://issues.couchbase.com/browse/CCBC-1395): We no longer expose `LCB_ERR_BUCKET_NOT_FOUND` in operation callbacks. Instead, the operation is automatically retried until timeout.
* [CBCC-1280](https://issues.couchbase.com/browse/CCBC-1280): Support for OpenTelemetry tracing.  
  Tracing updated to allow for an external tracer that creates and finishes spans, adds tags, destroys spans.  Also,  
spans now have the notion of being the 'outer' span.  That is the span that has all the outer span tags, and is the one  
whose duration is used to determine whether or not the operation has exceeded the threshold if the  
ThresholdLoggingTracer is used.  
  If you pass in a parent that is an outer span, you must call `lcbtrace_span_finish` yourself. When an operation  
begins, if there is no parent span passed in, or if there is but it isn't an 'outer' span, then the operation creates  
the outer span itself.  
See `/examples/tracing/otel_tracing.cc` for an example.
* [CCBC-1362](https://issues.couchbase.com/browse/CCBC-1362): Support for metrics.  
  When enabled, by default will output a histogram of latencies for various kv operations plus query, search, analytics  
and view queries.  
  If desired, an external metrics collector can be passed in when the instance is created, which will then be called  
with latencies for each operation.  This can be used to call into an opentelemetry meter for aggregation and export.  
See `/examples/metrics/otel_metrics.cc` for an example.
* [CCBC-1421](https://issues.couchbase.com/browse/CCBC-1421): Allow empty path for subdocument array methods.
* [CCBC-1417](https://issues.couchbase.com/browse/CCBC-1417): Deprecate CAS usage with counter operation.
* [CCBC-1418](https://issues.couchbase.com/browse/CCBC-1418): Map query error 13014 to `LCB_ERR_AUTHENTICATION_FAILURE`.
* [CCBC-1357](https://issues.couchbase.com/browse/CCBC-1357): Allow to preserve expiration with Replace, Upsert and MutateIn operations.
* [CCBC-1384](https://issues.couchbase.com/browse/CCBC-1384): Allow the operations to be deferred until the instance will be connected to cluster.
* [CCBC-1410](https://issues.couchbase.com/browse/CCBC-1410): Refactor dynamic authenticator. NOTE: this API still volatile and might be changed in future.  
In order to improve UX and allow caller to implement credential caching the API for authenticator was revised:
* instead of separate callbacks for username/password, now it uses single callback
* in the callback, the caller can figure out the reason of credentials request using `lcbauth_credentials_reason()`
* the caller can signal that it failed to retrieve credentials from external provider, and set result with `lcbauth_credentials_result()`. In this case the SDK will not retry the operation.
* [CCBC-1413](https://issues.couchbase.com/browse/CCBC-1413): Skip `SELECT_BUCKET` packets waiting retry queue.
* [CCBC-1169](https://issues.couchbase.com/browse/CCBC-1169): Request copy from active vbucket for `get_all_replicas` operation.
* [CCBC-1406](https://issues.couchbase.com/browse/CCBC-1406): Fill in prepared statement handle on retry.
* [CCBC-1405](https://issues.couchbase.com/browse/CCBC-1405): Remove const from command cookie.
* [CCBC-1402](https://issues.couchbase.com/browse/CCBC-1402): Fix parsing JSON primitives as query rows.
* Various improvements and fixes in test and build infrastructure

#### [](#downloads-24)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.2.0.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.2.0.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.2.0\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.2.0\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.2.0\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.2.0\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.2.0\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.2.0\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.2.0\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.2.0\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.2.0\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.2.0\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.2.0\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.2.0\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.2.0\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x64          | [libcouchbase-3.2.0\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.2.0%5Fvc16%5Famd64%5Fopenssl.zip)           |

## [](#c-sdk-3-1-releases)C SDK 3.1 Releases

### [](#version-3-1-3-10-may-2021)Version 3.1.3 (10 May 2021)

Version 3.1.3 is the fourth release of the 3.1 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.1.3/index.html)

* [CCBC-1395](https://issues.couchbase.com/browse/CCBC-1395): We no longer expose `LCB_ERR_BUCKET_NOT_FOUND` in operation callbacks. Instead, the operation is automatically retried until timeout.
* [CCBC-1398](https://issues.couchbase.com/browse/CCBC-1398): Parse and use `revEpoch` from configuration in order to allow the server to handle special cases of failover scenarios.
* [CCBC-1399](https://issues.couchbase.com/browse/CCBC-1399): Implement retry backoff for query requests. Instead of retrying requests immediately, use backoff period returned by retry strategy.
* [CCBC-1400](https://issues.couchbase.com/browse/CCBC-1400): Fill collection name when retrying collection resolution to avoid misrouting requests to default collection.
* [CCBC-1397](https://issues.couchbase.com/browse/CCBC-1397): Reset list of "used" nodes when retrying query to allow reusing endpoints.
* [CCBC-1401](https://issues.couchbase.com/browse/CCBC-1401): Fix special error message detection for Query requests. In addition to reacting on the error codes from query service, the library also scans error messages for particular sub-strings to decide whether retry is necessary.
* [CCBC-861](https://issues.couchbase.com/browse/CCBC-861): Purge pipelines on `lcb_destroy`. In order to avoid resource leaks, the library purges all pending (or waiting) commands from the pipelines upon destruction.
* Fix `cbc-proxy` tool.
* Upgrade snappy to 1.1.8

#### [](#downloads-25)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.1.3.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.1.3.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.1.3\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.1.3\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.1.3\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.1.3\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.1.3\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.1.3\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.1.3\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.1.3\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.1.3\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.1.3\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.1.3\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.1.3\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.1.3\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x64          | [libcouchbase-3.1.3\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.3%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-1-2-26-april-2021)Version 3.1.2 (26 April 2021)

Version 3.1.2 is the third release of the 3.1 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.1.2/index.html)

* [CCBC-1395](https://issues.couchbase.com/browse/CCBC-1394): We no longer expose `LCB_ERR_BUCKET_NOT_FOUND` in operation callbacks. Instead, the operation is automatically retried until timeout.
* [CCBC-1373](https://issues.couchbase.com/browse/CCBC-1373): Do not send collection in the key. Sending collection specification in both key and body breaks protocol, and the server will close the socket.
* [CCBC-1396](https://issues.couchbase.com/browse/CCBC-1396): Fix recalculaton of key length for alternative packets.
* [CCBC-1395](https://issues.couchbase.com/browse/CCBC-1395): Parse configuration revision as `int64_t`.
* [MB-45759](https://issues.couchbase.com/browse/MB-45759): Allow building libcouchbase with external Snappy.
* [CCBC-1330](https://issues.couchbase.com/browse/CCBC-1330): Detect unknown collection during "populate" phase of `cbc-pillowfight`.
* [CCBC-1386](https://issues.couchbase.com/browse/CCBC-1386): Remove legacy options for `cbc-bucket-create`.

#### [](#downloads-26)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.1.2.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.1.2.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.1.2\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.1.2\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.1.2\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.1.2\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.1.2\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.1.2\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.1.2\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.1.2\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.1.2\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.1.2\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.1.2\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.1.2\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.1.2\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x64          | [libcouchbase-3.1.2\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.2%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-1-1-9-april-2021)Version 3.1.1 (9 April 2021)

Version 3.1.1 is the second release of the 3.1 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.1.1/index.html)

* [CCBC-1382](https://issues.couchbase.com/browse/CCBC-1382): Return `LCB_ERR_CAS_MISMATCH` for operations with with REPLACE semantics instead of `LCB_ERR_DOCUMENT_EXISTS`.
* [CCBC-1389](https://issues.couchbase.com/browse/CCBC-1389): Fixed default collection parsing.
* [CCBC-1383](https://issues.couchbase.com/browse/CCBC-1383): Fixed protocol magic for durable remove. When durability level provided, the remove command should use "alternative request" as protocol magic byte.
* [CCBC-1381](https://issues.couchbase.com/browse/CCBC-1381): Protocol changes for `PROTOCOL_BINARY_CMD_COLLECTIONS_GET_CID` (`0xbb`). The server now expects collection specification passed as a command value during collection ID resolution.
* [CCBC-1385](https://issues.couchbase.com/browse/CCBC-1385): Restrict cases when Query error code `12009` is converted to `LCB_ERR_CAS_MISMATCH`. Now it returned only in cases where concurrency problem detected by query engine. Otherwise `LCB_ERR_DML_FAILURE` will be used.
* [CCBC-1373](https://issues.couchbase.com/browse/CCBC-1373): Return `LCB_ERR_TIMEOUT` if the library is not able to resolve collection identifier. Previously either `LCB_ERR_COLLECTION_NOT_FOUND` or `LCB_ERR_SCOPE_NOT_FOUND` might be returned.
* [CCBC-1109](https://issues.couchbase.com/browse/CCBC-1109): When dynamic authenticator is being used, the library will retry Query on error code `13014` (`datastore.couchbase.insufficient_credentials`).
* [CCBC-1392](https://issues.couchbase.com/browse/CCBC-1392): Query commands now invoke retry strategy hook to make decision about retrying.
* [CCBC-1379](https://issues.couchbase.com/browse/CCBC-1379): Error map could be disabled now using `LCB_CNTL_ENABLE_ERRMAP` or in the connection string with `enable_errmap=false`.
* [CCBC-1269](https://issues.couchbase.com/browse/CCBC-1269): Expose setting for N1QL grace period. This is a port of [CCBC-1122](https://issues.couchbase.com/browse/CCBC-1122). The example below will add extra 100ms to each N1QL query:  
```c  
lcb_cntl_setu32(instance, LCB_CNTL_QUERY_GRACE_PERIOD, 100000);  
```

#### [](#downloads-27)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.1.1.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.1.1.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.1.1\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.1.1\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.1.1\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.1.1\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.1.1\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.1.1\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.1.1\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.1.1\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.1.1\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.1.1\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.1.1\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.1.1\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.1.1\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x64          | [libcouchbase-3.1.1\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.1%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-1-0-3-march-2021)Version 3.1.0 (3 March 2021)

Version 3.1.0 is the first release of the 3.1 series.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.1.0/index.html)

* [CCBC-1376](https://issues.couchbase.com/browse/CCBC-1311): Propagate scope qualifier to prepared query statements.
* [CCBC-1283](https://issues.couchbase.com/browse/CCBC-1283): Added analytics support for scopes.
* [CCBC-1374](https://issues.couchbase.com/browse/CCBC-1374): Reintroduce input error classification macro.
* [CCBC-1375](https://issues.couchbase.com/browse/CCBC-1375): Translate query errors when scope/collection missing.
* [CCBC-1366](https://issues.couchbase.com/browse/CCBC-1366): Do not cache bucket-less configurations.
* [CCBC-1363](https://issues.couchbase.com/browse/CCBC-1363): Allow using parent project's `hdr_histogram_static` target.
* [CCBC-1361](https://issues.couchbase.com/browse/CCBC-1361): Allow `"_default._default"` collection for pre-collections servers.
* [MB-42884](https://issues.couchbase.com/browse/MB-42884): Correctly define `FILEVERSION` for libcouchbase.dll.
* [CCBC-1351](https://issues.couchbase.com/browse/CCBC-1351): Option to render cbc-ping output as a table.
* [CCBC-1323](https://issues.couchbase.com/browse/CCBC-1323): Return `LCB_ERR_DOCUMENT_EXISTS` only for insert operation.
* [CCBC-1346](https://issues.couchbase.com/browse/CCBC-1346): Return `LCB_ERR_DOCUMENT_LOCKED` for locked documents.

#### [](#downloads-28)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.1.0.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.1.0.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.1.0\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.1.0\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.1.0\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.1.0\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.1.0\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.1.0\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.1.0\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.1.0\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.1.0\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.1.0\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.1.0\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.1.0\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.1.0\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x64          | [libcouchbase-3.1.0\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.1.0%5Fvc16%5Famd64%5Fopenssl.zip)           |

## [](#c-sdk-3-0-releases)C SDK 3.0 Releases

### [](#version-3-0-7-16-december-2020)Version 3.0.7 (16 December 2020)

Version 3.0.7 is the eighth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.0.7/index.html)

* [CCBC-1350](https://issues.couchbase.com/browse/CCBC-1350): Implemented an option for `cbc-n1qlback` to control prepared/adhoc switch.
* [CCBC-1345](https://issues.couchbase.com/browse/CCBC-1345): Ensure all KV sockets select bucket on `lcb_open`.
* [CCBC-1348](https://issues.couchbase.com/browse/CCBC-1348): Bucket name now included in `diag` report.
* [CCBC-1308](https://issues.couchbase.com/browse/CCBC-1308): Defined FATAL and TRANSIENT classes for errors. Also defines corresponding macros for easy access `LCB_ERROR_IS_TRANSIENT` and `LCB_ERROR_IS_FATAL`.
* [CCBC-1342](https://issues.couchbase.com/browse/CCBC-1342): Check if collections supported by server before using them. Specifying a non-default collection on an operation against servers which do not support collections will now return a `FeatureNotSupported` error.
* [CCBC-1334](https://issues.couchbase.com/browse/CCBC-1334): Preserve status of KV protocol response for retry queue.
* [CCBC-1339](https://issues.couchbase.com/browse/CCBC-1339): Do not relocate get with replica on failover. The library should not relocate replica reads when new configuration applied.
* [CCBC-1344](https://issues.couchbase.com/browse/CCBC-1344): Consume response after retried command to avoid logging the command as "timed out".
* [CCBC-1343](https://issues.couchbase.com/browse/CCBC-1343): Do not schedule `NotMyVbucket` immediately by default and use retry strategy instead.
* [CCBC-1335](https://issues.couchbase.com/browse/CCBC-1335): Fixed next timeout computation on requesting config using `operation_timeout` instead of `config_node_timeout`.
* [CCBC-1337](https://issues.couchbase.com/browse/CCBC-1337): Expose setting for to control default search timeout.
* [CCBC-1331](https://issues.couchbase.com/browse/CCBC-1331): Fixed error at bootstrap callback, now it returns original error code, that caused the bootstrap failure.
* [CCBC-1333](https://issues.couchbase.com/browse/CCBC-1333): Allow setting `lcb_cmdget_locktime` to zero to use server default time.
* [CCBC-1324](https://issues.couchbase.com/browse/CCBC-1324): Defined HTTP type for Eventing management.
* Retry operations when the node is not ready.
* Report `LCB_ERR_BUCKET_NOT_FOUND` if Key/Value service is not configured.
* Update error codes for Query. Translate code 4300 to `LCB_ERR_PLANNING_FAILURE` and 5000 to `LCB_ERR_INTERNAL_SERVER_FAILURE` by default.
* Fix collection validation, it should pass empty string as valid collection specification element.
* Remove verbosity and mcversions commands. These parts of API are non-standard and volatile.
* Bundle HdrHistogram\_c v0.11.2 and allow to fall back to it.

#### [](#downloads-29)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.7.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.7.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.7\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.7\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.7\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.7\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.7\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.0.7\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.7\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.7\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.7\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.7\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.0.7\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.0.7\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.7\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fvc15%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2019 TLS (VC16) | x64          | [libcouchbase-3.0.7\_vc16\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.7%5Fvc16%5Famd64%5Fopenssl.zip)           |

### [](#version-3-0-6-21-october-2020)Version 3.0.6 (21 October 2020)

Version 3.0.6 is the seventh release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.0.6/index.html)

* [CCBC-1311](https://issues.couchbase.com/browse/CCBC-1311): Implemented `create_as_deleted` subdoc feature.
* [CCBC-1263](https://issues.couchbase.com/browse/CCBC-1263): Updated ping to report Analytics as Analytics Service instead of Query.
* [CCBC-1175](https://issues.couchbase.com/browse/CCBC-1175): Allow to specify timeout for `lcb_ping`.
* [CCBC-1262](https://issues.couchbase.com/browse/CCBC-1262): Added accessor for `report_id` in ping report.
* [CCBC-1176](https://issues.couchbase.com/browse/CCBC-1176): Renamed "scope" to "namespace" in ping report (also deprecated `lcb_respping_result_scope` in favour to `lcb_respping_result_namespace`).
* [CCBC-1261](https://issues.couchbase.com/browse/CCBC-1261): Set namespace length of service in ping report to zero if not applicable.
* [CCBC-1194](https://issues.couchbase.com/browse/CCBC-1194): Added extra checks for socket state in `lcb_diag` to avoid invalid access issues.
* [CCBC-1314](https://issues.couchbase.com/browse/CCBC-1314): Extra checks for socket state in `lcb_ping` to avoid invalid access issues.
* [CCBC-1316](https://issues.couchbase.com/browse/CCBC-1316): Fixed two-step bootstrap (`lcb_connect` \+ `lcb_open`) for memcached bucket.

#### [](#downloads-30)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.6.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.6.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.6\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.6\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.6\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.6\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.6\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.0.6\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.6\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.6\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.6\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.6\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.0.6\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.6\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.6%5Fvc15%5Famd64%5Fopenssl.zip)           |

### [](#version-3-0-5-21-september-2020)Version 3.0.5 (21 September 2020)

Version 3.0.5 is the sixth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.0.5/index.html)

* [CCBC-1307](https://issues.couchbase.com/browse/CCBC-1307): The SDK now allows the selection of any mechanisms for SASL regardless of the network protocol being usedm although by default the SDK will try to avoid downgrading to PLAIN on non-TLS connections. Also the change allows users to specify a list of preferred mechanisms instead of only one (through the use of a comma in the value of the `sasl_mech_force` connection string option).
* [CCBC-1276](https://issues.couchbase.com/browse/CCBC-1276): Addded flex (FTS) index usage to query options.
* [CCBC-1312](https://issues.couchbase.com/browse/CCBC-1312): Fixed return values for `lcb_cmdquery_scope_*`.
* [CCBC-1313](https://issues.couchbase.com/browse/CCBC-1313): Replaced `std::random_shuffle` with `std::shuffle`. fixing build of `cbc-n1qlback` tool.

#### [](#downloads-31)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.5.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.5.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.5\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.5\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.5\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.5\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.5\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.0.5\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.5\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.5\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.5\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.5\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.0.5\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.5\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.5%5Fvc15%5Famd64%5Fopenssl.zip)           |

### [](#version-3-0-4-26-august-2020)Version 3.0.4 (26 August 2020)

Version 3.0.4 is the fifth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.0.4/index.html)

* [CCBC-1281](https://issues.couchbase.com/browse/CCBC-1281): Implemented scope qualifier for queries.
* [CCBC-1301](https://issues.couchbase.com/browse/CCBC-1301): Expose cmake option to help dissect TLS traffic.
* Detect configuration change when replica indexes changed.

#### [](#downloads-32)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.4.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.4.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.4\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.4\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.4\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.4\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.4\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.0.4\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.4\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.4\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.4\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.4\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2015 TLS (VC14) | x64          | [libcouchbase-3.0.4\_vc14\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fvc14%5Famd64%5Fopenssl.zip)           |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.4\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.4%5Fvc15%5Famd64%5Fopenssl.zip)           |

### [](#version-3-0-3-27-july-2020)Version 3.0.3 (27 July 2020)

Version 3.0.3 is the fourth release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.0.3/index.html)

* Binary packages for Ubuntu 20.04 LTS (Focal Fossa)
* [CCBC-1265](https://issues.couchbase.com/browse/CCBC-1265): Enabled out of order execution by default.
* [CCBC-1189](https://issues.couchbase.com/browse/CCBC-1189): The SDK now validate collection and scope names early. The library will return an error if the collection name is not valid, without sending a command to the server.
* [CCBC-1278](https://issues.couchbase.com/browse/CCBC-1278): Fixed stripping payload over TLS connection. The library might propagate zero return code from `recv()` even when previous calls of `recv()` successfully transferred bytes to SSL context. In this case we might lose these trailing bytes and just close the socket.
* [CCBC-1264](https://issues.couchbase.com/browse/CCBC-1264): Fixed calculating key size when durability level specified.
* [CCBC-1258](https://issues.couchbase.com/browse/CCBC-1258): Fixed port order in vbucket diff info message.
* [CCBC-1274](https://issues.couchbase.com/browse/CCBC-1274): Fixed pointer casting in HTTP callback of `cbc` tool.
* [CCBC-1167](https://issues.couchbase.com/browse/CCBC-1167): Fixed tests build on MacOS.
* [CCBC-1248](https://issues.couchbase.com/browse/CCBC-1248): The SDK will now always request error map feature and send HELLO message to speedup bootstrap.
* Implemented tick for IOCP plugin on Windows.
* Improved build on Windows (fixed static build, and PDB installation).
* Fixed collections issues for future server release.

#### [](#downloads-33)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.3.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.3.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.3\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.3\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.3\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.3\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.3\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Ubuntu 20.04 (focal)          | x64          | [libcouchbase-3.0.3\_ubuntu2004\_focal\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fubuntu2004%5Ffocal%5Famd64.tar)   |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.3\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.3\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.3\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.3\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.3\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.3%5Fvc15%5Famd64%5Fopenssl.zip)           |

### [](#version-3-0-2-10-june-2020)Version 3.0.2 (10 June 2020)

Version 3.0.2 is the third release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

[API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.0.2/index.html)

* [CCBC-1200](https://issues.couchbase.com/browse/CCBC-1200): LCB will now retry bootstrap on missing bucket error until timeout. Bootstrap timeout is controlled by "config\_total\_timeout" in connection string or `LCB_CNTL_CONFIGURATION_TIMEOUT`.
* [CCBC-1190](https://issues.couchbase.com/browse/CCBC-1190): When performing an operation immediately after bucket creation, the server returns `TMPFAIL` and libcouchbase bubbled this up rather than restarting. Now fixed so LCB automatic retries for temporary failures from the server.
* [CCBC-1158](https://issues.couchbase.com/browse/CCBC-1158): Reduced retrying on unknown collection to a sensible level.
* [CCBC-1254](https://issues.couchbase.com/browse/CCBC-1254): It's now possible to use a separate option for default timeout of Analytics queries (connection string "analytics\_timeout").
* [CCBC-1178](https://issues.couchbase.com/browse/CCBC-1178): It is now no longer possible to (illigally) set CAS for upsert and insert operations.
* [CCBC-1156](https://issues.couchbase.com/browse/CCBC-1156): Fixed enum value for analytics type of HTTP request.
* [CCBC-1251](https://issues.couchbase.com/browse/CCBC-1251): No longer log error when using GCCCP on pre-6.5 Couchbase Server.
* [CCBC-1234](https://issues.couchbase.com/browse/CCBC-1234): Fixed SRV resolution to work with large record sizes.
* [CCBC-1222](https://issues.couchbase.com/browse/CCBC-1222): Tracing thresholds for query and search fixed in connection strings: `tracing_threshold_search` and `tracing_threshold_query`.
* [CCBC-1187](https://issues.couchbase.com/browse/CCBC-1187): `lcb_respexists_is_found` can no longer return true for deleted documents.
* [CCBC-1233](https://issues.couchbase.com/browse/CCBC-1233): Updated RTO to independently specify operation\_name.
* [CCBC-1205](https://issues.couchbase.com/browse/CCBC-1205): Do not include trailing zero for endpoint length for KV context.
* [CCBC-1215](https://issues.couchbase.com/browse/CCBC-1215): Fixed segfault in exists calls.
* [CCBC-1218](https://issues.couchbase.com/browse/CCBC-1218): Fixed intermittent segfault in client durable store.
* Documentation issues addressed ([CCBC-1240](https://issues.couchbase.com/browse/CCBC-1240), [CCBC-1241](https://issues.couchbase.com/browse/CCBC-1241), [CCBC-1243](https://issues.couchbase.com/browse/CCBC-1243), [CCBC-1245](https://issues.couchbase.com/browse/CCBC-1245))

#### [](#downloads-34)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.2.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.2.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.2\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.2\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.2\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.2\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.2\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.2\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.2\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.2\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.2\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.2\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.2%5Fvc15%5Famd64%5Fopenssl.zip)           |

### [](#version-3-0-1-8-april-2020)Version 3.0.1 (8 April 2020)

Version 3.0.1 is the second release of the 3.0 series, bringing enhancements and bugfixes over the last stable release.

#### [](#fixed-issues)Fixed Issues

* [CCBC-1188](https://issues.couchbase.com/browse/CCBC-1188): cbc-pillowfight: fixed `--collection` switch.
* [CCBC-1173](https://issues.couchbase.com/browse/CCBC-1173): Fixed exporting `lcb_cmdquery_consistency_token_for_keyspace`.
* [CCBC-1168](https://issues.couchbase.com/browse/CCBC-1168): Exposed `max_parallelism` for query.
* [CCBC-1171](https://issues.couchbase.com/browse/CCBC-1171): Exposed `profile` option for query.
* [CCBC-1170](https://issues.couchbase.com/browse/CCBC-1170): Exposed `scan_wait` option for query.
* [CCBC-1159](https://issues.couchbase.com/browse/CCBC-1159): Fixed error codes for Management API.
* [MB-37768](https://issues.couchbase.com/browse/MB-37768): Fixed issue where \`CMAKE\_INSTALL\_RPATH\`was overriden, affecting cbc tools.
* [CCBC-1208](https://issues.couchbase.com/browse/CCBC-1208): Added a fail-fast retry strategy.
* [CCBC-1209](https://issues.couchbase.com/browse/CCBC-1209): Renamed functions of embedded `http_parser` to avoid name clash.
* Removed use of deprecated function `std::random_shuffle`. `std::random_shuffle` is deprecated in C14, removed in C17\. Replaced with `std::shuffle`.
* Fixed several issues reported by coverity.

#### [](#known-issues)Known Issues

* Attempting to install libcouchbase via homebrew on OS X prior to June 8th, 2020 would result in libcouchbase 2.10 being installed instead of 3.0.

#### [](#downloads-35)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.1.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.1.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.1\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.1\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.1\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.1\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.1\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.1\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.1\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.1\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.1\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.1\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.1%5Fvc15%5Famd64%5Fopenssl.zip)           |

### [](#version-3-0-0-17-january-2020)Version 3.0.0 (17 January 2020)

This is the first GA release of the third generation C SDK.

#### [](#fixed-issues-2)Fixed Issues

* [CCBC-1152](https://issues.couchbase.com/browse/CCBC-1152): Enabled `SCRAM-SHA*` SASL by default.
* [CCBC-1153](https://issues.couchbase.com/browse/CCBC-1153): Renamed `lcb_wait3` to `lcb_wait`.
* [CCBC-1147](https://issues.couchbase.com/browse/CCBC-1147): Return `LCB_SUCCESS` for `lcb_exists` when the document is missing. `lcb_respexists_is_found` should be used on its response object to check the presense of the document.
* [CCBC-1152](https://issues.couchbase.com/browse/CCBC-1152): Do not allow to use SASL PLAIN on non-TLS connections. Compiling libcouchbase with OpenSSL is strongly recommended.
* [CCBC-1032](https://issues.couchbase.com/browse/CCBC-1032): Use operation node to resolve collection and return timeout when collection cannot be resolved
* Added shortcut for query options to request metrics
* Do not fallback to single subdocument API when only one specification passed to `lcb_subdoc`.
* [CCBC-1137](https://issues.couchbase.com/browse/CCBC-1137): Allow to retrieve error context for HTTP response (`lcb_http` API).
* [CCBC-1145](https://issues.couchbase.com/browse/CCBC-1145): Expose endpoints in error context.
* [CCBC-1146](https://issues.couchbase.com/browse/CCBC-1146): Expose user-cookie in retry handler.
* [CCBC-1148](https://issues.couchbase.com/browse/CCBC-1148): Added NULL checks for enhanced error info.
* [CCBC-1075](https://issues.couchbase.com/browse/CCBC-1075): Renamed "FTS" to "SEARCH" in the APIs.
* [CCBC-1073](https://issues.couchbase.com/browse/CCBC-1073): Renamed "N1QL" to "QUERY" in the APIs.
* Fixed bucketless bootstrap for Server 6.0.
* Fixed various memory leaks. Improved build, testing and packaging systems.

#### [](#known-issues-2)Known Issues

* Attempting to install libcouchbase via homebrew on OS X prior to June 8th, 2020 would result in libcouchbase 2.10 being installed instead of 3.0.

#### [](#downloads-36)Downloads

| Platform                      | Architecture | File                                                                                                                                               |
| ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Checksums                     | Any          | [libcouchbase-3.0.0.sha256sum](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0.sha256sum)                                              |
| Source Archive                | Any          | [libcouchbase-3.0.0.tar.gz](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0.tar.gz)                                                    |
| Amazon Linux 2                | x64          | [libcouchbase-3.0.0\_amzn2\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Famzn2%5Fx86%5F64.tar)                       |
| Enterprise Linux 7            | x64          | [libcouchbase-3.0.0\_centos7\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fcentos7%5Fx86%5F64.tar)                   |
| Enterprise Linux 8            | x64          | [libcouchbase-3.0.0\_centos8\_x86\_64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fcentos8%5Fx86%5F64.tar)                   |
| Ubuntu 16.04 (xenial)         | x64          | [libcouchbase-3.0.0\_ubuntu1604\_xenial\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fubuntu1604%5Fxenial%5Famd64.tar) |
| Ubuntu 18.04 (bionic)         | x64          | [libcouchbase-3.0.0\_ubuntu1804\_bionic\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fubuntu1804%5Fbionic%5Famd64.tar) |
| Debian 9 (stretch)            | x64          | [libcouchbase-3.0.0\_debian9\_stretch\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fdebian9%5Fstretch%5Famd64.tar)     |
| Debian 10 (buster)            | x64          | [libcouchbase-3.0.0\_debian10\_buster\_amd64.tar](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fdebian10%5Fbuster%5Famd64.tar)     |
| Visual Studio 2015 (VC14)     | x64          | [libcouchbase-3.0.0\_vc14\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fvc14%5Famd64.zip)                              |
| Visual Studio 2017 (VC15)     | x64          | [libcouchbase-3.0.0\_vc15\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fvc15%5Famd64.zip)                              |
| Visual Studio 2019 (VC16)     | x64          | [libcouchbase-3.0.0\_vc16\_amd64.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fvc16%5Famd64.zip)                              |
| Visual Studio 2017 TLS (VC15) | x64          | [libcouchbase-3.0.0\_vc15\_amd64\_openssl.zip](https://packages.couchbase.com/clients/c/libcouchbase-3.0.0%5Fvc15%5Famd64%5Fopenssl.zip)           |

### [](#pre-releases)Pre-releases

Numerous _Alpha_ and _Beta_ releases were made in the run-up to the 3.0 release, and although unsupported, the release notes and download links are retained for archive purposes [here](#3.0@c-sdk:project-docs:3.0-pre-release-notes.adoc).

## [](#older-releases)Older Releases

Although [no longer supported](https://www.couchbase.com/support-policy/enterprise-software), documentation for older releases continues to be available in our [docs archive](https://docs-archive.couchbase.com/home/index.html).