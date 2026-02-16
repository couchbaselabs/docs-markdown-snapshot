[View original HTML](/server/current/search/search-facets.html)

> Use Search facets to collect specific, additional information about the documents included in results for a specific search query. 

The Search Service supports the following facet types:

* [Term Facet](#term-facet)
* [Numeric Range Facet](#numeric-range-facet)
* [Date Range Facet](#date-range-facet)

## [](#term-facet)Term Facet

Use a term facet to return a count for the number of documents in your search results that have a specific term in a field.

|  | For best results with a term facet, use the [keyword analyzer](default-analyzers-reference.md#keyword) on the field you want to use for the facet. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------- |

Term facets work best when you have a field with a limited range of values, such as a type or tags field.

For example, the following Search request searches for the word `water` in the Search index, and calculates a term facet for the value of the `country` field:

```console
curl -X POST -H "Content-Type: application/json" \
http://{HOSTNAME}:8094/api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}/query -d \
'{
    "size": 10,
    "query": {
        "boost": 1,
        "query": "water"
     },
    "facets": {
         "country": {
             "size": 5,
             "field": "country"
         }
    }
}'
```

At the end of your search results, the Search Service would return the following object with the term facet information:

```json
"facets": {
    "country": {
        "field": "country",
        "total": 94,
        "missing": 0,
        "other": 0,
        "terms": [
            {
                "term": "United States",
                "count": 46
            },
            {
                "term": "United Kingdom",
                "count": 42
            },
            {
                "term": "France",
                "count": 6
            }
        ]
    }
}
```

Term facet results include the following information, under the named facet object you created in your query:

| Key     | Description                                                                                                                                                                                                                                                                                                                                                 |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| field   | The name of the field where the Search Service collected facet information.                                                                                                                                                                                                                                                                                 |
| total   | The total number of values checked for returning the facet. If every document had a single term, this value would be the total number of documents returned in your search results. This can change if you have multiple partitions in your Search index, or your size parameter is not large enough to accommodate all of the unique terms for your facet. |
| missing | The number of documents in your search results that did not have a value in the field you specified for the facet.                                                                                                                                                                                                                                          |
| other   | The number of documents in your search results that did have a value in the field you specified, but did not fit within the size parameter for the facet.                                                                                                                                                                                                   |
| terms   | The unique terms found for the facet. Includes the specific term and the count of how many documents had that term in your specified field.                                                                                                                                                                                                                 |

[Run a search with the Server Web Console](simple-search-ui.md) to view facet information in a table format.

For more information about how to configure a term facet in your Search query, see [facets](search-request-params.md#facets) or [{facet-name} Object](search-request-params.md#facet-name).

## [](#numeric-range-facet)Numeric Range Facet

Use a numeric range facet to define a numeric range and receive the number of documents with a field value that falls within that range.

|  | For best results with a numeric range facet, use a field with a number type in your documents. |
|  | ---------------------------------------------------------------------------------------------- |

For example, you could define numeric range facets to collect information about the ABV values for different beers in the `beer-sample` sample data:

* You could define a numeric range facet, `high`, for ABV values greater than 7.
* You could define another numeric range facet, `low`, for ABV values less than 7.

You could define a `min` and `max` for every numeric range, or just the `min` or `max` value.

The curl request for your query and the specific facet information would be:

```console
curl -X POST -H "Content-Type: application/json" \
http://{HOSTNAME}:8094/api/bucket/beer-sample/scope/_default/index/beer-index/query -d \
'{
    "size": 10,
    "query": {
        "boost": 1,
        "query": "water"
    },
    "facets": {
        "abv": {
            "size": 5,
            "field": "abv",
            "numeric_ranges": [
                {
                    "name": "high",
                    "min": 7
                },
                {
                    "name": "low",
                    "max": 7
                }
             ]
        }
    }
}'
```

At the end of your search results, the Search Service would return the following object with the numeric range facet information:

```json
"facets": {
    "abv": {
        "field": "abv",
        "total": 70,
        "missing": 21,
        "other": 0,
        "numeric_ranges": [
            {
                "name": "low",
                "max": 7,
                "count": 57
            },
            {
                "name": "high",
                "min": 7,
                "count": 13
            }
        ]
    }
}
```

Numeric range facet results include the following information, under the named facet object you created in your query:

| Key             | Description                                                                                                                                                                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| field           | The name of the field where the Search Service collected facet information.                                                                                                                                                                                                                                  |
| total           | The total number of values checked for returning the facet. This value should be the total number of documents returned in your search results. This can change if you have multiple partitions in your Search index, or your size parameter is not large enough to accommodate all of the facet categories. |
| missing         | The number of documents in your search results that did not have a value in the field you specified for the facet.                                                                                                                                                                                           |
| other           | The number of documents in your search results that did have a value in the field you specified, but did not fit within the size parameter for the facet.                                                                                                                                                    |
| numeric\_ranges | Includes an object for each numeric range you defined in your facet. Each object includes the name of the numeric range, the min and max values that defined the range, and the number of documents that had a value that matched that range.                                                                |

[Run a search with the Server Web Console](simple-search-ui.md) to view facet information in a table format.

For more information about how to configure a numeric range facet in your Search query, see:

* [facets](search-request-params.md#facets)
* [{facet-name} Object](search-request-params.md#facet-name)
* [numeric\_ranges Array Objects](search-request-params.md#numeric)

## [](#date-range-facet)Date Range Facet

Use a date range facet to define a date range and receive the number of documents with a date field value that falls within that range.

|  | For best results with a date range facet, use a field with the datetime type in your documents. Make sure to use a [date/time parser](customize-index.md#date-time) that matches your date and time data. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

For example, you could define date range facets to collect information about the last time a document was updated in the `beer-sample` sample data:

* You could define a date range facet, `new`, for dates later than August 1st, 2010.
* You could define another numeric range facet, `old`, for dates earlier than August 1st, 2010.

You could define a `start` and `end` for every numeric range, or just the `start` or `end` value.

The curl request for your query and the specific facet information would be:

```console
curl -X POST -H "Content-Type: application/json" \
http://{HOSTNAME}:8094/api/bucket/beer-sample/scope/_default/index/beer-index/query -d \
'{
    "query": {
        "field": "country",
        "term": "united"
    },
    "facets": {
        "updated": {
            "size": 10,
            "field": "updated",
            "date_ranges": [
                {
                "name": "old",
                "end": "2010-08-01"
                },
                {
                "name": "new",
                "start": "2010-08-01"
                }
            ]
        }
    }
}'
```

At the end of your search results, the Search Service would return the following object with the date range facet information:

```json
"facets": {
    "updated": {
        "field": "updated",
        "total": 954,
        "missing": 0,
        "other": 0,
        "date_ranges": [
            {
                "name": "old",
                "end": "2010-08-01T00:00:00Z",
                "count": 934
            },
            {
                "name": "new",
                "start": "2010-08-01T00:00:00Z",
                "count": 20
            }
        ]
    }
}
```

Date range facet results include the following information, under the named facet object you created in your query:

| Key          | Description                                                                                                                                                                                                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| field        | The name of the field where the Search Service collected facet information.                                                                                                                                                                                                                                  |
| total        | The total number of values checked for returning the facet. This value should be the total number of documents returned in your search results. This can change if you have multiple partitions in your Search index, or your size parameter is not large enough to accommodate all of the facet categories. |
| missing      | The number of documents in your search results that did not have a value in the field you specified for the facet.                                                                                                                                                                                           |
| other        | The number of documents in your search results that did have a value in the field you specified, but did not fit within the size parameter for the facet.                                                                                                                                                    |
| date\_ranges | Includes an object for each date range you defined in your facet. Each object includes the name of the date range, the start and end values that defined the range, and the number of documents that had a value that matched that range.                                                                    |

[Run a search with the Server Web Console](simple-search-ui.md) to view facet information in a table format.

For more information about how to configure a date range facet in your Search query, see:

* [facets](search-request-params.md#facets)
* [{facet-name} Object](search-request-params.md#facet-name)
* [date\_ranges Array Objects](search-request-params.md#date)

## [](#next-steps)Next Steps

For more information about how to structure a Search query, see [Search Request JSON Properties](search-request-params.md).