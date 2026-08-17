---
title: "Creating a Query: Rectangle-Based"
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-geo-bounded-rectangle.adoc
  xref: xref:7.2@server:fts:fts-supported-queries-geo-bounded-rectangle.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-geo-bounded-rectangle.html)

# Creating a Query: Rectangle-Based

Note that a detailed example for Geopoint index creation and also executing queries can be found at [Geopoint Index Creation](fts-supported-queries-geopoint-spatial.md#creating%5Fa%5Fgeospatial%5Fgeopoint%5Findex) and running queries [Geopoint Radius Queries](fts-supported-queries-geopoint-spatial.md#creating%5Fgeopoint%5Frest%5Fquery%5Fradius%5Fbased).

In addition detailed information on performing queries with the Search REST API can be found in [Searching with the REST API](fts-searching-with-curl-http-requests.md); which shows how to use the full `curl` command and how to incorporate query-bodies into your cURL requests.

In the following query-body, the `top_left` of a rectangle is expressed by means of an array of two floating-point numbers, specifying a longitude of `-2.235143` and a latitude of `53.482358`. The `bottom_right` is expressed by means of key-value pairs, specifying a longitude of `28.955043` and a latitude of `40.991862`. The results are specified to be sorted on `name` alone.

```json
{
  "from": 0,
  "size": 10,
  "query": {
    "top_left": [-2.235143, 53.482358],
    "bottom_right": {
      "lon": 28.955043,
      "lat": 40.991862
     },
    "field": "geo"
  },
  "sort": [
    "name"
  ]
}
```

A subset of formatted output might appear as follows:

```json
          .
          .
          .
"hits": [
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "landmark_16144",
    "score": 0.004836809397039384,
    "sort": [
      "02"
    ]
  },
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "hotel_9905",
    "score": 0.01625607942050202,
    "sort": [
      "1"
    ]
  },
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "hotel_16460",
    "score": 0.004836809397039384,
    "sort": [
      "11"
    ]
  },
  {
    "index": "test_geopoint_610cbb5808dfd319_4c1c5584",
    "id": "hotel_21674",
    "score": 0.010011952055063241,
    "sort": [
      "17"
    ]
  },
          .
          .
          .
```