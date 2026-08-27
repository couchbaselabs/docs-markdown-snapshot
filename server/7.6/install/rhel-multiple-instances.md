---
title: Installing Multiple Instances on Linux Platforms
description: Multiple instances of Couchbase Server can be installed on one
  physical machine for the Linux operating system.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/rhel-multiple-instances.adoc
  xref: xref:7.6@server:install:rhel-multiple-instances.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/rhel-multiple-instances.html)

# Installing Multiple Instances on Linux Platforms

> Multiple instances of Couchbase Server can be installed on one physical machine for the Linux operating system. 

> [!IMPORTANT]
> This installation method is intended for development purposes only and not supported in production.

The number of Couchbase Server instances running on a single machine depends on its physical capacity.

## [](#requirements)Requirements

Make sure that a minimum of 4Gb RAM and 8 Core CPUs are available for each Couchbase Server instance. When installing multiple instances on a physical machine, install as one of these two users:

## [](#setting-up-multiple-instances)Setting up Multiple Instances

Use Docker to set up multiple cluster instances running on a physical machine.

The steps to carry out the Docker installation are given here: [getting-started-docker.adoc#section\_deploy\_multiple\_clusters](getting-started-docker.md#section%5Fdeploy%5Fmultiple%5Fclusters)