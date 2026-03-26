---
title: Install and Start Using the C SDK with Couchbase Server
description: The Couchbase C SDK (libcouchbase - LCB) enables you to interact
  with a Couchbase Server cluster from the C language.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:c-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/c-sdk/current/hello-world/start-using-sdk.html)

# Install and Start Using the C SDK with Couchbase Server

> The Couchbase C SDK (libcouchbase - LCB) enables you to interact with a Couchbase Server cluster from the C language. It was used by older versions of the Node.js, PHP, and Python SDKs to communicate with the Couchbase Server. 

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

## [](#documentation-and-examples)Documentation and Examples

* Small standalone examples can be found in the [github repository](https://github.com/couchbase/libcouchbase/tree/master/example).
* Other Couchbase SDKs are written on top of the C SDK and show more complex usage of the library's features:

  * [Python SDK](https://github.com/couchbase/couchbase-python-client)
  * [Node.js SDK](https://github.com/couchbase/couchnode)
* The library's own `cbc` (<https://github.com/couchbase/libcouchbase/blob/master/tools/cbc.cc>) and `cbc-pillowfight` (<https://github.com/couchbase/libcouchbase/blob/master/tools/cbc-pillowfight.cc>) utilities. Note that these tools may use internal APIs not intended for public use.

## [](#hello-couchbase)Hello Couchbase

Now you have the C client installed, you need to include the following in your first program:

```c
lcb_CREATEOPTS *create_options = NULL;
lcb_createopts_create(&create_options, LCB_TYPE_CLUSTER);
lcb_createopts_connstr(create_options, argv[1], strlen(argv[1]));
// username, password
lcb_createopts_credentials(create_options, argv[2], strlen(argv[2]), argv[3], strlen(argv[3]));
```

If you are connecting to Couchbase Cloud rather than a local Couchbase Server, see the [Cloud section](#cloud-connections), below.

Couchbase uses [Role Based Access Control (RBAC)](../../../server/current/learn/security/roles.md) to control access to resources. Here we will use the _Full Admin_ role created during installation of the Couchbase Data Platform. For production client code, you will want to use [more appropriate, restrictive settings](../howtos/managing-connections.md#rbac), but here we want to get you up and running quickly. If you're developing client code on the same VM or machine as the Couchbase Server, your URI can be _localhost_.

```c
lcb_STATUS rc; /* return code, that have to be checked */
lcb_INSTANCE *instance;
rc = lcb_create(&instance, &create_options);
lcb_createopts_destroy(create_options);
rc = lcb_connect(instance);
rc = lcb_wait(instance);
rc = lcb_get_bootstrap_status(instance);
```

After initializing the cluster, we open a bucket:

```c
static void open_callback(lcb_INSTANCE *instance, lcb_STATUS rc)
{
    printf("open bucket: %s\n", lcb_strerror_short(rc));
}

// associate instance with a bucket
lcb_set_open_callback(instance, open_callback);
const char *name = "bucket-name";
rc = lcb_open(instance, name, strlen(name)),
```

If you installed the travel sample data bucket, substitute _travel-sample_ for _bucket-name_.

The 3.x SDKs support full integration with the [Collections](../concept-docs/collections.md) feature introduced in Couchbase Server 7.0\. This includes complete support of Collections, allowing Documents to be grouped by purpose or theme, according to a specified _Scope_. Here we will use the `users` collection within the `tenant_agent_00` scope from `travel-sample` bucket as an example.

```c
static void store_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPSTORE *resp)
{
    const char *key;
    size_t nkey;
    uint64_t cas;
    lcb_respstore_key(resp, &key, &nkey);
    lcb_respstore_cas(resp, &cas);
    printf("status: %s, key: %.*s, CAS: 0x%" PRIx64 "\n",
       lcb_strerror_short(lcb_respstore_status(resp)), (int)nkey, key, cas);
}

lcb_install_callback3(instance, LCB_CALLBACK_STORE, (lcb_RESPCALLBACK)store_callback);

lcb_STATUS rc;
lcb_CMDSTORE *cmd;
const char *scope = "tenant_agent_00", *collection = "users";
const char *key = "my-document";
const char *value = "{\"name\": \"mike\"}";
rc = lcb_cmdstore_create(&cmd, LCB_STORE_UPSERT);
rc = lcb_cmdstore_collection(cmd, scope, strlen(scope), collection, strlen(collection));
rc = lcb_cmdstore_key(cmd, key, strlen(key));
rc = lcb_cmdstore_value(cmd, value, strlen(value));
rc = lcb_store(instance, NULL, cmd);
rc = lcb_cmdstore_destroy(cmd);
rc = lcb_wait(instance);
```

```c
static void get_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
{
    const char *key, *value;
    size_t nkey, nvalue;
    uint64_t cas;
    lcb_respget_key(resp, &key, &nkey);
    lcb_respget_value(resp, &value, &nvalue);
    lcb_respget_cas(resp, &cas);
    printf("status: %s, key: %.*s, CAS: 0x%" PRIx64 "\n",
       lcb_strerror_short(lcb_respget_status(resp)), (int)nkey, key, cas);
    printf("value:\n%s\n", (int)nvalue, value);
}

lcb_install_callback3(instance, LCB_CALLBACK_GET, (lcb_RESPCALLBACK)get_callback);

lcb_STATUS rc;
lcb_CMDGET *cmd;
const char *scope = "tenant_agent_00", *collection = "users";
const char *key = "my-document";
rc = lcb_cmdget_create(&cmd);
rc = lcb_cmdget_collection(cmd, scope, strlen(scope), collection, strlen(collection));
rc = lcb_cmdget_key(cmd, key, strlen(key));
rc = lcb_get(instance, NULL, cmd);
rc = lcb_cmdget_destroy(cmd);
rc = lcb_wait(instance);
```

This code shows how you would use a named collection and scope. A named or default [collection](../../../server/current/learn/data/scopes-and-collections.md) will provide the same functionality as bucket-level operations did in previous versions of Couchbase Server.

## [](#cloud-connections)Cloud Connections

For developing on Couchbase Cloud, if you are not working from the same _Availability Zone_, refer to the following:

* Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments),
* [Network Requirements](../project-docs/compatibility.md#network-requirements),
* If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).

## [](#additional-resources)Additional Resources

The API reference is generated for each release and the latest can be found [here](http://docs.couchbase.com/sdk-api/couchbase-c-client/). Older API references are linked from their respective sections in the [Release Notes](../project-docs/sdk-release-notes.md).

Couchbase welcomes community contributions to the C SDK. The C SDK source code is available on [GitHub](https://github.com/couchbase/libcouchbase).