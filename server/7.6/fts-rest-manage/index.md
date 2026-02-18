---
title: Search Manager Options REST API
description: The Search Manager Options REST API is provided by the Search
  Service. This API enables you to set cluster-level Search settings; in
  particular, to configure rebalance based on file transfer.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/fts-rest-manage/pages/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/fts-rest-manage/index.html)

# Search Manager Options REST API

## [](#overview)Overview

The Search Manager Options REST API is provided by the Search service. This API enables you to set Search manager options; in particular, to configure rebalance based on file transfer.

### Version information

**Version:** 7.6

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                              |
| ---------- | ---------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                     |
| **host**   | The host name or IP address of a node running the Search Service. **Example:** localhost |
| **port**   | The Search Service REST port. Use 18094 for secure access. **Values:** 8094, 18094       |

### Examples on this page

In the HTTP request examples:

* `$HOST` is the host name or IP address of a node running the Search Service.
* `$USER` is the user name of an authorized user — see [Security](#security).
* `$PASSWORD` is the password to connect to Couchbase Server.

## [](#resources)Resources

This section describes the operations available with this REST API.

[Modify Search Manager Options](#put%5Foptions)

### [](#put%5Foptions)Modify Search Manager Options

PUT /api/managerOptions

#### [](#put%5Foptions-description)Description

Sets Search manager options. Note that only one setting is available: `disableFileTransferRebalance`.

The Search Service automatically partitions its indexes across all Search nodes in the cluster, ensuring optimal distribution, following rebalance.

To achieve this, in versions of Couchbase Server prior to 7.1, by default, partitions needing to be newly created were entirely built, on their newly assigned nodes. In 7.1+, by default, new partitions are created by the transfer of partition files from old nodes to new nodes: this significantly enhances performance. This is an Enterprise-only feature, which requires all Search Service nodes either to be running 7.1 or later; or to be running 7.0.2, with the feature explicitly switched on by means of this endpoint. Users of 7.1+ can explicitly switch the feature off by means of this endpoint; in which case partition build is used to establish new partitions, rather than file transfer.

During file transfer, should an unresolvable error occur, file transfer is automatically abandoned, and partition build is used instead.

Consumes

* application/json

Produces

* application/json

#### [](#put%5Foptions-parameters)Parameters

Body Parameter

| Name             | Description                                  | Schema              |
| ---------------- | -------------------------------------------- | ------------------- |
| **Body**optional | An object specifying Search manager options. | [Options](#Options) |

#### [](#put%5Foptions-responses)Responses

| HTTP Code | Description                                                          | Schema                |
| --------- | -------------------------------------------------------------------- | --------------------- |
| 200       | The operation was successful.                                        | [Response](#Response) |
| 401       | Failure to authenticate. The user name or password may be incorrect. | [Response](#Response) |
| 404       | Object not found. The URL may be incorrectly specified.              | [Response](#Response) |
| 405       | Method not allowed. The method may be incorrectly specified.         | [Response](#Response) |

#### [](#put%5Foptions-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#put%5Foptions-ex-curl)Example HTTP Request

The [Disable](#put%5Foptions-ex-curl-0) request disables the creation of new partitions by means of file transfer. From this point, Search Service index partitions are built on the new nodes assigned to them during rebalance.

The [Enable](#put%5Foptions-ex-curl-1) request re-enables the creation of new partitions by means of file transfer. From this point, Search Service index partitions are again created by file transfer, on the new nodes assigned to them during rebalance.

Disable

```sh
curl -X PUT http://$HOST:8094/api/managerOptions \
-u $USER:$PASSWORD \
-H "Content-type:application/json" \
-d '{"disableFileTransferRebalance": "true" }'
```

Enable

```sh
curl -X PUT http://$HOST:8094/api/managerOptions \
-u $USER:$PASSWORD \
-H "Content-type:application/json" \
-d '{"disableFileTransferRebalance": "false" }'
```

#### [](#put%5Foptions-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok"
}
```

Response 405

```json
{
  "error" : "Method not allowed for endpoint",
  "status" : "fail"
}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Options](#Options)  
[Response](#Response)

### [](#Options)Options

 Object

| Property                                 |                                                                                                                                                                                                                                                                                             | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **disableFileTransferRebalance**optional | If the value is false (the default), new Search Service partitions are created during rebalance by means of partition file transfer. If the value is true, partitions are created by means of partition build, from scratch, over DCP connections from the Data Service. **Default:** false | Boolean |

### [](#Response)Response

 Object

| Property           |                                                         | Schema |
| ------------------ | ------------------------------------------------------- | ------ |
| **status**required | The status of the operation.                            | String |
| **error**optional  | The error message, if the operation was not successful. | String |

## [](#security)Security

The Search REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-Default)Default

**Type:** http

For more information, see [Roles](../learn/security/roles.md).

## [](#see-also)See Also

* An overview of rebalance for all services is provided at [Rebalance](../learn/clusters-and-availability/rebalance.md).
* An overview of the REST API for the Search Service is provided at [Search API](../rest-api/rest-fts.md).
* An architectural summary of the Search Service is provided at [Search Service Architecture](../learn/services-and-indexes/services/search-service.md#search-service-architecture).