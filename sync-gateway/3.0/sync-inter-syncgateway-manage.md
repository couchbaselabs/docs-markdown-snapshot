---
title: Manage Inter-Sync Gateway Replications
description: Managing inter-Sync Gateway replications
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/sync-inter-syncgateway-manage.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@sync-gateway::sync-inter-syncgateway-manage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/sync-inter-syncgateway-manage.html)

# Manage Inter-Sync Gateway Replications

> Managing inter-Sync Gateway replications  

_Related topics_: [Overview](sync-inter-syncgateway-overview.md) | [Run](sync-inter-syncgateway-run.md) | Manage | [Monitor](sync-inter-syncgateway-monitor.md) | [Conflict](sync-inter-syncgateway-conflict-resolution.md)

_Other Topics_: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md) | [Admin REST API](rest-api-admin.md)

> [!IMPORTANT]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see the documentation for the appropriate release.

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

You can update an existing replication's definition, whether configured or initialized by Admin REST API, by providing the details you want to change in an API call ([Example 3](#update-replication-definition)). Changes will only be made to those parameters provided in the call.

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

See: [Admin REST API](rest-api-admin.md) | Endpoint [PUT/{url}/{db}/\_replication/example-rep-db1](rest-api-admin.md#/replication/put%5F%5Fdb%5F%5F%5Freplication%5F%5FreplicationID%5F)

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

See: [Admin REST API](rest-api-admin.md) | Endpoint [DELETE/{url}/{db}/\_replication/example-rep-db1](rest-api-admin.md#/replication/delete%5F%5Fdb%5F%5F%5Freplication%5F%5FreplicationID%5F)

## [](#getting-replication-status-data)Getting Replication Status Data

Sync Gateway provides easy access to replication status data through the Admin REST API.

You can obtain the replication status details for a specific replication, or for all replications across all nodes. This option can be useful, for example, to find any auto-generated replication\_id details needed to enable further replication management activities.

> [!TIP]
> BAD ADMONITION \[COMMUNITY EDITION\](https://www.couchbase.com/products/editions) Only Replications always run on the node on which they are configured. Users can only access replications on the node from which they make the request.

For more information on monitoring see: [Inter Sync Gateway Sync - Monitor](sync-inter-syncgateway-monitor.md)

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

This example targets all replications across all nodes. It filters the results using a query string — see: [Inter Sync Gateway Sync - Monitor](sync-inter-syncgateway-monitor.md) for more on using this option.

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

The configuration setting. `database.this_db.unsupported.sgr_tls_skip_verify`, can be used to skip the validation of TLS certificates, simplifying development and testing — see: [Example 10](#using-sgr-tls-skip-verify) and the configuration item [unsupported.sgr\_tls\_skip\_verify](configuration-schema-database.md#database-unsupported-sgr%5Ftls%5Fskip%5Fverify).

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

## [](#handling-channel-access-revocation)Handling Channel Access Revocation

Users may lose access to channels for many reasons, including:

* The User loses direct access to channel
* The User is removed from a role
* A role the user belongs to is revoked access to channel

By default, documents are **not** auto purged on the active sync gateway even if the user on the passive sync gateway loses channel access.

Note: that _users_ are cluster-specific; _userA_ in custer A is not the same entity as _userA_ in cluster B.

If required, you can override this behavior using the configurable option (`enable_auto_purge-true`).

> [!NOTE]
> The behavior of the config flag is the **reverse** of what is done on Couchbase Lite.

Using this option auto-purges documents on the active Sync Gateway that are no longer accessible, unless a document belongs to another of replicating user's channels. This applies even if they are not actively replicating that channel.

> [!TIP]
> When `enable_auto_purge-true=true`, documents in revoked user channels are auto purged from Sync Gateway.

This is consistent with _Sync Gateway_'s handling of document access revocation using the `purge-on-removal` option

### [](#access-reassignment)Access Reassignment

Where a user loses access to a channel and is then reassigned access to a channel, any previously auto-purged documents still assigned to any of the user's channels are automatically pulled down by the active Sync Gateway.

> [!NOTE]
> This will not impact active nodes that have turned off auto-purge behavior. Auto-purged documents removed from a user's channels subsequent to the purge will not be synced again.

If you want to control whether to sync previous auto purged versions of the document and do not want to pull down purged documents, you must remove the documents from all of the users channels to ensure they are not synced down again.

### [](#pull-only-replication)Pull-only Replication

The expected impact of the enablement of auto purge behavior when

Scenario

The replicating user of a pull-only replication is revoked channel access.  
ISGR is configured to run as admin user on active peer

In ISGR, by default, access control policies are only enforced at remote cluster. The `_sync` function on an active node is by default run in context of admin user and as such there is no enforcement of access policies on the active side.

| System State                                        | Impact on Sync                 |                                                      |
| --------------------------------------------------- | ------------------------------ | ---------------------------------------------------- |
| Active Sync Gateway (Local) (Running as admin user) | Passive Sync Gateway (Remote)  | Expected behavior when enable\_auto\_purge is TRUE   |
| N/A                                                 | User revoked access to channel | Previously synced documents are auto purged on local |

Scenario

The replicating user of a pull-only replication is revoked channel access.

ISGR is configured to run as a non-admin user on active peer.

> [!NOTE]
> Depends on availability of a new feature (3.0) wherein the active peer is also running as the replicating user.

| System State                                                                     | Impact on Sync                                                       |                                                                                                                                                |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Sync Gateway (Local) (Running as non-admin user user1)                    | Passive Sync Gateway (Remote)                                        | Expected behavior when enable\_auto\_purge is TRUE                                                                                             |
| User1 revoked access to channel                                                  | User2 revoked access to channel                                      | Previously synced documents for User2 are auto purged on local                                                                                 |
| User1 revoked access to channel Sync Function includes requireAccess ("channel") | User2 still has access to channel                                    | Config option has no impact. Previously synced documents for User2 remain on local Subsequent remote changes synced down are rejected by local |
| User still has access to channel                                                 | User revoked access to channel Sync Function access policy is a Noop | Previously synced documents are auto purged on local                                                                                           |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](sync-with-couchbase-server.md)

###### [](#-3)

Reference material …​

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)
* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Conflict Related Blogs

* [Automatic Conflict Resolution](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)
* [Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/)
* [Conflict Resolution (category)](https://blog.couchbase.com/tag/conflict-resolution/)