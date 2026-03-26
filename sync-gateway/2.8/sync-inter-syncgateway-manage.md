---
title: Manage Inter-Sync Gateway Replications
description: Managing inter-Sync Gateway replications
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/sync-inter-syncgateway-manage.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::sync-inter-syncgateway-manage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/sync-inter-syncgateway-manage.html)

# Manage Inter-Sync Gateway Replications

> Managing inter-Sync Gateway replications  

_Related inter-syncgateway topics_: [Overview](../current/sync/sync-inter-syncgateway-overview.md) | [Run](../current/sync/sync-inter-syncgateway-run.md) | Manage | [Monitor](../current/sync/sync-inter-syncgateway-monitor.md) | [Conflict](../current/sync/sync-inter-syncgateway-conflict-resolution.md)

_Other related topics_: [Configuration Properties](../current/configuration/configuration-properties-legacy.md) | [Admin REST API](../current/rest-api/rest-api-admin.md)

> [!CAUTION]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see [SG-Replicate](#sync-gateway::legacy-sg-replicate.adoc)

## [](#admin-capabilities)Admin capabilities

The Admin REST API provides two endpoints to assist in the monitoring, administration and management of replications. These enable users to examine, update, start and stop replications:

You can use the endpoints manually or by using automation (for example, scripts or a container orchestration system such as Kubernetes).

The available endpoints used for admin tasks are:

* `_replication` — Retrieve, Update or Remove a _replication definition_
* `_replicationStatus` — Stop, Start or Reset a replication

> [!TIP]
> BAD ADMONITION \[COMMUNITY EDITION\](https://www.couchbase.com/products/editions) Only Replications always run on the node on which they are configured. Users can only access replications on the node from which they make the request.

## [](#getting-replication-details)Getting Replication Details

You can view the current definition details of a replication. This includes replications configured in the `JSON` file and those initialized using the Admin REST API. You can do this for:

* Individual replications ([Example 1](#get-replication-definition))
* All replications defined for a specified database ([Example 2](#get-replication-definition-all))

Replication information is returned a JSON object.

Example 1\. Get a replication definition

* Request
* Response

```json
curl --location --request GET 'http://localhost:4985/db1-local/_replication/db1-rep-id1' \
--header 'Content-Type: application/json' \
```

```json
Success Response::
  Response Status 200 OK
  Payload in body
{
  "db1-rep-id1": {
    "replication_id": "db1-rep-id1",
    "remote": "http://user1:****@example.com:4984/db1-remote",
    "direction": "pull",
    "purge_on_removal": true,
    "continuous": true,
    "filter": "sync_gateway/bychannel",
    "query_params": {
      "channels": [
        "channel.user1"
      ]
    },
    "assigned_node": "1de4994d136b982e"
  }
}
```

The following example retrieves definitions for all replications on a specified database, regardless of the node on which it was configured. The results are returned in an array; one entry per replication.

Example 2\. Get all replication definitions (for a database)

* Request
* Response

```json
curl --location --request GET 'http://localhost:4985/db1-local/_replication' \
--header 'Content-Type: application/json' \
```

```json
Success Response::
  Response Status 200 OK
  Payload in body
{
  "db1-rep-id1": {
      "replication_id": "db1-rep-id1",
      "remote": "http://user1:****@example1.com:4984/db1-remote",
      "direction": "pushAndPull",
      "conflict_resolution_type": "remoteWins",
      "purge_on_removal": true,
      "enable_delta_sync": true,
      "initial_state": "stopped",
      "continuous": true,
      "filter": "sync_gateway/bychannel",
      "query_params": {
          "channels": [
              "channel.user1"
          ]
      },
      "batch_size": 1000,
      "assigned_node": "2c9b0d00a4e7c65a"
  },
  "db1-rep-id2": {
      "replication_id": "db1-rep-id2",
      "remote": "http://user1:****@example2.com:4984/db1-remote",
      "direction": "pushAndPull",
      "conflict_resolution_type": "remoteWins",
      "purge_on_removal": true,
      "enable_delta_sync": true,
      "max_backoff_time": 5,
      "initial_state": "running",
      "continuous": true,
      "filter": "sync_gateway/bychannel",
      "query_params": {
          "channels": [
              "channel.user1"
          ]
      },
      "adhoc": true,
      "batch_size": 1000,
      "assigned_node": "2c9b0d00a4e7c65a"
  }
}
```

## [](#updating-a-replication)Updating a Replication

You can update an existing replication's definition, whether configured or initialized by Admin Rest API, by providing the details you want to change in an API call ([Example 3](#update-replication-definition)). Changes will only be made to those parameters provided in the call.

If you change the remote URI it must be to a valid URI.

> [!TIP]
> How do I change an existing replication's definition details?
> 
> Send a `PUT` request to the `_replication` endpoint. Specify just the changed items in the JSON body.

Example 3\. Update a replication's details

* Request
* Response

```json
curl --location --request PUT 'http://localhost:4985/db1-local/_replication/db1-rep-id1 \
--header 'Content-Type: application/json' \
--data-raw '{
  "direction": "push",
  "purge_on_removal":false, // set back to default
  "remote": "http://user1:password1@example.com:4984/db1-remote",
  "filter":"sync_gateway/bychannel",
  "query_params": {
    "channels":["channel.user1"]
  },
  "continuous": false
  }'
```

A successful update will return a 200 response, with the following body:

```json
Success Response::
  Response Status 200 OK
  No payload
```

If the `replication_id` in the body does not match that quoted in the URI you will see a 400 response as below.

```json
Bad Request Response::
  Response Status 400 Bad request

{
    "error": "Bad Request",
    "reason": "Replication ID in body \"db1-rep-id1\" does not match request URI"
}
```

See: [Admin REST API](../current/rest-api/rest-api-admin.md) | Endpoint [PUT/{tkn-url}/{db}/\_replication/example-rep-db1](../current/rest-api/rest-api-admin.md#/replication/put%5F%5Fdb%5F%5F%5Freplication%5F%5FreplicationID%5F)

## [](#removing-a-replication)Removing a Replication

Removing a replication will delete:

* The persisted replication definition
* All [checkpoints![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#checkpoint) associated with the replication
* All replication status information associated with the replication

To find the replication\_id of an existing replication see [Getting Replication Status Data](#getting-replication-status-data).

_Action_: Send a `DELETE` request to the `replication` endpoint specifying the replication\_id to remove

Example 4\. Removing a replication

* Request
* Response

```json
curl --location --request DELETE 'http://localhost:4985/db2-local/_replication/db2-rep-id3' \
--header 'Content-Type: application/json' \
```

```json
Success Response::
  Response Status 200 OK
  No payload
```

See: [Admin REST API](../current/rest-api/rest-api-admin.md) | Endpoint [DELETE/{tkn-url}/{db}/\_replication/example-rep-db1](../current/rest-api/rest-api-admin.md#/replication/delete%5F%5Fdb%5F%5F%5Freplication%5F%5FreplicationID%5F)

## [](#getting-replication-status-data)Getting Replication Status Data

Sync Gateway provides easy access to replication status data through the Admin REST API.

You can obtain the replication status details for a specific replication, or for all replications across all nodes. This option can be useful, for example, to find any auto-generated replication\_id details needed to enable further replication management activities.

> [!TIP]
> BAD ADMONITION \[COMMUNITY EDITION\](https://www.couchbase.com/products/editions) Only Replications always run on the node on which they are configured. Users can only access replications on the node from which they make the request.

For more information on monitoring see: [Monitor Inter-Sync Gateway Replications](../current/sync/sync-inter-syncgateway-monitor.md)

Example 5\. For a Single Replication

This example targets a known `replication-id` and returns its status data.

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

Example 6\. For All Replications

This example targets all replications across all nodes. It filters the results using a query string — see: [Monitor Inter-Sync Gateway Replications](../current/sync/sync-inter-syncgateway-monitor.md) for more on using this option.

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

## [](#starting-a-replication)Starting a Replication

You can start a persistent or ad hoc replication not already in the running state. You need to specify the `replication_id`.

If the replication is resetting it cannot be started until the reset is complete.

_Action_: Send a `POST` request to the `_replicationStatus` endpoint with `action=start`

Example 7\. Start a replication

* Request
* Response

```json
curl --location --request PUT 'http://localhost:4985/db1-local/_replicationStatus/\{{db1-rep-id}}?action=start' \
--header 'Content-Type: application/json' \
```

```json
Success Response::
  Response Status 200 OK
  Payload in body
{
  "replication_id": "db1-rep-id1",
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
```

## [](#stopping-a-replication)Stopping a Replication

You can stop a persistent or ad hoc replication not already in the stopped state. You can use this, for example, to offline an edge cluster without waiting for a long replication to complete.

_Action_: Send a `POST` request to the `_replicationStatus` endpoint with `action=stop`

Example 8\. Stopping replications

* Request
* Response

```json
curl --location --request PUT 'http://localhost:4985/db1-local/_replicationStatus/\{{db1-rep-id1}}?action=stop' \
--header 'Content-Type: application/json' \
```

```json
Success Response::
  Response Status 200 OK
  Payload in body
{
  "replication_id": "db1-rep-id1",
  "docs_read": 0,
  "docs_written": 0,
  "doc_write_failures": 0,
  "doc_write_conflict": 0,
  "status": "stopped",
  "rejected_by_remote": 0,
  "rejected_by_local": 0
}
```

## [](#resetting-a-replication)Resetting a Replication

You can reset a persistent replication not in the running state. This can be useful to escape a system state where one or more documents have failed to sync but where resuming from previous synced [checkpoint![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#checkpoint) would skip over those documents. You need to specify the `replication_id`.

If the replication is resetting it cannot be started until the reset is complete. The replication must be stopped before it can be reset.

_Action_: Send a `POST` request to the `_replicationStatus` endpoint with `action=reset`

Example 9\. Reset a replication

* Request
* Response

```json
curl --location --request PUT 'http://localhost:4985/db1-local/_replicationStatus/\{{db1-rep-id2}}?action=reset' \
--header 'Content-Type: application/json' \
```

```json
Success Response::
  Response Status 200 OK
  Payload in body
{
  "replication_id": "db1-rep-id2",
  "docs_read": 0,
  "docs_written": 0,
  "doc_write_failures": 0,
  "doc_write_conflict": 0,
  "status": "stopped",
  "rejected_by_remote": 0,
  "rejected_by_local": 0
}
```

## [](#skipping-tls-certificate-verification)Skipping TLS Certificate Verification

> [!CAUTION]
> Development and Testing Option ONLY
> 
> This is an **unsupported** configuration option. It must not be used in a production environment. Its ongoing availability is not guaranteed.

The configuration setting. `database.this_db.unsupported.sgr_tls_skip_verify`, can be used to skip the validation of TLS certificates, simplifying development and testing — see: [Example 10](#using-sgr-tls-skip-verify) and the configuration item [unsupported.sgr\_tls\_skip\_verify](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-unsupported-sgr%5Ftls%5Fskip%5Fverify).

Example 10\. Using sgr\_tls\_skip\_verify

```json
{
  "databases": {
    "db1": {
      "server": "couchbase://localhost",
      "bucket": "db1",
      "username": "Administrator",
      "password": "password",
      "unsupported": {
        "sgr_tls_skip_verify": true
      },
      "replications": {
        "repl1": {
          "direction": "pushAndPull",
          "remote": "https://remotehost:4985/db1",
          "continuous": true
        }
      }
    }
  }
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