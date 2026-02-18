---
title: Object Functions
description: You can use object functions to evaluate objects, perform
  computations on attributes in an object, and to return a new object based on a
  transformation.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/objectfun.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/objectfun.html)

# Object Functions

You can use object functions to evaluate objects, perform computations on attributes in an object, and to return a new object based on a transformation.

## [](#fn-obj-add)OBJECT\_ADD(`object`, `new_attr_key`, `new_attr_value`)

### [](#description)Description

This function adds new attributes and values to a given object.

### [](#arguments)Arguments

object

An expression representing the object that you want to add to.

new\_attr\_key

The name of the attribute to add.

new\_attr\_value

The value of the attribute to add.

### [](#return-value)Return Value

The updated object.

* This function does not perform key substitution.
* If you add a duplicate attribute (that is, if the key is found), it returns an error or NULL object.
* If `new_attr_key` or `new_attr_value` is MISSING, or if `new_attr_key` is NULL, it returns the `object` unmodified.
* If `object` is not an object or NULL, it returns a NULL value object.

### [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
SELECT schedule[0] AS original,
       OBJECT_ADD(schedule[0], "day_new", 1) AS output
FROM route
LIMIT 1;
```

Results

```json
[
  {
    "original": {
      "day": 0,
      "flight": "AF198",
      "utc": "10:13:00"
    },
    "output": {
      "day": 0,
      "day_new": 1,
      "flight": "AF198",
      "utc": "10:13:00"
    }
  }
]
```

## [](#fn-obj-concat)OBJECT\_CONCAT(`expr`, `expr` …​)

### [](#description-2)Description

This function concatenates the input objects and returns a new object. It requires a minimum of two input objects.

### [](#arguments-2)Arguments

expr

An expression representing an object.

### [](#return-value-2)Return Value

An object constructed by concatenating all the input objects. If any of the input objects contain the same attribute name, the attribute from the last relevant object in the input list is copied to the output; similarly-named attributes from earlier objects in the input list are ignored.

### [](#examples-2)Examples

Query

```sqlpp
SELECT OBJECT_CONCAT({"flight": "AF198"},
    {"utc": "4:44:44"},
    {"code": "green"},
    {"code": "yellow"},
    {"passengers": ["Corrine Hill", "Vallie Ryan"]}
);
```

Results

```json
[
  {
    "$1": {
      "flight": "AF198",
      "utc": "4:44:44",
      "code": "yellow",
      "passengers": [
        "Corrine Hill",
        "Vallie Ryan"
      ]
    }
  }
]
```

## [](#fn-obj-concat2)OBJECT\_CONCAT2(`expr`, `expr` …​)

Couchbase Server 8.0

### [](#description-3)Description

This function concatenates multiple input objects into a single new object, and requires at least two input objects to work. Unlike [OBJECT\_CONCAT()](#fn-obj-concat), this function supports both plain objects and arrays of objects as arguments.

### [](#arguments-3)Arguments

expr

An expression representing an object or an array of objects. The first argument must be a plain object and cannot be an array.

### [](#return-value-3)Return Value

An object constructed by concatenating all the input objects. If any of the input objects contain the same attribute name, the attribute from the last relevant object in the input list is copied to the output; similarly-named attributes from earlier objects in the input list are ignored.

### [](#examples-3)Examples

Query

```sqlpp
SELECT OBJECT_CONCAT2(
    {"flight": "AF198"},
    [ {"utc": "4:44:44"},
      {"code": "green"},
      {"airline": "Air France"},
      {"airline": "Delta"}
    ]
);
```

Results

```json
[
  {
    "$1": {
      "flight": "AF198",
      "utc": "4:44:44",
      "code": "green",
      "airline": "Delta"
    }
  }
]
```

## [](#fn-obj-field)OBJECT\_FIELD(`object`, `field`)

### [](#description-4)Description

This function returns the value of the specified field within the given object. A field in this context may be any attribute or element, nested at any level within the object.

### [](#arguments-4)Arguments

expr

An expression representing an object.

field

A string, or any valid [expression](index.md) which evaluates to a string, representing the path to a field within the object.

You can use [nested operators](nestedops.md) to specify the path to a nested attribute or element. If any attribute names within the field path contain special characters, they must be escaped using backticks (``` `` ```).

### [](#return-value-4)Return Value

The value of the specified field. If the object does not exist, or the field cannot be found within the object at the specified location, the function returns NULL.

### [](#examples-4)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Top-Level Fields

This example returns the complete values of the specified attributes at the top level of the object.

Query

```sqlpp
SELECT OBJECT_FIELD(hotel, "public_likes") AS `array`,
       OBJECT_FIELD(hotel, "vacancy") AS `boolean`,
       OBJECT_FIELD(hotel, "id") AS `number`,
       OBJECT_FIELD(hotel, "geo") AS `object`,
       OBJECT_FIELD(hotel, "name") AS `string`
