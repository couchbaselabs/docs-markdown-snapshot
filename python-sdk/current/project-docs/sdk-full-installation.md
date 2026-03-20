---
title: Full Installation
description: Installation instructions for the Couchbase Python Client.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:python-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Couchbase Python Client. 

This page covers installation of the SDK. A quick start guide in our [Getting Started Guide](../hello-world/start-using-sdk.md) should work for most users — and for anyone in a hurry to try out the SDK and our _Hello World_ program, that page is usually the best place to get started — but more detailed installation instructions are provided here on this page for every supported platform. This guide assumes you have some familiarity with development using Python — if you are evaluating the SDK as a software architect, tester, or other non-Python role, you will benefit from our [Platform Help page](../hello-world/platform-help.md).

The Couchbase SDK 3.x API (used in the Python SDK 3.0 - 4.0) is a complete rewrite of the API, reducing the number of overloads to present a simplified surface area, and adding support for Couchbase Server features like [Collections and Scopes](../concept-docs/collections.md) (available from Couchbase Server 7.0).

3.x Python SDK introduced comprehensive [PEP-484](https://www.python.org/dev/peps/pep-0484/) style type annotations.

## [](#requirements)Requirements

Couchbase Python SDK bundles Couchbase++ automatically, so no need to install it separately. You may need CMake (a version >= 3.18) to install, although the installer will attempt to download it from PyPI automatically.

The Python SDK 4.x requires Python 3\. See the [Python Version Compatibility](compatibility.md#python-version-compat) section for details on supported versions of Python.

> [!NOTE]
> Currently the Python Client source distribution requires the OpenSSL headers and libraries that the Python client itself was built against to be installed prior to the client itself. Additionally the installer relies on PEP517 which older versions of PIP do not support. If you experience issues installing it is advised to upgrade your PIP/setuptools installation as follows:
> 
> ```console
> $ python3 -m pip install --upgrade pip setuptools wheel
> ```

## [](#installation)Installation

For [supported Operating Systems](compatibility.md#platform-compatibility):

* macOS
* Debian & Ubuntu
* RHEL & CentOS
* Windows
* Conda

Best practice is to use a Python virtual environment such as _venv_ or _pyenv_ to manage multible versions of Python, but in cases where this is not practicable follow the `brew` steps below, and also modify your `$PATH` as shown.

The Python SDK has wheels available on macOS for [supported versions of Python](compatibility.md#python-version-compat).

> [!NOTE]
> There can be a problem when using the Python (3.8.2) that ships with Xcode on Catalina. It is advised to install Python via [pyenv](https://github.com/pyenv/pyenv#homebrew-on-macos)(see the Python SDK [Github README](https://github.com/couchbase/couchbase-python-client#mac-os-pyenv-install) for further details on pyenv installation), [Homebrew](http://brew.sh/), or [python.org](https://www.python.org/downloads)

To install the library on Mac OS, first install [Homebrew](http://brew.sh/).

> [!NOTE]
> Later versions of Mac OS can break the python3 homebrew installer. Simple mitigating steps may be found [here](https://stackoverflow.com/questions/47255517/brew-install-python3-didnt-install-pip3).

The following example uses the Python supplied by the _Homebrew_ package manager and not the vendor-supplied Python which ships with Mac OS. Once _Homebrew_ is configured:

Get a list of the latest packages

```console
$ brew update
```

Install compatible Python 3

```console
$ brew install python3
```

For ZSH (MacOS 10.15 Catalina and newer)

```console
$ echo 'export PATH="/usr/local/bin:"$PATH' >> ~/.zshrc
```

```console
$ source ~/.zshrc
```

Install the latest Python SDK:

```console
$ sudo -H python3 -m pip install couchbase
```

> [!NOTE]
> Starting with Python 3.11.5, macOS installers from python.org now use [OpenSSL 3.0](https://docs.python.org/3/whatsnew/3.11.html#notable-changes-in-3-11-5). If using a version prior to 4.1.9 of the Python SDK, a potential side-effect of this change is an `ImportError: DLL load failed while importing pycbc_core` error. Upgrade the SDK to a version >= 4.1.9 to avoid this side-effect. If unable to upgrade, a work-around is to set the `PYCBC_OPENSSL_DIR` environment variable to the path where the OpenSSL 1.1 libraries (`` libssl.1.1.dylib ` and `libcrypto.1.1.dylib ``) can be found.

This SDK runs on top of the C++ core, Couchbase++, which requires a C++ 17 compiler, such as GCC 8.0, or more recent versions. Older versions of Debian and Ubuntu ship with an older version of GCC.

> [!IMPORTANT]
> While workarounds are available for installing a newer build chain, some may not be within your company’s policy, so also take a look at container options — such as the unofficial Docker builds provided in the Python SDK 4.x examples folder [here](https://github.com/couchbase/couchbase-python-client/tree/master/examples/dockerfiles), which can at least be used as a reference to a known working set-up.

Check that you have a new enough release of Python.

Best practice is to use a Python virtual environment such as _venv_ or _pyenv_ to manage multible versions of Python. See [pyenv docs](https://github.com/pyenv/pyenv#basic-github-checkout) for details.

The Python SDK has manylinux wheels available for [supported versions of Python](compatibility.md#python-version-compat).

During first-time setup:

```console
$ sudo apt-get install git-all python3-dev python3-pip python3-setuptools build-essential
```

First, make sure the [requirements](#linux) have been installed.

Install the latest Python SDK:

```console
$ python3 -m pip install couchbase
```

This SDK runs on top of the C++ core, Couchbase++, which requires a C++ 17 compiler, such as GCC 8.0, or more recent versions. Older versions of Debian and Ubuntu ship with an older version of GCC.

> [!IMPORTANT]
> Workarounds are available for installing a newer build chain with [EPEL](https://fedoraproject.org/wiki/EPEL), but this may not be within your company’s policy, so also take a look at container options — such as the unofficial Docker builds provided in the Python SDK 4.x examples folder [here](https://github.com/couchbase/couchbase-python-client/tree/master/examples/dockerfiles), which can at least be used as a reference to a known working set-up.

Check that you have a new enough release of Python, and if not then investigate the [EPEL](https://fedoraproject.org/wiki/EPEL) repository.

Best practice is to use a Python virtual environment such as _venv_ or _pyenv_ to manage multible versions of Python. See [pyenv docs](https://github.com/pyenv/pyenv#basic-github-checkout) for details.

The Python SDK has manylinux wheels available for [supported versions of Python](compatibility.md#python-version-compat).

During first-time setup:

```console
$ sudo yum install gcc gcc-c++ python3-devel python3-pip
```

> [!TIP]
> You may need to update your installed version of CMake. For example, by following the steps [here](https://idroot.us/install-cmake-centos-8).

> [!NOTE]
> RHEL/CentOS distributions may not provide the `python3-pip` package in the base repositories. It may be found in the [EPEL](https://fedoraproject.org/wiki/EPEL) repository.

First, make sure the [requirements](#linux) have been installed.

Install the latest Python SDK:

```console
$ python3 -m pip install couchbase
```

Note, the OpenSSL version needed for TLS 1.3 (mandated for secure connection to Couchbase Capella) is openssl 1.1.1\. This is newer than the one available in CentOS 7, and updated your OS’s libraries is beyond the scope of this documentation — but this can be installed through the already-mentioned EPEL repository. Once openssl (and other dependencies) are updated, an already-installed Couchbase Python SDK can be re-installed to use the libraries with:

```console
$ python3 -m pip install --force-reinstall --no-cache couchbase
```

Download and install Python from [python.org](https://www.python.org/downloads). Best practice is to use a Python virtual environment such as _venv_ or _pyenv_.

> [!TIP]
> Checkout the [pyenv-win](https://github.com/pyenv-win/pyenv-win) project to manage multiple versions of Python.

The Python SDK has wheels available on Windows for [supported versions of Python](compatibility.md#python-version-compat).

First, make sure the [requirements](#microsoft-windows) have been installed.

> [!NOTE]
> Commands assume user is working within a virtual environment.

Install the latest Python SDK:

```console
python -m pip install couchbase
```

> [!NOTE]
> Starting with Python 3.11.5, Windows builds from python.org now use [OpenSSL 3.0](https://docs.python.org/3/whatsnew/3.11.html#notable-changes-in-3-11-5). If using a version prior to 4.1.9 of the Python SDK, a potential side-effect of this change is an `ImportError: DLL load failed while importing pycbc_core` error. Upgrade the SDK to a version >= 4.1.9 to avoid this side-effect. If unable to upgrade, a work-around is to set the `PYCBC_OPENSSL_DIR` environment variable to the path where the OpenSSL 1.1 libraries (`libssl-1_1.dll` and `libcrypto-1_1.dll`) can be found.

The standard Python distributions for Windows include OpenSSL DLLs, as PIP and the inbuilt `ssl` module require it for correct operation. Prior to version 4.1.9 of the Python SDK, the binary wheels for Windows are built against OpenSSL 1.1\. Version 4.1.9 and beyond statically link against BoringSSL thus removing the OpenSSL requirement.

> [!NOTE]
> If you require a version that doesn’t have a suitable binary wheel on PyPI, follow the [build instructions](https://github.com/couchbase/couchbase-python-client#alternative-installation-methods) on the GitHub repo.

To use the SDK within the Anaconda / Miniconda platform, make sure the prerequisites for the desired Operating System are met:

`git-all python3-dev python3-pip python3-setuptools build-essential`

In the _Anaconda Prompt_, create a new environment:

```console
conda create -n test_env python=3.9
```

Activate the environment:

```console
conda activate test_env
```

Install the SDK:

```console
python -m pip install couchbase
```

> [!NOTE]
> If you require a version that doesn’t have a suitable binary wheel on PyPI, follow the [build instructions](https://github.com/couchbase/couchbase-python-client#alternative-installation-methods) on the GitHub repo.

### [](#pypy-support)PyPy support

Because the Python SDK is written primarily in C using the CPython API, the official SDK will not work on PyPy.