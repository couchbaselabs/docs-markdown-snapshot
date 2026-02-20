---
title: Run a Simple Search with the REST API and curl/HTTP
description: You can use the REST API and a curl command to run a search against
  a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/simple-search-rest-api.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:search:simple-search-rest-api.adoc[]
---

[View original HTML](/server/7.6/search/simple-search-rest-api.html)

# Run a Simple Search with the REST API and curl/HTTP

> You can use the REST API and a curl command to run a search against a Search index. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* Your user account has the **Search Admin** or **Search Reader** role for the bucket or buckets that contain the Search indexes you want to search.
* You installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../../current/manage/manage-nodes/list-cluster-nodes.md).
* You have created a Search index.  
For more information about how to create a Search index, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md) or [Create a Search Index with the REST API and curl/HTTP](create-search-index-rest-api.md).

## [](#procedure)Procedure

To run a simple search with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPOST` verb.
2. Set your header content to include `"Content-Type: application/json"`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to query:  
```console  
curl -s -XPOST -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/${BUCKET-NAME}/scope/${SCOPE-NAME}/index/${INDEX-NAME}/query -d \  
```  
To use SSL, use the `https` protocol in the Search Service endpoint URL and port `18094`.
4. Enter the JSON payload for your query.  
> [!TIP]  
> Couchbase Server version 7.6.2  
>  
> You can copy the JSON for a Search query from the Couchbase Server Web Console to use in your REST API call. You can choose to copy a full command-line curl example, or copy just the [JSON payload](search-request-params.md). For more information about how to perform a search with the UI, see [Run A Simple Search with the Web Console](simple-search-ui.md).

### [](#example-simple-text-search)Example: Simple Text Search

In the following example, the JSON payload queries an index named `landmark-content-index` for the strings `view`, `food`, and `beach`:

```console
curl -XPOST -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/travel-sample/scope/inventory/index/landmark-content-index/query \
  -d '{
    "explain": true,
    "fields": [
      "*"
    ],
    "highlight": {},
    "query": {
      "query": "+view +food +beach"
    },
    "size": 10,
    "from": 0
  }'
```

If the request is successful, the Search Service API starts by returning a status and a summary of the query request:

```json
    "status": {
        "total": 1,
        "failed": 0,
        "successful": 1
    },
    "request": {
        "query": {
            "query": "+view +food +beach"
        },
        "size": 10,
        "from": 0,
        "highlight": {
            "style": null,
            "fields": null
        },
        "fields": [
            "*"
        ],
        "facets": null,
        "explain": true,
        "sort": [
            "-_score"
        ],
        "includeLocations": false,
        "search_after": null,
        "search_before": null,
        "knn": null,
        "knn_operator": ""
    },
