---
title: Replication Monitoring and Statistics
description: Monitoring inter-Sync Gateway replications
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/sync/pages/sync-inter-syncgateway-monitor.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/sync/sync-inter-syncgateway-monitor.html)

# Replication Monitoring and Statistics

> Monitoring inter-Sync Gateway replications  
> This content covers the retrieval of status and statistical data relating to replication.

_Related topics_: [Overview](sync-inter-syncgateway-overview.md) | [Run](sync-inter-syncgateway-run.md) | [Manage](sync-inter-syncgateway-manage.md) | [Monitor](sync-inter-syncgateway-monitor.md) | [Conflict](sync-inter-syncgateway-conflict-resolution.md)

_Other Topics_: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) | [Admin REST API](../rest-api/rest-api-admin.md)

> [!IMPORTANT]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see the documentation for the appropriate release.

## [](#overview)Overview

### [](#status-information)Status Information

Sync Gateway provides a replication status Admin REST API endpoint to enable effective monitoring of replications.

Use the [/{db}/\_replicationStatus/{replicationid}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication/operation/get%5Fdb-%5FreplicationStatus-replicationid) endpoint to check the status of individual replications and-or the [/{db}/\_replicationStatus/{replicationid}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication/operation/get%5Fdb-%5FreplicationStatus-replicationid) endpoint to get status information on all replications, filtered by the querystring criteria.

### [](#sync-gateway-statistics)Sync Gateway Statistics

Sync Gateway maintains a comprehensive set of statistics, including a replication-specific subset.

You can access these statistics using the `_expvar` endpoint.

## [](#retrieving-replication-status-data)Retrieving Replication Status Data

Sync Gateway provides easy access to replication status data through the Admin REST API.

You can obtain the replication status details for a specific replication, or for all replications across all nodes. This option can be useful, for example, to find any auto-generated replication\_id details needed to enable further replication management activities.

> [!TIP]
> BAD ADMONITION \[COMMUNITY EDITION\](https://www.couchbase.com/products/editions) Only Replications always run on the node on which they are configured. Users can only access replications on the node from which they make the request.

### [](#retrieving-status-data-for-a-specific-replication)Retrieving Status Data for a Specific Replication

Use the Admin REST API endpoint `replicationStatus` to easily access replication status data for a specific replication id. Status data is returned regardless of the node the replication is running (or ran) on.

_Action_: Send a `GET` request to the `_replicationStatus` endpoint with the required `replication_id`

Example 1\. Get status data for a specified replication

This example returns status information for replication id 'db1-rep-id2'.

* Request
* Response

```json
curl --location --request GET 'http://localhost:4985/db1/_replicationStatus/db1-rep-id2' \
--header 'Content-Type: application/json' \
```

```json
[
  {
    "replication_id": "db1-rep-id2",
    "docs_read": 0,
    "docs_written": 10,
    "doc_write_failures": 0,
    "doc_write_conflict": 0,
    "status": "running",
    "rejected_by_remote": 0,
    "rejected_by_local": 0,
    "last_seq_pull": "8851",
    "last_seq_push": "10402"
}
]
```

### [](#retrieving-status-data-for-all-replications)Retrieving Status Data for All Replications

Use the Admin REST API’s `_replicationStatus` endpoint to access replication status data for all replications run, or running, on any node within the cluster. The JSON response comprises an array of results, one per replication.

You can easily filter the results using the query string: `` ?activeOnly=false&includeConfig=true&localOnly=false&includeError=true` ``

Available query string filters comprise:

* activeOnly - return only active replications (default=false)
* localOnly - return replications from the local node only (default=false)
* includeError - return replications even if their status is "error" (default=true)
* includeConfig - return the replication definition details (configuration) as well as the status data. This will include remote configuration definitions if `localOnly=false` (default=false)

_Action_: Send a `GET` request to the `_replicationStatus` endpoint with an optional query string

Example 2\. Get status data for all replications meeting criteria

This example retrieves status data, from across all nodes, for all replications that meet the specified criteria. The results are returned in an array; one entry per replication.

* Request
* Response

```json
curl --location --request GET "http://localhost:4985/db1-local/_replicationStatus?activeOnly=false&includeConfig=true&localOnly=false&includeError=true" \ (1)
--header 'Content-Type: application/json' \
```

| **1** | This example’s criteria selects replications with any status (including errors), on local and remote nodes. The returned status details also include replication definition details. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

```json
[
  {
    "replication_id": "db1-rep-id1-pull",
    "docs_read": 0,
    "docs_written": 0,
    "doc_write_failures": 0,
    "doc_write_conflict": 0,
    "status": "running",
    "rejected_by_remote": 0,
    "rejected_by_local": 0,
    "config": { (1)
        "replication_id": "db1-rep-id1-pull",
        "cancel": true,
        "direction": "pull",
        "purge-on-removal": true,
        "remote": "http://user:****@example.com:4985/db1-remote",
        "filter":"sync_gateway/bychannel",
        "query_params": {
          "channels": ["channel1.user1"]
        },
        "continuous": true
    }
  },
  {
    "replication_id": "db1-rep-id2",
    "docs_read": 0,
    "docs_written": 0,
    "doc_write_failures": 0,
    "doc_write_conflict": 0,
    "status": "stopped",  (2)
    "rejected_by_remote": 0,
    "rejected_by_local": 0,
    "config": {
        "replication_id": "db1-rep-id2",
        "direction": "pull",
        "remote": "http://user:****@example.com:4985/db1-remote",
        "continuous": true
      }
  },
  {
    "replication_id": "db2-rep-id1",
    "docs_read": 0,
    "docs_written": 0,
    "doc_write_failures": 0,
    "doc_write_conflict": 0,
    "status": "error", (3)
    "rejected_by_remote": 0,
    "rejected_by_local": 0,
    "config": {
      "replication_id": "db2-rep-id1",
      "direction": "pull",
      "remote": "http://user:****@example2.com:4985/db2-remote",
      "continuous": true
    }
  }
]
```

| **1** | The configuration details included because includeConfig=true |
| ----- | ------------------------------------------------------------- |
| **2** | "Stopped" replications included because activeOnly=false      |
| **3** | "error" replications included because includeError=true       |

## [](#retrieving-sync-gateway-statistics)Retrieving Sync Gateway Statistics

Sync Gateway maintains a comprehensive set of metrics covering performance and resource utilization.

The statistics schema includes replication metrics collected on a per-replication basis. These can be especially useful in monitoring the health of Sync Gateway nodes. An increasingly important activity as deployments scale to support cloud-to-edge use cases.

Access to this data is provided through the Admin REST API endpoint `/_expvar`.

See: [Monitor](../manage/stats-monitoring.md) for a full description of the available metrics.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](sync-with-couchbase-server.md)

###### [](#-3)

Reference material …​

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)
* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Conflict Related Blogs

* [Automatic Conflict Resolution](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)
* [Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/)
* [Conflict Resolution (category)](https://blog.couchbase.com/tag/conflict-resolution/)