---
title: Point Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-queryshape-point.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-queryshape-point.html)

# Point Query

> A GeoJSON Point Query against any GeoJSON type. 

## [](#queryshape-for-a-point-query)QueryShape for a Point Query

A GeoJSON query via a GeoShape of Point to find GeoJSON types in a Search index using the 3 relations intersects, contains, and within.

### [](#point-intersects-query)Point `Intersects` Query

A point `intersection` query sample is given below.

```json
{
  "query": {
    "field": "<<fieldName>>",
    "geometry": {
      "shape": {
        "type": "point",
        "coordinates": [1.954764, 50.962097]
      },
      "relation": "intersects"
    }
  }
}
```

Intersection rules for the Point Query with other indexed GeoJSON shapes in the document set are given below.

| Intersects (relation)Document Shape | Point (GeoShape)                                                                                                                      |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Point                               | Matches when the query point overlaps the point in the document (as point is a non-closed shapes).                                    |
| LineString                          | Matches when the query point overlaps any of the line endpoints in the document (as linestring is a non-closed shapes).               |
| Polygon                             | Matches when the query point lies within the area of the polygon.                                                                     |
| MultiPoint                          | Matches when the query point overlaps with any of the many points in the multipoint array in the document.                            |
| MultiLineString                     | Matches when the query point overlaps with any of the linestring endpoints in the multilinestring array in the document.              |
| MultiPolygon                        | Matches when the query point lies within the area of any of the polygons in the multipolygon array in the document.                   |
| GeometryCollection                  | Matches when the query point overlaps with any of the heterogeneous (above 6) shapes in the geometrycollection array in the document. |
| Circle                              | Matches when the query point lies within the area of the circular region in the document.                                             |
| Envelope                            | Matches when the query point lies within the area of the rectangular/bounded box region in the document.                              |

### [](#point-contains-query)Point `Contains` Query

As the point is a non-closed/single spot there is no difference between `intersects` and `contains` query for this GeoShape. The guiding rules for the `contains` relation are exactly similar to that `intersects`.

A point `contains` query sample is given below.

```json
{
  "query": {
    "field": "<<fieldName>>",
    "geometry": {
      "shape": {
        "type": "point",
        "coordinates": [1.954764, 50.962097]
      },
      "relation": "contains"
    }
  }
}
```

## [](#point-within-query)Point `WithIn` Query

As the point is a non-closed shape, it is not possible for it to contain any larger shapes other than just the point itself.

A point `contains` query sample is given below.

```json
{
  "query": {
    "field": " << fieldName >> ",
    "geometry": {
      "shape": {
        "type": "point",
        "coordinates": [1.954764, 50.962097]
      },
      "relation": "within"
    }
  }
}
```

WithIn rules for the Point Query with other indexed GeoJSON shapes in the document set are given below.

| WithIn (relation)Document Shape | Point (GeoShape)                                                        |
| ------------------------------- | ----------------------------------------------------------------------- |
| Point (document shape)          | Matches when the query point is exactly the same point in the document. |

## [](#example-point-query-against-points)Example Point Query (against Points)

> [!NOTE]
> It is assumed that you your cluster has 1) a modified [travel-sample with GeoJSON data](fts-supported-queries-geojson-spatial.md#prerequisites-dataset) and 2) a Search index as per [Creating a GeoJSON Index via the REST API](fts-creating-index-from-REST-geojson.md) prior to running this example.

Matches when the query point overlaps the point in the document (as point is a non-closed shapes).

The results are specified to be sorted on `name`. Note type hotel and landmark have a name field and type airport has an airportname field all these values are analyzed as a keyword (exposed as `name`).

```command
curl -s -XPOST -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/test_geojson/query \
-d '{
  "fields": ["name"],
  "query": {
    "field": "geojson",
    "geometry": {
      "shape": {
        "type": "point",
        "coordinates": [1.954764, 50.962097]
      },
      "relation": "contains"
    }
  },
  "sort": ["name"]
}' |  jq .
```

The output of one (1) hit (from a total of 1 matching docs) is as follows

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
          "type": "point",
          "coordinates": [
            1.954764,
            50.962097
          ]
        },
        "relation": "contains"
      },
      "field": "geojson"
    },
    "size": 10,
    "from": 0,
    "highlight": null,
    "fields": [
      "name"
    ],
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
      "score": 9.234442801897503,
      "sort": [
        "Calais Dunkerque"
      ],
      "fields": {
        "name": "Calais Dunkerque"
      }
    }
  ],
  "total_hits": 1,
  "max_score": 9.234442801897503,
  "took": 10557459,
  "facets": null
}
```

## [](#example-point-query-against-circles)Example Point Query (against Circles)

> [!NOTE]
> It is assumed that you your cluster has 1) a modified [travel-sample with GeoJSON data](fts-supported-queries-geojson-spatial.md#prerequisites-dataset) and 2) a Search index as per [Creating a GeoJSON Index via the REST API](fts-creating-index-from-REST-geojson.md) prior to running this example.

Matches when the query point lies within the area of the circular region in the document.

The results are specified to be sorted on `name`. Note type hotel and landmark have a name field and type airport has an airportname field all these values are analyzed as a keyword (exposed as `name`).

```command
curl -s -XPOST -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/test_geojson/query \
-d '{
  "fields": ["name"],
  "query": {
    "field": "geoarea",
    "geometry": {
      "shape": {
        "type": "point",
        "coordinates": [1.954764, 50.962097]
      },
      "relation": "intersects"
    }
  },
  "sort": ["name"]
}' |  jq .
```

The output of one (1) hit (from a total of 1 matching docs) is as follows

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
          "type": "point",
          "coordinates": [
            1.954764,
            50.962097
          ]
        },
        "relation": "intersects"
      },
      "field": "geoarea"
    },
    "size": 10,
    "from": 0,
    "highlight": null,
    "fields": [
      "name"
    ],
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
      "score": 1.2793982619305806,
      "sort": [
        "Calais Dunkerque"
      ],
      "fields": {
        "name": "Calais Dunkerque"
      }
    }
  ],
  "total_hits": 1,
  "max_score": 1.2793982619305806,
  "took": 6334489,
  "facets": null
}
```