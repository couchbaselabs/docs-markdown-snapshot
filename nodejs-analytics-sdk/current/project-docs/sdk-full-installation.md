---
title: Full Installation
description: Installation instructions for the Node.js Analytics SDK.
editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:nodejs-analytics-sdk:project-docs:sdk-full-installation.adoc[]
---

[View original HTML](/nodejs-analytics-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Node.js Analytics SDK. 

## [](#before-you-start)Before You Start

Set up an [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) cluster.

### [](#prerequisites)Prerequisites

The Columnar Node.js SDK supports LTS versions of Node.js — these are 24 and 22 at the time of the 1.0.0 release (August 2025). See the [compatibility page](compatibility.md#platform-compatibility) for more information about platform support.

We recommend using the most recent long-term support (LTS) version of Node.js — at the time of writing (August 2025) this is version 24.

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `npm`:

```console
npm install couchbase-analytics
```

## [](#other-installation-methods)Other Installation Methods

A select set of packages with prebuilt binaries are available on the [GitHub Releases page](https://github.com/couchbase/analytics-nodejs-client/releases). If a packages is not available for your specific platform, See the [GitHub Building page](https://github.com/couchbase/analytics-nodejs-client/blob/main/BUILDING.md) for details on how to build the SDK’s binary.

### [](#installing-from-a-downloaded-package)Installing from a Downloaded Package

To install the SDK from a package on the [GitHub Releases page](https://github.com/couchbase/analytics-nodejs-client/releases):

1. Download the appropriate package
2. Unzip the downloaded file
3. Install via npm: `npm install <path to unzipped file>`

### [](#building-from-source)Building from Source

If a compatible package is not available, the SDK’s binary will need to be built from source:

* Follow the steps on the [GitHub Building page](https://github.com/couchbase/analytics-nodejs-client/blob/main/BUILDING.md).
* After the build succeeds, the SDK can be used by running Node scripts from within the cloned repository — or the SDK can be installed via `npm`: `npm install <path to cloned repository>`.