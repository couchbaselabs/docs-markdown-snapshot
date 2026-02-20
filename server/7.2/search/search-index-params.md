---
title: Search Index JSON Properties
description: Use a JSON payload to control the settings for a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/search-index-params.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:search:search-index-params.adoc[]
---

[View original HTML](/server/7.2/search/search-index-params.html)

# Search Index JSON Properties

> Use a JSON payload to control the settings for a Search index. 

When you [create a Search index with the REST API](create-search-index-rest-api.md), you must give a JSON payload with the settings for the new Search index.

Your JSON payload must contain the properties described in [Initial Settings](#initial), including the [Params Object](#params).

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

| Property     | Type   | Required? | Description                                                                                                                                                                                                                                                           |
| ------------ | ------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name         | String | Yes       | The name of the Search index. A Search index name must be unique for each cluster.                                                                                                                                                                                    |
| type         | String | Yes       | The type of index you want to create: fulltext-index: Create a Search index. fulltext-alias: Create an alias for a Search index. For more information about Search index aliases, see [Create Search Index Aliases](../../current/search/index-aliases.md).           |
| uuid         | String | No        | The Search Service automatically generates a UUID for a Search index. If you use an existing UUID, the Search Service updates the existing Search index. Don’t include the uuid property when you want to copy an index to a different cluster or create a new index. |
| sourceType   | String | Yes       | The sourceType is always "gocbcore".                                                                                                                                                                                                                                  |
| sourceName   | String | Yes       | The name of the bucket where you want to create the Search index. The Search Service automatically finds the UUID for the bucket.                                                                                                                                     |
| sourceUUID   | String | No        | The UUID of the bucket where you want to create the Search index. The Search Service automatically finds the UUID for the bucket. Don’t include the sourceUUID property when you want to copy an index to a different cluster, or create a new index.                 |
| sourceParams | Object | No        | This object contains advanced settings for index behavior. Don’t add content into this object unless instructed by Couchbase Support.                                                                                                                                 |
| planParams   | Object | Yes       | An object that sets the Search index’s partitions and replications. For more information, see [planParams Object](#planparams).                                                                                                                                       |
| params       | Object | Yes       | An object that sets the Search index’s type identifier, type mappings, and analyzers. For more information, see [Params Object](#params).                                                                                                                             |

## [](#planparams)planParams Object

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

| Property               | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxPartitionsPerPIndex | n/a    | No        | This setting is deprecated. Use indexPartitions, instead.                                                                                                                                                                                                                                                                                                                                                                                   |
| indexPartitions        | Number | Yes       | The number of partitions to split the Search index into, across the nodes you have available in your database with the Search Service enabled. Use index partitions to increase index and query performance on large datasets.                                                                                                                                                                                                              |
| numReplicas            | Number | Yes       | For high-availability, set the number of replicas the Search Service creates for the Search index. You can create up to three replicas for a Search index. Each replica creates a full copy of the Search index to increase high-availability. To turn off replication for the Search index, set numReplicas to 0. The number of replicas you can create depends on the number of nodes you have available with the Search Service enabled. |

## [](#params)Params Object

The `params` object sets a Search index’s [type identifier](customize-index.md#type-identifiers), [type mappings](customize-index.md#type-mappings), and [analyzers](customize-index.md#analyzers).

It contains the following properties:

| Property    | Type   | Required? | Description                                                                                                                   |
| ----------- | ------ | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| doc\_config | Object | Yes       | An object that sets how the Search index sets a document’s type. For more information, see [Doc\_config Object](#doc-config). |
| mapping     | Object | Yes       | An object that sets the analyzers and type mappings for a Search index. For more information, see [Mapping Object](#mapping). |

### [](#doc-config)Doc\_config Object

The `doc_config` object sets how the Search index sets a document’s type:

```json
        "doc_config": {
            "docid_prefix_delim": "",
            "docid_regexp": "",
            "mode": "scope.collection.type_field",
            "type_field": "type"
        },
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `doc_config` object is a child object of the [Params Object](#params). It contains the following properties:

Property

Type

Required?

Description

mode

String

Yes

Set a [type identifier](#customize-search-index.adoc#type-identifiers) for the Search index to filter documents from search results:

* `type_field`: Use the value from a specific field in the documents.
* `docid_prefix_delim`: Use the leading characters in the documents' ID values, up to but not including a specified separator.
* `docid_regexp`: Use a regular expression on the documents' ID values.

> [!NOTE]
> If you want your Search index to only include documents from a specific collection, the `mode` value must be `"scope.collection.{mode}"`.

docid\_prefix\_delim

String

Yes

If `mode` is `docid_prefix_delim`, set the separator character to use on a document’s ID value.

For example, to filter documents based on the characters before a  in their ID values, set `docid_prefix_delim` to ``. 

docid\_regexp

String

Yes

If `mode` is `docid_regexp`, set the regular expression to use on a document’s ID value to determine its type.

For example, to filter documents that contain the characters 40 in their ID value, set `docid_regexp` to `[3-5]0`. 

type\_field

String

Yes

If `mode` is `type_field`, set the name of the field to use to filter documents.

For example, to filter documents based on the value of their `type` field, set `type_field` to `type`.

### [](#mapping)Mapping Object

The `mapping` object contains a Search index’s [analyzers](customize-index.md#analyzers) and other [advanced settings from the UI](set-advanced-settings.md):

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
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `mapping` object is a child object of the [Params Object](#params). It contains the following properties:

| Property                  | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analysis                  | Object  | Yes       | An object that contains the following child objects: [Analyzers Object](#analyzers) [Char\_filters Object](#char%5Ffilters) [Tokenizers Object](#tokenizers) [Token\_filters Object](#token%5Ffilters) [Token\_maps Object](#token%5Fmaps) [Date\_time\_parsers Object](#date%5Ftime%5Fparsers)                                                                                           |
| default\_analyzer         | String  | Yes       | The name of the default analyzer to use for the Search index. For more information about analyzers, see [Analyzers](customize-index.md#analyzers).                                                                                                                                                                                                                                        |
| default\_datetime\_parser | String  | Yes       | The name of the default date/time parser to use for the Search index. For more information about date/time parsers, see [Date/Time Parsers](customize-index.md#date-time).                                                                                                                                                                                                                |
| default\_field            | String  | Yes       | Set a name for the all field in the Search index. If you enable the [include\_in\_all property](#include-in-all) for a child field, the contents of that child field can be searched without specifying a field name or by specifying the default field’s name in your Search query.                                                                                                      |
| default\_mapping          | Object  | No        | An object that contains settings for the default type mapping on the Search index. The default type mapping contains all documents under the \_default scope and \_default collection in the bucket. This type mapping is included for compatibility only. For more information about the properties inside the default\_mapping object, see [Default\_mapping Object](#default-mapping). |
| default\_type             | String  | No        | This setting is included for compatibility with earlier indexes only.                                                                                                                                                                                                                                                                                                                     |
| docvalues\_dynamic        | Boolean | Yes       | To include the values for an indexed field in the Search index, set docvalues\_dynamic to true. To exclude the values for an indexed field in the index, set docvalues\_dynamic to false.                                                                                                                                                                                                 |
| index\_dynamic            | Boolean | Yes       | To index any fields in the Search index where dynamic is true, set index\_dynamic to true. To exclude dynamic fields from the index, set index\_dynamic to false.                                                                                                                                                                                                                         |
| store\_dynamic            | Boolean | Yes       | To return the content from an indexed field in the Search index, set store\_dynamic to true. To exclude field content from the index, set store\_dynamic to false.                                                                                                                                                                                                                        |
| type\_field               | String  | No        | Use the same value assigned to the type\_field in doc\_config, if applicable.                                                                                                                                                                                                                                                                                                             |
| types                     | Object  | No        | An object that contains any user-defined type mappings for the Search index, as {scope}.{collection} objects inside a types object. For more information, see [Types Object](#types).                                                                                                                                                                                                     |

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

For example, if you use a [whitespace tokenizer](#guides:search/default-tokenizers-reference.adoc#whitespace), a range with a minimum of two and a maximum of three, and a space as a separator, the token `abc def` becomes `abc`, `def`, and `abc def`.

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
                }
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

| Property | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                       |
| -------- | ------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dynamic  | Boolean | Yes       | To index all available fields in a document with the default type mapping, set dynamic to true. To only index the fields you specify in the type mapping, set dynamic to false.                                                                                                                                                   |
| enabled  | Boolean | Yes       | To enable the Search Service’s default type mapping, set enabled to true. The default type mapping includes all documents in the bucket in the Search index, even if they don’t match another configured type mapping. This can increase index size and indexing time. To disable the default type mapping, set enabled to false. |

## [](#types)Types Object

The `types` object contains any additional user-defined type mappings for a Search index.

```json
            "types": {
                "inventory.hotel": {
                    "dynamic": false,
                    "enabled": true,
                    "properties": {
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
                        }
                    }
                }
            }
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `types` object is a child object of the [Mapping Object](#mapping). It contains any number of [{scope}.{collection} objects](#scope-collection):

| Property             | Type   | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {scope}.{collection} | Object | Yes       | The name of the type mapping. Corresponds to the selected scope and collection where the type mapping applies. For example, inventory.airline. For more information about the properties in an {scope}.{collection} object, see [{Scope}.{collection} Object](#scope-collection). To add a type identifier as an additional filter to your type mapping, add the filter to the end of your {scope}.{collection} object. For example, to use a type\_field filter that uses the type field, and add only documents with a type value of hotel, the object name would be {scope}.{collection}.hotel |

### [](#scope-collection){Scope}.{collection} Object

The `{scope}.{collection}` object defines a custom type mapping for a Search index:

```json
                "inventory.hotel": {
                    "dynamic": false,
                    "enabled": true,
                    "properties": {
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
                        }
                    }
                }
```

A `{scope}.{collection}` object is a child object of the [Types Object](#types). It contains the following properties:

| Property   | Type    | Required? | Description                                                                                                                                                                                                                                       |
| ---------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dynamic    | Boolean | Yes       | To index all fields under the specified scope and collection, set dynamic to true. To only index the fields you specify and enable the properties block, set dynamic to false.                                                                    |
| enabled    | Boolean | Yes       | To enable the type mapping and include any documents that match it in the Search index, set enabled to true. To remove any documents that match this type mapping from the Search index, set enabled to false.                                    |
| properties | Object  | No        | The properties object is only enabled if dynamic is set to false. Specifies properties for the fields to index in the type mapping. Contains any number of {field\_name} objects. For more information, see [{field\_name} Object](#child-fields) |

### [](#child-fields){field\_name} Object

The `{field_name}` object contains properties and an array for a child field in a type mapping. You can have multiple `{field_name}` objects in a [properties object](#properties).

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

| Property | Type    | Required? | Description                                                                                                                                        |
| -------- | ------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| enabled  | Boolean | Yes       | To add this child field to the Search index, set enabled to true. To remove this child field from the index, set enabled to false.                 |
| dynamic  | Boolean | No        | This field is included for legacy compatibility only.                                                                                              |
| fields   | Array   | Yes       | An array that contains objects with settings for each child field to index in the type mapping. For more information, see [Fields Array](#fields). |

### [](#fields)Fields Array

The `fields` array contains objects with settings for each child field to index in the type mapping:

```json
                                    "fields": [
                                        {
                                            "docvalues": true,
                                            "include_in_all": true,
                                            "include_term_vectors": true,
                                            "index": true,
                                            "name": "content",
                                            "store": true,
                                            "type": "text",
                                            "analyzer": "My_Analyzer"
                                        }
                                    ]
```

> [!TIP]
> To view the entire JSON payload, click **View**.

The `fields` array is located inside a [{field\_name} object](#child-fields). It contains the following properties:

| Property               | Type    | Required? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | ------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docvalues              | Boolean | Yes       | To include the value for each instance of the field in the Search index to support [facets](search-request-params.md#facet-name) and sorting search results, set docvalues to true. To exclude the values for each instance of this field from the index, set docvalues to false.                                                                                                                                                                   |
| include\_in\_all       | Boolean | Yes       | To allow this field to be searched without specifying the specific field’s name in the search, set include\_in\_all to true. When enabled, you can search this field through the specified default\_field set in the type mapping. To only search this field by specifying the field name, set include\_in\_all to false.                                                                                                                           |
| include\_term\_vectors | Boolean | Yes       | To use term vectors, store must be set to true. To allow the Search Service to highlight matching search terms in search results for this field, set include\_term\_vectors to true. You must also enable term vectors to use includeLocations in a Search query. For more information, see [includeLocations](search-request-params.md#includelocations). To disable term highlighting and reduce index size, set include\_term\_vectors to false. |
| index                  | Boolean | Yes       | To include the child field in the Search index, set index to true. To exclude the child field from the index, set index to false.                                                                                                                                                                                                                                                                                                                   |
| name                   | String  | Yes       | The child field’s name.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| store                  | Boolean | Yes       | To include the content of the child field in the Search index and allow its content to be viewed in search results, set store to true. To exclude the content of the child field from the index, set store to false.                                                                                                                                                                                                                                |
| type                   | String  | Yes       | The child field’s type. Can be one of: text number datetime boolean geopoint geoshape disabled For more information about the available field data types, see [Field Data Types](field-data-types-reference.md).                                                                                                                                                                                                                                    |
| analyzer               | String  | No        | If the child field’s type is text, set the analyzer to use for the child field. If you want to use the default analyzer for the content of this child field, you don’t need to include an analyzer property.                                                                                                                                                                                                                                        |