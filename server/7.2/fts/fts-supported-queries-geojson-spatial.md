---
title: Geospatial GeoJSON Queries
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-geojson-spatial.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-supported-queries-geojson-spatial.adoc[]
---

[View original HTML](/server/7.2/fts/fts-supported-queries-geojson-spatial.html)

# Geospatial GeoJSON Queries

> _GeoJSON_ queries return documents that contain location in either legacy Geopoint format or standard GeoJSON, thus providing more utility than that of legacy point-distance, bounded-rectangle and bounded-polygon against the indexed Geopoint fields. 

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

## [](#prerequisites-dataset)Prerequisites - Modify the travel-sample dataset

The `travel-sample` bucket, provided for test and development, DOES NOT contains any GeoJSON constructs in the documents (only legacy Geopoint information) as such you will need to modify the `travel-sample` data to work with GeoJSON.

A dataset modification can be easily accomplished via either

* Adding a new GeoJSON object(s) to your documents.
* Converting Geopoints to GeoJSON Point types in your documents.

To run the examples in this documentation the first update method **"Adding a new GeoJSON object(s) to your documents"** is needed.

* Example documents that have a geo field (airports, hotels or landmarks) such as `airport_1254` in `travel-sample._default._default`:  
```json  
{  
  "airportname": "Calais Dunkerque",  
  "city": "Calais",  
  "country": "France",  
  "faa": "CQF",  
  "geo": {  
    "alt": 12,  
    "lat": 50.962097,  
    "lon": 1.954764  
  },  
  "icao": "LFAC",  
  "id": 1254,  
  "type": "airport",  
  "tz": "Europe/Paris"  
}  
```
* **Adding a new GeoJSON object(s) (required for running the examples)**  
Using SQL++ (or SQL++) in the Query Workbench we can quickly read the "geo" objects in `travel-sample._default._default` and generate and add a new geojson object to each document. In addition the second statement will add a higher level GeoJSON (Couchbase addition to the spec) object representing a 10 mile radius around each airport (only for type=airport).  
```n1ql  
UPDATE `travel-sample`._default._default  
    SET geojson = { "type": "Point", "coordinates": [geo.lon, geo.lat] }  
    WHERE geo IS NOT null;  
UPDATE  `travel-sample`._default._default  
    SET geoarea = { "coordinates": [geo.lon, geo.lat], "type": "circle", "radius": "10mi"}  
    WHERE geo IS NOT null AND type="airport";  
```  
After running the above conversion we would get updated documents for airports like (hotels and landmarks will not have a geoarea sub-object):  
```json  
{  
  "airportname": "Calais Dunkerque",  
  "city": "Calais",  
  "country": "France",  
  "faa": "CQF",  
  "geo": {  
    "alt": 12,  
    "lat": 50.962097,  
    "lon": 1.954764  
  },  
  "geoarea": {  
    "coordinates": [
      1.954764,
      50.962097  
    ],  
    "radius": "10mi",  
    "type": "circle"  
  },  
  "geojson": {  
    "coordinates": [
      1.954764,
      50.962097  
    ],  
    "type": "Point"  
  },  
  "icao": "LFAC",  
  "id": 1254,  
  "type": "airport",  
  "tz": "Europe/Paris"  
}  
```
* **Converting Geopoints (for reference only, do not use for the examples)**  
Using SQL++ (or SQL++) in the Query Workbench we can quickly convert all top level "geo" objects in `travel-sample._default._default`  
```n1ql  
UPDATE `travel-sample`._default._default  
    SET geo.type = "Point", geo.coordinates = [geo.lon, geo.lat] WHERE geo IS NOT null;  
UPDATE `travel-sample`._default._default  
    UNSET geo.lat, geo.lon WHERE geo IS NOT null;  
```  
After running the above conversion we would get updated documents like:  
```json  
{  
  "airportname": "Calais Dunkerque",  
  "city": "Calais",  
  "country": "France",  
  "faa": "CQF",  
  "geo": {  
    "alt": 12,  
    "coordinates": [
      1.954764,
      50.962097  
    ],  
    "type": "Point"  
  },  
  "icao": "LFAC",  
  "id": 1254,  
  "type": "airport",  
  "tz": "Europe/Paris"  
}  
```

## [](#geojson-syntax)GeoJSON Syntax

As previously discussed the supported GeoJSON shapes in the Search service are:

* **Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection**

