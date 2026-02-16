[View original HTML](/server/7.2/rest-api/get-settings-indexes.html)

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
    "indexerThreads": 0,
    "logLevel": "info",
    "maxRollbackPoints": 5,
    "memorySnapshotInterval": 200,
    "stableSnapshotInterval": 5000,
    "storageMode": "forestdb"
}
```

**401**

This response code returns an empty body.