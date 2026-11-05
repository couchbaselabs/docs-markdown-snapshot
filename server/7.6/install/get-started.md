---
title: Couchbase Server Deployment Options
description: Couchbase Server can be deployed on a variety of platforms, from
  traditional bare metal servers, to containers running in a public or private
  cloud.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/get-started.adoc
  xref: xref:7.6@server:install:get-started.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/get-started.html)

# Couchbase Server Deployment Options

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Couchbase Server can be deployed on a variety of platforms, from traditional bare metal servers, to containers running in a public or private cloud. 

__Table 1\. Options to Get Started With Couchbase Server__
| ![couchbase logo](_images/couchbase-logo.jpg)On-Premises (Non-Cloud)                                                                                                | ![couchbase in containers](_images/couchbase-in-containers.jpg)Virtual Machines and Containers                                                                                                                                            | ![couchbase in the cloud](_images/couchbase-in-the-cloud.jpg)Public Cloud                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deploy Couchbase Server in a traditional data center on bare metal servers.                                                                                         | Deploy Couchbase Server within a virtualized or containerized environment, such as VMware or Docker.                                                                                                                                      | Deploy Couchbase Server in a public cloud, such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform.                                                                     |
| [System Requirements](plan-for-production.md) [Deployment Guidelines](install-production-deployment.md) [Installing the Couchbase Server Cluster](install-intro.md) | [Deployment Considerations for Virtual Machines and Containers](best-practices-vm.md) [Deploying Couchbase Server in Containers](../cloud/couchbase-cloud-deployment.md) [Couchbase Containers FAQ](../cloud/couchbase-containers-faq.md) | [Deploying Couchbase in the Cloud](../cloud/couchbase-cloud-deployment.md) [Getting started with Couchbase Capella, our fully-managed solution](../../../cloud/get-started/create-account.md) |

## [](#about-couchbase-server-editions)About Couchbase Server Editions

Couchbase Server comes in two different editions: Enterprise Edition and Community Edition. Each edition offers different features and levels of support that might affect your deployment. The [Couchbase Editions](https://www.couchbase.com/products/editions) page provides a feature comparison of each edition. Couchbase Server Enterprise Edition is recommended for production environments.