---
title: System Requirements
description: Couchbase Server has a basic set of installation and networking
  requirements that apply to nearly every deployment.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/plan-for-production.adoc
  xref: xref:7.6@server:install:plan-for-production.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/plan-for-production.html)

# System Requirements

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Couchbase Server has a basic set of installation and networking requirements that apply to nearly every deployment. 

Deploying Couchbase Server into production requires that the hardware and software requirements are met, and that the deployment guidelines and security considerations are taken into account before installation.

__Table 1\. Couchbase System Requirements__
| Requirement                          | Description                                                                                                                                                                                                                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Platform support**                 | Ensure that you are deploying onto a platform that is supported. [Supported Platforms](install-platforms.md)                                                                                                                                                                  |
| **Hardware requirements**            | Ensure that your production environment has adequate hardware and system resources to meet the needs of your deployment. [System Resource Requirements](pre-install.md)                                                                                                       |
| **Additional requirements**          | Ensure that your production environment meets all the necessary additional requirements for the components that you plan to deploy. [Additional Requirements](install-environments.md)                                                                                        |
| **Networking requirements**          | Review the Couchbase Server networking requirements to ensure that your environment can accommodate the various components that you plan to deploy. [Couchbase Server Ports](install-ports.md) [Using IPv6 With Couchbase](../manage/manage-nodes/manage-address-families.md) |
| **Deployment-specific requirements** | Review [Deployment Guidelines](install-production-deployment.md) to make sure you are following the best practices for your deployment.                                                                                                                                       |