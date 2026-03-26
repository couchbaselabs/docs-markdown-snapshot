---
title: MultiPoint Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-queryshape-multipoint.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:fts:fts-queryshape-multipoint.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-queryshape-multipoint.html)

# MultiPoint Query

> A GeoJSON MultiPoint Query against any GeoJSON type. 

## [](#queryshape-for-a-multipoint-query)QueryShape for a MultiPoint Query

A GeoJSON query via a GeoShape of MultiPoint to find GeoJSON types in a Search index using the 3 relations intersects, contains, and within.

### [](#multipoint-intersects-query)MultiPoint `Intersects` Query

An `intersect` query for multipoint returns all the matched documents with shapes that overlap any of the multiple points in the multipoint array within the query.

A multipoint `intersection` query sample is given below.

```json
{
  "query": {
    "field": "<<fieldName>>",
    "geometry": {
      "shape": {
        "type": "MultiPoint",
        "coordinates": [
          [1.954764, 50.962097],
          [3.029578, 49.868547]
        ]
      },
      "relation": "intersects"
    }
  }
}
```

Intersection rules for the MultiPoint Query with other indexed GeoJSON shapes in the document set are given below.

| Intersects (relation)Document Shape | MultiPoint (GeoShape)                                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Point                               | Intersects when any of the query points overlaps the point in the document. (as point is a non-closed shapes)                                    |
| LineString                          | Intersects when any of the query points overlaps with any of the line endpoints in the document.(as linestring is a non-closed shapes)           |
| Polygon                             | Intersects when any of the query points lies within the area of the polygon.                                                                     |
| MultiPoint                          | Intersects when any of the query points overlaps with any of the many points in the multipoint array in the document.                            |
| MultiLineString                     | Intersects when any of the query points overlaps with any of the linestring endpoints in the multilinestring array in the document.              |
| MultiPolygon                        | Intersects when any of the query points lies within the area of any of the polygons in the multipolygon array in the document.                   |
| GeometryCollection                  | Intersects when any of the query points overlaps with any of the heterogeneous (above 6) shapes in the geometrycollection array in the document. |
| Circle                              | Intersects when any of the query points lies within the area of the circular region in the document.                                             |
| Envelope                            | Intersects when any of the query points lies within the area of the rectangular/bounded box region in the document.                              |

### [](#multipoint-contains-query)MultiPoint `Contains` Query

A `contains` query for multipoint returns all the matched documents with shapes that contain the multipoint within the query.

A multipoint `contains` query sample is given below.

```json
{
  "query": {
    "field": "<<fieldName>>",
    "geometry": {
      "shape": {
        "type": "MultiPoint",
        "coordinates": [
          [1.954764, 50.962097],
          [3.029578, 49.868547]
        ]
      },
      "relation": "contains"
    }
  }
}
```

Containment rules for the MultiPoint Query with other indexed GeoJSON shapes in the document set are given below.

| Contains (relation)Document Shape | MultiPoint (GeoShape)                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Point                             | NA. A point can't contain a multipoint.                                                                                                                               |
| LineString                        | NA. A linestring can't contain a multipoint.                                                                                                                          |
| Polygon                           | Contains when all of the query points in the multipoint array lie within the area of the polygon.                                                                     |
| MultiPoint                        | Contains when all of the query points in the multipoint array overlap with any of the many points in the multipoint array in the document.                            |
| MultiLineString                   | NA. A multi linestring can't contain a multipoint.                                                                                                                    |
| MultiPolygon                      | Contains when all of the query points in the multipoint array lie within the area of any of the polygons in the multipolygon array in the document.                   |
| GeometryCollection                | Contains when all of the query points in the multipoint array overlap with any of the heterogeneous (above 6) shapes in the geometrycollection array in the document. |
| Circle                            | Contains when all of the query points in the multipoint array lie within the area of the circular region in the document.                                             |
| Envelope                          | Contains when all of the query points in the multipoint array lie within the area of the rectangular/bounded box region in the document.                              |

### [](#multipoint-within-query)MultiPoint `WithIn` Query

The Within query is not supported by line geometries.

A `within` query for multipoint returns all the matched documents with shapes that contain the multipoint within the query.

A multipoint `contains` query sample is given below.

```json
{
  "query": {
    "field": "<<fieldName>>",
    "geometry": {
      "shape": {
        "type": "MultiPoint",
        "coordinates": [
          [1.954764, 50.962097],
          [3.029578, 49.868547]
        ]
      },
      "relation": "within"
    }
  }
}
```

WithIn rules for the MultiPoint Query with other indexed GeoJSON shapes in the document set are given below.

| Contains (relation)Document Shape | MultiPoint (GeoShape)                                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Point                             | Matches when any of the query points in the multipoint array overlap with the geo points in the document.                                 |
| LineString                        | NA.                                                                                                                                       |
| Polygon                           | NA                                                                                                                                        |
| MultiPoint                        | Matches when all of the query points in the multipoint array overlap with any of the many points in the multipoint array in the document. |
| MultiLineString                   | NA                                                                                                                                        |
| MultiPolygon                      | NA                                                                                                                                        |
| GeometryCollection                | NA                                                                                                                                        |
| Circle                            | NA                                                                                                                                        |
| Envelope                          | NA                                                                                                                                        |

