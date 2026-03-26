---
title: Supported Environments
description: Sync Gateway's Supported Operating System and Cloud environments
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/supported-environments.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@sync-gateway::supported-environments.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/supported-environments.html)

# Supported Environments

> Sync Gateway's Supported Operating System and Cloud environments  
> Sync Gateway is supported on several popular operating systems and virtual environments.

## [](#supported-versions)Supported Versions

Make sure that your chosen operating system or cloud environment is listed in one of the following tables before you install _Sync Gateway_. See the [Deprecated Versions](#deprecated-versions) section for information about platform support changes, including deprecated platforms.

> [!IMPORTANT]
> sync gateway clusters on mixed platforms are not supported. Nodes in a sync gateway cluster should all be running on the same OS, and every effort should be made to apply the same OS patches across the entire cluster.

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions                      |
| ------------------------------- | --------------------------------------- |
| Red Hat Enterprise Linux (RHEL) | 7.x and 8.x                             |
| CentOS                          | 7.x and 8.x                             |
| Ubuntu                          | 20.04 LTS and 18.04                     |
| 16.04 — deprecated at 3.0.0     |                                         |
| Debian                          | 10.x and 9.x                            |
| 8.x — deprecated at 3.0.0       |                                         |
| Windows Server                  | 20192016 (64-bit) — deprecated at 3.0.0 |

__Table 2\. Supported Cloud Environments for Development, Testing, and Production__
| Platform                  | Operating System      | Supported Versions |
| ------------------------- | --------------------- | ------------------ |
| AWS                       | Amazon Linux 2 ARM v8 | LTS                |
| Azure                     | Ubuntu                | 20.0418.04         |
| Google Cloud              | Ubuntu                | 20.0418.04         |
| Docker (Docker Hub)       | CentOS                | 7                  |
| OpenShift (RedHat Portal) | RHEL                  | 7.2                |

__Table 3\. Supported Operating Systems for Development and Testing Only__
| Operating System | Supported Versions             |
| ---------------- | ------------------------------ |
| macOS            | 11.x (Big Sur) 10.15(Catalina) |
| Windows          | Desktop 10                     |
| Apple M1 ARM64   | macOS 11                       |

## [](#deprecated-versions)Deprecated Versions

Deprecated versions will be removed in a future release and we recommend that you plan to migrate away from the deprecated OS versions.

__Table 4\. Deprecated at 2.8__
| Operating System         | Deprecated Versions                | Deprecation Release |
| ------------------------ | ---------------------------------- | ------------------- |
| Linux                    | RHEL 6.xCentos 6.xUbuntu 14.04 LTS | 2.6                 |
| Microsoft Windows Server | 2012                               | 2.8                 |

## [](#end-of-life)End of Life

Support for sync gateway on these operating systems is removed at the current major release

__Table 5\. Removed at 3.0.0__
| Operating System | Deprecated Versions | Deprecation Release |
| ---------------- | ------------------- | ------------------- |
| Windows Server   | 2012 (64-bit)       | 3.0.0               |
| OSX              | 10.14 "Mojave"      | 3.0.0               |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)