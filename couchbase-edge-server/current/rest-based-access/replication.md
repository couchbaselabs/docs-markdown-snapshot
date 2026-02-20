---
title: Manage Replication with Edge Server
description: The replicate endpoint enables you to synchronize Edge Server with
  another server, for example Sync Gateway or Couchbase Capella App Services.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/rest-based-access/pages/replication.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-edge-server:rest-based-access:replication.adoc[]
---

[View original HTML](/couchbase-edge-server/current/rest-based-access/replication.html)

# Manage Replication with Edge Server

> The replicate endpoint enables you to synchronize Edge Server with another server, for example Sync Gateway or Couchbase Capella App Services. 

## [](#prerequisites)Prerequisites

To set up replication, you must first configure Sync Gateway, Couchbase Capella App Services, or another Edge Server installation, to allow Edge Server to connect.

For example, to replicate with a Couchbase Capella database:

* You must have created an App Service connected to the Couchbase Capella database you want to replicate.
* You must have created an App Endpoint connected to the App Service, with access to the collections you want to replicate.
* The App Endpoint must be active.
* You must have set up a username, password, and authentication providers to enable Edge Server to connect to the App Endpoint.
* You must have allowed IP access from the address that the Edge Server client will use.
* You must have copied the public connection URL for the App Endpoint.

For more information, see [Sync](../sync/sync-landing.md).

## [](#start-replication-automatically)Start Replication Automatically

You can configure Edge Server so that replication starts automatically when Edge Server starts. This is usually used for continuous replication.

