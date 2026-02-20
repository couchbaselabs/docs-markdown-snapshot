---
title: Supported Environments
description: Sync Gateway's Supported Operating System and Cloud environments
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/product-notes/pages/supported-environments.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.3@sync-gateway:product-notes:supported-environments.adoc[]
---

[View original HTML](/sync-gateway/3.3/product-notes/supported-environments.html)

# Supported Environments

> Sync Gateway’s Supported Operating System and Cloud environments  
> Sync Gateway is supported on several popular operating systems and virtual environments.

## [](#supported-versions)Supported Versions

Make sure that your chosen operating system or cloud environment is listed in one of the following tables before you install _Sync Gateway_. See the [Deprecated Versions](#deprecated-versions) section for information about platform support changes, including deprecated platforms.

> [!IMPORTANT]
> sync gateway clusters on mixed platforms are not supported. Nodes in a sync gateway cluster should all be running on the same OS, and every effort should be made to apply the same OS patches across the entire cluster.

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions           |
| ------------------------------- | ---------------------------- |
| Red Hat Enterprise Linux (RHEL) | 10.x                         |
| 9.x                             |                              |
| Alma Linux                      | 9.x                          |
| Rocky Linux                     | 9.x                          |
| Ubuntu                          | 24.04 LTS ARM, 24.04 LTS x86 |
| 22.04 LTS ARM, 22.04 LTS x86    |                              |
| Debian                          | 12.x                         |
| 11.x                            |                              |
| Windows Server                  | 2022                         |

__Table 2\. Supported Cloud Environments for Development, Testing, and Production__
| Platform                  | Operating System                       | Supported Versions                         |
| ------------------------- | -------------------------------------- | ------------------------------------------ |
| AWS                       | Amazon Linux                           | 2023 LTS (ARM, x86)                        |
| Amazon Linux              | 2 LTS (ARM, x86) — Deprecated at 3.3.0 |                                            |
| Azure                     | Ubuntu                                 | 24.04 LTS (ARM, x86), 22.04 LTS (ARM, x86) |
| Google Cloud              | Ubuntu                                 | 24.04 LTS (ARM, x86) 22.04 LTS (ARM, x86)  |
| OpenShift (RedHat Portal) | RHEL                                   | 10                                         |
| RHEL                      | 9                                      |                                            |
| Ubuntu                    |                                        | 24.04 LTS, 22.04 LTS                       |

__Table 3\. Supported Operating Systems for Development and Testing Only__
| Operating System                          | Supported Versions  |
| ----------------------------------------- | ------------------- |
| macOS                                     | 14 M1 ARM64, 14 x86 |
| 13 M1 ARM64, 13 x86 — Deprecated at 3.3.0 |                     |
| Windows Desktop                           | 11                  |
| 10                                        |                     |

## [](#deprecated-versions)Deprecated Versions

Deprecated versions will be removed in a future release and we recommend that you plan to migrate away from the deprecated OS versions.

__Table 4\. Deprecated Versions Table__
| Operating System | Versions             | Deprecation Release |
| ---------------- | -------------------- | ------------------- |
| Amazon Linux     | 2 LTS ARM, 2 LTS x86 | 3.3.0               |
| MacOS            | 13 M1 ARM64, 13 x86  | 3.3.0               |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)