FROM hotel
LIMIT 1;
```

Results

```json
[
  {
    "array": [
      "Julius Tromp I",
      "Corrine Hilll",
      "Jaeden McKenzie",
      "Vallie Ryan",
      "Brian Kilback",
      "Lilian McLaughlin",
      "Ms. Moses Feeney",
      "Elnora Trantow"
    ],
    "boolean": true,
    "number": 10025,
    "object": {
      "accuracy": "RANGE_INTERPOLATED",
      "lat": 51.35785,
      "lon": 0.55818
    },
    "string": "Medway Youth Hostel"
  }
]
```

Nested Fields

This example specifies a nested array element and a nested object attribute at different depths in the hierarchy. In the path to the nested object attribute, the final attribute name is escaped, as it contains special characters.

Query

```sqlpp
SELECT
  OBJECT_FIELD(hotel, "reviews[1]")
    AS array_element,
  OBJECT_FIELD(hotel, "reviews[1].ratings.`Business service (e.g., internet access)`")
    AS object_attribute
FROM hotel
LIMIT 1;
```

Results

```json
[
  {
    "array_element": {
      "author": "Barton Marks",
      "content": "We found the hotel de la Monnaie through Interval ...",
      "date": "2015-03-02 19:56:13 +0300",
      "ratings": {
        "Business service (e.g., internet access)": 4,
        "Check in / front desk": 4,
        "Cleanliness": 4,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 3,
        "Value": 5
      }
    },
    "object_attribute": 4
  }
]
```

## [](#fn-obj-filter)OBJECT\_FILTER(`expression` \[, `options`\])

Couchbase Server 8.0

### [](#description-5)Description

This function extracts and returns nested fields from an input object that match a specified pattern, while retaining their original hierarchical path structure in the output. This is particularly useful when working with complex objects, as it allows you to filter fields based on patterns using either regular expressions or exact matches.

### [](#arguments-5)Arguments

expression

An expression representing an object.

options

\[Optional\] A JSON object specifying options for the function.

### [](#options)Options

| Name                          | Description                                                                                                                                                                                                                                                                                                                                                                                 | Schema  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **pattern** _optional_        | The pattern to match. This can be a regular expression or a simple string, depending on the regex parameter.                                                                                                                                                                                                                                                                                | String  |
| **regex** _optional_          | If TRUE, the pattern is treated as a regular expression. If FALSE, the pattern is treated as a simple string. **Default:** TRUE                                                                                                                                                                                                                                                             | Boolean |
| **arraysubscript** _optional_ | Specifies whether array subscripts are included in field names before applying the filter. If TRUE, array subscripts are included. If FALSE, array subscripts are replaced by \*. **Default:** TRUE                                                                                                                                                                                         | Boolean |
| **composites** _optional_     | Specifies whether the pattern should match field names that contain values requiring further processing, such as nested objects or arrays. If TRUE, the pattern is matched against every level of nested fields. If FALSE, the pattern is matched only against the deepest level of nested fields. **Default:** TRUE                                                                        | Boolean |
| **patternspace** _optional_   | A string literal with two possible values. "field": The pattern is matched against individual field names. "path": The pattern is matched against composite path names. **Default:** "path"                                                                                                                                                                                                 | String  |
| **exact** _optional_          | Specifies whether the provided pattern must be an exact match for the field or path (as determined by the patternspace parameter). This is a short-cut for the regular expression start (^) and end ($) anchors, and can be used even when regex is set to false. If TRUE, the pattern must be an exact match. If FALSE, the pattern does not need to be an exact match. **Default:** FALSE | Boolean |
| **ignorecase** _optional_     | If TRUE, the pattern matching is case-sensitive. If FALSE, the pattern matching ignores case. **Default:** FALSE                                                                                                                                                                                                                                                                            | Boolean |

### [](#return-value-5)Return Value

An object containing only the fields that match the specified pattern. Non-matching fields are excluded from the output.

### [](#examples-5)Examples

Filtering by field name

Query

```sqlpp
SELECT OBJECT_FILTER(t, {"pattern":"Business service"})
FROM `travel-sample`.`inventory`.`hotel` t
WHERE type = 'hotel'
LIMIT 2;
```

Results

```json
[
  {
    "$1": {
      "reviews": [
        {
          "ratings": {
            "Business service (e.g., internet access)": 4
          }
        }
      ]
    }
  },
  {
    "$1": null
  }
]
```

Filtering by full path

You can use [OBJECT\_PATHS()](#fn-obj-paths) to generate the full path to a field, and then use that path in the `pattern` parameter.

Query

```sqlpp
SELECT OBJECT_FILTER(t, { "pattern": "reviews[1].ratings.Service", "regex": false })
FROM `travel-sample`.`inventory`.`hotel` t
WHERE type = 'hotel'
LIMIT 1;
```

Results

```json
[
  {
    "$1": {
      "reviews": [
        {
          "ratings": {
            "Service": 3
          }
        }
      ]
    }
  }
]
```

## [](#fn-obj-inner-pairs)OBJECT\_INNER\_PAIRS(`expression`)

### [](#description-6)Description

This function returns an array of objects, containing the names and values of each attribute in the input object. It is particularly useful when iterating over multiple objects in an array, as it collates the values from similarly-named attributes into a single nested array.

In this case, the function does not return a value from any object which does not contain the shared attribute name, rather like an INNER JOIN. For an illustration, refer to the examples below.

### [](#arguments-6)Arguments

expression

An expression representing an object.

### [](#return-value-6)Return Value

An array of objects, each containing two attributes:

name

The name of an attribute in the source object.

val

The value of an attribute in the source object; or an array, containing the collated values of similarly-named attributes in the source objects.

The objects in the array are sorted by attribute name, in SQL++ collation order.

### [](#examples-6)Examples

Single object

Query

```sqlpp
SELECT OBJECT_INNER_PAIRS({"flight": "AI444", "utc": "4:44:44", "codename": "green"})
    AS inner_pairs;
