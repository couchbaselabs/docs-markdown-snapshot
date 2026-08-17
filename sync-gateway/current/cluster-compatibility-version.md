---
title: Cluster Compatibility Version
description: Use the cluster compatibility version to perform a rolling upgrade
  of Sync Gateway 4.1 without downtime and with a safe rollback path.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/ROOT/pages/cluster-compatibility-version.adoc
  xref: xref:sync-gateway::cluster-compatibility-version.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/cluster-compatibility-version.html)

# Cluster Compatibility Version

> Use the cluster compatibility version to perform a rolling upgrade of Sync Gateway 4.1 without downtime and with a safe rollback path.  

Related _Application Deployment_ topics: [Release Notes](product-notes/release-notes.md) | [Compatibility Matrix](product-notes/compatibility.md)

## [](#overview)Overview

The cluster compatibility version is a cluster-wide value that Sync Gateway uses to coordinate behaviour across nodes running different versions during a rolling upgrade.

Introduced in Sync Gateway 4.1, the cluster compatibility version lets you:

* Perform a rolling upgrade without downtime or reduction in cluster capacity.
* Preserve a safe rollback path during the upgrade window.
* Ensure that new cluster-wide features activate only after all nodes reach the new version.

> [!NOTE]
> Downgrading after the full cluster has been upgraded is not supported. The cluster compatibility version mechanism provides an upgrade rollback path while at least one node is still on the previous version, or the compatibility version is still frozen at a previous version.

## [](#how-the-cluster-compatibility-version-works)How the Cluster Compatibility Version Works

Without a freeze, the cluster compatibility version is always the minimum version across all live nodes in the cluster. As you upgrade nodes one by one, the minimum advances when older nodes are replaced.

Sync Gateway uses the compatibility version to gate cluster-wide feature activation. Features that could cause incompatibilities with older nodes remain inactive until the compatibility version reaches the version that introduced them. New features that do not depend on metadata shared by other Sync Gateway nodes activate immediately on each upgraded node regardless of the compatibility version. These are considered node-local features, and include areas such as caching, read-only operations, general bug fixes, and performance improvements.

On a homogeneous cluster where all nodes run the same version, the compatibility version equals that version. The value is not present in the API response immediately after startup before any node has registered.

## [](#about-the-freeze)About the Freeze

Freezing pins the cluster compatibility version at its current value, regardless of which nodes you subsequently upgrade. While the version is frozen, upgrading a node does not advance the reported compatibility version.

This preserves the option to roll back any upgraded node to the previous version without data loss or invasive data operations such as bucket flushing or backup and restore.

Use the freeze when you want a safe rollback window during the upgrade. It is optional. If you do not need a rollback path, you can upgrade without freezing.

> [!IMPORTANT]
> A freeze persists across node restarts. It is cluster-wide and stored in the cluster, not in node memory. You must unfreeze manually by calling the unfreeze endpoint. The freeze does not clear automatically when all nodes reach the new version.

## [](#upgrade-with-cluster-compatibility-version-safe-rollback-path)Upgrade with Cluster Compatibility Version (Safe Rollback Path)

Use this procedure when you want to preserve the option to roll back during the upgrade.

### [](#prerequisites)Prerequisites

* All nodes are running Sync Gateway 4.1 or later.
* You have Admin REST API access to the cluster.
* See [Rolling Upgrade](rolling-upgrade.md) for version requirements and the node upgrade procedure.

### [](#procedure)Procedure

Step 1: Check the current cluster compatibility version

Call [GET /\_cluster\_compat\_version](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/get%5F%5Fcluster%5Fcompat%5Fversion) to confirm the current state before starting.

```bash
GET /_cluster_compat_version
```

Example response on a homogeneous 4.1 cluster:

```json
{
  "cluster_compat_version": "4.1",
  "nodes": {
    "node1-uid": "4.1",
    "node2-uid": "4.1",
    "node3-uid": "4.1"
  }
}
```

Step 2: Freeze the cluster compatibility version

