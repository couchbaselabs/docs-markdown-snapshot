---
title: Supported Platforms
description: Couchbase Server supports several popular operating systems and
  virtual environments. The Couchbase Server Web Console supports most recent
  major browsers.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/install-platforms.adoc
  xref: xref:7.6@server:install:install-platforms.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/install-platforms.html)

# Supported Platforms

> Couchbase Server supports several popular operating systems and virtual environments. The Couchbase Server Web Console supports most recent major browsers. 

## [](#oses)Supported Operating Systems

Choose an operating system from the following list for your Couchbase Server deployment.

> [!NOTE]
> Couchbase clusters on mixed platforms are not supported. Nodes in a Couchbase cluster should all be running on the same OS. Be sure to apply the same OS updates to all nodes the cluster.

ARM64 support requires ARMv8 CPUs, such as the Amazon Graviton series.

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                                          | Supported Versions (64-bit)                                                                                                            |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Alma Linux                                                | 9.x                                                                                                                                    |
| Amazon Linux 2                                            | LTS (x86-64, ARM64) (deprecated in Couchbase Server 7.6)                                                                               |
| Amazon Linux 2023                                         | AL2023 (x86-64, ARM64)                                                                                                                 |
| Debian                                                    | 12.x 11.x                                                                                                                              |
| Oracle Linux\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 9.x 8.x                                                                                                                                |
| Red Hat Enterprise Linux (RHEL)                           | 9.x 8.x                                                                                                                                |
| Rocky Linux                                               | 9.x                                                                                                                                    |
| SUSE Linux Enterprise Server (SLES)                       | 15.x 12.x (Deprecated in Couchbase Server 7.6) Versions earlier than 12 SP2 are no longer supported in Couchbase Server 7.2 and later. |
| Ubuntu                                                    | 24.04 LTS (x86, ARM64) 22.x LTS (x86, ARM64) 20.04 LTS (x86, ARM64) (deprecated in Couchbase Server 7.6)                               |
| Windows Server                                            | 2022 2019 (deprecated in Couchbase Server 7.6)                                                                                         |

__Table 2\. Supported Operating Systems for Development and Testing Only__
| Operating System | Supported Versions (64-bit)                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------ |
| macOS            | 14 "Sonoma" 13 "Ventura" 12 "Monterey" (x86-64 and Apple Silicon ARM64) deprecated in Couchbase Server 7.6.0 |
| Windows Desktop  | 11 10 (requires Anniversary Update) Deprecated in 7.6.4                                                      |

## [](#supported-virtualization-and-container-platforms)Supported Virtualization and Container Platforms

When running Couchbase Server in virtualized or containerized environments, base the container or VM on one of the operating systems listed under [Supported Operating Systems](#oses). Couchbase Server has no operating system requirements for the system hosting the VM or container.

__Table 3\. Supported VM and Container Platforms__
| Platform                           | Notes                                                                                                                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Docker                             | Couchbase Server is compatible with Docker. You can find official Docker images at [Docker Hub](https://hub.docker.com/%5F/couchbase). Follow the best practices to run [Couchbase Server on a virtualized environment](best-practices-vm.md). |
| Kernel-based Virtual Machine (KVM) | Couchbase Server is compatible with KVM. Follow the best practices to run [Couchbase Server on a virtualized environment](best-practices-vm.md).                                                                                               |
| Kubernetes                         | [Couchbase Autonomous Operator](../../../operator/current/overview.md) provides Kubernetes integration.                                                                                                                                        |
| Red Hat OpenShift                  | [Couchbase Autonomous Operator](../../../operator/current/overview.md) provides Red Hat OpenShift integration.                                                                                                                                 |
| VMware                             | Couchbase Server is compatible with VMware. Follow the best practices to run [Couchbase Server on a virtualized environment](best-practices-vm.md).                                                                                            |

## [](#supported-browsers)Supported Web Browsers

Couchbase Web Console is supported on a variety of modern Web browsers.

__Table 4\. Couchbase Web Console Supported Web Browsers__
| Browser         | Operating System (64-bit) | Browser Version | Couchbase platform |
| --------------- | ------------------------- | --------------- | ------------------ |
| Apple Safari    | macOS                     | 11.1+           | 7.67.27.17.0       |
| Google Chrome   | macOS, Windows            | 67+             | 7.67.27.17.0       |
| Microsoft Edge  | Windows                   | 80+             | 7.67.27.17.0       |
| Mozilla Firefox | macOS, Windows            | 67+             | 7.67.27.17.0       |

## [](#capella-browser-support)Capella Browser Support

See [Supported Web Browsers](../../../cloud/reference/browser-compatibility.md) for a list of the web browsers that Capella supports.

---

[1](#%5Ffootnoteref%5F1). Only the Red Hat Compatible Kernel (RHCK) is supported. The Unbreakable Enterprise Kernel (UEK) is not supported.