```

Results

```json
[
  {
    "inner_pairs": [
      {
        "name": "codename",
        "val": "green"
      },
      {
        "name": "flight",
        "val": "AI444"
      },
      {
        "name": "utc",
        "val": "4:44:44"
      }
    ]
  }
]
```

Iterating over objects in an array

In this example, notice that where the source objects have similarly-named attributes, the values from each of those attributes are collated into a single array in the output.

Query

```sqlpp
WITH special_flights AS ([{"flight": "AI444", "utc": "4:44:44", "codename": "green"},
                          {"flight": "AI333", "utc": "3:33:33", "alert": "red"},
                          {"flight": "AI222", "utc": "2:22:22", "codename": "yellow"}])
SELECT OBJECT_INNER_PAIRS(special_flights[*]) AS inner_pairs;
```

Results

```json
[
  {
    "inner_pairs": [
      {
        "name": "alert",
        "val": "red"
      },
      {
        "name": "codename",
        "val": [
          "green",
          "yellow"
        ]
      },
      {
        "name": "flight",
        "val": [
          "AI444",
          "AI333",
          "AI222"
        ]
      },
      {
        "name": "utc",
        "val": [
          "4:44:44",
          "3:33:33",
          "2:22:22"
        ]
      }
    ]
  }
]
```

## [](#fn-obj-inner-values)OBJECT\_INNER\_VALUES(`expression`)

### [](#description-7)Description

This function returns an array, containing the values of each attribute in the input object. It is particularly useful when iterating over multiple objects in an array, as it collates the values from similarly-named attributes into a single nested array.

In this case, the function does not return a value from any object which does not contain the shared attribute name, rather like an INNER JOIN. For an illustration, refer to the examples below.

### [](#arguments-7)Arguments

expression

An expression representing an object.

### [](#return-value-7)Return Value

An array of the values contained within the source object. The values in the array are sorted by the corresponding attribute names in the source object, in SQL++ collation order.

### [](#examples-7)Examples

Single object

Query

```sqlpp
SELECT OBJECT_INNER_VALUES({"flight": "AI444", "utc": "4:44:44", "codename": "green"})
    AS inner_values;
```

Results

```json
[
  {
    "inner_values": [
      "green",
      "AI444",
      "4:44:44"
    ]
  }
]
```

Iterating over objects in an array

In this example, notice that where the source objects have similarly-named attributes, the values from each of those attributes are collated into a single array in the output.

Query

```sqlpp
WITH special_flights AS ([{"flight": "AI444", "utc": "4:44:44", "codename": "green"},
                          {"flight": "AI333", "utc": "3:33:33", "alert": "red"},
                          {"flight": "AI222", "utc": "2:22:22", "codename": "yellow"}])
SELECT OBJECT_INNER_VALUES(special_flights[*]) AS inner_values;
```

Results

```json
[
  {
    "inner_values": [
      "red",
      [
        "green",
        "yellow"
      ],
      [
        "AI444",
        "AI333",
        "AI222"
      ],
      [
        "4:44:44",
        "3:33:33",
        "2:22:22"
      ]
    ]
  }
]
```

## [](#fn-obj-length)OBJECT\_LENGTH(`expression`)

_Equivalent_: [LEN()](metafun.md#len)

### [](#description-8)Description

This function returns the number of name-value pairs in the object. It only counts the top-level attributes and does not recurse into nested objects.

### [](#arguments-8)Arguments

expression

An object or an expression that evaluates to an object.

### [](#return-value-8)Return Value

An integer.

If the input expression is not an object, the function returns `null`; if the input expression is `missing`, the function returns `missing`.

### [](#examples-8)Examples

Query

```sqlpp
SELECT OBJECT_LENGTH({"abc": 1, "def": 2, "ghi": {"uvw": 3, "xyz": 4}});
```

Results

```json
[
    {
        "$1": 3
    }
]
```

## [](#fn-obj-names)OBJECT\_NAMES(`expression`)

### [](#description-9)Description

This function returns an array, containing the names of each attribute in the input object. It is particularly useful when iterating over multiple objects in an array, as it collates similar attribute names.

### [](#arguments-9)Arguments

expression

An expression representing an object.

### [](#return-value-9)Return Value

An array of the attribute names contained within the source object. The attribute names are sorted in SQL++ collation order.

### [](#examples-9)Examples

Single object

Query

```sqlpp
SELECT OBJECT_NAMES({"flight": "AI444", "utc": "4:44:44", "codename": "green"})
    AS names;
```

Results

```json
[
  {
    "names": [
      "codename",
      "flight",
      "utc"
    ]
  }
]
```

Iterating over objects in an array

Query

```sqlpp
WITH special_flights AS ([{"flight": "AI444", "utc": "4:44:44", "codename": "green"},
                          {"flight": "AI333", "utc": "3:33:33", "alert": "red"},
                          {"flight": "AI222", "utc": "2:22:22", "codename": "yellow"}])
