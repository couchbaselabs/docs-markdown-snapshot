---
title: XDCR Filtering Expressions
description: XDCR filtering expressions allow a document to be included in or
  excluded from a filtered replication, based on the document's fields and
  values.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/xdcr-reference/pages/xdcr-filtering-expressions.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/xdcr-reference/xdcr-filtering-expressions.html)

# XDCR Filtering Expressions

> XDCR filtering expressions allow a document to be included in or excluded from a filtered replication, based on the document’s fields and values. 

## [](#understanding-filtering-expressions)Understanding Filtering Expressions

XDCR Advanced Filtering _expressions_, applied to the documents within a specified source bucket, allow case-sensitive matches to be made on:

* _id_ and _xattrs_ values, within the document’s _metadata_.
* Field-names and values, within the document’s _data_, nested to any degree.

Every document on which a match is successfully made is included in the filtered replication. Other documents are _not_ included.

XDCR filtering expressions constitute a subset of _SQL++_ expressions, with some additions.

Sections on this page list the available expressions, provide examples of their usage, and provide links to documentation for the comparable SQL++ expressions. A list of _reserved words_ is provided. Additionally, relationships between expressions are listed in in BNF (_Backus-Naur Form_) notation.

Note that most examples assume the `travel-sample` bucket to be the source of the filtered replication. For information on installing this bucket, see [Install Sample Buckets](../manage/manage-settings/install-sample-buckets.md).

XDCR Advanced Filtering can be managed by means of Couchbase Web Console (see [Filter a Replication](../manage/manage-xdcr/filter-xdcr-replication.md)), the CLI (see [xdcr-replicate](../cli/cbcli/couchbase-cli-xdcr-replicate.md)), and the REST API (see [Creating XDCR Replications](../rest-api/rest-xdcr-create-replication.md)).

## [](#pattern-matching)Pattern Matching

Pattern matching is supported with the following syntax:

REGEXP_CONTAINS (_expression_, _pattern_)

For example, the following expression specifies `country` as the _expression_, and `"France"` as the pattern:

```sqlpp
REGEXP_CONTAINS(country, "France")
```

If `travel-sample.inventory.airline` is used as the source collection, every document that contains a field `country` whose value is `"France"` is replicated to the target. For example, this would include the document `airline_1191`:

```json
{
  "callsign": "REUNION",
  "country": "France",
  "iata": "UU",
  "icao": "REU",
  "id": 1191,
  "name": "Air Austral",
  "type": "airline"
}
```

### [](#mata-data-access)Metadata Access

Each document contains _metadata_, as well as _data_. Within the metadata, a document’s _id_ and _extended attributes_ can be accessed by means of the reserved word `META`, used as part of the the pattern-matching _expression_.

For example, the following expression seeks a match on any document the value of whose metadata _id_ field contains the substring `"airline_10"`:

```sqlpp
REGEXP_CONTAINS(META().id, "airline_10")
```

This would match a number of documents from the `travel-sample.inventory.airline` collection, including `airline_10`, whose metadata is as follows:

```json
{
  "meta": {
    "id": "airline_10",
    "rev": "1-159642cc11a000000000000002000000",
    "expiration": 0,
    "flags": 33554432,
    "type": "json"
  },
  "xattrs": {}
}
```

_Extended Attributes_ are optionally used to define application-specific metadata. Their field name is `xattrs`. In the metadata example shown above, no value exists for the field. If an extended attribute were fully defined — for example, a `color` field, assigned the value `blue` — the appearance within the metadata would be as follows:

```json
  "xattrs": {
    "color": "blue"
  }
```

The extended attribute’s value could then be filtered and matched with the following expression:

```sqlpp
REGEXP_CONTAINS(META().xattrs.color, "blue")
```

For information on extended attributes, see [Extended Attributes](../learn/data/extended-attributes-fundamentals.md).

### [](#lookahead)Lookahead

XDCR Advanced Filtering is supported by _lookahead_. Lookahead is used to specify a _pattern_, in pattern matching; and permits a match when one specified character or character-sequence:

* Is followed by another specified character or character-sequence. This is termed _positive_ lookahead.  
The following syntax is used:  
_char1_ ( ?= _char2_ )  
The specified _char1_ must therefore be located and, for a successful match to be obtained, must be followed by the specified _char2_.
* Is _not_ followed by another specified character or character-sequence. This is termed _negative_ lookahead.  
The following syntax is used:  
_char1_ ( ?! _char2_ )  
The specified _char1_ must therefore be located, and, for a successful match to be obtained, must _not_ be followed by the specified _char2_.

