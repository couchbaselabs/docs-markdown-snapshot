---
title: SG Replicate
description: SG Replicate protocol supports inter-Sync Gateway replication
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/legacy-sg-replicate.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::legacy-sg-replicate.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/legacy-sg-replicate.html)

# SG Replicate

> SG Replicate protocol supports inter-Sync Gateway replication  
> This content is deprecated. It provides an introduction to, and overview of SG Replicate, which was replaced by a completely redesigned and rearchitected version in release 2.8.

Related _Inter-Sync Gateway Replication_ topics: [Configuration Properties](../current/configuration/configuration-properties-legacy.md) | [Admin REST API](../current/rest-api/rest-api-admin.md)

> [!CAUTION]
> Context Clarification
> 
> This content relates to inter-Sync Gateway replication in pre-2.8 versions of Sync Gateway, also known as SG Replicate. For documentation on inter-Sync Gateway replication in Sync Gateway 2.8+ see [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)

## [](#replicating-between-sync-gateway-clusters)Replicating between Sync Gateway Clusters

We support the ability to run replications between two Sync Gateway clusters. SG-Replicate is the protocol that supports that replication. Documents go through the Sync Function on the target Sync Gateway instance which ensures that access permissions are updated. On the architecture diagram below, any changes that users/systems make on either Sync Gateway instance will be replicated to the other Sync Gateway instance.

![running replications](_images/running-replications.png) 

> [!NOTE]
> A _Sync Gateway database_ can also be referred to as a namespace for documents, the data is **always** stored in Couchbase Server.

## [](#sg-replicate-vs-xdcr)SG Replicate vs XDCR

[XDCR](../../server/current/manage/manage-xdcr/xdcr-management-overview.md) (cross data centre replication) is the Couchbase Server API used to replicate between Couchbase Server clusters. Both XDCR and SG Replicate can be used to keep clusters in different data centres in sync. However, SG Replicate was designed specifically for a Couchbase Mobile deployment and it must be used for replication between mobile clusters.

## [](#features)Features

* Replicates via the Sync Gateway REST API
* JSON configuration to specify replications
* Supports multiple replications running concurrently
* Can run both OneShot and Continuous replications
* Does not store anything persistently
* Stateless — can be interrupted/restarted anytime without negative side effects
* Can specify which channel(s) to sync
* Supports Primary/Primary and Primary/Secondary topologies
* A warning message is logged whenever an SG Replicate replication is initialized (either through config or REST end point). The message emphasizes that this feature is deprecated.

## [](#limitations)Limitations

* Can only replicates SG databases that are hosted on recent versions of Sync Gateway (after commit 50d30eb3d on March 7, 2014)
* In deployments with multiple Sync Gateway nodes, only _one_ of the Sync Gateways should be configured for replications. If multiple Sync Gateways are configured for replications, it could substantially increase the amount of duplicate work, and therefore should be avoided. The limitation is that the system is not guaranteed to be Highly Available: if the Sync Gateway that is chosen to drive the replication goes down or is otherwise removed from the system, then the replications will stop.
* Replication between Sync Gateway databases doesn’t support automatic conflict resolution even when the no-conflicts mode is enabled (i.e ["allow\_conflicts": false](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-allow%5Fconflicts)). Apps will continue to rely on the 1.x REST APIs to asynchronously detect and resolve conflicts. The `allow_conflicts` property must be true in both source and target sync gateways. When running two Sync Gateway clusters with the no-conflicts mode enabled, cross-cluster document conflicts will result in that document no longer being replicated. Deployments must implement a custom conflict resolver in an external app as specified [here](sync-sgreplicate-resolving-conflicts-legacy.md). To avoid this, the application must ensure concurrent, cross-cluster updates are not made to a given document.
* Delta-sync is disabled
* Replication State is not configurable . It will default to running state.
* Purge-on-removal — document removals are ignored by target and not purged.
* No exponential backoff is available — replications will attempt to reconnect every 500 msec, indefinitely.
* TLS — there is no option to skip TLS certificate validation for self-signed certificates.

## [](#running-replications-via-the-rest-api)Running replications via the REST API