The search service follows strict GeoJSON syntax for the above seven (7) standard types:

* GeoJSON position arrays are either \[longitude, latitude\], or \[longitude, latitude, altitude\].

  * `However the Search service only supports [longitude, latitude].`
* Right-hand rule winding order as per RFC 7946 GeoJSON recommendations

  * LineString and Polygon geometries contain coordinates in an order: lines go in a certain direction, and polygon rings do too.
  * The direction of LineString often reflects the direction of something in real life: a GPS trace will go in the direction of movement, or a street in the direction of allowed traffic flows.
  * Polygon ring order is undefined in GeoJSON, but there’s a useful default to acquire: the right hand rule. Specifically this means that

    * The exterior ring should be counterclockwise.
    * Interior rings should be clockwise.

In addition to the above shapes, Search also supports a two of additional custom shapes (Couchbase specific) to make the spatial approximations easier for users to utilize:

* **Circle, and Envelope**

The search service follows its own syntax for the above two (2) custom types (see below).

## [](#supported-geojson-data-types)Supported GeoJSON Data Types

### [](#point-rfc-7946-3-1-2)Point ([RFC 7946: 3.1.2](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.2))

The following specifies a GeoJSON Point field in a document:

```json
{
 "type": "Point",
 "coordinates": [75.05687713623047,22.53539059204079]
}
```

A point is a single geographic coordinate, such as the location of a building or the current position given by any Geolocation API. Note : The standard only supports a single way of specifying the coordinates like an array format of longitude followed by latitude. i.e.: \[lng, lat\].

### [](#linestring-rfc-7946-3-1-4)Linestring ([RFC 7946: 3.1.4](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.4))

The following specifies a GeoJSON Linestring field in a document:

```json
{
   "type": "LineString",
   "coordinates": [
[ 77.01416015625, 23.0797317624497],
[ 78.134765625, 20.385825381874263]
    ]
}
```

A linestring defined by an array of two or more positions. By specifying only two points, the linestring will represent a straight line. Specifying more than two points creates an arbitrary path.

### [](#polygon-rfc-7946-3-1-6)Polygon ([RFC 7946: 3.1.6](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6))

The following specifies a GeoJSON Polygon field in a document:

```json
{
 "type": "Polygon",
 "coordinates": [ [ [ 85.605, 57.207],
                    [ 86.396, 55.998],
                    [ 87.033, 56.716],
                    [ 85.605, 57.207]
                ] ]
}
```

A polygon is defined by a list of a list of points. The first and last points in each (outer) list must be the same (i.e., the polygon must be closed). And the exterior coordinates have to be in Counter Clockwise Order in a polygon. (CCW) Polygons with holes are also supported. The holes has to follow Clockwise Order for the boundary vertices. For Polygons with a single ring, the ring cannot self-intersect NOTE: The CCW order of vertices is strictly mandated for the geoshapes in Couchbase Server and any violation of this requirement would result in unexpected search results.

### [](#multipoint-rfc-7946-3-1-3)MultiPoint ([RFC 7946: 3.1.3](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.3))

The following specifies a GeoJSON Multipoint field in a document:

```json
{
 "type": "MultiPoint",
 "coordinates": [
    [ -115.8343505859375, 38.45789034424927],
    [ -115.81237792968749, 38.19502155795575],
    [ -120.80017089843749, 36.54053616262899],
    [ -120.67932128906249, 36.33725319397006]
 ]
}
```

### [](#multilinestring-rfc-7946-3-1-5)MultiLineString ([RFC 7946: 3.1.5](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.5))

The following specifies a GeoJSON MultiLineString field in a document:

```json
{
 "type": "MultiLineString",
 "coordinates": [
    [ [ -118.31726074, 35.250105158],[ -117.509765624, 35.3756141] ],
    [ [ -118.6962890, 34.624167789],[ -118.317260742, 35.03899204] ],
    [ [ -117.9492187, 35.146862906], [ -117.6745605, 34.41144164] ]
]
}
```

### [](#multipolygon-rfc-7946-3-1-7)MultiPolygon ([RFC 7946: 3.1.7](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.7))

The following specifies a GeoJSON MultiPolygon field in a document:

```json
{
 "type": "MultiPolygon",
 "coordinates": [
    [ [ [ -73.958, 40.8003 ], [ -73.9498, 40.7968 ],
        [ -73.9737, 40.7648 ], [ -73.9814, 40.7681 ],
        [ -73.958, 40.8003 ] ] ],


    [ [ [ -73.958, 40.8003 ], [ -73.9498, 40.7968 ],
        [ -73.9737, 40.7648 ], [ -73.958, 40.8003 ] ] ]
 ]
}
```