Lookahead might therefore be used on the `travel-sample.default.default` collection, to filter documents whose metadata _id_ contains `airport` rather than `airline`, or vice versa. For example, the following expression uses _positive_ lookahead to specify that the metadata _id_ that begins with `air` should be immediately followed by the character `p`; thereby returning documents whose metadata _id_ value is `airport`, but not `airline`:

```sqlpp
REGEXP_CONTAINS(META().id, "^air(?=p)")
```

For information on the expression `^`, see [XDCR Regular Expressions](xdcr-regular-expressions.md).

Alternatively, _negative_ lookahead might be used to specify that the metadata _id_ that begins with `air` should _not_ be followed by the character `l`; thereby returning documents whose metadata _id_ value is `airport`, but not `airline`:

```sqlpp
REGEXP_CONTAINS(META().id, "^air(?!l)")
```

### [](#xdcr-pattern-matching-comparison-with-sql)XDCR Pattern Matching: Comparison with SQL++

The function `REGEXP_CONTAINS` is also supported by SQL++. Note, however, that SQL++ does not support forward lookahead.

SQL++ supports a number of pattern-matching functions in addition to `REGEXP_CONTAINS`: see [Pattern-matching Functions](../n1ql/n1ql-language-reference/patternmatchingfun.md).

`META` is one of a group of _reserved words_ used by XDCR Advanced Filtering. For details, [Reserved Words](#reserved-words), below. `META` is also one of a larger group of reserved words used by SQL++. For details, see the page for SQL++ [Reserved Words](../n1ql/n1ql-language-reference/reservedwords.md). Note that in SQL++, `META` provides access to a wider range of extended attributes.

## [](#checking-for-existence)Checking for Existence

The existence of a field can be checked for, by means of the Collection Operator `EXISTS`. The syntax is as follows:

EXISTS ( _expression_ )

For example:

```sqlpp
EXISTS(country)
```

This returns every document that contains a `country` field. This would therefore include `airline_10`:

```json
{
  "callsign": "MILE-AIR",
  "country": "United States",
  "iata": "Q5",
  "icao": "MLA",
  "id": 10,
  "name": "40-Mile Air",
  "type": "airline"
}
```

### [](#xdcr-collection-operator-comparison-with-sql)XDCR Collection Operator: Comparison with SQL++

XDCR Advanced Filtering provides the single Collection Operator, `EXISTS`; which determines whether or not a specified field exists in the body of a document. SQL++ uses `EXISTS` on subclauses; and provides a variety of additional Collection Operators. For details, see the SQL++ page for [Collection Operators](../n1ql/n1ql-language-reference/collectionops.md).

## [](#using-logical-operators)Using Logical Operators

XDCR Advanced Filtering provides the Logical Operators `AND`, `OR`, and `NOT`. See the [Filtering Expression BNF](#filtering-expression-bnf), below, for the syntactic possibilities of these operators.

`AND` can be used to add a required condition to an expression. For example:

```sqlpp
REGEXP_CONTAINS(country, "France") AND airportname = "La Teste De Buch"
```

This provides a successful match on any document whose `country` value is `"France"`, and whose `aiportname` value is `"La Test De Buch"`. This would therefore include the following document in the replication:

```json
{
  "airportname": "La Teste De Buch",
  "city": "Arcachon",
  "country": "France",
  "faa": "XAC",
  "geo": {
    "alt": 49,
    "lat": 44.59639,
    "lon": -1.110833
  },
  "icao": "LFCH",
  "id": 1283,
  "type": "airport",
  "tz": "Europe/Paris"
}
```

`OR` can be used to add an alternative condition to an expression. For example:

```sqlpp
REGEXP_CONTAINS(country, "France") OR country = "United States"
```

This provides a successful match on any document whose `country` value is either `"France"` or `"United States"`.

`NOT` can be prepended to a condition, to allow a successful match only when the condition is false. For example:

```sqlpp
REGEXP_CONTAINS(country, "France") AND NOT airportname = "La Teste De Buch"
```

This provides a successful match on every document that contains the `country` value `"France"`, and contains an `airportname` value that is _not_ `"La Teste De Buch"`.

All words used as Logical Operators for XDCR Advanced Filtering are _reserved_. For details, see [Reserved Words](#reserved-words), below.

### [](#xdcr-logical-operators-comparison-with-sql)XDCR Logical Operators: Comparison with SQL++

SQL++ provides the same Logical Operators as does XDCR Advanced Filtering. For details, see the SQL++ page for [Logical Operators](../n1ql/n1ql-language-reference/logicalops.md).

## [](#using-comparison-operators)Using Comparison Operators

XDCR Advanced Filtering provides the following Comparison Operators:

| \= _and_ \== | != _and_ <>    |
| ------------ | -------------- |
| \>           | \>=            |
| <            | <=             |
| IS NULL      | IS NOT NULL    |
| IS MISSING   | IS NOT MISSING |

As this indicates, the tests for equality and inequality are each provided in two versions, to ensure compatibility with different languages.

Note that for purposes of comparison, each field within a document is categorized as one of the following:

* Has a non-_null_ value
* Is specified as _null_
* Is missing a non-_null_ value, and is not specified as _null_

Therefore:

* `IS NULL` is successfully matched with _null_.
* `IS NOT NULL` is successfully matched when the field either has a value, or is missing a value.
* `IS MISSING` is successfully matched when neither _null_ nor a value is present.
* `IS NOT MISSING` is successfully matched when either _null_ or a value is present.

For example:

```sqlpp
REGEXP_CONTAINS(country, "France") AND name != "40-Mile Air"
```

This provides a successful match with every document whose `country` value is `"France"`, and whose `name` value is not `"40-Mile Air"`. This would include `airline_1191`:

```json
{
  "callsign": "REUNION",
  "country": "France",
  "iata": "UU",
  "icao": "REU",
  "id": 1191,
  "name": "Air Austral",
  "type": "airline"
}
```

The following, additional example tests for a _null_ `icao` field, on documents whose `country` value is `United States`:

```sqlpp
REGEXP_CONTAINS(country, "United States") AND icao IS NULL
```

This returns a number of matches, one of which is `airport_4079`:

```json
{
  "airportname": "Orlando",
  "city": "Orlando",
  "country": "United States",
  "faa": "DWS",
  "geo": {
    "alt": 340,
    "lat": 28.398,
    "lon": -81.57
  },
  "icao": null,
  "id": 4079,
  "type": "airport",
  "tz": "America/New_York"
}
```

All words used in Comparison Operators for XDCR Advanced Filtering are _reserved_. For details, see [Reserved Words](#reserved-words), below.

### [](#xdcr-comparison-operators-comparison-with-sql)XDCR Comparison Operators: Comparison with SQL++

The Comparison Operators provided by XDCR Advanced Filtering are a subset of those provided by SQL++. For details, see the SQL++ page for [Comparison Operators](../n1ql/n1ql-language-reference/comparisonops.md).

## [](#selecting-fields-and-elements)Selecting Fields and Elements

XDCR Advanced Filtering provides operators for Field Selection and Element Selection.

### [](#field-selection)Field Selection

The Field Selection Operator is the period: `.`This allows a child-field, within a parent-field, to be specified. Note that the Field Selection Operator was used to specify the metadata `id` field, in [Metadata Access](#mata-data-access), above.

The following example uses the Field Selection Operator to obtain a match on any document that contains a `country` field with a value of `"United States"`, and also has an `alt` field, within the value of its `geo` field, with a value that is greater than or equal to `6813`.

```sqlpp
REGEXP_CONTAINS(country, "United States") AND geo.alt >= 6813
```

This returns a number of matches, including `airport_4084`:

```json
{
  "airportname": "Telluride",
  "city": "Telluride",
  "country": "United States",
  "faa": "TEX",
  "geo": {
    "alt": 9078,
    "lat": 37.953759,
    "lon": -107.90848
  },
  "icao": "KTEX",
  "id": 4084,
  "type": "airport",
  "tz": "America/Denver"
}
```

When non-standard alphanumeric characters have been used in field-naming (for example, space or bracket characters), the field, when referenced in an advanced filtering expression, should be escaped with backticks: eg, `` field.`the field name` ``.

### [](#element-selection)Element Selection

The Element Selection Operator, which is provided for use on arrays, takes the form `[` _n_ `]`, where _n_ is an array-position.

For example, the following provides a successful match when a document whose `airline` value is `"AA"` also contains a `schedule` array, whose initial member has a field `flight` with a value of `"AA679"`:

```sqlpp
REGEXP_CONTAINS(airline, "AA") AND schedule[0].flight = "AA679"
```

This produces a match on document `route_5784`:

```json
{
  "airline": "AA",
  "airlineid": "airline_24",
  "destinationairport": "PHL",
  "distance": 153.59665185566308,
  "equipment": "E90 DH3 319",
  "id": 5784,
  "schedule": [{
    "day": 0,
    "flight": "AA679",
    "utc": "22:01:00"
  }, {
    "day": 0,
    "flight": "AA253",
    "utc": "22:29:00"
  }, {
    "day": 1,
      .
      .
      .
  }, {
    "day": 6,
    "flight": "AA661",
    "utc": "16:35:00"
  }],
  "sourceairport": "LGA",
  "stops": 0,
  "type": "route"
}
```

### [](#xdcr-selection-operators-comparison-with-sql)XDCR Selection Operators: Comparison with SQL++

The Field Selection Operator is used in SQL++ with additional functionality: _nested expressions_ support is provided. The Element Selection Operator is also used in SQL++ with additional functionality: negative indexing of arrays and the `*` operator are supported. SQL++ also provides _array slicing_ that allows the building of sub-slices of arrays. For information, see the SQL++ page for [Nested Operators and Expressions](../n1ql/n1ql-language-reference/nestedops.md).

## [](#using-arithmetic-operators)Using Arithmetic Operators

XDCR Advanced Filtering is supported by the following arithmetic operators:

| Operator | Description                                                                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| +        | Add values.                                                                                                                                                  |
| \-       | Subtract right value from left value.                                                                                                                        |
| \*       | Multiply values.                                                                                                                                             |
| /        | Divide left value by right value.                                                                                                                            |
| %        | Modulo. Divide left value by right value and return the remainder. Note that modulo is an integer operator and will use only the integer part of each value. |
| \-value  | Negate value.                                                                                                                                                |

For additional details on syntax and return values, see the SQL++ page for [Arithmetic Operators](../n1ql/n1ql-language-reference/arithmetic.md).

For example, the following filtering expression provides a successful match on documents whose `country` value is `United States` and whose `id` is an integer value that returns a value of less than or equal to `3`, when modulo `7` is applied:

```sqlpp
REGEXP_CONTAINS(country, "United States") AND id % 7 <=  3
```

### [](#xdcr-arithmetic-operators-comparison-with-sql)XDCR Arithmetic Operators: Comparison with SQL++

SQL++ provides the same arithmetic operators, with the same semantics and return values. See the SQL++ page for [Arithmetic Operators](../n1ql/n1ql-language-reference/arithmetic.md).

## [](#number-functions)Number Functions

XDCR Advanced Filtering is supported by Number Functions. These functions are the same as those provided by SQL++. However, the following SQL++ Number Functions do _not_ apply to XDCR Advanced Filtering:

* RANDOM
* SIGN
* TRUNC

For information on all other functions, see the SQL++ page for [Number Functions](../n1ql/n1ql-language-reference/numericfun.md).

## [](#handling-dates)Handling Dates

XDCR Advanced Filtering provides a basic DATE function that allows user to compose filtering expressions based on dates.

Dates can be specified in [RFC3339](https://tools.ietf.org/html/rfc3339) format. Dates can also be specified in the following ISO-8601 formats:

| ISO-8601 Format      | Example              |
| -------------------- | -------------------- |
| Date                 | 2019-01-25           |
| Date and time in UTC | 2019-01-25T18:40:37Z |

For example:

```sqlpp
REGEXP_CONTAINS(event_type, "birthday") AND DATE(date) >= DATE("2019-01-25")
```

This seeks a match on any document whose `date` value is equal to or later than `"2019-01-25"`. If created, the following hypothetical document provides a successful match:

```json
{
  "event_type": "birthday",
  "venue": "white hart hotel, salisbury, uk",
  "session": "afternoon",
  "dining_preference": "buffet",
  "number_of_guests": 25,
  "date": "2019-01-25"
}
```

Note that _times_ are supported by utilizing the following RFC-3339 format:

```sqlpp
DATE(transaction.time) < DATE(2018-01-01T12:00Z)
```

### [](#xdcr-date-operators-comparison-with-sql)XDCR Date Operators: Comparison with SQL++

SQL++ date functions are _not_ supported by XDCR Advanced Filtering. For information on SQL++ date functions, see the SQL++ page for [Date Functions](../n1ql/n1ql-language-reference/datefun.md).

## [](#reserved-words)Reserved Words

_Reserved Words_ are words used syntactically by XDCR Advanced Filtering. If these words have used as _identifiers_ in JSON documents, in order to be referenced in filtering expressions, they must be _escaped_, by means of backticks. The complete list of words is as follows:

| AND  | EXISTS | FALSE   | IF  |
| ---- | ------ | ------- | --- |
| IS   | META   | MISSING | NOT |
| NULL | OR     | TRUE    |     |

## [](#filtering-expression-bnf)Filtering Expression BNF

The relationships between available expressions for XDCR Advanced Filtering are expressed in the following table, in _Backus-Naur Form_.

| Expression             | Is Equal To                                                                                                                     |                      |       |      |      |     |     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----- | ---- | ---- | --- | --- |
| FilterExpression       | ( "(" FilterExpression ")" { "AND" FilterExpression } { "OR" FilterExpression } ) \| InnerExpression { "AND" FilterExpression } |                      |       |      |      |     |     |
| InnerExpression        | AndCondition { "OR" AndCondition }                                                                                              |                      |       |      |      |     |     |
| AndCondition           | Condition { "AND" Condition }                                                                                                   |                      |       |      |      |     |     |
| Condition              | ( \[ "NOT" \] Condition ) \| Operand                                                                                            |                      |       |      |      |     |     |
| Operand                | BooleanExpr \| ( LHS ( CheckOp                                                                                                  | ( CompareOp RHS) ) ) |       |      |      |     |     |
| BooleanExpr            | Boolean \| BooleanFuncExpr                                                                                                      |                      |       |      |      |     |     |
| LHS                    | ConstFuncExpr \| Boolean                                                                                                        | Field                | Value |      |      |     |     |
| RHS                    | ConstFuncExpr \| Boolean                                                                                                        | Value                | Field |      |      |     |     |
| CompareOp              | "=" \| "=="                                                                                                                     | "<>"                 | "!="  | ">"  | ">=" | "<" | "⇐" |
| CheckOp                | ( "IS" \[ "NOT" \] ( NULL \| MISSING ) )                                                                                        |                      |       |      |      |     |     |
| Field                  | { @"-" } OnePath { "." OnePath } { MathOp MathValue }                                                                           |                      |       |      |      |     |     |
| OnePath                | ( PathFuncExpression \| StringType ){ ArrayIndex }                                                                              |                      |       |      |      |     |     |
| StringType             | @String \| @Ident                                                                                                               | @RawString           | @Char |      |      |     |     |
| ArrayIndex             | "\[" @Int "\]"                                                                                                                  |                      |       |      |      |     |     |
| Value                  | @String                                                                                                                         |                      |       |      |      |     |     |
| ConstFuncExpr          | ConstFuncNoArg \| ConstFuncOneArg                                                                                               | ConstFuncTwoArgs     |       |      |      |     |     |
| ConstFuncNoArg         | ConstFuncNoArgName "(" ")"                                                                                                      |                      |       |      |      |     |     |
| ConstFuncNoArgName     | "PI" \| "E"                                                                                                                     |                      |       |      |      |     |     |
| ConstFuncOneArg        | ConstFuncOneArgName "(" ConstFuncArgument ")"                                                                                   |                      |       |      |      |     |     |
| ConstFuncOneArgName    | "ABS" \| "ACOS"…​                                                                                                               |                      |       |      |      |     |     |
| ConstFuncTwoArgs       | ConstFuncTwoArgsName "(" ConstFuncArgument "," ConstFuncArgument ")"                                                            |                      |       |      |      |     |     |
| ConstFuncTwoArgsName   | "ATAN2" \| "POW"                                                                                                                |                      |       |      |      |     |     |
| ConstFuncArgument      | Field \| Value                                                                                                                  | ConstFuncExpr        |       |      |      |     |     |
| ConstFuncArgumentRHS   | Value                                                                                                                           |                      |       |      |      |     |     |
| PathFuncExpression     | OnePathFuncNoArg                                                                                                                |                      |       |      |      |     |     |
| OnePathFuncNoArg       | OnePathFuncNoArgName "(" ")"                                                                                                    |                      |       |      |      |     |     |
| MathOp                 | @"+" \| @"-"                                                                                                                    | @"\*"                | @"/"  | @"%" |      |     |     |
| MathValue              | @Int \| @Float                                                                                                                  |                      |       |      |      |     |     |
| OnePathFuncNoArgName   | "META"                                                                                                                          |                      |       |      |      |     |     |
| BooleanFuncExpr        | BooleanFuncTwoArgs \| ExistsClause                                                                                              |                      |       |      |      |     |     |
| BooleanFuncTwoArgs     | BooleanFuncTwoArgsName "(" ConstFuncArgument "," ConstFuncArgumentRHS ")"                                                       |                      |       |      |      |     |     |
| BooleanFuncTwoArgsName | "REGEXP\_CONTAINS"                                                                                                              |                      |       |      |      |     |     |
| ExistsClause           | ( "EXISTS" "(" Field ")" )                                                                                                      |                      |       |      |      |     |     |