SELECT OBJECT_NAMES(special_flights[*]) AS names;
```

Results

```json
[
  {
    "names": [
      "alert",
      "codename",
      "flight",
      "utc"
    ]
  }
]
```

## [](#fn-obj-pairs)OBJECT\_PAIRS(`expression` \[, `options` \])

_Alias_: **OBJECT\_OUTER\_PAIRS(`expression` \[, `options` \])**

### [](#description-10)Description

This function returns an array of objects, containing the names and values of each attribute in the input object. It also provides an option to return attribute types instead of values.

The function is particularly useful when iterating over multiple objects in an array, as it collates the values from similarly-named attributes into a single nested array. However, if an object does not contain a shared attribute name, it returns a null entry, similar to an OUTER JOIN.

For an illustration, refer to the examples below.

### [](#arguments-10)Arguments

expression

An expression representing an object.

options

\[Optional\] A JSON object specifying options for the function.

### [](#options-2)Options

| Name                 | Description                                                                                                                                                                                                        | Schema  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| **types** _required_ | Determines whether to return attribute types or values. If TRUE, the function returns the name and type of each attribute. If FALSE, the function returns the name and value of each attribute. **Default:** FALSE | Boolean |

### [](#return-value-10)Return Value

An array of objects, each containing the following attributes:

| Name     | Description                                                                                                                                      | Schema                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **name** | The name of an attribute in the source object.                                                                                                   | String                                                                         |
| **val**  | The value of an attribute in the source object; or an array, containing the collated values of similarly-named attributes in the source objects. | Depends on the value returned. It can be a string, number, boolean, or others. |
| **type** | The type of an attribute in the source object. Returned only when the types parameter is set to TRUE.                                            | String                                                                         |

> [!NOTE]
> Each returned object will have either **val** or **type** (depending on the specified options), and not both. Also, the objects in the array are sorted by attribute name, in SQL++ collation order.

### [](#examples-10)Examples

A single input object returning names and values

Query

```sqlpp
SELECT OBJECT_PAIRS({"flight": "AI444", "utc": "4:44:44", "codename": "green"})
    AS outer_pairs;
```

Results

```json
[
  {
    "outer_pairs": [
      {
        "name": "codename",
        "val": "green"
      },
      {
        "name": "flight",
        "val": "AI444"
      },
      {
        "name": "utc",
        "val": "4:44:44"
      }
    ]
  }
]
```

A single input object returning names and types

Query

```sqlpp
SELECT OBJECT_PAIRS({"flight": "AI444", "utc": "4:44:44", "codename": "green"},{"types":TRUE})
    AS outer_pairs;
```

Results

```json
[
  {
    "outer_pairs": [
      {
        "name": "codename",
        "type": "string"
      },
      {
        "name": "flight",
        "type": "string"
      },
      {
        "name": "utc",
        "type": "string"
      }
    ]
  }
]
```

Iterating over objects in an array

In this example, notice that where the source objects have similarly-named attributes, the values from each of those attributes are collated into a single array in the output.

Query

```sqlpp
WITH special_flights AS ([{"flight": "AI444", "utc": "4:44:44", "codename": "green"},
                          {"flight": "AI333", "utc": "3:33:33", "alert": "red"},
                          {"flight": "AI222", "utc": "2:22:22", "codename": "yellow"}])
SELECT OBJECT_PAIRS(special_flights[*]) AS outer_pairs;
```

Results

```json
[
  {
    "outer_pairs": [
      {
        "name": "alert",
        "val": [
          null,
          "red",
          null
        ]
      },
      {
        "name": "codename",
        "val": [
          "green",
          null,
          "yellow"
        ]
      },
      {
        "name": "flight",
        "val": [
          "AI444",
          "AI333",
          "AI222"
        ]
      },
      {
        "name": "utc",
        "val": [
          "4:44:44",
          "3:33:33",
          "2:22:22"
        ]
      }
    ]
  }
]
```

## [](#fn-obj-pairs-nested)OBJECT\_PAIRS\_NESTED(`object` \[, `options`\])

### [](#description-11)Description

Similar to [OBJECT\_PAIRS()](#fn-obj-pairs), this function returns an array of objects, containing the names and values of each field in the input object. It also provides an option to return field types instead of values. A field in this context may be any attribute or element, nested at any level within the object.

This function may be useful when iterating over multiple objects in an array, as it collates and unnests the values from similarly-named fields across all objects in the input array. However, if an object does not contain a shared field name, it returns a null entry, similar to an OUTER JOIN.

For an illustration, refer to the examples below.

### [](#arguments-11)Arguments

object

An expression representing an object.

options

\[Optional\] A JSON object specifying options for the function.

### [](#options-3)Options

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                  | Schema  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **composites** _optional_   | If TRUE, every level of every nested field is displayed. If FALSE, only the deepest possible nested fields are returned. **Default:** FALSE                                                                                                                                                                                                                                                  | Boolean |
| **types** _optional_        | Determines whether to return field types or values. If TRUE, the function returns the name and type of each field. If FALSE, the function returns the name and value of each field. **Default:** FALSE                                                                                                                                                                                       | Boolean |
| **pattern** _optional_      | The pattern used to filter the returned paths. It can be a regular expression or a simple string, depending on the regex parameter.                                                                                                                                                                                                                                                          | String  |
| **regex** _optional_        | If TRUE, the pattern is treated as a regular expression. If FALSE, the pattern is treated as a simple string. **Default:** TRUE                                                                                                                                                                                                                                                              | Boolean |
| **patternspace** _optional_ | A string literal with two possible values. "field": The pattern is matched against individual field names. "path": The pattern is matched against composite path names. **Default:** "path"                                                                                                                                                                                                  | String  |
| **exact** _optional_        | Determines whether the provided pattern must be an exact match for the field or path (as determined by the patternspace parameter). This is a short-cut for the regular expression start (^) and end ($) anchors, and can be used even when regex is set to false. If TRUE, the pattern must be an exact match. If FALSE, the pattern does not need to be an exact match. **Default:** FALSE | Boolean |
| **ignorecase** _optional_   | If TRUE, the pattern matching is case-sensitive. If FALSE, the pattern matching ignores case. **Default:** FALSE                                                                                                                                                                                                                                                                             | Boolean |
| **report** _optional_       | Controls the output of the name field, allowing selection between the full path or the final field name. Possible values are: "field": Outputs only the final field name. "path": Outputs the full path to the field. **Default:** "path"                                                                                                                                                    | String  |

### [](#return-value-11)Return Value

An array of objects, each containing the following attributes:

| Name     | Description                                                                                                                                                                                                                                                                                                                  | Schema                                                                         |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **name** | The full path to every possible field within the source object, subject to the specified options. The result uses [nested operators](nestedops.md) to specify the path to all nested attributes or elements. If any attribute names within a field path contain special characters, they are escaped using backticks (\`\`). | String                                                                         |
| **val**  | The value of a field in the source object; or an array, containing the collated values of similarly-named fields in the source objects.                                                                                                                                                                                      | Depends on the value returned. It can be a string, number, boolean, or others. |
| **type** | The type of a field in the source object. Returned only when the 'types' parameter is set to 'TRUE'.                                                                                                                                                                                                                         | String                                                                         |

> [!NOTE]
> Each returned object will have either **val** or **type** (depending on the specified options), and not both. Also, the objects in the array are sorted by field name, in SQL++ collation order.

### [](#examples-11)Examples

Single object

Query

```sqlpp
WITH input AS ({
    "attribute": {"flight-name": "AI444", "flight-number": 737}
  })
