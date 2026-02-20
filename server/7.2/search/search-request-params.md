---
title: Search Request JSON Properties
description: You can add additional properties to a Search request to control
  how the Search Service returns results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/search-request-params.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:search:search-request-params.adoc[]
---

[View original HTML](/server/7.2/search/search-request-params.html)

# Search Request JSON Properties

> You can add additional properties to a Search request to control how the Search Service returns results. 

The following is an example Search request:

```json
{
    "query": {
        "must": {
            "conjuncts":[
                {
                    "field": "free_breakfast",
                    "bool": false
                },
                {
                    "field": "ratings.Cleanliness",
                    "inclusive_min": 1,
                    "inclusive_max": 3
                }
            ]
        },
        "must_not": {
            "disjuncts": [
                {
                    "field": "geojson",
                    "geometry": {
                        "shape": {
                            "coordinates": [-2.2450285424707204, 53.48503270828377],
                            "type": "circle",
                            "radius": "100mi"
                        },
                        "relation": "within"
                    }
                }
            ],
            "min": 1
        },
        "should": {
            "disjuncts": [
                {
                    "match_phrase": "very nice",
                    "field": "reviews.content"
                }
            ]
        }
    },
    "ctl": {
        "timeout": 10000,
        "consistency": {
            "vectors": {
                "searchIndexName": {
                    "607/205096593892159": 2,
                    "640/298739127912798": 4  
                }
            },
            "level": "at_plus",
            "results": "complete"
        }
    },
    "size": 10,
    "from": 0,
    "highlight": {

        "style": "html",
        "fields": ["textField"]

    },
    "fields": ["textField"],
    "facets": {

        "field1": {
            "size": 5,
            "field": "field1"
        },

        "field2": {
            "size": 5,
            "field": "field2",
            "numeric_ranges": [
                {

                    "name": "high",
                    "min": 7,
                    "max": 10

                },
                {

                    "name": "low",
                    "min": 0,
                    "max": 7

                }
             ]
        },

        "field3": {
            "size": 10,
            "field": "dateField",
            "date_ranges": [
                {
                    "name": "old",
                    "start": "2020-12-31",
                    "end": "2023-12-31"
                },
                {
                    "name": "new",
                    "start": "2023-12-31",
                    "end": "2024-12-31"
                }  
            ]
        }

    },
    "explain": true,
    "sort": [

        "field1",
            {
                "by": "field",
                "field": "field2",
                "desc": false,
                "mode": "max",
                "missing": "last",
                "type": "number"
            },
            "-_score",
            "-_id"
            
    ],
    "includeLocations": false,
    "score": "none",
    "search_after": ["field1Value", "5", "10.033205341869529", "1234"],
    "search_before": ["field1Value", "5", "10.033205341869529", "1234"],
    "limit": 10,
    "offset": 0,
    "collections": ["collection1", "collection2"]
}
```

A Search request can contain the following properties:

