[View original HTML](/cloud/n1ql/n1ql-language-reference/typefun.html)

> Type functions perform operations that check or convert expressions. 

|  | If any arguments to any of the following functions are MISSING then the result is also MISSING (i.e. no result is returned). Similarly, if any of the arguments passed to the functions are NULL or are of the wrong type (e.g. an integer instead of a string), then NULL is returned as the result. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#fn-type-isarray)ISARRAY(expression)

### [](#description)Description

Checks if the supplied expression is an array.

### [](#arguments)Arguments

expression

\[Required\] The expression to check.

### [](#return-value)Return Value

Returns True if expression is an array, otherwise returns MISSING, NULL or false.

### [](#examples)Examples

```sqlpp
SELECT ISARRAY(true) AS `boolean`,
       ISARRAY(MISSING) AS `missing`,
       ISARRAY(NULL) AS `null`,
       ISARRAY(123) AS `number`,
       ISARRAY("hello world") AS `string`,
       ISARRAY([1, 2, 3]) AS `array`,
       ISARRAY({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": true,
    "boolean": false,
    "null": null,
    "number": false,
    "object": false,
    "string": false
  }
]
```

## [](#fn-type-isatom)ISATOM(expression)

### [](#description-2)Description

Checks if the supplied expression is a Boolean, number, or string.

### [](#arguments-2)Arguments

expression

\[Required\] The expression to check.

### [](#return-value-2)Return Value

Returns True if expression is a Boolean, number, or string, otherwise returns MISSING, NULL or false.

### [](#examples-2)Examples

```sqlpp
SELECT ISATOM(true) AS `boolean`,
       ISATOM(MISSING) AS `missing`,
       ISATOM(NULL) AS `null`,
       ISATOM(123) AS `number`,
       ISATOM("hello world") AS `string`,
       ISATOM([1, 2, 3]) AS `array`,
       ISATOM({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": false,
    "boolean": true,
    "null": null,
    "number": true,
    "object": false,
    "string": true
  }
]
```

## [](#fn-type-isboolean)ISBOOLEAN(expression)

### [](#description-3)Description

Checks if the supplied expression is a Boolean.

### [](#arguments-3)Arguments

expression

\[Required\] The expression to check.

### [](#return-value-3)Return Value

Returns True if expression is a Boolean, otherwise returns MISSING, NULL or false.

### [](#examples-3)Examples

```sqlpp
SELECT ISBOOLEAN(true) AS `boolean`,
       ISBOOLEAN(MISSING) AS `missing`,
       ISBOOLEAN(NULL) AS `null`,
       ISBOOLEAN(123) AS `number`,
       ISBOOLEAN("hello world") AS `string`,
       ISBOOLEAN([1, 2, 3]) AS `array`,
       ISBOOLEAN({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": false,
    "boolean": true,
    "null": null,
    "number": false,
    "object": false,
    "string": false
  }
]
```

## [](#fn-type-isnumber)ISNUMBER(expression)

### [](#description-4)Description

Checks if the supplied expression is a number.

### [](#arguments-4)Arguments

expression

\[Required\] The expression to check.

### [](#return-value-4)Return Value

Returns True if expression is a number, otherwise returns MISSING, NULL or false.

### [](#examples-4)Examples

```sqlpp
SELECT ISNUMBER(true) AS `boolean`,
       ISNUMBER(MISSING) AS `missing`,
       ISNUMBER(NULL) AS `null`,
       ISNUMBER(123) AS `number`,
       ISNUMBER("hello world") AS `string`,
       ISNUMBER([1, 2, 3]) AS `array`,
       ISNUMBER({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": false,
    "boolean": false,
    "null": null,
    "number": true,
    "object": false,
    "string": false
  }
]
```

## [](#fn-type-isobject)ISOBJECT(expression)

### [](#description-5)Description

Checks if the supplied expression is an object.

### [](#arguments-5)Arguments

expression

\[Required\] The expression to check.

### [](#return-value-5)Return Value

Returns True if expression is an object, otherwise returns MISSING, NULL or false.

### [](#examples-5)Examples

```sqlpp
SELECT ISOBJECT(true) AS `boolean`,
       ISOBJECT(MISSING) AS `missing`,
       ISOBJECT(NULL) AS `null`,
       ISOBJECT(123) AS `number`,
       ISOBJECT("hello world") AS `string`,
       ISOBJECT([1, 2, 3]) AS `array`,
       ISOBJECT({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": false,
    "boolean": false,
    "null": null,
    "number": false,
    "object": true,
    "string": false
  }
]
```

## [](#fn-type-isstring)ISSTRING(expression)

### [](#description-6)Description

Checks if the supplied expression is a string.

### [](#arguments-6)Arguments

expression

\[Required\] The expression to check.

### [](#return-value-6)Return Value

Returns True if expression is a string, otherwise returns MISSING, NULL or false.

### [](#examples-6)Examples

