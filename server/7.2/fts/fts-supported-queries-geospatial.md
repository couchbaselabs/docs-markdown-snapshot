---
title: Geospatial Queries
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-geospatial.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-supported-queries-geospatial.adoc[]
---

[View original HTML](/server/7.2/fts/fts-supported-queries-geospatial.html)

# Geospatial Queries

> _Geospatial_ queries return documents that contain location in either legacy Geopoint format or standard GeoJSON structures. 

## [](#geopoint-type-geopoint)Geopoint (type geopoint)

Legacy or Geopoint documents which specify a geographical location.

For these queries the Search service lets users index the single dimensional geopoint/location fields and perform various bounding queries like point-distance, bounded-rectangle and bounded-polygon against the indexed geopoint field.

For higher level shapes and structures refer to GeoJSON below.

## [](#geojson-type-geojson)GeoJSON (type geojson)

For these queries the Search service supports higher dimensional spatial structures that enable the users to approximate a large variety of real life shapes like a postal or jurisdictional region boundaries, a route for a delivery vehicle or an airline career or the boundaries of various water bodies like a river, lake, stream etc..

GeoJSON is a geospatial data interchange format based on JavaScript Object Notation (JSON). It defines several types of JSON objects and the manner in which they are combined to represent data about geographic features, their properties, and their spatial extents. GeoJSON uses a geographic coordinate reference system, World Geodetic System 1984, and units of decimal degrees.

Internally the Search service supports the GeoJSON spatial data formats on [spherical geodesics](https://s2geometry.io/devguide/s2cell%5Fhierarchy.html) via S2 cells. Furthermore the Search service adheres to the GeoJSON standard [RFC 7946](https://www.rfc-editor.org/rfc/rfc7946) allows users to address query use cases like:

* Finding all the documents with any GeoJSON shapes that **contains** the spatial field of the query shape.
* Finding all the documents with any GeoJSON shapes that are **within** the spatial field of the query shape.
* Finding all the documents with any GeoJSON shapes that **intersects** the spatial field of the query shape.

The supported GeoJSON shapes in the Search service are:

* **Point** _(equivalent to a legacy Geopoint)_
* **LineString**
* **Polygon** _(equivalent to a legacy Polygon)_
* **MultiPoint**
* **MultiLineString**
* **MultiPolygon**
* **GeometryCollection**

In addition to the above shapes, Search also supports a couple of additional custom shapes to make the spatial approximations easier for users to utilize. The two extra shapes supported are:

* **Circle** _(equivalent to a legacy Radius)_
* **Envelope** _(equivalent to a legacy Rectangle)_