Call [POST /\_cluster\_compat\_version/freeze](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fcluster%5Fcompat%5Fversion%5Ffreeze) to pin the version before upgrading any node.

```bash
POST /_cluster_compat_version/freeze
```

Example response:

```json
{
  "cluster_compat_version": "4.1",
  "nodes": {
    "node1-uid": "4.1",
    "node2-uid": "4.1",
    "node3-uid": "4.1"
  },
  "frozen_cluster_compat_version": "4.1"
}
```

The presence of `frozen_cluster_compat_version` in the response confirms the freeze is active.

Step 3: Upgrade each node

For each node in the cluster, follow the steps in [Rolling Upgrade](rolling-upgrade.md).

While the freeze is in effect, `cluster_compat_version` remains pinned at the frozen value even as nodes come online at the new version. Call [GET /\_cluster\_compat\_version](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/get%5F%5Fcluster%5Fcompat%5Fversion) at any time to confirm the freeze is still active and to check the individual version of each node.

Step 4: Verify all nodes are on the new version

Call [GET /\_cluster\_compat\_version](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/get%5F%5Fcluster%5Fcompat%5Fversion) and confirm all nodes in the `nodes` map show the new version.

```json
{
  "cluster_compat_version": "4.1",
  "nodes": {
    "node1-uid": "4.2",
    "node2-uid": "4.2",
    "node3-uid": "4.2"
  },
  "frozen_cluster_compat_version": "4.1"
}
```

Step 5: Unfreeze to commit the upgrade

Call [POST /\_cluster\_compat\_version/unfreeze](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fcluster%5Fcompat%5Fversion%5Funfreeze) to clear the freeze.

```bash
POST /_cluster_compat_version/unfreeze
```

Example response after a successful unfreeze:

```json
{
  "cluster_compat_version": "4.2",
  "nodes": {
    "node1-uid": "4.2",
    "node2-uid": "4.2",
    "node3-uid": "4.2"
  }
}
```

The absence of `frozen_cluster_compat_version` confirms the freeze has cleared. The `cluster_compat_version` advances to `4.2` and new cluster-wide features introduced in 4.2 become active.

> [!NOTE]
> If the unfreeze does not fully apply, the endpoint returns a 503 with the current state. The `cluster_compat_version` may still be held back. Retry the unfreeze request.

## [](#rolling-back-during-an-upgrade)Rolling Back During an Upgrade

If you discover an issue after upgrading some nodes and the freeze is in effect, you can roll back the upgraded nodes to the previous version.

1. Downgrade the affected nodes to the previous Sync Gateway version using the same rolling process: remove from load balancer, downgrade, restart, verify, re-add.
2. The `cluster_compat_version` remains pinned at the frozen value throughout.
3. Once all nodes are back on the previous version, call [POST /\_cluster\_compat\_version/unfreeze](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fcluster%5Fcompat%5Fversion%5Funfreeze) to clear the freeze.

> [!IMPORTANT]
> Rollback is only possible while the freeze is in effect and at least one node is still on the previous version. Downgrading after calling unfreeze and completing the full cluster upgrade is not supported.

## [](#api-reference)API Reference

| Endpoint                                                                                                                                         | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [GET /\_cluster\_compat\_version](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/get%5F%5Fcluster%5Fcompat%5Fversion)                       | Returns the current cluster compatibility version, the version of each registered node, and the frozen value if a freeze is active.                                      |
| [POST /\_cluster\_compat\_version/freeze](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fcluster%5Fcompat%5Fversion%5Ffreeze)     | Pins the cluster compatibility version at its current value. The freeze persists across node restarts.                                                                   |
| [POST /\_cluster\_compat\_version/unfreeze](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fcluster%5Fcompat%5Fversion%5Funfreeze) | Clears the pinned version. The compatibility version resumes tracking the minimum across live nodes. Returns 503 if the unfreeze did not fully apply; retry the request. |

Required Sync Gateway RBAC role: Sync Gateway Dev Ops.

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