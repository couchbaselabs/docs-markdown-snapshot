---
title: Full Installation
description: Installation instructions for the Python Operational Insights SDK.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Python Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-python/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:python-operational-insights-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-operational-insights-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Python Operational Insights SDK. 

## [](#before-you-start)Before You Start

Set up an [Operational Insights](../../../operational-insights/current/intro/intro.md) cluster.

### [](#prerequisites)Prerequisites

Currently Python 3.11 - Python 3.15 is supported. See the [compatibility page](compatibility.md#platform-compatibility) for more information about platform support.

We also recommend the following command to install or update `pip`, `setuptools`, and `wheel`:

```console
$ python3 -m pip install --upgrade pip setuptools wheel
```

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `pip`:

```console
$ python3 -m pip install couchbase-operational-insights
```

## [](#other-installation-methods)Other Installation Methods

### [](#install-from-source)Install from Source

The SDK can be installed from source with the following command:

```console
$ python3 -m pip install git+https://github.com/couchbase/operational-insights-python-client.git
```