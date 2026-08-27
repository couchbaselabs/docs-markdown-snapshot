---
title: Full Installation of the C&#43;&#43; SDK
description: Installation instructions for the Couchbase C&#43;&#43; Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.2/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:1.2@cxx-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.2/project-docs/sdk-full-installation.html)

# Full Installation of the C&#43;&#43; SDK

> Installation instructions for the Couchbase C++ Client. 

This page gives full installation instructions for the C++ SDK. In most cases, the [Quickstart Guide](../hello-world/start-using-sdk.md) should be enough to get you up and running if you're in a hurry.

## [](#prerequisites)Prerequisites

A C++ 17 compiler and [CMake](https://cmake.org/) version 3.19 or newer is required. See the [Compatibility](compatibility.md) section for details on supported platforms.

## [](#installing-the-sdk)Installing the SDK

### [](#with-cpm-cmake)With CPM.cmake

[CPM.cmake](https://github.com/cpm-cmake/CPM.cmake) makes it really easy to include the library in your project. You only need to include the following command in your `CMakeLists.txt`.

```cmake
CPMAddPackage(
  NAME
  couchbase_cxx_client
  GIT_TAG
  1.2.1
  VERSION
  1.2.1
  GITHUB_REPOSITORY
  "couchbase/couchbase-cxx-client"
  OPTIONS
  "COUCHBASE_CXX_CLIENT_STATIC_BORINGSSL ON")
```

### [](#building-from-source)Building from source

Full instructions to build the SDK from source are given in the README of our [GitHub repository](https://github.com/couchbase/couchbase-cxx-client).

### [](#install-on-macos-x)Install on MacOS X

Install Homebrew using instructions from <https://docs.brew.sh/Installation>.

Configure tap for Couchbase:

```console
$ brew tap couchbaselabs/homebrew-couchbase
```

Install the library:

```console
$ brew install couchbase-cxx-client
```

### [](#install-on-rpm-based-systems)Install on RPM-based Systems

First, check how the platform identifies itself

```console
$ rpm -E '%dist/%_arch' | sed 's/^\.//'
```

This command would print the distribution/architecture part of the `.repo` URL. For example, for AmazonLinux 2023 on ARM architecture it prints the following:

```console
$ rpm -E '%dist/%_arch' | sed 's/^\.//'
amzn2023/aarch64
```

Now use this string to download repository URL:

```console
DIST_ARCH=$(rpm -E '%dist/%_arch' | sed 's/^\.//')
REPO_URL="https://packages.couchbase.com/clients/cxx/repos/rpm/${DIST_ARCH}/couchbase-cxx-client.repo"
curl -L -o/etc/yum.repos.d/couchbase-cxx-client.repo $REPO_URL
```

To list all the packages provided by the repository run this command:

```console
$ dnf list --available --disablerepo=* --enablerepo=couchbase
Available Packages
couchbase-cxx-client.aarch64                     1.0.3-1.amzn2023      couchbase
couchbase-cxx-client.src                         1.0.3-1.amzn2023      couchbase
couchbase-cxx-client-debuginfo.aarch64           1.0.3-1.amzn2023      couchbase
couchbase-cxx-client-debugsource.aarch64         1.0.3-1.amzn2023      couchbase
couchbase-cxx-client-devel.aarch64               1.0.3-1.amzn2023      couchbase
couchbase-cxx-client-tools.aarch64               1.0.3-1.amzn2023      couchbase
couchbase-cxx-client-tools-debuginfo.aarch64     1.0.3-1.amzn2023      couchbase
```

To install the library with the headers:

```console
dnf install couchbase-cxx-client couchbase-cxx-client-devel
```

To install the command line tools:

```console
dnf install couchbase-cxx-client-tools
```

Currently supported platforms are `aarch64` and `x86_64` for the following distributions:

* `amzn2023` AmazonLinux 2023 (<https://aws.amazon.com/linux/amazon-linux-2023/>).
* `el8` Rocky Linux 8 (<https://docs.rockylinux.org/release%5Fnotes/8%5F10/>), Red Hat Enterprise Linux 8 (<https://developers.redhat.com/rhel8>), AlmaLinux 8 (<https://wiki.almalinux.org/release-notes/8.10.html>), and Oracle Linux 8 (<https://docs.oracle.com/en/operating-systems/oracle-linux/8/>).
* `el9` Rocky Linux 9 (<https://docs.rockylinux.org/release%5Fnotes/9%5F4/>), Red Hat Enterprise Linux 9 (<https://developers.redhat.com/products/rhel/overview>), AlmaLinux 9 (<https://wiki.almalinux.org/release-notes/9.4.html>), and Oracle Linux 9 (<https://docs.oracle.com/en/operating-systems/oracle-linux/9/>).
* `suse.lp155` openSUSE Leap 15.5 (<https://get.opensuse.org/leap/15.5>).
* `fc40` Fedora Linux 40 (<https://docs.fedoraproject.org/en-US/fedora/f40/release-notes/>).
* `fc41` Fedora Linux 41 (<https://docs.fedoraproject.org/en-US/fedora/f41/release-notes/>).

### [](#install-on-deb-based-systems)Install on DEB-based Systems

First, check how the platform identifies itself:

```console
$ (source /etc/os-release; echo ${VERSION_CODENAME}/$(uname -m))
```

This command prints the distribution/architecture part of the `.source` URL. For example, for Ubuntu 20.04 on x86\_64 architecture it prints the following:

```console
$ (source /etc/os-release; echo ${VERSION_CODENAME}/$(uname -m))
```

```console
jammy/x86_64
```

Ensure that `GnuPG` and `curl` are installed:

```console
$ apt update && apt install curl gpg
```

Now use this string to download the repository URL:

```console
$ DIST_ARCH=$(source /etc/os-release; echo ${VERSION_CODENAME}/$(uname -m))
```

```console
$ curl -L https://packages.couchbase.com/clients/cxx/repos/deb/${DIST_ARCH}/DEB-GPG-KEY.txt | \
  gpg --yes --dearmor -o /usr/share/keyrings/couchbase-archive-keyring.gpg
```

```console
$ curl -L -o/etc/apt/sources.list.d/couchbase-cxx-client.sources \
  https://packages.couchbase.com/clients/cxx/repos/deb/${DIST_ARCH}/couchbase-cxx-client.sources
```

Update the apt Sources

```console
$ apt update
```

Install the library with the headers:

```console
$ apt install couchbase-cxx-client couchbase-cxx-client-dev
```

Install the command line tools:

```console
apt install couchbase-cxx-client-tools
```

Currently supported platforms are `aarch64` and `x86_64` for the following distributions:

* `bookworm` Debian 12 (<https://www.debian.org/releases/bookworm/>).
* `jammy` Ubuntu 22.04 (<https://www.releases.ubuntu.com/jammy/>).
* `noble` Ubuntu 24.04 (<https://www.releases.ubuntu.com/noble/>).