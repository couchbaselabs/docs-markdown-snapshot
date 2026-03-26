---
title: Replication Monitoring and Statistics
description: Monitoring inter-Sync Gateway replications
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/sync-inter-syncgateway-monitor.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::sync-inter-syncgateway-monitor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/sync-inter-syncgateway-monitor.html)

# Replication Monitoring and Statistics

> Monitoring inter-Sync Gateway replications  
> This content covers the retrieval of status and statistical data relating to replication.

_Related inter-syncgateway topics_: [Overview](../current/sync/sync-inter-syncgateway-overview.md) | [Run](../current/sync/sync-inter-syncgateway-run.md) | [Manage](../current/sync/sync-inter-syncgateway-manage.md) | Monitor | [Conflict](../current/sync/sync-inter-syncgateway-conflict-resolution.md)

_Other related topics_: [Configuration Properties](../current/configuration/configuration-properties-legacy.md) | [Admin REST API](../current/rest-api/rest-api-admin.md)

> [!CAUTION]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see [SG-Replicate](#sync-gateway::legacy-sg-replicate.adoc)

## [](#overview)Overview

### [](#status-information)Status Information

Sync Gateway provides a replication status Admin REST API endpoint to enable effective monitoring of replications.

Use the [\_replicationStatus(replicationID)](../current/rest-api/rest-api-admin.md#/replication/get%5F%5Fdb%5F%5F%5FreplicationStatus%5F%5FreplicationID%5F) endpoint to check the status of individual replications and-or the [\_replicationStatus](../current/rest-api/rest-api-admin.md#/replication/get%5F%5Fdb%5F%5F%5FreplicationStatus%5F%5FqueryString%5F) endpoint to get status information on all replications, filtered by the querystring criteria.

### [](#sync-gateway-statistics)Sync Gateway Statistics

Sync Gateway maintains a comprehensive set of statistics, including a replication-specific subset.

You can access these statistics using the `_expvars` endpoint.

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

Use the Admin REST API's `_replicationStatus` endpoint to access replication status data for all replications run, or running, on any node within the cluster. The JSON response comprises an array of results, one per replication.

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

| **1** | This example's criteria selects replications with any status (including errors), on local and remote nodes. The returned status details also include replication definition details. |
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

Access to this data is provided through the Admin REST API endpoint `/_expvars`.

See: [Monitor](../current/manage/stats-monitoring.md) for a full description of the available metrics.

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)
* [SG-Replicate](#sync-gateway::legacy-sg-replicate.adoc)
* [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md)

###### [](#-2)

Reference material …​

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)
* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Conflict Related Blogs

* [Automatic Conflict Resolution](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)
* [Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/)
* [Conflict Resolution (category)](https://blog.couchbase.com/tag/conflict-resolution/)