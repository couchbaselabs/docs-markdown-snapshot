---
title: Supported Platforms
description: Enterprise Analytics supports several popular operating systems and
  virtual environments. The Enterprise Analytics Web Console supports most
  recent major browsers.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/supported-platform.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:install:supported-platform.adoc[]
---

[View original HTML](/enterprise-analytics/current/install/supported-platform.html)

# Supported Platforms

> Enterprise Analytics supports several popular operating systems and virtual environments. The Enterprise Analytics Web Console supports most recent major browsers. 

## [](#Supported-Operating-Systems)Supported Operating Systems

Choose an operating system from the following list for your Enterprise Analytics deployment.

> [!NOTE]
> Couchbase clusters on mixed platforms are not supported and nodes in a Couchbase cluster should be running on the same operating system.

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions (64-bit)                  |
| ------------------------------- | -------------------------------------------- |
| Red Hat Enterprise Linux (RHEL) | 10.x 9.x 8.x                                 |
| Ubuntu                          | 24.04 LTS (x86, ARM64) 22.x LTS (x86, ARM64) |
| Debian                          | 12.x                                         |

## [](#supported-virtualization-and-container-platforms)Supported Virtualization and Container Platforms

When running Enterprise Analytics in virtualized or containerized environments, base the container or VM on 1 of the operating systems listed under [Supported Operating Systems](#Supported-Operating-Systems). Enterprise Analytics has no operating system requirements for the system hosting the VM or container.

__Table 2\. Supported VM and Container Platforms__
| Platform                           | Notes                                                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Docker                             | Enterprise Analytics is compatible with Docker. You can find official Docker images at [Docker Hub](https://hub.docker.com/r/couchbase/enterprise-analytics). |
| Kernel-based Virtual Machine (KVM) | Enterprise Analytics is compatible with KVM.                                                                                                                  |
| VMware                             | Enterprise Analytics is compatible with VMware.                                                                                                               |

## [](#supported-browsers)Supported Web Browsers

Enterprise Analytics Web Console is supported on a variety of modern web browsers.

__Table 3\. Enterprise Analytics Web Console Supported Web Browsers__
| Browser         | Operating System (64-bit) | Browser Version | Enterprise Analytics Version |
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

## [](#supported-object-storage-solutions)Supported Object Storage Solutions

Enterprise Analytics employs a compute-storage separation architecture that allows for scaling compute and storage independently. As a result, it requires an object store as its persistent storage. The certified supported object storage solutions are:

* [AWS S3](../manage/manage-nodes/aws-s3.md)
* [S3-Compatible Storage](../manage/manage-nodes/s3-compatible-storage.md)
* [Azure Blob Storage](../manage/manage-nodes/azure-blob-storage.md)