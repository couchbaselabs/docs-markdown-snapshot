---
title: Search Index JSON Properties
description: Use a JSON payload to control the settings for a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/search-index-params.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/search/search-index-params.html)

# Search Index JSON Properties

> Use a JSON payload to control the settings for a Search index. 

You can choose to create a Search index with a JSON payload, and [import it through the Capella UI](import-search-index.md). This JSON payload sets all the settings for your new Search index.

Your JSON payload must contain the properties described in [Initial Settings](#initial), including the [Params Object](#params).

[Search index aliases](index-aliases.md) only need to include the properties described in [Initial Settings](#initial).

## [](#initial)Initial Settings

The start of the JSON payload for a Search index contains important settings for your index:

```json
{
    "name": "gfx",
    "type": "fulltext-index",
    "uuid": "28b999e9e17dd4a7",
    "sourceType": "gocbcore",
    "sourceName": "travel-sample",
    "sourceUUID": "d3604c0ec4792b4c6c5f7f2cc8207b80",
    "sourceParams": {},
    "planParams": {
        "maxPartitionsPerPIndex": 1024,
        "indexPartitions": 1,
        "numReplicas": 0
    },
    "params": {
```

> [!TIP]
> To view the entire JSON payload, click **View**.

All Search index payloads have the following properties:

| Property     | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name         | String | Yes       | The name of the Search index. A Search index name must be unique for each cluster.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| type         | String | Yes       | The type of index you want to create: fulltext-index: Create a Search index. fulltext-alias: Create an alias for a Search index. For more information about Search index aliases, see [Create Search Index Aliases](index-aliases.md).                                                                                                                                                                                                                                                              |
| uuid         | String | No        | The UUID for the Search index. The Search Service automatically generates a UUID for a Search index. If you use an existing UUID, the Search Service updates the existing Search index. Do not include the uuid property when you want to copy an index to a different cluster or create a new index. View the UUID for an existing index from the Capella UI by selecting an existing index and clicking **Index Definition**. The UUID displays in the Index Definition on the Update Index page. |
| sourceType   | String | Yes       | The sourceType is always "gocbcore" for a Search index. For a [Search index alias](index-aliases.md), it’s "nil".                                                                                                                                                                                                                                                                                                                                                                                   |
| sourceName   | String | Yes       | The name of the bucket where you want to create the Search index. Do not include a sourceName for a Search index alias.                                                                                                                                                                                                                                                                                                                                                                             |
| sourceUUID   | String | No        | The UUID of the bucket where you want to create the Search index. The Search Service automatically finds the UUID for the bucket. Do not include the sourceUUID property when you want to copy an index to a different cluster, or create a new index.                                                                                                                                                                                                                                              |
| sourceParams | Object | No        | This object contains advanced settings for index behavior. Do not add content into this object unless instructed by Couchbase Support.                                                                                                                                                                                                                                                                                                                                                              |
| planParams   | Object | Yes       | An object that sets the Search index’s partitions and replications. For more information, see [planParams Object](#planparams). Do not include any of the properties in a planParams object for a [Search index alias](index-aliases.md).                                                                                                                                                                                                                                                           |
| params       | Object | Yes       | An object that sets the Search index’s type identifier, type mappings, and analyzers. For more information, see [Params Object](#params). For a [Search index alias](index-aliases.md), this object contains the [targets object](#targets).                                                                                                                                                                                                                                                        |
| store        | Object | No        | An object that controls merge policy, concurrent persister behavior, and file format version for the Search index. The Search Service can automatically set these to reasonable default values, based on the other settings in your Search index definition. For more information, see [Store Object](#store).                                                                                                                                                                                      |

## [](#planparams)planParams Object

> [!NOTE]
> Do not include any of the properties in a `planParams` object for a [Search index alias](index-aliases.md).

The `planParams` object sets a Search index’s partition and replication settings:

```json
    "planParams": {
        "maxPartitionsPerPIndex": 1024,
        "indexPartitions": 1,
        "numReplicas": 0
    },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `planParams` object contains the following properties:

| Property               | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxPartitionsPerPIndex | n/a     | No        | This setting is deprecated. Use indexPartitions, instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| indexPartitions        | Integer | Yes       | The number of partitions to split the Search index into, across the nodes you have available in your cluster with the Search Service enabled. Use index partitions to increase index and query performance on large datasets. The scoring calculation for regular Search queries can be affected by the number of partitions in your Search index, and how the Search Service distributes documents across partitions. This is a limitation of the [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) weighting scheme. |
| numReplicas            | Integer | Yes       | For high-availability, set the number of replicas the Search Service creates for the Search index. You can create up to three replicas for a Search index. Each replica creates a full copy of the Search index to increase high-availability. To turn off replication for the Search index, set numReplicas to 0. The number of replicas you can create depends on the number of nodes you have available with the Search Service enabled.                                                                                 |

## [](#params)Params Object

The `params` object sets a Search index’s [type identifier](customize-index.md#type-identifiers), [type mappings](customize-index.md#type-mappings), and [analyzers](customize-index.md#analyzers).

For a [Search index alias](index-aliases.md), it includes a JSON object for each Search index to include in the alias.

It contains the following properties:

| Property    | Type   | Required?        | Description                                                                                                                                                                                                                                          |
| ----------- | ------ | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| doc\_config | Object | Yes              | An object that sets how the Search index sets a document’s type. For more information, see [Doc\_config Object](#doc-config).                                                                                                                        |
| mapping     | Object | Yes              | An object that sets the analyzers and type mappings for a Search index. For more information, see [Mapping Object](#mapping).                                                                                                                        |
| targets     | Object | Index Alias Only | An object that contains JSON objects for each Search index to add to the alias definition. The key for each JSON object must be the fully qualified name of each Search index. For example: "targets": {     "vector-sample.color.color-index": {} } |

### [](#doc-config)Doc\_config Object

The `doc_config` object sets how the Search index sets a document’s type:

```json
        "doc_config": {
            "docid_prefix_delim": "",
            "docid_regexp": "",
            "mode": "scope.collection.custom",
            "type_field": "type",
            "doc_filter": {
                "free_breakfast_true": {
                    "bool": true,
                    "field": "free_breakfast",
                    "order": 1
                },
                "review_date_range": {
                    "start": "2015-01-01",
                    "end": "2019-01-01",
                    "inclusive_end": true,
                    "inclusive_start": false,
                    "field": "reviews.date",
                    "order": 2,
                    "datetime_parser": "My_Date_Time_Parser"
                },
                "cleanliness_range": {
                    "min": 3,
                    "max": 5,
                    "inclusive_min": true,
                    "inclusive_max": true,
                    "field": "reviews.ratings.Cleanliness",
                    "order": 3
                },
                "free_parking_AND_vacancy": {
                    "conjuncts": [
                        {
                            "bool": true,
                            "field": "vacancy"
                        },
                        {
                            "bool": true,
                            "field": "free_parking"
                        }
                    ],
                    "order": 4
                },
                "location_OR_service": {
                    "disjuncts": [
                        {
                            "min": 5,
                            "field": "reviews.ratings.Service"
                        },
                        {
                            "min": 5,
                            "field": "reviews.ratings.Location"
                        }
                    ],
                    "order": 6
                },
                "name_hotel": {
                    "term": "Hotel",
                    "order": 5,
                    "field": "name"
                }

            }
        },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `doc_config` object is a child object of the [Params Object](#params). It contains the following properties:

| Property             | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mode                 | String | Yes       | Set a [type identifier](customize-index.md#type-identifiers) for the Search index to filter documents. Set the mode for your type identifier by setting this property to "scope.collection.{mode}"You can choose from one of the following mode values: type\_field: Use the value from a specific field in the documents. docid\_prefix\_delim: Use the leading characters in the documents' ID values, up to but not including a specified separator. docid\_regexp: Use a regular expression on the documents' ID values. custom: Use a custom document filter expression to filter documents based on specific values. See [doc\_filter](#doc%5Ffilter).                                                                                                                                     |
| docid\_prefix\_delim | String | Yes       | If mode is docid\_prefix\_delim, set the separator character to use on a document’s ID value. For example, to filter documents based on the characters before a \_ in their ID values, set docid\_prefix\_delim to \_. To use this filter later, you need to modify the name of the type mapping where you want to use the filter. For example, you could set a specific filter value of hotel on a type mapping. If docid\_prefix\_delim is set to \_, a document would have to have the string hotel before the character \_ in its ID value to pass the filter. To use the filter, set the [{scope}.{collection} object](#scope-collection) name to {scope}.{collection}.hotel. If the document passes the filter, it’s included in the type mapping, and your Search index.                  |
| docid\_regexp        | String | Yes       | If mode is docid\_regexp, set the regular expression to use on a document’s ID value to determine its type. For example, to filter documents that contain the characters \_40 in their ID value, set docid\_regexp to \_\[3-5\]0. To use this filter later, you need to modify the name of the type mapping where you want to use the filter. For example, you could set a specific filter value of \_40 on a type mapping. A document with the characters \_40 in its ID value would pass the filter. To use the filter, set the [{scope}.{collection} object](#scope-collection) name to {scope}.{collection}.\_40. If the document passes the filter, it’s included in the type mapping, and your Search index.                                                                               |
| type\_field          | String | Yes       | If mode is type\_field, set the name of the field to use to filter documents. For example, to filter documents based on the value of their type field, set type\_field to type. To use this filter later, you need to modify the name of the type mapping where you want to use the filter. For example, you could use a field called type as your type\_field. To use the filter, set your [{scope}.{collection} object](#scope-collection) name to {scope}.{collection}.landmark. With type as the type\_field and landmark as the configured filter, a document would have to have landmark in its type field to pass the filter.                                                                                                                                                             |
| doc\_filter          | Object | Yes       | Couchbase Server 8.0 If mode is custom, provide an object that sets a custom document filter for a scope and collection in your Search index. You can filter documents with custom filters based on the value of: [A boolean field](#boolean%5Ffilter). [A date field, within a specific range](#date%5Frange%5Ffilter). [A numeric field, within a specific range](#numeric%5Frange%5Ffilter). [A term in a text field](#term%5Ffilter). A [conjunct](#conjunct%5Ffilter) or [disjunct](#disjunct%5Ffilter) object that combines 2 or more of the available filters. You can add up to a maximum of 100 document filters on a single Search index. For more information about how to define each type of filter in your Search index definition, see [Doc\_filter Object](#doc%5Ffilter%5Fobj). |

#### [](#doc%5Ffilter%5Fobj)Doc\_filter Object

Couchbase Server 8.0

The `doc_filter` object contains JSON objects for each document filter you want to apply to a type mapping in your Search index:

```json
            "doc_filter": {
                "free_breakfast_true": {
                    "bool": true,
                    "field": "free_breakfast",
                    "order": 1
                },
                "review_date_range": {
                    "start": "2015-01-01",
                    "end": "2019-01-01",
                    "inclusive_end": true,
                    "inclusive_start": false,
                    "field": "reviews.date",
                    "order": 2,
                    "datetime_parser": "My_Date_Time_Parser"
                },
                "cleanliness_range": {
                    "min": 3,
                    "max": 5,
                    "inclusive_min": true,
                    "inclusive_max": true,
                    "field": "reviews.ratings.Cleanliness",
                    "order": 3
                },
                "free_parking_AND_vacancy": {
                    "conjuncts": [
                        {
                            "bool": true,
                            "field": "vacancy"
                        },
                        {
                            "bool": true,
                            "field": "free_parking"
                        }
                    ],
                    "order": 4
                },
                "location_OR_service": {
                    "disjuncts": [
                        {
                            "min": 5,
                            "field": "reviews.ratings.Service"
                        },
                        {
                            "min": 5,
                            "field": "reviews.ratings.Location"
                        }
                    ],
                    "order": 6
                },
                "name_hotel": {
                    "term": "Hotel",
                    "order": 5,
                    "field": "name"
                }

            }
```

> [!TIP]
> To view the entire JSON payload, click **View**.

You can add up to a maximum of 100 document filters on a single Search index.

You can define the following types of document filters:

* [Boolean Document Filters](#boolean%5Ffilter)
* [Date Range Document Filters](#date%5Frange%5Ffilter)
* [Numeric Range Document Filters](#numeric%5Frange%5Ffilter)
* [Term Document Filters](#term%5Ffilter)
* [Conjunct Document Filter](#conjunct%5Ffilter)
* [Disjunct Document Filter](#disjunct%5Ffilter)

##### [](#boolean%5Ffilter)Boolean Document Filters

Couchbase Server 8.0

A boolean document filter adds or removes documents from a type mapping based on the value of a boolean field:

```json
                "free_breakfast_true": {
                    "bool": true,
                    "field": "free_breakfast",
                    "order": 1
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

Set the name of your boolean document filter object to the name you want for your filter. Use this name to use the filter on a [{scope}.{collection} object](#scope-collection). For example, `{scope}.{collection}.free_breakfast_true`.

A boolean document filter can have the following properties:

| Property | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| bool     | Boolean | Yes       | Set bool to the value a document must have in your chosen boolean field for a document to pass the filter. bool can be true or false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| field    | String  | Yes       | Enter the name of the field that contains a boolean value you want to use as a filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| order    | Number  | Yes       | Set the filtering order for this document filter, compared to the other document filters in use on the Search index. The Search Service applies document filters on type mappings in the order you specify. For example, if a document does not pass a type mapping filter where "order": 1, the Search Service checks the document against the filter with "order": 2. The Search Service continues checking documents against any filters defined on type mappings in your Search index until a document passes a filter, or there are no more defined type mapping filters. If a document does not pass any defined filters, it’s not included in your Search index. If you’re defining a document filter inside a conjuncts or disjuncts array, you do not need to include the order property for each filter object. Add the order property to the conjuncts or disjuncts filter object, instead. |

##### [](#date%5Frange%5Ffilter)Date Range Document Filters

Couchbase Server 8.0

A date range document filter adds or removes documents from a type mapping based on the value of a date field and a specified range:

```json
                "review_date_range": {
                    "start": "2015-01-01",
                    "end": "2019-01-01",
                    "inclusive_end": true,
                    "inclusive_start": false,
                    "field": "reviews.date",
                    "order": 2,
                    "datetime_parser": "My_Date_Time_Parser"
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

Set the name of your date range document filter object to the name you want for your filter. Use this name to use the filter on a [{scope}.{collection} object](#scope-collection). For example, `{scope}.{collection}.review_date_range`.

A date range document filter can have the following properties:

| Property         | Type                 | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------- | -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| start            | Date and Time String | No        | Set the start date for the range you want to use as a filter. Dates occurring before your start value do not pass the filter. You can choose to set only a start value or only an end value for the filter. By default, the value for start is included in your date range filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| end              | Date and Time String | No        | Set the end date for the range you want to use as a filter. Dates occurring after your end value do not pass the filter. You can choose to set only a start value or only an end value for the filter. By default, the value for end is excluded from your date range filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| inclusive\_start | Boolean              | No        | Set whether the value of start should be included or excluded from the range: If inclusive\_start is true, documents with the same date and time string as start pass the filter. If inclusive\_start is false, documents must have a date and time string that’s later than the value of start to pass the filter. If you do not set a value for inclusive\_start, by default, start is inclusive to your date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| inclusive\_end   | Boolean              | No        | Set whether the value of end should be included or excluded from the range: If inclusive\_end is true, documents with the same date and time string as end pass the filter. If inclusive\_end is false, documents must have a date and time string that’s earlier than the value of end to pass the filter. If you do not set a value for inclusive\_end, by default, end is not included in your date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| field            | String               | Yes       | Enter the name of the field that contains a date value you want to use as a filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| order            | Number               | Yes       | Set the filtering order for this document filter, compared to the other document filters in use on the Search index. The Search Service applies document filters on type mappings in the order you specify. For example, if a document does not pass a type mapping filter where "order": 1, the Search Service checks the document against the filter with "order": 2. The Search Service continues checking documents against any filters defined on type mappings in your Search index until a document passes a filter, or there are no more defined type mapping filters. If a document does not pass any defined filters, it’s not included in your Search index. If you’re defining a document filter inside a conjuncts or disjuncts array, you do not need to include the order property for each filter object. Add the order property to the conjuncts or disjuncts filter object, instead. |
| datetime\_parser | String               | No        | Enter the name of the date/time parser you want to use to interpret your date and time strings. You can use a [default date/time parser](default-date-time-parsers-reference.md) or reference a date/time parser from the [Date\_time\_parsers Object](#date%5Ftime%5Fparsers).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

##### [](#numeric%5Frange%5Ffilter)Numeric Range Document Filters

Couchbase Server 8.0

A numeric range document filter adds or removes documents from a type mapping based on the value of a numeric field and a specified range:

```json
                "cleanliness_range": {
                    "min": 3,
                    "max": 5,
                    "inclusive_min": true,
                    "inclusive_max": true,
                    "field": "reviews.ratings.Cleanliness",
                    "order": 3
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

Set the name of your numeric range document filter object to the name you want for your filter. Use this name to use the filter on a [{scope}.{collection} object](#scope-collection). For example, `{scope}.{collection}.cleanliness_range`.

A numeric range document filter can have the following properties:

| Property       | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| min            | Number  | No        | Set the minimum value for the range you want to use as a filter. Values smaller than your min value do not pass the filter. You can choose to set only a min value or only a max value for the filter. By default, the value for min is included in your numeric range filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| max            | Number  | No        | Set the maximum value for the range you want to use as a filter. Values larger than your max value do not pass the filter. You can choose to set only a min value or only a max value for the filter. By default, the value for max is excluded from your numeric range filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| inclusive\_min | Boolean | No        | Set whether the value of min should be included or excluded from the range: If inclusive\_min is true, documents with the same value as min pass the filter. If inclusive\_min is false, documents must have a value that’s larger than the value of min to pass the filter. If you do not set a value for inclusive\_min, by default, min is inclusive to your numeric range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| inclusive\_max | Boolean | No        | Set whether the value of max should be included or excluded from the range: If inclusive\_max is true, documents with the same value as max pass the filter. If inclusive\_max is false, documents must have a value that’s smaller than the value of max to pass the filter. If you do not set a value for inclusive\_max, by default, max is not included in your numeric range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| field          | String  | Yes       | Enter the name of the field that contains a numeric value you want to use as a filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| order          | Number  | Yes       | Set the filtering order for this document filter, compared to the other document filters in use on the Search index. The Search Service applies document filters on type mappings in the order you specify. For example, if a document does not pass a type mapping filter where "order": 1, the Search Service checks the document against the filter with "order": 2. The Search Service continues checking documents against any filters defined on type mappings in your Search index until a document passes a filter, or there are no more defined type mapping filters. If a document does not pass any defined filters, it’s not included in your Search index. If you’re defining a document filter inside a conjuncts or disjuncts array, you do not need to include the order property for each filter object. Add the order property to the conjuncts or disjuncts filter object, instead. |

##### [](#term%5Ffilter)Term Document Filters

Couchbase Server 8.0

A term document filter adds or removes documents from a type mapping based on the existence of a term in a specified document field:

```json
                "name_hotel": {
                    "term": "Hotel",
                    "order": 5,
                    "field": "name"
                }
```

> [!TIP]
> To view the entire JSON payload, click **View**.

Set the name of your term document filter object to the name you want for your filter. Use this name to use the filter on a [{scope}.{collection} object](#scope-collection). For example, `{scope}.{collection}.name_hotel`.

A term document filter can have the following properties:

| Property | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| term     | String | Yes       | Enter a string that must exist inside field for a document to pass the filter. The string must be an exact match for a document to pass.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| field    | String | Yes       | Enter the name of the field where you want to search for the value of term.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| order    | Number | Yes       | Set the filtering order for this document filter, compared to the other document filters in use on the Search index. The Search Service applies document filters on type mappings in the order you specify. For example, if a document does not pass a type mapping filter where "order": 1, the Search Service checks the document against the filter with "order": 2. The Search Service continues checking documents against any filters defined on type mappings in your Search index until a document passes a filter, or there are no more defined type mapping filters. If a document does not pass any defined filters, it’s not included in your Search index. If you’re defining a document filter inside a conjuncts or disjuncts array, you do not need to include the order property for each filter object. Add the order property to the conjuncts or disjuncts filter object, instead. |

##### [](#conjunct%5Ffilter)Conjunct Document Filter

Couchbase Server 8.0

A conjunct document filter can contain any number of the other document filter types:

* [Boolean Document Filters](#boolean%5Ffilter)
* [Date Range Document Filters](#date%5Frange%5Ffilter)
* [Numeric Range Document Filters](#numeric%5Frange%5Ffilter)
* [Term Document Filters](#term%5Ffilter)
* [Conjunct Document Filter](#conjunct%5Ffilter)
* [Disjunct Document Filter](#disjunct%5Ffilter)A document must pass every filter inside the `conjuncts` array to pass a conjunct document filter and be included in a type mapping:

```json
                "free_parking_AND_vacancy": {
                    "conjuncts": [
                        {
                            "bool": true,
                            "field": "vacancy"
                        },
                        {
                            "bool": true,
                            "field": "free_parking"
                        }
                    ],
                    "order": 4
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

Set the name of your conjunct document filter object to the name you want for your filter. Use this name to use the filter on a [{scope}.{collection} object](#scope-collection). For example, `{scope}.{collection}.free_parking_AND_vacancy`.

A conjunct document filter can have the following properties:

| Property  | Type             | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------- | ---------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| conjuncts | Array of Objects | Yes       | Add an object to define each filter you want a document to pass before a document can be included in a type mapping. The conjuncts array can contain any other document filter type, including additional conjunct and disjunct document filters. You cannot nest more than 5 conjunct or disjunct document filters inside a single filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| order     | Number           | Yes       | Set the filtering order for this document filter, compared to the other document filters in use on the Search index. The Search Service applies document filters on type mappings in the order you specify. For example, if a document does not pass a type mapping filter where "order": 1, the Search Service checks the document against the filter with "order": 2. The Search Service continues checking documents against any filters defined on type mappings in your Search index until a document passes a filter, or there are no more defined type mapping filters. If a document does not pass any defined filters, it’s not included in your Search index. If you’re defining a document filter inside a conjuncts or disjuncts array, you do not need to include the order property for each filter object. Add the order property to the conjuncts or disjuncts filter object, instead. |

##### [](#disjunct%5Ffilter)Disjunct Document Filter

Couchbase Server 8.0

A disjunct document filter can contain any number of the other document filter types:

* [Boolean Document Filters](#boolean%5Ffilter)
* [Date Range Document Filters](#date%5Frange%5Ffilter)
* [Numeric Range Document Filters](#numeric%5Frange%5Ffilter)
* [Term Document Filters](#term%5Ffilter)
* [Conjunct Document Filter](#conjunct%5Ffilter)
* [Disjunct Document Filter](#disjunct%5Ffilter)A document must pass at least the number of filters you specify as `min` from the `disjuncts` array to pass the filter and be included in a type mapping:

```json
                "location_OR_service": {
                    "disjuncts": [
                        {
                            "min": 5,
                            "field": "reviews.ratings.Service"
                        },
                        {
                            "min": 5,
                            "field": "reviews.ratings.Location"
                        }
                    ],
                    "order": 6
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

Set the name of your disjunct document filter object to the name you want for your filter. Use this name to use the filter on a [{scope}.{collection} object](#scope-collection). For example, `{scope}.{collection}.location_OR_service`.

A disjunct document filter can have the following properties:

| Property  | Type             | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------- | ---------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| disjuncts | Array of Objects | Yes       | Add an object to define each filter you want to run against a document for this disjunct document filter. The disjuncts array can contain any other document filter type, including additional conjunct and disjunct document filters. You cannot nest more than 5 conjunct or disjunct document filters inside a single filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| min       | Number           | Yes       | Set min to the minimum number of filters from disjuncts that a document must pass to be included in a type mapping.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| order     | Number           | Yes       | Set the filtering order for this document filter, compared to the other document filters in use on the Search index. The Search Service applies document filters on type mappings in the order you specify. For example, if a document does not pass a type mapping filter where "order": 1, the Search Service checks the document against the filter with "order": 2. The Search Service continues checking documents against any filters defined on type mappings in your Search index until a document passes a filter, or there are no more defined type mapping filters. If a document does not pass any defined filters, it’s not included in your Search index. If you’re defining a document filter inside a conjuncts or disjuncts array, you do not need to include the order property for each filter object. Add the order property to the conjuncts or disjuncts filter object, instead. |

### [](#mapping)Mapping Object

The `mapping` object contains a Search index’s [analyzers](customize-index.md#analyzers) and other global index settings. Some of these settings map to [Global Index Settings in the UI](create-search-index-ui.md#configure-settings):

```json
        "mapping": {
            "analysis": {
                "analyzers": {
                    "My_Analyzer": {
                        "token_filters": [
                            "apostrophe",
                            "My_Token_Filter"
                        ],
                        "char_filters": [
                            "asciifolding",
                            "html",
                            "My_Char_Filter"
                        ],
                        "type": "custom",
                        "tokenizer": "My_Tokenizer_Excep"
                    }
                },
                "char_filters": {
                    "My_Char_Filter": {
                        "regexp": "[']",
                        "replace": " ",
                        "type": "regexp"
                    }
                },
                "tokenizers": {
                    "My_Tokenizer_Excep": {
                        "exceptions": [
                            "[*]"
                        ],
                        "tokenizer": "unicode",
                        "type": "exception"
                    },
                    "My_Tokenizer_RegExp": {
                        "regexp": "[*]",
                        "type": "regexp"
                    }
                },
                "token_filters": {
                    "My_Token_Filter": {
                        "min": 3,
                        "max": 255,
                        "type": "length"
                    }
                },
                "token_maps": {
                    "My_Wordlist": {
                        "type": "custom",
                        "tokens": [
                            "the",
                            "is",
                            "and"
                        ]
                    }
                },
                "date_time_parsers": {
                    "My_Date_Time_Parser": {
                        "type": "flexiblego",
                        "layouts": [
                            "RFC850"
                        ]
                    }
                },
                "synonym_sources": {
                    "synonyms_en": {
                        "analyzer": "My_Analyzer",
                        "collection": "synonyms_en"
                    }
                }
            },
            "default_analyzer": "standard",
            "default_datetime_parser": "dateTimeOptional",
            "default_field": "_all",
            "default_mapping": {
                "dynamic": false,
                "enabled": false
            },
            "default_type": "_default",
            "docvalues_dynamic": true,
            "index_dynamic": true,
            "scoring_model": "bm25",
            "store_dynamic": true,
            "type_field": "_type",
            "types": {
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `mapping` object is a child object of the [Params Object](#params). It contains the following properties:

| Property                  | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| analysis                  | Object  | Yes       | An object that contains the following child objects: [Analyzers Object](#analyzers) [Char\_filters Object](#char%5Ffilters) [Tokenizers Object](#tokenizers) [Token\_filters Object](#token%5Ffilters) [Token\_maps Object](#token%5Fmaps) [Date\_time\_parsers Object](#date%5Ftime%5Fparsers) [Synonym\_sources Object](#synonym%5Fsources)                                                                                                                                                                                                                                                                            |
| default\_analyzer         | String  | Yes       | The name of the default analyzer to use for the Search index. For more information about analyzers, see [Analyzers](customize-index.md#analyzers).                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| default\_datetime\_parser | String  | Yes       | The name of the default date/time parser to use for the Search index. For more information about date/time parsers, see [Date/Time Parsers](customize-index.md#date-time).                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| default\_field            | String  | Yes       | Set a name for the all field in the Search index. If you enable the [include\_in\_all property](#include-in-all) for a document field, the contents of that document field can be searched without specifying a field name or by specifying the default field’s name in your Search query.                                                                                                                                                                                                                                                                                                                               |
| default\_mapping          | Object  | No        | An object that contains settings for the default type mapping on the Search index. The default type mapping contains all documents under the \_default scope and \_default collection in the bucket. This type mapping is included for compatibility only. For more information about the properties inside the default\_mapping object, see [Default\_mapping Object](#default-mapping).                                                                                                                                                                                                                                |
| default\_synonym\_source  | String  | No        | Couchbase Server 8.0 The name of the default synonym source to use for the Search index. The value of default\_synonym\_source must match a defined [{synonym\_collection\_name} Object](#synonym%5Fname) in your Search index definition. For more information about using synonyms with the Search Service, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md).                                                                                                                                                                                                                                         |
| default\_type             | String  | No        | This setting is included for compatibility with earlier indexes only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| docvalues\_dynamic        | Boolean | Yes       | To include the value for each instance of an indexed field in the Search index to support [facets](search-request-params.md#facet-name) and sorting search results, set docvalues\_dynamic to true. To exclude the values for an indexed field in the index, set docvalues\_dynamic to false.                                                                                                                                                                                                                                                                                                                            |
| index\_dynamic            | Boolean | Yes       | To index any fields in the Search index where dynamic is true, set index\_dynamic to true. To exclude dynamic fields from the index, set index\_dynamic to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| scoring\_model            | String  | Yes       | Couchbase Server 8.0 Choose the specific scoring model you want to use for scoring search results for this Search index: tf-idf: The standard scoring model for the Search Service. A higher tf-idf score for a document places that document higher in your search results. bm25: A scoring model better suited to hybrid searches with the Search Service. A hybrid Search query uses [Vector Search](../vector-search/vector-search.md) together with a standard Search query. For more information about the calculations for scoring for each algorithm, see [Scoring for Search Queries](run-searches.md#scoring). |
| store\_dynamic            | Boolean | Yes       | To return the content from an indexed field in the Search index, set store\_dynamic to true. To exclude field content from the index, set store\_dynamic to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| type\_field               | String  | No        | Use the same value assigned to the type\_field in doc\_config, if applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| types                     | Object  | No        | An object that contains any user-defined type mappings for the Search index, as {scope}.{collection} objects inside a types object. For more information, see [Types Object](#types).                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## [](#analyzers)Analyzers Object

The `analyzers` object contains any custom analyzers defined for a Search index.

```json
                "analyzers": {
                    "My_Analyzer": {
                        "token_filters": [
                            "apostrophe",
                            "My_Token_Filter"
                        ],
                        "char_filters": [
                            "asciifolding",
                            "html",
                            "My_Char_Filter"
                        ],
                        "type": "custom",
                        "tokenizer": "My_Tokenizer_Excep"
                    }
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `analyzers` object is a child object of the [analysis object](#analysis). It contains any number of [{analyzer\_name} objects](#analyzer-name):

| Property         | Type   | Required? | Description                                                                                                                                                                                                                                                                                                     |
| ---------------- | ------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {analyzer\_name} | Object | Yes       | Set the name of this object to the name you want for your custom analyzer. You can reference the {analyzer\_name} object elsewhere in your Search index definition to use the analyzer. For more information about the properties in an {analyzer\_name} object, see [{Analyzer\_name} Object](#analyzer-name). |

### [](#analyzer-name){Analyzer\_name} Object

The `{analyzer_name}` object defines a custom analyzer for a Search index:

```json
                    "My_Analyzer": {
                        "token_filters": [
                            "apostrophe",
                            "My_Token_Filter"
                        ],
                        "char_filters": [
                            "asciifolding",
                            "html",
                            "My_Char_Filter"
                        ],
                        "type": "custom",
                        "tokenizer": "My_Tokenizer_Excep"
                    }
```

An `{analyzer_name}` object is a child object of the [Analyzers Object](#analyzers). It contains the following properties:

| Property       | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                              |
| -------------- | ------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| token\_filters | Array  | Yes       | An array of strings that contains the token filters for the custom analyzer. For more information about the token filters you can define in a Search index JSON payload, see [Token\_filters Object](#token%5Ffilters). You can also use one of the [default token filters](default-token-filters-reference.md).                         |
| char\_filters  | Array  | Yes       | An array of strings that contains the character filters for the custom analyzer. For more information about the character filters you can define in a Search index JSON payload, see [Char\_filters Object](#char%5Ffilters). You can also use one of the [default character filters](default-character-filters-reference.md) available. |
| type           | String | Yes       | The type is always "custom".                                                                                                                                                                                                                                                                                                             |
| tokenizer      | String | Yes       | The selected tokenizer for the custom analyzer.                                                                                                                                                                                                                                                                                          |

## [](#char%5Ffilters)Char\_filters Object

The `char_filters` object contains any custom character filters defined for a Search index:

```json
                "char_filters": {
                    "My_Char_Filter": {
                        "regexp": "[']",
                        "replace": " ",
                        "type": "regexp"
                    }
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `char_filters` object is a child object of the [analysis object](#analysis). It contains any number of [{char\_filter\_name} objects](#char-name):

| Property             | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {char\_filter\_name} | Object | Yes       | Set the name of this object to the name you want for your custom character filter. You can reference the {char\_filter\_name} object elsewhere in your Search index definition to use the character filter. For more information about the properties in an {char\_filter\_name} object, see [{Char\_filter\_name} Object](#char-name). |

### [](#char-name){Char\_filter\_name} Object

The `{char_filter_name}` object defines a specific custom character filter for a Search index:

```json
                    "My_Char_Filter": {
                        "regexp": "[']",
                        "replace": " ",
                        "type": "regexp"
                    }
```

A `{char_filter_name}` object is a child object of the [Char\_filters Object](#char%5Ffilters). It contains the following properties:

| Property | Type   | Required? | Description                                                                           |
| -------- | ------ | --------- | ------------------------------------------------------------------------------------- |
| regexp   | String | Yes       | The regular expression to use to filter characters from search queries and documents. |
| replace  | String | No        | The content to insert instead of the content in the regexp property.                  |
| type     | String | Yes       | The type is always regexp.                                                            |

## [](#tokenizers)Tokenizers Object

The `tokenizers` object contains any custom [tokenizers](customize-index.md#tokenizers) defined for a Search index:

```json
                "tokenizers": {
                    "My_Tokenizer_Excep": {
                        "exceptions": [
                            "[*]"
                        ],
                        "tokenizer": "unicode",
                        "type": "exception"
                    },
                    "My_Tokenizer_RegExp": {
                        "regexp": "[*]",
                        "type": "regexp"
                    }
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `tokenizers` object is a child object of the [analysis object](#analysis). It contains any number of [{tokenizer\_name objects}](#tokenizer-name):

| Property          | Type   | Required? | Description                                                                                                                                                                                                                                                                                                           |
| ----------------- | ------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {tokenizer\_name} | Object | Yes       | Set the name of this object to the name you want for your custom tokenizer. You can reference the {tokenizer\_name} object elsewhere in your Search index definition to use the tokenizer. For more information about the properties in an {tokenizer\_name} object, see [{Tokenizer\_name} Object](#tokenizer-name). |

### [](#tokenizer-name){Tokenizer\_name} Object

The `{tokenizer_name}` object defines a specific custom tokenizer for a Search index. For example, the following `My_Tokenizer_Excep` object defines an `exception` tokenizer:

```json
                    "My_Tokenizer_Excep": {
                        "exceptions": [
                            "[*]"
                        ],
                        "tokenizer": "unicode",
                        "type": "exception"
                    },
```

A `{tokenizer_name}` object is a child object of the [Tokenizers Object](#tokenizers). It contains the following properties:

| Property   | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| exceptions | Array  | Yes       | If the tokenizer’s [type value](#tokenizer%5Ftype) is exception, define an array of regular expressions to remove from text input to create tokens. For example, if you add the characters sh as a string to the exceptions array, an input string of shTimeshToshGo has the tokens Time, To, and Go.                                                                                            |
| regexp     | String | Yes       | If the tokenizer’s [type value](#tokenizer%5Ftype) is regexp, set the regular expression that the tokenizer uses to divide input into tokens. The tokenizer takes any matches for the regular expression from the input text stream and uses them as tokens. For example, if you use the regular expression \\w\*\\w, an input string of Full Text Search has the tokens Full, Text, and Search. |
| tokenizer  | String | Yes       | If the tokenizer’s type value is exception, give a default tokenizer to apply to the tokens created with the exceptions array. You can choose a [default tokenizer](default-tokenizers-reference.md) or use a tokenizer defined in the tokenizers object.                                                                                                                                        |
| type       | String | Yes       | The tokenizer’s type. Can be one of: regexp: The tokenizer uses a regular expression to create tokens. The tokenizer uses any matches to the regular expression as individual tokens. exception: The tokenizer uses an array of regular expressions to remove content and create tokens. The tokenizer uses any matches to the regular expressions and creates tokens from the surrounding text. |

## [](#token%5Ffilters)Token\_filters Object

The `token_filters` object contains any custom token filters defined for a Search index.

```json
                "token_filters": {
                    "My_Token_Filter": {
                        "min": 3,
                        "max": 255,
                        "type": "length"
                    }
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `token_filters` object is a child object of the [analysis object](#analysis). It contains any number of [{token\_filter\_name} objects](#token-filter-name):

| Property              | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| {token\_filter\_name} | Object | Yes       | Set the name of this object to the name you want for your custom token filter. You can reference the {token\_filter\_name} object elsewhere in your Search index definition to use the token filter. For more information about the properties in an {token\_filter\_name} object, see [{Token\_filter\_name} Object](#token-filter-name). |

### [](#token-filter-name){Token\_filter\_name} Object

The `{token_filter_name}` object defines a custom token filter for a Search index. For example, the following `My_Token_Filter` object defines a custom `length` token filter:

```json
                    "My_Token_Filter": {
                        "min": 3,
                        "max": 255,
                        "type": "length"
                    }
```

A `{token_filter_name}` object is a child object of the [Token\_filters Object](#token%5Ffilters). It contains the following properties:

| Property | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------- | ------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type     | String | Yes       | The token filter’s type. Can be one of: dict\_compound: Use a wordlist to find and create tokens from compound words in existing tokens. See [Dict\_compound Token Filters](#dict%5Fcompound). edge\_ngram: Use a set character length to create tokens from the start or end of existing tokens. See [Edge\_ngram Token Filters](#edge%5Fngram). elision: Use a wordlist to remove elisions from input tokens. See [Elision Token Filters](#elision). keyword\_marker: Use a wordlist of keywords to find and create new tokens. See [Keyword\_marker Token Filters](#keyword%5Fmarker). length: Use a set character length to filter tokens that are too long or too short. See [Length Token Filters](#length). ngram: Use a set character length to create new tokens. See [Ngram Token Filters](#ngram). normalize\_unicode: Use Unicode Normalization to convert tokens. See [Normalize\_unicode Token Filters](#normalize). shingle: Use a set character length and separator to concatenate and create new tokens. See [Shingle Token Filters](#shingle). stop\_tokens: Use a wordlist to find and remove words from tokens. See [Stop\_tokens Token Filters](#stop%5Ftoken). truncate\_token: Use a set character length to truncate existing tokens. See [Truncate\_token Token Filters](#truncate%5Ftoken). |

#### [](#dict%5Fcompound)Dict\_compound Token Filters

A `dict_compound` token filter uses a wordlist to find subwords inside an input token. If the token filter finds a subword inside a compound word, it turns it into a separate token.

```json
      "My_Dict_Compound_Filter": {
        "dict_token_map": "articles_ca",
        "type": "dict_compound"
      },
```

For example, if you had a wordlist that contained `play` and `jump`, the token filter converts `playful jumping` into two tokens: `play` and `jump`.

![dict](_images/dict-3bbc6a301122c6fca086b287e7ea7c7af2e758bb.svg) 

| Property         | Type   | Required? | Description                                                                                                                                                                          |
| ---------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| dict\_token\_map | String | Yes       | The wordlist to use to find subwords in existing tokens. You can use a [default wordlist](default-wordlists-reference.md) or one defined in the [Token\_maps Object](#token%5Fmaps). |

#### [](#edge%5Fngram)Edge\_ngram Token Filters

An `edge_ngram` token filter uses a specified range to create new tokens. You can also choose whether to create the new token from the start or backward from the end of the input token.

```json
      "My_Edge_ngram_Filter": {
        "back": false,
        "min": 4,
        "max": 5,
        "type": "edge_ngram"
      },
```

For example, if you had a miminum of four and a maximum of five with an input token of `breweries`, the token filter creates the tokens `brew` and `brewe`.

![edge](_images/edge-53b440c158199de38d7528e48e6b15a36426f3d9.svg) 

| Property | Type    | Required? | Description                                                                                                                                                                                                   |
| -------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| back     | Boolean | Yes       | To create new tokens starting from the end and moving backward in an input token, set back to true. To create new tokens starting from the beginning and moving forward in an input token, set back to false. |
| min      | Integer | Yes       | Set the minimum character length for a new token.                                                                                                                                                             |
| max      | Integer | Yes       | Set the maximum character length for a new token.                                                                                                                                                             |

#### [](#elision)Elision Token Filters

An `elision` token filter removes elisions from input tokens.

```json
      "My_Elision_Filter": {
        "articles_token_map": "stop_fr",
        "type": "elision"
      },
```

For example, if you had the `stop_fr` wordlist in an elision token filter, the token `je m’appelle John` becomes the tokens `je`, `appelle`, and `John`.

![elision](_images/elision-f3bfe6d06370309959606d5b1299ce61a2a9feef.svg) 

| Property             | Type   | Required? | Description                                                                                                                                                                                     |
| -------------------- | ------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| articles\_token\_map | String | Yes       | The wordlist to use to find and remove elisions in existing tokens. You can use a [default wordlist](default-wordlists-reference.md) or one defined in the [Token\_maps Object](#token%5Fmaps). |

#### [](#keyword%5Fmarker)Keyword\_marker Token Filters

A `keyword_marker` token filter finds keywords in an input token and turns them into tokens.

```json
      "My_Keyword_Marker_Filter": {
        "keywords_token_map": "articles_ca",
        "type": "keyword_marker"
      },
```

For example, if you had a wordlist that contained the keyword `beer`, the token `beer and breweries` becomes the token `beer`.

![keyword](_images/keyword-bfcc125930301861a91933fe34a0f600db3f8eee.svg) 

| Property             | Type   | Required? | Description                                                                                                                                                                          |
| -------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| keywords\_token\_map | String | Yes       | The wordlist to use to find keywords in existing tokens. You can use a [default wordlist](default-wordlists-reference.md) or one defined in the [Token\_maps Object](#token%5Fmaps). |

#### [](#length)Length Token Filters

A `length` token filter removes tokens that are shorter or longer than a set character length.

```json
      "My_Length_Filter": {
       "min": 2,
       "max": 4,
       "type": "length"
      },
```

For example, if you had a range with a minimum of two and a maximum of four, the token `beer and breweries` becomes the tokens `beer` and `and`.

![length](_images/length-1b79deaad25f915c0885ca143a6685dad8939b92.svg) 

| Property | Type    | Required? | Description                                                         |
| -------- | ------- | --------- | ------------------------------------------------------------------- |
| min      | Integer | Yes       | The minimum character length for a new token from the token filter. |
| max      | Integer | Yes       | The maximum character length for a new token from the token filter. |

#### [](#ngram)Ngram Token Filters

An `ngram` token filter uses a specified character length to split an input token into new tokens.

```json
      "My_Ngram_Filter": {
        "min": 4,
        "max": 5,
        "type": "ngram"
      },
```

For example, if you had a range with a minimum of four and a maximum of five, the token `beers` becomes the tokens `beer`, `beers`, and `eers`.

![ngram](_images/ngram-2126d46f08f25dc72513faacb0ff70924f58021e.svg) 

| Property | Type    | Required? | Description                                                         |
| -------- | ------- | --------- | ------------------------------------------------------------------- |
| min      | Integer | Yes       | The minimum character length for a new token from the token filter. |
| max      | Integer | Yes       | The maximum character length for a new token from the token filter. |

#### [](#normalize)Normalize\_unicode Token Filters

A `normalize_unicode` token filter uses a specified Unicode Normalization form to create new tokens.

```json
      "My_Normalize_Unicode_Filter": {
        "form": "nfkd",
        "type": "normalize_unicode"
      },
```

| Property | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| form     | String | Yes       | Select the form of Unicode Normalization to use on input tokens: nfc: Use canonical decomposition and canonical composition to normalize characters. The token filter separates combined unicode characters, then merges them into a single character. nfd: Use canonical decomposition to normalize characters. The token filter separates combined unicode characters. nfkc: Use compatibility decomposition to normalize characters. The token filter converts unicode characters to remove variants. nfkd: Use compatibility decomposition and canonical composition to normalize characters. The token filter removes variants, then separates combined unicode characters to merge them into a single character. For more information about Unicode Normalization, see the Unicode Consortium’s [Unicode Normalization Forms](https://unicode.org/reports/tr15/#Introduction) report. |

#### [](#shingle)Shingle Token Filters

A `shingle` token filter uses a specified character length and separator to create new tokens.

```json
      "My_Shingle_Filter":{
        "min": 2,
        "max": 3,
        "output_original": true,
        "separator": " ",
        "filler": "x",
        "type": "shingle"
      },
```

For example, if you use a [whitespace tokenizer](default-tokenizers-reference.md#whitespace), a range with a minimum of two and a maximum of three, and a space as a separator, the token `abc def` becomes `abc`, `def`, and `abc def`.

![shingle](_images/shingle-bc68693147c520ba6def14401d61d5ba22710a7d.svg) 

| Property         | Type    | Required? | Description                                                                                                                                                                        |
| ---------------- | ------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| min              | Integer | Yes       | The minimum character length for a new token before concatenation.                                                                                                                 |
| max              | Integer | Yes       | The maximum character length for a new token before concatenation.                                                                                                                 |
| output\_original | Boolean | Yes       | To add the original token to the token filter’s output, set output\_original to true. To exclude the original token from the token filter’s output, set output\_original to false. |
| separator        | String  | No        | Set a separator to include a character or characters in between concatenated tokens.                                                                                               |
| filler           | String  | No        | If another token filter removes a token from the input for this token filter, set a filler to replace the removed token.                                                           |

#### [](#stop%5Ftoken)Stop\_tokens Token Filters

A `stop_tokens` token filter uses a wordlist to remove specific tokens from input.

```json
      "My_Stop_Tokens_Filter":{
        "stop_token_map": "articles_ca",
        "type": "stop_tokens"
      },
```

For example, if you have a wordlist that contains the word `and`, the token `beers and breweries` becomes `beers` and `breweries`.

![stop](_images/stop-de565d1d82022c6d4d8d3d4f574c90b8c13b24e0.svg) 

| Property         | Type   | Required? | Description                                                                                                                                                                                                                                           |
| ---------------- | ------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| stop\_token\_map | String | Yes       | The wordlist to use to filter tokens. The token filter removes any tokens from input that match an entry in the wordlist. You can use a [default wordlist](default-wordlists-reference.md) or one defined in the [Token\_maps Object](#token%5Fmaps). |

#### [](#truncate%5Ftoken)Truncate\_token Token Filters

A `truncate_token` token filter uses a specified character length to shorten any input tokens that are too long.

```json
      "My_Truncate_Token_Filter":{
        "length": 4,
        "type": "truncate_token"
      }
```

For example, if you had a `length` of four, the token `beer and breweries` becomes `beer`, `and`, and `brewe`.

![truncate](_images/truncate-eb79f973d761c93658082540e5665474e15eebbe.svg) 

| Property | Type    | Required? | Description                                       |
| -------- | ------- | --------- | ------------------------------------------------- |
| length   | Integer | Yes       | The maximum character length for an output token. |

## [](#token%5Fmaps)Token\_maps Object

The `token_maps` object contains any custom wordlists defined for a Search index:

```json
                "token_maps": {
                    "My_Wordlist": {
                        "type": "custom",
                        "tokens": [
                            "the",
                            "is",
                            "and"
                        ]
                    }
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `token_maps` object is a child object of the [analysis object](#analysis). It contains any number of [{wordlist\_name} objects](#wordlist-name):

| Property         | Type   | Required? | Description                                                                                                                                                                                                                                                                                                     |
| ---------------- | ------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {wordlist\_name} | Object | Yes       | Set the name of this object to the name you want for your custom wordlist. You can reference the {wordlist\_name} object elsewhere in your Search index definition to use the wordlist. For more information about the properties in an {wordlist\_name} object, see [{Wordlist\_name} Object](#wordlist-name). |

### [](#wordlist-name){Wordlist\_name} Object

The `{wordlist_name}` object defines a custom wordlist for a Search index:

```json
                    "My_Wordlist": {
                        "type": "custom",
                        "tokens": [
                            "the",
                            "is",
                            "and"
                        ]
                    }
```

A `{wordlist_name}` object is a child object of the [Token\_maps Object](#token%5Fmaps). It contains the following properties:

| Property | Type   | Required? | Description                                                        |
| -------- | ------ | --------- | ------------------------------------------------------------------ |
| type     | String | Yes       | The type is always "custom".                                       |
| tokens   | Array  | Yes       | An array of strings that contains each word added to the wordlist. |

## [](#date%5Ftime%5Fparsers)Date\_time\_parsers Object

The `date_time_parsers` object contains any custom date/time parsers defined for a Search index:

```json
                "date_time_parsers": {
                    "My_Date_Time_Parser": {
                        "type": "flexiblego",
                        "layouts": [
                            "RFC850"
                        ]
                    }
                },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `date_time_parsers` object is a child object of the [analysis object](#analysis). It contains any number of [{date\_time\_parser\_name} objects](#dt-parser-name):

| Property                   | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------- | ------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {date\_time\_parser\_name} | Object | Yes       | Set the name of this object to the name you want for your custom date/time parser. You can reference the {date\_time\_parser\_name} object elsewhere in your Search index definition to use the date/time parser. For more information about the properties in an {date\_time\_parser\_name} object, see [{date\_time\_parser\_name} Object](#dt-parser-name). |

### [](#dt-parser-name){date\_time\_parser\_name} Object

The `{date_time_parser_name}` object defines a custom date/time parser for a Search index:

```json
                    "My_Date_Time_Parser": {
                        "type": "flexiblego",
                        "layouts": [
                            "RFC850"
                        ]
                    }
```

A `{date_time_parser_name}` object is a child object of the [Date\_time\_parsers Object](#date%5Ftime%5Fparsers). It contains the following properties:

| Property | Type   | Required? | Description                                                                                                                                                                                |
| -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| type     | String | Yes       | The type is always "flexiblego".                                                                                                                                                           |
| layouts  | Array  | Yes       | An array of strings that contains layouts for date and time fields. Use a layout from the [Go Programming Language Time Package’s Layout Constant](https://pkg.go.dev/time#pkg-constants). |

## [](#synonym%5Fsources)Synonym\_sources Object

Couchbase Server 8.0

The `synonym_sources` object contains any synonym collections defined for a Search index:

```json
                "synonym_sources": {
                    "synonyms_en": {
                        "analyzer": "My_Analyzer",
                        "collection": "synonyms_en"
                    }
                }
```

> [!TIP]
> To view the entire JSON payload, click **View**.

For more information about synonym searches, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md).

The `synonym_sources` object is a child object of the [analysis object](#analysis). It contains any number of [{synonym\_collection\_name} objects](#synonym%5Fname):

| Property                    | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| {synonym\_collection\_name} | Object | Yes       | Set the name of this object to the name you want to use to identify your synonym collection in your Search index. Reference the {synonym\_collection\_name} object in a text field definition to use synonym searches with that text field. For more information about the properties in an {synonym\_collection\_name} object, see [{synonym\_collection\_name} Object](#synonym%5Fname). |

### [](#synonym%5Fname){synonym\_collection\_name} Object

Couchbase Server 8.0

The `{synonym_collection_name}` object defines a synonym collection on a Search index:

```json
                    "synonyms_en": {
                        "analyzer": "My_Analyzer",
                        "collection": "synonyms_en"
                    }
```

For more information about synonym searches, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md).

A `{synonym_collection_name}` object is a child object of the [Synonym\_sources Object](#synonym%5Fsources). It contains the following properties:

| Property   | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------- | ------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analyzer   | String | Yes       | Enter the name of the analyzer to use for the synonym documents stored in this collection. Set the analyzer for a synonym collection to the same analyzer you set in the [Fields Array](#fields) for a text field. You cannot use synonym searches on a field unless the [synonym\_source](#synonym%5Fsource%5Ffield) is set and the analyzers match.                                                                                                                                                                   |
| collection | String | Yes       | Enter the name of the collection where your synonym documents are stored on your cluster. The synonym collection must be in the same bucket and scope as where you want to define your Search index. Synonym documents must have the proper syntax to be used by the Search Service. For more information, see [Create a Synonym Collection and Documents](synonyms/create-synonym-collection-docs.md). Do not add your synonym collections as a [{scope}.{collection} object](#scope-collection) in your Search index. |

## [](#default-mapping)Default\_mapping Object

The `default_mapping` object contains settings for the default type mapping on the Search index. The default type mapping is a legacy feature and only included for compatibility.

```json
            "default_mapping": {
                "dynamic": false,
                "enabled": false
            },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `default_mapping` object is a child object of the [Mapping Object](#mapping). It contains the following properties:

| Property | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                        |
| -------- | ------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dynamic  | Boolean | Yes       | To index all available fields in a document with the default type mapping, set dynamic to true. To only index the fields you specify in the type mapping, set dynamic to false.                                                                                                                                                    |
| enabled  | Boolean | Yes       | To enable the Search Service’s default type mapping, set enabled to true. The default type mapping includes all documents in the bucket in the Search index, even if they do not match another configured type mapping. This can increase index size and indexing time. To disable the default type mapping, set enabled to false. |

## [](#types)Types Object

The `types` object contains any additional user-defined type mappings for a Search index.

```json
            "types": {
                "inventory.hotel": {
                    "dynamic": false,
                    "enabled": true,
                    "properties": {
                        "_$xattrs": {
                            "dynamic": true,
                            "enabled": true
                        },
                        "reviews": {
                            "dynamic": false,
                            "enabled": true,
                            "properties": {
                                "content": {
                                    "enabled": true,
                                    "dynamic": false,
                                    "fields": [
                                        {
                                            "docvalues": true,
                                            "include_in_all": true,
                                            "include_term_vectors": true,
                                            "index": true,
                                            "name": "content",
                                            "store": true,
                                            "synonym_source": "synonyms_en",
                                            "type": "text",
                                            "analyzer": "My_Analyzer"
                                        }
                                    ]
                                }
                            }
                        },
                        "city": {
                            "enabled": true,
                            "dynamic": false,
                            "fields": [
                                {
                                    "docvalues": true,
                                    "include_in_all": true,
                                    "include_term_vectors": true,
                                    "index": true,
                                    "name": "city",
                                    "store": true,
                                    "type": "text"
                                }
                            ]
                        },
                        "inventory.hotel.free_breakfast_true": {
                            "dynamic": true,
                            "enabled": true,
                            "properties": {
                                "free_breakfast": {
                                    "dynamic": false,
                                    "enabled": true,
                                    "fields": [
                                        {
                                            "docvalues": true,
                                            "include_in_all": true,
                                            "index": true,
                                            "name": "free_breakfast",
                                            "store": true,
                                            "type": "boolean"
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            }
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `types` object is a child object of the [Mapping Object](#mapping). It contains any number of [{scope}.{collection} objects](#scope-collection):

| Property             | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {scope}.{collection} | Object | Yes       | The name of the type mapping. Corresponds to the selected scope and collection where the type mapping applies. For example, inventory.airline. For more information about the properties in an {scope}.{collection} object, see [{Scope}.{collection} Objects, JSON Object Field Objects, and XATTRs Objects](#scope-collection). To add a type identifier as an additional filter to your type mapping, add the filter to the end of your {scope}.{collection} object. For example, to use a type\_field filter that uses the type field, and add only documents with a type value of hotel, the object name would be {scope}.{collection}.hotel |

### [](#scope-collection){Scope}.{collection} Objects, JSON Object Field Objects, and XATTRs Objects

The `{scope}.{collection}` object defines a custom type mapping for a Search index, on a specific scope and collection in the cluster:

```json
                "inventory.hotel": {
                    "dynamic": false,
                    "enabled": true,
                    "properties": {
                        "_$xattrs": {
                            "dynamic": true,
                            "enabled": true
                        },
                        "reviews": {
                            "dynamic": false,
                            "enabled": true,
                            "properties": {
                                "content": {
                                    "enabled": true,
                                    "dynamic": false,
                                    "fields": [
                                        {
                                            "docvalues": true,
                                            "include_in_all": true,
                                            "include_term_vectors": true,
                                            "index": true,
                                            "name": "content",
                                            "store": true,
                                            "synonym_source": "synonyms_en",
                                            "type": "text",
                                            "analyzer": "My_Analyzer"
                                        }
                                    ]
                                }
                            }
                        },
                        "city": {
                            "enabled": true,
                            "dynamic": false,
                            "fields": [
                                {
                                    "docvalues": true,
                                    "include_in_all": true,
                                    "include_term_vectors": true,
                                    "index": true,
                                    "name": "city",
                                    "store": true,
                                    "type": "text"
                                }
                            ]
                        },
                        "inventory.hotel.free_breakfast_true": {
                            "dynamic": true,
                            "enabled": true,
                            "properties": {
                                "free_breakfast": {
                                    "dynamic": false,
                                    "enabled": true,
                                    "fields": [
                                        {
                                            "docvalues": true,
                                            "include_in_all": true,
                                            "index": true,
                                            "name": "free_breakfast",
                                            "store": true,
                                            "type": "boolean"
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
```

A `{scope}.{collection}` object is a child object of the [Types Object](#types).

A JSON object field object is a child object of the `{scope}.{collection}` object. It defines a mapping for a field that contains a JSON object in your document schema. It can contain additional mappings as [{field\_name} Object](#child-fields) under its [properties](#properties) object.

A JSON object field object must:

* Be a child object of a `{scope}.{collection}` object.
* Have a name that matches a JSON object field in your documents.
* Use the same property structure as a `{scope}.{collection}` object.

If your cluster is running Couchbase Server version 7.6.2 and later and you’re adding Extended Attributes (XATTRs) from your document metadata to your Search index, your XATTRs mapping definition must:

* Be a child object of a `{scope}.{collection}` object.
* Have the name `_$xattrs`.
* Use the same property structure as a `{scope}.{collection}` object.

For example, the following JSON index definition snippet defines a `{scope}.{collection}` object for the `inventory.hotel` scope and collection. It adds a dynamic mapping for any XATTRs metadata present on documents in the collection. It adds two nested JSON Object Field objects, `reviews` and `ratings`, that contain a single [document field object](#child-fields) for the `Cleanliness` field:

```json
{
    "inventory.hotel": {
        "dynamic": false,
        "enabled": true,
        "properties": {
            "_$xattrs": {
                "dynamic": true,
                "enabled": true
            },
            "reviews": {
                "dynamic": false,
                "enabled": true,
                "properties": {
                    "ratings": {
                        "dynamic": false,
                        "enabled": true,
                        "properties": {
                            "Cleanliness": {
                                "enabled": true,
                                "dynamic": false,
                                "fields": [
                                    {
                                        "docvalues": true,
                                        "include_in_all": true,
                                        "index": true,
                                        "name": "Cleanliness",
                                        "store": true,
                                        "type": "number"
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
}
```

You can view the JSON document schema for this example by looking at any document in the `hotel` collection from the `travel-sample` dataset. For more information, see [Manage Documents with the Capella UI](../clusters/data-service/manage-documents.md).

`{scope}.{collection}` objects, JSON Object Field objects, and XATTRs objects can contain the following properties:

| Property                 | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dynamic                  | Boolean | Yes       | To index all fields under the specified scope and collection, JSON object, or all fields inside XATTRs, set dynamic to true. This creates a [dynamic type mapping](about-mappings.md#dynamic). To only index the fields you specify and enable the properties block, set dynamic to false. This creates a [static type mapping](about-mappings.md#static).                                                                                                                                                                                                                                                                                                                                                |
| enabled                  | Boolean | Yes       | To enable the mapping and include any documents that match it in the Search index, set enabled to true. To remove any documents that match this mapping from the Search index, set enabled to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| default\_analyzer        | String  | No        | The name of the default analyzer to use for any text field defined under this type mapping. If the type mapping is dynamic, this analyzer applies to every text field for documents that match the type mapping. If the type mapping is static, this analyzer only applies to the text fields you add in the properties object that do not have a defined analyzer. The value of default\_analyzer must match a defined [{Analyzer\_name} Object](#analyzer-name) in your Search index definition, or [a default analyzer](default-analyzers-reference.md). For more information about analyzers, see [Analyzers](customize-index.md#analyzers).                                                          |
| default\_synonym\_source | String  | No        | Couchbase Server 8.0 The name of the default synonym source to use for any text fields defined under this type mapping. If the type mapping is dynamic, this synonym source applies to every text field for documents that match the type mapping. If the type mapping is static, this synonym source only applies to the text fields you add in the properties object that do not have a defined synonym source. The value of default\_synonym\_source must match a defined [{synonym\_collection\_name} Object](#synonym%5Fname) in your Search index definition. For more information about using synonyms with the Search Service, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md). |
| properties               | Object  | No        | The properties object is only enabled if dynamic is set to false. Specifies properties for the fields to index in the mapping. Contains any number of {field\_name} objects. For more information, see [{field\_name} Object](#child-fields).                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### [](#child-fields){field\_name} Object

The `{field_name}` object contains properties and an array for a document field in a type mapping. You can have multiple `{field_name}` objects in a [properties object](#properties).

```json
                        "reviews": {
                            "dynamic": false,
                            "enabled": true,
                            "properties": {
                                "content": {
                                    "enabled": true,
                                    "dynamic": false,
                                    "fields": [
                                        {
                                            "docvalues": true,
                                            "include_in_all": true,
                                            "include_term_vectors": true,
                                            "index": true,
                                            "name": "content",
                                            "store": true,
                                            "synonym_source": "synonyms_en",
                                            "type": "text",
                                            "analyzer": "My_Analyzer"
                                        }
                                    ]
                                }
                            }
                        },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The name of the object corresponds to the name of the field you want to include or exclude from your Search index.

A `{field_name}` object contains the following properties:

| Property | Type    | Required? | Description                                                                                                                                           |
| -------- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| enabled  | Boolean | Yes       | To add this document field to the Search index, set enabled to true. To remove this document field from the index, set enabled to false.              |
| dynamic  | Boolean | No        | This field is included for legacy compatibility only.                                                                                                 |
| fields   | Array   | Yes       | An array that contains objects with settings for each document field to index in the type mapping. For more information, see [Fields Array](#fields). |

### [](#fields)Fields Array

The `fields` array contains objects with settings for each document field to index in the type mapping:

```json
                                    "fields": [
                                        {
                                            "docvalues": true,
                                            "include_in_all": true,
                                            "include_term_vectors": true,
                                            "index": true,
                                            "name": "content",
                                            "store": true,
                                            "synonym_source": "synonyms_en",
                                            "type": "text",
                                            "analyzer": "My_Analyzer"
                                        }
                                    ]
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `fields` array is located inside a [{field\_name} object](#child-fields). It contains the following properties:

| Property                      | Type    | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analyzer                      | String  | Text Only   | If the document field’s type is text, set the analyzer to use for the document field. If you want to use the default analyzer for the content of this document field, you do not need to include an analyzer property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| dims                          | Integer | Vector Only | For a vector child field, enter the total number of elements in the vector embedding array. From Couchbase Server version 7.6.2 and later, Search Vector Indexes can support arrays with up to 4096 elements. Arrays can be an array of arrays. For more information about Search Vector Indexes, see [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md) or [Create a Search Vector Index in Quick Mode](../vector-search/create-vector-search-index-ui.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| docvalues                     | Boolean | Yes         | To include the value for each instance of the field in the Search index to support [facets](search-request-params.md#facet-name) and sorting search results, set docvalues to true. To exclude the values for each instance of this field from the index, set docvalues to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| include\_in\_all              | Boolean | Yes         | To allow this field to be searched without specifying the specific field’s name in the search, set include\_in\_all to true. When enabled, you can search this field through the specified default\_field set in the type mapping. To only search this field by specifying the field name, set include\_in\_all to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| include\_term\_vectors        | Boolean | Yes         | To use term vectors, store must be set to true. To allow the Search Service to highlight matching search terms in search results for this field, set include\_term\_vectors to true. You must also enable term vectors to use includeLocations in a Search query. For more information, see [includeLocations](search-request-params.md#includelocations). To disable term highlighting and reduce index size, set include\_term\_vectors to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| index                         | Boolean | Yes         | To include the document field in the Search index, set index to true. To exclude the document field from the index, set index to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| name                          | String  | Yes         | The document field’s name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| similarity                    | String  | Vector Only | For a vector child field, choose the method to calculate the similarity between the vector embedding in a Search Vector Index and the vector embedding in a Vector Search query. It’s recommended to choose the same similarity metric for your Search index as the one used in your embedding model. **dot\_product**: Calculated by adding the result of multiplying a vector’s components, or the product of the magnitudes of the vectors and the cosine of the angle between them. The dot product of 2 vectors is affected by the length and direction of each of the vectors, rather than just taking a straight-line distance. Dot product similarity is commonly used by Large Language Models (LLMs). Use **dot\_product** to get the best results with an embedding model that uses dot product similarity. **l2\_norm**: Also known as Euclidean distance. Uses the straight-line distance between 2 vectors to calculate similarity. Smaller euclidean distances mean that the values of each coordinate in the vectors are closer together. It’s best to use **l2\_norm** similarity when your embeddings contain information about the count or measure of specific things, and your embedding model uses the same similarity metric. **cosine**: From Couchbase Server version 7.6.5 and later, the **cosine** similarity metric is calculated by adding the result of multiplying a vector’s components, or the product of the magnitudes of the vectors and the cosine of the angle between them. This metric is not affected by the size of the vectors being measured. Use **cosine** similarity to get the best results with an embedding model that uses cosine similarity. Cosine similarity works well for semantic search, document classification, and recommendation systems. The Search Service will normalize any vectors in your documents before indexing when using cosine similarity. It will also normalize any vectors in your queries if the field for those queries uses cosine similarity. Use **dot\_product** similarity if your vectors are already normalized. For more information about Search Vector Indexes, see [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md) or [Create a Search Vector Index in Quick Mode](../vector-search/create-vector-search-index-ui.md). |
| store                         | Boolean | Yes         | To include the content of the document field in the Search index and allow its content to be viewed in search results, set store to true. To exclude the content of the document field from the index, set store to false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| synonym\_source               | String  | No          | Couchbase Server 8.0 Enter the name of the [{synonym\_collection\_name} Object](#synonym%5Fname) you want to use for synonym searches on this field. The Search Service uses any synonym documents stored in this synonym collection for synonym searches on this field. You can only use synonym searches on a field with a type of text. The analyzer set on this field must match the analyzer set on the {synonym\_collection\_name} object. For more information about synonym searches, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| type                          | String  | Yes         | The document field’s type. Can be one of: text number datetime boolean geopoint geoshape disabled ip vector (Server version 7.6.2 and later) vector\_base64 For more information about the available field data types, see [Field Data Types](field-data-types-reference.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| vector\_index\_optimized\_for | String  | Vector Only | For a vector child field, choose whether the Search Service should prioritize recall, latency, or memory efficiency when returning similar vectors in search results: **recall**: The Search Service prioritizes returning the most accurate result. This may increase resource usage for Search queries. The Search Service uses an nprobe value to calculate the number of centroids to search when using recall priority. This value is calculated by taking the square root of the number of centroids in the index. **latency**: The Search Service prioritizes returning results with lower latency. This may reduce the accuracy of results. The Search Service uses half the nprobe value calculated for **recall** priority. **memory-efficient**: From Couchbase Server version 7.6.5 and later, choose this option to prioritize reducing memory usage and optimize search operations for less resources. This may reduce both accuracy (recall) and latency. The Search Service uses either an inverted file index with scalar quantization, or a directly mapped index with exact vector comparisons, depending on the number of vectors in your data. For more information about Search Vector Indexes, see [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md) or [Create a Search Vector Index in Quick Mode](../vector-search/create-vector-search-index-ui.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## [](#store)Store Object

The `store` object can change settings for merge policy, concurrent persister behavior, and file format version on your Search index. Depending on your performance needs and specific Search use case, you may want to adjust these values, or leave them as default.

You do not need to provide this object when creating a Search index.

```json
        "store": {
            "indexType": "scorch",
            "scorchPersisterOptions": {
                "maxSizeInMemoryMergePerWorker": 20971520,
                "numPersisterWorkers": 4
            },
            "scorchMergePlanOptions":{
                "floorSegmentFileSize": 3495253
            },
            "segmentVersion": 16
        }
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `store` object contains the following properties:

| Property               | Type    | Required? | Description                                                                                                                                                                               |
| ---------------------- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| indexType              | String  | No        | The indexType is always scorch.                                                                                                                                                           |
| scorchPersisterOptions | Object  | No        | Couchbase Server 8.0 An object that contains settings for in-memory buffer processing in your Search index. For more information, see [ScorchPersisterOptions Object](#scorch-persister). |
| scorchMergePlanOptions | Object  | No        | Couchbase Server 8.0 An object that contains settings for background merging behavior in your Search index. For more information, see [ScorchMergePlanOptions Object](#scorch-merge).     |
| segmentVersion         | Integer | No        | The segmentVersion is always 16.                                                                                                                                                          |

### [](#scorch-persister)ScorchPersisterOptions Object

Couchbase Server 8.0

The `scorchPersisterOptions` object controls in-memory buffer processing on your Search index.

```json
            "scorchPersisterOptions": {
                "maxSizeInMemoryMergePerWorker": 20971520,
                "numPersisterWorkers": 4
            },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `scorchPersisterOptions` object contains the following properties:

| Property                      | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxSizeInMemoryMergePerWorker | Integer | No        | Set a value, in bytes, for how much data from the in-memory buffers each worker should process and flush to disk. A higher value means healthier data flushing from memory to disk, but longer flushing times for each worker, because of the higher data volume. For a FTS Vector Index, set maxSizeInMemoryMergePerWorker to 400 MB. For a regular Search index, set maxSizeInMemoryMergePerWorker to 20 MB. You may want to change these recommended values based on your specific use case.                                                                                       |
| numPersisterWorkers           | Integer | No        | Set a value for the total number of workers you want to use to process data from in-memory buffers. More workers increases the rate of memory being flushed to disk, but increases the number of files on disk and your disk I/O. For a FTS Vector Index, set numPersisterWorkers to 4. For a regular Search index, set numPersisterWorkers to 4. You may want to change these recommended values based on your specific use case. If you increase your workers, make sure to increase the [floorSegmentFileSize](#floor%5Fsegment%5Fsize), to keep your number of segment files low. |

### [](#scorch-merge)ScorchMergePlanOptions Object

Couchbase Server 8.0

The `scorchMergePlanOptions` object controls the background merging behavior for segment files in your Search index.

```json
            "scorchMergePlanOptions":{
                "floorSegmentFileSize": 3495253
            },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `scorchMergePlanOptions` object contains the following properties:

| Property             | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| floorSegmentFileSize | Integer | No        | Set a value, in bytes, for the Search Service’s minimum segment file size. The Search Service merges segments to improve query performance and storage. If a segment is smaller than this minimum file size, the Search Service will merge it during its background merging. A higher value for the minimum segment file size means more aggressive merging behavior and better query performance, at the cost of increased disk I/O and longer merge cycles, with more resource usage. For a FTS Vector Index, set floorSegmentFileSize to: \\$(\\m\\a\\x\\SizeInMem\\o\\r\\yMer\\g\\ePerW\\o\\r\\ker)/3\\$ If you want to improve I/O and indexing performance at the cost of query performance, set floorSegmentFileSize to: \\$(\\m\\a\\x\\SizeInMem\\o\\r\\yMer\\g\\ePerW\\o\\r\\ker)/6\\$ For a regular Search index, set floorSegmentFileSize to the same value as [maxSizeInMemoryMergePerWorker](#max%5Fsize%5Fmemory%5Fmerge). You may want to change these recommended values based on your specific use case. |