```

The Search Service returns an array, called `hits`, which contains objects that describe the matches found in each document in the Search index:

```json
        {
            "index": "travel-sample.inventory.landmark-content-index_6369e656b9eec849_4c1c5584",
            "id": "landmark_4428",
            "score": 2.425509689250102,
            "explanation": {
                "value": 2.425509689250102,
                "message": "sum of:",
                "children": [
                    {
                        "value": 2.425509689250102,
                        "message": "sum of:",
                        "children": [
                            {
                                "value": 1.0124422206433388,
                                "message": "product of:",
                                "children": [
                                    {
                                        "value": 1.0124422206433388,
                                        "message": "sum of:",
                                        "children": [
                                            {
                                                "value": 1.0124422206433388,
                                                "message": "weight(_all:view^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\nN), product of:",
                                                "children": [
                                                    {
                                                        "value": 0.6460760126054528,
                                                        "message": "queryWeight(_all:view^1.000000), product of:",
                                                        "children": [
                                                            {
                                                                "value": 1,
                                                                "message": "boost"
                                                            },
                                                            {
                                                                "value": 4.701190745593387,
                                                                "message": "idf(docFreq=110, maxDocs=4495)"
                                                            },
                                                            {
                                                                "value": 0.1374281639627249,
                                                                "message": "queryNorm"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "value": 1.5670636285665962,
                                                        "message": "fieldWeight(_all:view in \u0000\u0000\u0000\u0000\u0000\u0000\nN), product of:",
                                                        "children": [
                                                            {
                                                                "value": 1,
                                                                "message": "tf(termFreq(_all:view)=1"
                                                            },
                                                            {
                                                                "value": 0.3333333432674408,
                                                                "message": "fieldNorm(field=_all, doc=\u0000\u0000\u0000\u0000\u0000\u0000\nN)"
                                                            },
                                                            {
                                                                "value": 4.701190745593387,
                                                                "message": "idf(docFreq=110, maxDocs=4495)"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "value": 1,
                                        "message": "coord(1/1)"
                                    }
                                ]
                            },
                            {
                                "value": 0.9006237048061059,
                                "message": "product of:",
                                "children": [
                                    {
                                        "value": 0.9006237048061059,
                                        "message": "sum of:",
                                        "children": [
                                            {
                                                "value": 0.9006237048061059,
                                                "message": "weight(_all:beach^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\nN), product of:",
                                                "children": [
                                                    {
                                                        "value": 0.6093547205466089,
                                                        "message": "queryWeight(_all:beach^1.000000), product of:",
                                                        "children": [
                                                            {
                                                                "value": 1,
                                                                "message": "boost"
                                                            },
                                                            {
                                                                "value": 4.433987204485146,
                                                                "message": "idf(docFreq=144, maxDocs=4495)"
                                                            },
                                                            {
                                                                "value": 0.1374281639627249,
                                                                "message": "queryNorm"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "value": 1.4779957788760876,
                                                        "message": "fieldWeight(_all:beach in \u0000\u0000\u0000\u0000\u0000\u0000\nN), product of:",
                                                        "children": [
                                                            {
                                                                "value": 1,
                                                                "message": "tf(termFreq(_all:beach)=1"
                                                            },
                                                            {
                                                                "value": 0.3333333432674408,
                                                                "message": "fieldNorm(field=_all, doc=\u0000\u0000\u0000\u0000\u0000\u0000\nN)"
                                                            },
                                                            {
                                                                "value": 4.433987204485146,
                                                                "message": "idf(docFreq=144, maxDocs=4495)"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "value": 1,
                                        "message": "coord(1/1)"
                                    }
                                ]
                            },
                            {
                                "value": 0.5124437638006571,
                                "message": "product of:",
                                "children": [
                                    {
                                        "value": 0.5124437638006571,
                                        "message": "sum of:",
                                        "children": [
                                            {
                                                "value": 0.5124437638006571,
                                                "message": "weight(_all:food^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\nN), product of:",
                                                "children": [
                                                    {
                                                        "value": 0.4596440040764192,
                                                        "message": "queryWeight(_all:food^1.000000), product of:",
                                                        "children": [
                                                            {
                                                                "value": 1,
                                                                "message": "boost"
                                                            },
                                                            {
                                                                "value": 3.3446128568019726,
                                                                "message": "idf(docFreq=430, maxDocs=4495)"
                                                            },
                                                            {
                                                                "value": 0.1374281639627249,
                                                                "message": "queryNorm"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "value": 1.1148709854930678,
                                                        "message": "fieldWeight(_all:food in \u0000\u0000\u0000\u0000\u0000\u0000\nN), product of:",
                                                        "children": [
                                                            {
                                                                "value": 1,
                                                                "message": "tf(termFreq(_all:food)=1"
                                                            },
                                                            {
                                                                "value": 0.3333333432674408,
                                                                "message": "fieldNorm(field=_all, doc=\u0000\u0000\u0000\u0000\u0000\u0000\nN)"
                                                            },
                                                            {
                                                                "value": 3.3446128568019726,
                                                                "message": "idf(docFreq=430, maxDocs=4495)"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "value": 1,
                                        "message": "coord(1/1)"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "locations": {
                "content": {
                    "beach": [
                        {
                            "pos": 11,
                            "start": 61,
                            "end": 66,
                            "array_positions": null
                        }
                    ],
                    "food": [
                        {
                            "pos": 3,
                            "start": 13,
                            "end": 17,
                            "array_positions": null
                        }
                    ],
                    "view": [
                        {
                            "pos": 8,
                            "start": 46,
                            "end": 50,
                            "array_positions": null
                        }
                    ]
                }
            },
            "fragments": {
                "content": [
                    "serves fresh <mark>food</mark> at very reasonable prices - <mark>view</mark> of stoney <mark>beach</mark> with herons"
                ]
            },
            "sort": [
                "_score"
            ],
            "fields": {
                "content": "serves fresh food at very reasonable prices - view of stoney beach with herons"
            }
        },
```

The Search query set score explanations to `true`, so the Search Service shows how it calculated the score for each document.

It also includes the locations of each match, under the `locations` object:

```json
            "locations": {
                "content": {
                    "beach": [
                        {
                            "pos": 11,
                            "start": 61,
                            "end": 66,
                            "array_positions": null
                        }
                    ],
                    "food": [
                        {
                            "pos": 3,
                            "start": 13,
                            "end": 17,
                            "array_positions": null
                        }
                    ],
                    "view": [
                        {
                            "pos": 8,
                            "start": 46,
                            "end": 50,
                            "array_positions": null
                        }
                    ]
                }
            },
```

The Search query enabled highlighting, so the Search Service uses the `<mark>` HTML tag to mark each match it found inside the Search index, inside a `fragments` object:

```json
            "fragments": {
                "content": [
                    "serves fresh <mark>food</mark> at very reasonable prices - <mark>view</mark> of stoney <mark>beach</mark> with herons"
                ]
            },
```

Since the target Search index was configured to store field values and return them in results, the Search Service returns the original field content in the `fields` object:

```json
            "fields": {
                "content": "serves fresh food at very reasonable prices - view of stoney beach with herons"
            }
```

At the end of the `hits` array, the Search Service returns a quick summary of the total number of hits, the maximum score, how long the query took, and other information:

```json
    "total_hits": 3,
    "cost": 123616,
    "max_score": 2.425509689250102,
    "took": 636964,
    "facets": null
```

For more information about the available properties for a Search query JSON payload, see [Search Request JSON Properties](search-request-params.md).

If the REST API call is successful, the Search Service returns a `200 OK` and the following JSON response:

```json
{
    "status": {
        "total": 1,
        "failed": 0,
        "successful": 1
    },
    "hits": [
        {
            "index": "travel-sample.inventory.landmark-content-index_49563a96ea6d3686_4c1c5584",
            "id": "landmark_4428",
            "score": 2.425509689250102,
            "sort": [
                "_score"
            ],
            "fields": {
                "content": "serves fresh food at very reasonable prices - view of stoney beach with herons"
            }
        },
        {
            "index": "travel-sample.inventory.landmark-content-index_49563a96ea6d3686_4c1c5584",
            "id": "landmark_26385",
            "score": 1.6270812956011347,
            "sort": [
                "_score"
            ],
            "fields": {
                "content": "Burgers, seafood, and other simple but tasty meals right at the harbor. You can take your food around the corner to sit on the beach or the sea wall and enjoy the ocean view while you eat."
            }
        },
        {
            "index": "travel-sample.inventory.landmark-content-index_49563a96ea6d3686_4c1c5584",
            "id": "landmark_38035",
            "score": 1.1962539437368078,
            "sort": [
                "_score"
            ],
            "fields": {
                "content": "Famous for &quot;the Blue Lady&quot;, a ghost rumored to haunt the premises, the Moss Beach distillery offers a full menu, Sunday brunch, drinks, and a tremendous ocean view with comfortable fire pits. Happy hour Mon-Fri from 5PM to 7PM offers half-priced drinks and a discounted food menu."
            }
        }
    ],
    "total_hits": 3,
    "cost": 150479,
    "max_score": 2.425509689250102,
    "took": 1441203,
    "facets": null
}
```

### [](#example-validate-a-search-request)Example: Validate a Search Request

Couchbase Server 7.6.4

In the following example, the JSON payload queries a Search index, `landmark-content-index`, using a [Distance/Radius-Based Geopoint Query](search-request-params.md#geopoint-queries-distance) on the `geo` field:

```json
curl -XPOST -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/travel-sample/scope/inventory/index/landmark-content-index/query \
  -d '{
    "explain": true,
    "fields": [
      "content"
    ],
    "highlight": {},
    "query": {
        "location": {
            "lon": -2.235143,
            "lat": 53.482358
        },
            "distance": "100mi",
            "field": "geo"
    },
    "size": 10,
    "from": 0
  }'
```

The query runs, but does not return any results:

```json
{
    "status": {
        "total": 1,
        "failed": 0,
        "successful": 1
    },
    "request": {
        "query": {
            "location": [
                -2.235143,
                53.482358
            ],
            "distance": "100mi",
            "field": "geo"
        },
        "size": 10,
        "from": 0,
        "highlight": {
            "style": null,
            "fields": null
        },
        "fields": [
            "content"
        ],
        "facets": null,
        "explain": true,
        "sort": [
            "-_score"
        ],
        "includeLocations": false,
        "search_after": null,
        "search_before": null,
        "knn": null,
        "knn_operator": ""
    },
    "hits": [],
    "total_hits": 0,
    "cost": 0,
    "max_score": 0,
    "took": 4150150,
    "facets": null
}
```

To try and validate why the query did not return any results, you can include the [ctl object](search-request-params.md#ctl) with the `validate` property:

```json
curl -XPOST -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/travel-sample/scope/inventory/index/landmark-content-index/query \
  -d '{
    "explain": true,
    "fields": [
      "content"
    ],
    "highlight": {},
    "query": {
        "location": {
            "lon": -2.235143,
            "lat": 53.482358
        },
            "distance": "100mi",
            "field": "geo"
    },
    "ctl": {
        "validate": true
    },
    "size": 10,
    "from": 0
  }'
```

With the `validate` property included, the Search query now returns a `400 Bad Request` error and the following JSON response:

```json
{
    "error": "rest_index: Query, indexName: travel-sample.inventory.landmark-content-index, err: bleve: QueryBleve query validation failed against index, err: query_validate: field not indexed, name: geo, type: geopoint",
    "request": {
        "ctl": {
            "validate": true
        },
        "explain": true,
        "fields": [
            "content"
        ],
        "from": 0,
        "highlight": {},
        "query": {
            "distance": "100mi",
            "field": "geo",
            "location": {
                "lat": 53.482358,
                "lon": -2.235143
            }
        },
        "size": 10
    },
    "status": "fail"
}
```

The Search Service validates the query and identifies that the `geo` field used in the query is not included in the Search index.

## [](#next-steps)Next Steps

If you do not get the search results you were expecting, you can change the JSON payload [for your Search index](search-index-params.md) or [for your Search query](search-request-params.md).

If your cluster is running Couchbase Server version 7.6.2 and later, you can also copy a full command-line curl example from the Server Web Console to use with the REST API, or edit a generated Search query with the built-in code editor.

You can also [Customize a Search Index with the Web Console](customize-index.md).