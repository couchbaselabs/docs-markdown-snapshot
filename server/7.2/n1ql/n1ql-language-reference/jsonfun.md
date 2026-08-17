---
title: JSON Functions
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/jsonfun.adoc
  xref: xref:7.2@server:n1ql:n1ql-language-reference/jsonfun.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/jsonfun.html)

# JSON Functions

Functions for manipulating data in JSON.

## [](#decode%5Fjsonexpression)DECODE\_JSON(expression)

### [](#description)Description

Unmarshals the JSON-encoded string into a SQL++ value. The empty string is MISSING.

### [](#example)Example

Example 1\. Encode a returned result set as a JSON string.

Query

```sqlpp
select ENCODE_JSON(airline) as airline
from `travel-sample`.`inventory`.`airline` airline
where `id` = 10
```

Result

```json5
[
  {
    "airline": "{\"callsign\":\"MILE-AIR\",\"country\":\"United States\",\"iata\":\"Q5\",\"icao\":\"MLA\",\"id\":10,\"name\":\"40-Mile Air\",\"type\":\"airline\"}"
  }
]
```

## [](#encode%5Fjsonexpression)ENCODE\_JSON(expression)

### [](#description-2)Description

Marshals the SQL++ value into a JSON-encoded string. MISSING becomes the empty string.

### [](#example-2)Example

Example 2\. Unmarshal a JSON string into an SQL++ value.

Query

```sqlpp
select DECODE_JSON("{\"airline\":{\"callsign\": \"Mile-Air\", \"country\": \"United States\", \"iata\": \"Q5\", \"id\": 10, \"name\": \"40-mile Air\", \"type\": \"airline\"}}") as jsonObj
```

Result

```json5
[
  {
    "jsonObj": {
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

## [](#encoded%5Fsizeexpression)ENCODED\_SIZE(expression)

### [](#description-3)Description

Number of bytes in an uncompressed JSON encoding of the value. The exact size is implementation-dependent. Always returns an integer, and never MISSING or NULL. Returns 0 for MISSING.

### [](#example-3)Example

Example 3\. Return the size of the returned object.

Query

```sqlpp
select ENCODED_SIZE(airline) as airline_size
from `travel-sample`.`inventory`.`airline` airline
where `id` = 10
```

Result

```sqlpp
[
  {
    "airline_size": 120
  }
]
```

## [](#poly%5Flengthexpression)POLY\_LENGTH(expression)

### [](#description-4)Description

Returns length of the value after evaluating the expression. The exact meaning of length depends on the type of the value:

### [](#example-4)Example

Example 4\. Return the length of the retrieved object.

Query

```sqlpp
select POLY_LENGTH(airline) as airline_length
from `travel-sample`.`inventory`.`airline` airline
where `id` = 10
```

Result

```json5
[
  {
    "airline_length": 7
  }
]
```

* MISSING: MISSING
* NULL: NULL
* String: The length of the string.
* Array: The number of elements in the array.
* Object: The number of name/value pairs in the object
* Any other value: NULL