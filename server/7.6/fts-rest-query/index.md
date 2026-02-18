---
title: Couchbase Search Active Queries REST API
description: The Search Active Queries REST API is provided by the Search
  Service. This API enables you to get information about active Search queries.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/fts-rest-query/pages/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/fts-rest-query/index.html)

# Couchbase Search Active Queries REST API

## [](#overview)Overview

The Search Active Queries REST API is provided by the Search service. This API enables you to get information about active Search queries.

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

[View Active Node Queries](#api-query)  
[Cancel Active Queries](#api-query-cancel)  
[View Active Index Queries](#api-query-index)

### [](#api-query)View Active Node Queries

GET /api/query

#### [](#api-query-description)Description

Gets the details of all the active queries in any Search node in a cluster.

Produces

* application/json

#### [](#api-query-parameters)Parameters

Query Parameters

| Name                   | Description                                                                                                                                                                                                                                            | Schema            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **longerThan**optional | Filters the queries running beyond the given span of time. The duration string is a signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as 20s, \-1.5h or 2h45m. Valid time units are ns, us (or µs), ms, s, m, h. | String (duration) |

#### [](#api-query-responses)Responses

| HTTP Code | Description                                                          | Schema                             |
| --------- | -------------------------------------------------------------------- | ---------------------------------- |
| 200       | A list of all active Search queries across all nodes in the cluster. | [Active Response](#ActiveResponse) |

#### [](#api-query-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#api-query-ex-curl)Example HTTP Request

The [All](#api-query-ex-curl-0) request finds all active queries across the Search cluster.

The [Filtered](#api-query-ex-curl-1) request finds all queries across the cluster that have been running for longer than 7 s.

All

```sh
curl -XGET -H "Content-Type: application/json" \
  -u $USER:$PASSWORD \
  "http://$HOST:8094/api/query"
```

Filtered

```sh
curl -XGET -H "Content-Type: application/json" \
  -u $USER:$PASSWORD \
  "http://$HOST:8094/api/query?longerThan=7s"
```

#### [](#api-query-ex-response)Example HTTP Response

Response 200

All active node queries

```json
{
  "status" : "ok",
  "stats" : {
    "total" : 3,
    "successful" : 3
  },
  "totalActiveQueryCount" : 4,
  "filteredActiveQueries" : {
    "queryCount" : 4,
    "queryMap" : {
      "b91d75480470f979f65f04e8f20a1f7b-17" : {
        "QueryContext" : {
          "query" : {
            "query" : "good restaurants in france"
          },
          "size" : 10,
          "from" : 0,
          "timeout" : 120000,
          "index" : "DemoIndex1"
        },
        "executionTime" : "2.144802122s"
      },
      "b91d75480470f979f65f04e8f20a1f7b-18" : {
        "QueryContext" : {
          "query" : {
            "query" : "decent hotel with a pool in italy"
          },
          "size" : 10,
          "from" : 0,
          "timeout" : 120000,
          "index" : "DemoIndex2"
        },
        "executionTime" : "2.144712787s"
      },
      "b91d75480470f979f65f04e8f20a1f7b-19" : {
        "QueryContext" : {
          "query" : {
            "query" : "germany"
          },
          "size" : 10,
          "from" : 0,
          "timeout" : 120000,
          "index" : "DemoIndex2"
        },
        "executionTime" : "2.143957727s"
      },
      "f76b2d51397feee28c1e757ed426ef93-3" : {
        "QueryContext" : {
          "query" : {
            "query" : "mexican food in england"
          },
          "size" : 10,
          "from" : 0,
          "timeout" : 120000,
          "index" : "DemoIndex1"
        },
        "executionTime" : "2.14286421s"
      }
    }
  }
}
```

All active node queries (filtered)

```json
{
  "status" : "ok",
  "stats" : {
    "total" : 3,
    "successful" : 3
  },
  "totalActiveQueryCount" : 3,
  "filteredActiveQueries" : {
    "longerThan" : "7s",
    "queryCount" : 1,
    "queryMap" : {
      "b91d75480470f979f65f04e8f20a1f7b-21" : {
        "QueryContext" : {
          "query" : {
            "query" : "decent hotel with a pool in italy"
          },
          "size" : 10,
          "from" : 0,
          "timeout" : 120000,
          "index" : "DemoIndex1"
        },
        "executionTime" : "10.541956741s"
      }
    }
  }
}
```

### [](#api-query-cancel)Cancel Active Queries

POST /api/query/{queryID}/cancel

#### [](#api-query-cancel-description)Description

Allows the user to cancel an active query that's running longer than expected. Use the View Active Index Queries API or the View Active Node Queries API to get the parameters `queryID` and `uuid`, which are used to identify and cancel the query.

Consumes

* application/json

Produces

* application/json

#### [](#api-query-cancel-parameters)Parameters

Path Parameters

| Name                | Description                                                                                | Schema  |
| ------------------- | ------------------------------------------------------------------------------------------ | ------- |
| **queryID**required | The ID of the active query. This ID is used to identify the query that you want to cancel. | Integer |

Body Parameter

| Name             | Description                                                                                                                               | Schema                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Body**optional | The body contains the UUID of the node where the query is running. This is optional and allows cancellation of queries on specific nodes. | [Cancellation Request](#CancelRequest) |

#### [](#api-query-cancel-responses)Responses

| HTTP Code | Description                          | Schema                                   |
| --------- | ------------------------------------ | ---------------------------------------- |
| 200       | The query was successfully canceled. | [Cancellation Response](#CancelResponse) |

#### [](#api-query-cancel-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#api-query-cancel-ex-curl)Example HTTP Request

This request cancels a long running query with query ID `24` whose coordinator node has a UUID `b91d75480470f979f65f04e8f20a1f7b`.

```sh
curl -X POST -H "Content-Type: application/json" -u $USER:$PASSWORD \
  "http://$HOST:8094/api/query/24/cancel" -d \
  '{ "uuid": "b91d75480470f979f65f04e8f20a1f7b" }'
```

#### [](#api-query-cancel-ex-request)Example Request Body

```json
{
  "uuid" : "b91d75480470f979f65f04e8f20a1f7b"
}
```

#### [](#api-query-cancel-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "msg" : "query with ID '24' on node 'b91d75480470f979f65f04e8f20a1f7b' was aborted!"
}
```

### [](#api-query-index)View Active Index Queries

GET /api/query/index/{indexName}

#### [](#api-query-index-description)Description

Gets the details of all the active queries for any given Search index in the system.

Produces

* application/json

#### [](#api-query-index-parameters)Parameters

Path Parameters

| Name                  | Description                   | Schema |
| --------------------- | ----------------------------- | ------ |
| **indexName**required | The name of the Search index. | String |

Query Parameters

| Name                   | Description                                                                                                                                                                                                                                            | Schema            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **longerThan**optional | Filters the queries running beyond the given span of time. The duration string is a signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as 20s, \-1.5h or 2h45m. Valid time units are ns, us (or µs), ms, s, m, h. | String (duration) |

#### [](#api-query-index-responses)Responses

| HTTP Code | Description                                              | Schema                             |
| --------- | -------------------------------------------------------- | ---------------------------------- |
| 200       | A list of active queries for the specified Search index. | [Active Response](#ActiveResponse) |

#### [](#api-query-index-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#api-query-index-ex-curl)Example HTTP Request

This request finds queries on the index `DemoIndex1` that have been running for longer than 1 ms.

```sh
curl -XGET -H "Content-Type: application/json" \
-u $USER:$PASSWORD \
"http://$HOST:8094/api/query/index/DemoIndex1?longerThan=1ms"
```

#### [](#api-query-index-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "stats" : {
    "total" : 3,
    "successful" : 3
  },
  "totalActiveQueryCount" : 4,
  "filteredActiveQueries" : {
    "indexName" : "DemoIndex1",
    "longerThan" : "1ms",
    "queryCount" : 2,
    "queryMap" : {
      "b91d75480470f979f65f04e8f20a1f7b-16" : {
        "QueryContext" : {
          "query" : {
            "query" : "good restaurants in france"
          },
          "size" : 10,
          "from" : 0,
          "timeout" : 120000,
          "index" : "DemoIndex1"
        },
        "executionTime" : "1.059754811s"
      },
      "f76b2d51397feee28c1e757ed426ef93-2" : {
        "QueryContext" : {
          "query" : {
            "query" : "mexican food in england"
          },
          "size" : 10,
          "from" : 0,
          "timeout" : 120000,
          "index" : "DemoIndex1"
        },
        "executionTime" : "1.058247896s"
      }
    }
  }
}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Active Response](#ActiveResponse)  
[Filtered Active Queries](#ActiveResponseFilter)  
[Query Map](#ActiveResponseFilterMap)  
[Query Map Item](#ActiveResponseFilterMapItem)  
[Query Context](#ActiveResponseFilterMapItemContext)  
[Stats](#ActiveResponseStats)  
[Cancellation Request](#CancelRequest)  
[Cancellation Response](#CancelResponse)

### [](#ActiveResponse)Active Response

 Object

| Property                          |                                                              | Schema                                           |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------ |
| **status**optional                | The status of the request.                                   | String                                           |
| **stats**optional                 | An object containing request statistics.                     | [Stats](#ActiveResponseStats)                    |
| **totalActiveQueryCount**optional | The total number of active queries.                          | Integer                                          |
| **filteredActiveQueries**optional | An object containing details of the filtered active queries. | [Filtered Active Queries](#ActiveResponseFilter) |

#### Filtered Active Queries

 Object

| Property               |                                                                                                          | Schema                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **indexName**optional  | The name of the Search index. Only included if viewing active queries for a specific index.              | String                                |
| **longerThan**optional | The duration used to filter the active queries. Only included if the longerThan query parameter is used. | String (duration)                     |
| **queryCount**optional | The number of filtered active queries.                                                                   | Integer                               |
| **queryMap**optional   | Contains 1 or more nested objects, each containing the details of a single active query.                 | [Query Map](#ActiveResponseFilterMap) |

#### Query Map

 Object

| Property           |                                                                                                                                                                                    | Schema                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| additionalproperty | The details of a single active query. The name of the property is the UUID of the node on which the query is running, and the ID of the query on that node, separated by a hyphen. | [Query Map Item](#ActiveResponseFilterMapItem) |

#### Query Map Item

 Object

| Property                  |                                      | Schema                                               |
| ------------------------- | ------------------------------------ | ---------------------------------------------------- |
| **QueryContext**optional  | The query context.                   | [Query Context](#ActiveResponseFilterMapItemContext) |
| **executionTime**optional | The time taken to execute the query. | String (duration)                                    |

#### Query Context

 Object

| Property            |                                                                                                                                          | Schema  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **query**optional   | An object containing the Search query. For more information, see [Search Request JSON Properties](../search/search-request-params.html). | Object  |
| **size**optional    | **Example:** 10                                                                                                                          | Integer |
| **from**optional    | **Example:** 0                                                                                                                           | Integer |
| **timeout**optional | **Example:** 120000                                                                                                                      | Integer |
| **index**optional   | The name of a Search index.                                                                                                              | String  |

#### Stats

 Object

| Property               |                | Schema  |
| ---------------------- | -------------- | ------- |
| **total**optional      | **Example:** 3 | Integer |
| **successful**optional | **Example:** 3 | Integer |

### [](#CancelRequest)Cancellation Request

 Object

| Property         |                                                                                                                                                                                                             | Schema |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **uuid**optional | Represents the active query's coordinator node's UUID, where the query will be canceled. This parameter allows the user to cancel a query anywhere in the system by specifying its coordinator node's UUID. | String |

### [](#CancelResponse)Cancellation Response

 Object

| Property           |                                                                     | Schema |
| ------------------ | ------------------------------------------------------------------- | ------ |
| **status**optional | The status of the request.                                          | String |
| **msg**optional    | The response message, giving details of the node UUID and query ID. | String |

## [](#security)Security

The Search REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-Default)Default

**Type:** http

For more information, see [Roles](../learn/security/roles.md).