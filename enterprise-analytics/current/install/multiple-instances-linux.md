---
title: Installing Multiple Instances on Linux Platforms
description: You can install multiple instances of Enterprise Analytics on one
  physical machine for the Linux operating system.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/install/pages/multiple-instances-linux.adoc
  xref: xref:enterprise-analytics:install:multiple-instances-linux.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/install/multiple-instances-linux.html)

# Installing Multiple Instances on Linux Platforms

> You can install multiple instances of Enterprise Analytics on one physical machine for the Linux operating system. 

> [!IMPORTANT]
> This installation method is intended for development purposes only and not supported in production.

The number of Enterprise Analytics instances running on a single machine depends on its physical capacity.

## [](#requirements)Requirements

Make sure that a minimum of 4Gb RAM and 8 Core CPUs are available for each Enterprise Analytics instance. When installing multiple instances on a physical machine, install as a `sudo` user.

## [](#setting-up-multiple-instances)Setting Up Multiple Instances

Use Docker to set up multiple cluster instances running on a physical machine.

For information about Docker installation, see [Install Enterprise Analytics Using Docker](getting-started-docker.md).