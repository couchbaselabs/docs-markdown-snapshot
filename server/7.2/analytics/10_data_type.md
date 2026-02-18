---
title: Data Types
description: A description of data types in Couchbase SQL++ for Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/10_data_type.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/analytics/10_data_type.html)

# Data Types

This section describes the data types which Couchbase Analytics can operate on.

An instance of Couchbase Analytics data model can be a **_primitive type_** (`BOOLEAN`, `STRING`, `BIGINT`, or `DOUBLE`), a **_special type_** (`NULL` or `MISSING`), or a **_composite type_** (`OBJECT`, `ARRAY`, or `MULTISET`).

The type names are case-insensitive; for example, both `BIGINT` and `bigint` are acceptable.

## [](#PrimitiveTypes)Primitive Types

### [](#PrimitiveTypesBoolean)Boolean

The `boolean` data type has only two values: `true` and `false`.

Examples:

true
false

> [!NOTE]
> An expression that compares two values, such as `weight > limit`, might return a `boolean` value, or it might return one of the special values `null` or `missing`. For details, see [Comparison Operators](2%5Fexpr.md#Comparison%5Foperators).

### [](#PrimitiveTypesString)String

A `string` represents a sequence of characters. The total length of the sequence can be up to 2,147,483,648.

A literal string can be enclosed in single or double quotes.

Examples:

"This is a string."
'Have you read "War and Peace"?'
"I don't think so."

> [!NOTE]
> For more details on string literals, see [Literals](2%5Fexpr.md#Literals).

### [](#PrimitiveTypesInt)Bigint

A `bigint` is a 64-bit integer. The range of `bigint` is from -9223372036854775808 to 9223372036854775807.

Examples:

45
-27900

> [!NOTE]
> In general, arithmetic operations on two `bigint` values return a `bigint` result. However, two kinds of division operators are provided:
> 
> * `5 / 2` returns `2.5`, a value of type `double`.
> * `5 div 2` returns `2`, a value of type `bigint`, by truncating the result.

### [](#PrimitiveTypesDouble)Double (double precision)

The `double` type represents approximate numeric data values using 8 bytes. The range of a `double` value can be from `(2^(-1022))` to `(2-2^(-52))·2^(1023)` for both positive and negative numbers. Expressions that compute values outside these ranges will return `INF` or `-INF`. The special value `NaN` (not a number) is also supported.

A numeric literal is treated as a `double` if it contains a decimal point or an exponent.

Examples:

45.
-2.79E4
2.79E-4

> [!NOTE]
> All numbers in the incoming JSON which are not integers are parsed as `double` values.

## [](#TemporalData)Temporal Data

Temporal data (dates, times, and timestamps) are important for many applications. Since JSON does not provide data types for temporal data, SQL++ for Analytics uses the `string` and `bigint` types for this purpose. SQL++ for Analytics provides many builtin functions, called temporal functions, that operate on `string` or `bigint` values, interpreting them as dates or times. For a list of these functions, see [Temporal Functions](8%5Fbuiltin.md#TemporalFunctions).

### [](#TemporalDataBigint)Using `bigint` for Temporal Data

Some temporal functions take `bigint` values and interpret them as representing a number of milliseconds since the beginning of the "Unix Epoch" at 00:00:00 UTC on January 1, 1970\. Here are two of these temporal functions and some examples of their use.

* `now_millis( )` returns the current point in time as a `bigint` representing Unix Epoch milliseconds.
* `date_diff_millis(t1, t2, unit)` returns the difference between two points in time (`t1` and `t2`), in terms of the designated units (years, months, weeks, days, hours, seconds, or milliseconds).

Examples:

* `now_millis( )` returns `1655230396621` at the start of an experiment.
* `now_millis( )` returns `1655231924715` at the end of the experiment.
* `date_diff_millis(1655231924715, 1655230396621, "minute")` returns `25`, showing that the experiment lasted for 25 minutes.
* `date_diff_millis(1655231924715, 1655230396621, "second")` returns `1528`, providing a finer measurement: the experiment lasted for 1528 seconds.

### [](#TemporalDataString)Using `string` for Temporal Data

A string in ISO-8601 format can represent a date, time, or timestamp. The ISO format is illustrated by the following example, which represents the 30.55 seconds after 15:10 (3:10pm) on June 14, 2022 in a timezone that (like San Francisco) is eight hours behind Coordinated Universal Time (UTC).

"2022-06-14T15:10:30.55-8:00"

When using a string to represent temporal data, various parts of the ISO format can be omitted. For example:

* `"2022-06-14"` represents the day June 14, 2022.
* `"15:10:30"` represents a time 30 seconds past 15:10 (3:10pm)

In general, two temporal values can be compared only if they have the same components, for example two dates or two times. Violations of this rule usually give `null` results. These rules are illustrated by the following examples, which use the `date_diff_str` function to compare two temporal values and return the difference in a designated unit:

Examples:

* `date_diff_str("2022-06-22", "2022-06-15", "day")` returns `7`.
* `date_diff_str("09:20:00", "08:00:00", "hour")` returns `1`.
* `date_diff_str("09:20:00", "08:00:00", "minute")` returns `80`.
* `date_diff_str("2022-06-22", "10:00:00", "hour")` returns `null`.

For more information about the ISO-8601 format for temporal data, see [Date Formats](../n1ql/n1ql-language-reference/datefun.md#date-formats).

## [](#IncompleteInformationTypes)Incomplete Information Types

### [](#IncompleteInformationTypesNull)Null

`null` is a special value that is often used to represent an unknown value. For example, a user might not be able to know the value of a field and let it be `null`.

* Example:  
{ "field": null };
* The expected result is:  
{ "field": null }

### [](#IncompleteInformationTypesMissing)Missing

`missing` indicates that a name-value pair is missing from an object. If a missing name-value pair is accessed, an empty result value is returned by the query.

As neither the data model nor the system enforces homogeneity for datasets or collections, items in a dataset or collection can be of heterogeneous types and so a field can be present in one object and `missing` in another.

* Example:  
{ "field": missing };
* The expected result is:  
{  }

Since a field with value `missing` means the field is absent, we get an empty object.

> [!NOTE]
> A `missing` value is converted to `null` when converted to JSON in the query results.

## [](#CompositeTypes)Composite Types

### [](#CompositeTypesObject)Object

An `object` (a.k.a., JSON object) contains a set of fields, where each field is described by its name.

Syntactically, object constructors are surrounded by curly braces "{…​}". For example:

{ "name": "Joe Blow", "rank": "Sergeant", "serialno": 1234567 }
{ "rank": "Private", "serialno": 9876543 }
{ "name": "Sally Forth", "rank": "Major", "serialno": 2345678, "gender": "F" }

### [](#CompositeTypesArray)Array

An `array` is a container that holds a fixed number of values. An `array` is an ordered collection of items. Array constructors are denoted by brackets: "\[…​\]".

An example would be:

["alice", 123, "bob", null]

> [!NOTE]
> An `array` can appear in the incoming JSON and can be constructed by the query. Each SELECT statement with an ORDER BY clause returns an `array`.

### [](#CompositeTypesMultiset)Multiset

A `multiset` is an unordered collection of items. A `multiset` allows multiple instances of its elements.

> [!NOTE]
> A `multiset` cannot appear in the incoming JSON. A `multiset` is converted into a JSON array with an undefined order of elements in the query results. The order of the items in the result might change from one query execution to another. Each SELECT statement without an ORDER BY clause returns a `multiset`.