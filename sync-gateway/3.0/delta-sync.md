---
title: Delta Sync
description: Use Sync Gateway's delta sync feature for secure, resilient, and
  efficient sync from cloud to edge
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/delta-sync.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::delta-sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/delta-sync.html)

# Delta Sync

> Use Sync Gateway’s delta sync feature for secure, resilient, and efficient sync from cloud to edge  
> This content introduces Sync Gateway’s delta sync feature; sync only the data that has changed.

Related _Sync_ topics: [Sync with Couchbase Lite](sync-using-app.md) | [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md) | [Delta Sync](#) | [Resync](resync.md)

## [](#overview)Overview

Delta Sync provides the ability to replicate only those parts of a Couchbase Mobile document that have changed. This can result in significant savings in bandwidth consumption as well as throughput improvements, especially useful where network bandwidth is constrained.

## [](#operation)Operation

Delta sync is disabled by default on Sync Gateway databases.

If delta sync is enabled on a Sync Gateway database (see: [Example 1](#sample-cfg)), then Couchbase Lite clients syncing with that database will switch to using delta sync automatically. It is also automatically enabled for peer-to-peer sync between Couchbase Lite clients. However, if delta sync is disabled on Sync Gateway then Couchbase Lite clients will operate in normal mode.

For inter-Sync Gateway Replication — You should note that delta sync does not apply to attachment contents and that it is disabled for Couchbase Lite database replicas.

Replication does not use Delta Sync when pushing to a pre-2.8 target.

## [](#configuration)Configuration

You can enable delta-sync on a per-database basic in your Sync Gateway configuration file using the `delta_sync` properties in [Database Configuration](rest-api-admin.md) — as shown in [Example 1](#sample-cfg):

Example 1\. Sample of Database with Delta Sync

```json
// ... other configuration properties as appropriate
{
  "databases": {
    "db": {
      "name": "dbname",
      "bucket": "default",
      "allow_conflicts": false,
      "revs_limit": 20,
      "delta_sync": { (1)
        "enabled": true,
        "rev_max_age_seconds": 86400
      }
      // ... any other configuration properties as appropriate
    }
  }
}
```

| **1** | [database\_schema.delta\_sync](configuration-schema-database.md#database-delta%5Fsync) — enable or disable delta sync property for this database; also allows you to tune the amount of additional Couchbase Server bucket storage used by delta sync — see: [Couchbase Server Bucket Storage Needs](#tuning). |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#tuning)Couchbase Server Bucket Storage Needs

Delta sync’s storage of backed-up revision bodies in the Couchbase Server bucket means additional Couchbase Server storage is required. This storage is used by Sync Gateway to generate the deltas between old and new revisions. — see [Example 2](#addl-storage).

> [!TIP]
> Calculate required storage using: `(doc_size * updates_per_day * 86400) / rev_max_age_seconds`

With each delta sync write operation the revision body is backed up in the bucket and retained for _rev\_max\_age\_seconds_ to calculate future revision deltas. So new deltas can only be generated for read requests arriving within the _rev\_max\_age\_seconds_ time window.

Setting `rev_max_age_seconds = 0` will generate deltas opportunistically on pull replications, with no additional storage requirements.

Example 2\. Additional storage calculation

Using:

* _rev\_max\_age\_seconds_ \= default value
* average document size = 4 KB
* writes/day = 100

Then enabling delta sync would take up an additional 400 KB of storage on Couchbase Server:  
`((4 * 100 * 86400)/86400)`

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