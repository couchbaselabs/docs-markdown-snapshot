---
title: Manage Backup Service Threads
description: You can change the number of threads a Backup Service node uses
  when backing up data.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/backup-node-threads.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:rest-api:backup-node-threads.adoc[]
---

[View original HTML](/server/7.6/rest-api/backup-node-threads.html)

# Manage Backup Service Threads

> You can change the number of threads a Backup Service node uses when backing up data. 

## [](#http-methods-and-uris)HTTP Methods and URIs

Get all overrides to the thread Backup Service settings

```uri
GET /api/v1/nodesThreadsMap
```

Overwrite all thread settings with new values

```uri
POST /api/v1/nodesThreadsMap
```

Update some thread settings

```uri
PATCH /api/v1/nodesThreadsMap
```

## [](#description)Description

The `nodesThreadMap` endpoint lets you change the number of threads the Backup Service uses on a node. The default number of threads the Backup Service uses is based on the number of CPU cores in the node: \\(\\max(1, cpu\\\_cores \\times 0.75)\\). The number of threads also sets the number of concurrent client connections the service uses to retrieve data from nodes in the cluster. Each thread creates one connection. See [Thread Usage](../learn/services-and-indexes/services/backup-service.md#threads) for more information about how the number of threads affects the Backup Service.

## [](#curl-syntax)Curl Syntax

Get the current thread overrides

```console
curl -u $USER:$PASSWORD -X GET \
     http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/api/v1/nodesThreads
```

Overwrite all thread settings

```console
 curl -u Administrator:password -X POST \
      http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/api/v1/nodesThreadsMap \
      -d <nodes_thread_map>
```

Update/set some thread settings

```console
 curl -u Administrator:password -X PATCH \
      http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/api/v1/nodesThreadsMap \
      -d <nodes_thread_map>
```

__Table 1\. POST Parameters__
| Name               | Description                                                                                                                                                                                                                                                                                                                              | Schema                                             |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| nodes\_thread\_map | An object that sets the number of threads for Backup Service nodes. When you use the PATCH method, the changes only apply to the nodes in the map. Any existing settings that are not in the map remain in effect. Calling POST, removes any existing overrides. After the call, only the overrides you supply in the map are in effect. | [Node Threads Map](#nodes%5Fthread%5Fmap%5Fschema) |

Node Thread Map Schema

```json
{"nodes_threads_map": {
    <backup_node_uuid>:<threads>, . . .
    }
}
```

| Name               | Description                                                                                                                                                                                                        | Schema  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| backup\_node\_uuid | The unique identifier for a node running the Backup Service. You can get this value from the /pools/nodes REST API. See [Getting Information on Nodes](rest-node-get-info.md).                                     | string  |
| threads            | The number of threads for the Backup Service to use. When set to 0, the Backup Service uses the default number of threads based on the number of CPU cores in the node: \\(\\max(1, cpu\\\_cores \\times 0.75)\\). | integer |

## [](#responses)Responses

| Value         | Description                                                                                                                                                                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200 OK        | Successful calls to POST and PATCH just return the response code. When calling the GET method, you receive a JSON object mapping the node UUIDs to thread values. See [Examples](#examples) for details.                                                                           |
| 403 Forbidden | User does not have the proper permission to call the API endpoint. In addition, the call returns a JSON object similar to the following: {   "message": "Forbidden. User needs one of the following permissions",   "permissions": \[     "ro\_admin"   \] }                       |
| 404 Not Found | The resource was not found. If you call the GET method before you have created a nodes threads map by calling POST or PATCH, you also receive the following JSON message: {     "status":404,     "msg":"Could not find the Nodes Threads Map",     "extras":"element not found" } |

## [](#required-permissions)Required Permissions

* `GET`: Full Admin, Backup Full Admin, Read-Only Admin
* `POST` and `PATCH`: Full Admin, Backup Full Admin

## [](#examples)Examples

Set a backup service node to use a single thread, overwriting any existing overrides

```console
curl -s -u Administrator:password -X \
     POST http://localhost:8097/api/v1/nodesThreadsMap \
     -d '{"nodes_threads_map":{"cb5c77719df4f33131251afdca00531a":1}}'
```

Get the thread settings

```console
curl -s -u Administrator:password -X \
     GET http://node3:8097/api/v1/nodesThreadsMap | jq
```

The previous example returns output similar to the following:

```json
{
  "cb5c77719df4f33131251afdca00531a": 1
}
```

## [](#see-also)See Also

* For a an overview of the Backup Service, see [Backup Service](../learn/services-and-indexes/services/backup-service.md).
* For a step-by-step guide to configure and use the Backup Service using the Couchbase Server Web Console, see [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).
* See [Thread Usage](../learn/services-and-indexes/services/backup-service.md#threads) for more information about how the number of threads affects the Backup Service.