## [](#example-multipoint-query-against-points)Example MultiPoint Query (against Points)

> [!NOTE]
> It is assumed that you your cluster has 1) a modified [travel-sample with GeoJSON data](fts-supported-queries-geojson-spatial.md#prerequisites-dataset) and 2) a Search index as per [Creating a GeoJSON Index via the REST API](fts-creating-index-from-REST-geojson.md) prior to running this example.

Matches when any of the query points in the multipoint array overlap with the geo points in the document.

The results are specified to be sorted on `name`. Note type hotel and landmark have a name field and type airport has an airportname field all these values are analyzed as a keyword (exposed as `name`).

```command
curl -s -XPOST -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/test_geojson/query \
-d '{
  "query": {
    "field": "geojson",
    "geometry": {
      "shape": {
        "type": "MultiPoint",
        "coordinates": [
          [1.954764, 50.962097],
          [3.029578, 49.868547]
        ]
      },
      "relation": "within"
    }
  },
  "size": 5,
  "from": 0,
  "sort": ["name"]
}' |  jq .
```

The output of two (2) hits (from a total of 2 matching docs) is as follows

```json
{
  "status": {
    "total": 1,
    "failed": 0,
    "successful": 1
  },
  "request": {
    "query": {
      "geometry": {
        "shape": {
          "type": "MultiPoint",
          "coordinates": [
            [
              1.954764,
              50.962097
            ],
            [
              3.029578,
              49.868547
            ]
          ]
        },
        "relation": "within"
      },
      "field": "geojson"
    },
    "size": 5,
    "from": 0,
    "highlight": null,
    "fields": null,
    "facets": null,
    "explain": false,
    "sort": [
      "name"
    ],
    "includeLocations": false,
    "search_after": null,
    "search_before": null
  },
  "hits": [
    {
      "index": "test_geojson_3397081757afba65_4c1c5584",
      "id": "airport_1254",
      "score": 3.5287254429876733,
      "sort": [
        "Calais Dunkerque"
      ]
    },
    {
      "index": "test_geojson_3397081757afba65_4c1c5584",
      "id": "airport_1255",
      "score": 3.5326647348568896,
      "sort": [
        "Peronne St Quentin"
      ]
    }
  ],
  "total_hits": 2,
  "max_score": 3.5326647348568896,
  "took": 10149092,
  "facets": null
}
```

## [](#example-multipoint-query-against-circles)Example MultiPoint Query (against Circles)

> [!NOTE]
> It is assumed that you your cluster has 1) a modified [travel-sample with GeoJSON data](fts-supported-queries-geojson-spatial.md#prerequisites-dataset) and 2) a Search index as per [Creating a GeoJSON Index via the REST API](fts-creating-index-from-REST-geojson.md) prior to running this example.

Intersects when any of the query points lies within the area of the circular region in the document.

The results are specified to be sorted on `name`. Note type hotel and landmark have a name field and type airport has an airportname field all these values are analyzed as a keyword (exposed as `name`).

```command
curl -s -XPOST -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/test_geojson/query \
-d '{
  "query": {
    "field": "geoarea",
    "geometry": {
      "shape": {
        "type": "MultiPoint",
        "coordinates": [
          [1.954764, 50.962097],
          [3.029578, 49.868547]
        ]
      },
      "relation": "intersects"
    }
  },
  "size": 5,
  "from": 0,
  "sort": ["name"]
}' |  jq .
```

The output of two (2) hits (from a total of 2 matching docs) is as follows

```json
{
  "status": {
    "total": 1,
    "failed": 0,
    "successful": 1
  },
  "request": {
    "query": {
      "geometry": {
        "shape": {
          "type": "MultiPoint",
          "coordinates": [
            [
              1.954764,
              50.962097
            ],
            [
              3.029578,
              49.868547
            ]
          ]
        },
        "relation": "intersects"
      },
      "field": "geoarea"
    },
    "size": 5,
    "from": 0,
    "highlight": null,
    "fields": null,
    "facets": null,
    "explain": false,
    "sort": [
      "name"
    ],
    "includeLocations": false,
    "search_after": null,
    "search_before": null
  },
  "hits": [
    {
      "index": "test_geojson_3397081757afba65_4c1c5584",
      "id": "airport_1254",
      "score": 0.490187283157727,
      "sort": [
        "Calais Dunkerque"
      ]
    },
    {
      "index": "test_geojson_3397081757afba65_4c1c5584",
      "id": "airport_1255",
      "score": 0.7869533596268505,
      "sort": [
        "Peronne St Quentin"
      ]
    }
  ],
  "total_hits": 2,
  "max_score": 0.7869533596268505,
  "took": 7023893,
  "facets": null
}
```