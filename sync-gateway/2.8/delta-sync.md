---
title: Delta Sync
description: Use Sync Gateway's delta sync feature for secure, resilient and
  efficient sync from cloud to edge
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/delta-sync.adoc
  xref: xref:2.8@sync-gateway::delta-sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/delta-sync.html)

# Delta Sync

> Use Sync Gateway's delta sync feature for secure, resilient and efficient sync from cloud to edge  
> This content introduces Sync Gateway's delta sync feature; sync only the data that has changed.

Related _Sync_ topics: [Sync with Couchbase Lite](../current/sync/sync-using-app.md) | [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md) | [Delta Sync](../current/sync/delta-sync.md) | [Resync](../current/manage/resync.md)

## [](#overview)Overview

Delta Sync provides the ability to replicate only those parts of a Couchbase Mobile document that have changed. This can result in significant savings in bandwidth consumption as well as throughput improvements, especially useful where network bandwidth is constrained.

## [](#operation)Operation

Delta sync is disabled by default on Sync Gateway databases.

If delta sync is enabled on a Sync Gateway database (see: [Example 1](#sample-cfg)), then Couchbase Lite clients syncing with that database will switch to using delta sync automatically. It is also automatically enabled for peer-to-peer sync between Couchbase Lite clients. However, if delta sync is disabled on Sync Gateway then Couchbase Lie clients will operate in normal mode.

You should note that delta sync does not apply to attachment contents and that it is disabled for Couchbase Lite database replicas.

> [!NOTE]
> Push replications do not use Delta Sync when pushing to a pre-2.8 target.

## [](#configuration)Configuration

You can enable delta-sync on a per-database basic in your Sync Gateway configuration file using the [this\_db.delta\_sync](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-delta%5Fsync) properties — as shown in [Example 1](#sample-cfg):

Example 1\. Sample of Database with Delta Sync

```json
// ... other configuration properties as appropriate
{
  "logging": {
    "console": {
      "log_keys": ["*"]
    }
  },
  "databases": {
    "db": {
      "server": "http://localhost:8091",
      "bucket": "default",
      "users": { "GUEST": { "disabled": false, "admin_channels": ["*"] } },
      "allow_conflicts": false,
      "revs_limit": 20,
      "delta_sync": {
        "enabled": true, (1)
        "rev_max_age_seconds": 86400 (2)
      }
      // ... any other configuration properties as appropriate
    }
  }
}
```

| **1** | [this\_db.delta\_sync.enabled](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-delta%5Fsync-enabled) — enabled or disables delta sync for this database                                                                                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [this\_db.delta\_sync.rev\_max\_age\_seconds](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) — allows you to tune the amount of additional Couchbase Server bucket storage used by delta sync — see: [Couchbase Server Bucket Storage Needs](#tuning). |

## [](#tuning)Couchbase Server Bucket Storage Needs

Delta sync's storage of backed up revision bodies in the Couchbase Server bucket means additional Couchbase Server storage is required — see [Example 2](#addl-storage).

> [!TIP]
> Calculate required storage using: `doc_size * updates_per_day * 86400) / rev_max_age_seconds`

With each delta sync write operation the revision body is backed up in the bucket and retained for _rev\_max\_age\_seconds_ to calculate future revision deltas. So new deltas can only be generated for read requests arriving within the _rev\_max\_age\_seconds_ time window.

Setting `rev_max_age_seconds = 0` will generate deltas opportunistically on pull replications, with no additional storage requirements.

Example 2\. Additional storage calulation

Using:

* _rev\_max\_age\_seconds_ \= default value
* average document size = 4 KB
* writes/day = 100

Then enabling delta sync would take up an additional 400 KB of storage on Couchbase Server:  
`((4 * 100 * 86400)/86400)`

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