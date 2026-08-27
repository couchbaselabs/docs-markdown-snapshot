---
title: Creating a Legacy Index via the REST API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-index-from-REST-legacy.adoc
  xref: xref:7.2@server:fts:fts-creating-index-from-REST-legacy.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-index-from-REST-legacy.html)

# Creating a Legacy Index via the REST API

This example quickly creates the same index as [Creating a Legacy Index via the UI](fts-creating-index-from-UI-classic-editor-legacy.md#main).

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

_Note a legacy index can only work on just one keyspace <bucket\_name>.\_default.\_default._

```command
curl -s -XPUT -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/travel-sample-index -d \
'{
  "type": "fulltext-index",
  "name": "travel-sample-index",
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
      "mode": "type_field",
      "type_field": "type"
    },
    "mapping": {
      "analysis": {},
      "default_analyzer": "standard",
      "default_datetime_parser": "dateTimeOptional",
      "default_field": "_all",
      "default_mapping": {
        "dynamic": true,
        "enabled": true
      },
      "default_type": "_default",
      "docvalues_dynamic": false,
      "index_dynamic": true,
      "store_dynamic": false,
      "type_field": "_type"
    },
    "store": {
      "indexType": "scorch",
      "segmentVersion": 15
    }
  },
  "sourceParams": {}
}'  | jq .
```

If you successfully create the index you should a response liekt the follwoing

```json
{
  "status": "ok",
  "uuid": "20fcc810e312083b
}
```

## [](#test-the-legacy-index-with-a-simple-query)Test the Legacy Index with a simple query

Request the first 10 items where the content field in the collection \`travel-sample\`\_default.\_default has documents with: "view", "food", and "beach"

```command
curl -s -XPOST -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/travel-sample-index/query \
-d '{
  "query": {
    "query": "+view +food +beach"
  },
  "size": 10,
  "from": 0
}' |  jq .
```

The output of a ten (10) hits (from a total of 121 matching docs) is as follows

```json
{
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
    "highlight": null,
    "fields": null,
    "facets": null,
    "explain": false,
    "sort": [
      "-_score"
    ],
    "includeLocations": false,
    "search_after": null,
    "search_before": null
  },
  "hits": [
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "landmark_38035",
      "score": 1.1579735254455,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "landmark_4428",
      "score": 1.0216606971061395,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "landmark_26385",
      "score": 0.8510363574544033,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "hotel_6169",
      "score": 0.6627638582612397,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "hotel_15914",
      "score": 0.6488767405998539,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "hotel_15917",
      "score": 0.6408954058353277,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "hotel_35855",
      "score": 0.5994386303570878,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "hotel_21855",
      "score": 0.5876768363989866,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "hotel_21889",
      "score": 0.5815097705436758,
      "sort": [
        "_score"
      ]
    },
    {
      "index": "travel-sample-index_20fcc810e312083b_4c1c5584",
      "id": "hotel_5080",
      "score": 0.5795265708969183,
      "sort": [
        "_score"
      ]
    }
  ],
  "total_hits": 121,
  "max_score": 1.1579735254455,
  "took": 1479872,
  "facets": null
}
```