A replication is run by sending a POST request to the server endpoint `_replicate`, with a JSON object defining the replication parameters. Both one-shot and continuous replications can be run. Each replication is one-way between two local or remote Sync Gateway databases. Multiple replications can run simultaneously, supporting bi-directional replications and different replication topologies. Be aware that both databases being synchronized should have the same sync function, otherwise it could lead to unexpected behavior.

These parameters start a one-shot replication between two databases on the local Sync Gateway instance. The request will block until the replication has completed.

```javascript
{
    "source": "db",
    "target": "db-copy"
}
```

These parameters start a one-shot replication between one database on the local Sync Gateway instance and one on a remote Sync Gateway instance, with user credentials. The request will return immediately and the replication will run asynchronously.

```javascript
{
    "source": "db",
    "target": "http://user:password@example.com:4985/db-copy",
    "async":true
}
```

These parameters start a continuous replication between one database on the local Sync Gateway instance and one on a remote Sync Gateway instance with the user provided `replication_id`. The request will return immediately and the replication will run asynchronously.

```javascript
{
    "replication_id":"my-named-replication",
    "source": "db",
    "target": "http://user:password@example.com:4985/db-copy",
    "continuous":true
}
```

These parameters start a continuous replication between one database on the local Sync Gateway instance and one on a remote Sync Gateway instance. The replicator will batch up to 1000 revisions at a time, this will improve replication performance but will use more memory resources. Source database documents will be filtered so that only those tagged with the channel names "channel1" or "channel2" are replicated.

```javascript
{
    "source": "db",
    "target": "http://user:password@example.com:4985/db-copy",
    "continuous":true,
    "changes_feed_limit":1000,
    "filter":"sync_gateway/bychannel",
    "query_params":["channel1","channel2"]
}
```

## [](#configuration-properties)Configuration Properties

The `_replicate` JSON Object supports the following properties.

| Name                 | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | Default |
| -------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| source               | URL     | _Required._ A URL pointing to the source database for the replication, the URL may be relative i.e. just the name of a local database on the Sync Gateway instance. The URL may point to the Admin REST API which will replicate all documents in the DB, or it may point to the public REST API which will only copy documents in the users assigned channels. When specifying credentials, the URL must be of the form user:password@host. | none    |
| target               | URL     | _Required._ A URL pointing to the target database for the replication, the URL may be relative i.e. just the name of a local database on the Sync Gateway instance. The URL may point to the Admin REST API or it may point to the public REST API, this will impact the behavior of the target database sync function. When specifying credentials, the URL must be of the form user:password@host.                                         | none    |
| continuous           | Boolean | _Optional._ Indicates whether the replication should be a one-shot or continuous replication.                                                                                                                                                                                                                                                                                                                                                | false   |
| filter               | String  | _Optional._ Passes the name of filter to apply to the source documents, currently the only supported filter is "sync\_gateway/bychannel", this will replicate documents only from the set of named channels.                                                                                                                                                                                                                                 | none    |
| query\_params        | Object  | _Optional._ Passes parameters to the filter, for the "sync\_gateway/bychannel" filter the value should be an array or channel names (JSON strings).                                                                                                                                                                                                                                                                                          | none    |
| cancel               | Boolean | _Optional._ Indicates that a running replication task should be canceled, the running task is identified by passing its replication\_id or by passing the original source and target values.                                                                                                                                                                                                                                                 | false   |
| replication\_id      | String  | _Optional._ If the cancel parameter is true then this is the id of the active replication task to be canceled, otherwise this is the replication\_id to be used for the new replication. If no replication\_id is given for a new replication it will be assigned a random UUID.                                                                                                                                                             | false   |
| async                | Boolean | _Optional._ Indicates that a one-shot replication should be run asynchronously and the request should return immediately. Replication progress can be monitored by using the \_active\_tasks resource.                                                                                                                                                                                                                                       | false   |
| changes\_feed\_limit | Number  | _Optional._ The maximum number of change entries to pull in each loop of a continuous changes feed.                                                                                                                                                                                                                                                                                                                                          | 50      |

## [](#running-replication-on-startup)Running replication on startup

If you want to run replications as soon as Sync Gateway starts, you can define replications in the top level "replications" property of the Sync Gateway configuration, the "replications" value is an array of objects, each object defines a single replication, the object properties are the same as those for the `_replicate` end-point on the Admin REST API.