### [](#geometrycollection-rfc-7946-3-1-8)GeometryCollection ([RFC 7946: 3.1.8](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.8))

The following specifies a GeoJSON GeometryCollection field in a document: A GeometryCollection has a member with the name "geometries". The value of "geometries" is an array. Each element of this array is a GeoJSON Geometry object. It is possible for this array to be empty.

Unlike the other geometry types described above, a GeometryCollection can be a heterogeneous composition of smaller Geometry objects. For example, a Geometry object in the shape of a lowercase roman "i" can be composed of one point and one LineString. Nested GeometryCollections are invalid.

```json
{
 "type": "GeometryCollection",
 "geometries": [
    {
      "type": "MultiPoint",
      "coordinates": [
         [ -73.9580, 40.8003 ],
         [ -73.9498, 40.7968 ],
         [ -73.9737, 40.7648 ],
         [ -73.9814, 40.7681 ]
      ]
    },
    {
      "type": "MultiLineString",
      "coordinates": [
         [ [ -73.96943, 40.78519 ], [ -73.96082, 40.78095 ] ],
         [ [ -73.96415, 40.79229 ], [ -73.95544, 40.78854 ] ],
         [ [ -73.97162, 40.78205 ], [ -73.96374, 40.77715 ] ],
         [ [ -73.97880, 40.77247 ], [ -73.97036, 40.76811 ] ]
      ]
    },
    {
      "type" : "Polygon",
      "coordinates" : [
    [ [ 0 , 0 ] , [ 3 , 6 ] , [ 6 , 1 ] , [ 0 , 0 ] ],
    [ [ 2 , 2 ] , [ 3 , 3 ] , [ 4 , 2 ] , [ 2 , 2 ] ]
    ]
   }
]
}
```

### [](#envelope-couchbase-specific-extension)Envelope (Couchbase specific extension)

Envelope type, which consists of coordinates for upper left and lower right points of the shape to represent a bounding rectangle in the format: \[\[minLon, maxLat\], \[maxLon, minLat\]\].

```json
{
    "type": "envelope",
    "coordinates": [
      [72.83, 18.979],
      [78.508, 17.4555]
    ]
}
```

### [](#circle-couchbase-specific-extension)Circle (Couchbase specific extension)

If the user wishes to cover a circular region over earth’s surface, then they could use this shape. A sample circular shape is as below.

```json
{
 "type": "circle",
 "coordinates": [75.05687713623047,22.53539059204079],
 "radius": "1000m"
}
```

Circle is specified over the center point coordinates along with the radius (or distance).

Example formats supported for radius are: "5in" , "5inch" , "7yd" , "7yards", "9ft" , "9feet", "11km", "11kilometers", "3nm" "3nauticalmiles", "13mm" , "13millimeters", "15cm", "15centimeters", "17mi", "17miles" "19m" or "19meters".

## [](#specifying-distances)Distances

Multiple unit-types can be used to express the radius (or distance) of the **Circle** type. These are listed in the table below, with the strings that specify them in REST queries.

| Units          | Specify with        |
| -------------- | ------------------- |
| inches         | in or inch          |
| feet           | ft or feet          |
| yards          | yd or yards         |
| miles          | mi or miles         |
| nautical miles | nm or nauticalmiles |
| millimeters    | mm or millimeters   |
| centimeters    | cm or centimeters   |
| meters         | m or meters         |
| kilometers     | km or kilometers    |

The integer used to specify the number of units must precede the unit-name, with no space left in-between. For example, _five inches_ can be specified either by the string `"5in"`, or by the string `"5inches"`; while _thirteen nautical miles_ can be specified as either `"13nm"` or `"13nauticalmiles"`.

If the unit cannot be determined, the entire string is parsed, and the distance is assumed to be in _meters_.

# [](#querying-the-geojson-spatial-fields)Querying the GeoJSON spatial fields

Search primarily supports three types of spatial querying capability across those heterogeneous types of geoshapes indexed this is accomplished via a JSON Query Structure.

## [](#query-structure)Query Structure:

```json
{
  "query": {
    "field": " << fieldName >> ",
    "geometry": {
      "shape": {
        "type": " << shapeDesc >> ",
        "coordinates": [[[ ]]]
      },
      "relation": " << relation >> "
    }
  }
}
```

