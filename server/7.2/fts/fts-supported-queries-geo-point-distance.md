---
title: "Creating a Query: Radius-Based"
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-geo-point-distance.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-supported-queries-geo-point-distance.html)

# Creating a Query: Radius-Based

Note that a detailed example for Geopoint index creation and also executing queries can be found at [Geopoint Index Creation](fts-supported-queries-geopoint-spatial.md#creating%5Fa%5Fgeospatial%5Fgeopoint%5Findex) and running queries [Geopoint Radius Queries](fts-supported-queries-geopoint-spatial.md#creating%5Fgeopoint%5Frest%5Fquery%5Fradius%5Fbased).

In addition detailed information on performing queries with the Search REST API can be found in [Searching with the REST API](fts-searching-with-curl-http-requests.md); which shows how to use the full `curl` command and how to incorporate query-bodies into your cURL requests.

The following query-body specifies a longitude of `-2.235143` and a latitude of `53.482358`. The target-field `geo` is specified, as is a `distance` of `100` miles: this is the radius within which target-locations must reside for their documents to be returned.

```json
{
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
}
```

The query contains a `sort` object, which specifies that the returned documents should be ordered in terms of their _geo\_distance_ from specified `lon` and `lat` coordinates: these values need not be identical to those specified in the `query` object.

A subset of formatted console output might appear as follows:

```json
            .
            .
            .
"hits": [
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "landmark_17411",
    "score": 0.025840756648257503,
    "sort": [
      " \u0001?E#9>N\f\"e"
    ]
  },
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "landmark_17409",
    "score": 0.025840756648257503,
    "sort": [
      " \u0001?O~i*(kD,"
    ]
  },
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "landmark_17403",
    "score": 0.025840756648257503,
    "sort": [
      " \u0001?Sg*|/t\u001f\u0002"
    ]
  },
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "hotel_17413",
    "score": 0.025840756648257503,
    "sort": [
      " \u0001?U]S\\.e\u0002_"
    ]
  },
            .
            .
            .
```