To configure automatic replication, use the top-level [replications](../configuration/edge-server-configuration.md#replications) property in the configuration file. This property is an array of objects, each of which has the following properties.

| Name                       | Description                                                                                                                                                                                                                                                                                                | Schema                 |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **source** _required_      | The source database. \[[1](#fn-1)\]                                                                                                                                                                                                                                                                        | string                 |
| **target** _required_      | The destination database. \[[1](#fn-1)\]                                                                                                                                                                                                                                                                   | string                 |
| **bidirectional**          | Set to true for bidirectional push/pull replication.                                                                                                                                                                                                                                                       | boolean                |
| **continuous**             | Set to true for continuous replication.                                                                                                                                                                                                                                                                    | boolean                |
| **collections** _optional_ | Specifies collections to replicate. If not given, only the default collection is replicated. \[[2](#fn-2)\] If it’s an array, each item must be a collection name. If it’s an object, the keys must be collection names and the values objects; each value may have its own channels and/or doc\_ids keys. | array / object         |
| **channels**               | Channel filter, an array of Sync Gateway channel names. (Only if collections is missing.) \[[2](#fn-2)\]                                                                                                                                                                                                   | array                  |
| **doc\_ids**               | An array of document IDs to be replicated. (Only if collections is missing.) \[[2](#fn-2)\]                                                                                                                                                                                                                | array                  |
| **headers**                | Extra HTTP headers; keys are header names, values are header values. \[[2](#fn-2)\]                                                                                                                                                                                                                        | array                  |
| **trusted\_root\_certs**   | The name of a file in PEM format containing one or more trusted root certificates. Use this if the remote server’s certificate is signed by a nonstandard certificate authority.                                                                                                                           | string                 |
| **pinned\_cert**           | The name of a file in PEM format containing a copy of the remote server’s certificate. This certificate will be trusted, and will be the _only_ certificate allowed. This option is useful if the server uses a self-signed certificate.                                                                   | string                 |
| **auth**                   | Authorization credentials.                                                                                                                                                                                                                                                                                 | [Authorization](#auth) |
| **proxy**                  | HTTP proxy settings. \[[2](#fn-2)\]                                                                                                                                                                                                                                                                        | object                 |

**Authorization**

| Name                       | Description                                                                             | Schema |
| -------------------------- | --------------------------------------------------------------------------------------- | ------ |
| **user**                   | Username for HTTP Basic auth to remote server.                                          | string |
| **password**               | Password for HTTP Basic auth to remote server.                                          | string |
| **session\_cookie**        | A Sync Gateway session cookie for authentication.                                       | string |
| **openid\_token**          | An OpenID Connect token for authentication.                                             | string |
| **tls\_client\_cert**      | This Edge Server’s TLS client certificate, for mTLS. (Requires tls\_client\_cert\_key.) | string |
| **tls\_client\_cert\_key** | Private key of TLS client certificate. (Requires tls\_client\_cert.)                    | string |

1. One of `source` or `target` must be a local database name; the other must be a remote `ws:` or `wss:` sync URL.
2. For more details, see [Edge Server Configuration Schema](../configuration/edge-server-configuration.md).

## [](#start-replication-with-the-rest-api)Start Replication with the REST API

Alternatively, you can start replication using the REST API. You don’t need to set up reduplication in the configuration file to do this. Instead, you pass the replication options in the JSON request body.

The JSON request body uses the same format as the items in the [replications](../configuration/edge-server-configuration.md#replications) array in the configuration file. The only difference is that `trusted_root_certs` and `pinned_cert` should contain the certificate data in string form, not filenames.

To start replication with the REST API:

1. Make a POST call to the `_replicate` endpoint.
2. In the JSON request body, set the `source`, `target`, and any other replication options as required. For full details of the replication options, see the REST API Reference.

Replication is asynchronous. The response is returned immediately, as soon as the replication is queued.

## [](#monitor-status)Monitor Status

To get the status of all active replications, changes feeds, and sync tasks, make a GET call to the `_active_tasks` endpoint. This returns a JSON array, with one item for each replication, changes feed, or sync task. Each item is an object giving information about the active task.

To get the status of all replications, make a GET call to the `_replicate` endpoint.

To get the status of a particular replication, make a GET call to the `_replicate` endpoint with a path parameter whose value is the replication’s task ID.

## [](#stop-replication)Stop Replication

To stop a replication, make a DELETE call to the `_replicate` endpoint with a path parameter whose value is the replication’s task ID.

## [](#examples)Examples

In the command line examples:

* `$USER` and `$PASSWORD` are the credentials for Couchbase Edge Server.
* `$CERT` is the name and path to a TLS certificate file, for example `cert.cer`.
* `$HOST` and `$PORT` are the host and port to connect to Couchbase Edge Server, for example `localhost:59840`.

Note that the following cURL examples use a self-signed TLS server certificate. In production, you are strongly recommended to use a TLS certificate generated by a well-known authority.

### [](#ex-start-replication)Start Replication

The following request starts replication between a Capella App Endpoint and the local `travel-sample` database.

HTTP Request

```sh
curl --cacert $CERT --user $USER:$PASSWORD \
  "https://$HOST:$PORT/_replicate" --json '{
  "source": "wss://<redacted>:4984/travel-sample",
  "target": "travel-sample",
  "bidirectional": true, (1)
  "continuous": true,
  "collections": {
    "inventory.airport": {
      "channels": [
        "airport" (2)
      ]
    }
  },
  "auth": {
    "user": "demo@example.com", (3)
    "password": "Password!1"
  }
}'
```

| **1** | Replication is bidrectional and continuous.                                          |
| ----- | ------------------------------------------------------------------------------------ |
| **2** | Only the airport collection is replicated.                                           |
| **3** | The user and password match the authentication that was set up for the App Endpoint. |

A successful response has a `202` (Accepted) status and a JSON body containing a `session_id` property, whose value is an integer identifying this replication task. An error status will only be returned if the parameters are invalid.

### [](#ex-active-tasks)List All Active Tasks

The following request lists all active replications, changes feeds, and sync tasks.

HTTP Request

```sh
curl --cacert $CERT --user $USER:$PASSWORD \
  "https://$HOST:$PORT/_active_tasks"
```

### [](#ex-monitor-replications)List All Replications

The following request gets the status of all replications.

HTTP Request

```sh
curl --cacert $CERT --user $USER:$PASSWORD \
  "https://$HOST:$PORT/_replicate"
```

### [](#ex-monitor-replication)Monitor Replication

The following request gets the status of the specified replication task.

HTTP Request

```sh
curl --cacert $CERT --user $USER:$PASSWORD \
  "https://$HOST:$PORT/_replicate/1234"
```

### [](#ex-stop-replication)Stop Replication

The following request stops the specified replication task.

HTTP Request

```sh
curl -XDELETE --cacert $CERT --user $USER:$PASSWORD \
  "https://$HOST:$PORT/_replicate/1234"
```

## [](#see-also)See Also

* [Edge Server REST API](rest-api-landing.md)
* [Get Started with the Edge Server REST API](rest-api-start.md)
* [Database Operations with Edge Server](database-operations.md)
* [Document Access with Edge Server](document-access.md)
* [Monitor Changes with Edge Server](changes-feed.md)
* [Run Queries with Edge Server](queries-api.md)
* [Edge Server Public REST API](../public-api-reference/index.md)