SELECT OBJECT_PAIRS_NESTED(input) AS nested_pairs,
       OBJECT_PAIRS_NESTED(input, {"composites": true}) AS nested_pairs_comp,
       OBJECT_PAIRS_NESTED(input, {"pattern": "name"}) AS nested_pairs_pattern,
       OBJECT_PAIRS_NESTED(input, {"types": true}) AS nested_pairs_types,
       OBJECT_PAIRS_NESTED(input, {"pattern": "number", "patternspace":"field"}) AS filtered_fields,
       OBJECT_PAIRS_NESTED(input, {"pattern": "-name$", "patternspace":"field", "regex":true})
                                   AS filtered_fields_regex;
```

Results

```json
[
  {
    "nested_pairs": [
      {
        "name": "attribute.flight-name",
        "val": "AI444"
      },
      {
        "name": "attribute.flight-number",
        "val": 737
      }
    ],
    "nested_pairs_comp": [
      {
        "name": "attribute",
        "val": {
          "flight-name": "AI444",
          "flight-number": 737
        }
      },
      {
        "name": "attribute.flight-name",
        "val": "AI444"
      },
      {
        "name": "attribute.flight-number",
        "val": 737
      }
    ],
    "nested_pairs_pattern": [
      {
        "name": "attribute.flight-name",
        "val": "AI444"
      }
    ],
    "nested_pairs_types": [
      {
        "name": "attribute.flight-name",
        "type": "string"
      },
      {
        "name": "attribute.flight-number",
        "type": "number"
      }
    ],
    "filtered_fields": [
      {
        "name": "attribute.flight-number",
        "val": 737
      }
    ],
    "filtered_fields_regex": [
      {
        "name": "attribute.flight-name",
        "val": "AI444"
      }
    ]
  }
]
```

Iterating over objects in an array

In this example, notice that where the source objects have similarly-named attributes, the values from each of those attributes are collated into a single array in the output. Each collated array is then unnested to show the name and value of its elements.

Query

```sqlpp
WITH special_flights AS ([{"flight": "AI444", "utc": "4:44:44", "codename": "green"},
                          {"flight": "AI333", "utc": "3:33:33", "alert": "red"},
                          {"flight": "AI222", "utc": "2:22:22", "codename": "yellow"}])
