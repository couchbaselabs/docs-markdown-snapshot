[View original HTML](/server/7.2/n1ql/n1ql-language-reference/metafun.html)

Miscellaneous utility functions enable you to perform tasks beyond the usual evaluation and transformation of data. For example, there are functions to retrieve information about a document or item, perform base64 encoding and decoding, generate UUIDs, and control the flow of a query.

## [](#abort)ABORT(`expression`)

### [](#description)Description

Generates an error. The error message contains the text specified by the given `expression`.

This function is useful for flow control when [creating inline user-defined functions](createfunction.md). You can use [conditional operators](conditionalops.md) to check the parameters, and use this function to generate an error if something is wrong.

### [](#arguments)Arguments

expression

An expression resolving to a string.

### [](#return-value)Return Value

The function does not return a return value.

If this function is executed in a query, it causes the query to halt with an error code 5011\. The error message contains the text specified by the given `expression`.

When this function is executed by a user-defined function, it causes the query to halt with an error code 10109\. The error message shows the name of the user-defined function and contains the text specified by the given `expression`.

### [](#examples)Examples

Abort a query

Query

```sqlpp
SELECT ABORT("Something went wrong");
```

Result

```json
[
  {
    "code": 5011,
    "msg": "Abort: \"Something went wrong\". - cause: \"Something went wrong\""
  }
]
```

User-defined function with error checking

Function

```sqlpp
CREATE OR REPLACE FUNCTION rstr(vString, vLen) LANGUAGE INLINE AS
CASE
  WHEN NOT IS_STRING(vString)
    THEN ABORT("Search string is not a string")
  WHEN NOT IS_NUMBER(vLen)
    THEN ABORT("Substring length is not a number")
  WHEN vLen > LENGTH(vString)
    THEN ABORT("Substring longer than search string")
  ELSE SUBSTR(vString, LENGTH(vString) - vLen, vLen)
END;
```

Test invalid string argument

```sqlpp
EXECUTE FUNCTION rstr(100, 4);
```

Result

```json
[
  {
    "code": 10109,
    "msg": "Error executing function rstr : \"Search string is not a string\" - cause: \"Search string is not a string\""
  }
]
```

Test invalid number argument

```sqlpp
EXECUTE FUNCTION rstr("Couchbase", "foo");
```

Result

```json
[
  {
    "code": 10109,
    "msg": "Error executing function rstr : \"Substring length is not a number\" - cause: \"Substring length is not a number\""
  }
]
```

Test out-of-range value

```sqlpp
EXECUTE FUNCTION rstr("Couchbase", 10);
```

Result

```json
[
  {
    "code": 10109,
    "msg": "Error executing function rstr : \"Substring longer than search string\" - cause: \"Substring longer than search string\""
  }
]
```

Test with valid arguments

```sqlpp
EXECUTE FUNCTION rstr("Couchbase", 4);
```

Result

```json
[
  "base"
]
```

## [](#base64)BASE64(`expression`)

