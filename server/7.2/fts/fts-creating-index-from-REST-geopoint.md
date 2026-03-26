---
title: Creating a Geopoint Index via the REST API
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-index-from-REST-geopoint.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:fts:fts-creating-index-from-REST-geopoint.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-index-from-REST-geopoint.html)

# Creating a Geopoint Index via the REST API

This example quickly creates the same index as [Creating a Geopoint Index via the UI](fts-creating-index-from-UI-classic-editor-geopoint.md#main).

The cURL command below was initially created via the Classic Editor in the UI, however the follwoing modifications were made.

* The curl flag "**\-s**" to suppress some runtime output.
* The credentials "**\-u <username>:<password>**" were altered to "**\-u** $**{CB\_USERNAME}**:$**{CB\_PASSWORD}**".
* The hostname or IP address was replaced with $**{CB\_HOSTNAME}**.
* The commands output is piped through the utility **[jq](http://stedolan.github.io/jq)** to enhance readability.
* The two (2) UUIDs were removed (similar to the below) because we want to make a new index not modify an existing one.  
```json  
  "uuid": "273a60635f5248e5",  
  "sourceUUID": "2b421d183cb76aebbffa45424736ec2e",  
```

# [](#the-creation-command)The Creation Command

The full command to create the index is below and can be executed verbatim if you have the environment variable $**{CB\_USERNAME}**, $**{CB\_PASSWORD}** and $**{CB\_HOSTNAME}** set.

```command
curl -s -XPUT -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/test_geopoint -d \
'{
  "type": "fulltext-index",
  "name": "test_geopoint",
  "sourceType": "gocbcore",
  "sourceName": "travel-sample",
  "planParams": {
    "maxPartitionsPerPIndex": 1024,
    "indexPartitions": 1
  },
  "params": {
    "doc_config": {
      "docid_prefix_delim": "",
      "docid_regexp": "",
      "mode": "scope.collection.type_field",
      "type_field": "type"
    },
    "mapping": {
      "analysis": {},
      "default_analyzer": "standard",
      "default_datetime_parser": "dateTimeOptional",
      "default_field": "_all",
      "default_mapping": {
        "dynamic": true,
        "enabled": false
      },
      "default_type": "_default",
      "docvalues_dynamic": false,
      "index_dynamic": true,
      "store_dynamic": false,
      "type_field": "_type",
      "types": {
        "_default._default": {
          "dynamic": true,
          "enabled": true,
          "properties": {
            "geo": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "include_in_all": true,
                  "index": true,
                  "name": "geo",
                  "type": "geopoint"
                }
              ]
            }
          }
        }
      }
    },
    "store": {
      "indexType": "scorch",
      "segmentVersion": 15,
      "spatialPlugin": "s2"
    }
  },
  "sourceParams": {}
}'  | jq .
```

If you successfully create the index you should a response liekt the follwoing

```json
{
  "status": "ok",
  "uuid": "274e2bf04ddc8d3e"
}
```

## [](#test-the-geopoint-index-with-a-simple-query)Test the Geopoint Index with a simple query

Request the first 10 item closet to a longitude of `-2.235143` and a latitude of `53.482358`. The target-field `geo` is specified, as is a `distance` of `100` miles: this is the radius within which target-locations must reside for their documents to be returned. Don't worry about newlines when you paste the text.

```command
curl -s -XPOST -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/test_geopoint/query \
-d '{
  "from": 0,
  "size": 10,
  "query": {
    "location": {
      "lon": -2.235143,
      "lat": 53.482358
     },
      "distance": "100mi",
      "field": "geo"
    },
  "sort": [
    {
      "by": "geo_distance",
      "field": "geo",
      "unit": "mi",
      "location": {
      "lon": -2.235143,
      "lat": 53.482358
      }
    }
  ]
}' |  jq .
```

The output of a ten (10) hits (from a total of 847 matching docs) is as follows

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
    "highlight": null,
    "fields": null,
    "facets": null,
    "explain": false,
    "sort": [
      {
        "by": "geo_distance",
        "field": "geo",
        "location": {
          "lat": 53.482358,
          "lon": -2.235143
        },
        "unit": "mi"
      }
    ],
    "includeLocations": false,
    "search_after": null,
    "search_before": null
  },
  "hits": [
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17411",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?E#9>N\f\"e"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17409",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?O~i*(kD,"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17403",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?Sg*|/t\u001f\u0002"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "hotel_17413",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?U]S\\.e\u0002_"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "hotel_17414",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?Z\u0000./\u0007Q\u0012\t"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17410",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?Z3T6 \u0010\u0019@"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17412",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?]-\u000fm?\u000b\u0014#"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17408",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?^DV7\u0014t:^"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17406",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?_<\u00009\u001eW\u0013\u0012"
      ]
    },
    {
      "index": "test_geopoint_274e2bf04ddc8d3e_4c1c5584",
      "id": "landmark_17397",
      "score": 0.025840756648257503,
      "sort": [
        " \u0001?c\u001cx\u0010n\u0016Wl"
      ]
    }
  ],
  "total_hits": 847,
  "max_score": 0.2099587543053028,
  "took": 69084563,
  "facets": null
}
```