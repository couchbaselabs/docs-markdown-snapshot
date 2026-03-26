---
title: Full Installation
description: Installation instructions for the Node.js Columnar SDK.
editUrl: https://github.com/couchbase/docs-columnar-sdk-nodejs/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:nodejs-columnar-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-columnar-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Node.js Columnar SDK. 

## [](#before-you-start)Before You Start

Sign up for a [Capella account](../../../cloud/get-started/create-account.md), and choose a [Columnar](../../../analytics/intro/intro.md) cluster.

### [](#prerequisites)Prerequisites

The Columnar Node.js SDK supports LTS versions of Node.js — these are 20 and 22 at the time of the 1.0.0 release (October 2024). See the [compatibility page](compatibility.md#platform-compatibility) for more information about platform support.

We recommend using the most recent long-term support (LTS) version of Node.js — at the time of writing (October 2024) this is version 22.

> [!WARNING]
> Don't Mix Columnar & Operational SDKs.
> 
> Do not combine the Node.js Columnar SDK with the Node.js Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs.
> 
> Note, this does not apply to combining our Enterprise Analytics SDKs with our Operational SDKs. See the [Analytics SDK page](../../../home/analytics-sdk.md) for a reminder of which Analytics SDK to use with which Analytics service.

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `npm`:

```console
npm install couchbase-columnar
```

## [](#other-installation-methods)Other Installation Methods

A select set of packages with prebuilt binaries are available on the [GitHub Releases page](https://github.com/couchbaselabs/columnar-nodejs-client/releases). If a packages is not available for your specific platform, See the [GitHub Building page](https://github.com/couchbaselabs/columnar-nodejs-client/blob/main/BUILDING.md) for details on how to build the SDK's binary.

### [](#installing-from-a-downloaded-package)Installing from a Downloaded Package

To install the SDK from a package on the [GitHub Releases page](https://github.com/couchbaselabs/columnar-nodejs-client/releases):

1. Download the appropriate package
2. Unzip the downloaded file
3. Install via npm: `npm install <path to unzipped file>`

### [](#building-from-source)Building from Source

If a compatible package is not available, the SDK's binary will need to be built from source:

* Follow the steps on the [GitHub Building page](https://github.com/couchbaselabs/columnar-nodejs-client/blob/main/BUILDING.md).
* After the build succeeds, the SDK can be used by running Node scripts from within the cloned repository — or the SDK can be installed via `npm`: `npm install <path to cloned repository>`.