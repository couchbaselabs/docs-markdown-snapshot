---
title: Full Installation
description: Installation instructions for the Python Analytics SDK.
editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.1/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:python-analytics-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-analytics-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Python Analytics SDK. 

## [](#before-you-start)Before You Start

Set up an [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) cluster.

### [](#prerequisites)Prerequisites

Currently Python 3.10 - Python 3.14 is supported. See the [compatibility page](compatibility.md#platform-compatibility) for more information about platform support.

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `pip`:

```console
python -m pip install couchbase-analytics
```

## [](#other-installation-methods)Other Installation Methods

### [](#install-from-source)Install from Source

The SDK can be installed from source with the following command:

```console
python -m pip install git+https://github.com/couchbase/analytics-python-client.git
```