The item **fieldName** is the indexed field to apply the Query Structure against.

The item **shapeDesc** can be any of the 9 types like Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection, Circle and Envelope.

The item **relation** can be any of the 3 types like intersects , contains and within.

| Relation   | Result                                                                  |
| ---------- | ----------------------------------------------------------------------- |
| INTERSECTS | Return all documents whose spatial field intersects the query geometry. |
| CONTAINS   | Return all documents whose spatial field contains the query geometry    |
| WITHIN     | Return all documents whose spatial field is within the query geometry.  |

## [](#sample-query-structures)Sample Query Structures

### [](#a-point-contains-query)A point `contains` query

The `contains` query for point returns all the matched documents with shapes that contain the given point in the query.

```json
{
  "query": {
  "field": "<<fieldName>>",
  "geometry": {
    "shape": {
      "type": "point",
      "coordinates": [75.05687713623047, 22.53539059204079]
    },
    "relation": "contains"
    }
  }
}
```

### [](#linestring-intersects-query)LineString `intersects` query

An `intersect` query for linestring returns all the matched documents with shapes that intersects with the linestring in the query.

```json
{
  "query": {
  "field": "<<fieldName>>",
    "geometry": {
      "shape": {
        "type": "linestring",
        "coordinates": [
          [77.01416015625, 23.079731762449878],
          [78.134765625, 20.385825381874263]
        ]
      },
      "relation": "intersects"
    }
  }
}
```

### [](#polygon-within-query)Polygon `WithIn` Query

A `within` query for polygon returns all the matched documents with shapes that are residing completely within the area of the polygon in the query.

```json
{
  "query": {
  "field": "<<fieldName>>",
    "geometry": {
      "shape": {
        "type": "polygon",
        "coordinates": [
          [
            [77.59012699127197, 12.959853852513307],
            [77.59836673736572, 12.959853852513307],
            [77.59836673736572, 12.965541604118611],
            [77.59012699127197, 12.965541604118611],
            [77.59012699127197, 12.959853852513307]
          ]
        ]
      },
      "relation": "within"
    }
  }
}
```

## [](#detailed-geojson-examples)Detailed examples for every QueryShape:

The Sample Query Structures above just introduces some of the basic QueryShapes, the full list below covers the nine (9) unique QueryShapes utilizes each of them to query 1) a set of GeoJSON points and 2) a set of GeoJSON area shapes in this case Circles (but the "area shapes" could be anything):

* [Point Query](fts-queryshape-point.md)
* [LineString Query](fts-queryshape-linestring.md)
* [Polygon Query](fts-queryshape-polygon.md)
* [MultiPoint Query](fts-queryshape-multipoint.md)
* [MultiLineString Query](fts-queryshape-multilinestring.md)
* [MultiPolygon Query](fts-queryshape-multipolygon.md)
* [GeometryCollection Query](fts-queryshape-geometrycollection.md)
* [Circle Query](fts-queryshape-circle.md)
* [Envelope Query](fts-queryshape-envelope.md)

## [](#creating%5Fa%5Fgeojson%5Findex)Creating a Geospatial Index (type geojson)

To be successful, a geospatial GeoJSON query must reference an index that applies the _geojson_ type mapping to the field containing any of the standard types **Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, and GeometryCollection** plus the extended types of **Circle and Envelope**.

This can be achieved with Couchbase Web Console, or with the REST endpoints provided for managing [Indexes](../rest-api/rest-fts-indexing.md). Detailed instructions for setting up indexes, and specifying type mappings, are provided in [Creating Indexes](fts-creating-indexes.md).

