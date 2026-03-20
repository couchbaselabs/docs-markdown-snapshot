---
title: Supported Platforms
description: Couchbase Server is supported on several popular operating systems
  and virtual environments.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/install-platforms.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:install:install-platforms.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/install-platforms.html)

# Supported Platforms

> Couchbase Server is supported on several popular operating systems and virtual environments. 

## [](#supported-operating-systems)Supported Operating Systems

Make sure that your chosen operating system is listed below before you install Couchbase Server.

Note that Couchbase clusters on mixed platforms are not supported. Nodes in a Couchbase cluster should all be running on the same OS, and every effort should be made to apply the same OS patches across the entire cluster.

ARM64 support requires ARMv8 CPUs, such as the Amazon Graviton series.

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                                          | Supported Versions (64-bit)                                                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Alma Linux                                                | 9.x                                                                                                                                   |
| Amazon Linux 2                                            | LTS (x86-64, ARM64)                                                                                                                   |
| Amazon Linux 2023                                         | AL2023 (x86-64, ARM64)                                                                                                                |
| Debian                                                    | 11.x 10.x (deprecated in 7.2)                                                                                                         |
| Oracle Linux\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 8.x 9.x                                                                                                                               |
| Red Hat Enterprise Linux (RHEL)                           | 7.x (unsupported in Couchbase Server 7.2) 8.x 9.x                                                                                     |
| Rocky Linux                                               | 9.x                                                                                                                                   |
| SUSE Linux Enterprise Server (SLES)                       | 12.x (deprecated in Couchbase Server 7.2) 15.x (Note that versions earlier than SP2 are no longer supported in Couchbase Server 7.2.) |
| Ubuntu                                                    | 24.04 LTS (x86, ARM64)  22.x LTS (x86, ARM64)  20.04 LTS (x86, ARM64) (deprecated in Couchbase Server 7.6)                            |
| Windows Server                                            | 2022 2019                                                                                                                             |

__Table 2\. Supported Operating Systems for Development and Testing Only__
| Operating System | Supported Versions (64-bit)                                                     |
| ---------------- | ------------------------------------------------------------------------------- |
| macOS            | 11 "Big Sur" (deprecated in 7.2) 12 "Monterey" (x86-64 and Apple Silicon ARM64) |
| Windows Desktop  | 10 (requires Anniversary Update)                                                |

## [](#supported-virtualization-and-container-platforms)Supported Virtualization and Container Platforms

__Table 3\. Supported VM and Container Platforms__
| Platform                           | Notes                                                                                                                                                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Docker                             | Couchbase Server is compatible with Docker. Official Docker images are available on [Docker Hub](https://hub.docker.com/%5F/couchbase). Follow the best practices to run [Couchbase Server on a virtualized environment](best-practices-vm.md). |
| Kernel-based Virtual Machine (KVM) | Couchbase Server is compatible with KVM. Follow the best practices to run [Couchbase Server on a virtualized environment](best-practices-vm.md).                                                                                                |
| Kubernetes                         | First-party integration with Kubernetes is made available with the [Couchbase Autonomous Operator](../../../operator/current/overview.md).                                                                                                      |
| Red Hat OpenShift                  | First-party integration with Red Hat OpenShift is made available with the [Couchbase Autonomous Operator](../../../operator/current/overview.md).                                                                                               |
| VMware                             | Couchbase Server is compatible with VMware. Follow the best practices to run [Couchbase Server on a virtualized environment](best-practices-vm.md).                                                                                             |

## [](#supported-browsers)Supported Web Browsers

Couchbase Web Console is supported on a variety of modern Web browsers.

__Table 4\. Couchbase Web Console Supported Web Browsers__
| Browser         | Operating System (64-bit) | Browser Version | Couchbase platform |
| --------------- | ------------------------- | --------------- | ------------------ |
| Apple Safari    | macOS                     | 11.1+           | 7.27.17.0          |
| Google Chrome   | macOS, Windows            | 67+             | 7.27.17.0          |
| Microsoft Edge  | Windows                   | 80+             | 7.27.17.0          |
| Mozilla Firefox | macOS, Windows            | 67+             | 7.27.17.0          |

## [](#capella-browser-support)Capella Browser Support

A list of the supported web browsers for Capella is provided [here](../../../cloud/reference/browser-compatibility.md).

---

[1](#%5Ffootnoteref%5F1). Only the Red Hat Compatible Kernel (RHCK) is supported. The Unbreakable Enterprise Kernel (UEK) is not supported.