_Alias_: [BASE64\_ENCODE()](#base64-encode)

### [](#description-2)Description

Returns the [base64](https://en.wikipedia.org/wiki/Base64) encoding of the given `expression`.

### [](#arguments-2)Arguments

expression

An expression representing any supported SQL++ datatype.

### [](#return-value-2)Return Value

A string representing the base64 encoding of the input expression. If the input expression is `missing`, the return value is also `missing`.

### [](#example)Example

Query

```sqlpp
SELECT BASE64([1, 2, 3, 4]) AS `array`,
       BASE64(false) AS `boolean`,
       BASE64(missing) AS `missing`,
       BASE64(null) AS `null`,
       BASE64(1234) AS `number`,
       BASE64( {"a": 1, "b": 2, "c": [1, 2, 3]} ) AS `object`,
       BASE64("Couchbase") AS `string`;
```

Result

```json
[
  {
    "array": "WzEsMiwzLDRd",
    "boolean": "ZmFsc2U=",
    "null": "bnVsbA==",
    "number": "MTIzNA==",
    "object": "eyJhIjoxLCJiIjoyLCJjIjpbMSwyLDNdfQ==",
    "string": "IkNvdWNoYmFzZSI="
  }
]
```

## [](#base64-encode)BASE64\_ENCODE(`expression`)

Alias of [BASE64()](#base64).

## [](#base64-decode)BASE64\_DECODE(`expression`)

### [](#description-3)Description

Reverses the encoding done by the [BASE64()](#base64) or [BASE64\_ENCODE()](#base64-encode) functions.

### [](#arguments-3)Arguments

expression

An expression representing a valid base64-encoded string.

### [](#return-value-3)Return Value

The decoded value of the input expression. If the input expression is `missing`, the return value is also `missing`.

### [](#example-2)Example

Query

```sqlpp
SELECT BASE64_DECODE("WzEsMiwzLDRd") AS `array`,
       BASE64_DECODE("ZmFsc2U=") AS `boolean`,
       BASE64_DECODE(missing) AS `missing`,
       BASE64_DECODE("bnVsbA==") AS `null`,
       BASE64_DECODE("MTIzNA==") AS `number`,
       BASE64_DECODE("eyJhIjoxLCJiIjoyLCJjIjpbMSwyLDNdfQ==") AS `object`,
       BASE64_DECODE("IkNvdWNoYmFzZSI=") AS `string`;
```

Result

```json
[
  {
    "array": [
      1,
      2,
      3,
      4
    ],
    "boolean": false,
    "null": null,
    "number": 1234,
    "object": {
      "a": 1,
      "b": 2,
      "c": [
        1,
        2,
        3
      ]
    },
    "string": "Couchbase"
  }
]
```

## [](#current-users)CURRENT\_USERS()

### [](#description-4)Description

Returns the authenticated users for the current statement.

### [](#arguments-4)Arguments

None.

### [](#return-value-4)Return Value

An array of strings, each representing a user name.

### [](#example-3)Example

Query

```sqlpp
SELECT CURRENT_USERS() as current_users;
```

Results

```json
[
  {
    "current_users": [
      "local:97cdc7bd-f808-458e-9753-7f5119326198"
    ]
  }
]
```

## [](#ds-version)DS\_VERSION()

### [](#description-5)Description

Returns the Couchbase Server version.

### [](#arguments-5)Arguments

None.

### [](#return-value-5)Return Value

Returns string containing the Couchbase Server version.

### [](#example-4)Example

Query

```sqlpp
SELECT DS_VERSION() as server_version;
```

Results

```json
[
  {
    "server_version": "7.2.3-6705-enterprise"
  }
]
```

## [](#flatten%5Fkeys)FLATTEN\_KEYS(`expr1` \[ `modifiers` \], `expr2` \[ `modifiers` \], …​)

### [](#description-6)Description

This function can only be used when defining an index key for an [array index](indexing-arrays.md).

If you need to index multiple fields within an array, this function enables you to _flatten_ the specified expressions, and index them as if they were separate index keys. All subsequent index keys are accordingly moved to the right. Queries will be [sargable](selectintro.md#index-selection) and will generate spans.

### [](#arguments-6)Arguments

expr1, expr2, …​

\[At least 1 and at most 32 argument-values are required\] Each argument is an expression over a field within an array, which constitutes an array index key.

modifiers

\[Optional\] Arguments can be modified with `ASC` or `DESC` to specify the [sort order](createindex.md#index-order) of the index key. If this modifier is omitted, the default sort order is `ASC`.

The first argument may be also modified with `IGNORE MISSING`. This modifier may only be used when the function is being used in the definition of the leading index key. If this modifier is present, documents which do not contain the specified field are indexed anyway. If this modifier is omitted, documents which do not contain the specified field are not indexed.

When the `IGNORE MISSING` modifier and the `ASC` or `DESC` modifier are used together, the order of the modifiers does not matter.

Note that `FLATTEN_KEYS()` cannot be used recursively.

### [](#return-value-6)Return Value

The return value is a flattened list of array elements for use in an array index key.

### [](#examples-2)Examples

For examples, refer to [Array Indexing Examples](indexing-arrays.md#examples).

## [](#len)LEN(`expression`)

### [](#description-7)Description

A general function to return the length of an item.

### [](#arguments-7)Arguments

expression

An expression representing any supported SQL++ datatype.

### [](#return-value-7)Return Value

The return value is usually a number, depending on the datatype of the input expression.

| Input Expression | Return Value                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| String           | The number of code points in the string — equivalent to [LENGTH()](stringfun.md#fn-str-length). |
| Object           | The field count — equivalent to [OBJECT\_LENGTH()](objectfun.md#fn-obj-length).                 |
| Array            | The number of elements — equivalent to [ARRAY\_LENGTH()](arrayfun.md#fn-array-length).          |
| Binary           | The size of the binary object.                                                                  |
| Boolean          | 1                                                                                               |
| Number           | The number of characters in the number’s text representation.                                   |
| MISSING          | missing                                                                                         |
| NULL             | null                                                                                            |

For any item not listed above, the return value is `null`.

### [](#example-5)Example

Query

```sqlpp
SELECT LEN([1, 2, 3, 4]) AS `array`,
       LEN(false) AS `boolean`,
       LEN(missing) AS `missing`,
       LEN(null) AS `null`,
       LEN(1234) AS `number`,
       LEN( {"a": 1, "b": 2, "c": [1, 2, 3]} ) AS `object`,
       LEN("Couchbase") AS `string`;
```

Result

```json
[
  {
    "array": 4,
    "boolean": 1,
    "null": null,
    "number": 4,
    "object": 3,
    "string": 9
  }
]
```

## [](#meta)META( \[ `keyspace_expr` \] ) \[ .`property` \]

### [](#description-8)Description

This function returns the [metadata](../../learn/data/data.md#metadata) for the document or keyspace specified by `keyspace_expr`. The metadata is returned as a JSON object.

To return a single property from the metadata, you must use a [nested expression](nestedops.md#field-selection) containing the `META()` function and the required property, for example `META().id`. The supported metadata properties are described below.

You can use the `META()` function with a property to [index metadata information](indexing-meta-info.md). Only certain metadata properties are indexable; these are indicated in the description below.

You can also use the `META()` function with a property in the predicate of an [ANSI JOIN Clause](join.md#section%5Fek1%5Fjnx%5F1db).

### [](#arguments-8)Arguments

keyspace\_expr

\[Optional. Default is current keyspace.\]

String or an expression that results in a keyspace or a document. This argument is not required when creating an index, since the `META()` function implicitly uses the keyspace being indexed.

property

\[Optional\] The name of a single metadata property. The property name must be separated from the `META()` function by a dot (`.`) and may be one of the following:

cas

Value representing the current state of an item which changes every time the item is modified. For details, refer to [Concurrent Document Mutations](../../../../java-sdk/current/howtos/concurrent-document-mutations.md).

This property is indexable.

expiration

Value representing a document’s expiration date. A value of 0 (zero) means no expiration date. For details, refer to [KV Operations](../../../../java-sdk/current/howtos/kv-operations.md#document-expiration).

This property is indexable.

flags

Value set by the SDKs for non-JSON documents. For details, refer to [Non-JSON Documents](../../../../java-sdk/current/howtos/transcoders-nonjson.md).

This property is not indexable. If you attempt to build an index on this property, an error is returned.

id

Value representing a document’s unique ID number.

This property is indexable.

type

Value for the type of document; currently only `json` is supported.

This property is not indexable. If you attempt to build an index on this property, an error is returned.

### [](#return-value-8)Return Value

The bare function returns a JSON object containing the specified document’s metadata. When the function is used with a property as part of a nested expression, the expression returns the JSON value of the property.

### [](#examples-3)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Return all metadata

Query

```sqlpp
SELECT META() AS metadata
FROM airline
LIMIT 3;
```

Results

```json
[
  {
      "metadata": {
          "cas": 1583859008179798016,
          "expiration": 0,
          "flags": 33554432,
          "id": "airline_10",
          "type": "json"
      }
  },
  {
      "metadata": {
          "cas": 1583859008180846592,
          "expiration": 0,
          "flags": 33554432,
          "id": "airline_10123",
          "type": "json"
      }
  },
  {
      "metadata": {
          "cas": 1583859008181895168,
          "expiration": 0,
          "flags": 33554432,
          "id": "airline_10226",
          "type": "json"
      }
  }
]
```

Return a single metadata property

Query

```sqlpp
SELECT META().id AS id
FROM airline
LIMIT 3;
```

Results

```json
[
  {
    "id": "airline_10"
  },
  {
    "id": "airline_10123"
  },
  {
    "id": "airline_10226"
  }
]
```

Return a single metadata property for a specified keyspace

Query

```sqlpp
SELECT META(route).id AS id (1)
FROM route
JOIN airport
ON route.sourceairport = airport.faa
WHERE airport.city = "Paris"
LIMIT 3;
```

| **1** | You must specify a keyspace for the META() function because there is more than one FROM term. |
| ----- | --------------------------------------------------------------------------------------------- |

Results

```json
[
  {
    "id": "route_10136"
  },
  {
    "id": "route_10137"
  },
  {
    "id": "route_10138"
  }
]
```

For examples showing how to index metadata information, refer to [Indexing Meta Info](indexing-meta-info.md).

For examples showing how to use metadata information in the predicate of an ANSI JOIN clause, refer to [JOIN Clause](join.md).

## [](#node-name)NODE\_NAME()

### [](#description-9)Description

Returns the name of the node on which the query is running.

### [](#arguments-9)Arguments

None.

### [](#return-value-9)Return Value

A string representing a node name.

### [](#example-6)Example

Query

```sqlpp
SELECT NODE_NAME() AS node_name;
```

Results

```json
[
  {
    "node_name": "127.0.0.1:8091"
  }
]
```

## [](#pairs)PAIRS(`obj`)

### [](#description-10)Description

This function generates an array of arrays of \[`field_name`, `value`\] pairs of all possible fields in the given JSON object `obj`.

|  | Nested sub-object fields are explored recursively. |
|  | -------------------------------------------------- |

### [](#arguments-10)Arguments

obj

An expression resolving to an object.

### [](#return-value-10)Return Value

Array of \[`field_name`, `value`\] arrays for each field in the input object `obj`.

* If `obj` has nested objects, then fields of such nested sub-objects are also explored and corresponding inner-array elements are produced.
* If `obj` is an array, then each element of the array is explored and corresponding inner-array elements are produced.
* If `obj` is a primitive data type of integer or string, then it returns NULL, as they don’t have a name.
* If `obj` is an array of primitive data types, then it returns an empty array `[]`.
* If `obj` is an array of objects, then it returns an array of objects.

|  | If you wrap an array of primitive data types in an [object constructor](constructionops.md#object-construction), it’s treated as an object and returns an array; without the object constructor, it’s treated as an array of primitive data types and returns \[\]. For example, in [PAIRS() Example 2](#pairs-example2): PAIRS(public\_likes) returns \[\] PAIRS({public\_likes}) returns an array |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#examples-4)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Input value of a nested object

Query

```sqlpp
SELECT t        AS orig_t,
       PAIRS(t) AS pairs_t
FROM   airport t
LIMIT  1;
```

Result

```json
[
  {
    "orig_t": {
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
    },
    "pairs_t": [
      [
        "id",
        1254
      ],
      [
        "city",
        "Calais"
      ],
      [
        "faa",
        "CQF"
      ],
      [
        "geo",
        {
          "alt": 12,
          "lat": 50.962097,
          "lon": 1.954764
        }
      ],
      [
        "lon",
        1.954764
      ],
      [
        "alt",
        12
      ],
      [
        "lat",
        50.962097
      ],
      [
        "type",
        "airport"
      ],
      [
        "tz",
        "Europe/Paris"
      ],
      [
        "airportname",
        "Calais Dunkerque"
      ],
      [
        "country",
        "France"
      ],
      [
        "icao",
        "LFAC"
      ]
    ]
  }
]
```

Input value of an array

Query

```sqlpp
SELECT public_likes          AS orig_t,
       PAIRS(public_likes)   AS pairs_array_t,
       PAIRS({public_likes}) AS pairs_obj_t
FROM   hotel
LIMIT  1;
```

Result

```json
[
  {
    "orig_t": [
      "Julius Tromp I",
      "Corrine Hilll",
      "Jaeden McKenzie",
      "Vallie Ryan",
      "Brian Kilback",
      "Lilian McLaughlin",
      "Ms. Moses Feeney",
      "Elnora Trantow"
    ],
    "pairs_array_t": [],
    "pairs_obj_t": [
      [
        "public_likes",
        [
          "Julius Tromp I",
          "Corrine Hilll",
          "Jaeden McKenzie",
          "Vallie Ryan",
          "Brian Kilback",
          "Lilian McLaughlin",
          "Ms. Moses Feeney",
          "Elnora Trantow"
        ]
      ],
      [
        "public_likes",
        "Julius Tromp I"
      ],
      [
        "public_likes",
        "Corrine Hilll"
      ],
      [
        "public_likes",
        "Jaeden McKenzie"
      ],
      [
        "public_likes",
        "Vallie Ryan"
      ],
      [
        "public_likes",
        "Brian Kilback"
      ],
      [
        "public_likes",
        "Lilian McLaughlin"
      ],
      [
        "public_likes",
        "Ms. Moses Feeney"
      ],
      [
        "public_likes",
        "Elnora Trantow"
      ]
    ]
  }
]
```

Input value of a primitive (field document string) data type

Query

```sqlpp
SELECT country        AS orig_t,
       PAIRS(country) AS pairs_t
FROM   airport
LIMIT  1;
```

Result

```json
[
  {
    "orig_t": "France",
    "pairs_t": null
  }
]
```

Input value of a primitive (constant) data type

Query

```sqlpp
SELECT PAIRS("N1QL")             AS constant_string,
       PAIRS(4)                  AS constant_int,
       PAIRS([1,2,3])            AS constant_int_array,
       PAIRS({"name" : 3})       AS object_constant_int,
       PAIRS({"name" : [1,2,3]}) AS object_constant_int_array;
```

Result

```json
[
  {
    "constant_int": null,
    "constant_int_array": [],
    "constant_string": null,
    "object_constant_int": [
      [
        "name",
        3
      ]
    ],
    "object_constant_int_array": [
      [
        "name",
        [
          1,
          2,
          3
        ]
      ],
      [
        "name",
        1
      ],
      [
        "name",
        2
      ],
      [
        "name",
        3
      ]
    ]
  }
]
```

Input value of an array of objects

Query

```sqlpp
SELECT reviews[*].ratings,
       PAIRS({reviews[*].ratings}) AS pairs_t
FROM   hotel
LIMIT  1;
```

Result

```json
[
  {
    "pairs_t": [
      [
        "ratings",
        [
          {
            "Cleanliness": 5,
            "Location": 4,
            "Overall": 4,
            "Rooms": 3,
            "Service": 5,
            "Value": 4
          },
          {
            "Business service (e.g., internet access)": 4,
            "Check in / front desk": 4,
            "Cleanliness": 4,
            "Location": 4,
            "Overall": 4,
            "Rooms": 3,
            "Service": 3,
            "Value": 5
          }
        ]
      ],
      [
        "ratings",
        {
          "Cleanliness": 5,
          "Location": 4,
          "Overall": 4,
          "Rooms": 3,
          "Service": 5,
          "Value": 4
        }
      ],
      [
        "ratings",
        {
          "Business service (e.g., internet access)": 4,
          "Check in / front desk": 4,
          "Cleanliness": 4,
          "Location": 4,
          "Overall": 4,
          "Rooms": 3,
          "Service": 3,
          "Value": 5
        }
      ],
      [
        "Cleanliness",
        5
      ],
      [
        "Location",
        4
      ],
      [
        "Overall",
        4
      ],
      [
        "Rooms",
        3
      ],
      [
        "Service",
        5
      ],
      [
        "Value",
        4
      ],
      [
        "Cleanliness",
        4
      ],
      [
        "Location",
        4
      ],
      [
        "Rooms",
        3
      ],
      [
        "Value",
        5
      ],
      [
        "Business service (e.g., internet access)",
        4
      ],
      [
        "Check in / front desk",
        4
      ],
      [
        "Overall",
        4
      ],
      [
        "Service",
        3
      ]
    ],
    "ratings": [
      {
        "Cleanliness": 5,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 5,
        "Value": 4
      },
      {
        "Business service (e.g., internet access)": 4,
        "Check in / front desk": 4,
        "Cleanliness": 4,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 3,
        "Value": 5
      }
    ]
  }
]
```

## [](#unnest-pos)UNNEST\_POS(`expr`)

You can use the `UNNEST_POS()` function with the [UNNEST Clause](unnest.md) to return the position of each element in an unnested array.

This function has a synonym [UNNEST\_POSITION()](#unnest-position).

### [](#description-11)Description

The `UNNEST_POS` function takes an unnested array and returns the position value of each element in the array.

### [](#arguments-11)Arguments

expr

\[Required\] The alias of the unnested array from an [UNNEST Clause](unnest.md).

### [](#return-values)Return Values

The `UNNEST_POS` function returns the position of each element in the unnested array, `expr`, as an integer. It returns each position value as a separate row in JSON format. The first element in the array is at position `0`.

In all other cases, the `UNNEST_POS` function returns `NULL` or `MISSING`.

### [](#example-7)Example

In the following example, the `UNNEST_POS` function takes the result of an `UNNEST` Clause on a given array, `a1`. The `UNNEST` function returns the position of each element in the unnested `a1` array , `u`, as the `upos` value.

```N1QL
SELECT UNNEST_POS(u) AS upos, u FROM [{"a1":[10,9,4]}] AS d UNNEST d.a1 AS u;
```

Results

```json
[
    {
        "u": 10,
        "upos": 0
    },
    {
        "u": 9,
        "upos": 1
    },
    {
        "u": 4,
        "upos": 2
    }
]
```

### [](#related-clauses)Related Clauses

* [UNNEST Clause](unnest.md)
* [FROM Clause](from.md)

## [](#unnest-position)UNNEST\_POSITION(`expr`)

Synonym of [UNNEST\_POS()](#unnest-pos).

## [](#uuid)UUID()

### [](#description-12)Description

Generates a universally unique identifier (UUID) according to [RFC 4122](https://www.ietf.org/rfc/rfc4122.txt).

### [](#arguments-12)Arguments

None.

### [](#return-value-11)Return Value

A string representing a version 4 UUID.

### [](#example-8)Example

This query will return a different UUID each time you run it.

Query

```sqlpp
SELECT UUID() AS uuid;
```

Results

```json
[
  {
    "uuid": "2ca78bd8-0a28-4d68-995f-0da5e20e0964"
  }
]
```

For further examples using `UUID()`, refer to the [INSERT](insert.md) and [MERGE](merge.md) statements.

## [](#version)VERSION()

### [](#description-13)Description

Returns SQL++ version.

### [](#arguments-13)Arguments

None.

### [](#return-value-12)Return Value

Returns string containing the SQL++ version.

### [](#example-9)Example

Query

```sqlpp
SELECT VERSION() as language_version;
```

Results

```json
[
  {
    "language_version": "7.2.3-N1QL"
  }
]
```