| Property         | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| query            | Object  | Yes       | An object that contains the properties for one of the supported query types. For more information about how to configure the query object, see [Query Object](#query-object).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ctl              | Object  | No        | An object that contains properties for query consistency. For more information about how to configure Search query consistency inside the ctl object, see [Ctl Object](#ctl).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| size/limit       | Integer | No        | Set the total number of results to return for a single page of search results. If you provide both the size and limit properties, the Search Service uses the size value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| from/offset      | Integer | No        | Set an offset value to change where pagination starts for search results, based on the Search query’s [Sort Object](#sort). For example, if you set a size value of 5 and a from value of 10, the Search query returns results 11 through 15 on a page. If you provide both the from and offset properties, the Search Service uses the from value.                                                                                                                                                                                                                                                                                                                                              |
| highlight        | Object  | No        | Contains properties to control search result highlighting. For more information about how to configure highlighting in Search results, see [Highlight Object](#highlight).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| fields           | Array   | No        | An array of strings to specify each indexed field you want to return in search results. You must add a field and its contents to a Search index to view it in search results or add it to the fields array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| facets           | Object  | No        | Contains {facet-name} objects to define each facet you want to return with search results. The Search Service supports the following facet types: **Term Facet**: Counts the documents that have the same value for a specified field. **Numeric Range Facet**: Counts the documents with numeric field values that are greater than or less than a specified range or ranges. **Date Range Facet**: Counts the documents with date field values that are earlier or later than a specified range or ranges. For more information, about how to configure the different facet types inside the facets object, see [{facet-name} Object](#facet-name).                                            |
| explain          | Boolean | No        | To create an explanation for a search result’s score in search results, set explain to true. To turn off explanations for search result scoring, set explain to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| sort             | Array   | No        | Contains an array of strings or JSON objects to set how to sort search results. The strings can be: {field\_name}: Specify the name of a field to use to sort the search results. \_id: Use the document’s identifier to sort the search results. \_score: Use the document’s score from the Search query to sort the search results. For more information about the properties for a sort JSON object, see [Sort Object](#sort).                                                                                                                                                                                                                                                                |
| includeLocations | Boolean | No        | To return the position of each occurrence of a search term inside a document, set includeLocations to true. You must have **Include Term Vectors** enabled or the include\_term\_vectors property set to true on a field to use includeLocations. For more information about how to enable term vectors, see [Create a Child Field](create-child-field.md#term-vectors) or [Search Index JSON Properties](search-index-params.md#term-vectors). To turn off term locations, set includeLocations to false.                                                                                                                                                                                       |
| score            | String  | No        | To turn off document relevancy scoring in search results, set score to none. To turn on document relevancy scoring in search results, remove the score property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| search\_after    | Array   | No        | If you use search\_after in a search request, you can’t use search\_before. Both properties are included in the example code to show the correct syntax. Use search\_after with from/offset and sort to control pagination in search results. Give a value for each string or JSON object in the sort array to the search\_after array. The Search Service starts search result pagination after the document with those values. You must provide the values in the same order that they appear in the sort array. For example, if you had a set of 10 documents to sort based on \_id values of 1-10, with from set to 2 and search\_after set to 8, documents 9-10 appear on the same page.    |
| search\_before   | Array   | No        | If you use search\_before in a search request, you can’t use search\_after. Both properties are included in the example code to show the correct syntax. Use search\_before with from/offset and sort to control pagination in search results. Give a value for each string or JSON object in the sort array to the search\_before array. The Search Service starts search result pagination before the document with those values. You must provide the values in the same order that they appear in the sort array. For example, if you had a set of 10 documents to sort based on \_id values of 1-10, with from set to 2 and search\_before set to 8, documents 2-6 appear on the same page. |
| collections      | Array   | No        | Contains an array of strings that specify the collections where you want to run the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## [](#query-object)Query Object

Use the `query` object to set the specific details of your Search query.

Use the properties in the `query` object to control search result rankings, add multiple subqueries, and more.

```json
{
    "query": {
        "must": {
            "conjuncts":[
                {
                    "field": "free_breakfast",
                    "bool": false
                },
                {
                    "field": "ratings.Cleanliness",
                    "inclusive_min": 1,
                    "inclusive_max": 3
                }
            ]
        },
        "must_not": {
            "disjuncts": [
                {
                    "field": "geojson",
                    "geometry": {
                        "shape": {
                            "coordinates": [-2.2450285424707204, 53.48503270828377],
                            "type": "circle",
                            "radius": "100mi"
                        },
                        "relation": "within"
                    }
                }
            ],
            "min": 1
        },
        "should": {
            "disjuncts": [
                {
                    "match_phrase": "very nice",
                    "field": "reviews.content"
                }
            ]
        }
    },
```

### [](#boolean-queries)Boolean Queries

Use any of the following properties to run a boolean query. A boolean query searches for a combination of queries that a document must match to be included in search results.

Boolean queries use a [compound query array](#compound-queries) inside the [must](#must), [must\_not](#must%5Fnot) and [should](#should) objects to set the queries a document must match.

| Property  | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| must      | Object | Use a must object to create a boolean query. A must object must contain a [conjuncts array](#conjuncts). The array lists all the queries that must have a match in a document to include the document in search results. For example, a query could have a must object with 2 queries in a conjuncts array. The Search Service must find a match for both those queries in a document to include it in search results.                      | reviews.content field must contain "location" and the phrase "nice view" {     "query":{         "must":{             "conjuncts":\[                 {                     "field": "reviews.content",                      "match": "location"                 },                 {                     "field":"reviews.content",                     "match\_phrase": "nice view"                 }             \]         }     } }                                                             |
| must\_not | Object | Use a must\_not object to create a boolean query. A must\_not object must contain a [disjuncts array](#disjuncts). The array lists all the queries that must have a match in a document to include the document in search results. For example, a query could have a must\_not object with 3 queries in a disjuncts array. The Search Service must not find a match for any of the 3 queries in a document to include it in search results. | free\_breakfast field must not be false and reviews.Cleanliness field must not be between 1 and 3 {     "query":{         "must\_not":{             "disjuncts":\[                 {                     "field": "free\_breakfast",                     "bool": false                 },                 {                     "field": "ratings.Cleanliness",                     "inclusive\_min": 1,                     "inclusive\_max": 3                 }             \]         }     } } |
| should    | Object | Use a should object to create a boolean query. A should object must contain a [disjuncts array](#disjuncts). The array lists all the queries that must have a match in a document to score the document higher in search results. A document can be included in search results if it does not match the query or queries in a should object. The document scores higher in search results if it does match the query.                       | free\_parking and free\_internet fields should be true {     "query":{         "should":{             "disjuncts":\[                 {                     "field": "free\_parking",                     "bool": true                 },                 {                     "field": "free\_internet",                     "bool": true                 }             \],             "min": 1         }     } }                                                                                 |

### [](#compound-queries)Compound Queries (AND and OR)

Use a compound query array to specify multiple child queries that must have a match in a document for that document to be included in search results.

You must use compound query arrays to run a [boolean query](#boolean-queries), but you can use a compound query array outside of a boolean query.

You can use 2 different types of compound queries:

| Property  | Type  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| conjuncts | Array | Use the conjuncts array to specify multiple child queries in a single query object. You can use the conjuncts array inside a [must object](#must) or directly inside a query object. If you use the conjuncts array, every query object in the array must have a match in a document to include the document in search results. You can create objects in a conjuncts array to describe any of the available query types: [Analytic Queries](#analytic-queries) [Non-Analytic Queries](#non-analytic-queries) [Numeric Range Queries](#numeric-range-queries) [Date Range Queries](#date-range-queries) [Term Range Queries](#term-range-queries) [Distance/Radius-Based Geopoint Queries](#geopoint-queries-distance) [Rectangle-Based Geopoint Queries](#geopoint-queries-rectangle) [Polygon-Based Geopoint Queries](#geopoint-queries-polygon) [Point GeoJSON Queries](#geojson-queries-point) [LineString GeoJSON Queries](#geojson-queries-linestring) [Polygon GeoJSON Queries](#geojson-queries-polygon) [MultiPoint GeoJSON Queries](#geojson-queries-multipoint) [MultiLineString GeoJSON Queries](#geojson-queries-multilinestring) [MultiPolygon GeoJSON Queries](#geojson-queries-multipolygon) [GeometryCollection GeoJSON Queries](#geojson-queries-geometrycollection) [Circle GeoJSON Queries](#geojson-queries-circle) [Envelope GeoJSON Queries](#geojson-queries-envelope)                                                                                                                                                   | reviews.date field must be between 2001-10-09 and 2016-10-31 and description field must contain "pool" {     "query":{         "conjuncts":\[             {                 "field": "reviews.date",                 "start": "2001-10-09",                 "end": "2016-10-31",                 "inclusive\_start": false,                 "inclusive\_end": false             },             {                 "field": "description",                 "match": "pool"             }         \]     } } |
| disjuncts | Array | Use the disjuncts array to specify multiple child queries in a single query object. You can use the disjuncts array inside a [must\_not object](#must%5Fnot), [should object](#should), or directly inside a query object. Use a min property to set the number of query objects from the disjuncts array that must have a match in a document. If a document does not match the min number of query objects, the Search Service does not include the document in search results. You can create objects in a disjuncts array to describe any of the available query types: [Analytic Queries](#analytic-queries) [Non-Analytic Queries](#non-analytic-queries) [Numeric Range Queries](#numeric-range-queries) [Date Range Queries](#date-range-queries) [Term Range Queries](#term-range-queries) [Distance/Radius-Based Geopoint Queries](#geopoint-queries-distance) [Rectangle-Based Geopoint Queries](#geopoint-queries-rectangle) [Polygon-Based Geopoint Queries](#geopoint-queries-polygon) [Point GeoJSON Queries](#geojson-queries-point) [LineString GeoJSON Queries](#geojson-queries-linestring) [Polygon GeoJSON Queries](#geojson-queries-polygon) [MultiPoint GeoJSON Queries](#geojson-queries-multipoint) [MultiLineString GeoJSON Queries](#geojson-queries-multilinestring) [MultiPolygon GeoJSON Queries](#geojson-queries-multipolygon) [GeometryCollection GeoJSON Queries](#geojson-queries-geometrycollection) [Circle GeoJSON Queries](#geojson-queries-circle) [Envelope GeoJSON Queries](#geojson-queries-envelope) | free\_parking field must be true or checkin field must be "1PM" {     "query":{         "disjuncts":\[             {                 "field": "free\_parking",                 "bool": true             },             {                 "field": "checkin",                 "match": "1PM"             }         \],         "min": 1     } }                                                                                                                                                            |

### [](#query-string-query-syntax)Query String Query Syntax

Use the following properties and syntax to run a Query String query.

Query String queries let you express more complex queries with a special syntax. You can reduce the properties you need to specify for a Search query with Query String syntax.

If you do not add any additional Query String syntax to a query, the Search Service interprets the query as a match query. It searches for an exact match to the provided term in any fields that have been added to the `default` field. For more information about how to configure the default field for your Search index, see [Set Search Index General Settings](set-advanced-settings.md#all-field) or the [default\_field property](search-index-params.md#all-field).

> [!CAUTION]
> Query String syntax is not recommended for use in production environments.

| Operator          | Property                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ^                 | See [boost](#boost).                                                                               | If you use multiple clauses in a query, you can use the ^ operator to assign the relative importance to a clause. Clauses with a larger number after the ^ operator score higher and appear earlier in search results.                                                                                                                                                                                                                                                                                                                                                                                                                                   | Query String query with a boost on the name field containing pool {     "query": {         "query": "description:pool name:pool^5"     } }                                                                                                                                                                                                      |
| \>, \>=, <, and ⇐ | See [Date Range Queries](#date-range-queries) or [Numeric Range Queries](#numeric-range-queries).  | You can run two types of range queries with the the later than (\>), later than or equal to (\>=), earlier than (<), and earlier than or equal to (⇐) operators: Use the operators with a date value to run a **date range query**. The Search Service searches for a date value in the specified field that matches the specified operator. Use operators with a numeric value to run a **numeric range query**. The Search Service searches for a numeric value in the specified field that matches the specified operator.                                                                                                                            | Query String query for a date in the created field after September 21, 2016 {     "query": {         "query": "reviews.date:>\\"2012-09-21\\""     } } Query String query for a rating in the reviews.ratings.Cleanliness field greater than 4 {     "query": {         "query": "reviews.ratings.Cleanliness:>4"     } }                       |
| \\                | N/A                                                                                                | Use a backslash character (\\) to escape characters in a Query String query. You must escape the following characters to search for them literally in a Query String query: Quotes (") Plus sign (+) Dash (\-) Equals sign (\=) Ampersand (&) Caret (^) Asterix (\*) Pipe (\|) Greater than and less than symbol (\> and <) Exclamation mark (!) Question mark (?) Parentheses (( )) Curly braces ({ }) Square brackets (\[ \]) Single or double backslash (\\) Forward slash (/) Tilde (\~) Colon (:)                                                                                                                                                   | Query String match query with escaped exclamation mark (!) {     "query": {         "query": "\\!"     } } Query String match phrase query with escaped quotation mark (") {      "query": {         "query": "\\" a phrase in quotes \\""     } }                                                                                              |
| {field-name}:     | See [field](#field).                                                                               | Set the field in a document where the Search Service should search for your query by adding a field name and a colon to the start of a search term. Use dot notation for the field name. For example, parentField.childField. The Query String syntax does not support SQL++ field syntax. For example, you cannot use \[\*\] or \[3\] as array locations in a field name path.                                                                                                                                                                                                                                                                          | Query String query for "pool" in the description field {      "query": {         "query": "description:pool"     } }                                                                                                                                                                                                                            |
| + and \-          | See the [must property](#must), [must\_not property](#must%5Fnot), and [should property](#should). | Use the + and \- operators before a clause in a Query String query to run a [boolean query](#boolean-queries): The + operator adds the clause to the MUST list of a boolean query. The \- operator adds the clause to the MUST\_NOT list of a boolean query. The Search Service adds any additional query clauses not marked with a + or a \- operator to the SHOULD list of a boolean query. Documents that match the SHOULD list of queries score higher than those that do not return a match.                                                                                                                                                        | Query String query with boolean syntax {     "query": {         "query": "+description:pool -continental breakfast"     } } The Query String syntax specifies that: The document must have pool in the description field. The document must not have continental in the default field. The document should have breakfast in the default field. |
| ""                | See [match\_phrase property](#match%5Fphrase).                                                     | Surround a search term in quotation marks (" ") to run a match phrase query. To use a match phrase query: You must specify a field to search with the [field property](#field) or the [{field-name}](#field-name) syntax in your search query. You must have **Include Term Vectors** enabled or the include\_term\_vectors property set to true on the field you want to search. For more information about how to enable term vectors, see [Create a Child Field](create-child-field.md#term-vectors) or [Search Index JSON Properties](search-index-params.md#term-vectors). The Search Service searches for exact matches to the phrase you specify. | Query String match phrase query for "continental breakfast" {      "query": {         "query": "continental breakfast"     } }                                                                                                                                                                                                                  |

### [](#analytic-queries)Analytic Queries

Analytic queries use an analyzer to analyze the contents of your Search query, and find a match in the documents inside your Search index.

For more information about analyzers, see [Customize a Search Index with the Web Console](customize-index.md#analyzers).

| Property      | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Examples                                                                                                                                                                                                                               |
| ------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| match         | String | Use the match property to run a match query. The Search Service searches for an exact match to the specified term inside the Search index’s default field. You can set a specific field to search with the [field property](#field). You can change the matching behavior by using the [fuzziness property](#fuzziness). You cannot include spaces inside the string you provide to the match property without specifying the [operator property](#operator), which tells the Search Service how to interpret the string. For more information about the properties you can specify with a match query, see [Additional Query Object Properties](#additional-query-properties).                                                                                                                                                                                                                                                                | Match query for "best" or "great" in reviews.content with the "standard" analyzer {     "query": {         "match": "best great",         "field": "reviews.content",         "analyzer": "standard",         "operator": "or"     } } |
| match\_phrase | String | Use the match\_phrase property to run a match phrase query. The Search Service searches for exact matches to the phrase you specify. Unlike a match query string, a match\_phrase query string can contain spaces without using the [operator property](#operator). To use a match phrase query: You must specify a field to search with the [field property](#field) or the [{field-name}](#field-name) syntax in your search query. You must have **Include Term Vectors** enabled or the include\_term\_vectors property set to true on the field you want to search. For more information about how to enable term vectors, see [Create a Child Field](create-child-field.md#term-vectors) or [Search Index JSON Properties](search-index-params.md#term-vectors). For more information about the additional properties you can specify with a match phrase query, see [Additional Query Object Properties](#additional-query-properties). | Match phrase query for "very nice" in reviews.content {     "query": {         "match\_phrase": "very nice",         "field": "reviews.content"     } }                                                                                |

### [](#non-analytic-queries)Non-Analytic Queries

Use Non-Analytic queries to run a search query without using an analyzer on the contents of your Search query.

For more information about analyzers, see [Customize a Search Index with the Web Console](customize-index.md#analyzers).

| Property | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Examples                                                                                                                                                                                                                |
| -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bool     | Boolean | Use the bool property to query a field that contains a boolean value. Use the [field property](#field) and set the bool property to true or false to run a search. The Search Service does not use any analyzers on the contents of your query. For more information about the additional properties you can specify with a bool query, see [Additional Query Object Properties](#additional-query-properties).                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Search for documents where the pets\_ok field is true {      "query": {         "field": "pets\_ok",         "bool": true     } }                                                                                       |
| prefix   | String  | Use the prefix property to run a prefix query. Set the property to a string to return matches for any term that starts with that string in search results. For example, you could set the prefix property to inter to return matches for interview, internal, interesting, and so on. If you use the prefix property, the Search Service does not use any analyzers on the contents of your query text. For more information about the additional properties you can specify with a prefix query, see [Additional Query Object Properties](#additional-query-properties).                                                                                                                                                                                                                                                                                                         | Search for terms that start with "inter" inside the reviews.content field {     "query": {         "prefix": "inter",         "field": "reviews.content"     } }                                                        |
| regexp   | String  | Use the regexp property to run a regular expression query. Set the property to a regular expression to return matches for that regular expression in search results. If you use the regexp property, the Search Service does not use any analyzers on the contents of your query text. For more information about the additional properties you can specify with a regexp query, see [Additional Query Object Properties](#additional-query-properties).                                                                                                                                                                                                                                                                                                                                                                                                                          | Search for terms that match the regular expression "plan.+" inside the reviews.content field {      "query": {         "regexp": "plan.+",         "field": "reviews.content"     } }                                   |
| term     | String  | Use the term property to run a term query. The Search Service searches for an exact match for the text you provide in the term property. You can change the matching behavior by using the [fuzziness property](#fuzziness). If you use the term property, the Search Service does not use any analyzers on the contents of your query text. For more information about the additional properties you can specify with a term query, see [Additional Query Object Properties](#additional-query-properties).                                                                                                                                                                                                                                                                                                                                                                      | Search for terms that match the term "interest" inside the reviews.content field with a fuzziness of 2 {      "query": {         "term": "interest",         "field": "reviews.content",         "fuzziness": 2     } } |
| terms    | Array   | Use the terms array to run a phrase query. The Search Service searches for the strings you provide in the terms array in the specified order. Unlike the [match\_phrase property](#match%5Fphrase), the terms array does not use any analyzers on the contents of your query text. For example, set the terms array to \["nice", "view"\]. The Search Service looks for any occurrences of nice in a document that are followed by an occurrence of view. To use a phrase query: You must set the [field property](#field) in your search query. You must have **Include Term Vectors** enabled or the include\_term\_vectors property set to true on the field you want to search. For more information about how to enable term vectors, see [Create a Child Field](create-child-field.md#term-vectors) or [Search Index JSON Properties](search-index-params.md#term-vectors). | Search for the phrase "nice view" in the reviews.content field {      "query": {         "terms": \["nice", "view"\],         "field": "reviews.content"     } }                                                        |
| wildcard | String  | Use the wildcard property to run a wildcard query. Set the property to a regular expression that includes a wildcard character in the middle or end of a search term: Use ? to allow a match to any single character. Use \* to allow a match to zero or many characters. For example, you could set the wildcard property to inter\* to return matches for interview, interject, internal, and so on. You cannot place the wildcard character at the start of the search term. If you use the wildcard property, the Search Service does not use any analyzers on the contents of your query text.                                                                                                                                                                                                                                                                               | Search for any terms that start with "inter" followed by zero or more characters in the reviews.content field {      "query": {         "wildcard": "inter\*",         "field": "reviews.content"     } }               |

### [](#numeric-range-queries)Numeric Range Queries

Use a numeric range query to search for a range of numbers inside documents in your Search index:

```json
{ 
    "query": {
        "min": 3,
        "max": 5,
        "inclusive_min": false,
        "inclusive_max": true,
        "field": "reviews.ratings.Cleanliness"
    }
}
```

The `field` value is an optional property. For more information about the `field` property, see [Additional Query Object Properties](#additional-query-properties).

| Property       | Type    | Required? | Description                                                                                                                                                                                                                                                                             |
| -------------- | ------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| min            | Integer | No        | Set the minimum value of the numeric range that you want to search for. You can specify only a min value or only a max value on your numeric range. By default, min is inclusive to the range.                                                                                          |
| max            | Integer | No        | Set the maximum value of the numeric range that you want to search for. You can specify only a max value or only a min value on your numeric range. By default, max is exclusive to the range.                                                                                          |
| inclusive\_min | Boolean | No        | Set whether the Search Service should return documents that contain the exact min value. If you set inclusive\_min to false, only values greater than min count as a match to your Search query. If you do not set the inclusive\_min value, by default, min is inclusive to the range. |
| inclusive\_max | Boolean | No        | Set whether the Search Service should return documents that contain the exact max value. If you set inclusive\_max to false, only values less than max count as a match to your Search query. If you do not set the inclusive\_max value, by default, max is exclusive to the range.    |

### [](#date-range-queries)Date Range Queries

Use a date range query to search for a range of date values inside documents in your Search index:

```json
{
    "query": {
        "start": "2001-10-09T10:20:30-08:00",
        "end": "2016-10-31",
        "inclusive_start": false,
        "inclusive_end": false,
        "field": "reviews.date"
    }
}
```

The `field` value is an optional property. For more information about the `field` property, see [Additional Query Object Properties](#additional-query-properties).

| Property         | Type    | Required? | Description                                                                                                                                                                                                                                                                                    |
| ---------------- | ------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start            | Integer | No        | Set the start date of the date range that you want to search for. You can specify only a start value or only a end value on your date range. By default, start is inclusive to the range.                                                                                                      |
| end              | Integer | No        | Set the end date of the date range that you want to search for. You can specify only a end value or only a start value on your date range. By default, end is exclusive to the range.                                                                                                          |
| inclusive\_start | Boolean | No        | Set whether the Search Service should return documents that contain the exact start value. If you set inclusive\_start to false, only dates later than start count as a match to your Search query. If you do not set the inclusive\_start value, by default, start is inclusive to the range. |
| inclusive\_end   | Boolean | No        | Set whether the Search Service should return documents that contain the exact end value. If you set inclusive\_end to false, only dates earlier than end count as a match to your Search query. If you do not set the inclusive\_end value, by default, end is exclusive to the range.         |

### [](#term-range-queries)Term Range Queries

Use a term range query to search for a range of terms inside documents in your Search index.

For example, the following query searches for any terms that occur in alphabetical order between `be` and `beautiful` from the `reviews.content` field in a Search index:

```json
{ 
    "query": {  
        "min": "be", 
        "max": "beautiful",  
        "inclusive_min": true,  
        "inclusive_max": true,  
        "field": "reviews.content" 
    }
}
```

The query returns results such as `beach`, `beaches`, `beans`, and `beast`.

The `field` value is an optional property. For more information about the `field` property, see [Additional Query Object Properties](#additional-query-properties).

| Property       | Type    | Required? | Description                                                                                                                                                                                                                                                                                                         |
| -------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| min            | Integer | No        | Set the minimum term of the term range that you want to search for. You can specify only a min value or only a max value on your term range. By default, min is inclusive to the range.                                                                                                                             |
| max            | Integer | No        | Set the minimum term of the term range that you want to search for. You can specify only a max value or only a min value on your term range. By default, max is exclusive to the range.                                                                                                                             |
| inclusive\_min | Boolean | No        | Set whether the Search Service should return documents that contain the exact min value. If you set inclusive\_min to false, only terms that would occur after min in the dictionary count as a match to your Search query. If you do not set the inclusive\_min value, by default, min is inclusive to the range.  |
| inclusive\_max | Boolean | No        | Set whether the Search Service should return documents that contain the exact max value. If you set inclusive\_max to false, only terms that would occur before max in the dictionary count as a match to your Search query. If you do not set the inclusive\_max value, by default, max is exclusive to the range. |

### [](#ip-address-range-queries)IP Address Range Queries

Use an IP Address Range query to search for IP address data in your Search index.

You can use IPv4 or IPv6 CIDR syntax in your query.

For example, the following query searches for any IP addresses in the range `2.7.13.141/32` and `2001:4860:4860::8888/24`:

```json
{
    "query": {
        "conjuncts": [
            {
                "cidr": "2.7.13.0/24",
                "field": "ipv4"
            },
            {
                "cidr": "2001:db8:1234:5678::/119",
                "field": "ipv6"
            }
        ]
    }
}
```

> [!NOTE]
> If your IP range includes over 1024 IP addresses, you must update the `bleveMaxResultWindow` setting to accommodate your results. For more information about how to change this setting, see [bleveMaxResultWindow](../../current/fts/fts-advanced-settings-bleveMaxResultWindow.md).

| Property | Type                                         | Required? | Description                                                                                                                                                                                                   |
| -------- | -------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cidr     | String Containing An IPv4 or IPv6 IP Address | Yes       | Enter an IP address range or single IP address, in IPv4 or IPv6 CIDR notation. The Search Service returns documents with IP addresses that fall inside the specified range or match the specified IP address. |

### [](#geopoint-queries-distance)Distance/Radius-Based Geopoint Queries

Use a Geopoint distance/radius-based query to search for geo location values in a set radius around a specified latitude and longitude:

```json
{
  "query": {
      "location": {
        "lon": -2.235143,
        "lat": 53.482358
      },
        "distance": "100mi",
        "field": "geo"
  }
}
```

To use a Geopoint query, you must have a child field in your Search index with the `geopoint` type. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property | Type            | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------- | --------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| location | Object or Array | Yes       | Set the geo location value to use as the center of the search radius for your query. If you use location as an object, you must set two values: lon: The longitude of the geo location to use as the center of the search radius. lat: The latitude of the geo location to use as the center of the search radius. If you use location as an array, your array must contain a longitude value followed by a latitude value. For example, \[-2.235143, 53.482358\], where \-2.235143 is the longitude. |
| distance | String          | Yes       | The radius where the Search Service should search for matching geo location values. Enter the radius as a single string, with a numeric value and a unit value. For example, 100.5mi. You can use the following distance units: mm: Millimeters cm: Centimeters in: Inches yd: Yards ft: Feet m: Meters km: Kilometers mi: Miles nm: Nautical miles                                                                                                                                                   |

### [](#geopoint-queries-rectangle)Rectangle-Based Geopoint Queries

Use a Geopoint rectangle-based query to search for geo location values in a defined rectangle:

```json
{ 
  "query": {
      "top_left": [-2.235143, 53.482358],
      "bottom_right": {
        "lon": 28.955043,
        "lat": 40.991862
      },
      "field": "geo"
  }
}
```

The Search Service takes a value for the top-left and bottom-right corners of a rectangle, and draws a bounding box that connects those points. The resulting rectangle is used as the search area for geo location values.

To use a Geopoint query, you must have a child field in your Search index with the `geopoint` type. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property      | Type            | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------- | --------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| top\_left     | Object or Array | Yes       | Set the geo location value to use as the top-left corner point of the rectangle search area. If you use top\_left as an object, you must set two values: lon: The longitude of the geo location to use as the top-left corner of the rectangle. lat: The latitude of the geo location to use as the top-left corner of the rectangle. If you use top\_left as an array, your array must contain a longitude floating point value followed by a latitude floating point value. For example, \[-2.235143, 53.482358\], where \-2.235143 is the longitude.                     |
| bottom\_right | Object or Array | Yes       | Set the geo location value to use as the bottom-right corner point of the rectangle search area. If you use bottom\_right as an object, you must set two values: lon: The longitude of the geo location to use as the bottom-right corner of the rectangle. lat: The latitude of the geo location to use as the bottom-right corner of the rectangle. If you use bottom\_right as an array, your array must contain a longitude floating point value followed by a latitude floating point value. For example, \[-2.235143, 53.482358\], where \-2.235143 is the longitude. |

### [](#geopoint-queries-polygon)Polygon-Based Geopoint Queries

Use a Geopoint polygon-based query to search for geo location values in a defined polygon:

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
  }
}
```

The Search Service takes an array of latitude and longitude values and connects them in the specified order to form a polygon. The resulting polygon is used as the search area for geo location values.

To use a Geopoint query, you must have a child field in your Search index with the `geopoint` type. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property        | Type  | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| polygon\_points | Array | Yes       | Set an array of latitude and longitude string values to use as the points in your polygon search area. For example, an array of \[ "37.79393211306212,-122.44234633404847", "37.77995881733997,-122.43977141339417", "37.788031092020155,-122.42925715405579"\] is interpreted as 3 separate polygon points and creates a 3-sided polygon. For polygon\_points, the first value in the string is the latitude, and the second is the longitude. You can set the last value in the array to the same value as the first latitude and longitude to explicitly close your polygon. Otherwise, the Search Service infers the polygon’s closure. |

### [](#geojson-queries-point)Point GeoJSON Queries

Use a GeoJSON Point query to search for a single latitude and longitude coordinate that intersects or is contained inside a GeoJSON shape in your documents:

```json
{
    "query": {        
        "field": "geojson",     
        "geometry": {                
            "shape": {                      
                "type": "point",                      
                "coordinates": [0.47482593026924746, 51.31232878073189]               
            },                
            "relation": "intersects"          
        }    
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | ------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object | Yes       | Contains the [shape property](#point-shape) and [relation](#point-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| shape       | Object | Yes       | Contains the [type property](#point-type) and [coordinates property](#point-coordinates). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| type        | String | Yes       | Set type to point.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| coordinates | Array  | Yes       | An array of coordinate floating point values that define the GeoJSON shape. For a point query, set the coordinates array to a single array with a longitude and latitude value. The Search Service uses the first value in the coordinates array as the longitude value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| relation    | String | Yes       | Set how the Search Service should return a match for a GeoJSON Point search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: The defined query Point overlaps a defined Point or LineString, or exists within the defined area for a Polygon, Circle, or Envelope. For multi-shape geometries, the query point must only overlap with one Point, LineString, or Polygon. contains: The defined query Point overlaps a defined Point or LineString, or exists within the defined area for a Polygon, Circle, or Envelope. For multi-shape geometries, the query point must only overlap with one Point, LineString, or Polygon. within: Not supported for Point queries. |

### [](#geojson-queries-linestring)LineString GeoJSON Queries

Use a GeoJSON LineString query to search for a line of coordinates that intersects or is contained inside a GeoJSON shape in your documents:

```json
{
    "query": {
        "field": "geojson",
        "geometry": {
            "shape": {
            "type": "linestring",
            "coordinates": [
                    [-2.753735609842721, 53.94860827535115],
                    [-2.599898256093695,53.65007434185782]
                ]
            },
            "relation": "intersects"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type            | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------- | --------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object          | Yes       | Contains the [shape property](#linestring-shape) and [relation](#linestring-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| shape       | Object          | Yes       | Contains the [type property](#linestring-type) and [coordinates property](#linestring-coordinates). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| type        | String          | Yes       | Set type to linestring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coordinates | Array of Arrays | Yes       | An array that contains arrays of 2 coordinate floating point values that define the GeoJSON LineString shape. For a linestring query, the coordinates array can contain multiple coordinate point arrays. The Search Service uses the first value in any nested coordinates array as the longitude value for the coordinate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| relation    | String          | Yes       | Set how the Search Service should return a match for a GeoJSON LineString search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: The defined query LineString overlaps a defined Point or LineString, or intersects with the defined edges of a Polygon, Circle, or Envelope. For multi-shape geometries, the defined LineString must only overlap one Point, or intersect one LineString or Polygon. contains: The start and end points of the LineString are within the defined area of a Polygon, Circle, or Envelope. Points and LineStrings are not supported. For MultiPolygon or GeometryCollection shapes, only one Polygon must contain both the start and end points of the LineString. within: Not supported for LineString queries. |

### [](#geojson-queries-polygon)Polygon GeoJSON Queries

Use a GeoJSON Polygon query to search for a defined area that intersects, is contained inside, or surrounds a GeoJSON shape in your documents:

```json
{
    "query": {
        "field": "geojson",
        "geometry": {
            "shape": {
                "type": "Polygon",
                "coordinates": [
                    [
                    [
                        0.47482593026924746,
                        51.31232878073189
                    ],
                    [
                        0.6143265647863245,
                        51.31232878073189
                    ],
                    [
                        0.6143265647863245,
                        51.384000374770466
                    ],
                    [
                        0.47482593026924746,
                        51.384000374770466
                    ],
                    [
                        0.47482593026924746,
                        51.31232878073189
                    ]
                    ]
                ]
            },
            "relation": "within"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type            | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | --------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object          | Yes       | Contains the [shape property](#polygon-shape) and [relation](#polygon-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| shape       | Object          | Yes       | Contains the [type property](#polygon-type) and [coordinates property](#polygon-coordinates). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| type        | String          | Yes       | Set type to polygon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| coordinates | Array of Arrays | Yes       | An array that contains an outer array, and arrays of 2 coordinate floating point values that define the GeoJSON Polygon shape. The Search Service uses the first value in any nested coordinates array as the longitude value for the coordinate. The Search Service also follows strict GeoJSON syntax, and expects exterior coordinates in a polygon to be in counterclockwise order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| relation    | String          | Yes       | Set how the Search Service should return a match for a GeoJSON Polygon search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: The defined query Polygon contains a Point, or one of its edges intersects a LineString, Polygon, Circle, or Envelope. For multi-shape geometries, only one Point must be contained, or only one LineString or Polygon must intersect. contains: The entire defined area of the query Polygon exists inside a Polygon, Circle, or Envelope. Points and LineStrings are not supported. For multi-shape geometries, one shape must contain the entirety of the defined query Polygon. within: The query Polygon contains a Point, the endpoints of a LineString, or the entirety of a Polygon, Circle, or Envelope. For multi-shape geometries, the query Polygon must contain the entirety of each defined Point, LineString, or Polygon. |

### [](#geojson-queries-multipoint)MultiPoint GeoJSON Queries

Use a GeoJSON MultiPoint query to search for multiple coordinate points that intersect or are contained inside a GeoJSON shape in your documents:

```json
{
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
            "relation": "intersects"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type            | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| geometry    | Object          | Yes       | Contains the [shape property](#multipoint-shape) and [relation](#multipoint-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| shape       | Object          | Yes       | Contains the [type property](#multipoint-type) and [coordinates property](#multipoint-coordinates). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| type        | String          | Yes       | Set type to multipoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| coordinates | Array of Arrays | Yes       | An array that contains arrays of 2 coordinate floating point values that define the GeoJSON MultiPoint shape. The Search Service uses the first value in any nested coordinates array as the longitude value for the coordinate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| relation    | String          | Yes       | Set how the Search Service should return a match for a GeoJSON MultiPoint search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: One of the points in the MultiPoint overlaps a Point or a LineString endpoint, or exists inside the area of a Polygon, Circle, or Envelope. For multi-shape geometries, only one Point must inside the shape or overlap a Point or endpoint. contains: All points in the MultiPoint exist inside a Polygon, Circle, or Envelope. Points and LineStrings are not supported. A MultiPoint shape can return a match if all points in the query overlap with the MultiPoint in the document. A MultiPolygon or GeometryCollection returns a match if all query points exist within any of the defined Polygons or MultiPoints. within: Any of the points in the query MultiPoint overlap with a defined Point. A MultiPoint shape returns a match if all points in the query overlap with the MultiPoint in the document. |

### [](#geojson-queries-multilinestring)MultiLineString GeoJSON Queries

Use a GeoJSON MultiLineString query to search for multiple [LineStrings](#geojson-queries-linestring) that intersect or are contained inside a GeoJSON shape in your documents:

```json
{
    "query": {
        "field": "geojson",
        "geometry": {
            "shape": {
                "type": "MultiLineString",
                "coordinates": [
                        [ [1.954764, 50.962097], [3.029578, 49.868547] ],
                        [ [3.029578, 49.868547], [-0.387444, 48.545836] ]
                    ]
            },
            "relation": "intersects"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type            | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | --------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object          | Yes       | Contains the [shape property](#multilinestring-shape) and [relation](#multilinestring-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| shape       | Object          | Yes       | Contains the [type property](#multilinestring-type) and [coordinates property](#multilinestring-coordinates). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| type        | String          | Yes       | Set type to multilinestring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| coordinates | Array of Arrays | Yes       | An array that contains nested arrays, each with their own nested arrays of 2 coordinate floating point values. For example, the following coordinates array defines 2 LineStrings with start and end points: "coordinates": \[     \[         \[1.954764, 50.962097\], \[3.029578, 49.868547\]     \],     \[         \[3.029578, 49.868547\], \[-0.387444, 48.545836\]     \] \] The innermost arrays define the individual points for a LineString in the MultiLineString shape. The Search Service uses the first value in the nested coordinates arrays as the longitude value for a coordinate.                                                                                                                                                                                                                                                                                                                                                |
| relation    | String          | Yes       | Set how the Search Service should return a match for a GeoJSON MultiLineString search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: Any LineString inside the defined query MultiLineString overlaps a defined Point or LineString, or intersects with the defined edges of a Polygon, Circle, or Envelope. For multi-shape geometries, any defined LineString must only overlap one Point, or intersect one LineString or Polygon. contains: The start and end points of every LineString inside the defined query MultiLineString are within the defined area of a Polygon, Circle, or Envelope. Points and LineStrings are not supported. For MultiPolygon or GeometryCollection shapes, only one Polygon must contain both the start and end points of every LineString. within: Not supported for MultiLineString queries. |

### [](#geojson-queries-multipolygon)MultiPolygon GeoJSON Queries

Use a GeoJSON MultiPolygon query to search for a group of defined [Polygons](#geojson-queries-polygon) that intersect, are contained inside, or surround a GeoJSON shape in your documents:

```json
{
    "query": {
        "field": "geojson",
        "geometry": {
            "shape": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [[-1.8167959002718135, 53.8626654046235],
                        [-1.8728039536828476, 53.6335890387158],
                        [-1.4029586167332582, 53.57727933778668],
                        [-1.0031233465474827, 53.664942195474936],
                        [-1.1742590653039997, 53.84522968338081],
                        [-1.5523134258297944, 53.89384804206853],
                        [-1.8167959002718135, 53.8626654046235]]
                    ],
                    [
                        [[-2.4935598789906805, 53.64373525825596],
                        [-2.664695597747226, 53.33735696804186],
                        [-2.0143798664721544, 53.28065279675474],
                        [-1.8572461610683888, 53.550482816448266],
                        [-2.309977926141812, 53.604982015453714],
                        [-2.4935598789906805, 53.64373525825596]]
                    ]
                ]
            },
            "relation": "within"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type            | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------- | --------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object          | Yes       | Contains the [shape property](#multipolygon-shape) and [relation](#multipolygon-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| shape       | Object          | Yes       | Contains the [type property](#multipolygon-type) and [coordinates property](#multipolygon-coordinates). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| type        | String          | Yes       | Set type to multipolygon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| coordinates | Array of Arrays | Yes       | An array that contains arrays that describe a GeoJSON Polygon shape. Each inner array that describes a Polygon can contain multiple arrays with 2 coordinate floating point values. These innermost arrays describe the coordinates of the Polygon. The Search Service uses the first value in any nested coordinates array as the longitude value for the coordinate. The Search Service also follows strict GeoJSON syntax, and expects exterior coordinates in a polygon to be in counterclockwise order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| relation    | String          | Yes       | Set how the Search Service should return a match for a GeoJSON MultiPolygon search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: Any of the Polygons defined in the query MultiPolygon contain a Point, or one of their edges intersects a LineString, Polygon, Circle, or Envelope. For multi-shape geometries, only one Point must be contained in a query Polygon, or only one LineString or Polygon must intersect. contains: Every Polygon defined in the query MultiPolygon exists inside a Polygon, Circle, or Envelope. Points and LineStrings are not supported. For multi-shape geometries, one shape must contain the entirety of the defined query Polygons. within: Any of the Polygons defined in the query MultiPolygon contain a Point, the endpoints of a LineString, or the entirety of a Polygon, Circle, or Envelope. For multi-shape geometries, any of the query Polygons must collectively contain the entirety of each defined Point, LineString, or Polygon. |

### [](#geojson-queries-geometrycollection)GeometryCollection GeoJSON Queries

Use a GeoJSON GeometryCollection query to search for a group of defined [Points](#geojson-queries-point), [LineStrings](#geojson-queries-linestring), or [Polygons](#geojson-queries-polygon) that intersect, are contained inside, or surround a GeoJSON shape in your documents:

```json
{
    "query": {
        "field": "geojson",
        "geometry": {
            "shape": {
                "type": "geometrycollection",
                "geometries": [
                    {
                        "type": "linestring",
                        "coordinates": [
                            [-2.753735609842721, 53.94860827535115],
                            [-2.599898256093695, 53.65007434185782]
                        ]
                    }, 
                    {
                        "type": "multipolygon",
                        "coordinates": [
                            [[
                                [-1.8167959002718135, 53.8626654046235],
                                [-1.8728039536828476, 53.6335890387158],
                                [-1.4029586167332582, 53.57727933778668],
                                [-1.0031233465474827, 53.664942195474936],
                                [-1.1742590653039997, 53.84522968338081],
                                [-1.5523134258297944, 53.89384804206853],
                                [-1.8167959002718135, 53.8626654046235]
                            ]],
                            [[
                                [-2.4935598789906805, 53.64373525825596],
                                [-2.664695597747226, 53.33735696804186],
                                [-2.0143798664721544, 53.28065279675474],
                                [-1.8572461610683888, 53.550482816448266],
                                [-2.309977926141812, 53.604982015453714],
                                [-2.4935598789906805, 53.64373525825596]
                            ]]
                        ]
                    }
                ]
            },
            "relation": "contains"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type                     | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | ------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object                   | Yes       | Contains the [shape property](#geometrycollection-shape) and [relation](#geometrycollection-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| shape       | Object                   | Yes       | Contains the [type property](#geometrycollection-type) and [geometries property](#geometrycollection-geometries).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| type        | String                   | Yes       | Set type to geometrycollection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| geometries  | Array of Objects         | Yes       | Contains objects to define each GeoJSON shape in the GeometryCollection. Each object in the geometries array has a type property and a [coordinates property](#geometrycollection-coordinates). Set the type property inside the object to the specific shape type you want to define: [point](#geojson-queries-point) [linestring](#geojson-queries-linestring) [polygon](#geojson-queries-polygon) [multipoint](#geojson-queries-multipoint) [multilinestring](#geojson-queries-multilinestring) [multipolygon](#geojson-queries-multipolygon)                                                                                      |
| coordinates | Array or Array of Arrays | Yes       | An array or array of arrays that describes a GeoJSON shape. The exact structure of the arrays depends on the shape: [Point](#geojson-queries-point) [LineString](#geojson-queries-linestring) [Polygon](#geojson-queries-polygon) [MultiPoint](#geojson-queries-multipoint) [MultiLineString](#geojson-queries-multilinestring) [MultiPolygon](#geojson-queries-multipolygon) For any array that contains only floating point values, the Search Service uses the first value as the longitude. The Search Service also follows strict GeoJSON syntax, and expects exterior coordinates in a polygon to be in counterclockwise order. |
| relation    | String                   | Yes       | Set how the Search Service should return a match for a GeoJSON GeometryCollection search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: If any of the shapes in the query intersect with a shape in the document, the Search Service returns the document. contains: Every shape in the query must be contained, cumulatively, inside the shape or shapes defined in a document. within: Any of the shapes in a document must be contained within a shape in the query.                                            |

### [](#geojson-queries-circle)Circle GeoJSON Queries

Use a GeoJSON Circle query to search in a radius around a single latitude and longitude coordinate:

```json
{
    "query": {
        "field": "geojson",
        "geometry": {
            "shape": {
                "coordinates": [-2.2450285424707204, 53.48503270828377],
                "type": "circle",
                "radius": "100mi"
            },
            "relation": "within"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | ------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object | Yes       | Contains the [shape property](#circle-shape) and [relation](#circle-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| shape       | Object | Yes       | Contains the [type property](#circle-type), [coordinates property](#circle-coordinates), and [radius property](#circle-radius). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| type        | String | Yes       | Set type to circle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| coordinates | Array  | Yes       | An array of coordinate floating point values that define the center point of the Circle. Set the coordinates array to a single array with a longitude and latitude value. The Search Service uses the first value in the coordinates array as the longitude value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| radius      | String | Yes       | Set the radius of the Circle. Enter the radius as a single string, with a numeric value and a unit value. For example, 100.5mi. You can use the following distance units: mm: Millimeters cm: Centimeters in: Inches yd: Yards ft: Feet m: Meters km: Kilometers mi: Miles nm: Nautical miles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| relation    | String | Yes       | Set how the Search Service should return a match for a GeoJSON Circle search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: A defined Point exists within the radius of the Circle, or a LineString, Polygon, Envelope or Circle intersects the Circle. For multi-shape geometries, the Circle must only contain with one Point, or intersect one LineString or Polygon. contains: A defined Polygon, Envelope, or Circle contains the entire defined query Circle. Points and LineStrings are not supported. For MultiPolygons or GeometryCollections containing only Polygons, the query Circle must be contained by one Polygon. within: All defined GeoJSON shapes in the document must exist inside the defined query Circle. |

### [](#geojson-queries-envelope)Envelope GeoJSON Queries

Use a GeoJSON Envelope query to search in a bounded rectangle, based on a pair of coordinates that define the minimum and maxium longitude and latitude:

```json
{
    "query": {
        "field": "geojson",
        "geometry": {
            "shape": {
                "type": "Envelope",
                "coordinates": [
                    [-3.1720240079703785, 53.58545703217979],
                    [-1.8566251855731082, 53.282076725710596]
                ]
            },
            "relation": "intersects"
        }
    }
}
```

To use a GeoJSON query, you must have a child field in your Search index with the `geoshape` type. The `geoshape` field must contain a `type` property and a `coordinates` array. For more information about how to create a child field, see [Create a Child Field](create-child-field.md) or [the {field-name} object](#child-fields).

| Property    | Type              | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | ----------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| geometry    | Object            | Yes       | Contains the [shape property](#envelope-shape) and [relation](#envelope-relation) property. Defines the GeoJSON shape and how the Search Service should find a match in documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| shape       | Object            | Yes       | Contains the [type property](#envelope-type) and [coordinates property](#envelope-coordinates). Defines the specific GeoJSON shape to use in the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| type        | String            | Yes       | Set type to envelope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| coordinates | Array of 2 Arrays | Yes       | An array of 2 different arrays that contain coordinate floating point values. The first coordinates nested array contains the minimum longitude and maximum latitude, or the top-left corner of the rectangle. The second nested array contains the maximum longitude and minimum latitude, or the bottom-right corner. The Search Service uses the first value in the nested coordinates array as the longitude value.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| relation    | String            | Yes       | Set how the Search Service should return a match for a GeoJSON Envelope search. Your selected relation type determines which shapes return a match for your query. You can use the following string values in the relation property: intersects: A defined Point exists within the Envelope, or a LineString, Polygon, Envelope or Circle intersects the Envelope. For multi-shape geometries, the Envelope must only contain with one Point, or intersect one LineString or Polygon. contains: A defined Polygon, Envelope, or Circle contains the entire defined query Envelope. Points and LineStrings are not supported. For MultiPolygons or GeometryCollections containing only Polygons, the query Envelope must be contained by one Polygon. within: All defined GeoJSON shapes in the document must exist inside the defined query Envelope. |

### [](#special-queries)Special Queries

You can use the following special queries as the only properties inside a `query` object to return all or no documents from your Search index in search results.

| Property    | Type   | Description                                                                                                                          | Examples                                                                                     |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| match\_all  | Object | Use the match\_all object as the only property in your query object to return all documents from the Search index in search results. | Return all documents in the Search index {      "query": {         "match\_all": {}     } }  |
| match\_none | Object | Use the match\_none object as the only property in your query object to return no documents from the Search index in search results. | Return no documents from the Search index {     "query": {         "match\_none": {}     } } |

### [](#additional-query-properties)Additional Query Object Properties

You can use the following properties to modify the results returned by specific query types.

| Property       | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Examples                                                                                                                                                                                                                                                                                                                                                              |
| -------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analyzer       | String  | Use the analyzer property to modify the behavior of a [match query](#match) or a [match phrase query](#match%5Fphrase). Set the analyzer property to the name of the analyzer you want to use on the contents of the [match property](#match) or [match\_phrase property](#match%5Fphrase). The specified analyzer only applies to the content of your Search request. It does not apply to the contents of documents in the Search index.                                                                                                                                                                                                                                                                                          | Match query for "location" and "hostel" in reviews.content with the "en" analyzer {     "query":{         "match": "location hostel",         "field": "reviews.content",         "analyzer": "en"     } }                                                                                                                                                            |
| boost          | Integer | If you use multiple clauses in a query, you can use the boost property to assign the relative importance to a clause. Clauses with a higher value in the boost property score higher and appear earlier in search results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Disjunction query with boost property on the city field containing glossop {     "query": {         "disjuncts": \[             {                 "match": "glossop",                 "field": "city",                 "boost": 10             },             {                 "match": "glossop",                 "field": "title"             }         \]     } } |
| field          | String  | Specify a specific field name, using dot notation, where the Search Service should search for a match to your search query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Search for documents where the pets\_ok field is true {      "query": {         "field": "pets\_ok",         "bool": true     } }                                                                                                                                                                                                                                     |
| fuzziness      | Integer | Use the fuzziness property to run a fuzzy query. The fuzziness property uses your specified edit distance to match terms based on their similarity, rather than exact matches. You can set fuzziness to a maximum value of 2. Use the fuzziness property with the [term property](#term) for a term query or the [match property](#match) for a match query.                                                                                                                                                                                                                                                                                                                                                                        | Search for a match the term "interest" inside the reviews.content field with a fuzziness of 2 {      "query": {         "term": "interest",         "field": "reviews.content",         "fuzziness": 2     } }                                                                                                                                                        |
| operator       | String  | Use the operator property to modify the behavior of a [match query](#match): "and": Any spaces between terms in the [match property](#match) are interpreted as the AND operator. Documents must match all of the terms in the query. "or": Any spaces between terms in the [match property](#match) are interpreted as the OR operator. Documents must match at least one of the terms in the query. For example, if you set a match property to the value "good great" and the operator property to "and", the Search Service only returns matches for documents that contain good and great. If you set the operator property to "or", a document only needs to contain one of the terms from the match property: good or great. | Match query for "best" or "worst" in reviews.content {     "query": {         "match": "best worst",         "field": "reviews.content",         "operator": "or"     } }                                                                                                                                                                                             |
| prefix\_length | Integer | Use the prefix\_length property to modify the behavior of a [match query](#match). The prefix\_length changes a [match query](#match) to a prefix match query. The Search Service matches terms based on the query and the result sharing a prefix of the specified length.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Match query for "location hostel" in reviews.content with a prefix\_length of 4 {     "query": {         "match": "location hostel",         "field": "reviews.content",         "prefix\_length": 4     } }                                                                                                                                                          |

## [](#ctl)Ctl Object

Use the `ctl` object to make sure that the Search Service runs your Search query against the latest version of the documents in your database.

The `ctl` object and its properties cause the Search Service to run your query against the latest version of a document written to a [vBucket](../../current/learn/buckets-memory-and-storage/vbuckets.md). The Search Service uses a consistency vector to synchronize the last document write to a vBucket from the Data Service with the Search index.

```json
    "ctl": {
        "timeout": 10000,
        "consistency": {
            "vectors": {
                "searchIndexName": {
                    "607/205096593892159": 2,
                    "640/298739127912798": 4  
                }
            },
            "level": "at_plus",
            "results": "complete"
        }
    },
```

The `ctl` object contains the following properties:

| Property    | Type    | Required? | Description                                                                                                                                                                                                                                                                   |
| ----------- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timeout     | Integer | No        | Set the maximum time, in milliseconds, that a Search query can execute on a Search index partition. If the query time exceeds the timeout, the Search Service cancels the query. The query might return partial results if any index partitions responded before the timeout. |
| consistency | Object  | Yes       | An object that contains a vectors object and the level and results properties. For more information, see [Consistency Object](#consistency).                                                                                                                                  |

### [](#consistency)Consistency Object

Use the `consistency` object to control the consistency behavior for a Search index:

```json
        "consistency": {
            "vectors": {
                "searchIndexName": {
                    "607/205096593892159": 2,
                    "640/298739127912798": 4  
                }
            },
            "level": "at_plus",
            "results": "complete"
        }
```

A `consistency` object has the following properties:

| Property | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| vectors  | Object | Yes       | An object that contains a {search-index-name} object for each Search index in the query. For more information about the {search-index-name} object, see [{search-index-name} Object](#vectors).                                                                                                                                                                                                                                            |
| level    | String | Yes       | Set the consistency to bounded or unbounded consistency: at\_plus: The Search query executes but requires that the Search index matches the timestamp of the last document update. You must provide a vectors object not\_bounded: The Search query executes without a consistency requirement. not\_bounded is faster than at\_plus, as it doesn’t rely on a vectors object or wait for the Search index to match the Data Service index. |
| results  | String | No        | To display an error instead of partial results if any index partitions are unavailable on a node, set results to complete. To return partial results from a query if a node is unreachable, remove the results property.                                                                                                                                                                                                                   |

#### [](#vectors){search-index-name} Object

Use a `{search-index-name}` object to set the Search index and consistency vectors for a Search query.

The `{search-index-name}` object contains a vBucket mapping and UUID property with the sequence number for each update to a vBucket’s data that you want to include in your search results:

```json
            "vectors": {
                "searchIndexName": {
                    "607/205096593892159": 2,
                    "640/298739127912798": 4  
                }
            },
```

If your Search query uses an [index alias](../../current/search/index-aliases.md) that references multiple Search indexes, you must include a `{search-index-name}` object for each Search index in the alias.

To get the vBucket mapping, UUID, and the sequence number for a data write, use a `MutationToken` from a Data Service `MutationResult`. The Data Service returns a `MutationResult` object or promise for CRUD operations. For more information, see [Work with Documents](../../current/guides/kv-operations.md).

For examples on how to obtain and use a `MutationToken` with the Couchbase SDKs, see:

* [.NET](../../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md#consistency)| [Go](../../../go-sdk/current/howtos/full-text-searching-with-sdk.md#consistency)| [Java](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md#consistency)| [Kotlin](../../../kotlin-sdk/current/howtos/full-text-search.md#scan-consistency)| [Node.js](../../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md#scan-consistency-and-consistentwith)| [PHP](../../../php-sdk/current/howtos/full-text-searching-with-sdk.md#consistency)| [Python](../../../python-sdk/current/howtos/full-text-searching-with-sdk.md#scan-consistency-and-consistent-with)| [Ruby](../../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md#consistency)| [Scala](../../../scala-sdk/current/howtos/full-text-searching-with-sdk.md#consistency)

| Property            | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| {search-index-name} | Object | Yes       | The name of the Search index that you want to search and use with consistency. The {search-index-name} object contains a {vBucketMapping}/{vBucketUUID} property for each document write operation that you want in your search results. Set the value of the property to the sequence number for the write operation. For example, if you had a property of 607/205096593892159": 2, the Search Service looks for a write operation on vBucket 607, with a UUID of 205096593892159, with sequence number 2. |

## [](#highlight)Highlight Object

Use the `highlight` object to control how the Search Service highlights matches in search results.

```json
    "highlight": {

        "style": "html",
        "fields": ["textField"]

    },
```

| Property | Type   | Required? | Description                                                                                                                                                                                                                            |
| -------- | ------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| style    | String | No        | Sets how the Search Service highlights a match from a search query: ansi: The Search Service highlights matches with a yellow background (\\u001b\[43m). html: The Search Service surrounds matches with <mark> and </mark> HTML tags. |
| fields   | Array  | No        | Contains an array of strings for each field name where you want to highlight a search query match. If you include the fields array, the Search Service only highlights fields that are in the array.                                   |

## [](#facet-name){facet-name} Object

Use a `{facet-name}` object to create a search facet.

You can have multiple `{facet-name}` objects inside the [facets object](#facets) in your search query.

```json
    "facets": {

        "field1": {
            "size": 5,
            "field": "field1"
        },

        "field2": {
            "size": 5,
            "field": "field2",
            "numeric_ranges": [
                {

                    "name": "high",
                    "min": 7,
                    "max": 10

                },
                {

                    "name": "low",
                    "min": 0,
                    "max": 7

                }
             ]
        },

        "field3": {
            "size": 10,
            "field": "dateField",
            "date_ranges": [
                {
                    "name": "old",
                    "start": "2020-12-31",
                    "end": "2023-12-31"
                },
                {
                    "name": "new",
                    "start": "2023-12-31",
                    "end": "2024-12-31"
                }  
            ]
        }

    },
```

A `{facet-name}` object contains the following properties:

| Property        | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                               |
| --------------- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| size            | Integer | Yes       | Set the total number of categories to return with the search results for a Term facet. The Search Service orders facet categories from values with the most occurrences to the least occurrences. For Numeric Range and Date Range facets, the total number of categories returned depends on the number of ranges defined for the facet. |
| field           | String  | Yes       | The name of the field to use to collect facet information.                                                                                                                                                                                                                                                                                |
| numeric\_ranges | Array   | No        | If you want to collect a Numeric Range facet, add a numeric\_ranges array. A numeric\_ranges array contains objects that define each numeric range you want to collect with your search results. For more information, see [Numeric\_ranges Array Objects](#numeric).                                                                     |
| date\_ranges    | Array   | No        | If you want to collect a Date Range facet, add a date\_ranges array. A date\_ranges array contains objects that define each date range you want to collect with your search results. For more information, see [Date\_ranges Array Objects](#date).                                                                                       |

### [](#numeric)Numeric\_ranges Array Objects

The objects in a `numeric_ranges` array specify the range or ranges for a Numeric Range facet.

For example, the following `numeric_ranges` array sets two ranges, `high` and `low`, to collect for a Numeric Range facet:

```json
            "numeric_ranges": [
                {

                    "name": "high",
                    "min": 7,
                    "max": 10

                },
                {

                    "name": "low",
                    "min": 0,
                    "max": 7

                }
             ]
```

The Search query increments the `count` property for `high` when the value of the `field` in the [{facet-name} Object](#facet-name) is greater than 7 but less than 10.

If the document’s `field` value is less than 7 but greater than 0, the query increments the `count` value for `low`.

You can set both a `min` and `max` for a range, or just a `min` or `max`.

| Property | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                          |
| -------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name     | String  | Yes       | The name for the numeric range.                                                                                                                                                                                                                                                                                                      |
| min      | Integer | No        | The minimum value to compare against the value of the field in the [{facet-name} Object](#facet-name). If a document’s value for the field is greater than min, the Search Service increments the count value returned in the Search query results. You can also define a max property to set an upper limit for your numeric range. |
| max      | Integer | No        | The maximum value to compare against the value of the field in the [{facet-name} Object](#facet-name). If a document’s value for the field is less than max, the Search Service increments the count value returned in the Search query results. You can also define a min property to set a lower limit for your numeric range.     |

### [](#date)Date\_ranges Array Objects

The objects in a `date_ranges` array specify the range or ranges for a Date Range facet.

For example, the following `date_ranges` array sets two ranges, `old` and `new`, to collect for a Date Range facet:

```json
            "date_ranges": [
                {
                    "name": "old",
                    "start": "2020-12-31",
                    "end": "2023-12-31"
                },
                {
                    "name": "new",
                    "start": "2023-12-31",
                    "end": "2024-12-31"
                }  
            ]
```

The Search query increments the `count` property for `old` when the value of the `field` in the [{facet-name} Object](#facet-name) is later than `2020-12-31` but earlier than `2023-12-31`.

If the document’s `field` value is later than `2023-12-31` but earlier than `2024-12-31`, the query increments the `count` value for `new`.

You can set both a `start` and `end` for a range, or just a `start` or `end`.

| Property | Type                           | Required? | Description                                                                                                                                                                                                                                                                                                                             |
| -------- | ------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name     | String                         | Yes       | The name for the date range.                                                                                                                                                                                                                                                                                                            |
| start    | RFC-3339 formatted Date String | No        | The starting date value to compare against the value of the field in the [{facet-name} Object](#facet-name). If a document’s value for the field is later than start, the Search Service increments the count value returned in the Search query results. You can also define a end property to set an upper limit for your date range. |
| end      | RFC-3339 formatted Date String | No        | The ending date value to compare against the value of the field in the [{facet-name} Object](#facet-name). If a document’s value for the field is earlier than end, the Search Service increments the count value returned in the Search query results. You can also define a start property to set a lower limit for your date range.  |

## [](#sort)Sort Object

Use the `sort` object to control how the Search Service sorts search results.

The following `sort` object orders search results by the values in `field1`, then by `field2`, the document’s score, and then the document’s ID value:

```json
    "sort": [

        "field1",
            {
                "by": "field",
                "field": "field2",
                "desc": false,
                "mode": "max",
                "missing": "last",
                "type": "number"
            },
            "-_score",
            "-_id"
            
    ],
```

The `sort` object can contain the following string values:

| Value         | Description                                                                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {field\_name} | The name of a field in the Search index. The Search Service sorts documents based on the value of the field, in ascending order. To sort in descending order based on a {field-name}, add a hyphen (-) to the start of the field name string. |
| \_id          | The Search Service sorts documents based on their identifier value, in ascending order. To sort in descending order based on a document’s ID value, add a hyphen (-) before the underscore (\_) in the \_id string.                           |
| \_score       | The Search Service sorts documents based on their score value, in ascending order. To sort in descending order based on a document’s score, add a hyphen (-) before the underscore (\_) in the \_score string.                                |

To customize search result sorting beyond ascending and descending values, use a JSON object.

JSON objects in a `sort` object can contain the following properties:

| Property | Type    | Required? | Description                                                                                                                                                                                                                                                                                      |
| -------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| by       | String  | Yes       | Sets what value to use for the sort: id: Uses the document’s ID value. score: Uses the document’s score. field: Uses the value of a specific field to sort. See [field](#field).                                                                                                                 |
| field    | String  | No        | When by is set to field, specify the name of the field to use to sort search results.                                                                                                                                                                                                            |
| desc     | Boolean | Yes       | To sort the values in the field in descending order, set desc to true. To sort the values in the field in ascending order, set desc to false.                                                                                                                                                    |
| mode     | String  | Yes       | Set the order for search results when the field contains multiple values, such as an array: default: Use the first value in the field as the sort key. min: Use the smallest value in the field as the sort key. max: Use the largest value in the field as the sort key.                        |
| missing  | String  | Yes       | Set how the Search Service sorts documents that do not have a value for the field specified in field: first: Documents with a missing value appear first and before other results in search results. last: Documents with a missing value appear last and after other results in search results. |
| type     | String  | Yes       | Set the data type of the field specified in field: string: The field contains a string. date: The field contains date/time data. number: The field contains a number or geographic data, like a latitude or longitude value.                                                                     |
| unit     | String  | No        | When running a [Geopoint Distance/Radius query](#geopoint-queries-distance), you can set the unit of distance to use when sorting documents. The unit of distance does not have to match the unit specified in the [query object](#query-object).                                                |