> [!NOTE]
> For initial experimentation with geospatial GeoJSON querying (based on the type geojson), the `travel-sample._default._default` must updated as per [Prerequisites for GeoJSON Search](#prerequisites-dataset) to ensure your dataset contains GeoJSON objects that can be indexed.

* Click the **Add Index** link in the upper right of the **Couchbase Web Console** \> **Search** page.  
![fts add initial](_images/fts-add-initial.png)
* To define any index on which Full Text Search a unique name for the index in the **Index Name** field, on the upper-left. Note that only alphanumeric characters, hyphens, and underscores are allowed for index names and the first character of the name must be alphabetic.  
Enter **test\_geopoint** as the name of the Search index you are creating in the **Index Name** text-box.  
![fts index name geojson](_images/fts-index-name-geojson.png)
* Select the bucket **travel-sample** from the **Bucket** pull-down menu.  
Use the pull-down menu provided for the Bucket field, on the upper-right, and select a bucket that you are allowed to access to via the cluster’s RBAC settings.  
![fts index name and bucket geojson](_images/fts-index-name-and-bucket-geojson.png)
* Select the checkbox **\[X\] Use non-default scope/collections**  
This allows your index to stream mutations from one or more non-default collections under the selected bucket and scope.  
![fts select geojson scope collections](_images/fts-select-geojson-scope-collections.png)
* You will see a newly visible pull-down menu provided for the **Scope** field, under the **\[X\] Use non-default scope/collections** checkbox, and select a bucket that you are allowed to access to via the cluster’s RBAC settings.  
For this example leave the setting as **\_default** which is used to migrate bucket based data into the collections paradigm.
* Under **Type Mapings**, unselect the checkbox **\[ \] default | dynamic**.  
This is required as this type mapping (the default mapping) is only valid for the <bucket>.\_default.\_default which is typically used to upgrade a 6.X server from a bucket into a more powerful collections paradigm. In this example we will do the equivalent but on a per collections basis.  
![fts uncheck default mapping](_images/fts-uncheck-default-mapping.png)
* Click on the button **\+ Add Type Mapping**

  * A new section with a **Collection** pull-down, **Analyzer** pull-down and a **\[ \] only index specified fields** checkbox will appear.  
  ![fts index menu1 nondefault empty](_images/fts-index-menu1-nondefault-empty.png)
  * Select **\_default** from the **Collection** pull-down, note the pull down will change to a text field prefilled with **\_default.\_default**  
  ![fts index menu1 geopoint filled](_images/fts-index-menu1-geopoint-filled.png)
  * Leave the **\[ \] only index specified fields** checkbox blank or unset.  
  This will index all fields in the scope **\_default** collection **\_default**, however not this is not recommended for large production datasets.
  * Click on the blue **ok** at the right of the section to save this mapping.
  * Hover over your newly created/saved row
  * Click on the blue **+** button the right side of the row.  
  ![fts index menu1 geopoint hover](_images/fts-index-menu1-geopoint-hover.png)
  * A context menu of "insert child mapping" (for sub-objects) and "insert child field" (for properties) will appear.  
  ![fts index menu2 geopoint empty](_images/fts-index-menu2-geopoint-empty.png)
  * Select **insert child field**
  * another row menu will appear with the following controls: "field", "type", "text", "searchable as", "analyzer" "inherit", "index", "store", "include in \_all field", "include term vectors", and "docvalues".  
  ![fts index menu2 geojson filled](_images/fts-index-menu2-geojson-filled.png)
  * Set the text box **field** to **geojson**, this will also update "searchable as" to **geojson**.
  * Change the pull-down **type** to **geoshape**.  
  By configuring the child field information form, specifically identify the object **geo** as type **geopoint** this will tell the Search indexer to recognize top level sub-objects like:  
  ```json  
    "geojson": {  
      "coordinates": [
      1.954764,
      50.962097  
      ],  
      "type": "Point"  
    },  
  ```
  * Check **\[X\]** the boxes "store" and "include in \_all field"
  * Click on the blue **ok** at the right of the section to save this sub-form.  
  ![fts index menu2 geojson filled](_images/fts-index-menu2-geojson-filled.png)
  * Hover again over the row # \_default.\_default | dynamic
  * Click on the blue **+** button the right side of the row.  
  ![fts index menu1a geojson hover](_images/fts-index-menu1a-geojson-hover.png)
  * A context menu of "insert child mapping" (for sub-objects) and "insert child field" (for properties) will appear.  
  ![fts index menu2a geojson empty](_images/fts-index-menu2a-geojson-empty.png)
  * Select **insert child field**
  * another row menu will appear with the following controls: "field", "type", "text", "searchable as", "analyzer" "inherit", "index", "store", "include in \_all field", "include term vectors", and "docvalues".  
  ![fts index menu2a geojson filled](_images/fts-index-menu2a-geojson-filled.png)
  * Set the text box **field** to **geoarea**, this will also update "searchable as" to **geoarea**.
  * Change the pull-down **type** to **geoshape**.  
  By configuring the child field information form, specifically identify the object **geo** as type **geopoint** this will tell the Search indexer to recognize top level sub-objects like:  
  ```json  
    "geoarea": {  
      "coordinates": [
      1.954764,
      50.962097  
      ],  
      "radius": "10mi",  
      "type": "circle"  
    },  
  ```
  * Check **\[X\]** the boxes "store" and "include in \_all field"
  * Click on the blue **ok** at the right of the section to save this sub-form.  
  ![fts index menu2a geojson filled](_images/fts-index-menu2a-geojson-filled.png)
* Save your index, left-click on the **Create Index** button near the bottom of the screen.  
This is all you need to specify in order to create a more advanced index for test and development. No further configuration is required.  
![fts index create button](_images/fts-index-create-button.png)
* If you subsequently Edit your Index it should look like the following:  
![fts edit index geojson](_images/fts-edit-index-geojson.png)

> [!NOTE]
> Indexing all fields as above indexes across all fields is not recommended for production environments since it creates indexes that may be unnecessarily large, and therefore insufficiently performant. However this index can be edited and optimized if you check **\[X\] only index specified fields** under the Type Mappings section. This will result in a much smaller index and a faster index build since only the fields **geojson** and **geoarea** will be indexed in the set of documents.

The index once created can also be accessed by means of the Search REST API see [Searching with the REST API](fts-searching-with-curl-http-requests.md). Furthermore the index could have been created in the first place via the Search REST API see [Index Creation with REST API](fts-creating-index-with-rest-api.md) for more information on using the Search REST API syntax.

## [](#creating%5Fgeojson%5Frest%5Fquery%5Fradius%5Fbased)Creating a Query: Radius-Based

This section and those following, provide examples of the query-bodies required to make geospatial queries with the Couchbase REST API. Note that more detailed information on performing queries with the Couchbase REST API can be found in [Searching with the REST API](fts-searching-with-curl-http-requests.md); which shows how to use the full `curl` command and how to incorporate query-bodies into it.

The following query-body specifies a longitude of `-2.235143` and a latitude of `53.482358`. The target-field `geo` is specified, as is a `distance` of `100` miles: this is the radius within which target-locations must reside for their documents to be returned.

```json
{
  "query": {
    "geometry": {
      "shape": {
        "coordinates": [
          -2.235143,
          53.482358
        ],
        "type": "circle",
        "radius": "100mi"
      },
      "relation": "within"
    },
    "field": "geojson"
  },
  "size": 10,
  "from": 0,
  "sort": [
    {
      "by": "geo_distance",
      "field": "geojson",
      "unit": "mi",
      "location": {
        "lon": -2.235143,
        "lat": 53.482358
      }
    }
  ]
}
```

The above query contains a `sort` object, which specifies that the returned documents should be ordered in terms of their _geo\_distance_ from specified `lon` and `lat` coordinates: these values need not be identical to those specified in the `query` object.

![fts geojson search 01](_images/fts-geojson-search_01.png) 

You can cut-n-paste the above Search body definition into the text area that says "search this index…​"

![fts geojson search 02](_images/fts-geojson-search_02.png) 

Once pasted hit the **Search** button and the UI will show the first 10 hits

![fts geojson search 03](_images/fts-geojson-search_03.png) 

The console allows searches performed via the UI to be translated dynamically into cURL examples. To create a cURL command to do this first check **\[X\] show advanced query settings** and then check **\[X\] show command-line query example**.

You should have a cURL command similar to the following:

```console
curl -XPOST -H "Content-Type: application/json" \
-u <username>:<password> http://192.168.3.150:8094/api/index/test_geojson/query \
-d '{
  "query": {
    "geometry": {
      "shape": {
        "coordinates": [
          -2.235143,
          53.482358
        ],
        "type": "circle",
        "radius": "100mi"
      },
      "relation": "within"
    },
    "field": "geojson"
  },
  "size": 10,
  "from": 0,
  "sort": [
    {
      "by": "geo_distance",
      "field": "geojson",
      "unit": "mi",
      "location": {
        "lon": -2.235143,
        "lat": 53.482358
      }
    }
  ]
}'
```

If you copy and then run the above cURL command via the console the response from the Search service will report that there are 847 total\_hits but only return the first 10 hits. A subset of formatted console output might appear as follows:

> [!NOTE]
> To pretty print the response just pipe the output through the utility [jq](http://stedolan.github.io/jq) to enhance readability.

```json
"hits": [
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "landmark_3604",
    "score": 0.21532348857041025,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "landmark_5571",
    "score": 0.12120554320433605,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "landmark_3577",
    "score": 0.2153234885704102,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "hotel_3606",
    "score": 0.2153234885704102,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "landmark_40167",
    "score": 0.27197802451106445,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "landmark_36152",
    "score": 0.12120554320433605,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "landmark_11329",
    "score": 0.12120554320433605,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "hotel_3643",
    "score": 0.2153234885704102,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "landmark_40038",
    "score": 0.27197802451106445,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  },
  {
    "index": "test_geojson_690ac8f8179a4a86_4c1c5584",
    "id": "airport_565",
    "score": 0.12120554320433605,
    "sort": [
      " \u0001\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f\u007f"
    ]
  }
]
```

## [](#creating%5Fgeojson%5Frest%5Fquery%5Fbounding%5Fbox%5Fbased)Creating a Query: Envelope (or Rectangle-Based)

In the following query-body, the `top_left` of a rectangle is expressed by means of an **Envelope**, specifying \[\[minLon, maxLat\], \[maxLon, minLat\]\] = \[\[-2.235143, 53.482358\],\[28.955043, 40.991862\]\]

The results are specified to be sorted on `name` alone, since only type hotel and landmark have a name the sort will occur on the tokenized values (they analyzer would need to be type keyword to sort on the actual field names).

```json
{
  "query": {
    "geometry": {
      "shape": {
        "coordinates": [
          [-2.235143, 53.482358],
          [28.955043, 40.991862]
        ],
        "type": "envelope"
      },
      "relation": "within"
    },
    "field": "geojson"
  },
  "sort": ["name"],
  "size": 10,
  "from": 0
}
```

A subset of formatted output might appear as follows:

```json
"hits": [
  {
    "index": "test_geojson_3dd53eb1ac88768c_4c1c5584",
    "id": "landmark_3604",
    "score": 0.004703467956838207,
    "sort": [
      "ô¿¿ô¿¿ô¿¿"
    ]
  },
  {
    "index": "test_geojson_3dd53eb1ac88768c_4c1c5584",
    "id": "landmark_6067",
    "score": 0.004703467956838207,
    "sort": [
      "ô¿¿ô¿¿ô¿¿"
    ]
  },
  {
    "index": "test_geojson_3dd53eb1ac88768c_4c1c5584",
    "id": "landmark_16320",
    "score": 0.004703467956838207,
    "sort": [
      "ô¿¿ô¿¿ô¿¿"
    ]
  },
```

If we added two (2) more child field into the Index definition as follows where both items are searchable as "name"

![fts geojson mod index](_images/fts-geojson-mod-index.png) 

The sort would be on the actual airportname and name fields and the query itself would return these values.

```json
"hits": [
  {
    "index": "test_geojson_4391b0a68d5cc865_4c1c5584",
    "id": "hotel_1364",
    "score": 0.05896334942635901,
    "sort": [
      "'La Mirande Hotel"
    ]
  },
  {
    "index": "test_geojson_4391b0a68d5cc865_4c1c5584",
    "id": "landmark_16144",
    "score": 0.004703467956838207,
    "sort": [
      "02 Shepherd's Bush Empire"
    ]
  },
  {
    "index": "test_geojson_4391b0a68d5cc865_4c1c5584",
    "id": "landmark_16181",
    "score": 0.004703467956838207,
    "sort": [
      "2 Willow Road"
    ]
  },
  {
    "index": "test_geojson_4391b0a68d5cc865_4c1c5584",
    "id": "landmark_16079",
    "score": 0.004703467956838207,
    "sort": [
      "20 Fenchurch Street"
    ]
  },
```

## [](#creating%5Fgeojson%5Frest%5Fquery%5Fpolygon%5Fbased)Creating a Query: Polygon-Based

The following query-body uses an array, each of whose elements is a string, containing multiple floating-point number pairs; to specify the longitude and latitude of each of the lon/lat pairs of a polygon — known as _polygon points_. In all cases, the `lon` floating-point value precedes the `lat` for the correct GeoJSON winding.

Here, the last-specified pair in the array is identical to the initial pair, thus explicitly closing the polygon. However, specifying an explicit closure in this way is optional: closure will be inferred by Couchbase Server if not explicitly specified.

If a target data-location falls within the polygon, its document is returned.

Request the first 10 items within the state of Utah (note the query body consists of simple set of hand drawn set of corner points). The target-field `geojson` is specified, to be compared to the query Polygon the target-locations must reside for their documents to be returned. Don’t worry about newlines when you paste the text.

The results are specified to be sorted on `name` alone, since only type hotel and landmark have a name the sort will occur on the tokenized values (they analyzer would need to be type keyword to sort on the actual field names).

```json
{
  "query": {
    "geometry": {
      "shape": {
        "coordinates": [
          [
            [-114.027099609375, 42.00848901572399],
            [-114.04907226562499, 36.99377838872517],
            [-109.05029296875, 36.99377838872517],
            [-109.05029296875, 40.98819156349393],
            [-111.060791015625, 40.98819156349393],
            [-111.02783203125, 42.00848901572399],
            [-114.027099609375, 42.00848901572399]
          ]
        ],
        "type": "Polygon"
      },
      "relation": "within"
    },
    "field": "geojson"
  },
  "size": 10,
  "from": 0,
  "sort": ["name"]
}
```

A subset of formatted output might appear as follows:

```json
"hits": [
  {
    "index": "test_geojson_4330cb585620d5e8_4c1c5584",
    "id": "airport_7857",
    "score": 0.27669394470240527,
    "sort": [
      "ô¿¿ô¿¿ô¿¿"
    ]
  },
  {
    "index": "test_geojson_4330cb585620d5e8_4c1c5584",
    "id": "airport_7581",
    "score": 0.13231342774148913,
    "sort": [
      "ô¿¿ô¿¿ô¿¿"
    ]
  },
  {
    "index": "test_geojson_4330cb585620d5e8_4c1c5584",
    "id": "airport_7727",
    "score": 0.27669394470240527,
    "sort": [
      "ô¿¿ô¿¿ô¿¿"
    ]
  },
  {
    "index": "test_geojson_4330cb585620d5e8_4c1c5584",
    "id": "airport_9279",
    "score": 0.27669394470240527,
    "sort": [
      "ô¿¿ô¿¿ô¿¿"
    ]
  },
```

Again if we added two (2) more child field into the Index definition as follows where both items are searchable as "name"

![fts geojson mod index](_images/fts-geojson-mod-index.png) 

The sort would be on the actual airportname and name fields (but there are only airports returned) and the query itself would return these values.

```json
"hits": [
  {
    "index": "test_geojson_4391b0a68d5cc865_4c1c5584",
    "id": "airport_6999",
    "score": 0.13231342774148913,
    "sort": [
      "Brigham City"
    ]
  },
  {
    "index": "test_geojson_4391b0a68d5cc865_4c1c5584",
    "id": "airport_7857",
    "score": 0.27669394470240527,
    "sort": [
      "Bryce Canyon"
    ]
  },
  {
    "index": "test_geojson_4391b0a68d5cc865_4c1c5584",
    "id": "airport_7074",
    "score": 0.13231342774148913,
    "sort": [
      "Canyonlands Field"
    ]
  },
```

This example quickly creates the same index as [Creating a GeoJSON Index via the REST API](fts-creating-index-from-REST-geojson.md). Note it has the two (2) additional child field definitions to allow keyword sorting.

## [](#final-geojson-index)Final GeoJSON Search index

Note, for the samples above that return actual airportname and name fields and also the nine (9) QueryShape examples referenced in [Detailed examples for every QueryShape](#detailed-geojson-examples)

the Search index used is as follows:

```json
{
  "type": "fulltext-index",
  "name": "test_geojson",
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
            "airportname": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "analyzer": "keyword",
                  "include_in_all": true,
                  "index": true,
                  "name": "name",
                  "store": true,
                  "type": "text"
                }
              ]
            },
            "geoarea": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "include_in_all": true,
                  "index": true,
                  "name": "geoarea",
                  "type": "geoshape"
                }
              ]
            },
            "geojson": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "include_in_all": true,
                  "index": true,
                  "name": "geojson",
                  "type": "geoshape"
                }
              ]
            },
            "name": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "analyzer": "keyword",
                  "include_in_all": true,
                  "index": true,
                  "name": "name",
                  "store": true,
                  "type": "text"
                }
              ]
            }
          }
        }
      }
    },
    "store": {
      "indexType": "scorch",
      "segmentVersion": 15
    }
  },
  "sourceParams": {}
}
```

If viewed in the UI:

![fts geojson mod index full](_images/fts-geojson-mod-index-full.png)