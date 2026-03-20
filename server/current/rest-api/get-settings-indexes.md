---
title: Retrieve GSI Settings
description: To retrieve the global secondary index settings use <code>GET
  /settings/indexes</code>.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/get-settings-indexes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:rest-api:get-settings-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/get-settings-indexes.html)

# Retrieve GSI Settings

> To retrieve the global secondary index settings use `GET /settings/indexes`. 

## [](#description)Description

This endpoint returns the current index settings for the cluster.

## [](#http-method-and-uri)HTTP Method and URI

```http
GET http://<host>:8091/settings/indexes
```

## [](#response-codes)Response Codes

| Response Code | Description   |
| ------------- | ------------- |
| 200           | Success.      |
| 401           | Unauthorized. |

## [](#sample-curl-command)Sample Curl Command

The following example retrieves the global secondary index settings of the cluster that the node `localhost` is a part of.

```bash
curl -X GET -u 'Administrator:password' 'http://localhost:8091/settings/indexes'
```

## [](#sample-response)Sample Response

**200**

```json
{
  "redistributeIndexes": false,
  "numReplica": 0,
  "enablePageBloomFilter": false,
  "enableShardAffinity": false,
  "indexerThreads": 4,
  "memorySnapshotInterval": 200,
  "stableSnapshotInterval": 5000,
  "maxRollbackPoints": 2,
  "logLevel": "verbose",
  "storageMode": "plasma"
}
```

**401**

This response code returns an empty body.