SELECT OBJECT_PAIRS_NESTED(special_flights[*], {"composites": true}) AS nested_pairs;
```

Results

```json
[
  {
    "nested_pairs": [
      {
        "name": "alert",
        "val": [
          null,
          "red",
          null
        ]
      },
      {
        "name": "alert[0]",
        "val": null
      },
      {
        "name": "alert[1]",
        "val": "red"
      },
      {
        "name": "alert[2]",
        "val": null
      },
      {
        "name": "codename",
        "val": [
          "green",
          null,
          "yellow"
        ]
      },
      {
        "name": "codename[0]",
        "val": "green"
      },
      {
        "name": "codename[1]",
        "val": null
      },
      {
        "name": "codename[2]",
        "val": "yellow"
      },
      {
        "name": "flight",
        "val": [
          "AI444",
          "AI333",
          "AI222"
        ]
      },
      {
        "name": "flight[0]",
        "val": "AI444"
      },
      {
        "name": "flight[1]",
        "val": "AI333"
      },
      {
        "name": "flight[2]",
        "val": "AI222"
      },
      {
        "name": "utc",
        "val": [
          "4:44:44",
          "3:33:33",
          "2:22:22"
        ]
      },
      {
        "name": "utc[0]",
        "val": "4:44:44"
      },
      {
        "name": "utc[1]",
        "val": "3:33:33"
      },
      {
        "name": "utc[2]",
        "val": "2:22:22"
      }
    ]
  }
]
```

Compare this example with [OBJECT\_PAIRS() Example 3](#obj-pairs-ex3).

## [](#fn-obj-paths)OBJECT\_PATHS(`object` \[, `options`\] )

### [](#description-12)Description

This function returns the paths to all the fields within an object. A field in this context may be any attribute or element, nested at any level within the object.

### [](#arguments-12)Arguments

object

An expression representing an object.

options

\[Optional\] An object containing the following possible parameters.

### [](#options-4)Options

| Name                          | Description                                                                                                                                                                                                                                                                                                                                                                                  | Schema  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **composites** _optional_     | If TRUE, every level of every nested field is displayed. If FALSE, only the deepest possible nested fields are returned. **Default:** TRUE                                                                                                                                                                                                                                                   | Boolean |
| **arraysubscript** _optional_ | If TRUE, array subscripts are returned. If FALSE, array subscripts are replaced by \*. **Default:** TRUE                                                                                                                                                                                                                                                                                     | Boolean |
| **unique** _optional_         | If TRUE, duplicate field names are collapsed to single unique field name. If FALSE, all duplicate field names are returned. Typically used when arrays are expanded and array subscripts are not returned. **Default:** TRUE                                                                                                                                                                 | Boolean |
| **pattern** _optional_        | A regular expression used to filter the returned paths. Used in conjunction with the patternspace setting.                                                                                                                                                                                                                                                                                   | String  |
| **patternspace** _optional_   | A string literal with two possible values. "field": The pattern is matched against individual field names. "path": The pattern is matched against composite path names. **Default:** "path"                                                                                                                                                                                                  | String  |
| **exact** _optional_          | Determines whether the provided pattern must be an exact match for the field or path (as determined by the patternspace parameter). This is a short-cut for the regular expression start (^) and end ($) anchors, and can be used even when regex is set to false. If TRUE, the pattern must be an exact match. If FALSE, the pattern does not need to be an exact match. **Default:** FALSE | Boolean |
| **ignorecase** _optional_     | If TRUE, the pattern matching is case-sensitive. If FALSE, the pattern matching ignores case. **Default:** FALSE                                                                                                                                                                                                                                                                             | Boolean |

### [](#return-value-12)Return Value

An array containing the full path to every possible field within the source object, subject to the specified options.

The result uses [nested operators](nestedops.md) to specify the path to all nested attributes or elements. If any attribute names within a field path contain special characters, they are escaped using backticks (``` `` ```).

* If `object` is MISSING, the function returns a MISSING value.
* If `object` is not an object, the function returns a NULL value.
* If `options` is not an object, the function returns a NULL value.

### [](#examples-12)Examples

Composite paths

Query

```sqlpp
WITH input AS ({
  "attribute": {"first-part": 1, "second-part": 2}
})
SELECT OBJECT_PATHS(input, {"composites": true}) AS composite,
       OBJECT_PATHS(input, {"composites": false}) AS non_composite;
```

Results

```json
[
  {
    "composite": [
      "attribute",
      "attribute.first-part",
      "attribute.second-part"
    ],
    "non_composite": [
      "attribute.first-part",
      "attribute.second-part"
    ]
  }
]
```

Array subscripts and unique field names

Query

```sqlpp
WITH input AS ({
  "attribute": [ { "name": "elem1"}, {"name": "elem2"}]
})
SELECT
  OBJECT_PATHS(input, {"arraysubscript": true})
    AS subscripts,
  OBJECT_PATHS(input, {"arraysubscript": false, "unique": false})
    AS no_subscripts_not_unique,
  OBJECT_PATHS(input, {"arraysubscript": false, "unique": true})
    AS no_subscripts_unique;
```

Results

```json
[
  {
    "no_subscripts_not_unique": [
      "attribute",
      "attribute[*].name",
      "attribute[*].name"
    ],
    "no_subscripts_unique": [
      "attribute",
      "attribute[*].name"
    ],
    "subscripts": [
      "attribute",
      "attribute[0].name",
      "attribute[1].name"
    ]
  }
]
```

Pattern matching and pattern space

This example searches for strings beginning with "n" and also fields that exactly match "name".

Query

```sqlpp
WITH input AS ({
  "attribute": {"name": "elem1"}
})
SELECT
  OBJECT_PATHS(input)
    AS all_paths,
  OBJECT_PATHS(input, {"pattern": "^n", "patternspace": "field"})
    AS field_starts_with_n,
  OBJECT_PATHS(input, {"pattern": "^n", "patternspace": "path"})
    AS path_starts_with_n,
  OBJECT_PATHS(input, {"pattern": "name", "patternspace": "field", "exact": true})
    AS exact_field_name;
```

Results

```json
[
  {
    "all_paths": [
      "attribute",
      "attribute.name"
    ],
    "field_starts_with_n": [
      "attribute.name"
    ],
    "path_starts_with_n": [],
    "exact_field_name": [
      "attribute.name"
    ]
  }
]
```

Complex example

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
SELECT OBJECT_PATHS(hotel, {"composites": false, "arraysubscript": false}) AS paths
FROM hotel
LIMIT 1;
```

