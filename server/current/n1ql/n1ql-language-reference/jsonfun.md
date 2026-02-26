---
title: JSON Functions
description: Functions for encoding, decoding, and evaluating JSON values.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/jsonfun.adoc
pubDate: 2026-02-26T12:08:50.459Z
link: xref:server:n1ql:n1ql-language-reference/jsonfun.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-language-reference/jsonfun.html)

# JSON Functions

> Functions for encoding, decoding, and evaluating JSON values. 

## [](#decode%5Fjsonexpression)DECODE\_JSON(`expression`)

Converts a JSON-encoded string into a SQL++ value.

### [](#arguments)Arguments

expression

\[Required\] An expression that represents a JSON-encoded string.

### [](#return-value)Return Value

The function returns 1 of the following:

* A SQL++ value.
* `NULL` if the input is NULL or not a valid JSON value.
* `MISSING` if the input is empty.

### [](#example)Example

Example 1\. Decode a JSON string into a SQL++ value

Query

```sqlpp
SELECT DECODE_JSON(
    "{\"airline\":
        { \"callsign\": \"Mile-Air\",
          \"country\": \"United States\",
          \"iata\": \"Q5\",
          \"id\": 10,
          \"name\": \"40-mile Air\",
          \"type\": \"airline\"
        }
    }"
) as decoded_value;
```

Result

```json
[
  {
    "decoded_value": {
      "airline": {
        "callsign": "Mile-Air",
        "country": "United States",
        "iata": "Q5",
        "id": 10,
        "name": "40-mile Air",
        "type": "airline"
      }
    }
  }
]
```

## [](#encode%5Fjsonexpression)ENCODE\_JSON(`expression`)

Converts a SQL++ value into a JSON-encoded string.

### [](#arguments-2)Arguments

expression

\[Required\] A SQL++ expression to be encoded.

### [](#return-value-2)Return Value

The function returns 1 of the following:

* A JSON encoded string.
* `NULL` if the input is `NULL`.
* `MISSING` if the input is `MISSING`.

### [](#example-2)Example

Example 2\. Encode a SQL++ value into a JSON string

Query

```sqlpp
SELECT ENCODE_JSON(
    {
        "airline": {
            "callsign": "Mile-Air",
            "country": "United States",
            "iata": "Q5",
            "id": 10,
            "name": "40-mile Air",
            "type": "airline"
        }
    }
) as encoded_value;
```

Result

```json
[
  {
    "encoded_value":
        "{ \"airline\":
             { \"callsign\":\"Mile-Air\",
               \"country\":\"United States\",
               \"iata\":\"Q5\",
               \"id\":10,
               \"name\":\"40-mile Air\",
               \"type\":\"airline\"
            }
        }"
  }
]
```

## [](#encoded%5Fsizeexpression)ENCODED\_SIZE(`expression`)

Returns the number of bytes in an uncompressed JSON encoding of a value. The exact size depends on the implementation and may vary.

### [](#arguments-3)Arguments

expression

\[Required\] An expression to evaluate.

### [](#return-value-3)Return Value

An integer representing the size in bytes.

The function never returns `NULL` or `MISSING`. If the input value is `MISSING`, the function returns `0`.

### [](#example-3)Example

Example 3\. Calculate the size of a JSON-encoded value

Query

```sqlpp
SELECT ENCODED_SIZE(
    {
        "airline": {
            "callsign": "Mile-Air",
            "country": "United States",
            "iata": "Q5",
            "id": 10,
            "name": "40-mile Air",
            "type": "airline"
        }
    }
) as encoded_size;
```

Result

```json
[
  {
    "encoded_size": 119
  }
]
```

## [](#poly%5Flengthexpression)POLY\_LENGTH(`expression`)

Evaluates an expression and returns the length of the resulting value. The definition of length depends on the type of the evaluated value. For more information, see the [Return Value](#poly-length-return-value) section.

### [](#arguments-4)Arguments

expression

\[Required\] An expression to evaluate.

### [](#poly-length-return-value)Return Value

The function returns a value based on the data type of the result:

* String: Returns the number of characters in the string.
* Array: Returns the number of elements in the array.
* Object: Returns the number of name/value pairs in the object.
* MISSING: Returns `MISSING`.
* NULL: Returns `NULL`.
* Any other value: Returns `NULL`.

### [](#example-4)Example

Example 4\. Find the length of a string, array, and object

Query

```sqlpp
SELECT
    POLY_LENGTH("Flight 101") as string_length,
    POLY_LENGTH(["Flight 101", "Flight 202", "Flight 303"]) as array_length,
    POLY_LENGTH({
        "flight": 101,
        "airline": "Mile-Air",
        "destination": "United States"
    }) as object_length;
```

Result

```json
[
  {
    "string_length": 10,
    "array_length": 3,
    "object_length": 3
  }
]
```