```sqlpp
SELECT ISSTRING(true) AS `boolean`,
       ISSTRING(MISSING) AS `missing`,
       ISSTRING(NULL) AS `null`,
       ISSTRING(123) AS `number`,
       ISSTRING("hello world") AS `string`,
       ISSTRING([1, 2, 3]) AS `array`,
       ISSTRING({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": false,
    "boolean": false,
    "null": null,
    "number": false,
    "object": false,
    "string": true
  }
]
```

## [](#isvector)ISVECTOR(`vector`, `dimension`, `format`)

### [](#description-7)Description

Checks if the supplied expression is an array of floating point numbers with the specified number of dimensions. This can be used to determine whether a field contains a vector value.

### [](#arguments-7)Arguments

vector

An array of floating point numbers, or any SQL++ expression that evaluates to an array of floating point numbers.

dimension

An integer representing the number of dimensions.

format

A string. This argument must always be present and must have the value `"float32"`.

### [](#return-value-7)Return Value

Returns `true` if the expression is an array of floating point numbers with the specified number of dimensions.

### [](#examples-7)Examples

To try the examples in this section, you must install the `rgb` and `rgb-questions` collections from the supplied vector sample, as described in [Prerequisites](../../vector-index/hyperscale-vector-index.md#prerequisites).

ISVECTOR() Example 1

Query

```sqlpp
SELECT ISVECTOR([1, 2, 3, 4], 4, "float32") as vector,
       ISVECTOR([1, 2, 3, 4], 3, "float32") as wrong_dimension,
       ISVECTOR(["a", "b", "c", "d"], 4, "float32") as wrong_values;
```

Results

```json
[
  {
    "vector": true,
    "wrong_dimension": false,
    "wrong_values": false
  }
]
```

ISVECTOR() Example 2

Check whether the specified fields in the `rgb` collection contain vector values.

Query

```sqlpp
SELECT ISVECTOR(description, 1, "float32") AS description,
       ISVECTOR(colorvect_l2, 3, "float32") AS colorvect_l2,
       ISVECTOR(embedding_vector_dot, 1536, "float32") AS embedding_vector_dot
FROM `color-vector-sample`.color.rgb LIMIT 1;
```

Results

```json
[{
    "description": false,
    "colorvect_l2": true,
    "embedding_vector_dot": true
}]
```

The results show that the `description` field is not a vector field. The `colorvect_l2` and `embedding_vector_dot` fields are vector fields, with the specified number of dimensions.

## [](#fn-type-type)TYPE(expression)

### [](#description-8)Description

Checks the type of the supplied expression.

### [](#arguments-8)Arguments

expression

\[Required\] The expression to check.

### [](#return-value-8)Return Value

Returns one of the following strings, based on the value of expression:

* "missing"
* "null"
* "boolean"
* "number"
* "string"
* "array"
* "object"
* "binary"

### [](#examples-8)Examples

```sqlpp
SELECT TYPE(true) AS `boolean`,
       TYPE(MISSING) AS `missing`,
       TYPE(NULL) AS `null`,
       TYPE(123) AS `number`,
       TYPE("hello world") AS `string`,
       TYPE([1, 2, 3]) AS `array`,
       TYPE({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": "array",
    "boolean": "boolean",
    "missing": "missing",
    "null": "null",
    "number": "number",
    "object": "object",
    "string": "string"
  }
]
```

## [](#fn-type-toarray)TOARRAY(expression)

### [](#description-9)Description

Converts the supplied expression to an array.

### [](#arguments-9)Arguments

expression

\[Required\] The expression to convert.

### [](#return-value-9)Return Value

Returns one of the following strings, based on the value of expression:

Returns array as follows:

* MISSING is MISSING.
* NULL is NULL.
* Arrays are themselves.
* All other values are wrapped in an array.

### [](#examples-9)Examples

```sqlpp
SELECT TOARRAY(true) AS `boolean`,
       TOARRAY(MISSING) AS `missing`,
       TOARRAY(NULL) AS `null`,
       TOARRAY(123) AS `number`,
       TOARRAY("hello world") AS `string`,
       TOARRAY([1, 2, 3]) AS `array`,
       TOARRAY({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": [
      1,
      2,
      3
    ],
    "boolean": [
      true
    ],
    "null": null,
    "number": [
      123
    ],
    "object": [
      {
        "hello": "world"
      }
    ],
    "string": [
      "hello world"
    ]
  }
]
```

## [](#fn-type-toatom)TOATOM(expression)

### [](#description-10)Description

Converts the supplied expression to Boolean, number, or string.

### [](#arguments-10)Arguments

expression

\[Required\] The expression to convert.

### [](#return-value-10)Return Value

Returns atomic value as follows:

* MISSING is MISSING.
* NULL is NULL.
* Arrays of length 1 are the result of TOATOM() on their single element.
* Objects of length 1 are the result of TOATOM() on their single value.
* Booleans, numbers, and strings are themselves.
* All other values are NULL.

### [](#examples-10)Examples

```sqlpp
SELECT TOATOM(true) AS `boolean`,
       TOATOM(MISSING) AS `missing`,
       TOATOM(NULL) AS `null`,
       TOATOM(123) AS `number`,
       TOATOM("hello world") AS `string`,
       TOATOM([1, 2, 3]) AS `array`,
       TOATOM({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": null,
    "boolean": true,
    "null": null,
    "number": 123,
    "object": "world",
    "string": "hello world"
  }
]
```

## [](#fn-type-toboolean)TOBOOLEAN(expression)

### [](#description-11)Description

Converts the supplied expression to a Boolean.

### [](#arguments-11)Arguments

expression

\[Required\] The expression to convert.

### [](#return-value-11)Return Value

Returns Boolean as follows:

* MISSING is MISSING.
* NULL is NULL.
* False is false.
* Numbers +0, -0, and NaN are false.
* Empty strings, arrays, and objects are false.
* All other values are true.

### [](#examples-11)Examples

```sqlpp
SELECT TOBOOLEAN(true) AS `boolean`,
       TOBOOLEAN(MISSING) AS `missing`,
       TOBOOLEAN(NULL) AS `null`,
       TOBOOLEAN(123) AS `number`,
       TOBOOLEAN("hello world") AS `string`,
       TOBOOLEAN([1, 2, 3]) AS `array`,
       TOBOOLEAN({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": true,
    "boolean": true,
    "null": null,
    "number": true,
    "object": true,
    "string": true
  }
]
```

## [](#fn-type-tonumber)TONUMBER(expression \[, string-expression\])

### [](#description-12)Description

Converts the supplied expression to a number.

### [](#arguments-12)Arguments

expression

\[Required\] The expression to convert.

string-expression

\[Optional\] Characters to strip from the input expression before conversion, if the input expression is a string.

### [](#return-value-12)Return Value

Returns number as follows:

* MISSING is MISSING.
* NULL is NULL.
* False is 0.
* True is 1.
* Numbers are themselves.
* Strings that parse as numbers are those numbers.
* All other values are NULL.

If `string-expression` is supplied, and the input expression is a string, then the following operations are carried out before conversion:

* All whitespace is stripped from the input expression string.
* All characters listed in `string-expression` are stripped from the input expression string.
* If a decimal comma is detected, it is replaced with a decimal point — all other points must be removed from the input expression string.

If `string-expression` is not supplied, then the input expression string is parsed as-is.

### [](#examples-12)Examples

```sqlpp
SELECT TONUMBER(true) AS `boolean`,
       TONUMBER(MISSING) AS `missing`,
       TONUMBER(NULL) AS `null`,
       TONUMBER(123) AS `number`,
       TONUMBER("hello world") AS `string`,
       TONUMBER([1, 2, 3]) AS `array`,
       TONUMBER({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": null,
    "boolean": 1,
    "null": null,
    "number": 123,
    "object": null,
    "string": null
  }
]
```

```sqlpp
SELECT TONUMBER("AU$123456.78", "AU$") AS `aud`,
       TONUMBER("€123.456,78   ", "€.") AS `eur`,
       TONUMBER("$   123,456.78", "$,") AS `usd`,
       TONUMBER("¥123 456 789.00", "¥") AS `yen`;
```

```json
[
  {
    "aud": 123456.78,
    "eur": 123456.78,
    "usd": 123456.78,
    "yen": 123456789
  }
]
```

## [](#fn-type-toobject)TOOBJECT(expression)

### [](#description-13)Description

Converts the supplied expression to an object.

### [](#arguments-13)Arguments

expression

\[Required\] The expression to convert.

### [](#return-value-13)Return Value

Returns object as follows:

* MISSING is MISSING.
* NULL is NULL.
* Objects are themselves.
* All other values are the empty object.

### [](#examples-13)Examples

```sqlpp
SELECT TOOBJECT(true) AS `boolean`,
       TOOBJECT(MISSING) AS `missing`,
       TOOBJECT(NULL) AS `null`,
       TOOBJECT(123) AS `number`,
       TOOBJECT("hello world") AS `string`,
       TOOBJECT([1, 2, 3]) AS `array`,
       TOOBJECT({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": {},
    "boolean": {},
    "null": null,
    "number": {},
    "object": {
      "hello": "world"
    },
    "string": {}
  }
]
```

## [](#fn-type-tostring)TOSTRING(expression)

### [](#description-14)Description

Converts the supplied expression to a string.

### [](#arguments-14)Arguments

expression

\[Required\] The expression to convert.

### [](#return-value-14)Return Value

Returns string as follows:

* MISSING is MISSING.
* NULL is NULL.
* False is "false".
* True is "true".
* Numbers are their string representation.
* Strings are themselves.
* All other values are NULL.

### [](#examples-14)Examples

```sqlpp
SELECT TOSTRING(true) AS `boolean`,
       TOSTRING(MISSING) AS `missing`,
       TOSTRING(NULL) AS `null`,
       TOSTRING(123) AS `number`,
       TOSTRING("hello world") AS `string`,
       TOSTRING([1, 2, 3]) AS `array`,
       TOSTRING({"hello": "world"}) AS `object`;
```

```json
[
  {
    "array": null,
    "boolean": "true",
    "null": null,
    "number": "123",
    "object": null,
    "string": "hello world"
  }
]
```