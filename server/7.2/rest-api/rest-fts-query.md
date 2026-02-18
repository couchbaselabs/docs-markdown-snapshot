---
title: Active Queries REST API
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-fts-query.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/rest-api/rest-fts-query.html)

# Active Queries REST API

## [](#overview)Overview

The Active Queries REST API is provided by the Search service. This API enables you to get information about active FTS queries.

The API schemes and host URLs are as follows:

* `http://node:8094/`
* `https://node:18094/` (for secure access)

where `node` is the host name or IP address of a computer running the Search service.

### [](#version-information)Version information

_Version_ : 7.0

### [](#produces)Produces

* `application/json`

## [](#paths)Paths

**Table of Contents**

* [View Active Index Queries](#api-query-index)
* [View Active Node Queries](#api-query)
* [Cancel Active Queries](#api-query-cancel)

### [](#api-query-index)View Active Index Queries

GET /api/query/index/{indexName}

#### [](#description)Description

Gets the details of all the active queries for any given FTS index in the system.

#### [](#parameters)Parameters

| Type      | Name                      | Description                                                                                                                                                                                                                                            | Schema            |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **Path**  | **indexName** _required_  | The name of a full-text index.                                                                                                                                                                                                                         | string            |
| **Query** | **longerThan** _optional_ | Filters the queries running beyond the given span of time. The duration string is a signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as 20s, \-1.5h or 2h45m. Valid time units are ns, us (or µs), ms, s, m, h. | string (duration) |

#### [](#example-http-request)Example HTTP request

Request 1: Find queries on the index `DemoIndex1` that have been running for longer than 1 ms.

Curl request

```shell
curl -XGET -H "Content-Type: application/json" \
-u <username>:<password> \
'http://localhost:8094/api/query/index/DemoIndex1?longerThan=1ms'
```

#### [](#example-http-response)Example HTTP response

Result of [request 1](#request-1).

Response 200

```json
{
  "status": "ok",
  "stats": {
    "total": 3,
    "successful": 3
  },
  "totalActiveQueryCount": 4,
  "filteredActiveQueries": {
    "indexName": "DemoIndex1",
    "longerThan": "1ms",
    "queryCount": 2,
    "queryMap": {
      "b91d75480470f979f65f04e8f20a1f7b-16": {
        "QueryContext": {
          "query": {
            "query": "good restraunts in france"
          },
          "size": 10,
          "from": 0,
          "timeout": 120000,
          "index": "DemoIndex1"
        },
        "executionTime": "1.059754811s"
      },
      "f76b2d51397feee28c1e757ed426ef93-2": {
        "QueryContext": {
          "query": {
            "query": "mexican food in england"
          },
          "size": 10,
          "from": 0,
          "timeout": 120000,
          "index": "DemoIndex1"
        },
        "executionTime": "1.058247896s"
      }
    }
  }
}
```

### [](#api-query)View Active Node Queries

GET /api/query

#### [](#description-2)Description

Gets the details of all the active queries in any FTS node in a cluster. The response of the endpoint will have the entries in `queryMap` whose key is of the format "nodeUUID-queryID". So, the key tells that the active query, which is the value, is running on the node with uuid equal to `nodeUUID` and has an ID `queryID` on that node.

#### [](#parameters-2)Parameters

| Type      | Name                      | Description                                                                                                                                                                                                                                            | Schema            |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **Query** | **longerThan** _optional_ | Filters the queries running beyond the given span of time. The duration string is a signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as 20s, \-1.5h or 2h45m. Valid time units are ns, us (or µs), ms, s, m, h. | string (duration) |

#### [](#example-http-request-2)Example HTTP request

Request 2: Find all active queries across the fts cluster.

Curl request

```shell
curl -XGET -H "Content-Type: application/json" \
-u <username>:<password> \
http://localhost:8094/api/query
```

Request 3: Find all queries across cluster that have been running for longer than 7s.

Curl request

```shell
curl -XGET -H "Content-Type: application/json" \
-u <username>:<password> \
'http://localhost:8094/api/query?longerThan=7s'
```

#### [](#example-http-response-2)Example HTTP response

Result of [request 2](#request-2).

Response 200

```json
{
  "status": "ok",
  "stats": {
    "total": 3,
    "successful": 3
  },
  "totalActiveQueryCount": 4,
  "filteredActiveQueries": {
    "queryCount": 4,
    "queryMap": {
      "b91d75480470f979f65f04e8f20a1f7b-17": {
        "QueryContext": {
          "query": {
            "query": "good restraunts in france"
          },
          "size": 10,
          "from": 0,
          "timeout": 120000,
          "index": "DemoIndex1"
        },
        "executionTime": "2.144802122s"
      },
      "b91d75480470f979f65f04e8f20a1f7b-18": {
        "QueryContext": {
          "query": {
            "query": "decent hotel with a pool in italy"
          },
          "size": 10,
          "from": 0,
          "timeout": 120000,
          "index": "DemoIndex2"
        },
        "executionTime": "2.144712787s"
      },
      "b91d75480470f979f65f04e8f20a1f7b-19": {
        "QueryContext": {
          "query": {
            "query": "germany"
          },
          "size": 10,
          "from": 0,
          "timeout": 120000,
          "index": "DemoIndex2"
        },
        "executionTime": "2.143957727s"
      },
      "f76b2d51397feee28c1e757ed426ef93-3": {
        "QueryContext": {
          "query": {
            "query": "mexican food in england"
          },
          "size": 10,
          "from": 0,
          "timeout": 120000,
          "index": "DemoIndex1"
        },
        "executionTime": "2.14286421s"
      }
    }
  }
}
```

Result of [request 3](#request-3).

Response 200

```json
{
  "status": "ok",
  "stats": {
    "total": 3,
    "successful": 3
  },
  "totalActiveQueryCount": 3,
  "filteredActiveQueries": {
    "longerThan": "7s",
    "queryCount": 1,
    "queryMap": {
      "b91d75480470f979f65f04e8f20a1f7b-21": {
        "QueryContext": {
          "query": {
            "query": "decent hotel with a pool in italy"
          },
          "size": 10,
          "from": 0,
          "timeout": 120000,
          "index": "DemoIndex1"
        },
        "executionTime": "10.541956741s"
      }
    }
  }
}
```

### [](#api-query-cancel)Cancel Active Queries

POST /api/query/{queryID}/cancel

#### [](#description-3)Description

Allows the user to cancel an active query that’s running longer than expected. This API is used along side the view active queries API to get the parameters `queryID` and `uuid` which will be used to cancel the query.

#### [](#parameters-3)Parameters

| Type          | Name                   | Description                                                                                                                                                                                                                                  | Schema            |
| ------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **Query ID**  | **queryID** _required_ | The active query’s ID                                                                                                                                                                                                                        | integer           |
| **Node UUID** | **uuid** _optional_    | Passed as a body parameter. uuid represents the active query’s coordinator node’s UUID, where the query will be canceled. This parameter allows the user to cancel a query anywhere in the system by specifying its coordinator node’s UUID. | string (duration) |

#### [](#example-http-request-3)Example HTTP request

Request 4: Cancel a long running query with query ID 24 whose coordinator node has a uuid b91d75480470f979f65f04e8f20a1f7b.

Curl request

```shell
curl -X POST -H "Content-Type: application/json" -u <username>:<password> \
http://localhost:8094/api/query/24/cancel -d \
'{ "uuid": "b91d75480470f979f65f04e8f20a1f7b" }'
```

#### [](#example-http-response-3)Example HTTP response

Result of [request 4](#request-4).

Response 200

```json
{
  "status": "ok",
  "msg": "query with ID '24' on node 'b91d75480470f979f65f04e8f20a1f7b' was aborted!"
}
```