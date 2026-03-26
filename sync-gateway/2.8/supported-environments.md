---
title: Supported Environments
description: Couchbase Sync Gateway's Supported Operating System and Cloud environments
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/supported-environments.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::supported-environments.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/supported-environments.html)

# Supported Environments

> Couchbase Sync Gateway's Supported Operating System and Cloud environments  
> Couchbase Sync Gateway is supported on several popular operating systems and virtual environments.

## [](#supported-versions)Supported Versions

Make sure that your chosen operating system or cloud environment is listed in one of the following tables before you install Sync Gateway. See the [Deprecated Versions](#deprecated-versions) section for information about platform support changes, including deprecated platforms.

> [!IMPORTANT]
> Sync Gateway clusters on mixed platforms are not supported. Nodes in a Sync Gateway cluster should all be running on the same OS, and every effort should be made to apply the same OS patches across the entire cluster.

__Table 1\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions                                          |
| ------------------------------- | ----------------------------------------------------------- |
| Red Hat Enterprise Linux (RHEL) | 7.x and 8.x                                                 |
| CentOS                          | 7.x and 8.x                                                 |
| Ubuntu                          | 16.04 LTS and 18.04                                         |
| Debian                          | 8.x and 9.x                                                 |
| Windows Server                  | 2012 (64-bit) DEPRECATED at Sync Gateway 2.8+ 2016 (64-bit) |

__Table 2\. Supported Cloud Environments for Development, Testing, and Production__
| Platform                  | Operating System | Supported Versions |
| ------------------------- | ---------------- | ------------------ |
| AWS                       | Amazon Linux AMI | 2017.092018.03     |
| Azure                     | Ubuntu           | 16.04              |
| Google Cloud              | Ubuntu           | 16.04              |
| Docker (Docker Hub)       | CentOS           | 7                  |
| OpenShift (RedHat Portal) | RHEL             | 7.2                |

__Table 3\. Supported Operating Systems for Development and Testing Only__
| Operating System | Supported Versions            |
| ---------------- | ----------------------------- |
| macOS            | 10.15(Catalina)10.14 (Mojave) |
| Windows Desktop  | 2010                          |

## [](#deprecated-versions)Deprecated Versions

Deprecated versions will be removed in a future release and we recommend that you plan to migrate away from the deprecated OS versions.

__Table 4\. Deprecated at 2.8__
| Operating System         | Deprecated Versions                | Deprecation Release |
| ------------------------ | ---------------------------------- | ------------------- |
| Linux                    | RHEL 6.xCentos 6.xUbuntu 14.04 LTS | 2.6                 |
| Microsoft Windows Server | 2012                               | 2.8                 |

## [](#end-of-life)End of Life

Support for Couchbase Sync Gateway on these operating systems is removed at the current major release

__Table 5\. Removed at 2.8__
| Operating System | Deprecated Versions   | Deprecation Release |
| ---------------- | --------------------- | ------------------- |
| OSX              | 10.12.6 "High Sierra" | 2.6                 |

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)