Results

```json
[
  {
    "paths": [
      "address",
      "alias",
      "checkin",
      "checkout",
      "city",
      "country",
      "description",
      "directions",
      "email",
      "fax",
      "free_breakfast",
      "free_internet",
      "free_parking",
      "geo.accuracy",
      "geo.lat",
      "geo.lon",
      "id",
      "name",
      "pets_ok",
      "phone",
      "price",
      "public_likes",
      "reviews[*].author",
      "reviews[*].content",
      "reviews[*].date",
      "reviews[*].ratings[*].Cleanliness",
      "reviews[*].ratings[*].Location",
      "reviews[*].ratings[*].Overall",
      "reviews[*].ratings[*].Rooms",
      "reviews[*].ratings[*].Service",
      "reviews[*].ratings[*].Value",
      "reviews[*].ratings[*].`Business service (e.g., internet access)`",
      "reviews[*].ratings[*].`Check in / front desk`",
      "state",
      "title",
      "tollfree",
      "type",
      "url",
      "vacancy"
    ]
  }
]
```

## [](#fn-obj-put)OBJECT\_PUT(`object`, `attr_key`, `attr_value`)

### [](#description-13)Description

This function adds new or updates existing attributes and values to a given object.

### [](#arguments-13)Arguments

object

An expression representing an object.

attr\_key

The name of the attribute to insert or update.

attr\_value

The value of the attribute.

### [](#return-value-13)Return Value

The updated object.

