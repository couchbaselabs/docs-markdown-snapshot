---
title: Upgrade Sync Gateway
description: Overview of upgrade paths, version requirements, and supported
  approaches for upgrading Sync Gateway.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/ROOT/pages/upgrading.adoc
  xref: xref:sync-gateway::upgrading.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/upgrading.html)

# Upgrade Sync Gateway

> Overview of upgrade paths, version requirements, and supported approaches for upgrading Sync Gateway.  

Related _Application Deployment_ topics: [Prepare](start-here/get-started-prepare.md) | [Install](start-here/get-started-install.md) | [Release Notes](product-notes/release-notes.md)

## [](#overview)Overview

This section covers upgrading Sync Gateway to a new version. Use the pages in this section based on what you need to do:

* [Rolling Upgrade](rolling-upgrade.md) — Step-by-step procedures for upgrading a Sync Gateway cluster node by node, including version-specific requirements.
* [Cluster Compatibility Version](cluster-compatibility-version.md) — How to use the cluster compatibility version mechanism introduced in Sync Gateway 4.1 to upgrade without downtime and with a safe rollback path.
* [Migrate Metadata to System Collection](migrate-metadata-system-collection.md) — How to opt in to moving Sync Gateway internal metadata from the default collection to the system collection in Sync Gateway 4.1.

For compatibility information, see the [Compatibility Matrix](product-notes/compatibility.md).

## [](#upgrade-requirements-by-version)Upgrade Requirements by Version

### [](#syncgateway-4-1)Sync Gateway 4.1

| Requirement                   | Detail                                                                                                                                                                                                                                                                                        |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Couchbase Server              | 7.6.0 or later. 7.6.6 or later required for bi-directional XDCR features.                                                                                                                                                                                                                     |
| Unsupported settings          | The following settings are not supported and must be removed from your configuration before upgrading: shared\_bucket\_access=false allow\_conflicts=true enable\_star\_channel=false                                                                                                         |
| Metadata migration (optional) | Sync Gateway 4.1 introduces an opt-in migration that moves internal metadata from the default collection to the system collection. This is not required for upgrading and is never applied automatically. See [Migrate Metadata to System Collection](migrate-metadata-system-collection.md). |

> [!NOTE]
> Downgrading from Sync Gateway 4.1 to an earlier version is not supported after the full cluster has been upgraded. To preserve a rollback path during the upgrade window, use [Cluster Compatibility Version](cluster-compatibility-version.md).

### [](#syncgateway-4-0)Sync Gateway 4.0

| Requirement          | Detail                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Couchbase Server     | 7.6.0 or later. 7.6.6 or later required for bi-directional XDCR features.                                                                                                             |
| Unsupported settings | The following settings are not supported and must be removed from your configuration before upgrading: shared\_bucket\_access=false allow\_conflicts=true enable\_star\_channel=false |

> [!NOTE]
> Downgrading from Sync Gateway 4.0 to earlier versions is not supported.

### [](#syncgateway-3-1)Sync Gateway 3.1

| Requirement      | Detail                                                                                                                                                                                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Couchbase Server | See [Compatibility Matrix](product-notes/compatibility.md) for the minimum supported Couchbase Server version for Sync Gateway 3.1.                                                            |
| Configuration    | Sync Gateway 3.1 uses Persistent Configuration by default. Upgrading to 3.1 converts existing configuration files to the persistent format automatically. This migration is a one-way process. |

## [](#upgrading-couchbase-server)Upgrading Couchbase Server

If you also need to upgrade Couchbase Server, for more information, see the [Upgrading Couchbase Server](../../server/current/install/upgrade.md) documentation for supported approaches. When running a Couchbase Server rolling upgrade alongside Sync Gateway, Server rebalance operations can cause transient connection errors between Sync Gateway and Couchbase Server.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](start-here/get-started-prepare.md)
* [Install](start-here/get-started-install.md)
* [Configure](start-here/get-started-configure.md)

###### [](#-3)

Product Information

* [Release Notes](product-notes/release-notes.md)
* [Compatibility Matrix](product-notes/compatibility.md)
* [Supported OS](product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)