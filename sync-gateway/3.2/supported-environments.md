[View original HTML](/sync-gateway/3.2/supported-environments.html)

> Sync Gateway’s Supported Operating System and Cloud environments  
> Sync Gateway is supported on several popular operating systems and virtual environments.

## [](#supported-versions)Supported Versions

Make sure that your chosen operating system or cloud environment is listed in one of the following tables before you install _Sync Gateway_. See the [Deprecated Versions](#deprecated-versions) section for information about platform support changes, including deprecated platforms.

|  | Sync Gateway clusters on mixed platforms are not supported. Nodes in a Sync Gateway cluster should all be running on the same OS, and every effort should be made to apply the same OS patches across the entire cluster. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions           |
| ------------------------------- | ---------------------------- |
| Red Hat Enterprise Linux (RHEL) | 9.x                          |
| 8.x — Deprecated at 3.2.0       |                              |
| Alma Linux                      | 9.x                          |
| Rocky Linux                     | 9.x                          |
| Ubuntu                          | 24.04 LTS ARM, 24.04 LTS x86 |
| 22.04 LTS ARM, 22.04 LTS x86    |                              |
| 20.04 LTS ARM, 20.04 LTS x86    |                              |
| Debian                          | 12.x                         |
| 11.x                            |                              |
| 10.x — Deprecated at 3.2.0      |                              |
| Windows Server                  | 2022                         |
| 2019 — Deprecated at 3.2.0      |                              |

__Table 2\. Supported Cloud Environments for Development, Testing, and Production__
| Platform                  | Operating System                                        | Supported Versions                                               |
| ------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------- |
| AWS                       | Amazon Linux 2023 (ARM, x86), Amazon Linux 2 (ARM, x86) | LTS                                                              |
| Azure                     | Ubuntu                                                  | 24.04 LTS (ARM, x86), 22.04 LTS (ARM, x86), 20.04 LTS (ARM, x86) |
| Google Cloud              | Ubuntu                                                  | 24.04 LTS (ARM, x86) 22.04 LTS (ARM, x86), 20.04 LTS (ARM, x86)  |
| OpenShift (RedHat Portal) | RHEL                                                    | 9                                                                |
| RHEL                      | 8 — Deprecated at 3.2.0                                 |                                                                  |
| Ubuntu                    |                                                         | 24.04 LTS, 22.04 LTS, 20.04 LTS                                  |

__Table 3\. Supported Operating Systems for Development and Testing Only__
| Operating System               | Supported Versions |
| ------------------------------ | ------------------ |
| macOS                          | 14                 |
| 13                             |                    |
| 12 — Deprecated at 3.2.0       |                    |
| Windows Desktop                | 11                 |
| 10                             |                    |
| Apple M1 ARM64                 | macOS 14           |
| macOS 13                       |                    |
| macOS 12 — Deprecated at 3.2.0 |                    |

## [](#deprecated-versions)Deprecated Versions

Deprecated versions will be removed in a future release and we recommend that you plan to migrate away from the deprecated OS versions.

__Table 4\. Deprecated Versions Table__
| Operating System                | Versions                     | Deprecation Release |
| ------------------------------- | ---------------------------- | ------------------- |
| Red Hat Enterprise Linux (RHEL) | 8                            | 3.2.0               |
| Ubuntu                          | 20.04 LTS ARM, 20.04 LTS x86 | 3.2.0               |
| Debian                          | 10                           | 3.2.0               |
| Windows Server                  | 2019                         | 3.2.0               |
| MacOS                           | 12                           | 3.2.0               |

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