---
title: Couchbase Search Advanced API
description: The Search Advanced REST APIs are provided by the Search Service.
  These APIs enable you to manage and monitor advanced settings of your Search
  indexes.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/fts-rest-advanced/pages/index.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:7.6@server:fts-rest-advanced:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts-rest-advanced/index.html)

# Couchbase Search Advanced API

## [](#overview)Overview

The Advanced Search REST APIs are provided by the Search Service. These APIs enable you to manage and query Search index partitions and to specify advanced settings.

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

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Definition](#tag-Definition)  
[Query](#tag-Query)  
[Quota](#tag-Quota)

### [](#tag-Definition)Definition

Operations for Search index partition definition.

[Get Index Partition Information](#getPartition)  
[Get Index Partition by Name](#getPartitionName)

#### [](#getPartition)Get Index Partition Information

GET /api/pindex

##### [](#getPartition-description)Description

Get information about a Search index partition.

Produces

* application/json

##### [](#getPartition-responses)Responses

| HTTP Code | Description                                                      | Schema                              |
| --------- | ---------------------------------------------------------------- | ----------------------------------- |
| 200       | A JSON object containing the Search index partition information. | [Index Partitions](#indexPartition) |

##### [](#getPartition-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#getPartition-ex-response)Example HTTP Response

Response 200

```json
{
  "pindexes" : {
    "myFirstIndex_6cc599ab7a85bf3b_0" : {
      "indexName" : "myFirstIndex",
      "indexParams" : "",
      "indexType" : "blackhole",
      "indexUUID" : "6cc599ab7a85bf3b",
      "name" : "myFirstIndex_6cc599ab7a85bf3b_0",
      "sourceName" : "",
      "sourceParams" : "",
      "sourcePartitions" : "",
      "sourceType" : "nil",
      "sourceUUID" : "",
      "uuid" : "2d9ecb8b574a9f6a"
    }
  },
  "status" : "ok"
}
```

#### [](#getPartitionName)Get Index Partition by Name

GET /api/pindex/{pindexName}

##### [](#getPartitionName-description)Description

Get information about a specific Search index partition by name.

##### [](#getPartitionName-parameters)Parameters

Path Parameters

| Name                   | Description                             | Schema |
| ---------------------- | --------------------------------------- | ------ |
| **pindexName**required | The name of the Search index partition. | String |

##### [](#getPartitionName-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | Success     |        |

##### [](#getPartitionName-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

### [](#tag-Query)Query

Operations for querying Search index partitions.

[Get Index Partition Document Count](#getPartitionCount)  
[Query Index Partition](#queryPartition)

#### [](#getPartitionCount)Get Index Partition Document Count

GET /api/pindex/{pindexName}/count

##### [](#getPartitionCount-description)Description

Get the document count of a specific Search index partition.

Produces

* application/json

##### [](#getPartitionCount-parameters)Parameters

Path Parameters

| Name                   | Description                             | Schema |
| ---------------------- | --------------------------------------- | ------ |
| **pindexName**required | The name of the Search index partition. | String |

##### [](#getPartitionCount-responses)Responses

| HTTP Code | Description                                                        | Schema                           |
| --------- | ------------------------------------------------------------------ | -------------------------------- |
| 200       | The Search Service returns a response that includes the status ok. | [Document Count](#DocumentCount) |

##### [](#getPartitionCount-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#getPartitionCount-ex-response)Example HTTP Response

Response 200

```json
{
  "count" : 0,
  "status" : "ok"
}
```

#### [](#queryPartition)Query Index Partition

POST /api/pindex/{pindexName}/query

##### [](#queryPartition-description)Description

Execute a query against a specific Search index partition by name.

Consumes

* application/json

Produces

* application/json

##### [](#queryPartition-parameters)Parameters

Path Parameters

| Name                   | Description                             | Schema |
| ---------------------- | --------------------------------------- | ------ |
| **pindexName**required | The name of the Search index partition. | String |

Body Parameter

| Name             | Description                                                                                                                                                                                                  | Schema                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **Body**required | A JSON object to define the settings for your Search query. For more information about how to create a Search query JSON object, see [Search Request JSON Properties](../search/search-request-params.html). | [Query Request](#QueryRequest) |

##### [](#queryPartition-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                                       | Schema                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| 200       | The response object has a status section that must be checked for every request. Under nearly all circumstances, the query response will be HTTP 200 even though individual index shards (partitions) may encounter a timeout or return an error. | [Query Response](#QueryResponse) |

##### [](#queryPartition-security)Security

| Type         | Name                     |
| ------------ | ------------------------ |
| http (basic) | [Write](#security-Write) |

##### [](#queryPartition-ex-request)Example Request Body

```json
{
  "fields" : [ "*" ],
  "query" : {
    "query" : "+view +food +beach"
  },
  "size" : 10,
  "from" : 0
}
```

##### [](#queryPartition-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : {
    "total" : 1,
    "failed" : 0,
    "successful" : 1
  },
  "hits" : [ {
    "index" : "travel-sample.inventory.landmark-content-index_49563a96ea6d3686_4c1c5584",
    "id" : "landmark_4428",
    "score" : 2.425509689250102,
    "sort" : [ "_score" ],
    "fields" : {
      "content" : "serves fresh food at very reasonable prices - view of stoney beach with herons"
    }
  }, {
    "index" : "travel-sample.inventory.landmark-content-index_49563a96ea6d3686_4c1c5584",
    "id" : "landmark_26385",
    "score" : 1.6270812956011347,
    "sort" : [ "_score" ],
    "fields" : {
      "content" : "Burgers, seafood, and other simple but tasty meals right at the harbor. You can take your food around the corner to sit on the beach or the sea wall and enjoy the ocean view while you eat."
    }
  }, {
    "index" : "travel-sample.inventory.landmark-content-index_49563a96ea6d3686_4c1c5584",
    "id" : "landmark_38035",
    "score" : 1.1962539437368078,
    "sort" : [ "_score" ],
    "fields" : {
      "content" : "Famous for &quot;the Blue Lady&quot;, a ghost rumored to haunt the premises, the Moss Beach distillery offers a full menu, Sunday brunch, drinks, and a tremendous ocean view with comfortable fire pits. Happy hour Mon-Fri from 5PM to 7PM offers half-priced drinks and a discounted food menu."
    }
  } ],
  "total_hits" : 3,
  "cost" : 150479,
  "max_score" : 2.425509689250102,
  "took" : 1441203,
  "facets" : null
}
```

### [](#tag-Quota)Quota

Operations for managing Search memory quota.

[Set Search Memory Quota](#setFtsMemoryQuota)

#### [](#setFtsMemoryQuota)Set Search Memory Quota

POST /pools/default

##### [](#setFtsMemoryQuota-description)Description

Sets the memory quota for the Search Service.

Consumes

* application/x-www-form-urlencoded

##### [](#setFtsMemoryQuota-parameters)Parameters

Form Parameters

| Name                       | Description                                              | Schema  |
| -------------------------- | -------------------------------------------------------- | ------- |
| **ftsMemoryQuota**optional | The memory quota for the Search Service. **Example:** 56 | Integer |

##### [](#setFtsMemoryQuota-responses)Responses

| HTTP Code | Description       | Schema |
| --------- | ----------------- | ------ |
| 200       | Memory quota set. |        |

##### [](#setFtsMemoryQuota-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Document Count](#DocumentCount)  
[Index Partitions](#indexPartition)  
[Index Partitions Wrapper](#indexPartitionPIndex)  
[Index Partition](#indexPartitionPIndexInner)  
[Query Request](#QueryRequest)  
[Query Response](#QueryResponse)

### [](#DocumentCount)Document Count

 Object

| Property           |                                             | Schema  |
| ------------------ | ------------------------------------------- | ------- |
| **status**optional | The status of the operation.                | String  |
| **count**optional  | The document count for the specified index. | Integer |

### [](#indexPartition)Index Partitions

 Object

| Property             |                                                                           | Schema                                            |
| -------------------- | ------------------------------------------------------------------------- | ------------------------------------------------- |
| **pindexes**optional | An object containing information about 1 or more Search index partitions. | [Index Partitions Wrapper](#indexPartitionPIndex) |
| **status**optional   | The status of the request.                                                | String                                            |

#### Index Partitions Wrapper

 Object

| Property           |                                                                                                                                             | Schema                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| additionalproperty | An object containing information about a single Search index partition. The name of the property is the name of the Search index partition. | [Index Partition](#indexPartitionPIndexInner) |

#### Index Partition

 Object

| Property                     |                                                                                                                                                                        | Schema      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **indexName**optional        | The name of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                                | String      |
| **indexParams**optional      | The Search index's type identifier, type mappings, and analyzers. For more information, see [Params Object](../search/search-index-params.html#params).                | Object      |
| **indexType**optional        | The type of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial). **Values:** "fulltext-index", "fulltext-alias" | String      |
| **indexUUID**optional        | The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                                | UUID (UUID) |
| **name**optional             | The name of the Search index partition.                                                                                                                                | String      |
| **sourceName**optional       | The name of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).                     | String      |
| **sourceParams**optional     | Advanced settings for Search index behavior. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                 | Object      |
| **sourcePartitions**optional |                                                                                                                                                                        | String      |
| **sourceType**optional       | The type of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).                     | String      |
| **sourceUUID**optional       | The UUID of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).                     | UUID (UUID) |
| **uuid**optional             | The UUID of the Search index partition.                                                                                                                                | String      |

### [](#QueryRequest)Query Request

 Object

| Property                     |                                                                                                                                                                                  | Schema         |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **query**optional            | An object that contains the properties for one of the supported query types. For more information, see [Query Object](../search/search-request-params.html#query-object).        | Object         |
| **knn**optional              | An array that contains objects that describe a Vector Search query. For more information, see [Knn Objects](../search/search-request-params.html#knn-object).                    | Object array   |
| **ctl**optional              | An object that contains properties for query consistency. For more information, see [Ctl Object](../search/search-request-params.html#ctl).                                      | Object         |
| **size**optional             | Set the total number of results to return for a single page of search results.                                                                                                   | Integer        |
| **from**optional             | Set an offset value to change where pagination starts for search results.                                                                                                        | Integer        |
| **highlight**optional        | Contains properties to control search result highlighting. For more information, see [Highlight Objects](../search/search-request-params.html#highlight).                        | Object         |
| **fields**optional           | An array of strings to specify each indexed field you want to return in search results.                                                                                          | String array   |
| **facets**optional           | Contains nested objects to define each facet you want to return with search results. For more information, see [Facet Objects](../search/search-request-params.html#facet-name). | Object         |
| **explain**optional          | Whether to create an explanation for a search result's score in search results.                                                                                                  | Boolean        |
| **sort**optional             | Contains an array of strings or JSON objects to set how to sort search results. For more information, see [Sort Object](../search/search-request-params.html#sort).              | Any Type array |
| **includeLocations**optional | Whether to return the position of each occurrence of a search term inside a document.                                                                                            | Boolean        |
| **score**optional            | Whether to include document relevancy scoring in search results.                                                                                                                 | String         |
| **search\_after**optional    | Use to control pagination in search results.                                                                                                                                     | String array   |
| **search\_before**optional   | Use to control pagination in search results.                                                                                                                                     | String array   |
| **collections**optional      | An array of strings that specify the collections where you want to run the query.                                                                                                | String array   |

### [](#QueryResponse)Query Response

 Object

| Property            |                                  | Schema       |
| ------------------- | -------------------------------- | ------------ |
| **status**optional  | The status of the operation.     | String       |
| **results**optional | The results of the Search query. | Object array |

## [](#security)Security

The Search REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-Manage)Manage

You must have the **Search Admin** role, with FTS Manage permissions on the required bucket.

**Type:** http

### [](#security-Read)Read

You must have the **Search Reader** or **Search Admin** role, with FTS Read permissions on the required bucket.

**Type:** http

### [](#security-Write)Write

You must have the **Search Admin** role, with FTS Write permissions on the required bucket.

**Type:** http

For more information, see [Roles](../learn/security/roles.md).