* If `attr_key` is found in the object, it replaces the corresponding attribute value by `attr_value`.
* If `attr_value` is MISSING, it deletes the corresponding existing key (if any), like [OBJECT\_REMOVE()](#fn-obj-remove).
* If `attr_key` is MISSING, it returns a MISSING value.
* If `attr_key` is not an object, it returns a NULL value.

### [](#examples-13)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
SELECT schedule[0] AS original,
       OBJECT_PUT(schedule[0], "day", 1) AS output
FROM route
LIMIT 1;
```

Results

```json
[
  {
    "original": {
      "day": 0,
      "flight": "AF198",
      "utc": "10:13:00"
    },
    "output": {
      "day": 1,
      "flight": "AF198",
      "utc": "10:13:00"
    }
  }
]
```

## [](#fn-obj-rename)OBJECT\_RENAME(`input_obj`, `old_field`, `new_field`)

### [](#description-14)Description

Renames the attribute `old_field` to `new_field` in the JSON input object `input_obj`.

### [](#arguments-14)Arguments

input\_obj

Any JSON object, or SQL++ expression that can evaluate to a JSON object, representing the search object.

old\_field

A string, or any valid [expression](index.md) which evaluates to a string, representing the old (original) attribute name inside the JSON object `input_obj`.

new\_field

A string, or any valid [expression](index.md) which evaluates to a string, representing the new attribute name to replace `old_field` inside the JSON object `input_obj`.

### [](#return-value-14)Return Value

The input object with the new attribute name. Note that if the new attribute name already exists in the input object, the original attribute with that name is replaced.

### [](#examples-14)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Changing a field name

Query

```sqlpp
SELECT t AS original,
       OBJECT_RENAME(t, "name", "new_name") AS output
FROM airline AS t
LIMIT 1;
```

Results

```json
[
  {
    "original": {
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "name": "40-Mile Air",
      "type": "airline"
    },
    "output": {
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "new_name": "40-Mile Air",
      "type": "airline"
    }
  }
]
```

## [](#fn-obj-remove)OBJECT\_REMOVE(`object`, `attr_key`)

### [](#description-15)Description

This function removes the specified attribute and corresponding values from the given object.

### [](#attributes)Attributes

object

An expression representing an object.

attr\_key

The name of the attribute to remove.

### [](#return-value-15)Return Value

The input object without the removed attribute.

* If the `attr_key` is MISSING, it returns a MISSING value.
* If the `attr_key` is not an object, it returns a NULL value.

### [](#examples-15)Examples

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
SELECT schedule[0] AS original,
       OBJECT_REMOVE(schedule[0], "day") AS output
FROM route
LIMIT 1;
```

Results

```json
[
  {
    "original": {
      "day": 0,
      "flight": "AF198",
      "utc": "10:13:00"
    },
    "output": {
      "flight": "AF198",
      "utc": "10:13:00"
    }
  }
]
```

Query

```sqlpp
SELECT OBJECT_REMOVE({"abc": 1, "def": 2, "ghi": 3}, "def");
```

Results

```json
[
  {
    "$1": {
      "abc": 1,
      "ghi": 3
    }
  }
]
```

## [](#fn-obj-replace)OBJECT\_REPLACE(`input_obj`, `old_value`, `new_value`)

### [](#description-16)Description

Replaces all occurrences of the value `value_old` to `value_new` in the JSON input object `input_obj`.

### [](#arguments-15)Arguments

input\_obj

Any JSON object, or SQL++ expression that can evaluate to a JSON object, representing the search object.

old\_value

A string, or any valid [expression](index.md) which evaluates to a string, representing the old (original) value name inside the JSON object `input_obj`.

new\_value

A string, or any valid [expression](index.md) which evaluates to a string, representing the new value name to replace `old_value` inside the JSON object `input_obj`.

### [](#return-value-16)Return Value

The JSON object `input_obj` with replaced values.

### [](#examples-16)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Replace any occurrences of "airline" with "airplane"

Query

```sqlpp
SELECT t AS original,
       OBJECT_REPLACE(t, "airline", "airplane") AS output
FROM airline AS t
LIMIT 1;
```

Results

```json
[
  {
    "original": {
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "name": "40-Mile Air",
      "type": "airline"
    },
    "output": {
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "name": "40-Mile Air",
      "type": "airplane"
    }
  }
]
```

## [](#fn-obj-type)OBJECT\_TYPES(`expression`)

Couchbase Server 8.0

### [](#description-17)Description

This function returns the data type of every field in the supplied object, as reported by the [TYPE()](typefun.md#fn-type-type) function.

### [](#arguments-16)Arguments

expression

An expression representing an object.

### [](#return-value-17)Return Value

An object with the same fields as the input object, but with all values replaced by their corresponding data types.

### [](#example)Example

Query

```sqlpp
SELECT OBJECT_TYPES({"flight": "AI444",
                     "duration": 180,
                     "gate": NULL,
                     "aircraft": {"model": "Boeing 737"}})
    AS object_types;
```

Results

```json
[
    {
        "object_types":{
            "flight":"string",
            "duration":"number",
            "gate":"null",
            "aircraft":"object"
        }
    }
]
```

## [](#fn-obj-types-nested)OBJECT\_TYPES\_NESTED(`expression`)

Couchbase Server 8.0

### [](#description-18)Description

This function returns the data type of every non-composite field in the supplied object, as reported by the [TYPE()](typefun.md#fn-type-type) function. Additionally, all composite type fields (ARRAYs and OBJECTs) are recursively processed in the same way, returning the data types of all nested values.

### [](#arguments-17)Arguments

expression

An expression representing an object.

### [](#return-value-18)Return Value

An object with the same fields as the input object, but with all values replaced by their corresponding non-composite data types.

### [](#example-2)Example

Query

```sqlpp
SELECT OBJECT_TYPES_NESTED({"flight":"AI444",
                            "crewMembers": ["Alice Bobson",
                                            "John Flo",
                                            true],
                            "gate": NULL,
                            "aircraft": {"model": "Boeing 737",
                                         "capacity":200}})
    AS object_types_nested;
```

Results

```json
[
  {
    "object_types_nested": {
      "flight": "string",
      "crewMembers": [
        "string",
        "string",
        "boolean"
      ],
      "gate": "null",
      "aircraft": {
        "model": "string",
        "capacity":"number"
      }
    }
  }
]
```

## [](#fn-obj-unwrap)OBJECT\_UNWRAP(`expression`)

### [](#description-19)Description

This function enables you to unwrap an object without knowing the name of the attribute.

### [](#arguments-18)Arguments

expression

An expression representing an object.

### [](#return-value-19)Return Value

If the argument is an object with exactly one attribute, this function returns the value in the attribute. If the argument is MISSING, it returns MISSING. For all other cases, it returns NULL.

### [](#examples-17)Examples

Query

```sqlpp
SELECT OBJECT_UNWRAP({"name": "value"}) AS single,
       OBJECT_UNWRAP({"name": MISSING}) AS `missing`,
       OBJECT_UNWRAP({"name": "value", "name2": "value2"}) AS multiple,
       OBJECT_UNWRAP("some-string") AS `string`;
```

Results

```json
[
  {
    "missing": null,
    "multiple": null,
    "single": "value",
    "string": null
  }
]
```

## [](#fn-obj-values)OBJECT\_VALUES(`expression`)

_Alias_: **OBJECT\_OUTER\_VALUES(`expression`)**

### [](#description-20)Description

This function returns an array, containing the values of each attribute in the input object. It is particularly useful when iterating over multiple objects in an array, as it collates the values from similarly-named attributes into a single nested array.

In this case, the function returns a null entry from any object which does not contain the shared attribute name, rather like an OUTER JOIN. For an illustration, refer to the examples below.

### [](#arguments-19)Arguments

expression

An expression representing an object.

### [](#return-value-20)Return Value

An array of the values contained within the source object. The values in the array are sorted by the corresponding attribute names in the source object, in SQL++ collation order.

### [](#examples-18)Examples

Single object

Query

```sqlpp
SELECT OBJECT_VALUES({"flight": "AI444", "utc": "4:44:44", "codename": "green"})
    AS outer_values;
```

Results

```json
[
  {
    "outer_values": [
      "green",
      "AI444",
      "4:44:44"
    ]
  }
]
```

Iterating over objects in an array

In this example, notice that where the source objects have similarly-named attributes, the values from each of those attributes are collated into a single array in the output.

Query

```sqlpp
WITH special_flights AS ([{"flight": "AI444", "utc": "4:44:44", "codename": "green"},
                          {"flight": "AI333", "utc": "3:33:33", "alert": "red"},
                          {"flight": "AI222", "utc": "2:22:22", "codename": "yellow"}])
SELECT OBJECT_VALUES(special_flights[*]) AS outer_values;
```

Results

```json
[
  {
    "outer_values": [
      [
        null,
        "red",
        null
      ],
      [
        "green",
        null,
        "yellow"
      ],
      [
        "AI444",
        "AI333",
        "AI222"
      ],
      [
        "4:44:44",
        "3:33:33",
        "2:22:22"
      ]
    ]
  }
]
```