---
title: Full Installation
description: Installation instructions for the Python Columnar SDK.
editUrl: https://github.com/couchbase/docs-columnar-sdk-python/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/python-columnar-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Python Columnar SDK. 

## [](#before-you-start)Before You Start

Sign up for a [Capella account](../../../cloud/get-started/create-account.md), and choose a [Columnar](../../../analytics/intro/intro.md) cluster.

### [](#prerequisites)Prerequisites

Currently Python 3.9 - Python 3.12 is supported. See the [compatibility page](compatibility.md#platform-compatibility) for more information about platform support.

> [!WARNING]
> Don’t Mix Columnar & Operational SDKs.
> 
> Do not combine the Python Columnar SDK with the Python Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs.
> 
> Note, this does not apply to combining our Enterprise Analytics SDKs with our Operational SDKs. See the [Analytics SDK page](#home::analytics-sdk.adoc) for a reminder of which Analytics SDK to use with which Analytics service.

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `npm`:

```console
python -m pip install couchbase-columnar
```

## [](#other-installation-methods)Other Installation Methods

A select set of wheels is available on the [GitHub Releases page](https://github.com/couchbaselabs/columnar-python-client/releases). If a wheel is not available for your specific Python version and/or platform, See the [GitHub Building page](https://github.com/couchbaselabs/columnar-python-client/blob/main/BUILDING.md) for details on how to build the SDK’s binary.

### [](#installing-from-a-downloaded-package)Installing from a Downloaded Package

To install the SDK from a wheel on the [GitHub Releases page](https://github.com/couchbaselabs/columnar-python-client/releases):

1. Download the appropriate wheel
2. Unzip the downloaded file
3. Install via pip: `python3 -m pip install <path to unzipped wheel>`

### [](#building-from-source)Building from Source

If a compatible wheel is not available, the SDK’s binary will need to be built from source:

* Follow the steps on the [GitHub Building page](https://github.com/couchbaselabs/columnar-python-client/blob/main/BUILDING.md).
* After the build succeeds, the SDK can be used by running Python scripts from within the cloned repository — or the SDK can be installed via pip: `python3 -m pip install <path to cloned repository>`