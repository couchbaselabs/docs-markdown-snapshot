---
title: Geospatial Geopoint Queries
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-geopoint-spatial.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-supported-queries-geopoint-spatial.html)

# Geospatial Geopoint Queries

> _Geospatial_ geopoint queries return documents that contain location. Each document specifies a geographical location. 

A _geospatial geopoint query_ specifies an area and returns each document that contains a reference to a location within the area. Areas and locations are represented by _latitude_\-_longitude_ coordinate pairs.

The location data provided by a geospatial geopoint query can be any of the following:

* A location, is specified as a longitude-latitude coordinate pair; and a distance. The location determines the center of a circle whose radius-length is the specified distance. Documents are returned if they reference a location within the circle. For details of the units and formats in which distances can be specified, see [Specifying Distances](#specifying-distances).
* Two latitude-longitude coordinate pairs. These are respectively taken to indicate the top left and bottom right corners of a _rectangle_. Documents are returned if they reference a location within the area of the rectangle.
* An array of three or more latitude-longitude coordinate pairs. Each of the pairs is taken to indicate one corner of a _polygon_. Documents are returned if they reference a location within the area of the polygon.

A geospatial geopoint query must be applied to an index that uses the _geopoint_ type mapping to the document-field that contains the target longitude-latitude coordinate pair.

To be successful, a geospatial geopoint query must reference an index within which the _geopoint_ type mapping has been applied to the field containing the target latitude-longitude coordinate pair.

Geospatial queries return _all_ documents whose locations are within the query-specified area. To specify _holes_ within the area so that one or more subsets of returned documents can be omitted from the final results, boolean queries should be applied to the set of documents returned by the geospatial geopoint query. See [Supported Queries](fts-supported-queries.md).

Latitude-longitude coordinate pairs can be specified in multiple ways, including as _geohashes_; as demonstrated in [Specifying Coordinates](#specifying-coordinates), below.

## [](#recognizing%5Ftarget%5Fdata)Recognizing Target Data

The `travel-sample` bucket, provided for test and development, contains multiple documents that specify locations. For example, those that represent airports, such as `airport_1254`:

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

The `geo` field contains the `lon` and `lat` key-value pairs. Note that the `geo` field needs to contain the longitude-latitude information in the form of a string (comma separated numeric content or a hash), array, or object.

* String syntax: `"lat,lon"`, `"geohash"`
* Array syntax: `[lon, lat]` (where lon and lat are both floating point integers)
* Object syntax: `{"lon" : 0.0, "lat": 0.0}`, `{"lng": 0.0, "lat": 0.0}` (note that these are the only accepted field names for longitude and latitude)

Moreover, any other child-fields, such as `alt` (in the above example) - are ignored.

For information on installing the `travel-sample` bucket, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).

### [](#specifying-coordinates)Specifying Coordinates

Each latitude-longitude coordinate can be expressed by means of any of the following.

#### [](#two-key-value-pairs)Two Key-Value Pairs

An individual latitude-longitude coordinate can be expressed by means of an object containing two key-value pairs. For example, the central location for a radius-based area can be expressed as follows:

```json
"location": {
       "lon": -2.235143,
       "lat": 53.482358
     }
```

Where multiple coordinates are required, for the specifying of a polygon, an array of such objects can be specified, as follows:

```json
"polygon_points": [
  { “lat”: 37.79393211306212, “lon”: -122.44234633404847 },
  { “lat”: 37.77995881733997, “lon”: -122.43977141339417 },
  { “lat”: 37.788031092020155, “lon”: -122.4292571540557 },
  { “lat”: 37.79026946582319, “lon”: -122.41149020154114 },
  { “lat”: 37.79571192027403, “lon”: -122.40735054016113 },
  { “lat”: 37.79393211306212, “lon”: -122.44234633404847 }
]
```

#### [](#a-string-containing-two-floating-point-numbers)A String, Containing Two Floating-Point Numbers

An individual latitude-longitude coordinate can be expressed as a string containing two floating-point numbers — the first signifying latitude, the second longitude. For example, the center of a circle can be specified as follows:

```json
"location": "53.482358,-2.235143"
```

Where multiple coordinates are required, for the specifying of a polygon, an array of such strings can be specified, as follows:

```json
"polygon_points": [
  "37.79393211306212,-122.44234633404847",
  "37.77995881733997,-122.43977141339417",
  "37.788031092020155,-122.42925715405579",
  "37.79026946582319,-122.41149020154114",
  "37.79571192027403,-122.40735054016113",
  "37.79393211306212,-122.44234633404847"
]
```

#### [](#an-array-of-floating-point-numbers)An Array of Two Floating-Point Numbers

An individual latitude-longitude coordinate can be expressed as an array of two floating-point numbers — the first signifying longitude, the second latitude. For example, the top left corner of a rectangle can be specified as follows:

```javascript
"top_left": [ -2.235143, 53.482358 ]
```

Where multiple coordinates are required, for the specifying of a polygon, an array of such arrays can be specified, as follows:

```json
"polygon_points": [
  [ -122.44234633404847, 37.79393211306212 ],
  [ -122.43977141339417, 37.77995881733997 ],
  [ -122.42925715405579, 37.78803109202015 ],
  [ -122.41149020154114, 37.79026946582319 ],
  [ -122.40735054016113, 37.79571192027403 ],
  [ -122.44234633404847, 37.79393211306212 ]
]
```

#### [](#a-geohash)A Geohash

A latitude-longitude coordinate can be expressed by means of a single [Geohash](https://en.wikipedia.org/wiki/Geohash) encoding. For example, the bottom right corner of a rectangle can be specified as follows:

```json
"bottom_right": "gcw2m0hmm6hs"
```

Where multiple coordinates are required, for the specifying of a polygon, an array of geohashes can be specified, as follows:

```json
"polygon_points": [
  “9q8zjbkp”,
  “9q8yvvdh”,
  “9q8yyp1e”,
  “9q8yyrw8”,
  “9q8zn83x”,
  “9q8zjb0j”
]
```

Means of latitude-longitude conversion to and from this format are provided at [Geohash Converter](http://geohash.co/). Additional information, including on the _precision_ of values specified in this format, is provided at [Movable Type Scripts — Geohashes](https://www.movable-type.co.uk/scripts/geohash.html).

### [](#specifying-distances)Specifying Distances

Multiple unit-types can be used to express distance. These are listed in the table below, with the strings that specify them in REST queries.

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

## [](#creating%5Fa%5Fgeospatial%5Fgeopoint%5Findex)Creating a Geospatial Index (type geopoint)

To be successful, a geospatial geopoint query must reference an index that applies the _geopoint_ type mapping to the field containing the latitude-longitude coordinate pair. This can be achieved with Couchbase Web Console, or with the REST endpoints provided for managing [Indexes](../rest-api/rest-fts-indexing.md). Detailed instructions for setting up indexes, and specifying type mappings, are provided in [Creating Indexes](fts-creating-indexes.md).

For initial experimentation with geospatial geopoint querying (based on the type geopoint), the `geo` field of documents within the `travel-sample` bucket can be specified as a child field of the `default` type mapping (keyspace `travel-sample._default._default` as follows:

* Click the **Add Index** link in the upper right of the **Couchbase Web Console** \> **Search** page.  
![fts add initial](_images/fts-add-initial.png)
* To define any index on which Full Text Search a unique name for the index in the **Index Name** field, on the upper-left. Note that only alphanumeric characters, hyphens, and underscores are allowed for index names and the first character of the name must be alphabetic.  
Enter **test\_geopoint** as the name of the Search index you are creating in the **Index Name** text-box.  
![fts index name geopoint](_images/fts-index-name-geopoint.png)
* Select the bucket **travel-sample** from the **Bucket** pull-down menu.  
Use the pull-down menu provided for the Bucket field, on the upper-right, and select a bucket that you are allowed to access to via the cluster’s RBAC settings.  
![fts index name and bucket geopoint](_images/fts-index-name-and-bucket-geopoint.png)
* Select the checkbox **\[X\] Use non-default scope/collections**  
This allows your index to stream mutations from one or more non-default collections under the selected bucket and scope.  
![fts select geopoint scope collections](_images/fts-select-geopoint-scope-collections.png)
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
  ![fts index menu2 geopoint filled](_images/fts-index-menu2-geopoint-filled.png)
  * Set the text box **field** to **geo**, this will also update "searchable as" to **geo**.
  * Change the pull-down **type** to **geopoint**.  
  By configuring the child field information form, specifically identify the object **geo** as type **geopoint** this will tell the Search indexer to recognize top level sub-objects like:  
  ```json  
    "geo": {  
      "lat": 53.48253,  
      "lon": -2.23527,  
      "accuracy": "ROOFTOP"  
    },  
  ```
  * Check **\[X\]** the boxes "store" and "include in \_all field"
  * Click on the blue **ok** at the right of the section to save this sub-form.  
  ![fts index menu2 geopoint filled](_images/fts-index-menu2-geopoint-filled.png)
* Save your index, left-click on the **Create Index** button near the bottom of the screen.  
This is all you need to specify in order to create a more advanced index for test and development. No further configuration is required.  
![fts index create button](_images/fts-index-create-button.png)
* If you subsequently Edit your Index it should look like the following:  
![fts edit index geopoint](_images/fts-edit-index-geopoint.png)

> [!NOTE]
> Indexing all fields as above indexes across all fields is not recommended for production environments since it creates indexes that may be unnecessarily large, and therefore insufficiently performant. However this index can be edited and optimized if you check **\[X\] only index specified fields** under the Type Mappings section. This will result in a much smaller index and a faster index build since only the field **geo** will be indexed in the set of documents.

The index once created can also be accessed by means of the Search REST API see [Searching with the REST API](fts-searching-with-curl-http-requests.md). Furthermore the index could have been created in the first place via the Search REST API see [Index Creation with REST API](fts-creating-index-with-rest-api.md) for more information on using the Search REST API syntax.

## [](#creating%5Fgeopoint%5Frest%5Fquery%5Fradius%5Fbased)Creating a Query: Radius-Based

This section and those following, provide examples of the query-bodies required to make geospatial queries with the Couchbase REST API. Note that more detailed information on performing queries with the Couchbase REST API can be found in [Searching with the REST API](fts-searching-with-curl-http-requests.md); which shows how to use the full `curl` command and how to incorporate query-bodies into it.

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

The above query contains a `sort` object, which specifies that the returned documents should be ordered in terms of their _geo\_distance_ from specified `lon` and `lat` coordinates: these values need not be identical to those specified in the `query` object.

![fts geopoint search 01](_images/fts-geopoint-search_01.png) 

You can cut-n-paste the above Search body definition into the text area that says "search this index…​"

![fts geopoint search 02](_images/fts-geopoint-search_02.png) 

Once pasted hit the **Search** button and the UI will show the first 10 hits

![fts geopoint search 03](_images/fts-geopoint-search_03.png) 

The console allows searches performed via the UI to be translated dynamically into cURL examples. To create a cURL command to do this first check **\[X\] show advanced query settings** and then check **\[X\] show command-line query example**.

You should have a cURL command similar to the following:

```console
curl -XPOST -H "Content-Type: application/json" \
-u <username>:<password> http://localhost:8094/api/index/test_geopoint/query \
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
}'
```

If you copy and then run the above cURL command via the console the response from the Search service will report that there are 847 total\_hits but only return the first 10 hits. A subset of formatted console output might appear as follows:

> [!NOTE]
> To pretty print the response just pipe the output through the utility **[jq](http://stedolan.github.io/jq)** to enhance readability.

```json
"hits": [
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "landmark_17411",
    "score": 0.025840756648257503,
    "sort": [
      " \u0001?E#9>N\f\"e"
    ]
  },
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "landmark_17409",
    "score": 0.025840756648257503,
    "sort": [
      " \u0001?O~i*(kD,"
    ]
  },
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "landmark_17403",
    "score": 0.025840756648257503,
    "sort": [
      " \u0001?Sg*|/t\u001f\u0002"
    ]
  }
]
```

## [](#creating%5Fgeoppoint%5Frest%5Fquery%5Fbounding%5Fbox%5Fbased)Creating a Query: Rectangle-Based

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
"hits": [
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "landmark_16144",
    "score": 0.004836809397039384,
    "sort": [
      "02"
    ]
  },
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "hotel_9905",
    "score": 0.01625607942050202,
    "sort": [
      "1"
    ]
  },
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "hotel_16460",
    "score": 0.004836809397039384,
    "sort": [
      "11"
    ]
  },
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "hotel_21674",
    "score": 0.010011952055063241,
    "sort": [
      "17"
    ]
  }
]
```

## [](#creating%5Fgeopoint%5Frest%5Fquery%5Fpolygon%5Fbased)Creating a Query: Polygon-Based

The following query-body uses an array, each of whose elements is a string, containing two floating-point numbers; to specify the latitude and longitude of each of the corners of a polygon — known as _polygon points_. In each string, the `lat` floating-point value precedes the `lon.`

Here, the last-specified string in the array is identical to the initial string, thus explicitly closing the box. However, specifying an explicit closure in this way is optional: closure will be inferred by Couchbase Server if not explicitly specified.

If a target data-location falls within the box, its document is returned. The results are specified to be sorted on `name` alone.

```json
{
  "query": {
    "field": "geo",
    "polygon_points": [
      "37.79393211306212,-122.44234633404847",
      "37.77995881733997,-122.43977141339417",
      "37.788031092020155,-122.42925715405579",
      "37.79026946582319,-122.41149020154114",
      "37.79571192027403,-122.40735054016113",
      "37.79393211306212,-122.44234633404847"
    ]
  },
  "sort": [
    "name"
  ]
}
```

A subset of formatted output might appear as follows:

```json
"hits": [
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "landmark_25944",
    "score": 0.23634379439298683,
    "sort": [
      "4"
    ]
  },
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "landmark_25681",
    "score": 0.31367419004657393,
    "sort": [
      "alta"
    ]
  },
  {
    "index": "test_geopoint_7d088ca77bbecbe2_4c1c5584",
    "id": "landmark_25686",
    "score": 0.31367419004657393,
    "sort": [
      "atherton"
    ]
  }
]
```

> [!NOTE]
> When we sort on a string that uses the default analyzer that string is tokenized and you may get unexpected results as you are sorting on the tokenized field. If you want to sort on the actual text in the field should use the **analyzer: "keyword"** to sort by the original text in the field. In addition if you want to include the keyword in the index itself you will need to check **\[X\] store** or check **\[X\] docvalues**.

## [](#sorting-by-keywords)Sorting by Keywords

To sort by the actual names we need to take into account that for type="airport" has a field called "airportname" and for type="landmark" has a field called "name".

By inserting editing the index and inserting two more child fields as follows:

* for type="airport"  
![fts geopoint update1](_images/fts-geopoint-update1.png)
* for type="landmark"  
![fts geopoint update2](_images/fts-geopoint-update2.png)
* Click the **Update Index** button

If you look carefully above both the actual fields "airportname" and "name" will be searchable as name.

At this point if you Edit the index again the complete definition should look like:

![fts geopoint updated index](_images/fts-geopoint-updated-index.png) 

Now repeating the above "Polygon-Based" Query we see that the data is sorted based on the original field names.

```json
"hits": [
  {
    "index": "test_geopoint_6e91b22c20945813_4c1c5584",
    "id": "landmark_25681",
    "score": 0.31367419004657393,
    "sort": [
      "Alta Plaza Park"
    ]
  },
  {
    "index": "test_geopoint_6e91b22c20945813_4c1c5584",
    "id": "landmark_25686",
    "score": 0.31367419004657393,
    "sort": [
      "Atherton House"
    ]
  },
  {
    "index": "test_geopoint_6e91b22c20945813_4c1c5584",
    "id": "landmark_25944",
    "score": 0.23634379439298683,
    "sort": [
      "Big 4 Restaurant"
    ]
  },
  {
    "index": "test_geopoint_6e91b22c20945813_4c1c5584",
    "id": "landmark_25739",
    "score": 0.31367419004657393,
    "sort": [
      "Blu"
    ]
  },
  {
    "index": "test_geopoint_6e91b22c20945813_4c1c5584",
    "id": "landmark_36047",
    "score": 0.25593551041769463,
    "sort": [
      "Cable Car Museum"
    ]
  },
```

Finally since we checked **\[X\] store** for the child mappings for both "airportname" and "name" we modify the above “Polygon-Based” by adding **"fields": \["name"\],** and then run it in the UI.

```json
{
  "fields": ["name"],
  "query": {
    "field": "geo",
    "polygon_points": [
      "37.79393211306212,-122.44234633404847",
      "37.77995881733997,-122.43977141339417",
      "37.788031092020155,-122.42925715405579",
      "37.79026946582319,-122.41149020154114",
      "37.79571192027403,-122.40735054016113",
      "37.79393211306212,-122.44234633404847"
    ]
  },
  "sort": [
    "name"
  ]
}
```

Copy and paste the above into the UI’s index search text box the result will be as follows:

![fts geopoint updated index seach stored](_images/fts-geopoint-updated-index-seach-stored.png) 

Because we added **"fields": \["name"\],** and the fields "airportname" and "name" were specified to be stored the index returns the actual value (the mapped name of name) both in the UI. If we passed the new query body to cURL the value will also be returned via the REST call.