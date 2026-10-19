---
title: Supported Platforms
description: Operational Insights supports several popular operating systems and
  virtual environments. The Operational Insights Web Console supports most
  recent major browsers.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/supported-platform.adoc
  xref: xref:enterprise-analytics:install:supported-platform.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/supported-platform.html)

# Supported Platforms

> Operational Insights supports several popular operating systems and virtual environments. The Operational Insights Web Console supports most recent major browsers. 

## [](#Supported-Operating-Systems)Supported Operating Systems

Choose an operating system from the following list for your Operational Insights deployment.

> [!NOTE]
> Couchbase clusters on mixed platforms are not supported and nodes in a Couchbase cluster should be running on the same operating system.

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions (64-bit)                  |
| ------------------------------- | -------------------------------------------- |
| Red Hat Enterprise Linux (RHEL) | 10.x 9.x 8.x                                 |
| Ubuntu                          | 24.04 LTS (x86, ARM64) 22.x LTS (x86, ARM64) |
| Debian                          | 12.x                                         |

## [](#supported-virtualization-and-container-platforms)Supported Virtualization and Container Platforms

When running Operational Insights in virtualized or containerized environments, base the container or VM on 1 of the operating systems listed under [Supported Operating Systems](#Supported-Operating-Systems). Operational Insights has no operating system requirements for the system hosting the VM or container.

__Table 2\. Supported VM and Container Platforms__
| Platform                           | Notes                                                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Docker                             | Operational Insights is compatible with Docker. You can find official Docker images at [Docker Hub](https://hub.docker.com/r/couchbase/operational-insights). |
| Kernel-based Virtual Machine (KVM) | Operational Insights is compatible with KVM.                                                                                                                  |
| VMware                             | Operational Insights is compatible with VMware.                                                                                                               |

## [](#supported-browsers)Supported Web Browsers

Operational Insights Web Console is supported on a variety of modern web browsers.

__Table 3\. Operational Insights Web Console Supported Web Browsers__
| Browser         | Operating System (64-bit) | Browser Version | Operational Insights Version |
| --------------- | ------------------------- | --------------- | ---------------------------- |
| Apple Safari    | macOS                     | 11.1+           | 2.0+                         |
| Google Chrome   | macOS                     | 67+             | 2.0+                         |
| Microsoft Edge  | Windows                   | 80+             | 2.0+                         |
| Mozilla Firefox | macOS                     | 67+             | 2.0+                         |

## [](#recommended-nodes-requirement)Recommended Nodes Requirement

__Table 4\. Recommended Nodes Requirement__
| Components          | Recommended Requirement                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| Nodes               | 1 (Minimum for Dev and Test) 3-32 ( For Production )                                     |
| Nodes Configuration | 4 Cores/32GiB 8 Cores/32GiB 8 Cores/64GiB 16 Cores/64GiB 16 Cores/128GiB 32 Cores/256GiB |