One-shot replications are always run asynchronously even if the `async` property is not set to true.

A One-shot replication that references a local database for either source or target, will be run after a short delay (5 seconds) in order to allow the local REST API’s to come up. Replications may be given a user defined `replication_id` otherwise Sync Gateway will generate a random UUID. Replications defined in config may not contain the `cancel` property.

```javascript
{
    "log":["*"],
    "replications":[
        {
            "source": "db",
            "target": "db-copy"
        },
        {
            "source": "db",
            "target": "http://user:password@example.com:4985/db-copy"
        },
        {
            "replication_id":"continuous-remote-local",
            "source": "http://user:password@example.com:4985/db-backup",
            "target": "db"
            "continuous":true
        },
        {
            "replication_id":"continuous-filtered",
            "source": "db",
            "target": "http://user:password@example.com:4985/db-copy"
            "continuous":true,
            "changes_feed_limit":1000,
            "filter":"sync_gateway/bychannel",
            "query_params":["channel1","channel2"]
        }
    ],
    "databases": {
        "db": {
            "server": "http://localhost:8091",
            "bucket": "db",
            "users": {
                "GUEST": {"disabled": false, "admin_channels": ["*"]}
            }
        },
        "db-copy": {
            "server": "http://localhost:8091",
            "bucket": "db-copy",
            "users": {
                "GUEST": {"disabled": false, "admin_channels": ["*"]}
            }
        }
    }
}
```

## [](#monitoring-replications)Monitoring replications

By default a simple one-shot replication blocks until it is complete and returns the stats for the completed task. Async one-shot and continuous replications return immediately with the in flight task stats.

You can get a list of active replication tasks by sending a GET request to the `_active_tasks` endpoint, this will return a list of all running one-shot and continuous replications for the current Sync Gateway instance.

The response is a JSON array of active task objects, each object contains the original request parameters for the replication, a unique `replication_id` and some stats for the replication instance. The list of returned stats and their meaning can be found on the API reference of the [\_active\_tasks](../current/rest-api/rest-api-admin.md#/server/get\%5F%5Factive%5Ftasks) endpoint.

```javascript
[
    {
        "type":"replication",
        "replication_id":"6a4924c24424b635a80f50cd660fb192",
        "continuous":true,
        "source":"http://example.com:4985/source",
        "target":"http://example.com:4985/target",
        "docs_read":0,
        "docs_written":0,
        "doc_write_failures":0,
        "end_last_seq":null
        "is_persistent": true,
        "status": "string",
        "last_seq_push": 0,
        "last_seq_pull": 0
    },
    {
        "type":"replication",
        "replication_id":"active-to-backup",
        "continuous":true,
        "source":"http://example2.com:4985/active",
        "target":"http://example2.com:4985/backup",
        "docs_read":1000,
        "docs_written":850,
        "doc_write_failures":10,
        "doc_write_failures": 0,
        "end_last_seq":25680
        "is_persistent": true,
        "status": "string",
        "last_seq_push": 0,
        "last_seq_pull": 0
    }
]
```

## [](#canceling-replications)Canceling replications

An active replication task is canceled by sending a POST request to the server endpoint `_replicate`, with a JSON object. The JSON object must contain the `cancel` property set to true and either a valid `replication_id` or the identical source, target and continuous values used to start the replication.

This will cancel an active replication with a `replication_id` of "my-one-shot-replication", the `replication_id` value can be obtained by sending a request to `_active_tasks`.

```javascript
{
    "cancel": true,
    "replication_id": "my-one-shot-replication"
}
```

This will cancel a replication that was started with same "source" and "target" values as those in the cancel request. By omitting the "continuous" property it’s value will default to **false**, a replication must also have been started as a one-shot to match.

```javascript
{
    "cancel":true,
    "source": "db",
    "target": "db-copy"
}
```

When an active task is canceled, the response returns the stats of the replication up to the point when it was stopped.

```javascript
{
    "type":"replication",
    "replication_id":"3791d562153505408e0b2730603ed7c1",
    "continuous":true,
    "source":"http://0.0.0.0:4985/source",
    "target":"http://0.0.0.0:4985/target",
    "docs_read":12,
    "docs_written":12,
    "doc_write_failures":0,
    "start_last_seq":0,
    "end_last_seq":"28"
}
```

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